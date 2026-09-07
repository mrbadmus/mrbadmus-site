"""Biology · Organisation — the eleven BASE subtopics of AQA 4.2.

Covers `principles-of-organisation` through `translocation`: the cell-to-
organism hierarchy, the digestive system and its enzymes, the heart, blood
vessels and blood, coronary heart disease, health and risk factors, cancer,
and the three plant subtopics (tissues, transpiration, translocation).

Every subtopic here is BASE — a Foundation Combined class sits all of it —
so nothing in these stems or options reaches into the Higher extension
(cohesion-tension theory, active-loading pressure gradients, pacemakers and
artificial hearts, evaluating epidemiological evidence) or into Triple-only
material. No question needs a figure: the heart is described in words and
asked about as an order, a function or a consequence, never as a diagram.

The distractors are built from the misconceptions the pages themselves
declare: a tissue confused with an organ, bile called an enzyme, enzymes
"killed" rather than denatured, arteries assumed always to carry oxygenated
blood, the left ventricle said to be thicker because it holds more blood,
white blood cells credited with carrying oxygen, platelets called cells, a
stent confused with a bypass, health read as merely the absence of disease,
a risk factor read as a certainty, a benign tumour read as harmless in every
case, and xylem and phloem — transpiration and translocation — swapped.

Nothing here restates a lesson page's own "Test yourself" question or its
matching block: those are a different pool, printed with their answers on a
page the child can open at will.
"""

TOPIC = "organisation"
SUBJECT = "biology"

QUESTIONS = [
    # ── principles-of-organisation ──────────────────────────────────────
    {
        "id": "ks4-principles-of-organisation-e01",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Glandular tissue in the stomach wall is made of one type of "
                "cell that releases enzymes. State its level of organisation.",
        "options": [
            "An organ, because it releases a substance the body needs",
            "An organ system, because it works with the intestines",
            "A tissue, because it is one cell type with one function",
            "An organism, because it is alive and carries out a process",
        ],
        "correct_index": 2,
        "why": "A tissue is a group of similar cells doing one job; only an "
               "organ contains several different tissue types.",
    },
    {
        "id": "ks4-principles-of-organisation-e02",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is at a HIGHER level of organisation than a "
                "single organ?",
        "options": [
            "The respiratory system — lungs, trachea and diaphragm together",
            "Cardiac muscle — the cells that contract rhythmically in the heart",
            "Epithelial tissue lining the airways of the lungs",
            "A neurone carrying an electrical impulse to a muscle",
        ],
        "correct_index": 0,
        "why": "An organ system is several organs working together, so it "
               "sits one level above an organ in the hierarchy.",
    },
    {
        "id": "ks4-principles-of-organisation-e03",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Xylem is made of one type of cell, all forming hollow tubes "
                "that carry water. State its level of organisation.",
        "options": [
            "An organ of the plant",
            "A tissue of the plant",
            "An organ system of the plant",
            "A whole plant organism",
        ],
        "correct_index": 1,
        "why": "One cell type carrying out one function is a tissue — the "
               "leaf that contains it is the organ.",
    },
    {
        "id": "ks4-principles-of-organisation-e04",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Every cell in one person contains the same DNA. State what "
                "makes a muscle cell different from a red blood cell.",
        "options": [
            "The muscle cell holds extra DNA that the red blood cell lacks",
            "The red blood cell lost some of its genes as it developed",
            "The two cells came from two different organisms originally",
            "Different genes are switched on in the two cell types",
        ],
        "correct_index": 3,
        "why": "Specialisation comes from which genes are switched on, not "
               "from cells carrying different DNA.",
    },
    {
        "id": "ks4-principles-of-organisation-s01",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says 'the heart is a tissue because it is made of "
                "cardiac muscle'. Explain the error in this statement.",
        "options": [
            "The heart is a tissue, but it is built from epithelial cells not muscle",
            "The heart is an organ system, as it works with blood vessels",
            "Cardiac muscle is an organ, so the heart is an organ system",
            "The heart also contains valves and blood vessels, so it is an organ",
        ],
        "correct_index": 3,
        "why": "The heart combines cardiac muscle with valve and vessel "
               "tissue — several tissues in one structure makes it an organ.",
    },
    {
        "id": "ks4-principles-of-organisation-s02",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A leaf contains palisade mesophyll, xylem, phloem and "
                "epidermis. Explain what this tells you about the leaf.",
        "options": [
            "It is a tissue, because all of these are found in one leaf",
            "It is an organ, built from several different tissue types",
            "It is an organ system, because each tissue is itself an organ",
            "It is a single cell, because each part is one specialised cell",
        ],
        "correct_index": 1,
        "why": "Several different tissues working together for one function "
               "is the definition of an organ — in plants as in animals.",
    },
    {
        "id": "ks4-principles-of-organisation-s03",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to the level of organisation as you "
                "move from the stomach to the digestive system.",
        "options": [
            "It rises by one level — from an organ to an organ system",
            "It falls by one level — from an organ system to an organ",
            "It stays the same — both of them are organs of the body",
            "It rises by two levels — from a tissue to an organ system",
        ],
        "correct_index": 0,
        "why": "The stomach is one organ; the digestive system is the group "
               "of organs it belongs to, one level higher.",
    },
    {
        "id": "ks4-principles-of-organisation-s04",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The lungs contain epithelial tissue lining the airways, "
                "muscle tissue and blood vessels. Determine the level of "
                "organisation of the lungs, and give the reason.",
        "options": [
            "A tissue, because every cell in the lungs carries out the same job",
            "An organism, because the lungs carry out gas exchange by themselves",
            "An organ, because several different tissues work together in one structure",
            "An organ system, because the lungs and the windpipe work together",
        ],
        "correct_index": 2,
        "why": "An organ is one structure built from several different "
               "tissues; a group of organs working together would be an organ "
               "system.",
    },
    {
        "id": "ks4-principles-of-organisation-h01",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A faulty gene in liver cells can affect a whole person. "
                "Explain how, using the levels of organisation.",
        "options": [
            "A single faulty cell rewrites the DNA of every other cell that it touches",
            "Faulty cells build a faulty tissue and organ, so the whole body suffers",
            "Cells are the highest level, so the organism must copy their fault",
            "The organism level controls the cell level, passing the fault down",
        ],
        "correct_index": 1,
        "why": "Each level is built from the one below, so a fault in cells "
               "is carried upwards into the tissue, organ and organism.",
    },
    {
        "id": "ks4-principles-of-organisation-h02",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare muscle and the stomach as levels of organisation in "
                "the human body.",
        "options": [
            "Both are organs, but the stomach also contains glandular tissue",
            "Muscle is an organ system and the stomach is one organ inside it",
            "Muscle is one cell type; the stomach combines several tissues",
            "Both are tissues, but the stomach is made of much larger cells",
        ],
        "correct_index": 2,
        "why": "Muscle is a tissue — one cell type, one function; the stomach "
               "is an organ because it holds muscle, glandular and epithelial "
               "tissue together.",
    },
    {
        "id": "ks4-principles-of-organisation-h03",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A biologist studies cells that all look alike, all contract, "
                "and lie side by side in a heart wall. Determine the level.",
        "options": [
            "An organ, because these cells are found inside the heart itself",
            "An organ system, because contraction moves blood round the body",
            "An organism, because the cells work together to keep a person alive",
            "A tissue, because they are similar cells with one shared function",
        ],
        "correct_index": 3,
        "why": "Similar cells with one shared function form a tissue, whatever "
               "organ that tissue happens to sit inside.",
    },
    {
        "id": "ks4-principles-of-organisation-h04",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Every structure made of more than "
                "one cell must be an organ.'",
        "options": [
            "Wrong — a tissue has many cells too, but all of one single type",
            "Correct — any multicellular structure in the body is an organ",
            "Wrong — an organ must be made of exactly one type of cell only",
            "Correct — only a single cell sits below the level of an organ",
        ],
        "correct_index": 0,
        "why": "Cell number is not the test: an organ is defined by containing "
               "several different tissues, not by being multicellular.",
    },

    # ── digestive-system ────────────────────────────────────────────────
    {
        "id": "ks4-digestive-system-e01",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two products formed when lipase digests a lipid.",
        "options": [
            "Amino acids and maltose",
            "Fatty acids and glycerol",
            "Glucose and glycerol",
            "Fatty acids and amino acids",
        ],
        "correct_index": 1,
        "why": "Lipase breaks a lipid into fatty acids and glycerol, both "
               "small enough to be absorbed through the intestine wall.",
    },
    {
        "id": "ks4-digestive-system-e02",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the reagent used to test a food sample for protein, "
                "and the colour change of a positive result.",
        "options": [
            "Iodine solution — it turns blue-black",
            "Benedict's solution — it turns brick red",
            "Ethanol — it forms a cloudy white emulsion",
            "Biuret reagent — it turns purple",
        ],
        "correct_index": 3,
        "why": "Biuret reagent turns from blue to purple when protein is "
               "present; the other three tests detect starch, sugar and fat.",
    },
    {
        "id": "ks4-digestive-system-e03",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the muscular tube that carries a bolus of food from the "
                "mouth down to the stomach.",
        "options": [
            "The oesophagus",
            "The trachea",
            "The pancreatic duct",
            "The small intestine",
        ],
        "correct_index": 0,
        "why": "The oesophagus moves food to the stomach by peristalsis — "
               "waves of muscle contraction along its wall.",
    },
    {
        "id": "ks4-digestive-system-e04",
        "subtopic_slug": "digestive-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where bile is stored after the liver has produced it.",
        "options": [
            "In the pancreas",
            "In the lining of the stomach",
            "In the gall bladder",
            "In the large intestine",
        ],
        "correct_index": 2,
        "why": "The liver makes bile, the gall bladder stores it, and it is "
               "released into the small intestine when fatty food arrives.",
    },
    {
        "id": "ks4-digestive-system-s01",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hydrochloric acid is released into the stomach.",
        "options": [
            "It kills most bacteria in food and gives pepsin its optimum pH",
            "It digests protein into amino acids without any enzyme being needed",
            "It neutralises the alkaline bile arriving from the gall bladder",
            "It emulsifies fat droplets so that lipase can act on them faster",
        ],
        "correct_index": 0,
        "why": "The acid has two jobs: it destroys most bacteria in food and "
               "it holds the stomach near pH 2, where pepsin works best.",
    },
    {
        "id": "ks4-digestive-system-s02",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the difference between mechanical and chemical "
                "digestion, using chewing and amylase as your examples.",
        "options": [
            "Chewing breaks chemical bonds; amylase only changes the piece size",
            "Both break chemical bonds, but chewing does it far more quickly",
            "Chewing breaks food into pieces; amylase breaks bonds in starch",
            "Chewing digests starch; amylase increases the food's surface area",
        ],
        "correct_index": 2,
        "why": "Mechanical digestion only makes the pieces smaller; chemical "
               "digestion, done by enzymes, breaks the molecules apart.",
    },
    {
        "id": "ks4-digestive-system-s03",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why starch cannot be absorbed into the blood but "
                "glucose can.",
        "options": [
            "Starch is already soluble, so the body has no reason to absorb it",
            "Starch is stored in the liver rather than being absorbed at all",
            "Glucose is broken down by bile before it ever reaches the blood",
            "Starch molecules are too large to cross the intestine wall",
        ],
        "correct_index": 3,
        "why": "Only small, soluble molecules can pass through the small "
               "intestine wall, which is why starch must be digested first.",
    },
    {
        "id": "ks4-digestive-system-s04",
        "subtopic_slug": "digestive-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person has had their gall bladder removed. Suggest the "
                "effect this has on the digestion of a fatty meal.",
        "options": [
            "Protein digestion slows, as pepsin has no acid left to work in",
            "Fat digestion is slower, as bile is not stored and released in bulk",
            "Fat digestion stops completely, as no bile can now be made at all",
            "Starch digestion slows, as amylase is no longer being released",
        ],
        "correct_index": 1,
        "why": "The liver still makes bile, but without a store it cannot be "
               "released in a large amount, so fat is emulsified more slowly.",
    },
    {
        "id": "ks4-digestive-system-h01",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's pancreas produces very little lipase. Predict "
                "what will be found in their faeces.",
        "options": [
            "Undigested starch, because amylase cannot work without lipase",
            "Large amounts of protein, because protease needs lipase to start",
            "Undigested fat, because it is not broken into fatty acids and glycerol",
            "Almost no water at all, because water absorption in the large intestine stops",
        ],
        "correct_index": 2,
        "why": "Lipase is the only enzyme that chemically digests fat, so "
               "without it fat passes through the gut unabsorbed.",
    },
    {
        "id": "ks4-digestive-system-h02",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a villus needs a rich blood supply as well as a "
                "wall that is only one cell thick.",
        "options": [
            "The blood supply produces the enzymes that finish digestion inside it",
            "Blood carries absorbed molecules away, keeping the gradient steep",
            "The blood supply warms the villus so that diffusion can happen at all",
            "Blood pressure pushes digested food through the wall of the villus",
        ],
        "correct_index": 1,
        "why": "Removing absorbed glucose and amino acids keeps their "
               "concentration low in the blood, so diffusion continues.",
    },
    {
        "id": "ks4-digestive-system-h03",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bile is alkaline. Explain why this matters for the enzymes "
                "released into the small intestine by the pancreas.",
        "options": [
            "It makes the intestine acidic, the optimum pH for those enzymes",
            "It supplies the alkali that pancreatic enzymes use as a substrate",
            "It denatures pancreatic enzymes so digestion can be slowed down",
            "It neutralises stomach acid, giving them the neutral pH they need",
        ],
        "correct_index": 3,
        "why": "Chyme leaving the stomach is acidic; bile neutralises it so "
               "that pancreatic enzymes meet their optimum pH of about 7-8.",
    },
    {
        "id": "ks4-digestive-system-h04",
        "subtopic_slug": "digestive-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Food passes through a patient's large intestine unusually "
                "quickly. Predict the effect on their faeces and explain why.",
        "options": [
            "Watery faeces, because less time is available to absorb water",
            "Hard, dry faeces, because water is absorbed faster at higher speed",
            "No change, because water is absorbed in the small intestine instead",
            "Fatty faeces, because bile cannot reach the large intestine in time",
        ],
        "correct_index": 0,
        "why": "The large intestine absorbs water from the material passing "
               "through it, so less contact time leaves the faeces watery.",
    },

    # ── enzymes ─────────────────────────────────────────────────────────
    {
        "id": "ks4-enzymes-e01",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Enzymes are biological catalysts. State the type of molecule "
                "that every enzyme is made from.",
        "options": [
            "A carbohydrate",
            "A lipid",
            "A mineral ion",
            "A protein",
        ],
        "correct_index": 3,
        "why": "Every enzyme is a protein, folded into a shape that creates "
               "its active site — which is why heat can change that shape.",
    },
    {
        "id": "ks4-enzymes-e02",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate optimum temperature of most human "
                "enzymes.",
        "options": [
            "37 °C",
            "20 °C",
            "60 °C",
            "100 °C",
        ],
        "correct_index": 0,
        "why": "Human enzymes work fastest at about body temperature, 37 °C, "
               "and denature above it.",
    },
    {
        "id": "ks4-enzymes-e03",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the word catalyst.",
        "options": [
            "A substance that is used up as it speeds a reaction up",
            "A substance that slows a reaction so it can be measured",
            "A substance that speeds a reaction up without being used up",
            "A substance that supplies the energy that a reaction needs to start",
        ],
        "correct_index": 2,
        "why": "A catalyst increases the rate of a reaction and is released "
               "unchanged, so one enzyme molecule works many times over.",
    },
    {
        "id": "ks4-enzymes-e04",
        "subtopic_slug": "enzymes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In Required Practical 3, state which solution is used to "
                "show that starch is still present in the mixture.",
        "options": [
            "Benedict's solution",
            "Iodine solution",
            "Biuret reagent",
            "Limewater",
        ],
        "correct_index": 1,
        "why": "Iodine solution turns blue-black while starch remains, and "
               "stays orange-brown once amylase has digested it all.",
    },
    {
        "id": "ks4-enzymes-s01",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an enzyme-catalysed reaction speeds up as the "
                "temperature is raised from 10 °C to 30 °C.",
        "options": [
            "The active sites slowly change shape to fit more substrates in",
            "Molecules gain kinetic energy, so more collisions happen each second",
            "The cell simply makes far more enzyme molecules at higher temperatures",
            "The substrate molecules break apart before reaching the enzyme",
        ],
        "correct_index": 1,
        "why": "More kinetic energy means more collisions between substrate "
               "and active site each second, so more product is made.",
    },
    {
        "id": "ks4-enzymes-s02",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pancreatic enzymes have an optimum pH of about 8. Explain "
                "what happens if they are placed in stomach acid at pH 2.",
        "options": [
            "They work faster, because the acid supplies extra energy to them",
            "They are unaffected, because pH only alters protein digestion rate",
            "Their active sites change shape, so substrate no longer fits them",
            "They turn into pepsin, the enzyme that works best at pH 2",
        ],
        "correct_index": 2,
        "why": "A pH far from the optimum alters the bonds holding the enzyme "
               "in shape, so the active site no longer matches the substrate.",
    },
    {
        "id": "ks4-enzymes-s03",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In Required Practical 3, a student records the time taken "
                "for iodine to stop turning blue-black. Explain what this "
                "time measures.",
        "options": [
            "How long amylase takes to break down all the starch at that pH",
            "How long the iodine takes to react completely with the amylase",
            "How long the starch takes to dissolve fully in the warm water",
            "How long the sugars take to be built back up into starch again",
        ],
        "correct_index": 0,
        "why": "Iodine only goes blue-black with starch, so the moment it "
               "stops doing so is the moment the amylase has digested it all.",
    },
    {
        "id": "ks4-enzymes-s04",
        "subtopic_slug": "enzymes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the body does not simply raise its temperature "
                "to 50 °C in order to make digestion faster.",
        "options": [
            "At 50 °C enzymes work slowly because collisions become less frequent",
            "At 50 °C the food molecules would be destroyed before being digested",
            "At 50 °C the body would stop making enzymes, so digestion would pause",
            "Above the optimum, human enzymes denature and activity falls to zero",
        ],
        "correct_index": 3,
        "why": "Past the optimum the enzyme's active site is permanently "
               "changed, so raising the temperature further destroys the rate.",
    },
    {
        "id": "ks4-enzymes-h01",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect on an enzyme of cooling it to 5 °C and of "
                "heating it to 70 °C.",
        "options": [
            "At 5 °C it is slow but undamaged; at 70 °C it is permanently denatured",
            "At both temperatures the active site of the enzyme is destroyed for good",
            "At 5 °C it is denatured; at 70 °C it simply works more slowly",
            "At both temperatures the enzyme works at the same reduced rate",
        ],
        "correct_index": 0,
        "why": "Cold only slows collisions down, and warming restores the "
               "rate; heat past the optimum changes the active site for good.",
    },
    {
        "id": "ks4-enzymes-h02",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Boiling the amylase killed it, so no "
                "starch was digested.' Evaluate the wording of this "
                "conclusion.",
        "options": [
            "Fully correct — boiling kills the enzyme so no starch is digested",
            "Wrong — boiling makes enzymes work faster, so the starch was digested",
            "Wrong — the amylase survived, and the starch was digested slowly",
            "The science is right, but an enzyme is a protein — it is denatured",
        ],
        "correct_index": 3,
        "why": "An enzyme is a protein, not a living thing: heat denatures it "
               "by changing the shape of its active site.",
    },
    {
        "id": "ks4-enzymes-h03",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Salivary amylase has an optimum pH of about 7. Predict what "
                "happens to it when the food it is mixed with reaches the "
                "stomach.",
        "options": [
            "It speeds up, because the stomach is warmer than the mouth is",
            "It stops working, because pH 2 changes the shape of its active site",
            "It carries on unchanged, protected inside the bolus of food",
            "It becomes a protease instead, which is the enzyme that the stomach needs",
        ],
        "correct_index": 1,
        "why": "Stomach acid is far from amylase's optimum pH, so its active "
               "site changes shape and starch digestion in the stomach stops.",
    },
    {
        "id": "ks4-enzymes-h04",
        "subtopic_slug": "enzymes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two beakers of identical starch solution each receive the "
                "same mass of amylase. Beaker A is at pH 7 and beaker B at "
                "pH 3. Explain the difference in digestion time.",
        "options": [
            "Beaker B is faster, because acid helps to break the starch apart",
            "Both take the same time, because the same mass of amylase was used",
            "Beaker A is faster, because pH 7 is amylase's optimum pH",
            "Beaker B is faster, because acid stops the enzyme being used up",
        ],
        "correct_index": 2,
        "why": "At its optimum pH the active site keeps its shape, so more "
               "enzyme-substrate complexes form and the starch goes faster.",
    },

    # ── heart-blood-vessels ─────────────────────────────────────────────
    {
        "id": "ks4-heart-blood-vessels-e01",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the blood vessel that carries oxygenated blood away "
                "from the left ventricle to the rest of the body.",
        "options": [
            "The aorta",
            "The vena cava",
            "The pulmonary artery",
            "The pulmonary vein",
        ],
        "correct_index": 0,
        "why": "The aorta is the artery leaving the left ventricle, carrying "
               "oxygenated blood at high pressure to every body organ.",
    },
    {
        "id": "ks4-heart-blood-vessels-e02",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the rule that decides whether a blood vessel is called "
                "an artery or a vein.",
        "options": [
            "Arteries carry oxygenated blood; veins carry deoxygenated blood",
            "Arteries lie deep in the body; veins lie close to the skin",
            "Arteries carry blood away from the heart; veins carry it towards",
            "Arteries contain valves along their length; veins do not",
        ],
        "correct_index": 2,
        "why": "The name depends on direction, not on oxygen — which is why "
               "the pulmonary artery can carry deoxygenated blood.",
    },
    {
        "id": "ks4-heart-blood-vessels-e03",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many times blood passes through the heart during "
                "one complete circuit of the body.",
        "options": [
            "Once",
            "Three times",
            "Four times",
            "Twice",
        ],
        "correct_index": 3,
        "why": "Humans have a double circulatory system: once through the "
               "right side to the lungs, once through the left to the body.",
    },
    {
        "id": "ks4-heart-blood-vessels-e04",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of muscle that the walls of the heart are "
                "made from.",
        "options": [
            "Skeletal muscle",
            "Cardiac muscle",
            "Smooth muscle",
            "Voluntary muscle",
        ],
        "correct_index": 1,
        "why": "Cardiac muscle contracts and relaxes rhythmically without "
               "tiring, which is why the heart can beat for a lifetime.",
    },
    {
        "id": "ks4-heart-blood-vessels-s01",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Blood has just been pumped out of the right ventricle. "
                "Describe where it travels to next.",
        "options": [
            "Along the aorta to the organs and tissues of the body",
            "Back into the right atrium through the atrioventricular valve",
            "Along the pulmonary artery to the lungs",
            "Along the pulmonary vein to the left atrium",
        ],
        "correct_index": 2,
        "why": "The right ventricle pumps deoxygenated blood into the "
               "pulmonary artery, which carries it to the lungs.",
    },
    {
        "id": "ks4-heart-blood-vessels-s02",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the route a red blood cell takes from the vena cava "
                "to the lungs.",
        "options": [
            "Vena cava, left atrium, left ventricle, pulmonary artery, lungs",
            "Vena cava, right atrium, right ventricle, pulmonary artery, lungs",
            "Vena cava, right atrium, right ventricle, pulmonary vein, lungs",
            "Vena cava, right ventricle, right atrium, aorta, lungs",
        ],
        "correct_index": 1,
        "why": "Blood returning from the body enters the right atrium, drops "
               "into the right ventricle and leaves by the pulmonary artery.",
    },
    {
        "id": "ks4-heart-blood-vessels-s03",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the walls of arteries contain elastic fibres.",
        "options": [
            "They let the artery squeeze blood along without help from the heart",
            "They let the artery narrow enough to keep the blood pressure low",
            "They act as valves, closing the artery each time the heart relaxes",
            "They stretch as blood surges through, then recoil to smooth the flow",
        ],
        "correct_index": 3,
        "why": "Blood leaves the heart in surges; the elastic fibres stretch "
               "and recoil so that flow further along stays steady.",
    },
    {
        "id": "ks4-heart-blood-vessels-s04",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why substances move between a capillary and the "
                "cells around it without the body using any energy.",
        "options": [
            "They move by diffusion, down a concentration gradient",
            "They are pushed across by the force of the heart's contraction",
            "They are carried across by valves inside the capillary wall",
            "They are moved across the wall by active transport proteins",
        ],
        "correct_index": 0,
        "why": "Oxygen and glucose are more concentrated in the blood, carbon "
               "dioxide in the cells, so both simply diffuse down a gradient.",
    },
    {
        "id": "ks4-heart-blood-vessels-h01",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the wall of the aorta with the wall of the vena "
                "cava, and explain the difference between them.",
        "options": [
            "They are equally thick, because both of them carry the same volume of blood",
            "The vena cava is thicker, as it holds blood from the whole body",
            "The vena cava is thicker, because it must contain valves inside it",
            "The aorta is thicker and more muscular, as its blood is at high pressure",
        ],
        "correct_index": 3,
        "why": "The aorta receives blood straight from the left ventricle at "
               "high pressure, so its wall must be thick enough to withstand it.",
    },
    {
        "id": "ks4-heart-blood-vessels-h02",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's coronary artery is almost completely blocked. "
                "Explain the effect this has on the heart.",
        "options": [
            "Heart muscle gets too little oxygen to respire and contract properly",
            "Blood cannot reach the lungs at all, so no oxygen enters the blood",
            "Blood leaks backwards from the ventricle into the atrium each beat",
            "The left ventricle is starved of blood and stops filling completely",
        ],
        "correct_index": 0,
        "why": "The coronary arteries supply the heart muscle itself, so a "
               "blockage starves that muscle of the oxygen it needs to respire.",
    },
    {
        "id": "ks4-heart-blood-vessels-h03",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why humans need a double circulatory system rather "
                "than a single one.",
        "options": [
            "It lets blood reach the lungs without passing through any organ",
            "Pressure falls in the lungs, so it is raised again before the body",
            "It keeps the number of heartbeats needed per minute as low as it can",
            "It lets red blood cells be replaced each time they pass the heart",
        ],
        "correct_index": 1,
        "why": "Blood loses pressure crossing the lungs, so returning it to "
               "the heart lets the left ventricle send it to the body strongly.",
    },
    {
        "id": "ks4-heart-blood-vessels-h04",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The valve between the left atrium and the left ventricle "
                "does not close fully. Predict the consequence of this.",
        "options": [
            "Blood flows straight back from the aorta into the left ventricle",
            "Blood cannot enter the left atrium from the pulmonary vein at all",
            "Blood leaks back into the atrium, so less is pumped to the body",
            "Blood is pumped into the pulmonary artery instead of the aorta",
        ],
        "correct_index": 2,
        "why": "Valves exist to stop backflow, so a leaking one lets blood "
               "return to the atrium and reduces the volume pumped out.",
    },

    # ── blood ───────────────────────────────────────────────────────────
    {
        "id": "ks4-blood-e01",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the protein inside a red blood cell that binds to "
                "oxygen.",
        "options": [
            "Fibrin",
            "Haemoglobin",
            "Carbohydrase",
            "Amylase",
        ],
        "correct_index": 1,
        "why": "Haemoglobin fills a red blood cell and is the molecule that "
               "picks up oxygen in the lungs and releases it in the tissues.",
    },
    {
        "id": "ks4-blood-e02",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the compound formed when haemoglobin binds to oxygen "
                "in the lungs.",
        "options": [
            "Oxyhaemoglobin",
            "Carboxyhaemoglobin",
            "Deoxyhaemoglobin",
            "Haemoglobin oxide",
        ],
        "correct_index": 0,
        "why": "In the lungs, where oxygen is plentiful, haemoglobin binds it "
               "to form oxyhaemoglobin, which releases it again in the tissues.",
    },
    {
        "id": "ks4-blood-e03",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which component of blood is a fragment of a cell "
                "rather than a whole cell.",
        "options": [
            "A red blood cell",
            "A phagocyte",
            "A lymphocyte",
            "A platelet",
        ],
        "correct_index": 3,
        "why": "Platelets are cell fragments with no nucleus, which is why "
               "they are never described as a type of blood cell.",
    },
    {
        "id": "ks4-blood-e04",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the protein that forms a mesh of fibres to trap red "
                "blood cells when a wound clots.",
        "options": [
            "Haemoglobin",
            "An antibody",
            "Fibrin",
            "Pepsin",
        ],
        "correct_index": 2,
        "why": "Fibrin fibres form a mesh across the wound, trapping red "
               "blood cells to make the clot that later dries into a scab.",
    },
    {
        "id": "ks4-blood-s01",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the biconcave disc shape of a red blood cell "
                "helps it to do its job.",
        "options": [
            "It makes the cell rigid so it is not damaged inside a capillary",
            "It creates a space in the middle where oxygen is stored as a gas",
            "It allows the cell to divide quickly and replace worn-out cells",
            "It increases surface area and shortens the diffusion distance",
        ],
        "correct_index": 3,
        "why": "A dimpled disc has more surface area and a thin centre, so "
               "oxygen diffuses in and out of it quickly.",
    },
    {
        "id": "ks4-blood-s02",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a phagocyte destroys a bacterium.",
        "options": [
            "It produces an antibody that sticks to the bacterium's antigen",
            "It releases a chemical that dissolves the bacterium from a distance",
            "Its membrane surrounds the bacterium and enzymes digest it inside",
            "It clumps with platelets to trap the bacterium inside a fibrin mesh",
        ],
        "correct_index": 2,
        "why": "Phagocytosis: the phagocyte's membrane engulfs the pathogen "
               "and enzymes inside the cell break it down.",
    },
    {
        "id": "ks4-blood-s03",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person who has had measles once rarely catches "
                "it a second time.",
        "options": [
            "Memory lymphocytes remain, so antibodies are made quickly again",
            "The measles virus is destroyed everywhere after a single outbreak",
            "Red blood cells learn the shape of the virus and carry it away",
            "Platelets seal the airways so that the virus can no longer enter",
        ],
        "correct_index": 0,
        "why": "Memory lymphocytes survive after the infection, so the second "
               "antibody response is fast enough to stop illness developing.",
    },
    {
        "id": "ks4-blood-s04",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why one single lymphocyte cannot fight every type of "
                "pathogen.",
        "options": [
            "Lymphocytes are used up by the first pathogen that they meet",
            "Each antibody has a shape that fits only one type of antigen",
            "Lymphocytes only reach pathogens that are inside the bloodstream",
            "Each lymphocyte survives for only a few hours after it is made",
        ],
        "correct_index": 1,
        "why": "An antibody binds to a specific antigen shape, so a different "
               "pathogen needs a different lymphocyte and a different antibody.",
    },
    {
        "id": "ks4-blood-h01",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's bone marrow is damaged and makes very few red "
                "blood cells. Predict a symptom and explain it.",
        "options": [
            "Wounds bleed for far longer, because clots can no longer form",
            "Repeated bacterial infections, because pathogens are not engulfed",
            "Tiredness and breathlessness, as less oxygen reaches the cells",
            "Swelling of the legs, because plasma leaks out of the capillaries",
        ],
        "correct_index": 2,
        "why": "Fewer red blood cells means less haemoglobin, so less oxygen "
               "reaches respiring cells and less energy is released.",
    },
    {
        "id": "ks4-blood-h02",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the role of a phagocyte with the role of a "
                "lymphocyte in defending the body.",
        "options": [
            "Phagocytes make antibodies while lymphocytes engulf the pathogens",
            "Both make antibodies, but only lymphocytes engulf pathogens too",
            "Phagocytes carry the oxygen and lymphocytes the carbon dioxide",
            "Phagocytes engulf any pathogen; lymphocytes make one antibody",
        ],
        "correct_index": 3,
        "why": "Phagocytes act non-specifically against any pathogen, while a "
               "lymphocyte makes one antibody matching one antigen.",
    },
    {
        "id": "ks4-blood-h03",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon monoxide in cigarette smoke binds permanently to "
                "haemoglobin. Explain the effect this has on a smoker.",
        "options": [
            "Blood clots more slowly, as platelets cannot reach the wound",
            "Less oxygen is carried, so tissues receive less for respiration",
            "More oxygen is carried, as carbon monoxide is a smaller molecule",
            "Antibodies cannot be made, so every infection lasts much longer",
        ],
        "correct_index": 1,
        "why": "Every haemoglobin molecule holding carbon monoxide is one that "
               "can no longer carry oxygen to respiring tissues.",
    },
    {
        "id": "ks4-blood-h04",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe, in order, what happens at a cut from the moment "
                "the blood vessel is damaged.",
        "options": [
            "Platelets clump, a fibrin mesh forms, cells are trapped, a scab dries",
            "A fibrin mesh forms, platelets dissolve it, red cells seal the gap",
            "Lymphocytes clump at the wound and antibodies form a sealing mesh",
            "Plasma thickens into a solid and platelets then harden on top of it",
        ],
        "correct_index": 0,
        "why": "Platelets clump first and trigger the reactions that make "
               "fibrin; the trapped cells and fibrin dry to form the scab.",
    },

    # ── coronary-heart-disease ──────────────────────────────────────────
    {
        "id": "ks4-coronary-heart-disease-e01",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the arteries that supply the heart muscle itself with "
                "oxygenated blood.",
        "options": [
            "The pulmonary arteries",
            "The renal arteries",
            "The coronary arteries",
            "The carotid arteries",
        ],
        "correct_index": 2,
        "why": "The coronary arteries branch off the aorta to feed the "
               "cardiac muscle, so a blockage in them starves the heart.",
    },
    {
        "id": "ks4-coronary-heart-disease-e02",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what statins do in the body.",
        "options": [
            "They widen the coronary arteries by relaxing muscle in their walls",
            "They dissolve blood clots that have already formed in an artery",
            "They replace a diseased heart valve with a mechanical valve",
            "They lower the level of cholesterol in the blood",
        ],
        "correct_index": 3,
        "why": "Statins reduce blood cholesterol, which slows the build-up of "
               "fatty plaques in the artery walls.",
    },
    {
        "id": "ks4-coronary-heart-disease-e03",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the fatty deposits that build up inside the walls of "
                "the coronary arteries.",
        "options": [
            "Fibrin clots",
            "Plaques",
            "Villi",
            "Platelets",
        ],
        "correct_index": 1,
        "why": "Plaques are the fatty deposits of atherosclerosis; they "
               "narrow the lumen and reduce blood flow to the heart muscle.",
    },
    {
        "id": "ks4-coronary-heart-disease-e04",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to heart muscle when a coronary artery "
                "becomes completely blocked.",
        "options": [
            "It is starved of oxygen and its cells begin to die",
            "It contracts much harder to force blood past the blockage",
            "It is supplied instead by blood from the pulmonary artery",
            "It fills with fatty deposits and its wall becomes thicker",
        ],
        "correct_index": 0,
        "why": "With no blood supply the muscle cannot respire, so those "
               "cells die — this is a heart attack.",
    },
    {
        "id": "ks4-coronary-heart-disease-s01",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a plaque in a coronary artery can lead to a "
                "heart attack.",
        "options": [
            "It narrows the artery, and if it ruptures a clot can block it",
            "It dissolves into the blood and blocks a capillary in the lungs",
            "It stretches the artery wall so far that the artery bursts open",
            "It stops the heart valves closing, so blood leaks back each beat",
        ],
        "correct_index": 0,
        "why": "A narrowed artery already reduces flow, and a clot forming on "
               "a ruptured plaque can cut the supply off completely.",
    },
    {
        "id": "ks4-coronary-heart-disease-s02",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how smoking increases a person's risk of developing "
                "coronary heart disease.",
        "options": [
            "Tar coats the coronary arteries and physically blocks them up",
            "Carbon monoxide damages artery walls and nicotine raises blood pressure",
            "Smoke lowers body temperature, so the heart has to work harder",
            "Nicotine thickens the blood so that it cannot pass through the capillaries",
        ],
        "correct_index": 1,
        "why": "Damaged artery walls collect plaques more easily, and raised "
               "heart rate and blood pressure add further strain.",
    },
    {
        "id": "ks4-coronary-heart-disease-s03",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient is told their stent 'does not treat the underlying "
                "cause'. Explain why this is said of a stent.",
        "options": [
            "A stent lowers blood cholesterol but does not open the artery",
            "A stent is removed after a few weeks, so its effect is temporary",
            "A stent widens one artery but fatty build-up continues elsewhere",
            "A stent only works while the patient also takes daily statins",
        ],
        "correct_index": 2,
        "why": "The stent fixes one narrowed section mechanically; the "
               "atherosclerosis that caused it carries on in other arteries.",
    },
    {
        "id": "ks4-coronary-heart-disease-s04",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a patient who has had a heart transplant must "
                "take immunosuppressant drugs for the rest of their life.",
        "options": [
            "The drugs stop the donor heart from beating too fast for the body",
            "The drugs prevent fatty plaques forming in the donor heart's arteries",
            "The drugs replace the hormones the removed heart used to produce",
            "The drugs stop the immune system attacking the donor heart",
        ],
        "correct_index": 3,
        "why": "The donor heart carries antigens the patient's immune system "
               "reads as foreign, so rejection must be suppressed permanently.",
    },
    {
        "id": "ks4-coronary-heart-disease-h01",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a stent with bypass surgery as treatments for a "
                "narrowed coronary artery.",
        "options": [
            "Both remove the plaque: the stent with a drug, the bypass by surgery",
            "A stent props the narrowed artery open; a bypass routes blood around it",
            "A stent creates a new route for blood; a bypass holds the artery open",
            "Both create a new route, but a bypass uses metal and a stent a vein",
        ],
        "correct_index": 1,
        "why": "A stent works inside the original artery; a bypass graft "
               "carries blood along an entirely new path around the blockage.",
    },
    {
        "id": "ks4-coronary-heart-disease-h02",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that statins are a better treatment than "
                "a stent for every patient with coronary heart disease.",
        "options": [
            "Not for everyone — statins cannot open an already narrowed artery",
            "Yes — statins remove existing plaques, so surgery is never needed",
            "Yes — statins have no side effects, unlike any surgical treatment",
            "No — statins are only ever given after a stent has been fitted",
        ],
        "correct_index": 0,
        "why": "Statins slow future plaque build-up but cannot restore flow "
               "through an artery that is already badly narrowed.",
    },
    {
        "id": "ks4-coronary-heart-disease-h03",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two patients have the same diet and exercise. One had a "
                "parent who had a heart attack at 45. Explain why that "
                "patient may still be at higher risk.",
        "options": [
            "Family history is not a risk factor at all, so the two are at equal risk",
            "Their diet must be worse in reality, as risk is only lifestyle",
            "They will certainly have a heart attack at 45 years old as well",
            "Genetics is a risk factor that cannot be changed, and it adds to lifestyle",
        ],
        "correct_index": 3,
        "why": "Risk factors add together, and family history is one that a "
               "patient cannot alter however good their lifestyle is.",
    },
    {
        "id": "ks4-coronary-heart-disease-h04",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a doctor may prescribe statins to a patient who "
                "has already had a stent fitted.",
        "options": [
            "Statins stop the metal of the stent from rusting inside the artery",
            "Statins widen the stent gradually as the patient's artery grows",
            "Statins slow further plaque build-up, in that artery and in others",
            "Statins dissolve the plaque that the stent was pushed through",
        ],
        "correct_index": 2,
        "why": "The stent treats one narrowing; statins act on the cholesterol "
               "that would otherwise keep narrowing the rest.",
    },

    # ── health-disease ──────────────────────────────────────────────────
    {
        "id": "ks4-health-disease-e01",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the World Health Organisation defines health.",
        "options": [
            "Being free of every infectious disease",
            "Being physically fit enough to exercise daily",
            "Having no inherited conditions in the family",
            "Complete physical, mental and social wellbeing",
        ],
        "correct_index": 3,
        "why": "The WHO definition is deliberately wider than illness: health "
               "includes mental and social wellbeing, not just a working body.",
    },
    {
        "id": "ks4-health-disease-e02",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what causes a communicable disease.",
        "options": [
            "A person's diet and their level of exercise",
            "A pathogen, such as a bacterium or a virus",
            "A mutation inherited from one of their parents",
            "Long-term exposure to UV radiation from the sun",
        ],
        "correct_index": 1,
        "why": "Communicable diseases are caused by pathogens, which is what "
               "allows them to be passed from one organism to another.",
    },
    {
        "id": "ks4-health-disease-e03",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of disease that asthma is.",
        "options": [
            "Non-communicable",
            "Communicable, spread by droplets",
            "Communicable, spread by an insect",
            "Communicable, caused by a fungus",
        ],
        "correct_index": 0,
        "why": "Asthma is not caused by a pathogen and cannot be passed on, "
               "so it is a non-communicable disease.",
    },
    {
        "id": "ks4-health-disease-e04",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a risk factor.",
        "options": [
            "Something that always causes the disease in anyone who is exposed to it",
            "Something that protects a person from developing a disease",
            "Something that increases the probability of developing a disease",
            "Something that proves one thing has caused another thing",
        ],
        "correct_index": 2,
        "why": "A risk factor changes the probability of disease; it never "
               "makes that disease certain.",
    },
    {
        "id": "ks4-health-disease-s01",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person with no illness at all might still not "
                "be considered healthy.",
        "options": [
            "They may not have been vaccinated against every communicable disease",
            "They may be carrying a pathogen without showing any symptoms yet",
            "Health includes mental and social wellbeing, not just no disease",
            "They may have inherited genes that raise their risk of disease later",
        ],
        "correct_index": 2,
        "why": "Health is defined as complete physical, mental and social "
               "wellbeing, so poor mental health alone makes a person unhealthy.",
    },
    {
        "id": "ks4-health-disease-s02",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person living with HIV is more likely to catch "
                "other infections.",
        "options": [
            "HIV damages the immune system, so pathogens are fought off less well",
            "HIV is spread in exactly the same way as every other disease is",
            "HIV makes a person produce far too many antibodies all at once",
            "HIV changes a person's diet, and that weakens the body over a long time",
        ],
        "correct_index": 0,
        "why": "One disease can raise the risk of another: HIV attacks immune "
               "cells, leaving the body less able to defend itself.",
    },
    {
        "id": "ks4-health-disease-s03",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient having chemotherapy for cancer keeps catching "
                "infections. Explain the link between the two.",
        "options": [
            "Chemotherapy drugs are themselves pathogens that spread in the body",
            "Chemotherapy damages rapidly dividing cells, including immune cells",
            "Chemotherapy makes cancer communicable, so infections spread easily",
            "Chemotherapy raises body temperature, which helps bacteria to grow",
        ],
        "correct_index": 1,
        "why": "Treatment for one disease can raise the risk of another: "
               "chemotherapy suppresses the immune system as a side effect.",
    },
    {
        "id": "ks4-health-disease-s04",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the difference between a lifestyle risk factor and "
                "a genetic risk factor, using an example of each.",
        "options": [
            "Lifestyle factors are inherited, while genetic factors are freely chosen",
            "Lifestyle factors cause disease; genetic factors only correlate",
            "Lifestyle factors affect adults only; genetic ones affect children",
            "A lifestyle factor such as smoking can be changed; an inherited one cannot",
        ],
        "correct_index": 3,
        "why": "The distinction is whether the factor can be modified: "
               "smoking is a choice, an inherited predisposition is not.",
    },
    {
        "id": "ks4-health-disease-h01",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A survey finds that towns with more fast-food shops have "
                "higher rates of type 2 diabetes. Evaluate what this shows.",
        "options": [
            "A correlation only — income or exercise levels may also explain it",
            "That fast food is the only cause of type 2 diabetes in those towns",
            "That having type 2 diabetes causes fast-food shops to open in a town",
            "Nothing whatever, because population surveys can never show a link",
        ],
        "correct_index": 0,
        "why": "A link between two things measured together is a correlation; "
               "other factors must be ruled out before causation is claimed.",
    },
    {
        "id": "ks4-health-disease-h02",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a heavy smoker may never develop lung cancer "
                "while some people who have never smoked do.",
        "options": [
            "Lung cancer is communicable, so it depends on who a person meets",
            "Smoking is only a risk factor for heart disease, not for cancer",
            "A risk factor raises the probability of disease, but not to certainty",
            "The non-smoker must in fact have smoked at some point without realising it",
        ],
        "correct_index": 2,
        "why": "Risk factors shift the odds across a population; they do not "
               "decide what happens to any one individual.",
    },
    {
        "id": "ks4-health-disease-h03",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why non-communicable diseases have become more common "
                "in wealthier countries.",
        "options": [
            "Pathogens spread more easily where more people live close together",
            "People in wealthier countries inherit more faulty genes than others",
            "Vaccination against non-communicable disease is not available yet",
            "Diets high in fat, sugar and salt, and less exercise, are common",
        ],
        "correct_index": 3,
        "why": "Non-communicable disease tracks lifestyle, and richer "
               "countries tend to have higher-fat diets and less activity.",
    },
    {
        "id": "ks4-health-disease-h04",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why obesity is described as a risk factor for several "
                "different diseases at the same time.",
        "options": [
            "Obesity is a pathogen that can settle in several organs at once",
            "It raises blood pressure and cholesterol, which harm several organs",
            "Obesity is inherited, so any disease running in a family gets likelier",
            "Obesity makes a person less likely to see a doctor, so all go untreated",
        ],
        "correct_index": 1,
        "why": "One risk factor can act through several routes, so obesity "
               "raises the risk of diabetes, heart disease and some cancers.",
    },

    # ── cancer ──────────────────────────────────────────────────────────
    {
        "id": "ks4-cancer-e01",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what cancer is caused by.",
        "options": [
            "Uncontrolled cell division following mutations in regulatory genes",
            "Bacteria that invade a tissue and then multiply inside its cells",
            "Cells shrinking and dying faster than the body can replace them",
            "A shortage of oxygen reaching one particular organ of the body",
        ],
        "correct_index": 0,
        "why": "Mutations in the genes that control the cell cycle stop the "
               "'stop dividing' signal working, so cells divide without limit.",
    },
    {
        "id": "ks4-cancer-e02",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process by which cancer cells spread from the "
                "original tumour to other organs.",
        "options": [
            "Emulsification",
            "Translocation",
            "Denaturation",
            "Metastasis",
        ],
        "correct_index": 3,
        "why": "Metastasis is cells breaking away and travelling in the blood "
               "or lymph to form secondary tumours elsewhere.",
    },
    {
        "id": "ks4-cancer-e03",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the treatment that uses high-energy radiation aimed "
                "directly at a tumour.",
        "options": [
            "Chemotherapy",
            "Surgery",
            "Radiotherapy",
            "A daily course of statins",
        ],
        "correct_index": 2,
        "why": "Radiotherapy directs gamma rays or X-rays at the tumour, "
               "damaging the DNA of its cells so they cannot divide.",
    },
    {
        "id": "ks4-cancer-e04",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name given to a mass of cells produced by "
                "uncontrolled cell division.",
        "options": [
            "A plaque",
            "A tumour",
            "A clot",
            "A villus",
        ],
        "correct_index": 1,
        "why": "A tumour is the mass that accumulates; whether it is cancer "
               "depends on whether it is benign or malignant.",
    },
    {
        "id": "ks4-cancer-s01",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how radiotherapy destroys cancer cells.",
        "options": [
            "It raises the temperature of the tumour until its cells denature",
            "It damages the DNA of the cells so that they can no longer divide",
            "It cuts off the blood supply so the tumour is starved of oxygen",
            "It carries drugs in the blood to every cancer cell in the body",
        ],
        "correct_index": 1,
        "why": "High-energy radiation damages DNA, and a cell that cannot "
               "divide cannot keep the tumour growing.",
    },
    {
        "id": "ks4-cancer-s02",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why surgery alone may not cure a cancer that has "
                "already spread.",
        "options": [
            "Secondary tumours have formed elsewhere and cannot all be cut out",
            "Surgery makes the remaining cancer cells divide even more quickly",
            "Surgery cannot be used on any tumour that has its own blood supply",
            "Removing a tumour turns the cells left behind from benign to malignant",
        ],
        "correct_index": 0,
        "why": "Once cells have metastasised there are tumours in many places, "
               "so removing the original one leaves the rest behind.",
    },
    {
        "id": "ks4-cancer-s03",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a benign tumour growing in the brain can still "
                "be dangerous.",
        "options": [
            "It spreads through the blood to the lungs and forms new tumours",
            "It always turns into a malignant tumour if it is left untreated",
            "It releases a poison into the blood that damages other organs",
            "It can press on vital parts of the brain as it grows larger",
        ],
        "correct_index": 3,
        "why": "Benign means it does not spread, not that it is harmless — a "
               "growing mass can still squeeze the tissue around it.",
    },
    {
        "id": "ks4-cancer-s04",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how HPV is linked to cancer.",
        "options": [
            "It is a bacterium that produces a carcinogenic waste product",
            "It weakens the immune system so that every cancer becomes likelier",
            "It is a virus that causes most cases of cervical cancer",
            "It is a chemical in tobacco smoke that damages DNA in cells",
        ],
        "correct_index": 2,
        "why": "HPV is a viral risk factor: infection with it causes the great "
               "majority of cervical cancer cases.",
    },
    {
        "id": "ks4-cancer-h01",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the way chemotherapy and surgery reach cancer cells "
                "in the body.",
        "options": [
            "Both reach only the original tumour and leave any spread untreated",
            "Chemotherapy removes the tumour physically; surgery uses drugs",
            "Surgery removes one tumour; chemotherapy travels in the blood",
            "Both travel in the blood, but only surgery harms healthy cells",
        ],
        "correct_index": 2,
        "why": "Surgery can only reach a tumour a surgeon can find, while "
               "drugs in the bloodstream reach dividing cells anywhere.",
    },
    {
        "id": "ks4-cancer-h02",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient having chemotherapy is advised to avoid crowded "
                "places because of infection risk. Explain why.",
        "options": [
            "Chemotherapy drugs spread from person to person in crowded places",
            "Bone marrow cells divide fast, so the white blood cell count falls",
            "Chemotherapy makes the patient's cancer communicable to others",
            "Crowds raise the patient's body temperature, helping tumours grow",
        ],
        "correct_index": 1,
        "why": "Chemotherapy targets any rapidly dividing cell, and bone "
               "marrow makes white blood cells, so immunity is suppressed.",
    },
    {
        "id": "ks4-cancer-h03",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A long-term smoker develops bladder cancer. Suggest how "
                "smoking can cause a cancer so far from the lungs.",
        "options": [
            "Carcinogens are absorbed into the blood and carried to other organs",
            "Tumour cells travel from the lung to the bladder, so it is one cancer",
            "Smoke is swallowed and passes through the gut to reach the bladder",
            "Bladder cancer is inherited, and smokers are likelier to inherit it",
        ],
        "correct_index": 0,
        "why": "Carcinogens from tobacco smoke enter the blood at the lungs "
               "and can damage DNA in cells anywhere the blood carries them.",
    },
    {
        "id": "ks4-cancer-h04",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two patients are diagnosed with a tumour of the same size. "
                "One is benign and one malignant. Predict the difference in "
                "outlook and explain it.",
        "options": [
            "The benign one is worse, as it sits in a capsule that cannot be cut",
            "The outlook is the same, since both are masses of dividing cells",
            "The malignant one is easier to treat, as drugs in blood can reach it",
            "The malignant one is more serious, as its cells can start new tumours",
        ],
        "correct_index": 3,
        "why": "Size is not what decides the danger: a malignant tumour's "
               "cells can break away and seed tumours in other organs.",
    },

    # ── plant-tissues ───────────────────────────────────────────────────
    {
        "id": "ks4-plant-tissues-e01",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the plant organ that anchors the plant and absorbs "
                "water and mineral ions from the soil.",
        "options": [
            "The leaf",
            "The stem",
            "The root",
            "The flower",
        ],
        "correct_index": 2,
        "why": "Roots hold the plant in the soil and take up the water and "
               "mineral ions that the xylem then carries upwards.",
    },
    {
        "id": "ks4-plant-tissues-e02",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the substance that strengthens and waterproofs the "
                "walls of xylem cells.",
        "options": [
            "Cellulose",
            "Lignin",
            "Chlorophyll",
            "Sucrose",
        ],
        "correct_index": 1,
        "why": "Lignin makes xylem walls hard and waterproof, so the tubes "
               "stay open and do not collapse as water is pulled up them.",
    },
    {
        "id": "ks4-plant-tissues-e03",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where most of the stomata are found on a typical leaf.",
        "options": [
            "On the lower surface",
            "On the upper surface",
            "Inside the xylem vessels",
            "Around the base of the stem",
        ],
        "correct_index": 0,
        "why": "Stomata are concentrated on the shaded lower surface, where "
               "less direct sun means less water is lost through them.",
    },
    {
        "id": "ks4-plant-tissues-e04",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the perforated end walls that let sugar solution pass "
                "along a phloem tube.",
        "options": [
            "Guard cells",
            "Air spaces",
            "Lignin rings",
            "Sieve plates",
        ],
        "correct_index": 3,
        "why": "Sieve plates are the pierced end walls between phloem cells, "
               "letting the sugar solution flow from one cell to the next.",
    },
    {
        "id": "ks4-plant-tissues-s01",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a leaf is classified as an organ.",
        "options": [
            "It is made of one type of cell, all carrying out photosynthesis",
            "It is an organ system, because it contains veins as well as cells",
            "It works with the stem and root, so those three form one organ",
            "It contains several different tissues working together for one job",
        ],
        "correct_index": 3,
        "why": "Mesophyll, epidermis, xylem and phloem are separate tissues, "
               "and a structure combining several tissues is an organ.",
    },
    {
        "id": "ks4-plant-tissues-s02",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how guard cells close the stomata at night.",
        "options": [
            "They lose water, become floppy, and the pore between them closes",
            "They take in water, swell up, and squeeze the pore shut between them",
            "They divide to make new cells that block the pore up completely",
            "They produce a waxy layer that seals the pore over until morning",
        ],
        "correct_index": 0,
        "why": "Turgid guard cells bend apart and open the pore; when they "
               "lose water they go flaccid and the pore closes.",
    },
    {
        "id": "ks4-plant-tissues-s03",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the upper epidermis of a leaf is thin and "
                "transparent.",
        "options": [
            "It allows water to evaporate quickly from the top of the leaf",
            "It lets carbon dioxide diffuse straight through to the mesophyll",
            "It lets light pass through to the palisade cells beneath it",
            "It stops the leaf being eaten by insects and other animals",
        ],
        "correct_index": 2,
        "why": "The palisade cells below hold most of the chloroplasts, so the "
               "layer above them must not block the light reaching them.",
    },
    {
        "id": "ks4-plant-tissues-s04",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the role of companion cells in phloem tissue.",
        "options": [
            "They store the sucrose away until the plant needs it during winter",
            "They supply the energy used to load sucrose into the sieve tubes",
            "They carry water up to the leaves alongside the xylem vessels",
            "They form the sieve plates at the end of each phloem cell",
        ],
        "correct_index": 1,
        "why": "Sieve tube cells have little cytoplasm of their own, so the "
               "companion cell beside them supplies the energy for loading.",
    },
    {
        "id": "ks4-plant-tissues-h01",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a xylem vessel with a phloem sieve tube.",
        "options": [
            "Both are living: xylem carries the water and phloem the sugars",
            "Xylem is dead and hollow and carries water; phloem is living",
            "Xylem is living and carries sugars; phloem is dead and carries water",
            "Both are dead, but only xylem is strengthened by lignin in its walls",
        ],
        "correct_index": 1,
        "why": "Xylem is dead, hollow and lignified for water; phloem is "
               "living, with sieve plates and companion cells, for sugars.",
    },
    {
        "id": "ks4-plant-tissues-h02",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is kept in complete darkness for two days. Predict "
                "what happens to its stomata and to photosynthesis.",
        "options": [
            "Stomata open wider, so more carbon dioxide enters and the rate rises",
            "Stomata stay exactly as they were, since light does not affect them",
            "Stomata close, but photosynthesis continues using stored light energy",
            "Stomata close, so little carbon dioxide enters — and there is no light",
        ],
        "correct_index": 3,
        "why": "Guard cells lose water in the dark and close the pores, and "
               "without light photosynthesis cannot happen in any case.",
    },
    {
        "id": "ks4-plant-tissues-h03",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a plant growing in a hot desert may have a much "
                "thicker waxy cuticle than one growing in a shaded wood.",
        "options": [
            "A thicker cuticle reduces water loss, which matters far more in dry heat",
            "A thicker cuticle lets more light reach the palisade cells in bright sun",
            "A thicker cuticle allows more carbon dioxide into the leaf for photosynthesis",
            "A thicker cuticle helps the leaf absorb water straight from the dry air",
        ],
        "correct_index": 0,
        "why": "The cuticle is a waterproof layer, so a thicker one cuts "
               "evaporation from the leaf surface where water is scarce.",
    },
    {
        "id": "ks4-plant-tissues-h04",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A complete ring of bark, which contains the phloem, is cut "
                "away from around a tree trunk. Predict the effect on the "
                "roots and explain it.",
        "options": [
            "The roots die, because water can no longer travel down from leaves",
            "The roots are unaffected, as they make their own sugars underground",
            "The roots are starved of sugar, as the route from the leaves is cut",
            "The roots grow faster, as sugar builds up below the cut in the phloem",
        ],
        "correct_index": 2,
        "why": "Roots do not photosynthesise, so cutting the phloem removes "
               "the only route by which sugar reaches them from the leaves.",
    },

    # ── transpiration ───────────────────────────────────────────────────
    {
        "id": "ks4-transpiration-e01",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the apparatus used to measure the rate of water uptake "
                "by a leafy shoot.",
        "options": [
            "A calorimeter",
            "A burette",
            "A gas syringe",
            "A potometer",
        ],
        "correct_index": 3,
        "why": "A potometer times how far an air bubble travels along a "
               "capillary tube as the shoot draws water up.",
    },
    {
        "id": "ks4-transpiration-e02",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the part of the plant from which most water is lost "
                "during transpiration.",
        "options": [
            "The root hairs",
            "The waxy cuticle",
            "The stomata in the leaves",
            "The phloem sieve tubes in the stem",
        ],
        "correct_index": 2,
        "why": "Water vapour escapes mainly through the open stomata, which "
               "is why closing them is a plant's defence against drying out.",
    },
    {
        "id": "ks4-transpiration-e03",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name given to the continuous movement of water "
                "from the roots up to the leaves.",
        "options": [
            "Translocation",
            "The transpiration stream",
            "Active loading of minerals",
            "Emulsification",
        ],
        "correct_index": 1,
        "why": "The transpiration stream is the unbroken column of water "
               "drawn up the xylem as water evaporates from the leaves.",
    },
    {
        "id": "ks4-transpiration-e04",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a potometer actually measures.",
        "options": [
            "The volume of water taken up by the shoot",
            "The mass of sugar made by the leaves",
            "The volume of oxygen given off by the shoot",
            "The number of stomata open on the leaves",
        ],
        "correct_index": 0,
        "why": "The moving bubble tracks water entering the shoot, which is "
               "used as an indicator of the transpiration rate.",
    },
    {
        "id": "ks4-transpiration-s01",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a potometer the air bubble moves 60 mm along the "
                "capillary tube in 5 minutes. Calculate the rate of water "
                "uptake in mm/min.",
        "options": [
            "12 mm/min",
            "300 mm/min",
            "0.083 mm/min",
            "55 mm/min",
        ],
        "correct_index": 0,
        "why": "Rate is distance divided by time: 60 mm ÷ 5 min = 12 mm/min.",
    },
    {
        "id": "ks4-transpiration-s02",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a potometer is said to measure water uptake "
                "rather than transpiration itself.",
        "options": [
            "Water taken up is always far greater than the water ever lost",
            "The bubble measures air entering the shoot, not water leaving it",
            "Transpiration happens only in light, but uptake happens all the time",
            "A little of the water taken up is used by the plant, not evaporated",
        ],
        "correct_index": 3,
        "why": "Some water taken up is used in photosynthesis and to keep "
               "cells turgid, so uptake is only an indicator of water loss.",
    },
    {
        "id": "ks4-transpiration-s03",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant wilts on a hot, dry day.",
        "options": [
            "The stomata open wider in the heat so more carbon dioxide enters",
            "The phloem stops carrying sugar, so the leaves run out of energy",
            "Water is lost faster than the roots take it up, so cells go floppy",
            "The xylem vessels collapse because their lignin softens in the heat",
        ],
        "correct_index": 2,
        "why": "Wilting is a water balance problem: once loss outruns uptake "
               "the cells lose turgor and the leaves droop.",
    },
    {
        "id": "ks4-transpiration-s04",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how transpiration helps a plant to obtain the "
                "mineral ions it needs.",
        "options": [
            "Minerals are made in the leaves and washed down by water to the roots",
            "Minerals dissolved in the water are carried up from roots to leaves",
            "Minerals enter through the stomata as the water vapour leaves them",
            "Minerals are loaded into the phloem by the companion cells beside it",
        ],
        "correct_index": 1,
        "why": "Mineral ions dissolve in the water taken up by the roots and "
               "travel with it up the xylem in the transpiration stream.",
    },
    {
        "id": "ks4-transpiration-h01",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical shoots are set up in potometers. One has a fan "
                "blowing across it and one does not. Predict which takes up "
                "water faster and explain why.",
        "options": [
            "The still one, because moist air around its leaves keeps stomata open",
            "Both take up water equally, because they have the same leaf area",
            "The one with the fan, because moving air keeps the gradient steep",
            "The still one, because moving air cools the leaves and slows loss",
        ],
        "correct_index": 2,
        "why": "Wind removes the humid layer of air next to the stomata, so "
               "the water vapour gradient out of the leaf stays steep.",
    },
    {
        "id": "ks4-transpiration-h02",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a potometer a bubble moves 45 mm in 3 minutes at 20 °C, "
                "and 45 mm in 90 seconds at 30 °C. Calculate how many times "
                "faster the rate is at 30 °C.",
        "options": [
            "2 times faster",
            "0.5 times faster",
            "3 times faster",
            "1.5 times faster",
        ],
        "correct_index": 0,
        "why": "15 mm/min at 20 °C and 30 mm/min at 30 °C, and 30 ÷ 15 = 2.",
    },
    {
        "id": "ks4-transpiration-h03",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student coats the lower surface of a leaf with petroleum "
                "jelly. Predict the effect on transpiration and explain it.",
        "options": [
            "It rises sharply, as water is forced out through the upper surface",
            "It falls sharply, as most stomata are on that surface and are blocked",
            "It stays the same, as water evaporates equally from both surfaces",
            "It falls slightly, as the jelly only slows water moving up the xylem",
        ],
        "correct_index": 1,
        "why": "Nearly all the stomata are on the lower surface, so sealing "
               "it blocks the main route by which water vapour escapes.",
    },
    {
        "id": "ks4-transpiration-h04",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant sealed inside a clear plastic bag "
                "transpires more slowly after an hour.",
        "options": [
            "The plant runs out of water in its xylem after about an hour",
            "The bag blocks the light, so the guard cells close every stoma",
            "Carbon dioxide builds up inside the bag and forces the stomata to shut",
            "Water vapour builds up, so the gradient out of the leaf is shallow",
        ],
        "correct_index": 3,
        "why": "Trapped water vapour raises the humidity around the leaf, so "
               "the concentration gradient driving evaporation flattens.",
    },

    # ── translocation ───────────────────────────────────────────────────
    {
        "id": "ks4-translocation-e01",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a 'source' in translocation.",
        "options": [
            "Any part of the plant where sugars are stored away as starch",
            "The part of the plant where sugars are made, mainly the leaves",
            "The vessel that carries sugars from one part of the plant to another",
            "The pore through which water vapour leaves the surface of the leaf",
        ],
        "correct_index": 1,
        "why": "The source is where sucrose is loaded into the phloem — "
               "usually the leaves, where photosynthesis makes it.",
    },
    {
        "id": "ks4-translocation-e02",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of cell that supplies the energy for loading "
                "sucrose into a phloem sieve tube.",
        "options": [
            "A guard cell",
            "A palisade cell",
            "A companion cell",
            "A root hair cell",
        ],
        "correct_index": 2,
        "why": "Companion cells sit beside the sieve tubes and provide the "
               "energy that loading sucrose into them requires.",
    },
    {
        "id": "ks4-translocation-e03",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which description fits phloem sieve tubes.",
        "options": [
            "Dead, hollow cells strengthened with lignin in their walls",
            "Dead cells joined end to end with perforated end walls",
            "Living cells with lignified walls and no end walls at all",
            "Living cells with perforated end walls called sieve plates",
        ],
        "correct_index": 3,
        "why": "Phloem cells stay alive and are joined by sieve plates; it is "
               "xylem that is dead, hollow and lignified.",
    },
    {
        "id": "ks4-translocation-e04",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process by which dissolved sugars are moved through "
                "the phloem of a plant.",
        "options": [
            "Translocation",
            "Transpiration",
            "Emulsification",
            "Phagocytosis",
        ],
        "correct_index": 0,
        "why": "Translocation is the movement of dissolved sugars in phloem; "
               "transpiration is the loss of water from the leaves.",
    },
    {
        "id": "ks4-translocation-s01",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why translocation requires energy but the "
                "transpiration stream does not.",
        "options": [
            "Sugars are heavier than water, so more force is needed to move them",
            "Phloem tubes are much narrower than xylem, so flow has to be pushed",
            "Sucrose is actively loaded into phloem; water is pulled by evaporation",
            "Water moves down with gravity, while all the sugars must be carried upwards",
        ],
        "correct_index": 2,
        "why": "Evaporation from the leaves does the work in xylem for free, "
               "while loading sucrose into phloem has to be paid for.",
    },
    {
        "id": "ks4-translocation-s02",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In summer a potato plant's leaves make sugar and its tubers "
                "store starch. Explain the role of a tuber at this time.",
        "options": [
            "It is a source, because it holds the plant's supply of stored sugar",
            "It is neither, because starch is never moved through the phloem",
            "It is a source, because sucrose is loaded into the phloem there",
            "It is a sink, because sucrose is unloaded there and stored as starch",
        ],
        "correct_index": 3,
        "why": "A sink is anywhere sucrose is unloaded to be used or stored, "
               "and in summer the tuber is storing it as starch.",
    },
    {
        "id": "ks4-translocation-s03",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sugars must be able to travel downwards in a "
                "plant as well as upwards.",
        "options": [
            "Roots do not photosynthesise, so sugar must be sent down to them",
            "Sugar is made in the roots and must travel up to the leaves to be used",
            "Water travels downwards in the xylem, and the sugar must follow it",
            "Sugar would be lost through the stomata if it only travelled upwards",
        ],
        "correct_index": 0,
        "why": "Roots are underground and make no sugar of their own, so the "
               "phloem must carry sucrose down to them for respiration.",
    },
    {
        "id": "ks4-translocation-s04",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to sucrose when it arrives at a sink.",
        "options": [
            "It evaporates out of the phloem through the nearest open stomata",
            "It is unloaded and then used in respiration or stored as starch",
            "It is loaded into the xylem and carried back up to the leaves",
            "It stays inside the sieve tube until the plant needs it in winter",
        ],
        "correct_index": 1,
        "why": "At the sink sucrose leaves the phloem to be respired or "
               "converted to starch, which keeps the flow towards that sink.",
    },
    {
        "id": "ks4-translocation-h01",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says 'transpiration and translocation both carry "
                "water up the plant'. Evaluate this statement.",
        "options": [
            "Fully correct — both processes move water upwards through the plant",
            "Half correct — translocation moves the water up, and transpiration sugars",
            "Fully wrong — neither process involves water moving inside a plant",
            "Half correct — transpiration moves water up, translocation sugars both ways",
        ],
        "correct_index": 3,
        "why": "Transpiration moves water up the xylem only; translocation "
               "moves dissolved sugars through the phloem in either direction.",
    },
    {
        "id": "ks4-translocation-h02",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An aphid pushes a needle-like mouthpart into a single phloem "
                "tube and sugary liquid flows out on its own. Explain what "
                "this shows about translocation.",
        "options": [
            "The phloem contents are under pressure, created by loading at the source",
            "The phloem is a hollow dead tube, so liquid escapes as soon as it is opened",
            "The aphid must pump the sap out, as phloem is not under any pressure",
            "Sugar is carried in the xylem, and the aphid has reached that instead",
        ],
        "correct_index": 0,
        "why": "Sugar loaded at the source draws in water and builds pressure, "
               "which is what drives the solution along and out of a puncture.",
    },
    {
        "id": "ks4-translocation-h03",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "All the leaves are stripped from a healthy plant. Predict "
                "the effect on translocation and explain it.",
        "options": [
            "It continues unchanged, because the roots make their own sucrose",
            "It reverses permanently, carrying sugar up from the roots for ever",
            "It slows and stops, because the main source of sucrose has gone",
            "It speeds up, because sucrose no longer has to be loaded at a leaf",
        ],
        "correct_index": 2,
        "why": "The leaves are the source that loads sucrose into the phloem, "
               "so with them removed there is nothing left to translocate.",
    },
    {
        "id": "ks4-translocation-h04",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why translocation stops when a plant's respiration "
                "is blocked, while the transpiration stream keeps going.",
        "options": [
            "Respiration produces the water that the phloem needs to carry sugar",
            "Loading sucrose needs energy from respiration; transpiration needs none",
            "Respiration opens the stomata, and translocation cannot happen while shut",
            "Transpiration also needs energy, but the xylem has days of it stored",
        ],
        "correct_index": 1,
        "why": "Translocation depends on energy released by respiration to "
               "load sucrose, while transpiration is driven by evaporation.",
    },
]
