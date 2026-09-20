"""Biology · Bioenergetics — the MRB-338 expansion of `aerobic-respiration`.

One leaf only: AQA 8461 §4.4.2.1. The original twelve rows in
`bioenergetics.py` take the balanced symbol equation, the exothermic
classification, the ~36-38 ATP yield, the cristae, why the coefficient 6
appears twice, active transport's need for ATP, a yeast-versus-liver-cell
product comparison, body temperature rising on a run, a cristae-blocking
drug's effect on a heart cell, complete breakdown releasing more energy,
the eighteen-fold ATP gap against anaerobic respiration, and the "energy
is created in the mitochondria" misconception.

This file takes what they leave: ATP as the energy currency spent on
muscle contraction, active transport, protein synthesis and cell
division; the breathing-versus-respiration distinction from a fresh
scenario each time rather than the lesson's own quiz stem; named cells
built around a high mitochondrial count — sperm, liver, heart — and why;
a run of ATP-yield arithmetic in both directions; and a set of predict
and evaluate items that test the same handful of facts from unfamiliar
angles: a poisoned mitochondrion, a cooled donor organ, a lizard's low
demand, a cell engineered with extra cristae surface area.

Numbers here use the same rough 37 ATP per glucose figure the baseline
gives as "36-38", rounded to a workable 37 throughout so every
calculation comes out clean.
"""

TOPIC = "bioenergetics"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═══════════════════════════════════════
    {
        "id": "ks4-aerobic-respiration-e05",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the organelle in which aerobic respiration takes place.",
        "options": [
            "Mitochondria",
            "Ribosomes",
            "The nucleus",
            "Chloroplasts",
        ],
        "correct_index": 0,
        "why": "Aerobic respiration takes place inside a cell's mitochondria.",
    },
    {
        "id": "ks4-aerobic-respiration-e06",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the letters ATP stand for.",
        "options": [
            "Amino transfer protein",
            "Adenosine triphosphate",
            "Active transport protein",
            "Aerobic transfer particle",
        ],
        "correct_index": 1,
        "why": "ATP stands for adenosine triphosphate, the molecule that directly powers a "
               "cell's activities.",
    },
    {
        "id": "ks4-aerobic-respiration-e07",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these processes is powered directly by ATP.",
        "options": [
            "Diffusion of oxygen into a cell",
            "Osmosis of water into a root hair cell",
            "Contraction of a muscle fibre",
            "Reflection of light by a chloroplast",
        ],
        "correct_index": 2,
        "why": "Muscle contraction is an active process that needs the energy ATP supplies; "
               "diffusion and osmosis need no ATP.",
    },
    {
        "id": "ks4-aerobic-respiration-e08",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State when aerobic respiration happens in a living cell.",
        "options": [
            "Just during exercise",
            "Just while a person is awake, not at any other time of the day",
            "Just inside muscle cells",
            "All the time, in every living cell",
        ],
        "correct_index": 3,
        "why": "Aerobic respiration runs continuously, day and night, in every living cell.",
    },
    {
        "id": "ks4-aerobic-respiration-e09",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these cells would be expected to contain the most "
               "mitochondria.",
        "options": [
            "A sperm cell",
            "A skin cell",
            "A mature red blood cell",
            "A bone cell",
        ],
        "correct_index": 0,
        "why": "A sperm cell needs a constant, large supply of ATP to power its flagellum, "
               "so it is packed with mitochondria.",
    },
    {
        "id": "ks4-aerobic-respiration-e10",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the folded structures inside a mitochondrion that increase its surface "
               "area.",
        "options": [
            "Villi",
            "Cristae",
            "Alveoli",
            "Microvilli",
        ],
        "correct_index": 1,
        "why": "Cristae are the folded inner membranes that give a mitochondrion a large "
               "surface area for its reactions.",
    },
    {
        "id": "ks4-aerobic-respiration-e11",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these, besides carbon dioxide, is released by aerobic "
               "respiration.",
        "options": [
            "Oxygen",
            "Glucose",
            "Water",
            "ATP molecules leaving the cell",
        ],
        "correct_index": 2,
        "why": "Water is made when the hydrogen from glucose combines with oxygen during "
               "aerobic respiration.",
    },
    {
        "id": "ks4-aerobic-respiration-e12",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name two body organs whose cells hold unusually many mitochondria because of "
               "their high energy demand.",
        "options": [
            "The skin and the hair",
            "The bones and the nails",
            "The stomach lining and the teeth",
            "The liver and the heart",
        ],
        "correct_index": 3,
        "why": "Liver cells and heart muscle cells both carry out very energy-demanding "
               "work, so both are rich in mitochondria.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════
    {
        "id": "ks4-aerobic-respiration-s05",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that holding your breath stops respiration happening in your "
               "cells. Explain why this is wrong.",
        "options": [
            "Respiration is a chemical process in cells, separate from breathing",
            "Holding your breath stops your heart from beating too",
            "Respiration happens in the lungs, but not in other cells",
            "Breathing and respiration are simply two names for the same process",
        ],
        "correct_index": 0,
        "why": "Breathing moves air physically; respiration is the chemical reaction "
               "releasing energy inside cells, and the two are not the same process.",
    },
    {
        "id": "ks4-aerobic-respiration-s06",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sperm cells contain unusually large numbers of mitochondria.",
        "options": [
            "Sperm cells store extra oxygen inside their many mitochondria",
            "They need extra ATP to power the whipping of their flagellum",
            "Mitochondria protect the sperm's DNA from damage",
            "Sperm cells respire anaerobically, which needs more mitochondria",
        ],
        "correct_index": 1,
        "why": "Swimming towards an egg needs continuous ATP for the flagellum, so sperm "
               "cells carry unusually many mitochondria.",
    },
    {
        "id": "ks4-aerobic-respiration-s07",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why liver cells contain a large number of mitochondria.",
        "options": [
            "Liver cells store more oxygen than most other body cells",
            "Liver cells need extra water for the reactions they carry out",
            "Liver cells carry out many energy-demanding reactions and need plenty of ATP",
            "Liver cells respire mainly at night, needing extra mitochondria to catch up",
        ],
        "correct_index": 2,
        "why": "The liver's many chemical reactions demand a constant, large supply of ATP, "
               "so its cells hold many mitochondria.",
    },
    {
        "id": "ks4-aerobic-respiration-s08",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's muscle cells are found to contain far fewer mitochondria than "
               "normal. Suggest the most likely effect on the muscle.",
        "options": [
            "The muscle would contract more powerfully than normal",
            "The muscle would need less oxygen than before",
            "The muscle would store more glucose as a result",
            "The muscle would tire more quickly, from a shortage of ATP",
        ],
        "correct_index": 3,
        "why": "Fewer mitochondria means less ATP can be released per minute, so the muscle "
               "tires sooner.",
    },
    {
        "id": "ks4-aerobic-respiration-s09",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a cell described as 'metabolically very active' needs a good "
               "supply of oxygen.",
        "options": [
            "Aerobic respiration, which needs oxygen, supplies most of its ATP",
            "Oxygen is itself the fuel that active cells burn for energy",
            "Active cells convert oxygen directly into glucose for storage",
            "Oxygen is needed to cool a metabolically active cell down",
        ],
        "correct_index": 0,
        "why": "Aerobic respiration is what supplies most of an active cell's ATP, and it "
               "depends on a steady oxygen supply.",
    },
    {
        "id": "ks4-aerobic-respiration-s10",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the amount of ATP released by aerobic respiration with the amount "
               "released by anaerobic respiration.",
        "options": [
            "Aerobic respiration releases far less ATP per glucose molecule",
            "Aerobic respiration releases far more ATP per glucose molecule",
            "Both release exactly the same amount of ATP per glucose molecule",
            "Anaerobic respiration releases ATP, but aerobic respiration releases none",
        ],
        "correct_index": 1,
        "why": "Complete breakdown with oxygen releases roughly eighteen times as much ATP "
               "per glucose molecule as the anaerobic route.",
    },
    {
        "id": "ks4-aerobic-respiration-s11",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell's mitochondria are damaged by a poison. Predict the effect on the "
               "cell's ATP supply, and explain.",
        "options": [
            "ATP supply would rise, since damaged mitochondria release ATP directly",
            "ATP supply would be unaffected, since ATP is made in the cytoplasm instead",
            "ATP supply would fall sharply, since aerobic respiration could no longer "
            "take place there",
            "ATP supply would fall just if the cell also stopped taking in glucose",
        ],
        "correct_index": 2,
        "why": "With its mitochondria damaged, a cell loses the site of aerobic respiration "
               "and so loses most of its ATP supply.",
    },
    {
        "id": "ks4-aerobic-respiration-s12",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a runner's muscle cells consume oxygen faster during a race than "
               "at rest.",
        "options": [
            "Running warms the muscle, needing extra oxygen",
            "Running increases the muscle's need for glucose, but not for oxygen",
            "Resting muscle respires faster than exercising muscle does",
            "Contracting muscle needs more ATP, so it respires aerobically faster",
        ],
        "correct_index": 3,
        "why": "Harder-working muscle needs more ATP, and aerobic respiration speeds up to "
               "supply it, using more oxygen.",
    },
    {
        "id": "ks4-aerobic-respiration-s13",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the difference between breathing and respiration.",
        "options": [
            "Breathing moves air in and out of the lungs; respiration is a chemical "
            "reaction in cells",
            "Breathing and respiration both mean exactly the same physical process",
            "Breathing is chemical; respiration is the physical movement of the chest, "
            "which is the reverse of what actually happens in a cell",
            "Breathing happens in cells; respiration happens in the lungs instead",
        ],
        "correct_index": 0,
        "why": "Breathing is the mechanical movement of air; respiration is the separate "
               "chemical process releasing energy in cells.",
    },
    {
        "id": "ks4-aerobic-respiration-s14",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete's resting heart rate can be low, yet their muscles "
               "still receive enough oxygen during a race.",
        "options": [
            "A slow resting heart rate means less oxygen reaches the muscles, regardless "
            "of how well trained the heart itself has become",
            "Training raises the amount of blood pumped per beat, delivering oxygen "
            "efficiently",
            "Training stops the muscles needing any oxygen once fully fit",
            "A slow heart rate means the muscles have stopped respiring aerobically",
        ],
        "correct_index": 1,
        "why": "A trained heart pumps more blood with every beat, so it can deliver enough "
               "oxygen even at a lower rate.",
    },
    {
        "id": "ks4-aerobic-respiration-s15",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug increases the number of mitochondria in a patient's muscle cells. "
               "Predict the effect on their aerobic capacity.",
        "options": [
            "Their capacity would fall, since more mitochondria compete for the same "
            "oxygen",
            "Their capacity would be unaffected, since mitochondria number makes no "
            "difference",
            "Their capacity would rise, since more ATP could be released per minute",
            "Their capacity would rise just if their heart also stopped beating faster",
        ],
        "correct_index": 2,
        "why": "More mitochondria give a cell more capacity to release ATP per minute, "
               "raising its aerobic capacity.",
    },
    {
        "id": "ks4-aerobic-respiration-s16",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why water, as well as carbon dioxide, is a product of aerobic "
               "respiration.",
        "options": [
            "Water is needed to cool the mitochondria as the reaction proceeds",
            "Carbon dioxide reacts with oxygen inside the cell to form water",
            "Water evaporates away once all the glucose has been used up",
            "Water is released when oxygen reacts with the hydrogen from glucose",
        ],
        "correct_index": 3,
        "why": "Glucose's hydrogen atoms combine with oxygen during aerobic respiration, "
               "forming water as a product.",
    },
    {
        "id": "ks4-aerobic-respiration-s17",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell respires 4 molecules of glucose aerobically. Using roughly 37 ATP per "
               "glucose molecule, estimate the total ATP released.",
        "options": [
            "Around 148 ATP",
            "Around 41 ATP",
            "Around 4 ATP",
            "Around 296 ATP",
        ],
        "correct_index": 0,
        "why": "4 molecules x 37 ATP each gives roughly 148 ATP in total.",
    },
    {
        "id": "ks4-aerobic-respiration-s18",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aerobic respiration in a cell releases about 222 ATP. Given roughly 37 ATP "
               "per glucose molecule, work out how many glucose molecules were respired.",
        "options": [
            "222 molecules",
            "6 molecules",
            "37 molecules",
            "12 molecules",
        ],
        "correct_index": 1,
        "why": "222 ATP divided by 37 ATP per glucose gives 6 molecules of glucose respired.",
    },
    {
        "id": "ks4-aerobic-respiration-s19",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a heart muscle cell, which never stops contracting, needs an "
               "especially reliable supply of ATP.",
        "options": [
            "A heart cell stores enough ATP in advance to last several days, far longer "
            "than any cell could really manage without one",
            "A heart cell can pause its contraction if its ATP briefly runs low",
            "A heart cell would stop contracting almost at once without a constant ATP "
            "supply",
            "A heart cell relies on anaerobic respiration for its ATP",
        ],
        "correct_index": 2,
        "why": "A heart cell holds very little spare ATP, so a continuous aerobic supply is "
               "essential to keep it contracting.",
    },
    {
        "id": "ks4-aerobic-respiration-s20",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare where in a cell aerobic respiration takes place with where protein "
               "synthesis takes place.",
        "options": [
            "Both take place in the mitochondria",
            "Aerobic respiration in the nucleus; protein synthesis in the mitochondria",
            "Aerobic respiration in the ribosomes; protein synthesis in the mitochondria",
            "Aerobic respiration in the mitochondria; protein synthesis at the ribosomes",
        ],
        "correct_index": 3,
        "why": "Aerobic respiration happens in the mitochondria, while proteins are "
               "assembled at the ribosomes.",
    },
    {
        "id": "ks4-aerobic-respiration-s21",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a cell that has just divided needs a burst of aerobic "
               "respiration afterwards.",
        "options": [
            "Building the new structures of a fresh daughter cell demands extra ATP",
            "Cell division uses up all of a cell's existing mitochondria",
            "A newly divided cell briefly stops needing any oxygen",
            "Division converts every one of the cell's mitochondria into ribosomes",
        ],
        "correct_index": 0,
        "why": "A new cell has to build fresh membranes and structures, which takes extra "
               "ATP from a burst of aerobic respiration.",
    },
    {
        "id": "ks4-aerobic-respiration-s22",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A poison stops mitochondria using oxygen. Predict the short-term effect on a "
               "person's cells.",
        "options": [
            "Cells would keep respiring aerobically, since the poison affects the lungs "
            "instead",
            "Cells would rapidly run short of ATP, since aerobic respiration would stop",
            "Cells would begin photosynthesising instead",
            "Cells would be unaffected, since oxygen plays no part in this",
        ],
        "correct_index": 1,
        "why": "Blocking oxygen use in the mitochondria stops aerobic respiration, so ATP "
               "production falls quickly.",
    },
    {
        "id": "ks4-aerobic-respiration-s23",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a marathon runner trains at high altitude, where oxygen is "
               "scarcer, in the weeks before a race.",
        "options": [
            "High altitude training removes the need for oxygen during the race",
            "High altitude training stops the muscles respiring aerobically",
            "It encourages the body to adapt so it can supply oxygen more efficiently",
            "High altitude has no effect on how the body supplies oxygen to muscles",
        ],
        "correct_index": 2,
        "why": "Training where oxygen is scarce encourages the body to adapt, so it can "
               "supply oxygen to respiring muscles more efficiently.",
    },
    {
        "id": "ks4-aerobic-respiration-s24",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a small, cold-blooded lizard needs far fewer mitochondria per "
               "cell than a similarly sized warm-blooded mammal.",
        "options": [
            "Lizards do not respire aerobically, unlike mammals",
            "Lizards have a much higher resting energy demand than mammals",
            "Lizards store far more ATP in advance than a mammal ever does",
            "Lizards do not need to maintain a constant high body temperature",
        ],
        "correct_index": 3,
        "why": "A mammal spends a great deal of ATP simply keeping its body warm, a demand a "
               "cold-blooded lizard does not have.",
    },
    {
        "id": "ks4-aerobic-respiration-s25",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why increasing the temperature of a cell's surroundings, up to a "
               "point, speeds up aerobic respiration.",
        "options": [
            "Warmer conditions give the enzymes controlling respiration more kinetic "
            "energy",
            "Warmer conditions convert carbon dioxide back into glucose faster",
            "Warmer conditions let a cell absorb oxygen without using mitochondria, well "
            "beyond anything the enzymes could actually use",
            "Warmer conditions stop water being made during the reaction",
        ],
        "correct_index": 0,
        "why": "Warmth speeds up the enzyme-controlled reactions of respiration, up until "
               "the enzymes' optimum temperature.",
    },
    {
        "id": "ks4-aerobic-respiration-s26",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ten molecules of glucose are respired aerobically in a muscle cell. Taking "
               "the yield as roughly 37 ATP per glucose molecule, calculate the total ATP "
               "this releases.",
        "options": [
            "47 ATP",
            "370 ATP",
            "10 ATP",
            "27 ATP",
        ],
        "correct_index": 1,
        "why": "10 molecules x 37 ATP each gives approximately 370 ATP in total.",
    },

    # ══ harder · h05–h26 ═══════════════════════════════════════
    {
        "id": "ks4-aerobic-respiration-h05",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a cell's energy is 'created' inside its "
               "mitochondria.",
        "options": [
            "It is correct; mitochondria generate entirely new energy from nothing",
            "It is correct, provided the cell is also photosynthesising at the time",
            "It is wrong; energy already stored in glucose is transferred, not created",
            "It is wrong; mitochondria destroy energy rather than transferring it",
        ],
        "correct_index": 2,
        "why": "Energy cannot be created or destroyed; respiration transfers energy already "
               "stored in glucose into ATP.",
    },
    {
        "id": "ks4-aerobic-respiration-h06",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug blocks the cristae of every mitochondrion in a heart muscle cell. "
               "Predict the effect on the heart, and explain.",
        "options": [
            "The heart would beat more strongly, needing less ATP to relax",
            "The heart would switch permanently to anaerobic respiration",
            "The heart would be unaffected, storing enough ATP for a lifetime",
            "The heart would soon fail to contract, starved of the ATP it depends on",
        ],
        "correct_index": 3,
        "why": "Blocking the cristae stops aerobic respiration, and without a steady ATP "
               "supply the heart cannot keep contracting.",
    },
    {
        "id": "ks4-aerobic-respiration-h07",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a scientist measuring a cell's rate of aerobic respiration "
               "chooses to measure oxygen uptake rather than trying to measure ATP directly.",
        "options": [
            "ATP breaks down almost as soon as it forms, but oxygen uptake can be "
            "measured directly and reliably",
            "ATP is impossible to detect in a laboratory under any circumstances, however "
            "sensitive the laboratory equipment being used might be",
            "Oxygen uptake and ATP production are entirely unrelated to one another",
            "Measuring ATP would show a higher rate than measuring oxygen uptake does",
        ],
        "correct_index": 0,
        "why": "ATP is used almost as soon as it is made, so a stable, measurable stand-in "
               "like oxygen uptake gives a far more practical reading of respiration rate.",
    },
    {
        "id": "ks4-aerobic-respiration-h08",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In aerobic respiration, every carbon atom in a glucose molecule ends up in "
               "carbon dioxide. Explain what this shows about the reaction.",
        "options": [
            "Glucose is partly broken down, leaving carbon locked inside it",
            "Glucose is broken down completely, releasing all of its stored energy",
            "Glucose is converted directly into oxygen, releasing no energy",
            "Carbon dioxide is a reactant of aerobic respiration, not a product",
        ],
        "correct_index": 1,
        "why": "Every carbon atom reaching carbon dioxide shows that glucose has been broken "
               "down entirely, releasing the whole of its energy.",
    },
    {
        "id": "ks4-aerobic-respiration-h09",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because respiration needs oxygen, all of a cell's "
               "energy must come directly from the air. Evaluate this argument.",
        "options": [
            "It is correct; oxygen itself is the source of all a cell's energy, with "
            "glucose itself playing no part in the process whatsoever",
            "It is correct, provided the cell has a large number of mitochondria",
            "It is wrong; the energy comes from glucose, and oxygen only allows it to be "
            "released",
            "It is wrong; cells get no energy of any kind from aerobic respiration",
        ],
        "correct_index": 2,
        "why": "Glucose is the true energy store; oxygen is what allows that stored energy "
               "to be released completely.",
    },
    {
        "id": "ks4-aerobic-respiration-h10",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the ATP yield of aerobic respiration with the energy a cell would "
               "gain simply by digesting glucose in the gut.",
        "options": [
            "Digestion in the gut releases more usable ATP than respiration ever could",
            "Both release exactly the same amount of usable ATP for the cell",
            "Digestion releases no usable energy; respiration is what does this",
            "Digestion breaks glucose into smaller units, but only respiration releases "
            "ATP from it",
        ],
        "correct_index": 3,
        "why": "Digestion simply breaks food down into absorbable units; only respiration "
               "inside cells then releases that energy as ATP.",
    },
    {
        "id": "ks4-aerobic-respiration-h11",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A liver cell respires 25 molecules of glucose in an hour. Using a yield of "
               "about 37 ATP per glucose molecule, determine the total ATP produced.",
        "options": [
            "Around 925 ATP",
            "Around 62 ATP",
            "Around 37 ATP",
            "Around 1,480 ATP",
        ],
        "correct_index": 0,
        "why": "25 molecules x 37 ATP each gives roughly 925 ATP in total.",
    },
    {
        "id": "ks4-aerobic-respiration-h12",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's mitochondria are found to have unusually few cristae. Explain "
               "the likely effect on their cells' ATP production.",
        "options": [
            "ATP production would rise, since fewer cristae need less oxygen",
            "ATP production would fall, since less surface area is available for the "
            "reactions",
            "ATP production would be unaffected, since cristae play no part in "
            "respiration",
            "ATP production would stop just if the nucleus were also damaged",
        ],
        "correct_index": 1,
        "why": "Cristae provide the surface area for respiration's reactions, so fewer of "
               "them means less ATP can be released.",
    },
    {
        "id": "ks4-aerobic-respiration-h13",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete's muscle cells develop more mitochondria after months "
               "of endurance training, but not after a single training session.",
        "options": [
            "A single session destroys more mitochondria than it creates",
            "Building new mitochondria happens instantly, within a single session",
            "Building new cell structures takes sustained, repeated demand over time",
            "Mitochondria numbers are fixed at birth and cannot increase",
        ],
        "correct_index": 2,
        "why": "Growing new mitochondria is a gradual adaptation that needs repeated demand "
               "over weeks and months, not a single session.",
    },
    {
        "id": "ks4-aerobic-respiration-h14",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two otherwise identical cells respire glucose aerobically, but one has twice "
               "as many mitochondria as the other. Predict which can sustain a higher rate "
               "of ATP production, and explain.",
        "options": [
            "Neither; mitochondria number has no bearing on how much ATP is made",
            "The cell with fewer mitochondria, since each one then works harder",
            "Both equally, since ATP production depends on the glucose supply instead, so "
            "neither cell's mitochondrial number changes the outcome at all",
            "The cell with more mitochondria, since more surface area drives more ATP "
            "release",
        ],
        "correct_index": 3,
        "why": "More mitochondria give more surface area for respiration's reactions, "
               "allowing a higher maximum rate of ATP production.",
    },
    {
        "id": "ks4-aerobic-respiration-h15",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that doubling a cell's oxygen supply will double its rate "
               "of aerobic respiration in every case.",
        "options": [
            "It is wrong; once glucose or mitochondria become limiting, extra oxygen "
            "makes little difference",
            "It is correct; oxygen alone decides the rate of aerobic respiration, "
            "whatever else happens to be limiting the reaction at the time",
            "It is correct, provided the cell is also kept in complete darkness",
            "It is wrong; oxygen has no effect on the rate of aerobic respiration",
        ],
        "correct_index": 0,
        "why": "Once something other than oxygen becomes the scarcer factor, more oxygen "
               "alone cannot keep raising the rate.",
    },
    {
        "id": "ks4-aerobic-respiration-h16",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A liver cell and a bone cell are compared. Explain why the liver cell "
               "contains far more mitochondria.",
        "options": [
            "A bone cell is simply too small to contain many mitochondria",
            "A liver cell carries out many more energy-demanding reactions",
            "A bone cell respires anaerobically instead of aerobically",
            "A liver cell needs mitochondria to build its structural cells",
        ],
        "correct_index": 1,
        "why": "The liver's constant metabolic workload needs far more ATP than the quieter "
               "chemistry of a bone cell.",
    },
    {
        "id": "ks4-aerobic-respiration-h17",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell has produced approximately 1,110 ATP through aerobic respiration. "
               "Assuming a yield of about 37 ATP per glucose molecule, find how many glucose "
               "molecules this required.",
        "options": [
            "1,110 molecules",
            "41 molecules",
            "30 molecules",
            "37 molecules",
        ],
        "correct_index": 2,
        "why": "1,110 ATP divided by 37 ATP per glucose gives 30 molecules of glucose "
               "respired.",
    },
    {
        "id": "ks4-aerobic-respiration-h18",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant cell, unlike an animal cell, can survive for a time on "
               "the products of its own photosynthesis without absorbing extra glucose.",
        "options": [
            "Plant cells do not carry out aerobic respiration",
            "Photosynthesis and respiration share one organelle",
            "Animal cells can also make their own glucose from carbon dioxide",
            "Photosynthesis supplies the plant cell's own mitochondria with glucose",
        ],
        "correct_index": 3,
        "why": "A plant cell's chloroplasts make glucose that its own mitochondria can then "
               "respire, something an animal cell cannot do.",
    },
    {
        "id": "ks4-aerobic-respiration-h19",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is engineered to have mitochondria with double the normal surface "
               "area of cristae. Predict the likely effect on its maximum rate of ATP "
               "production.",
        "options": [
            "It would rise, since more surface area allows more reactions to occur at "
            "once",
            "It would fall, since larger mitochondria take up too much space",
            "It would be unaffected, since cristae surface area makes no difference, "
            "however much the surface area of its cristae might change",
            "It would fall just if the cell's glucose supply also increased",
        ],
        "correct_index": 0,
        "why": "A larger surface area of cristae allows more of respiration's reactions to "
               "take place at once, raising the maximum ATP output.",
    },
    {
        "id": "ks4-aerobic-respiration-h20",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the usefulness to a cell of aerobic respiration with a process that "
               "released the same total energy as heat alone, with no ATP made.",
        "options": [
            "Both are equally useful, since the total energy released is identical",
            "Aerobic respiration is far more useful, since the energy is captured as "
            "usable ATP",
            "The heat-releasing process is more useful, since heat can also power a cell",
            "Neither process is useful to a cell, since both simply waste the energy",
        ],
        "correct_index": 1,
        "why": "Capturing energy as ATP lets a cell use it for specific jobs, while heat "
               "alone cannot power a cell's processes directly.",
    },
    {
        "id": "ks4-aerobic-respiration-h21",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "During a burst of hard exercise, a heart muscle cell breaks down 50 glucose "
               "molecules through aerobic respiration. Taking the yield as 37 ATP each, work "
               "out the total energy release in ATP.",
        "options": [
            "87 ATP",
            "1,340 ATP",
            "1,850 ATP",
            "37 ATP",
        ],
        "correct_index": 2,
        "why": "50 molecules x 37 ATP each gives approximately 1,850 ATP in total.",
    },
    {
        "id": "ks4-aerobic-respiration-h22",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a cell with plenty of oxygen but almost no glucose "
               "can still respire aerobically at a high rate.",
        "options": [
            "It is correct; oxygen alone sustains a high rate",
            "It is correct, provided the cell also has extra mitochondria",
            "It is wrong; oxygen is toxic to a cell that lacks enough glucose",
            "It is wrong; without enough glucose as fuel, the rate cannot stay high",
        ],
        "correct_index": 3,
        "why": "Oxygen alone cannot sustain a high rate of respiration; glucose is the fuel "
               "being broken down, and a shortage of it limits the rate.",
    },
    {
        "id": "ks4-aerobic-respiration-h23",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why surgeons cool a donor organ before transporting it for a "
               "transplant.",
        "options": [
            "Cooling slows the enzyme-controlled reactions of respiration, preserving the "
            "tissue",
            "Cooling speeds up aerobic respiration, using up the tissue's stored oxygen "
            "and glucose faster",
            "Cooling converts the tissue's stored glucose directly into oxygen",
            "Cooling stops the tissue needing oxygen for the whole journey",
        ],
        "correct_index": 0,
        "why": "Cold slows the tissue's respiration, reducing how quickly it uses up its "
               "limited oxygen and glucose supply before transplant.",
    },
    {
        "id": "ks4-aerobic-respiration-h24",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sprinting athlete's muscle cell generates about 296 ATP from aerobic "
               "respiration. With a yield of roughly 37 ATP per glucose molecule, determine "
               "how many glucose molecules were used.",
        "options": [
            "296 molecules",
            "8 molecules",
            "37 molecules",
            "11 molecules",
        ],
        "correct_index": 1,
        "why": "296 ATP divided by 37 ATP per glucose gives 8 molecules of glucose respired.",
    },
    {
        "id": "ks4-aerobic-respiration-h25",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist compares the mitochondria in a resting muscle cell with those in "
               "the same cell during a race. Predict what changes, and explain.",
        "options": [
            "The number of mitochondria present changes within seconds of starting to run",
            "Nothing changes; mitochondria work at their maximum rate even at rest",
            "The existing mitochondria release ATP faster as demand for it rises",
            "The mitochondria switch entirely to anaerobic respiration during the race",
        ],
        "correct_index": 2,
        "why": "The number of mitochondria stays the same in the short term, but each one "
               "releases ATP faster as the muscle's demand rises.",
    },
    {
        "id": "ks4-aerobic-respiration-h26",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete who has just finished a hard race continues to "
               "breathe heavily, even though their muscles are no longer contracting "
               "forcefully.",
        "options": [
            "Aerobic respiration in the muscles stops completely the instant exercise "
            "ends",
            "Breathing heavily has no connection to the oxygen the muscles now need",
            "A muscle's mitochondria stop needing oxygen once exercise has ended",
            "Recovering muscles still need extra oxygen to restore their normal ATP "
            "reserves and clear waste products",
        ],
        "correct_index": 3,
        "why": "Recovery still demands extra oxygen, both to rebuild spent ATP reserves and "
               "to help clear the waste products of hard exercise.",
    },
]
