#!/usr/bin/env python3
"""
Biology subtopics — Triple HIGHER (AQA 8461)
COMPLETE — 85 subtopics

Includes all Triple Foundation content PLUS:
  - Higher fields on applicable subtopics
  - 2 new HT-only subtopics:
      infection-response: monoclonal-antibodies
      ecology: environmental-change
"""

BIOLOGY_COLOR = "#6BCB77"

BIOLOGY_SUBTOPICS_ALL = {

"cell-biology": [{'common_mistake': 'Prokaryotic cells have NO nucleus and NO membrane-bound organelles. Students often write '
                    "'bacteria have a nucleus' — they do not. The DNA is a single circular loop loose in the "
                    'cytoplasm. Also: the bacterial cell wall is made of PEPTIDOGLYCAN, not cellulose (cellulose = '
                    'plant cell walls).',
  'equations': ['Magnification (M) = Image size (I) ÷ Actual size (A)'],
  'fifas': [{'label': 'Magnification Calculation',
             'question': 'A bacterium is drawn 30 mm long in a diagram. Its actual length is 0.003 mm. Calculate the '
                         'magnification.',
             'steps': [('F', 'Magnification = Image size ÷ Actual size'),
                       ('I', 'M = 30 ÷ 0.003'),
                       ('F', 'Both values already in mm — no conversion needed'),
                       ('A', 'Magnification = ×10,000')]},
            {'label': 'Finding Actual Size',
             'question': 'A cell is shown at ×500 magnification and measures 10 mm in the image. Calculate the actual '
                         'size in µm.',
             'steps': [('F', 'Actual size = Image size ÷ Magnification'),
                       ('I', 'A = 10 mm ÷ 500 = 0.02 mm'),
                       ('F', 'Convert to µm: 0.02 mm × 1000 = 20 µm'),
                       ('A', 'Actual size = 20 µm')]}],
  'higher': None,
  'id': 'eukaryotes-prokaryotes',
  'key_note': 'Eukaryote = nucleus present. Prokaryote = no nucleus, DNA floats free. Size: bacterium ~1–5 µm; animal '
              'cell ~20 µm; plant cell ~40–80 µm. Units: 1 mm = 1000 µm.',
  'matching': {'instruction': 'Sort each feature — does it belong to eukaryotic cells, prokaryotic cells, or both?',
               'pairs': [('Eukaryote only', 'Has a true membrane-bound nucleus containing DNA'),
                         ('Prokaryote only', 'DNA is a single circular loop floating in cytoplasm'),
                         ('Prokaryote only', 'May have plasmids — small extra circular DNA rings'),
                         ('Eukaryote only', 'Contains mitochondria for aerobic respiration'),
                         ('Both', 'Has a cell membrane and cytoplasm'),
                         ('Both', 'Contains ribosomes for protein synthesis')],
               'title': 'Eukaryote or Prokaryote?'},
  'quiz': [{'opts': [('Eukaryotes have a membrane-bound nucleus; prokaryotes do not', True),
                     ('Prokaryotes are larger and more complex than eukaryotes', False),
                     ('Eukaryotes have no cell membrane', False),
                     ('Prokaryotes have mitochondria but eukaryotes do not', False)],
            'q': 'What is the key structural difference between eukaryotic and prokaryotic cells?',
            'wrong_explanations': {1: 'Prokaryotes are SMALLER and SIMPLER — roughly 10× smaller than a typical animal '
                                      'cell.',
                                   2: 'ALL cells have a cell membrane — it is the universal feature of all living '
                                      'cells.',
                                   3: 'It is the OPPOSITE — eukaryotes have mitochondria. Prokaryotes have NO '
                                      'membrane-bound organelles at all.'}},
           {'opts': [('The animal cell is roughly 10× larger — approximately 20 µm', True),
                     ('They are about the same size', False),
                     ('The bacterium is larger — bacteria are bigger than animal cells', False),
                     ('The animal cell is 1000× larger than the bacterium', False)],
            'q': 'A bacterium is approximately 2 µm in length. How does this compare to a typical animal cell?',
            'wrong_explanations': {1: 'They are definitely not the same size — a bacterium at 2 µm vs an animal cell '
                                      'at ~20 µm is a clear 10× size difference.',
                                   2: 'Bacteria are SMALLER — roughly 10× smaller than animal cells, not larger.',
                                   3: '1000× larger would make the animal cell 2000 µm — about 2 mm! Animal cells are '
                                      'only ~10× larger, not 1000×.'}},
           {'opts': [('Plasmids', True), ('Mitochondria', False), ('A nucleus', False), ('A cell membrane', False)],
            'q': 'Which of the following is found in a bacterial cell but NOT in a typical animal cell?',
            'wrong_explanations': {1: 'Animal cells have mitochondria for aerobic respiration — bacteria do not have '
                                      'mitochondria.',
                                   2: 'Animal cells HAVE a nucleus — bacteria do not. The question asks what bacteria '
                                      "have that animal cells don't.",
                                   3: 'Both animal cells AND bacteria have a cell membrane — it is a universal '
                                      'feature.'}},
           {'opts': [('1,000 µm', True), ('100 µm', False), ('1,000,000 µm', False), ('10 µm', False)],
            'q': '1 mm is equal to how many micrometres (µm)?',
            'wrong_explanations': {1: '100 µm = 0.1 mm. The conversion is 1 mm = 1000 µm.',
                                   2: '1,000,000 µm = 1 metre. The conversion you need is: 1 mm = 1000 µm.',
                                   3: '10 µm = 0.01 mm. Remember: milli means one thousandth, so 1 mm = 1000 µm.'}},
           {'opts': [('A rotating tail-like structure used for movement', True),
                     ('A small ring of extra DNA used for genetic transfer', False),
                     ('A thick outer layer that protects the bacterium', False),
                     ('The region of cytoplasm where the DNA is stored', False)],
            'q': 'What is a flagellum in a bacterial cell?',
            'wrong_explanations': {1: 'A small ring of extra DNA = a PLASMID, not a flagellum.',
                                   2: 'A thick outer protective layer = the CAPSULE (or cell wall). The flagellum is '
                                      'the structure for movement.',
                                   3: 'The region where DNA sits loosely in the cytoplasm is called the nucleoid '
                                      'region — the flagellum is an external motor structure.'}}],
  'rp': None,
  'spec': '4.1.1.1',
  'summary': 'Compare the key features of eukaryotic and prokaryotic cells, including scale and size.',
  'theory': [{'content': 'Every living organism on Earth is made of one of two fundamentally different types of cell: '
                         'eukaryotic or prokaryotic.\n'
                         'The single most important difference between them is whether the cell has a TRUE NUCLEUS — a '
                         'membrane-bound compartment containing the DNA.\n'
                         'Eukaryotic cells HAVE a nucleus. Prokaryotic cells DO NOT.\n'
                         'This distinction is so fundamental that it defines two of the largest groupings of life on '
                         'Earth.',
              'heading': 'The Two Fundamental Types of Cell'},
             {'content': 'Eukaryotic cells are larger, more complex cells that have:\n'
                         '• A true nucleus — DNA enclosed in a nuclear membrane.\n'
                         '• Membrane-bound organelles — mitochondria, endoplasmic reticulum, Golgi apparatus etc.\n'
                         '• A cytoskeleton — internal protein framework.\n'
                         'All animals, plants, fungi and protists are made of eukaryotic cells.\n'
                         'Typical size: 10–100 micrometres (µm).\n'
                         'The nucleus protects DNA and allows its activity to be carefully regulated.',
              'heading': 'Eukaryotic Cells'},
             {'content': 'Prokaryotic cells are smaller and simpler. All bacteria are prokaryotes.\n'
                         'Key features:\n'
                         '• NO nucleus — DNA is a SINGLE CIRCULAR LOOP floating free in the cytoplasm.\n'
                         '• NO membrane-bound organelles — no mitochondria, no chloroplasts.\n'
                         '• DO have: cytoplasm, a cell membrane, a cell wall (made of peptidoglycan — not cellulose), '
                         'and ribosomes (smaller than eukaryotic ribosomes).\n'
                         '• May also have: PLASMIDS (small extra circular loops of DNA, not essential for survival), a '
                         'FLAGELLUM (rotating tail for movement), and a CAPSULE (slimy outer layer for protection and '
                         'attachment).\n'
                         'Typical size: 1–10 µm — roughly 10× smaller than a typical animal cell.',
              'heading': 'Prokaryotic Cells — Bacteria'},
             {'content': 'The small size of prokaryotic cells gives them a very HIGH surface area to volume ratio '
                         '(SA:V).\n'
                         'This means that relative to their volume, bacteria have a lot of membrane surface available '
                         'for absorbing nutrients and removing waste.\n'
                         'This is one reason bacteria can grow and reproduce extremely fast — every 20 minutes under '
                         'ideal conditions.\n'
                         'Larger eukaryotic cells have a lower SA:V ratio — they need specialised exchange surfaces '
                         'and transport systems (e.g. lungs, circulatory system) to move substances efficiently.',
              'heading': 'Why Size Matters — Surface Area to Volume Ratio'},
             {'content': 'Working with cells requires understanding very small units:\n'
                         '• 1 metre (m) = 1,000 millimetres (mm)\n'
                         '• 1 mm = 1,000 micrometres (µm)\n'
                         '• 1 µm = 1,000 nanometres (nm)\n'
                         'So: 1 m = 1,000,000 µm = 1,000,000,000 nm\n'
                         'Typical sizes to remember:\n'
                         '• Animal cell: ~20 µm\n'
                         '• Plant cell: ~40–80 µm\n'
                         '• Bacterium: ~1–5 µm\n'
                         '• Virus: ~0.1 µm (100 nm)\n'
                         '• Ribosome: ~20 nm\n'
                         'You need to be able to convert between these units and use them in magnification '
                         'calculations.',
              'heading': 'Units and Scale'}],
  'title': 'Eukaryotes and Prokaryotes',
  'triple_only': None,
  'variables': [('M', 'Magnification', 'no unit', '×'),
                ('I', 'Image size', 'mm or µm', 'mm / µm'),
                ('A', 'Actual size', 'mm or µm', 'mm / µm')]},
 {'common_mistake': 'NOT all plant cells have chloroplasts — ONLY cells exposed to light. Root cells are underground '
                    'so never receive light and have NO chloroplasts. Students also often forget that plant cells have '
                    'a cell wall AND a cell membrane — both are present. The cell wall is outside, the cell membrane '
                    'is inside it.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'animal-plant-cells',
  'key_note': 'Animal cells: nucleus, cell membrane, cytoplasm, mitochondria, ribosomes. Plant cells: all of the above '
              'PLUS cell wall (cellulose), chloroplasts (light-exposed cells only), permanent vacuole.',
  'matching': {'instruction': 'Drag each function to match the correct organelle.',
               'pairs': [('Nucleus', 'Contains DNA in chromosomes — controls all cell activity'),
                         ('Cell membrane', 'Selectively permeable barrier — controls what enters and leaves'),
                         ('Mitochondria', 'Site of aerobic respiration — releases energy as ATP'),
                         ('Ribosomes', 'Site of protein synthesis — builds proteins from amino acids'),
                         ('Cell wall', 'Made of cellulose — rigid support, prevents cell bursting'),
                         ('Chloroplasts', 'Contain chlorophyll — absorb light energy for photosynthesis'),
                         ('Permanent vacuole', 'Filled with cell sap — contributes to turgor pressure')],
               'title': 'Match the Organelle to its Function'},
  'quiz': [{'opts': [('Ribosomes', True), ('Mitochondria', False), ('Nucleus', False), ('Chloroplasts', False)],
            'q': 'Which organelle is responsible for protein synthesis?',
            'wrong_explanations': {1: 'Mitochondria are the site of aerobic RESPIRATION — they release energy from '
                                      "glucose, they don't make proteins.",
                                   2: 'The nucleus contains the DNA instructions for making proteins, but the actual '
                                      'assembly of amino acids into proteins happens at RIBOSOMES.',
                                   3: 'Chloroplasts carry out PHOTOSYNTHESIS — capturing light energy to make glucose. '
                                      'Not involved in protein synthesis.'}},
           {'opts': [('Root cells are underground — no light reaches them, so chloroplasts are not present', True),
                     ('Root cells are too small to contain chloroplasts', False),
                     ('Root cells are prokaryotic and cannot have chloroplasts', False),
                     ('Chloroplasts are only present in animal cells', False)],
            'q': 'A student looks at a plant cell from a root. They expect to see chloroplasts but find none. Why?',
            'wrong_explanations': {1: 'Root cells are eukaryotic plant cells — size is not the reason. Palisade cells '
                                      'are similar in size and have many chloroplasts.',
                                   2: 'ALL plant cells are eukaryotic. Root cells are plant cells — they are '
                                      'eukaryotic. Only bacteria (and other prokaryotes) lack membrane-bound '
                                      'organelles.',
                                   3: 'Chloroplasts are found in PLANT cells — not animal cells. Animal cells never '
                                      'have chloroplasts.'}},
           {'opts': [('Filled with cell sap — contributes to turgor pressure, keeping the cell firm', True),
                     ('Stores chlorophyll for photosynthesis', False),
                     ('Acts as the site of aerobic respiration', False),
                     ('Controls what enters and leaves the cell', False)],
            'q': 'What is the function of the permanent vacuole in a plant cell?',
            'wrong_explanations': {1: 'Chlorophyll is stored in CHLOROPLASTS — not the vacuole. The vacuole contains '
                                      'cell sap (sugars and salts).',
                                   2: 'Aerobic respiration occurs in MITOCHONDRIA. The vacuole is a storage '
                                      'compartment.',
                                   3: 'Controlling what enters and leaves = the CELL MEMBRANE. The vacuole is a '
                                      'storage structure filled with cell sap.'}},
           {'opts': [('Mitochondria', True),
                     ('Cell wall', False),
                     ('Chloroplasts', False),
                     ('Permanent vacuole', False)],
            'q': 'Which of the following is present in both animal and plant cells?',
            'wrong_explanations': {1: 'Cell walls are only found in plant cells (and bacteria, fungi) — NOT in animal '
                                      'cells.',
                                   2: 'Chloroplasts are found only in plant cells that are exposed to light. Animal '
                                      'cells never have chloroplasts.',
                                   3: 'The permanent vacuole is a plant cell feature — animal cells do not have a '
                                      'large permanent vacuole (though they may have small temporary vacuoles).'}},
           {'opts': [('Muscle cells need much more ATP energy for contraction — more mitochondria produce more ATP',
                      True),
                     ('Muscle cells are larger, so they need more organelles to fill the space', False),
                     ('Mitochondria help muscle cells to absorb oxygen from the blood', False),
                     ("Skin cells don't respire — they don't need mitochondria at all", False)],
            'q': 'Why do very active muscle cells contain many more mitochondria than skin cells?',
            'wrong_explanations': {1: "Cell size doesn't directly dictate organelle number — it is energy demand that "
                                      'determines mitochondria count.',
                                   2: 'Oxygen is absorbed by diffusion through the cell membrane — mitochondria USE '
                                      "oxygen in respiration, they don't absorb it.",
                                   3: 'All living cells respire all the time — skin cells do have mitochondria. Active '
                                      'cells simply have FAR MORE.'}}],
  'rp': 'RP1 — Use a light microscope to observe, draw and label plant and animal cells. Include a scale bar and '
        'calculate magnification.',
  'spec': '4.1.1.2',
  'summary': 'Describe the sub-cellular structures of animal and plant cells and relate structure to function.',
  'theory': [{'content': 'All animal cells contain these five essential structures:\n'
                         '\n'
                         "NUCLEUS: contains the cell's DNA, organised into chromosomes. The nucleus controls all cell "
                         'activity by determining which proteins are made. It has a double membrane called the nuclear '
                         'envelope with pores that allow molecules to pass in and out.\n'
                         '\n'
                         'CELL MEMBRANE: a thin, flexible layer made of phospholipids and proteins. It controls what '
                         'enters and leaves the cell — it is selectively permeable. It also plays a role in '
                         'communication between cells.\n'
                         '\n'
                         'CYTOPLASM: a watery, gel-like substance that fills the cell. Most chemical reactions happen '
                         'here. It contains dissolved enzymes, salts, sugars and other molecules, as well as all the '
                         'organelles.\n'
                         '\n'
                         'MITOCHONDRIA: oval-shaped organelles with a folded inner membrane (cristae). This is where '
                         'aerobic respiration occurs — glucose is broken down using oxygen to release energy as ATP. '
                         'Cells that are very active (muscle cells, sperm cells, liver cells) have many more '
                         'mitochondria than less active cells.\n'
                         '\n'
                         'RIBOSOMES: tiny structures found either floating in the cytoplasm or attached to the '
                         'endoplasmic reticulum. This is where PROTEIN SYNTHESIS takes place — amino acids are joined '
                         'in a specific sequence to build proteins. Every cell needs proteins, so all cells have '
                         'ribosomes.',
              'heading': 'Animal Cell Structures and Functions'},
             {'content': 'Plant cells have all five animal cell structures PLUS up to three additional ones:\n'
                         '\n'
                         'CELL WALL: a rigid outer layer made of cellulose fibres. It surrounds the cell membrane and '
                         'gives the cell a fixed shape. It prevents the cell from bursting when it absorbs water by '
                         'osmosis — the wall resists the pressure. This is what makes plants structurally rigid (along '
                         'with turgor pressure).\n'
                         '\n'
                         'CHLOROPLASTS: oval-shaped organelles containing the green pigment chlorophyll. Chlorophyll '
                         'absorbs light energy, which is used to drive photosynthesis — converting CO₂ and water into '
                         'glucose. IMPORTANT: only cells that are exposed to light have chloroplasts. Root cells, '
                         'storage cells (e.g. in potato tubers) and cells deep inside stems do NOT have chloroplasts.\n'
                         '\n'
                         'PERMANENT VACUOLE: a large central compartment in mature plant cells, filled with cell sap '
                         '(a solution of sugars, salts and pigments). The vacuole pushes against the cell wall and '
                         'contributes to TURGOR PRESSURE — the pressure that keeps plant cells firm and gives the '
                         'plant structural support. Without water in the vacuole, the plant wilts.',
              'heading': "Plant Cells — What's Extra"},
             {'content': 'The key principle to understand is that every structural feature exists because it serves a '
                         'specific function.\n'
                         '\n'
                         'More mitochondria = more aerobic respiration = more ATP energy. Cells with high energy '
                         'demands (muscle, sperm, liver) have the most mitochondria.\n'
                         '\n'
                         'More chloroplasts = more photosynthesis. Palisade mesophyll cells in leaves have up to 70 '
                         'chloroplasts — they are the main photosynthetic cells of the plant.\n'
                         '\n'
                         'Large vacuole = more turgor pressure = firmer cell. This is why plants wilt when they lose '
                         'water — the vacuoles deflate and cells lose their rigidity.\n'
                         '\n'
                         'Cell wall + vacuole together = turgid plant cell that holds its shape and provides '
                         'structural support to the whole plant.',
              'heading': 'Why Structure Matches Function'},
             {'content': 'To observe cells under a light microscope:\n'
                         '1. Prepare a thin section of tissue (e.g. onion epidermis, cheek cells).\n'
                         '2. Place on a glass slide with a drop of water or mounting fluid.\n'
                         '3. Add a coverslip carefully to avoid air bubbles.\n'
                         '4. Apply a stain if needed — iodine solution stains starch and nuclei blue/purple; methylene '
                         'blue stains nuclei of animal cells.\n'
                         '5. Focus using the coarse adjustment knob first, then the fine adjustment.\n'
                         'You can observe with a light microscope: nucleus, cytoplasm, cell wall, vacuole, '
                         'chloroplasts.\n'
                         'You CANNOT see clearly: individual ribosomes (too small), cell membrane detail, internal '
                         'mitochondria structure.',
              'heading': 'Using a Light Microscope to Observe Cells'}],
  'title': 'Animal and Plant Cells',
  'triple_only': None,
  'variables': []},
 {'common_mistake': "Students often say 'root hair cells absorb water by active transport' — this is WRONG. Water "
                    'enters by OSMOSIS (passive). Mineral IONS are absorbed by active transport. These are two '
                    "different processes happening in the same cell. Don't mix them up.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'cell-specialisation',
  'key_note': 'Differentiation = cells becoming specialised by switching genes on/off. Animals: mostly at embryo '
              'stage. Plants: meristems continue throughout life. Every adaptation has a specific reason — always link '
              'structure to function.',
  'matching': {'instruction': 'Match each cell type to the adaptation that makes it suited to its function.',
               'pairs': [('Sperm cell', 'Flagellum and many mitochondria — to swim to the egg'),
                         ('Red blood cell', 'Biconcave disc, no nucleus — maximises haemoglobin space'),
                         ('Neurone', 'Long axon with myelin sheath — fast impulse transmission'),
                         ('Root hair cell', 'Long projection, no chloroplasts — absorbs water and minerals from soil'),
                         ('Xylem', 'Hollow, dead, lignified walls — forms a tube for water transport'),
                         ('Palisade cell', 'Packed with chloroplasts near leaf surface — photosynthesis')],
               'title': 'Match the Specialised Cell to its Key Adaptation'},
  'quiz': [{'opts': [('It needs large amounts of ATP energy to power its flagellum and swim to the egg', True),
                     ('Mitochondria help the sperm digest through the egg membrane', False),
                     ('More mitochondria make the sperm cell larger and more visible', False),
                     ("Mitochondria store the sperm's genetic material", False)],
            'q': 'Why does a sperm cell contain many mitochondria?',
            'wrong_explanations': {1: 'Digesting the egg membrane is the function of the ACROSOME — an enzyme-filled '
                                      'cap at the tip of the sperm head. Mitochondria provide energy.',
                                   2: 'Sperm cells are actually very small and streamlined to reduce drag — larger '
                                      'would mean slower swimming. Mitochondria provide energy, not bulk.',
                                   3: 'Genetic material (DNA) is stored in the NUCLEUS, not in mitochondria. '
                                      'Mitochondria have their own small amount of DNA but this is not what carries '
                                      'genetic information to the egg.'}},
           {'opts': [('More internal space for haemoglobin, allowing the cell to carry more oxygen', True),
                     ('Without a nucleus it cannot be destroyed by white blood cells', False),
                     ('It can reproduce more quickly without a nucleus getting in the way', False),
                     ("The absence of a nucleus reduces the cell's oxygen needs", False)],
            'q': 'A red blood cell has no nucleus. How does this benefit its function?',
            'wrong_explanations': {1: 'White blood cells do patrol for pathogens, but red blood cell lifespan (~120 '
                                      'days) is determined by membrane wear — not by whether they have a nucleus.',
                                   2: 'Cells without a nucleus CANNOT reproduce — red blood cells are made in bone '
                                      'marrow and released as mature, non-dividing cells.',
                                   3: "Cells don't 'need' oxygen for the nucleus — they need it for respiration in "
                                      'mitochondria. Red blood cells actually have very few mitochondria and mainly '
                                      'use anaerobic respiration.'}},
           {'opts': [('Root hair cells are underground — there is no light available for photosynthesis', True),
                     ('Root hair cells are too small to fit chloroplasts inside', False),
                     ('Chloroplasts would prevent water absorption from the soil', False),
                     ('Root hair cells are a type of prokaryotic cell and cannot have organelles', False)],
            'q': 'Why does a root hair cell have no chloroplasts?',
            'wrong_explanations': {1: 'Root hair cells are of similar size to leaf cells — size is not the limiting '
                                      'factor. The absence of light is the reason.',
                                   2: "Chloroplasts don't block water entry — they are simply absent because they "
                                      'would serve no purpose underground where there is no light.',
                                   3: 'All plant cells are EUKARYOTIC. Root hair cells are eukaryotic plant cells — '
                                      'they could have organelles, but chloroplasts specifically are not present due '
                                      'to the lack of light.'}},
           {'opts': [('They are dead and hollow — no cell contents blocking the continuous water column', True),
                     ('They contain many chloroplasts to produce energy for pumping water upwards', False),
                     ('They have a large vacuole to store water temporarily', False),
                     ('They have very thin walls to allow water to pass through easily', False)],
            'q': 'What structural feature of xylem cells makes them well-suited for water transport?',
            'wrong_explanations': {1: 'Chloroplasts would only be present if the xylem cell was exposed to light — and '
                                      'the purpose of xylem is water transport, not photosynthesis. The hollow dead '
                                      'cells are the key feature.',
                                   2: "Xylem cells don't store water — they are a continuous flow pipe. Vacuoles are a "
                                      'feature of living plant cells for support.',
                                   3: 'Xylem walls are actually THICK and reinforced with lignin — this gives them '
                                      'strength to withstand the tension created as water is pulled upwards, '
                                      'preventing the xylem from collapsing.'}}],
  'rp': None,
  'spec': '4.1.1.3',
  'summary': 'Explain how and why cells become specialised, with examples from animals and plants.',
  'theory': [{'content': 'All multicellular organisms begin life as a single fertilised egg cell (zygote). This one '
                         'cell divides repeatedly by mitosis to produce all the billions of cells in the organism.\n'
                         'As cells divide, they become progressively more specialised — this process is called '
                         'DIFFERENTIATION.\n'
                         'Differentiation means a cell switches on certain genes and switches off others, causing it '
                         'to develop a specific structure suited to a specific function.\n'
                         'The result: specialised cells that are experts at one job, making the whole organism far '
                         'more efficient.\n'
                         'In ANIMALS: most differentiation occurs early during embryonic development. Once '
                         'differentiated, most animal cells lose the ability to become a different type — they are '
                         'committed.\n'
                         "In PLANTS: differentiation can continue throughout the plant's life. Meristem cells (at root "
                         'and shoot tips) remain undifferentiated and can keep producing new specialised cells.',
              'heading': 'What is Cell Differentiation?'},
             {'content': 'SPERM CELL — function: swim to and fertilise an egg.\n'
                         'Adaptations:\n'
                         '• Streamlined head — reduces drag when swimming.\n'
                         '• Flagellum (tail) — rotates to propel the sperm through fluid.\n'
                         '• Many mitochondria in the midpiece — aerobic respiration provides ATP energy for swimming.\n'
                         "• Acrosome (cap on the head) — contains enzymes that digest through the egg's outer "
                         'membrane.\n'
                         '• Haploid nucleus — contains only 23 chromosomes (half the normal number) so that after '
                         'fertilisation the normal 46 is restored.\n'
                         '\n'
                         'RED BLOOD CELL (erythrocyte) — function: carry oxygen from lungs to tissues.\n'
                         'Adaptations:\n'
                         '• Biconcave disc shape — large surface area for oxygen absorption; thin centre = short '
                         'diffusion distance for O₂.\n'
                         '• No nucleus — creates more space for HAEMOGLOBIN, the oxygen-carrying protein.\n'
                         '• Flexible — can squeeze through narrow capillaries without tearing.\n'
                         '• Packed with haemoglobin — each cell contains ~270 million haemoglobin molecules.\n'
                         '\n'
                         'NEURONE (nerve cell) — function: transmit electrical impulses rapidly over long distances.\n'
                         'Adaptations:\n'
                         '• Very long axon — can be over a metre long (e.g. sciatic nerve), allowing signals to travel '
                         'from brain to toe without interruption.\n'
                         '• Myelin sheath — fatty insulating layer that speeds up impulse conduction (signals jump '
                         'between gaps called nodes of Ranvier).\n'
                         '• Dendrites — short branching fibres that receive signals from other neurones.\n'
                         '• Synaptic terminals — the axon ends in bulb-like structures that release neurotransmitters '
                         'to communicate with the next cell.\n'
                         '\n'
                         'MUSCLE CELL — function: contract to produce movement.\n'
                         'Adaptations:\n'
                         '• Contains contractile proteins (actin and myosin) that slide past each other to shorten the '
                         'cell.\n'
                         '• Many mitochondria — large energy demand for constant contraction.\n'
                         '• Can store glycogen as an energy reserve.',
              'heading': 'Specialised Animal Cells'},
             {'content': 'ROOT HAIR CELL — function: absorb water and mineral ions from soil.\n'
                         'Adaptations:\n'
                         '• Long, thin hair-like projection extending from the cell — massively increases the surface '
                         'area in contact with soil water.\n'
                         '• No chloroplasts — underground, no light available for photosynthesis.\n'
                         '• Thin cell wall — short diffusion distance for water and minerals.\n'
                         '• Large permanent vacuole — maintains a low water potential inside the cell to draw water in '
                         'by osmosis.\n'
                         '\n'
                         'XYLEM CELL — function: transport water and dissolved minerals from roots up to leaves.\n'
                         'Adaptations:\n'
                         '• Dead cells — no cytoplasm or nucleus (no living contents obstructing flow).\n'
                         '• Hollow lumen — forms a continuous open tube for water to flow through.\n'
                         '• Walls thickened with LIGNIN — a hard, waterproof substance that prevents collapse under '
                         'pressure and makes xylem very strong.\n'
                         '• No end walls — cells are stacked end-to-end to form an uninterrupted column.\n'
                         '\n'
                         'PHLOEM CELL — function: transport dissolved sugars (sucrose) from leaves to the rest of the '
                         'plant.\n'
                         'Adaptations:\n'
                         '• Living cells with little cytoplasm.\n'
                         '• Sieve plates — porous plates at the end walls that allow sugar solution to flow between '
                         'cells.\n'
                         '• Companion cells alongside each sieve tube cell — provide energy (ATP) for active loading '
                         'of sugars.\n'
                         '\n'
                         'PALISADE MESOPHYLL CELL — function: photosynthesis.\n'
                         'Adaptations:\n'
                         '• Packed with many chloroplasts.\n'
                         '• Found at the top of the leaf — closest to sunlight.\n'
                         '• Tall, column shape — allows maximum chloroplasts to be stacked near the leaf surface.',
              'heading': 'Specialised Plant Cells'}],
  'title': 'Cell Specialisation and Differentiation',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Units must be the same before calculating. If image size is in mm and actual size is in µm, you '
                    'MUST convert first or your answer will be wrong by a factor of 1000. Always write out the units '
                    "in your working — this forces you to spot when they don't match.",
  'equations': ['M = I ÷ A', 'A = I ÷ M', 'I = A × M'],
  'fifas': [{'label': 'Example 1 — Find magnification',
             'question': 'A cell appears 54 mm wide in a diagram. Its actual width is 0.018 mm. Calculate the '
                         'magnification.',
             'steps': [('F', 'M = Image size ÷ Actual size'),
                       ('I', 'M = 54 ÷ 0.018'),
                       ('F', 'Both values are in mm — no unit conversion needed'),
                       ('A', 'M = ×3000')]},
            {'label': 'Example 2 — Find actual size',
             'question': 'A mitochondrion appears 12 mm long in an electron micrograph at ×80,000 magnification. '
                         'Calculate its actual length in µm.',
             'steps': [('F', 'Actual size = Image size ÷ Magnification'),
                       ('I', 'A = 12 mm ÷ 80,000 = 0.00015 mm'),
                       ('F', 'Convert mm to µm: 0.00015 × 1000 = 0.15 µm'),
                       ('A', 'Actual length = 0.15 µm')]},
            {'label': 'Example 3 — Find image size',
             'question': 'A bacterium has an actual diameter of 2 µm. It is drawn at ×2000 magnification. How large '
                         'should the drawing be in mm?',
             'steps': [('F', 'Image size = Actual size × Magnification'),
                       ('I', 'I = 2 µm × 2000 = 4000 µm'),
                       ('F', 'Convert µm to mm: 4000 ÷ 1000 = 4 mm'),
                       ('A', 'Drawing should be 4 mm wide')]}],
  'higher': 'Electron microscopes have much greater magnification and resolution than light microscopes — they can '
            'reveal sub-cellular structures invisible to light microscopes. Resolution is the ability to distinguish '
            'two points; light microscopes are limited by the wavelength of light (~200 nm). Scanning electron '
            'microscopes (SEM) show surface detail; transmission electron microscopes (TEM) show internal structure. '
            'Use the magnification formula: magnification = image size ÷ actual size. Convert between mm, μm and nm '
            'when calculating.',
  'id': 'microscopy',
  'key_note': 'Light microscope: max ×2000, resolution 200 nm, can view living cells. Electron microscope: max '
              '×2,000,000, resolution 0.1 nm, specimens must be dead. Resolution = sharpness. Magnification = size '
              'increase.',
  'matching': {'instruction': 'Sort each statement to the correct type of microscope.',
               'pairs': [('Electron microscope',
                          'Resolution of 0.1 nm — can distinguish structures 2000× finer than a light microscope'),
                         ('Light microscope', 'Can be used to view living cells without any special preparation'),
                         ('Electron microscope',
                          'First revealed the detailed internal structure of mitochondria and ribosomes'),
                         ('Light microscope', 'Maximum magnification of approximately ×2,000'),
                         ('Electron microscope', 'Specimens must be dead — the beam operates in a vacuum'),
                         ('Both', 'Used to calculate magnification using M = I ÷ A')],
               'title': 'Light Microscope or Electron Microscope?'},
  'quiz': [{'opts': [('Approximately ×2,000', True),
                     ('Approximately ×2,000,000', False),
                     ('Approximately ×200', False),
                     ('Approximately ×20,000', False)],
            'q': 'What is the maximum magnification of a light microscope?',
            'wrong_explanations': {1: '×2,000,000 is the maximum for an ELECTRON microscope — far more powerful than a '
                                      'light microscope.',
                                   2: '×200 is a common low-power objective on a school microscope — but the total '
                                      'maximum for light microscopes is around ×2,000.',
                                   3: "×20,000 doesn't correspond to either type — light microscopes reach ~×2,000 and "
                                      'electron microscopes ~×2,000,000.'}},
           {'opts': [('×5,000', True), ('×500', False), ('×50,000', False), ('×4,500', False)],
            'q': 'An image is 45 mm wide. The actual size is 0.009 mm. What is the magnification?',
            'wrong_explanations': {1: 'Check: 45 ÷ 0.09 = 500, but actual size is 0.009 (not 0.09). 45 ÷ 0.009 = 5000.',
                                   2: '45 ÷ 0.009 = 5000 not 50,000. Check you moved the decimal correctly.',
                                   3: '45 minus 0.009 is not how you calculate magnification! Use M = I ÷ A = 45 ÷ '
                                      '0.009 = 5000.'}},
           {'opts': [('Ribosomes (~20 nm) are far below the resolution limit of light microscopes (~200 nm)', True),
                     ('Ribosomes are only visible in living cells and electron microscopes can see living cells', True),
                     ('Ribosomes are colourless and no stain existed until recently', False),
                     ('Ribosomes only appear in plant cells which were studied less', False)],
            'q': 'Why were ribosomes not discovered until electron microscopes became available?',
            'wrong_explanations': {1: 'Electron microscopes cannot view LIVING specimens — they require dead specimens '
                                      'in a vacuum. The key advantage is RESOLUTION, not viewing live cells.',
                                   2: 'Staining could make ribosomes coloured — but even stained, they are too small '
                                      'to be resolved by a light microscope.',
                                   3: 'Ribosomes are found in ALL cells — animal, plant and bacterial. They were not '
                                      'limited to plant cells.'}},
           {'opts': [('Magnification = how much bigger the image appears; resolution = how clearly fine detail can be '
                      'distinguished',
                      True),
                     ('They are the same thing — both refer to how large the image looks', False),
                     ('Magnification refers to electron microscopes only; resolution applies to light microscopes',
                      False),
                     ('Resolution is measured in × and magnification is measured in nm', False)],
            'q': 'What is the difference between magnification and resolution?',
            'wrong_explanations': {1: 'They are NOT the same. You can have a highly magnified but blurry image — that '
                                      'is high magnification but low resolution.',
                                   2: 'Both types of microscope have both magnification and resolution — the terms '
                                      'apply to all microscopes.',
                                   3: 'Magnification has no unit (×) — it is a ratio. Resolution is measured in nm '
                                      '(nanometres). You have these exactly the wrong way around.'}},
           {'opts': [('20,000 µm', True), ('0.125 µm', False), ('450 µm', False), ('2,000 µm', False)],
            'q': 'A cell has an actual diameter of 50 µm. At ×400 magnification, how large will the image appear in '
                 'µm?',
            'wrong_explanations': {1: 'You divided instead of multiplying. Image = Actual × Magnification = 50 × 400 = '
                                      '20,000 µm.',
                                   2: 'You added the magnification to the actual size. Image = Actual × Magnification '
                                      '= 50 × 400 = 20,000 µm.',
                                   3: 'You used the wrong magnification value. Image = 50 × 400 = 20,000 µm — not 2000 '
                                      'µm.'}}],
  'rp': 'RP1 — Use a light microscope to observe, draw and label plant and animal cells. Include a scale bar. '
        'Calculate the magnification of your drawing.',
  'spec': '4.1.1.5',
  'summary': 'Compare light and electron microscopes, and carry out magnification calculations.',
  'theory': [{'content': 'Light microscopes use VISIBLE LIGHT focused by glass lenses to produce a magnified image of '
                         'a specimen.\n'
                         'Key facts:\n'
                         '• Maximum magnification: approximately ×2,000\n'
                         '• Maximum resolution: approximately 200 nm — cannot distinguish two points closer than this\n'
                         '• Can view living specimens — no special preparation needed\n'
                         '• Relatively cheap — used in schools and hospitals worldwide\n'
                         '• Images are in colour (natural or stained)\n'
                         'What you CAN see: cells, nucleus, cell wall, vacuole, chloroplasts, large organelles at high '
                         'magnification\n'
                         'What you CANNOT see clearly: ribosomes (~20 nm), internal membrane detail, individual '
                         'proteins\n'
                         'STAINING: many specimens are colourless, so dyes are used:\n'
                         '• Iodine solution: stains starch blue/black; stains nuclei light brown\n'
                         '• Methylene blue: stains cell nuclei dark blue — great for animal cells\n'
                         '• Toluidine blue: stains plant cell walls\n'
                         'Staining kills cells — so stained specimens cannot be living.',
              'heading': 'Light Microscopes'},
             {'content': 'Electron microscopes use a BEAM OF ELECTRONS instead of light.\n'
                         'Because electrons have a much shorter wavelength than visible light, they can produce far '
                         'more detailed images.\n'
                         'Key facts:\n'
                         '• Maximum magnification: approximately ×2,000,000\n'
                         '• Maximum resolution: approximately 0.1 nm — 2000× better than light microscopes\n'
                         '• Specimens must be dead — the electron beam operates in a vacuum (no air, so no living '
                         'cells)\n'
                         '• Very expensive — found in universities and research centres\n'
                         '• Images are black and white (false colour can be added digitally afterwards)\n'
                         'Two main types:\n'
                         '• Transmission electron microscope (TEM): beam passes THROUGH a very thin slice of specimen '
                         '— shows internal detail of organelles\n'
                         '• Scanning electron microscope (SEM): beam scans the SURFACE of a specimen — produces a '
                         '3D-looking image of the external structure\n'
                         'Electron microscopes revealed: the detailed internal structure of mitochondria, ribosomes, '
                         'the nuclear envelope, endoplasmic reticulum and many more previously unknown structures — '
                         'transforming our understanding of cell biology.',
              'heading': 'Electron Microscopes'},
             {'content': 'These two terms are often confused:\n'
                         'MAGNIFICATION: how many times bigger the image is compared to the actual object. A ×1000 '
                         'magnification makes things appear 1000× bigger.\n'
                         'RESOLUTION: the ability to see fine detail — how clearly two close-together points can be '
                         'distinguished as SEPARATE objects rather than blurring into one.\n'
                         'You can have high magnification but low resolution — like zooming in on a pixelated photo. '
                         'The image is big but blurry.\n'
                         'Electron microscopes gave scientists BOTH very high magnification AND very high resolution — '
                         'this is what made them revolutionary.\n'
                         'Analogy: imagine trying to read a book from across a room. You could use a magnifying glass '
                         '(high magnification) but if the lens is poor quality, the words are still blurry (low '
                         'resolution). A high-quality telescope gives you both magnification and resolution.',
              'heading': 'Resolution vs Magnification'},
             {'content': 'The formula: Magnification = Image size ÷ Actual size\n'
                         'Rearranged:\n'
                         '• Actual size = Image size ÷ Magnification\n'
                         '• Image size = Actual size × Magnification\n'
                         'CRUCIAL RULE: both measurements must be in the SAME UNITS before you calculate.\n'
                         'If image size is in mm and actual size is in µm → convert before calculating.\n'
                         'Unit conversions:\n'
                         '• mm to µm: multiply by 1000 (1 mm = 1000 µm)\n'
                         '• µm to mm: divide by 1000\n'
                         'Tip: use the formula triangle — write M at the top, I bottom-left, A bottom-right. Cover the '
                         'one you want to find.',
              'heading': 'The Magnification Formula'}],
  'title': 'Microscopy',
  'triple_only': None,
  'variables': [('M', 'Magnification', 'no unit', '×'),
                ('I', 'Image size', 'mm or µm', 'mm / µm'),
                ('A', 'Actual size', 'mm or µm', 'mm / µm')]},
 {'common_mistake': 'Mitosis produces TWO daughter cells that are genetically IDENTICAL to each other and to the '
                    'parent — same number of chromosomes (46 in humans). Do NOT confuse with meiosis (not required at '
                    'Foundation but you will hear the word). Meiosis produces FOUR cells each with HALF the '
                    'chromosomes — used only for making gametes. Mitosis = for the BODY. Meiosis = for GAMETES.',
  'equations': [],
  'fifas': [],
  'higher': 'The cell cycle has three stages: (1) growth/interphase — cell grows, DNA replicates, organelles increase; '
            '(2) mitosis — chromosomes line up and are pulled to opposite ends of the cell; (3) cytokinesis — '
            'cytoplasm divides to form two identical daughter cells. Cancer results from uncontrolled cell division '
            'caused by mutations in genes controlling the cell cycle. Mitosis produces two genetically identical '
            'diploid daughter cells.',
  'id': 'chromosomes-mitosis',
  'key_note': 'Mitosis: growth, repair, replacement. Two identical daughter cells. 46 → 46. DNA replicates BEFORE '
              'division. Cancer = uncontrolled mitosis caused by mutation in regulatory genes.',
  'matching': {'instruction': 'Match each description to the correct phase of the cell cycle.',
               'pairs': [('Interphase — growth (G1)', 'Cell grows in size and produces more organelles and proteins'),
                         ('Interphase — DNA replication (S phase)',
                          'Every chromosome is copied — cell now has double the DNA'),
                         ('Mitosis',
                          'Duplicated chromosomes separate to opposite ends of the cell — two new nuclei form'),
                         ('Cytokinesis', 'Cytoplasm divides — two genetically identical daughter cells produced')],
               'title': 'Cell Cycle — Match the Phase to What Happens'},
  'quiz': [{'opts': [('46', True), ('23', False), ('92', False), ('12', False)],
            'q': 'A human body cell has 46 chromosomes. How many chromosomes will each daughter cell have after '
                 'mitosis?',
            'wrong_explanations': {1: '23 chromosomes = the haploid number found in GAMETES after meiosis. Mitosis '
                                      'maintains the FULL chromosome number.',
                                   2: '92 is the number of chromatids DURING DNA replication — before the cell '
                                      'divides. After mitosis, each daughter cell has 46.',
                                   3: '12 has no biological relevance here. The answer is always the same as the '
                                      'parent cell — mitosis maintains chromosome number.'}},
           {'opts': [('It must be replicated — each chromosome is copied so the cell has double the DNA', True),
                     ('The DNA must be destroyed and completely rebuilt from scratch', False),
                     ('The chromosome number must be halved by meiosis first', False),
                     ('Nothing — the DNA divides automatically with no prior preparation', False)],
            'q': 'What must happen to DNA before a cell can divide by mitosis?',
            'wrong_explanations': {1: 'DNA is never destroyed during the cell cycle — it is carefully replicated and '
                                      'preserved. Destroying it would kill the cell.',
                                   2: 'Halving chromosomes = MEIOSIS. Mitosis MAINTAINS chromosome number. You cannot '
                                      'prepare for mitosis by halving DNA.',
                                   3: 'DNA replication MUST occur before division. Each daughter cell needs a complete '
                                      "set of chromosomes — if DNA wasn't replicated, one cell would get half and the "
                                      'other cell would get the other half.'}},
           {'opts': [('Benign stays in one place; malignant spreads to other parts of the body (metastasis)', True),
                     ('Benign is caused by genetics; malignant is caused by lifestyle only', False),
                     ('Malignant tumours are always fatal; benign tumours always disappear on their own', False),
                     ('Benign tumours are larger than malignant tumours', False)],
            'q': 'What is the difference between a benign and a malignant tumour?',
            'wrong_explanations': {1: 'Both benign and malignant tumours can have genetic causes and both can be '
                                      'influenced by lifestyle. The defining difference is whether the tumour SPREADS.',
                                   2: 'Malignant tumours vary hugely in outlook — many can be treated successfully. '
                                      "And benign tumours don't always disappear — they may need surgical removal.",
                                   3: 'Tumour size does not define whether it is benign or malignant. Malignant '
                                      'tumours are defined by their ability to invade and spread.'}},
           {'opts': [('Growth, repair and replacement of body cells — producing genetically identical daughter cells',
                      True),
                     ('Producing gametes (sperm and eggs) with half the chromosome number', False),
                     ('Creating genetic variation in the offspring of an organism', False),
                     ('Repairing damaged DNA before it can be copied', False)],
            'q': 'Which of the following best describes the purpose of mitosis?',
            'wrong_explanations': {1: 'Producing gametes = MEIOSIS. Gametes need half the chromosome number — mitosis '
                                      'would give them the full 46.',
                                   2: 'Mitosis produces IDENTICAL cells — there is no genetic variation. Genetic '
                                      'variation comes from meiosis and mutation.',
                                   3: 'DNA repair mechanisms exist but are separate from mitosis. Mitosis is the '
                                      'division process, not the repair process.'}},
           {'opts': [('Mutations in genes that control the cell cycle — causing uncontrolled cell division', True),
                     ('Too many mitochondria in a cell causing overproduction of ATP', False),
                     ('Cells reversing their differentiation and becoming stem cells again', False),
                     ('The immune system attacking healthy body cells', False)],
            'q': 'Cancer is caused by...',
            'wrong_explanations': {1: 'Mitochondria number has nothing to do with cancer. Cancer is caused by loss of '
                                      'cell cycle regulation due to gene mutation.',
                                   2: 'Some cancer cells do share characteristics with stem cells (undifferentiation), '
                                      'but cancer is specifically caused by mutations in regulatory genes — not by a '
                                      'deliberate reversal of differentiation.',
                                   3: 'The immune system attacking healthy cells = autoimmune disease (e.g. Type 1 '
                                      'diabetes, rheumatoid arthritis). Cancer is caused by mutated regulatory '
                                      'genes.'}}],
  'rp': None,
  'spec': '4.1.2.1',
  'summary': 'Describe chromosomes, the stages of the cell cycle and the process and purpose of mitosis.',
  'theory': [{'content': 'The nucleus of every body cell contains chromosomes — long, tightly coiled molecules of '
                         'DNA.\n'
                         'Each chromosome is one very long DNA molecule associated with proteins called histones that '
                         'help package it.\n'
                         'Each chromosome carries many GENES — a gene is a specific section of DNA coding for one '
                         'protein.\n'
                         'Humans have 46 chromosomes in most body cells, arranged as 23 PAIRS of homologous '
                         'chromosomes.\n'
                         "'Homologous' means matching — each pair carries genes for the same characteristics, but may "
                         'carry different alleles (versions) of those genes.\n'
                         'One chromosome in each pair came from the mother (via the egg) and one from the father (via '
                         'the sperm).\n'
                         'BODY CELLS: 46 chromosomes (diploid — 2n). All cells in your body except gametes.\n'
                         'GAMETES (sperm and eggs): 23 chromosomes (haploid — n). When two gametes fuse at '
                         'fertilisation: 23 + 23 = 46 — the full number is restored.',
              'heading': 'Chromosomes'},
             {'content': 'The cell cycle is the ordered series of events that a cell goes through from its formation '
                         'to its division into two new cells.\n'
                         'The cycle has three main phases:\n'
                         '\n'
                         'PHASE 1 — INTERPHASE (growth and preparation):\n'
                         'This is the longest phase — the cell spends most of its life here.\n'
                         '• G1 phase: cell grows in size. Proteins are synthesised. Number of organelles increases '
                         '(more ribosomes, mitochondria etc).\n'
                         '• S phase (DNA synthesis): each chromosome is REPLICATED — a new copy of every DNA molecule '
                         'is made. The cell now has 92 chromatids (2 copies of each of the 46 chromosomes, held '
                         'together).\n'
                         '• G2 phase: further growth. Cell checks that DNA has been copied accurately.\n'
                         '\n'
                         'PHASE 2 — MITOSIS (nuclear division):\n'
                         'The duplicated chromosomes are separated into two identical sets, each with 46 chromosomes.\n'
                         '\n'
                         'PHASE 3 — CYTOKINESIS (cytoplasm division):\n'
                         'The cytoplasm divides to form two separate daughter cells, each containing a complete '
                         'nucleus with 46 chromosomes.',
              'heading': 'The Cell Cycle'},
             {'content': 'Mitosis is the type of nuclear division that produces two genetically IDENTICAL nuclei.\n'
                         'You do NOT need to know the names of the specific phases (prophase, metaphase, anaphase, '
                         'telophase) for Foundation GCSE.\n'
                         'What you DO need to know is the overall process:\n'
                         '1. Chromosomes condense and become visible (they have already been duplicated during '
                         'interphase)\n'
                         '2. The duplicated chromosomes line up along the middle of the cell\n'
                         '3. The two copies of each chromosome are pulled to OPPOSITE ENDS of the cell\n'
                         '4. The nuclear membrane reforms around each set — two new nuclei form\n'
                         '5. The cytoplasm divides (cytokinesis) → two daughter cells, each with 46 chromosomes\n'
                         'RESULT: two cells genetically identical to each other AND to the original parent cell.',
              'heading': 'Mitosis — What Happens'},
             {'content': 'Mitosis is used for:\n'
                         '• GROWTH: from a single fertilised egg, all the trillions of body cells are produced by '
                         'repeated mitosis.\n'
                         '• REPAIR: damaged tissues are repaired by producing new identical cells — e.g. healing a cut '
                         'skin wound.\n'
                         '• REPLACEMENT: some cells wear out quickly and must be continuously replaced — red blood '
                         'cells (~120 days), gut lining cells (~5 days), skin cells (~2–4 weeks).\n'
                         '• ASEXUAL REPRODUCTION: some organisms reproduce entirely through mitosis — all offspring '
                         'are clones of the parent.\n'
                         '\n'
                         'CANCER — when the cell cycle goes wrong:\n'
                         'Normally, the cell cycle is tightly controlled by regulatory genes.\n'
                         'If a MUTATION occurs in these regulatory genes, the control is lost and cells divide '
                         'uncontrollably.\n'
                         'This produces a mass of cells called a TUMOUR.\n'
                         'Benign tumour: grows in one place, does not invade surrounding tissue, usually not '
                         'life-threatening.\n'
                         'Malignant tumour (cancer): cells break away, travel through blood or lymph, and form NEW '
                         'tumours elsewhere in the body — this spreading is called METASTASIS.\n'
                         'Treatments: surgery (remove the tumour), radiotherapy (gamma rays damage tumour cell DNA), '
                         'chemotherapy (drugs that kill rapidly dividing cells).',
              'heading': 'Why Mitosis is Important'}],
  'title': 'Chromosomes, the Cell Cycle and Mitosis',
  'triple_only': None,
  'variables': []},
 {'common_mistake': "Students often say stem cells 'replace organs' — they don't. They differentiate into SPECIFIC "
                    'CELL TYPES that can be used to repair or replace damaged cells within an organ. Also: embryonic '
                    'stem cells are TOTIPOTENT (any cell type). Adult stem cells are MULTIPOTENT (limited range). '
                    "Don't mix these terms up.",
  'equations': [],
  'fifas': [],
  'higher': "In therapeutic cloning, a patient's nucleus is inserted into an enucleated egg cell — the embryo produced "
            'is genetically identical to the patient. Stem cells from this embryo will not be rejected by the '
            "patient's immune system. Risks include viral transfer. Ethical issues: some object to embryo use. Plant "
            'meristems provide a source of totipotent stem cells for rapid cloning of rare or disease-resistant '
            'varieties.',
  'id': 'stem-cells',
  'key_note': 'Embryonic stem cells: totipotent (any cell type), ethically controversial, from IVF embryos. Adult stem '
              'cells: multipotent (limited types), bone marrow → all blood cells, used for leukaemia. Plant meristems: '
              'totipotent for plants, found at root/shoot tips, used for cloning.',
  'matching': {'instruction': 'Match each description to the correct type of stem cell.',
               'pairs': [('Embryonic stem cell', 'Totipotent — can become any of the 200+ cell types in the body'),
                         ('Adult stem cell (bone marrow)',
                          'Produces all types of blood cell — used in bone marrow transplants for leukaemia'),
                         ('Plant meristem cell',
                          'Found at root and shoot tips — can differentiate into any plant cell type'),
                         ('Embryonic stem cell',
                          'Obtained from early embryos — raises ethical concerns about destroying potential life'),
                         ('Adult stem cell', 'Multipotent — more limited range of cell types than embryonic')],
               'title': 'Match the Stem Cell Type to its Features'},
  'quiz': [{'opts': [('The cell can differentiate into any type of cell in the organism', True),
                     ('The cell can only differentiate into cells of one specific tissue type', False),
                     ('The cell can divide indefinitely without ever differentiating', False),
                     ('The cell has already partially specialised and cannot reverse', False)],
            'q': "What does 'totipotent' mean when describing stem cells?",
            'wrong_explanations': {1: 'Differentiating into cells of one tissue type = MULTIPOTENT (e.g. bone marrow '
                                      'stem cells → blood cells only). Totipotent = ANY cell type.',
                                   2: 'The ability to divide indefinitely is SELF-RENEWAL — a separate property of '
                                      'stem cells. Totipotency refers to differentiation potential.',
                                   3: 'Partially specialised cells that cannot reverse are already differentiated '
                                      'cells — not stem cells at all.'}},
           {'opts': [('A bone marrow transplant: cancerous blood cells destroyed, then donor stem cells replace them '
                      'and produce healthy blood cells',
                      True),
                     ('Embryonic stem cells are injected into the blood to replace cancer cells', False),
                     ('Stem cells are used to make antibodies that kill cancer cells directly', False),
                     ('Stem cells repair the damaged DNA in leukaemia cells, reversing the cancer', False)],
            'q': 'How are stem cells used to treat leukaemia?',
            'wrong_explanations': {1: 'Embryonic stem cells are not used for leukaemia treatment — adult bone marrow '
                                      "stem cells are used. They are donated or sometimes the patient's own (after "
                                      'treatment).',
                                   2: 'Antibodies that target cancer cells are a different therapy (monoclonal '
                                      'antibodies) — not how stem cells work in leukaemia treatment.',
                                   3: "Stem cells don't repair cancer cell DNA — the cancer cells are destroyed by "
                                      'chemotherapy/radiotherapy first, then NEW healthy cells are produced from '
                                      'transplanted stem cells.'}},
           {'opts': [('Obtaining them requires destroying an embryo — which some consider to be destroying a potential '
                      'human life',
                      True),
                     ('They cause cancer in patients who receive them', False),
                     ('They are ineffective at treating disease', False),
                     ('They are too expensive to collect and store', False)],
            'q': 'Why are embryonic stem cells ethically controversial?',
            'wrong_explanations': {1: 'Cancer risk is a technical concern — the main ETHICAL controversy is about the '
                                      'moral status of the embryo that is destroyed.',
                                   2: 'Embryonic stem cells are actually MORE effective than adult stem cells because '
                                      'they are totipotent — the concern is ethical, not about effectiveness.',
                                   3: 'Cost and practicality are challenges — but the defining controversy is ethical: '
                                      'is it acceptable to destroy a potential human life for medical research?'}},
           {'opts': [('Plant meristem cells are totipotent — they can form any plant cell type; adult animal stem '
                      'cells are only multipotent',
                      True),
                     ('Plant meristem cells can only form root cells; animal stem cells are more versatile', False),
                     ('Plant meristem cells are found throughout all plant tissues; animal stem cells are only in bone '
                      'marrow',
                      False),
                     ('There is no difference — both types have the same level of potency', False)],
            'q': 'What is special about plant meristem cells compared to adult animal stem cells?',
            'wrong_explanations': {1: 'It is almost the opposite — plant meristems are MORE versatile (totipotent), '
                                      'not less.',
                                   2: 'Meristems are found in specific regions (root tips, shoot tips, cambium) — not '
                                      'throughout all tissues. And they can form any plant cell type, not just root '
                                      'cells.',
                                   3: 'There is a significant difference in potency — plant meristem cells are '
                                      'essentially totipotent while most adult animal stem cells are multipotent.'}}],
  'rp': None,
  'spec': '4.1.2.3',
  'summary': 'Describe the properties and uses of stem cells, including embryonic, adult and plant meristem cells.',
  'theory': [{'content': 'A stem cell is an undifferentiated cell — a cell that has not yet specialised.\n'
                         'All stem cells share two key properties:\n'
                         '1. SELF-RENEWAL: they can divide by mitosis to produce more copies of themselves '
                         'indefinitely.\n'
                         '2. POTENCY: they can differentiate into one or more types of specialised cell.\n'
                         'Stem cells are essential during development — they provide the source from which all '
                         'specialised cells of the body are produced.\n'
                         'They also play a role in maintenance and repair throughout life — replacing worn-out or '
                         'damaged cells in certain tissues.',
              'heading': 'What Are Stem Cells?'},
             {'content': 'EMBRYONIC STEM CELLS are found in the inner cell mass of a human embryo at 3–5 days old '
                         '(called a blastocyst).\n'
                         'They are TOTIPOTENT — they can differentiate into ANY of the more than 200 cell types in the '
                         'human body.\n'
                         'This makes them the most versatile type of stem cell.\n'
                         'How they are obtained: the embryo is destroyed to extract the stem cells. This is usually '
                         'done using embryos left over from IVF (in vitro fertilisation) treatment that would '
                         'otherwise be discarded.\n'
                         'Potential uses:\n'
                         '• Replacing insulin-producing beta cells in the pancreas → treating Type 1 diabetes\n'
                         "• Growing new neurones → treating Parkinson's disease or spinal cord injuries\n"
                         '• Producing heart muscle cells → repairing damage after a heart attack\n'
                         '• Growing skin for burns victims\n'
                         "Challenges: immune rejection (the patient's immune system may attack the transplanted "
                         'cells), and the risk of tumour formation if undifferentiated cells remain.',
              'heading': 'Embryonic Stem Cells'},
             {'content': 'ADULT STEM CELLS are found in specific tissues throughout the body — even in fully-grown '
                         'adults.\n'
                         'They are MULTIPOTENT — they can only differentiate into the cell types found in the tissue '
                         'where they live.\n'
                         'Bone marrow stem cells are the most well-known and well-used:\n'
                         '• Haematopoietic (blood-forming) stem cells in bone marrow produce ALL types of blood cell: '
                         'red blood cells, white blood cells, platelets.\n'
                         'Clinical use — bone marrow transplant:\n'
                         '• Used to treat leukaemia (cancer of blood cells).\n'
                         "• The patient's cancerous bone marrow is destroyed by high-dose chemotherapy/radiotherapy.\n"
                         '• Healthy donor bone marrow (containing stem cells) is transplanted → new, healthy blood '
                         'cells are produced.\n'
                         'Advantages of adult over embryonic stem cells: no ethical controversy, the patient can be '
                         'their own donor (if using their own stem cells — autologous transplant).\n'
                         'Disadvantages: more limited range of cell types, harder to grow in large numbers.',
              'heading': 'Adult Stem Cells'},
             {'content': 'Plants have their own form of stem cells — MERISTEM CELLS, found in regions of the plant '
                         'called MERISTEMS.\n'
                         'Meristems are located:\n'
                         '• At the tips of roots and shoots (apical meristems) — responsible for lengthening\n'
                         '• Along the sides of stems (lateral meristems) — responsible for thickening\n'
                         'Unlike most animal adult stem cells, plant meristem cells are essentially TOTIPOTENT — they '
                         'can differentiate into ANY type of plant cell.\n'
                         'This is why plants can keep growing throughout their entire lives — a new leaf, root or '
                         'flower can always be produced from meristem cells.\n'
                         'Applications:\n'
                         '• CLONING: a single meristem cell or small section of tissue can be grown into an entirely '
                         'new, genetically identical plant (tissue culture / micropropagation).\n'
                         '• Conserving rare or endangered plant species.\n'
                         '• Mass-producing disease-resistant crop plants.\n'
                         '• Creating large numbers of identical, high-quality plants quickly.',
              'heading': 'Plant Meristem Cells'},
             {'content': 'Stem cell research — particularly using embryonic stem cells — raises significant ethical '
                         'questions:\n'
                         'ARGUMENTS FOR:\n'
                         '• Could cure debilitating diseases that currently have no treatment\n'
                         '• Embryos used are from IVF treatment and would be destroyed anyway\n'
                         '• Early embryos (blastocysts) are just a ball of ~100 cells — not yet a person\n'
                         'ARGUMENTS AGAINST:\n'
                         '• Destroying an embryo destroys a potential human life — many religious groups hold this '
                         'view\n'
                         '• The embryo cannot consent to being used for research\n'
                         "• Concerns that this could lead to cloning of humans ('slippery slope' argument)\n"
                         '• Risk of exploitation — women may be pressured to donate eggs\n'
                         'In the UK, embryonic stem cell research is strictly regulated by the Human Fertilisation and '
                         'Embryology Authority (HFEA) — research is permitted up to 14 days of embryo development.',
              'heading': 'Ethical Issues around Stem Cell Research'}],
  'title': 'Stem Cells',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Osmosis involves WATER ONLY — through a PARTIALLY PERMEABLE MEMBRANE. Glucose, ions and other '
                    'molecules do NOT move by osmosis. Active transport goes AGAINST the gradient and requires ATP '
                    'energy — without ATP (no respiration) it stops. Diffusion and osmosis are both PASSIVE — no ATP '
                    "needed. Never say 'diffusion requires energy'.",
  'equations': [],
  'fifas': [{'label': 'Osmosis — Percentage Change in Mass',
             'question': 'A potato cylinder has a mass of 4.0 g before being placed in a concentrated sugar solution. '
                         'After 30 minutes it has a mass of 3.4 g. Calculate the percentage change in mass.',
             'steps': [('F', '% change = (final mass − initial mass) ÷ initial mass × 100'),
                       ('I', '% change = (3.4 − 4.0) ÷ 4.0 × 100'),
                       ('F', '= (−0.6) ÷ 4.0 × 100 = −15%'),
                       ('A', '% change = −15% (a decrease — water left by osmosis into the concentrated solution)')]}],
  'higher': 'Calculating percentage change in mass in osmosis: % change = (change in mass ÷ original mass) × 100. The '
            'isotonic point — where a plant tissue neither gains nor loses mass — is where the external solution '
            "concentration matches the cell's water potential. Exchange surfaces are adapted with large surface area, "
            'thin walls, good blood supply/ventilation. Students should be able to explain and calculate surface area '
            'to volume ratios and explain why large organisms need exchange systems.',
  'id': 'transport-in-cells',
  'key_note': 'Diffusion: particles, high → low, passive. Osmosis: water only, dilute → concentrated, partially '
              'permeable membrane, passive. Active transport: low → high, against gradient, requires ATP + carrier '
              'proteins.',
  'matching': {'instruction': 'Match each description to diffusion, osmosis or active transport.',
               'pairs': [('Diffusion', 'Net movement of particles from high to low concentration — no energy needed'),
                         ('Osmosis',
                          'Movement of water molecules only across a partially permeable membrane — passive'),
                         ('Active transport',
                          'Movement against the concentration gradient — requires ATP and carrier proteins'),
                         ('Diffusion', 'Oxygen moving from alveoli into the blood — no ATP required'),
                         ('Osmosis',
                          'Water entering a root hair cell from the soil — the soil water is more dilute than cell '
                          'contents'),
                         ('Active transport',
                          'Mineral ions absorbed into root hair cells from dilute soil water — against the gradient')],
               'title': 'Match the Transport Process'},
  'quiz': [{'opts': [('Active transport', True),
                     ('Diffusion', False),
                     ('Osmosis', False),
                     ('Both diffusion and osmosis', False)],
            'q': 'Which process requires ATP energy to move substances across a cell membrane?',
            'wrong_explanations': {1: 'Diffusion is PASSIVE — particles move due to their own random kinetic energy, '
                                      'not ATP.',
                                   2: 'Osmosis is also PASSIVE — water moves down its own concentration gradient '
                                      'without energy input.',
                                   3: 'NEITHER diffusion nor osmosis requires ATP. Only active transport requires '
                                      'energy — that is what distinguishes it from the other two.'}},
           {'opts': [('It gains mass — water enters by osmosis from the dilute water into the more concentrated cell '
                      'contents',
                      True),
                     ('It loses mass — salt leaves the potato into the water by diffusion', False),
                     ('Nothing — the potato is not permeable to water', False),
                     ('It gains mass because water enters by active transport', False)],
            'q': 'A potato cylinder is placed in pure water. What happens and why?',
            'wrong_explanations': {1: 'Salt does diffuse slightly — but the dominant effect is water moving by OSMOSIS '
                                      'into the cells, increasing mass.',
                                   2: 'Cell membranes are selectively permeable — water moves freely across them by '
                                      'osmosis. The potato is very much permeable to water.',
                                   3: 'Osmosis is PASSIVE — it requires no energy input. Water moves down its '
                                      'concentration gradient automatically.'}},
           {'opts': [('No oxygen → aerobic respiration stops → no ATP produced → no energy for active transport', True),
                     ('Oxygen is a carrier protein that directly powers active transport', False),
                     ('Without oxygen, the cell membrane becomes impermeable to all substances', False),
                     ('Removing oxygen changes the concentration gradient, making active transport unnecessary',
                      False)],
            'q': 'Why does active transport stop if oxygen is removed from the environment of a cell?',
            'wrong_explanations': {1: "Oxygen doesn't directly power carrier proteins — it is needed for aerobic "
                                      'respiration to produce ATP, which then powers the carriers.',
                                   2: 'Membranes remain structurally intact without oxygen — it is the ATP supply that '
                                      'is lost, not membrane structure.',
                                   3: "Removing oxygen doesn't change concentration gradients. It removes the ATP "
                                      'supply needed to pump substances against those gradients.'}},
           {'opts': [('Water leaves by osmosis → the cell becomes flaccid → the cell membrane pulls away from the cell '
                      'wall (plasmolysis)',
                      True),
                     ('Water enters by osmosis → the cell becomes turgid and very firm', False),
                     ('Salt enters by active transport → the cell becomes denser', False),
                     ('The cell bursts because it cannot handle the osmotic pressure', False)],
            'q': 'A plant cell is placed in a very concentrated salt solution. What will happen?',
            'wrong_explanations': {1: 'Water enters when the EXTERNAL solution is MORE DILUTE than the cell contents. '
                                      'In concentrated salt solution, it is the other way round — water leaves.',
                                   2: 'Salt ions may slowly diffuse in, but the dominant effect is OSMOSIS — water '
                                      'moves to the MORE CONCENTRATED solution (the salt solution outside), not into '
                                      'the cell.',
                                   3: 'Plant cells have a rigid CELL WALL that prevents bursting — unlike animal '
                                      "cells. A plant cell can become flaccid or plasmolyse, but it won't burst."}},
           {'opts': [('The net movement of water molecules across a partially permeable membrane from a dilute '
                      'solution to a more concentrated solution',
                      True),
                     ('The movement of any particles from high to low concentration — passive', False),
                     ('The movement of water molecules against a concentration gradient using ATP', False),
                     ('The diffusion of water molecules through any membrane in any direction', False)],
            'q': 'What is the definition of osmosis?',
            'wrong_explanations': {1: 'The movement of ANY particles from high to low = DIFFUSION. Osmosis is '
                                      'specifically about WATER ONLY through a PARTIALLY PERMEABLE membrane.',
                                   2: 'Movement against a gradient using ATP = ACTIVE TRANSPORT. Osmosis is passive — '
                                      'water moves DOWN its concentration gradient.',
                                   3: 'Osmosis only occurs through a PARTIALLY PERMEABLE membrane, not any membrane. '
                                      'And it only moves water in ONE net direction — from dilute to concentrated.'}}],
  'rp': 'RP2 — Investigate osmosis: place potato cylinders in different concentrations of sucrose solution. Measure '
        'mass before and after. Calculate % change in mass.',
  'spec': '4.1.3',
  'summary': 'Describe and compare the three ways substances move into and out of cells.',
  'theory': [{'content': 'DIFFUSION is the net movement of particles (molecules or ions) from a region of HIGHER '
                         'concentration to a region of LOWER concentration — down the concentration gradient.\n'
                         'It is a PASSIVE process — no energy (ATP) is required. Particles move due to their own '
                         'random kinetic energy.\n'
                         'Diffusion continues until concentrations are equal on both sides — this is called '
                         "EQUILIBRIUM. Even at equilibrium, particles are still moving randomly — there's just no NET "
                         'movement.\n'
                         '\n'
                         'Factors that increase the rate of diffusion:\n'
                         '• STEEPER concentration gradient — bigger difference in concentration = faster net movement\n'
                         '• HIGHER temperature — more kinetic energy → particles move faster\n'
                         '• LARGER surface area — more space available for diffusion to occur across\n'
                         '• SHORTER diffusion distance — thinner membrane → particles cross faster\n'
                         '\n'
                         'Examples in biology:\n'
                         '• O₂ diffuses from alveoli (high [O₂]) → into blood (lower [O₂]) → into muscle cells (even '
                         'lower [O₂])\n'
                         '• CO₂ diffuses from respiring cells (high [CO₂]) → into blood → into alveoli (low [CO₂])\n'
                         '• Glucose diffuses from the small intestine (high [glucose] after digestion) → into blood\n'
                         '• Urea diffuses from liver cells (where it is made) → into blood → into kidney tubules → '
                         'excreted in urine',
              'heading': 'Diffusion'},
             {'content': 'OSMOSIS is a special type of diffusion — it is the net movement of WATER MOLECULES ONLY '
                         'across a PARTIALLY PERMEABLE MEMBRANE, from a DILUTE solution (more water molecules, high '
                         'water potential) to a MORE CONCENTRATED solution (fewer water molecules, low water '
                         'potential).\n'
                         'A partially permeable membrane has tiny pores that allow small water molecules through but '
                         'block larger solute molecules.\n'
                         'Osmosis is also PASSIVE — no ATP energy is required.\n'
                         '\n'
                         'In PLANT CELLS:\n'
                         '• Cell placed in DILUTE solution: water enters by osmosis → vacuole swells → cell membrane '
                         'pushes against rigid cell wall → cell becomes TURGID (firm). Turgid cells provide structural '
                         'support to the plant.\n'
                         '• Cell placed in CONCENTRATED solution: water leaves by osmosis → vacuole and cytoplasm '
                         'shrink → cell membrane pulls away from cell wall → PLASMOLYSIS. Plant wilts.\n'
                         '\n'
                         'In ANIMAL CELLS (no cell wall to limit swelling):\n'
                         '• Cell in DILUTE solution: water enters by osmosis → cell SWELLS → may BURST (LYSIS) if too '
                         'much water enters — e.g. red blood cells burst in pure water\n'
                         '• Cell in CONCENTRATED solution: water leaves by osmosis → cell SHRINKS (CRENATION)\n'
                         'This is why the body carefully controls the concentration of blood and body fluids — '
                         'deviations cause serious damage to cells.',
              'heading': 'Osmosis'},
             {'content': 'ACTIVE TRANSPORT is the movement of substances from a region of LOWER concentration to a '
                         'region of HIGHER concentration — AGAINST the concentration gradient.\n'
                         'This requires:\n'
                         '1. ENERGY from ATP (produced by aerobic respiration)\n'
                         '2. CARRIER PROTEINS embedded in the cell membrane\n'
                         'Because it requires ATP, active transport STOPS immediately if respiration is blocked (e.g. '
                         'by cyanide, which blocks aerobic respiration, or by removing oxygen).\n'
                         '\n'
                         'Examples in biology:\n'
                         '• ROOTS absorbing minerals: the concentration of mineral ions (e.g. nitrates, magnesium) '
                         'inside root hair cells is ALREADY HIGHER than in the soil water. Yet plants need even more. '
                         'Active transport pumps them in against the gradient.\n'
                         '• SMALL INTESTINE absorbing glucose: once most glucose has been absorbed by diffusion, the '
                         'remaining glucose must be moved from the gut (low [glucose]) into the blood (higher '
                         '[glucose]) by active transport — ensuring all available glucose is absorbed.',
              'heading': 'Active Transport'},
             {'content': 'Single-celled organisms have a high surface area to volume ratio — simple diffusion is '
                         'sufficient.\n'
                         'Large multicellular organisms have a much LOWER surface area to volume ratio — the distance '
                         'from surface to interior cells is too great for diffusion alone.\n'
                         'They need SPECIALISED EXCHANGE SURFACES and TRANSPORT SYSTEMS.\n'
                         '\n'
                         'Features of an efficient exchange surface:\n'
                         '• LARGE SURFACE AREA: more area for particles to cross per unit time\n'
                         '• THIN MEMBRANE: short diffusion path\n'
                         '• STEEP CONCENTRATION GRADIENT: maintained by good blood supply (or ventilation for gas '
                         'exchange)\n'
                         '\n'
                         'Examples:\n'
                         '• ALVEOLI (lungs): surrounded by dense capillary network, one cell thick, highly folded — '
                         'for O₂/CO₂ exchange\n'
                         '• VILLI (small intestine): finger-like projections with microvilli (brush border), rich '
                         'blood supply, one cell thick walls — for nutrient absorption\n'
                         '• ROOT HAIR CELLS: long projections increase surface area enormously — for water and mineral '
                         'absorption from soil',
              'heading': 'Exchange Surfaces in Multicellular Organisms'}],
  'title': 'Diffusion, Osmosis and Active Transport',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Petri dishes in school are incubated at 25°C — NOT at 37°C (body temperature). This is '
                    'deliberately to reduce the risk of growing dangerous human pathogens. A larger inhibition zone '
                    'means MORE effective antibiotic — the bacteria cannot grow in that area. A disc with no clear '
                    'zone = resistant bacteria.',
  'equations': ['Area of inhibition zone = π × r²'],
  'fifas': [{'label': 'Inhibition Zone Area',
             'question': 'An antibiotic disc produces a clear zone with a diameter of 18 mm. Calculate the area of the '
                         'inhibition zone.',
             'steps': [('F', 'Area = π × r²'),
                       ('I', 'Diameter = 18 mm → radius = 9 mm. Area = π × 9²'),
                       ('F', 'Area = π × 81 = 254.47...'),
                       ('A', 'Area ≈ 254 mm²')]}],
  'higher': None,
  'id': 'culturing-microorganisms',
  'key_note': 'Culture medium: agar + nutrients in Petri dish. Aseptic technique: sterilise equipment, flame loops, '
              'work near Bunsen. Incubate at max 25°C in school (safety). Inhibition zone: clear area around '
              'antibiotic disc — larger = more effective.',
  'matching': {'instruction': 'Match each step to why it is done.',
               'pairs': [('Autoclave Petri dishes and media', 'Kills all microorganisms including spores before use'),
                         ('Flame the inoculating loop',
                          'Sterilises the loop before and after use — prevents contamination'),
                         ('Work near a Bunsen burner',
                          'Rising hot air carries airborne contaminants away from the work surface'),
                         ('Seal Petri dish with tape',
                          'Prevents airborne microorganisms from entering after inoculation'),
                         ('Incubate at 25°C not 37°C', 'Safety — reduces risk of growing dangerous human pathogens'),
                         ('Larger inhibition zone',
                          'More effective antibiotic — bacteria cannot grow in a wider area')],
               'title': 'Match the Aseptic Technique Step'},
  'quiz': [{'opts': [('Safety — bacteria that grow optimally at 37°C are more likely to be harmful human pathogens',
                      True),
                     ('Bacteria grow faster at 25°C', False),
                     ('37°C would melt the agar', False),
                     ('Antibiotics only work at 25°C', False)],
            'q': 'Why are school bacterial cultures incubated at 25°C rather than 37°C?',
            'wrong_explanations': {1: 'Bacteria generally grow FASTER at higher temperatures — 37°C would give quicker '
                                      'results, but the safety risk outweighs this.',
                                   2: 'Agar melts at much higher temperatures (around 85°C) — 37°C would not melt it.',
                                   3: 'Antibiotic effectiveness is not temperature-dependent in this way — the safety '
                                      'concern is the primary reason.'}},
           {'opts': [('The antibiotic is highly effective against that bacterium — it diffuses outward and kills '
                      'bacteria in a wide area',
                      True),
                     ('The bacteria are resistant — they moved away from the antibiotic', False),
                     ('The disc absorbed the bacteria, leaving a clear area', False),
                     ('The agar failed to set properly in that area', False)],
            'q': 'What does a large inhibition zone around an antibiotic disc indicate?',
            'wrong_explanations': {1: 'Resistant bacteria show NO inhibition zone — they grow right up to the disc.',
                                   2: "Discs absorb the antibiotic solution — they don't absorb bacteria.",
                                   3: 'Properly prepared agar sets evenly — uneven setting would affect all areas, not '
                                      'just around specific discs.'}},
           {'opts': [('To sterilise it — killing all microorganisms before use (preventing contamination) and after '
                      'use (preventing spread)',
                      True),
                     ('To warm the loop so bacteria transfer more easily', False),
                     ('To melt the agar so bacteria can be mixed in', False),
                     ('To activate the bacteria before plating', False)],
            'q': 'Why is an inoculating loop flamed before and after transferring bacteria?',
            'wrong_explanations': {1: 'Warming would not sterilise — only red-hot temperatures kill all '
                                      'microorganisms.',
                                   2: 'The loop does not touch agar during streaking in a way that needs melting — it '
                                      'is used at room temperature to spread bacteria on the surface.',
                                   3: "Bacteria don't need 'activation' — flaming is purely for sterilisation."}}],
  'rp': 'RP6 — Required practical: investigate the effect of antiseptics or antibiotics on bacterial growth using agar '
        'plates and measuring inhibition zones.',
  'spec': '4.1.2',
  'summary': 'Describe how bacteria are cultured in the laboratory and how to prevent contamination.',
  'theory': [{'content': 'CULTURING microorganisms means growing them in controlled laboratory conditions so we can '
                         'study them.\n'
                         '\n'
                         'Culturing bacteria is essential for:\n'
                         'Testing the effectiveness of antibiotics and antiseptics.\n'
                         'Studying the growth and behaviour of pathogens.\n'
                         'Producing medicines, foods (yoghurt, bread, cheese) and industrial chemicals.\n'
                         'Researching new drugs and treatments.\n'
                         '\n'
                         'Bacteria and fungi are grown on or in a CULTURE MEDIUM — a substance containing all the '
                         'nutrients the microorganism needs:\n'
                         'Carbon source (glucose or other sugar) for energy.\n'
                         'Nitrogen source (nitrates or amino acids) for protein synthesis.\n'
                         'Minerals and vitamins.\n'
                         '\n'
                         'The most common culture medium is AGAR — a gel made from seaweed. Nutrients are dissolved in '
                         'warm liquid agar which is then poured into PETRI DISHES where it sets into a firm gel. '
                         'Bacteria grow on the surface, forming visible colonies.',
              'heading': 'Why We Culture Microorganisms'},
             {'content': 'Contamination means unwanted microorganisms getting into the culture — this would give false '
                         'results and could introduce dangerous pathogens.\n'
                         '\n'
                         'ASEPTIC TECHNIQUE is the set of procedures used to prevent contamination:\n'
                         '\n'
                         'STERILISING EQUIPMENT:\n'
                         'Petri dishes and culture media are sterilised using an AUTOCLAVE (high-pressure steam at '
                         '121°C) — kills all microorganisms including spores.\n'
                         'Glass equipment (beakers, loops) can be sterilised by heating in a Bunsen flame.\n'
                         '\n'
                         'PROCEDURE:\n'
                         'Work near a Bunsen burner — hot rising air carries contaminants away from the work area.\n'
                         'Flame the inoculating loop until red hot before AND after use — kills all bacteria on it.\n'
                         'Flame the neck of the culture bottle or test tube before opening.\n'
                         'Lift the Petri dish lid only slightly and briefly — never fully open it.\n'
                         'Seal Petri dishes with tape after inoculation — prevents airborne contamination.\n'
                         '\n'
                         'TEMPERATURE OF INCUBATION:\n'
                         'In school laboratories, cultures are incubated at a MAXIMUM of 25°C — not at body '
                         'temperature (37°C).\n'
                         'This is a safety precaution — bacteria that thrive at 37°C are more likely to be harmful '
                         'human pathogens.\n'
                         'In industry and research, 37°C may be used under strict controlled conditions.',
              'heading': 'Preventing Contamination — Aseptic Technique'},
             {'content': 'Agar plates are used to test which antibiotics or antiseptics are most effective against '
                         'bacteria.\n'
                         '\n'
                         'METHOD:\n'
                         '1. Spread bacteria evenly over the surface of an agar plate (lawn of bacteria).\n'
                         '2. Place discs of filter paper soaked in different antibiotics/antiseptics on the agar '
                         'surface.\n'
                         '3. Incubate at 25°C for 24–48 hours.\n'
                         '4. Observe and measure the CLEAR ZONES (inhibition zones) around each disc.\n'
                         '\n'
                         'INHIBITION ZONE:\n'
                         'As the antibiotic/antiseptic diffuses outward from the disc, it kills or inhibits nearby '
                         'bacteria.\n'
                         'A LARGER inhibition zone = MORE EFFECTIVE antibiotic/antiseptic at that concentration.\n'
                         'NO inhibition zone = the bacteria are RESISTANT to that antibiotic.\n'
                         '\n'
                         'CALCULATING ZONE AREA:\n'
                         'Area = π × r² (where r = radius of clear zone)\n'
                         'Compare zones to determine which substance is most effective.\n'
                         '\n'
                         'CONTROL DISC: a disc soaked in distilled water only — confirms that any inhibition is due to '
                         'the substance, not the disc itself.',
              'heading': 'Investigating Antibiotic and Antiseptic Effectiveness'}],
  'title': 'Culturing Microorganisms',
  'triple_only': None,
  'variables': []}],

"organisation": [{'common_mistake': 'Students confuse tissue and organ. Remember: a tissue is ONE type of cell doing ONE job. An organ '
                    'contains MULTIPLE tissue types. The stomach is an ORGAN (it has muscle tissue, glandular tissue '
                    'and epithelial tissue). Muscle is a TISSUE.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'principles-of-organisation',
  'key_note': 'Cell → Tissue (same cells, one function) → Organ (multiple tissues) → Organ System (multiple organs) → '
              'Organism. Each level is more complex than the one before.',
  'matching': {'instruction': 'Match each example to its correct level of organisation.',
               'pairs': [('Cell', 'A single red blood cell carrying oxygen in the blood'),
                         ('Tissue', 'Muscle — a group of muscle cells that contract together'),
                         ('Organ', 'The stomach — contains muscle, glandular and epithelial tissue'),
                         ('Organ system', 'The digestive system — stomach, intestines, liver and pancreas'),
                         ('Organism', 'A complete human being — all systems functioning together')],
               'title': 'Match the Level of Organisation'},
  'quiz': [{'opts': [('Cell → Tissue → Organ → Organ system → Organism', True),
                     ('Tissue → Cell → Organ → Organ system → Organism', False),
                     ('Cell → Organ → Tissue → Organism → Organ system', False),
                     ('Organism → Organ system → Organ → Tissue → Cell', False)],
            'q': 'What is the correct order of organisation from simplest to most complex?',
            'wrong_explanations': {1: 'Tissues are made of cells — cells always come before tissues in the hierarchy.',
                                   2: 'Organs contain tissues, not the other way round — tissue must come before '
                                      'organ.',
                                   3: 'This is the correct order in reverse — from most complex down to simplest.'}},
           {'opts': [('A group of similar cells working together to perform a specific function', True),
                     ('A group of different organs working together', False),
                     ('A single highly specialised cell', False),
                     ('Another name for an organ', False)],
            'q': 'What is a tissue?',
            'wrong_explanations': {1: 'A group of different organs = an ORGAN SYSTEM. Tissues are made of similar '
                                      'cells, not organs.',
                                   2: 'A single specialised cell is just a cell — not a tissue. A tissue is a GROUP of '
                                      'cells.',
                                   3: 'Tissues and organs are different levels. An organ is made of SEVERAL tissue '
                                      'types.'}},
           {'opts': [('Organ', True), ('Tissue', False), ('Organ system', False), ('Organism', False)],
            'q': 'The stomach contains muscle tissue, glandular tissue and epithelial tissue. What level of '
                 'organisation is the stomach?',
            'wrong_explanations': {1: 'A tissue is made of ONE type of cell — the stomach has multiple tissue types, '
                                      'so it is an organ.',
                                   2: 'An organ system is a GROUP of organs — the stomach is just one organ within the '
                                      'digestive system.',
                                   3: 'An organism is the complete living thing — a human, plant or bacterium.'}},
           {'opts': [('The digestive system — stomach, intestines, liver and pancreas working together', True),
                     ('Muscle tissue — cells that contract to produce movement', False),
                     ('The heart — contains cardiac muscle and valves', False),
                     ('A liver cell — specialised to carry out chemical reactions', False)],
            'q': 'Which of these is an example of an organ system?',
            'wrong_explanations': {1: 'Muscle tissue = a TISSUE (one cell type). Organ systems are made of multiple '
                                      'organs.',
                                   2: 'The heart = an ORGAN (contains multiple tissue types). An organ system requires '
                                      'multiple organs.',
                                   3: 'A liver cell = a CELL — the simplest level of organisation.'}}],
  'rp': None,
  'spec': '4.2.1',
  'summary': 'Describe the levels of organisation in living organisms from cells to organisms.',
  'theory': [{'content': 'Living organisms are built from simple parts that are organised into increasingly complex '
                         'levels.\n'
                         '\n'
                         'The levels in order from simplest to most complex are:\n'
                         'CELL → TISSUE → ORGAN → ORGAN SYSTEM → ORGANISM\n'
                         '\n'
                         'This hierarchy is the foundation of biology — understanding it helps you understand how the '
                         'body works as a whole, and why problems at one level (e.g. a faulty cell) can affect the '
                         'whole organism.',
              'heading': 'The Hierarchy of Organisation'},
             {'content': 'A cell is the smallest unit capable of carrying out all the processes of life.\n'
                         '\n'
                         'Every living organism is made of at least one cell.\n'
                         '\n'
                         'Different cell types are specialised for different jobs — a muscle cell is built to '
                         'contract, a red blood cell is built to carry oxygen, a root hair cell is built to absorb '
                         'water.\n'
                         '\n'
                         'All cells in one organism contain the same DNA, but different genes are switched on in '
                         'different cell types.',
              'heading': 'Cells — The Basic Unit of Life'},
             {'content': 'A tissue is a group of similar cells working together to carry out a particular function.\n'
                         '\n'
                         'Key examples of animal tissues:\n'
                         'Muscle tissue — cells that can contract and relax to produce movement.\n'
                         'Epithelial tissue — thin cells that line surfaces (e.g. gut lining, airway lining, skin '
                         'surface).\n'
                         'Glandular tissue — cells that produce and release substances such as enzymes, hormones or '
                         'mucus.\n'
                         'Nervous tissue — neurones that carry electrical impulses.\n'
                         '\n'
                         'Key examples of plant tissues:\n'
                         'Mesophyll tissue — cells in leaves packed with chloroplasts for photosynthesis.\n'
                         'Xylem tissue — hollow dead cells that transport water upwards.\n'
                         'Phloem tissue — living cells that transport dissolved sugars.',
              'heading': 'Tissues'},
             {'content': 'An organ is a structure made of several DIFFERENT types of tissue working together to '
                         'perform a specific function.\n'
                         '\n'
                         'Key examples:\n'
                         'The STOMACH — contains muscle tissue (churns food), epithelial tissue (lines the stomach '
                         'wall), glandular tissue (secretes HCl and pepsin enzymes).\n'
                         '\n'
                         'The LEAF — contains mesophyll tissue (photosynthesis), xylem (water supply), phloem (sugar '
                         'transport), epidermis (protection), guard cells (gas exchange).\n'
                         '\n'
                         'The HEART — contains cardiac muscle tissue (pumps blood), valves (prevent backflow), '
                         'coronary blood vessels (supply oxygen to heart muscle).\n'
                         '\n'
                         'The KEY DIFFERENCE between a tissue and an organ: a tissue is made of ONE type of cell. An '
                         'organ contains MULTIPLE different tissue types.',
              'heading': 'Organs'},
             {'content': 'An organ system is a group of organs that work together to perform a major function.\n'
                         '\n'
                         'Examples:\n'
                         'Digestive system — mouth, oesophagus, stomach, small intestine, large intestine, liver, '
                         'pancreas. Function: breaks down food and absorbs nutrients.\n'
                         '\n'
                         'Circulatory system — heart, blood vessels, blood. Function: transports oxygen, nutrients and '
                         'waste products.\n'
                         '\n'
                         'Respiratory system — lungs, trachea, bronchi, diaphragm. Function: gas exchange (O₂ in, CO₂ '
                         'out).\n'
                         '\n'
                         'Nervous system — brain, spinal cord, nerves. Function: detects stimuli and coordinates '
                         'responses.\n'
                         '\n'
                         'An ORGANISM is the complete living individual — all organ systems working together to '
                         'sustain life.',
              'heading': 'Organ Systems and Organisms'}],
  'title': 'Principles of Organisation',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Bile is NOT an enzyme and does NOT chemically digest fats. It EMULSIFIES them — a physical '
                    'process that breaks large fat droplets into smaller ones to give lipase more surface area to work '
                    "on. Students often say 'bile digests fat' — it does not. LIPASE chemically digests fat.",
  'equations': [],
  'fifas': [],
  'higher': 'Bile emulsifies fats — breaking large droplets into smaller ones, greatly increasing the surface area for '
            'lipase. The alkaline conditions created by bile neutralising stomach acid provide the optimum pH for '
            'pancreatic enzymes. Villi and microvilli on the intestinal lining further maximise surface area for '
            'absorption. Students should be able to explain how the small intestine is adapted for efficient '
            'absorption (large surface area, thin walls, rich blood supply).',
  'id': 'digestive-system',
  'key_note': 'Mouth: amylase digests starch. Stomach: pepsin digests proteins, HCl creates pH 2. Small intestine: all '
              'three enzymes from pancreas + bile from liver. Large intestine: absorbs water.',
  'matching': {'instruction': 'Match each organ to what it does.',
               'pairs': [('Mouth', 'Amylase begins starch digestion — teeth grind food — bolus formed'),
                         ('Stomach', 'HCl + pepsin — proteins digested — chyme produced'),
                         ('Pancreas', 'Produces amylase, protease and lipase — released into small intestine'),
                         ('Liver', 'Produces bile — stored in gall bladder — emulsifies fats in small intestine'),
                         ('Small intestine', 'Main site of digestion and absorption — villi absorb nutrients'),
                         ('Large intestine', 'Absorbs water from undigested material — faeces formed')],
               'title': 'Match the Organ to its Role in Digestion'},
  'quiz': [{'opts': [('Emulsifies fats — breaks large droplets into smaller ones to increase surface area for lipase',
                      True),
                     ('Chemically digests fats into fatty acids and glycerol', False),
                     ('Kills bacteria in the small intestine using its acidity', False),
                     ('Digests proteins into amino acids in the small intestine', False)],
            'q': 'What is the role of bile in digestion?',
            'wrong_explanations': {1: 'Chemical digestion of fats = LIPASE. Bile only emulsifies — a physical process.',
                                   2: 'Bile is ALKALINE, not acidic. HCl in the stomach kills bacteria. Bile actually '
                                      'neutralises the stomach acid.',
                                   3: 'Protein digestion = PROTEASES (pepsin in the stomach, pancreatic proteases in '
                                      'the small intestine). Bile is not a protease.'}},
           {'opts': [('To provide a large surface area for absorbing digested nutrients into the blood', True),
                     ('To produce digestive enzymes for breaking down food', False),
                     ('To neutralise the acid from the stomach', False),
                     ('To store bile before it is released onto food', False)],
            'q': 'Why does the small intestine have villi?',
            'wrong_explanations': {1: 'Digestive enzymes in the small intestine come from the PANCREAS — the villi are '
                                      'for absorption, not enzyme production.',
                                   2: 'Bile neutralises stomach acid — villi are surface-area adaptations for '
                                      'absorption.',
                                   3: 'Bile is stored in the GALL BLADDER, not in villi.'}},
           {'opts': [('The stomach — by the enzyme pepsin in the presence of HCl', True),
                     ('The mouth — by salivary amylase', False),
                     ('The large intestine — by bacteria', False),
                     ('The liver — by bile salts', False)],
            'q': 'Where are proteins first chemically digested?',
            'wrong_explanations': {1: 'Salivary amylase in the mouth digests STARCH, not proteins. Amylase has no '
                                      'effect on protein.',
                                   2: 'Bacteria in the large intestine help break down some fibre but are not the main '
                                      'site of protein digestion.',
                                   3: 'The liver produces bile which emulsifies FATS — bile has no protein-digesting '
                                      'function.'}},
           {'opts': [('Water — from the remaining undigested material', True),
                     ('Glucose — the final stage of carbohydrate absorption', False),
                     ('Amino acids — the final stage of protein absorption', False),
                     ('Fatty acids — the final stage of fat absorption', False)],
            'q': 'What does the large intestine absorb?',
            'wrong_explanations': {1: 'Glucose is absorbed in the SMALL INTESTINE — by the time food reaches the large '
                                      'intestine, glucose has already been absorbed.',
                                   2: 'Amino acids are absorbed in the SMALL INTESTINE — through the villi walls into '
                                      'the blood.',
                                   3: 'Fatty acids and glycerol are absorbed in the SMALL INTESTINE into the lacteals '
                                      '(lymph vessels in villi).'}},
           {'opts': [('Amylase — breaks down starch into maltose', True),
                     ('Pepsin — breaks down proteins', False),
                     ('Lipase — breaks down fats', False),
                     ('Bile — emulsifies fats', False)],
            'q': 'Which enzyme is produced by the salivary glands?',
            'wrong_explanations': {1: 'Pepsin is produced by glandular tissue in the STOMACH WALL — not the salivary '
                                      'glands.',
                                   2: 'Lipase is produced by the PANCREAS — not the salivary glands.',
                                   3: 'Bile is not an enzyme — it is produced by the LIVER and stored in the gall '
                                      'bladder.'}}],
  'rp': "RP4 — Food tests: iodine solution tests for starch (blue-black = positive), Benedict's solution tests for "
        'glucose (brick red = positive), Biuret reagent tests for protein (purple = positive), ethanol emulsion test '
        'for fat (cloudy white = positive).',
  'spec': '4.2.2.1',
  'summary': 'Describe the organs of the digestive system and what happens to food at each stage.',
  'theory': [{'content': 'Food is made up of large, insoluble molecules — starch, proteins and fats — that are too big '
                         'to pass through the wall of the small intestine into the blood.\n'
                         '\n'
                         'Digestion breaks these large molecules into small, soluble ones that CAN be absorbed.\n'
                         '\n'
                         'There are two types of digestion:\n'
                         'MECHANICAL DIGESTION — physical breakdown (chewing, churning). Increases surface area for '
                         'enzymes.\n'
                         'CHEMICAL DIGESTION — enzymes break chemical bonds to produce smaller molecules.',
              'heading': 'Why We Need to Digest Food'},
             {'content': 'Digestion begins in the mouth.\n'
                         '\n'
                         'Teeth physically grind food into smaller pieces — increasing surface area for enzymes to '
                         'work on.\n'
                         '\n'
                         'Salivary glands produce SALIVA, which contains:\n'
                         'Amylase — begins the chemical digestion of starch → maltose (a sugar).\n'
                         'Mucus — lubricates food to make swallowing easier.\n'
                         '\n'
                         'The tongue shapes food into a BOLUS (a soft ball) that is swallowed.\n'
                         '\n'
                         'The OESOPHAGUS is a muscular tube that carries food from the mouth to the stomach using '
                         'waves of muscle contractions called PERISTALSIS.',
              'heading': 'The Mouth'},
             {'content': 'The stomach is a muscular bag that churns food (mechanical digestion) and carries out '
                         'chemical digestion.\n'
                         '\n'
                         'Glandular tissue in the stomach wall produces GASTRIC JUICE, which contains:\n'
                         'Hydrochloric acid (HCl) — makes the stomach very acidic (pH ~2). This KILLS most bacteria in '
                         'food and provides the optimum pH for the enzyme pepsin.\n'
                         'Pepsin (a PROTEASE enzyme) — breaks proteins into shorter chains of amino acids.\n'
                         '\n'
                         'Food stays in the stomach for several hours, slowly being mixed into a liquid called CHYME.\n'
                         '\n'
                         'Chyme is released in small amounts into the small intestine through the pyloric sphincter.',
              'heading': 'The Stomach'},
             {'content': 'The small intestine is the main site of both DIGESTION and ABSORPTION.\n'
                         '\n'
                         'The PANCREAS produces digestive enzymes that are released into the small intestine:\n'
                         'Pancreatic AMYLASE — continues starch → maltose digestion.\n'
                         'Pancreatic PROTEASES — continue breaking proteins → amino acids.\n'
                         'Pancreatic LIPASE — breaks fats → fatty acids + glycerol.\n'
                         '\n'
                         'The LIVER produces BILE, which is stored in the GALL BLADDER and released into the small '
                         'intestine. Bile:\n'
                         'Emulsifies fats — breaks large fat droplets into many small ones, increasing surface area '
                         'for lipase.\n'
                         'Is alkaline — neutralises the stomach acid, creating the correct pH (neutral/alkaline) for '
                         'pancreatic enzymes to work.\n'
                         '\n'
                         'ABSORPTION — digested molecules (glucose, amino acids, fatty acids, glycerol) pass through '
                         'the wall of the small intestine into the blood.\n'
                         '\n'
                         'The small intestine is adapted for absorption with VILLI — finger-like folds that massively '
                         'increase surface area. Villi have:\n'
                         'A large surface area for fast absorption.\n'
                         'Thin walls — only one cell thick — so the diffusion distance is very short.\n'
                         'A rich blood supply — maintains the concentration gradient by constantly removing absorbed '
                         'molecules.',
              'heading': 'The Small Intestine — Digestion and Absorption'},
             {'content': 'By the time food reaches the large intestine, most nutrients have already been absorbed.\n'
                         '\n'
                         'The LARGE INTESTINE absorbs water from the remaining undigested material.\n'
                         '\n'
                         'Too little water absorbed → diarrhoea (watery faeces).\n'
                         'Too much water absorbed → constipation (hard, dry faeces).\n'
                         '\n'
                         'The RECTUM stores faeces (made of undigested fibre, dead cells, bacteria and bile pigments '
                         'which give it the brown colour).\n'
                         '\n'
                         'Faeces are expelled through the ANUS.',
              'heading': 'The Large Intestine, Rectum and Anus'}],
  'title': 'The Digestive System',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Enzymes are DENATURED at high temperatures — NOT killed. They are proteins, not living things. '
                    'You cannot kill a protein. Denaturation means the active site shape is permanently changed. '
                    'Cooling the enzyme down afterwards will NOT bring it back to life — the damage is permanent.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'enzymes',
  'key_note': 'Lock and key: enzyme active site + specific substrate → enzyme-substrate complex → products released → '
              'enzyme reused. Denaturation is permanent — caused by high temperature or extreme pH.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Active site', 'The specific region of an enzyme where the substrate binds'),
                         ('Substrate', "The specific molecule that fits into an enzyme's active site"),
                         ('Enzyme-substrate complex', "Formed when the substrate binds to the enzyme's active site"),
                         ('Denaturation',
                          "Permanent change in the shape of an enzyme's active site — caused by high temperature or "
                          'extreme pH'),
                         ('Optimum temperature', 'The temperature at which an enzyme works at its maximum rate'),
                         ('Lock and key model', 'Explains why each enzyme only works with one specific substrate')],
               'title': 'Match the Enzyme Concept'},
  'quiz': [{'opts': [('It denatures — the active site shape permanently changes and the substrate can no longer bind',
                      True),
                     ('It works faster because higher temperature gives more energy', False),
                     ('It is killed by the heat', False),
                     ('It becomes temporarily inactive but recovers when cooled', False)],
            'q': 'An enzyme is heated to 80°C. What happens to it?',
            'wrong_explanations': {1: 'Above the optimum (~37°C for human enzymes), the rate does increase — but 80°C '
                                      'is far above optimum, causing denaturation, not faster activity.',
                                   2: "Enzymes are proteins, not living organisms — they cannot be 'killed'. "
                                      'Denaturation is the correct term.',
                                   3: 'Denaturation is PERMANENT. Once the active site shape is changed, cooling does '
                                      'NOT restore it.'}},
           {'opts': [('Pepsin works in the stomach where HCl creates pH 2 — the active site shape is optimal at this '
                      'pH',
                      True),
                     ('All enzymes work best at pH 2 — it is the universal optimum', False),
                     ('pH 2 provides more substrate molecules for pepsin to work on', False),
                     ('Pepsin denatures at any pH above 2', False)],
            'q': 'Why does pepsin work best at pH 2?',
            'wrong_explanations': {1: 'Different enzymes have different optimum pH values. Salivary amylase works best '
                                      'at pH 7, pancreatic enzymes at pH 7–8. Only pepsin has an optimum around pH 2.',
                                   2: 'pH does not affect the number of substrate molecules — it affects the SHAPE of '
                                      'the active site.',
                                   3: 'Pepsin can work at a range of acidic pH values — though its optimum is around '
                                      "pH 2. It doesn't instantly denature above pH 2."}},
           {'opts': [("Amylase's active site is shaped to fit starch molecules only — proteins have a different shape "
                      'and cannot bind',
                      True),
                     ('Amylase is only produced in the mouth, where no proteins are found', False),
                     ('Amylase is too small to interact with large protein molecules', False),
                     ('Proteins repel enzymes and cannot form enzyme-substrate complexes', False)],
            'q': 'According to the lock and key model, why can amylase only digest starch — not proteins?',
            'wrong_explanations': {1: 'Amylase is produced in the mouth AND pancreas — it encounters proteins, but its '
                                      "active site shape doesn't match protein structure.",
                                   2: "Enzyme size is not the issue — it's the shape of the ACTIVE SITE that "
                                      'determines which substrate can bind.',
                                   3: "Proteins don't repel enzymes — proteases bind to proteins very effectively. "
                                      "It's specifically amylase whose active site doesn't fit proteins."}},
           {'opts': [('Rate increases — more substrate molecules collide with active sites — until all active sites '
                      'are occupied',
                      True),
                     ('Rate stays the same — substrate concentration does not affect enzyme activity', False),
                     ('Rate decreases — more substrate molecules compete for fewer active sites', False),
                     ('Rate immediately reaches maximum as soon as any substrate is added', False)],
            'q': 'What happens to the rate of an enzyme-catalysed reaction when substrate concentration increases?',
            'wrong_explanations': {1: 'Substrate concentration absolutely affects rate — more substrate = more '
                                      'collisions = faster rate (up to a limit).',
                                   2: "Substrates don't 'compete' — each active site accepts substrate molecules one "
                                      'at a time. More substrate means MORE active sites occupied at any given moment.',
                                   3: 'Rate only reaches maximum when ALL active sites are occupied — the enzyme is '
                                      'then saturated. At low substrate concentrations, many active sites are empty.'}},
           {'opts': [('It is released unchanged and can catalyse another reaction — it is not used up', True),
                     ('It is permanently bonded to the product and cannot be reused', False),
                     ('It is broken down and must be rebuilt before working again', False),
                     ('It loses its active site after each reaction and must reform it', False)],
            'q': 'After an enzyme-catalysed reaction, what happens to the enzyme?',
            'wrong_explanations': {1: 'Enzymes form temporary enzyme-SUBSTRATE complexes — once products are released, '
                                      'the enzyme is free and fully intact.',
                                   2: "Enzymes are not broken down during catalysis — that's what makes them "
                                      'catalysts. They are reused many times.',
                                   3: "Active sites are a permanent part of the enzyme's structure — they reform "
                                      'automatically because the enzyme is unchanged.'}}],
  'rp': 'RP3 — Investigate the effect of pH on the rate of amylase activity. Use iodine solution to test for starch at '
        'regular intervals. Compare time taken to digest starch at different pH values.',
  'spec': '4.2.2.2',
  'summary': 'Explain how enzymes work, how temperature and pH affect them, and describe the lock and key model.',
  'theory': [{'content': 'Enzymes are biological catalysts — proteins that speed up chemical reactions in living '
                         'organisms without being used up in the reaction.\n'
                         '\n'
                         'Without enzymes, many reactions in the body would happen too slowly to sustain life.\n'
                         '\n'
                         'Every enzyme is a protein with a specific 3D shape. Part of this shape forms the ACTIVE SITE '
                         '— a region with a very specific shape that fits only ONE type of molecule (the SUBSTRATE).\n'
                         '\n'
                         'This specificity (one enzyme = one substrate) is explained by the LOCK AND KEY MODEL.',
              'heading': 'What Are Enzymes?'},
             {'content': 'The lock and key model explains enzyme specificity.\n'
                         '\n'
                         'The ENZYME is the lock — its active site has a unique shape.\n'
                         'The SUBSTRATE is the key — only the correctly shaped substrate fits into the active site.\n'
                         '\n'
                         'What happens:\n'
                         "1. The substrate collides with the enzyme's active site.\n"
                         '2. The substrate binds to form an ENZYME-SUBSTRATE COMPLEX.\n'
                         '3. The enzyme catalyses the reaction — substrate is converted into PRODUCTS.\n'
                         '4. Products are released from the active site.\n'
                         '5. The enzyme is UNCHANGED and ready to bind another substrate molecule.\n'
                         '\n'
                         'This is why enzymes are NOT used up — they can be used over and over again.\n'
                         '\n'
                         'Real-life example: amylase (enzyme) has an active site that ONLY fits starch molecules '
                         '(substrate). It will not break down proteins or fats — their shape is different.',
              'heading': 'The Lock and Key Model'},
             {'content': 'Temperature has a huge effect on how fast enzymes work.\n'
                         '\n'
                         'LOW TEMPERATURE (e.g. 10°C):\n'
                         'Particles have less kinetic energy.\n'
                         'Fewer enzyme-substrate collisions per second.\n'
                         'Reaction rate is slow.\n'
                         '\n'
                         'RISING TEMPERATURE:\n'
                         'More kinetic energy → more collisions → more enzyme-substrate complexes formed → faster '
                         'reaction rate.\n'
                         '\n'
                         'OPTIMUM TEMPERATURE:\n'
                         'The temperature at which the enzyme works fastest.\n'
                         'For most human enzymes: approximately 37°C (body temperature).\n'
                         '\n'
                         'ABOVE OPTIMUM TEMPERATURE:\n'
                         'Vibrations in the enzyme become too violent.\n'
                         'The shape of the active site is permanently changed — DENATURATION.\n'
                         'Substrate can no longer fit into the denatured active site.\n'
                         'Reaction rate falls rapidly to zero.\n'
                         '\n'
                         'IMPORTANT: denaturation is PERMANENT. Cooling the enzyme back down does NOT restore its '
                         'activity.',
              'heading': 'Effect of Temperature on Enzyme Activity'},
             {'content': 'Each enzyme also has an OPTIMUM pH — the pH at which it works best.\n'
                         '\n'
                         'PH AWAY FROM THE OPTIMUM:\n'
                         'Changes in pH alter the charges on the amino acids that form the active site.\n'
                         'Hydrogen bonds in the enzyme are disrupted.\n'
                         'The shape of the active site changes.\n'
                         'The substrate no longer fits — enzyme activity decreases.\n'
                         'At extreme pH values, the enzyme DENATURES permanently.\n'
                         '\n'
                         'Different enzymes have different optimum pH values depending on where they work:\n'
                         'Salivary amylase — optimum pH ~7 (neutral — the mouth).\n'
                         'Pepsin — optimum pH ~2 (acidic — the stomach, where HCl is present).\n'
                         'Pancreatic enzymes — optimum pH ~7–8 (neutral to slightly alkaline — small intestine, where '
                         'bile has neutralised the acid).\n'
                         '\n'
                         'This is WHY the body produces acid in the stomach and bile to neutralise it — creating the '
                         'right pH for each enzyme in each location.',
              'heading': 'Effect of pH on Enzyme Activity'},
             {'content': 'Three key factors affect the rate of enzyme-catalysed reactions:\n'
                         '\n'
                         '1. TEMPERATURE — increases rate up to optimum (~37°C for human enzymes), then denaturation '
                         'causes rate to fall sharply.\n'
                         '\n'
                         '2. pH — each enzyme has an optimum pH. Too acidic or too alkaline = active site changes '
                         'shape = slower reaction or denaturation.\n'
                         '\n'
                         '3. SUBSTRATE CONCENTRATION — more substrate molecules = more collisions with enzyme = faster '
                         'rate (up to a point). Once all enzyme active sites are occupied, adding more substrate has '
                         'no effect — the enzyme is saturated.',
              'heading': 'Factors That Affect Enzyme Rate — Summary'}],
  'title': 'Enzymes',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Arteries do NOT always carry oxygenated blood. The PULMONARY ARTERY carries DEOXYGENATED blood '
                    'from the heart to the lungs. Veins do NOT always carry deoxygenated blood — the PULMONARY VEIN '
                    'carries OXYGENATED blood from the lungs to the heart. The rule is: Arteries = Away from heart. '
                    'Veins = to heart. Not about oxygen content.',
  'equations': [],
  'fifas': [],
  'higher': 'Artificial pacemakers correct irregular heart rhythms. Faulty heart valves can be replaced with '
            'biological valves (from pigs or cows) or mechanical valves. Artificial hearts maintain circulation while '
            'waiting for a transplant or during recovery. Students should be able to evaluate the advantages and '
            'disadvantages of drug treatment vs mechanical devices vs transplant for cardiovascular disease.',
  'id': 'heart-blood-vessels',
  'key_note': 'Left ventricle = thickest wall (pumps to whole body). Right ventricle = pumps to lungs only. Arteries: '
              'away, thick walls, high pressure. Veins: to heart, valves, low pressure. Capillaries: one cell thick, '
              'exchange site.',
  'matching': {'instruction': 'Match each structure to what it does.',
               'pairs': [('Left ventricle', 'Pumps oxygenated blood to the whole body via the aorta — thickest walls'),
                         ('Right ventricle', 'Pumps deoxygenated blood to the lungs via the pulmonary artery'),
                         ('Valves', 'Prevent backflow of blood — open and close with pressure changes'),
                         ('Coronary arteries', 'Supply the heart muscle itself with oxygenated blood'),
                         ('Pulmonary vein', 'Carries oxygenated blood FROM the lungs TO the left atrium'),
                         ('Vena cava', 'Carries deoxygenated blood FROM the body TO the right atrium')],
               'title': 'Match the Heart Structure to its Function'},
  'quiz': [{'opts': [('It pumps blood to the whole body — needs much higher pressure than the right ventricle which '
                      'only pumps to the nearby lungs',
                      True),
                     ('It receives more blood than the right ventricle so needs to be stronger', False),
                     ('The left side of the body is larger so the heart must compensate', False),
                     ('The left ventricle contains oxygenated blood which is heavier', False)],
            'q': 'Why does the left ventricle have thicker walls than the right ventricle?',
            'wrong_explanations': {1: 'Both ventricles receive the same volume of blood per beat — the difference is '
                                      'in the distance the blood must be pumped, not the volume.',
                                   2: "Body size has no relationship to heart wall thickness — it's purely about "
                                      'pumping distance and pressure.',
                                   3: 'Oxygenated and deoxygenated blood have essentially the same density — the '
                                      'thickness difference is purely about pressure requirements.'}},
           {'opts': [('Deoxygenated blood — it has just returned from the body and needs to be reoxygenated', True),
                     ('Oxygenated blood — all arteries carry oxygenated blood', False),
                     ('A mixture of oxygenated and deoxygenated blood', False),
                     ('Blood with no red blood cells — only plasma', False)],
            'q': 'The pulmonary artery carries blood from the heart to the lungs. What type of blood does it carry?',
            'wrong_explanations': {1: 'This is the most common mistake in this topic! Arteries carry blood AWAY from '
                                      'the heart — but the pulmonary artery specifically carries deoxygenated blood to '
                                      'be oxygenated in the lungs.',
                                   2: 'Blood in the heart is kept completely separate — left side carries oxygenated, '
                                      'right side carries deoxygenated. There is no mixing.',
                                   3: 'All blood contains red blood cells — plasma alone would have no oxygen-carrying '
                                      'capacity.'}},
           {'opts': [('Blood pressure in veins is low — valves prevent backflow. Arterial pressure is high enough to '
                      'keep blood flowing in the right direction',
                      True),
                     ("Arteries have thicker walls so they don't need valves", False),
                     ('Veins carry deoxygenated blood which needs extra support to flow', False),
                     ('Valves in arteries would slow down the high-pressure blood flow too much', False)],
            'q': 'Why do veins have valves but arteries do not?',
            'wrong_explanations': {1: 'Wall thickness helps arteries withstand pressure — but valves are specifically '
                                      'about preventing BACKFLOW, which is a problem in low-pressure veins, not '
                                      'high-pressure arteries.',
                                   2: 'The oxygen content of blood has nothing to do with the need for valves — the '
                                      'PRESSURE is what matters.',
                                   3: "Valves in veins do slightly slow flow, but that's acceptable — their role is to "
                                      'prevent dangerous backflow in low-pressure vessels.'}},
           {'opts': [('Walls are only one cell thick — very short diffusion distance. Dense network = large surface '
                      'area',
                      True),
                     ('They have the highest blood pressure of all blood vessels', False),
                     ('They carry both oxygenated and deoxygenated blood simultaneously', False),
                     ('They have valves to keep substances moving in one direction', False)],
            'q': 'What makes capillaries efficient at exchanging substances?',
            'wrong_explanations': {1: 'Capillaries have the LOWEST blood pressure — that is why they can be one cell '
                                      'thick without bursting.',
                                   2: 'Capillaries carry either oxygenated or deoxygenated blood depending on location '
                                      '— not both at once.',
                                   3: 'Capillaries have no valves — substances move by DIFFUSION driven by '
                                      'concentration gradients.'}}],
  'rp': None,
  'spec': '4.2.3',
  'summary': 'Describe the structure and function of the heart, the double circulatory system and the three types of '
             'blood vessel.',
  'theory': [{'content': 'Humans have a DOUBLE circulatory system — the blood passes through the heart twice for every '
                         'complete circuit of the body.\n'
                         '\n'
                         'Circuit 1 — PULMONARY CIRCULATION:\n'
                         'Right side of heart → lungs → left side of heart.\n'
                         'Deoxygenated blood is pumped to the lungs to pick up oxygen and lose carbon dioxide.\n'
                         '\n'
                         'Circuit 2 — SYSTEMIC CIRCULATION:\n'
                         'Left side of heart → body organs and tissues → right side of heart.\n'
                         'Oxygenated blood is delivered to all body tissues at high pressure.\n'
                         '\n'
                         'WHY DOUBLE? Having two separate circuits means oxygenated blood is always kept separate from '
                         'deoxygenated blood, and the left side can pump oxygenated blood to the body at high pressure '
                         '— ensuring efficient oxygen delivery to even distant organs.',
              'heading': 'The Double Circulatory System'},
             {'content': 'The heart has FOUR chambers:\n'
                         'Right atrium — receives deoxygenated blood from the body via the VENA CAVA.\n'
                         'Right ventricle — pumps deoxygenated blood to the lungs via the PULMONARY ARTERY.\n'
                         'Left atrium — receives oxygenated blood from the lungs via the PULMONARY VEIN.\n'
                         'Left ventricle — pumps oxygenated blood to the whole body via the AORTA.\n'
                         '\n'
                         'The LEFT VENTRICLE has much thicker, more muscular walls than the right ventricle because it '
                         'must pump blood to the entire body — a much greater distance and requiring much higher '
                         'pressure than the right ventricle (which only pumps to the nearby lungs).\n'
                         '\n'
                         'VALVES prevent blood flowing backwards:\n'
                         'Atrioventricular (AV) valves — between atria and ventricles.\n'
                         'Semilunar valves — in the pulmonary artery and aorta.\n'
                         'Valves open when pressure is higher on one side and snap shut to prevent backflow — this '
                         "creates the 'lub-dub' heart sound.\n"
                         '\n'
                         'The heart is made of CARDIAC MUSCLE — a special type of muscle that contracts and relaxes '
                         'rhythmically, never getting tired.\n'
                         '\n'
                         'The CORONARY ARTERIES supply the heart muscle itself with oxygenated blood. If these are '
                         'blocked, the heart muscle is deprived of oxygen — causing a heart attack.',
              'heading': 'Structure of the Heart'},
             {'content': 'Arteries carry blood AWAY from the heart.\n'
                         '\n'
                         'Key features:\n'
                         'Thick, muscular walls — to withstand the high pressure of blood pumped directly from the '
                         'heart.\n'
                         'Elastic fibres in the walls — stretch as blood surges through with each heartbeat, then '
                         'recoil to maintain smooth blood flow.\n'
                         'Narrow lumen (central channel) — helps maintain high pressure.\n'
                         'NO valves — pressure is high enough to keep blood flowing in the correct direction.\n'
                         '\n'
                         'Most arteries carry oxygenated blood — EXCEPT the PULMONARY ARTERY, which carries '
                         'deoxygenated blood from the right ventricle to the lungs.\n'
                         '\n'
                         'Memory tip: Arteries = Away from heart.',
              'heading': 'Arteries'},
             {'content': 'Veins carry blood TOWARDS the heart.\n'
                         '\n'
                         'Key features:\n'
                         'Thinner walls — blood pressure is much lower in veins (far from the heart).\n'
                         'Wider lumen — accommodates the slower, lower-pressure flow.\n'
                         'VALVES — essential to prevent backflow of blood. Without valves, gravity and low pressure '
                         'would allow blood to pool in the legs and flow backwards.\n'
                         '\n'
                         'Most veins carry deoxygenated blood — EXCEPT the PULMONARY VEIN, which carries oxygenated '
                         'blood from the lungs to the left atrium.\n'
                         '\n'
                         'Memory tip: Veins → towards the heart. Valves in Veins.',
              'heading': 'Veins'},
             {'content': 'Capillaries are the smallest blood vessels — connecting arteries to veins.\n'
                         '\n'
                         'Key features:\n'
                         'Walls are only ONE CELL THICK — the shortest possible diffusion distance.\n'
                         'Very narrow — red blood cells must squeeze through in single file.\n'
                         'Form a dense network throughout all body tissues.\n'
                         'Very large total surface area — maximises exchange.\n'
                         '\n'
                         'At the capillaries, EXCHANGE of substances takes place:\n'
                         'Oxygen and glucose diffuse OUT of the blood into body cells.\n'
                         'Carbon dioxide and waste products diffuse INTO the blood from cells.\n'
                         '\n'
                         'This exchange happens by DIFFUSION down concentration gradients — no energy required.',
              'heading': 'Capillaries'}],
  'title': 'The Heart and Blood Vessels',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Red blood cells carry oxygen — white blood cells do NOT carry oxygen. White blood cells fight '
                    'infection. Platelets are NOT cells — they are cell fragments with no nucleus. They are involved '
                    'in clotting, NOT in carrying oxygen or fighting infection.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'blood',
  'key_note': 'Red blood cells: O₂ transport, haemoglobin, no nucleus, biconcave. White blood cells: immune defence — '
              'phagocytes engulf, lymphocytes make antibodies. Platelets: clotting. Plasma: liquid transport medium.',
  'matching': {'instruction': 'Match each blood component to its primary role.',
               'pairs': [('Red blood cells', 'Carry oxygen using haemoglobin — biconcave disc, no nucleus'),
                         ('Phagocytes', 'Engulf and destroy pathogens — non-specific immune defence'),
                         ('Lymphocytes', 'Produce specific antibodies that match pathogen antigens'),
                         ('Platelets', 'Involved in blood clotting — form a fibrin mesh to seal wounds'),
                         ('Plasma', 'Liquid that transports glucose, CO₂, urea, hormones and heat')],
               'title': 'Match the Blood Component to its Function'},
  'quiz': [{'opts': [('To create more space for haemoglobin — allowing the cell to carry more oxygen', True),
                     ('So they can divide and replace themselves when worn out', False),
                     ('To reduce their weight so they flow faster through blood vessels', False),
                     ('So they can squeeze through capillaries more easily', False)],
            'q': 'Why do red blood cells have no nucleus?',
            'wrong_explanations': {1: 'Cells without a nucleus CANNOT divide — red blood cells are produced in bone '
                                      'marrow and cannot reproduce themselves.',
                                   2: 'Weight difference between a nucleus and haemoglobin molecules is negligible — '
                                      'the primary reason is space for haemoglobin.',
                                   3: 'Flexibility helps red blood cells squeeze through capillaries — but this is a '
                                      'result of their biconcave shape and flexibility, not the absence of a '
                                      'nucleus.'}},
           {'opts': [('Unable to produce specific antibodies — prolonged or repeated infections that are hard to clear',
                      True),
                     ('Unable to carry oxygen — severe anaemia', False),
                     ('Blood will not clot properly — excessive bleeding from wounds', False),
                     ('Unable to digest food properly — nutrients not absorbed', False)],
            'q': 'A patient has very few lymphocytes. What is the most likely consequence?',
            'wrong_explanations': {1: 'Oxygen carrying = RED BLOOD CELLS using haemoglobin. Lymphocytes are white '
                                      'blood cells.',
                                   2: 'Blood clotting = PLATELETS forming a fibrin mesh. Lymphocytes produce '
                                      'antibodies, not clotting factors.',
                                   3: 'Food digestion = digestive enzymes in the gut. Lymphocytes are part of the '
                                      'immune system.'}},
           {'opts': [('Blood clotting — they clump at wound sites and trigger fibrin mesh formation to seal the damage',
                      True),
                     ('Carrying oxygen from the lungs to body tissues', False),
                     ('Producing antibodies to fight specific pathogens', False),
                     ('Engulfing and digesting bacteria by phagocytosis', False)],
            'q': 'What is the role of platelets in the body?',
            'wrong_explanations': {1: 'Oxygen transport = RED BLOOD CELLS using haemoglobin.',
                                   2: 'Producing antibodies = LYMPHOCYTES (a type of white blood cell).',
                                   3: 'Engulfing bacteria = PHAGOCYTES (a type of white blood cell).'}},
           {'opts': [('Oxygen — this is carried by haemoglobin inside red blood cells', True),
                     ('Glucose from the small intestine to body cells', False),
                     ('Urea from the liver to the kidneys', False),
                     ('Carbon dioxide from respiring cells to the lungs', False)],
            'q': 'Which substance does plasma NOT transport?',
            'wrong_explanations': {1: 'Glucose IS carried in plasma — after absorption from the small intestine.',
                                   2: 'Urea IS carried in plasma — from the liver to the kidneys for excretion.',
                                   3: 'Carbon dioxide IS dissolved in plasma — most CO₂ travels as bicarbonate ions '
                                      'dissolved in plasma.'}}],
  'rp': None,
  'spec': '4.2.3.2',
  'summary': 'Describe the four components of blood and the function of each.',
  'theory': [{'content': 'Blood is a connective tissue — a liquid tissue that flows through blood vessels.\n'
                         '\n'
                         'It has four main components:\n'
                         '1. Red blood cells (erythrocytes)\n'
                         '2. White blood cells (leucocytes)\n'
                         '3. Platelets\n'
                         '4. Plasma\n'
                         '\n'
                         'Each component has a distinct and essential function. Together they transport substances, '
                         "defend against disease and maintain the body's internal environment.",
              'heading': 'Blood — A Tissue'},
             {'content': 'Red blood cells carry OXYGEN from the lungs to all body tissues.\n'
                         '\n'
                         'They are uniquely adapted for this function:\n'
                         'BICONCAVE DISC SHAPE — increases surface area for oxygen absorption and releases carbon '
                         'dioxide. The thin centre reduces the diffusion distance for gas exchange.\n'
                         'NO NUCLEUS — the nucleus is lost as red blood cells mature. This creates more space for '
                         'HAEMOGLOBIN — the protein that binds and carries oxygen.\n'
                         'Packed with HAEMOGLOBIN — each red blood cell contains ~270 million haemoglobin molecules.\n'
                         'FLEXIBLE — can squeeze through narrow capillaries without tearing.\n'
                         '\n'
                         'In the lungs, haemoglobin binds to oxygen (forming oxyhaemoglobin) where oxygen '
                         'concentration is high.\n'
                         'In body tissues, oxyhaemoglobin releases oxygen where concentration is low.\n'
                         '\n'
                         'Red blood cells are made in the bone marrow and last about 120 days before being broken down '
                         'in the spleen.',
              'heading': 'Red Blood Cells'},
             {'content': 'White blood cells are part of the IMMUNE SYSTEM — they defend the body against pathogens.\n'
                         '\n'
                         'Unlike red blood cells, white blood cells have a nucleus.\n'
                         '\n'
                         'There are two main types:\n'
                         '\n'
                         'PHAGOCYTES:\n'
                         'Engulf and destroy pathogens by PHAGOCYTOSIS — the cell membrane wraps around the pathogen '
                         'and pulls it inside where enzymes digest it.\n'
                         'Non-specific — they attack any pathogen they encounter.\n'
                         'Respond quickly — first responders at an infection site.\n'
                         '\n'
                         'LYMPHOCYTES:\n'
                         'Produce ANTIBODIES — proteins with a specific shape that binds to ANTIGENS on the surface of '
                         'a specific pathogen.\n'
                         'One lymphocyte produces ONE type of antibody for ONE specific antigen.\n'
                         'Antigens are molecules on the surface of pathogens that the immune system recognises as '
                         'foreign.\n'
                         'After infection, MEMORY LYMPHOCYTES remain in the blood for years or for life — if the same '
                         'pathogen invades again, a rapid, large-scale antibody response destroys it before it can '
                         'cause disease. This is the basis of IMMUNITY.',
              'heading': 'White Blood Cells'},
             {'content': 'Platelets are tiny cell FRAGMENTS — they are not complete cells and have no nucleus.\n'
                         '\n'
                         'When a blood vessel is damaged, platelets are involved in BLOOD CLOTTING:\n'
                         '1. Platelets are activated and clump together at the wound site.\n'
                         '2. A series of chemical reactions produces FIBRIN — a protein that forms a mesh of fibres.\n'
                         '3. Red blood cells are trapped in the fibrin mesh → a CLOT forms.\n'
                         '4. The clot dries to form a SCAB — sealing the wound, preventing blood loss and stopping '
                         'pathogens from entering.\n'
                         '\n'
                         'Without platelets, even a small cut could lead to dangerous blood loss and open infection.',
              'heading': 'Platelets'},
             {'content': 'Plasma is the pale yellow LIQUID component of blood — it makes up about 55% of blood '
                         'volume.\n'
                         '\n'
                         'Plasma transports almost everything in the blood:\n'
                         'Digested food molecules — glucose and amino acids from the small intestine to cells.\n'
                         'Carbon dioxide — from respiring cells to the lungs.\n'
                         'Urea — from the liver (where it is made) to the kidneys (where it is excreted in urine).\n'
                         'Hormones — from endocrine glands to their target organs.\n'
                         'Antibodies — produced by lymphocytes, carried to infection sites.\n'
                         'Heat — distributes warmth from active muscles to cooler parts of the body, helping regulate '
                         'body temperature.',
              'heading': 'Plasma'}],
  'title': 'Blood',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'A STENT holds a narrowed artery open — it does NOT bypass the blockage. A BYPASS SURGERY creates '
                    'a new route around the blockage using a grafted blood vessel. Students often confuse these two '
                    'treatments.',
  'equations': [],
  'fifas': [],
  'higher': 'Statins lower LDL cholesterol — slowing fatty deposit formation in arteries. Stents keep coronary '
            'arteries open mechanically. Bypass surgery grafts a vessel (usually from the leg) around the blockage. '
            'Heart transplants replace the whole heart — require immunosuppression. Artificial hearts provide '
            'temporary support. Faulty valves can be replaced with biological or mechanical alternatives. Each '
            'treatment has risks (surgery complications, rejection, infection) and benefits to evaluate.',
  'id': 'coronary-heart-disease',
  'key_note': 'CHD = narrowed coronary arteries (atherosclerosis/plaques). Risk factors: smoking, high cholesterol, '
              'high blood pressure, poor diet, lack of exercise. Treatments: statins (lower cholesterol), stents (hold '
              'artery open), bypass surgery (reroute blood).',
  'matching': {'instruction': 'Match each treatment to its mechanism.',
               'pairs': [('Statins', 'Drugs that lower LDL cholesterol in the blood — slow plaque formation'),
                         ('Stent', 'Metal mesh tube inserted into a narrowed artery to hold it open'),
                         ('Bypass surgery', 'Grafts a healthy blood vessel around the blocked coronary artery'),
                         ('Heart transplant', 'Replaces the diseased heart — last resort, risk of rejection')],
               'title': 'Match the CHD Treatment to How it Works'},
  'quiz': [{'opts': [('Fatty plaques (atherosclerosis) build up in the coronary arteries, narrowing them and reducing '
                      'blood flow to the heart muscle',
                      True),
                     ('The heart muscle becomes too weak to pump blood effectively due to overuse', False),
                     ('Blood becomes too thick and cannot flow through the coronary arteries', False),
                     ('The coronary arteries grow too narrow naturally with age', False)],
            'q': 'What causes coronary heart disease?',
            'wrong_explanations': {1: 'Heart muscle weakness (heart failure) is a consequence of CHD, not the cause — '
                                      'the cause is specifically fatty plaque build-up.',
                                   2: 'Blood viscosity can affect flow, but CHD is specifically about PLAQUE build-up '
                                      'in artery walls, not blood thickness.',
                                   3: "Arteries don't naturally narrow with age — they narrow because of PLAQUES "
                                      '(fatty deposits) accumulating over time due to risk factors.'}},
           {'opts': [('It is inserted into the narrowed artery and expands to hold it open — restoring blood flow',
                      True),
                     ('It dissolves the fatty plaques blocking the artery', False),
                     ('It reroutes blood around the blocked artery using a grafted vessel', False),
                     ('It lowers blood cholesterol levels to prevent further plaque formation', False)],
            'q': 'How does a stent treat coronary heart disease?',
            'wrong_explanations': {1: 'Stents do not dissolve plaques — they physically hold the narrowed artery open.',
                                   2: 'Rerouting blood around a blockage using a grafted vessel = BYPASS SURGERY, not '
                                      'a stent.',
                                   3: 'Lowering cholesterol = STATINS (medication), not a stent.'}},
           {'opts': [('Smoking cigarettes', True),
                     ('Family history of heart disease (genetics)', False),
                     ('Being male', False),
                     ('Increasing age', False)],
            'q': 'Which of the following is a lifestyle risk factor for CHD that CAN be changed?',
            'wrong_explanations': {1: 'Genetics is a risk factor — but you cannot change your DNA. It is a '
                                      'non-modifiable risk factor.',
                                   2: 'Sex (being male) slightly increases CHD risk, particularly at younger ages — '
                                      'but you cannot change this.',
                                   3: 'Age increases CHD risk, but everyone ages — you cannot avoid this risk '
                                      'factor.'}}],
  'rp': None,
  'spec': '4.2.3.3',
  'summary': 'Describe the causes and treatments of coronary heart disease.',
  'theory': [{'content': 'Coronary heart disease (CHD) is a condition in which the CORONARY ARTERIES — the blood '
                         'vessels that supply the heart muscle itself with oxygen and glucose — become narrowed and '
                         'partially or completely blocked.\n'
                         '\n'
                         'The heart muscle is always active, always respiring — it needs a continuous supply of '
                         'oxygen. If this supply is reduced or cut off, the heart muscle cannot function properly.\n'
                         '\n'
                         'CHD is one of the leading causes of death in the UK and worldwide.',
              'heading': 'What is Coronary Heart Disease?'},
             {'content': 'CHD develops through a process called ATHEROSCLEROSIS:\n'
                         '\n'
                         '1. Over many years, fatty substances (mainly cholesterol) build up in the walls of the '
                         'coronary arteries.\n'
                         '2. These fatty deposits are called PLAQUES or ATHEROMAS.\n'
                         '3. The plaques harden over time, making artery walls less elastic.\n'
                         '4. The lumen (central channel) of the artery becomes progressively NARROWER.\n'
                         '5. Blood flow to the heart muscle is reduced.\n'
                         '6. If a plaque ruptures, a BLOOD CLOT can form at that site — this can completely block the '
                         'artery.\n'
                         '\n'
                         'Complete blockage = HEART ATTACK. The heart muscle supplied by that artery receives no '
                         'oxygen and begins to die. This causes severe chest pain, shortness of breath and can be '
                         'fatal.',
              'heading': 'How CHD Develops — Atherosclerosis'},
             {'content': 'Several factors increase the risk of developing CHD:\n'
                         '\n'
                         'LIFESTYLE FACTORS (can be changed):\n'
                         'SMOKING — carbon monoxide damages artery walls; nicotine increases heart rate and blood '
                         'pressure.\n'
                         'HIGH BLOOD CHOLESTEROL — excess cholesterol deposits in artery walls forming plaques.\n'
                         'HIGH BLOOD PRESSURE — damages artery walls, making them more susceptible to plaque '
                         'formation.\n'
                         'POOR DIET — high in saturated fats and salt raises cholesterol and blood pressure.\n'
                         'LACK OF EXERCISE — physical activity strengthens the heart and helps control weight and '
                         'cholesterol.\n'
                         'OBESITY — associated with high blood pressure, high cholesterol and type 2 diabetes.\n'
                         '\n'
                         'NON-LIFESTYLE FACTORS (cannot be changed):\n'
                         'GENETICS — family history of CHD significantly increases risk.\n'
                         'AGE — risk increases with age as arteries gradually narrow.\n'
                         'SEX — males tend to develop CHD at younger ages than females (though risk equalises after '
                         'menopause).',
              'heading': 'Risk Factors for CHD'},
             {'content': 'Several treatments can reduce the effects of CHD:\n'
                         '\n'
                         'STATINS (medication):\n'
                         'Drugs that reduce the level of LDL cholesterol in the blood.\n'
                         'Slows the build-up of plaques in arteries.\n'
                         'Taken daily — can significantly reduce heart attack and stroke risk.\n'
                         'Side effects: muscle pain in some patients.\n'
                         '\n'
                         'STENTS (surgical):\n'
                         'A small metal mesh tube inserted into a narrowed coronary artery.\n'
                         'Holds the artery open, restoring blood flow.\n'
                         'Inserted during a procedure called angioplasty — a thin tube is passed through a blood '
                         'vessel to the narrowed area.\n'
                         'Effective but does not treat the underlying cause.\n'
                         '\n'
                         'BYPASS SURGERY:\n'
                         'A healthy blood vessel from another part of the body (e.g. leg vein) is grafted around the '
                         'blocked section of coronary artery.\n'
                         'Creates a new route for blood to reach the heart muscle.\n'
                         'Major surgery with risks, but effective for severe blockages.\n'
                         '\n'
                         'HEART TRANSPLANT:\n'
                         'Replacing the entire diseased heart with a donor heart.\n'
                         'Last resort for severe heart failure.\n'
                         'Risks: immune rejection, waiting time for a suitable donor.\n'
                         'Patient must take immunosuppressant drugs for life to prevent rejection.',
              'heading': 'Treatments for CHD'}],
  'title': 'Coronary Heart Disease',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'A risk factor INCREASES the probability of getting a disease — it does NOT mean you WILL get it. '
                    'A non-smoker can develop lung cancer; a heavy smoker might not. Risk factors change the '
                    'statistical likelihood, not the certainty. Also — correlation does NOT always mean causation, '
                    'though for many lifestyle risk factors, both have been established.',
  'equations': [],
  'fifas': [],
  'higher': 'Students should be able to evaluate the evidence that links lifestyle factors (smoking, obesity, alcohol, '
            'diet) to non-communicable disease. Correlation does not prove causation — consider confounding variables. '
            'Some risk factors are non-modifiable (genetics, age) while others are modifiable (lifestyle). Statistical '
            'analysis of large population data provides the strongest evidence.',
  'id': 'health-disease',
  'key_note': 'Communicable = caused by pathogens, can spread. Non-communicable = cannot spread, often '
              'lifestyle-related. Risk factors: lifestyle (smoking, diet, alcohol), environmental (UV, pollution), '
              'genetic. Risk factor = increased probability, NOT certainty.',
  'matching': {'instruction': 'Sort each disease into communicable or non-communicable.',
               'pairs': [('Communicable', 'Influenza — caused by a virus, spread by droplets'),
                         ('Non-communicable', 'Coronary heart disease — caused by lifestyle factors and genetics'),
                         ('Communicable', 'Tuberculosis (TB) — caused by bacteria, spread by airborne droplets'),
                         ('Non-communicable', 'Type 2 diabetes — linked to obesity and diet, cannot be spread'),
                         ('Communicable', 'Malaria — caused by Plasmodium protist, spread by mosquito'),
                         ('Non-communicable', 'Skin cancer — caused by UV radiation, not spread between people')],
               'title': 'Communicable or Non-Communicable?'},
  'quiz': [{'opts': [('Communicable diseases are caused by pathogens and can spread between organisms. '
                      'Non-communicable diseases cannot spread.',
                      True),
                     ('Communicable diseases are always fatal. Non-communicable diseases are always mild.', False),
                     ('Communicable diseases are caused by lifestyle. Non-communicable diseases are caused by '
                      'pathogens.',
                      False),
                     ('They are the same thing — both terms describe infectious disease.', False)],
            'q': 'What is the difference between a communicable and a non-communicable disease?',
            'wrong_explanations': {1: 'Neither type is always fatal or always mild — severity varies enormously in '
                                      'both categories.',
                                   2: 'This is exactly the wrong way round. Communicable = pathogens. Non-communicable '
                                      '= lifestyle, genetics, environment.',
                                   3: 'They are not the same — the key difference is whether the disease can be spread '
                                      'from person to person.'}},
           {'opts': [('A correlation between red meat consumption and bowel cancer — further research is needed to '
                      'establish causation',
                      True),
                     ('Red meat DEFINITELY causes bowel cancer in everyone who eats it', False),
                     ('Bowel cancer causes people to eat more red meat', False),
                     ('This is meaningless data — correlations in diet studies are never reliable', False)],
            'q': 'A study finds that people who eat more red meat have higher rates of bowel cancer. What does this '
                 'show?',
            'wrong_explanations': {1: 'Correlation does not automatically mean causation — the relationship could be '
                                      'due to other factors (e.g. diet quality overall, exercise levels).',
                                   2: 'This would be reverse causation — the data shows a link, but the disease '
                                      "developing before changing diet doesn't fit the timeline.",
                                   3: 'Epidemiological (population-based) data is valuable scientific evidence — '
                                      'correlation studies are an important first step in identifying risk factors.'}},
           {'opts': [('Smoking cigarettes', True),
                     ('Being 70 years old', False),
                     ('Having a family history of heart disease', False),
                     ('Living near a motorway (air pollution)', False)],
            'q': 'Which of the following is a LIFESTYLE risk factor for non-communicable disease?',
            'wrong_explanations': {1: 'Age is a NON-LIFESTYLE (non-modifiable) risk factor — everyone ages and it '
                                      'cannot be changed.',
                                   2: 'Family history = GENETIC risk factor — also non-modifiable. You cannot choose '
                                      'your genes.',
                                   3: 'Living near a motorway = ENVIRONMENTAL risk factor — though this can sometimes '
                                      'be changed (by moving), it is generally classified as environmental rather than '
                                      'lifestyle.'}}],
  'rp': None,
  'spec': '4.2.4',
  'summary': 'Define health and disease, distinguish communicable from non-communicable diseases, and explain risk '
             'factors.',
  'theory': [{'content': 'The World Health Organisation (WHO) defines health as:\n'
                         "'A state of complete physical, mental and social wellbeing — not merely the absence of "
                         "disease or infirmity.'\n"
                         '\n'
                         'This definition is important because it highlights that health is about more than just not '
                         'being ill. A person can be free of physical disease but still be unhealthy if they have poor '
                         'mental health or are isolated from society.\n'
                         '\n'
                         'Good health requires:\n'
                         'Physical wellbeing — the body functions properly, free from disease.\n'
                         'Mental wellbeing — good emotional and psychological state.\n'
                         'Social wellbeing — positive relationships and a functioning role in society.',
              'heading': 'Defining Health'},
             {'content': 'A disease is a condition that impairs the normal functioning of the body.\n'
                         '\n'
                         'COMMUNICABLE DISEASES (infectious):\n'
                         'Caused by pathogens — bacteria, viruses, fungi, protists.\n'
                         'Can be spread from one organism to another.\n'
                         'Examples: influenza, HIV, tuberculosis (TB), measles, malaria, salmonella food poisoning.\n'
                         '\n'
                         'NON-COMMUNICABLE DISEASES (non-infectious):\n'
                         'Cannot be spread from person to person.\n'
                         'Typically caused by genetic factors, lifestyle choices or environmental exposure.\n'
                         'Examples: coronary heart disease, type 2 diabetes, most cancers, asthma.\n'
                         '\n'
                         'Interactions between diseases: having one disease can affect the risk of developing another. '
                         'For example:\n'
                         'HIV weakens the immune system → patient more vulnerable to other infections.\n'
                         'Cancer treatment (chemotherapy) suppresses immunity → risk of other infections increases.\n'
                         'Diabetes increases risk of cardiovascular disease.',
              'heading': 'Types of Disease'},
             {'content': 'A risk factor is anything that increases the probability of developing a disease — but does '
                         'NOT guarantee it.\n'
                         '\n'
                         'There is an important distinction:\n'
                         'CORRELATION — a statistical link between a risk factor and a disease.\n'
                         'CAUSATION — evidence that the risk factor directly CAUSES the disease.\n'
                         '\n'
                         'Many risk factors show strong correlation with disease AND have been shown to cause disease '
                         'through scientific study (e.g. smoking and lung cancer).\n'
                         '\n'
                         'Others show correlation but causation is harder to prove.\n'
                         '\n'
                         'Risk factors can be:\n'
                         'LIFESTYLE FACTORS (choices): smoking, diet, alcohol consumption, physical inactivity.\n'
                         'ENVIRONMENTAL FACTORS: air pollution, UV radiation, exposure to chemicals or asbestos.\n'
                         'GENETIC FACTORS: inherited predispositions to certain diseases.',
              'heading': 'Risk Factors'},
             {'content': 'Non-communicable diseases are increasingly common in wealthy countries — often linked to '
                         'lifestyle choices.\n'
                         '\n'
                         'Key links between lifestyle and non-communicable disease:\n'
                         '\n'
                         'SMOKING:\n'
                         'Strongly linked to lung cancer, mouth cancer, throat cancer, bladder cancer.\n'
                         'Also linked to coronary heart disease and chronic obstructive pulmonary disease (COPD).\n'
                         '\n'
                         'ALCOHOL:\n'
                         'Excessive alcohol linked to liver disease (cirrhosis), liver cancer, mouth cancer, brain '
                         'damage.\n'
                         'Increases risk of accidents and mental health problems.\n'
                         '\n'
                         'POOR DIET:\n'
                         'High saturated fat diet → high cholesterol → increased CHD risk.\n'
                         'High sugar diet → type 2 diabetes, obesity.\n'
                         'Low fibre diet → increased bowel cancer risk.\n'
                         '\n'
                         'LACK OF EXERCISE:\n'
                         'Increases risk of obesity, CHD, type 2 diabetes, some cancers.\n'
                         '\n'
                         'OBESITY (BMI > 30):\n'
                         'Strongly linked to type 2 diabetes, CHD, high blood pressure, some cancers.\n'
                         '\n'
                         'UV RADIATION (from sunlight/sunbeds):\n'
                         'Causes skin cancer (including melanoma — the most dangerous type).',
              'heading': 'Non-Communicable Disease and Lifestyle'}],
  'title': 'Health, Disease and Risk Factors',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'BENIGN tumours stay in one place and are not cancer. MALIGNANT tumours spread (metastasis) and '
                    "are cancer. Students often use 'tumour' and 'cancer' interchangeably — a benign tumour is NOT "
                    "cancer. Also: chemotherapy targets ALL rapidly dividing cells, not just cancer cells — that's why "
                    'it causes hair loss and immune suppression as side effects.',
  'equations': [],
  'fifas': [],
  'higher': 'Benign tumours remain localised and are not cancerous. Malignant tumours invade surrounding tissue and '
            'metastasise (spread via blood or lymph). Risk factors include lifestyle (smoking→ lung/mouth/bladder '
            'cancer; alcohol→ liver cancer; UV→ skin cancer), environmental (asbestos→ mesothelioma) and genetic '
            '(BRCA1/2 mutations increase breast/ovarian cancer risk). Chemotherapy and radiotherapy both target '
            'rapidly dividing cells — explaining their side effects on healthy tissues.',
  'id': 'cancer',
  'key_note': 'Cancer = uncontrolled cell division caused by mutations in regulatory genes. Benign = stays put, not '
              'cancerous. Malignant = spreads via blood/lymph (metastasis) = cancer. Treatments: surgery, radiotherapy '
              '(gamma rays), chemotherapy (drugs).',
  'matching': {'instruction': 'Sort each description into benign tumour or malignant tumour.',
               'pairs': [('Benign tumour', 'Grows in one place — stays enclosed, does not invade surrounding tissues'),
                         ('Malignant tumour',
                          'Cells break away and travel through blood or lymph to form new tumours — metastasis'),
                         ('Benign tumour', 'Usually not life-threatening — often removed by surgery'),
                         ('Malignant tumour', 'Much harder to treat once it has spread to other organs'),
                         ('Both', 'Caused by uncontrolled cell division due to gene mutation')],
               'title': 'Benign or Malignant?'},
  'quiz': [{'opts': [('Benign tumours stay in one place. Malignant tumours spread to other parts of the body '
                      '(metastasis).',
                      True),
                     ('Benign tumours grow faster than malignant tumours.', False),
                     ('Malignant tumours are caused by lifestyle; benign tumours are genetic.', False),
                     ('Benign tumours require chemotherapy; malignant tumours only need surgery.', False)],
            'q': 'What is the key difference between a benign and a malignant tumour?',
            'wrong_explanations': {1: 'Malignant tumours typically grow FASTER and spread — benign tumours tend to '
                                      'grow more slowly and stay localised.',
                                   2: 'Both types can have genetic or lifestyle causes — the distinction is about '
                                      'whether the tumour SPREADS, not its cause.',
                                   3: 'This is the wrong way round — surgery is often used for localised (benign or '
                                      'early malignant) tumours. Chemotherapy is used for cancer that has spread.'}},
           {'opts': [('UV radiation damages DNA in skin cells — causing mutations in genes that control cell division',
                      True),
                     ('UV radiation directly kills healthy skin cells, forcing the body to replace them rapidly',
                      False),
                     ('UV radiation heats skin cells above their optimum temperature, causing them to mutate', False),
                     ("UV radiation reduces the immune system's ability to detect and destroy abnormal cells", False)],
            'q': 'How does UV radiation cause skin cancer?',
            'wrong_explanations': {1: "UV radiation doesn't kill healthy cells en masse — it damages DNA specifically. "
                                      'Rapid replacement due to damage is related to wound healing, not cancer.',
                                   2: "UV radiation doesn't work by heat — it carries photons that directly interact "
                                      'with and damage DNA molecules.',
                                   3: 'UV radiation can slightly suppress immunity, but the primary cancer-causing '
                                      'mechanism is direct DNA mutation in skin cells.'}},
           {'opts': [('Chemotherapy targets all rapidly dividing cells — hair follicle cells divide rapidly, so they '
                      'are also damaged',
                      True),
                     ('Chemotherapy drugs are toxic to the scalp skin only', False),
                     ('The immune system attacks hair follicles as a reaction to chemotherapy drugs', False),
                     ('Chemotherapy only causes hair loss when combined with radiotherapy', False)],
            'q': 'Why does chemotherapy cause hair loss as a side effect?',
            'wrong_explanations': {1: 'Chemotherapy drugs are not scalp-specific — they circulate in the blood and '
                                      'affect rapidly dividing cells throughout the whole body.',
                                   2: "The immune reaction to chemotherapy doesn't specifically target hair follicles "
                                      '— the damage is from the drugs directly targeting dividing cells.',
                                   3: 'Hair loss can occur from chemotherapy alone — it is caused by the drug '
                                      'mechanism, not only in combination with radiotherapy.'}}],
  'rp': None,
  'spec': '4.2.4.1',
  'summary': 'Explain how cancer develops, the difference between benign and malignant tumours, and how cancer is '
             'treated.',
  'theory': [{'content': 'Cancer is a disease caused by UNCONTROLLED CELL DIVISION.\n'
                         '\n'
                         'Normally, cell division is carefully regulated by genes that control the cell cycle — '
                         'telling cells when to divide and when to stop.\n'
                         '\n'
                         'Cancer begins when MUTATIONS occur in these regulatory genes:\n'
                         "The 'stop dividing' signals are ignored.\n"
                         'Cells keep dividing repeatedly, producing more and more abnormal cells.\n'
                         'A mass of cells — called a TUMOUR — accumulates.\n'
                         '\n'
                         'Cancers can develop in almost any tissue of the body. Common types include: breast cancer, '
                         'lung cancer, bowel cancer, prostate cancer, skin cancer (melanoma).',
              'heading': 'What is Cancer?'},
             {'content': 'Not all tumours are cancerous. There are two types:\n'
                         '\n'
                         'BENIGN TUMOUR:\n'
                         'Grows slowly and stays in ONE PLACE.\n'
                         'Does not invade surrounding tissues.\n'
                         'Cells remain enclosed in a capsule.\n'
                         'Does not spread to other parts of the body.\n'
                         'Usually not life-threatening — can often be removed by surgery.\n'
                         'Can cause problems if it presses on a vital structure (e.g. a benign brain tumour pressing '
                         'on important brain regions).\n'
                         '\n'
                         'MALIGNANT TUMOUR (CANCER):\n'
                         'Grows quickly and INVADES surrounding tissues.\n'
                         'Cells break away from the original tumour.\n'
                         'Travel through the BLOOD or LYMPH system.\n'
                         'Settle in other organs and form NEW TUMOURS — this spread is called METASTASIS.\n'
                         'Much harder to treat once it has spread.\n'
                         'Malignant tumours are the dangerous, life-threatening form.',
              'heading': 'Benign vs Malignant Tumours'},
             {'content': 'Several factors increase the risk of developing cancer:\n'
                         '\n'
                         'LIFESTYLE RISK FACTORS:\n'
                         'Smoking — strongly linked to lung cancer, mouth cancer, throat cancer, bladder cancer. '
                         'Carcinogens in tobacco smoke damage DNA in cells.\n'
                         'Alcohol — linked to liver cancer, mouth and throat cancer.\n'
                         'Obesity — associated with bowel cancer, breast cancer, uterine cancer.\n'
                         'Poor diet — low fibre linked to bowel cancer; processed meat linked to bowel cancer.\n'
                         '\n'
                         'ENVIRONMENTAL RISK FACTORS:\n'
                         'UV radiation — sunlight and sunbeds cause skin cancer by damaging DNA in skin cells.\n'
                         'Ionising radiation — X-rays, gamma rays and nuclear radiation can damage DNA.\n'
                         'Asbestos — fibres lodge in lung tissue and damage cells → mesothelioma (lung cancer).\n'
                         'Certain chemicals — industrial carcinogens.\n'
                         '\n'
                         'GENETIC RISK FACTORS:\n'
                         'Some people inherit mutations in tumour suppressor genes (e.g. BRCA1/2 gene mutations '
                         'increase breast and ovarian cancer risk).\n'
                         'Having a family history of certain cancers increases personal risk.\n'
                         '\n'
                         'VIRAL RISK FACTORS:\n'
                         'HPV (Human Papillomavirus) — causes most cases of cervical cancer.\n'
                         'Hepatitis B and C viruses — linked to liver cancer.',
              'heading': 'Risk Factors for Cancer'},
             {'content': 'Cancer is treated using several approaches, often in combination:\n'
                         '\n'
                         'SURGERY:\n'
                         'Physical removal of the tumour.\n'
                         'Effective for localised (non-metastatic) tumours.\n'
                         'Cannot remove cancer that has spread throughout the body.\n'
                         '\n'
                         'RADIOTHERAPY:\n'
                         'High-energy radiation (gamma rays or X-rays) is directed at tumour cells.\n'
                         'Damages the DNA of cancer cells → they cannot divide → they die.\n'
                         'Side effects: damages healthy cells near the tumour, causing fatigue, nausea, hair loss in '
                         'the treatment area.\n'
                         '\n'
                         'CHEMOTHERAPY:\n'
                         'Drugs that target rapidly dividing cells — killing cancer cells.\n'
                         'Can reach cancer cells throughout the body, useful for metastatic cancer.\n'
                         'Side effects: also damages rapidly dividing HEALTHY cells (hair follicles, gut lining, bone '
                         'marrow) — causing hair loss, nausea, immune suppression.',
              'heading': 'Treatment of Cancer'}],
  'title': 'Cancer',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Xylem transports WATER and MINERALS. Phloem transports SUGARS. Students regularly mix these up. A '
                    'good memory trick: Xylem = water (X for H2O is a stretch, but think: Xylem goes up like water). '
                    'Phloem = food (sugars). Also: xylem cells are DEAD; phloem cells are LIVING.',
  'equations': [],
  'fifas': [],
  'higher': 'The transpiration stream is driven by evaporation from leaves — creating a tension that pulls water '
            'continuously up through xylem (cohesion-tension theory). Students should be able to explain how the '
            'transpiration rate is measured using a potometer. Phloem translocation is driven by active loading of '
            'sucrose at source cells (using ATP from companion cells) creating a pressure gradient to sink cells.',
  'id': 'plant-tissues',
  'key_note': 'Xylem: water + minerals, upwards only, dead cells, lignified walls. Phloem: sugars (translocation), '
              'both directions, living cells. Stomata: CO₂ in, O₂ and water vapour out. Controlled by guard cells.',
  'matching': {'instruction': 'Match each tissue to its role in the plant.',
               'pairs': [('Xylem', 'Transports water and mineral ions from roots to leaves — dead, hollow, lignified'),
                         ('Phloem', 'Transports dissolved sugars from leaves to the rest of the plant — translocation'),
                         ('Palisade mesophyll',
                          'Packed with chloroplasts near leaf surface — main site of photosynthesis'),
                         ('Spongy mesophyll', 'Air spaces between cells — allows CO₂ and O₂ to diffuse easily'),
                         ('Guard cells',
                          'Control opening and closing of stomata — regulate gas exchange and water loss'),
                         ('Waxy cuticle', 'Waterproof covering on epidermis — reduces water loss from the leaf')],
               'title': 'Match the Plant Tissue to its Function'},
  'quiz': [{'opts': [('Water and dissolved mineral ions — upwards from roots to leaves', True),
                     ('Dissolved sugars from leaves to other parts of the plant', False),
                     ('Oxygen produced by photosynthesis', False),
                     ('Carbon dioxide for use in photosynthesis', False)],
            'q': 'What is transported in xylem?',
            'wrong_explanations': {1: 'Dissolved sugars = PHLOEM (translocation). Xylem carries water and minerals '
                                      'only.',
                                   2: 'Oxygen diffuses through air spaces in the spongy mesophyll and out through '
                                      "stomata — it doesn't travel in xylem.",
                                   3: "CO₂ diffuses through stomata into air spaces — it doesn't travel in xylem."}},
           {'opts': [('Dead cells have no contents — forming a completely hollow tube for water to flow through '
                      'without obstruction',
                      True),
                     ('Xylem cells die because the lignin in their walls is toxic', False),
                     ('Dead cells are lighter, helping water move upwards against gravity', False),
                     ('Xylem cells die when the plant is no longer growing', False)],
            'q': 'Why are xylem cells dead?',
            'wrong_explanations': {1: 'Lignin is not toxic — it strengthens the walls. The cells die as part of their '
                                      'normal development, leaving behind a hollow lignified tube.',
                                   2: "Dead cell content doesn't significantly change the weight of xylem — water "
                                      'moves upward due to the transpiration pull, not because of weight.',
                                   3: 'Xylem cells die as they mature during normal development, regardless of whether '
                                      'the plant is actively growing — this is a programmed developmental process.'}},
           {'opts': [('Allow CO₂ in for photosynthesis and O₂ out — also allow water vapour to escape during '
                      'transpiration',
                      True),
                     ('Absorb water directly from the air into the leaf', False),
                     ('Produce the waxy cuticle to reduce water loss', False),
                     ('Store glucose produced by photosynthesis', False)],
            'q': 'What is the role of stomata in leaves?',
            'wrong_explanations': {1: 'Stomata can absorb some water vapour in humid conditions, but their primary '
                                      'function is gas EXCHANGE, not water absorption.',
                                   2: 'The waxy cuticle is produced by the EPIDERMIS cells — it is a secreted layer, '
                                      'not produced by stomata.',
                                   3: 'Glucose storage as starch happens in chloroplasts and other cells — stomata are '
                                      'pores for gas exchange.'}}],
  'rp': None,
  'spec': '4.2.5',
  'summary': 'Describe the tissues found in plant organs and how they are adapted to their functions.',
  'theory': [{'content': 'Plants are multicellular organisms with specialised organs, just like animals.\n'
                         '\n'
                         'The main plant organs are:\n'
                         'LEAF — the main site of photosynthesis and gas exchange.\n'
                         'STEM — provides support and transports substances between roots and leaves.\n'
                         'ROOT — anchors the plant and absorbs water and mineral ions from the soil.\n'
                         'FLOWER — involved in reproduction.\n'
                         '\n'
                         'Each organ is made of different types of TISSUE, each adapted to its specific function.',
              'heading': 'Plant Organs'},
             {'content': 'The leaf is the most important organ for photosynthesis. It contains several specialised '
                         'tissues:\n'
                         '\n'
                         'EPIDERMIS (upper and lower):\n'
                         'A thin, transparent layer covering the leaf surface.\n'
                         'Produces a WAXY CUTICLE — a waterproof coating that reduces water loss by evaporation.\n'
                         '\n'
                         'PALISADE MESOPHYLL:\n'
                         'Found in the upper part of the leaf — closest to sunlight.\n'
                         'Cells are tall and column-shaped, packed with many CHLOROPLASTS.\n'
                         'This is the main site of photosynthesis — receives maximum light.\n'
                         '\n'
                         'SPONGY MESOPHYLL:\n'
                         'Below the palisade layer.\n'
                         'Cells are loosely arranged with large AIR SPACES between them.\n'
                         'Air spaces allow CO₂ to diffuse easily to photosynthesising cells.\n'
                         'Also allows O₂ produced by photosynthesis to diffuse out.\n'
                         '\n'
                         'GUARD CELLS and STOMATA:\n'
                         'Guard cells are pairs of cells surrounding tiny pores called STOMATA (singular: stoma) on '
                         'the lower leaf surface.\n'
                         'Stomata open to allow CO₂ in for photosynthesis and O₂ out — also allow water vapour to '
                         'escape (transpiration).\n'
                         'Guard cells control stomata opening: in the light, guard cells absorb water and become '
                         'turgid → stomata OPEN. In the dark or when dehydrated, guard cells lose water → stomata '
                         'CLOSE.\n'
                         '\n'
                         'XYLEM and PHLOEM:\n'
                         'Run through the leaf as vascular bundles (veins).\n'
                         'Xylem brings water to the leaf. Phloem takes away sugars made by photosynthesis.',
              'heading': 'Tissues in the Leaf'},
             {'content': 'Xylem is a tissue that transports WATER and dissolved MINERAL IONS from the roots upwards to '
                         'the leaves.\n'
                         '\n'
                         'Key features of xylem cells:\n'
                         'DEAD cells — no cytoplasm or nucleus, forming a completely hollow tube.\n'
                         'No end walls — cells are stacked end-to-end to form one continuous open column.\n'
                         'Walls strengthened with LIGNIN — a hard, waterproof material that makes xylem very strong '
                         'and prevents the tubes from collapsing.\n'
                         'Water moves through xylem in one direction only — upwards.\n'
                         '\n'
                         'The movement of water through xylem is driven by the TRANSPIRATION STREAM — water '
                         'evaporating from leaves creates a pulling force that draws water up from the roots.',
              'heading': 'Xylem Tissue'},
             {'content': 'Phloem is a tissue that transports dissolved SUGARS (mainly sucrose) from leaves to other '
                         'parts of the plant. This process is called TRANSLOCATION.\n'
                         '\n'
                         'Key features of phloem cells:\n'
                         'LIVING cells — unlike xylem, phloem cells are alive.\n'
                         'SIEVE TUBES — cells with perforated end walls (sieve plates) that allow sugar solution to '
                         'flow through.\n'
                         'COMPANION CELLS — next to each sieve tube cell, providing energy (ATP) for the active '
                         'loading of sugars into the phloem.\n'
                         '\n'
                         'Sugars travel in BOTH DIRECTIONS in phloem — from leaves (source) to roots, growing tips, '
                         'fruits and other areas where sugar is needed (sinks).',
              'heading': 'Phloem Tissue'}],
  'title': 'Plant Tissues and Organs',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Transpiration is fastest in HOT, BRIGHT, DRY and WINDY conditions. Students often get humidity '
                    'wrong — LOW humidity means DRY air which INCREASES transpiration rate (bigger concentration '
                    'gradient for water vapour). HIGH humidity SLOWS transpiration. Think of it like this: dry air '
                    "'pulls' the water out of the leaf faster.",
  'equations': [],
  'fifas': [],
  'higher': 'Investigating transpiration: use a potometer to measure water uptake (indicative of transpiration). Vary '
            'one factor (temperature, humidity, light intensity, wind speed) while controlling others. Record distance '
            'air bubble moves per unit time. Calculate rate and plot a graph. Students should be able to design and '
            'evaluate such an investigation.',
  'id': 'transpiration',
  'key_note': 'Transpiration: water evaporates from stomata → transpiration pull draws water up xylem from roots. '
              'Fastest in: high temperature, high light intensity, low humidity, high wind. Measured with a potometer.',
  'matching': {'instruction': 'Sort each condition — does it increase or decrease the rate of transpiration?',
               'pairs': [('Increases transpiration', 'High temperature — more kinetic energy, faster evaporation'),
                         ('Increases transpiration', 'Bright light — stomata open wider, more water vapour escapes'),
                         ('Increases transpiration',
                          'Low humidity (dry air) — steep concentration gradient for water vapour'),
                         ('Increases transpiration',
                          'Wind — blows away moist air near stomata, maintains steep gradient'),
                         ('Decreases transpiration', 'High humidity — gradient between leaf and air is reduced'),
                         ('Decreases transpiration', 'Darkness — stomata close, water vapour cannot escape')],
               'title': 'Does this Speed Up or Slow Down Transpiration?'},
  'quiz': [{'opts': [('The evaporation of water from the leaves of a plant through the stomata', True),
                     ('The transport of dissolved sugars from leaves to the rest of the plant', False),
                     ('The absorption of water by root hair cells from the soil', False),
                     ('The process of photosynthesis producing water as a product', False)],
            'q': 'What is transpiration?',
            'wrong_explanations': {1: 'Transport of dissolved sugars = TRANSLOCATION (in phloem). Transpiration is '
                                      'specifically water evaporation from leaves.',
                                   2: 'Water absorption by roots = OSMOSIS through root hair cells. Transpiration is '
                                      'what happens at the LEAVES end.',
                                   3: 'Photosynthesis produces OXYGEN, not water — water is a REACTANT of '
                                      'photosynthesis (6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂).'}},
           {'opts': [('Transpiration increases significantly — lower humidity and wind both increase the rate', True),
                     ('Transpiration decreases — the plant closes its stomata to conserve water', False),
                     ('Transpiration stays the same — the two factors cancel each other out', False),
                     ('Transpiration increases due to humidity but decreases due to wind — net effect is zero', False)],
            'q': 'A plant is moved from a humid greenhouse to a dry, windy environment. What happens to its '
                 'transpiration rate?',
            'wrong_explanations': {1: 'The plant may eventually close stomata if it loses too much water — but the '
                                      'immediate effect of moving to dry, windy conditions is faster transpiration. '
                                      'Stomata closing is a response to stress, not an immediate automatic reaction.',
                                   2: "The two factors don't cancel out — both low humidity AND wind INCREASE "
                                      'transpiration rate. They act in the same direction.',
                                   3: 'Both low humidity and wind INCREASE transpiration — humidity and wind both '
                                      'affect the concentration gradient for water vapour in the same way (they both '
                                      'maintain a steep gradient).'}},
           {'opts': [('Brighter light causes stomata to open wider — allowing more water vapour to escape', True),
                     ('Brighter light increases the temperature of the leaf, causing faster evaporation', False),
                     ('Brighter light increases the rate of photosynthesis, which produces more water', False),
                     ('Brighter light makes chlorophyll absorb water directly from the air', False)],
            'q': 'Why do plants transpire faster in brighter light?',
            'wrong_explanations': {1: 'Brighter light does warm leaves slightly — but the PRIMARY mechanism is guard '
                                      'cells responding to light by opening stomata wider.',
                                   2: 'Photosynthesis uses water as a REACTANT — it consumes water, not produces it. '
                                      'Oxygen is the gas product.',
                                   3: 'Chlorophyll absorbs LIGHT energy — it does not absorb water from the air.'}}],
  'rp': None,
  'spec': '4.2.5.2',
  'summary': 'Describe transpiration and the factors that affect its rate.',
  'theory': [{'content': 'Transpiration is the evaporation of water from the leaves (and other aerial parts) of a '
                         'plant.\n'
                         '\n'
                         'Water is absorbed by roots → travels up the stem through xylem → reaches the leaves → '
                         'evaporates through stomata as water vapour into the atmosphere.\n'
                         '\n'
                         'This continuous movement of water from roots to leaves through the xylem is called the '
                         'TRANSPIRATION STREAM.\n'
                         '\n'
                         'How it works: as water evaporates from leaf cells into the air spaces and out through '
                         'stomata, the cells become slightly drier → they absorb water from neighbouring cells by '
                         'osmosis → this creates a pulling force that draws water up through the xylem all the way '
                         'from the roots.\n'
                         '\n'
                         'This pull is called TRANSPIRATION PULL — it works because water molecules are attracted to '
                         'each other (cohesion) and to the xylem walls (adhesion), forming a continuous column of '
                         'water.',
              'heading': 'What is Transpiration?'},
             {'content': 'Transpiration serves several important functions:\n'
                         '\n'
                         'WATER SUPPLY — transports water from roots to leaves where it is needed for photosynthesis.\n'
                         '\n'
                         'MINERAL TRANSPORT — mineral ions dissolved in water are carried up from the roots to the '
                         'leaves.\n'
                         '\n'
                         'COOLING — evaporation of water from leaf surfaces has a cooling effect — similar to sweating '
                         'in humans.\n'
                         '\n'
                         'However, too much transpiration is a problem — excessive water loss can cause wilting and '
                         'ultimately death. Plants have several adaptations to reduce water loss (waxy cuticle, '
                         'closing stomata, reduced leaf surface area in dry environments).',
              'heading': 'Why Transpiration Matters'},
             {'content': 'Four main factors affect how fast water evaporates from leaves:\n'
                         '\n'
                         '1. TEMPERATURE:\n'
                         'Higher temperature → more kinetic energy → water molecules evaporate faster from leaf '
                         'surface → steeper concentration gradient between leaf and air → faster transpiration.\n'
                         '\n'
                         '2. LIGHT INTENSITY:\n'
                         'Brighter light → stomata open WIDER to allow more CO₂ in for photosynthesis → more water '
                         'vapour can escape → faster transpiration.\n'
                         'In the dark, stomata close → transpiration almost stops.\n'
                         '\n'
                         '3. HUMIDITY:\n'
                         'Low humidity (dry air) → large difference in water vapour concentration between inside the '
                         'leaf and outside → steep diffusion gradient → faster transpiration.\n'
                         'High humidity (moist air) → gradient is smaller → slower transpiration.\n'
                         '\n'
                         '4. AIR MOVEMENT / WIND:\n'
                         'Wind blows away water vapour that has accumulated near the stomata → prevents the air near '
                         'the leaf becoming saturated → maintains a steep diffusion gradient → faster transpiration.\n'
                         'In still air, a layer of moist air builds up around the leaf → reduces the gradient → slows '
                         'transpiration.',
              'heading': 'Factors That Increase the Rate of Transpiration'},
             {'content': 'A POTOMETER is an apparatus used to measure the rate of water uptake by a plant shoot — used '
                         'as an indicator of transpiration rate.\n'
                         '\n'
                         'How it works:\n'
                         'A leafy shoot is placed in a sealed tube of water with a capillary tube attached.\n'
                         'As the plant transpires and takes up water, an air bubble in the capillary tube moves '
                         'towards the plant.\n'
                         'The DISTANCE the bubble moves per unit time = rate of water uptake.\n'
                         '\n'
                         'The potometer measures water UPTAKE, not transpiration directly — but the two are closely '
                         'related.\n'
                         '\n'
                         'You can investigate the effect of each environmental factor by:\n'
                         'Changing temperature (place near heater or in cold room).\n'
                         'Changing light intensity (move lamp closer/further).\n'
                         'Changing humidity (blow dry air at the plant or enclose in moist environment).\n'
                         'Changing air movement (use a fan).',
              'heading': 'Measuring Transpiration — The Potometer'}],
  'title': 'Transpiration',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Translocation = SUGARS in PHLOEM. Transpiration = WATER in XYLEM. These are the two most commonly '
                    'confused terms in plant biology. Translocation moves in BOTH directions — transpiration only goes '
                    'UPWARDS. Phloem cells are LIVING — xylem cells are DEAD.',
  'equations': [],
  'fifas': [],
  'higher': 'Active loading of sucrose into phloem sieve tubes at source cells (leaves) requires ATP from companion '
            'cells. This creates high osmotic pressure — water enters by osmosis from adjacent xylem, increasing '
            'hydrostatic pressure. The pressure gradient drives sucrose solution toward sink cells (roots, fruits, '
            'growing tips) where sucrose is actively unloaded — maintaining the gradient.',
  'id': 'translocation',
  'key_note': 'Translocation: sucrose in phloem, source (leaves) to sink (roots, fruits, tips), both directions, '
              'living cells, uses ATP. NOT the same as transpiration (water in xylem, upwards only, dead cells, '
              'passive).',
  'matching': {'instruction': 'Sort each statement into transpiration or translocation.',
               'pairs': [('Transpiration', 'Water moves up through xylem from roots to leaves — pulled by evaporation'),
                         ('Translocation', 'Sucrose moves through phloem from leaves to growing roots and fruits'),
                         ('Transpiration', 'Involves dead, hollow, lignified cells'),
                         ('Translocation', 'Can move substances both upwards and downwards in the plant'),
                         ('Transpiration', 'Rate increases in hot, bright, dry and windy conditions'),
                         ('Translocation', 'Requires ATP energy — companion cells supply energy to sieve tubes')],
               'title': 'Transpiration or Translocation?'},
  'quiz': [{'opts': [('Sucrose (dissolved sugar) — from leaves to other parts of the plant', True),
                     ('Water and dissolved mineral ions — from roots to leaves', False),
                     ('Oxygen produced by photosynthesis', False),
                     ('Carbon dioxide for use in photosynthesis', False)],
            'q': 'What is the main substance transported in phloem?',
            'wrong_explanations': {1: 'Water and minerals = XYLEM transport (transpiration stream). Phloem carries '
                                      'sugars.',
                                   2: 'Oxygen diffuses through air spaces and out through stomata — it is not '
                                      'transported in phloem.',
                                   3: 'CO₂ diffuses through stomata into the leaf — it is not transported in phloem.'}},
           {'opts': [('Both upwards and downwards — from source (leaves) to any sink where sugar is needed', True),
                     ('Upwards only — like the transpiration stream in xylem', False),
                     ('Downwards only — gravity pulls the sugar solution down to the roots', False),
                     ('Outwards only — from the centre of the stem to the leaf surfaces', False)],
            'q': 'In which direction does translocation move?',
            'wrong_explanations': {1: 'Upwards only = TRANSPIRATION in XYLEM. Translocation in phloem moves in both '
                                      'directions depending on where the sink is.',
                                   2: 'If translocation were downwards only, growing shoot tips at the top of the '
                                      'plant could never receive sugars — but they clearly do.',
                                   3: 'Translocation moves along the length of the plant (up and down), not outwards '
                                      'from centre to leaf surface.'}},
           {'opts': [('Any part of the plant where sugars are used or stored — e.g. roots, fruits, growing tips', True),
                     ('The leaves — where sugars are produced by photosynthesis', False),
                     ('The phloem vessels that transport sugars through the plant', False),
                     ('The stomata — where water and gases are exchanged', False)],
            'q': "What is a 'sink' in the context of translocation?",
            'wrong_explanations': {1: 'The leaves are the SOURCE — where sugars are MADE. A sink is the DESTINATION '
                                      'where sugars are used or stored.',
                                   2: 'The phloem is the VESSEL — not the destination. Sinks are the organs that USE '
                                      'or STORE the sugars.',
                                   3: 'Stomata are gas exchange pores — they have no role in the source-sink '
                                      'relationship of translocation.'}}],
  'rp': None,
  'spec': '4.2.5.3',
  'summary': 'Describe translocation and how it differs from transpiration.',
  'theory': [{'content': 'Translocation is the transport of dissolved SUGARS (mainly SUCROSE) through the PHLOEM from '
                         'where they are produced to where they are needed or stored.\n'
                         '\n'
                         'Source → Sink:\n'
                         'SOURCE — the place where sugars are made or released (mainly the LEAVES, where '
                         'photosynthesis takes place).\n'
                         'SINK — any place where sugars are used or stored:\n'
                         'Growing shoot tips — sugars needed for cell division and growth.\n'
                         'Roots — sugars needed for respiration and converted to starch for storage.\n'
                         'Fruits and seeds — sugars needed for development.\n'
                         'Flowers — sugars needed for reproduction.\n'
                         '\n'
                         'Unlike the transpiration stream, translocation can move sugars in BOTH DIRECTIONS in the '
                         'phloem — up to growing tips AND down to roots and storage organs.',
              'heading': 'What is Translocation?'},
             {'content': 'Sucrose is ACTIVELY LOADED into phloem sieve tubes at the source (leaves) using energy (ATP) '
                         'from companion cells.\n'
                         '\n'
                         'This creates a high concentration of sucrose in the phloem at the source end.\n'
                         '\n'
                         "Water enters the phloem by osmosis (moving from xylem, where it's more dilute) → increases "
                         'pressure at the source end.\n'
                         '\n'
                         'This pressure drives the flow of sugar solution THROUGH the phloem towards the sink.\n'
                         '\n'
                         'At the sink, sucrose is actively UNLOADED from the phloem and used or converted to starch '
                         'for storage.\n'
                         '\n'
                         'This reduces the concentration at the sink end, maintaining the pressure difference and '
                         'keeping the flow going.',
              'heading': 'How Translocation Works'},
             {'content': 'Students often confuse these two transport processes. Here is a clear comparison:\n'
                         '\n'
                         'TRANSPIRATION:\n'
                         'Substance moved: WATER (and dissolved minerals)\n'
                         'Vessel: XYLEM\n'
                         'Direction: UPWARDS ONLY (roots → leaves)\n'
                         'Cells: DEAD cells\n'
                         'Driving force: evaporation from leaves creating transpiration pull\n'
                         'Energy: PASSIVE (no ATP needed)\n'
                         '\n'
                         'TRANSLOCATION:\n'
                         'Substance moved: SUGARS (sucrose)\n'
                         'Vessel: PHLOEM\n'
                         'Direction: BOTH DIRECTIONS (source → sink)\n'
                         'Cells: LIVING cells\n'
                         'Driving force: active loading of sucrose creates pressure\n'
                         'Energy: ACTIVE (ATP required to load/unload sucrose)',
              'heading': 'Transpiration vs Translocation — Key Differences'}],
  'title': 'Translocation',
  'triple_only': None,
  'variables': []}],

"infection-response": [{'common_mistake': "Antibiotics kill BACTERIA only — they have absolutely NO effect on viruses. Never say 'take "
                    "antibiotics for a virus'. Flu is caused by a virus — antibiotics will not help. Also: phagocytes "
                    'ENGULF pathogens. Lymphocytes PRODUCE ANTIBODIES. These are different white blood cells with '
                    'different jobs.',
  'equations': [],
  'fifas': [],
  'higher': 'The secondary immune response is faster and larger than the primary — memory B-cells rapidly '
            'differentiate into plasma cells producing large quantities of specific antibodies. This is the basis of '
            'vaccination and acquired immunity. Students should be able to explain how memory cells allow rapid '
            'response on re-exposure to a specific pathogen.',
  'id': 'communicable-diseases-defence',
  'key_note': 'Physical barriers: skin, mucus, cilia, stomach acid — first line of defence. Phagocytes: engulf and '
              'destroy (non-specific). Lymphocytes: make specific antibodies. Memory cells: rapid response on '
              're-infection = immunity.',
  'matching': {'instruction': 'Match each defence mechanism to its correct description.',
               'pairs': [('Skin', 'Physical barrier — prevents pathogens entering the body as long as it is unbroken'),
                         ('Cilia', 'Sweep mucus with trapped pathogens upwards towards the throat'),
                         ('Stomach acid', 'pH ~2 — kills most pathogens that are swallowed'),
                         ('Phagocytes', 'Engulf and digest pathogens — non-specific immune defence'),
                         ('Lymphocytes', 'Produce specific antibodies that bind to pathogen antigens'),
                         ('Memory cells',
                          'Remain after infection — allow rapid antibody response if same pathogen returns')],
               'title': 'Match the Defence to How it Works'},
  'quiz': [{'opts': [('Phagocytes engulf pathogens non-specifically. Lymphocytes produce specific antibodies.', True),
                     ('Phagocytes produce antibodies. Lymphocytes engulf pathogens.', False),
                     ('Both engulf pathogens — they are the same type of white blood cell.', False),
                     ('Phagocytes fight bacterial infections only. Lymphocytes fight viral infections only.', False)],
            'q': 'What is the difference between a phagocyte and a lymphocyte?',
            'wrong_explanations': {1: 'This is exactly the wrong way around. Phagocytes = engulf. Lymphocytes = '
                                      'antibodies.',
                                   2: 'Both are white blood cells but they have completely different functions — '
                                      'phagocytes engulf, lymphocytes make antibodies.',
                                   3: 'Both types of white blood cell work against a wide range of pathogens — they '
                                      'are not limited to one type of infection.'}},
           {'opts': [('They remain in the blood after infection and allow a rapid, large antibody response if the same '
                      'pathogen is encountered again',
                      True),
                     ('They physically block pathogens from entering the bloodstream', False),
                     ('They produce antibiotics to destroy bacterial infections', False),
                     ('They replace damaged body cells after an infection has passed', False)],
            'q': 'Why are memory cells important for immunity?',
            'wrong_explanations': {1: "Memory cells are immune cells — they don't form physical barriers. That role "
                                      'belongs to skin, mucus and cilia.',
                                   2: 'Antibiotics are medicines — they are not produced by any body cells. Memory '
                                      'cells produce antibodies, not antibiotics.',
                                   3: 'Cell replacement is done by stem cells and normal cell division — memory cells '
                                      'specifically remember and respond to specific pathogens.'}},
           {'opts': [('It is a vector — it carries the Plasmodium protist and injects it into humans when it bites',
                      True),
                     ('The mosquito itself causes malaria — it is the pathogen', False),
                     ('Mosquito bites break the skin, allowing malaria bacteria from the air to enter', False),
                     ('The mosquito contaminates water sources with Plasmodium', False)],
            'q': 'How does the Anopheles mosquito spread malaria?',
            'wrong_explanations': {1: 'The MOSQUITO is the vector — Plasmodium is the pathogen. The mosquito carries '
                                      'and transmits Plasmodium but does not cause the disease itself.',
                                   2: 'Malaria is caused by a PROTIST (Plasmodium) — not bacteria. And it is injected '
                                      'through the bite, not from the air.',
                                   3: 'Malaria is transmitted through bites — not through water. Cholera spreads '
                                      'through contaminated water.'}},
           {'opts': [('To trap inhaled pathogens and particles before they reach the lungs — cilia then sweep the '
                      'mucus up to be swallowed',
                      True),
                     ('To provide a moist surface for gas exchange in the lungs', False),
                     ('To produce antibodies that neutralise pathogens in the airways', False),
                     ('To prevent the airways from drying out in cold weather', False)],
            'q': 'Why does the body produce mucus in the airways?',
            'wrong_explanations': {1: 'Gas exchange occurs in the ALVEOLI — the main function of mucus in the airways '
                                      'is trapping pathogens, not gas exchange.',
                                   2: 'Antibodies are produced by LYMPHOCYTES in the blood — not by mucus. Mucus is a '
                                      'physical/chemical barrier.',
                                   3: 'Moisture in the airways is a secondary benefit — the PRIMARY function of mucus '
                                      'is trapping pathogens and particles.'}}],
  'rp': None,
  'spec': '4.3.1',
  'summary': 'Describe what communicable diseases are, how pathogens spread and how the body defends itself.',
  'theory': [{'content': 'A communicable disease (also called an infectious disease) is one caused by a PATHOGEN — a '
                         'microorganism that infects and harms the host.\n'
                         '\n'
                         'Communicable diseases can be SPREAD from one organism to another — either directly or '
                         'through a vector (a carrier organism like a mosquito).\n'
                         '\n'
                         'There are four main types of pathogen:\n'
                         'BACTERIA — single-celled prokaryotes. Reproduce rapidly by binary fission inside the body. '
                         'Cause disease mainly by producing TOXINS. Examples: Salmonella, Gonorrhoea, Tuberculosis.\n'
                         "VIRUSES — not true cells. Much smaller than bacteria. Enter host cells and use the cell's "
                         'machinery to replicate, destroying the host cell in the process. Examples: Measles, HIV, '
                         'Influenza, TMV.\n'
                         "FUNGI — eukaryotic organisms. Grow on or in host tissue. Examples: Athlete's foot, Rose "
                         'black spot.\n'
                         'PROTISTS — single-celled eukaryotes. Examples: Plasmodium (causes malaria).',
              'heading': 'What is a Communicable Disease?'},
             {'content': 'Pathogens use different routes to move from one host to another:\n'
                         '\n'
                         'AIRBORNE DROPLETS — coughing, sneezing, talking release tiny droplets containing pathogens. '
                         'Examples: influenza, measles, COVID-19, tuberculosis.\n'
                         '\n'
                         'CONTAMINATED WATER — drinking or bathing in water containing pathogens. Example: cholera '
                         '(bacteria), typhoid.\n'
                         '\n'
                         'DIRECT CONTACT — skin contact, sexual contact, touching contaminated surfaces. Examples: '
                         "athlete's foot (skin contact), gonorrhoea (sexual contact), rose black spot (plant "
                         'contact).\n'
                         '\n'
                         "VECTORS — an organism that carries the pathogen but doesn't cause the disease itself. "
                         'Example: Anopheles mosquito carries Plasmodium (malaria) and injects it when it bites.\n'
                         '\n'
                         'CONTAMINATED FOOD — eating food containing pathogens. Example: Salmonella in undercooked '
                         'poultry.\n'
                         '\n'
                         'BLOOD CONTACT — sharing needles, transfusions. Example: HIV, Hepatitis B.',
              'heading': 'How Pathogens Spread'},
             {'content': 'The body has several lines of defence against pathogens — the first line stops pathogens '
                         'from entering at all.\n'
                         '\n'
                         'SKIN — a tough, continuous physical barrier. As long as the skin is unbroken, most pathogens '
                         'cannot pass through it. The skin also produces slightly acidic secretions that inhibit '
                         'bacterial growth.\n'
                         '\n'
                         'MUCUS — goblet cells in the lining of the airways, nose and throat produce sticky mucus. '
                         'Pathogens and particles breathed in get trapped in this mucus before they can reach the '
                         'lungs.\n'
                         '\n'
                         'CILIA — tiny hair-like structures on the cells lining the trachea and bronchi. They beat '
                         'rhythmically, sweeping the mucus (with trapped pathogens) upwards towards the throat where '
                         'it is swallowed. The stomach acid then kills any pathogens.\n'
                         '\n'
                         'STOMACH ACID — hydrochloric acid (HCl) in the stomach is very acidic (pH ~2). Most pathogens '
                         'that are swallowed are killed here before they can cause infection.',
              'heading': "The Body's Physical and Chemical Barriers"},
             {'content': 'If pathogens get past the physical barriers, the IMMUNE SYSTEM takes over.\n'
                         '\n'
                         'PHAGOCYTES:\n'
                         'These are white blood cells that carry out PHAGOCYTOSIS — they identify and engulf (eat) '
                         'pathogens.\n'
                         'The cell membrane wraps around the pathogen and pulls it inside the cell.\n'
                         'Enzymes inside the phagocyte then digest and destroy it.\n'
                         'Phagocytes are NON-SPECIFIC — they attack any pathogen they encounter without needing to '
                         'learn its identity first.\n'
                         '\n'
                         'LYMPHOCYTES:\n'
                         'These white blood cells produce ANTIBODIES — proteins with a specific shape that binds to '
                         'ANTIGENS on the surface of a particular pathogen.\n'
                         'Each lymphocyte makes ONE type of antibody for ONE specific antigen.\n'
                         'Antigens are molecules on the surface of pathogens that the immune system identifies as '
                         'foreign.\n'
                         'Antibodies can neutralise pathogens, mark them for destruction, or cause them to clump '
                         'together.\n'
                         'After an infection, MEMORY CELLS remain in the blood for years or for life.\n'
                         'If the same pathogen invades again, memory cells rapidly produce large quantities of '
                         'antibodies — destroying the pathogen before it causes disease. This is IMMUNITY.',
              'heading': 'The Immune System — White Blood Cells'}],
  'title': 'Communicable Diseases and Human Defence Systems',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'HIV and AIDS are NOT the same thing. HIV is the VIRUS. AIDS is the CONDITION that develops when '
                    'HIV has destroyed enough lymphocytes that the immune system collapses. You can have HIV for many '
                    'years without having AIDS if treated with ARVs. Also: antibiotics DO NOT treat viral infections — '
                    'not measles, not HIV, not flu.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'viral-diseases',
  'key_note': 'Measles: droplets, rash + fever, MMR vaccine prevents it. HIV: bodily fluids, destroys lymphocytes → '
              'AIDS, managed with ARVs. TMV: plant virus, mosaic leaf pattern, reduced photosynthesis.',
  'matching': {'instruction': 'Match each disease to its transmission route and key symptom.',
               'pairs': [('Measles', 'Airborne droplets — red skin rash and high fever — prevented by MMR vaccine'),
                         ('HIV', 'Bodily fluids — destroys T-lymphocytes — eventually causes AIDS'),
                         ('Tobacco mosaic virus',
                          'Contact/tools — mosaic discolouration of leaves — reduced photosynthesis')],
               'title': 'Match the Viral Disease to its Key Features'},
  'quiz': [{'opts': [('HIV destroys T-lymphocytes — the immune system becomes too weak to fight off infections', True),
                     ('HIV produces toxins that directly damage all organs simultaneously', False),
                     ('HIV causes the body to overproduce white blood cells, overwhelming the system', False),
                     ('HIV converts into the AIDS virus after several years in the body', False)],
            'q': 'Why does HIV lead to AIDS?',
            'wrong_explanations': {1: "HIV specifically targets immune cells — it doesn't produce toxins that damage "
                                      'other organs directly.',
                                   2: 'HIV destroys white blood cells (lymphocytes) — it does not cause '
                                      'overproduction.',
                                   3: "HIV doesn't 'convert' into AIDS — AIDS is the CONDITION resulting from immune "
                                      'system collapse caused by HIV destroying lymphocytes.'}},
           {'opts': [('It disrupts chlorophyll production — leaves develop mosaic discolouration and photosynthesise '
                      'less efficiently',
                      True),
                     ('It blocks the xylem, preventing water reaching the leaves', False),
                     ('It causes root cells to die, so the plant cannot absorb minerals', False),
                     ('It produces toxins that kill plant cells directly', False)],
            'q': 'How does tobacco mosaic virus affect plant growth?',
            'wrong_explanations': {1: 'TMV affects leaf cells and chlorophyll — not the xylem. The reduced '
                                      'photosynthesis from less chlorophyll is the key effect.',
                                   2: 'TMV infects leaf cells, not root cells. Mineral absorption is unaffected '
                                      'directly.',
                                   3: "TMV disrupts chlorophyll production in leaf cells — it doesn't produce toxins "
                                      'that kill cells outright.'}},
           {'opts': [('Measles is caused by a virus — antibiotics only kill bacteria and have no effect on viruses',
                      True),
                     ('Antibiotics would make the rash worse', False),
                     ('The patient is too young for antibiotics', False),
                     ('Paracetamol is stronger than antibiotics', False)],
            'q': 'A measles patient is told to rest and take paracetamol. Why are they not given antibiotics?',
            'wrong_explanations': {1: 'Rash worsening from antibiotics is not a reason — the fundamental reason is '
                                      'that antibiotics target bacterial cell walls and structures that viruses simply '
                                      "don't have.",
                                   2: "Age is not the deciding factor — the pathogen type is. Antibiotics don't work "
                                      'on viruses regardless of patient age.',
                                   3: 'Paracetamol relieves symptoms — it does not treat the infection. Antibiotics '
                                      'treat bacterial infections — but measles is viral.'}}],
  'rp': None,
  'spec': '4.3.1.2',
  'summary': 'Describe the main viral diseases — measles, HIV/AIDS and tobacco mosaic virus.',
  'theory': [{'content': 'Viruses are not living cells — they are particles of genetic material (DNA or RNA) '
                         'surrounded by a protein coat.\n'
                         '\n'
                         "They cannot reproduce on their own — they must invade a HOST CELL and use the cell's own "
                         'machinery to make copies of themselves.\n'
                         '\n'
                         'This process destroys the host cell when new virus particles burst out.\n'
                         '\n'
                         'Viruses cause disease by:\n'
                         'Destroying cells as they replicate.\n'
                         'Triggering an immune response (the fever, aches and fatigue you feel are largely your immune '
                         'system fighting the virus).\n'
                         'Disrupting normal organ function.',
              'heading': 'How Viruses Cause Disease'},
             {'content': 'CAUSE: Measles virus (a paramyxovirus).\n'
                         '\n'
                         'TRANSMISSION: Airborne droplets — spread very easily through coughing, sneezing and close '
                         'contact.\n'
                         '\n'
                         'SYMPTOMS:\n'
                         'High fever.\n'
                         'Red, blotchy skin rash spreading from face to body.\n'
                         'Runny nose, cough, sore red eyes.\n'
                         "White spots inside the mouth (Koplik's spots — a diagnostic sign).\n"
                         '\n'
                         'COMPLICATIONS: Measles can be very serious — can lead to pneumonia (lung infection), '
                         'encephalitis (brain inflammation) and death, particularly in malnourished children or '
                         'immunocompromised individuals.\n'
                         '\n'
                         'PREVENTION: The MMR vaccine (measles, mumps, rubella) — given in two doses in childhood. '
                         'Highly effective.\n'
                         '\n'
                         'TREATMENT: No specific antiviral drug — rest, fluids, paracetamol for fever. The immune '
                         'system clears the infection.',
              'heading': 'Measles'},
             {'content': 'CAUSE: HIV (Human Immunodeficiency Virus) — a retrovirus.\n'
                         '\n'
                         'TRANSMISSION: Through bodily fluids — unprotected sexual contact, sharing needles, blood '
                         'transfusions (in countries without screening), mother to baby (during pregnancy, birth or '
                         'breastfeeding).\n'
                         '\n'
                         'WHAT HIV DOES: HIV specifically targets and destroys CD4+ T-helper lymphocytes — the very '
                         'cells that coordinate the immune response. Over time, the immune system is progressively '
                         'weakened.\n'
                         '\n'
                         'AIDS: AIDS (Acquired Immune Deficiency Syndrome) develops when HIV has destroyed so many '
                         'lymphocytes that the immune system can no longer function. The patient becomes vulnerable to '
                         'OPPORTUNISTIC INFECTIONS — infections that a healthy immune system would easily fight off '
                         '(e.g. rare pneumonias, certain cancers).\n'
                         '\n'
                         'PREVENTION: Condoms, clean needles, screening blood supplies, antiretroviral drugs for '
                         'pregnant women with HIV.\n'
                         '\n'
                         'TREATMENT: ANTIRETROVIRAL DRUGS (ARVs) — prevent HIV from replicating. Cannot cure HIV but '
                         'allow patients to live near-normal lives. Must be taken for life.',
              'heading': 'HIV and AIDS'},
             {'content': 'CAUSE: Tobacco mosaic virus — affects a wide range of plants including tobacco, tomatoes, '
                         'peppers and cucumbers.\n'
                         '\n'
                         'TRANSMISSION: Direct contact between plants, contaminated tools, insects feeding on plants, '
                         'and handling by humans.\n'
                         '\n'
                         'SYMPTOMS: A distinctive MOSAIC PATTERN of light and dark green or yellow patches on leaves. '
                         'Leaves may also be distorted or stunted.\n'
                         '\n'
                         "WHY IT'S HARMFUL: Infected cells cannot produce chlorophyll properly. The mosaic-patterned "
                         'leaves have LESS CHLOROPHYLL than healthy leaves → reduced rate of photosynthesis → plant '
                         'grows poorly and produces less fruit/yield.\n'
                         '\n'
                         'PREVENTION: Removing and destroying infected plants, cleaning tools, using virus-free seeds, '
                         'controlling insect vectors.',
              'heading': 'Tobacco Mosaic Virus (TMV)'}],
  'title': 'Viral Diseases',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Gonorrhoea IS treatable with antibiotics — but antibiotic-resistant strains are emerging. Do not '
                    "say 'gonorrhoea cannot be treated'. Say instead: 'it can be treated, but resistance is a growing "
                    "problem'. Also: Salmonella causes disease primarily through TOXINS — not just by the bacteria "
                    'damaging cells directly.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'bacterial-diseases',
  'key_note': 'Salmonella: bacteria, contaminated food, symptoms = fever/vomiting/diarrhoea, prevented by cooking '
              'thoroughly. Gonorrhoea: bacteria, STI, discharge and pain, treated by antibiotics (resistance growing).',
  'matching': {'instruction': 'Match each feature to Salmonella or Gonorrhoea.',
               'pairs': [('Salmonella', 'Spread through undercooked food — prevented by thorough cooking and hygiene'),
                         ('Gonorrhoea', 'Sexually transmitted — thick discharge and pain when urinating'),
                         ('Salmonella', 'Bacteria produce toxins in the gut — causing vomiting and diarrhoea'),
                         ('Gonorrhoea', 'Antibiotic-resistant strains have emerged — major public health concern'),
                         ('Salmonella', 'Often resolves without antibiotics — rest and fluids usually sufficient')],
               'title': 'Match the Bacterial Disease to its Features'},
  'quiz': [{'opts': [('Thorough cooking to kill bacteria, good food hygiene, refrigeration and hand washing', True),
                     ('Taking antibiotics before eating suspected food', False),
                     ('Avoiding all animal products entirely', False),
                     ('Vaccinating all humans against Salmonella', False)],
            'q': 'How is Salmonella food poisoning prevented?',
            'wrong_explanations': {1: 'Taking antibiotics preventatively is dangerous — it promotes antibiotic '
                                      'resistance without benefit.',
                                   2: "Thorough cooking makes animal products safe — you don't need to avoid them "
                                      'entirely.',
                                   3: 'Human Salmonella vaccines are not routinely used — poultry vaccination is used '
                                      'in the UK to reduce the source.'}},
           {'opts': [('Antibiotic-resistant strains have evolved — bacteria with resistance mutations survive '
                      'antibiotic treatment and pass on resistance genes',
                      True),
                     ('Gonorrhoea has mutated into a virus, which antibiotics cannot target', False),
                     ('New strains produce proteins that destroy antibiotic molecules before they can work', False),
                     ('People have developed immunity to the antibiotics used to treat it', False)],
            'q': 'Why is gonorrhoea becoming harder to treat?',
            'wrong_explanations': {1: 'Gonorrhoea remains a bacterium — bacteria cannot evolve into viruses. The issue '
                                      'is antibiotic resistance in bacterial populations.',
                                   2: 'Some resistant bacteria do produce enzymes (like beta-lactamases) that break '
                                      'down antibiotics — this is one mechanism of resistance, but the question is '
                                      'about the broader process of natural selection producing resistant strains.',
                                   3: 'People develop immunity to pathogens, not to medicines. Antibiotic resistance '
                                      'is a property of the BACTERIA, not of human patients.'}}],
  'rp': None,
  'spec': '4.3.1.3',
  'summary': 'Describe Salmonella food poisoning and Gonorrhoea as examples of bacterial diseases.',
  'theory': [{'content': 'Bacteria are single-celled prokaryotes. They can reproduce very rapidly — doubling every 20 '
                         'minutes under ideal conditions.\n'
                         '\n'
                         'Bacteria cause disease in two main ways:\n'
                         'PRODUCING TOXINS — many bacteria secrete chemicals (toxins) that damage cells and tissues. '
                         'It is often the toxins, not the bacteria themselves, that cause the symptoms of disease.\n'
                         'DIRECT CELL DAMAGE — some bacteria invade and destroy body cells directly.\n'
                         '\n'
                         'Unlike viruses, bacteria CAN be treated with ANTIBIOTICS — drugs that specifically target '
                         "bacterial structures (e.g. cell walls) that human cells don't have.",
              'heading': 'How Bacteria Cause Disease'},
             {'content': 'CAUSE: Salmonella bacteria (various species).\n'
                         '\n'
                         'TRANSMISSION: Eating food contaminated with Salmonella — most commonly undercooked poultry, '
                         'raw or undercooked eggs, unpasteurised milk. Also spread through poor kitchen hygiene '
                         '(cross-contamination from raw to cooked food) and unwashed hands.\n'
                         '\n'
                         'SYMPTOMS: Begin 12–72 hours after eating contaminated food:\n'
                         'Fever.\n'
                         'Stomach cramps and abdominal pain.\n'
                         'Vomiting.\n'
                         'Diarrhoea (which can be severe and bloody).\n'
                         'Symptoms usually last 4–7 days.\n'
                         '\n'
                         "MECHANISM: Salmonella bacteria survive cooking if the food isn't heated properly. They reach "
                         'the small intestine, colonise the gut lining and produce toxins — causing the symptoms.\n'
                         '\n'
                         'PREVENTION: Thorough cooking (bacteria are killed by heat), good hygiene (wash hands, clean '
                         'surfaces), refrigeration (slows bacterial growth), pasteurisation of dairy products, '
                         'vaccination of poultry flocks.\n'
                         '\n'
                         'TREATMENT: Most cases resolve without antibiotics — rest and plenty of fluids. Severe cases '
                         'may need antibiotics and hospital treatment.',
              'heading': 'Salmonella Food Poisoning'},
             {'content': 'CAUSE: Neisseria gonorrhoeae bacteria.\n'
                         '\n'
                         'TRANSMISSION: Sexual contact — a sexually transmitted infection (STI). Passed during '
                         'vaginal, anal or oral sex without barrier contraception.\n'
                         '\n'
                         'SYMPTOMS:\n'
                         'IN FEMALES: Often NO symptoms (asymptomatic) — this makes it particularly dangerous as it '
                         'can spread unknowingly. When symptoms occur: thick yellow/green vaginal discharge, pain when '
                         'urinating.\n'
                         'IN MALES: Thick yellow/green discharge from the penis, burning pain when urinating.\n'
                         '\n'
                         'COMPLICATIONS: If untreated:\n'
                         'Pelvic inflammatory disease (PID) in females → can cause infertility.\n'
                         'Increased risk of HIV infection.\n'
                         'Can be passed from mother to baby during birth → eye infection in newborn.\n'
                         '\n'
                         'PREVENTION: Using condoms (barrier contraception), reducing number of sexual partners, '
                         'regular STI testing.\n'
                         '\n'
                         'TREATMENT: Antibiotics — however, ANTIBIOTIC-RESISTANT strains have emerged, making '
                         'gonorrhoea increasingly difficult to treat. This is a serious and growing public health '
                         'problem.\n'
                         '\n'
                         'ANTIBIOTIC RESISTANCE in gonorrhoea happens through natural selection:\n'
                         'Random mutations in bacteria can produce resistance.\n'
                         'Antibiotics kill non-resistant bacteria but resistant ones survive.\n'
                         'Resistant bacteria reproduce, passing on resistance genes.\n'
                         'Over time, the population becomes resistant.',
              'heading': 'Gonorrhoea'}],
  'title': 'Bacterial Diseases',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The MOSQUITO is the VECTOR for malaria — not the pathogen. Plasmodium (the protist) is the '
                    'pathogen that causes disease. The mosquito carries and transmits it. This distinction is a very '
                    'common exam question. Also: rose black spot is caused by a FUNGUS — not bacteria, not a virus.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'fungal-protist-diseases',
  'key_note': 'Rose black spot: fungus, water/wind spread, leaf spots → defoliation → less photosynthesis. Malaria: '
              'Plasmodium protist, Anopheles mosquito = vector, destroys red blood cells, recurring fever.',
  'matching': {'instruction': 'Sort each feature to the correct disease.',
               'pairs': [('Rose black spot', 'Caused by a fungus — spreads via water and wind'),
                         ('Malaria', 'Caused by a protist — transmitted by Anopheles mosquito bites'),
                         ('Rose black spot', 'Black spots on leaves — causes defoliation and reduced photosynthesis'),
                         ('Malaria', 'Destroys red blood cells — causes cyclical fever and can be fatal'),
                         ('Rose black spot', 'Treated with fungicide — infected leaves removed and destroyed'),
                         ('Malaria',
                          'Prevented with mosquito nets and insecticides — anti-malarial drugs for treatment')],
               'title': 'Rose Black Spot or Malaria?'},
  'quiz': [{'opts': [('Infected leaves develop spots and fall off — less leaf area means less photosynthesis and less '
                      'glucose for growth',
                      True),
                     ('The fungus blocks the xylem, preventing water reaching the leaves', False),
                     ('The fungus produces toxins that directly kill root cells', False),
                     ('Spores block stomata, preventing CO₂ from entering the leaf', False)],
            'q': 'Why does rose black spot cause poor plant growth?',
            'wrong_explanations': {1: "Rose black spot infects LEAF CELLS — it doesn't block xylem. The impact is "
                                      'through reduced photosynthetic capacity.',
                                   2: "Rose black spot is a leaf disease — it doesn't specifically target roots.",
                                   3: 'Blocking stomata is not the primary mechanism — the main effect is leaf loss '
                                      'through defoliation reducing total photosynthesis.'}},
           {'opts': [('It is the vector — it carries Plasmodium from one human to another when it bites', True),
                     ('It is the pathogen — the mosquito itself causes the disease', False),
                     ('It injects its own saliva which contains the fever-causing toxin', False),
                     ('It is only involved in spreading malaria in tropical countries — not elsewhere', False)],
            'q': 'What is the role of the Anopheles mosquito in malaria?',
            'wrong_explanations': {1: 'The PATHOGEN is Plasmodium (the protist). The mosquito is the VECTOR — it '
                                      'carries and transmits the pathogen without being the cause of disease itself.',
                                   2: 'Mosquito saliva can cause local irritation — but the disease malaria is caused '
                                      'specifically by Plasmodium being injected, not by the saliva itself.',
                                   3: 'Malaria is predominantly tropical because Anopheles mosquitoes thrive in warm, '
                                      "wet environments — but the mosquito's role as vector is the same wherever it "
                                      'lives.'}}],
  'rp': None,
  'spec': '4.3.1.4',
  'summary': 'Describe rose black spot (fungal) and malaria (protist) as examples of these disease types.',
  'theory': [{'content': 'CAUSE: Diplocarpon rosae — a fungal pathogen that infects rose plants.\n'
                         '\n'
                         'TRANSMISSION: Fungal spores spread through WATER (rain splashing from leaf to leaf) and by '
                         'WIND. Spores land on leaves and germinate when conditions are warm and wet.\n'
                         '\n'
                         'SYMPTOMS:\n'
                         'Purple or black spots appearing on rose leaves.\n'
                         'Leaves turn yellow around the spots.\n'
                         'Affected leaves drop off the plant prematurely — DEFOLIATION.\n'
                         '\n'
                         'WHY IT MATTERS: The loss of leaves is the key problem. Fewer leaves → less surface area for '
                         'photosynthesis → the plant grows poorly, produces fewer flowers and is weakened overall. '
                         'Severely infected plants may die.\n'
                         '\n'
                         'PREVENTION AND TREATMENT:\n'
                         'Remove and destroy infected leaves immediately — do NOT compost them (spores can survive).\n'
                         'Apply FUNGICIDE sprays to remaining leaves — kills fungal growth.\n'
                         'Choose disease-resistant rose varieties.\n'
                         'Avoid overhead watering — wet leaves encourage fungal growth.',
              'heading': 'Fungal Diseases — Rose Black Spot'},
             {'content': 'CAUSE: Plasmodium — a protist (single-celled eukaryote). Several species cause malaria; '
                         'Plasmodium falciparum is the most deadly.\n'
                         '\n'
                         'VECTOR: The female Anopheles mosquito — she bites infected humans, picks up Plasmodium, and '
                         'injects it into the next person she bites. The mosquito is the VECTOR, not the pathogen.\n'
                         '\n'
                         'LIFE CYCLE IN BRIEF:\n'
                         'Plasmodium is injected into the human bloodstream during a mosquito bite.\n'
                         'It travels to the liver and multiplies.\n'
                         'It then infects and DESTROYS red blood cells in cycles.\n'
                         'The destruction of red blood cells causes the characteristic RECURRING FEVER.\n'
                         '\n'
                         'SYMPTOMS: High fever (cyclical — comes and goes in waves), headache, vomiting, muscle pain '
                         'and fatigue. Severe malaria can cause: anaemia (from red blood cell destruction), kidney '
                         'failure, cerebral malaria (affecting the brain), coma and death.\n'
                         '\n'
                         'PREVENTION (breaking the transmission cycle):\n'
                         'Mosquito nets (especially insecticide-treated bed nets — ITNs).\n'
                         'Insecticide sprays to kill mosquitoes.\n'
                         'Draining standing water where mosquitoes breed.\n'
                         'Anti-malarial drugs taken before and during travel to high-risk areas.\n'
                         '\n'
                         'TREATMENT: Anti-malarial drugs (e.g. artemisinin-based combination therapies). Resistance to '
                         'some anti-malarials is also emerging.',
              'heading': 'Protist Diseases — Malaria'},
             {'content': 'It helps to compare these two types side by side:\n'
                         '\n'
                         'ROSE BLACK SPOT:\n'
                         'Pathogen type: FUNGUS.\n'
                         'Host: Rose plants.\n'
                         'Spread: Water and wind carrying spores.\n'
                         'Damage: Leaf spots and defoliation → reduced photosynthesis.\n'
                         'Treatment: Fungicide, removing infected leaves.\n'
                         '\n'
                         'MALARIA:\n'
                         'Pathogen type: PROTIST (Plasmodium).\n'
                         'Host: Humans (and other primates).\n'
                         'Spread: Via the Anopheles mosquito VECTOR.\n'
                         'Damage: Destroys red blood cells → recurring fever, anaemia, can be fatal.\n'
                         'Treatment: Anti-malarial drugs.',
              'heading': 'Comparing Fungal and Protist Diseases'}],
  'title': 'Fungal and Protist Diseases',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Vaccines do NOT give you the disease. They contain harmless forms of the pathogen (dead, weakened '
                    'or just antigens) — they cannot cause the actual disease. The immune response to the vaccine '
                    "(mild fever, soreness) is your body's NORMAL reaction to stimulation — not the disease itself.",
  'equations': [],
  'fifas': [],
  'higher': 'Herd immunity requires a threshold proportion of the population to be immune — for measles ~95% '
            'vaccination coverage is needed. Students should be able to evaluate data on vaccination programmes and '
            'the incidence of disease, including interpreting graphs of disease cases before and after vaccination '
            'introduction. mRNA vaccines (e.g. COVID-19) instruct cells to produce a viral antigen, triggering an '
            'immune response without using any viral material.',
  'id': 'vaccination',
  'key_note': 'Vaccine → harmless antigen → immune response → memory cells → rapid response on real infection. Herd '
              "immunity: enough vaccinated → pathogen can't spread → vulnerable people protected. Smallpox = only "
              'disease fully eradicated by vaccination.',
  'matching': {'instruction': 'Match each concept to its correct description.',
               'pairs': [('Memory cells',
                          'Produced during vaccination — allow rapid antibody production if real pathogen is later '
                          'encountered'),
                         ('Herd immunity',
                          'When enough of the population is immune that the pathogen cannot spread — protects '
                          'unvaccinated individuals'),
                         ('MMR vaccine',
                          'Protects against measles, mumps and rubella — given in two doses in childhood'),
                         ('Smallpox',
                          'The only human disease ever fully eradicated — achieved through global vaccination'),
                         ('Flu vaccine',
                          'Updated annually because the influenza virus mutates its surface antigens each year')],
               'title': 'Match the Vaccination Concept'},
  'quiz': [{'opts': [('It stimulates an immune response and produces memory cells — so the body responds rapidly if '
                      'the real pathogen invades',
                      True),
                     ('It kills any pathogen that enters the body for the rest of your life', False),
                     ('It strengthens all aspects of the immune system permanently', False),
                     ('It prevents the pathogen from ever entering the body', False)],
            'q': 'How does a vaccine protect against future infection?',
            'wrong_explanations': {1: "Vaccines don't provide a permanent killing effect — they prepare MEMORY CELLS "
                                      'that respond quickly if the pathogen arrives.',
                                   2: "Vaccines provide SPECIFIC immunity to one pathogen — they don't generally boost "
                                      'the whole immune system.',
                                   3: 'Pathogens can still enter the body after vaccination — the vaccine means the '
                                      "immune system destroys them so quickly they don't cause disease."}},
           {'opts': [('When enough of a population is immune that the pathogen cannot spread effectively — protecting '
                      'even unvaccinated individuals',
                      True),
                     ('When every single person in a population has been vaccinated', False),
                     ('When an entire herd of animals is vaccinated against a disease', False),
                     ('When a person becomes naturally immune after recovering from a disease', False)],
            'q': 'What is herd immunity?',
            'wrong_explanations': {1: "Herd immunity doesn't require 100% vaccination — it just needs enough people to "
                                      'be immune to break the chain of transmission.',
                                   2: "'Herd' refers to any population — not just animal herds. Herd immunity applies "
                                      'to human populations too.',
                                   3: 'Natural immunity after infection DOES contribute to herd immunity — but '
                                      'vaccination is the safer way to achieve it without suffering the disease.'}},
           {'opts': [("The influenza virus mutates rapidly — its surface antigens change, so last year's vaccine may "
                      "no longer match this year's strains",
                      True),
                     ('Memory cells from flu vaccines only last one year before disappearing', False),
                     ('Flu vaccines contain live viruses that must be freshly prepared each season', False),
                     ('The government changes the vaccine composition each year as a precaution', False)],
            'q': 'Why is the flu vaccine updated every year?',
            'wrong_explanations': {1: 'Memory cells from vaccines can last many years or a lifetime — the issue is not '
                                      'memory cell lifespan but viral mutation.',
                                   2: 'Many flu vaccines use inactivated (killed) viruses — not live ones. The reason '
                                      'for annual updates is viral mutation.',
                                   3: 'The composition is updated based on scientific surveillance of which influenza '
                                      "strains are circulating — it's not an arbitrary precaution."}}],
  'rp': None,
  'spec': '4.3.2',
  'summary': 'Explain how vaccines work, why they protect populations and what herd immunity means.',
  'theory': [{'content': 'A vaccine introduces a small, harmless amount of a pathogen (or part of one) into the body '
                         'to stimulate an immune response WITHOUT causing the actual disease.\n'
                         '\n'
                         'Vaccines can contain:\n'
                         "Dead or inactivated pathogens — can't cause disease but still have antigens.\n"
                         'Weakened (attenuated) live pathogens — cause only a very mild or no illness.\n'
                         'Antigens only (fragments of the pathogen surface) — the pathogen itself is never '
                         'introduced.\n'
                         'mRNA coding for a pathogen antigen (e.g. COVID-19 mRNA vaccines).\n'
                         '\n'
                         'What happens after vaccination:\n'
                         '1. Phagocytes engulf the vaccine material.\n'
                         '2. Lymphocytes recognise the pathogen antigens and produce specific antibodies.\n'
                         '3. MEMORY CELLS are produced — these remain in the blood for many years or for life.\n'
                         '4. If the real pathogen later invades, memory cells respond RAPIDLY and MASSIVELY — '
                         'producing antibodies so fast that the pathogen is destroyed before it causes symptoms.\n'
                         '\n'
                         'The KEY POINT: vaccines work by training the immune system in advance, so it is ready to '
                         'respond instantly if the real pathogen ever arrives.',
              'heading': 'How Vaccines Work'},
             {'content': 'HERD IMMUNITY is achieved when enough of a population is immune (through vaccination or past '
                         'infection) that the pathogen cannot spread efficiently — even unvaccinated individuals are '
                         'protected.\n'
                         '\n'
                         'How it works:\n'
                         'If most people are immune, a newly infected person encounters mostly immune individuals.\n'
                         'The pathogen cannot find enough new hosts to continue spreading.\n'
                         'The chain of transmission is broken.\n'
                         '\n'
                         'Why it matters:\n'
                         'Some people CANNOT be vaccinated — newborn babies (too young), immunocompromised patients '
                         '(e.g. on chemotherapy), people with certain allergies.\n'
                         'Herd immunity protects these vulnerable individuals indirectly.\n'
                         '\n'
                         'The percentage of the population needed for herd immunity varies by disease:\n'
                         'Measles requires ~95% vaccination coverage (because it spreads very easily).\n'
                         'Polio requires ~80–85%.\n'
                         '\n'
                         'When vaccination rates drop below the threshold, outbreaks occur — as happened with measles '
                         'in some countries after false concerns about the MMR vaccine.',
              'heading': 'Herd Immunity'},
             {'content': 'MMR vaccine: protects against measles, mumps and rubella. Given at 12–15 months and again at '
                         '3–5 years. Highly effective.\n'
                         '\n'
                         'SMALLPOX: The only human disease to be completely ERADICATED (wiped out globally) — achieved '
                         'entirely through worldwide vaccination. The last natural case was in 1977.\n'
                         '\n'
                         'POLIO: Nearly eradicated through global vaccination campaigns — still circulating in a small '
                         'number of countries.\n'
                         '\n'
                         "FLU VACCINE: Updated each year because influenza virus mutates rapidly — last year's vaccine "
                         "may not protect against this year's strains.\n"
                         '\n'
                         'COVID-19: mRNA vaccines developed and deployed at record speed (2020–21), demonstrating new '
                         'vaccine technology.\n'
                         '\n'
                         'HPV VACCINE: Protects against Human Papillomavirus — which causes most cervical cancers. '
                         'Given to teenagers before sexual activity begins.',
              'heading': 'Examples of Successful Vaccination'},
             {'content': 'Vaccines are among the most extensively tested and monitored medicines in existence.\n'
                         '\n'
                         'All vaccines undergo rigorous testing before approval:\n'
                         'Laboratory and animal testing.\n'
                         'Phase 1, 2 and 3 clinical trials (see Drug Development subtopic).\n'
                         'Regulatory review by agencies like the MHRA (UK) or FDA (USA).\n'
                         '\n'
                         'Common side effects are mild and temporary:\n'
                         'Soreness at injection site.\n'
                         'Low-grade fever for 1–2 days.\n'
                         'Fatigue.\n'
                         '\n'
                         'SERIOUS side effects are extremely rare — and the risk of serious illness from the actual '
                         'disease is far greater than any risk from the vaccine.\n'
                         '\n'
                         'Misinformation about vaccine safety has caused vaccination rates to drop in some '
                         'communities, leading to preventable outbreaks of serious diseases.',
              'heading': 'Are Vaccines Safe?'}],
  'title': 'Vaccination',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Painkillers do NOT treat infections — they only relieve symptoms. A patient taking only '
                    'paracetamol for a bacterial infection is NOT treating the infection. Also: always complete '
                    'antibiotic courses — stopping early is a major driver of resistance because the bacteria that '
                    'survive are likely to be the more resistant ones.',
  'equations': [],
  'fifas': [],
  'higher': 'Antibiotic resistance develops through natural selection: random resistance mutations exist in a '
            'bacterial population → antibiotics act as selection pressure killing non-resistant bacteria → resistant '
            'bacteria survive, reproduce and pass on resistance genes → resistance spreads. MRSA is a clinically '
            'important example. Students should be able to explain why reducing unnecessary antibiotic use and '
            'completing courses slows resistance development.',
  'id': 'antibiotics-painkillers',
  'key_note': 'Antibiotics: kill bacteria, NO effect on viruses, target bacterial cell walls/ribosomes. Antibiotic '
              'resistance: natural selection of resistant mutants — avoid misuse. Painkillers: treat symptoms only, '
              "don't kill pathogens.",
  'matching': {'instruction': 'Sort each statement to the correct type of drug.',
               'pairs': [('Antibiotic', 'Kills bacteria — works by targeting bacterial cell walls or ribosomes'),
                         ('Painkiller', 'Relieves fever and pain — does not kill any pathogens'),
                         ('Antiviral', 'Prevents viral replication — used for HIV and influenza'),
                         ('Antibiotic', 'Has no effect on viral infections — useless against flu or measles'),
                         ('Painkiller', 'Examples: paracetamol, ibuprofen, aspirin')],
               'title': 'Antibiotic, Painkiller or Antiviral?'},
  'quiz': [{'opts': [("Viruses don't have cell walls or bacterial ribosomes — the structures antibiotics target don't "
                      'exist in viruses',
                      True),
                     ('Viruses are too small for antibiotics to reach', False),
                     ('Antibiotics are absorbed too slowly to reach viruses in the bloodstream', False),
                     ('Viruses produce enzymes that destroy antibiotics', False)],
            'q': "Why can't antibiotics treat viral infections?",
            'wrong_explanations': {1: "Viruses are smaller than bacteria — but size is not why antibiotics don't work. "
                                      "Antibiotics target specific bacterial structures that viruses simply don't "
                                      'have.',
                                   2: 'Antibiotics are absorbed into the bloodstream — but they have no biological '
                                      'target in virus particles, so reaching them makes no difference.',
                                   3: 'Some resistant bacteria do produce enzymes that destroy antibiotics — but this '
                                      'is a bacterial resistance mechanism, not a general viral property.'}},
           {'opts': [('Stopping early leaves the most resistant bacteria alive — they survive and reproduce, '
                      'increasing resistance',
                      True),
                     ('Stopping early means the antibiotics already taken are wasted and have no effect', False),
                     ('Partial courses make the bacteria grow faster as a response', False),
                     ("It doesn't matter — stopping early is fine if symptoms improve", False)],
            'q': 'Why is it important to always complete a full course of antibiotics?',
            'wrong_explanations': {1: 'The antibiotics already taken do have effect — they kill susceptible bacteria. '
                                      'The problem is that the resistant survivors are left to reproduce.',
                                   2: "Bacteria don't 'grow faster' in response to antibiotics stopping — the issue is "
                                      'selective survival of resistant variants.',
                                   3: 'This is a dangerous misconception — symptoms improving means the immune system '
                                      'and antibiotics are working, but bacteria may still be present. Stopping early '
                                      'increases resistance risk.'}}],
  'rp': None,
  'spec': '4.3.3',
  'summary': 'Explain how antibiotics work, why antibiotic resistance is a threat, and the role of painkillers.',
  'theory': [{'content': 'Antibiotics are drugs that kill bacteria or prevent them from reproducing — they are used to '
                         'treat BACTERIAL infections.\n'
                         '\n'
                         'How they work: Antibiotics target specific structures in bacteria that are NOT present in '
                         'human cells — for example:\n'
                         'PENICILLIN (and similar antibiotics) disrupts bacterial CELL WALL synthesis. Human cells '
                         "have no cell wall, so penicillin doesn't harm them.\n"
                         'Other antibiotics target bacterial ribosomes or DNA replication.\n'
                         '\n'
                         'Different antibiotics work on different bacteria:\n'
                         'BROAD SPECTRUM antibiotics work against many different bacterial species.\n'
                         'NARROW SPECTRUM antibiotics target specific types of bacteria.\n'
                         '\n'
                         'Antibiotics CANNOT treat viral infections because:\n'
                         'Viruses have no cell walls, no bacterial ribosomes and no bacterial DNA replication '
                         'machinery — there is nothing for antibiotics to target.\n'
                         'Viruses live INSIDE host cells — drugs that killed them would also damage the host cell.\n'
                         '\n'
                         'Antibiotics were discovered by Alexander Fleming in 1928 — he noticed Penicillium mould was '
                         'killing bacteria on a petri dish.',
              'heading': 'Antibiotics'},
             {'content': 'Antibiotic resistance is one of the greatest threats to global health.\n'
                         '\n'
                         'How it develops through NATURAL SELECTION:\n'
                         '1. Within a population of bacteria, random MUTATIONS occur naturally during reproduction.\n'
                         '2. Occasionally, a mutation gives a bacterium resistance to an antibiotic.\n'
                         '3. When antibiotics are used, non-resistant bacteria are killed.\n'
                         '4. Resistant bacteria SURVIVE and REPRODUCE — passing on the resistance gene to offspring.\n'
                         '5. Over time, the entire population becomes resistant — the antibiotic no longer works.\n'
                         '\n'
                         'Why resistance is spreading:\n'
                         "OVER-PRESCRIBING — doctors prescribing antibiotics for viral infections or 'just in case'.\n"
                         'NOT COMPLETING COURSES — stopping early leaves some bacteria alive; the survivors are more '
                         'likely to be partially resistant.\n'
                         'AGRICULTURE — antibiotics used to promote growth in livestock, creating resistant bacteria '
                         'in food chains.\n'
                         '\n'
                         'Consequences: Infections once easily treated (e.g. tuberculosis, some pneumonias) are '
                         'becoming dangerous again. MRSA (methicillin-resistant Staphylococcus aureus) is an example '
                         'of a serious antibiotic-resistant bacterium.\n'
                         '\n'
                         'How to slow resistance:\n'
                         'Only use antibiotics when genuinely necessary.\n'
                         'Always complete the full course.\n'
                         'Never share or save antibiotics for later.\n'
                         'Reduce agricultural antibiotic use.',
              'heading': 'Antibiotic Resistance — A Global Crisis'},
             {'content': 'Painkillers (analgesics) relieve pain and reduce fever — but they do NOT kill pathogens or '
                         'treat the cause of infection.\n'
                         '\n'
                         'Common painkillers: paracetamol, ibuprofen, aspirin.\n'
                         '\n'
                         'They treat SYMPTOMS — making the patient feel more comfortable — but the immune system still '
                         'needs to fight the infection.\n'
                         '\n'
                         'A patient with a bacterial infection may take BOTH:\n'
                         'Antibiotics — to kill the bacteria (treating the cause).\n'
                         'Painkillers — to manage fever, pain and discomfort (treating the symptoms).\n'
                         '\n'
                         'ANTIVIRAL DRUGS are medicines that do treat viral infections — but they are much harder to '
                         "develop than antibiotics because viruses use the host cell's own machinery.\n"
                         'Examples: oseltamivir (Tamiflu) for influenza, antiretroviral drugs (ARVs) for HIV.\n'
                         "Antivirals don't kill viruses outright — they usually prevent replication.",
              'heading': 'Painkillers'}],
  'title': 'Antibiotics and Painkillers',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'A DOUBLE-BLIND trial means NEITHER the patient NOR the doctor knows who is getting the real drug. '
                    "A SINGLE-BLIND trial means only the patient doesn't know. Double-blind removes bias from both "
                    'sides. A PLACEBO is a dummy treatment — not a low dose of the real drug.',
  'equations': [],
  'fifas': [],
  'higher': 'Pre-clinical testing: cell cultures → computer models → animal testing. Clinical trial phases: Phase 1 '
            '(safety, healthy volunteers), Phase 2 (efficacy, patients), Phase 3 (large-scale, double-blind, '
            'placebo-controlled). Double-blind eliminates bias from both patients AND doctors. Peer review validates '
            "findings before publication. Thalidomide's withdrawal led to much stricter testing requirements, "
            'particularly for testing effects on embryo development.',
  'id': 'drug-discovery-development',
  'key_note': 'Drug testing: pre-clinical (cells → computer → animals) → Phase 1 (safety, healthy volunteers) → Phase '
              '2 (efficacy, patients) → Phase 3 (large comparison, double-blind, placebo) → regulatory approval.',
  'matching': {'instruction': 'Match each description to the correct stage of drug testing.',
               'pairs': [('Pre-clinical — cells and animals',
                          'Drug tested in lab on cells and then animals — checks basic safety before human trials'),
                         ('Phase 1 clinical trial',
                          'Small group of healthy volunteers — checks the drug is safe in humans'),
                         ('Phase 2 clinical trial',
                          'Patients with the condition — checks the drug actually works at the right dose'),
                         ('Phase 3 clinical trial',
                          'Large-scale, double-blind, placebo-controlled — compares to existing treatment'),
                         ('Double-blind trial',
                          'Neither patient nor doctor knows who is receiving the real drug — eliminates bias'),
                         ('Placebo', 'Inactive dummy treatment — controls for the psychological placebo effect')],
               'title': 'Match the Stage of Drug Development'},
  'quiz': [{'opts': [('Neither the patients nor the doctors know who is receiving the real drug or the placebo — '
                      'eliminates bias from both sides',
                      True),
                     ("Only the patients don't know which treatment they are receiving", False),
                     ('The trial uses two different drugs tested simultaneously against each other', False),
                     ('The trial is conducted in the dark to prevent visual identification of the drug', False)],
            'q': 'What is a double-blind clinical trial?',
            'wrong_explanations': {1: "If only the PATIENT doesn't know = single-blind. Double-blind means BOTH "
                                      "patient AND doctor are unaware — this prevents the doctor's expectations "
                                      'influencing how they assess patient progress.',
                                   2: 'A trial testing two real drugs against each other is a comparative trial — '
                                      'double-blind refers to who knows about treatment allocation, not how many drugs '
                                      'are tested.',
                                   3: "'Blind' in a clinical context means 'unaware of treatment allocation' — it has "
                                      'nothing to do with actual darkness.'}},
           {'opts': [('To control for the placebo effect — some patients improve just because they believe they are '
                      'being treated',
                      True),
                     ('To give patients a low starting dose before they receive the real drug', False),
                     ('To ensure every patient receives some form of medical benefit during the trial', False),
                     ('To test the side effects of inactive substances', False)],
            'q': 'Why is a placebo used in clinical trials?',
            'wrong_explanations': {1: 'A placebo is not a low dose — it is INACTIVE and contains no active ingredient.',
                                   2: 'Patients in the placebo group receive no active treatment — this is ethically '
                                      'managed carefully and only used when ethically appropriate.',
                                   3: 'Placebos by definition have no pharmacological activity — any side effects are '
                                      'psychological or coincidental.'}},
           {'opts': [('Drugs must be rigorously tested for all potential effects including effects on embryos — '
                      'testing requirements were significantly strengthened',
                      True),
                     ('Natural drugs are always safer than synthetic ones', False),
                     ('Sedatives should never be prescribed during pregnancy', False),
                     ('Clinical trials are unnecessary if a drug has been shown to be safe in adults', False)],
            'q': 'What was the key lesson from the thalidomide tragedy?',
            'wrong_explanations': {1: 'Thalidomide was a synthetic drug — but many synthetic drugs are completely '
                                      'safe. The lesson was specifically about testing for effects on ALL groups, '
                                      'especially embryos.',
                                   2: 'The lesson was specifically about testing for ALL effects in ALL populations — '
                                      'not a blanket ban on sedatives in pregnancy.',
                                   3: 'The thalidomide case showed exactly WHY clinical trials must be thorough — an '
                                      'adult-safe drug was devastating to embryos.'}}],
  'rp': None,
  'spec': '4.3.4',
  'summary': 'Describe how new drugs are discovered, tested and approved before being used on patients.',
  'theory': [{'content': 'Throughout history, many important drugs were discovered from NATURAL SOURCES:\n'
                         '\n'
                         'PENICILLIN — discovered by Alexander Fleming (1928) from the Penicillium mould. He noticed '
                         'bacteria on a petri dish were being killed near a mould contamination.\n'
                         '\n'
                         'ASPIRIN — derived from salicylic acid found in willow bark. Used as a pain reliever for '
                         'centuries before the active compound was isolated.\n'
                         '\n'
                         'MORPHINE — derived from opium poppies — a powerful painkiller still used today.\n'
                         '\n'
                         'QUININE — extracted from cinchona tree bark — historically the main treatment for malaria.\n'
                         '\n'
                         'Modern drug discovery also uses:\n'
                         'Synthetic chemistry — designing molecules in the laboratory.\n'
                         'Computer modelling — predicting how molecules interact with biological targets.\n'
                         'Biotechnology — using genetically modified organisms to produce medicines (e.g. human '
                         'insulin produced by GM bacteria).',
              'heading': 'Where New Drugs Come From'},
             {'content': 'Before any new drug is tested on humans, it must undergo PRE-CLINICAL TESTING:\n'
                         '\n'
                         'CELL CULTURES — the drug is tested on cells grown in the laboratory. Checks basic toxicity '
                         'and whether the drug has any biological effect.\n'
                         '\n'
                         "COMPUTER MODELS — simulate the drug's behaviour and interactions in the body before any "
                         'living organism is used.\n'
                         '\n'
                         'ANIMAL TESTING — the drug is tested on animals (usually mice or rats) to check:\n'
                         'Whether it is safe in a living organism.\n'
                         'How it is absorbed, distributed and broken down.\n'
                         'What side effects occur.\n'
                         'Whether it has any effect on the target disease.\n'
                         '\n'
                         'Many potential drugs fail at this stage and are abandoned. Only those that show promise and '
                         'acceptable safety proceed to human trials.',
              'heading': 'Pre-Clinical Testing'},
             {'content': 'Drugs that pass pre-clinical testing move to CLINICAL TRIALS — testing in human volunteers. '
                         'This happens in three phases:\n'
                         '\n'
                         'PHASE 1 — Safety:\n'
                         'Small group of healthy volunteers.\n'
                         'Very low doses given initially, then gradually increased.\n'
                         'Aim: check the drug is safe in humans and identify any side effects.\n'
                         '\n'
                         'PHASE 2 — Efficacy:\n'
                         'Larger group of patients who have the condition the drug treats.\n'
                         'Aim: check the drug actually works and find the optimal dose.\n'
                         '\n'
                         'PHASE 3 — Large-scale comparison:\n'
                         'Hundreds or thousands of patients.\n'
                         'The drug is compared to either an EXISTING TREATMENT or a PLACEBO.\n'
                         'DOUBLE-BLIND TRIALS are used — neither the patients nor the doctors administering the trial '
                         'know who is receiving the real drug or the placebo. This eliminates bias.\n'
                         'A PLACEBO is an inactive dummy treatment (e.g. a sugar pill) that looks identical to the '
                         'real drug. Used to control for the PLACEBO EFFECT — where patients improve simply because '
                         'they believe they are receiving treatment.\n'
                         '\n'
                         'If Phase 3 is successful, the drug is submitted for regulatory approval. In the UK this is '
                         'the MHRA (Medicines and Healthcare products Regulatory Agency).',
              'heading': 'Clinical Trials — Testing on Humans'},
             {'content': 'Thalidomide was developed in the 1950s as a sedative and treatment for morning sickness in '
                         'pregnancy.\n'
                         '\n'
                         'It had not been adequately tested for effects on developing embryos.\n'
                         '\n'
                         'When taken by pregnant women, it caused severe birth defects — particularly abnormal limb '
                         'development (phocomelia — very short or absent limbs).\n'
                         '\n'
                         'An estimated 10,000 babies were affected worldwide before the drug was withdrawn in 1961.\n'
                         '\n'
                         'This case led directly to much stricter drug testing requirements worldwide — particularly '
                         'the requirement to test drugs on pregnant animals before use in humans.\n'
                         '\n'
                         "Thalidomide's lesson: drugs must be tested thoroughly for ALL potential uses and ALL "
                         'population groups, including pregnant women.\n'
                         '\n'
                         'Interestingly, thalidomide is now used again under very strict controls to treat some '
                         'cancers (multiple myeloma) and leprosy — illustrating that even a harmful drug can have safe '
                         'medical uses in the right context.',
              'heading': 'Thalidomide — A Cautionary Tale'}],
  'title': 'Drug Discovery and Development',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Plants do NOT have an immune system like animals — no antibodies, no lymphocytes, no phagocytes. '
                    'Their defences are physical (walls, wax, bark) and chemical (poisons, antimicrobials). They are '
                    'passive or triggered responses, not a learned adaptive immune system.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'plant-disease-detection-defence',
  'key_note': 'Plant physical defences: cell walls, waxy cuticle, bark, thorns, closing stomata. Chemical defences: '
              'antibacterial compounds (e.g. allicin), poisons/alkaloids (e.g. nicotine, caffeine, quinine). Active '
              'responses: hypersensitive response (kills cells around infection), systemic acquired resistance.',
  'matching': {'instruction': 'Sort each plant defence into physical or chemical.',
               'pairs': [('Physical', 'Cell walls — rigid cellulose barrier around each cell'),
                         ('Physical', 'Waxy cuticle — waterproof surface layer prevents colonisation'),
                         ('Chemical', 'Nicotine in tobacco — highly toxic to insects, deters feeding'),
                         ('Physical', 'Thorns — deter herbivores from eating the plant'),
                         ('Chemical', 'Allicin in garlic — antibacterial and antifungal compound'),
                         ('Chemical', 'Tannins in oak bark — bitter taste deters herbivores')],
               'title': 'Physical or Chemical Plant Defence?'},
  'quiz': [{'opts': [('Rose black spot — a fungal disease caused by Diplocarpon rosae', True),
                     ('Tobacco mosaic virus — a viral disease causing discolouration', False),
                     ('Salmonella — a bacterial infection from contaminated soil', False),
                     ('The plant is simply overwatered and needs less water', False)],
            'q': 'A gardener notices black spots on their rose leaves and the leaves are turning yellow. What is most '
                 'likely causing this?',
            'wrong_explanations': {1: 'TMV causes a mosaic pattern of light and dark green/yellow patches — not '
                                      'specific black spots with yellowing leaves around them.',
                                   2: 'Salmonella affects animals, not plants — it does not cause leaf spots in roses.',
                                   3: 'Overwatering can cause some yellowing, but the distinctive BLACK SPOTS '
                                      'specifically indicate rose black spot fungal infection.'}},
           {'opts': [('It provides a waterproof physical barrier that prevents pathogens from landing and colonising '
                      'the leaf surface',
                      True),
                     ('It contains antibiotics that kill any bacteria landing on the leaf', False),
                     ('It absorbs UV radiation to prevent DNA damage in leaf cells', False),
                     ('It makes leaves slippery so insects cannot grip and feed on them', False)],
            'q': 'Why does the waxy cuticle on leaves help protect the plant from disease?',
            'wrong_explanations': {1: 'The cuticle does not contain antibiotics — it is a physical, waterproof '
                                      'barrier. Plant chemical defences (like tannins or allicin) are separate from '
                                      'the cuticle.',
                                   2: 'UV protection is a secondary function in some plants — but the PRIMARY '
                                      'defensive role of the cuticle is as a physical barrier to pathogens and water '
                                      'loss.',
                                   3: 'Waxiness can make leaves slippery, but the main function is waterproofing — '
                                      'creating an inhospitable surface for pathogen growth.'}},
           {'opts': [('The plant rapidly kills cells around an infection site, creating a dead zone that contains the '
                      'pathogen and prevents it spreading',
                      True),
                     ('The plant produces excess antibodies to destroy the invading pathogen', False),
                     ('The plant overreacts to harmless stimuli and closes all its stomata', False),
                     ('The plant produces spores to spread its own genetic material before dying', False)],
            'q': 'What is the hypersensitive response in plants?',
            'wrong_explanations': {1: "Plants don't produce antibodies — that is an animal immune system response. "
                                      "Plants' active responses involve chemical signalling and cell death.",
                                   2: "Closing stomata IS a response to pathogens — but the 'hypersensitive response' "
                                      'specifically refers to deliberately killing cells around the infection site as '
                                      'a containment strategy.',
                                   3: 'Sporulation is a reproductive or survival strategy in some fungi and bacteria — '
                                      'not part of the plant hypersensitive response.'}}],
  'rp': None,
  'spec': '4.3.5',
  'summary': 'Describe how plant diseases are identified and how plants defend themselves against pathogens and pests.',
  'theory': [{'content': 'Plants can be infected by bacteria, viruses, fungi and other parasites — just like animals. '
                         'Recognising disease symptoms is important for farmers, gardeners and conservationists.\n'
                         '\n'
                         'Common symptoms of plant disease:\n'
                         'STUNTED GROWTH — plant is smaller or grows more slowly than expected for its age and growing '
                         'conditions.\n'
                         'SPOTS ON LEAVES — discoloured patches, often black, brown or orange.\n'
                         'AREAS OF DECAY (ROT) — brown, soft, collapsing tissue in stems, roots or fruit.\n'
                         'ABNORMAL GROWTHS — unusual swellings, galls or distorted structures.\n'
                         'MALFORMED LEAVES OR STEMS — twisted, curled or distorted plant parts.\n'
                         'DISCOLOURATION — yellowing (chlorosis), bleaching, mosaic patterns.\n'
                         '\n'
                         'How to identify the specific cause:\n'
                         'Look up symptoms in a plant disease identification guide or database.\n'
                         'Send a sample to a laboratory for microscopic examination.\n'
                         'Test using specific diagnostic kits (e.g. lateral flow tests for specific pathogens).\n'
                         'Observe when and where the disease appears — conditions often give clues (e.g. fungal '
                         'diseases favour wet, warm weather).',
              'heading': 'Identifying Plant Disease'},
             {'content': 'Plants have evolved a range of physical defences that act as barriers to prevent pathogens '
                         'and pests from entering:\n'
                         '\n'
                         'CELL WALLS made of cellulose — provide a rigid physical barrier around each cell. Much '
                         'harder for pathogens to penetrate than a soft cell membrane alone.\n'
                         '\n'
                         'WAXY CUTICLE on leaves and stems — a waterproof, waxy layer secreted by epidermal cells. '
                         'Prevents pathogens from landing and colonising the leaf surface. Also reduces water loss.\n'
                         '\n'
                         'BARK on woody stems — tough outer layers protect living tissue (phloem and cambium) '
                         'underneath from physical damage and pathogen entry.\n'
                         '\n'
                         'THORNS and SPINES — physical deterrents to herbivores, reducing the chances of wounds '
                         'through which pathogens can enter.\n'
                         '\n'
                         'CLOSING OF STOMATA — when plants detect pathogen attack, they can close stomata to prevent '
                         'pathogen entry through these openings.',
              'heading': 'Physical Defences in Plants'},
             {'content': 'Plants also produce a wide range of chemicals that deter herbivores and fight pathogens:\n'
                         '\n'
                         'ANTIBACTERIAL COMPOUNDS — some plants produce substances with antimicrobial properties:\n'
                         'Allicin in garlic — shown to have antibacterial and antifungal activity.\n'
                         'Tannins in oak bark and tea leaves — bitter astringent compounds that deter herbivores and '
                         'have some antimicrobial properties.\n'
                         '\n'
                         'POISONS (ALKALOIDS) — plants produce toxic secondary metabolites to deter animals from '
                         'eating them:\n'
                         'Nicotine in tobacco plants — highly toxic to insects (used as an insecticide).\n'
                         'Caffeine in coffee and tea plants — deters insects from feeding.\n'
                         'Quinine in cinchona trees — bitter taste deters herbivores; also has antimicrobial '
                         'properties.\n'
                         'Digitalis (foxglove) — toxic to vertebrates including humans if eaten in large quantities.\n'
                         '\n'
                         'INSECT-REPELLING COMPOUNDS — volatile chemicals released from leaves deter insects from '
                         'landing and laying eggs.\n'
                         '\n'
                         'STICKY RESINS and LATEX — trap insects on the surface or clog their mouthparts if they try '
                         'to feed.',
              'heading': 'Chemical Defences in Plants'},
             {'content': 'Plants can also mount active responses when they detect pathogen invasion:\n'
                         '\n'
                         'HYPERSENSITIVE RESPONSE — when a pathogen is detected, the plant rapidly KILLS the cells '
                         'immediately surrounding the infection site, creating a zone of dead cells.\n'
                         'This dead zone acts as a firebreak — the pathogen cannot spread through dead cells, '
                         'containing the infection.\n'
                         '\n'
                         'SYSTEMIC ACQUIRED RESISTANCE (SAR) — after a localised infection, the whole plant can become '
                         'more resistant to future attacks.\n'
                         'The plant produces signalling molecules (like salicylic acid) that travel to uninfected '
                         "parts of the plant, 'warning' them to prepare chemical defences.\n"
                         '\n'
                         'Many of the chemicals plants produce for defence have also been used by humans:\n'
                         'Aspirin derived from salicylic acid.\n'
                         'Quinine — antimalarial drug.\n'
                         'Morphine and codeine — painkillers from poppies.\n'
                         'Many modern medicines originated as plant defence chemicals.',
              'heading': 'Responding to Attack'}],
  'title': 'Plant Disease Detection and Defence',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Monoclonal antibodies are NOT the same as normal antibodies — they are IDENTICAL copies from ONE '
                    'clone, all specific to ONE antigen. Normal (polyclonal) antibodies are a mixture. Also: '
                    'monoclonal antibodies in cancer treatment target the cancer cells specifically — this is why they '
                    'cause fewer side effects than chemotherapy (which kills all rapidly dividing cells).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'monoclonal-antibodies',
  'key_note': 'Monoclonal antibodies: identical antibodies from one B-lymphocyte clone. Made by fusing lymphocytes '
              'with tumour cells → hybridoma cells. Uses: pregnancy tests (detect hCG), cancer treatment (targeted '
              'therapy), diagnostic tests (COVID LFT). More specific than chemotherapy.',
  'matching': {'instruction': 'Match each use to how monoclonal antibodies are used.',
               'pairs': [('Pregnancy test',
                          'Detects hCG hormone — monoclonal antibodies bind to hCG in urine, producing a colour '
                          'change'),
                         ('Cancer treatment',
                          'Antibodies bind to specific proteins on cancer cell surfaces — blocking growth or '
                          'delivering drugs'),
                         ('COVID lateral flow test',
                          'Antibodies detect specific viral antigens — rapid diagnostic result'),
                         ('Hybridoma cell',
                          'Fused B-lymphocyte + tumour cell — divides indefinitely and produces specific antibodies')],
               'title': 'Match the Monoclonal Antibody Use'},
  'quiz': [{'opts': [('A cell formed by fusing a lymphocyte with a tumour cell — it divides indefinitely AND produces '
                      'specific antibodies',
                      True),
                     ('A lymphocyte that has been infected by a virus — producing antibodies to fight it', False),
                     ('A stem cell that can differentiate into any type of immune cell', False),
                     ('A cancer cell that has been trained to produce antibodies by injecting it with antigens',
                      False)],
            'q': 'What is a hybridoma cell and why is it useful?',
            'wrong_explanations': {1: 'A virus-infected lymphocyte would produce antibodies against the virus — not a '
                                      'hybridoma.',
                                   2: 'Stem cells differentiate into specialised cells — hybridomas are a specific '
                                      'fusion product for antibody production.',
                                   3: "Cancer cells don't produce antibodies naturally — they are fused with "
                                      'lymphocytes to give them this ability.'}},
           {'opts': [('They bind specifically to proteins on cancer cell surfaces — leaving healthy cells unaffected',
                      True),
                     ('They are injected directly into tumours — not into the bloodstream', False),
                     ("They are made from the patient's own cells — so they know which cells are cancerous", False),
                     ('They kill cancer cells instantly — unlike chemotherapy which takes weeks', False)],
            'q': 'Why are monoclonal antibodies more targeted than conventional chemotherapy for cancer treatment?',
            'wrong_explanations': {1: 'Monoclonal antibodies can be given intravenously — the specificity comes from '
                                      'their precise binding to cancer-cell antigens, not from targeted injection.',
                                   2: "Current monoclonal antibodies are generally not made from the patient's own "
                                      'cells — they are produced from mouse or humanised cell lines.',
                                   3: 'Both treatments take time to work — the advantage of monoclonal antibodies is '
                                      'specificity, not speed.'}},
           {'opts': [('The antibodies bind ONLY to hCG molecules — not to other hormones or substances in urine', True),
                     ("The antibodies were taken from a pregnant woman's blood", False),
                     ('The antibodies can detect any hormone in the body', False),
                     ('The test uses polyclonal antibodies for a broad detection range', False)],
            'q': 'A pregnancy test uses monoclonal antibodies specific to hCG. What does this mean?',
            'wrong_explanations': {1: 'The antibodies come from hybridoma cells cultured in a laboratory — not from a '
                                      'pregnant woman.',
                                   2: 'Monoclonal antibodies are highly specific to ONE antigen — detecting any '
                                      'hormone would require polyclonal antibodies or a panel of specific tests.',
                                   3: 'Pregnancy tests use MONOCLONAL antibodies — specific to hCG only. This '
                                      'specificity prevents false positives from other hormones.'}}],
  'rp': None,
  'spec': '4.3.5',
  'summary': 'Describe how monoclonal antibodies are produced and their uses in medicine and diagnosis.',
  'theory': [{'content': 'MONOCLONAL ANTIBODIES are identical antibodies produced from a single clone of B-lymphocytes '
                         '— they are all specific to exactly the same antigen.\n'
                         '\n'
                         'Normal antibodies are polyclonal — a mixture of different antibodies made by different '
                         'lymphocytes, each responding to slightly different parts of a pathogen.\n'
                         '\n'
                         'Monoclonal antibodies are MONOSPECIFIC — they bind to one specific target molecule with very '
                         'high precision. This makes them extremely useful tools in medicine, diagnosis and research.\n'
                         '\n'
                         'Key property: because they are produced from a single clone, every antibody is IDENTICAL — '
                         'same shape, same binding site, same specificity.',
              'heading': 'What Are Monoclonal Antibodies?'},
             {'content': 'Producing monoclonal antibodies involves a clever combination of lymphocytes (which make '
                         "antibodies but don't divide indefinitely) and tumour cells (which divide indefinitely but "
                         "don't make useful antibodies).\n"
                         '\n'
                         'STEPS:\n'
                         "1. Inject a mouse with the target antigen → the mouse's immune system produces specific "
                         'lymphocytes.\n'
                         "2. Remove the lymphocytes from the mouse's spleen.\n"
                         '3. FUSE the lymphocytes with TUMOUR CELLS (myeloma cells) — this creates HYBRIDOMA CELLS.\n'
                         '4. Hybridoma cells divide indefinitely AND produce the specific antibody.\n'
                         '5. Select and clone the hybridoma cells that produce the desired antibody.\n'
                         '6. Culture the clone in large quantities → produces large amounts of identical monoclonal '
                         'antibodies.\n'
                         '7. Purify and collect the antibodies.\n'
                         '\n'
                         "Hybridoma cells are sometimes called 'immortal antibody factories' — they combine the "
                         'antibody-producing ability of B-cells with the unlimited division of cancer cells.',
              'heading': 'How Monoclonal Antibodies Are Produced'},
             {'content': 'PREGNANCY TESTS:\n'
                         'Detect the hormone hCG (human chorionic gonadotropin) — produced only during pregnancy.\n'
                         'Monoclonal antibodies specific to hCG are on the test strip.\n'
                         'If hCG is present in urine, it binds to the antibodies → produces a visible colour change.\n'
                         'Quick, accurate and specific — one of the most widely used diagnostic tests.\n'
                         '\n'
                         'CANCER TREATMENT (targeted therapy):\n'
                         'Monoclonal antibodies can be designed to bind to SPECIFIC PROTEINS on cancer cell surfaces.\n'
                         'This can: block signals that tell cancer cells to divide; mark cancer cells for destruction '
                         'by the immune system; or carry a drug/radioactive substance directly to the cancer cell '
                         '(magic bullet therapy).\n'
                         'Example: Herceptin (trastuzumab) binds to HER2 receptors on some breast cancer cells — '
                         'blocking tumour growth.\n'
                         'Advantage over chemotherapy: targets cancer cells specifically — less damage to healthy '
                         'cells.\n'
                         '\n'
                         'DIAGNOSTIC TESTS:\n'
                         'Used in lateral flow tests (e.g. COVID-19 LFTs, flu tests) — detect specific antigens '
                         'quickly.\n'
                         'Used in blood tests to detect hormones, pathogens or cancer markers.\n'
                         'Used in research to locate specific molecules in tissues (immunohistochemistry).\n'
                         '\n'
                         'SIDE EFFECTS:\n'
                         'Monoclonal antibodies can cause fever, rashes, joint pain, low blood pressure.\n'
                         'Some trigger allergic reactions — the immune system may respond to the foreign antibody '
                         'proteins.\n'
                         'Long-term effects are still being researched for newer treatments.',
              'heading': 'Uses of Monoclonal Antibodies'}],
  'title': 'Monoclonal Antibodies',
  'triple_only': None,
  'variables': []}],

"bioenergetics": [{'common_mistake': 'Photosynthesis only happens in LIGHT and only in cells with CHLOROPLASTS. Respiration happens ALL '
                    "THE TIME in ALL living cells. Never say 'plants don't respire' — they do, constantly. In bright "
                    'light they photosynthesise faster than they respire, which is why we see net O₂ production.',
  'equations': ['6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂  (light energy)'],
  'fifas': [],
  'higher': None,
  'id': 'photosynthesis',
  'key_note': 'Photosynthesis: CO₂ + H₂O → glucose + O₂. Needs light energy. Occurs in chloroplasts. Endothermic — '
              'stores energy. Chlorophyll absorbs red and blue light, reflects green.',
  'matching': {'instruction': 'Match each item to the correct category.',
               'pairs': [('Reactant', 'Carbon dioxide — enters through stomata from the air'),
                         ('Reactant', 'Water — absorbed by roots, travels up through xylem'),
                         ('Product', 'Glucose — used for energy, building and storage'),
                         ('Product', 'Oxygen — released as a by-product through stomata'),
                         ('Where it happens', 'Chloroplasts — contain chlorophyll that absorbs light'),
                         ('Energy type', 'Endothermic — light energy absorbed and stored in glucose')],
               'title': 'Photosynthesis — Match the Term'},
  'quiz': [{'opts': [('Carbon dioxide + water → glucose + oxygen', True),
                     ('Glucose + oxygen → carbon dioxide + water', False),
                     ('Carbon dioxide + glucose → water + oxygen', False),
                     ('Water + oxygen → carbon dioxide + glucose', False)],
            'q': 'What is the word equation for photosynthesis?',
            'wrong_explanations': {1: 'That is the equation for AEROBIC RESPIRATION — the exact reverse of '
                                      'photosynthesis.',
                                   2: 'CO₂ and glucose are never on the same side. CO₂ is a reactant; glucose is a '
                                      'product of photosynthesis.',
                                   3: "Oxygen is a PRODUCT — it is produced by photosynthesis and released. It doesn't "
                                      'go in.'}},
           {'opts': [('Chlorophyll reflects green light — it absorbs red and blue wavelengths instead', True),
                     ('Plants produce green light as a by-product of photosynthesis', False),
                     ('Green light is needed most for photosynthesis so it is absorbed', False),
                     ('All plant cells are filled with green-coloured water', False)],
            'q': 'Why do plants appear green?',
            'wrong_explanations': {1: "Plants don't produce or emit light — they only reflect it. Green is the colour "
                                      'reflected, not produced.',
                                   2: 'Green is actually the LEAST useful wavelength for photosynthesis — red and blue '
                                      'are absorbed most efficiently.',
                                   3: 'Cell sap in vacuoles is usually colourless — the green colour comes from '
                                      'chlorophyll in chloroplasts.'}},
           {'opts': [('No — photosynthesis requires light energy and cannot occur in darkness', True),
                     ('Yes — plants always photosynthesise, day and night', False),
                     ('Yes — plants store light energy during the day and use it at night', False),
                     ("Only partially — stomata close so photosynthesis slows but doesn't stop", False)],
            'q': 'In a dark room, does a plant carry out photosynthesis?',
            'wrong_explanations': {1: 'Respiration occurs day and night — but PHOTOSYNTHESIS specifically requires '
                                      'light energy. Without light, it stops completely.',
                                   2: 'Plants do store glucose — but photosynthesis itself cannot run without light. '
                                      'The stored glucose is used in respiration at night.',
                                   3: 'Stomata closing does reduce gas exchange in the dark, but photosynthesis stops '
                                      'specifically because there is no light energy, not because stomata are '
                                      'closed.'}},
           {'opts': [('Chloroplasts — which contain the chlorophyll pigment that absorbs light', True),
                     ('Mitochondria — which produce the energy needed for photosynthesis', False),
                     ('The nucleus — which contains the genes controlling photosynthesis', False),
                     ('The vacuole — which stores the raw materials for photosynthesis', False)],
            'q': 'Where exactly in a plant cell does photosynthesis take place?',
            'wrong_explanations': {1: 'Mitochondria are the site of RESPIRATION — they produce ATP energy but do not '
                                      'carry out photosynthesis.',
                                   2: 'The nucleus contains the DNA instructions but is not the location where '
                                      'photosynthesis reactions actually occur.',
                                   3: 'The vacuole stores cell sap (sugars and salts) — it is not involved in carrying '
                                      'out photosynthesis.'}}],
  'rp': 'RP5 — Investigate the effect of light intensity on the rate of photosynthesis using aquatic plants (e.g. '
        'Elodea or Cabomba). Count oxygen bubbles per minute at different distances from a lamp.',
  'spec': '4.4.1.1',
  'summary': 'Describe photosynthesis — what it is, where it happens and what the equation means.',
  'theory': [{'content': 'Photosynthesis is the process by which green plants (and some other organisms) use LIGHT '
                         'ENERGY to make their own food.\n'
                         '\n'
                         'It converts two simple raw materials — carbon dioxide and water — into glucose and oxygen.\n'
                         '\n'
                         'Photosynthesis is an ENDOTHERMIC reaction — it takes in energy (from light) and stores it as '
                         'chemical energy in glucose molecules.\n'
                         '\n'
                         'This is the opposite of respiration, which releases energy from glucose.\n'
                         '\n'
                         'Photosynthesis is the foundation of almost all food chains on Earth — it is the process that '
                         "converts the Sun's energy into a form that living organisms can use.",
              'heading': 'What is Photosynthesis?'},
             {'content': 'Photosynthesis takes place in the CHLOROPLASTS — organelles found in the cells of green '
                         'plants and algae.\n'
                         '\n'
                         'Chloroplasts contain a green pigment called CHLOROPHYLL.\n'
                         '\n'
                         'Chlorophyll absorbs LIGHT ENERGY — mainly red and blue wavelengths of light.\n'
                         '\n'
                         'Green light is REFLECTED by chlorophyll — this is why plants appear green to our eyes.\n'
                         '\n'
                         'Not all plant cells have chloroplasts:\n'
                         'Leaf palisade cells — packed with chloroplasts (maximum photosynthesis).\n'
                         'Root cells — no chloroplasts (underground, no light available).\n'
                         'Storage cells — no chloroplasts (no photosynthesis needed).',
              'heading': 'Where Photosynthesis Happens'},
             {'content': 'Word equation:\n'
                         'carbon dioxide + water → glucose + oxygen\n'
                         '\n'
                         'Symbol equation:\n'
                         '6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂\n'
                         '\n'
                         'This equation requires LIGHT ENERGY — usually written above the arrow.\n'
                         '\n'
                         'REACTANTS (what goes in):\n'
                         'Carbon dioxide (CO₂) — absorbed from the air through stomata in the leaves.\n'
                         'Water (H₂O) — absorbed from the soil by root hair cells, transported up to leaves through '
                         'xylem.\n'
                         '\n'
                         'PRODUCTS (what comes out):\n'
                         'Glucose (C₆H₁₂O₆) — a sugar used by the plant for energy and building materials.\n'
                         'Oxygen (O₂) — released as a by-product through stomata.',
              'heading': 'The Equation for Photosynthesis'},
             {'content': 'Students often confuse these two processes. Here is the key difference:\n'
                         '\n'
                         'PHOTOSYNTHESIS:\n'
                         'Occurs ONLY in light.\n'
                         'Occurs ONLY in cells that have chloroplasts.\n'
                         'Takes in CO₂ and water → makes glucose and O₂.\n'
                         'Stores energy in glucose (endothermic).\n'
                         '\n'
                         'RESPIRATION:\n'
                         'Occurs ALL THE TIME — day and night.\n'
                         'Occurs in ALL living cells (including animals, bacteria).\n'
                         'Breaks down glucose + O₂ → CO₂ and water.\n'
                         'Releases energy from glucose (exothermic).\n'
                         '\n'
                         'In BRIGHT LIGHT: rate of photosynthesis > rate of respiration → net release of oxygen.\n'
                         'In LOW LIGHT: rate of photosynthesis < rate of respiration → net release of carbon dioxide.\n'
                         'At the COMPENSATION POINT: rate of photosynthesis = rate of respiration → no net gas '
                         'exchange.',
              'heading': 'Photosynthesis vs Respiration'}],
  'title': 'Photosynthesis',
  'triple_only': None,
  'variables': []},
 {'common_mistake': "When a graph of photosynthesis rate levels off (plateaus), students often say 'the plant has run "
                    "out of chlorophyll' or 'there is no more light'. The correct answer is that ANOTHER FACTOR has "
                    "become limiting — usually CO₂ or temperature. The plant hasn't run out of anything — a different "
                    'factor is now the bottleneck.',
  'equations': [],
  'fifas': [],
  'higher': 'Inverse square law: light intensity is proportional to 1/distance². Doubling the distance from the lamp '
            'quarters the light intensity. If a plant is 10 cm from the lamp and moved to 20 cm, light intensity drops '
            'to 1/4. Students should be able to apply this to RP5 data and interpret rate vs light intensity graphs — '
            'explaining plateau regions as evidence of another limiting factor.',
  'id': 'rate-of-photosynthesis',
  'key_note': 'Three limiting factors: light intensity, CO₂ concentration, temperature. Rate increases with each up to '
              'a point, then another factor limits. Above optimum temperature — enzymes denature, rate falls.',
  'matching': {'instruction': 'Match each condition to what happens to the rate of photosynthesis.',
               'pairs': [('Low light intensity',
                          'Not enough energy — rate is slow even if CO₂ and temperature are optimal'),
                         ('Low CO₂ concentration', 'Not enough raw material to build glucose — rate is slow'),
                         ('Low temperature',
                          'Enzymes have less kinetic energy — fewer successful collisions, slow rate'),
                         ('Temperature above optimum', 'Enzymes denature permanently — rate falls sharply to zero'),
                         ('Rate levels off (plateau)',
                          'Another factor has become limiting — not that the plant ran out of chlorophyll')],
               'title': 'Match the Limiting Factor to its Effect'},
  'quiz': [{'opts': [('Temperature — enzyme activity is now the bottleneck', True),
                     ('Light intensity — the plant needs even more light', False),
                     ('Carbon dioxide — the plant needs more CO₂', False),
                     ('The plant has used up all its chlorophyll', False)],
            'q': 'A plant is given very bright light and high CO₂. The rate of photosynthesis stops increasing. What '
                 'is now the most likely limiting factor?',
            'wrong_explanations': {1: 'Light is already very bright — it is NOT the limiting factor.',
                                   2: 'CO₂ is already high — it is NOT the limiting factor.',
                                   3: 'Chlorophyll is not used up — it is a pigment that absorbs light and is not '
                                      'consumed. Another factor is now limiting the rate.'}},
           {'opts': [('Light intensity is the limiting factor at that distance — reducing it reduces the rate of '
                      'photosynthesis',
                      True),
                     ('The plant needs to be closer to warm water', False),
                     ('CO₂ levels decrease as the lamp moves further away', False),
                     ('The plant becomes stressed when the lamp moves', False)],
            'q': 'In an experiment, moving a lamp further from an aquatic plant reduces the bubble count. What does '
                 'this show?',
            'wrong_explanations': {1: 'The lamp produces light, not heat — the water bath controls temperature.',
                                   2: "Moving a lamp doesn't change CO₂ levels — CO₂ comes from the water/air around "
                                      'the plant.',
                                   3: "Plants don't have a stress response in the same way animals do — the reduced "
                                      'bubble rate is a direct physical consequence of reduced light energy.'}},
           {'opts': [('Enzymes in the chloroplast denature — their active sites change shape permanently and can no '
                      'longer function',
                      True),
                     ('The plant closes its stomata to prevent water loss in the heat', False),
                     ('High temperatures cause chlorophyll to break down permanently', False),
                     ('More CO₂ evaporates from the leaf at higher temperatures', False)],
            'q': 'Why does photosynthesis rate decrease at temperatures above the optimum?',
            'wrong_explanations': {1: 'Stomata closing reduces CO₂ entry — but the primary reason for rate decrease '
                                      'above optimum temperature is ENZYME DENATURATION.',
                                   2: 'Chlorophyll can be affected by extreme heat, but at typical above-optimum '
                                      'temperatures (e.g. 45–50°C) the main limiting effect is enzyme denaturation.',
                                   3: "CO₂ is a gas that dissolves in water — it doesn't 'evaporate from the leaf'. "
                                      'The CO₂ supply issue is about stomata and diffusion rates.'}}],
  'rp': 'RP5 — Investigate the effect of light intensity on rate of photosynthesis using aquatic plants. Count bubbles '
        'per minute. Move lamp to change light intensity. Control CO₂ (add sodium bicarbonate) and temperature.',
  'spec': '4.4.1.2',
  'summary': 'Explain what limits the rate of photosynthesis and how to investigate it.',
  'theory': [{'content': 'A LIMITING FACTOR is any factor that, when in short supply, restricts the rate of a reaction '
                         '— even if all other factors are in abundance.\n'
                         '\n'
                         'Imagine a factory with three workers on a production line. If one worker is absent (or '
                         'working slowly), the whole line slows down — even if the other two are working perfectly.\n'
                         '\n'
                         'For photosynthesis, the three main limiting factors are:\n'
                         '1. LIGHT INTENSITY\n'
                         '2. CARBON DIOXIDE CONCENTRATION\n'
                         '3. TEMPERATURE\n'
                         '\n'
                         'At any given moment, the rate of photosynthesis is limited by whichever of these three '
                         'factors is in shortest supply.',
              'heading': 'What is a Limiting Factor?'},
             {'content': 'Light provides the ENERGY for photosynthesis.\n'
                         '\n'
                         'As light intensity INCREASES:\n'
                         'More energy available → chlorophyll absorbs more light → faster reactions → rate of '
                         'photosynthesis increases.\n'
                         '\n'
                         'But once light is no longer the limiting factor, increasing it further has NO effect — '
                         'another factor takes over as the bottleneck.\n'
                         '\n'
                         'In very LOW light:\n'
                         'Rate is slow — not enough energy to drive the reactions.\n'
                         'This is why plants grow more slowly in winter (shorter days, lower light levels).\n'
                         '\n'
                         'EVIDENCE in experiments:\n'
                         'Aquatic plants (e.g. Elodea) produce oxygen bubbles.\n'
                         'Moving a lamp CLOSER increases bubble rate.\n'
                         'Moving it FURTHER decreases bubble rate.\n'
                         '\n'
                         'NOTE: Light intensity decreases with distance from a source.',
              'heading': 'Light Intensity'},
             {'content': 'Carbon dioxide is a RAW MATERIAL for photosynthesis — needed to build glucose molecules.\n'
                         '\n'
                         'As CO₂ concentration INCREASES:\n'
                         'More raw material available → more glucose can be produced → rate increases.\n'
                         '\n'
                         'If CO₂ falls too low:\n'
                         'Rate is limited even if light and temperature are optimal.\n'
                         '\n'
                         'This is why GREENHOUSES often pump extra CO₂ into the air — raising CO₂ concentration above '
                         'the normal atmospheric level (~0.04%) can significantly increase crop yields.\n'
                         '\n'
                         'Normal atmospheric CO₂ is quite low — for many plants, CO₂ is often the limiting factor '
                         'during a warm, sunny day.',
              'heading': 'Carbon Dioxide Concentration'},
             {'content': 'Temperature affects the ENZYMES that control the reactions of photosynthesis.\n'
                         '\n'
                         'As temperature INCREASES (below optimum):\n'
                         'Enzyme molecules and substrate molecules have more kinetic energy.\n'
                         'More frequent and more successful collisions.\n'
                         'Rate of photosynthesis increases.\n'
                         '\n'
                         'At OPTIMUM TEMPERATURE (~25–40°C depending on the plant):\n'
                         'Maximum rate of photosynthesis.\n'
                         '\n'
                         'ABOVE OPTIMUM TEMPERATURE:\n'
                         'Enzymes in the chloroplast BEGIN TO DENATURE.\n'
                         'Active site shape changes permanently.\n'
                         'Enzyme-substrate complexes can no longer form.\n'
                         'Rate of photosynthesis FALLS SHARPLY — eventually to zero.\n'
                         '\n'
                         'This explains why very hot conditions reduce photosynthesis even in good light with plenty '
                         'of CO₂ — the enzyme system has broken down.',
              'heading': 'Temperature'},
             {'content': 'The rate of photosynthesis can be measured by:\n'
                         'Counting the number of O₂ bubbles produced per minute by an aquatic plant.\n'
                         'Measuring the volume of O₂ collected over a set time.\n'
                         'Using a CO₂ sensor to measure how fast CO₂ is being absorbed.\n'
                         '\n'
                         'In RP5 you investigate the effect of LIGHT INTENSITY:\n'
                         'Set up a beaker of water with an aquatic plant (Elodea or Cabomba).\n'
                         'Place a lamp at a measured distance.\n'
                         'Count bubbles per minute (or collect gas).\n'
                         'Move the lamp to different distances and repeat.\n'
                         'Plot a graph of rate (bubbles/min) against light intensity.\n'
                         '\n'
                         'Key controls:\n'
                         'Keep temperature constant (use a water bath or ice).\n'
                         'Keep CO₂ constant (add sodium bicarbonate solution to the water).\n'
                         'This ensures only light intensity is the independent variable.',
              'heading': 'Investigating Photosynthesis Rate'}],
  'title': 'Rate of Photosynthesis',
  'triple_only': None,
  'variables': []},
 {'common_mistake': "Starch is stored instead of glucose because starch is INSOLUBLE — it doesn't affect osmosis. "
                    'Glucose is soluble and would draw water into cells by osmosis if it accumulated. Students often '
                    "say 'starch is easier to digest' — that's not the reason plants store starch instead of glucose.",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'uses-of-glucose',
  'key_note': 'Glucose uses: respiration (energy), cellulose (cell walls), starch (storage — insoluble), proteins '
              '(needs nitrate ions from soil), fats/oils (membranes, seeds). Starch stored not glucose because starch '
              'is insoluble.',
  'matching': {'instruction': 'Match each molecule to how it is made from glucose.',
               'pairs': [('Respiration', 'Glucose broken down to release ATP energy for all cell processes'),
                         ('Cellulose', 'Glucose polymerised to make plant cell walls — structural support'),
                         ('Starch', 'Glucose converted to insoluble storage carbohydrate in leaves, roots and seeds'),
                         ('Proteins', 'Glucose + nitrate ions → amino acids → proteins (enzymes, structure)'),
                         ('Fats and oils',
                          'Glucose converted to lipids — used in membranes and as energy-rich seed stores')],
               'title': 'Match the Use of Glucose'},
  'quiz': [{'opts': [("Starch is insoluble — it doesn't affect osmosis or water potential inside cells", True),
                     ('Starch contains more energy per molecule than glucose', False),
                     ('Starch is easier to transport around the plant than glucose', False),
                     ('Glucose would be eaten by bacteria if stored directly', False)],
            'q': 'Why do plants store glucose as starch rather than keeping it as glucose?',
            'wrong_explanations': {1: 'Glucose and starch (a polymer of glucose) contain the same energy per gram — '
                                      "starch isn't more energy-dense.",
                                   2: "It's actually GLUCOSE that is transported in the phloem (as sucrose) — not "
                                      'starch. Starch is specifically an insoluble store.',
                                   3: 'Bacteria can break down starch too — the reason is osmosis, not bacterial '
                                      'protection.'}},
           {'opts': [('Proteins — amino acids need nitrogen (from nitrates) to form the amino group', True),
                     ('Glucose — nitrates are needed for photosynthesis', False),
                     ('Starch — nitrate ions are needed to convert glucose to starch', False),
                     ('Cellulose — cell walls require nitrogen to polymerise glucose', False)],
            'q': 'A plant is grown in soil with no nitrate ions. Which molecule will it struggle to make?',
            'wrong_explanations': {1: 'Glucose is produced by photosynthesis using CO₂ and water — nitrates are not '
                                      'needed.',
                                   2: 'Starch is made from glucose polymerisation — no nitrogen is needed for this '
                                      'process.',
                                   3: 'Cellulose is made from glucose joined by glycosidic bonds — no nitrogen '
                                      'involved.'}},
           {'opts': [('Aerobic respiration — releasing energy (ATP) to power all cell processes', True),
                     ('Making starch — all glucose is stored for later use', False),
                     ("Building cell walls from cellulose — the plant's primary structural need", False),
                     ('Making proteins — converting glucose to amino acids', False)],
            'q': 'What is the main use of glucose in plants?',
            'wrong_explanations': {1: 'Not all glucose is stored — plants use glucose continuously for growth, which '
                                      'means some becomes cellulose, but energy supply via respiration is the primary '
                                      'ongoing use.',
                                   2: 'Cellulose is important but only for cell walls — energy supply through '
                                      'respiration is the primary ongoing requirement.',
                                   3: 'Protein synthesis is important, but requires nitrogen — not all glucose goes to '
                                      'proteins.'}}],
  'rp': None,
  'spec': '4.4.1.3',
  'summary': 'Describe how plants use the glucose produced by photosynthesis.',
  'theory': [{'content': 'After photosynthesis produces glucose, the plant uses it in several important ways.\n'
                         '\n'
                         "Glucose is the plant's primary fuel and building material — it is used for energy, for "
                         'constructing cell structures, and for making other essential molecules.\n'
                         '\n'
                         'Understanding the uses of glucose helps explain how plants grow, store energy and support '
                         'animal life.',
              'heading': 'What Does a Plant Do with Glucose?'},
             {'content': 'The PRIMARY use of glucose is AEROBIC RESPIRATION — breaking down glucose to release energy '
                         '(ATP).\n'
                         '\n'
                         'This energy powers everything the plant does:\n'
                         'Active transport — moving mineral ions into root cells against concentration gradients.\n'
                         'Cell division — growing new cells during growth.\n'
                         'Protein synthesis — making enzymes and structural proteins.\n'
                         'Movement — opening and closing stomata (guard cells).\n'
                         '\n'
                         'Respiration occurs in ALL living plant cells, day and night — using glucose produced by '
                         'photosynthesis.',
              'heading': 'Respiration'},
             {'content': 'Glucose molecules are joined together to form CELLULOSE — a structural carbohydrate.\n'
                         '\n'
                         'Cellulose makes up the CELL WALLS of plant cells — providing rigidity and structural '
                         'support.\n'
                         '\n'
                         'This is why plants can stand upright and have firm stems and leaves.\n'
                         '\n'
                         'Cellulose is the most abundant organic molecule on Earth — made entirely from glucose '
                         'produced by photosynthesis.',
              'heading': 'Making Cellulose'},
             {'content': 'When glucose is produced faster than it can be used, plants convert it into STARCH for '
                         'storage.\n'
                         '\n'
                         'Why starch and not glucose?\n'
                         'Glucose is SOLUBLE — it would dissolve in cell sap and change the water potential of cells, '
                         'causing osmosis problems.\n'
                         "Starch is INSOLUBLE — it does not dissolve, so it doesn't affect osmosis and can be packed "
                         'into cells safely.\n'
                         'Starch can be converted BACK to glucose when energy is needed.\n'
                         '\n'
                         'Where starch is stored:\n'
                         'Leaves — starch grains in chloroplasts and cells.\n'
                         'Roots — e.g. carrots, parsnips are swollen roots packed with starch.\n'
                         'Seeds — energy store for germination.\n'
                         'Tubers — e.g. potato tubers are storage organs filled with starch.',
              'heading': 'Making Starch for Storage'},
             {'content': 'PROTEINS:\n'
                         'Glucose provides the CARBON SKELETON for making amino acids.\n'
                         'NITRATE IONS (absorbed from the soil through roots) provide the NITROGEN needed to make the '
                         'amino group (–NH₂) part of amino acids.\n'
                         'Amino acids are joined to make PROTEINS — enzymes, structural proteins, transport proteins.\n'
                         '\n'
                         'FATS AND OILS:\n'
                         'Glucose is also used to make LIPIDS (fats and oils).\n'
                         'Used in cell membranes (phospholipids).\n'
                         'Used as energy-rich storage in seeds (oils in sunflower seeds, olive oil etc).\n'
                         'Also used to make the waxy cuticle on leaf surfaces.',
              'heading': 'Making Proteins and Fats'}],
  'title': 'Uses of Glucose from Photosynthesis',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'RESPIRATION is not the same as BREATHING. Breathing is ventilation — moving air in and out of '
                    'lungs. Respiration is the CHEMICAL PROCESS in cells that releases energy from glucose. Also: '
                    'aerobic respiration happens in MITOCHONDRIA — not in the nucleus, not in chloroplasts.',
  'equations': ['glucose + oxygen → carbon dioxide + water', 'C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O'],
  'fifas': [],
  'higher': 'ATP (adenosine triphosphate) is the immediate energy currency of cells — it directly powers muscle '
            'contraction, active transport, protein synthesis and cell division. Aerobic respiration produces ~36–38 '
            'ATP per glucose molecule. This compares to only ~2 ATP from anaerobic respiration — which is why aerobic '
            'respiration is much more efficient and is used for sustained activity.',
  'id': 'aerobic-respiration',
  'key_note': 'Aerobic respiration: glucose + oxygen → CO₂ + water. In mitochondria. Releases ~36–38 ATP. Continuous '
              'in all living cells. Exothermic — energy released.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Glucose', 'The fuel molecule broken down in respiration'),
                         ('Oxygen', 'Needed for aerobic respiration — allows complete breakdown of glucose'),
                         ('ATP', 'The energy molecule produced — directly powers all cell processes'),
                         ('Carbon dioxide', 'Waste product — produced when glucose is completely broken down'),
                         ('Mitochondria', 'The organelle where aerobic respiration takes place'),
                         ('Water', 'Produced when hydrogen from glucose combines with oxygen')],
               'title': 'Aerobic Respiration — Match the Term'},
  'quiz': [{'opts': [('Mitochondria', True), ('Chloroplasts', False), ('Nucleus', False), ('Ribosomes', False)],
            'q': 'Where in the cell does aerobic respiration take place?',
            'wrong_explanations': {1: 'Chloroplasts carry out PHOTOSYNTHESIS — they capture energy from light. '
                                      'Mitochondria RELEASE energy from glucose.',
                                   2: 'The nucleus contains DNA and controls the cell — it is not the site of aerobic '
                                      'respiration.',
                                   3: 'Ribosomes build proteins — they are not involved in energy release from '
                                      'glucose.'}},
           {'opts': [('Breathing moves air in and out of the lungs. Respiration is the chemical process in cells that '
                      'releases energy from glucose.',
                      True),
                     ('They are the same process — both refer to taking in oxygen and releasing carbon dioxide.',
                      False),
                     ('Breathing produces ATP. Respiration produces oxygen.', False),
                     ('Respiration only occurs in the lungs. Breathing occurs throughout the body.', False)],
            'q': 'What is the difference between respiration and breathing?',
            'wrong_explanations': {1: 'Breathing and respiration are NOT the same — confusing them is one of the most '
                                      'common biology mistakes. Breathing is a mechanical process; respiration is a '
                                      'chemical one.',
                                   2: 'Breathing takes in air (including O₂) — but ATP is produced by RESPIRATION in '
                                      'cells. Oxygen is produced by photosynthesis, not breathing.',
                                   3: 'Respiration occurs in ALL living cells throughout the body — not just the '
                                      'lungs.'}},
           {'opts': [('Muscle cells need much more ATP energy for contraction — more mitochondria produce more ATP',
                      True),
                     ('Mitochondria are heavier than other organelles and sink to the bottom of active cells', False),
                     ('Skin cells are too small to contain many mitochondria', False),
                     ('Muscle cells use more oxygen, so they need more mitochondria to absorb it', False)],
            'q': 'Why do muscle cells contain more mitochondria than skin cells?',
            'wrong_explanations': {1: "Organelles don't 'sink' — they are distributed throughout the cytoplasm based "
                                      'on cellular need.',
                                   2: "Skin cells are actually similar in size to muscle cells — it's energy demand, "
                                      'not size, that determines mitochondria number.',
                                   3: 'Mitochondria do use oxygen in respiration — but they use it to produce ATP. The '
                                      'driving factor for more mitochondria is the ENERGY DEMAND, not simply oxygen '
                                      'availability.'}}],
  'rp': None,
  'spec': '4.4.2.1',
  'summary': 'Describe aerobic respiration — what it is, where it happens and what it produces.',
  'theory': [{'content': 'Respiration is the process by which ALL living cells release energy from organic molecules — '
                         'mainly GLUCOSE — to produce ATP (adenosine triphosphate).\n'
                         '\n'
                         'ATENTION: Respiration is NOT the same as BREATHING. Breathing (ventilation) moves air in and '
                         'out of the lungs. Respiration is a CHEMICAL PROCESS happening inside every cell.\n'
                         '\n'
                         'ATP is the ENERGY CURRENCY of cells — it is the molecule that directly powers all cellular '
                         'processes:\n'
                         'Muscle contraction.\n'
                         'Active transport.\n'
                         'Protein synthesis.\n'
                         'Cell division.\n'
                         'Maintaining body temperature.\n'
                         '\n'
                         'Respiration is continuous — happening in every living cell, day and night, throughout your '
                         'entire life.',
              'heading': 'What is Respiration?'},
             {'content': 'Aerobic respiration uses OXYGEN to completely break down glucose.\n'
                         '\n'
                         'Word equation:\n'
                         'glucose + oxygen → carbon dioxide + water (+ energy released as ATP)\n'
                         '\n'
                         'Symbol equation:\n'
                         'C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O\n'
                         '\n'
                         'Key points:\n'
                         'Glucose is completely broken down — all the carbon atoms end up as CO₂.\n'
                         'Water is produced — the hydrogen from glucose combines with oxygen.\n'
                         'Large amount of ENERGY is released — approximately 36–38 ATP molecules per glucose.\n'
                         'This is the most efficient form of respiration.',
              'heading': 'The Equation for Aerobic Respiration'},
             {'content': "Aerobic respiration takes place in the MITOCHONDRIA — the 'powerhouses' of the cell.\n"
                         '\n'
                         'The mitochondria have a folded inner membrane (called cristae) which increases the surface '
                         'area for the reactions.\n'
                         '\n'
                         'Cells with HIGH energy demands have MORE mitochondria:\n'
                         'Muscle cells — need large amounts of ATP for contraction.\n'
                         'Liver cells — highly metabolically active, many chemical reactions.\n'
                         'Sperm cells — need ATP to power the flagellum for swimming.\n'
                         'Heart muscle cells — never stop contracting, need a constant ATP supply.\n'
                         '\n'
                         'Cells with lower energy demands have fewer mitochondria.',
              'heading': 'Where Aerobic Respiration Occurs'},
             {'content': 'Aerobic respiration releases approximately 36–38 ATP molecules per glucose molecule — far '
                         'more than anaerobic respiration (which produces only about 2 ATP).\n'
                         '\n'
                         'This is because oxygen allows the complete breakdown of glucose:\n'
                         'All six carbon atoms → 6 CO₂ (carbon fully released).\n'
                         'All hydrogen atoms → 6 H₂O (hydrogen fully removed).\n'
                         'All the chemical energy stored in the C–H bonds of glucose is harvested.\n'
                         '\n'
                         'Without oxygen, only a small fraction of this energy can be released — the rest remains '
                         'locked in the waste products (lactic acid or ethanol).\n'
                         '\n'
                         'This is why we breathe — to supply the constant oxygen demand of aerobic respiration in '
                         'every cell.',
              'heading': 'Why Aerobic Respiration is so Efficient'}],
  'title': 'Aerobic Respiration',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Anaerobic respiration in ANIMALS produces LACTIC ACID. Anaerobic respiration in YEAST produces '
                    'ETHANOL + CO₂. These are different products — this distinction comes up repeatedly in exams. Do '
                    "NOT say 'lactic acid' when asked about yeast fermentation.",
  'equations': ['Anaerobic (animals): glucose → lactic acid', 'Anaerobic (yeast): glucose → ethanol + carbon dioxide'],
  'fifas': [],
  'higher': None,
  'id': 'anaerobic-respiration',
  'key_note': 'Animals: glucose → lactic acid (no O₂, little ATP, causes muscle fatigue). Yeast: glucose → ethanol + '
              'CO₂ (fermentation — used in bread, beer, wine). Both produce far less ATP than aerobic respiration.',
  'matching': {'instruction': 'Sort each statement into the correct type of respiration.',
               'pairs': [('Aerobic', 'Requires oxygen — produces CO₂, water and ~36 ATP'),
                         ('Anaerobic — animals', 'No oxygen — produces lactic acid, causes burning feeling in muscles'),
                         ('Anaerobic — yeast',
                          'No oxygen — produces ethanol and CO₂, used in bread and alcohol production'),
                         ('Anaerobic — animals', 'Causes muscle fatigue during intense exercise'),
                         ('Anaerobic — yeast', 'CO₂ produced makes bread dough rise')],
               'title': 'Aerobic or Anaerobic — and Which Organism?'},
  'quiz': [{'opts': [('Ethanol and carbon dioxide', True),
                     ('Lactic acid', False),
                     ('Glucose and oxygen', False),
                     ('Carbon dioxide and water', False)],
            'q': 'What is produced by anaerobic respiration in yeast?',
            'wrong_explanations': {1: 'Lactic acid is produced by ANIMAL muscles during anaerobic respiration — NOT by '
                                      'yeast. Yeast produces ethanol + CO₂.',
                                   2: 'Glucose and oxygen are the REACTANTS in aerobic respiration — they go in, not '
                                      'come out of anaerobic respiration.',
                                   3: 'CO₂ and water = products of AEROBIC respiration. Anaerobic respiration in yeast '
                                      'produces ethanol + CO₂ (not water).'}},
           {'opts': [('Yeast ferments sugars in the dough — the CO₂ produced forms bubbles that make the dough expand',
                      True),
                     ('Yeast produces oxygen which inflates the dough', False),
                     ('Yeast absorbs water from the dough, making it lighter', False),
                     ('Yeast produces lactic acid which reacts with flour to create gas', False)],
            'q': 'Why does bread dough rise when yeast is added?',
            'wrong_explanations': {1: 'Yeast produces CO₂ and ethanol during fermentation — not oxygen. The ethanol '
                                      'evaporates when the bread is baked.',
                                   2: "Yeast absorbs sugars for fermentation — it doesn't absorb significant water "
                                      'from the dough.',
                                   3: 'Yeast (not animals) in bread produces ethanol and CO₂ — not lactic acid.'}},
           {'opts': [('The muscles are working so hard that oxygen cannot be delivered fast enough — anaerobic '
                      'respiration continues without it',
                      True),
                     ('Anaerobic respiration produces more ATP, so athletes switch to it for maximum performance',
                      False),
                     ('The lungs stop absorbing oxygen during intense exercise', False),
                     ('Glucose runs out during sprinting so the muscles use a different fuel', False)],
            'q': "During a sprint race, an athlete's muscles switch to anaerobic respiration. Why?",
            'wrong_explanations': {1: 'Anaerobic respiration produces FAR LESS ATP (~2 vs ~36) — it is not chosen for '
                                      'maximum performance. It is an emergency fallback when oxygen supply is '
                                      'insufficient.',
                                   2: 'The lungs work harder during exercise, not less — breathing rate and depth '
                                      "increase. But even this can't supply enough oxygen for maximum muscle output.",
                                   3: 'Muscles use glucose during sprinting — glycogen stores are broken down to '
                                      "supply glucose. Glucose shortage ('hitting the wall') is different from the "
                                      'short-term switch to anaerobic respiration.'}},
           {'opts': [('Aerobic respiration — approximately 36–38 ATP compared to 2 ATP from anaerobic', True),
                     ('Anaerobic respiration — it happens faster so produces more total ATP', False),
                     ('They produce the same amount — both start with glucose', False),
                     ('Anaerobic respiration — the lactic acid contains extra energy', False)],
            'q': 'Which process produces more ATP per glucose molecule?',
            'wrong_explanations': {1: 'Anaerobic can produce ATP FASTER per unit time in emergencies — but produces '
                                      'FAR LESS per glucose molecule.',
                                   2: 'They both start with glucose but have completely different efficiencies. '
                                      'Aerobic: ~36–38 ATP. Anaerobic: ~2 ATP.',
                                   3: "Lactic acid does retain some chemical energy (glucose isn't fully broken down) "
                                      "— but from the cell's perspective, anaerobic yields only ~2 ATP of USABLE "
                                      'energy.'}}],
  'rp': None,
  'spec': '4.4.2.2',
  'summary': 'Describe anaerobic respiration in animals and yeast and explain its uses.',
  'theory': [{'content': 'Anaerobic respiration is respiration WITHOUT OXYGEN.\n'
                         '\n'
                         'It occurs when oxygen is in short supply — for example, during very intense exercise when '
                         'muscles cannot get enough oxygen fast enough.\n'
                         '\n'
                         'Anaerobic respiration:\n'
                         'Does NOT require oxygen.\n'
                         'Starts with glucose, like aerobic respiration.\n'
                         'Produces MUCH LESS ATP than aerobic respiration (only about 2 ATP per glucose compared to '
                         '~36 for aerobic).\n'
                         'Produces different waste products depending on the organism.\n'
                         '\n'
                         'It is a short-term emergency measure — useful for bursts of intense activity but not '
                         'sustainable for long.',
              'heading': 'What is Anaerobic Respiration?'},
             {'content': 'In animal muscles (and some bacteria):\n'
                         '\n'
                         'Word equation:\n'
                         'glucose → lactic acid\n'
                         '\n'
                         'No oxygen needed. Only a small amount of ATP is produced.\n'
                         '\n'
                         'Lactic acid is produced because glucose cannot be fully broken down without oxygen — lactic '
                         'acid is the incomplete breakdown product.\n'
                         '\n'
                         'Effects of lactic acid:\n'
                         'Lactic acid LOWERS the pH inside muscle cells.\n'
                         'This disrupts enzyme activity → muscles stop contracting properly.\n'
                         'This causes the BURNING SENSATION in muscles during intense exercise.\n'
                         'Leads to MUSCLE FATIGUE — the muscles cannot maintain maximum effort.\n'
                         '\n'
                         'Lactic acid is NOT toxic long-term — after exercise, it is transported to the LIVER where it '
                         'is converted back to glucose (or broken down further in aerobic respiration).',
              'heading': 'Anaerobic Respiration in Animals (including Humans)'},
             {'content': 'In YEAST (and also in plants under waterlogged conditions):\n'
                         '\n'
                         'Word equation:\n'
                         'glucose → ethanol + carbon dioxide\n'
                         '\n'
                         'This process is called FERMENTATION.\n'
                         '\n'
                         'Fermentation is enormously important in food and drink production:\n'
                         '\n'
                         'BREAD MAKING:\n'
                         'Yeast is added to dough.\n'
                         'Yeast ferments sugars in the dough → produces CO₂.\n'
                         'CO₂ bubbles make the dough RISE (become light and airy).\n'
                         'Ethanol produced evaporates during baking.\n'
                         '\n'
                         'ALCOHOLIC DRINKS (beer, wine, cider):\n'
                         'Yeast ferments sugars in grain (beer), grapes (wine) or fruit (cider).\n'
                         'Ethanol accumulates → forms the alcohol in the drink.\n'
                         'CO₂ also produced → gives fizzy drinks their bubbles.\n'
                         '\n'
                         'BIOFUELS:\n'
                         'Ethanol from fermentation can be used as a biofuel — a renewable energy source.',
              'heading': 'Anaerobic Respiration in Yeast (Fermentation)'},
             {'content': 'Here is a clear side-by-side comparison:\n'
                         '\n'
                         'AEROBIC RESPIRATION:\n'
                         'Needs oxygen? YES.\n'
                         'Products: CO₂ + water.\n'
                         'ATP produced: ~36–38 per glucose.\n'
                         'Where: Mitochondria.\n'
                         'When used: Normal conditions.\n'
                         '\n'
                         'ANAEROBIC RESPIRATION (animals):\n'
                         'Needs oxygen? NO.\n'
                         'Products: Lactic acid.\n'
                         'ATP produced: ~2 per glucose.\n'
                         'Where: Cytoplasm.\n'
                         'When used: Intense exercise, emergency.\n'
                         '\n'
                         'ANAEROBIC RESPIRATION (yeast):\n'
                         'Needs oxygen? NO.\n'
                         'Products: Ethanol + CO₂.\n'
                         'ATP produced: ~2 per glucose.\n'
                         'Where: Cytoplasm.\n'
                         'When used: Absence of oxygen (e.g. in dough, in fermenting liquid).',
              'heading': 'Comparing Aerobic and Anaerobic Respiration'}],
  'title': 'Anaerobic Respiration',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Oxygen debt is NOT the lack of oxygen in the blood during exercise. It is the EXTRA oxygen needed '
                    "AFTER exercise to convert the lactic acid that accumulated. Students often say 'you breathe "
                    "harder during exercise to repay oxygen debt' — you breathe harder DURING exercise to supply O₂, "
                    'and continue breathing hard AFTER to repay the debt.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'response-to-exercise',
  'key_note': 'Exercise → more O₂ and glucose needed → heart rate up, breathing rate up, vasodilation. Intense '
              'exercise → anaerobic → lactic acid → muscle fatigue. After exercise → oxygen debt → lactic acid '
              'converted to glucose in liver.',
  'matching': {'instruction': 'Match each change to why it happens during exercise.',
               'pairs': [('Heart rate increases', 'Delivers more O₂ and glucose to muscles, removes CO₂ faster'),
                         ('Breathing rate and depth increase', 'Takes in more O₂ and expels more CO₂ per minute'),
                         ('Vasodilation in muscles', 'More blood redirected to active muscles — better O₂ supply'),
                         ('Glycogen breakdown in liver', 'Converts stored glycogen to glucose to fuel muscles'),
                         ('Continued heavy breathing after exercise',
                          'Repaying oxygen debt — extra O₂ to convert lactic acid back to glucose')],
               'title': 'Match the Exercise Response to its Purpose'},
  'quiz': [{'opts': [('To deliver more oxygen and glucose to muscles and remove CO₂ and lactic acid faster', True),
                     ('To raise body temperature to improve enzyme efficiency', False),
                     ('To produce more red blood cells for the increased demand', False),
                     ('To increase blood pressure so more oxygen enters through the skin', False)],
            'q': 'Why does heart rate increase during exercise?',
            'wrong_explanations': {1: 'Exercise does raise body temperature slightly — but this is a consequence, not '
                                      'the purpose of increased heart rate.',
                                   2: 'New red blood cells take days to produce — the immediate response is to pump '
                                      'existing blood faster.',
                                   3: "Oxygen doesn't enter through the skin in humans — it enters through the lungs. "
                                      "The skin's increased blood flow is for COOLING, not oxygen absorption."}},
           {'opts': [('Repaying the oxygen debt — extra O₂ is needed to convert accumulated lactic acid back to '
                      'glucose in the liver',
                      True),
                     ('The lungs take time to slow down after being stimulated', False),
                     ('To replace all the oxygen used during exercise', False),
                     ('Lactic acid in the blood stimulates the lungs to keep working hard', False)],
            'q': 'Why do you continue to breathe heavily for several minutes after stopping intense exercise?',
            'wrong_explanations': {1: 'The lungs respond to chemical signals from the blood — they slow down when CO₂ '
                                      'and lactic acid levels normalise.',
                                   2: 'All the oxygen used during exercise was already replaced during exercise — the '
                                      'post-exercise breathing is specifically about the lactic acid that accumulated.',
                                   3: 'Lactic acid in the blood does stimulate breathing — but the reason breathing '
                                      'stays elevated is specifically to process that lactic acid in the liver.'}},
           {'opts': [('The extra oxygen needed after exercise to convert accumulated lactic acid back to glucose in '
                      'the liver',
                      True),
                     ('The oxygen missing from muscle cells during intense exercise', False),
                     ('The difference between oxygen inhaled and oxygen used during exercise', False),
                     ('The oxygen stored in myoglobin in muscles before exercise', False)],
            'q': 'What is oxygen debt?',
            'wrong_explanations': {1: 'The lack of oxygen in muscles during exercise is what CAUSES anaerobic '
                                      'respiration — oxygen debt specifically refers to the post-exercise oxygen '
                                      'requirement to process the resulting lactic acid.',
                                   2: 'Difference between inhaled and used oxygen relates to metabolic efficiency — '
                                      'oxygen debt is specifically post-exercise processing of lactic acid.',
                                   3: "Myoglobin stores oxygen in muscles — this is used during exercise, but 'oxygen "
                                      "debt' refers to the post-exercise recovery process."}}],
  'rp': None,
  'spec': '4.4.2.3',
  'summary': 'Describe how the body responds during and after exercise, including oxygen debt.',
  'theory': [{'content': 'During exercise, muscles work harder — contracting more frequently and with more force.\n'
                         '\n'
                         'This increased muscle activity requires:\n'
                         'MORE GLUCOSE — the fuel for respiration.\n'
                         'MORE OXYGEN — for aerobic respiration.\n'
                         'FASTER REMOVAL of carbon dioxide and lactic acid — waste products.\n'
                         '\n'
                         'The body must respond to these increased demands almost immediately.\n'
                         '\n'
                         'Three systems work together to meet the demands of exercise:\n'
                         'The HEART — pumps blood faster and harder.\n'
                         'The LUNGS — breathe faster and deeper.\n'
                         'The BLOOD VESSELS — redistribute blood flow to muscles.',
              'heading': 'Why Exercise Demands More from the Body'},
             {'content': 'The body makes several rapid adjustments when exercise begins:\n'
                         '\n'
                         'HEART RATE INCREASES:\n'
                         'The heart beats faster (higher rate) and contracts more strongly (higher stroke volume).\n'
                         'More blood circulates per minute → more O₂ and glucose delivered to muscles.\n'
                         'More CO₂ and waste removed per minute.\n'
                         '\n'
                         'BREATHING RATE AND DEPTH INCREASE:\n'
                         'You breathe faster and take deeper breaths.\n'
                         'More O₂ inhaled per minute.\n'
                         'More CO₂ exhaled per minute.\n'
                         'Maintains the concentration gradients in the alveoli.\n'
                         '\n'
                         'VASODILATION — blood vessels to muscles widen:\n'
                         'More blood is redirected to active muscles.\n'
                         'Skin flushes (more blood near surface for cooling).\n'
                         'Blood flow reduced to non-essential organs (e.g. digestive system) temporarily.\n'
                         '\n'
                         'GLYCOGEN BREAKDOWN:\n'
                         'Glycogen stored in the LIVER and MUSCLES is converted back to glucose.\n'
                         'Increases the blood glucose supply to muscles.',
              'heading': 'Changes During Exercise'},
             {'content': 'During very intense exercise (e.g. sprinting), the body cannot supply oxygen fast enough.\n'
                         '\n'
                         'Muscles switch to ANAEROBIC RESPIRATION:\n'
                         'glucose → lactic acid\n'
                         '\n'
                         'LACTIC ACID ACCUMULATES in muscles:\n'
                         'Lowers the pH of the muscle tissue.\n'
                         'Disrupts enzyme activity.\n'
                         'Causes the burning, aching sensation during intense effort.\n'
                         'Leads to muscle fatigue.\n'
                         '\n'
                         'OXYGEN DEBT (also called EPOC — Excess Post-Exercise Oxygen Consumption):\n'
                         'After exercise stops, the body continues to breathe faster than normal.\n'
                         'This extra oxygen is used to process the accumulated lactic acid.\n'
                         'Lactic acid is transported in the blood to the LIVER.\n'
                         'In the liver, lactic acid is converted BACK into glucose — this requires oxygen.\n'
                         'The amount of extra oxygen needed after exercise to clear the lactic acid = the OXYGEN '
                         'DEBT.\n'
                         '\n'
                         'The harder the exercise, the more lactic acid produced, the larger the oxygen debt, and the '
                         'longer recovery takes.',
              'heading': 'Lactic Acid and Oxygen Debt'},
             {'content': "Regular exercise training causes adaptations that improve the body's response:\n"
                         '\n'
                         'HEART:\n'
                         'Cardiac muscle becomes stronger — heart pumps more blood per beat (larger stroke volume).\n'
                         'Resting heart rate falls (a sign of cardiovascular fitness).\n'
                         '\n'
                         'MUSCLES:\n'
                         'More mitochondria develop in muscle cells — greater capacity for aerobic respiration.\n'
                         'Larger glycogen stores — more fuel available.\n'
                         'Improved blood vessel density — more efficient oxygen delivery.\n'
                         '\n'
                         'LUNGS:\n'
                         'Larger lung capacity.\n'
                         'More efficient gas exchange.\n'
                         '\n'
                         'BLOOD:\n'
                         'Higher red blood cell count in trained athletes — more haemoglobin → more O₂ carried per '
                         'litre of blood.',
              'heading': 'Why Training Improves Performance'}],
  'title': 'Response to Exercise',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Metabolism is the TOTAL of ALL chemical reactions — not just respiration. Students often say '
                    "'metabolism = respiration' but metabolism includes digestion, protein synthesis, DNA replication, "
                    'urea production and many more reactions. Respiration is the most central metabolic process, but '
                    'not the only one.',
  'equations': [],
  'fifas': [],
  'higher': 'Metabolic rate is the rate of all chemical reactions in the body. It is affected by body size, muscle '
            'mass (metabolically active), age, temperature (in ectotherms) and hormones (thyroxine from thyroid '
            'controls basal metabolic rate). Anabolism = building molecules (protein synthesis, glycogen synthesis, '
            'lipid synthesis). Catabolism = breaking molecules down (respiration, digestion, deamination of amino '
            'acids in liver → urea).',
  'id': 'metabolism',
  'key_note': 'Metabolism = all chemical reactions in the body. Anabolism = building up (uses ATP). Catabolism = '
              'breaking down (releases ATP). Key examples: protein synthesis, respiration, digestion, glycogen '
              'synthesis, urea production.',
  'matching': {'instruction': 'Sort each reaction into building up (anabolism) or breaking down (catabolism).',
               'pairs': [('Anabolism — building up', 'Amino acids joined to make proteins at ribosomes'),
                         ('Catabolism — breaking down', 'Glucose broken down in aerobic respiration to release ATP'),
                         ('Anabolism — building up', 'Glucose polymerised to make glycogen in liver and muscles'),
                         ('Catabolism — breaking down', 'Proteins in food broken down to amino acids by proteases'),
                         ('Catabolism — breaking down', 'Excess amino acids deaminated in the liver to produce urea'),
                         ('Anabolism — building up',
                          'Fatty acids and glycerol joined to form triglycerides for fat storage')],
               'title': 'Anabolism or Catabolism?'},
  'quiz': [{'opts': [('The sum of all chemical reactions taking place in a cell or organism', True),
                     ('Only the reactions that release energy — such as respiration', False),
                     ('The process of digesting food in the gut', False),
                     ('How quickly a person breathes and moves', False)],
            'q': 'What is metabolism?',
            'wrong_explanations': {1: 'Metabolism includes ALL reactions — both energy-releasing (catabolism) and '
                                      'energy-using (anabolism). Respiration is just one part.',
                                   2: 'Digestion is one part of metabolism — but metabolism includes protein '
                                      'synthesis, DNA replication, glycogen synthesis, and many more reactions.',
                                   3: 'Breathing rate and movement speed are consequences of metabolic activity — '
                                      'metabolism itself refers to the chemical reactions, not the physical '
                                      'movements.'}},
           {'opts': [('Excess amino acids cannot be stored — the amino group is removed (deamination) and converted to '
                      'urea for excretion',
                      True),
                     ('Urea is produced when glucose is broken down in anaerobic respiration', False),
                     ('The liver converts CO₂ and water into urea to reduce acid in the blood', False),
                     ('Urea is made when fat molecules are broken down into fatty acids', False)],
            'q': 'Why is urea produced in the liver?',
            'wrong_explanations': {1: 'Anaerobic respiration in animals produces LACTIC ACID — not urea. Urea comes '
                                      'specifically from amino acid breakdown.',
                                   2: 'CO₂ is transported in the blood and exhaled — it is not converted to urea.',
                                   3: 'Fat breakdown produces fatty acids and glycerol — not urea. Urea specifically '
                                      'comes from amino acid deamination.'}},
           {'opts': [('Amino acids joined together at ribosomes to make a protein', True),
                     ('Glucose broken down in aerobic respiration to release ATP', False),
                     ('Starch digested by amylase into maltose in the mouth', False),
                     ('Lactic acid produced in muscles during anaerobic respiration', False)],
            'q': 'Which of the following is an example of an ANABOLIC (building) reaction?',
            'wrong_explanations': {1: 'Aerobic respiration BREAKS DOWN glucose — this is a catabolic reaction.',
                                   2: 'Digestion BREAKS DOWN starch — another catabolic reaction.',
                                   3: 'Lactic acid production is the result of breaking down glucose — catabolic.'}}],
  'rp': None,
  'spec': '4.4.2.4',
  'summary': 'Define metabolism and describe the key metabolic reactions in living organisms.',
  'theory': [{'content': 'METABOLISM is the sum of ALL the chemical reactions taking place in a cell or organism at '
                         'any given time.\n'
                         '\n'
                         'Every reaction that builds something up or breaks something down is part of metabolism.\n'
                         '\n'
                         'Metabolism is what keeps you alive — it powers growth, movement, repair, digestion, nerve '
                         'signals, and every other process your body performs.\n'
                         '\n'
                         'Metabolic reactions fall into two broad categories:\n'
                         'CATABOLISM — breaking large molecules into smaller ones (releasing energy).\n'
                         'ANABOLISM — building large molecules from smaller ones (requires energy).',
              'heading': 'What is Metabolism?'},
             {'content': 'These reactions USE energy (ATP) to build large molecules from small ones:\n'
                         '\n'
                         'Protein synthesis:\n'
                         'Amino acids → proteins (e.g. enzymes, haemoglobin, structural proteins).\n'
                         'Requires ATP and takes place at ribosomes.\n'
                         '\n'
                         'Cellulose synthesis:\n'
                         'Glucose molecules → cellulose (for plant cell walls).\n'
                         '\n'
                         'Starch and glycogen synthesis:\n'
                         'Glucose → starch (storage in plants).\n'
                         'Glucose → glycogen (storage in animal liver and muscles).\n'
                         '\n'
                         'Fat synthesis:\n'
                         'Fatty acids + glycerol → triglycerides (for cell membranes, energy storage, insulation).\n'
                         '\n'
                         'DNA replication:\n'
                         'Nucleotides → new DNA strands (before cell division).',
              'heading': 'Building Reactions (Anabolism)'},
             {'content': 'These reactions RELEASE energy by breaking large molecules into smaller ones:\n'
                         '\n'
                         'Respiration (the most important catabolic reaction):\n'
                         'Glucose + oxygen → carbon dioxide + water (releases ATP).\n'
                         '\n'
                         'Digestion:\n'
                         'Starch → maltose → glucose (by amylase).\n'
                         'Proteins → amino acids (by proteases).\n'
                         'Fats → fatty acids + glycerol (by lipase).\n'
                         '\n'
                         'Glycolysis:\n'
                         'Glucose broken down in the cytoplasm — the first step of respiration.\n'
                         '\n'
                         'Deamination (in the liver):\n'
                         'Excess amino acids → removed amino group → excreted as urea.\n'
                         'The remaining carbon skeleton → used in respiration.\n'
                         '\n'
                         'All these reactions are controlled by ENZYMES — which is why temperature and pH are so '
                         'important for survival.',
              'heading': 'Breaking-Down Reactions (Catabolism)'},
             {'content': "Metabolic rate is the overall speed at which an organism's metabolism runs.\n"
                         '\n'
                         'Factors affecting metabolic rate:\n'
                         'BODY SIZE — larger organisms have a higher total metabolic rate (but lower per gram).\n'
                         'MUSCLE MASS — muscle tissue is metabolically very active; more muscle = higher metabolic '
                         'rate.\n'
                         'EXERCISE — physical activity greatly increases metabolic rate.\n'
                         'TEMPERATURE — ectothermic organisms (e.g. reptiles) have metabolic rates heavily influenced '
                         'by external temperature.\n'
                         'HORMONES — thyroxine (from the thyroid gland) controls the basal metabolic rate.\n'
                         '\n'
                         'UREA PRODUCTION is a key metabolic waste product:\n'
                         'Excess amino acids cannot be stored.\n'
                         'The liver removes the amino group (–NH₂) through DEAMINATION.\n'
                         'Ammonia is produced → converted to UREA (less toxic).\n'
                         'Urea is carried in the blood to the KIDNEYS where it is filtered out and excreted in urine.',
              'heading': 'Why Metabolism Matters'}],
  'title': 'Metabolism',
  'triple_only': None,
  'variables': []}],

"homeostasis": [{'common_mistake': 'Negative feedback does NOT mean the response is negative or harmful. It means the response '
                    'OPPOSES the change — it is a corrective response. If temperature rises, the negative feedback '
                    "brings it back DOWN. If temperature falls, it brings it back UP. The 'negative' refers to the "
                    'direction of the response relative to the change.',
  'equations': [],
  'fifas': [],
  'higher': 'Negative feedback: response opposes the change — brings variable back to set point. Positive feedback '
            'amplifies a change (e.g. blood clotting, uterine contractions during labour). All homeostatic systems '
            'include: receptor (detects change), coordination centre (compares to set point, determines response) and '
            'effector (corrects deviation). Students should be able to construct and interpret diagrams of negative '
            'feedback loops.',
  'id': 'homeostasis',
  'key_note': 'Homeostasis: stable internal environment via negative feedback. Receptor → coordination centre → '
              'effector. Controls: temperature (37°C), blood glucose (~5 mmol/L), water content. Essential because '
              'enzymes are sensitive to these conditions.',
  'matching': {'instruction': 'Match each component to its role in the homeostatic control system.',
               'pairs': [('Receptor', 'Detects a change in the variable — generates a signal'),
                         ('Coordination centre', 'Receives the signal, compares to set point, decides the response'),
                         ('Effector', 'Carries out the response — a muscle or gland'),
                         ('Negative feedback',
                          'The response opposes the original change — brings the variable back to the set point'),
                         ('Set point', 'The target value the body aims to maintain — e.g. 37°C for temperature')],
               'title': 'Match the Homeostatic Component'},
  'quiz': [{'opts': [('Maintaining a stable internal environment using negative feedback mechanisms', True),
                     ('Increasing body temperature when the environment is hot', False),
                     ('Removing waste products from the body through excretion', False),
                     ('Controlling how fast organisms grow', False)],
            'q': 'What is homeostasis?',
            'wrong_explanations': {1: 'Increasing body temperature when hot would make things WORSE — homeostasis '
                                      'CORRECTS deviations. When the body is hot, homeostasis acts to COOL it down.',
                                   2: 'Excretion is important but homeostasis specifically refers to maintaining '
                                      'STABLE internal conditions like temperature, blood glucose and water content.',
                                   3: 'Growth rate is controlled by hormones and genetics — not by homeostatic '
                                      'mechanisms.'}},
           {'opts': [('Enzymes in the body work best at this temperature — deviations cause slower reactions or '
                      'denaturation',
                      True),
                     ('Bacteria cannot survive at 37°C, so the body stays infection-free', False),
                     ('The heart muscle can only contract at exactly 37°C', False),
                     ('Red blood cells carry oxygen most efficiently at 37°C', False)],
            'q': 'Why is maintaining body temperature at 37°C so important?',
            'wrong_explanations': {1: 'Bacteria can survive at 37°C — indeed, body temperature of ~37°C is actually '
                                      'ideal for many pathogens like Staphylococcus.',
                                   2: 'Cardiac muscle can contract across a range of temperatures — the critical issue '
                                      'is enzyme function at the cellular level.',
                                   3: 'Red blood cells do function across a range of temperatures — the enzyme '
                                      'sensitivity argument is the primary reason for temperature homeostasis.'}},
           {'opts': [('Negative feedback — mechanisms are activated to raise blood glucose back to the set point',
                      True),
                     ('Positive feedback — more insulin is released to lower it further', False),
                     ('No response — the body cannot detect blood glucose levels', False),
                     ("The person's temperature rises to compensate for the energy loss", False)],
            'q': "A person's blood glucose level drops too low. What type of response will occur?",
            'wrong_explanations': {1: 'Positive feedback would make the problem WORSE — releasing more insulin when '
                                      'glucose is already low would be dangerous. Homeostasis uses negative feedback '
                                      'to correct deviations.',
                                   2: 'The pancreas and liver continuously monitor and respond to blood glucose levels '
                                      '— receptors in the pancreas detect low glucose and release glucagon.',
                                   3: 'Temperature and blood glucose are regulated independently by different systems '
                                      '— a drop in glucose does not trigger a temperature rise.'}}],
  'rp': None,
  'spec': '4.5.1',
  'summary': 'Define homeostasis and explain how negative feedback maintains a stable internal environment.',
  'theory': [{'content': 'HOMEOSTASIS is the maintenance of a stable internal environment despite changes in external '
                         'conditions or internal activity.\n'
                         '\n'
                         'The body must keep the following conditions within very narrow limits:\n'
                         'BODY TEMPERATURE — maintained at ~37°C for optimal enzyme activity.\n'
                         'BLOOD GLUCOSE CONCENTRATION — maintained at ~5 mmol/L for cell function.\n'
                         'WATER CONTENT of blood and tissue fluid — controlled to prevent cells shrinking or '
                         'swelling.\n'
                         '\n'
                         'If any of these deviate significantly from their set points, cells and organs begin to '
                         'malfunction — potentially causing death.\n'
                         '\n'
                         'Homeostasis is what allows warm-blooded animals like humans to survive in very different '
                         'environments, from Arctic tundra to tropical desert.',
              'heading': 'What is Homeostasis?'},
             {'content': 'All homeostatic control systems use NEGATIVE FEEDBACK.\n'
                         '\n'
                         'Negative feedback means: when a variable moves AWAY from the set point, the system responds '
                         'to bring it BACK.\n'
                         '\n'
                         "The word 'negative' means the response OPPOSES the change — it works against the deviation, "
                         'not with it.\n'
                         '\n'
                         'Example: if body temperature rises, the response is to COOL the body (opposing the rise). If '
                         'body temperature falls, the response is to WARM the body (opposing the fall).\n'
                         '\n'
                         'Negative feedback keeps variables oscillating slightly around a set point — rarely exactly '
                         'at it, but always returning to it.',
              'heading': 'Negative Feedback'},
             {'content': 'Every homeostatic control system has the same three components:\n'
                         '\n'
                         '1. RECEPTOR (sensor):\n'
                         'Detects changes in the variable being controlled.\n'
                         'Generates a signal proportional to the degree of change.\n'
                         'Examples: thermoreceptors in skin (detect temperature), osmoreceptors in hypothalamus '
                         '(detect blood water content), glucose receptors in pancreas.\n'
                         '\n'
                         '2. COORDINATION CENTRE (control centre):\n'
                         'Receives information from receptors.\n'
                         'Compares the actual value to the set point.\n'
                         'Determines the appropriate response.\n'
                         'Examples: the hypothalamus in the brain (temperature, water), the pancreas (blood glucose).\n'
                         '\n'
                         '3. EFFECTOR:\n'
                         'Carries out the response that corrects the deviation.\n'
                         'Can be a MUSCLE (e.g. skeletal muscles shivering) or a GLAND (e.g. sweat glands, endocrine '
                         'glands releasing hormones).\n'
                         '\n'
                         "The effector's response reduces the original stimulus — this completes the negative feedback "
                         'loop.',
              'heading': 'The Three Components of Homeostatic Control'},
             {'content': 'Enzymes control almost every biochemical reaction in the body — and enzymes are extremely '
                         'sensitive to temperature, pH and concentration.\n'
                         '\n'
                         'IF TEMPERATURE RISES TOO HIGH:\n'
                         'Enzymes denature → active site shape changes permanently → reactions stop → cells die.\n'
                         'Body temperature above ~40°C causes proteins to denature → organ failure → death.\n'
                         '\n'
                         'IF BLOOD GLUCOSE FALLS TOO LOW (hypoglycaemia):\n'
                         'Brain cells are starved of glucose → confusion, unconsciousness, brain damage, coma.\n'
                         '\n'
                         'IF BLOOD GLUCOSE STAYS TOO HIGH (hyperglycaemia):\n'
                         'Long-term damage to blood vessels → blindness, kidney failure, nerve damage, cardiovascular '
                         'disease.\n'
                         '\n'
                         'IF WATER CONTENT IS WRONG:\n'
                         'Too little water → cells shrink → dehydration of tissues → organ failure.\n'
                         'Too much water → cells swell → can burst (lysis) in animal cells.\n'
                         '\n'
                         'Homeostasis protects all these systems from harmful fluctuations.',
              'heading': 'Why Homeostasis is Essential'}],
  'title': 'Homeostasis',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Transmission WITHIN a neurone is electrical (an impulse). Transmission ACROSS a synapse is '
                    "CHEMICAL (neurotransmitters). Students often say 'electrical signals cross the synapse' — they "
                    'cannot. The synapse is a gap and must be crossed using chemical neurotransmitters that then '
                    'trigger a new electrical impulse in the next neurone.',
  'equations': [],
  'fifas': [],
  'higher': 'Synapses allow one-way signal transmission between neurones via neurotransmitter diffusion. Drugs '
            'affecting synapses: stimulants (caffeine, nicotine, cocaine) increase neurotransmitter activity; '
            'depressants (alcohol, benzodiazepines) reduce synaptic activity; SSRIs block serotonin reabsorption '
            'increasing its concentration. The myelin sheath insulates axons and allows faster signal conduction by '
            'saltatory (jumping) transmission.',
  'id': 'nervous-system',
  'key_note': 'CNS = brain + spinal cord. PNS = all nerves. Sensory: receptor → CNS. Relay: within CNS. Motor: CNS → '
              'effector. Synapse: electrical → chemical (neurotransmitter) → electrical. One-way transmission.',
  'matching': {'instruction': 'Match each component to its correct role.',
               'pairs': [('Sensory neurone', 'Carries impulse FROM receptor TO CNS'),
                         ('Relay neurone', 'Connects sensory and motor neurones — found within the CNS'),
                         ('Motor neurone', 'Carries impulse FROM CNS TO effector (muscle or gland)'),
                         ('Synapse', 'Junction between neurones — signal crosses via chemical neurotransmitters'),
                         ('Myelin sheath', 'Fatty insulating layer around axon — speeds up impulse conduction'),
                         ('CNS', 'Brain and spinal cord — processes information and coordinates responses')],
               'title': 'Match the Nervous System Component'},
  'quiz': [{'opts': [('Receptor → sensory neurone → relay neurone → motor neurone → effector', True),
                     ('Receptor → motor neurone → relay neurone → sensory neurone → effector', False),
                     ('Effector → sensory neurone → CNS → motor neurone → receptor', False),
                     ('Receptor → CNS → sensory neurone → motor neurone', False)],
            'q': 'What is the correct pathway for a nerve signal from receptor to effector?',
            'wrong_explanations': {1: 'Motor and sensory neurones are in the wrong order. SENSORY carries to the CNS; '
                                      'MOTOR carries away from the CNS.',
                                   2: 'The pathway runs from receptor to effector — not in reverse.',
                                   3: 'Sensory neurones carry signals TO the CNS. They come AFTER the receptor, not '
                                      'after the CNS.'}},
           {'opts': [('Neurotransmitters are released, diffuse across the gap and bind to receptors on the next '
                      'neurone',
                      True),
                     ('The electrical impulse jumps across the gap directly', False),
                     ('The two neurones fuse temporarily to allow the signal through', False),
                     ('Blood vessels carry chemical signals across the synaptic gap', False)],
            'q': 'How does a nerve signal cross a synapse?',
            'wrong_explanations': {1: 'The synapse is a liquid-filled gap — electrical impulses cannot jump across it. '
                                      'Chemical neurotransmitters are essential.',
                                   2: 'Neurones never physically fuse — the synaptic gap is always maintained. Fusion '
                                      'would prevent the one-way transmission that synapses provide.',
                                   3: 'Synaptic transmission takes microseconds — blood flow is far too slow. '
                                      'Neurotransmitters diffuse across the tiny gap.'}},
           {'opts': [('Neurotransmitters are released only from the pre-synaptic side, and receptors are only on the '
                      'post-synaptic side',
                      True),
                     ('Electrical impulses can only travel in one direction through an axon', False),
                     ('The synaptic gap is too narrow for signals to travel both ways', False),
                     ('Enzymes on the post-synaptic side destroy neurotransmitters before they can go back', False)],
            'q': 'Why is synaptic transmission one-directional?',
            'wrong_explanations': {1: 'Electrical impulses technically can propagate in both directions in an isolated '
                                      'axon — the one-way nature of synapse transmission comes from the asymmetry of '
                                      'neurotransmitter release and receptor location.',
                                   2: "Gap width has nothing to do with directionality — it's the arrangement of "
                                      'vesicles and receptors that enforces one-way flow.',
                                   3: 'Enzymes do break down neurotransmitters after binding — but this prevents '
                                      'prolonged stimulation, not directionality.'}}],
  'rp': None,
  'spec': '4.5.2',
  'summary': 'Describe the structure and function of the nervous system, neurones and synapses.',
  'theory': [{'content': 'The nervous system detects changes (stimuli) in the environment and coordinates rapid '
                         'responses.\n'
                         '\n'
                         'It is divided into two main parts:\n'
                         'CENTRAL NERVOUS SYSTEM (CNS): the BRAIN and SPINAL CORD. Processes all incoming information '
                         'and determines the appropriate response.\n'
                         'PERIPHERAL NERVOUS SYSTEM (PNS): all the NERVES that connect the CNS to the rest of the body '
                         '— carrying signals to and from every organ, muscle and sense organ.\n'
                         '\n'
                         'The nervous system communicates via ELECTRICAL IMPULSES — signals that travel along '
                         'specialised cells called NEURONES at speeds of up to 120 m/s.\n'
                         '\n'
                         'This is much faster than hormonal communication, making the nervous system ideal for rapid, '
                         'precise responses.',
              'heading': 'Overview of the Nervous System'},
             {'content': 'There are three types of neurone, each with a specific role:\n'
                         '\n'
                         'SENSORY NEURONE:\n'
                         'Carries electrical impulses FROM receptors (sense organs) TO the CNS.\n'
                         'Long dendron carrying signal towards the cell body, then axon to the CNS.\n'
                         'Example: carries pain signal from finger to spinal cord when you burn yourself.\n'
                         '\n'
                         'RELAY NEURONE:\n'
                         'Found entirely WITHIN the CNS (brain and spinal cord).\n'
                         'Connects sensory neurones to motor neurones.\n'
                         'Acts as a processing junction — signals can be passed on, filtered or directed to the '
                         'appropriate response pathway.\n'
                         '\n'
                         'MOTOR NEURONE:\n'
                         'Carries impulses FROM the CNS TO effectors (muscles or glands).\n'
                         'Long axon — can be over 1 metre long (e.g. from spinal cord to foot).\n'
                         'Covered in a MYELIN SHEATH — a fatty insulating layer that speeds up signal conduction.\n'
                         'Example: carries signal to leg muscle to pull foot away from a sharp object.',
              'heading': 'Types of Neurone'},
             {'content': 'A SYNAPSE is the junction between two neurones — a tiny gap called the SYNAPTIC CLEFT.\n'
                         '\n'
                         'Electrical impulses CANNOT jump across this gap — transmission across a synapse is '
                         'CHEMICAL.\n'
                         '\n'
                         'How a synapse works:\n'
                         '1. An electrical impulse arrives at the end of the pre-synaptic neurone (the sending '
                         'neurone).\n'
                         '2. Vesicles containing NEUROTRANSMITTER molecules fuse with the membrane.\n'
                         '3. Neurotransmitters are released into the synaptic cleft.\n'
                         '4. They DIFFUSE across the gap.\n'
                         '5. They bind to RECEPTOR PROTEINS on the post-synaptic neurone (the receiving neurone).\n'
                         '6. This triggers a new electrical impulse in the next neurone.\n'
                         '7. Neurotransmitters are then broken down by enzymes or reabsorbed — resetting the synapse.\n'
                         '\n'
                         'Transmission is ONE-WAY only — neurotransmitters are released from the pre-synaptic side and '
                         'receptors are only on the post-synaptic side.',
              'heading': 'The Synapse'},
             {'content': 'Many drugs affect the nervous system by interfering with synapse function:\n'
                         '\n'
                         'STIMULANTS (e.g. caffeine, nicotine, cocaine, amphetamines):\n'
                         'Increase neurotransmitter activity at synapses.\n'
                         'More impulses transmitted → increased alertness, faster heart rate, increased energy.\n'
                         'Can cause addiction — the brain adapts to higher neurotransmitter levels and requires the '
                         'drug to function normally.\n'
                         '\n'
                         'DEPRESSANTS (e.g. alcohol, benzodiazepines, sleeping tablets):\n'
                         'Reduce neurotransmitter activity.\n'
                         'Fewer impulses transmitted → slowed reactions, reduced anxiety, drowsiness, loss of '
                         'coordination.\n'
                         'Alcohol specifically slows the CNS — increasing reaction time significantly.\n'
                         '\n'
                         'SSRIs (antidepressants, e.g. fluoxetine):\n'
                         'Block the reabsorption of serotonin after it has been released.\n'
                         'Serotonin stays in the synapse longer — improves mood.\n'
                         'Used to treat depression and anxiety.',
              'heading': 'How Drugs Affect Synapses'}],
  'title': 'The Human Nervous System',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'A reflex bypasses the CONSCIOUS BRAIN (cerebral cortex) — it is processed in the SPINAL CORD. The '
                    "brain does receive the signal (that's why you become aware of it), but it does NOT initiate the "
                    "reflex. Students often say 'the brain controls reflexes' — the brain is only aware of them "
                    'afterwards.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'reflex-actions',
  'key_note': 'Reflex arc: stimulus → receptor → sensory neurone → relay neurone (spinal cord) → motor neurone → '
              'effector → response. Faster than voluntary because it bypasses the conscious brain. Involuntary and '
              'automatic.',
  'matching': {'instruction': 'Match each component to its role in the reflex arc.',
               'pairs': [('Stimulus', 'The change that triggers the reflex — e.g. touching a sharp object'),
                         ('Receptor', 'Detects the stimulus and generates an electrical impulse'),
                         ('Sensory neurone', 'Carries the impulse from the receptor to the spinal cord'),
                         ('Relay neurone', 'In the spinal cord — connects sensory to motor neurone'),
                         ('Motor neurone', 'Carries impulse from spinal cord to the effector'),
                         ('Effector', 'Muscle contracts or gland secretes — produces the response')],
               'title': 'Match Each Step of the Reflex Arc'},
  'quiz': [{'opts': [('They bypass the conscious brain — the signal is processed in the spinal cord using a shorter '
                      'pathway',
                      True),
                     ('Reflex neurones conduct impulses faster than voluntary neurones', False),
                     ('Reflexes use fewer neurotransmitters so synaptic delay is reduced', False),
                     ('The brain prioritises reflex signals over other information', False)],
            'q': 'Why are reflexes faster than voluntary responses?',
            'wrong_explanations': {1: 'Neurone conduction speed varies by myelination — not fundamentally by whether '
                                      "it's a reflex or voluntary pathway.",
                                   2: 'Synaptic delay is similar in both — the key saving is the elimination of the '
                                      'brain processing step entirely.',
                                   3: "The brain doesn't 'prioritise' reflexes — it is simply not involved in "
                                      'initiating them.'}},
           {'opts': [('The reflex arc bypasses the conscious brain — the withdrawal response occurred before pain was '
                      'processed',
                      True),
                     ("Pain receptors in the hand don't work under extreme heat", False),
                     ('The brain sends an emergency signal faster than normal in dangerous situations', False),
                     ('Motor neurones are faster than sensory neurones', False)],
            'q': 'You touch a hot surface and pull your hand away before you feel pain. What does this demonstrate?',
            'wrong_explanations': {1: 'Pain receptors DO work — you feel the pain a fraction of a second after your '
                                      'hand has already moved away.',
                                   2: "The brain doesn't speed up for emergencies — the reflex works independently of "
                                      'conscious brain processing.',
                                   3: 'Motor and sensory neurones have similar conduction speeds — the key is the '
                                      'PATHWAY length, not individual neurone speed.'}},
           {'opts': [('The spinal cord — relay neurones connect sensory and motor neurones here', True),
                     ('The cerebral cortex — the thinking part of the brain', False),
                     ('The cerebellum — which coordinates movement', False),
                     ('The medulla oblongata — which controls heart rate and breathing', False)],
            'q': 'In which part of the CNS is a spinal reflex arc processed?',
            'wrong_explanations': {1: 'The cerebral cortex is the conscious thinking brain — reflex arcs specifically '
                                      'BYPASS this to be fast.',
                                   2: 'The cerebellum coordinates balance and smooth movement — it is not the site of '
                                      'spinal reflex processing.',
                                   3: 'The medulla oblongata controls automatic functions like heart rate — but reflex '
                                      'arcs for quick withdrawal responses are processed in the spinal cord.'}}],
  'rp': None,
  'spec': '4.5.2',
  'summary': 'Describe reflex actions, the reflex arc and why reflexes are faster than voluntary responses.',
  'theory': [{'content': 'A REFLEX is a rapid, automatic response to a stimulus that does not require conscious '
                         'thought.\n'
                         '\n'
                         'Reflexes are protective — they allow the body to respond to potentially harmful stimuli '
                         'BEFORE the conscious brain can process the situation.\n'
                         '\n'
                         'Key features of a reflex:\n'
                         'AUTOMATIC — happens without thinking.\n'
                         'RAPID — much faster than a voluntary response.\n'
                         'INVOLUNTARY — you cannot choose not to do it.\n'
                         'STEREOTYPED — always the same response to the same stimulus.\n'
                         '\n'
                         'Examples:\n'
                         'Withdrawing your hand from a hot surface.\n'
                         'Knee-jerk reflex (tapping the patellar tendon).\n'
                         'Pupil constricting in bright light (pupil reflex).\n'
                         'Sneezing and coughing.\n'
                         'Blinking when an object moves towards the eye.\n'
                         "Baby's grasp reflex.",
              'heading': 'What is a Reflex?'},
             {'content': 'A reflex arc is the specific nerve pathway along which a reflex signal travels. Crucially, '
                         'it passes through the SPINAL CORD rather than up to the conscious brain — this is what makes '
                         'it so fast.\n'
                         '\n'
                         'The pathway of a reflex arc:\n'
                         '1. STIMULUS — a change detected by a sense organ (e.g. heat on the skin).\n'
                         '2. RECEPTOR — specialised cells detect the stimulus and generate an electrical impulse.\n'
                         '3. SENSORY NEURONE — carries the impulse to the spinal cord (part of the CNS).\n'
                         '4. RELAY NEURONE — in the spinal cord, receives the impulse and passes it on. Also sends a '
                         'signal UP to the brain — so the brain becomes aware AFTER the reflex has already occurred.\n'
                         '5. MOTOR NEURONE — carries impulse from spinal cord to the effector.\n'
                         '6. EFFECTOR — the muscle contracts (or gland secretes) to produce the response.\n'
                         '7. RESPONSE — e.g. the hand moves away from the heat source.\n'
                         '\n'
                         'The brain is aware of the reflex — but AFTER the response has already happened.',
              'heading': 'The Reflex Arc'},
             {'content': 'VOLUNTARY response pathway:\n'
                         'Receptor → sensory neurone → spinal cord → UP to brain → conscious processing → DOWN from '
                         'brain → motor neurone → effector.\n'
                         '\n'
                         'REFLEX pathway:\n'
                         'Receptor → sensory neurone → spinal cord (relay neurone) → motor neurone → effector.\n'
                         '\n'
                         'The reflex bypasses the conscious brain (cerebral cortex) — this eliminates the time needed '
                         'for:\n'
                         'Signal travelling up to the brain.\n'
                         'Conscious processing and decision-making.\n'
                         'Signal travelling back down from the brain.\n'
                         '\n'
                         'Typical voluntary reaction time: 0.2–0.3 seconds.\n'
                         'Typical reflex reaction time: 0.04–0.1 seconds.\n'
                         '\n'
                         'This 3–5× speed advantage can prevent serious injury — for example, moving your hand away '
                         'from a sharp object or flame before the pain signal has even reached consciousness.',
              'heading': 'Why Reflexes are Faster than Voluntary Responses'}],
  'title': 'Reflex Actions',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'VASODILATION means blood vessels WIDEN — MORE blood near skin surface — MORE heat lost — occurs '
                    'when TOO HOT. VASOCONSTRICTION means blood vessels NARROW — LESS blood near skin surface — LESS '
                    'heat lost — occurs when TOO COLD. Students often get these mixed up. Remember: Dilation = '
                    'Diameter increases = more heat lost.',
  'equations': [],
  'fifas': [],
  'higher': 'The hypothalamus monitors core blood temperature and skin temperature (via peripheral thermoreceptors). '
            'Vasoconstriction: arterioles near skin narrow → less blood near surface → less heat lost. Vasodilation: '
            'arterioles widen → more blood near surface → more heat lost. Sweating: evaporation removes latent heat. '
            'Shivering: rapid muscle contraction generates metabolic heat. Hairs erect: trap air as insulation. '
            'Students should be able to explain these mechanisms in terms of negative feedback.',
  'id': 'thermoregulation',
  'key_note': 'Too hot: sweat (evaporation cools), vasodilation (more heat lost from skin), hairs flat. Too cold: '
              'shiver (respiration generates heat), vasoconstriction (less heat lost), hairs raised (insulation). '
              'Hypothalamus = the thermostat.',
  'matching': {'instruction': 'Sort each response — does it happen when the body is too hot or too cold?',
               'pairs': [('Too hot', 'Sweating — evaporation removes heat from the body surface'),
                         ('Too hot', 'Vasodilation — blood vessels widen, more heat lost from skin surface'),
                         ('Too cold', 'Shivering — rapid muscle contractions generate heat via respiration'),
                         ('Too cold', 'Vasoconstriction — blood vessels narrow, less heat lost from skin'),
                         ('Too hot', 'Hairs lie flat — less insulation, more heat can escape'),
                         ('Too cold', 'Hairs stand on end — traps air for insulation (causes goosebumps)')],
               'title': 'Too Hot or Too Cold?'},
  'quiz': [{'opts': [('Water evaporating from the skin surface absorbs latent heat energy from the body — cooling it',
                      True),
                     ('Sweat removes hot blood from deep in the body and cools it at the surface', False),
                     ('The salt in sweat chemically reacts with the skin to absorb heat', False),
                     ('Sweating increases blood flow to the skin, which cools the blood', False)],
            'q': 'Why does sweating cool the body down?',
            'wrong_explanations': {1: "Sweating doesn't involve blood — it is a secretion from sweat glands. The "
                                      'cooling effect is from EVAPORATION.',
                                   2: 'Salt in sweat helps retain water on the skin surface longer — the cooling '
                                      'mechanism is evaporation of water, not a chemical reaction.',
                                   3: 'Vasodilation increases blood flow to the skin for cooling — sweating itself is '
                                      'a separate mechanism that works through evaporation.'}},
           {'opts': [('Blood vessels near the skin widen — occurs when the body is too hot, allowing more heat to be '
                      'lost',
                      True),
                     ('Blood vessels narrow — occurs when the body is too cold, to conserve heat', False),
                     ('Blood vessels widen — occurs when the body is too cold, to warm the skin', False),
                     ('Blood vessels contract — occurs when the body is too hot, to prevent overheating', False)],
            'q': 'What is vasodilation and when does it occur?',
            'wrong_explanations': {1: 'Blood vessels NARROWING = VASOCONSTRICTION — this happens when cold, to reduce '
                                      'heat loss. Vasodilation is widening.',
                                   2: 'If blood vessels widened when cold, more heat would be LOST — that would make '
                                      'the cold problem worse. Vasodilation occurs when HOT.',
                                   3: 'Blood vessels CONTRACTING = VASOCONSTRICTION — occurs when cold, not hot.'}},
           {'opts': [('Rapid muscle contractions require aerobic respiration — heat is released as a by-product of '
                      'respiration',
                      True),
                     ('Shivering increases blood flow to the skin, warming the surface', False),
                     ('The vibration of muscles generates electrical energy that heats the body', False),
                     ('Shivering activates sweat glands which release warm fluid to the skin', False)],
            'q': 'Why does shivering help when you are cold?',
            'wrong_explanations': {1: 'Increased blood flow to the skin (vasodilation) increases heat LOSS — when '
                                      'cold, vasoconstriction REDUCES blood flow to the skin. Shivering warms the body '
                                      'through metabolic heat.',
                                   2: 'Muscles generate heat through CHEMICAL energy released in respiration — not by '
                                      'converting movement to electrical energy.',
                                   3: 'Sweat glands are LESS active when cold — sweating causes heat loss, which is '
                                      "the opposite of what's needed."}}],
  'rp': None,
  'spec': '4.5.1',
  'summary': 'Describe how the body maintains a constant core temperature of 37°C.',
  'theory': [{'content': 'The human body must maintain a core temperature of approximately 37°C.\n'
                         '\n'
                         'This is the OPTIMUM TEMPERATURE for human enzymes — the temperature at which they work most '
                         'efficiently.\n'
                         '\n'
                         'If temperature rises above ~40°C: enzymes denature → reactions stop → organ failure → death '
                         '(hyperthermia).\n'
                         '\n'
                         'If temperature falls below ~34°C: enzyme activity decreases dramatically → brain and heart '
                         'function affected → loss of consciousness → death (hypothermia).\n'
                         '\n'
                         'The body is constantly generating heat (from respiration in all cells) and losing heat (to '
                         'the environment). Thermoregulation balances these.',
              'heading': 'Why Temperature Must Be Controlled'},
             {'content': "The HYPOTHALAMUS — a region in the brain — acts as the body's thermostat.\n"
                         '\n'
                         'It has two types of thermoreceptors:\n'
                         'CENTRAL THERMORECEPTORS in the hypothalamus itself — monitor the temperature of blood '
                         'flowing through the brain.\n'
                         'PERIPHERAL THERMORECEPTORS in the skin — detect changes in surface temperature (giving '
                         'advance warning of environmental temperature changes).\n'
                         '\n'
                         'When the hypothalamus detects deviation from 37°C, it sends signals via the nervous system '
                         'and hormones to trigger corrective responses.',
              'heading': "The Hypothalamus — The Body's Thermostat"},
             {'content': 'When body temperature rises ABOVE 37°C, the hypothalamus triggers responses to LOSE heat:\n'
                         '\n'
                         'SWEATING:\n'
                         'Sweat glands in the skin produce sweat (mainly water + salts).\n'
                         'Sweat spreads over the skin surface.\n'
                         'As water EVAPORATES from the skin, it absorbs latent heat from the body → body cools.\n'
                         'More sweating occurs in hot conditions or during exercise.\n'
                         '\n'
                         'VASODILATION:\n'
                         'Blood vessels (arterioles) near the skin surface WIDEN.\n'
                         'More blood flows close to the skin surface.\n'
                         'More heat is lost by radiation and convection from the skin.\n'
                         'This is why the skin looks flushed or red when hot.\n'
                         '\n'
                         'HAIRS LIE FLAT:\n'
                         'Erector pili muscles RELAX → hairs lie flat.\n'
                         'No trapped air layer → less insulation → more heat can escape.\n'
                         '(More significant in other mammals than in humans due to less body hair.)',
              'heading': 'Responses When Too Hot'},
             {'content': 'When body temperature falls BELOW 37°C, the hypothalamus triggers responses to GENERATE and '
                         'RETAIN heat:\n'
                         '\n'
                         'SHIVERING:\n'
                         'Skeletal muscles contract rapidly and repeatedly.\n'
                         'Muscle contractions require RESPIRATION → releases heat as a by-product.\n'
                         'Shivering can increase heat production up to 5× the resting rate.\n'
                         '\n'
                         'VASOCONSTRICTION:\n'
                         'Blood vessels near the skin surface NARROW.\n'
                         'Less blood flows close to the skin surface.\n'
                         'Less heat lost by radiation from the skin.\n'
                         'Fingers and toes may become pale or blue in extreme cold.\n'
                         '\n'
                         'HAIRS STAND ON END:\n'
                         'Erector pili muscles CONTRACT → hairs raise upright.\n'
                         'Traps a layer of warm air close to the skin → insulation layer.\n'
                         "(More effective in other mammals — in humans this causes 'goosebumps').\n"
                         '\n'
                         'REDUCED SWEATING:\n'
                         'Sweat glands become less active.\n'
                         'Less evaporative cooling.\n'
                         '\n'
                         'ADRENALINE RELEASED:\n'
                         'Hormone that increases metabolic rate → more respiration → more heat produced.',
              'heading': 'Responses When Too Cold'}],
  'title': 'Thermoregulation',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Hormones travel in the BLOOD to target organs — they do NOT travel along nerves. Do not confuse '
                    'the two systems. Also: not all organs respond to every hormone — only TARGET ORGANS with the '
                    'correct receptor proteins respond.',
  'equations': [],
  'fifas': [],
  'higher': "The pituitary gland ('master gland') controls other endocrine glands via tropic hormones: TSH stimulates "
            'thyroid, FSH/LH control reproduction, ACTH stimulates adrenal cortex, ADH controls kidney water '
            'reabsorption. Adrenaline (fight or flight): increases heart rate, dilates pupils, redirects blood to '
            'muscles, raises blood glucose by stimulating liver to convert glycogen to glucose (glycogenolysis).',
  'id': 'endocrine-system',
  'key_note': 'Endocrine system: hormones in blood → target organs. Key glands: pituitary (master), thyroid '
              '(metabolism), adrenal (adrenaline), pancreas (insulin/glucagon), ovaries/testes (sex hormones). Slower '
              'but longer-lasting than nervous communication.',
  'matching': {'instruction': 'Match each gland to what it produces and what that hormone does.',
               'pairs': [('Pituitary gland', "FSH, LH and growth hormone — controls other glands — 'master gland'"),
                         ('Thyroid gland', 'Thyroxine — controls metabolic rate and development'),
                         ('Adrenal gland', 'Adrenaline — fight or flight, increases heart rate and breathing'),
                         ('Pancreas', 'Insulin and glucagon — regulate blood glucose concentration'),
                         ('Ovaries', 'Oestrogen and progesterone — menstrual cycle and female characteristics'),
                         ('Testes', 'Testosterone — male characteristics and sperm production')],
               'title': 'Match the Gland to its Hormone and Function'},
  'quiz': [{'opts': [('Via the bloodstream — secreted directly into the blood by endocrine glands', True),
                     ('Via nerve fibres — along the same pathways as electrical impulses', False),
                     ('Through ducts that lead directly to the target organ', False),
                     ('They diffuse through tissue fluid between neighbouring cells only', False)],
            'q': 'How do hormones reach their target organs?',
            'wrong_explanations': {1: 'Hormones travel in BLOOD, not along nerves — this is the fundamental difference '
                                      'between the two communication systems.',
                                   2: 'EXOCRINE glands (e.g. salivary glands, sweat glands) use ducts. ENDOCRINE '
                                      'glands secrete directly into the blood — they have no ducts.',
                                   3: "Hormones travel long distances in the blood — they don't diffuse locally like "
                                      'paracrine signals.'}},
           {'opts': [('Adrenaline — released by the adrenal glands in response to stress or danger', True),
                     ('Insulin — released by the pancreas to lower blood glucose', False),
                     ('Thyroxine — released by the thyroid to increase metabolic rate', False),
                     ('Oestrogen — released by the ovaries to prepare the body for reproduction', False)],
            'q': "Which hormone prepares the body for 'fight or flight'?",
            'wrong_explanations': {1: 'Insulin lowers blood glucose — it is released after eating, not in response to '
                                      'danger.',
                                   2: 'Thyroxine controls long-term metabolic rate — it is not the emergency stress '
                                      'hormone.',
                                   3: 'Oestrogen is involved in the menstrual cycle — not in acute stress responses.'}},
           {'opts': [('Nervous = fast, short-lived, specific target via nerves. Hormonal = slower, longer-lasting, via '
                      'bloodstream to target organs.',
                      True),
                     ('Nervous = slow, long-lasting. Hormonal = fast, short-lived.', False),
                     ('They work in the same way — both use chemicals to transmit signals.', False),
                     ('Nervous system only controls muscles. Hormonal system only controls glands.', False)],
            'q': 'Which best describes the difference between nervous and hormonal communication?',
            'wrong_explanations': {1: 'This is exactly the wrong way round. Nervous is FAST and SHORT. Hormonal is '
                                      'SLOWER and LONGER-LASTING.',
                                   2: 'Both do use chemicals at some point (neurotransmitters at synapses / hormones '
                                      'in blood) — but their overall mechanisms, speeds and targets are very '
                                      'different.',
                                   3: 'The nervous system controls both muscles AND glands. Hormones affect many '
                                      'different tissues — not just glands.'}}],
  'rp': None,
  'spec': '4.5.3',
  'summary': 'Describe the endocrine system, the main glands and hormones, and compare hormonal with nervous '
             'communication.',
  'theory': [{'content': "The ENDOCRINE SYSTEM is the body's chemical communication system.\n"
                         '\n'
                         'It uses HORMONES — chemical messenger molecules — to coordinate responses across the body.\n'
                         '\n'
                         'Hormones are produced by ENDOCRINE GLANDS and secreted DIRECTLY INTO THE BLOODSTREAM — they '
                         'have no ducts (unlike exocrine glands like salivary glands which have ducts).\n'
                         '\n'
                         'The blood carries hormones to every organ in the body — but only TARGET ORGANS respond, '
                         'because only they have the correct RECEPTOR PROTEINS for that hormone.\n'
                         '\n'
                         'Hormonal responses are:\n'
                         'SLOWER to start than nervous responses (blood must carry the hormone to the target).\n'
                         'LONGER LASTING than nervous responses.\n'
                         'More WIDESPREAD — hormones reach all organs (though only targets respond).',
              'heading': 'What is the Endocrine System?'},
             {'content': 'PITUITARY GLAND (in the brain — below the hypothalamus):\n'
                         "The 'master gland' — releases hormones that control other endocrine glands.\n"
                         'Produces: FSH and LH (control reproduction), growth hormone, ADH (water balance).\n'
                         '\n'
                         'THYROID GLAND (in the neck):\n'
                         'Produces THYROXINE — controls METABOLIC RATE (the speed of chemical reactions in cells).\n'
                         'Also involved in growth and development.\n'
                         '\n'
                         'ADRENAL GLANDS (above the kidneys — one on each kidney):\n'
                         "Produce ADRENALINE — the 'fight or flight' hormone.\n"
                         'Released in response to stress, fear or excitement.\n'
                         'Effects: increased heart rate, increased breathing rate, pupils dilate, blood redirected to '
                         'muscles.\n'
                         'Prepares the body for rapid physical action.\n'
                         '\n'
                         'PANCREAS:\n'
                         'Produces INSULIN and GLUCAGON — regulate blood glucose concentration (see next subtopic).\n'
                         '\n'
                         'OVARIES (females):\n'
                         'Produce OESTROGEN and PROGESTERONE — control the menstrual cycle and female secondary sexual '
                         'characteristics.\n'
                         '\n'
                         'TESTES (males):\n'
                         'Produce TESTOSTERONE — controls male secondary sexual characteristics and sperm production.',
              'heading': 'Key Endocrine Glands and Their Hormones'},
             {'content': 'The nervous system and endocrine system both communicate and coordinate responses, but work '
                         'differently:\n'
                         '\n'
                         'NERVOUS SYSTEM:\n'
                         'Signal type: electrical impulse along neurones.\n'
                         'Speed: very fast — up to 120 m/s.\n'
                         'Duration: short-lived (milliseconds to seconds).\n'
                         'Target: specific cells connected by nerve fibres.\n'
                         'Response: immediate and precise.\n'
                         'Examples: muscle contraction, reflex arc, heart rate control.\n'
                         '\n'
                         'ENDOCRINE SYSTEM:\n'
                         'Signal type: chemical hormone in bloodstream.\n'
                         'Speed: slower — limited by blood flow speed.\n'
                         'Duration: longer lasting (minutes to hours or even days).\n'
                         'Target: any organ with the correct receptor.\n'
                         'Response: prolonged, broader.\n'
                         'Examples: blood glucose regulation, puberty, growth, stress response.\n'
                         '\n'
                         'BOTH SYSTEMS WORK TOGETHER:\n'
                         'For example, during an emergency:\n'
                         'The NERVOUS SYSTEM detects danger and triggers an immediate response (e.g. jump back).\n'
                         'The ENDOCRINE SYSTEM releases adrenaline to sustain the response over the next few minutes.',
              'heading': 'Nervous vs Hormonal Communication'}],
  'title': 'The Endocrine System',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'INSULIN lowers blood glucose by promoting GLYCOGEN STORAGE (glucose → glycogen). GLUCAGON raises '
                    'blood glucose by promoting GLYCOGEN BREAKDOWN (glycogen → glucose). Students constantly confuse '
                    'which hormone does which. Memory trick: INsulin = INto storage. Glucagon = Get glucose out of '
                    'storage.',
  'equations': [],
  'fifas': [{'label': 'Blood Glucose Negative Feedback',
             'question': 'Describe what happens to blood glucose and hormones after a person eats a meal containing a '
                         'large amount of carbohydrates.',
             'steps': [('F', 'Identify the change: carbohydrates digested → glucose absorbed → blood glucose RISES'),
                       ('I', 'Pancreas beta cells detect the rise → release INSULIN into the blood'),
                       ('F', 'Insulin travels to liver and muscles → glucose converted to glycogen (glycogenesis)'),
                       ('A', 'Blood glucose FALLS back to ~5 mmol/L — negative feedback complete')]}],
  'higher': 'Insulin (from pancreatic beta cells) causes glucose uptake and glycogenesis (glucose → glycogen). '
            'Glucagon (from alpha cells) causes glycogenolysis (glycogen → glucose) and gluconeogenesis (making new '
            'glucose). Negative feedback maintains blood glucose at ~4–6 mmol/L. Type 1: autoimmune destruction of '
            'beta cells — insulin injections essential (cannot take orally as insulin is a protein, digested in gut). '
            'Type 2: insulin resistance — managed with diet, exercise, metformin. Both lead to hyperglycaemia if '
            'untreated.',
  'id': 'blood-glucose-diabetes',
  'key_note': 'Glucose too high → pancreas releases INSULIN → glycogen stored → glucose falls. Glucose too low → '
              'pancreas releases GLUCAGON → glycogen broken down → glucose rises. Type 1: no insulin (autoimmune). '
              'Type 2: insulin resistance (lifestyle).',
  'matching': {'instruction': 'Match each statement to the correct hormone — insulin or glucagon.',
               'pairs': [('Insulin', 'Released when blood glucose is TOO HIGH — after eating a meal'),
                         ('Glucagon', 'Released when blood glucose is TOO LOW — between meals or after exercise'),
                         ('Insulin', 'Causes liver and muscle cells to convert glucose → glycogen for storage'),
                         ('Glucagon', 'Causes liver cells to break down glycogen → glucose and release it into blood'),
                         ('Insulin', 'Missing or ineffective in diabetes — leads to hyperglycaemia if untreated')],
               'title': 'Insulin or Glucagon?'},
  'quiz': [{'opts': [('Insulin — released by pancreas beta cells, causes glucose to be converted to glycogen in the '
                      'liver',
                      True),
                     ('Glucagon — released by pancreas alpha cells, causes glycogen to be broken down', False),
                     ('Adrenaline — released by adrenal glands, increases blood glucose further', False),
                     ('Thyroxine — released by thyroid, converts glucose to glycogen', False)],
            'q': 'Blood glucose rises after eating. Which hormone is released and what does it do?',
            'wrong_explanations': {1: 'Glucagon is released when blood glucose is TOO LOW — it would make a post-meal '
                                      'rise even worse.',
                                   2: 'Adrenaline does raise blood glucose (for fight or flight) — but is not the '
                                      'routine homeostatic response to eating.',
                                   3: 'Thyroxine controls metabolic rate — it does not regulate blood glucose '
                                      'directly.'}},
           {'opts': [('Insulin is a protein — it would be digested and destroyed by proteases in the gut before '
                      'reaching the blood',
                      True),
                     ("Insulin tablets haven't been invented yet", False),
                     ('The stomach acid destroys insulin too slowly for it to work', False),
                     ('Tablets cannot reach the pancreas where insulin needs to work', False)],
            'q': 'Why must Type 1 diabetics inject insulin rather than take it as a tablet?',
            'wrong_explanations': {1: 'Oral insulin formulations are being researched (with special protective '
                                      'coatings) but the traditional reason is protein digestion in the gut.',
                                   2: "It's not about speed — insulin is a large protein molecule that gets broken "
                                      'down into amino acids by digestive enzymes before being absorbed.',
                                   3: "Insulin doesn't work IN the pancreas — it is secreted by the pancreas and works "
                                      'on LIVER and MUSCLE cells. The issue is gut digestion.'}},
           {'opts': [('Type 1: pancreas produces no insulin (autoimmune). Type 2: cells become resistant to insulin '
                      '(lifestyle-related).',
                      True),
                     ('Type 1 is more common than Type 2', False),
                     ('Type 2 requires insulin injections; Type 1 can be managed with diet alone', False),
                     ('Both types are caused by the immune system destroying pancreas cells', False)],
            'q': 'What is the key difference between Type 1 and Type 2 diabetes?',
            'wrong_explanations': {1: 'Type 2 is FAR MORE COMMON — it makes up about 90% of all diabetes cases. Type 1 '
                                      'is less common.',
                                   2: 'This is the wrong way round. TYPE 1 requires insulin injections because the '
                                      'pancreas cannot make it. TYPE 2 is usually managed first with diet, exercise '
                                      'and tablets.',
                                   3: 'Only TYPE 1 is autoimmune. TYPE 2 develops due to insulin resistance — the '
                                      'immune system is not the cause.'}}],
  'rp': None,
  'spec': '4.5.3',
  'summary': 'Describe how insulin and glucagon regulate blood glucose, and explain Type 1 and Type 2 diabetes.',
  'theory': [{'content': 'Blood glucose concentration must be kept within a narrow range — approximately 4–6 mmol/L.\n'
                         '\n'
                         'TOO LOW (hypoglycaemia):\n'
                         'Brain cells are deprived of glucose → confusion, weakness, loss of consciousness, coma, '
                         'brain damage.\n'
                         'The brain depends almost entirely on glucose as its energy source.\n'
                         '\n'
                         'TOO HIGH (hyperglycaemia):\n'
                         'Long-term: glucose draws water out of cells by osmosis → dehydration of tissues.\n'
                         'Damages blood vessel walls → reduced blood supply → blindness, kidney failure, poor wound '
                         'healing.\n'
                         'Damages nerves → neuropathy (tingling, pain, numbness in hands and feet).\n'
                         'Increased risk of heart attack and stroke.\n'
                         '\n'
                         'The PANCREAS is the organ that monitors and regulates blood glucose — it contains '
                         'specialised cells that detect glucose concentration and release hormones accordingly.',
              'heading': 'Why Blood Glucose Must Be Controlled'},
             {'content': 'After eating a meal:\n'
                         'Carbohydrates are digested → glucose absorbed into blood → blood glucose RISES.\n'
                         'Pancreas BETA CELLS detect the rise and release INSULIN into the bloodstream.\n'
                         '\n'
                         'Insulin travels to the LIVER and MUSCLE CELLS and causes them to:\n'
                         'Absorb MORE glucose from the blood.\n'
                         'Convert glucose → GLYCOGEN (a storage polymer) — this is called GLYCOGENESIS.\n'
                         '\n'
                         'Blood glucose concentration FALLS back to the set point.\n'
                         '\n'
                         'This is NEGATIVE FEEDBACK — the response (insulin release + glucose storage) opposes the '
                         'original change (rising glucose).',
              'heading': 'Insulin — Lowering Blood Glucose'},
             {'content': 'Between meals, during fasting or after exercise:\n'
                         'Cells use glucose for respiration → blood glucose FALLS.\n'
                         'Pancreas ALPHA CELLS detect the fall and release GLUCAGON into the bloodstream.\n'
                         '\n'
                         'Glucagon travels to the LIVER and causes it to:\n'
                         'Break down stored GLYCOGEN back into glucose — this is called GLYCOGENOLYSIS.\n'
                         'Release glucose back into the blood.\n'
                         '\n'
                         'Blood glucose concentration RISES back to the set point.\n'
                         '\n'
                         'Again this is NEGATIVE FEEDBACK — glucagon release opposes the fall in glucose.',
              'heading': 'Glucagon — Raising Blood Glucose'},
             {'content': 'Both types of diabetes result in poorly controlled blood glucose — but for different '
                         'reasons.\n'
                         '\n'
                         'TYPE 1 DIABETES:\n'
                         'Cause: The immune system attacks and destroys the BETA CELLS in the pancreas (autoimmune '
                         'condition).\n'
                         'Result: Little or no insulin produced — blood glucose cannot be lowered after eating.\n'
                         'Onset: Usually in childhood or adolescence.\n'
                         'Treatment: INSULIN INJECTIONS (or insulin pump) — insulin cannot be taken as a tablet '
                         'because it is a protein and would be digested.\n'
                         'Patients must monitor blood glucose and adjust insulin doses accordingly.\n'
                         '\n'
                         'TYPE 2 DIABETES:\n'
                         'Cause: Body cells become RESISTANT to insulin — they no longer respond to it properly. The '
                         "pancreas may still produce insulin, but it doesn't work.\n"
                         'Result: Blood glucose remains elevated after eating.\n'
                         'Risk factors: Obesity, lack of exercise, poor diet (high sugar/refined carbs), family '
                         'history, age.\n'
                         'Treatment: Lifestyle changes — weight loss, increased exercise, healthier diet.\n'
                         'Medication: Metformin (increases cell sensitivity to insulin).\n'
                         'In advanced cases: insulin injections may also be needed.',
              'heading': 'Type 1 and Type 2 Diabetes'}],
  'title': 'Blood Glucose Control and Diabetes',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'FSH stimulates EGG MATURATION (not ovulation). LH triggers OVULATION. Oestrogen REBUILDS the '
                    'uterus lining. Progesterone MAINTAINS the lining. The pituitary produces FSH and LH. The ovaries '
                    'produce oestrogen and progesterone. Students often confuse which gland makes which hormone.',
  'equations': [],
  'fifas': [],
  'higher': 'The full hormonal control of the menstrual cycle: FSH (pituitary) → follicle development and oestrogen '
            'production. Low oestrogen → inhibits FSH (negative feedback). Rising oestrogen → triggers LH surge '
            '(positive feedback at high concentration). LH surge → ovulation at Day ~14. Corpus luteum → progesterone '
            '→ maintains uterus lining, inhibits FSH and LH. No pregnancy → corpus luteum degenerates → progesterone '
            'falls → menstruation → FSH rises → new cycle.',
  'id': 'human-reproduction-hormones',
  'key_note': 'FSH (pituitary) → egg matures, oestrogen produced. Oestrogen (ovary) → uterus lining rebuilds. LH surge '
              '→ ovulation (Day ~14). Progesterone (corpus luteum) → maintains lining. If no pregnancy → progesterone '
              'falls → menstruation.',
  'matching': {'instruction': 'Match each hormone to its source and main function.',
               'pairs': [('FSH', 'From pituitary — causes egg to mature in follicle, stimulates oestrogen production'),
                         ('Oestrogen', 'From ovaries — repairs uterus lining, triggers LH surge at high levels'),
                         ('LH', 'From pituitary — surge at Day ~14 triggers ovulation'),
                         ('Progesterone', 'From corpus luteum — maintains uterus lining in second half of cycle'),
                         ('Testosterone',
                          'From testes — causes male secondary sexual characteristics and sperm production')],
               'title': 'Match the Reproductive Hormone'},
  'quiz': [{'opts': [('LH (Luteinising Hormone) — a surge at around Day 14 releases the egg from the follicle', True),
                     ('FSH — it stimulates the follicle to release the egg', False),
                     ('Oestrogen — high oestrogen directly causes egg release', False),
                     ('Progesterone — it relaxes the follicle wall to release the egg', False)],
            'q': 'Which hormone triggers ovulation?',
            'wrong_explanations': {1: "FSH stimulates EGG MATURATION — it prepares the follicle but doesn't trigger "
                                      'the release. The LH SURGE causes ovulation.',
                                   2: "High oestrogen causes the RELEASE OF LH from the pituitary — it's the "
                                      'subsequent LH surge that triggers ovulation, not oestrogen directly.',
                                   3: 'Progesterone is produced AFTER ovulation by the corpus luteum — it maintains '
                                      'the uterus lining. It does not trigger ovulation.'}},
           {'opts': [('Progesterone falls — the uterus lining breaks down — menstruation begins and the cycle restarts',
                      True),
                     ('Progesterone rises — signalling the body to prepare for pregnancy anyway', False),
                     ('Progesterone stays the same indefinitely until the next menstrual cycle', False),
                     ('Progesterone triggers FSH release to immediately start a new cycle', False)],
            'q': 'What happens to progesterone levels if fertilisation does NOT occur?',
            'wrong_explanations': {1: "Progesterone rising would signal PREGNANCY — which hasn't occurred. Without an "
                                      'embryo producing hormones, the corpus luteum degenerates and progesterone '
                                      'falls.',
                                   2: 'Progesterone cannot stay elevated indefinitely — the corpus luteum degenerates '
                                      'after about 14 days without an embryo implanting.',
                                   3: 'FSH is released at the start of a new cycle as progesterone falls — but it is '
                                      'oestrogen and progesterone levels, not progesterone directly stimulating FSH.'}},
           {'opts': [('Repairs and thickens the uterus lining after menstruation — also triggers the LH surge at high '
                      'levels',
                      True),
                     ('Triggers ovulation directly at low concentrations', False),
                     ('Maintains the uterus lining in the second half of the cycle', False),
                     ('Stimulates egg maturation in the follicle', False)],
            'q': 'What is the role of oestrogen in the menstrual cycle?',
            'wrong_explanations': {1: 'Oestrogen at HIGH concentrations triggers LH release, and LH causes ovulation — '
                                      'but at LOW concentrations, oestrogen inhibits FSH, not triggers ovulation.',
                                   2: 'Maintaining the uterus lining in the second half = PROGESTERONE. Oestrogen '
                                      'rebuilds it in the first half.',
                                   3: 'Stimulating egg maturation = FSH. Oestrogen is produced AS A RESULT of FSH '
                                      'stimulation, not a cause of egg maturation.'}}],
  'rp': None,
  'spec': '4.5.4',
  'summary': 'Describe puberty, the menstrual cycle and the hormones that control human reproduction.',
  'theory': [{'content': 'PUBERTY is the period of physical and hormonal development that prepares the body for '
                         'reproduction.\n'
                         '\n'
                         'In FEMALES: the pituitary gland releases FSH and LH → ovaries begin producing OESTROGEN.\n'
                         'Oestrogen causes female secondary sexual characteristics:\n'
                         'Breast development.\n'
                         'Widening of the pelvis.\n'
                         'Pubic and underarm hair growth.\n'
                         'Beginning of the menstrual cycle.\n'
                         'Growth spurt.\n'
                         '\n'
                         'In MALES: the pituitary gland releases LH → testes begin producing TESTOSTERONE.\n'
                         'Testosterone causes male secondary sexual characteristics:\n'
                         'Enlargement of the penis and testes.\n'
                         'Voice breaking (larynx enlarges).\n'
                         'Facial, pubic and body hair growth.\n'
                         'Muscle mass increase.\n'
                         'Sperm production begins (spermatogenesis).\n'
                         'Growth spurt.',
              'heading': 'Puberty and Sex Hormones'},
             {'content': 'The menstrual cycle is approximately 28 days long (varies between individuals).\n'
                         '\n'
                         'It prepares the female reproductive system for potential pregnancy each month.\n'
                         '\n'
                         'Day 1: MENSTRUATION begins — the uterus lining (endometrium) is shed as the lining breaks '
                         'down.\n'
                         'Days 1–13: The uterus lining rebuilds and thickens — stimulated by oestrogen.\n'
                         'Day ~14: OVULATION — a mature egg is released from one of the ovaries.\n'
                         'Days 14–28: The uterus lining remains thick (prepared for implantation if fertilisation '
                         'occurs) — maintained by progesterone.\n'
                         '\n'
                         'If FERTILISATION occurs: the embryo implants in the uterus wall and pregnancy begins. '
                         'Progesterone remains high.\n'
                         'If NO FERTILISATION: progesterone falls, the uterus lining breaks down → menstruation begins '
                         'and the cycle repeats.',
              'heading': 'The Menstrual Cycle — Overview'},
             {'content': 'Four hormones work together to control the menstrual cycle:\n'
                         '\n'
                         'FSH (Follicle Stimulating Hormone) — from the PITUITARY GLAND:\n'
                         'Causes an egg inside a follicle to mature in the ovary.\n'
                         'Stimulates the ovaries to produce oestrogen.\n'
                         '\n'
                         'OESTROGEN — from the OVARIES:\n'
                         'Repairs and thickens the uterus lining after menstruation.\n'
                         'At low levels: inhibits FSH production (prevents too many eggs maturing at once).\n'
                         'At HIGH levels (mid-cycle): triggers a surge in LH production.\n'
                         '\n'
                         'LH (Luteinising Hormone) — from the PITUITARY GLAND:\n'
                         'The LH surge at approximately Day 14 triggers OVULATION — the egg is released from the '
                         'follicle.\n'
                         '\n'
                         'PROGESTERONE — from the CORPUS LUTEUM (the remains of the follicle after ovulation):\n'
                         'Maintains the thickened uterus lining during the second half of the cycle.\n'
                         'Inhibits FSH and LH production (negative feedback).\n'
                         'If no pregnancy: corpus luteum breaks down → progesterone falls → lining breaks down → '
                         'menstruation begins.',
              'heading': 'Hormones Controlling the Menstrual Cycle'}],
  'title': 'Human Reproduction and Hormones',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'The contraceptive pill does NOT protect against STIs — only BARRIER METHODS (condoms) protect '
                    'against both pregnancy AND sexually transmitted infections. The combined pill prevents OVULATION '
                    'by inhibiting FSH — without ovulation, there is no egg to fertilise. In IVF, FSH is given to '
                    'stimulate MULTIPLE egg production — not to help with implantation (progesterone does that).',
  'equations': [],
  'fifas': [],
  'higher': 'The combined pill uses oestrogen to inhibit FSH (preventing egg maturation) and progesterone to thicken '
            'cervical mucus. IVF process: FSH stimulation → egg collection → in vitro fertilisation → embryo culture → '
            'transfer to uterus + progesterone to maintain lining. Ethical issues: disposal of unused embryos, risk of '
            'multiple births, access and cost, use of donor eggs/sperm. Students should be able to evaluate these '
            'issues from multiple perspectives.',
  'id': 'contraception-fertility',
  'key_note': 'Hormonal contraception: prevents ovulation (pill, implant, injection). Barrier methods: prevent sperm '
              'reaching egg, ALSO prevent STIs. IVF: FSH → multiple eggs → fertilised in lab → embryo implanted. '
              'Copper IUD: no hormones, sperm toxic.',
  'matching': {'instruction': 'Match each method to how it prevents pregnancy.',
               'pairs': [('Combined pill', 'Contains oestrogen — inhibits FSH → prevents egg maturation and ovulation'),
                         ('Male condom', 'Barrier method — stops sperm reaching egg — ALSO prevents STIs'),
                         ('Copper IUD', 'Copper ions are toxic to sperm — no hormones involved'),
                         ('Implant', 'Releases progesterone under the skin for up to 3 years — prevents ovulation'),
                         ('Vasectomy', 'Cuts the vas deferens — sperm cannot be released during ejaculation')],
               'title': 'Match the Contraceptive to its Mechanism'},
  'quiz': [{'opts': [('Condoms (male or female) — barrier methods prevent both pregnancy and STI transmission', True),
                     ('The combined contraceptive pill', False),
                     ('The copper IUD', False),
                     ('The contraceptive implant', False)],
            'q': 'Which contraceptive method ALSO protects against sexually transmitted infections?',
            'wrong_explanations': {1: 'The pill prevents pregnancy hormonally but does not prevent STI transmission — '
                                      'pathogens can still be exchanged.',
                                   2: "The copper IUD works inside the uterus — it doesn't prevent STI transmission "
                                      'during sexual contact.',
                                   3: 'The implant prevents ovulation — it provides no barrier against pathogen '
                                      'transmission.'}},
           {'opts': [('To stimulate the ovaries to produce multiple eggs so more can be collected and fertilised',
                      True),
                     ('To prepare the uterus lining for embryo implantation', False),
                     ('To prevent the immune system from rejecting the embryo', False),
                     ('To fertilise the eggs in the laboratory', False)],
            'q': 'In IVF, why is FSH given to the woman at the start of treatment?',
            'wrong_explanations': {1: 'Preparing the uterus lining for implantation = PROGESTERONE — given later in '
                                      'IVF treatment. FSH specifically stimulates egg production.',
                                   2: 'Immune suppression is managed separately — FSH is specifically a reproductive '
                                      'hormone that drives follicle development and egg production.',
                                   3: 'Fertilisation is done by adding sperm to eggs in a laboratory dish — FSH is a '
                                      'hormone, not a fertilisation agent.'}},
           {'opts': [('The oestrogen it contains inhibits FSH production — no FSH means no egg maturation and no '
                      'ovulation',
                      True),
                     ('It thickens the cervical mucus so sperm cannot swim through', False),
                     ('It prevents sperm from entering the vagina during sex', False),
                     ('It causes the uterus lining to shed more frequently', False)],
            'q': 'How does the combined contraceptive pill prevent pregnancy?',
            'wrong_explanations': {1: 'Thickening cervical mucus = PROGESTERONE-ONLY PILL (mini-pill). The COMBINED '
                                      'pill works primarily by suppressing ovulation through oestrogen inhibiting FSH.',
                                   2: 'Preventing sperm entering = BARRIER METHODS (condoms, diaphragm). The pill has '
                                      'no physical barrier effect.',
                                   3: 'The combined pill actually STABILISES the uterus lining — frequent shedding '
                                      "would be a side effect of other hormone imbalances, not the pill's "
                                      'mechanism.'}}],
  'rp': None,
  'spec': '4.5.4',
  'summary': 'Describe methods of contraception and fertility treatments including IVF.',
  'theory': [{'content': 'Contraception prevents pregnancy by interfering with fertilisation, ovulation or '
                         'implantation.\n'
                         '\n'
                         'HORMONAL METHODS — prevent ovulation:\n'
                         'COMBINED PILL — contains oestrogen and progesterone. Oestrogen inhibits FSH production → no '
                         'egg maturation → no ovulation. Taken daily.\n'
                         'PROGESTERONE-ONLY PILL (mini-pill) — thickens cervical mucus (stops sperm reaching egg) and '
                         'may also prevent ovulation.\n'
                         'IMPLANT — small rod inserted under skin of upper arm, releases progesterone for up to 3 '
                         'years. Prevents ovulation.\n'
                         'INJECTION — progesterone injected every 8–12 weeks. Prevents ovulation.\n'
                         'HORMONAL IUD (Mirena coil) — releases progesterone locally in the uterus.\n'
                         '\n'
                         'BARRIER METHODS — prevent sperm reaching the egg:\n'
                         'MALE CONDOM — placed over the penis. ALSO protects against STIs — the only contraceptive '
                         'that does this.\n'
                         'FEMALE CONDOM — inserted into the vagina. Also protects against STIs.\n'
                         'DIAPHRAGM — placed over the cervix before sex.\n'
                         '\n'
                         'NON-HORMONAL:\n'
                         'COPPER IUD (copper coil) — T-shaped device placed in the uterus. Copper ions are toxic to '
                         'sperm. No hormones involved.\n'
                         '\n'
                         'SURGICAL (permanent):\n'
                         'VASECTOMY — vas deferens cut or tied in males → sperm cannot be released.\n'
                         'TUBAL LIGATION — fallopian tubes cut or tied in females → eggs cannot reach the uterus.',
              'heading': 'Methods of Contraception'},
             {'content': 'Some couples have difficulty conceiving naturally. Medical treatments can help.\n'
                         '\n'
                         'FSH AND LH TREATMENT (fertility drugs):\n'
                         "Women who don't ovulate regularly are prescribed FSH (and sometimes LH) to stimulate egg "
                         'maturation and ovulation.\n'
                         'Risk: can cause multiple eggs to mature at once → multiple pregnancy (twins, triplets).\n'
                         '\n'
                         'IN VITRO FERTILISATION (IVF):\n'
                         "'In vitro' means 'in glass' — fertilisation takes place in a laboratory dish, outside the "
                         'body.\n'
                         '\n'
                         'The IVF process:\n'
                         '1. The woman is given FSH (and LH) to stimulate the ovaries to produce multiple eggs.\n'
                         '2. Eggs are collected from the ovaries using a fine needle under sedation.\n'
                         '3. Eggs are mixed with sperm in a laboratory dish — fertilisation occurs.\n'
                         '4. Embryos develop for 2–5 days in the laboratory.\n'
                         "5. One or two embryos are placed into the woman's uterus through the cervix.\n"
                         '6. Progesterone is given to help maintain the uterus lining for implantation.\n'
                         '7. If an embryo implants successfully, pregnancy begins.\n'
                         '\n'
                         'Success rates: approximately 30–40% per cycle for women under 35, declining with age.',
              'heading': 'Fertility Treatments'},
             {'content': 'Both contraception and fertility treatment raise important ethical questions.\n'
                         '\n'
                         'CONTRACEPTION:\n'
                         'Some religious groups oppose artificial contraception (e.g. the Catholic Church teaches '
                         'natural family planning only).\n'
                         "Emergency contraception ('morning-after pill') is controversial — some consider it "
                         'preventing implantation of a fertilised egg.\n'
                         'Condoms are widely supported as they also prevent spread of STIs.\n'
                         '\n'
                         'FERTILITY TREATMENT (IVF):\n'
                         'Multiple embryos are often created — unused embryos may be frozen, destroyed or donated to '
                         'research. This raises questions about the moral status of embryos.\n'
                         'Pre-implantation genetic diagnosis (PGD) — testing embryos for genetic conditions before '
                         "implantation. Raises concerns about 'designer babies'.\n"
                         'IVF is expensive — raises questions about who should have access.\n'
                         'The physical and emotional burden on women undergoing IVF is significant.\n'
                         'Donor eggs or sperm raise questions about identity and donor anonymity.',
              'heading': 'Ethical Considerations'}],
  'title': 'Contraception and Fertility Treatment',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'When calculating reaction time from the ruler drop test — distance must be in METRES (not cm). g '
                    '= 10 m/s² (or 9.8 m/s² for more precision). Rearrange d = ½gt² to get t = √(2d/g). Always take '
                    'multiple repeats and use the MEAN — single measurements are unreliable.',
  'equations': ['d = ½ × g × t²', 't = √(2d ÷ g)'],
  'fifas': [{'label': 'Reaction Time Calculation',
             'question': 'A ruler falls 20 cm before being caught. Calculate the reaction time. (g = 10 m/s²)',
             'steps': [('F', 't = √(2d ÷ g)'),
                       ('I', 'd = 20 cm = 0.20 m. t = √(2 × 0.20 ÷ 10)'),
                       ('F', 't = √(0.40 ÷ 10) = √0.04'),
                       ('A', 't = 0.2 seconds')]}],
  'higher': None,
  'id': 'reaction-time',
  'key_note': 'Reaction time: time from stimulus to response. Ruler drop test: measure distance fallen → calculate '
              'time using t = √(2d/g). Affected by: fatigue, alcohol, drugs, age, distraction. Multiple repeats → mean '
              'for reliability.',
  'matching': {'instruction': 'Does each factor increase or decrease reaction time?',
               'pairs': [('Increases reaction time', 'Alcohol — a depressant that slows synaptic transmission'),
                         ('Decreases reaction time', 'Caffeine — a stimulant that increases neurotransmitter activity'),
                         ('Increases reaction time', 'Fatigue — tired nervous system responds more slowly'),
                         ('Increases reaction time', 'Distraction — divided attention reduces processing speed'),
                         ('Decreases reaction time', 'Practice — repeated performance improves speed of response')],
               'title': 'Match the Factor to its Effect on Reaction Time'},
  'quiz': [{'opts': [('t = √(2 × 0.45 ÷ 10) = √0.09 = 0.30 s', True),
                     ('t = √(2 × 45 ÷ 10) = 3.0 s', False),
                     ('t = 0.45 ÷ 10 = 0.045 s', False),
                     ('t = 2 × 0.45 × 10 = 9.0 s', False)],
            'q': 'In a ruler drop test, a ruler falls 45 cm before being caught. Which calculation gives the reaction '
                 'time? (g = 10 m/s²)',
            'wrong_explanations': {1: '45 cm must be converted to metres (0.45 m) before using in the formula. Using '
                                      '45 gives a nonsensically large answer.',
                                   2: 't = d/g is not the correct formula. The correct rearrangement of d = ½gt² gives '
                                      't = √(2d/g).',
                                   3: 'Multiplying gives a large number — the formula requires square root of (2d/g), '
                                      'not multiplication of all terms.'}},
           {'opts': [('Reaction time varies randomly between trials — the mean gives a more reliable estimate of true '
                      'reaction time',
                      True),
                     ('The ruler wears out and becomes less accurate after each drop', False),
                     ("The person's brain learns the formula and gets better at calculating the answer", False),
                     ('Multiple repeats prevent the person from practising and improving', False)],
            'q': 'Why should a reaction time experiment use multiple repeats and calculate the mean?',
            'wrong_explanations': {1: "Rulers don't wear out with use — the variation is in the human nervous system "
                                      'response, not the equipment.',
                                   2: 'The person does not calculate anything during the experiment — they simply '
                                      'catch the ruler. Multiple repeats address random biological variation.',
                                   3: 'Practice effects are a potential confound — but the PRIMARY reason for multiple '
                                      'repeats is to reduce random variation in measurements.'}}],
  'rp': None,
  'spec': '4.5.2',
  'summary': 'Describe how to measure reaction time and explain what affects it.',
  'theory': [{'content': 'REACTION TIME is the time between a stimulus being detected and a response being made.\n'
                         '\n'
                         'It involves the complete nervous system pathway:\n'
                         'Stimulus detected by receptor → electrical impulse along sensory neurone → relay neurone in '
                         'CNS → motor neurone → effector responds.\n'
                         '\n'
                         'Typical human reaction time: 0.2–0.3 seconds for a simple stimulus.\n'
                         '\n'
                         'Reaction time varies between individuals and is affected by several factors:\n'
                         'AGE — reaction time generally increases (worsens) with age.\n'
                         'GENDER — some research suggests small differences between males and females.\n'
                         'STIMULUS TYPE — auditory (sound) reactions are slightly faster than visual (light) '
                         'reactions.\n'
                         'PRACTICE — repeated performance improves reaction time.\n'
                         'FATIGUE — tiredness slows reaction time significantly.\n'
                         'DRUGS AND ALCOHOL — depressants (alcohol, sedatives) slow reaction time; stimulants '
                         '(caffeine) may slightly improve it.\n'
                         'DISTRACTION — dividing attention (e.g. using a phone while driving) significantly increases '
                         'reaction time.',
              'heading': 'What is Reaction Time?'},
             {'content': 'The RULER DROP TEST is a simple method to measure reaction time:\n'
                         '\n'
                         'METHOD:\n'
                         '1. Person A holds a ruler vertically with the 0 cm mark at the bottom.\n'
                         '2. Person B places their thumb and finger at the 0 cm mark, not touching the ruler.\n'
                         '3. Without warning, Person A drops the ruler.\n'
                         '4. Person B catches it as quickly as possible.\n'
                         '5. The distance the ruler falls before being caught is measured.\n'
                         '6. Use the distance to calculate reaction time using the formula: d = ½ × g × t²\n'
                         '   Rearranging: t = √(2d/g) where g = 10 m/s².\n'
                         '7. Repeat multiple times and calculate the MEAN to reduce the effect of random variation.\n'
                         '\n'
                         'IMPROVING RELIABILITY:\n'
                         'Conduct multiple repeats and calculate a mean.\n'
                         'Ensure no anticipation of the drop (no pattern or warning).\n'
                         'Keep conditions consistent (same ruler, same position, same person).\n'
                         '\n'
                         'COMPUTER-BASED TESTS:\n'
                         'More accurate than the ruler test — use a computer screen stimulus and measure time to press '
                         'a key.\n'
                         'Remove human error in reading the ruler distance.',
              'heading': 'Measuring Reaction Time — The Ruler Drop Test'},
             {'content': 'Common investigations into reaction time:\n'
                         '\n'
                         'EFFECT OF CAFFEINE:\n'
                         'Caffeine is a stimulant — it increases the release of neurotransmitters at synapses.\n'
                         'Hypothesis: caffeine will decrease reaction time (improve performance).\n'
                         'Method: measure reaction time before and after consuming caffeine. Compare to a placebo '
                         'group.\n'
                         'Controls: same person, same test, same time of day, account for practice effect.\n'
                         '\n'
                         'EFFECT OF DISTRACTION:\n'
                         'Using a phone or listening to music divides attention.\n'
                         'Hypothesis: distraction will increase reaction time.\n'
                         'Method: test reaction time with and without a distractor (e.g. mental arithmetic task '
                         'simultaneously).\n'
                         '\n'
                         'IMPORTANT: the ruler drop test has limitations:\n'
                         'Random variation — each trial can differ.\n'
                         'Subject may anticipate the drop.\n'
                         'Measuring exactly where the ruler is caught introduces error.\n'
                         'This is why multiple repeats and means are essential.',
              'heading': 'Factors Affecting Reaction Time — Investigations'}],
  'title': 'Reaction Time',
  'triple_only': None,
  'variables': [('d', 'Distance ruler falls', 'metres', 'm'),
                ('t', 'Reaction time', 'seconds', 's'),
                ('g', 'Gravitational field strength', 'm/s²', '')]},
 {'common_mistake': 'Students often mix up the three main brain regions. CEREBRAL CORTEX = thinking, memory, language, '
                    'voluntary movement. CEREBELLUM = coordination and balance. MEDULLA = heart rate and breathing '
                    "(vital automatic functions). A useful memory trick: 'Cerebellum = coordination' (both start with "
                    "C and 'coordination').",
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'the-brain',
  'key_note': 'Cerebral cortex: consciousness, intelligence, memory, personality. Cerebellum: coordination, balance. '
              'Medulla: heart rate, breathing — vital automatic functions. Studied by: MRI, EEG, electrical '
              'stimulation, brain damage case studies. Hard to treat: no neurone regeneration, blood-brain barrier.',
  'matching': {'instruction': 'Match each brain region to what it controls.',
               'pairs': [('Cerebral cortex', 'Consciousness, memory, language, intelligence, voluntary movement'),
                         ('Cerebellum', 'Coordination of movement, balance and posture'),
                         ('Medulla oblongata', 'Heart rate, breathing rate — unconscious vital functions'),
                         ('fMRI scan', 'Shows which brain regions are active by detecting changes in blood flow'),
                         ('EEG', 'Records electrical activity of the brain via electrodes on the scalp')],
               'title': 'Match the Brain Region to its Function'},
  'quiz': [{'opts': [('Coordination and balance — the cerebellum controls smooth, coordinated movement', True),
                     ('Heart rate — the cerebellum controls autonomic functions', False),
                     ('Memory and language — the cerebellum controls higher cognitive functions', False),
                     ('Breathing — the cerebellum controls respiratory rate', False)],
            'q': 'A patient suffers a stroke affecting the cerebellum. Which function is most likely to be impaired?',
            'wrong_explanations': {1: 'Heart rate and breathing are controlled by the MEDULLA OBLONGATA — not the '
                                      'cerebellum.',
                                   2: 'Memory and language are controlled by the CEREBRAL CORTEX — not the cerebellum.',
                                   3: 'Breathing rate is controlled by the MEDULLA — the cerebellum coordinates '
                                      'movement.'}},
           {'opts': [('Adult brain neurones cannot regenerate — unlike most other body cells, damaged neurones are not '
                      'replaced',
                      True),
                     ('The blood-brain barrier prevents blood from reaching damaged areas', False),
                     ('Strokes destroy the entire brain — there is no undamaged tissue to repair from', False),
                     ('The immune system attacks any new neurones, preventing recovery', False)],
            'q': 'Why is it difficult to repair brain damage caused by a stroke?',
            'wrong_explanations': {1: 'The blood-brain barrier restricts what substances cross from blood to brain — '
                                      "it doesn't prevent blood from reaching the brain (in fact strokes are often "
                                      'caused by blood supply being cut off).',
                                   2: 'Strokes affect specific regions — not the whole brain. The challenge is neurone '
                                      'regeneration in those regions.',
                                   3: 'The immune system does play a role in brain inflammation after injury — but the '
                                      'primary reason for poor recovery is the inability of neurones to regenerate.'}}],
  'rp': None,
  'spec': '4.5.2.4',
  'summary': 'Describe the structure of the brain, the functions of its main regions and how the brain is studied.',
  'theory': [{'content': 'The BRAIN is the most complex organ in the human body — containing approximately 86 billion '
                         'neurones, each connected to thousands of others.\n'
                         '\n'
                         'The brain has several distinct regions, each responsible for different functions:\n'
                         '\n'
                         'CEREBRAL CORTEX (cerebrum):\n'
                         'The largest part of the brain — the highly folded outer layer.\n'
                         'Responsible for: consciousness, intelligence, memory, language, personality, voluntary '
                         'movement, sensory perception.\n'
                         'Divided into left and right hemispheres — each processes information from the opposite side '
                         'of the body.\n'
                         'The folded structure (gyri and sulci) increases surface area for more neurones.\n'
                         '\n'
                         'CEREBELLUM:\n'
                         'Located at the back and base of the brain.\n'
                         'Responsible for: coordination of movement, balance, posture, fine motor control.\n'
                         'Damage → loss of coordination and balance.\n'
                         '\n'
                         'MEDULLA OBLONGATA:\n'
                         'At the base of the brain, continuous with the spinal cord.\n'
                         'Controls: unconscious vital functions — heart rate, breathing rate, blood pressure, '
                         'swallowing, vomiting.\n'
                         'Damage is life-threatening — these functions are essential for survival.',
              'heading': 'Structure of the Brain'},
             {'content': 'The brain is extremely complex and difficult to study — it cannot easily be biopsied or '
                         'experimented on safely.\n'
                         '\n'
                         'METHODS:\n'
                         '\n'
                         'ELECTROENCEPHALOGRAPHY (EEG):\n'
                         'Electrodes placed on the scalp record electrical activity of the brain as patterns of '
                         'waves.\n'
                         'Used to diagnose epilepsy and sleep disorders.\n'
                         'Shows which areas are active but with limited spatial resolution.\n'
                         '\n'
                         'FUNCTIONAL MRI (fMRI):\n'
                         'Detects changes in blood flow to different brain regions — more active regions need more '
                         'blood and oxygen.\n'
                         'Produces detailed 3D images showing which brain regions are active during different tasks.\n'
                         'Allows mapping of brain function non-invasively.\n'
                         'Used in research to understand language, memory, emotion and decision-making.\n'
                         '\n'
                         'ELECTRICAL STIMULATION:\n'
                         'Neurosurgeons can stimulate specific brain regions electrically during brain surgery '
                         '(patient kept awake).\n'
                         'The patient reports what they experience — helping identify which areas control which '
                         'functions.\n'
                         'Led to early mapping of sensory and motor areas.\n'
                         '\n'
                         'STUDYING BRAIN DAMAGE:\n'
                         'Case studies of patients with specific brain injuries have provided crucial insights.\n'
                         'Famous case: Phineas Gage — a railway worker whose personality changed dramatically after a '
                         'rod passed through his frontal lobe (1848).\n'
                         'Patient HM — removal of hippocampus to treat epilepsy caused inability to form new long-term '
                         'memories.',
              'heading': 'How We Study the Brain'},
             {'content': 'Treating brain conditions is extremely challenging:\n'
                         '\n'
                         'BLOOD-BRAIN BARRIER:\n'
                         'A layer of tightly packed cells around brain blood vessels that prevents many substances '
                         'from crossing from blood into brain tissue.\n'
                         'Protects the brain from pathogens and toxins — but also prevents many drugs from reaching '
                         'brain tissue.\n'
                         'Drug delivery to the brain is a major challenge in neurology and psychiatry.\n'
                         '\n'
                         'NEURONE REPAIR:\n'
                         'Unlike most body tissues, adult brain neurones cannot regenerate if damaged.\n'
                         'This is why brain injuries (stroke, trauma) often cause permanent deficits.\n'
                         'Stem cell research aims to find ways to regenerate damaged brain tissue.\n'
                         '\n'
                         'ETHICAL CONSTRAINTS:\n'
                         'Brain tissue cannot be biopsied safely — unlike a tumour elsewhere.\n'
                         'Experimentation is limited by the ethical requirement to protect patients.\n'
                         'Much of our knowledge comes from accidents, disease and animal studies.',
              'heading': 'Why the Brain is Difficult to Treat'}],
  'title': 'The Brain',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'For near vision: ciliary muscles CONTRACT and lens becomes more ROUNDED. For far vision: ciliary '
                    'muscles RELAX and lens becomes FLATTER. Students often get this backwards. Remember: when you '
                    'look at something NEAR, the ciliary muscle has to work hard (CONTRACT) to make the lens rounder.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'the-eye',
  'key_note': 'Cornea: main refraction. Lens: fine focus (accommodation). Near: ciliary contracts → lens round. Far: '
              'ciliary relaxes → lens flat. Retina: rods (dim/mono), cones (colour/bright). Fovea: sharpest vision. '
              'Optic nerve → brain.',
  'matching': {'instruction': 'Match each structure to what it does.',
               'pairs': [('Cornea', "Transparent curved surface — provides most of the eye's refraction"),
                         ('Iris', 'Coloured ring of muscle — controls pupil size and light entry'),
                         ('Lens', 'Flexible disc — fine-tunes focus by changing shape (accommodation)'),
                         ('Ciliary muscle', 'Contracts or relaxes to change lens shape via suspensory ligaments'),
                         ('Retina',
                          'Light-sensitive layer — contains rods and cones that convert light to electrical signals'),
                         ('Optic nerve', 'Carries electrical impulses from the retina to the brain')],
               'title': 'Match the Eye Structure to its Function'},
  'quiz': [{'opts': [('Ciliary muscles contract → suspensory ligaments slacken → lens becomes more rounded for near '
                      'vision',
                      True),
                     ('Ciliary muscles relax → suspensory ligaments become taut → lens becomes flatter for near vision',
                      False),
                     ('Ciliary muscles contract → suspensory ligaments become taut → lens becomes flatter', False),
                     ('Ciliary muscles relax → suspensory ligaments slacken → lens becomes more rounded', False)],
            'q': 'A student looks from a distant window to a book close to them. What happens to the ciliary muscles '
                 'and lens?',
            'wrong_explanations': {1: 'Relaxing ciliary muscles = FAR vision (flat lens). For NEAR vision, ciliary '
                                      'muscles must CONTRACT.',
                                   2: 'When ciliary muscles contract, ligaments SLACKEN (not become taut). The lens '
                                      'rounds up because tension is removed.',
                                   3: 'Relaxing ciliary muscles causes ligaments to become taut — but the lens becomes '
                                      'FLAT, not rounded.'}},
           {'opts': [('To reduce the amount of light entering the eye — preventing damage to the sensitive retina',
                      True),
                     ('To increase the amount of light entering — bright light improves vision', False),
                     ('To improve colour vision — cones work better with a smaller pupil', False),
                     ('The lens expands when bright and blocks more of the pupil', False)],
            'q': 'Why do the pupils constrict in bright light?',
            'wrong_explanations': {1: 'Constriction REDUCES light entry — pupils dilate to INCREASE light entry in dim '
                                      'conditions.',
                                   2: 'Cones work well in bright light regardless of pupil size — the pupil reflex is '
                                      'about PROTECTING the retina from excessive light.',
                                   3: "The lens doesn't change size or block the pupil — accommodation changes lens "
                                      'shape, not size.'}}],
  'rp': None,
  'spec': '4.5.2.5',
  'summary': 'Describe the structure of the eye and the function of each part.',
  'theory': [{'content': 'The eye is a sense organ — it detects light stimuli and converts them into electrical '
                         'impulses sent to the brain via the optic nerve.\n'
                         '\n'
                         'Key structures:\n'
                         '\n'
                         'CORNEA — transparent, curved front surface. Refracts (bends) light — does most of the '
                         'focusing (about 70% of total refraction).\n'
                         '\n'
                         'IRIS — the coloured ring of muscle around the pupil. Controls the size of the PUPIL to '
                         'regulate how much light enters.\n'
                         '\n'
                         'PUPIL — the hole in the centre of the iris. Not a structure itself — just the opening. Lets '
                         'light into the eye.\n'
                         '\n'
                         'LENS — a flexible, transparent disc behind the iris. Fine-tunes focusing by changing shape '
                         '(ACCOMMODATION). Held in place by suspensory ligaments attached to the ciliary body.\n'
                         '\n'
                         'CILIARY MUSCLE — ring of muscle surrounding the lens. Contracts or relaxes to change the '
                         'tension on the lens via the suspensory ligaments, altering the lens shape and focal length.\n'
                         '\n'
                         'SUSPENSORY LIGAMENTS — fibres connecting the lens to the ciliary muscle. When ciliary muscle '
                         'contracts → ligaments loosen → lens becomes more rounded (for near vision).\n'
                         '\n'
                         'RETINA — the light-sensitive layer at the back of the eye. Contains two types of '
                         'photoreceptor cells: RODS (sensitive to light intensity — monochrome, dim conditions) and '
                         'CONES (sensitive to colour — need bright light, concentrated in the fovea).\n'
                         '\n'
                         'FOVEA (yellow spot) — area of highest cone density on the retina — sharpest colour vision.\n'
                         '\n'
                         'OPTIC NERVE — carries electrical impulses from the retina to the brain for processing.\n'
                         '\n'
                         'BLIND SPOT — where the optic nerve exits — no photoreceptors here, so no vision in this '
                         'area.',
              'heading': 'Structure of the Eye'},
             {'content': 'ACCOMMODATION is the process by which the lens changes shape to focus on objects at '
                         'different distances.\n'
                         '\n'
                         'FOCUSING ON A NEAR OBJECT:\n'
                         'Ciliary muscles CONTRACT.\n'
                         'Suspensory ligaments SLACKEN (less tension on lens).\n'
                         'Lens becomes more ROUNDED (more curved, fatter).\n'
                         'More refraction → shorter focal length → image focused on retina.\n'
                         '\n'
                         'FOCUSING ON A DISTANT OBJECT:\n'
                         'Ciliary muscles RELAX.\n'
                         'Suspensory ligaments become TAUT (pull on lens).\n'
                         'Lens becomes FLATTER (less curved, thinner).\n'
                         'Less refraction → longer focal length → image focused on retina.\n'
                         '\n'
                         'MEMORY AID:\n'
                         'Near = ciliary contracts, lens round.\n'
                         'Far = ciliary relaxes, lens flat.\n'
                         '\n'
                         'THE PUPIL REFLEX (controlling light entry):\n'
                         'BRIGHT LIGHT → circular muscles of iris CONTRACT → pupil CONSTRICTS (gets smaller) → less '
                         'light enters → prevents damage to retina.\n'
                         'DIM LIGHT → radial muscles of iris CONTRACT → pupil DILATES (gets larger) → more light '
                         'enters → improves vision in low light.',
              'heading': 'How the Eye Focuses — Accommodation'}],
  'title': 'The Eye',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Short-sight is corrected by a CONCAVE lens (diverging). Long-sight is corrected by a CONVEX lens '
                    '(converging). Students often get these the wrong way round. Memory tip: Short-sight = Concave = '
                    'diverging (spreads light out, moves focal point back). Long-sight = convex = converging (brings '
                    'light together, moves focal point forward).',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'defects-of-the-eye',
  'key_note': 'Short-sight (myopia): eyeball too long, image in front of retina → correct with CONCAVE lens. '
              'Long-sight (hyperopia): eyeball too short, image behind retina → correct with CONVEX lens. Laser '
              'surgery reshapes cornea permanently.',
  'matching': {'instruction': 'Match each feature to short-sight or long-sight.',
               'pairs': [('Short-sight', 'Cannot see distant objects clearly — eyeball too long or lens too curved'),
                         ('Long-sight', 'Cannot see near objects clearly — eyeball too short or lens too flat'),
                         ('Short-sight', 'Corrected with a concave (diverging) lens'),
                         ('Long-sight', 'Corrected with a convex (converging) lens'),
                         ('Short-sight', 'Image forms in front of the retina'),
                         ('Long-sight', 'Image would form behind the retina')],
               'title': 'Short-sight or Long-sight?'},
  'quiz': [{'opts': [('Short-sight (myopia) — corrected with concave (diverging) lenses', True),
                     ('Long-sight (hyperopia) — corrected with convex (converging) lenses', False),
                     ('Short-sight (myopia) — corrected with convex (converging) lenses', False),
                     ('Long-sight (hyperopia) — corrected with concave (diverging) lenses', False)],
            'q': 'A student cannot see the board clearly but can read their textbook easily. What is the most likely '
                 'condition and correction?',
            'wrong_explanations': {1: 'Cannot see far (board) but CAN see near (textbook) = LONG-SIGHT. Long-sight is '
                                      'corrected with CONVEX lenses.',
                                   2: 'Cannot see far but CAN see near = SHORT-SIGHT. Concave lenses correct '
                                      'short-sight, not convex.',
                                   3: 'Long-sight cannot see near objects and CAN see distant objects more easily. If '
                                      "near vision is fine, it's short-sight."}},
           {'opts': [('The laser flattens the cornea — reducing its curvature and refractive power, moving the focal '
                      'point back onto the retina',
                      True),
                     ('The laser makes the cornea more curved — increasing refraction and moving the focal point '
                      'forward',
                      False),
                     ('The laser reshapes the lens — making it flatter to reduce refraction', False),
                     ('The laser shortens the eyeball — bringing the retina closer to the focal point', False)],
            'q': 'How does laser eye surgery correct short-sight?',
            'wrong_explanations': {1: 'Making the cornea MORE curved = correcting LONG-SIGHT (needs more refraction). '
                                      'Short-sight needs LESS refraction = FLATTER cornea.',
                                   2: 'Laser surgery operates on the CORNEA — not the lens. The lens is not reshaped '
                                      'by laser treatment.',
                                   3: 'Laser surgery cannot change the physical length of the eyeball — it only '
                                      "reshapes the cornea's surface curvature."}}],
  'rp': None,
  'spec': '4.5.2.6',
  'summary': 'Describe the causes of long-sight and short-sight and how they are corrected.',
  'theory': [{'content': 'SHORT-SIGHT (MYOPIA) means being unable to see distant objects clearly — they appear '
                         'blurred.\n'
                         '\n'
                         'CAUSE:\n'
                         'The eyeball is too LONG (front to back), OR the lens is too curved (too powerful).\n'
                         'Light from distant objects is brought to a focus IN FRONT OF the retina — not on it.\n'
                         'The image on the retina is therefore blurred.\n'
                         'Close objects can still be seen clearly — the lens can round up enough to focus them.\n'
                         '\n'
                         'CORRECTION:\n'
                         'CONCAVE (diverging) LENS — diverges the light rays before they enter the eye.\n'
                         'This moves the focal point backwards — onto the retina.\n'
                         'Concave lenses have a negative power value.\n'
                         'Can also be corrected by: laser eye surgery (reshaping the cornea to reduce its curvature).\n'
                         '\n'
                         'PREVALENCE: short-sight has become more common globally — particularly in young people. '
                         'Thought to be linked to increased close-up work (screens, reading) and less time outdoors.',
              'heading': 'Short-Sightedness (Myopia)'},
             {'content': 'LONG-SIGHT (HYPEROPIA) means being unable to see near objects clearly — they appear '
                         'blurred.\n'
                         '\n'
                         'CAUSE:\n'
                         'The eyeball is too SHORT (front to back), OR the lens is too flat (not powerful enough).\n'
                         'Light from nearby objects would be brought to a focus BEHIND the retina — but the retina '
                         'intercepts the rays before they converge.\n'
                         'The image on the retina is blurred.\n'
                         'Distant objects may be seen more clearly as they require less refraction.\n'
                         '\n'
                         'CORRECTION:\n'
                         'CONVEX (converging) LENS — converges the light rays before they enter the eye.\n'
                         'This moves the focal point forward — onto the retina.\n'
                         'Convex lenses have a positive power value.\n'
                         'Can also be corrected by: laser eye surgery (reshaping the cornea to increase curvature).\n'
                         '\n'
                         'AGE-RELATED LONG-SIGHT (PRESBYOPIA):\n'
                         'As people age, the lens becomes less flexible → cannot round up as much → difficulty '
                         'focusing on near objects.\n'
                         'This is why many people need reading glasses after the age of 40–50.',
              'heading': 'Long-Sightedness (Hyperopia)'},
             {'content': 'SPECTACLES (GLASSES):\n'
                         'Safest option — no surgery involved.\n'
                         'Easily updated as prescription changes.\n'
                         'Convex lenses for long-sight; concave lenses for short-sight.\n'
                         '\n'
                         'CONTACT LENSES:\n'
                         'Sit directly on the cornea.\n'
                         'Invisible when worn — cosmetic advantage.\n'
                         'Risk of infection if not handled hygienically.\n'
                         'Same lens types as glasses (concave or convex).\n'
                         '\n'
                         'LASER EYE SURGERY:\n'
                         'Uses a laser to reshape the CORNEA — permanently altering its curvature.\n'
                         'Short-sight: cornea flattened → less refraction → focal point moves back.\n'
                         'Long-sight: cornea made more curved → more refraction → focal point moves forward.\n'
                         'Permanent correction — no need for glasses or contacts afterwards.\n'
                         'Risks: dry eyes, glare, halos, rare complications. Only suitable for adults with stable '
                         'prescription.',
              'heading': 'Corrective Methods Compared'}],
  'title': 'Defects of the Eye',
  'triple_only': None,
  'variables': []}],

"inheritance": [{'common_mistake': 'MITOSIS produces IDENTICAL cells (used for growth and repair). MEIOSIS produces GAMETES with HALF '
                    'the chromosome number — and they are genetically different from each other. Students often '
                    'confuse these two. Remember: MEiosis → gamEtes. Mitosis → most body cells.',
  'equations': [],
  'fifas': [],
  'higher': 'Meiosis produces four haploid genetically different gametes from one diploid cell. Key events: homologous '
            'chromosomes pair and exchange segments (CROSSING OVER) in prophase I; homologous pairs separate in '
            'meiosis I; chromatids separate in meiosis II. Independent assortment (random orientation of chromosome '
            'pairs) and crossing over both increase genetic variation. The combination of meiosis and fertilisation '
            'produces enormous genetic diversity.',
  'id': 'sexual-asexual-reproduction',
  'key_note': 'Asexual: 1 parent, mitosis, clones, fast, no variation. Sexual: 2 parents, meiosis + fertilisation, '
              'variation, drives evolution. Meiosis halves chromosome number: 46 → 23. Fertilisation restores: 23 + 23 '
              '= 46.',
  'matching': {'instruction': 'Sort each feature into sexual or asexual reproduction.',
               'pairs': [('Asexual', 'Offspring are genetically identical clones of the parent — produced by mitosis'),
                         ('Sexual',
                          'Involves fusion of gametes — offspring are genetically different from both parents'),
                         ('Asexual', 'Only one parent needed — fast, energy efficient'),
                         ('Sexual', 'Creates genetic variation — allows populations to adapt and evolve'),
                         ('Sexual', 'Gametes produced by meiosis — chromosome number halved'),
                         ('Asexual', 'Strawberry plants reproducing via runners — all offspring identical')],
               'title': 'Sexual or Asexual Reproduction?'},
  'quiz': [{'opts': [('It creates genetic variation — offspring differ from parents, allowing adaptation to changing '
                      'environments',
                      True),
                     ('It is faster — more offspring are produced in less time', False),
                     ('Only one parent is needed — saving time and energy', False),
                     ('All offspring are perfectly adapted — no risk of poor survival', False)],
            'q': 'What is the main genetic advantage of sexual reproduction over asexual reproduction?',
            'wrong_explanations': {1: 'ASEXUAL reproduction is faster — producing large numbers of identical offspring '
                                      'quickly. Sexual reproduction is slower but creates variation.',
                                   2: 'Requiring only ONE parent = ASEXUAL reproduction. Sexual reproduction needs two '
                                      'parents.',
                                   3: 'It is ASEXUAL reproduction where all offspring are identical clones of a '
                                      'well-adapted parent. Sexual reproduction means offspring vary.'}},
           {'opts': [('So that when two gametes fuse at fertilisation, the offspring has the correct number (46) and '
                      'not double (92)',
                      True),
                     ('To create more genetic variation by reducing the number of genes', False),
                     ('Because cells with fewer chromosomes divide more easily', False),
                     ('Meiosis does not halve chromosome number — it doubles it', False)],
            'q': 'Why does meiosis halve the chromosome number?',
            'wrong_explanations': {1: 'Fewer chromosomes do allow more combinations, but the PRIMARY reason for '
                                      'halving is to prevent the chromosome number doubling each generation.',
                                   2: 'Cell division speed is not the biological reason — the function is specifically '
                                      'to allow fertilisation to restore the correct diploid number.',
                                   3: 'Meiosis HALVES chromosome number (46 → 23). Doubling occurs at fertilisation '
                                      'when two haploid gametes combine to make a diploid zygote.'}},
           {'opts': [('Asexual reproduction — one parent, offspring are genetically identical clones', True),
                     ('Sexual reproduction — two bacteria combine to share genetic material', False),
                     ('Meiosis — the chromosome number is halved in each new bacterium', False),
                     ('Fertilisation — two gametes fuse to form a new bacterium', False)],
            'q': 'Bacteria reproduce by binary fission — splitting into two identical cells. What type of reproduction '
                 'is this?',
            'wrong_explanations': {1: 'Some bacteria do exchange genetic material (conjugation) — but binary fission '
                                      'specifically produces identical copies from one parent. It is asexual.',
                                   2: 'Binary fission produces identical cells from ONE parent — it does not involve '
                                      'halving chromosome numbers. Bacteria are haploid anyway.',
                                   3: "Gametes are specialised sex cells — bacteria don't produce gametes in binary "
                                      'fission.'}}],
  'rp': None,
  'spec': '4.6.1',
  'summary': 'Compare sexual and asexual reproduction and explain the role of meiosis in sexual reproduction.',
  'theory': [{'content': 'ASEXUAL REPRODUCTION involves only ONE parent organism — no gametes (sex cells) are '
                         'involved.\n'
                         '\n'
                         'New offspring are produced by MITOSIS — cell division that creates genetically IDENTICAL '
                         'copies of the parent.\n'
                         '\n'
                         'Offspring from asexual reproduction are called CLONES — they are genetically identical to '
                         'the parent and to each other.\n'
                         '\n'
                         'ADVANTAGES:\n'
                         'Fast — large numbers of offspring can be produced very quickly.\n'
                         'No mate needed — energy efficient.\n'
                         'All offspring are well-adapted if the parent is well-adapted to its environment.\n'
                         "Useful in stable environments where the parent's traits are advantageous.\n"
                         '\n'
                         'DISADVANTAGES:\n'
                         'No genetic variation — all offspring identical.\n'
                         'If the environment changes or a new disease emerges, ALL offspring are equally vulnerable.\n'
                         'Cannot adapt to new conditions.\n'
                         '\n'
                         'EXAMPLES: Bacteria (binary fission), plants via runners (strawberries), bulbs (daffodils), '
                         'tubers (potatoes), budding (hydra), some fungi.',
              'heading': 'Asexual Reproduction'},
             {'content': 'SEXUAL REPRODUCTION involves TWO parent organisms — each contributes a GAMETE (sex cell).\n'
                         '\n'
                         'Gametes are produced by MEIOSIS — a special type of cell division that HALVES the chromosome '
                         'number.\n'
                         '\n'
                         'FERTILISATION: a male gamete and female gamete FUSE to form a ZYGOTE (fertilised egg), '
                         'restoring the full chromosome number.\n'
                         '\n'
                         'Because DNA from TWO different individuals is combined, offspring are genetically DIFFERENT '
                         'from both parents and from each other.\n'
                         '\n'
                         'ADVANTAGES:\n'
                         'Creates genetic VARIATION — offspring differ from parents and from each other.\n'
                         'Variation means some offspring may be better adapted if the environment changes.\n'
                         'Drives EVOLUTION — natural selection can act on the variation produced.\n'
                         '\n'
                         'DISADVANTAGES:\n'
                         'Requires two parents — time and energy needed to find a mate.\n'
                         'Slower — fewer offspring produced.\n'
                         'Some offspring may inherit unfavourable gene combinations.',
              'heading': 'Sexual Reproduction'},
             {'content': 'MEIOSIS is the type of cell division used to produce gametes (sperm, eggs, pollen).\n'
                         '\n'
                         'Starting cell: a body cell with 46 chromosomes (23 pairs).\n'
                         '\n'
                         'In meiosis:\n'
                         'The chromosome number is HALVED — each gamete receives 23 chromosomes (one from each pair).\n'
                         'FOUR daughter cells are produced.\n'
                         'Each daughter cell is GENETICALLY DIFFERENT from the others.\n'
                         '\n'
                         'WHY halve the chromosome number? When two gametes fuse at fertilisation, 23 + 23 = 46 — '
                         'restoring the correct number. If gametes had 46 chromosomes each, the offspring would have '
                         '92 — doubling every generation.\n'
                         '\n'
                         'Genetic variation in meiosis arises because:\n'
                         'Chromosomes are shuffled before dividing (independent assortment).\n'
                         'Sections of chromosomes can be exchanged between homologous pairs (crossing over).\n'
                         'This means every gamete has a unique combination of alleles.',
              'heading': 'Meiosis — Producing Gametes'}],
  'title': 'Sexual and Asexual Reproduction',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Meiosis produces FOUR cells, not two. Mitosis produces two. Meiosis produces genetically '
                    'DIFFERENT cells — not identical. The daughter cells are HAPLOID (half chromosome number). '
                    'Students often confuse meiosis with mitosis — remember: Meiosis = gametes, Mix up alleles, 4 '
                    'cells.',
  'equations': [],
  'fifas': [],
  'higher': 'Explain how crossing over (chiasmata) during prophase I exchanges segments of homologous chromosomes '
            'creating new allele combinations. Explain independent assortment — random orientation of homologous pairs '
            'at metaphase I. Calculate the number of possible gamete combinations from a given number of chromosome '
            'pairs (2ⁿ). Explain the significance of meiotic variation for natural selection and evolution.',
  'id': 'meiosis',
  'key_note': 'Meiosis: produces 4 haploid gametes (23 chromosomes in humans). Two divisions. Crossing over creates '
              'new allele combinations → genetic variation. Meiosis I: separates homologous pairs. Meiosis II: '
              'separates chromatids. Variation = essential for evolution.',
  'matching': {'instruction': 'Match each feature to meiosis, mitosis, or both.',
               'pairs': [('Meiosis only', 'Produces 4 daughter cells — all genetically different'),
                         ('Mitosis only', 'Produces 2 daughter cells — genetically identical to parent'),
                         ('Meiosis only', 'Daughter cells are haploid — half the chromosome number'),
                         ('Both', 'DNA replication occurs before division begins'),
                         ('Meiosis only',
                          'Crossing over between homologous chromosomes creates new allele combinations')],
               'title': 'Meiosis vs Mitosis'},
  'quiz': [{'opts': [('23 — meiosis halves the chromosome number so that fertilisation restores the full 46', True),
                     ('46 — gametes have the same chromosome number as body cells', False),
                     ('92 — gametes have double the chromosome number ready for fertilisation', False),
                     ('23 pairs — gametes have paired chromosomes just like body cells', False)],
            'q': 'How many chromosomes does a human gamete contain, and why?',
            'wrong_explanations': {1: 'If gametes had 46 chromosomes, fertilisation would produce 92 — doubling every '
                                      'generation. Meiosis halves the number to 23 so fertilisation gives 46.',
                                   2: 'Gametes have 23 SINGLE chromosomes — not 23 pairs. The pairs are only restored '
                                      'after fertilisation.',
                                   3: 'Gametes have unpaired chromosomes — 23 singles. Paired chromosomes (46 total) '
                                      'are in body cells, not gametes.'}},
           {'opts': [('Crossing over exchanges DNA between homologous chromosomes, and random separation of pairs '
                      'creates new allele combinations',
                      True),
                     ('Meiosis makes errors in DNA replication — these errors cause the variation', False),
                     ('Gametes are made in different organs — different environments cause different genes', False),
                     ('Each gamete gets a random selection of completely new genes, not inherited ones', False)],
            'q': 'Why does meiosis produce genetically varied gametes rather than identical ones?',
            'wrong_explanations': {1: 'Crossing over is a precise process, not an error — it deliberately exchanges '
                                      'segments between chromosomes.',
                                   2: 'Gametes are made in the same organ (gonads) — the variation comes from the '
                                      'process of meiosis, not the environment.',
                                   3: "Gametes inherit combinations of the parent's existing alleles — no new genes "
                                      'are created. New COMBINATIONS are produced.'}}],
  'rp': None,
  'spec': '4.6.1.2',
  'summary': 'Describe meiosis, explain how it produces genetically varied gametes and why variation is important.',
  'theory': [{'content': 'MEIOSIS is a type of cell division that produces GAMETES (sex cells — sperm and eggs in '
                         'animals; pollen and ovules in plants).\n'
                         '\n'
                         'Key features of meiosis:\n'
                         'Produces FOUR daughter cells (not two like mitosis).\n'
                         'Each daughter cell has HALF the chromosome number of the parent cell.\n'
                         'In humans: body cells have 46 chromosomes (23 pairs); gametes have 23 chromosomes (one from '
                         'each pair).\n'
                         'This is called the HAPLOID number (23) vs DIPLOID number (46).\n'
                         '\n'
                         'When two gametes fuse at fertilisation:\n'
                         'Sperm (23) + Egg (23) = Zygote (46) — full diploid number restored.\n'
                         'This ensures the chromosome number stays constant from generation to generation.',
              'heading': 'What Is Meiosis?'},
             {'content': 'MEIOSIS involves two divisions:\n'
                         '\n'
                         'FIRST DIVISION (Meiosis I):\n'
                         'Chromosomes replicate (as in mitosis).\n'
                         'Homologous pairs line up together.\n'
                         'Pairs are SEPARATED — one chromosome from each pair goes to each new cell.\n'
                         'Produces 2 cells, each with 23 chromosomes (but each is a double-stranded copy).\n'
                         '\n'
                         'SECOND DIVISION (Meiosis II):\n'
                         'The two cells divide again.\n'
                         'The double-stranded chromosomes split — one strand to each cell.\n'
                         'Produces 4 haploid cells, each with 23 single chromosomes.\n'
                         '\n'
                         'GENETIC VARIATION:\n'
                         'During Meiosis I, CROSSING OVER occurs — chromosomes exchange sections of DNA.\n'
                         'This creates new combinations of alleles — novel genetic variation.\n'
                         'Random SHUFFLING of which chromosome from each pair goes to each cell also creates '
                         'variation.\n'
                         'This is why siblings (same parents) are not genetically identical.',
              'heading': 'How Meiosis Works'},
             {'content': 'MEIOSIS vs MITOSIS — key differences:\n'
                         '\n'
                         'MITOSIS:\n'
                         'Produces 2 genetically IDENTICAL daughter cells.\n'
                         'Daughter cells are DIPLOID (same chromosome number as parent).\n'
                         'Used for growth, repair, asexual reproduction.\n'
                         '\n'
                         'MEIOSIS:\n'
                         'Produces 4 genetically DIFFERENT daughter cells.\n'
                         'Daughter cells are HAPLOID (half the chromosome number).\n'
                         'Used only for gamete production (in gonads — testes and ovaries in humans).\n'
                         '\n'
                         'IMPORTANCE OF MEIOSIS:\n'
                         'Ensures gametes have half the chromosome number — so fertilisation restores the full '
                         'number.\n'
                         'Creates genetic variation among offspring — important for evolution and adaptation.\n'
                         'Variation means populations can respond to changing environments.',
              'heading': 'Meiosis vs Mitosis'}],
  'title': 'Meiosis',
  'triple_only': 'Meiosis (4.6.1.2) is biology-only — not in Combined Science. Includes the detail of two meiotic '
                 'divisions, crossing over as a source of genetic variation, and the significance of producing haploid '
                 'gametes.',
  'variables': []},
 {'common_mistake': 'Asexual reproduction does NOT mean no variation ever — mutations can still occur. It means '
                    'offspring are genetically identical to the parent UNLESS mutation happens. Sexual reproduction '
                    'ALWAYS produces variation because of meiosis and fertilisation combining different alleles.',
  'equations': [],
  'fifas': [],
  'higher': 'Analyse case studies of organisms using both methods (fungi, aphids, strawberries) and evaluate the '
            'evolutionary advantage of each in specific environments. Explain how prolonged asexual reproduction can '
            'lead to accumulation of harmful mutations. Evaluate the genetic bottleneck risk in asexually reproducing '
            'populations facing new pathogens.',
  'id': 'advantages-sexual-asexual',
  'key_note': 'Sexual: two parents, gametes, variation, slower, drives evolution. Asexual: one parent, mitosis, '
              'clones, fast, no variation. Sexual advantages: variation, adaptability. Asexual advantages: speed, '
              'energy efficient. Many organisms use both. Variation = essential for evolution and disease resistance.',
  'matching': {'instruction': 'Sort each advantage into sexual or asexual reproduction.',
               'pairs': [('Sexual reproduction',
                          'Produces genetic variation — populations can adapt to changing environments'),
                         ('Asexual reproduction', 'Fast — one parent can rapidly produce many identical offspring'),
                         ('Sexual reproduction',
                          'Variation reduces risk of whole population being wiped out by disease'),
                         ('Asexual reproduction', 'No energy wasted finding a mate — all energy goes to reproduction'),
                         ('Sexual reproduction', 'Drives evolution through natural selection acting on variation')],
               'title': 'Sexual vs Asexual Advantages'},
  'quiz': [{'opts': [('Almost all bacteria die — they are genetically identical so equally susceptible, though any '
                      'rare mutant may survive',
                      True),
                     ('All bacteria survive — asexual reproduction makes them immune to antibiotics', False),
                     ('Half survive — asexual reproduction produces 50% resistant offspring automatically', False),
                     ('They immediately switch to sexual reproduction to create resistant variants', False)],
            'q': 'A population of bacteria reproduces asexually. A new antibiotic is introduced. What is most likely '
                 'to happen?',
            'wrong_explanations': {1: 'Asexual reproduction produces identical clones — no resistance to antibiotics, '
                                      'not immune. Resistance must arise through rare mutations.',
                                   2: 'Asexual reproduction produces genetically identical offspring — not 50% '
                                      'resistant. Variation only arises from mutations, not from the mode of '
                                      'reproduction.',
                                   3: 'Bacteria cannot switch reproductive strategies on demand — and even if they '
                                      "could, sexual reproduction wouldn't instantly produce resistant offspring."}},
           {'opts': [('Asexual gives fast colonisation in stable conditions; sexual creates variation for adaptation '
                      'to changing environments',
                      True),
                     ('Sexual is used in summer and asexual in winter — seasons determine the method', False),
                     ("Asexual reproduction is used when they can't find mates; sexual when mates are available",
                      False),
                     ('Both methods produce identical offspring — there is no benefit to using both', False)],
            'q': 'Why do many plants use both sexual and asexual reproduction?',
            'wrong_explanations': {1: 'While seasons can influence reproduction, the key advantage is about STABILITY '
                                      'vs CHANGE — not specifically seasons.',
                                   2: "Plants don't find mates — sexual reproduction in plants uses pollen carried by "
                                      'wind or insects, available regardless of season.',
                                   3: 'Sexual and asexual reproduction produce very different offspring — sexual gives '
                                      'variation, asexual gives clones. There is a clear benefit to each.'}}],
  'rp': None,
  'spec': '4.6.1.3',
  'summary': 'Compare sexual and asexual reproduction in terms of genetic variation, speed and energy cost.',
  'theory': [{'content': 'SEXUAL REPRODUCTION involves the fusion of two gametes (one from each parent) — '
                         'fertilisation.\n'
                         '\n'
                         'ADVANTAGES:\n'
                         'Produces GENETIC VARIATION in offspring — each individual is genetically unique.\n'
                         'Variation means populations can ADAPT to changing environments.\n'
                         'Variation reduces the risk of entire population being wiped out by a single disease '
                         '(genetically diverse population = harder to infect all).\n'
                         'Drives EVOLUTION through natural selection acting on variation.\n'
                         '\n'
                         'DISADVANTAGES:\n'
                         'Requires FINDING A MATE — costly in time and energy.\n'
                         "ONLY HALF the parent's genes are passed to each offspring (other half from mate).\n"
                         'SLOWER reproduction — fewer offspring produced per time period.\n'
                         'Some offspring may be poorly adapted (variation includes disadvantageous combinations).',
              'heading': 'Sexual Reproduction'},
             {'content': 'ASEXUAL REPRODUCTION involves only ONE parent — offspring are produced by mitosis.\n'
                         'All offspring are GENETICALLY IDENTICAL to the parent (clones).\n'
                         '\n'
                         'ADVANTAGES:\n'
                         'FAST — can reproduce rapidly when conditions are favourable.\n'
                         'No need to FIND A MATE — energy efficient.\n'
                         "All offspring inherit the parent's successful adaptations exactly.\n"
                         "100% of parent's genes passed on.\n"
                         'Useful when parent is well-adapted to stable environment.\n'
                         '\n'
                         'DISADVANTAGES:\n'
                         'NO GENETIC VARIATION — all offspring identical.\n'
                         'If conditions change or a new disease appears, ALL offspring equally vulnerable.\n'
                         'Cannot evolve rapidly through natural selection.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Asexual: bacteria (binary fission), strawberry runners, potato tubers, Hydra budding.\n'
                         'Sexual: most animals, flowering plants (using seeds).\n'
                         '\n'
                         'SOME ORGANISMS DO BOTH:\n'
                         'Fungi: reproduce asexually rapidly when conditions good; sexually when stressed → creates '
                         'variation.\n'
                         'Some plants: strawberries use runners (asexual) AND seeds (sexual).',
              'heading': 'Asexual Reproduction'},
             {'content': 'WHEN IS EACH ADVANTAGEOUS?\n'
                         '\n'
                         'ASEXUAL IS BETTER WHEN:\n'
                         'Environment is STABLE and parent is well-adapted.\n'
                         'Needing to COLONISE an area quickly — produce many offspring fast.\n'
                         'Example: bacteria in an ideal growth medium reproduce asexually every 20 minutes.\n'
                         '\n'
                         'SEXUAL IS BETTER WHEN:\n'
                         'Environment is CHANGING or UNPREDICTABLE.\n'
                         'A new disease threatens the population — variation means some may survive.\n'
                         'Long-term survival of the species matters more than rapid short-term reproduction.\n'
                         '\n'
                         'MANY ORGANISMS SWITCH:\n'
                         'Aphids: asexual in summer (fast colonisation of plants), sexual in autumn (variation for '
                         'winter survival).\n'
                         'Slime moulds: asexual when food plentiful, sexual when stressed.\n'
                         '\n'
                         'HUMAN APPLICATIONS:\n'
                         'Crop plants grown by asexual reproduction (cuttings, tissue culture) — all identical, high '
                         'yield.\n'
                         'But: genetically uniform crops more vulnerable to new diseases (Irish Potato Famine '
                         'example).',
              'heading': 'Comparing in Context'}],
  'title': 'Advantages and Disadvantages of Sexual and Asexual Reproduction',
  'triple_only': 'Comparison of advantages and disadvantages of sexual and asexual reproduction (4.6.1.3) is '
                 'biology-only. Includes the evolutionary significance of variation from sexual reproduction and the '
                 'speed advantages of asexual reproduction.',
  'variables': []},
 {'common_mistake': 'A GENE is not the same as a CHROMOSOME. A chromosome contains THOUSANDS of genes. The GENOME is '
                    'the COMPLETE set of ALL genetic information — all genes on all chromosomes. Base pairing: A pairs '
                    'with T only. C pairs with G only. Never A-G or C-T.',
  'equations': [],
  'fifas': [],
  'higher': 'Each codon (triplet of DNA bases) codes for one amino acid. The genetic code is universal (almost all '
            'organisms use the same codons) — strong evidence for common ancestry. Non-coding DNA (formerly called '
            "'junk DNA') includes regulatory sequences and sequences that code for non-protein RNA. The Human Genome "
            'Project identified ~20,000 protein-coding genes out of ~3 billion base pairs — most DNA is non-coding.',
  'id': 'dna-genome',
  'key_note': 'DNA = double helix. A-T and C-G base pairs. Gene = section of DNA coding for a protein. Chromosome = '
              'contains thousands of genes. Genome = complete genetic information of an organism. Human genome: '
              '~20,000 genes, ~3 billion base pairs.',
  'matching': {'instruction': 'Match each term to its correct definition.',
               'pairs': [('Nucleotide', 'The monomer unit of DNA — contains a sugar, phosphate and one base'),
                         ('Gene', 'A specific sequence of DNA bases that codes for a particular protein'),
                         ('Chromosome', 'A long coiled DNA molecule — contains thousands of genes'),
                         ('Allele', 'A different version of the same gene — slightly different base sequence'),
                         ('Genome', 'The complete set of genetic information in an organism'),
                         ('Base pairing', 'A always pairs with T; C always pairs with G — holds DNA strands together')],
               'title': 'DNA and Genome Vocabulary'},
  'quiz': [{'opts': [('A with T, and C with G', True),
                     ('A with G, and C with T', False),
                     ('A with C, and G with T', False),
                     ('All four bases pair randomly', False)],
            'q': 'In DNA, which bases pair together?',
            'wrong_explanations': {1: 'Wrong pairing — A pairs with T (2 hydrogen bonds) and C pairs with G (3 '
                                      'hydrogen bonds). A-G pairings do not occur.',
                                   2: 'Wrong pairing — A-C and G-T pairings do not occur in DNA. Base pairing is '
                                      'strictly A-T and C-G.',
                                   3: 'Base pairing in DNA is NOT random — it is strictly determined by molecular '
                                      'structure. A-T and C-G only.'}},
           {'opts': [('A specific sequence of DNA bases that codes for a particular protein', True),
                     ('A complete chromosome containing all the genetic information', False),
                     ('A unit of heredity that controls physical appearance only', False),
                     ('Any section of DNA — all DNA constitutes genes', False)],
            'q': 'What is a gene?',
            'wrong_explanations': {1: 'A complete chromosome contains thousands of genes — it is not itself a gene.',
                                   2: 'Genes code for proteins, which then influence characteristics — but genes '
                                      'control far more than physical appearance (e.g. enzyme production, cell '
                                      'signalling).',
                                   3: 'Not all DNA codes for proteins — a significant portion of the genome is '
                                      'non-coding DNA. Genes are specifically the protein-coding sequences.'}},
           {'opts': [('An international project that sequenced all ~3 billion base pairs of human DNA and mapped all '
                      'human genes',
                      True),
                     ('A project to create genetically modified humans with improved characteristics', False),
                     ('A database of all known genetic diseases and their cures', False),
                     ('A study comparing the DNA of humans to chimpanzees', False)],
            'q': 'What was the Human Genome Project?',
            'wrong_explanations': {1: 'The Human Genome Project was about SEQUENCING and MAPPING the genome — not '
                                      'about genetically modifying humans.',
                                   2: 'While comparisons with other species were made using genome data, the primary '
                                      'goal was mapping and sequencing the HUMAN genome itself.',
                                   3: 'While the HGP has helped identify disease genes, it was a mapping and '
                                      'sequencing project — not a medical treatment database.'}}],
  'rp': None,
  'spec': '4.6.2',
  'summary': 'Describe the structure of DNA, what genes are, and what the human genome project achieved.',
  'theory': [{'content': 'DNA (Deoxyribonucleic Acid) is the molecule that carries genetic information in all living '
                         'organisms.\n'
                         '\n'
                         'DNA is a POLYMER made of repeating units called NUCLEOTIDES.\n'
                         '\n'
                         'Each nucleotide contains:\n'
                         'A deoxyribose SUGAR.\n'
                         'A PHOSPHATE group.\n'
                         'One of four BASES: Adenine (A), Thymine (T), Cytosine (C) or Guanine (G).\n'
                         '\n'
                         'Two strands of nucleotides wind around each other to form the famous DOUBLE HELIX — like a '
                         'twisted ladder.\n'
                         '\n'
                         'The strands are held together by hydrogen bonds between complementary BASE PAIRS:\n'
                         'A always pairs with T (adenine — thymine).\n'
                         'C always pairs with G (cytosine — guanine).\n'
                         '\n'
                         'This base pairing rule (A-T, C-G) is fundamental — it allows DNA to be replicated accurately '
                         'before cell division.',
              'heading': 'DNA Structure'},
             {'content': 'A GENE is a specific sequence of DNA bases that codes for the production of a specific '
                         'PROTEIN.\n'
                         '\n'
                         'The sequence of bases in a gene determines the sequence of AMINO ACIDS in a protein — '
                         'different base sequences produce different proteins with different functions.\n'
                         '\n'
                         'Genes are located on CHROMOSOMES — long, tightly coiled DNA molecules.\n'
                         '\n'
                         'Humans have 46 chromosomes arranged as 23 PAIRS. One chromosome in each pair came from the '
                         'mother; one from the father.\n'
                         '\n'
                         'Each chromosome contains thousands of genes — there are approximately 20,000–25,000 '
                         'protein-coding genes in the human genome.\n'
                         '\n'
                         'ALLELES are different versions of the same gene, caused by slightly different base sequences '
                         'at the same position on homologous chromosomes.',
              'heading': 'Genes and Chromosomes'},
             {'content': 'The GENOME is the complete set of genetic information in an organism — every gene in every '
                         'chromosome.\n'
                         '\n'
                         'The HUMAN GENOME PROJECT was an international scientific collaboration that:\n'
                         'Ran from 1990 to 2003.\n'
                         'Mapped and sequenced all approximately 3 BILLION base pairs of the human genome.\n'
                         'Identified the location and sequence of all human genes.\n'
                         '\n'
                         'Why it matters:\n'
                         'Identifying genes linked to INHERITED DISEASES — e.g. BRCA1/2 (breast cancer risk), cystic '
                         'fibrosis gene.\n'
                         "Developing PERSONALISED MEDICINE — treatments tailored to an individual's genetic make-up.\n"
                         'Understanding HUMAN EVOLUTION and our relationship to other species.\n'
                         'Forensic science — DNA profiling to identify individuals.\n'
                         'Understanding gene function in health and disease.',
              'heading': 'The Human Genome'}],
  'title': 'DNA and the Genome',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'A always pairs with T, and G always pairs with C — never A-G or T-C. This complementary base '
                    "pairing is fixed. Students often mix up which bases pair together — use the memory: 'Apples in "
                    "Trees, Cars in Garages' (A-T, C-G).",
  'equations': [],
  'fifas': [],
  'higher': 'Explain semi-conservative replication in detail: double helix unwinds, each strand acts as template, free '
            'nucleotides pair by complementary base pairing (A-T, G-C), joined by DNA polymerase. Describe how '
            'mutations (substitution, insertion, deletion) alter the base sequence and may change the amino acid '
            'sequence and therefore the structure and function of the protein produced.',
  'id': 'dna-structure',
  'key_note': 'DNA: double helix, two strands of nucleotides (sugar + phosphate + base). Bases: A-T, C-G '
              '(complementary pairing). Gene = sequence of bases coding for a protein. 3 bases = 1 codon = 1 amino '
              'acid. Protein synthesis: transcription (DNA→mRNA) then translation (mRNA→protein). Replication: '
              'semi-conservative, each strand acts as template.',
  'matching': {'instruction': 'Match each base to its complementary partner.',
               'pairs': [('Adenine (A)', 'Thymine (T) — always paired by two hydrogen bonds'),
                         ('Guanine (G)', 'Cytosine (C) — always paired by three hydrogen bonds'),
                         ('Template strand', 'Original DNA strand used as a blueprint during replication'),
                         ('Codon', 'Three consecutive bases that code for one amino acid')],
               'title': 'Complementary Base Pairs'},
  'quiz': [{'opts': [('TAGCAT — A pairs with T, T pairs with A, C pairs with G, G pairs with C, T pairs with A, A '
                      'pairs with T',
                      True),
                     ('ATCGTA — the complementary strand is identical to the original', False),
                     ('UAGCAU — RNA bases replace DNA bases on the complementary strand', False),
                     ('TACGAT — bases pair like-for-like: A with A, T with T', False)],
            'q': 'A section of DNA has the base sequence ATCGTA. What is the complementary strand sequence?',
            'wrong_explanations': {1: 'The complementary strand is NOT identical — A pairs with T and G pairs with C, '
                                      'producing a different sequence.',
                                   2: 'U (uracil) replaces T in RNA — but this question asks about the complementary '
                                      'DNA strand, which uses T not U.',
                                   3: 'Bases pair with their COMPLEMENTS, not like-for-like: A pairs with T (not A), G '
                                      'pairs with C (not G).'}},
           {'opts': [('Semi-conservative replication — each original strand acts as a template and a new complementary '
                      'strand is built alongside it',
                      True),
                     ('Conservative replication — one cell gets both original strands, the other gets two new strands',
                      False),
                     ('The DNA is split randomly — sometimes two original, sometimes two new strands end up in one '
                      'cell',
                      False),
                     ('Only one strand is ever copied — the other strand stays as original in both cells', False)],
            'q': 'During DNA replication, why does each daughter cell end up with one original and one new DNA strand?',
            'wrong_explanations': {1: 'Conservative replication (one cell gets both originals) was one proposed model '
                                      '— but experiments showed semi-conservative replication is what actually '
                                      'happens.',
                                   2: 'DNA replication is NOT random — it is a precise, controlled process producing '
                                      'two identical double helices, each with one original strand.',
                                   3: 'Both strands are copied — each serves as a template for a new complementary '
                                      'strand.'}}],
  'rp': None,
  'spec': '4.6.2.1',
  'summary': 'Describe the structure of DNA including the double helix, bases, and the complementary base pairing '
             'rule.',
  'theory': [{'content': 'DNA (deoxyribonucleic acid) is the molecule that carries genetic information in all living '
                         'organisms.\n'
                         '\n'
                         'DNA has a DOUBLE HELIX structure — two strands twisted around each other like a twisted '
                         'ladder.\n'
                         '\n'
                         'Each strand is made of NUCLEOTIDES. Each nucleotide contains:\n'
                         '1. A SUGAR molecule (deoxyribose)\n'
                         '2. A PHOSPHATE group\n'
                         '3. One of four BASES: Adenine (A), Thymine (T), Guanine (G), Cytosine (C)\n'
                         '\n'
                         'The two strands are held together by WEAK HYDROGEN BONDS between the bases.\n'
                         '\n'
                         'COMPLEMENTARY BASE PAIRING:\n'
                         'Bases always pair in the same way:\n'
                         'A pairs with T (Adenine with Thymine)\n'
                         'G pairs with C (Guanine with Cytosine)\n'
                         '\n'
                         "This means if you know one strand's sequence, you can work out the other strand.\n"
                         'This complementary pairing is essential for accurate DNA replication.',
              'heading': 'The Structure of DNA'},
             {'content': 'A GENE is a sequence of bases on a DNA molecule that codes for a specific protein.\n'
                         '\n'
                         'The base sequence acts as a CODE — it determines the sequence of amino acids that make up a '
                         'protein.\n'
                         'Each group of three bases (a CODON) codes for a specific amino acid.\n'
                         "The order of amino acids determines the protein's shape → which determines its function.\n"
                         '\n'
                         'With 4 bases and 3-base codons: 4³ = 64 possible codons — more than enough for 20 amino '
                         'acids.\n'
                         '\n'
                         'NON-CODING DNA:\n'
                         'Large sections of DNA between genes do not code for proteins.\n'
                         'Some non-coding DNA regulates when genes are switched on or off.\n'
                         '\n'
                         'PROTEIN SYNTHESIS:\n'
                         'Genes are first TRANSCRIBED to make mRNA (messenger RNA).\n'
                         'mRNA travels out of the nucleus to ribosomes.\n'
                         'At ribosomes, the mRNA is TRANSLATED — amino acids are assembled in the correct sequence.\n'
                         'The chain of amino acids folds into a specific protein shape.',
              'heading': 'Genes and the Genetic Code'},
             {'content': 'Before cell division, DNA must be REPLICATED (copied) so each daughter cell gets a full '
                         'set.\n'
                         '\n'
                         'SEMI-CONSERVATIVE REPLICATION:\n'
                         '1. The double helix UNWINDS and the two strands SEPARATE (hydrogen bonds break).\n'
                         '2. Each original strand acts as a TEMPLATE.\n'
                         '3. FREE NUCLEOTIDES from the nucleus pair up with complementary bases on each template '
                         'strand.\n'
                         '4. New hydrogen bonds form between paired bases.\n'
                         '5. Two new identical double helices are formed — each with one original strand + one new '
                         'strand.\n'
                         '\n'
                         'Why semi-conservative?\n'
                         'Each new DNA molecule keeps ONE original strand and one newly made strand.\n'
                         "'Semi' = half original.\n"
                         '\n'
                         'This process is highly accurate but errors (mutations) can occasionally occur.\n'
                         'MUTATIONS: changes in the base sequence → may alter the protein produced → may affect the '
                         'organism.',
              'heading': 'DNA Replication'}],
  'title': 'DNA Structure',
  'triple_only': 'DNA structure detail (4.6.2.1) is biology-only — Combined Science covers DNA and the genome more '
                 'broadly without the structural detail of the double helix, nucleotides, base pairing or the '
                 'mechanism of DNA replication.',
  'variables': []},
 {'common_mistake': 'A CARRIER (Bb) has the recessive allele but does NOT show the condition — they appear completely '
                    "normal. Students often say carriers 'have the disease mildly' — this is WRONG. A carrier is "
                    'phenotypically normal but genotypically heterozygous. Two carriers (Bb × Bb) have a 25% chance of '
                    'an affected (bb) child.',
  'equations': [],
  'fifas': [{'label': 'Punnett Square — Heterozygous Cross',
             'question': 'Two parents are both heterozygous for brown eyes (Bb). Brown (B) is dominant over blue (b). '
                         'Calculate the probability of a child having blue eyes.',
             'steps': [('F', 'Draw a Punnett square: Bb × Bb'),
                       ('I', 'Offspring: BB, Bb, Bb, bb → genotype ratio 1:2:1'),
                       ('F', 'Only bb gives blue eyes (recessive phenotype) = 1 out of 4'),
                       ('A', 'Probability of blue eyes = 1/4 = 25%')]}],
  'higher': 'Codominance: both alleles expressed in the phenotype. Example: blood groups — IA and IB are codominant; '
            'IO is recessive. Blood group AB genotype = IAIB (both A and B antigens expressed). Students should be '
            'able to construct Punnett squares for crosses involving codominant alleles and predict the phenotype '
            'ratios for codominant inheritance.',
  'id': 'genetic-inheritance',
  'key_note': 'Dominant (capital) = expressed with one copy. Recessive (lowercase) = needs two copies. Genotype = '
              'alleles present. Phenotype = observable trait. Homozygous = both same. Heterozygous = different. '
              'Carrier = Bb, appears normal.',
  'matching': {'instruction': 'Match each genetics term to its correct definition.',
               'pairs': [('Genotype', 'The alleles present in an organism — e.g. Bb'),
                         ('Phenotype', 'The observable characteristic — e.g. brown eyes'),
                         ('Homozygous', 'Both alleles are the same — e.g. BB or bb'),
                         ('Heterozygous', 'Alleles are different — e.g. Bb'),
                         ('Dominant allele', 'Expressed in the phenotype even if only one copy is present'),
                         ('Carrier',
                          'Heterozygous individual with one recessive allele — appears normal but can pass it on')],
               'title': 'Genetics Vocabulary'},
  'quiz': [{'opts': [('1/4 (25%)', True),
                     ('1/2 (50%)', False),
                     ('3/4 (75%)', False),
                     ('0 — recessive cannot appear from two heterozygous parents', False)],
            'q': 'In a Bb × Bb cross, what fraction of offspring will show the RECESSIVE phenotype?',
            'wrong_explanations': {1: '50% occurs when one parent is homozygous recessive (bb × Bb). Two heterozygotes '
                                      'give 1 BB : 2 Bb : 1 bb → 25% recessive.',
                                   2: '3/4 is the proportion showing the DOMINANT phenotype (BB and Bb). Only 25% (bb) '
                                      'show recessive.',
                                   3: 'Two heterozygous parents (Bb × Bb) absolutely CAN produce a recessive child — '
                                      '25% chance (bb).'}},
           {'opts': [('They have one recessive allele (Ff) — they appear healthy but can pass the allele to offspring',
                      True),
                     ('They have the disease mildly — they have some symptoms but not severe ones', False),
                     ('They are homozygous recessive (ff) — they have the full condition', False),
                     ('They have been exposed to cystic fibrosis but their immune system fought it off', False)],
            'q': "A person is described as a 'carrier' of cystic fibrosis. What does this mean?",
            'wrong_explanations': {1: 'A carrier appears COMPLETELY NORMAL — there are no mild symptoms. Having one '
                                      'recessive allele (Ff) is masked by the dominant allele.',
                                   2: 'Homozygous recessive (ff) = HAS the condition. A carrier is HETEROZYGOUS (Ff) '
                                      'and does NOT have the condition.',
                                   3: 'Cystic fibrosis is a GENETIC condition — it is not an infection that can be '
                                      "'fought off' by the immune system."}},
           {'opts': [('Each pregnancy independently has a 25% chance of being affected — it does not mean exactly 1 in '
                      '4 children will be affected',
                      True),
                     ('Exactly one child out of every four they have will be affected', False),
                     ('If their first three children are unaffected, the fourth will definitely be affected', False),
                     ('The chance reduces after each unaffected child — the probability changes', False)],
            'q': 'If a Punnett square shows a 1 in 4 chance of having an affected child, what does this mean for a '
                 'couple?',
            'wrong_explanations': {1: 'Probability is not a guarantee of exact outcomes — with only 4 children, you '
                                      'might have 0, 1, 2, 3 or even 4 affected children.',
                                   2: 'Each pregnancy is INDEPENDENT — the outcome of previous pregnancies does not '
                                      'affect future ones. This is like flipping a coin.',
                                   3: "Probability doesn't 'accumulate' — each pregnancy always has the same 25% "
                                      'chance regardless of previous outcomes.'}}],
  'rp': None,
  'spec': '4.6.3',
  'summary': 'Explain dominant and recessive inheritance and use Punnett squares to predict offspring ratios.',
  'theory': [{'content': 'Each individual has TWO copies of most genes — one on each chromosome of a homologous pair. '
                         'These copies may be the same allele or different alleles.\n'
                         '\n'
                         'DOMINANT allele:\n'
                         'Expressed in the phenotype (physical characteristic) even if ONLY ONE COPY is present.\n'
                         'Written as a CAPITAL letter (e.g. B for brown eyes).\n'
                         '\n'
                         'RECESSIVE allele:\n'
                         'Only expressed if TWO COPIES are present — hidden by dominant allele if only one copy '
                         'exists.\n'
                         'Written as a LOWERCASE letter (e.g. b for blue eyes).\n'
                         '\n'
                         'GENOTYPE — the alleles an organism has (e.g. BB, Bb, bb).\n'
                         'PHENOTYPE — the observable characteristic expressed (e.g. brown eyes, blue eyes).\n'
                         '\n'
                         'HOMOZYGOUS — both alleles are the same (BB or bb).\n'
                         'HETEROZYGOUS — alleles are different (Bb).\n'
                         '\n'
                         'CARRIER — an individual with one recessive allele that is not expressed (Bb). They appear '
                         'normal but can pass the recessive allele to offspring.',
              'heading': 'Alleles — Dominant and Recessive'},
             {'content': 'A PUNNETT SQUARE is a grid used to predict the probability of offspring genotypes and '
                         'phenotypes from a genetic cross.\n'
                         '\n'
                         'How to draw one:\n'
                         '1. Write the alleles of one parent across the top.\n'
                         '2. Write the alleles of the other parent down the side.\n'
                         '3. Fill in each box by combining the alleles from the row and column.\n'
                         '4. The boxes show all possible offspring genotypes.\n'
                         '\n'
                         'EXAMPLE — Heterozygous cross (Bb × Bb):\n'
                         '\n'
                         'Parents: Bb × Bb\n'
                         'Offspring genotypes: BB, Bb, Bb, bb\n'
                         'Ratio: 1 BB : 2 Bb : 1 bb\n'
                         'Phenotype ratio: 3 dominant (BB and Bb) : 1 recessive (bb)\n'
                         'So 75% show dominant phenotype, 25% show recessive phenotype.\n'
                         '\n'
                         'EXAMPLE — Carrier × Normal (Bb × BB):\n'
                         'Offspring: BB, BB, Bb, Bb\n'
                         'All offspring show dominant phenotype — but 50% are carriers (Bb).',
              'heading': 'Using Punnett Squares'},
             {'content': 'Punnett squares give us PROBABILITIES — the likelihood of each outcome, not a guarantee.\n'
                         '\n'
                         'If a cross gives a 1 in 4 (25%) chance of an affected offspring, this means:\n'
                         'Each pregnancy independently has a 25% chance.\n'
                         'It does NOT mean that exactly 1 in every 4 children will be affected.\n'
                         'Small sample sizes may not reflect the expected ratio.\n'
                         '\n'
                         'Probability can be expressed as:\n'
                         'A fraction: 1/4.\n'
                         'A percentage: 25%.\n'
                         'A ratio: 1 in 4.\n'
                         '\n'
                         'Genetic counsellors use Punnett squares to advise couples on the risk of inherited '
                         'conditions in their children.',
              'heading': 'Probability in Genetics'}],
  'title': 'Genetic Inheritance',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Cystic fibrosis is RECESSIVE — both parents can be unaffected carriers. Polydactyly is DOMINANT — '
                    'at least one parent will always be affected (unless it arose from a new mutation). Students often '
                    'apply these rules the wrong way round. Remember: recessive conditions can SKIP GENERATIONS (via '
                    'carriers). Dominant conditions CANNOT skip generations.',
  'equations': [],
  'fifas': [{'label': 'CF Inheritance Cross',
             'question': 'Two carriers for cystic fibrosis (Ff × Ff) are expecting a child. What is the probability '
                         'the child will have CF?',
             'steps': [('F', 'Draw Punnett square: Ff × Ff. CF allele = f (recessive). Normal = F'),
                       ('I', 'Offspring: FF, Ff, Ff, ff → ratio 1:2:1'),
                       ('F', 'Only ff has cystic fibrosis = 1 out of 4 boxes'),
                       ('A', 'Probability of CF = 1/4 = 25%')]}],
  'higher': 'Embryo screening (PGD — preimplantation genetic diagnosis): embryos from IVF can be tested for genetic '
            'conditions before implantation. Allows selection of unaffected embryos. Ethical issues: is this a '
            'slippery slope to designer babies? Does it devalue people with that condition? Genetic counselling helps '
            'families understand inheritance patterns and risks without being directive about choices.',
  'id': 'inherited-disorders',
  'key_note': 'CF: recessive (ff), thick mucus in lungs and gut, 1 in 25 carriers in UK. Polydactyly: dominant (Dd), '
              'extra digits, appears every generation. Recessive can skip generations. Dominant cannot (unless new '
              'mutation).',
  'matching': {'instruction': 'Match each feature to the correct inherited disorder.',
               'pairs': [('Cystic fibrosis',
                          'Caused by a recessive allele — both copies needed for the condition to show'),
                         ('Polydactyly', 'Caused by a dominant allele — only one copy needed to show the condition'),
                         ('Cystic fibrosis', 'Causes thick sticky mucus in lungs and digestive system'),
                         ('Polydactyly', 'Causes extra fingers or toes — not life-threatening'),
                         ('Cystic fibrosis', 'Can skip generations — carriers appear healthy'),
                         ('Polydactyly',
                          'Appears in every generation — an affected person always has at least one affected parent')],
               'title': 'Cystic Fibrosis or Polydactyly?'},
  'quiz': [{'opts': [('Both parents are carriers — genotype Ff — they have one copy of the recessive allele each',
                      True),
                     ('One parent must have cystic fibrosis but is hiding it', False),
                     ('The child developed CF through a random environmental mutation', False),
                     ('The parents must be closely related — CF only occurs in related families', False)],
            'q': 'Both parents appear healthy but have a child with cystic fibrosis. What must be true of the parents?',
            'wrong_explanations': {1: "CF is a genetic condition — you cannot 'hide' it. If a parent had CF (ff) they "
                                      'would have serious symptoms.',
                                   2: 'CF is caused by inheriting TWO recessive alleles — both alleles must come from '
                                      'parents. The parents must both be carriers (Ff).',
                                   3: 'While CF is more common in some populations, it is not caused by family '
                                      'relatedness — it requires two carriers regardless of family relationship.'}},
           {'opts': [('Polydactyly is dominant — one copy is enough to show it. CF is recessive — carriers (Ff) appear '
                      "normal and don't show it.",
                      True),
                     ('Polydactyly is caused by a different chromosome than cystic fibrosis', False),
                     ('Cystic fibrosis is more severe so the body suppresses it in some generations', False),
                     ('Polydactyly affects more people so it appears more often', False)],
            'q': 'Why does polydactyly appear in every generation, while cystic fibrosis can skip generations?',
            'wrong_explanations': {1: 'The chromosomal location of a gene is irrelevant to whether the condition skips '
                                      "generations — it's the dominant/recessive nature that matters.",
                                   2: "The body doesn't suppress genetic conditions — whether a condition shows "
                                      'depends entirely on genotype and allele dominance.',
                                   3: "Prevalence doesn't determine whether a condition skips generations — "
                                      'dominance/recessiveness does.'}}],
  'rp': None,
  'spec': '4.6.3.2',
  'summary': 'Describe cystic fibrosis and polydactyly as examples of inherited genetic disorders.',
  'theory': [{'content': "Cystic fibrosis (CF) is caused by a RECESSIVE allele — written as 'f' (faulty) while 'F' is "
                         'the normal allele.\n'
                         '\n'
                         'GENOTYPES:\n'
                         'FF — unaffected, not a carrier.\n'
                         'Ff — carrier — appears healthy but carries one copy of the faulty allele.\n'
                         'ff — affected — has cystic fibrosis.\n'
                         '\n'
                         'For a child to have CF, they must inherit TWO recessive alleles — one from each parent.\n'
                         'Two carriers (Ff × Ff) have a 25% chance of an affected child per pregnancy.\n'
                         '\n'
                         'EFFECTS OF CYSTIC FIBROSIS:\n'
                         'The faulty allele affects a protein that controls the movement of salt and water across cell '
                         'membranes.\n'
                         'This causes a build-up of THICK, STICKY MUCUS in:\n'
                         'The LUNGS — makes breathing difficult, blocks airways, traps bacteria → repeated chest '
                         'infections → lung damage.\n'
                         'The DIGESTIVE SYSTEM — blocks ducts from the pancreas → digestive enzymes cannot reach the '
                         'gut → poor absorption of nutrients.\n'
                         '\n'
                         'TREATMENT: physiotherapy to loosen mucus, antibiotics for infections, enzyme supplements '
                         'with food. No cure (though gene therapy is in development).\n'
                         '\n'
                         'CF is the most common serious inherited disorder in the UK — approximately 1 in 25 people '
                         'carry the allele.',
              'heading': 'Cystic Fibrosis'},
             {'content': "Polydactyly is caused by a DOMINANT allele — written as 'D' while 'd' is the normal allele.\n"
                         '\n'
                         'GENOTYPES:\n'
                         'DD — affected (rare — very few people have two copies of the dominant allele).\n'
                         'Dd — affected — only ONE copy needed to show the condition.\n'
                         'dd — unaffected.\n'
                         '\n'
                         'A person with polydactyly has one or more EXTRA FINGERS OR TOES.\n'
                         '\n'
                         'Because the allele is DOMINANT:\n'
                         'Only ONE copy is needed — so an affected parent (Dd) has a 50% chance of passing the '
                         'condition to each child.\n'
                         'The condition appears in EVERY GENERATION that carries the allele.\n'
                         'An affected person has at least one affected parent (unless it arose from a new mutation).\n'
                         '\n'
                         'Polydactyly is not life-threatening and can be surgically corrected.\n'
                         '\n'
                         'KEY CONTRAST with cystic fibrosis:\n'
                         'CF = recessive — can skip generations (carriers appear normal).\n'
                         'Polydactyly = dominant — appears in every generation that carries it.',
              'heading': 'Polydactyly'},
             {'content': 'GENETIC TESTING can identify whether a person carries alleles for inherited conditions.\n'
                         '\n'
                         'Types of testing:\n'
                         'PRE-CONCEPTION testing — couples who have a family history of a genetic condition can be '
                         'tested to find out if they are carriers before having children.\n'
                         'PRE-NATAL testing — testing the embryo or foetus during pregnancy. Methods: amniocentesis '
                         '(sampling amniotic fluid), chorionic villus sampling (CVS — sampling placental tissue).\n'
                         'NEWBORN SCREENING — blood spot test (heel prick) shortly after birth screens for several '
                         'conditions including CF.\n'
                         '\n'
                         'ETHICAL CONSIDERATIONS:\n'
                         'Privacy — who has access to genetic information? Could affect insurance or employment.\n'
                         'Decision-making — if a foetus tests positive, should the pregnancy continue? Raises '
                         'difficult ethical questions.\n'
                         'Psychological impact — knowing you carry an allele for a serious condition causes anxiety.\n'
                         'Social stigma — discrimination against those known to have certain genetic profiles.\n'
                         'These are genuine ethical debates with no single correct answer — the key is to consider '
                         'multiple perspectives.',
              'heading': 'Genetic Testing and Ethical Issues'}],
  'title': 'Inherited Disorders',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'It is the SPERM that determines the sex of the child — not the egg. All eggs contain an X '
                    'chromosome. Sperm can contain either X or Y. If a Y-carrying sperm fertilises the egg, the child '
                    'is male (XY). Historically, women were sometimes blamed for not producing sons — this is '
                    'biologically incorrect.',
  'equations': [],
  'fifas': [],
  'higher': 'Sex-linked (X-linked) inheritance: genes on the X chromosome with no corresponding allele on the Y. Males '
            '(XY) have only one X — so any allele on their single X is expressed, even if recessive. This is why '
            'X-linked recessive conditions (colour blindness, haemophilia) are more common in males. Females can be '
            'carriers — one recessive allele masked by the dominant on the second X. Students should be able to '
            'construct and interpret Punnett squares for X-linked inheritance.',
  'id': 'sex-determination',
  'key_note': 'Female = XX. Male = XY. All eggs carry X. Sperm carry X or Y (50/50). Y-sperm → male (XY). X-sperm → '
              'female (XX). Sex determined at fertilisation by which sperm fertilises the egg. 50% probability each '
              'time.',
  'matching': {'instruction': 'Match each statement to the correct sex chromosome fact.',
               'pairs': [('Female', 'Has sex chromosomes XX — both are X chromosomes'),
                         ('Male', 'Has sex chromosomes XY — one X and one smaller Y chromosome'),
                         ('All eggs', 'Contain one X chromosome — females are XX so can only pass on X'),
                         ('Sperm', 'Contain either X or Y — determines the sex of the offspring'),
                         ('50%', 'Probability of a male offspring — same as probability of female offspring')],
               'title': 'Sex Determination Match'},
  'quiz': [{'opts': [('Which type of sperm (X or Y) fertilises the egg — Y-sperm → male, X-sperm → female', True),
                     ('The egg — females produce X and Y eggs, one type producing a boy and the other a girl', False),
                     ('The environment during pregnancy — temperature affects sex', False),
                     ('The age of the parents — older parents are more likely to have girls', False)],
            'q': 'What determines the biological sex of a human offspring?',
            'wrong_explanations': {1: 'Females (XX) can only produce X-bearing eggs — all eggs contain X. It is the '
                                      'SPERM that carries either X or Y.',
                                   2: 'Temperature does affect sex determination in some reptiles — but in humans, sex '
                                      'is determined genetically by which sperm fertilises the egg.',
                                   3: 'Parental age can affect fertility and some genetic risks — but does not '
                                      'determine sex.'}},
           {'opts': [('50% — each pregnancy is independent, the sex ratio is always 50:50', True),
                     ("Higher than 50% — after three girls they are 'due' a boy", False),
                     ('Lower than 50% — this couple clearly produce more girls than boys', False),
                     ('0% — if they have had three girls their sperm cannot produce Y chromosomes', False)],
            'q': 'A couple have three daughters. What is the probability their next child will be a son?',
            'wrong_explanations': {1: 'Each pregnancy is INDEPENDENT — like flipping a coin, the outcomes of previous '
                                      'pregnancies have no effect. This is a common misconception known as the '
                                      "gambler's fallacy.",
                                   2: 'Having three girls does not indicate a bias — small sample sizes often show '
                                      'runs of one outcome by chance. Males produce X and Y sperm equally.',
                                   3: 'Males always produce roughly 50% X-bearing and 50% Y-bearing sperm — three '
                                      "daughters doesn't change this."}}],
  'rp': None,
  'spec': '4.6.3.3',
  'summary': 'Explain how biological sex is determined by the X and Y chromosomes.',
  'theory': [{'content': 'In humans, biological sex is determined by a pair of SEX CHROMOSOMES — one of the 23 pairs '
                         'of chromosomes.\n'
                         '\n'
                         'FEMALES: XX — two X chromosomes.\n'
                         'MALES: XY — one X chromosome and one Y chromosome.\n'
                         '\n'
                         'The Y chromosome is smaller than the X chromosome and contains fewer genes. It carries the '
                         'genes responsible for male development, including the SRY gene which triggers the '
                         'development of testes.\n'
                         '\n'
                         'All other 22 chromosome pairs are called AUTOSOMES — they are the same in males and females.',
              'heading': 'Sex Chromosomes'},
             {'content': 'All eggs produced by a female contain ONE X chromosome (since females are XX).\n'
                         '\n'
                         'Sperm produced by a male contain EITHER:\n'
                         'an X chromosome (approximately 50% of sperm), OR\n'
                         'a Y chromosome (approximately 50% of sperm).\n'
                         '\n'
                         'At fertilisation:\n'
                         'If an X-bearing sperm fertilises the egg: XX → FEMALE.\n'
                         'If a Y-bearing sperm fertilises the egg: XY → MALE.\n'
                         '\n'
                         'Therefore: the SPERM determines the biological sex of the offspring — not the egg.\n'
                         '\n'
                         'Probability: 50% chance of a female child, 50% chance of a male child in each pregnancy.',
              'heading': 'How Sex is Determined at Fertilisation'},
             {'content': 'We can use a Punnett square to show sex determination:\n'
                         '\n'
                         'Mother (XX) × Father (XY)\n'
                         '\n'
                         'Sperm: X or Y (50/50)\n'
                         'Eggs: X only (100%)\n'
                         '\n'
                         'Offspring:\n'
                         'XX = female (50%)\n'
                         'XY = male (50%)\n'
                         '\n'
                         'This shows why the sex ratio in human populations is approximately 50:50.\n'
                         '\n'
                         'Key point: the sex of a child is determined RANDOMLY at fertilisation — it cannot be '
                         'predicted in advance for a specific pregnancy. The 50:50 ratio is the probability, not a '
                         'guarantee for any given family.',
              'heading': 'Punnett Square for Sex Determination'}],
  'title': 'Sex Determination',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Environmental variation is NOT inherited — you cannot pass your experiences, injuries or learned '
                    'skills to your children through DNA. Genetic variation IS inherited. Most mutations are neutral — '
                    'not harmful. Students often assume all mutations are dangerous, but the vast majority have no '
                    'detectable effect.',
  'equations': [],
  'fifas': [],
  'higher': 'Mutagens increase the frequency of mutations: UV radiation, ionising radiation (gamma rays, X-rays), '
            'certain chemicals (e.g. carcinogens in tobacco smoke). Most mutations are neutral (affect non-coding DNA '
            'or produce synonymous codons — same amino acid). The rare beneficial mutation is the raw material for '
            'natural selection and evolution. Students should understand that natural selection acts on existing '
            'variation — it cannot produce new alleles on demand.',
  'id': 'variation',
  'key_note': 'Variation: continuous (range of values) or discontinuous (distinct categories). Causes: genetic '
              '(mutation, meiosis, sexual reproduction), environmental (nutrition, sun, learned). Many traits = '
              'combination of both. Mutations: neutral, harmful or rarely beneficial.',
  'matching': {'instruction': 'Match each example to the cause of variation.',
               'pairs': [('Genetic', 'Blood group — determined entirely by inherited alleles'),
                         ('Environmental', 'A scar from a childhood accident — not passed to offspring'),
                         ('Both', 'Height — genes set the maximum potential; nutrition determines if it is reached'),
                         ('Environmental', 'Language spoken — entirely learned from the surrounding environment'),
                         ('Genetic', 'Cystic fibrosis — caused by inheriting two copies of the recessive allele'),
                         ('Both', 'Body weight — metabolic rate is genetic; diet and exercise are environmental')],
               'title': 'Genetic, Environmental or Both?'},
  'quiz': [{'opts': [('A combination of genetic potential and favourable environmental factors — e.g. excellent '
                      'nutrition during childhood',
                      True),
                     ('A mutation that occurred during development, making the child taller', False),
                     ('The child inherited more height genes from distant ancestors than from parents', False),
                     ('Environmental factors alone — height is entirely determined by diet', False)],
            'q': "A child is taller than expected given their parents' heights. What is the most likely cause?",
            'wrong_explanations': {1: 'A random mutation could theoretically increase height, but this is rare. The '
                                      "more likely explanation is that parents didn't reach their own genetic "
                                      'potential due to environmental factors.',
                                   2: "Genes don't skip generations in this simple way — the child can only inherit "
                                      'alleles from their parents.',
                                   3: 'Height is strongly influenced by genetics — children of tall parents tend to be '
                                      'taller. But environmental factors (particularly nutrition) also play a '
                                      'significant role.'}},
           {'opts': [('Blood group — a person is type A, B, AB or O with no intermediate values', True),
                     ('Height — people range from very short to very tall with all values in between', False),
                     ('Body weight — a continuous range from very light to very heavy', False),
                     ('Skin colour — a continuous range from very light to very dark', False)],
            'q': 'Which of the following is an example of DISCONTINUOUS variation?',
            'wrong_explanations': {1: 'Height is a classic example of CONTINUOUS variation — there is a smooth range '
                                      'from shortest to tallest with all intermediate heights present.',
                                   2: 'Body weight is CONTINUOUS — it forms a normal distribution curve across the '
                                      'population.',
                                   3: 'Skin colour is CONTINUOUS — determined by multiple genes and environmental '
                                      'factors (sun exposure), producing a smooth range of values.'}},
           {'opts': [('A change in the sequence of DNA bases — can be neutral, harmful or rarely beneficial', True),
                     ("A change in an organism's body caused by the environment during its lifetime", False),
                     ('The process of chromosomes being shuffled during meiosis', False),
                     ('A genetic disease inherited from parents', False)],
            'q': 'What is a mutation?',
            'wrong_explanations': {1: 'Environmental changes to the body (like a tan or muscle growth) are not '
                                      'mutations — they are phenotypic responses that are not passed on through DNA.',
                                   2: 'Chromosome shuffling during meiosis = INDEPENDENT ASSORTMENT and CROSSING OVER '
                                      '— these create variation but are not mutations.',
                                   3: 'Inherited diseases are caused by specific alleles — mutations can create new '
                                      'alleles, but the inherited disease itself is not a mutation.'}}],
  'rp': None,
  'spec': '4.6.4',
  'summary': 'Describe the causes of variation and distinguish between genetic, environmental and combination '
             'variation.',
  'theory': [{'content': 'VARIATION refers to the differences in characteristics between individuals of the same '
                         'species.\n'
                         '\n'
                         'Variation is absolutely essential for life on Earth:\n'
                         'It is the raw material on which NATURAL SELECTION acts.\n'
                         'Without variation, all individuals would be identical and no evolutionary change would be '
                         'possible.\n'
                         'Variation allows populations to adapt to changing environments.\n'
                         '\n'
                         'Variation can be:\n'
                         'CONTINUOUS — characteristics that show a range of values with no distinct categories (e.g. '
                         'height, weight, skin colour).\n'
                         'DISCONTINUOUS — characteristics that fall into distinct categories with no in-between values '
                         '(e.g. blood group A, B, AB or O; tongue rolling ability; ability to taste PTC).',
              'heading': 'What is Variation?'},
             {'content': 'Variation arises from three main sources:\n'
                         '\n'
                         '1. GENETIC VARIATION:\n'
                         'Differences in DNA sequences between individuals.\n'
                         'Arises through: MUTATIONS (random changes in DNA sequence), MEIOSIS (shuffling of '
                         'chromosomes and crossing over), SEXUAL REPRODUCTION (combining DNA from two parents).\n'
                         'Genetic variation is INHERITED — passed from parents to offspring.\n'
                         '\n'
                         '2. ENVIRONMENTAL VARIATION:\n'
                         'Differences caused by conditions an organism experiences during its lifetime.\n'
                         'Examples: height (affected by nutrition during childhood), skin colour (affected by sun '
                         'exposure), language spoken (learned from environment), scars and injuries.\n'
                         'Environmental variation is NOT inherited — you cannot pass on a learned language or a scar '
                         'to your offspring.\n'
                         '\n'
                         '3. COMBINATION OF BOTH:\n'
                         'Many characteristics are influenced by BOTH genes AND environment.\n'
                         'Examples: height (genes set the potential maximum; nutrition determines whether that '
                         'potential is reached), body weight (genes influence metabolism; diet and exercise are '
                         'environmental), skin colour (genes determine base colour; UV exposure adds a tan).',
              'heading': 'Causes of Variation'},
             {'content': 'A MUTATION is a change in the sequence of DNA bases in a gene or chromosome.\n'
                         '\n'
                         'Mutations can be:\n'
                         'Spontaneous — occurring randomly during DNA replication (copying errors).\n'
                         'Induced — caused by MUTAGENS: chemicals (e.g. carcinogens in tobacco smoke), radiation (UV, '
                         'gamma rays, X-rays), certain viruses.\n'
                         '\n'
                         'Effects of mutations:\n'
                         "Most mutations are NEUTRAL — they occur in non-coding DNA or don't change the protein "
                         'significantly.\n'
                         'Some mutations are HARMFUL — they alter a protein so it cannot function properly (e.g. '
                         'mutations causing cystic fibrosis, sickle cell disease).\n'
                         'Very occasionally, a mutation is BENEFICIAL — it improves the function of a protein or '
                         'produces a new useful function (e.g. mutations that gave early humans more efficient enzymes '
                         'or better immune responses).\n'
                         '\n'
                         'Beneficial mutations are the ultimate source of all new variation in a species — they are '
                         'the raw material on which natural selection acts.',
              'heading': 'Mutations'}],
  'title': 'Variation',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Natural selection does NOT cause mutations — mutations happen randomly. Natural selection SELECTS '
                    'from variation that already exists. Also: individuals do NOT evolve — POPULATIONS evolve over '
                    "many generations. And: 'survival of the fittest' does not mean 'strongest' — it means best "
                    'adapted to the environment.',
  'equations': [],
  'fifas': [],
  'higher': 'Speciation: geographic isolation divides a population → different selection pressures → allele '
            'frequencies diverge → accumulation of genetic differences → reproductive isolation → no longer able to '
            'interbreed → two species. Alfred Russel Wallace co-developed the theory of natural selection '
            'independently. Modern classification uses DNA sequence comparisons and evolutionary relationships '
            '(phylogenetics) rather than physical characteristics alone.',
  'id': 'evolution-natural-selection',
  'key_note': "Evolution = change in inherited characteristics over generations. Darwin's steps: variation → "
              'overproduction → struggle for survival → survival of the fittest → inheritance. Natural selection acts '
              'on existing variation — it does not cause mutations.',
  'matching': {'instruction': 'Match each step of natural selection to its correct description.',
               'pairs': [('Variation', 'Individuals in a population show differences in their characteristics'),
                         ('Overproduction', 'More offspring are produced than the environment can support'),
                         ('Struggle for survival', 'Competition for resources — not all offspring survive'),
                         ('Survival of the fittest',
                          'Individuals best adapted to the environment are more likely to survive and reproduce'),
                         ('Inheritance', 'Surviving individuals pass on advantageous alleles to offspring')],
               'title': 'Match the Step of Natural Selection'},
  'quiz': [{'opts': [('Natural selection — dark mice are better camouflaged, survive predation better and reproduce '
                      'more, passing on dark colour alleles',
                      True),
                     ('The mice deliberately changed colour to match their environment', False),
                     ('Dark soil contains minerals that cause mice to become darker', False),
                     ('Dark-coloured mice migrated from elsewhere and replaced the lighter mice', False)],
            'q': 'A population of mice lives on dark soil. Over many generations, the population becomes predominantly '
                 'dark-coloured. What explains this?',
            'wrong_explanations': {1: "Animals cannot deliberately change their genetic traits — they cannot 'choose' "
                                      'to become better adapted.',
                                   2: "Environmental exposure doesn't directly change DNA — this would be Lamarckian "
                                      'evolution, which has been disproved. Colour is a genetic trait, not caused by '
                                      'soil minerals.',
                                   3: 'While migration is possible, natural selection is the primary explanation — '
                                      'lighter mice are more visible to predators and are caught more often.'}},
           {'opts': [('It contradicted religious beliefs about creation, and Darwin lacked knowledge of the mechanism '
                      'of inheritance',
                      True),
                     ('It was based on observations from only one location and no experiments were done', False),
                     ('Darwin published it before collecting sufficient evidence, making it speculative', False),
                     ('The theory was too simple — scientists thought evolution must be more complicated', False)],
            'q': "Why was Darwin's theory of natural selection initially controversial?",
            'wrong_explanations': {1: 'Darwin travelled extensively (including the Galapagos, South America, '
                                      'Australia) and collected extensive evidence over many years.',
                                   2: 'Darwin actually delayed publication for over 20 years while gathering more '
                                      'evidence — he published when he felt the evidence was compelling.',
                                   3: 'The theory was considered TOO radical and COMPLICATED for many — particularly '
                                      'the idea of species changing over millions of years.'}},
           {'opts': [('Individuals best adapted to their environment are most likely to survive and reproduce — not '
                      'necessarily the strongest',
                      True),
                     ('The physically strongest and fastest individuals always survive', False),
                     ('Only the largest organisms in a population will reproduce', False),
                     ('Individuals that are most intelligent always out-compete others', False)],
            'q': "What does 'survival of the fittest' mean in evolution?",
            'wrong_explanations': {1: "Strength is one possible advantage in some environments — but 'fittest' "
                                      'specifically means best suited to the environment. A slow, toxic frog is '
                                      "'fitter' than a fast but tasty one in a predator-rich environment.",
                                   2: 'Size can be a disadvantage — larger organisms often need more food and may be '
                                      'more visible to predators.',
                                   3: 'Intelligence is advantageous in some contexts — but many highly successful '
                                      'organisms (bacteria, insects) have no intelligence.'}}],
  'rp': None,
  'spec': '4.6.5',
  'summary': "Describe Darwin's theory of evolution by natural selection and explain how populations change over time.",
  'theory': [{'content': 'EVOLUTION is the change in the inherited characteristics of a population over many '
                         'generations.\n'
                         '\n'
                         'It is driven by natural selection — the process by which individuals with characteristics '
                         'better suited to their environment are more likely to survive and reproduce.\n'
                         '\n'
                         'Evolution explains:\n'
                         'Why species change over time.\n'
                         'Why there are so many different species on Earth.\n'
                         'Why species share features with each other (common ancestry).\n'
                         'Why organisms are so well adapted to their environments.\n'
                         '\n'
                         'Evolution is the central organising principle of modern biology — it is one of the most '
                         'well-supported theories in all of science, supported by evidence from fossils, genetics, '
                         'anatomy and direct observation.',
              'heading': 'What is Evolution?'},
             {'content': 'Charles DARWIN (1809–1882) developed the theory of natural selection after extensive '
                         'observation of wildlife, particularly during his voyage on HMS Beagle (1831–1836).\n'
                         '\n'
                         "Darwin's theory in five steps:\n"
                         '1. VARIATION — individuals within a population show differences in their characteristics.\n'
                         '2. OVERPRODUCTION — populations produce more offspring than the environment can support.\n'
                         '3. STRUGGLE FOR SURVIVAL — competition for resources (food, water, mates, territory). Not '
                         'all offspring survive.\n'
                         '4. SURVIVAL OF THE FITTEST — individuals with characteristics best adapted to the '
                         'environment are more likely to SURVIVE and REPRODUCE.\n'
                         '5. INHERITANCE — surviving individuals pass on their ALLELES to offspring. The next '
                         'generation has more individuals with the advantageous characteristics.\n'
                         '\n'
                         'Over many generations → advantageous alleles become MORE COMMON in the population → the '
                         'population changes → EVOLUTION has occurred.',
              'heading': "Darwin's Theory of Natural Selection"},
             {'content': "Darwin published his theory in 'On the Origin of Species' in 1859.\n"
                         '\n'
                         'It was NOT immediately accepted — reasons include:\n'
                         'Religious opposition — contradicted the biblical account of creation and the idea that '
                         'species were fixed and created by God.\n'
                         'Lack of a mechanism — Darwin did not know HOW inheritance worked (DNA and genetics were not '
                         'yet understood). He could not fully explain HOW traits were passed on.\n'
                         'Insufficient evidence at the time — the fossil record had many gaps.\n'
                         'Difficulty of the concept — evolution over millions of years is hard to observe directly.\n'
                         '\n'
                         'Over time, as genetics was discovered (first Mendel, then Watson and Crick with DNA '
                         "structure), and as more fossil evidence accumulated, Darwin's theory gained overwhelming "
                         'scientific support.\n'
                         '\n'
                         'Today, evolution by natural selection is the scientific consensus — one of the most strongly '
                         'evidenced theories in science.',
              'heading': "Why Darwin's Theory Took Time to be Accepted"},
             {'content': 'ALFRED RUSSEL WALLACE (1823–1913) independently developed a theory of evolution by natural '
                         'selection at approximately the same time as Darwin.\n'
                         '\n'
                         'Wallace sent his ideas to Darwin in 1858 — this prompted Darwin to publish his own work.\n'
                         '\n'
                         "Both men's papers were presented to the Linnean Society of London in 1858.\n"
                         '\n'
                         'Wallace made important contributions to biogeography — the study of how species are '
                         'distributed across the Earth — and the patterns of species distribution supported the theory '
                         'of evolution.\n'
                         '\n'
                         "His work in Southeast Asia led to him identifying what is now called 'Wallace's line' — a "
                         'boundary between Asian and Australian species distributions.',
              'heading': 'Alfred Russel Wallace'}],
  'title': 'Evolution and Natural Selection',
  'triple_only': None,
  'variables': []},
 {'common_mistake': "Natural selection does NOT mean animals consciously choose to evolve. Organisms don't 'try' to "
                    'adapt — those with random variations that happen to be advantageous survive better and reproduce '
                    "more. The environment SELECTS — organisms don't choose. Also: Darwin AND Wallace both developed "
                    'the theory independently.',
  'equations': [],
  'fifas': [],
  'higher': 'Evaluate how evidence from DNA sequencing and protein analysis supports evolutionary relationships more '
            'reliably than morphology alone. Discuss the relative contributions of Darwin and Wallace. Explain how the '
            'modern evolutionary synthesis united Mendelian genetics with Darwinian natural selection. Evaluate how '
            'the mechanisms of evolution have been refined as new evidence has emerged.',
  'id': 'theory-of-evolution',
  'key_note': 'Natural selection: variation → struggle → survival of fittest → inheritance → evolution. Darwin and '
              "Wallace independently developed the theory. Darwin's book (1859) was the most comprehensive. Initially "
              'controversial: no known mechanism, religious opposition, incomplete fossils. Now supported by genetics, '
              'DNA evidence, fossil record, observed examples.',
  'matching': {'instruction': 'Put the four steps of natural selection in the correct order.',
               'pairs': [('Step 1', 'Variation — individuals in a population show different characteristics'),
                         ('Step 2',
                          'Struggle for survival — more offspring produced than can survive, resources limited'),
                         ('Step 3',
                          'Survival of the fittest — individuals with advantageous traits survive and reproduce'),
                         ('Step 4',
                          'Inheritance — advantageous traits passed to offspring, become more common over '
                          'generations')],
               'title': 'Natural Selection Steps'},
  'quiz': [{'opts': [('Wallace independently developed the theory of evolution by natural selection at the same time '
                      'as Darwin — both theories were presented together in 1858',
                      True),
                     ("Wallace was Darwin's assistant who helped collect evidence in the Galapagos Islands", False),
                     ('Wallace disproved evolution and it was Darwin who had to correct him', False),
                     ('Wallace developed the theory of evolution first and Darwin copied his ideas', False)],
            'q': "Which of the following best describes Alfred Russel Wallace's role in the theory of evolution?",
            'wrong_explanations': {1: 'Darwin worked independently in Britain and the Galapagos — Wallace worked in '
                                      'South-East Asia. They were not working together.',
                                   2: 'Wallace fully supported evolution — he independently developed the same theory. '
                                      'Neither disproved it.',
                                   3: "Both developed their ideas independently and at roughly the same time. Darwin's "
                                      'letter from Wallace prompted them to publish jointly in 1858.'}},
           {'opts': [('There was no known mechanism for inheritance, it conflicted with religious views, and the '
                      'fossil record had gaps at the time',
                      True),
                     ('Darwin had no scientific evidence at all — the theory was purely speculative', False),
                     ('Darwin claimed humans evolved from modern chimpanzees, which was clearly wrong', False),
                     ('The theory contradicted all other scientific ideas of the time without any supporting '
                      'observations',
                      False)],
            'q': "Why was Darwin's theory of natural selection initially controversial?",
            'wrong_explanations': {1: 'Darwin had extensive evidence from observations in the Galapagos and elsewhere '
                                      '— the issue was the gaps in the fossil record and lack of a known inheritance '
                                      'mechanism, not a total absence of evidence.',
                                   2: 'Darwin proposed humans shared common ancestors with apes — not that they '
                                      'evolved from modern chimps. Chimps and humans share a common ancestor.',
                                   3: "Darwin's observations of finches, barnacles and many other organisms DID "
                                      'support the theory — the controversy was about the mechanism of inheritance and '
                                      'religious implications.'}}],
  'rp': None,
  'spec': '4.6.3.3',
  'summary': "Describe Darwin's theory of evolution by natural selection and the role of Wallace.",
  'theory': [{'content': "CHARLES DARWIN proposed the theory of evolution by NATURAL SELECTION (1859, 'On the Origin "
                         "of Species').\n"
                         '\n'
                         'The mechanism has four key steps:\n'
                         '\n'
                         '1. VARIATION — individuals in a population show variation in their characteristics.\n'
                         '2. STRUGGLE FOR SURVIVAL — organisms produce more offspring than can survive; resources are '
                         'limited.\n'
                         '3. SURVIVAL OF THE FITTEST — individuals with advantageous characteristics are more likely '
                         'to survive and reproduce.\n'
                         '4. INHERITANCE — the advantageous characteristics are passed to offspring (heritable '
                         'variation).\n'
                         '\n'
                         'Over many generations → alleles for advantageous traits become more common in the population '
                         '→ the population EVOLVES.\n'
                         '\n'
                         'EXAMPLE — Peppered moth:\n'
                         'Before Industrial Revolution: light moths more common (camouflaged against pale bark).\n'
                         'After: soot darkened trees → dark moths better camouflaged → survived better → dark allele '
                         'became more common.',
              'heading': "Darwin's Theory of Natural Selection"},
             {'content': 'ALFRED RUSSEL WALLACE independently developed a theory of evolution by natural selection at '
                         'the same time as Darwin.\n'
                         '\n'
                         'Wallace wrote to Darwin in 1858 with his ideas — Darwin realised Wallace had reached the '
                         'same conclusions.\n'
                         'Both theories were presented together to the Linnean Society in 1858.\n'
                         "Darwin published 'On the Origin of Species' in 1859 — the most complete and evidenced "
                         'account.\n'
                         '\n'
                         "WALLACE'S CONTRIBUTIONS:\n"
                         "Wallace's work in South-East Asia — he noticed differences between species on different "
                         'islands.\n'
                         'Developed ideas about natural selection from observations of wildlife in the Amazon and '
                         'Malay Archipelago.\n'
                         'Wallace also pioneered ideas about biogeography — why different species live in different '
                         'regions.\n'
                         "His concept of 'warning colouration' (aposematism) — bright colours warning predators of "
                         'toxicity.\n'
                         '\n'
                         'Why Darwin gets more credit:\n'
                         'Darwin had 20 years more data and evidence supporting the theory.\n'
                         "Darwin's book was much more detailed and comprehensive.\n"
                         "But Wallace's independent discovery strengthens confidence in the theory.",
              'heading': 'Alfred Russel Wallace'},
             {'content': "Darwin's theory was initially CONTROVERSIAL for several reasons:\n"
                         '\n'
                         '1. LACK OF MECHANISM:\n'
                         "Darwin didn't know HOW characteristics were inherited (genetics wasn't understood yet).\n"
                         "Mendel's work on inheritance was concurrent but unknown to Darwin.\n"
                         '\n'
                         '2. RELIGIOUS OPPOSITION:\n'
                         'Conflicted with religious beliefs that species were created in their current form.\n'
                         'Implication that humans evolved from ape-like ancestors was particularly controversial.\n'
                         '\n'
                         '3. INCOMPLETE FOSSIL RECORD:\n'
                         'In 1859, there were gaps in the fossil record — critics argued there was insufficient '
                         'evidence.\n'
                         'Subsequent discoveries (e.g. transitional fossils like Archaeopteryx) provided more '
                         'support.\n'
                         '\n'
                         'WHY THE THEORY IS NOW ACCEPTED:\n'
                         'Genetics — discovered independently by Mendel, later integrated with evolution (Modern '
                         'Synthesis).\n'
                         'DNA evidence — genetic similarities between species match evolutionary relationships.\n'
                         'Fossil record — many transitional fossils now found.\n'
                         'Observed evolution — antibiotic resistance, Galapagos finch beak changes seen in real time.\n'
                         'The scientific community accepts evolution as the best explanation for the diversity of '
                         'life.',
              'heading': 'Why the Theory Was Controversial'}],
  'title': 'Theory of Evolution',
  'triple_only': 'Theory of evolution detail (4.6.3.3) is biology-only — Combined Science covers evolution and natural '
                 "selection more briefly. Triple includes Darwin's mechanism in detail, Wallace's contribution, and "
                 'why the theory was controversial and how it gained acceptance.',
  'variables': []},
 {'common_mistake': 'Selective breeding is NOT genetic engineering. Selective breeding uses natural reproduction — '
                    'choosing which organisms breed. Genetic engineering directly inserts, removes or modifies '
                    'specific genes. Selective breeding also does NOT create new genes — it selects and concentrates '
                    'alleles that already exist in the population.',
  'equations': [],
  'fifas': [],
  'higher': 'Continuous selective breeding over many generations reduces genetic diversity — all individuals become '
            'very similar genetically. This creates vulnerability: if a new pathogen emerges to which the population '
            'has no resistance, all individuals are equally affected (e.g. Irish Potato Famine — near-total loss of a '
            'single potato variety). Students should be able to evaluate the ethical implications of selective '
            'breeding including animal welfare concerns.',
  'id': 'selective-breeding',
  'key_note': 'Selective breeding: humans choose organisms with desired traits to breed. Takes many generations. '
              'Increases desired characteristics. Disadvantages: reduced genetic diversity, inbreeding, health '
              'problems in extreme cases.',
  'matching': {'instruction': 'Match each organism to the characteristic that has been selectively bred.',
               'pairs': [('Dairy cattle', 'Selectively bred for increased milk yield — e.g. Holstein Friesian'),
                         ('Wheat', 'Selectively bred for disease resistance and high grain yield'),
                         ('Dogs (greyhounds)', 'Selectively bred for speed in racing'),
                         ('Chickens', 'Selectively bred for rapid growth and/or high egg production'),
                         ('Maize (corn)',
                          'Selectively bred from a small wild grass to produce large cobs over thousands of years')],
               'title': 'Match the Selective Breeding Example'},
  'quiz': [{'opts': [('Reduced genetic diversity — the gene pool narrows, making populations vulnerable to new '
                      'diseases or environmental changes',
                      True),
                     ('Selective breeding always produces weaker offspring than wild populations', False),
                     ('It produces organisms that cannot survive outside captivity or cultivation', False),
                     ('The desired traits always disappear after a few generations', False)],
            'q': 'What is the main disadvantage of selective breeding over many generations?',
            'wrong_explanations': {1: 'Selectively bred organisms are often very productive — but reduced genetic '
                                      'diversity is the key long-term risk.',
                                   2: 'Many selectively bred organisms can survive in natural conditions — though some '
                                      'extreme examples (like bulldogs) do have welfare issues.',
                                   3: "Selective breeding fixes desired traits into the genome — they don't disappear "
                                      'unless the selection pressure is removed and interbreeding with different '
                                      'varieties occurs.'}},
           {'opts': [('Selective breeding uses natural reproduction to concentrate existing alleles. Genetic '
                      'engineering directly inserts, modifies or removes specific genes.',
                      True),
                     ('Selective breeding is faster than genetic engineering', False),
                     ('Selective breeding creates entirely new genes. Genetic engineering uses existing ones.', False),
                     ("They are essentially the same process — both involve deliberately changing an organism's DNA",
                      False)],
            'q': 'How is selective breeding different from genetic engineering?',
            'wrong_explanations': {1: 'Selective breeding is SLOW — it takes many generations. Genetic engineering can '
                                      'produce results in one generation.',
                                   2: 'Selective breeding works with EXISTING genetic variation — it cannot create new '
                                      'genes. Genetic engineering can introduce genes from completely different '
                                      'species.',
                                   3: 'Selective breeding does NOT directly change DNA sequences — it selects which '
                                      'individuals reproduce. Genetic engineering directly manipulates DNA.'}}],
  'rp': None,
  'spec': '4.6.6',
  'summary': 'Describe how selective breeding works and its applications and disadvantages.',
  'theory': [{'content': 'SELECTIVE BREEDING (also called artificial selection) is the process by which HUMANS choose '
                         'organisms with DESIRED CHARACTERISTICS to breed together, over many generations, in order to '
                         'enhance those characteristics.\n'
                         '\n'
                         'Humans have been selectively breeding animals and plants for approximately 10,000 years — '
                         'since the beginning of agriculture.\n'
                         '\n'
                         'The process:\n'
                         '1. Identify individuals in a population that show the desired characteristic most strongly.\n'
                         '2. Breed these selected individuals together.\n'
                         '3. From the offspring, select those that best show the desired characteristic.\n'
                         '4. Repeat over many generations.\n'
                         '5. After many generations, the desired trait becomes strongly established in the population.',
              'heading': 'What is Selective Breeding?'},
             {'content': 'ANIMALS:\n'
                         'DOGS — bred for specific behaviours and appearances: border collies (herding instinct), '
                         'greyhounds (speed), St. Bernards (size and rescue ability), bulldogs (appearance — though '
                         'controversial due to health issues).\n'
                         'CATTLE — bred for high milk yield (dairy breeds like Holstein) or high meat yield (beef '
                         'breeds like Angus).\n'
                         'CHICKENS — bred for rapid growth, high egg production, or both.\n'
                         'SHEEP — bred for high wool production, high meat yield or specific fleece qualities.\n'
                         '\n'
                         'PLANTS:\n'
                         'WHEAT — bred for disease resistance, high yield, drought tolerance, shorter stems (reduces '
                         'lodging in wind).\n'
                         'CORN (MAIZE) — from a small, wild grass (teosinte) to modern maize with large cobs over '
                         'thousands of years.\n'
                         'STRAWBERRIES — bred for larger fruit, sweeter taste, disease resistance.\n'
                         'ROSES — bred for specific colours, petal arrangements and scent.\n'
                         'BROCCOLI, CABBAGE, KALE, CAULIFLOWER — all bred from the same wild plant (Brassica oleracea) '
                         'by selecting for different features.',
              'heading': 'Examples of Selective Breeding'},
             {'content': 'ADVANTAGES:\n'
                         'Produces organisms with highly desirable characteristics — increased yield, disease '
                         'resistance, better flavour.\n'
                         'Has dramatically increased food production — helping feed a growing global population.\n'
                         'Can produce animals better suited to human purposes — working dogs, guide dogs, therapy '
                         'animals.\n'
                         '\n'
                         'DISADVANTAGES:\n'
                         'REDUCED GENETIC DIVERSITY — by continually selecting the same traits, populations become '
                         'genetically very similar (inbreeding).\n'
                         'INBREEDING problems — reduced variation means if a new disease or environmental change '
                         'occurs, the entire population may be vulnerable.\n'
                         'HEALTH PROBLEMS — selection for extreme traits can cause welfare issues. Examples: bulldogs '
                         'have such flat faces they struggle to breathe; some large dog breeds have hip problems; '
                         'high-yield dairy cows often suffer from mastitis.\n'
                         'INHERITED DISEASES — concentrated in small gene pool over generations.\n'
                         'The process is slow — takes many generations to achieve significant change.',
              'heading': 'Advantages and Disadvantages of Selective Breeding'}],
  'title': 'Selective Breeding',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Genetic engineering is NOT the same as selective breeding. Genetic engineering can transfer genes '
                    'between completely different species (e.g. human genes into bacteria). Selective breeding can '
                    'only work with organisms that can naturally reproduce together. Also: eating GM food does not '
                    "alter the consumer's own DNA.",
  'equations': [],
  'fifas': [],
  'higher': 'Restriction enzymes cut DNA at specific recognition sequences. Ligase enzymes join DNA fragments. The '
            'target gene is inserted into a vector (usually a bacterial plasmid). The vector is introduced into the '
            'host cell (bacteria, plant, animal). GM bacteria produce human insulin (insulin gene from human DNA '
            'inserted into E. coli). Students should evaluate both the potential benefits (medicine, food security) '
            'and risks (gene escape, biodiversity reduction, corporate control of food supply) of GM organisms.',
  'id': 'genetic-engineering',
  'key_note': 'Genetic engineering: cut gene with restriction enzymes → insert into vector (plasmid) → introduce to '
              'target organism. Examples: human insulin from GM bacteria, herbicide-resistant crops, Golden Rice. '
              'Ethical debate: benefits vs risks to biodiversity and ecosystems.',
  'matching': {'instruction': 'Match each application to how genetic engineering is used.',
               'pairs': [('GM bacteria → insulin',
                          'Human insulin gene inserted into bacteria — bacteria produce insulin for diabetics'),
                         ('Herbicide-resistant crops',
                          'Gene for herbicide resistance inserted into crop plants — farmer can spray without harming '
                          'the crop'),
                         ('Bt crops',
                          'Gene from Bacillus thuringiensis inserted — crop produces natural insecticide to repel '
                          'pests'),
                         ('Golden Rice',
                          'Gene inserted to produce beta-carotene — addresses vitamin A deficiency in developing '
                          'countries')],
               'title': 'Match the Genetic Engineering Example'},
  'quiz': [{'opts': [('GM bacterial insulin is identical to human insulin — fewer immune reactions and side effects',
                      True),
                     ('Bacterial insulin is cheaper to produce so more people can afford it', False),
                     ('Animal-derived insulin is no longer available — GM insulin is the only option', False),
                     ('GM bacteria produce insulin faster so it acts more quickly in the body', False)],
            'q': 'Why is GM bacterial insulin better for diabetics than insulin extracted from pigs or cattle?',
            'wrong_explanations': {1: 'Cost is an advantage, but the primary medical reason is that human sequence '
                                      'insulin causes fewer immune problems than animal sequence insulin.',
                                   2: 'Animal-derived insulin still exists in some countries — GM insulin has largely '
                                      'replaced it due to superior compatibility.',
                                   3: 'The speed of action is determined by the formulation (how the insulin is '
                                      'prepared), not where it came from.'}},
           {'opts': [('Cut the desired gene using restriction enzymes → insert into a plasmid vector → introduce the '
                      'vector into the target cell',
                      True),
                     ('Inject the desired gene directly into the cell nucleus using a syringe', False),
                     ('Breed the organism with another species that carries the desired gene', False),
                     ('Expose the organism to radiation to trigger the mutation needed', False)],
            'q': 'What is the basic process of introducing a new gene into an organism?',
            'wrong_explanations': {1: 'While microinjection into cells is a real technique used in some contexts, the '
                                      'standard recombinant DNA approach uses restriction enzymes and plasmid vectors.',
                                   2: 'Breeding between different species = selective breeding (and only works between '
                                      'related species). Genetic engineering specifically allows cross-species gene '
                                      'transfer.',
                                   3: 'Radiation causes RANDOM mutations — not the specific targeted change needed for '
                                      'genetic engineering.'}}],
  'rp': None,
  'spec': '4.6.7',
  'summary': 'Describe genetic engineering — how it works, examples and ethical considerations.',
  'theory': [{'content': 'GENETIC ENGINEERING (also called recombinant DNA technology or genetic modification) is the '
                         "direct manipulation of an organism's DNA — inserting, removing or modifying specific genes.\n"
                         '\n'
                         'Unlike selective breeding, genetic engineering:\n'
                         'Can introduce genes from COMPLETELY DIFFERENT SPECIES — e.g. human genes into bacteria.\n'
                         'Works in a single generation — no need to wait many generations.\n'
                         'Is extremely precise — targets a specific gene.\n'
                         '\n'
                         'The basic process:\n'
                         "1. The desired gene is CUT from the source organism's DNA using restriction enzymes "
                         '(molecular scissors).\n'
                         '2. The gene is INSERTED into a VECTOR — usually a bacterial PLASMID (a small circular piece '
                         'of DNA).\n'
                         "3. The vector is introduced into the target organism's cells.\n"
                         "4. The target organism's cells now EXPRESS the new gene — producing the desired protein.",
              'heading': 'What is Genetic Engineering?'},
             {'content': 'INSULIN PRODUCTION:\n'
                         'Human insulin gene inserted into BACTERIA.\n'
                         'Bacteria grow rapidly in large vats → produce large quantities of human insulin.\n'
                         'Used to treat Type 1 diabetes.\n'
                         'Before this (before ~1982), diabetics used insulin extracted from pig or cattle pancreases — '
                         'which caused immune reactions in some patients.\n'
                         'Human insulin from GM bacteria is identical to natural human insulin → fewer side effects.\n'
                         '\n'
                         'GM CROPS (Genetically Modified crops):\n'
                         'HERBICIDE RESISTANCE — a gene for herbicide resistance inserted into crop plants (e.g. GM '
                         'soybean). Farmers can spray the field to kill weeds without harming the crop.\n'
                         'PEST RESISTANCE — Bt crops: a gene from the bacterium Bacillus thuringiensis produces a '
                         'natural insecticide within the plant. Reduces need for chemical pesticides.\n'
                         'GOLDEN RICE — a gene from daffodils (and a bacterium) inserted into rice to produce '
                         'beta-carotene (precursor to vitamin A). Addresses vitamin A deficiency in developing '
                         'countries.\n'
                         'DROUGHT TOLERANCE — genes that increase water efficiency inserted into crops for use in dry '
                         'regions.',
              'heading': 'Examples of Genetic Engineering'},
             {'content': 'Genetic engineering raises significant ethical debates:\n'
                         '\n'
                         'ARGUMENTS FOR:\n'
                         'Can save lives — GM insulin prevents deaths from diabetes.\n'
                         'Can increase food security — GM crops produce higher yields, resist disease and pests.\n'
                         'Can address nutritional deficiencies — e.g. Golden Rice.\n'
                         'May reduce environmental impact — pest-resistant crops need fewer chemical pesticides.\n'
                         '\n'
                         'ARGUMENTS AGAINST:\n'
                         'UNCERTAINTY about long-term effects — what happens when GM organisms interact with wild '
                         'ecosystems?\n'
                         "BIODIVERSITY risks — modified genes could spread to wild relatives ('gene escape').\n"
                         'MONOCULTURES — large-scale GM crop production may reduce genetic diversity.\n'
                         'CORPORATE CONTROL — major biotechnology companies own patents on GM seeds, preventing '
                         'farmers from saving seeds.\n'
                         'ANIMAL WELFARE — concerns about use of genetically modified animals in research.\n'
                         "CONSUMER CONCERNS — some people don't want to eat GM food, regardless of scientific evidence "
                         'of safety.\n'
                         "Religious/ethical objections — interfering with 'nature' or 'playing God'.",
              'heading': 'Ethical Considerations of Genetic Engineering'}],
  'title': 'Genetic Engineering',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Clones are genetically identical but NOT necessarily physically identical — environment '
                    '(temperature, nutrition, upbringing) affects how genes are expressed. Dolly was genetically '
                    "identical to her donor but didn't look exactly the same. Genotype ≠ phenotype.",
  'equations': [],
  'fifas': [],
  'higher': 'Evaluate the potential medical applications of therapeutic cloning for producing patient-matched tissues. '
            'Discuss the scientific, ethical and social issues of human reproductive cloning. Evaluate the commercial '
            'implications of animal cloning in agriculture — compare costs, benefits and public concerns. Assess the '
            'risk of genetic uniformity in cloned animal populations.',
  'id': 'cloning',
  'key_note': 'Plant cloning: cuttings (simple, cheap) or tissue culture (micropropagation, thousands of plants). '
              'Animal cloning: embryo splitting or nuclear transfer (somatic cell). Dolly — first mammal cloned from '
              'adult cell (1996). Advantages: preserve species, superior traits. Disadvantages: low genetic diversity, '
              'ethical issues, health problems.',
  'matching': {'instruction': 'Match each cloning method to its description.',
               'pairs': [('Cuttings',
                          'Simple plant cloning — stem placed in soil with rooting hormone, grows into identical '
                          'plant'),
                         ('Tissue culture',
                          'Micropropagation — thousands of identical plants from tiny tissue sample on nutrient agar'),
                         ('Embryo transplant',
                          'Animal cloning — fertilised embryo split and implanted into surrogate mothers'),
                         ('Nuclear transfer',
                          'Adult body cell nucleus inserted into enucleated egg — method used to clone Dolly the '
                          'sheep')],
               'title': 'Cloning Methods'},
  'quiz': [{'opts': [('Reduced genetic diversity — all plants identical so equally susceptible to new diseases or '
                      'pests',
                      True),
                     ('Cloned plants grow slower than normal plants', False),
                     ('Cloned plants cannot reproduce sexually — they die after one generation', False),
                     ('Cloning uses up all the nutrients in the soil faster than non-cloned plants', False)],
            'q': 'What is the main disadvantage of producing large numbers of cloned crop plants?',
            'wrong_explanations': {1: 'Cloned plants can grow as fast as any plant — growth rate depends on genetics '
                                      'and environment, not the cloning process itself.',
                                   2: 'Cloned plants CAN reproduce sexually — they are genetically normal plants. The '
                                      "issue is that they are all identical, not that they can't reproduce.",
                                   3: "Cloned plants don't consume more nutrients — the genetic uniformity is the "
                                      'problem, not nutrient use.'}},
           {'opts': [('From the adult body cell (donor) — its nucleus contains the DNA used to produce the clone',
                      True),
                     ("From the egg cell — the egg's nucleus provides all the genetic material", False),
                     ('Equally from both the egg and the adult body cell', False),
                     ("From a combination of the surrogate mother's DNA and the donor's DNA", False)],
            'q': 'In nuclear transfer cloning, where does the genetic material of the clone come from?',
            'wrong_explanations': {1: 'The EGG nucleus is REMOVED (enucleated) — it contributes no nuclear DNA to the '
                                      'clone.',
                                   2: 'The nuclear DNA comes from the adult donor cell only. The egg contributes a '
                                      'tiny amount of mitochondrial DNA but its nucleus is removed.',
                                   3: 'The surrogate mother carries the embryo but contributes NO genetic material to '
                                      'the clone — she is just the carrier.'}}],
  'rp': None,
  'spec': '4.6.4',
  'summary': 'Describe cloning methods in plants and animals and evaluate their advantages and disadvantages.',
  'theory': [{'content': 'Plants can be cloned relatively easily using two main methods:\n'
                         '\n'
                         'TAKING CUTTINGS:\n'
                         'A stem or leaf cutting is taken from the parent plant.\n'
                         'The cut end is dipped in rooting hormone and planted in soil.\n'
                         'The cutting develops roots and grows into a new plant — genetically identical to the '
                         'parent.\n'
                         'Used for: roses, geraniums, herbs, many houseplants.\n'
                         'Advantages: simple, cheap, fast.\n'
                         '\n'
                         'TISSUE CULTURE (MICROPROPAGATION):\n'
                         'A tiny piece of plant tissue (explant) is removed — from the growing tip (meristem).\n'
                         'Placed on nutrient agar with plant hormones.\n'
                         'Cells divide and form a callus (undifferentiated mass of cells).\n'
                         'Callus is transferred to medium with different hormones → forms shoots and roots.\n'
                         'Thousands of identical plants produced from a single parent.\n'
                         'Advantages: produce many plants quickly, disease-free plants, preserve rare species.\n'
                         'Disadvantages: expensive, requires specialist equipment and sterile conditions.',
              'heading': 'Plant Cloning'},
             {'content': 'Animal cloning is more complex than plant cloning.\n'
                         '\n'
                         'EMBRYO TRANSPLANTS:\n'
                         '1. A female is given fertility drugs → produces multiple eggs.\n'
                         '2. Eggs are fertilised IN VITRO (outside the body) using selected sperm.\n'
                         '3. The developing embryo is split into multiple pieces before cells differentiate.\n'
                         '4. Each piece develops into a genetically identical embryo.\n'
                         '5. Embryos are transplanted into SURROGATE MOTHERS who carry them to birth.\n'
                         '\n'
                         'Used in: cattle and sheep farming to produce multiple offspring from genetically superior '
                         'parents.\n'
                         '\n'
                         'NUCLEAR TRANSFER (SOMATIC CELL NUCLEAR TRANSFER):\n'
                         'The technique used to produce Dolly the sheep (1996).\n'
                         '1. Nucleus removed from an unfertilised egg (enucleated egg).\n'
                         '2. Nucleus from an adult body cell (somatic cell) inserted into the enucleated egg.\n'
                         '3. Electric shock stimulates cell division.\n'
                         '4. Embryo develops and is implanted into a surrogate.\n'
                         '5. Offspring is genetically identical to the adult whose nucleus was used.\n'
                         '\n'
                         'Dolly was the first mammal cloned from an adult cell — a major scientific breakthrough.',
              'heading': 'Animal Cloning — Embryo Transplants'},
             {'content': 'ADVANTAGES:\n'
                         'Preserve ENDANGERED SPECIES — clone animals at risk of extinction.\n'
                         'Produce genetically SUPERIOR animals — all offspring inherit the best traits.\n'
                         'Medical research — produce animals with human diseases for drug testing.\n'
                         'Potential to produce organs for transplant (therapeutic cloning).\n'
                         'Preserve rare PLANT VARIETIES and produce disease-resistant crops.\n'
                         '\n'
                         'DISADVANTAGES:\n'
                         'REDUCES GENETIC DIVERSITY — large population of identical organisms vulnerable to same '
                         'disease.\n'
                         'ETHICAL CONCERNS about cloning humans (reproductive cloning).\n'
                         'CLONED ANIMALS often have health problems — Dolly developed arthritis and lung disease '
                         'early.\n'
                         'Expensive and technically difficult (animal cloning especially).\n'
                         'Low SUCCESS RATE for nuclear transfer — many attempts needed to produce one viable clone.\n'
                         '\n'
                         'ETHICAL DEBATE:\n'
                         'Therapeutic cloning (for medical treatment) vs reproductive cloning (creating cloned '
                         'organisms) — different ethical considerations.\n'
                         'Scientific community broadly supports therapeutic, opposes reproductive human cloning.',
              'heading': 'Advantages and Disadvantages of Cloning'}],
  'title': 'Cloning',
  'triple_only': 'Cloning (4.6.4) is biology-only — not in Combined Science. Covers plant cloning (cuttings and tissue '
                 'culture), animal cloning (embryo transplants and nuclear transfer), and evaluation of advantages and '
                 'disadvantages.',
  'variables': []},
 {'common_mistake': 'The fossil record is INCOMPLETE — most organisms never fossilise. This means gaps in the fossil '
                    "record are EXPECTED and do not disprove evolution. Students often say 'if there are gaps in the "
                    "fossil record, evolution can't be proven' — but the overall pattern of fossils strongly supports "
                    'evolution, even with gaps.',
  'equations': [],
  'fifas': [],
  'higher': 'Speciation provides the mechanism for the origin of new species through natural selection — it is the '
            'endpoint of divergent evolution from a common ancestor. Modern systematics uses DNA sequences and '
            'phylogenetic trees rather than physical appearance for classification. Convergent evolution (similar '
            'structures evolving independently in unrelated species due to similar selection pressures) must be '
            'distinguished from homologous structures (shared ancestry).',
  'id': 'evidence-for-evolution',
  'key_note': 'Evidence: fossils (older = simpler, gradual change), homologous structures (pentadactyl limb — common '
              'ancestor), DNA comparisons (similar species = similar DNA), direct observation (antibiotic resistance, '
              'flu evolution). All support evolution.',
  'matching': {'instruction': 'Match each piece of evidence to what it demonstrates about evolution.',
               'pairs': [('Fossil record',
                          'Shows gradual changes in organisms over millions of years — older fossils are simpler'),
                         ('Pentadactyl limb',
                          'Same bone structure in human, whale, bat and horse limbs — suggests common ancestor'),
                         ('DNA comparisons',
                          'Closely related species have more similar DNA sequences — reflects evolutionary distance'),
                         ('Antibiotic resistance',
                          'Bacteria evolving resistance in real time — direct observation of natural selection'),
                         ('Universal genetic code',
                          'All life uses the same DNA code — suggests all organisms descended from a common ancestor')],
               'title': 'Match the Evidence to What it Shows'},
  'quiz': [{'opts': [('They share the same underlying bone structure despite very different functions — suggesting a '
                      'common ancestor whose limb adapted differently in each lineage',
                      True),
                     ('They show that all vertebrates use their limbs in the same way — a universal design', False),
                     ('Five-digit limbs are the most efficient design, so evolution always produces them independently',
                      False),
                     ('It shows that whales were once land animals that walked on five-toed feet', False)],
            'q': 'Why do the pentadactyl (five-digit) limbs of humans, whales and bats support evolution?',
            'wrong_explanations': {1: 'Vertebrate limbs are used very differently — for flying, swimming, running and '
                                      'grasping. The similarity in structure, despite different functions, is '
                                      'precisely what makes it evidence of common ancestry.',
                                   2: "If five digits were universally optimal, we'd expect to see it in insects and "
                                      "fish too — but they don't have this arrangement. The pattern is phylogenetic "
                                      '(family-tree based), not design-based.',
                                   3: "While it's true whales evolved from land mammals, the pentadactyl limb evidence "
                                      'is specifically about STRUCTURAL SIMILARITY across multiple species, not '
                                      'specifically about whale evolution.'}},
           {'opts': [('It demonstrates natural selection occurring in real time — resistant variants survive and '
                      'reproduce, changing the population',
                      True),
                     ('It shows that bacteria can deliberately change their DNA in response to threats', False),
                     ('It proves that antibiotics cause mutations in bacteria', False),
                     ('It shows that evolution only happens in very simple organisms like bacteria', False)],
            'q': 'Why does antibiotic resistance in bacteria provide evidence for evolution?',
            'wrong_explanations': {1: 'Bacteria cannot choose or deliberately change their DNA — resistance arises '
                                      'from RANDOM mutations that existed before antibiotic exposure.',
                                   2: "Antibiotics SELECT resistant variants — they don't cause the mutations. The "
                                      'mutations existed before the antibiotic was used.',
                                   3: 'Evolution occurs in all organisms — bacteria just evolve faster because they '
                                      'reproduce rapidly (millions of generations in days). Natural selection has been '
                                      'directly observed in larger organisms too.'}}],
  'rp': None,
  'spec': '4.6.5',
  'summary': 'Describe the main types of evidence that support the theory of evolution.',
  'theory': [{'content': 'FOSSILS are the preserved remains or traces of organisms from the past.\n'
                         '\n'
                         "Fossils form when an organism's hard parts (bones, shells, teeth) are buried and slowly "
                         'replaced by minerals over millions of years. Soft tissue rarely fossilises — so the fossil '
                         'record is incomplete.\n'
                         '\n'
                         'Other types of fossil: trace fossils (footprints, burrows), preserved organisms in amber, '
                         'ice or tar pits.\n'
                         '\n'
                         'How fossils support evolution:\n'
                         'Older rock layers (deeper in the ground) contain simpler, more primitive organisms.\n'
                         'Younger rocks (closer to the surface) contain more complex, more modern-looking organisms.\n'
                         'Transitional fossils show intermediate forms between ancient and modern species — e.g. '
                         'Tiktaalik (fish-tetrapod transition), Archaeopteryx (dinosaur-bird transition).\n'
                         'Gradual changes in fossil series show how species changed over millions of years.\n'
                         '\n'
                         'Limitation: the fossil record is incomplete — most organisms never fossilise, and many '
                         'fossils are yet to be discovered.',
              'heading': 'The Fossil Record'},
             {'content': 'HOMOLOGOUS STRUCTURES are body parts that have the SAME UNDERLYING STRUCTURE but are adapted '
                         'for DIFFERENT FUNCTIONS in different species.\n'
                         '\n'
                         'The classic example is the PENTADACTYL LIMB (five-digit limb):\n'
                         'Human arm — for grasping and manipulating objects.\n'
                         'Whale flipper — for swimming.\n'
                         'Bat wing — for flying.\n'
                         'Horse leg — for running.\n'
                         'Frog limb — for swimming and jumping.\n'
                         '\n'
                         'All of these limbs have the same arrangement of bones (humerus, radius, ulna, carpals, '
                         'metacarpals, phalanges) — just modified in shape and proportion for different uses.\n'
                         '\n'
                         'This shared fundamental structure strongly suggests they all evolved from a COMMON ANCESTOR '
                         'that had a basic five-digit limb — the limbs diverged as each lineage adapted to different '
                         'environments.\n'
                         '\n'
                         'If these structures had evolved independently, there would be no reason for them to share '
                         'the same underlying bone arrangement.',
              'heading': 'Homologous Structures'},
             {'content': 'Modern molecular biology provides some of the strongest evidence for evolution.\n'
                         '\n'
                         'DNA COMPARISONS:\n'
                         'All living organisms use the same genetic code (the same triplet of bases codes for the same '
                         'amino acid, in virtually all species).\n'
                         'This UNIVERSAL GENETIC CODE strongly suggests all life descended from a common ancestor.\n'
                         'The more closely related two species are, the MORE SIMILAR their DNA sequences are.\n'
                         'Example: humans and chimpanzees share approximately 98.7% of their DNA — reflecting our '
                         'recent common ancestor.\n'
                         'Humans and yeast share about 25% of their genes — both are eukaryotes descended from the '
                         'same original eukaryotic ancestor.\n'
                         '\n'
                         'PROTEIN COMPARISONS:\n'
                         'Similarly, closely related species share more similar protein structures.\n'
                         'Haemoglobin (the oxygen-carrying protein in blood) has a very similar structure in all '
                         'vertebrates — with differences reflecting evolutionary distance.\n'
                         '\n'
                         'VIRUSES and BACTERIA evolving in real time:\n'
                         'Antibiotic resistance in bacteria.\n'
                         'New influenza strains each year.\n'
                         'COVID-19 variants (Alpha, Delta, Omicron).\n'
                         'All demonstrate evolution by natural selection occurring today — observable directly.',
              'heading': 'DNA and Molecular Evidence'}],
  'title': 'Evidence for Evolution',
  'triple_only': None,
  'variables': []},
 {'common_mistake': "Mendel did NOT discover DNA — he proposed 'heritable units' without knowing what they were "
                    'physically. DNA and chromosomes were discovered later. Mendel was rediscovered in 1900 — 16 years '
                    'after his death. His work was ignored because of communication issues and lack of a physical '
                    'mechanism, not because it was wrong.',
  'equations': [],
  'fifas': [],
  'higher': "Explain why Mendel's work was not accepted: obscure publication, unfamiliar statistical approach, no "
            "known physical mechanism. Describe how Mendel's work was vindicated in 1900 when chromosomes were "
            'discovered and three scientists independently reproduced his ratios. Explain how this illustrates the '
            'process of science: independent replication builds confidence; new physical evidence enables acceptance.',
  'id': 'understanding-genetics',
  'key_note': 'Mendel: pea plant experiments → dominant/recessive traits, 3:1 ratios, heritable units (genes). '
              'Published 1866 — ignored until rediscovered in 1900. Reasons for non-acceptance: obscure journal, '
              "mathematical approach, no known mechanism. Now: 'Father of Genetics'. His units = genes on chromosomes "
              '(meiosis explains separation).',
  'matching': {'instruction': "Match each statement to the correct aspect of Mendel's work.",
               'pairs': [("Mendel's finding",
                          'Some traits are dominant — they mask recessive traits when both are present'),
                         ("Mendel's finding",
                          'Crossing Tt × Tt produces a 3:1 ratio of dominant to recessive phenotype'),
                         ('Why ignored',
                          'Published in obscure journal, used unusual mathematical approach, no known physical '
                          'mechanism'),
                         ('Rediscovery 1900',
                          "Three scientists independently found the same ratios — chromosomes now known, Mendel's "
                          'units explained')],
               'title': "Mendel's Contributions"},
  'quiz': [{'opts': [('Genes — specific sequences of DNA on chromosomes that control characteristics', True),
                     ('Chromosomes — the structures in the nucleus that carry genetic information', False),
                     ('Alleles — different versions of the same characteristic', False),
                     ('Nucleotides — the building blocks of DNA molecules', False)],
            'q': "What name do we now give to Mendel's 'heritable units'?",
            'wrong_explanations': {1: "Chromosomes contain genes — they are not the same as Mendel's units. "
                                      'Chromosomes are the structures; genes are the specific sequences within them.',
                                   2: "Alleles are different versions of the SAME gene — Mendel's units are genes (not "
                                      "just alleles). Alleles are a type of unit, but 'genes' is the correct modern "
                                      'term.',
                                   3: 'Nucleotides are the building blocks of DNA — they make up genes but are not '
                                      "equivalent to Mendel's heritable units."}},
           {'opts': [('His results were published in a little-read journal, biologists were unfamiliar with '
                      "statistical approaches, and there was no known physical mechanism for his 'heritable units'",
                      True),
                     ('His results were wrong — the 3:1 ratio was only proven to be correct after his death', False),
                     ("Mendel refused to share his data — other scientists couldn't verify his work", False),
                     ('The church banned his work — scientists feared publishing support for it', False)],
            'q': "Why was Mendel's work not accepted by the scientific community during his lifetime?",
            'wrong_explanations': {1: "Mendel's 3:1 ratio was CORRECT and was reproduced exactly when his work was "
                                      'rediscovered in 1900 — the problem was communication and lack of a known '
                                      'mechanism.',
                                   2: 'Mendel DID publish his data in full — the problem was that few scientists read '
                                      'the journal and fewer understood his mathematical approach.',
                                   3: 'While Mendel was a monk, there is no evidence the church banned his work — he '
                                      "actually carried out his research with the monastery's support."}}],
  'rp': None,
  'spec': '4.6.3.4',
  'summary': "Describe Mendel's work on inheritance and explain why his ideas were not accepted during his lifetime.",
  'theory': [{'content': 'GREGOR MENDEL (1822–1884) was an Augustinian monk who carried out breeding experiments on '
                         'pea plants.\n'
                         '\n'
                         "MENDEL'S EXPERIMENTS:\n"
                         'Crossed pea plants with different characteristics — tall vs short, round seeds vs wrinkled, '
                         'yellow vs green.\n'
                         'Carefully counted the offspring in each generation.\n'
                         'Recorded results over many generations and thousands of plants.\n'
                         '\n'
                         'KEY FINDINGS:\n'
                         '1. Some traits are DOMINANT and some are RECESSIVE.\n'
                         "2. Characteristics are controlled by pairs of 'heritable units' (what we now call alleles).\n"
                         '3. The units separate during gamete formation — offspring inherit one unit from each '
                         'parent.\n'
                         '4. In a cross between tall (TT) × short (tt): all F1 offspring tall (Tt) — dominant masks '
                         'recessive.\n'
                         '5. F1 × F1 (Tt × Tt): 3 tall : 1 short ratio in F2 — the 3:1 ratio.\n'
                         '\n'
                         'These were the LAWS OF INHERITANCE — the foundation of genetics.',
              'heading': "Mendel's Pea Plant Experiments"},
             {'content': 'Mendel published his results in 1866 — but they were largely IGNORED for 34 years.\n'
                         '\n'
                         'REASONS FOR LACK OF ACCEPTANCE:\n'
                         '\n'
                         '1. COMMUNICATION:\n'
                         'Published in a relatively obscure journal (Proceedings of the Natural History Society of '
                         'Brünn).\n'
                         'Few scientists read it at the time.\n'
                         '\n'
                         '2. MATHEMATICAL APPROACH:\n'
                         'Mendel used statistics and ratios — unusual for biology at the time.\n'
                         'Most biologists were not comfortable with this mathematical approach.\n'
                         '\n'
                         '3. NO KNOWN MECHANISM:\n'
                         "Mendel proposed 'heritable units' but had no idea what they were physically.\n"
                         'Chromosomes and DNA were not yet discovered — his model had no physical basis anyone could '
                         'verify.\n'
                         '\n'
                         '4. DARWIN CONNECTION:\n'
                         "Darwin's work on evolution was the dominant biological discussion of the era.\n"
                         "Mendel's work was not connected to evolution at the time.\n"
                         '\n'
                         'REDISCOVERY (1900):\n'
                         "Three scientists — de Vries, Correns and von Tschermak — independently rediscovered Mendel's "
                         'ratios.\n'
                         "Chromosomes had been discovered by then → Mendel's 'units' could be explained as genes on "
                         'chromosomes.\n'
                         "Mendel's work was finally recognised and he is now called the 'Father of Genetics'.",
              'heading': 'Why Mendel Was Not Accepted in His Lifetime'},
             {'content': "The MODERN SYNTHESIS (1930s–1950s) united Mendel's genetics with Darwin's evolution and "
                         'chromosome biology.\n'
                         '\n'
                         'KEY CONNECTIONS:\n'
                         "Mendel's 'heritable units' = GENES (specific sequences of DNA on chromosomes).\n"
                         'Alternative versions of genes = ALLELES (different base sequences at the same locus).\n'
                         "Mendel's 'separation of units' = MEIOSIS (chromosomes separate into different gametes).\n"
                         'Dominant/recessive explained by: dominant allele codes for functional protein; recessive '
                         'allele often codes for non-functional version.\n'
                         '\n'
                         'WAY SCIENCE WORKS:\n'
                         "Mendel's story illustrates several key aspects of how science advances:\n"
                         '1. Good data can be overlooked if not communicated well.\n'
                         '2. Ideas need a physical mechanism to be fully accepted.\n'
                         "3. Discoveries can be 'ahead of their time' — no scientific framework to make sense of "
                         'them.\n'
                         '4. Independent replication (three scientists rediscovering the same ratios) strengthens '
                         'confidence.\n'
                         '5. Science is self-correcting — eventually the correct ideas are recognised.',
              'heading': 'Modern Genetics — Connecting Mendel and DNA'}],
  'title': 'Mendel and the Development of Genetics',
  'triple_only': "Mendel's work and the development of genetics (4.6.3.4) is biology-only. Covers the pea plant "
                 'experiments, the laws of inheritance, why Mendel was not accepted in his lifetime, and how modern '
                 "genetics connects Mendel's work to DNA and chromosomes.",
  'variables': []},
 {'common_mistake': 'Extinction is PERMANENT — a species cannot come back once all individuals are dead. The fossil '
                    'record being incomplete does NOT disprove evolution — it is expected and understandable given how '
                    'rare fossilisation is. Most organisms that ever lived left no fossil at all.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'fossils-extinction',
  'key_note': 'Fossils form by mineralisation, preservation in amber/ice/tar, or trace fossils. Record is incomplete '
              'because soft tissue rarely fossilises and conditions must be exact. Extinction = all individuals of '
              'species die — permanent. Causes: catastrophe, habitat loss, competition, disease, climate change, human '
              'activity.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Mineralisation',
                          'Hard parts replaced by minerals over millions of years as the organism is buried in '
                          'sediment'),
                         ('Amber preservation',
                          'Small organisms trapped in tree resin — perfectly preserved for millions of years'),
                         ('Trace fossil', 'Footprints, burrows or droppings preserved in rock — evidence of behaviour'),
                         ('Habitat destruction',
                          'Forests cleared, wetlands drained — species lose living space — extinction risk'),
                         ('Introduced species',
                          'New predator or competitor arrives in an ecosystem — native species may be outcompeted')],
               'title': 'Match the Fossil Type or Extinction Cause'},
  'quiz': [{'opts': [('Soft tissue decays quickly — it usually decomposes before mineralisation can occur', True),
                     ("Soft-bodied organisms don't have cells, so they cannot be fossilised", False),
                     ('Soft-bodied organisms only live in water — fossils only form on land', False),
                     ('Soft tissue is preserved perfectly but scientists cannot identify it', False)],
            'q': 'Why are soft-bodied organisms rarely found as fossils?',
            'wrong_explanations': {1: 'All living things have cells — soft-bodied organisms (jellyfish, worms etc.) '
                                      'are eukaryotes with normal cells.',
                                   2: 'Many fossils DO form in water and marine sediments — in fact, aquatic '
                                      'environments are often BETTER for fossilisation because rapid burial in '
                                      'sediment is more likely.',
                                   3: 'Soft tissue can be preserved in exceptional circumstances (amber, ice, peat '
                                      'bogs) — but in most cases it decays before preservation can occur.'}},
           {'opts': [('Human hunting and introduced species (rats and pigs eating eggs) — the dodo had no natural '
                      'predators and was not afraid of humans',
                      True),
                     ('A catastrophic volcanic eruption on Mauritius wiped out the entire population', False),
                     ('Climate change caused the fruit the dodo ate to disappear', False),
                     ('A deadly virus spread through the population before any could survive and develop immunity',
                      False)],
            'q': 'The dodo became extinct in the 17th century. What caused its extinction?',
            'wrong_explanations': {1: "No major volcanic eruption caused the dodo's extinction — it was a combination "
                                      'of human hunting and the introduction of invasive species.',
                                   2: 'Some habitat change occurred, but the primary drivers were hunting and invasive '
                                      'species, not climate-driven food loss.',
                                   3: 'While disease can cause extinction, the primary documented causes for the dodo '
                                      'are human hunting and introduced species.'}}],
  'rp': None,
  'spec': '4.6.5',
  'summary': 'Describe how fossils form and explain why species become extinct.',
  'theory': [{'content': 'A FOSSIL is the preserved remains or traces of an organism from the geological past.\n'
                         '\n'
                         'Fossils form in several ways:\n'
                         '\n'
                         'MINERALISATION:\n'
                         'An organism dies and is quickly buried by sediment (mud, sand).\n'
                         'Soft tissue decays, but hard parts (bones, teeth, shells) remain.\n'
                         'Over millions of years, minerals from the surrounding rock slowly replace the original '
                         'material.\n'
                         'Eventually all original material is replaced by rock → a fossil.\n'
                         '\n'
                         'PRESERVATION in extreme conditions:\n'
                         'AMBER — tree resin traps small organisms (insects, spiders) which are perfectly preserved.\n'
                         'ICE — frozen conditions preserve soft tissue (woolly mammoths found almost intact in '
                         'Siberia).\n'
                         'TAR PITS — organisms become trapped in natural asphalt and are preserved.\n'
                         'PEAT BOGS — acidic, anaerobic conditions preserve soft tissue (bog bodies found in northern '
                         'Europe).\n'
                         '\n'
                         'TRACE FOSSILS:\n'
                         'Footprints, burrows, bite marks or droppings preserved in rock.\n'
                         'Provide evidence of behaviour as well as body structure.',
              'heading': 'How Fossils Form'},
             {'content': 'The fossil record does not contain every organism that ever lived — it is significantly '
                         'INCOMPLETE.\n'
                         '\n'
                         'Reasons:\n'
                         'SOFT TISSUE rarely fossilises — decay is usually faster than mineralisation.\n'
                         'SMALL OR FRAGILE organisms are less likely to leave fossils.\n'
                         'CONDITIONS must be exactly right — rapid burial, appropriate chemistry, absence of '
                         'scavengers.\n'
                         'FOSSILS may be DESTROYED by geological processes — volcanic activity, erosion, subduction.\n'
                         "FOSSILS are simply not yet found — much of the Earth's rock has not been excavated.\n"
                         '\n'
                         'Despite being incomplete, the fossil record is remarkably consistent with evolution — older '
                         'fossils are simpler, newer fossils are more complex, and transitional forms have been found.',
              'heading': 'Why the Fossil Record is Incomplete'},
             {'content': 'EXTINCTION occurs when every individual member of a species dies — the species is gone '
                         'forever.\n'
                         '\n'
                         'Extinction is permanent — once a species is gone, it cannot return.\n'
                         '\n'
                         'Causes of extinction:\n'
                         'CATASTROPHIC EVENTS — e.g. asteroid impact (linked to mass extinction of dinosaurs ~66 '
                         'million years ago), volcanic eruptions producing climate change.\n'
                         'HABITAT DESTRUCTION — deforestation, draining of wetlands, urbanisation → species lose their '
                         'living space.\n'
                         'NEW COMPETITORS or PREDATORS — introduced species outcompeting or preying on native '
                         'species.\n'
                         'NEW DISEASES — disease spreading through a population with no natural immunity.\n'
                         'CLIMATE CHANGE — rapid shifts in temperature or rainfall patterns that species cannot adapt '
                         'to quickly enough.\n'
                         'OVERHUNTING/OVERFISHING — human hunting reducing populations below viable levels (e.g. dodo, '
                         'passenger pigeon, woolly mammoth — possibly).\n'
                         '\n'
                         'Current extinction crisis:\n'
                         'Scientists estimate we are currently experiencing a mass extinction event caused primarily '
                         'by human activity — habitat destruction, climate change, pollution and overexploitation.',
              'heading': 'Extinction'}],
  'title': 'Fossils and Extinction',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Antibiotics do NOT CAUSE mutations — they SELECT resistant bacteria that already exist. The '
                    'mutation happened randomly, long before the antibiotic was used. The antibiotic is the selection '
                    'pressure that determines which bacteria survive. This is a key distinction — evolution acts on '
                    "existing variation, it doesn't create new variation in response to need.",
  'equations': [],
  'fifas': [],
  'higher': 'MRSA developed resistance through natural selection in hospital environments where antibiotics are '
            'heavily used. Strategies to manage resistance: prescribe only when necessary, complete courses, reduce '
            'agricultural use, develop new antibiotics, explore alternative therapies (bacteriophage therapy — viruses '
            'that infect bacteria). Students should be able to explain why resistance is evolutionarily inevitable if '
            'antibiotics are overused — resistant variants will always be selected for.',
  'id': 'resistant-bacteria',
  'key_note': 'Resistance develops by natural selection: random resistance mutation exists → antibiotic kills '
              'non-resistant bacteria → resistant bacteria survive and reproduce → resistance spreads. Antibiotics '
              "select for resistance — they don't cause it. MRSA = serious hospital-acquired resistant bacterium.",
  'matching': {'instruction': 'Put the steps of antibiotic resistance development in order by matching each step.',
               'pairs': [('Step 1 — Variation',
                          'A random mutation gives one bacterium resistance to an antibiotic — before any antibiotic '
                          'is used'),
                         ('Step 2 — Selection pressure',
                          'Antibiotic is used — kills all non-resistant bacteria, resistant one survives'),
                         ('Step 3 — Reproduction',
                          'Resistant bacterium reproduces — passing resistance gene to millions of offspring'),
                         ('Step 4 — Population change',
                          'Resistant bacteria dominate the population — the antibiotic no longer works')],
               'title': 'Steps in Developing Antibiotic Resistance'},
  'quiz': [{'opts': [('A random mutation gives some bacteria resistance — antibiotics kill non-resistant bacteria but '
                      'resistant ones survive and reproduce',
                      True),
                     ('Bacteria deliberately mutate themselves when exposed to antibiotics to survive', False),
                     ('Antibiotics cause the mutation that produces resistance in bacteria', False),
                     ('Resistant bacteria migrate from other areas after non-resistant bacteria are killed', False)],
            'q': 'How does antibiotic resistance develop in bacteria?',
            'wrong_explanations': {1: 'Bacteria cannot deliberately change their DNA — mutations are RANDOM and '
                                      'SPONTANEOUS. Bacteria cannot respond to threats by choosing to mutate.',
                                   2: 'Antibiotics are the SELECTION PRESSURE — they select pre-existing resistant '
                                      'variants. They do not cause the mutations that produce resistance.',
                                   3: 'Migration can spread resistance — but the PRIMARY mechanism of resistance '
                                      'developing in a population is natural selection of pre-existing resistant '
                                      'mutants.'}},
           {'opts': [('Stopping early leaves the most resistant bacteria alive — they survive to reproduce and pass on '
                      'resistance genes',
                      True),
                     ('The remaining antibiotics are needed to prevent the infection returning to full strength',
                      False),
                     ('Unfinished antibiotics are wasted medicine that could have been used by others', False),
                     ('Stopping early makes the side effects of antibiotics worse', False)],
            'q': 'Why is it important to complete a full course of antibiotics even if you feel better?',
            'wrong_explanations': {1: 'Infections can return if bacteria are not fully cleared — but the MORE '
                                      'IMPORTANT reason in terms of antibiotic resistance is that the survivors of '
                                      'partial treatment are the most resistant bacteria.',
                                   2: 'While waste is a concern, the primary medical reason is resistance selection — '
                                      'the survivors of an incomplete course are more likely to be resistant.',
                                   3: 'Side effects are not affected by course completion — the resistance argument is '
                                      'the primary public health reason.'}},
           {'opts': [('Through natural selection — repeated antibiotic use in hospitals selected for bacteria with '
                      'resistance mutations, which then multiplied',
                      True),
                     ('MRSA was deliberately engineered in a laboratory as a biological weapon', False),
                     ('MRSA infected humans from animals and naturally carries more mutations than other bacteria',
                      False),
                     ('Hospital cleaning products cause bacteria to mutate and become resistant', False)],
            'q': 'MRSA is resistant to many antibiotics. How did this resistance arise?',
            'wrong_explanations': {1: 'MRSA arose naturally through the evolutionary process of natural selection — '
                                      'not deliberate engineering.',
                                   2: 'Staphylococcus aureus is primarily a human pathogen — while zoonotic '
                                      "transmission does occur, MRSA's resistance arose through natural selection in "
                                      'hospital environments.',
                                   3: 'Cleaning products can select for resistance to disinfectants — but antibiotic '
                                      'resistance specifically arises from exposure to antibiotics, not cleaning '
                                      'agents.'}}],
  'rp': None,
  'spec': '4.6.5',
  'summary': 'Explain how antibiotic resistance develops through natural selection and why it is a global health '
             'threat.',
  'theory': [{'content': 'Antibiotic resistance is a direct example of EVOLUTION BY NATURAL SELECTION occurring in our '
                         'lifetimes.\n'
                         '\n'
                         'The process:\n'
                         '1. VARIATION — within a population of bacteria, individuals vary slightly due to random '
                         'mutations. A very small number may have a mutation that gives RESISTANCE to a particular '
                         'antibiotic.\n'
                         '2. SELECTION PRESSURE — when antibiotics are used, they KILL bacteria that are NOT '
                         'resistant. The resistant bacteria SURVIVE.\n'
                         '3. REPRODUCTION — resistant bacteria reproduce (bacteria can double every 20 minutes). They '
                         'pass on the resistance gene to offspring.\n'
                         '4. SPREAD — resistant bacteria become increasingly common in the population. The antibiotic '
                         'no longer works.\n'
                         '\n'
                         'This is natural selection in real time — the antibiotic acts as the selection pressure. The '
                         "resistant mutation existed BEFORE the antibiotic was used — the antibiotic didn't create the "
                         'mutation, it selected for it.',
              'heading': 'How Antibiotic Resistance Develops'},
             {'content': 'MRSA (Methicillin-resistant Staphylococcus aureus) is a bacterium that has developed '
                         'resistance to many commonly used antibiotics.\n'
                         '\n'
                         'Staphylococcus aureus is normally a relatively harmless skin bacterium found on about 30% of '
                         'people.\n'
                         '\n'
                         'MRSA has acquired resistance through repeated exposure to antibiotics — particularly in '
                         'hospital settings where antibiotics are widely used.\n'
                         '\n'
                         'Why MRSA is dangerous:\n'
                         "Difficult to treat — standard antibiotics don't work.\n"
                         'Can cause serious infections: bloodstream infections (sepsis), pneumonia, wound infections.\n'
                         'Particularly dangerous for hospital patients who are already weakened or have wounds.\n'
                         'Few effective antibiotics remain — some strains are resistant to almost everything.\n'
                         '\n'
                         'MRSA shows what can happen when antibiotic resistance goes unchecked — a common bacterium '
                         'becomes a serious, life-threatening pathogen.',
              'heading': 'MRSA — A Serious Example'},
             {'content': 'Antibiotic resistance is one of the greatest threats to global health, food security and '
                         'development — according to the World Health Organisation.\n'
                         '\n'
                         'The problem is accelerating because:\n'
                         'OVER-PRESCRIPTION — antibiotics given for viral infections (where they have no effect) or '
                         "'just in case'.\n"
                         'INCOMPLETE COURSES — stopping antibiotics early leaves the most resistant bacteria alive to '
                         'reproduce.\n'
                         'AGRICULTURAL USE — antibiotics widely used in livestock farming to prevent disease and '
                         'promote growth → resistant bacteria enter food chains.\n'
                         'GLOBAL SPREAD — resistant bacteria travel with people internationally.\n'
                         'SLOW DEVELOPMENT of new antibiotics — pharmaceutical companies have reduced investment '
                         'because new antibiotics are not as profitable as drugs for chronic diseases.\n'
                         '\n'
                         'What can be done:\n'
                         'Prescribe antibiotics ONLY when necessary.\n'
                         'Patients must COMPLETE FULL COURSES.\n'
                         'Develop NEW antibiotics and alternative treatments (e.g. phage therapy — using viruses that '
                         'kill bacteria).\n'
                         'Reduce agricultural antibiotic use.\n'
                         'Better hygiene to prevent spread of resistant bacteria.',
              'heading': 'Why Antibiotic Resistance is a Global Crisis'}],
  'title': 'Resistant Bacteria',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'A species is defined by the ability to interbreed and produce FERTILE offspring — not just by '
                    'looking similar. Horses and donkeys can breed but produce sterile mules → they are different '
                    'species. The three-domain system has Archaea as a SEPARATE domain from Bacteria — they are not '
                    'the same despite both being prokaryotes.',
  'equations': [],
  'fifas': [],
  'higher': 'Explain how molecular evidence (rRNA sequences, DNA base sequences, amino acid sequences) has revised '
            'traditional morphology-based classification. Interpret evolutionary trees built from molecular data and '
            "explain why Woese's three-domain system replaced the five-kingdom system. Evaluate the impact of new "
            'molecular data on classification — explain that classification systems are working hypotheses, revised as '
            'evidence changes.',
  'id': 'classification-living-organisms',
  'key_note': 'Linnaeus: binomial naming (Genus species), Kingdom→Phylum→Class→Order→Family→Genus→Species. '
              'Three-domain system (Woese): Archaea, Bacteria, Eukarya — based on rRNA. Archaea more related to '
              'Eukaryotes than Bacteria. Evolutionary trees: nodes = common ancestors; molecular evidence now used '
              'alongside morphology.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Binomial name', 'Two-part Latin name: Genus species — e.g. Homo sapiens'),
                         ('Species', 'Organisms that can interbreed and produce fertile offspring'),
                         ('Three-domain system', 'Archaea, Bacteria, Eukarya — based on rRNA sequences (Woese, 1977)'),
                         ('Node on evolutionary tree',
                          'Represents a common ancestor from which two lineages diverged')],
               'title': 'Classification Concepts'},
  'quiz': [{'opts': [('rRNA sequence analysis showed Archaea are more closely related to Eukaryotes than to Bacteria — '
                      'despite appearing similar to bacteria under a microscope',
                      True),
                     ('The five-kingdom system had too many organisms — three domains is simpler to use', False),
                     ('Woese discovered a new type of organism that did not fit into any of the five kingdoms', False),
                     ('DNA evidence showed all five kingdoms were actually the same evolutionary group', False)],
            'q': "Why did Carl Woese's three-domain system replace the five-kingdom classification?",
            'wrong_explanations': {1: 'Simplicity was not the reason — the three-domain system is based on MOLECULAR '
                                      'EVIDENCE showing fundamental differences in RNA sequences between Archaea and '
                                      'Bacteria.',
                                   2: 'Archaea were already known — but rRNA sequencing revealed they were '
                                      'fundamentally different from bacteria at the molecular level despite looking '
                                      'similar.',
                                   3: 'DNA evidence shows the five kingdoms are related but distinct — the change was '
                                      'specifically about separating Archaea from Bacteria based on molecular '
                                      'differences.'}},
           {'opts': [('The first two species are more closely related — they diverged from a common ancestor more '
                      'recently',
                      True),
                     ('The first two species are less related — a recent ancestor means they have had less time to '
                      'evolve together',
                      False),
                     ('Both pairs are equally related — all organisms share a common ancestor eventually', False),
                     ('The species with the older common ancestor is more evolved — older means more advanced', False)],
            'q': 'Two species share a more recent common ancestor on an evolutionary tree than two other species. What '
                 'does this indicate?',
            'wrong_explanations': {1: 'More RECENT common ancestor = LESS evolutionary time since divergence = MORE '
                                      'closely related. More ancient ancestor = longer time apart = more distantly '
                                      'related.',
                                   2: 'All organisms do share ancient common ancestors, but sharing a MORE RECENT one '
                                      'indicates a CLOSER relationship — fewer differences have accumulated since '
                                      'divergence.',
                                   3: 'More evolved does not mean more advanced — evolution has no direction or goal. '
                                      'Having an older common ancestor simply means the lineages have been separate '
                                      'longer.'}}],
  'rp': None,
  'spec': '4.6.5',
  'summary': 'Describe the Linnaean classification system and the three-domain system, and explain how evolutionary '
             'trees show relationships.',
  'theory': [{'content': 'CLASSIFICATION is the organisation of living things into groups based on their similarities '
                         'and differences.\n'
                         '\n'
                         'CARLUS LINNAEUS (18th century) developed the binomial system of naming organisms:\n'
                         'Every organism has a two-part Latin name:\n'
                         '1. GENUS (capitalised) — a group of closely related species\n'
                         '2. SPECIES (lowercase) — organisms of the same species can interbreed to produce fertile '
                         'offspring\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Homo sapiens — genus Homo, species sapiens (modern humans)\n'
                         'Felis catus — domestic cat\n'
                         'Panthera leo — lion\n'
                         '\n'
                         'HIERARCHY OF GROUPS (largest to smallest):\n'
                         'Kingdom → Phylum → Class → Order → Family → Genus → Species\n'
                         "Memory: 'King Philip Came Over For Good Soup'\n"
                         '\n'
                         'TRADITIONAL KINGDOMS:\n'
                         'Animalia, Plantae, Fungi, Protista, Prokaryota (bacteria)',
              'heading': 'The Linnaean Classification System'},
             {'content': 'CARL WOESE proposed the THREE-DOMAIN SYSTEM in 1977 based on analysis of ribosomal RNA '
                         '(rRNA).\n'
                         '\n'
                         'This replaced the five-kingdom system with three domains:\n'
                         '\n'
                         '1. ARCHAEA — primitive prokaryotes, often found in extreme environments (hot springs, salt '
                         'lakes).\n'
                         'DNA differs significantly from bacteria despite looking similar under a microscope.\n'
                         '\n'
                         '2. BACTERIA — true bacteria, the most numerous organisms on Earth.\n'
                         'Cells without membrane-bound nuclei; different cell wall chemistry from Archaea.\n'
                         '\n'
                         '3. EUKARYA — all organisms with membrane-bound nuclei.\n'
                         'Includes all animals, plants, fungi, and protists.\n'
                         '\n'
                         'WHY THREE DOMAINS?\n'
                         'RNA sequencing showed Archaea are more closely related to Eukaryotes than to Bacteria — '
                         'despite looking like bacteria under the microscope.\n'
                         'This illustrates that observable characteristics can be misleading — molecular evidence is '
                         'more reliable.',
              'heading': 'The Three-Domain System'},
             {'content': 'EVOLUTIONARY TREES (phylogenetic trees) show the evolutionary relationships between '
                         'organisms.\n'
                         '\n'
                         'How to read an evolutionary tree:\n'
                         'Branching points (NODES) = common ancestors.\n'
                         'The LENGTH of branches may represent evolutionary time.\n'
                         'Organisms that share a more RECENT common ancestor are more closely related.\n'
                         '\n'
                         'EVIDENCE used to build evolutionary trees:\n'
                         'Anatomical similarities — homologous structures.\n'
                         'Fossil record — order of appearance of species.\n'
                         'DNA and RNA sequences — the more similar the sequences, the more closely related.\n'
                         'Protein similarities — amino acid sequences in key proteins (e.g. cytochrome c).\n'
                         '\n'
                         'IMPORTANCE:\n'
                         'Evolutionary trees help us understand how species are related.\n'
                         'Can identify the most likely common ancestor of a group.\n'
                         'Help in medicine — understanding which organisms are closely related to pathogens.\n'
                         '\n'
                         'LINNAEAN vs EVOLUTIONARY:\n'
                         'Linnaeus classified by appearance/structure (morphology).\n'
                         'Modern classification uses both morphology AND molecular evidence (DNA, RNA).\n'
                         'Molecular evidence has revised some traditional classifications.',
              'heading': 'Evolutionary Trees'}],
  'title': 'Classification of Living Organisms',
  'triple_only': 'Classification of living organisms (4.6.5) is biology-only — not in Combined Science. Covers '
                 'Linnaean classification, the three-domain system (Archaea, Bacteria, Eukarya), and evolutionary '
                 'trees as evidence for relationships between organisms.',
  'variables': []}],

"ecology": [{'common_mistake': 'Students often confuse COMMUNITY and ECOSYSTEM. A community is all the LIVING ORGANISMS in an '
                    'area. An ecosystem includes the community PLUS all the non-living (abiotic) factors. Remember: '
                    'Ecosystem = Community + Abiotic environment.',
  'equations': [],
  'fifas': [],
  'higher': 'Students should be able to explain how changes to abiotic and biotic factors affect communities, using '
            'data as evidence. Stable communities have balanced interactions — changes to one component ripple through '
            'the whole system. The concept of the ecosystem as a self-sustaining unit with inputs (sunlight, inorganic '
            'nutrients) and outputs (heat, waste) is important for understanding sustainability.',
  'id': 'ecosystems',
  'key_note': 'Organism → Population (one species) → Community (all species) → Ecosystem (community + abiotic '
              'factors). All species are interdependent — changes to one affect others (cascade effect). Stable '
              'community = populations roughly constant over time.',
  'matching': {'instruction': 'Match each term to its correct definition.',
               'pairs': [('Population', 'All individuals of ONE species in a given area'),
                         ('Community', 'ALL populations of different species living together in the same area'),
                         ('Ecosystem', 'Community PLUS all the non-living (abiotic) factors in the same area'),
                         ('Habitat', 'The specific place where an organism lives'),
                         ('Interdependence', 'All species in a community depend on each other directly or indirectly')],
               'title': 'Match the Ecology Term'},
  'quiz': [{'opts': [('A community is all the living organisms in an area. An ecosystem is the community PLUS all the '
                      'non-living (abiotic) factors.',
                      True),
                     ('A community is larger than an ecosystem — it includes several ecosystems.', False),
                     ('They are the same thing — both describe all organisms in an area.', False),
                     ('An ecosystem only includes animals. A community includes all living things.', False)],
            'q': 'What is the difference between a community and an ecosystem?',
            'wrong_explanations': {1: 'An ECOSYSTEM is larger — it includes the community PLUS all abiotic factors. A '
                                      'community is just the living part.',
                                   2: 'They are NOT the same — a community is the living component only. An ecosystem '
                                      'adds the non-living environment.',
                                   3: 'An ecosystem includes ALL living organisms (animals, plants, fungi, '
                                      'microorganisms) plus abiotic factors — not just animals.'}},
           {'opts': [('Deer population increases — deer overgraze vegetation — plant diversity declines — other '
                      'animals that depend on those plants also decline',
                      True),
                     ('The ecosystem immediately collapses — all species die without wolves', False),
                     ('Other predators increase in number to compensate for the wolves', False),
                     ('Nothing changes — deer populations regulate themselves', False)],
            'q': 'Wolves are removed from a woodland ecosystem. What is the most likely consequence?',
            'wrong_explanations': {1: 'Ecosystems rarely collapse immediately — they often shift to a new, less '
                                      'diverse stable state. But the cascade of effects described is accurate.',
                                   2: 'Some compensation by other predators may occur — but wolves are often keystone '
                                      'predators, so full compensation is rare.',
                                   3: 'Without predators, prey populations often grow beyond what the habitat can '
                                      'support — leading to overgrazing and eventual population crash.'}},
           {'opts': [('They are dominated by one or a few crop species — most other species are excluded or removed',
                      True),
                     ('Artificial ecosystems are physically smaller than natural ones', False),
                     ('Artificial ecosystems have less sunlight because they are sheltered', False),
                     ('Animals avoid artificial ecosystems because they can detect human presence', False)],
            'q': 'Why do artificial ecosystems (like farmland) tend to have lower biodiversity than natural '
                 'ecosystems?',
            'wrong_explanations': {1: 'Some farms are physically large — size is not the primary reason. MONOCULTURE '
                                      "(one crop species) and removal of 'weeds' and 'pests' dramatically reduces "
                                      'biodiversity.',
                                   2: 'Farmland typically receives as much sunlight as natural ecosystems — light is '
                                      'not the reason for lower biodiversity.',
                                   3: 'Many animals do live on farmland — but the monoculture crop structure and use '
                                      'of pesticides/herbicides removes habitat and food for most species.'}}],
  'rp': None,
  'spec': '4.7.1',
  'summary': 'Define ecosystem, population, community and habitat, and explain how organisms depend on each other.',
  'theory': [{'content': 'Ecology is the study of how organisms interact with each other and with their environment.\n'
                         '\n'
                         'ORGANISM — an individual living thing (e.g. one robin, one oak tree, one earthworm).\n'
                         '\n'
                         'POPULATION — all the individuals of ONE SPECIES living in the same area at the same time '
                         '(e.g. all the robins in a woodland).\n'
                         '\n'
                         'COMMUNITY — all the populations of DIFFERENT SPECIES living together in the same area (e.g. '
                         'all the animals, plants, fungi and microorganisms in a woodland).\n'
                         '\n'
                         'HABITAT — the specific place where an organism lives within an ecosystem (e.g. the woodland '
                         'floor, the canopy, a particular pond).\n'
                         '\n'
                         'ECOSYSTEM — a community of organisms PLUS all the non-living (abiotic) factors in the same '
                         'area. An ecosystem includes everything — living and non-living — in a defined area.',
              'heading': 'Key Ecology Terms'},
             {'content': 'All species within a community are INTERDEPENDENT — they depend on each other directly or '
                         'indirectly for their survival.\n'
                         '\n'
                         'If one species changes significantly, it affects others — sometimes the effects ripple '
                         'through the whole ecosystem (called a CASCADE EFFECT).\n'
                         '\n'
                         'Examples of interdependence:\n'
                         'Plants depend on bees for POLLINATION — without bees, many plants cannot reproduce.\n'
                         'Bees depend on flowering plants for NECTAR and POLLEN — their food source.\n'
                         'Shrews depend on earthworms for food.\n'
                         'Earthworms depend on leaf litter (decomposing plant material) for food.\n'
                         'Deer depend on grass and shrubs for food.\n'
                         'Wolves depend on deer as prey.\n'
                         'If wolves are removed → deer population explodes → vegetation is overgrazed → many plant '
                         'species decline → animals that depend on those plants also decline.\n'
                         '\n'
                         'A STABLE COMMUNITY is one where populations remain roughly constant over time — because the '
                         'various checks and balances (predation, competition, disease) keep each population within '
                         'its range.',
              'heading': 'Interdependence in Ecosystems'},
             {'content': 'Ecosystems exist at many scales and in many environments.\n'
                         '\n'
                         'NATURAL ECOSYSTEMS include: tropical rainforests, coral reefs, temperate woodlands, '
                         'grasslands, deserts, tundra, deep ocean.\n'
                         '\n'
                         'ARTIFICIAL ECOSYSTEMS created by humans include: farmland (agricultural fields), fish farms, '
                         'ornamental gardens, nature reserves.\n'
                         '\n'
                         'Artificial ecosystems tend to have LOWER BIODIVERSITY than natural ones — they are often '
                         'dominated by one or a few species (monocultures).\n'
                         '\n'
                         'Different ecosystems are characterised by their specific:\n'
                         'ABIOTIC CONDITIONS (temperature, rainfall, light levels, soil type).\n'
                         'BIOTIC FACTORS (which species live there, what eats what).\n'
                         'LEVEL OF PRODUCTIVITY (how much energy is fixed by plants).',
              'heading': 'Types of Ecosystem'}],
  'title': 'Ecosystems',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Students often list only one or two abiotic factors and forget others. The full list includes: '
                    'temperature, light intensity, water availability, soil pH, soil mineral content, wind speed, CO₂ '
                    'concentration and O₂ concentration. In exams, be specific about which factor and exactly HOW it '
                    'affects the organism.',
  'equations': [],
  'fifas': [],
  'higher': 'Indicator species are used to assess environmental quality: lichens indicate clean air (absent where SO₂ '
            'levels are high); mayfly larvae indicate clean, well-oxygenated water; bloodworms tolerate moderate '
            'pollution; rat-tailed maggots tolerate severe pollution. Students should be able to interpret data about '
            'indicator species distributions and draw conclusions about environmental quality.',
  'id': 'abiotic-biotic-factors',
  'key_note': 'Abiotic = non-living: temperature, light, water, pH, minerals, wind, CO₂, O₂. Biotic = living: '
              'predation, competition, disease, food availability, parasitism. Both affect distribution (where '
              'organisms live) and abundance (how many).',
  'matching': {'instruction': 'Sort each factor into abiotic (non-living) or biotic (living).',
               'pairs': [('Abiotic', 'Soil pH — affects which minerals are available for plant growth'),
                         ('Biotic', 'Predation — wolves hunting deer reduces deer population'),
                         ('Abiotic',
                          'Light intensity — determines which plant species can photosynthesise in that location'),
                         ('Biotic', 'Competition for food between red and grey squirrels'),
                         ('Abiotic', 'O₂ concentration in a river — affects which aquatic organisms can survive'),
                         ('Biotic', 'Disease — myxomatosis dramatically reduced the UK rabbit population')],
               'title': 'Abiotic or Biotic Factor?'},
  'quiz': [{'opts': [('O₂ concentration — a non-living chemical factor that affects aquatic organisms', True),
                     ('Fish population — the fish that die because of low oxygen', False),
                     ('Disease — bacteria cause the oxygen to fall', False),
                     ('Competition — fish compete for the remaining oxygen', False)],
            'q': 'A river becomes polluted and oxygen levels fall. Which of the following is an abiotic factor that '
                 'has changed?',
            'wrong_explanations': {1: 'Fish population = a BIOTIC factor — it is a living component. The O₂ level is '
                                      'the abiotic factor that changed.',
                                   2: 'Disease is a BIOTIC factor — caused by living pathogens. O₂ concentration is '
                                      'abiotic (a chemical feature of the water).',
                                   3: 'Competition is a BIOTIC factor between living organisms. The O₂ level itself is '
                                      'the abiotic factor.'}},
           {'opts': [('Biotic — interspecific competition between two different species for food and habitat', True),
                     ('Abiotic — grey squirrels changed the temperature of the habitat', False),
                     ('Biotic — intraspecific competition between individuals of the same species', False),
                     ('Abiotic — grey squirrels are larger so they change the physical environment', False)],
            'q': 'Grey squirrels were introduced to the UK and have outcompeted red squirrels. What type of factor is '
                 'this?',
            'wrong_explanations': {1: "Grey squirrels don't change temperature — their effect is through direct "
                                      'competition for food and habitat, which is a biotic factor.',
                                   2: 'INTRASPECIFIC competition = same species. Red vs grey = TWO DIFFERENT SPECIES = '
                                      'INTERSPECIFIC competition.',
                                   3: 'Grey squirrels being larger is a physical trait — their impact on red squirrels '
                                      'is through competition for resources (a biotic factor).'}}],
  'rp': None,
  'spec': '4.7.1',
  'summary': 'Describe the abiotic and biotic factors that affect the distribution and abundance of organisms.',
  'theory': [{'content': 'ABIOTIC FACTORS are non-living physical and chemical features of the environment that affect '
                         'organisms.\n'
                         '\n'
                         'Key abiotic factors:\n'
                         '\n'
                         'TEMPERATURE — affects enzyme activity and metabolic rate. Each species has a temperature '
                         'range it can tolerate. Cold-blooded organisms are most affected.\n'
                         '\n'
                         'LIGHT INTENSITY — essential for plants (photosynthesis). Affects which plants can grow in '
                         'different areas (e.g. shade-tolerant vs sun-loving species). Also affects animal behaviour '
                         '(nocturnal vs diurnal).\n'
                         '\n'
                         'WATER AVAILABILITY (rainfall) — water is essential for all life. Desert species are adapted '
                         'to low water; wetland species need abundant water.\n'
                         '\n'
                         'SOIL pH — affects which minerals are available and which organisms can live in the soil. '
                         'Some plants prefer acidic soils (heather, rhododendrons); others prefer alkaline (nettles, '
                         'ash trees).\n'
                         '\n'
                         'SOIL MINERAL CONTENT — nitrates, phosphates and other minerals are essential for plant '
                         'growth. Poor soils support fewer plant species.\n'
                         '\n'
                         'WIND SPEED — affects water loss from plants and animals, wave action in marine environments, '
                         'seed dispersal.\n'
                         '\n'
                         'CO₂ CONCENTRATION — limits photosynthesis rate. In greenhouses, elevated CO₂ increases plant '
                         'growth.\n'
                         '\n'
                         'O₂ CONCENTRATION — affects aquatic organisms. Low oxygen in water (e.g. due to algal blooms '
                         'and decomposition) kills fish and invertebrates.',
              'heading': 'Abiotic Factors — Non-living'},
             {'content': 'BIOTIC FACTORS are the effects of other living organisms on an individual.\n'
                         '\n'
                         'Key biotic factors:\n'
                         '\n'
                         'FOOD AVAILABILITY — if food (prey, plant material) becomes scarce, consumer populations '
                         'decline.\n'
                         '\n'
                         'PREDATION — predators control prey populations. If predator numbers rise → prey decline. If '
                         'prey decline → predator declines too (lagged response).\n'
                         '\n'
                         'COMPETITION — organisms compete for limited resources:\n'
                         'INTERSPECIFIC competition — between different species (e.g. red squirrels vs grey squirrels '
                         'competing for food and habitat).\n'
                         'INTRASPECIFIC competition — between individuals of the SAME species (most intense as they '
                         'have identical needs).\n'
                         '\n'
                         'DISEASE — pathogens can rapidly reduce population numbers (e.g. myxomatosis in rabbits, '
                         'Dutch elm disease in elm trees).\n'
                         '\n'
                         'PARASITISM — parasites harm the host organism (e.g. fleas, tapeworms, mistletoe on trees).\n'
                         '\n'
                         'POLLINATION — many plants depend on specific pollinators (bees, butterflies). Decline of '
                         'pollinators can devastate plant populations.\n'
                         '\n'
                         'SEED DISPERSAL — many plants depend on animals to disperse their seeds.',
              'heading': 'Biotic Factors — Living'},
             {'content': 'The distribution of organisms — where they live — is determined by a combination of abiotic '
                         'and biotic factors.\n'
                         '\n'
                         'Example 1 — Zonation on a rocky shore:\n'
                         'Most exposed area (top): only very hardy organisms (limpets, lichens) — extreme desiccation, '
                         'wave action, temperature fluctuation.\n'
                         'Lower zones: progressively more species as conditions become more stable.\n'
                         'Always submerged: richest community — stable temperature and water availability.\n'
                         '\n'
                         'Example 2 — Effect of pH on freshwater invertebrates:\n'
                         'Mayfly larvae are sensitive to acid — absent from acidic streams.\n'
                         'Bloodsucking leeches can tolerate moderate pollution.\n'
                         'Rat-tailed maggots can tolerate very poor water quality.\n'
                         'Used as INDICATOR SPECIES — their presence or absence indicates environmental conditions.\n'
                         '\n'
                         'Example 3 — Light and woodland plant distribution:\n'
                         'Sunlit clearings: grasses, foxgloves, brambles (high light demand).\n'
                         'Deep shade under canopy: shade-tolerant species only (ivy, mosses).\n'
                         'Woodland edge: a mix — transition zone.',
              'heading': 'How Factors Affect Distribution'}],
  'title': 'Abiotic and Biotic Factors',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Adaptations are NOT something an organism CHOOSES or deliberately develops. Organisms cannot '
                    'decide to grow a thicker coat because it is cold — adaptations arise through natural selection '
                    'over many generations. A single organism cannot adapt during its lifetime through genetic change.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'adaptations',
  'key_note': 'Adaptations: structural (physical features), behavioural (what organism does), functional (internal '
              'processes). Arise through natural selection. Cold adaptations: small surface area, insulation. Desert '
              'adaptations: water conservation, large surface area for cooling.',
  'matching': {'instruction': 'Match each adaptation to its correct type.',
               'pairs': [('Structural', 'Thick blubber layer in seals — insulates against cold ocean water'),
                         ('Behavioural', 'Hibernation in bears — reduces energy need during cold winter months'),
                         ('Functional', 'Kangaroo rat producing very concentrated urine — conserves water in desert'),
                         ('Structural',
                          'Forward-facing eyes in owls — binocular vision for judging distance when hunting'),
                         ('Behavioural', 'Wildebeest migrating in large herds — safety in numbers from predators'),
                         ('Functional',
                          'Antifreeze proteins in the blood of Arctic fish — prevents blood from freezing')],
               'title': 'Structural, Behavioural or Functional?'},
  'quiz': [{'opts': [('Structural — physical features of the body that improve survival in cold environments', True),
                     ('Behavioural — things the bear does to stay warm', False),
                     ('Functional — internal processes that generate extra body heat', False),
                     ("Environmental — the environment shaped the bear's appearance directly", False)],
            'q': 'A polar bear has thick white fur and a layer of blubber. What type of adaptations are these?',
            'wrong_explanations': {1: 'Behavioural adaptations are things the organism DOES — e.g. hibernating or '
                                      'huddling. Fur and blubber are physical STRUCTURAL features.',
                                   2: 'Functional (physiological) adaptations are internal chemical processes — e.g. '
                                      'antifreeze proteins, concentrated urine production. Fur and blubber are '
                                      'physical structures.',
                                   3: 'The environment selects for adaptations through natural selection — but '
                                      'adaptations are features OF the organism, not caused directly by the '
                                      'environment.'}},
           {'opts': [('Large ears increase the surface area for heat loss — helping the animal cool down in the hot '
                      'desert',
                      True),
                     ('Large ears help the animal hear predators from further away in the flat desert', False),
                     ('Large ears store water for use during droughts', False),
                     ('Large ears are a warning signal to predators that the animal is dangerous', False)],
            'q': 'Why do desert animals like the fennec fox have very large ears?',
            'wrong_explanations': {1: 'Hearing is enhanced too — but the PRIMARY ecological reason for the fennec '
                                      "fox's extraordinarily large ears relative to body size is thermoregulation "
                                      '(heat loss). Other desert animals with large ears (jackrabbits) also use them '
                                      'for cooling.',
                                   2: "Ears don't store water — water is stored in fat (camels) or conserved through "
                                      'concentrated urine (kangaroo rats). The large ear surface area is for cooling.',
                                   3: 'Warning colouration (aposematism) typically involves bright colours — large '
                                      'plain ears in desert animals are not a warning signal.'}}],
  'rp': None,
  'spec': '4.7.2',
  'summary': 'Describe structural, behavioural and functional adaptations and explain how they help survival.',
  'theory': [{'content': 'An ADAPTATION is any feature of an organism that makes it better suited to its environment — '
                         'increasing its chances of survival and reproduction.\n'
                         '\n'
                         'Adaptations arise through NATURAL SELECTION — individuals with features better suited to '
                         'their environment survive longer and reproduce more, passing those features to offspring. '
                         'Over many generations, the adaptation becomes more common in the population.\n'
                         '\n'
                         'There are three types of adaptation:\n'
                         "1. STRUCTURAL — physical features of the organism's body.\n"
                         '2. BEHAVIOURAL — things the organism does.\n'
                         '3. FUNCTIONAL (physiological) — internal chemical or biological processes.',
              'heading': 'What Are Adaptations?'},
             {'content': 'ARCTIC AND COLD ENVIRONMENTS:\n'
                         'Thick fur or blubber (fat layer) — STRUCTURAL — insulates against heat loss.\n'
                         'White colouration (e.g. polar bears, Arctic foxes in winter) — STRUCTURAL — camouflage '
                         'against snow.\n'
                         'Small ears and limbs relative to body size — STRUCTURAL — reduces surface area to volume '
                         'ratio, minimising heat loss.\n'
                         'Hibernation — BEHAVIOURAL — reduces energy need during winter when food is scarce.\n'
                         'Antifreeze proteins in blood of Arctic fish — FUNCTIONAL — prevents blood freezing.\n'
                         '\n'
                         'DESERT ENVIRONMENTS:\n'
                         'Large ears (e.g. fennec fox, jackrabbit) — STRUCTURAL — increase surface area for heat '
                         'loss.\n'
                         'Pale colouration — STRUCTURAL — reflects sunlight, reduces heat absorption.\n'
                         'Nocturnal behaviour — BEHAVIOURAL — avoids the intense daytime heat, active at night when '
                         'cooler.\n'
                         'Cactus: thick, waxy stem stores water; reduced leaves (spines) reduce water loss — '
                         'STRUCTURAL.\n'
                         'Camel: humps store fat (not water) as energy reserve; can tolerate significant dehydration — '
                         'FUNCTIONAL.\n'
                         'Kangaroo rat: produces very concentrated urine to conserve water — FUNCTIONAL.\n'
                         '\n'
                         'DEEP SEA:\n'
                         'Bioluminescence — FUNCTIONAL — producing light to attract prey or communicate in total '
                         'darkness.\n'
                         'High pressure tolerance — FUNCTIONAL — specialised cell membranes and proteins.\n'
                         'Large eyes — STRUCTURAL — maximise light detection in dim conditions.',
              'heading': 'Adaptations to Extreme Environments'},
             {'content': "The ongoing evolutionary 'arms race' between predators and prey drives many of the most "
                         'striking adaptations.\n'
                         '\n'
                         'PREDATOR ADAPTATIONS:\n'
                         'Forward-facing eyes — STRUCTURAL — binocular vision allows accurate depth perception for '
                         'judging distance when striking.\n'
                         'Sharp claws and teeth — STRUCTURAL — for catching and killing prey.\n'
                         'Camouflage — STRUCTURAL — stalking prey without being seen.\n'
                         'Speed and agility — STRUCTURAL/FUNCTIONAL — for chasing prey.\n'
                         'Pack hunting behaviour — BEHAVIOURAL — cooperating to take down larger prey.\n'
                         '\n'
                         'PREY ADAPTATIONS:\n'
                         'Side-facing eyes — STRUCTURAL — wide field of vision to detect approaching predators.\n'
                         'Camouflage — STRUCTURAL — hiding from predators.\n'
                         'Warning colours (aposematism) — STRUCTURAL — bright colours warn predators of toxicity (e.g. '
                         'poison dart frogs, wasps).\n'
                         'Herd behaviour — BEHAVIOURAL — safety in numbers; harder to single out individuals.\n'
                         'Speed and agility — STRUCTURAL/FUNCTIONAL — fleeing from predators.\n'
                         'Mimicry — STRUCTURAL — harmless species mimic toxic ones (e.g. hoverflies mimic wasps).',
              'heading': 'Predator and Prey Adaptations'}],
  'title': 'Adaptations',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Arrows in food chains show the direction of ENERGY FLOW — from what is eaten to what eats it. So '
                    'the arrow goes FROM prey TO predator. Students often draw arrows the wrong way, showing what the '
                    'predator eats rather than which way energy flows. Also: PRODUCERS are PLANTS (photosynthetic) — '
                    "not all plants in a food chain are 'prey', they are the PRODUCERS.",
  'equations': [],
  'fifas': [],
  'higher': 'Pyramids of biomass show dry mass at each trophic level — always narrowing upward. Pyramids of number can '
            'be inverted (e.g. one oak tree → thousands of insects). Efficiency of energy transfer: efficiency (%) = '
            '(biomass transferred ÷ biomass available) × 100. Typically ~10% efficient. This means 90% of biomass is '
            'lost at each level as heat (respiration), undigested material (faeces), and uneaten portions.',
  'id': 'food-chains-webs',
  'key_note': 'Food chain: producer → primary → secondary → tertiary consumer. Arrows show direction of energy flow. '
              'Only ~10% of energy passes to each next level — rest lost as heat, waste, movement. Food web = many '
              'interconnected chains. More realistic.',
  'matching': {'instruction': 'Match each organism to its role in a food chain.',
               'pairs': [('Producer', 'Grass — makes its own food by photosynthesis'),
                         ('Primary consumer', 'Rabbit — eats the producer (grass)'),
                         ('Secondary consumer', 'Fox — eats the primary consumer (rabbit)'),
                         ('Tertiary consumer', 'Eagle — eats the secondary consumer (fox)'),
                         ('Decomposer', 'Bacteria and fungi — break down dead organisms at all levels')],
               'title': 'Match the Trophic Level'},
  'quiz': [{'opts': [('Energy is lost at each level — so little remains by the top level that it cannot support many '
                      'organisms',
                      True),
                     ('Top predators are too large to find enough food in most ecosystems', False),
                     ('Longer food chains would be too complex for organisms to navigate', False),
                     ('Producers cannot support more than 4 levels of consumers', False)],
            'q': 'Why do food chains rarely have more than 4–5 trophic levels?',
            'wrong_explanations': {1: 'Size can increase up a food chain, but the limiting factor is ENERGY, not size. '
                                      'Even small top predators need large amounts of food.',
                                   2: "Food chains are not 'navigated' by organisms — the limit is thermodynamic "
                                      '(energy loss), not cognitive.',
                                   3: 'Producers can support more levels in principle — the limit is the progressive '
                                      'loss of energy at each transfer, not some fixed rule about producers.'}},
           {'opts': [('Grass decreases — more rabbits eat more grass', True),
                     ('Grass increases — without foxes, more nutrients return to soil', False),
                     ('Grass is unaffected — plants are not part of the animal food web', False),
                     ('Grass increases — rabbits and grass have a mutualistic relationship', False)],
            'q': 'In a food web, the rabbit population suddenly increases due to a disease killing foxes. What happens '
                 'to the grass?',
            'wrong_explanations': {1: 'Fox death → reduced decomposition adds some nutrients, but the dominant effect '
                                      'is that MORE RABBITS eat MORE GRASS → grass DECREASES.',
                                   2: 'Plants ARE part of food webs — as producers. They are directly affected by '
                                      'herbivore (rabbit) population changes.',
                                   3: 'Rabbits eat grass — this is a consumer-producer relationship '
                                      '(predation/herbivory), not mutualism. Rabbits benefit; grass is harmed.'}}],
  'rp': None,
  'spec': '4.7.1',
  'summary': 'Describe food chains and webs, trophic levels and energy transfer between them.',
  'theory': [{'content': 'A FOOD CHAIN shows the FEEDING RELATIONSHIPS between organisms — who eats whom — and the '
                         'direction of energy flow.\n'
                         '\n'
                         'Arrows in a food chain show the direction of ENERGY TRANSFER (from food to the organism '
                         'eating it).\n'
                         '\n'
                         'Roles in a food chain:\n'
                         'PRODUCER — an organism that MAKES its own food using sunlight energy via PHOTOSYNTHESIS '
                         '(green plants and algae). All food chains start with a producer.\n'
                         'PRIMARY CONSUMER — eats the producer (usually a herbivore).\n'
                         'SECONDARY CONSUMER — eats the primary consumer.\n'
                         'TERTIARY CONSUMER — eats the secondary consumer (often a top predator).\n'
                         '\n'
                         'Example:\n'
                         'Grass → Rabbit → Fox → Eagle\n'
                         '(Producer) → (Primary) → (Secondary) → (Tertiary)\n'
                         '\n'
                         'Each feeding level is called a TROPHIC LEVEL.',
              'heading': 'Food Chains'},
             {'content': 'Energy enters food chains as SUNLIGHT — absorbed by producers during photosynthesis and '
                         'stored in glucose.\n'
                         '\n'
                         'At each trophic level, ENERGY IS LOST — only a fraction is transferred to the next level.\n'
                         '\n'
                         'Energy is lost because:\n'
                         'ORGANISMS USE ENERGY for movement, keeping warm, growth and reproduction — energy used in '
                         'RESPIRATION is released as HEAT and lost to the environment.\n'
                         'NOT ALL OF THE ORGANISM IS EATEN — bones, roots, shells and other parts may not be '
                         'consumed.\n'
                         'SOME MATERIAL is excreted as faeces and not digested.\n'
                         '\n'
                         'Typically only about 10% of energy at one trophic level passes to the next level.\n'
                         '\n'
                         'This means:\n'
                         'Producers have the most energy and biomass.\n'
                         'Each level up has less energy and biomass — and fewer organisms.\n'
                         'Food chains are rarely more than 4–5 levels long — by the top level, so little energy '
                         'remains that few organisms can survive.',
              'heading': 'Energy Transfer and Loss'},
             {'content': 'A FOOD WEB shows many INTERCONNECTED food chains within an ecosystem — a more realistic '
                         'picture of feeding relationships.\n'
                         '\n'
                         'In reality, most organisms eat more than one thing and are eaten by more than one thing.\n'
                         '\n'
                         'Food webs show:\n'
                         'Which organisms are predators and which are prey.\n'
                         'Which organisms are most at risk if a species is removed.\n'
                         'How changes in one population ripple through the ecosystem.\n'
                         '\n'
                         'WHAT HAPPENS WHEN A SPECIES IS REMOVED:\n'
                         'If a predator is removed → its prey increase → the things the prey eat may decrease.\n'
                         'If a prey species is removed → predators that depended on it may decline → other prey '
                         'species may increase.\n'
                         '\n'
                         'KEYSTONE SPECIES are species that have a disproportionately large effect on the ecosystem '
                         'relative to their numbers — removing them causes major ecosystem changes (e.g. wolves in '
                         'Yellowstone, sea otters in kelp forests).',
              'heading': 'Food Webs'}],
  'title': 'Food Chains and Food Webs',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'In predator-prey cycles, the PREDATOR population FOLLOWS the prey — with a time lag. Predator '
                    'numbers rise AFTER prey numbers rise (because it takes time to breed). Predator numbers fall '
                    'AFTER prey decline. Students often draw them rising and falling at the same time — they should be '
                    'slightly out of phase.',
  'equations': [],
  'fifas': [],
  'higher': 'Students should be able to interpret predator-prey population graphs — explaining the time lag between '
            'predator and prey peaks, and predicting the effects of changing one population on others in a food web. '
            'The carrying capacity is the maximum population that resources can sustain. Students should understand '
            'the concept of intraspecific competition as the primary density-dependent control on population size.',
  'id': 'population-competition',
  'key_note': 'Population limited by resources (food, water, space), predation and disease = carrying capacity. '
              'Predator-prey cycles are out of phase — predator follows prey with a lag. Intraspecific (same species) '
              'competition is most intense. Interspecific = between different species.',
  'matching': {'instruction': 'Match each term to its correct description.',
               'pairs': [('Carrying capacity', 'Maximum population size that a habitat can sustainably support'),
                         ('Intraspecific competition',
                          'Competition between individuals of the SAME species — most intense'),
                         ('Interspecific competition',
                          'Competition between individuals of DIFFERENT species for the same resource'),
                         ('Predator-prey cycle',
                          'Predator and prey populations fluctuate — predator follows prey with a time lag'),
                         ('Density-dependent factor',
                          'Becomes more limiting as population density increases — e.g. food shortage, disease')],
               'title': 'Match the Population Ecology Concept'},
  'quiz': [{'opts': [('There is a time lag — it takes time for predators to reproduce in response to increased food '
                      'availability',
                      True),
                     ('Predators eat the prey before they can reproduce, causing prey to peak first', False),
                     ('Prey always outnumber predators — so prey peaks are automatically earlier', False),
                     ('Predators migrate to different areas before their numbers can increase', False)],
            'q': 'In a predator-prey graph, the predator population peaks AFTER the prey population peaks. Why?',
            'wrong_explanations': {1: 'The lag is specifically about REPRODUCTION — it takes time for increased food '
                                      'to result in increased offspring. Predators eating prey actually reduces prey '
                                      'numbers.',
                                   2: 'Prey outnumbering predators is normal — but the timing of peaks is about '
                                      'reproduction lag, not relative numbers.',
                                   3: 'Migration can occur — but the time lag in predator-prey cycles is primarily a '
                                      'biological response time, not migration.'}},
           {'opts': [('Individuals of the same species have identical needs — they compete for exactly the same '
                      'resources',
                      True),
                     ('Individuals of the same species are physically stronger and dominate others', False),
                     ('Intraspecific competition involves more individuals — so it is more intense by numbers', False),
                     ('Different species never compete — they always occupy different niches', False)],
            'q': 'Why is intraspecific competition more intense than interspecific competition?',
            'wrong_explanations': {1: 'Physical strength varies within a species — the intensity of competition is '
                                      'about OVERLAP OF RESOURCE NEEDS, not strength.',
                                   2: 'Many species are common — but interspecific competition can also involve large '
                                      'numbers. The intensity difference is about the degree of resource overlap.',
                                   3: 'Different species CAN compete — grey and red squirrels are a clear UK example. '
                                      'The ecological niche concept says species that overlap too much cannot coexist '
                                      'indefinitely.'}}],
  'rp': None,
  'spec': '4.7.1',
  'summary': 'Explain what limits population size and how competition shapes communities.',
  'theory': [{'content': 'A POPULATION grows when birth rate exceeds death rate — and shrinks when death rate exceeds '
                         'birth rate.\n'
                         '\n'
                         'In theory, a population could grow exponentially — doubling repeatedly. In practice, growth '
                         'is LIMITED by:\n'
                         'Food availability.\n'
                         'Water supply.\n'
                         'Space and territory.\n'
                         'Predation.\n'
                         'Disease.\n'
                         'Waste accumulation.\n'
                         '\n'
                         'The CARRYING CAPACITY is the maximum population size that a habitat can sustainably support, '
                         'given the available resources.\n'
                         '\n'
                         'Once a population reaches carrying capacity, birth rate and death rate roughly balance — the '
                         'population stabilises (with fluctuations).\n'
                         '\n'
                         'PREDATOR-PREY CYCLES:\n'
                         'In a predator-prey relationship, the two populations cycle:\n'
                         'Prey increase → more food for predators → predators increase → prey decrease → predators '
                         'decrease (less food) → prey recover → cycle repeats.\n'
                         'The predator population changes FOLLOW the prey population changes — there is a LAG (delay) '
                         'because it takes time for populations to respond.',
              'heading': 'Population Size and Carrying Capacity'},
             {'content': "COMPETITION occurs when organisms need the same limited resource and must 'fight' for it — "
                         'reducing the amount available to others.\n'
                         '\n'
                         'INTRASPECIFIC COMPETITION (within a species):\n'
                         'Between individuals of the SAME species — most intense because they have IDENTICAL needs.\n'
                         'Controls population size — as populations grow, competition for resources intensifies → '
                         'birth rate falls, death rate rises → population growth slows.\n'
                         'Examples: robins defending territories, stags fighting for mates, oak trees competing for '
                         'light.\n'
                         '\n'
                         'INTERSPECIFIC COMPETITION (between species):\n'
                         'Between individuals of DIFFERENT species that need the same resource.\n'
                         'The stronger competitor may drive the weaker one to local extinction.\n'
                         'Example: grey squirrels outcompeting red squirrels for food and nesting sites → red '
                         'squirrels now largely absent from England.\n'
                         '\n'
                         'RESOURCES COMPETED FOR:\n'
                         'Animals: food, water, territory, mates, shelter.\n'
                         'Plants: light, water, minerals (from soil), space.',
              'heading': 'Competition'},
             {'content': 'DENSITY-DEPENDENT factors become more limiting as population DENSITY increases:\n'
                         'Food shortages — more individuals compete for the same food supply.\n'
                         'Disease — pathogens spread more easily in dense populations.\n'
                         'Predation — predators focus on areas of high prey density.\n'
                         'Waste accumulation — toxins from metabolic waste build up.\n'
                         '\n'
                         'DENSITY-INDEPENDENT factors affect populations regardless of their density:\n'
                         'Severe weather — frost, drought, flood, fire.\n'
                         'Natural disasters — volcanic eruption, tsunami.\n'
                         'Human activity — habitat destruction, pollution.\n'
                         '\n'
                         'Human impacts on population:\n'
                         'Hunting and fishing can reduce populations below viable levels.\n'
                         'Deforestation reduces carrying capacity for forest species.\n'
                         'Pollution increases death rates.\n'
                         'Introduction of invasive species can cause collapse of native species populations.',
              'heading': 'Factors Limiting Population Growth'}],
  'title': 'Population and Competition',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Biodiversity is NOT just about the NUMBER of species — it also includes the RELATIVE ABUNDANCE of '
                    'each species. An ecosystem with 100 species but 99% of the biomass belonging to just one species '
                    'has LOW biodiversity in practice. High biodiversity means many species AND reasonable numbers of '
                    'each.',
  'equations': [],
  'fifas': [],
  'higher': 'The impact of environmental change on biodiversity: habitat destruction, climate change, invasive '
            'species, pollution and overexploitation all reduce biodiversity. Students should be able to evaluate '
            'conservation strategies — protected areas, captive breeding, seed banks, habitat restoration — '
            'considering their effectiveness, cost and limitations. International agreements (e.g. Convention on '
            'Biological Diversity) coordinate global conservation efforts.',
  'id': 'biodiversity',
  'key_note': 'Biodiversity = species diversity + genetic diversity. Importance: ecosystem services (food, medicine, '
              'clean water, pollination), stability, ethical reasons. Threats: habitat loss, pollution, invasive '
              'species, overexploitation, climate change. Conservation: protected areas, captive breeding, seed banks, '
              'legislation.',
  'matching': {'instruction': 'Sort each example into a threat to biodiversity or a conservation measure.',
               'pairs': [('Threat', 'Deforestation — habitat destroyed for agriculture or timber'),
                         ('Conservation',
                          'Captive breeding programmes — endangered species bred in zoos to prevent extinction'),
                         ('Threat', 'Invasive species — grey squirrels outcompeting native red squirrels'),
                         ('Conservation',
                          'Seed banks — storing seeds of thousands of plant varieties as genetic insurance'),
                         ('Threat', 'Overfishing — fish populations reduced below sustainable levels'),
                         ('Conservation', 'Marine protected areas — fishing banned to allow fish stocks to recover')],
               'title': 'Threat or Conservation Measure?'},
  'quiz': [{'opts': [('A genetically diverse population is more adaptable — some individuals will have alleles giving '
                      'resistance to new diseases or tolerance of changing conditions',
                      True),
                     ('Genetic diversity makes individuals physically larger and stronger', False),
                     ('Genetic diversity allows a species to reproduce more rapidly', False),
                     ('Genetic diversity means all individuals look different — making them harder for predators to '
                      'target',
                      False)],
            'q': 'Why is high genetic diversity within a species important?',
            'wrong_explanations': {1: "Genetic diversity doesn't directly affect physical size — size is just one "
                                      'trait among many.',
                                   2: 'Reproductive rate is not directly linked to genetic diversity — it depends on '
                                      'life history traits specific to the species.',
                                   3: 'Variation in appearance can help avoid predators — but the primary ecological '
                                      'importance of genetic diversity is ADAPTABILITY to change.'}},
           {'opts': [('They store seeds of thousands of plant varieties — preserving genetic diversity as insurance '
                      'against extinction of wild populations',
                      True),
                     ('They grow plants for replanting in habitats where species have become locally extinct', False),
                     ('They store seeds of food crops only — to ensure human food security', False),
                     ('They sell seeds to farmers to encourage growing a wider variety of crops', False)],
            'q': 'Why are seed banks important for biodiversity conservation?',
            'wrong_explanations': {1: 'Seed banks primarily STORE seeds in long-term preservation conditions — they '
                                      'are not generally growing facilities or nurseries (though some seed banks do '
                                      'have growing programmes).',
                                   2: 'Seed banks like the Svalbard Global Seed Vault store seeds of wild plant '
                                      'species AND crop varieties — not food crops only.',
                                   3: 'Seed banks are conservation facilities — not commercial enterprises, though '
                                      'some seed collections are used to support farmers.'}}],
  'rp': None,
  'spec': '4.7.4',
  'summary': 'Define biodiversity, explain its importance and describe threats to it and conservation measures.',
  'theory': [{'content': 'BIODIVERSITY is the variety of life on Earth.\n'
                         '\n'
                         'It has two components:\n'
                         'SPECIES DIVERSITY — the number of DIFFERENT SPECIES in an area AND the relative abundance of '
                         'each species.\n'
                         'GENETIC DIVERSITY — the variety of ALLELES (different versions of genes) within a species.\n'
                         '\n'
                         'High species diversity means many different species, each present in reasonable numbers.\n'
                         'High genetic diversity within a species means the population has a wide range of alleles — '
                         'making it adaptable.\n'
                         '\n'
                         'Why genetic diversity matters:\n'
                         'A genetically diverse population can cope with new diseases, climate shifts or environmental '
                         'changes — some individuals will have alleles giving resistance or tolerance.\n'
                         'A genetically uniform population (like a monoculture crop) is vulnerable — one disease can '
                         'devastate the whole population.',
              'heading': 'What is Biodiversity?'},
             {'content': 'High biodiversity provides essential ECOSYSTEM SERVICES that humans depend on:\n'
                         '\n'
                         'Food PRODUCTION — diverse ecosystems provide diverse foods. Wild relatives of crop plants '
                         'are a genetic reservoir for future crop improvement.\n'
                         '\n'
                         "POLLINATION — approximately 75% of the world's food crops depend on animal pollinators "
                         '(bees, butterflies, hoverflies). Loss of pollinator diversity threatens food security.\n'
                         '\n'
                         'Clean WATER — wetland plants and soil organisms filter pollutants from water naturally.\n'
                         '\n'
                         'Clean AIR — forests and vegetation absorb CO₂ and other pollutants.\n'
                         '\n'
                         'MEDICINES — many drugs come from wild species: aspirin from willow, penicillin from a mould, '
                         'cancer drugs from the Pacific yew tree. Undiscovered species may hold future cures.\n'
                         '\n'
                         'ECOSYSTEM STABILITY — more species = more connections = more resilience. If one species '
                         'declines, others can take over its role.\n'
                         '\n'
                         'CLIMATE REGULATION — forests absorb CO₂ and influence rainfall patterns.\n'
                         '\n'
                         'ETHICAL RESPONSIBILITY — many argue that all species have a right to exist, regardless of '
                         'utility to humans.',
              'heading': 'Why Biodiversity Matters'},
             {'content': 'THREATS:\n'
                         'HABITAT DESTRUCTION — deforestation, draining of wetlands, urbanisation, agricultural '
                         'expansion → loss of living space for species.\n'
                         'POLLUTION — pesticides, plastic, oil spills, acid rain damage habitats and directly kill '
                         'organisms.\n'
                         'INVASIVE SPECIES — introduced species outcompete or prey on native species (e.g. grey '
                         'squirrels, American mink, Japanese knotweed).\n'
                         'OVEREXPLOITATION — overfishing, overhunting, illegal wildlife trade reducing populations '
                         'below viable levels.\n'
                         'CLIMATE CHANGE — shifting temperature ranges, sea level rise, altered rainfall patterns '
                         'displace or eliminate species.\n'
                         '\n'
                         'CONSERVATION MEASURES:\n'
                         'PROTECTED AREAS — national parks, nature reserves, marine protected areas prevent habitat '
                         'destruction.\n'
                         'CAPTIVE BREEDING PROGRAMMES — zoos and wildlife centres breed endangered species to prevent '
                         'extinction.\n'
                         'SEED BANKS — e.g. Svalbard Global Seed Vault stores seeds of thousands of plant varieties as '
                         'insurance against loss.\n'
                         'REINTRODUCTION PROGRAMMES — reintroducing species to habitats where they once lived (e.g. '
                         'beavers in Scotland, white-tailed eagles in England).\n'
                         'LEGISLATION — laws protecting endangered species and their habitats (e.g. CITES, Wildlife '
                         'and Countryside Act).\n'
                         'HABITAT RESTORATION — rewilding projects restore degraded habitats.\n'
                         'SUSTAINABLE FISHING — quotas, minimum catch sizes, protected areas to allow fish stocks to '
                         'recover.',
              'heading': 'Threats to Biodiversity and Conservation'}],
  'title': 'Biodiversity',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'PLANTS also respire — they release CO₂ just like animals. The difference is that during the DAY, '
                    'photosynthesis removes MORE CO₂ than respiration releases — so there is net CO₂ uptake. At night, '
                    "only respiration occurs. Students often say 'plants absorb CO₂, they don't release it' — this is "
                    'wrong.',
  'equations': [],
  'fifas': [],
  'higher': 'Human impacts on the carbon cycle: burning fossil fuels releases ancient sequestered carbon rapidly; '
            'deforestation removes carbon sinks AND releases stored carbon. Rising atmospheric CO₂ enhances the '
            'greenhouse effect causing global warming and climate change. Ocean acidification — CO₂ dissolves in '
            'seawater forming carbonic acid — threatens coral reefs and shell-forming organisms. Students should '
            'understand the distinction between the short-term carbon cycle and the long-term geological cycle.',
  'id': 'carbon-cycle',
  'key_note': 'CO₂ removed by: photosynthesis, dissolution in oceans. CO₂ returned by: respiration (all organisms), '
              'decomposition, combustion, volcanic activity. Fossil fuels = long-term carbon store. Burning them '
              'releases ancient carbon rapidly → climate change.',
  'matching': {'instruction': 'Sort each process into removing CO₂ from or returning CO₂ to the atmosphere.',
               'pairs': [('Removes CO₂', 'Photosynthesis — plants convert CO₂ into glucose using light energy'),
                         ('Returns CO₂', 'Respiration — all living organisms release CO₂ as they break down glucose'),
                         ('Returns CO₂', 'Combustion — burning wood or fossil fuels releases CO₂'),
                         ('Removes CO₂', 'Dissolution in oceans — CO₂ absorbed into seawater'),
                         ('Returns CO₂', 'Decomposition — bacteria and fungi release CO₂ from dead organic matter'),
                         ('Returns CO₂', 'Volcanic activity — releases CO₂ from underground carbon stores')],
               'title': 'Carbon Cycle — Removes or Returns CO₂?'},
  'quiz': [{'opts': [('Fossil fuels contain carbon that has been stored underground for millions of years — releasing '
                      'it rapidly adds ancient carbon that had been removed from the active cycle',
                      True),
                     ('Fossil fuels burn hotter, so they release more CO₂ per reaction', False),
                     ('Wood absorbs CO₂ as it burns, partially cancelling its emissions', False),
                     ('Fossil fuels contain more hydrogen, which converts to CO₂ during combustion', False)],
            'q': 'Why does burning fossil fuels increase atmospheric CO₂ more than burning wood?',
            'wrong_explanations': {1: "Combustion temperature doesn't determine CO₂ output — the amount of carbon in "
                                      'the fuel does.',
                                   2: 'Wood does not absorb CO₂ while burning — it releases it. The difference is that '
                                      'wood carbon was recently absorbed from the atmosphere, while fossil fuel carbon '
                                      'was locked away for millions of years.',
                                   3: 'Hydrogen in fuels combines with oxygen to form WATER, not CO₂. Carbon combines '
                                      'with oxygen to form CO₂.'}},
           {'opts': [('Removes photosynthesising trees (less CO₂ absorbed) AND burning or rotting felled trees '
                      'releases CO₂ — a double increase in atmospheric CO₂',
                      True),
                     ('Deforestation only affects CO₂ if the wood is burned — leaving it to rot has no effect', False),
                     ('Deforestation decreases CO₂ because the dead wood is converted to fossil fuels underground',
                      False),
                     ('Deforestation has no effect on CO₂ — other plants regrow in the cleared areas quickly', False)],
            'q': 'How does deforestation affect atmospheric CO₂ levels?',
            'wrong_explanations': {1: 'Rotting (decomposition) DOES release CO₂ — decomposers respire and return '
                                      'carbon to the atmosphere, just more slowly than burning.',
                                   2: 'Fossil fuel formation takes millions of years under specific geological '
                                      'conditions — dead wood does not become fossil fuel on human timescales.',
                                   3: 'Regrowth does occur — but typically much less vegetation regrows than was '
                                      'removed, and regeneration takes decades. The net effect is increased '
                                      'atmospheric CO₂.'}}],
  'rp': None,
  'spec': '4.7.3',
  'summary': 'Describe how carbon is cycled through ecosystems and the atmosphere.',
  'theory': [{'content': 'Carbon is the backbone of ALL organic molecules — carbohydrates, proteins, fats, DNA. Life '
                         'as we know it is CARBON-BASED.\n'
                         '\n'
                         'The total amount of carbon on Earth is fixed — it cannot be created or destroyed.\n'
                         '\n'
                         'Carbon must be RECYCLED — continuously moving between living organisms, the atmosphere, '
                         'oceans, soil and rocks.\n'
                         '\n'
                         'The CARBON CYCLE describes how carbon atoms move through these different stores (also called '
                         'reservoirs or sinks).\n'
                         '\n'
                         'Main carbon stores:\n'
                         'ATMOSPHERE — as CO₂ and methane (CH₄).\n'
                         'LIVING ORGANISMS — carbon in organic molecules (glucose, proteins, fats, DNA).\n'
                         'SOIL — carbon in decomposing organic matter (humus).\n'
                         'OCEANS — dissolved CO₂ and carbonate in shells.\n'
                         'FOSSIL FUELS — coal, oil, gas (ancient organic carbon locked underground).\n'
                         'ROCKS — limestone (CaCO₃) formed from shells of ancient marine organisms.',
              'heading': 'Why Carbon Must Be Recycled'},
             {'content': 'REMOVING CO₂ FROM THE ATMOSPHERE:\n'
                         'PHOTOSYNTHESIS — plants and algae absorb CO₂ and convert it to glucose. Carbon is '
                         "incorporated into the plant's biomass.\n"
                         'DISSOLUTION IN OCEANS — CO₂ dissolves in seawater to form carbonic acid. Marine organisms '
                         'use dissolved carbon to make calcium carbonate (CaCO₃) shells.\n'
                         '\n'
                         'RETURNING CO₂ TO THE ATMOSPHERE:\n'
                         'RESPIRATION — ALL living organisms (plants, animals, fungi, bacteria) respire, releasing CO₂ '
                         'as glucose is broken down.\n'
                         'DECOMPOSITION — microorganisms (bacteria and fungi) break down dead organic matter, '
                         'releasing CO₂ and returning carbon to the atmosphere and soil.\n'
                         'COMBUSTION — burning of organic material (wood, coal, oil, gas) releases CO₂ rapidly into '
                         'the atmosphere.\n'
                         'VOLCANIC ACTIVITY — releases CO₂ from underground carbon stores (lava, volcanic gases).\n'
                         '\n'
                         'LONG-TERM CARBON STORAGE:\n'
                         'FOSSILISATION — over millions of years, the remains of organisms become compressed into '
                         'fossil fuels (coal from ancient forests, oil and gas from marine organisms).\n'
                         'Burning fossil fuels releases this long-term stored carbon rapidly — adding CO₂ to the '
                         'atmosphere FASTER than natural processes can remove it → CLIMATE CHANGE.',
              'heading': 'Processes in the Carbon Cycle'},
             {'content': 'Human activities are disrupting the carbon cycle by adding CO₂ to the atmosphere faster than '
                         'it can be removed.\n'
                         '\n'
                         'BURNING FOSSIL FUELS — coal, oil and natural gas burn to release CO₂ that has been stored '
                         'underground for millions of years.\n'
                         '\n'
                         'DEFORESTATION:\n'
                         'Felling trees removes photosynthesising plants → less CO₂ absorbed.\n'
                         'Burning or rotting felled trees releases CO₂.\n'
                         'Double negative impact on atmospheric CO₂.\n'
                         '\n'
                         'CEMENT PRODUCTION — manufacturing cement releases CO₂ from limestone (CaCO₃ → CaO + CO₂).\n'
                         '\n'
                         'RICE PADDY AGRICULTURE and LIVESTOCK — produce methane (CH₄), another greenhouse gas.\n'
                         '\n'
                         'CONSEQUENCES OF RISING CO₂:\n'
                         'Enhanced greenhouse effect → global warming → climate change.\n'
                         'Ocean acidification — more CO₂ dissolves → more carbonic acid → threatens marine ecosystems '
                         '(especially coral reefs and shell-forming organisms).',
              'heading': 'Human Impact on the Carbon Cycle'}],
  'title': 'The Carbon Cycle',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'TRANSPIRATION is the loss of water vapour from PLANT LEAVES through stomata — it is NOT the same '
                    'as evaporation from the soil or water surface. Both contribute to atmospheric water, but '
                    'transpiration is specifically the biological process in plants. Also: precipitation is NOT just '
                    'rain — it includes snow, sleet and hail.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'water-cycle',
  'key_note': 'Water cycle: evaporation + transpiration → condensation (clouds) → precipitation (rain/snow) → '
              'runoff/groundwater → back to sea. Plants contribute via transpiration. Deforestation reduces '
              'transpiration → less rainfall. Key: water is continuously recycled.',
  'matching': {'instruction': 'Match each stage to its correct description.',
               'pairs': [('Evaporation',
                          'Heat energy causes water to change from liquid to vapour from oceans, lakes and soil'),
                         ('Transpiration', 'Water vapour released by plants through stomata into the atmosphere'),
                         ('Condensation', 'Rising water vapour cools and forms tiny liquid droplets — creating clouds'),
                         ('Precipitation', 'Water droplets in clouds fall as rain, snow, sleet or hail'),
                         ('Runoff',
                          'Water flows across the land surface into streams, rivers and eventually back to the sea')],
               'title': 'Match the Stage of the Water Cycle'},
  'quiz': [{'opts': [('Through transpiration — water absorbed from soil is released as water vapour through leaf '
                      'stomata, returning water to the atmosphere',
                      True),
                     ('By storing water permanently in their cells — removing it from the cycle', False),
                     ('By producing water as a by-product of photosynthesis', False),
                     ('By preventing precipitation by blocking clouds with their canopy', False)],
            'q': 'How do plants contribute to the water cycle?',
            'wrong_explanations': {1: "Plants don't store water permanently — they continuously take it in and release "
                                      'it. Transpiration is the return pathway to the atmosphere.',
                                   2: 'Photosynthesis USES water as a reactant — it does not produce water as a '
                                      'by-product. Oxygen is the gas product of photosynthesis.',
                                   3: 'Forests influence local weather patterns but do not prevent precipitation — '
                                      'they actually INCREASE local rainfall by contributing to atmospheric water '
                                      'vapour.'}},
           {'opts': [('Trees release large amounts of water vapour through transpiration — removing them reduces the '
                      'water returning to the atmosphere, lowering precipitation',
                      True),
                     ('Trees attract rain clouds — without trees, clouds move away from the area', False),
                     ('Tree roots release chemicals that trigger condensation in the atmosphere above', False),
                     ('Deforestation increases runoff — water leaves the area before it can evaporate', False)],
            'q': 'Why does deforestation in tropical areas often lead to reduced local rainfall?',
            'wrong_explanations': {1: "Clouds are not 'attracted' to trees — the mechanism is through transpiration "
                                      'contributing to atmospheric moisture content.',
                                   2: 'Roots do not release chemicals that trigger condensation — their role in the '
                                      'water cycle is absorbing water from soil, which then passes up to leaves and '
                                      'out through transpiration.',
                                   3: 'Increased runoff does remove water quickly — but the PRIMARY reason for reduced '
                                      'local rainfall after deforestation is the loss of transpiration returning water '
                                      'to the atmosphere.'}}],
  'rp': None,
  'spec': '4.7.3',
  'summary': 'Describe how water is cycled through the environment.',
  'theory': [{'content': 'Water is essential to all life:\n'
                         'It is the SOLVENT for all biochemical reactions.\n'
                         'It is a REACTANT in photosynthesis and many other reactions.\n'
                         'It transports dissolved substances around organisms.\n'
                         'It provides structure to plant cells (turgor pressure).\n'
                         'It regulates body temperature (through sweating and evaporation).\n'
                         '\n'
                         'Like carbon, water is continuously RECYCLED through the environment in the WATER CYCLE (also '
                         'called the HYDROLOGICAL CYCLE).\n'
                         '\n'
                         'The total amount of water on Earth is effectively fixed — it moves between stores: oceans, '
                         'atmosphere, freshwater lakes and rivers, ice caps, groundwater, and living organisms.',
              'heading': 'Why Water Must Be Recycled'},
             {'content': 'EVAPORATION:\n'
                         "The sun's heat energy causes water to evaporate from the surfaces of oceans, lakes, rivers "
                         'and soil.\n'
                         'Water changes from liquid to water vapour — rising into the atmosphere.\n'
                         '\n'
                         'TRANSPIRATION:\n'
                         'Plants release water vapour through their stomata — a process called TRANSPIRATION.\n'
                         'In tropical rainforests, transpiration adds enormous quantities of water to the atmosphere — '
                         'maintaining local rainfall patterns.\n'
                         '\n'
                         'CONDENSATION:\n'
                         'As water vapour rises, it cools.\n'
                         'Cooling causes it to CONDENSE — changing from vapour back to tiny liquid water droplets.\n'
                         'These droplets form CLOUDS and mist.\n'
                         '\n'
                         'PRECIPITATION:\n'
                         'When water droplets in clouds collide and join to form larger drops, they fall as '
                         'PRECIPITATION — rain, snow, sleet or hail.\n'
                         '\n'
                         'RUNOFF AND GROUNDWATER:\n'
                         'Precipitation that falls on land either:\n'
                         'Flows across the surface as RUNOFF — into streams and rivers → back to the sea.\n'
                         'SOAKS INTO the ground to form GROUNDWATER — extracted by plant roots or flowing slowly to '
                         'rivers and sea.',
              'heading': 'Stages of the Water Cycle'},
             {'content': 'Living organisms play an important role in the water cycle:\n'
                         '\n'
                         'PLANTS:\n'
                         'Absorb water from the soil through root hair cells.\n'
                         'Transport water up through xylem to leaves.\n'
                         'Release water vapour through stomata (transpiration) — returns water to the atmosphere.\n'
                         'Soil absorption is helped by the structural effects of plant roots.\n'
                         '\n'
                         'ANIMALS:\n'
                         'Obtain water by drinking, and from food.\n'
                         'Return water to the environment through:\n'
                         'Urination and defaecation.\n'
                         'Exhaling water vapour.\n'
                         'Sweating.\n'
                         '\n'
                         'HUMAN IMPACTS on the water cycle:\n'
                         'DEFORESTATION — removing trees reduces transpiration → less water returned to atmosphere → '
                         'reduced local rainfall → increased risk of drought.\n'
                         'URBANISATION — impermeable surfaces (roads, buildings) prevent water soaking into soil → '
                         'increased runoff → flooding.\n'
                         'IRRIGATION — withdrawing groundwater for farming can deplete underground reserves.\n'
                         'CLIMATE CHANGE — warming increases evaporation → more intense rainfall events and more '
                         'severe droughts.',
              'heading': 'Living Organisms and the Water Cycle'}],
  'title': 'The Water Cycle',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'DENITRIFYING bacteria convert NITRATES BACK TO N₂ — they REDUCE soil nitrogen and make it less '
                    'fertile. NITRIFYING bacteria convert AMMONIA TO NITRATES — they INCREASE soil nitrogen '
                    'availability. These are opposite processes by different bacteria. Denitrification is favoured in '
                    'WATERLOGGED (anaerobic) soils.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'nitrogen-cycle',
  'key_note': 'N₂ → ammonia: nitrogen-fixing bacteria (soil or root nodules). Ammonia → nitrates: nitrifying bacteria. '
              'Plants absorb nitrates. Decomposers release ammonia. Nitrates → N₂: denitrifying bacteria (anaerobic). '
              'Eutrophication: nitrate leaching → algal bloom → O₂ depletion → fish die.',
  'matching': {'instruction': 'Match each process to the bacteria responsible and what it converts.',
               'pairs': [('Nitrogen fixation',
                          'Nitrogen-fixing bacteria — convert N₂ gas to ammonia in soil or root nodules'),
                         ('Nitrification',
                          'Nitrifying bacteria — convert ammonia to nitrites then nitrates in the soil'),
                         ('Denitrification',
                          'Denitrifying bacteria — convert nitrates back to N₂ gas in waterlogged soil'),
                         ('Decomposition (ammonification)',
                          'Decomposers (bacteria/fungi) — break down proteins in dead organisms, releasing ammonia'),
                         ('Absorption',
                          'Plant roots absorb nitrate ions from the soil to make amino acids and proteins')],
               'title': 'Match the Nitrogen Cycle Process'},
  'quiz': [{'opts': [('N₂ is an extremely unreactive gas — it must be fixed into ammonia or nitrates by bacteria '
                      'before plants can use it',
                      True),
                     ('N₂ molecules are too large to pass through root cell membranes', False),
                     ('Nitrogen is toxic to plants in its atmospheric form', False),
                     ("Plants already have enough nitrogen — they don't need more from the atmosphere", False)],
            'q': "Why can't plants use atmospheric nitrogen (N₂) directly?",
            'wrong_explanations': {1: 'N₂ is a small molecule — its unreactivity is due to the very strong triple bond '
                                      'between the nitrogen atoms, not its size.',
                                   2: 'N₂ is completely non-toxic — it makes up 78% of the air we breathe. Its issue '
                                      'is extreme chemical stability, not toxicity.',
                                   3: 'Plants are frequently nitrogen-limited in their growth — nitrogen deficiency '
                                      'causes yellowing leaves (chlorosis). They need nitrogen continuously.'}},
           {'opts': [('Excess nitrates enter water → algal bloom → plants die → decomposers use all O₂ → fish '
                      'suffocate — caused by fertiliser leaching from farmland',
                      True),
                     ('Acid rain lowering the pH of lakes and rivers — caused by nitrogen oxides from vehicle exhausts',
                      False),
                     ('Plastic pollution blocking light from reaching aquatic plants in rivers and lakes', False),
                     ('Warming water temperatures reducing oxygen solubility — caused by climate change', False)],
            'q': 'What is eutrophication and what causes it?',
            'wrong_explanations': {1: 'Acid rain from nitrogen oxides is a real environmental problem — but '
                                      'eutrophication specifically refers to the nitrate leaching → algal bloom → '
                                      'oxygen depletion sequence.',
                                   2: 'Plastic pollution is a serious problem — but eutrophication is specifically '
                                      'caused by NUTRIENT enrichment (excess nitrates/phosphates), not plastic.',
                                   3: 'Warming does reduce oxygen solubility — but eutrophication is specifically the '
                                      'nutrient enrichment process causing algal blooms and oxygen depletion.'}},
           {'opts': [('Legumes have root nodules containing nitrogen-fixing bacteria — these add nitrates to the soil, '
                      'naturally fertilising it for the next crop',
                      True),
                     ('Legumes have deeper roots that break up compacted soil to improve drainage', False),
                     ('Legumes produce chemicals that kill pests and diseases in the soil', False),
                     ('Legumes absorb excess water that would otherwise waterlog the soil', False)],
            'q': 'Why do farmers rotate crops, sometimes planting legumes (e.g. clover or peas)?',
            'wrong_explanations': {1: 'Root depth is an advantage of some legumes — but the primary reason for '
                                      'including them in rotation is NITROGEN FIXATION by Rhizobium bacteria in root '
                                      'nodules.',
                                   2: 'Some plants do suppress soil pests — but the specific benefit of legumes in '
                                      'crop rotation is nitrogen fixation, not pest control.',
                                   3: "Legumes don't have exceptional water absorption compared to other plants — the "
                                      'key benefit is nitrogen fixation.'}}],
  'rp': None,
  'spec': '4.7.3',
  'summary': 'Describe how nitrogen is cycled through ecosystems by bacteria and other processes.',
  'theory': [{'content': 'NITROGEN is essential for life — it is a key component of:\n'
                         'AMINO ACIDS — the building blocks of proteins (enzymes, structural proteins, haemoglobin).\n'
                         'NUCLEOTIDES — the building blocks of DNA and RNA.\n'
                         'CHLOROPHYLL — the photosynthetic pigment in plants.\n'
                         '\n'
                         'Nitrogen makes up approximately 78% of the atmosphere — but as N₂ gas, which is EXTREMELY '
                         'UNREACTIVE. Plants and animals CANNOT use N₂ directly.\n'
                         '\n'
                         'Nitrogen must first be FIXED — converted into a usable form (ammonia or nitrates) — before '
                         'organisms can use it.\n'
                         '\n'
                         'The nitrogen cycle describes how nitrogen moves between the atmosphere, soil, plants, '
                         'animals and decomposers.',
              'heading': 'Why Nitrogen is Essential'},
             {'content': 'NITROGEN FIXATION — converting N₂ to ammonia (NH₃):\n'
                         'CARRIED OUT BY: nitrogen-fixing bacteria.\n'
                         'IN SOIL: free-living bacteria (e.g. Azotobacter) fix N₂ in the soil.\n'
                         'IN ROOT NODULES: mutualistic bacteria (Rhizobium) live in the root nodules of LEGUMES (peas, '
                         'beans, clover, soybeans). They fix N₂, providing the plant with nitrates. The plant provides '
                         'the bacteria with glucose.\n'
                         'LIGHTNING: very high energy lightning can also fix small amounts of N₂.\n'
                         '\n'
                         'NITRIFICATION — converting ammonia to nitrates:\n'
                         'Ammonia (NH₃) in the soil is converted to NITRITES then NITRATES (NO₃⁻) by NITRIFYING '
                         'BACTERIA.\n'
                         'Plants can absorb nitrates through their roots.\n'
                         '\n'
                         'ABSORPTION — plants absorb nitrates from soil → use them to make amino acids → proteins.\n'
                         '\n'
                         'CONSUMPTION — animals eat plants → nitrogen passes along food chains.\n'
                         '\n'
                         'DECOMPOSITION — when organisms die:\n'
                         'DECOMPOSERS (bacteria and fungi) break down proteins and nucleic acids in dead organisms and '
                         'waste.\n'
                         'They release nitrogen as AMMONIA (ammonification).\n'
                         'Ammonia → nitrification → nitrates (cycle continues).\n'
                         '\n'
                         'DENITRIFICATION — converting nitrates back to N₂:\n'
                         'DENITRIFYING BACTERIA convert nitrates → N₂ gas, which returns to the atmosphere.\n'
                         "Occurs mainly in WATERLOGGED (anaerobic) soils — these bacteria don't need oxygen.\n"
                         'Reduces soil fertility.',
              'heading': 'The Key Processes'},
             {'content': 'FERTILISERS:\n'
                         'Farmers add ARTIFICIAL FERTILISERS (ammonium nitrate, etc.) or ORGANIC FERTILISERS (manure, '
                         'compost) to replace nitrates removed by harvesting crops.\n'
                         'Excess fertiliser can be washed from fields into rivers and lakes by rain — a process called '
                         'LEACHING.\n'
                         '\n'
                         'EUTROPHICATION — the consequence of nitrate leaching:\n'
                         '1. Excess nitrates enter a river or lake.\n'
                         '2. Algae grow rapidly (algal bloom) — covering the water surface.\n'
                         '3. Light cannot penetrate to underwater plants — they die.\n'
                         '4. Dead plants and algae are decomposed by bacteria.\n'
                         '5. Decomposing bacteria use up all the OXYGEN in the water (aerobic decomposition).\n'
                         '6. Oxygen concentration falls → fish and other aquatic animals suffocate and die.\n'
                         '\n'
                         'NITROGEN OXIDES from vehicle exhausts and power stations:\n'
                         'Fall as ACID RAIN — damages vegetation and acidifies rivers and lakes.',
              'heading': 'Human Impact on the Nitrogen Cycle'}],
  'title': 'The Nitrogen Cycle',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'DECOMPOSERS are bacteria and fungi — they chemically break down organic matter using enzymes. '
                    'DETRITIVORES (earthworms, woodlice) physically shred material into smaller pieces — increasing '
                    'surface area for decomposers. Detritivores do NOT chemically decompose material. Both are '
                    'important but they are different things.',
  'equations': [],
  'fifas': [],
  'higher': 'Rate of decomposition depends on: temperature (enzyme activity), moisture (decomposers need water), O₂ '
            'availability (aerobic decomposers work faster), pH (optimum pH for decomposer enzymes). Compost heaps are '
            'managed to optimise these conditions. Biogas digesters use anaerobic bacteria to produce methane from '
            'organic waste — used as a renewable fuel. Students should be able to design an experiment to investigate '
            'the effect of one factor on decomposition rate.',
  'id': 'decomposition',
  'key_note': 'Decomposers = bacteria and fungi. Recycle nutrients, complete carbon cycle. Detritivores (earthworms '
              'etc.) = physically shred material, increase surface area. Decomposition faster with: higher '
              'temperature, more moisture, more O₂, neutral pH. Used in composting and food preservation.',
  'matching': {'instruction': 'Match each condition to whether it speeds up or slows down decomposition.',
               'pairs': [('Speeds up', 'Warm, moist, aerobic conditions — ideal for decomposer enzyme activity'),
                         ('Slows down', 'Cold conditions — low temperature reduces enzyme activity'),
                         ('Slows down', 'Dry conditions — decomposers need water to function'),
                         ('Speeds up', 'Turning a compost heap regularly — adds oxygen for aerobic decomposers'),
                         ('Slows down', 'Waterlogged, anaerobic soil — most decomposers need oxygen'),
                         ('Slows down',
                          'Very acidic conditions (e.g. peat bog) — inhibits decomposer enzyme activity')],
               'title': 'Factors Affecting Decomposition'},
  'quiz': [{'opts': [('Decomposers (bacteria, fungi) chemically break down organic matter using enzymes. Detritivores '
                      '(earthworms, woodlice) physically shred it into smaller pieces.',
                      True),
                     ('Decomposers are larger organisms like earthworms. Detritivores are microscopic bacteria.',
                      False),
                     ('They are the same thing — both terms describe organisms that break down dead material.', False),
                     ('Decomposers work in soil only. Detritivores work above ground only.', False)],
            'q': 'What is the difference between decomposers and detritivores?',
            'wrong_explanations': {1: 'DECOMPOSERS are the MICROSCOPIC organisms (bacteria and fungi). DETRITIVORES '
                                      'are LARGER invertebrates like earthworms, woodlice and millipedes.',
                                   2: 'They are NOT the same — the distinction is between CHEMICAL breakdown '
                                      '(decomposers) and PHYSICAL breakdown (detritivores). They complement each '
                                      'other.',
                                   3: 'Both decomposers and detritivores can work in soil or in leaf litter — the '
                                      'distinction is not about location but about HOW they break down material.'}},
           {'opts': [('Low temperature slows enzyme activity in decomposer bacteria and fungi — decomposition rate '
                      'decreases significantly',
                      True),
                     ('The refrigerator removes oxygen from around the food — decomposers suffocate', False),
                     ('The cold temperature kills all bacteria in the food immediately', False),
                     ('Refrigerators produce chemicals that inhibit decomposer activity', False)],
            'q': 'Why does food last longer in a refrigerator than at room temperature?',
            'wrong_explanations': {1: "Refrigerators don't remove oxygen — they simply cool the air. The reduced "
                                      'decomposition rate is due to lower enzyme activity at low temperatures.',
                                   2: "Refrigeration SLOWS bacteria but doesn't kill them instantly — food still "
                                      'eventually spoils in the fridge. Freezing is needed to effectively stop '
                                      'bacteria.',
                                   3: "Refrigerators only cool — they don't produce inhibitory chemicals."}}],
  'rp': 'RP7 — Investigate the effect of temperature on the rate of decay. Place a food sample (e.g. bread) in '
        'different conditions. Record mould growth over time. Or: measure rate of decomposition of organic material at '
        'different temperatures using respirometers.',
  'spec': '4.7.3',
  'summary': 'Describe the role of decomposers in nutrient cycling and the factors that affect decomposition rate.',
  'theory': [{'content': 'DECOMPOSITION is the breakdown of dead organic matter (dead organisms, their waste products '
                         'and shed body parts) by MICROORGANISMS — primarily bacteria and fungi.\n'
                         '\n'
                         'Decomposers are absolutely essential for life on Earth:\n'
                         'They RECYCLE NUTRIENTS — releasing minerals (nitrates, phosphates) back into the soil where '
                         'plants can reabsorb them.\n'
                         'They complete the CARBON CYCLE — breaking down organic molecules and releasing CO₂ back to '
                         'the atmosphere.\n'
                         'Without decomposers, nutrients would remain locked in dead organisms → soil would rapidly '
                         'run out of minerals → plants could not grow → all life would eventually fail.\n'
                         '\n'
                         'DECOMPOSERS vs DETRITIVORES:\n'
                         'DECOMPOSERS: bacteria and fungi — chemically break down organic matter using enzymes '
                         '(EXTRACELLULAR DIGESTION — secreting enzymes outside the cell).\n'
                         'DETRITIVORES: earthworms, woodlice, millipedes — physically break down dead material into '
                         'smaller pieces. This INCREASES SURFACE AREA for decomposers to work on, speeding up '
                         'decomposition.\n'
                         'Both work together — detritivores break material up, decomposers chemically digest it.',
              'heading': 'What is Decomposition?'},
             {'content': 'Decomposers are living organisms — so decomposition rate is affected by the same factors '
                         'that affect all enzyme-controlled reactions.\n'
                         '\n'
                         'TEMPERATURE:\n'
                         'Higher temperature (up to ~40°C) → faster enzyme activity → faster decomposition.\n'
                         'Cold temperatures slow decomposition significantly — this is why refrigerators and freezers '
                         'preserve food.\n'
                         'Above ~40°C, decomposer enzymes start to denature → rate falls.\n'
                         '\n'
                         'MOISTURE (WATER AVAILABILITY):\n'
                         'Decomposers need water to survive and to transport dissolved nutrients.\n'
                         'Dry conditions → decomposition slows dramatically — this is why dried food lasts longer.\n'
                         'Waterlogged conditions can slow decomposition too — if the soil becomes anaerobic (no O₂).\n'
                         '\n'
                         'OXYGEN AVAILABILITY:\n'
                         'Most decomposers are AEROBIC — they need oxygen for respiration.\n'
                         'AEROBIC conditions (well-aerated soil or compost) → faster decomposition.\n'
                         'ANAEROBIC conditions (waterlogged soil, sealed containers) → slower decomposition → some '
                         'decomposers produce methane (CH₄) instead of CO₂.\n'
                         '\n'
                         'pH:\n'
                         'Decomposers have an optimum pH. Very acidic or very alkaline conditions slow enzyme activity '
                         '→ slower decomposition.\n'
                         'Peat bogs are very acidic → slow decomposition → organic matter accumulates as peat '
                         '(preserving bog bodies for thousands of years).',
              'heading': 'Factors Affecting Decomposition Rate'},
             {'content': 'Understanding decomposition has many practical applications:\n'
                         '\n'
                         'COMPOSTING:\n'
                         'Mixing organic waste (vegetable peelings, garden waste) in a COMPOST HEAP.\n'
                         'Optimal conditions: moisture, oxygen (turn the heap regularly), warmth.\n'
                         'Decomposers break down the material → releases nutrients → creates COMPOST — a rich organic '
                         'fertiliser for gardens.\n'
                         '\n'
                         'FOOD PRESERVATION:\n'
                         'Methods work by removing conditions decomposers need:\n'
                         'REFRIGERATION — low temperature slows decomposition.\n'
                         'FREEZING — very low temperature stops decomposition.\n'
                         'DRYING — removes moisture.\n'
                         'PICKLING — low pH (vinegar) inhibits decomposers.\n'
                         'VACUUM PACKING — removes O₂.\n'
                         'SUGARING or SALTING — draws water out of food by osmosis, dehydrating decomposers.\n'
                         '\n'
                         'SEWAGE TREATMENT:\n'
                         'Decomposers in sewage treatment works break down organic waste in human sewage.\n'
                         'Aerobic decomposers process the waste, removing pollutants.\n'
                         'Biogas (methane) captured from anaerobic decomposition used as a fuel.',
              'heading': 'Decomposition in Human Contexts'}],
  'title': 'Decomposition',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Arrows in food chains show the direction of ENERGY FLOW — from prey TO predator. They do NOT show '
                    "'what eats what' in the backward direction. Arrow = 'is eaten by' or 'energy flows to'. Also: "
                    'only ~10% of energy passes to the next level — most is lost in respiration.',
  'equations': [],
  'fifas': [],
  'higher': 'Calculate the efficiency of energy transfer between trophic levels. Explain ecological and practical '
            'implications of low efficiency — why supporting fewer trophic levels uses energy more sustainably. Apply '
            'trophic level analysis to evaluate the efficiency of human food production systems. Construct and '
            'interpret food webs and predict consequences of removing or adding a species.',
  'id': 'trophic-levels',
  'key_note': 'Trophic levels: 1 = producers (plants), 2 = primary consumers (herbivores), 3 = secondary consumers, 4 '
              '= tertiary consumers. ~10% energy transferred per level. Decomposers break down all levels. Arrows in '
              'food chains = direction of energy flow.',
  'matching': {'instruction': 'Match each organism to its trophic level.',
               'pairs': [('Trophic Level 1 — Producer', 'Oak tree — makes food by photosynthesis using sunlight'),
                         ('Trophic Level 2 — Primary consumer', 'Caterpillar — eats leaves from the oak tree'),
                         ('Trophic Level 3 — Secondary consumer', 'Blue tit — eats caterpillars'),
                         ('Trophic Level 4 — Tertiary consumer', 'Sparrowhawk — eats blue tits'),
                         ('Decomposer', 'Fungi and bacteria — break down dead organisms at all levels')],
               'title': 'Trophic Level Match'},
  'quiz': [{'opts': [('Arrows point from prey to predator — they show the direction of energy flow from grass to '
                      'rabbit to fox',
                      True),
                     ('Arrows point from predator to prey — they show what each animal eats', False),
                     ('Arrows point both ways — energy flows in both directions between organisms', False),
                     ("Arrows are just organisational — they don't have a specific meaning in food chains", False)],
            'q': 'In the food chain: Grass → Rabbit → Fox — which direction do the arrows point, and what do they '
                 'mean?',
            'wrong_explanations': {1: 'Arrows point FROM prey TO predator — showing the direction of energy transfer. '
                                      'So the arrow goes Grass → Rabbit, meaning energy flows FROM grass TO rabbit '
                                      '(rabbit eats grass).',
                                   2: 'Energy does not flow backwards in a food chain — energy is transferred in one '
                                      'direction only, from prey to predator.',
                                   3: 'Arrows have a precise meaning in food chains — they show the direction of '
                                      'energy flow, which is always one-way.'}},
           {'opts': [('Only about 10% of energy is transferred between each level — so little energy remains at higher '
                      'levels that another level cannot be supported',
                      True),
                     ('There are not enough different species to fill more levels', False),
                     ('Higher levels contain too many organisms — there is not enough space', False),
                     ('Predators at higher levels are too large to eat anything at a lower level', False)],
            'q': 'Why do food chains rarely have more than 4 or 5 trophic levels?',
            'wrong_explanations': {1: 'The number of species is not the limiting factor — energy availability is. The '
                                      '10% transfer rule means each successive level has drastically less energy.',
                                   2: 'Higher trophic levels have FEWER organisms (less energy = fewer individuals can '
                                      'be sustained), not more.',
                                   3: 'Predator size is not the reason — many small organisms occupy higher trophic '
                                      'levels (e.g. parasites, some insects).'}}],
  'rp': None,
  'spec': '4.7.4.1',
  'summary': 'Describe trophic levels in ecosystems and identify producers, primary and secondary consumers.',
  'theory': [{'content': 'A TROPHIC LEVEL describes the position of an organism in a food chain — how far it is from '
                         'the original energy source (the Sun).\n'
                         '\n'
                         'TROPHIC LEVEL 1 — PRODUCERS:\n'
                         'Plants and algae. Make their own food by photosynthesis. All energy in the ecosystem enters '
                         'through producers.\n'
                         'Examples: grass, oak trees, phytoplankton, seaweed.\n'
                         '\n'
                         'TROPHIC LEVEL 2 — PRIMARY CONSUMERS:\n'
                         'Herbivores — eat plants/algae.\n'
                         'Examples: rabbits, caterpillars, cows, zooplankton.\n'
                         '\n'
                         'TROPHIC LEVEL 3 — SECONDARY CONSUMERS:\n'
                         'Carnivores that eat primary consumers.\n'
                         'Examples: foxes (eating rabbits), frogs (eating insects), small fish (eating zooplankton).\n'
                         '\n'
                         'TROPHIC LEVEL 4 — TERTIARY CONSUMERS:\n'
                         'Carnivores that eat secondary consumers.\n'
                         'Examples: eagles, large sharks, humans (in some food chains).\n'
                         '\n'
                         'APEX PREDATORS: at the top of the food chain — not eaten by any other organism in that '
                         'ecosystem.',
              'heading': 'What Are Trophic Levels?'},
             {'content': 'DECOMPOSERS occupy a special role — they break down dead organisms and waste from all '
                         'trophic levels.\n'
                         '\n'
                         'Decomposers include: bacteria and fungi.\n'
                         'They digest complex organic molecules → release nutrients back into the soil.\n'
                         'Essential for NUTRIENT CYCLING — without them, nutrients would be locked in dead matter '
                         'forever.\n'
                         '\n'
                         'Decomposers are not usually assigned a numbered trophic level but are fundamental to '
                         'ecosystem function.\n'
                         '\n'
                         'FOOD CHAINS and FOOD WEBS:\n'
                         'Food chain: linear sequence showing feeding relationships. Arrow = energy transfer '
                         'direction.\n'
                         'Grass → Rabbit → Fox → Eagle\n'
                         '\n'
                         'Food web: multiple interconnected food chains — more realistic picture of an ecosystem.\n'
                         'Most organisms eat more than one thing and are eaten by more than one predator.\n'
                         '\n'
                         'KEYPOINT:\n'
                         'In food chains and food webs, ARROWS show the direction of ENERGY FLOW — from prey to '
                         "predator. The arrow means 'is eaten by' or 'energy flows to'.",
              'heading': 'Decomposers'},
             {'content': 'Energy enters ecosystems via PHOTOSYNTHESIS at trophic level 1.\n'
                         '\n'
                         'At each trophic level, energy is LOST:\n'
                         'Respiration — organisms use energy for life processes → released as heat.\n'
                         'Movement, excretion, undigested material.\n'
                         "Only a fraction of energy is incorporated into the organism's BIOMASS.\n"
                         '\n'
                         'Typically only about 10% of energy is transferred from one trophic level to the next.\n'
                         '(The exact value varies — 10% is a common approximation used at GCSE.)\n'
                         '\n'
                         'CONSEQUENCE:\n'
                         'Higher trophic levels have LESS energy available → can support fewer organisms.\n'
                         'This is why food chains rarely have more than 4–5 levels — too little energy to sustain '
                         'another level.\n'
                         '\n'
                         'EXAMPLE:\n'
                         '1000 kJ enters at trophic level 1 (producers).\n'
                         '~100 kJ available at level 2 (primary consumers).\n'
                         '~10 kJ available at level 3 (secondary consumers).\n'
                         '~1 kJ available at level 4 (tertiary consumers).\n'
                         '\n'
                         'This pattern of decreasing energy is shown in PYRAMIDS OF BIOMASS.',
              'heading': 'Energy Flow Through Trophic Levels'}],
  'title': 'Trophic Levels',
  'triple_only': 'Trophic levels in detail (4.7.4.1) is biology-only. Includes numbered trophic levels, the role of '
                 'decomposers, food webs, and the principle that ~10% of energy is transferred between trophic levels.',
  'variables': []},
 {'common_mistake': 'Pyramids of BIOMASS are almost always true pyramid shapes — the ONE exception can occur with '
                    'parasites (many small parasites on fewer large hosts). Pyramids of NUMBERS can be inverted (e.g. '
                    "one tree → many insects). Don't confuse the two. Trophic level 1 (producers) is ALWAYS at the "
                    'bottom.',
  'equations': [],
  'fifas': [],
  'higher': 'Construct accurate pyramids of biomass from quantitative data with appropriate scales. Explain why '
            'pyramids of biomass are more reliable than pyramids of numbers. Interpret unusual pyramid shapes (e.g. '
            'parasites, phytoplankton-zooplankton in oceans). Compare pyramids of biomass and pyramids of energy — '
            'explain why energy pyramids are always true pyramids.',
  'id': 'pyramids-of-biomass',
  'key_note': 'Pyramid of biomass: bar width ∝ total biomass at each level. Producers at bottom. Almost always true '
              'pyramid shape. Units: g/m² or kg/m². More reliable than number pyramids — accounts for organism size. '
              'Biomass decreases at higher levels due to energy lost in respiration.',
  'matching': {'instruction': 'Match each statement to the correct description.',
               'pairs': [('Width of bar', 'Proportional to total biomass at that trophic level'),
                         ('Trophic level 1 (producers)', 'Always at the BOTTOM of the pyramid — widest bar'),
                         ('Why biomass decreases upward',
                          'Energy lost at each level through respiration — less energy = less biomass at higher '
                          'levels'),
                         ('Units of biomass', 'g/m² or kg/m² — mass per unit area')],
               'title': 'Pyramid of Biomass'},
  'quiz': [{'opts': [('Biomass accounts for the size of organisms — one large organism may have more biomass than '
                      'thousands of small ones, giving a truer picture of energy stored',
                      True),
                     ('Biomass is easier to count than individual organisms in the wild', False),
                     ('Numbers pyramids always show the same shape — they give no useful information', False),
                     ('Biomass pyramids show the number of species, which is more informative than counting '
                      'individuals',
                      False)],
            'q': 'Why is a pyramid of biomass usually a more accurate representation of an ecosystem than a pyramid of '
                 'numbers?',
            'wrong_explanations': {1: 'Biomass is harder to measure than counting — it requires weighing all '
                                      'organisms. The advantage is accuracy, not ease.',
                                   2: 'Numbers pyramids CAN be inverted (e.g. one tree: many insects) — making them '
                                      'misleading. Biomass pyramids are almost always true pyramids.',
                                   3: 'Biomass pyramids show total MASS at each level — not species count. '
                                      'Biodiversity is a separate measure.'}},
           {'opts': [('1 cm — grasshopper biomass = 50 g; 50 ÷ 50 = 1 cm', True),
                     ('10 cm — grasshopper biomass = 50 g; 50 ÷ 5 = 10 cm', False),
                     ('5 cm — grasshopper biomass = 50 g; 50 ÷ 10 = 5 cm', False),
                     ('50 cm — each gram = 1 cm, so 50 g = 50 cm', False)],
            'q': 'In 1 m² of grassland, grass biomass is 500 g, grasshoppers 50 g, frogs 5 g. Using a scale of 1 cm = '
                 '50 g/m², how wide should the grasshopper bar be?',
            'wrong_explanations': {1: 'Scale is 1 cm = 50 g, not 1 cm = 5 g. So 50 g ÷ 50 = 1 cm, not 10 cm.',
                                   2: 'Scale is 1 cm = 50 g, not 1 cm = 10 g. So 50 ÷ 50 = 1 cm.',
                                   3: 'Scale is 1 cm = 50 g, not 1 cm = 1 g. Must divide by the scale factor.'}}],
  'rp': None,
  'spec': '4.7.4.2',
  'summary': 'Construct and interpret pyramids of biomass to represent relative biomass at each trophic level.',
  'theory': [{'content': 'A PYRAMID OF BIOMASS is a diagram that shows the relative TOTAL MASS OF LIVING MATERIAL '
                         '(biomass) at each trophic level in a food chain.\n'
                         '\n'
                         'HOW TO CONSTRUCT:\n'
                         'Each trophic level is represented by a horizontal BAR.\n'
                         'The WIDTH of each bar is proportional to the total biomass at that level.\n'
                         'Trophic level 1 (producers) is at the BOTTOM.\n'
                         'Higher trophic levels are stacked above, getting narrower.\n'
                         '\n'
                         'BIOMASS decreases at each higher trophic level because:\n'
                         'Energy is lost at each transfer (respiration, movement, heat).\n'
                         'Less energy → less mass can be supported.\n'
                         '\n'
                         'RESULT:\n'
                         'Pyramid of biomass is almost always a TRUE PYRAMID shape — wide at bottom, narrow at top.\n'
                         '\n'
                         'UNITS: biomass is measured in g/m² or kg/m² — mass per unit area of ground.',
              'heading': 'What Is a Pyramid of Biomass?'},
             {'content': 'PYRAMID OF NUMBERS shows the NUMBER of organisms at each level.\n'
                         'Can be an unusual shape — not always a true pyramid.\n'
                         '\n'
                         'EXAMPLE WHERE NUMBERS PYRAMID IS INVERTED:\n'
                         'One oak tree → hundreds of caterpillars → dozens of birds.\n'
                         'The oak tree is one organism (trophic level 1) but the caterpillars (level 2) are hundreds.\n'
                         'Numbers pyramid: narrow at bottom (1 tree) → wide in middle (many caterpillars).\n'
                         '\n'
                         'BUT the BIOMASS pyramid for this food chain IS a proper pyramid:\n'
                         'The one oak tree has far more biomass than all the caterpillars combined.\n'
                         'So biomass pyramid: wide bottom (large oak biomass) → narrower second level.\n'
                         '\n'
                         'BIOMASS PYRAMIDS are more reliable than number pyramids because they account for SIZE — one '
                         'large organism may have more biomass than thousands of small ones.\n'
                         '\n'
                         'BOTH pyramids are always drawn with producers at the BOTTOM.',
              'heading': 'Pyramids of Biomass vs Pyramids of Numbers'},
             {'content': 'DATA REQUIRED:\n'
                         'Total biomass of all organisms at each trophic level in a defined area.\n'
                         'Example: in 1 m² of grassland:\n'
                         'Level 1 (grass): 500 g/m²\n'
                         'Level 2 (grasshoppers): 50 g/m²\n'
                         'Level 3 (frogs): 5 g/m²\n'
                         'Level 4 (herons): 0.5 g/m²\n'
                         '\n'
                         'DRAWING THE PYRAMID:\n'
                         '1. Choose a scale — e.g. 1 cm = 50 g/m².\n'
                         '2. Draw level 1 at the bottom as the widest bar (10 cm wide for 500 g).\n'
                         '3. Draw level 2 above it, proportionally narrower (1 cm wide for 50 g).\n'
                         '4. Continue upward, each bar centred on the bar below.\n'
                         '5. Label each level with the organism name and trophic level.\n'
                         '\n'
                         'NOTE: It is the RELATIVE WIDTH that matters — bars should be drawn proportionally to the '
                         'data.\n'
                         'Always show the scale used.',
              'heading': 'Constructing a Pyramid of Biomass'}],
  'title': 'Pyramids of Biomass',
  'triple_only': 'Pyramids of biomass (4.7.4.2) is biology-only. Students must be able to construct accurate pyramids '
                 'of biomass from data and compare them with pyramids of numbers.',
  'variables': []},
 {'common_mistake': "The 10% transferred is the biomass that becomes part of the predator's BODY — not the amount "
                    'eaten. An animal may eat 1000 g of prey but only incorporate 100 g into its own biomass (10%). '
                    'The rest is lost through respiration, egestion and excretion.',
  'equations': ['Efficiency (%) = (biomass transferred ÷ biomass at current level) × 100'],
  'fifas': [{'label': 'Efficiency Calculation',
             'question': 'Grass has biomass 2000 g/m². Rabbits eating this grass have biomass 160 g/m². Calculate the '
                         'efficiency of transfer.',
             'steps': [('F', 'Efficiency (%) = (biomass at next level ÷ biomass at current level) × 100'),
                       ('I', 'Next level (rabbits) = 160; Current level (grass) = 2000'),
                       ('F', 'Efficiency = (160 ÷ 2000) × 100 = 0.08 × 100'),
                       ('A', 'Efficiency = 8%')]}],
  'higher': 'Calculate the efficiency of biomass transfer: efficiency (%) = (biomass at next level ÷ biomass at '
            'current level) × 100. Apply to evaluate farming practices — restricting movement reduces respiratory '
            'losses, improving efficiency. Calculate how many times more resource-efficient a plant-based diet is '
            'compared to a meat-based diet at successive trophic levels.',
  'id': 'transfer-of-biomass',
  'key_note': 'Biomass lost at each level due to: respiration (heat), egestion (faeces), excretion. ~10% efficiency '
              'per transfer. Efficiency = (next level ÷ current level) × 100. Eating lower in food chain more '
              'efficient. Restricting farm animal movement and controlling temperature improves efficiency.',
  'matching': {'instruction': 'Match each reason for biomass loss to the correct description.',
               'pairs': [('Respiration',
                          'Energy used for life processes released as heat — not passed to next trophic level'),
                         ('Egestion',
                          'Indigestible material leaves as faeces — energy goes to decomposers not predators'),
                         ('Excretion', 'Waste metabolic products (urine) removed — energy in these compounds is lost'),
                         ('~10% efficiency', 'Only about 1/10 of biomass at each level is transferred to the next')],
               'title': 'Biomass Transfer'},
  'quiz': [{'opts': [('10% — efficiency = (500 ÷ 5000) × 100 = 10%', True),
                     ('1% — efficiency = (50 ÷ 5000) × 100', False),
                     ('90% — the percentage NOT transferred = 90%', False),
                     ('500% — efficiency = (5000 ÷ 500) × 100', False)],
            'q': 'Producers have biomass 5000 g/m². Primary consumers have biomass 500 g/m². What is the efficiency of '
                 'transfer?',
            'wrong_explanations': {1: '(50 ÷ 5000) × 100 = 1% — but the biomass at the next level is 500, not 50.',
                                   2: '90% is the proportion LOST — not transferred. Efficiency = transferred ÷ '
                                      'available = 500 ÷ 5000 = 10%.',
                                   3: 'Must divide NEXT LEVEL by CURRENT LEVEL — not current by next. (5000 ÷ 500) × '
                                      '100 = 1000% which is impossible.'}},
           {'opts': [('Less movement means less energy used in respiration for muscle activity — more energy retained '
                      'as body mass (biomass for humans to eat)',
                      True),
                     ('Restricted movement prevents disease spreading between animals', False),
                     ('Animals that move less eat less food — reducing farming costs', False),
                     ('Restricted movement makes animals heavier due to water retention', False)],
            'q': "Why do intensive farming methods restrict farm animals' movement to improve food production "
                 'efficiency?',
            'wrong_explanations': {1: 'Disease prevention may be a concern but is not the reason for restricting '
                                      'movement in the context of energy efficiency.',
                                   2: 'Animals that move less may eat slightly less, but the key reason is that energy '
                                      'from food is retained as BIOMASS rather than used in movement.',
                                   3: 'Body mass increase is due to biomass accumulation — not water retention. The '
                                      'mechanism is reduced respiration for movement.'}}],
  'rp': None,
  'spec': '4.7.4.3',
  'summary': 'Explain why biomass is lost between trophic levels and calculate the efficiency of transfer.',
  'theory': [{'content': 'When an organism is eaten, not ALL of its biomass is transferred to the predator.\n'
                         '\n'
                         'BIOMASS IS LOST BECAUSE:\n'
                         '\n'
                         '1. RESPIRATION:\n'
                         'Organisms use energy from food for movement, growth, reproduction, and maintaining body '
                         'temperature.\n'
                         'This energy is released as HEAT to the surroundings — not available to the next level.\n'
                         'Warm-blooded (endothermic) animals lose proportionally more energy keeping warm.\n'
                         '\n'
                         '2. EGESTION:\n'
                         'Not all food consumed is digested — indigestible material (cellulose in plant cell walls, '
                         'bones) is excreted as FAECES.\n'
                         'Faeces energy is lost to decomposers, not to the next trophic level.\n'
                         '\n'
                         '3. EXCRETION:\n'
                         'Waste products of metabolism (urine, urea) are excreted — energy in these molecules is '
                         'lost.\n'
                         '\n'
                         '4. MOVEMENT:\n'
                         'Energy used for movement is released as heat.\n'
                         '\n'
                         "ONLY the energy that becomes part of the organism's OWN BIOMASS (growth) is available to the "
                         'next level.',
              'heading': 'Why Biomass Is Lost at Each Level'},
             {'content': 'The EFFICIENCY of energy transfer between trophic levels is typically about 10%.\n'
                         '\n'
                         'EFFICIENCY EQUATION:\n'
                         'Efficiency (%) = (biomass transferred to next level ÷ biomass at current level) × 100\n'
                         '\n'
                         'EXAMPLE:\n'
                         'Grass has biomass of 1000 g/m².\n'
                         'Grasshoppers consuming this grass have biomass of 100 g/m².\n'
                         'Efficiency = (100 ÷ 1000) × 100 = 10%\n'
                         '\n'
                         'APPLICATION — Why eating lower in the food chain is more efficient:\n'
                         'If humans eat grain (trophic level 2): 10% of grain energy available to us.\n'
                         'If humans eat beef (trophic level 3): only 10% × 10% = 1% of original grain energy '
                         'available.\n'
                         'Eating lower in the food chain is 10× more energy-efficient — important for global food '
                         'security.\n'
                         '\n'
                         'FARMING IMPLICATIONS:\n'
                         'Reducing energy losses from farm animals INCREASES efficiency:\n'
                         'Keeping animals warm → less energy wasted maintaining body temperature.\n'
                         'Limiting movement → less energy wasted on movement.\n'
                         'Result: more biomass available for human consumption.',
              'heading': 'Efficiency of Energy Transfer'},
             {'content': 'WORKED EXAMPLE:\n'
                         'A pond has 10,000 g/m² of algae (level 1).\n'
                         'Small fish eat algae and have biomass of 1000 g/m² (level 2).\n'
                         'Large fish eat small fish and have biomass of 100 g/m² (level 3).\n'
                         '\n'
                         'Efficiency level 1→2: (1000 ÷ 10,000) × 100 = 10%\n'
                         'Efficiency level 2→3: (100 ÷ 1000) × 100 = 10%\n'
                         '\n'
                         'WHAT HAPPENED TO THE OTHER 90% AT EACH LEVEL?\n'
                         'About 60–70%: used in respiration → heat.\n'
                         'About 20–30%: lost in egestion (undigested food).\n'
                         'Small fraction: lost in excretion.\n'
                         '\n'
                         'INTERPRETING DATA:\n'
                         'If given biomass at two consecutive levels, can calculate:\n'
                         'Mass transferred = biomass at next level.\n'
                         'Mass not transferred = biomass at current level − biomass at next level.\n'
                         '% efficiency = (next level biomass ÷ current level biomass) × 100.',
              'heading': 'Calculating Biomass Transfers'}],
  'title': 'Transfer of Biomass',
  'triple_only': 'Transfer of biomass (4.7.4.3) is biology-only. Includes calculating efficiency of biomass transfer, '
                 'reasons for biomass loss (respiration, egestion, excretion), and the implications for farming and '
                 'food security.',
  'variables': []},
 {'common_mistake': 'In the mark-recapture formula N = (n₁ × n₂) ÷ m — students often confuse what n₁, n₂ and m '
                    'represent. n₁ = first catch (all marked). n₂ = second catch (total number caught). m = marked '
                    'individuals IN the second catch. Do NOT divide by n₂ or mix up m and n₂.',
  'equations': ['N = (n₁ × n₂) ÷ m'],
  'fifas': [{'label': 'Mark-Recapture Calculation',
             'question': 'A student catches 40 woodlice, marks them and releases them. The next day, they catch 30 '
                         'woodlice and find that 6 are marked. Estimate the population.',
             'steps': [('F', 'N = (n₁ × n₂) ÷ m'),
                       ('I', 'N = (40 × 30) ÷ 6'),
                       ('F', 'N = 1200 ÷ 6'),
                       ('A', 'N = 200 woodlice')]}],
  'higher': 'Mark-recapture formula: N = (n₁ × n₂) ÷ m. Assumptions: random mixing of marked animals, no significant '
            'births/deaths/migration between captures, marking does not affect survival or recapture probability. '
            'Students should be able to evaluate the validity of these assumptions in given scenarios. Students should '
            'be able to use random number tables or coordinates to ensure random quadrat placement, reducing sampling '
            'bias.',
  'id': 'sampling-techniques',
  'key_note': 'Quadrats: random placement, count organisms, scale up. Transects: show distribution change across '
              'habitat. Mark-recapture: N = (n₁ × n₂) ÷ m — for mobile animals. Assumptions: random mixing, no '
              "population changes, mark doesn't harm animal.",
  'matching': {'instruction': 'Match each situation to the best sampling technique.',
               'pairs': [('Quadrats',
                          'Estimating the population of daisies in a field — stationary plants, random placement'),
                         ('Transect', 'Showing how plant species change from an open beach to a sheltered dune'),
                         ('Mark-recapture',
                          'Estimating the population of great crested newts in a pond — mobile animals'),
                         ('Quadrats', 'Counting the abundance of limpets on different zones of a rocky shore'),
                         ('Transect', 'Recording how lichen cover changes from a roadside to open countryside')],
               'title': 'Match the Sampling Technique'},
  'quiz': [{'opts': [('2000 — mean count (4) × (total area ÷ quadrat area) = 4 × 500 = 2000', True),
                     ('40 — mean count × number of quadrats = 4 × 10', False),
                     ('500 — total area of field', False),
                     ('50 — total area ÷ number of quadrats', False)],
            'q': 'A student places 10 quadrats (each 1 m²) randomly in a field (total area 500 m²). Mean dandelion '
                 'count = 4 per quadrat. Estimate the dandelion population.',
            'wrong_explanations': {1: '40 gives the total counted in ALL quadrats — not the estimated population of '
                                      'the whole field.',
                                   2: '500 is just the field area — it has nothing to do with the dandelion count.',
                                   3: '50 is just a spatial measurement — the estimated population requires scaling '
                                      'the mean count up to the full habitat area.'}},
           {'opts': [('100 — N = (25 × 20) ÷ 5 = 100', True),
                     ('250 — N = 25 × 20 ÷ 2 (dividing by wrong number)', False),
                     ('2500 — N = 25 × 20 × 5 (multiplying instead of dividing)', False),
                     ('1 — N = 5 ÷ (25 × 20)', False)],
            'q': 'In a mark-recapture study: 25 snails marked (n₁), 20 caught second time (n₂), 5 were marked (m). '
                 'What is the estimated population?',
            'wrong_explanations': {1: 'N = (n₁ × n₂) ÷ m = (25 × 20) ÷ 5 = 500 ÷ 5 = 100. Make sure to divide by m '
                                      '(number of marked in second catch = 5), not by n₂.',
                                   2: 'N = (n₁ × n₂) ÷ m = (25 × 20) ÷ 5 = 100. Multiplying gives an enormous '
                                      'overestimate.',
                                   3: 'The formula is N = (n₁ × n₂) ÷ m — not the inverse. Dividing m by the product '
                                      'gives a nonsensically small number.'}},
           {'opts': [('To avoid sampling bias — deliberately choosing areas with lots of organisms would overestimate '
                      'the population',
                      True),
                     ('Random placement ensures all quadrats are the same size', False),
                     ('Random placement prevents disturbing the organisms in the habitat', False),
                     ('It is a legal requirement for ecological surveys', False)],
            'q': 'Why must quadrats be placed RANDOMLY in a habitat?',
            'wrong_explanations': {1: "Quadrat size is fixed by the frame — it doesn't change with placement method.",
                                   2: 'Disturbance is minimised by careful technique — but the reason for random '
                                      'placement is specifically about statistical validity and avoiding bias.',
                                   3: 'There is no legal requirement for randomness — it is a scientific requirement '
                                      'to ensure the sample is representative of the whole habitat.'}}],
  'rp': 'RP6 — Use quadrats or transects to estimate population size or distribution of a species in a habitat. Place '
        'quadrats randomly and calculate mean count. Scale up to total habitat area.',
  'spec': '4.7.1',
  'summary': 'Describe how to estimate population size using quadrats, transects and mark-recapture.',
  'theory': [{'content': 'In ecology, it is usually IMPOSSIBLE to count every individual of a species in a habitat — '
                         'the area is too large or the organisms too numerous.\n'
                         '\n'
                         'Instead, ecologists take a SAMPLE — they count organisms in a smaller, representative '
                         'section of the habitat and use the results to estimate the total population.\n'
                         '\n'
                         'For a sample to be valid:\n'
                         'It must be RANDOM — to avoid bias (e.g. choosing only the easiest areas to access).\n'
                         'It must be REPRESENTATIVE — reflect the full range of conditions in the habitat.\n'
                         'A sufficient NUMBER of samples must be taken — to get a reliable mean.\n'
                         '\n'
                         'Three main sampling techniques:\n'
                         '1. QUADRATS — for slow-moving or stationary organisms.\n'
                         '2. TRANSECTS — to show how organisms change across a habitat.\n'
                         '3. MARK-RECAPTURE — for mobile animals.',
              'heading': 'Why We Sample'},
             {'content': 'A QUADRAT is a square frame placed on the ground to define a sample area.\n'
                         '\n'
                         'Typically 0.5 m × 0.5 m (0.25 m²) or 1 m × 1 m for vegetation.\n'
                         '\n'
                         'How to use quadrats:\n'
                         '1. Place the quadrat RANDOMLY in the habitat (use random number tables or throw the quadrat '
                         'over your shoulder).\n'
                         '2. Count or estimate the abundance of the target species within the quadrat.\n'
                         '3. Repeat many times across the habitat.\n'
                         '4. Calculate the MEAN count per quadrat.\n'
                         '5. SCALE UP: multiply the mean count by the total number of quadrat-sized areas in the whole '
                         'habitat.\n'
                         '\n'
                         'Formula:\n'
                         'Estimated population = (mean count per quadrat) × (total habitat area ÷ quadrat area)\n'
                         '\n'
                         'QUADRATS WORK BEST FOR:\n'
                         'Plants, mosses, lichens.\n'
                         'Slow-moving animals: limpets, snails, woodlice.\n'
                         '\n'
                         'NOT suitable for fast-moving animals — they escape before being counted.',
              'heading': 'Quadrats'},
             {'content': 'TRANSECTS:\n'
                         'A transect is a LINE drawn across a habitat — organisms are recorded at regular intervals '
                         'along the line.\n'
                         '\n'
                         'Used to show how species DISTRIBUTION changes across a habitat (e.g. from sea to land on a '
                         'rocky shore, or from open field to shaded woodland).\n'
                         '\n'
                         'BELT TRANSECT: a strip (e.g. 0.5 m wide) along the line — quadrats placed at regular '
                         'intervals. Records abundance.\n'
                         'LINE TRANSECT: simply records which species touch the line — presence/absence only.\n'
                         '\n'
                         'MARK-RECAPTURE (Lincoln Index):\n'
                         'Used for MOBILE ANIMALS that would escape quadrats.\n'
                         '\n'
                         'Method:\n'
                         '1. Capture a sample of the animal (n₁).\n'
                         '2. Mark each individual (e.g. paint a small spot on a snail shell, attach a leg ring to a '
                         'bird, clip a fin on a fish).\n'
                         '3. Release marked individuals back into the habitat.\n'
                         '4. Allow time for marked individuals to mix randomly with the population.\n'
                         '5. Capture a second sample (n₂).\n'
                         '6. Count the number of MARKED individuals in the second sample (m).\n'
                         '\n'
                         'Formula: N = (n₁ × n₂) ÷ m\n'
                         '\n'
                         'ASSUMPTIONS for the formula to be valid:\n'
                         'The mark does not affect survival (does not make animals more visible to predators or less '
                         'able to move).\n'
                         'Marked animals mix randomly with the rest of the population.\n'
                         'No significant immigration, emigration, births or deaths between the two captures.\n'
                         'All individuals are equally likely to be captured.',
              'heading': 'Transects and Mark-Recapture'}],
  'title': 'Sampling Techniques',
  'triple_only': None,
  'variables': [('N', 'Estimated population size', 'individuals', ''),
                ('n₁', 'Number caught and marked in first sample', 'individuals', ''),
                ('n₂', 'Total number caught in second sample', 'individuals', ''),
                ('m', 'Number of marked individuals in second sample', 'individuals', '')]},
 {'common_mistake': 'Lichens as indicator species indicate AIR QUALITY (sensitive to SO₂ air pollution). Mayfly larvae '
                    'indicate WATER QUALITY (sensitive to low oxygen/pollution). Students mix these up. Both are '
                    'absent from polluted environments — but one tells you about air, the other about water.',
  'equations': [],
  'fifas': [],
  'higher': None,
  'id': 'environmental-change',
  'key_note': 'Environmental change: natural or human-caused. Climate change → species moving poleward, seasonal '
              'mismatch, coral bleaching. Indicator species: lichens (air quality), mayfly larvae (water quality). '
              'Pollution → eutrophication, acid rain, oil spills. Habitat destruction → fragmentation → extinction '
              'risk.',
  'matching': {'instruction': 'Match each change to its ecological consequence.',
               'pairs': [('Rising temperatures', 'Many UK butterfly species expanding their range northwards'),
                         ('Eutrophication', 'Algal bloom → oxygen depletion → fish death in rivers'),
                         ('SO₂ air pollution',
                          'Lichens absent from polluted urban areas — indicator of poor air quality'),
                         ('Phenological mismatch',
                          "Caterpillars emerge earlier due to warmth — but birds don't breed earlier → chicks starve"),
                         ('Habitat fragmentation', 'Isolated habitat patches reduce gene flow between populations')],
               'title': 'Match the Environmental Impact'},
  'quiz': [{'opts': [('Water quality has deteriorated — mayfly larvae are sensitive to low oxygen and pollution; their '
                      'absence suggests nutrient runoff or other pollution',
                      True),
                     ('The river temperature has risen — mayfly larvae cannot survive in warm water', False),
                     ('A predator has eaten all the mayfly larvae in that section', False),
                     ('Mayfly larvae prefer the area upstream — they always migrate away from farmland', False)],
            'q': 'Scientists find that mayfly larvae are absent from a stretch of river downstream from a farm. What '
                 'does this suggest?',
            'wrong_explanations': {1: 'Temperature can affect mayfly larvae — but the downstream location from a farm '
                                      'specifically suggests NUTRIENT RUNOFF and eutrophication as the primary cause.',
                                   2: 'Predation could reduce numbers but is unlikely to eliminate an entire '
                                      'population in a specific stretch. The farm location strongly implies pollution.',
                                   3: 'Mayfly larvae are not known to actively migrate away from farmland — their '
                                      'absence is due to intolerable abiotic conditions (low oxygen from '
                                      'eutrophication).'}},
           {'opts': [('Climate change — rising spring temperatures trigger earlier breeding, as birds respond to '
                      'warmer conditions',
                      True),
                     ('Selective breeding by conservationists to match earlier insect emergence', False),
                     ('Reduced daylight in summer due to increased cloud cover', False),
                     ('Birds have evolved to breed earlier because earlier chicks survive better', False)],
            'q': 'Many bird species in the UK are breeding earlier in the year than they did 50 years ago. What is the '
                 'most likely cause?',
            'wrong_explanations': {1: "Conservationists don't selectively breed wild bird populations — the change is "
                                      'a response to environmental conditions.',
                                   2: 'Daylight hours have not significantly changed — it is TEMPERATURE that is '
                                      'changing with climate change. Day length is a key breeding trigger, but the '
                                      'earlier TIMING of temperature warming is causing earlier breeding.',
                                   3: 'While natural selection could eventually select for earlier breeding, the '
                                      'change has occurred too rapidly (within 50 years) to be explained by '
                                      'evolutionary change — it is a direct behavioural response to environmental '
                                      'change.'}}],
  'rp': None,
  'spec': '4.7.4',
  'summary': 'Describe how environmental changes affect the distribution and abundance of species.',
  'theory': [{'content': 'ENVIRONMENTAL CHANGE is any significant alteration to the abiotic or biotic conditions in an '
                         'ecosystem.\n'
                         '\n'
                         'Changes can be:\n'
                         'NATURAL — volcanic eruptions, floods, droughts, ice ages, disease outbreaks.\n'
                         'HUMAN-CAUSED (ANTHROPOGENIC) — deforestation, agriculture, pollution, climate change, '
                         'invasive species.\n'
                         '\n'
                         'Environmental change affects organisms because they are adapted to specific conditions.\n'
                         "If conditions change beyond an organism's tolerance range, it:\n"
                         'MOVES to a more suitable habitat (migration).\n'
                         'Adapts over many generations through natural selection.\n'
                         'BECOMES LOCALLY EXTINCT (extirpation).\n'
                         'BECOMES EXTINCT if it cannot move or adapt quickly enough.\n'
                         '\n'
                         'MONITORING ENVIRONMENTAL CHANGE:\n'
                         'POPULATION SIZE changes — increases or decreases indicate changes in habitat suitability.\n'
                         'SPECIES DISTRIBUTION — mapping where species occur over time shows range shifts.\n'
                         'INDICATOR SPECIES — species whose presence, absence or population size reflects '
                         'environmental quality.',
              'heading': 'Environmental Change and Species Distribution'},
             {'content': 'CLIMATE CHANGE is causing measurable shifts in species distributions worldwide.\n'
                         '\n'
                         'EFFECTS OF RISING TEMPERATURES:\n'
                         'SPECIES MOVING POLEWARD — organisms whose optimal temperature range is shifting move towards '
                         'the poles or to higher altitudes. Example: many UK butterfly species have expanded their '
                         'range northwards in recent decades.\n'
                         'SEASONAL TIMING SHIFTS (PHENOLOGY) — spring events happening earlier: flowers blooming '
                         "sooner, insects emerging earlier, birds migrating earlier. If these timing shifts don't "
                         'match between interdependent species (e.g. caterpillar emergence and bird breeding) — '
                         'MISMATCH occurs → reduced survival.\n'
                         'RANGE CONTRACTION — species at the warm edge of their range find conditions too hot and '
                         'cannot move further poleward → population declines.\n'
                         'CORAL BLEACHING — warmer oceans cause coral polyps to expel their symbiotic algae → coral '
                         'turns white and eventually dies if temperatures remain elevated.\n'
                         '\n'
                         'EFFECTS OF CHANGED RAINFALL PATTERNS:\n'
                         'Drought-prone areas expand → grasslands may become deserts.\n'
                         'Wetter areas may support new species previously excluded by dryness.\n'
                         '\n'
                         'SEA LEVEL RISE:\n'
                         'Coastal and low-lying habitats (salt marshes, mangroves, coral atolls) at risk.\n'
                         'Many coastal species lose their habitat.',
              'heading': 'Climate Change and Species Distribution'},
             {'content': 'POLLUTION affects species distribution:\n'
                         '\n'
                         'AIR POLLUTION:\n'
                         'SO₂ from burning fossil fuels — indicator species lichens are very sensitive to SO₂ and are '
                         'absent from polluted urban areas. Their presence indicates clean air.\n'
                         'Nitrogen oxides → acid rain → acidification of soils and rivers → loss of acid-sensitive '
                         'species.\n'
                         '\n'
                         'WATER POLLUTION:\n'
                         'Nitrate and phosphate runoff (eutrophication) → algal blooms → oxygen depletion → fish die.\n'
                         'OIL SPILLS — coat bird feathers and mammal fur → prevents insulation and waterproofing → '
                         'death. Oil is toxic to many marine organisms.\n'
                         'PLASTIC POLLUTION — entanglement, ingestion by marine animals.\n'
                         '\n'
                         'INDICATOR SPECIES for water quality:\n'
                         'Mayfly larvae — only in clean, well-oxygenated water (absent from polluted rivers).\n'
                         'Rat-tailed maggots — tolerate very low oxygen (indicate polluted water).\n'
                         'Bloodworms — intermediate tolerance.\n'
                         '\n'
                         'HABITAT DESTRUCTION:\n'
                         'Deforestation, draining of wetlands, urbanisation and agricultural expansion destroy '
                         'habitats.\n'
                         'Habitat fragmentation — dividing continuous habitats into isolated patches reduces gene flow '
                         'between populations and increases local extinction risk.',
              'heading': 'Pollution and Habitat Destruction'}],
  'title': 'The Impact of Environmental Change',
  'triple_only': None,
  'variables': []},
 {'common_mistake': 'Food security is about HAVING ENOUGH food — not just producing food. Distribution and access are '
                    'equally important. Even when enough food is produced globally, millions go hungry due to unequal '
                    'distribution, poverty and conflict.',
  'equations': [],
  'fifas': [],
  'higher': 'Evaluate the relative significance of different threats to food security using data. Analyse the '
            'environmental impact and ethical dimensions of different solutions. Assess the trade-offs between food '
            'production efficiency and biodiversity conservation. Evaluate global distribution of food insecurity and '
            'the role of political, economic and biological factors.',
  'id': 'factors-affecting-food-security',
  'key_note': 'Food security: enough food for all. Threats: rising population, changing diets (more meat), new '
              'pests/pathogens, climate change, conflict. Solutions: high-yield varieties, GM crops, better '
              'irrigation, reducing waste, changing diets, fair distribution.',
  'matching': {'instruction': 'Match each threat to its description.',
               'pairs': [('Increasing birth rate', 'World population growing — more food needed to feed more people'),
                         ('Changing diets',
                          'Wealthier nations eating more meat — meat production uses far more resources than plants'),
                         ('New pests and pathogens',
                          'New crop diseases spread globally through trade and travel — devastating harvests'),
                         ('Climate change',
                          'Changing rainfall, temperatures and extreme weather disrupt agricultural production '
                          'worldwide')],
               'title': 'Threats to Food Security'},
  'quiz': [{'opts': [('Producing meat is far less efficient than producing plant food — much more land, water and '
                      'grain is needed to produce the same amount of nutrition',
                      True),
                     ('Meat contains fewer nutrients than plant food — so people still go hungry even if they eat it',
                      False),
                     ('Meat spoils faster than plant food — more waste occurs during transport', False),
                     ('Meat-based diets reduce birth rates — fewer people means less food is produced', False)],
            'q': 'Why does a shift towards more meat-based diets in developing countries threaten food security?',
            'wrong_explanations': {1: 'Meat is nutritious — the problem is the INEFFICIENCY of producing it (much more '
                                      'grain and water needed per unit of food produced).',
                                   2: 'Spoilage is an issue but the primary concern is the much greater LAND AND '
                                      'RESOURCE USE of meat production vs equivalent plant nutrition.',
                                   3: 'Birth rate and meat consumption are not directly linked in this way — the issue '
                                      'is resource efficiency.'}},
           {'opts': [('A new pathogen that destroys wheat crops worldwide', True),
                     ('A country imposing trade tariffs on imported food', False),
                     ('Rising fuel costs making food transport more expensive', False),
                     ('Political instability preventing farmers from accessing markets', False)],
            'q': 'Which of the following is a biological factor threatening food security?',
            'wrong_explanations': {1: 'Trade tariffs are an ECONOMIC/POLITICAL factor — not a biological one.',
                                   2: 'Fuel costs are an ECONOMIC factor — not biological.',
                                   3: 'Political instability is a POLITICAL/SOCIAL factor — not biological. Biological '
                                      'factors include pests, pathogens, climate change effects on growth.'}}],
  'rp': None,
  'spec': '4.7.5.1',
  'summary': 'Describe the biological factors threatening food security globally.',
  'theory': [{'content': 'FOOD SECURITY means having enough food to feed a population.\n'
                         '\n'
                         'A country or region has food security when all people have access to sufficient, safe and '
                         'nutritious food.\n'
                         '\n'
                         'FOOD INSECURITY occurs when:\n'
                         'Food production cannot meet demand — too little food produced.\n'
                         'Food is unequally distributed — some have excess, others starve.\n'
                         'Food is unaffordable — people cannot access available food.\n'
                         '\n'
                         'Global food security is threatened by several biological factors:\n'
                         'The world population is currently over 8 billion and still growing.\n'
                         'Food demand is increasing, especially in developing countries.\n'
                         'Climate change is disrupting agricultural patterns worldwide.',
              'heading': 'What Is Food Security?'},
             {'content': '1. INCREASING BIRTH RATE:\n'
                         'World population growing rapidly — more mouths to feed.\n'
                         'Food production must increase to keep pace.\n'
                         '\n'
                         '2. CHANGING DIETS IN DEVELOPED COUNTRIES:\n'
                         'As countries develop economically, diets shift towards more meat and dairy.\n'
                         'Meat production requires far more land, water and grain than plant-based food.\n'
                         'Scarce food resources are transported around the world — not always to those who need it '
                         'most.\n'
                         '\n'
                         '3. NEW PESTS AND PATHOGENS:\n'
                         'New disease-causing microorganisms or pests can devastate crops and livestock.\n'
                         'Examples: wheat rust (fungus), blight (oomycete), foot-and-mouth disease in cattle.\n'
                         'Global travel and trade spread new pests faster than ever.\n'
                         '\n'
                         '4. ENVIRONMENTAL CHANGE:\n'
                         'Climate change → changing rainfall, temperatures, growing seasons.\n'
                         'Some regions becoming too hot and dry to grow current crops.\n'
                         'Rising sea levels reduce agricultural land.\n'
                         'Extreme weather events (floods, droughts) destroy harvests.\n'
                         '\n'
                         '5. CONFLICT AND POLITICS:\n'
                         'War and political instability disrupt farming and food distribution.\n'
                         'Trade restrictions limit access to food in some regions.\n'
                         '\n'
                         '6. COST OF AGRICULTURAL RESOURCES:\n'
                         'Fertilisers, pesticides and farm machinery are expensive.\n'
                         'Smallholder farmers in developing countries may lack access.',
              'heading': 'Biological Factors Threatening Food Security'},
             {'content': 'INCREASING FOOD PRODUCTION:\n'
                         'High-yield crop varieties — genetically improved strains that produce more food per '
                         'hectare.\n'
                         'Genetically modified (GM) crops — engineered for pest resistance, drought tolerance, higher '
                         'yield.\n'
                         'Better irrigation — efficient water use in dry regions.\n'
                         'Fertilisers — increase soil nutrient levels → better crop growth.\n'
                         'Pesticides — reduce crop losses to insects and disease.\n'
                         'Intensive farming — maximise yield per unit area.\n'
                         '\n'
                         'REDUCING FOOD WASTE:\n'
                         'Improved storage and distribution to reduce spoilage.\n'
                         'Better packaging and refrigeration.\n'
                         '\n'
                         'CHANGING DIETS:\n'
                         'Moving towards more plant-based diets — less resource-intensive.\n'
                         'Insect farming — insects convert plant material to protein more efficiently than livestock.\n'
                         '\n'
                         'FAIR DISTRIBUTION:\n'
                         'International food aid, trade reform, addressing poverty.\n'
                         'Better infrastructure in developing countries.',
              'heading': 'Solutions to Food Insecurity'}],
  'title': 'Factors Affecting Food Security',
  'triple_only': 'Factors affecting food security (4.7.5.1) is biology-only. Includes biological threats to food '
                 'security and the range of solutions to improve global food production.',
  'variables': []},
 {'common_mistake': 'Restricting farm animal movement improves efficiency because it reduces ENERGY LOST IN '
                    'RESPIRATION — not because it makes animals grow faster through some other mechanism. The energy '
                    'that would have been used for movement is retained as biomass instead.',
  'equations': [],
  'fifas': [],
  'higher': 'Evaluate ethical objections to intensive farming using evidence about animal welfare. Assess '
            'environmental impacts: eutrophication from fertiliser run-off, pesticide effects on non-target organisms '
            'including bees, antibiotic resistance from routine use in livestock. Evaluate biological pest control vs '
            'chemical pesticides in specific contexts — compare advantages, disadvantages and ecological risks.',
  'id': 'farming-techniques',
  'key_note': 'Intensive farming: restrict movement + control temperature → less respiration → more biomass. '
              'High-protein feed, pesticides, herbicides, fertilisers, greenhouses improve yield. Ethical concerns: '
              'animal welfare, eutrophication, biodiversity loss. Biological control: natural predators instead of '
              'pesticides.',
  'matching': {'instruction': 'Match each farming technique to how it improves food production.',
               'pairs': [('Restricting animal movement',
                          'Less energy used in respiration for muscle activity — more energy retained as body mass'),
                         ('Controlling temperature',
                          'Less energy spent maintaining body temperature — more energy available for growth'),
                         ('Using fertilisers',
                          'Adds essential minerals (NPK) to soil — improves crop growth and yield'),
                         ('Biological control',
                          'Uses natural predators to control pests — no chemical residues, less damage to non-target '
                          'species')],
               'title': 'Farming Methods'},
  'quiz': [{'opts': [('Battery chickens cannot exhibit natural behaviours and are kept in conditions that cause '
                      'physical and psychological suffering',
                      True),
                     ('Intensively farmed chickens produce lower-quality eggs — ethical concern about food standards',
                      False),
                     ('Intensive farming uses more water than free-range farming — wasteful of resources', False),
                     ('Battery farming produces more greenhouse gases than other methods', False)],
            'q': 'Why do some people have ethical objections to intensive farming of chickens?',
            'wrong_explanations': {1: 'Egg quality varies by diet and conditions, but the PRIMARY ethical objection is '
                                      'about ANIMAL WELFARE — inability to move, spread wings or behave naturally.',
                                   2: 'Water use may be a concern but is not the primary ethical objection to '
                                      'intensive farming.',
                                   3: 'Greenhouse gas emissions are an environmental concern — the ethical objection '
                                      'specifically is about animal welfare and suffering.'}},
           {'opts': [('Biological control uses natural predators — no chemical residues on food and less damage to '
                      'non-target species',
                      True),
                     ('Biological control always acts faster than pesticides', False),
                     ('Biological control eliminates all pests completely', False),
                     ('Biological control is always cheaper than pesticides', False)],
            'q': 'What is the advantage of using biological control instead of pesticides to manage crop pests?',
            'wrong_explanations': {1: 'Biological control is typically SLOWER than chemical pesticides — the advantage '
                                      'is specificity and no chemical residues.',
                                   2: 'Biological control reduces pest populations — it rarely eliminates them '
                                      'completely. Natural predator-prey relationships maintain a balance.',
                                   3: 'Biological control can be expensive to develop and implement — the advantage is '
                                      'environmental and health benefits, not necessarily cost.'}}],
  'rp': None,
  'spec': '4.7.5.2',
  'summary': 'Describe how modern farming techniques improve food production efficiency and evaluate their ethics.',
  'theory': [{'content': 'The EFFICIENCY of food production can be improved by reducing energy losses from food '
                         'animals to the environment.\n'
                         '\n'
                         'METHODS FOR ANIMALS:\n'
                         'RESTRICTING MOVEMENT:\n'
                         'Animals that move less use less energy in respiration → more energy retained as body mass.\n'
                         'Factory farming — animals kept in small enclosures (battery hens, veal calves).\n'
                         '\n'
                         'CONTROLLING TEMPERATURE:\n'
                         'Warm environments mean less energy spent maintaining body temperature.\n'
                         'Indoor farming with controlled heating.\n'
                         '\n'
                         'HIGH-PROTEIN FEED:\n'
                         'Animals fed concentrated, high-protein foods → faster growth.\n'
                         'Fish meal, soya protein used in poultry and pig farming.\n'
                         '\n'
                         'ANTIBIOTICS (historically):\n'
                         'Preventing disease → less energy lost to fighting infection → faster growth.\n'
                         '(Now regulated in many countries due to antibiotic resistance concerns.)\n'
                         '\n'
                         'METHODS FOR CROPS:\n'
                         'PESTICIDES — kill insects, fungi, bacteria that damage crops.\n'
                         'HERBICIDES — kill weeds competing with crops for light and nutrients.\n'
                         'FERTILISERS — add essential minerals (NPK) to soil → better crop growth.\n'
                         'GREENHOUSES — controlled temperature, CO₂ levels, watering → extended growing season, higher '
                         'yields.\n'
                         'MONOCULTURE — growing one crop type over large areas → economical but reduces biodiversity.',
              'heading': 'Increasing Farming Efficiency'},
             {'content': 'INTENSIVE FARMING raises ETHICAL CONCERNS:\n'
                         '\n'
                         'ANIMAL WELFARE:\n'
                         'Battery hens cannot spread wings or exhibit natural behaviour.\n'
                         'Veal calves confined in small crates — restricted movement causes distress.\n'
                         'Pigs in gestation crates unable to turn around.\n'
                         'Many consumers and scientists consider these practices inhumane.\n'
                         '\n'
                         'ENVIRONMENTAL CONCERNS:\n'
                         'Intensive use of fertilisers → EUTROPHICATION — excess nutrients in waterways → algal blooms '
                         '→ deoxygenation → fish death.\n'
                         'Pesticide runoff damages non-target species (bees, other insects).\n'
                         'Monoculture reduces habitat diversity and biodiversity.\n'
                         'Greenhouse gas emissions from livestock (methane from cattle).\n'
                         '\n'
                         'BALANCING ACT:\n'
                         'Intensive farming produces more food more cheaply → feeds more people.\n'
                         'But ethical and environmental costs are significant.\n'
                         'Consumers, farmers and governments must balance food production needs with animal welfare '
                         'and environmental protection.\n'
                         '\n'
                         'ORGANIC FARMING:\n'
                         'No pesticides, artificial fertilisers or routine antibiotics.\n'
                         'Higher animal welfare standards.\n'
                         'Lower yields but reduced environmental impact.\n'
                         'More expensive — not accessible to all.',
              'heading': 'Ethical Considerations'},
             {'content': 'BIOLOGICAL CONTROL uses natural predators or parasites to control pests — an alternative to '
                         'pesticides.\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Ladybirds and lacewings to control aphids on crops.\n'
                         'Bacillus thuringiensis bacteria (Bt) — produces toxins lethal to caterpillars but safe for '
                         'other organisms.\n'
                         'Sterile insect technique — release sterile male insects to reduce pest populations.\n'
                         'Parasitic wasps to control whitefly in greenhouses.\n'
                         '\n'
                         'ADVANTAGES over pesticides:\n'
                         'No chemical residues on food.\n'
                         'Specific to target pest — less impact on other species.\n'
                         'Sustainable — natural populations maintain themselves.\n'
                         'No pesticide resistance developing.\n'
                         '\n'
                         'DISADVANTAGES:\n'
                         'Slower acting than pesticides.\n'
                         'Can be less predictable — natural populations fluctuate.\n'
                         'Introduced species can become invasive (if not chosen carefully).\n'
                         'Not effective against all pests.',
              'heading': 'Biological Control'}],
  'title': 'Farming Techniques',
  'triple_only': 'Farming techniques (4.7.5.2) is biology-only. Includes methods to improve efficiency (restricting '
                 'movement, controlling temperature), ethical objections to intensive farming, and biological pest '
                 'control.',
  'variables': []},
 {'common_mistake': 'Fishing quotas are based on the SCIENCE of population biology — not arbitrary limits. They are '
                    'calculated to allow fish to reproduce faster than they are caught. Net size rules let YOUNG fish '
                    'escape — young fish are the future breeding population, so their survival is critical.',
  'equations': [],
  'fifas': [],
  'higher': 'Evaluate the effectiveness of different fish stock management strategies using population data. Analyse '
            'problems of international enforcement of fishing quotas. Evaluate the environmental and economic '
            'advantages and disadvantages of aquaculture. Interpret graphs of fish population data over time and '
            'relate changes to management interventions.',
  'id': 'sustainable-fisheries',
  'key_note': 'Sustainable fishing: catch rate ≤ reproduction rate. Methods: quotas (limit annual catch), minimum net '
              'size (let juveniles escape), exclusion zones, seasonal bans. Fish farming: controlled production but '
              'risks include disease, pollution, genetic mixing with wild stocks. Monitor populations scientifically '
              'to set quotas.',
  'matching': {'instruction': 'Match each method to how it helps maintain fish stocks.',
               'pairs': [('Fishing quotas', 'Legally limits annual catch — based on scientific population estimates'),
                         ('Minimum net mesh size',
                          'Allows young fish to escape — they grow, reproduce and maintain future populations'),
                         ('Exclusion zones',
                          'No-catch areas around breeding grounds — fish can reproduce without disturbance'),
                         ('Fish farming', 'Controlled production in tanks or cages — reduces pressure on wild stocks')],
               'title': 'Sustainable Fishing Methods'},
  'quiz': [{'opts': [('Young fish can escape through larger mesh — they reach adulthood, reproduce and maintain future '
                      'stocks',
                      True),
                     ('Larger mesh catches more adult fish per trawl — increasing fishing efficiency', False),
                     ('Small fish are inedible — minimum mesh size prevents catching commercially worthless fish',
                      False),
                     ('Larger mesh allows water to flow through more easily — reducing fuel costs', False)],
            'q': 'Why are minimum mesh size rules important for maintaining sustainable fish populations?',
            'wrong_explanations': {1: 'Larger mesh actually catches FEWER fish per trawl — the benefit is '
                                      'conservation, not efficiency.',
                                   2: 'Small fish ARE edible and have commercial value — but catching them prevents '
                                      'them from reaching reproductive age.',
                                   3: 'Water flow through mesh is a minor consideration — conservation of juvenile '
                                      'fish is the primary reason for minimum mesh size rules.'}},
           {'opts': [('High fish density in enclosures leads to rapid disease spread — often requiring heavy '
                      'antibiotic use',
                      True),
                     ('Fish farms always produce lower-quality fish than wild-caught fish', False),
                     ('Fish farming uses more water than wild fishing', False),
                     ('Farmed fish grow more slowly than wild fish', False)],
            'q': 'What is a potential disadvantage of fish farming compared to wild capture fishing?',
            'wrong_explanations': {1: 'Quality varies — some farmed fish (e.g. salmon) are considered high quality. '
                                      'The primary concern is disease, pollution and antibiotic use.',
                                   2: "Fish farms use water from rivers, sea or controlled systems — 'more water' is "
                                      'not a defined disadvantage. The specific concerns are pollution of that water.',
                                   3: 'Farmed fish often grow FASTER than wild fish due to controlled feeding and '
                                      'breeding — this is one of the advantages.'}}],
  'rp': None,
  'spec': '4.7.5.3',
  'summary': 'Describe methods used to maintain fish stocks at sustainable levels.',
  'theory': [{'content': 'OVERFISHING has led to dramatic declines in many fish populations worldwide.\n'
                         '\n'
                         'PROBLEM:\n'
                         'MODERN FISHING TECHNOLOGY — sonar, large nets, factory ships — allows far more fish to be '
                         'caught than can reproduce.\n'
                         'If fish are caught faster than they can reproduce, the population COLLAPSES.\n'
                         'Many species (Atlantic cod, North Sea herring) have been fished to critically low levels.\n'
                         '\n'
                         'CONSEQUENCES:\n'
                         'Collapsing fish populations → fishing industries lose income and livelihoods.\n'
                         'Ecosystem disruption — removing top predators disrupts food webs.\n'
                         'Food insecurity — billions of people depend on fish as their primary protein source.\n'
                         '\n'
                         'SUSTAINABILITY:\n'
                         'A SUSTAINABLE fish stock is maintained at a level where fish can be harvested indefinitely — '
                         'the catch rate does not exceed the reproduction rate.\n'
                         '\n'
                         'Scientific monitoring: regular surveys of fish populations → set sustainable catch limits.',
              'heading': 'Why Fish Stocks Are Declining'},
             {'content': 'FISHING QUOTAS:\n'
                         'Governments set LIMITS on how many fish can be caught per year.\n'
                         'Based on scientific estimates of population size and reproduction rates.\n'
                         'Enforced by fisheries inspectors — ships must report catches.\n'
                         'Example: European Common Fisheries Policy sets quotas for North Sea species.\n'
                         '\n'
                         'NET SIZE RESTRICTIONS:\n'
                         'Minimum mesh size rules ensure small, young fish can escape through the net.\n'
                         'Juvenile fish escape → grow to adulthood → reproduce → maintain the population.\n'
                         'Small mesh nets would catch juveniles → no fish left to breed next year.\n'
                         '\n'
                         'FISHING EXCLUSION ZONES:\n'
                         'No-catch areas around breeding grounds or areas where stocks are critically low.\n'
                         'Allows fish populations to recover without pressure.\n'
                         'Marine Protected Areas (MPAs) also protect habitat.\n'
                         '\n'
                         'SEASONS AND BANS:\n'
                         'Banning fishing during breeding season → fish can reproduce before being caught.\n'
                         'Temporary bans on specific species when populations are critically low.',
              'heading': 'Methods to Maintain Sustainable Fish Stocks'},
             {'content': 'FISH FARMING (AQUACULTURE) grows fish commercially in controlled environments — an '
                         'alternative to wild capture fishing.\n'
                         '\n'
                         'METHODS:\n'
                         'Caged fish in sea lochs, ponds or tanks (salmon, trout, carp, tilapia).\n'
                         'Controlled feeding, breeding and health management.\n'
                         '\n'
                         'ADVANTAGES:\n'
                         'Reduces pressure on wild fish stocks.\n'
                         'Consistent supply — not dependent on weather or wild population changes.\n'
                         'Can be located near markets — reduced transportation.\n'
                         'Fish can be selectively bred for faster growth.\n'
                         '\n'
                         'DISADVANTAGES:\n'
                         'HIGH DENSITY → disease spreads easily → heavy antibiotic use.\n'
                         'Sea cage escapes → farmed fish interbreed with wild stocks → genetic issues.\n'
                         'Water POLLUTION — excess feed and faeces pollute surrounding water.\n'
                         "REQUIRES FEED — often uses wild-caught 'trash fish' or fishmeal → still impacts ocean "
                         'ecosystems.\n'
                         'High energy input → expensive.\n'
                         '\n'
                         'SUSTAINABLE AQUACULTURE:\n'
                         'Using plant-based feeds where possible.\n'
                         'Closed recirculating systems — no pollution of natural water.\n'
                         'Vaccination instead of antibiotics.',
              'heading': 'Fish Farming (Aquaculture)'}],
  'title': 'Sustainable Fisheries',
  'triple_only': 'Sustainable fisheries (4.7.5.3) is biology-only. Covers methods to maintain sustainable fish stocks '
                 'including quotas, net size restrictions and exclusion zones, and fish farming with its advantages '
                 'and disadvantages.',
  'variables': []},
 {'common_mistake': 'GM crops are NOT the same as selective breeding — selective breeding uses existing natural '
                    'variation over generations. Genetic engineering directly inserts specific genes from other '
                    'species. Both aim to improve traits, but GM is faster and more precise. Also: mycoprotein (Quorn) '
                    'comes from a FUNGUS — not an animal or plant.',
  'equations': [],
  'fifas': [],
  'higher': 'Evaluate the potential and risks of GM crops using scientific evidence — distinguish evidence-based '
            'concerns from speculative fears. Discuss social and ethical issues: corporate patent control, labelling, '
            'consumer choice, equity of access in developing countries. Evaluate mycoprotein as sustainable food — '
            "compare resource efficiency with animal protein production. Assess biotechnology's role in addressing "
            'food security.',
  'id': 'role-of-biotechnology',
  'key_note': 'Biotechnology: traditional (fermentation, selective breeding) + modern (GM crops, tissue culture, '
              'mycoprotein). GM crops: higher yield, pest resistance (Bt), herbicide tolerance, improved nutrition '
              '(Golden Rice), drought tolerance. Concerns: gene flow, effect on non-target organisms, health unknowns, '
              'corporate patents. Mycoprotein (Quorn): Fusarium fungus in fermenters.',
  'matching': {'instruction': 'Match each GM crop to its modification and benefit.',
               'pairs': [('Golden Rice',
                          'Engineered to produce beta-carotene — helps prevent Vitamin A deficiency and blindness'),
                         ('Bt crops',
                          'Contain bacterial gene producing insecticide — reduces need for chemical pesticides'),
                         ('Herbicide-resistant crops',
                          'Survive herbicide spraying — allows weeds to be killed without damaging the crop'),
                         ('Mycoprotein (Quorn)',
                          'Fungus Fusarium grown in fermenters on glucose — efficient high-protein meat substitute')],
               'title': 'GM Crop Applications'},
  'quiz': [{'opts': [('The fungus Fusarium — grown in industrial fermenters and processed into a high-protein meat '
                      'substitute',
                      True),
                     ('Modified soya beans — a GM plant engineered to have higher protein content', False),
                     ('A type of algae grown in open-air ponds using sunlight', False),
                     ('Yeast — the same organism used in bread-making and brewing', False)],
            'q': 'What is the source of mycoprotein (Quorn)?',
            'wrong_explanations': {1: 'Soya is used as a protein source but is not mycoprotein — mycoprotein '
                                      'specifically refers to Fusarium fungus protein.',
                                   2: 'Quorn uses a fungus (Fusarium venenatum), not algae — though algae-based '
                                      'proteins are being developed as future food sources.',
                                   3: 'Yeast is also a fungus used in food production, but Quorn/mycoprotein is '
                                      'specifically from Fusarium venenatum, not yeast.'}},
           {'opts': [('GM herbicide-resistance genes could spread to wild plant relatives via pollen — creating '
                      "herbicide-resistant 'superweeds' that are hard to control",
                      True),
                     ('Herbicide-resistant crops absorb more herbicide into their tissues — making the food more toxic',
                      False),
                     ('The crops grow too fast and take over natural habitats', False),
                     ('Herbicide-resistant crops produce less yield than normal crops', False)],
            'q': 'Why are some environmentalists concerned about herbicide-resistant GM crops?',
            'wrong_explanations': {1: "GM crops are designed to withstand herbicide — they don't absorb more into "
                                      'edible tissue. The concern is about GENE FLOW to wild plants.',
                                   2: 'GM herbicide-resistant crops do not inherently grow faster or invade habitats — '
                                      'the specific concern is gene flow via pollen.',
                                   3: 'GM crops are developed specifically to MAINTAIN or INCREASE yield — not reduce '
                                      'it.'}}],
  'rp': None,
  'spec': '4.7.5.4',
  'summary': 'Describe how modern biotechnology can increase food production and evaluate its applications.',
  'theory': [{'content': 'BIOTECHNOLOGY uses biological systems and organisms to develop technologies and products — '
                         'including foods.\n'
                         '\n'
                         'TRADITIONAL BIOTECHNOLOGY:\n'
                         'Fermentation — using microorganisms to produce food and drink (bread, yogurt, cheese, beer, '
                         'wine).\n'
                         'Selective breeding — improving crop yields and animal traits over generations.\n'
                         '\n'
                         'MODERN BIOTECHNOLOGY:\n'
                         'Genetic engineering of crops and livestock.\n'
                         'Micropropagation (tissue culture) for cloning high-yield plant varieties.\n'
                         'Fermentation on industrial scale — mycoprotein production (Quorn).\n'
                         'Genetically modified microorganisms producing medicines (insulin).\n'
                         '\n'
                         'Mycoprotein (QUORN):\n'
                         'Fungus Fusarium grown in large fermenters on glucose syrup.\n'
                         'Produces high-protein mycoprotein — used as meat substitute.\n'
                         'Efficient: converts carbohydrate to protein faster than animals.\n'
                         'Low-fat, sustainable food source.',
              'heading': 'Biotechnology in Food Production'},
             {'content': 'GM CROPS have had their DNA modified to improve characteristics:\n'
                         '\n'
                         'EXAMPLES:\n'
                         'Golden Rice — engineered to produce beta-carotene (precursor to Vitamin A).\n'
                         'Could prevent Vitamin A deficiency in developing countries → prevent blindness.\n'
                         '\n'
                         'Bt Crops — contain gene from bacterium Bacillus thuringiensis.\n'
                         'Produce toxins lethal to specific insect pests.\n'
                         'Reduces need for chemical insecticides.\n'
                         '\n'
                         'Herbicide-resistant crops — engineered to survive herbicide spraying.\n'
                         'Allows farmers to spray entire fields, killing weeds but not the crop.\n'
                         '\n'
                         'Drought-tolerant crops — engineered to survive dry conditions.\n'
                         'Critical for food security in climate-change-affected regions.\n'
                         '\n'
                         'ADVANTAGES:\n'
                         'Higher yields — more food per hectare.\n'
                         'Reduced pesticide use (Bt crops).\n'
                         'Improved nutritional content (Golden Rice).\n'
                         'Better adaptation to climate change.\n'
                         'Reduced food waste (longer shelf life varieties).',
              'heading': 'Genetically Modified Crops'},
             {'content': 'CONCERNS about GM technology:\n'
                         '\n'
                         'ENVIRONMENTAL:\n'
                         "Gene flow — GM genes may spread to wild relatives via pollen → 'superweeds' resistant to "
                         'herbicides.\n'
                         'Effect on non-target organisms — Bt toxin affecting non-pest insects (bees, butterflies).\n'
                         'Reduced biodiversity — monocultures of GM crops replacing wild varieties.\n'
                         'Unknown long-term ecosystem effects.\n'
                         '\n'
                         'HEALTH:\n'
                         'Allergenicity — new proteins introduced might trigger allergies.\n'
                         'Antibiotic resistance markers — used in development, may transfer to gut bacteria.\n'
                         'Long-term health effects not yet fully understood.\n'
                         '\n'
                         'SOCIAL/ECONOMIC:\n'
                         'Patenting — large corporations (Monsanto/Bayer) own GM seed patents.\n'
                         'Farmers must buy new seeds each year — cannot save seeds.\n'
                         'Dependence on corporate suppliers, especially in developing countries.\n'
                         'GM crops may not benefit small-scale farmers.\n'
                         '\n'
                         'REGULATION:\n'
                         'GM crops are tightly regulated in the EU and UK.\n'
                         'Extensive safety testing required before approval.\n'
                         'Labelling requirements so consumers can make informed choices.',
              'heading': 'Concerns About GM Crops'}],
  'title': 'The Role of Biotechnology',
  'triple_only': 'Role of biotechnology (4.7.5.4) is biology-only. Covers GM crops (advantages and concerns), '
                 'mycoprotein production, and the broader role of modern biotechnology in addressing food security.',
  'variables': []}],

}
