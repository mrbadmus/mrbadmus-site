"""Biology · Bioenergetics — the MRB-338 expansion of `metabolism`.

One leaf only: AQA 8461 §4.4.2.4. The original twelve rows in
`bioenergetics.py` take catabolism's definition, deamination in the
liver, glycogen as the animal storage molecule, the kidneys removing
urea, why enzymes are needed for metabolic reactions, classifying starch
digestion as catabolic, why ammonia is converted to urea, predicting the
fate of excess protein, protein synthesis as anabolic and needing ATP,
comparing respiration with protein synthesis, illness on a protein-free
diet, and a growing cell's higher anabolic rate.

This file takes what they leave: the named anabolic reactions the
baseline does not reach — cellulose synthesis, fat synthesis, DNA
replication — and the named catabolic ones beyond starch digestion — fat
and protein digestion by name, glycolysis as respiration's first step —
each recalled, classified and compared in turn; the urea pathway worked
onward to the kidneys; and a run of ATP-balance arithmetic treating a
cell's catabolic and anabolic totals as a simple net-energy sum.

⚠️ Metabolic rate and its named factors (body size, muscle mass, exercise,
temperature, thyroxine) are Higher-extension content this base subtopic
does not reach, exactly as `bioenergetics.py`'s own docstring rules out —
nothing here touches them.
"""

TOPIC = "bioenergetics"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═══════════════════════════════════════
    {
        "id": "ks4-metabolism-e05",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define anabolism.",
        "options": [
            "Building larger molecules from smaller ones, using energy",
            "Breaking larger molecules into smaller ones, releasing energy",
            "Moving substances across a membrane against a gradient",
            "Copying a cell's DNA before it divides",
        ],
        "correct_index": 0,
        "why": "Anabolic reactions build larger molecules from smaller ones, and this needs "
               "energy from respiration.",
    },
    {
        "id": "ks4-metabolism-e06",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process that joins glucose molecules together to build cellulose.",
        "options": [
            "Deamination in the liver",
            "Cellulose synthesis",
            "Glycolysis",
            "Digestion",
        ],
        "correct_index": 1,
        "why": "Cellulose synthesis joins glucose molecules together to build the structural "
               "polymer cellulose.",
    },
    {
        "id": "ks4-metabolism-e07",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two types of molecule joined together to form a triglyceride.",
        "options": [
            "Amino acids and nitrate ions",
            "Glucose and oxygen",
            "Fatty acids and glycerol",
            "Starch and cellulose",
        ],
        "correct_index": 2,
        "why": "Fatty acids and glycerol are joined together to build a triglyceride, a fat "
               "molecule.",
    },
    {
        "id": "ks4-metabolism-e08",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process that copies a cell's DNA before it divides.",
        "options": [
            "Deamination",
            "Glycolysis",
            "Cellulose synthesis",
            "DNA replication",
        ],
        "correct_index": 3,
        "why": "DNA replication copies a cell's DNA, an anabolic reaction, before the cell "
               "divides.",
    },
    {
        "id": "ks4-metabolism-e09",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the enzyme that digests fat into fatty acids and glycerol.",
        "options": [
            "Lipase",
            "Protease",
            "Amylase",
            "Catalase",
        ],
        "correct_index": 0,
        "why": "Lipase is the enzyme that breaks fat down into fatty acids and glycerol.",
    },
    {
        "id": "ks4-metabolism-e10",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the enzyme that digests protein into amino acids.",
        "options": [
            "Amylase",
            "Protease",
            "Lipase",
            "Lactase",
        ],
        "correct_index": 1,
        "why": "Protease is the enzyme that breaks protein down into amino acids.",
    },
    {
        "id": "ks4-metabolism-e11",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the first stage of respiration, which takes place in the cytoplasm.",
        "options": [
            "Deamination",
            "DNA replication",
            "Glycolysis",
            "Fermentation",
        ],
        "correct_index": 2,
        "why": "Glycolysis is the first stage of respiration, breaking glucose down in the "
               "cytoplasm.",
    },
    {
        "id": "ks4-metabolism-e12",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these is an example of a catabolic reaction.",
        "options": [
            "Joining amino acids into a protein",
            "Joining glucose molecules into starch",
            "Joining fatty acids and glycerol into a fat",
            "Breaking starch down into glucose",
        ],
        "correct_index": 3,
        "why": "Breaking starch down into glucose is catabolic; the other three all build "
               "larger molecules and so are anabolic.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════
    {
        "id": "ks4-metabolism-s05",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify DNA replication as anabolic or catabolic, and explain.",
        "options": [
            "Anabolic; it builds new DNA strands from individual nucleotides",
            "Catabolic; it breaks an existing DNA strand into nucleotides",
            "Anabolic; it releases energy as new DNA strands form",
            "Catabolic; it uses ATP to break the cell in two",
        ],
        "correct_index": 0,
        "why": "DNA replication builds new strands from smaller nucleotide units, which "
               "makes it an anabolic reaction.",
    },
    {
        "id": "ks4-metabolism-s06",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cellulose synthesis is classed as an anabolic reaction.",
        "options": [
            "It breaks a large starch molecule down into smaller glucose units for "
            "storage",
            "It joins many glucose molecules together into a larger structural molecule",
            "It releases energy as the plant cell wall forms",
            "It uses no energy, since glucose is already available",
        ],
        "correct_index": 1,
        "why": "Joining many glucose units into the larger cellulose molecule is building "
               "up, which makes it anabolic.",
    },
    {
        "id": "ks4-metabolism-s07",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify the digestion of fat into fatty acids and glycerol as anabolic or "
               "catabolic, and explain.",
        "options": [
            "Anabolic; it builds a larger fat molecule from smaller parts",
            "Anabolic; it releases energy as the fat molecule forms",
            "Catabolic; it breaks a large fat molecule into smaller molecules",
            "Catabolic; it uses ATP to join fatty acids to glycerol",
        ],
        "correct_index": 2,
        "why": "Breaking a large fat molecule into smaller fatty acid and glycerol molecules "
               "is catabolic.",
    },
    {
        "id": "ks4-metabolism-s08",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why glycolysis is described as the first stage of respiration.",
        "options": [
            "It is the stage where oxygen is used to break glucose down completely",
            "It is the stage where carbon dioxide and water are formed as final products",
            "It is the stage where ATP is used to build new glucose molecules",
            "It is the stage in the cytoplasm where glucose is first broken down",
        ],
        "correct_index": 3,
        "why": "Glycolysis is the first step of respiration, breaking glucose down in the "
               "cytoplasm before the later stages.",
    },
    {
        "id": "ks4-metabolism-s09",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why building a triglyceride for long-term energy storage in a seed "
               "is classed as an anabolic reaction.",
        "options": [
            "It links fatty acid and glycerol molecules into one larger storage molecule",
            "It splits a stored fat molecule apart to release its energy",
            "It converts glucose directly into oxygen molecules without using cell energy",
            "It releases water as fatty acids and glycerol join together",
        ],
        "correct_index": 0,
        "why": "Building a triglyceride joins smaller molecules into a larger one, which is "
               "what makes it anabolic.",
    },
    {
        "id": "ks4-metabolism-s10",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says all metabolic reactions release energy. Correct this "
               "statement.",
        "options": [
            "This is correct; every metabolic reaction taking place in a cell releases "
            "some energy",
            "Anabolic reactions use energy to build molecules, while catabolic reactions "
            "release it",
            "No metabolic reaction releases any energy",
            "Reactions in the liver release energy; other reactions use it",
        ],
        "correct_index": 1,
        "why": "Metabolism includes both anabolic reactions, which use energy, and catabolic "
               "reactions, which release it.",
    },
    {
        "id": "ks4-metabolism-s11",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why deamination takes place specifically in the liver.",
        "options": [
            "The liver is where excess protein is first digested into amino acids",
            "The liver converts glucose into fat, producing ammonia as a waste product",
            "The liver removes the amino group from excess amino acids, forming ammonia",
            "The liver is where amino acids are first absorbed from the gut",
        ],
        "correct_index": 2,
        "why": "Deamination in the liver removes the amino group from excess amino acids, "
               "producing ammonia.",
    },
    {
        "id": "ks4-metabolism-s12",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ammonia is converted into urea rather than being excreted "
               "directly.",
        "options": [
            "Ammonia holds no nitrogen atoms, so the body cannot excrete it directly in "
            "urine",
            "Ammonia is a useful molecule, so the body keeps it in the blood",
            "Urea takes far less energy to make than ammonia does",
            "Ammonia is highly toxic, while urea is much less harmful to carry in the "
            "blood",
        ],
        "correct_index": 3,
        "why": "Ammonia is very toxic, so the liver converts it into the far less harmful "
               "urea before it travels in the blood.",
    },
    {
        "id": "ks4-metabolism-s13",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the enzymes needed to digest starch with those needed to digest fat.",
        "options": [
            "Starch is digested by amylase; fat is digested by lipase",
            "Starch is digested by lipase; fat is digested by protease",
            "Both are digested by exactly the same enzyme",
            "Starch is digested by protease; fat is digested by amylase",
        ],
        "correct_index": 0,
        "why": "Amylase digests starch into sugars, while a different enzyme, lipase, "
               "digests fat into fatty acids and glycerol.",
    },
    {
        "id": "ks4-metabolism-s14",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell increases its rate of protein synthesis. Explain what this means for "
               "its ATP use.",
        "options": [
            "ATP use falls, since building protein needs very little energy",
            "ATP use rises, since joining amino acids into protein needs energy",
            "ATP use stays the same, regardless of the rate of protein synthesis",
            "ATP is released rather than used during protein synthesis",
        ],
        "correct_index": 1,
        "why": "Protein synthesis is anabolic and needs ATP to join amino acids together, so "
               "a faster rate uses more ATP.",
    },
    {
        "id": "ks4-metabolism-s15",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the products of protein digestion, unlike those of starch "
               "digestion, can supply nitrogen to a cell.",
        "options": [
            "Amino acids and glucose both contain the same amount of nitrogen",
            "Starch digestion releases nitrogen gas as a by-product",
            "Amino acids contain nitrogen in their amino group; glucose does not",
            "Protein digestion releases no nitrogen of any kind",
        ],
        "correct_index": 2,
        "why": "Amino acids carry nitrogen in their amino group, while glucose, a "
               "carbohydrate, contains none.",
    },
    {
        "id": "ks4-metabolism-s16",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a plant cell carrying out rapid cellulose synthesis needs a good "
               "supply of glucose.",
        "options": [
            "Cellulose is built from amino acids, which are made from glucose",
            "Glucose is needed just to power the enzymes, not as a building block",
            "Cellulose synthesis releases glucose rather than using it",
            "Glucose molecules are joined together directly to build the cellulose",
        ],
        "correct_index": 3,
        "why": "Cellulose is a polymer of glucose, so building it directly requires a steady "
               "supply of glucose molecules.",
    },
    {
        "id": "ks4-metabolism-s17",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell respires 40 ATP worth of glucose and spends 25 ATP on protein "
               "synthesis in the same period. Determine how much ATP remains for other cell "
               "processes.",
        "options": [
            "15 ATP",
            "65 ATP",
            "40 ATP",
            "25 ATP",
        ],
        "correct_index": 0,
        "why": "40 ATP released minus 25 ATP spent on protein synthesis leaves 15 ATP for "
               "other processes.",
    },
    {
        "id": "ks4-metabolism-s18",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell's catabolic reactions release 90 ATP in an hour, and its anabolic "
               "reactions use 55 ATP in the same hour. Determine the net ATP gain for the "
               "cell.",
        "options": [
            "90 ATP",
            "35 ATP",
            "55 ATP",
            "145 ATP",
        ],
        "correct_index": 1,
        "why": "90 ATP released minus 55 ATP used leaves a net gain of 35 ATP.",
    },
    {
        "id": "ks4-metabolism-s19",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how much ATP a cell has left if it releases 70 ATP through "
               "respiration and spends 48 ATP building new proteins and DNA.",
        "options": [
            "70 ATP",
            "48 ATP",
            "22 ATP",
            "118 ATP",
        ],
        "correct_index": 2,
        "why": "70 ATP released minus 48 ATP spent leaves 22 ATP remaining.",
    },
    {
        "id": "ks4-metabolism-s20",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A liver cell deaminates excess amino acids and produces urea. Explain what "
               "happens to this urea next.",
        "options": [
            "It is stored permanently in the liver",
            "It is converted back into ammonia in the blood",
            "It is broken down further into carbon dioxide and water molecules",
            "It travels in the blood to the kidneys, where it is filtered out",
        ],
        "correct_index": 3,
        "why": "Urea made in the liver travels in the blood to the kidneys, where it is "
               "filtered out and excreted in urine.",
    },
    {
        "id": "ks4-metabolism-s21",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what a starch molecule and a protein molecule are broken down into "
               "during digestion.",
        "options": [
            "Starch is broken down into glucose; protein into amino acids",
            "Starch is broken down into amino acids; protein into glucose",
            "Both are broken down into exactly the same simple sugar",
            "Neither starch nor protein is broken down during digestion",
        ],
        "correct_index": 0,
        "why": "Digestion breaks starch down into glucose and protein down into amino acids, "
               "its own building blocks.",
    },
    {
        "id": "ks4-metabolism-s22",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a rapidly dividing cell needs a high rate of DNA replication as "
               "well as protein synthesis.",
        "options": [
            "Just one of the two daughter cells produced after division needs a full copy "
            "of the DNA",
            "Each new daughter cell needs its own complete copy of the DNA and its own "
            "proteins",
            "DNA replication happens just once protein synthesis has finished",
            "Dividing cells need no DNA until they have finished growing",
        ],
        "correct_index": 1,
        "why": "Every new daughter cell needs a full set of DNA and its own working "
               "proteins, so both processes must run at a high rate.",
    },
    {
        "id": "ks4-metabolism-s23",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why starch digestion is classified as catabolic, even though it "
               "needs an enzyme to happen.",
        "options": [
            "Needing an enzyme makes a reaction anabolic, regardless of what else it "
            "might do in the cell",
            "Starch digestion releases the enzyme amylase as one of its products",
            "It still breaks a large molecule down into smaller ones, which is what "
            "defines catabolism",
            "Starch digestion uses ATP to break the bonds within the starch molecule",
        ],
        "correct_index": 2,
        "why": "Whether a reaction needs an enzyme has no bearing on its classification; "
               "breaking a molecule down is what makes it catabolic.",
    },
    {
        "id": "ks4-metabolism-s24",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's liver is damaged and cannot convert ammonia into urea "
               "efficiently. Suggest the likely effect on their blood.",
        "options": [
            "Blood glucose would rise sharply, since ammonia converts directly into "
            "glucose molecules",
            "Blood oxygen would fall, since ammonia competes with oxygen in the blood",
            "Blood would carry more urea than normal, since deamination would speed up",
            "Blood would carry more ammonia than normal, since it is not being converted "
            "quickly enough",
        ],
        "correct_index": 3,
        "why": "If the liver cannot convert ammonia to urea efficiently, ammonia builds up "
               "in the blood instead of being safely converted.",
    },
    {
        "id": "ks4-metabolism-s25",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why fat digestion and protein digestion both count as catabolic "
               "reactions.",
        "options": [
            "Both break a larger molecule down into smaller molecules",
            "Both release nitrogen as a common waste product",
            "Both build larger molecules from smaller starting materials",
            "Both take place just inside the liver's own cells",
        ],
        "correct_index": 0,
        "why": "Both reactions break a large molecule into smaller ones, which is the "
               "defining feature of a catabolic reaction.",
    },
    {
        "id": "ks4-metabolism-s26",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how much ATP a cell has used on anabolic reactions if it releases "
               "120 ATP by respiration and finishes the hour with 65 ATP of that total "
               "unused.",
        "options": [
            "120 ATP",
            "55 ATP",
            "65 ATP",
            "185 ATP",
        ],
        "correct_index": 1,
        "why": "120 ATP released minus 65 ATP left unused means 55 ATP was spent on anabolic "
               "reactions.",
    },

    # ══ harder · h05–h26 ═══════════════════════════════════════
    {
        "id": "ks4-metabolism-h05",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that metabolism and respiration mean the same thing.",
        "options": [
            "It is correct; both terms describe exactly the same single reaction",
            "It is correct, provided the organism is respiring aerobically",
            "It is wrong; respiration is just one of the many reactions that make up "
            "metabolism",
            "It is wrong; metabolism and respiration have no meaningful connection",
        ],
        "correct_index": 2,
        "why": "Metabolism is the sum of all of an organism's chemical reactions, of which "
               "respiration is only one.",
    },
    {
        "id": "ks4-metabolism-h06",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist measures a cell's total ATP production and its total ATP use "
               "across an hour, and finds they are equal. Explain what this shows about the "
               "cell's anabolic and catabolic reactions.",
        "options": [
            "The cell is carrying out no catabolic reactions during that hour",
            "The cell is carrying out no anabolic reactions during that hour",
            "The cell's catabolic reactions have released more energy than its anabolic "
            "reactions have used up so far",
            "The cell's catabolic reactions are releasing exactly as much energy as its "
            "anabolic reactions are using",
        ],
        "correct_index": 3,
        "why": "Equal production and use of ATP means the energy released by catabolic "
               "reactions exactly matches the energy used by anabolic ones.",
    },
    {
        "id": "ks4-metabolism-h07",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant seedling germinating in complete darkness, using only "
               "its stored starch, still needs both anabolic and catabolic reactions to "
               "grow.",
        "options": [
            "Its cells still need to build new structures anabolically, powered by "
            "catabolic respiration of the starch",
            "A germinating seedling carries out just anabolic reactions until it reaches "
            "the light",
            "A germinating seedling carries out just catabolic reactions until it reaches "
            "the light",
            "Its stored starch supplies all of the finished structures the seedling will "
            "ever need, without any further building",
        ],
        "correct_index": 0,
        "why": "Respiring the stored starch (catabolic) releases the energy needed to build "
               "the seedling's new structures (anabolic).",
    },
    {
        "id": "ks4-metabolism-h08",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell increases both its rate of protein synthesis and its rate of "
               "respiration at the same time. Suggest why these two changes are linked.",
        "options": [
            "Protein synthesis supplies the ATP that respiration then uses up quickly",
            "Respiration supplies the extra ATP that faster protein synthesis needs",
            "The two processes have no real connection to one another",
            "Increasing one process decreases the other by the same amount",
        ],
        "correct_index": 1,
        "why": "Protein synthesis needs ATP, so a cell raising its rate of protein synthesis "
               "needs its respiration to supply more of it.",
    },
    {
        "id": "ks4-metabolism-h09",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the net ATP change for a cell that respires 150 ATP worth of "
               "glucose while spending 95 ATP on protein synthesis and 20 ATP on DNA "
               "replication in the same hour.",
        "options": [
            "150 ATP",
            "115 ATP",
            "35 ATP",
            "245 ATP",
        ],
        "correct_index": 2,
        "why": "150 ATP released minus (95 + 20) = 115 ATP spent leaves a net change of 35 "
               "ATP.",
    },
    {
        "id": "ks4-metabolism-h10",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a person with a damaged deamination pathway would "
               "show no other symptoms besides raised blood ammonia.",
        "options": [
            "It is correct; ammonia has no other effects anywhere else in the body",
            "It is correct, provided the kidneys are working normally",
            "It is wrong; the liver would also stop making urea, regardless of the "
            "pathway involved",
            "It is not entirely true; ammonia is toxic and would likely affect other "
            "tissues too",
        ],
        "correct_index": 3,
        "why": "Ammonia is toxic, so a build-up of it is likely to affect other tissues "
               "beyond simply raising its own blood concentration.",
    },
    {
        "id": "ks4-metabolism-h11",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell's catabolic reactions release 210 ATP across a day, and it ends the "
               "day having stored 40 ATP of that amount unused. Determine how much ATP the "
               "cell's anabolic reactions used.",
        "options": [
            "170 ATP",
            "210 ATP",
            "40 ATP",
            "250 ATP",
        ],
        "correct_index": 0,
        "why": "210 ATP released minus 40 ATP left unused means 170 ATP was used by anabolic "
               "reactions.",
    },
    {
        "id": "ks4-metabolism-h12",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the fate of the nitrogen in an amino acid with the fate of the "
               "carbon in a glucose molecule, once each has been fully broken down by the "
               "body.",
        "options": [
            "Both end up excreted as urea in urine",
            "The nitrogen ends up in urea; the carbon ends up in carbon dioxide",
            "The nitrogen ends up in carbon dioxide; the carbon ends up in urea",
            "Neither the nitrogen nor the carbon leaves the body in any form",
        ],
        "correct_index": 1,
        "why": "Nitrogen from a deaminated amino acid ends up in urea, while carbon from "
               "respired glucose ends up in carbon dioxide.",
    },
    {
        "id": "ks4-metabolism-h13",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that because digestion breaks food down, it must be the "
               "exact opposite of respiration. Evaluate this claim.",
        "options": [
            "It is correct; digestion and respiration reverse one another exactly",
            "It is correct, since both processes use exactly the same enzymes",
            "It is wrong; both digestion and respiration are catabolic, breaking "
            "molecules down rather than building them up",
            "It is wrong; digestion is anabolic, while respiration is catabolic",
        ],
        "correct_index": 2,
        "why": "Digestion and respiration are both catabolic reactions, so one is not the "
               "reverse of the other.",
    },
    {
        "id": "ks4-metabolism-h14",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bodybuilder eating far more protein than they need still "
               "excretes some of it as urea, rather than storing all of it as extra muscle.",
        "options": [
            "Protein is converted directly into fat once muscle growth stops",
            "The body can store unlimited amounts of protein once muscle mass increases "
            "enough during training",
            "Muscle growth uses no amino acids once a certain body mass is reached",
            "Amino acids beyond what is needed for growth are deaminated and their "
            "nitrogen excreted as urea",
        ],
        "correct_index": 3,
        "why": "The body cannot store surplus protein, so amino acids beyond what growth "
               "needs are deaminated, with their nitrogen excreted as urea.",
    },
    {
        "id": "ks4-metabolism-h15",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that anabolic reactions are 'good' for a cell and "
               "catabolic reactions are 'bad'.",
        "options": [
            "It is wrong; a cell needs both working together, since anabolic reactions "
            "depend on the energy catabolic ones release",
            "It is correct; a healthy cell should carry out just anabolic reactions",
            "It is correct; catabolic reactions damage the cell that carries them out",
            "It is wrong; a cell needs just catabolic reactions once it stops growing",
        ],
        "correct_index": 0,
        "why": "Anabolic reactions rely on the energy catabolic reactions release, so a cell "
               "genuinely needs both working together.",
    },
    {
        "id": "ks4-metabolism-h16",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A liver cell's rate of deamination rises sharply after a very high-protein "
               "meal. Predict the effect on the concentration of urea in the blood soon "
               "afterwards.",
        "options": [
            "Urea concentration would fall, since more nitrogen is being stored as "
            "protein",
            "Urea concentration would rise, since more ammonia is being converted into "
            "urea",
            "Urea concentration would stay the same regardless of the meal",
            "Urea concentration would fall to zero until the next meal is eaten",
        ],
        "correct_index": 1,
        "why": "More deamination produces more ammonia, and converting that ammonia to urea "
               "raises the blood's urea concentration.",
    },
    {
        "id": "ks4-metabolism-h17",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how much ATP was used on anabolic reactions in a cell that "
               "respired 180 ATP worth of glucose across a day and finished with 65 ATP "
               "still unspent.",
        "options": [
            "180 ATP",
            "65 ATP",
            "115 ATP",
            "245 ATP",
        ],
        "correct_index": 2,
        "why": "180 ATP released minus 65 ATP left unspent means 115 ATP was used on "
               "anabolic reactions.",
    },
    {
        "id": "ks4-metabolism-h18",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what happens to the carbon skeleton of an amino acid with what "
               "happens to its amino group, once the amino acid is deaminated.",
        "options": [
            "Both are excreted together, unchanged, as a single molecule of urea",
            "The carbon skeleton becomes urea; the amino group is respired for energy",
            "Neither the carbon skeleton nor the amino group is used again",
            "The amino group becomes urea; the carbon skeleton can be respired for energy",
        ],
        "correct_index": 3,
        "why": "Deamination removes the amino group, which becomes urea, leaving a carbon "
               "skeleton that can be respired for energy.",
    },
    {
        "id": "ks4-metabolism-h19",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a fever, which raises body temperature, tends to increase the "
               "rate at which a person's metabolic reactions occur.",
        "options": [
            "Warmer conditions speed up the enzyme-controlled reactions that make up "
            "metabolism",
            "A fever slows down every one of the body's many metabolic reactions without "
            "exception",
            "Metabolic reactions have no connection to body temperature",
            "A fever converts catabolic reactions into anabolic ones directly",
        ],
        "correct_index": 0,
        "why": "Metabolic reactions are enzyme-controlled, and warmer conditions speed up "
               "enzyme-controlled reactions, up to a point.",
    },
    {
        "id": "ks4-metabolism-h20",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell's DNA replication and protein synthesis both stop, but its "
               "respiration continues at the same rate. Predict what happens to its ATP "
               "levels, and explain.",
        "options": [
            "ATP levels would fall, since respiration alone cannot supply enough",
            "ATP levels would rise, since less ATP is now being used by anabolic "
            "reactions",
            "ATP levels would stay the same, regardless of what else in the cell changes",
            "ATP could no longer be produced once anabolic reactions stop",
        ],
        "correct_index": 1,
        "why": "With anabolic ATP use removed but respiration unchanged, more ATP builds up "
               "than before, so levels rise.",
    },
    {
        "id": "ks4-metabolism-h21",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a cell could survive indefinitely while carrying out "
               "only catabolic reactions.",
        "options": [
            "It is correct; catabolic reactions alone can maintain a cell forever",
            "It is correct, provided the cell has an unlimited supply of glucose",
            "It is wrong; without anabolic reactions the cell could not repair or replace "
            "its own structures",
            "It is wrong; catabolic reactions cannot take place without the anabolic ones "
            "happening first too",
        ],
        "correct_index": 2,
        "why": "A cell must also build and repair its own structures anabolically; catabolic "
               "reactions alone cannot sustain it indefinitely.",
    },
    {
        "id": "ks4-metabolism-h22",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the net ATP change for a cell that releases 260 ATP through "
               "respiration while spending 140 ATP on protein synthesis, 30 ATP on DNA "
               "replication and 15 ATP on cellulose synthesis.",
        "options": [
            "260 ATP",
            "185 ATP",
            "15 ATP",
            "75 ATP",
        ],
        "correct_index": 3,
        "why": "260 ATP released minus (140 + 30 + 15) = 185 ATP spent leaves a net change "
               "of 75 ATP.",
    },
    {
        "id": "ks4-metabolism-h23",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a growing embryo's cells show an especially high rate of both "
               "anabolic and catabolic reactions at the same time.",
        "options": [
            "Building new structures anabolically needs energy that only faster catabolic "
            "respiration can supply",
            "An embryo's cells carry out anabolic reactions alone, and no catabolic ones",
            "An embryo's cells carry out catabolic reactions alone, and no anabolic ones",
            "An embryo's overall rate of chemical reactions has no connection whatsoever "
            "to how fast it happens to be growing",
        ],
        "correct_index": 0,
        "why": "Rapid growth needs a high rate of anabolic building, which in turn needs a "
               "high rate of catabolic respiration to supply the energy.",
    },
    {
        "id": "ks4-metabolism-h24",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the energy demands of maintaining an adult cell that has stopped "
               "growing with those of a rapidly dividing embryonic cell.",
        "options": [
            "Both cells have identical energy demands, regardless of their rate of growth",
            "The dividing cell has far higher energy demands, to power its anabolic "
            "reactions",
            "The non-growing adult cell has far higher energy demands overall",
            "Neither cell has any real energy demand once it stops actively growing",
        ],
        "correct_index": 1,
        "why": "A dividing cell must build entirely new structures, so it has far higher "
               "anabolic energy demands than a cell simply maintaining itself.",
    },
    {
        "id": "ks4-metabolism-h25",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient eats a meal containing no protein, but plenty of starch and fat. "
               "Evaluate whether this diet alone can meet all of their metabolic needs.",
        "options": [
            "It can; starch and fat alone supply everything a cell's metabolism needs",
            "It can, provided the patient also drinks plenty of water",
            "It cannot; without amino acids, the body cannot carry out enough protein "
            "synthesis for repair and growth",
            "It cannot; starch and fat cannot be respired without protein present",
        ],
        "correct_index": 2,
        "why": "Starch and fat supply energy, but without protein's amino acids the body "
               "lacks what it needs for protein synthesis, repair and growth.",
    },
    {
        "id": "ks4-metabolism-h26",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why comparing two cells' rates of anabolic reactions only makes "
               "sense if you also know their rates of catabolic reactions.",
        "options": [
            "Anabolic and catabolic rates are identical in every healthy cell",
            "Catabolic rate has no bearing on how much anabolic activity is possible",
            "A cell with a high catabolic rate cannot carry out any anabolic reactions of "
            "its own",
            "Anabolic reactions draw on the energy catabolic reactions release, so the "
            "two are linked",
        ],
        "correct_index": 3,
        "why": "Anabolic reactions can only proceed as fast as catabolic reactions supply "
               "the energy for them, so the two rates are linked.",
    },
]
