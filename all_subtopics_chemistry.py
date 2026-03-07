#!/usr/bin/env python3
"""Chemistry subtopics — all topics"""

CHEMISTRY_COLOR = "#FF6B6B"

CHEMISTRY_SUBTOPICS_ALL = {

"atomic-structure": [
    {
        "id": "chem-atomic-structure",
        "title": "Atomic Structure and the Periodic Table",
        "spec": "4.1.1",
        "summary": "Describe atomic structure, electron shells and the layout of the periodic table.",
        "theory": [
            {"heading": "Inside Every Atom",
             "content": "Every atom has a nucleus containing protons (+) and neutrons (no charge).\nElectrons (−) orbit the nucleus in shells.\nIn a neutral atom: number of protons = number of electrons.\nThe atom is mostly empty space — the nucleus is tiny compared to the whole atom."},
            {"heading": "The Three Subatomic Particles",
             "content": "Proton: relative mass = 1, relative charge = +1, in nucleus.\nNeutron: relative mass = 1, relative charge = 0, in nucleus.\nElectron: relative mass ≈ 0, relative charge = −1, in shells.\nAtomic number (Z) = number of protons.\nMass number (A) = protons + neutrons.\nNeutrons = A − Z."},
            {"heading": "Electronic Structure",
             "content": "Electrons fill shells from inside out.\nShell 1: maximum 2 electrons.\nShell 2: maximum 8 electrons.\nShell 3: maximum 8 electrons (GCSE level).\nExample: Sodium (Z=11) → 2, 8, 1.\nOuter shell electrons determine chemical properties."},
            {"heading": "The Periodic Table",
             "content": "Elements arranged in order of atomic number.\nPeriod (row) = number of electron shells.\nGroup (column) = number of outer shell electrons.\nGroup 1: 1 outer electron — very reactive metals.\nGroup 7: 7 outer electrons — reactive non-metals.\nGroup 0: full outer shell — very unreactive noble gases."}
        ],
        "variables": [],
        "equations": ["Neutrons = mass number − atomic number"],
        "common_mistake": "Mass number = protons + neutrons (not protons + electrons — electrons have negligible mass). Also: Group 0 noble gases have a FULL outer shell, not zero electrons.",
        "key_note": "Period = number of shells. Group = number of outer electrons.",
        "higher": None, "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Element to its Electronic Structure",
            "instruction": "Match each element to its electron arrangement.",
            "pairs": [
                ("Hydrogen (H, Z=1)", "1"),
                ("Carbon (C, Z=6)", "2, 4"),
                ("Oxygen (O, Z=8)", "2, 6"),
                ("Sodium (Na, Z=11)", "2, 8, 1"),
                ("Chlorine (Cl, Z=17)", "2, 8, 7"),
                ("Argon (Ar, Z=18)", "2, 8, 8"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "An element has atomic number 11, mass number 23. How many neutrons does it have?",
             "opts": [("12", True), ("23", False), ("11", False), ("34", False)],
             "wrong_explanations": {1: "That's just the mass number. Neutrons = A − Z = 23 − 11 = 12.", 2: "That's the atomic number (protons). Neutrons = 23 − 11 = 12.", 3: "You added them. Neutrons = mass number − atomic number = 12."}},
            {"q": "Chlorine is in Group 7. How many outer shell electrons does it have?",
             "opts": [("7", True), ("2", False), ("17", False), ("8", False)],
             "wrong_explanations": {1: "2 is electrons in the FIRST shell. Group number = outer shell electrons = 7.", 2: "17 is chlorine's atomic number — the outer shell specifically has 7 electrons.", 3: "8 is a full outer shell (Group 0). Chlorine in Group 7 has 7."}},
            {"q": "An element is in Period 3. How many electron shells does it have?",
             "opts": [("3", True), ("1", False), ("8", False), ("2", False)],
             "wrong_explanations": {1: "Period 1 = 1 shell. Each period adds one shell. Period 3 = 3 shells.", 2: "8 is max electrons in outer shell — not the number of shells.", 3: "Period 2 = 2 shells. Period 3 = 3 shells."}},
            {"q": "What are isotopes?",
             "opts": [("Same element, same proton number, different neutron number", True), ("Same element, same neutron number, different proton number", False), ("Different elements with the same mass number", False), ("Atoms with equal protons and neutrons", False)],
             "wrong_explanations": {1: "Changing the proton number changes the ELEMENT — isotopes are the same element.", 2: "Different elements with the same mass number are called isobars — not isotopes.", 3: "Many atoms have equal protons and neutrons (like carbon-12) but that's not what defines an isotope."}},
            {"q": "In a neutral atom, what is always true?",
             "opts": [("Protons = electrons", True), ("Protons = neutrons", False), ("Electrons = neutrons", False), ("Mass number = atomic number", False)],
             "wrong_explanations": {1: "Protons = neutrons only in certain isotopes (e.g. carbon-12). Not always.", 2: "Electrons = neutrons is a coincidence in some atoms — not a rule.", 3: "Mass number = atomic number only if there are no neutrons — only true for hydrogen-1."}}
        ]
    },
    {
        "id": "periodic-table-groups",
        "title": "Groups in the Periodic Table",
        "spec": "4.1.2",
        "summary": "Describe trends and reactions of Group 1, Group 7 and Group 0 elements.",
        "theory": [
            {"heading": "Group 1 — The Alkali Metals",
             "content": "Li, Na, K, Rb, Cs — all have 1 outer electron.\nReact with water → metal hydroxide + hydrogen gas.\nReactivity INCREASES going down (outer electron further from nucleus, easier to lose).\nSoft metals, low melting points, float on water.\nK catches fire on water. Cs explodes!"},
            {"heading": "Group 7 — The Halogens",
             "content": "F, Cl, Br, I — all have 7 outer electrons, need 1 more for full shell.\nReactivity DECREASES going down (harder to attract an extra electron as atomic radius increases).\nMore reactive halogen displaces less reactive one from solution.\nAppearance: Cl₂ = green gas, Br₂ = brown liquid, I₂ = grey-black solid."},
            {"heading": "Group 0 — Noble Gases",
             "content": "He, Ne, Ar, Kr — full outer shells, extremely unreactive.\nMonatomic (single atoms, not molecules).\nBoiling points increase going down the group.\nUses: He in balloons (non-flammable), Ar in light bulbs (inert), Ne in neon signs."},
            {"heading": "Transition Metals",
             "content": "Central block — Fe, Cu, Ni, Cr etc.\nHigh melting points, hard and dense.\nForm coloured compounds (unlike Group 1).\nCan have variable oxidation states: Fe²⁺ and Fe³⁺, Cu⁺ and Cu²⁺.\nGood catalysts: Fe in Haber process, Pt in catalytic converters."}
        ],
        "variables": [],
        "equations": ["2Na + 2H₂O → 2NaOH + H₂", "Cl₂ + 2KBr → 2KCl + Br₂"],
        "common_mistake": "Group 1 reactivity INCREASES down the group. Group 7 reactivity DECREASES down the group. These are opposite trends and always mixed up in exams!",
        "key_note": "Halogen displacement: more reactive halogen displaces less reactive one. Cl > Br > I in reactivity.",
        "higher": None, "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Group to its Key Properties",
            "instruction": "Match each group to its trend and properties.",
            "pairs": [
                ("Group 1", "Reactivity increases down — react with water to give H₂"),
                ("Group 7", "Reactivity decreases down — displace less reactive halogens"),
                ("Group 0", "Full outer shell — very unreactive, monatomic"),
                ("Transition metals", "Coloured compounds, variable oxidation states, good catalysts"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "Which Group 1 metal reacts most vigorously with water?",
             "opts": [("Caesium (Cs)", True), ("Lithium (Li)", False), ("Sodium (Na)", False), ("They are equally reactive", False)],
             "wrong_explanations": {1: "Li is least reactive — it floats and fizzes gently. Reactivity increases down Group 1.", 2: "Na is more reactive than Li but less than K, Rb and Cs.", 3: "Reactivity clearly increases down the group — Cs is most reactive."}},
            {"q": "Chlorine water is added to potassium iodide solution. What happens?",
             "opts": [("Iodine is displaced — solution turns brown", True), ("Nothing happens", False), ("Chlorine is displaced", False), ("Hydrogen gas is produced", False)],
             "wrong_explanations": {1: "Cl₂ is MORE reactive than I₂ — it would not be displaced.", 2: "A more reactive halogen always displaces a less reactive one from solution.", 3: "Hydrogen comes from metal + acid or Group 1 + water — not halogen displacement."}},
            {"q": "Why are noble gases unreactive?",
             "opts": [("They have a full outer electron shell", True), ("They have no electrons at all", False), ("They are radioactive", False), ("They have too many protons", False)],
             "wrong_explanations": {1: "Noble gases definitely have electrons — helium has 2, neon has 10.", 2: "Noble gases are extremely stable — not radioactive.", 3: "Proton number doesn't determine reactivity — outer shell electrons do."}},
            {"q": "What gas is produced when potassium reacts with water?",
             "opts": [("Hydrogen", True), ("Oxygen", False), ("Carbon dioxide", False), ("Potassium gas", False)],
             "wrong_explanations": {1: "Oxygen would need electrolysis of water to produce.", 2: "CO₂ needs a carbon source — water and potassium contain no carbon.", 3: "Potassium is a solid metal — it doesn't vaporise in this reaction."}},
            {"q": "Which transition metal is used as a catalyst in the Haber process?",
             "opts": [("Iron (Fe)", True), ("Copper (Cu)", False), ("Gold (Au)", False), ("Platinum (Pt)", False)],
             "wrong_explanations": {1: "Copper is used in the Contact process for SO₃ production, not Haber.", 2: "Gold is too expensive and not particularly catalytic for this reaction.", 3: "Platinum is used in catalytic converters in cars — not the Haber process."}}
        ]
    },
],

"bonding": [
    {
        "id": "ionic-bonding",
        "title": "Ionic Bonding and Ionic Compounds",
        "spec": "4.2.1",
        "summary": "Explain ionic bonding and describe the properties of ionic compounds.",
        "theory": [
            {"heading": "What is Ionic Bonding?",
             "content": "Ionic bonding happens between a metal and a non-metal.\nThe metal LOSES electrons → positive ion (cation).\nThe non-metal GAINS electrons → negative ion (anion).\nOpposite charges attract → strong electrostatic force = the ionic bond.\nBoth ions achieve a full outer electron shell."},
            {"heading": "The Giant Ionic Lattice",
             "content": "Ions arrange in a regular 3D structure: the giant ionic lattice.\nEach positive ion surrounded by negative ions and vice versa.\nThousands of ions in a repeating pattern.\nExample: NaCl — each Na⁺ surrounded by 6 Cl⁻ ions."},
            {"heading": "Properties of Ionic Compounds",
             "content": "High melting/boiling points — strong electrostatic forces need lots of energy to break.\nConduct electricity when MOLTEN or DISSOLVED — ions free to move.\nDo NOT conduct when SOLID — ions locked in lattice.\nBrittle — layers shift under stress, like charges align and repel → shatters.\nMany are soluble in water."},
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "Ionic compounds conduct electricity ONLY when molten or dissolved in water — NOT as solids. In solids, ions are fixed in the lattice. This is the number one exam mistake on ionic bonding.",
        "key_note": None, "higher": "Dot-and-cross diagrams show electron transfer. Draw each ion in brackets with charge outside.", "triple_only": None, "rp": None, "matching": None,
        "fifas": [],
        "quiz": [
            {"q": "When can an ionic compound conduct electricity?",
             "opts": [("When molten or dissolved in water", True), ("When solid", False), ("Never", False), ("Always, in any state", False)],
             "wrong_explanations": {1: "Solid ionic compounds CANNOT conduct — ions are fixed.", 2: "Ionic compounds definitely CAN conduct — when ions are free to move.", 3: "They conduct when liquid or dissolved — just not solid."}},
            {"q": "Why do ionic compounds have high melting points?",
             "opts": [("Strong electrostatic forces between oppositely charged ions require lots of energy to break", True), ("They are made of metals", False), ("They are large molecules", False), ("They contain covalent bonds", False)],
             "wrong_explanations": {1: "Not all metals have high melting points — Group 1 metals actually melt quite easily.", 2: "Ionic compounds are NOT molecules — they are giant lattice structures.", 3: "Ionic compounds have ionic bonds — not covalent bonds."}},
            {"q": "Sodium (2,8,1) reacts with chlorine (2,8,7). What ions form?",
             "opts": [("Na⁺ and Cl⁻", True), ("Na⁻ and Cl⁺", False), ("Na²⁺ and Cl²⁻", False), ("No ions — they share electrons", False)],
             "wrong_explanations": {1: "Metals LOSE electrons to become positive. Na losing an electron would become negative — backwards!", 2: "Sodium needs to lose 1 electron (giving Na⁺) and chlorine gains 1 (giving Cl⁻).", 3: "Sharing electrons = covalent bonding. Metal + non-metal = ionic (transfer of electrons)."}},
            {"q": "Why is sodium chloride brittle?",
             "opts": [("Layers shift and like charges align, causing repulsion and shattering", True), ("The bonds are weak", False), ("It contains no covalent bonds", False), ("Ions are too small", False)],
             "wrong_explanations": {1: "Ionic bonds are VERY strong — high melting point proves this. Brittleness is about what happens when layers shift.", 2: "The absence of covalent bonds doesn't explain brittleness.", 3: "Ion size isn't the reason — it's the layer-shift mechanism."}},
            {"q": "What type of structure do ionic compounds form?",
             "opts": [("Giant ionic lattice", True), ("Simple molecular", False), ("Giant covalent", False), ("Metallic", False)],
             "wrong_explanations": {1: "Simple molecular = small discrete molecules like H₂O, CO₂. Not ionic.", 2: "Giant covalent = diamond, graphite, SiO₂. Made of covalent bonds.", 3: "Metallic = pure metals. Ionic is a different structure entirely."}}
        ]
    },
    {
        "id": "covalent-bonding",
        "title": "Covalent Bonding and Structures",
        "spec": "4.2.2",
        "summary": "Explain covalent bonding and compare simple molecular and giant covalent structures.",
        "theory": [
            {"heading": "What is Covalent Bonding?",
             "content": "Covalent bonding occurs between non-metal atoms.\nAtoms SHARE pairs of electrons to achieve full outer shells.\nEach shared pair = one covalent bond.\nDouble bond = 2 shared pairs (e.g. O=O, C=O in CO₂).\nCovalent bonds within molecules are very strong."},
            {"heading": "Simple Molecular Substances",
             "content": "Small molecules: H₂, O₂, H₂O, CO₂, CH₄, NH₃, Cl₂.\nStrong covalent bonds WITHIN molecules.\nWeak intermolecular forces BETWEEN molecules.\nLow melting/boiling points — weak between-molecule forces easy to overcome.\nDo NOT conduct electricity — no free ions or electrons."},
            {"heading": "Giant Covalent Structures",
             "content": "Diamond: each C bonded to 4 others → 3D network → extremely hard, very high mp, doesn't conduct.\nGraphite: each C bonded to 3 others in flat layers → slippery, DOES conduct (delocalised electrons between layers).\nSilicon dioxide (SiO₂, sand): giant structure, very high mp, doesn't conduct."},
            {"heading": "Metallic Bonding",
             "content": "Metal atoms lose outer electrons → positive ions in a sea of delocalised electrons.\nThe electrostatic attraction between ions and electrons = metallic bond.\nProperties: conducts electricity (free electrons), malleable (layers slide), high melting points (strong bonds), shiny.\nAlloys: mixing metals distorts the lattice → harder, stronger than pure metals."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "NOT all covalent substances have low melting points! Simple molecular compounds do — but giant covalent structures (diamond, SiO₂) have VERY high melting points. The key question is always: simple molecular or giant covalent?",
        "key_note": "Graphite conducts electricity — it has delocalised electrons between layers. Diamond does not conduct — no free electrons.",
        "higher": "Intermolecular forces increase with molecular size → larger molecules have higher boiling points (e.g. pentane boils higher than methane).",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Structure to its Properties",
            "instruction": "Match each structure type to its key properties.",
            "pairs": [
                ("Simple molecular", "Low mp, doesn't conduct, weak forces between molecules"),
                ("Giant ionic lattice", "High mp, conducts when molten/dissolved, brittle"),
                ("Giant covalent (diamond)", "Very high mp, extremely hard, doesn't conduct"),
                ("Giant covalent (graphite)", "High mp, conducts electricity, soft and slippery"),
                ("Metallic", "Conducts always, malleable, high mp"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "Why do simple molecular substances have low melting points?",
             "opts": [("Weak intermolecular forces between molecules require little energy to overcome", True), ("Covalent bonds within the molecules are weak", False), ("They have no electrons", False), ("They are ionic", False)],
             "wrong_explanations": {1: "Covalent bonds WITHIN molecules are strong — it's the BETWEEN-molecule forces that are weak.", 2: "All molecules have electrons — the key is intermolecular force strength.", 3: "If they were ionic they'd have high melting points."}},
            {"q": "Why does graphite conduct electricity but diamond doesn't?",
             "opts": [("Graphite has delocalised electrons between layers; diamond has no free electrons", True), ("Diamond is denser", False), ("Graphite has ionic bonds", False), ("Diamond is a larger structure", False)],
             "wrong_explanations": {1: "Density doesn't determine conductivity — it's the presence of free charge carriers.", 2: "Graphite is pure carbon — all covalent bonds, no ionic bonds.", 3: "Both are giant covalent structures. The difference is delocalised electrons in graphite."}},
            {"q": "What is an alloy?",
             "opts": [("A mixture of metals (or metal + non-metal) that is harder than pure metals", True), ("A pure metal with no impurities", False), ("A type of ionic compound", False), ("A metal that has been electrolysed", False)],
             "wrong_explanations": {1: "Pure metals with no impurities are weaker — regular layers slide easily. Alloys disrupt this.", 2: "Alloys are MIXTURES not pure substances — they contain two or more elements.", 3: "Electrolysis is used to extract or plate metals — not related to what an alloy is."}},
            {"q": "Which property do all metals share due to metallic bonding?",
             "opts": [("Good electrical conductors", True), ("Low melting points", False), ("Brittle", False), ("Transparent", False)],
             "wrong_explanations": {1: "Most metals have HIGH melting points — Group 1 metals (Na, K) are exceptions but most metals melt at high temps.", 2: "Metals are MALLEABLE (they bend and deform) — the opposite of brittle.", 3: "Metals are opaque and shiny — transparency is a property of some ionic and covalent substances."}},
            {"q": "Silicon dioxide (sand) has a very high melting point. Why?",
             "opts": [("It has a giant covalent structure — many strong covalent bonds to break", True), ("It is an ionic compound", False), ("It is a metal", False), ("It has strong intermolecular forces", False)],
             "wrong_explanations": {1: "SiO₂ is not ionic — it's a giant covalent structure with Si-O covalent bonds throughout.", 2: "Silicon and oxygen are both non-metals — they form covalent bonds, not ionic.", 3: "Intermolecular forces are for SIMPLE molecular substances. SiO₂ is giant covalent — it has covalent bonds throughout."}}
        ]
    },
],

"quantitative": [
    {
        "id": "moles-calculations",
        "title": "Moles, Mass and Relative Formula Mass",
        "spec": "4.3.1",
        "summary": "Calculate moles, mass and Mr, and use balanced equations for reacting quantities.",
        "theory": [
            {"heading": "Relative Formula Mass (Mr)",
             "content": "Mr = sum of all relative atomic masses (Ar) in the formula.\nH₂O: (2×1) + 16 = 18.\nCO₂: 12 + (2×16) = 44.\nNaCl: 23 + 35.5 = 58.5.\nMr has NO UNITS — it's a ratio."},
            {"heading": "The Mole",
             "content": "One mole = 6.02 × 10²³ particles (Avogadro's number).\n1 mole of any element weighs its Ar in grams.\n1 mole of any compound weighs its Mr in grams.\nFormula: moles = mass ÷ Mr."},
            {"heading": "Using Moles in Reactions",
             "content": "A balanced equation tells you the mole ratio of reactants and products.\nExample: 2H₂ + O₂ → 2H₂O means 2 mol H₂ reacts with 1 mol O₂ to give 2 mol H₂O.\nScale up or down using the ratio.\nHigher: limiting reactant = the one that runs out first and determines yield."},
            {"heading": "Conservation of Mass",
             "content": "Total mass of reactants = total mass of products.\nIf mass appears to decrease: a gas was produced and escaped.\nIf mass appears to increase: a gas from the atmosphere was absorbed (e.g. burning magnesium takes O₂ from air).\nAlways account for all products, including gases."}
        ],
        "variables": [
            ("n", "Amount of substance", "Moles", "mol"),
            ("m", "Mass", "Grams", "g"),
            ("Mr", "Relative formula mass", "no unit", ""),
        ],
        "equations": ["n = m ÷ Mr"],
        "common_mistake": "Mr has NO UNITS. Mass must be in GRAMS before using n = m ÷ Mr. If given in kg, convert first (×1000).",
        "key_note": "1 mole of any substance weighs Mr grams and contains 6.02 × 10²³ particles.",
        "higher": "Moles of gas at RTP: n = volume (dm³) ÷ 24. One mole of any gas = 24 dm³ at room temperature and pressure.",
        "triple_only": None, "rp": None, "matching": None,
        "fifas": [
            {"label": "Example 1 — Calculate moles",
             "question": "Calculate the moles in 44 g of CO₂. (C=12, O=16)",
             "steps": [("F","n = m ÷ Mr"), ("I","Mr(CO₂) = 12 + 32 = 44. n = 44 ÷ 44"), ("F","Mass already in grams"), ("A","n = 1 mol")]},
            {"label": "Example 2 — Calculate mass",
             "question": "What mass of NaCl (Mr=58.5) is in 0.5 mol?",
             "steps": [("F","m = n × Mr"), ("I","m = 0.5 × 58.5"), ("F","No conversion needed"), ("A","m = 29.25 g")]}
        ],
        "quiz": [
            {"q": "What is the Mr of H₂SO₄? (H=1, S=32, O=16)",
             "opts": [("98", True), ("66", False), ("50", False), ("81", False)],
             "wrong_explanations": {1: "Count carefully: 2H + S + 4O = 2 + 32 + 64 = 98. You may have used only 3 oxygens.", 2: "Mr = 2+32+64 = 98. You might have halved somewhere.", 3: "There are 4 oxygens in H₂SO₄. Mr = 2+32+(4×16) = 98."}},
            {"q": "How many moles are in 36 g of water? (Mr=18)",
             "opts": [("2 mol", True), ("18 mol", False), ("0.5 mol", False), ("36 mol", False)],
             "wrong_explanations": {1: "You used mass as moles directly. n = m ÷ Mr = 36 ÷ 18 = 2 mol.", 2: "You divided Mr by mass. n = m ÷ Mr = 36 ÷ 18 = 2 mol.", 3: "You used just the mass. n = 36 ÷ 18 = 2 mol."}},
            {"q": "What mass of CaCO₃ (Mr=100) contains 0.25 mol?",
             "opts": [("25 g", True), ("400 g", False), ("100 g", False), ("2.5 g", False)],
             "wrong_explanations": {1: "You divided Mr by mol. m = n × Mr = 0.25 × 100 = 25 g.", 2: "You used Mr alone without multiplying by 0.25. m = n × Mr = 0.25 × 100 = 25 g.", 3: "You divided by 10 instead of multiplying. m = 0.25 × 100 = 25 g."}},
            {"q": "A reaction produces 8 g of solid but the mass of the container decreased by 2 g. Why?",
             "opts": [("A gas was produced and escaped from the container", True), ("Energy was lost as heat", False), ("Mass was destroyed", False), ("The reactants were impure", False)],
             "wrong_explanations": {1: "Energy loss doesn't affect mass readings on a balance.", 2: "Mass is always conserved — it doesn't get destroyed.", 3: "Impurities might give a slightly different product mass but don't explain mass decrease."}},
            {"q": "What does conservation of mass mean in chemistry?",
             "opts": [("Total mass of reactants = total mass of products", True), ("Number of molecules stays the same", False), ("Number of atoms of each element stays the same", False), ("No energy is released", False)],
             "wrong_explanations": {1: "Molecule count can change — 2H₂ + O₂ → 2H₂O goes from 3 molecules to 2. Mass is what's conserved.", 2: "Conservation of mass is specifically about MASS — but the underlying reason is that atoms are rearranged, not created or destroyed.", 3: "Reactions always involve energy changes — conservation of mass and energy are separate."}}
        ]
    },
    {
        "id": "yield-atom-economy",
        "title": "Percentage Yield and Atom Economy",
        "spec": "4.3.3",
        "summary": "Calculate percentage yield and atom economy and explain their importance.",
        "theory": [
            {"heading": "Percentage Yield",
             "content": "Theoretical yield = maximum mass you should get from the balanced equation.\nActual yield = what you actually collect in the lab.\nYield is always less than 100% — some is always lost.\nReasons: reversible reactions, product lost in filtering/transferring, impurities, side reactions."},
            {"heading": "Atom Economy",
             "content": "Atom economy = what fraction of reactant atoms end up in the DESIRED product.\nCalculated from the balanced equation using Mr values — not actual masses.\n100% atom economy = no waste at all (all atoms go into useful product).\nIndustry prefers high atom economy → less waste, lower cost, more sustainable."},
            {"heading": "Green Chemistry",
             "content": "Green chemistry aims to make reactions more sustainable.\nHigh atom economy, renewable feedstocks, catalysts (lower energy), room temp reactions.\nHaber process has 100% atom economy (N₂ + 3H₂ → 2NH₃ — only one product).\nBut only ~15% yield per pass — recycled gases improve overall efficiency."}
        ],
        "variables": [],
        "equations": [
            "% yield = (actual yield ÷ theoretical yield) × 100",
            "Atom economy = (Mr of desired product ÷ sum of Mr of ALL products) × 100"
        ],
        "common_mistake": "Atom economy uses Mr from the EQUATION — not actual experimental masses. Percentage yield uses ACTUAL masses from the experiment. These are two completely different calculations.",
        "key_note": None, "higher": "Limiting reactant: calculate moles of each reactant and use ratio from equation to find which runs out first.", "triple_only": None, "rp": None, "matching": None,
        "fifas": [
            {"label": "Example — Percentage yield",
             "question": "Theoretical yield = 80 g. Actual yield collected = 60 g. Calculate percentage yield.",
             "steps": [("F","% yield = (actual ÷ theoretical) × 100"), ("I","% yield = (60 ÷ 80) × 100"), ("F","No conversion needed"), ("A","% yield = 75%")]}
        ],
        "quiz": [
            {"q": "Theoretical yield = 50 g, actual = 40 g. What is the % yield?",
             "opts": [("80%", True), ("125%", False), ("10%", False), ("40%", False)],
             "wrong_explanations": {1: "You divided theoretical by actual. Always: (actual ÷ theoretical) × 100 = (40÷50) × 100 = 80%.", 2: "You subtracted instead of dividing. % yield = (40÷50) × 100 = 80%.", 3: "You used actual yield as the answer. % yield = (actual ÷ theoretical) × 100 = 80%."}},
            {"q": "A reaction has 100% atom economy. What does this mean?",
             "opts": [("All reactant atoms end up in the desired product — no waste", True), ("All the product is collected (100% yield)", False), ("The reaction is very fast", False), ("No energy is needed", False)],
             "wrong_explanations": {1: "100% yield means all product is collected — separate from atom economy.", 2: "Atom economy is about waste products in the EQUATION — not about how much product you collect.", 3: "Atom economy says nothing about energy requirements."}},
            {"q": "Which formula is used to calculate atom economy?",
             "opts": [("(Mr of desired product ÷ sum of Mr of all products) × 100", True), ("(actual yield ÷ theoretical yield) × 100", False), ("(mass of product ÷ mass of reactant) × 100", False), ("(moles of product ÷ moles of reactant) × 100", False)],
             "wrong_explanations": {1: "That's % yield — not atom economy. Atom economy uses Mr values from the balanced equation.", 2: "That uses actual experimental masses — atom economy uses Mr values from the equation only.", 3: "Atom economy uses Mr values, not moles directly."}},
            {"q": "Why is a high atom economy desirable?",
             "opts": [("Less waste, lower costs, more sustainable", True), ("The reaction goes faster", False), ("It guarantees 100% yield", False), ("It reduces activation energy", False)],
             "wrong_explanations": {1: "Atom economy says nothing about reaction rate.", 2: "High atom economy and high yield are independent — a reaction can have 100% atom economy but only 20% yield.", 3: "Activation energy is affected by catalysts — not by atom economy."}}
        ]
    },
],

"chemical-changes": [
    {
        "id": "acids-reactions",
        "title": "Acids, Bases and Making Salts",
        "spec": "4.4.1",
        "summary": "Describe reactions of acids and explain how to make pure salts.",
        "theory": [
            {"heading": "The pH Scale",
             "content": "pH 0–6: acidic. pH 7: neutral. pH 8–14: alkaline.\nAcids produce H⁺ ions in solution.\nAlkalis produce OH⁻ ions in solution.\nNeutralisation: H⁺ + OH⁻ → H₂O.\nStrong acids fully dissociate (HCl, H₂SO₄, HNO₃).\nWeak acids partially dissociate (ethanoic acid, citric acid)."},
            {"heading": "Reactions of Acids",
             "content": "Acid + metal → salt + hydrogen.\nAcid + metal oxide/hydroxide (base) → salt + water.\nAcid + carbonate → salt + water + carbon dioxide.\nAcid + alkali → salt + water (neutralisation).\nTest H₂: burning splint → squeaky pop.\nTest CO₂: limewater → turns cloudy."},
            {"heading": "Naming Salts",
             "content": "Hydrochloric acid → chloride salts (e.g. NaCl = sodium chloride).\nSulfuric acid → sulfate salts (e.g. CuSO₄ = copper sulfate).\nNitric acid → nitrate salts (e.g. KNO₃ = potassium nitrate).\nSalt name = metal name + acid-derived name."},
            {"heading": "Making Pure Salt Crystals",
             "content": "Add excess solid (metal/carbonate/oxide) to acid — ensures all acid reacts.\nFilter off excess solid.\nEvaporate water gently → salt crystals form.\nDry the crystals.\nFor soluble salts: titration method — accurate volumes, no excess.\nFor insoluble salts: mix two soluble solutions → precipitate forms → filter and dry."}
        ],
        "variables": [],
        "equations": [
            "Acid + metal → salt + H₂",
            "Acid + base → salt + H₂O",
            "Acid + carbonate → salt + H₂O + CO₂",
            "H⁺ + OH⁻ → H₂O"
        ],
        "common_mistake": "Acid + metal oxide gives salt + WATER (not hydrogen!). Hydrogen only comes from acid + reactive metal. Students confuse products all the time — learn each reaction type separately.",
        "key_note": "Squeaky pop = H₂. Limewater cloudy = CO₂. Damp blue litmus turns red = acidic gas.",
        "higher": "pH = −log[H⁺]. pH change of 1 unit = ×10 change in H⁺ concentration.",
        "triple_only": None, "rp": "RP1 — Prepare a pure dry sample of a soluble salt (e.g. copper sulfate from copper oxide and sulfuric acid).",
        "matching": {
            "title": "Match the Acid Reaction to its Products",
            "instruction": "Match each reaction type to the correct products.",
            "pairs": [
                ("Acid + metal", "Salt + hydrogen gas"),
                ("Acid + metal oxide", "Salt + water"),
                ("Acid + carbonate", "Salt + water + carbon dioxide"),
                ("Acid + alkali", "Salt + water (neutralisation)"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "What gas is produced when zinc reacts with hydrochloric acid?",
             "opts": [("Hydrogen", True), ("Carbon dioxide", False), ("Oxygen", False), ("Chlorine", False)],
             "wrong_explanations": {1: "CO₂ comes from acid + CARBONATE reactions — not acid + metal.", 2: "Oxygen comes from electrolysis or decomposition of water — not this reaction.", 3: "Chlorine would require oxidation of Cl⁻ ions — not a simple acid + metal reaction."}},
            {"q": "What products form when sulfuric acid reacts with copper oxide?",
             "opts": [("Copper sulfate + water", True), ("Copper sulfate + hydrogen", False), ("Copper chloride + water", False), ("Copper + sulfur dioxide", False)],
             "wrong_explanations": {1: "Hydrogen comes from acid + METAL — copper oxide is a base/metal oxide, not a metal.", 2: "The acid here is SULFuric — it gives sulfate salts. Chloride would come from hydrochloric acid.", 3: "Copper oxide is the reactant — the copper becomes part of the salt product, not released as metal."}},
            {"q": "Marble chips (CaCO₃) react with HCl. What gas is produced?",
             "opts": [("Carbon dioxide", True), ("Hydrogen", False), ("Oxygen", False), ("Chlorine", False)],
             "wrong_explanations": {1: "Hydrogen comes from acid + METAL. CaCO₃ is a carbonate → CO₂ is produced.", 2: "No oxygen source in this reaction — oxygen needs electrolysis or decomposition.", 3: "Chlorine from this reaction would need the Cl⁻ to be oxidised — doesn't happen here."}},
            {"q": "What is the test for hydrogen gas?",
             "opts": [("Burning splint — squeaky pop", True), ("Glowing splint — relights", False), ("Limewater — turns cloudy", False), ("Damp litmus — bleaches", False)],
             "wrong_explanations": {1: "Glowing splint relights = OXYGEN test.", 2: "Limewater turning cloudy = CO₂ test.", 3: "Damp litmus bleaching = CHLORINE test."}},
            {"q": "What is the difference between a strong and weak acid at the same concentration?",
             "opts": [("Strong acid fully dissociates — more H⁺ ions, lower pH", True), ("Strong acid has more molecules", False), ("Weak acid has more H atoms per molecule", False), ("They are identical at the same concentration", False)],
             "wrong_explanations": {1: "Concentration = how much acid is present. Strength = how much dissociates. Different concentrations can have same pH if one is strong and one weak.", 2: "H atom count per molecule doesn't determine strength. HCl has 1 H, H₂SO₄ has 2, but both are strong acids.", 3: "They are definitely different — strong acid has lower pH at same concentration because more H⁺ ions."}}
        ]
    },
    {
        "id": "electrolysis",
        "title": "Electrolysis",
        "spec": "4.4.3",
        "summary": "Explain electrolysis and predict products at each electrode.",
        "theory": [
            {"heading": "What is Electrolysis?",
             "content": "Electrical energy decomposes an ionic compound.\nNeeds: electrolyte (free-moving ions) + electrodes + power supply.\nCathode (−): attracts positive ions → reduction (gain of electrons).\nAnode (+): attracts negative ions → oxidation (loss of electrons).\nOil Rig: Oxidation Is Loss, Reduction Is Gain."},
            {"heading": "Molten Compounds",
             "content": "Simple rule: positive metal ion → cathode → reduced to metal element.\nNegative non-metal ion → anode → oxidised to element.\nExample: molten PbBr₂:\nCathode: Pb²⁺ + 2e⁻ → Pb (lead metal deposited).\nAnode: 2Br⁻ → Br₂ + 2e⁻ (bromine gas)."},
            {"heading": "Aqueous Solutions",
             "content": "Water provides H⁺ and OH⁻ ions that compete with the dissolved ions.\nCathode: H₂ produced if metal is more reactive than hydrogen (H⁺ discharged instead of metal ion).\nAnode: O₂ produced if no halide present (OH⁻ discharged). Halogen gas produced if halide present.\nExample: brine (NaCl aq): cathode → H₂, anode → Cl₂, remaining solution → NaOH."},
            {"heading": "Electroplating and Industrial Uses",
             "content": "Electroplating: coat object in thin metal layer (protection/appearance).\nObject = cathode. Plating metal = anode. Solution = salt of plating metal.\nExtract reactive metals (Al from molten aluminium oxide).\nPurify copper: impure Cu anode dissolves, pure Cu deposits at cathode."}
        ],
        "variables": [],
        "equations": [
            "Cathode: positive ions + electrons → reduced to element",
            "Anode: negative ions − electrons → oxidised to element"
        ],
        "common_mistake": "Anode is POSITIVE and attracts NEGATIVE ions. Cathode is NEGATIVE and attracts POSITIVE ions. Students often mix these up — remember: CAThode = CATions (positive ions go there).",
        "key_note": "Oil Rig: Oxidation Is Loss (of electrons), Reduction Is Gain (of electrons). Anode = oxidation. Cathode = reduction.",
        "higher": "Half equations: Cu²⁺ + 2e⁻ → Cu (cathode). 2Cl⁻ → Cl₂ + 2e⁻ (anode).",
        "triple_only": None, "rp": "RP2 — Electrolysis of copper sulfate solution: observe copper depositing at cathode.",
        "matching": {
            "title": "Match the Electrode to What Happens",
            "instruction": "Match each scenario to the correct electrode product.",
            "pairs": [
                ("Cathode — molten PbBr₂", "Lead metal deposited"),
                ("Anode — molten PbBr₂", "Bromine gas produced"),
                ("Cathode — brine (NaCl aq)", "Hydrogen gas produced"),
                ("Anode — brine (NaCl aq)", "Chlorine gas produced"),
                ("Cathode — CuSO₄ aq", "Copper deposited"),
                ("Anode — CuSO₄ aq", "Oxygen gas produced"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "At which electrode does reduction occur?",
             "opts": [("Cathode (−)", True), ("Anode (+)", False), ("Both", False), ("Neither", False)],
             "wrong_explanations": {1: "Anode = OXIDATION (anions lose electrons). Cathode = REDUCTION (cations gain electrons).", 2: "Each electrode has a different process — not both.", 3: "Reduction definitely happens — at the cathode."}},
            {"q": "Lead bromide is electrolysed when molten. What forms at the anode?",
             "opts": [("Bromine gas", True), ("Lead metal", False), ("Oxygen gas", False), ("Lead bromide gas", False)],
             "wrong_explanations": {1: "Lead deposits at the CATHODE — Pb²⁺ ions go to the negative electrode.", 2: "Oxygen would form from OH⁻ in water — molten PbBr₂ has no water.", 3: "Lead bromide is the electrolyte — it doesn't reform as a gas."}},
            {"q": "Brine (sodium chloride solution) is electrolysed. What is produced at the cathode?",
             "opts": [("Hydrogen gas", True), ("Chlorine gas", False), ("Sodium metal", False), ("Oxygen gas", False)],
             "wrong_explanations": {1: "Chlorine is produced at the ANODE (Cl⁻ ions → Cl₂ + e⁻).", 2: "In aqueous solution, H⁺ from water is discharged instead of Na⁺ (sodium is too reactive).", 3: "Oxygen comes from OH⁻ ions — but in brine, Cl⁻ is preferentially discharged at the anode."}},
            {"q": "What does Oil Rig stand for?",
             "opts": [("Oxidation Is Loss of electrons, Reduction Is Gain of electrons", True), ("Oxidation Is Large, Reduction Is Gentle", False), ("Only In Lab, Reactions Improve Growth", False), ("It's just a made-up memory trick with no meaning", False)],
             "wrong_explanations": {1: "These don't match the actual electrochemistry.", 2: "Definitely not! Oil Rig is a real memory aid: Oxidation Is Loss, Reduction Is Gain — of electrons.", 3: "Oil Rig is a genuine scientific memory aid used worldwide for remembering electron transfer."}},
            {"q": "What is electroplating used for?",
             "opts": [("Depositing a thin metal layer onto an object for protection or appearance", True), ("Extracting metals from their ores", False), ("Purifying water", False), ("Measuring pH", False)],
             "wrong_explanations": {1: "Extracting metals uses electrolysis of MOLTEN ores — electroplating is about coating an existing object.", 2: "Water purification uses filtration, chlorination etc — not electroplating.", 3: "pH meters use electrical sensors — completely unrelated to electroplating."}}
        ]
    },
],

"rates-equilibrium": [
    {
        "id": "rate-collision-theory",
        "title": "Rate of Reaction and Collision Theory",
        "spec": "4.6.1",
        "summary": "Explain rate of reaction using collision theory and identify factors affecting it.",
        "theory": [
            {"heading": "Rate of Reaction",
             "content": "Rate = how quickly reactants become products.\nMeasured as: amount of product formed per unit time, or amount of reactant used per unit time.\nFaster rate = steeper graph at the start.\nRate = quantity ÷ time (e.g. g/s, cm³/s)."},
            {"heading": "Collision Theory",
             "content": "Reactions happen when particles collide with SUFFICIENT ENERGY.\nActivation energy = minimum energy needed for a successful collision.\nMore frequent collisions + more energetic collisions = faster rate.\nAny factor increasing collision frequency or energy speeds up the reaction."},
            {"heading": "Factors Affecting Rate",
             "content": "Temperature ↑ → particles move faster → more collisions AND more exceed activation energy → big rate increase.\nConcentration ↑ → more particles per volume → more frequent collisions → faster rate.\nSurface area ↑ → more exposed reactant surface → more contact → faster rate.\nCatalyst → lowers activation energy → more particles can react → faster rate."},
            {"heading": "Catalysts",
             "content": "Speed up reactions without being consumed.\nProvide an alternative pathway with lower activation energy.\nEnzymes = biological catalysts (proteins).\nIndustrial: iron (Haber), platinum (catalytic converter), vanadium pentoxide (Contact process).\nCatalysts allow lower operating temperatures → saves energy → cheaper."}
        ],
        "variables": [],
        "equations": ["Rate = quantity ÷ time"],
        "common_mistake": "A catalyst is NOT used up — it's unchanged at the end. Also, temperature affects rate much MORE dramatically than concentration because it affects BOTH collision frequency AND the proportion of particles above activation energy.",
        "key_note": None,
        "higher": "Maxwell-Boltzmann distribution: at higher temperatures, more particles exceed activation energy. Catalyst lowers the activation energy line — same distribution, more particles qualify.",
        "triple_only": None,
        "rp": ["RP4 — sodium thiosulfate + HCl: measure time for solution to turn cloudy (X disappears)", "RP5 — marble chips + HCl: measure mass loss over time"],
        "matching": {
            "title": "Match the Factor to its Effect on Rate",
            "instruction": "Match each factor to how it increases the rate of reaction.",
            "pairs": [
                ("Temperature increase", "Particles move faster — more and higher-energy collisions"),
                ("Concentration increase", "More particles per unit volume — more frequent collisions"),
                ("Surface area increase", "More reactant exposed — more collisions possible"),
                ("Catalyst added", "Lowers activation energy — more particles have enough energy"),
            ]
        },
        "fifas": [
            {"label": "Example — Rate calculation",
             "question": "24 cm³ of gas is produced in 40 seconds. Calculate the average rate.",
             "steps": [("F","Rate = quantity ÷ time"), ("I","Rate = 24 ÷ 40"), ("F","No unit conversion needed"), ("A","Rate = 0.6 cm³/s")]}
        ],
        "quiz": [
            {"q": "What is activation energy?",
             "opts": [("Minimum energy needed for a collision to cause a reaction", True), ("Total energy released in the reaction", False), ("Energy stored in chemical bonds", False), ("Energy of the catalyst", False)],
             "wrong_explanations": {1: "Total energy released = enthalpy change (ΔH) — not activation energy.", 2: "Bond energy is energy to break bonds — activation energy is the reaction energy barrier.", 3: "Catalysts don't store energy — they lower the activation energy."}},
            {"q": "How does increasing temperature increase rate?",
             "opts": [("Particles move faster — more frequent and more energetic collisions", True), ("It adds more reactant particles", False), ("It melts the reactants", False), ("It raises the activation energy", False)],
             "wrong_explanations": {1: "Temperature doesn't add particles — it gives energy to existing ones.", 2: "Melting only applies to solids. The mechanism is increased particle speed.", 3: "Catalysts LOWER activation energy — temperature doesn't change it."}},
            {"q": "Marble chips are replaced with marble powder (same mass). What happens to the rate?",
             "opts": [("Rate increases — more surface area exposed to acid", True), ("Rate decreases — smaller pieces have less mass", False), ("Rate stays the same — same number of moles", False), ("Rate increases — powder dissolves better", False)],
             "wrong_explanations": {1: "Same mass = same moles. Rate is affected by SURFACE AREA, not by mass alone.", 2: "Same moles means same total amount — but surface area is much greater for powder, giving faster collisions.", 3: "CaCO₃ doesn't dissolve — it reacts. Surface area determines how quickly acid can reach the solid."}},
            {"q": "What is the correct definition of rate of reaction?",
             "opts": [("The change in quantity of reactant or product per unit time", True), ("The total energy released", False), ("The temperature change during reaction", False), ("The time taken for the reaction to complete", False)],
             "wrong_explanations": {1: "Total energy released = enthalpy change — not rate.", 2: "Temperature change is measured in calorimetry — it's related to energy, not rate.", 3: "Time to complete is inversely related to rate — but rate itself is change per unit time, not total time."}},
            {"q": "20 cm³ of gas produced in 50 s. What is the rate?",
             "opts": [("0.4 cm³/s", True), ("1000 cm³/s", False), ("30 cm³/s", False), ("0.0025 cm³/s", False)],
             "wrong_explanations": {1: "You multiplied: 20 × 50 = 1000. Rate = quantity ÷ time = 20 ÷ 50 = 0.4 cm³/s.", 2: "You added quantity and time. Rate = 20 ÷ 50 = 0.4 cm³/s.", 3: "You divided time by quantity. Rate = quantity ÷ time = 20 ÷ 50 = 0.4 cm³/s."}}
        ]
    },
    {
        "id": "equilibrium-le-chatelier",
        "title": "Equilibrium and Le Chatelier's Principle",
        "spec": "4.6.2",
        "summary": "Describe dynamic equilibrium and apply Le Chatelier's principle to predict shifts.",
        "theory": [
            {"heading": "Reversible Reactions",
             "content": "A reversible reaction can go both forward and backward: A + B ⇌ C + D.\nIn a closed system, both directions happen simultaneously.\nAt equilibrium: rate forward = rate reverse → concentrations stay constant.\nEquilibrium is dynamic — reactions are still happening, just at equal rates."},
            {"heading": "Le Chatelier's Principle",
             "content": "If conditions change, equilibrium shifts to OPPOSE the change.\nIncrease reactant concentration → shifts right (makes more product).\nIncrease temperature → shifts in the ENDOTHERMIC direction.\nIncrease pressure (gases) → shifts to FEWER moles of gas side."},
            {"heading": "The Haber Process",
             "content": "N₂ + 3H₂ ⇌ 2NH₃  (forward reaction is exothermic, ΔH = −92 kJ/mol)\nTemperature: ~450°C — compromise between rate (needs heat) and yield (lower temp favours NH₃).\nPressure: ~200 atm — favours NH₃ side (4 mol gas → 2 mol gas) but is expensive.\nCatalyst: iron — speeds equilibrium without shifting position.\nYield: ~15% — unreacted N₂ and H₂ recycled."},
            {"heading": "Why Not Change Conditions to Maximise Yield?",
             "content": "Lower temperature → more NH₃ at equilibrium BUT too slow to be economical.\nHigher pressure → more NH₃ BUT very expensive equipment, safety risk.\n450°C and 200 atm are the industrial compromise.\nThe catalyst is essential — without it, equilibrium would be reached too slowly at 450°C."}
        ],
        "variables": [],
        "equations": ["N₂ + 3H₂ ⇌ 2NH₃"],
        "common_mistake": "A catalyst does NOT change equilibrium position — it speeds up reaching equilibrium but the final ratio of products to reactants is the same. Only temperature and pressure change the equilibrium POSITION.",
        "key_note": "Le Chatelier: changes are opposed. Endothermic forward → increase temp = more product. Fewer gas moles → increase pressure = more product.",
        "higher": "Equilibrium constant (Kc): concentration of products over reactants. Temperature is the ONLY thing that changes Kc.",
        "triple_only": None, "rp": None, "matching": None,
        "fifas": [],
        "quiz": [
            {"q": "The Haber process forward reaction is exothermic. Increasing temperature shifts equilibrium — which way?",
             "opts": [("Left — less ammonia produced", True), ("Right — more ammonia produced", False), ("No effect", False), ("Depends on pressure", False)],
             "wrong_explanations": {1: "Increasing temperature favours the ENDOTHERMIC direction. The forward (exothermic) reaction is disfavoured — equilibrium shifts LEFT.", 2: "Temperature always affects equilibrium — it shifts in the endothermic direction.", 3: "Temperature and pressure both independently affect equilibrium."}},
            {"q": "What does a catalyst do to a reaction at equilibrium?",
             "opts": [("Speeds up reaching equilibrium — doesn't change equilibrium position", True), ("Shifts equilibrium to the right", False), ("Increases the yield of product", False), ("Prevents the reverse reaction", False)],
             "wrong_explanations": {1: "Only temperature and pressure shift equilibrium position — not catalysts.", 2: "A catalyst can't create more product — it just helps reach the same equilibrium faster.", 3: "The reverse reaction still happens — catalysts speed up BOTH directions equally."}},
            {"q": "In the Haber process, why is 200 atm pressure used instead of 1000 atm?",
             "opts": [("1000 atm would be very expensive and dangerous — 200 atm is a practical compromise", True), ("1000 atm shifts equilibrium left", False), ("1000 atm would melt the iron catalyst", False), ("Higher pressure decreases yield in this reaction", False)],
             "wrong_explanations": {1: "Increasing pressure in the Haber process shifts equilibrium RIGHT (towards fewer moles of gas) — it would increase yield.", 2: "The iron catalyst melts at ~1538°C — pressure doesn't melt it.", 3: "Higher pressure increases yield (favours 2 moles NH₃ over 4 moles N₂+H₂). The issue is cost and safety."}},
            {"q": "What is meant by dynamic equilibrium?",
             "opts": [("Forward and reverse reactions occur at equal rates — concentrations are constant but not zero", True), ("The reaction has stopped completely", False), ("Only the forward reaction is occurring", False), ("Reactant and product concentrations are equal", False)],
             "wrong_explanations": {1: "Equilibrium means both reactions are STILL happening — not that they've stopped.", 2: "Only one direction = not equilibrium. At equilibrium both forward and reverse occur simultaneously.", 3: "Concentrations are CONSTANT at equilibrium but not necessarily equal — the ratio depends on the specific equilibrium."}}
        ]
    },
],

"organic": [
    {
        "id": "hydrocarbons",
        "title": "Hydrocarbons — Alkanes and Alkenes",
        "spec": "4.7.1",
        "summary": "Describe the structure and reactions of alkanes and alkenes.",
        "theory": [
            {"heading": "Crude Oil and Hydrocarbons",
             "content": "Crude oil = mixture of hydrocarbons (C and H only).\nSeparated by fractional distillation — different fractions condense at different temperatures.\nShorter chains: lower bp, more flammable, less viscous, more useful as fuels.\nLonger chains: higher bp, more viscous, less flammable, used in tarmac and lubricants."},
            {"heading": "Alkanes — Saturated Hydrocarbons",
             "content": "General formula: CₙH₂ₙ₊₂. Single bonds only — SATURATED.\nMethane (CH₄), ethane (C₂H₆), propane (C₃H₈), butane (C₄H₁₀).\nComplete combustion: CₙH₂ₙ₊₂ + O₂ → CO₂ + H₂O.\nIncomplete combustion (limited O₂): produces CO (toxic) + carbon soot."},
            {"heading": "Alkenes — Unsaturated Hydrocarbons",
             "content": "General formula: CₙH₂ₙ. Contains a C=C double bond — UNSATURATED.\nEthene (C₂H₄), propene (C₃H₆).\nMore reactive than alkanes — double bond available for addition reactions.\nTest: bromine water — decolourised by alkenes (orange → colourless). Alkanes: no reaction."},
            {"heading": "Cracking",
             "content": "Long-chain alkanes cracked → shorter alkanes + alkenes.\nThermal cracking: 700–1200°C, no catalyst.\nCatalytic cracking: ~500°C, aluminium oxide catalyst.\nImportant because demand for short-chain fuels (petrol) exceeds supply from distillation.\nAlkenes produced are used for making polymers (plastics)."}
        ],
        "variables": [],
        "equations": ["Alkanes: CₙH₂ₙ₊₂", "Alkenes: CₙH₂ₙ"],
        "common_mistake": "Alkanes are SATURATED (single bonds only). Alkenes are UNSATURATED (C=C double bond). The bromine water test distinguishes them: alkenes decolourise it, alkanes don't.",
        "key_note": "Bromine water: decolourised = alkene (unsaturated). Stays orange = alkane (saturated).",
        "higher": "Addition reactions of alkenes: add H₂ (hydrogenation), HBr, or H₂O (hydration) across the double bond.",
        "triple_only": "Amino acids: H₂N-CHR-COOH. Condensation polymerisation forms proteins (peptide bonds) and polyesters/polyamides.",
        "rp": None,
        "matching": {
            "title": "Alkane or Alkene?",
            "instruction": "Sort each property into alkane or alkene.",
            "pairs": [
                ("Alkane", "General formula CₙH₂ₙ₊₂, saturated"),
                ("Alkene", "General formula CₙH₂ₙ, unsaturated"),
                ("Alkene", "Decolourises bromine water"),
                ("Alkane", "Doesn't react with bromine water"),
                ("Both", "Combust in oxygen to produce CO₂ and H₂O"),
                ("Alkene", "Used to make addition polymers"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "What is the general formula for alkenes?",
             "opts": [("CₙH₂ₙ", True), ("CₙH₂ₙ₊₂", False), ("CₙH₂ₙ₋₂", False), ("CₙHₙ", False)],
             "wrong_explanations": {1: "CₙH₂ₙ₊₂ is for ALKANES — saturated, single bonds only.", 2: "CₙH₂ₙ₋₂ is for alkynes (triple bond) — not on GCSE spec.", 3: "CₙHₙ isn't a real GCSE homologous series."}},
            {"q": "Bromine water stays orange when added to an unknown gas. What does this tell you?",
             "opts": [("The gas is an alkane — saturated, no double bond", True), ("The gas is an alkene", False), ("The gas is hydrogen", False), ("The gas is carbon dioxide", False)],
             "wrong_explanations": {1: "Alkenes DECOLOURISE bromine water — if it stays orange, there's no C=C double bond.", 2: "Hydrogen doesn't react with bromine water at room temperature in this way.", 3: "CO₂ doesn't decolourise bromine water — it turns limewater cloudy."}},
            {"q": "What is produced in incomplete combustion of a hydrocarbon?",
             "opts": [("Carbon monoxide and soot (carbon)", True), ("Carbon dioxide and water", False), ("Oxygen and carbon", False), ("Hydrogen and carbon dioxide", False)],
             "wrong_explanations": {1: "CO₂ + H₂O = COMPLETE combustion (excess oxygen). Incomplete = limited O₂ → CO + soot.", 2: "Oxygen is a reactant — it's not produced. Limited O₂ → CO + carbon soot.", 3: "Hydrogen stays bonded as H₂O — incomplete combustion produces CO, not H₂."}},
            {"q": "Why is cracking important in the oil industry?",
             "opts": [("Converts less useful long-chain hydrocarbons into more useful shorter ones", True), ("Removes sulfur from crude oil", False), ("Converts alkenes into alkanes", False), ("Purifies crude oil by removing water", False)],
             "wrong_explanations": {1: "Desulfurisation removes sulfur — cracking changes chain length.", 2: "Cracking breaks long chains into short ones — producing alkenes, not converting them to alkanes.", 3: "Fractional distillation separates crude oil — cracking modifies the hydrocarbons."}},
            {"q": "Ethene (C₂H₄) reacts with bromine (Br₂). What type of reaction is this?",
             "opts": [("Addition reaction — bromine adds across the C=C double bond", True), ("Substitution reaction", False), ("Combustion", False), ("Cracking", False)],
             "wrong_explanations": {1: "Substitution is for alkanes reacting with halogens in UV light — not alkenes with bromine water.", 2: "Combustion requires oxygen and produces CO₂ and H₂O — not what happens here.", 3: "Cracking breaks long chains — this reaction is a small molecule adding across a double bond."}}
        ]
    },
],

"analysis": [
    {
        "id": "chemical-tests",
        "title": "Chemical Analysis and Identifying Substances",
        "spec": "4.8",
        "summary": "Use chromatography, flame tests and chemical tests to identify unknown substances.",
        "theory": [
            {"heading": "Pure Substances and Chromatography",
             "content": "A pure substance has a sharp, single melting point.\nA mixture melts over a range — or shows multiple spots on chromatography.\nRf = distance moved by spot ÷ distance moved by solvent front.\nRf is always between 0 and 1.\nSame Rf in same solvent = same substance."},
            {"heading": "Flame Tests",
             "content": "Li⁺: crimson red. Na⁺: yellow/orange. K⁺: lilac/violet.\nCa²⁺: orange-red. Cu²⁺: blue-green. Ba²⁺: green.\nMethod: clean platinum wire → dip in sample → blue Bunsen flame.\nSodium is very easy to see — even tiny traces give bright yellow."},
            {"heading": "Testing for Gases",
             "content": "H₂: burning splint → squeaky pop.\nO₂: glowing splint → relights.\nCO₂: limewater → turns milky/cloudy.\nCl₂: damp blue litmus → turns red then bleaches white."},
            {"heading": "Testing for Ions",
             "content": "Carbonate (CO₃²⁻): add dilute acid → fizzes, CO₂ produced → limewater test confirms.\nHalides (Cl⁻, Br⁻, I⁻): add dilute HNO₃ then silver nitrate → white (Cl⁻), cream (Br⁻), yellow (I⁻) precipitate.\nSulfate (SO₄²⁻): add dilute HCl then barium chloride → white precipitate (BaSO₄).\nAmmonium (NH₄⁺): add NaOH and warm → ammonia gas (turns damp red litmus blue)."}
        ],
        "variables": [],
        "equations": ["Rf = distance moved by spot ÷ distance moved by solvent"],
        "common_mistake": "Rf values CANNOT be greater than 1. If yours is above 1, check your measurements. Also — sodium gives YELLOW/ORANGE flame, not yellow-green. Barium gives green. Don't mix them up!",
        "key_note": None,
        "higher": "Mass spectrometry: molecular ion peak = Mr of compound. IR spectroscopy: identifies functional groups from absorption pattern.",
        "triple_only": None,
        "rp": ["RP6 — Paper chromatography to identify food dyes", "RP7 — Identify ions using flame tests and precipitation reactions"],
        "matching": {
            "title": "Match the Metal Ion to its Flame Colour",
            "instruction": "Match each ion to the correct flame test result.",
            "pairs": [
                ("Lithium Li⁺", "Crimson red"),
                ("Sodium Na⁺", "Yellow / orange"),
                ("Potassium K⁺", "Lilac / violet"),
                ("Calcium Ca²⁺", "Orange-red"),
                ("Copper Cu²⁺", "Blue-green"),
                ("Barium Ba²⁺", "Green"),
            ]
        },
        "fifas": [
            {"label": "Example — Rf calculation",
             "question": "A spot travels 3.6 cm. The solvent front travels 9.0 cm. Calculate Rf.",
             "steps": [("F","Rf = distance by spot ÷ distance by solvent"), ("I","Rf = 3.6 ÷ 9.0"), ("F","Check: must be between 0 and 1"), ("A","Rf = 0.4")]}
        ],
        "quiz": [
            {"q": "What colour flame does potassium produce?",
             "opts": [("Lilac/violet", True), ("Yellow/orange", False), ("Crimson red", False), ("Blue-green", False)],
             "wrong_explanations": {1: "Yellow/orange = SODIUM. Very common mix-up — potassium gives lilac/violet.", 2: "Crimson red = LITHIUM. Li is red like a ruby.", 3: "Blue-green = COPPER. Distinctive for copper compounds."}},
            {"q": "How do you test for hydrogen gas?",
             "opts": [("Burning splint — gives a squeaky pop", True), ("Glowing splint — relights", False), ("Limewater — turns cloudy", False), ("Damp litmus — bleaches", False)],
             "wrong_explanations": {1: "Glowing splint relighting = OXYGEN.", 2: "Limewater cloudy = CARBON DIOXIDE.", 3: "Litmus bleaching = CHLORINE."}},
            {"q": "A sample gives two spots on chromatography. What does this mean?",
             "opts": [("The sample is a mixture of at least two substances", True), ("The sample is very pure", False), ("The Rf is greater than 1", False), ("The solvent was too hot", False)],
             "wrong_explanations": {1: "One spot = pure substance. Two spots = mixture (two components with different Rf values).", 2: "Rf cannot be greater than 1 — the spot cannot travel further than the solvent.", 3: "Solvent temperature can affect separation but doesn't explain why two spots appear for a mixture."}},
            {"q": "Silver nitrate solution gives a yellow precipitate with an unknown solution. Which ion is present?",
             "opts": [("Iodide (I⁻)", True), ("Chloride (Cl⁻)", False), ("Bromide (Br⁻)", False), ("Sulfate (SO₄²⁻)", False)],
             "wrong_explanations": {1: "Chloride gives a WHITE precipitate (AgCl).", 2: "Bromide gives a CREAM precipitate (AgBr). Yellow = iodide.", 3: "Sulfate is tested with barium chloride — not silver nitrate."}},
            {"q": "What is the maximum Rf value possible?",
             "opts": [("1.0", True), ("Greater than 1 if substance is very soluble", False), ("10", False), ("It varies with temperature", False)],
             "wrong_explanations": {1: "Rf CANNOT exceed 1 — the spot can never travel further than the solvent front. If yours is >1, you measured wrong.", 2: "Rf scale is 0 to 1, not 0 to 10.", 3: "Temperature affects separation speed but Rf is always a ratio between 0 and 1."}}
        ]
    },
],

"atmosphere": [
    {
        "id": "atmosphere-climate",
        "title": "The Atmosphere and Climate Change",
        "spec": "4.9",
        "summary": "Describe the composition of the atmosphere, the greenhouse effect and human impact.",
        "theory": [
            {"heading": "Current Composition",
             "content": "Nitrogen (N₂): ~78%. Oxygen (O₂): ~21%. Argon (Ar): ~1%.\nCarbon dioxide (CO₂): ~0.04% (increasing due to human activity).\nPlus water vapour and trace gases.\nProportions have been roughly stable for ~200 million years."},
            {"heading": "Evolution of the Atmosphere",
             "content": "Early Earth: volcanoes released CO₂, water vapour, N₂. Very little or no oxygen.\nOceans formed as water vapour condensed.\nPhotosynthesis (early algae/plants): consumed CO₂, released O₂ → oxygen levels rose.\nCarbon locked in fossil fuels (dead organisms compressed over millions of years)."},
            {"heading": "The Greenhouse Effect",
             "content": "Greenhouse gases (CO₂, methane CH₄, water vapour H₂O) absorb outgoing infrared radiation.\nNatural greenhouse effect: keeps Earth warm enough for life (~+33°C above no-atmosphere temperature).\nEnhanced greenhouse effect: burning fossil fuels, deforestation, farming → more CO₂ and CH₄.\nMore greenhouse gas → more IR absorbed → Earth warms further → climate change."},
            {"heading": "Consequences and Solutions",
             "content": "Rising temperatures → melting ice → rising sea levels → flooding of low-lying land.\nMore extreme weather events. Disruption to ecosystems.\nSolutions: renewable energy, electric vehicles, reforestation, carbon capture, nuclear power, reduce meat consumption.\nCarbon footprint = total CO₂ equivalent produced by an activity or person."}
        ],
        "variables": [],
        "equations": [],
        "common_mistake": "The greenhouse effect is NOT inherently bad — without it Earth would be about −18°C. It's the ENHANCED greenhouse effect from human activities that causes climate change. Also: water vapour is actually the most abundant greenhouse gas — not CO₂.",
        "key_note": "Atmosphere: 78% N₂, 21% O₂, 1% Ar, 0.04% CO₂. Greenhouse gases: CO₂, CH₄, H₂O vapour.",
        "higher": "Evaluating climate change evidence: ice cores show CO₂ and temperature correlation over 800,000 years. Scientific consensus overwhelmingly supports human-caused warming.",
        "triple_only": None, "rp": None,
        "matching": {
            "title": "Match the Gas to its Role",
            "instruction": "Match each gas to its significance.",
            "pairs": [
                ("Nitrogen (N₂)", "~78% — mostly unreactive, used for making fertilisers"),
                ("Oxygen (O₂)", "~21% — essential for combustion and aerobic respiration"),
                ("Carbon dioxide (CO₂)", "Greenhouse gas — absorbed by plants in photosynthesis"),
                ("Methane (CH₄)", "Potent greenhouse gas — from cattle and landfill"),
                ("Argon (Ar)", "~1% — noble gas, completely inert"),
            ]
        },
        "fifas": [],
        "quiz": [
            {"q": "What percentage of the atmosphere is nitrogen?",
             "opts": [("~78%", True), ("~21%", False), ("~1%", False), ("~0.04%", False)],
             "wrong_explanations": {1: "~21% is OXYGEN — the second most abundant gas.", 2: "~1% is ARGON.", 3: "~0.04% is CO₂ — tiny but crucial."}},
            {"q": "What process increased oxygen in the early atmosphere?",
             "opts": [("Photosynthesis by early plants and algae", True), ("Volcanic eruptions", False), ("Decomposition", False), ("Evaporation of water", False)],
             "wrong_explanations": {1: "Volcanoes released CO₂ and water vapour — not oxygen.", 2: "Aerobic decomposition USES oxygen — doesn't produce it.", 3: "Evaporation forms clouds and rain — it doesn't produce oxygen."}},
            {"q": "Which gas is most associated with cattle farming as a greenhouse gas?",
             "opts": [("Methane (CH₄)", True), ("Carbon dioxide (CO₂)", False), ("Nitrogen (N₂)", False), ("Argon (Ar)", False)],
             "wrong_explanations": {1: "CO₂ is mainly from burning fossil fuels and deforestation.", 2: "Nitrogen is unreactive at room temperature — not a greenhouse gas.", 3: "Argon is a noble gas — completely inert and not a greenhouse gas."}},
            {"q": "What is a carbon footprint?",
             "opts": [("Total CO₂ equivalent greenhouse gas emissions from an activity", True), ("The amount of carbon in a substance", False), ("A carbon stain left on equipment", False), ("The mass of coal burned per year", False)],
             "wrong_explanations": {1: "Carbon content of a substance is nothing to do with carbon footprint.", 2: "Carbon footprint is a measure of environmental impact — not a physical mark.", 3: "Carbon footprint covers ALL activities, not just coal burning."}},
            {"q": "How does deforestation contribute to climate change?",
             "opts": [("Trees absorb CO₂ — removing them reduces uptake and releases stored carbon", True), ("Trees produce methane when they decompose", False), ("Forests cool the air — removing them warms it", False), ("Roots lock CO₂ underground", False)],
             "wrong_explanations": {1: "Decomposing trees do release some CO₂ (and small amounts of methane) but the main issue is loss of photosynthetic CO₂ absorption.", 2: "Forests do have a cooling microclimate effect, but the main climate issue is CO₂ balance.", 3: "It's LEAVES that absorb CO₂ through photosynthesis — not roots locking it underground."}}
        ]
    },
],

"resources": [
    {
        "id": "haber-resources",
        "title": "The Haber Process, Fertilisers and Using Resources",
        "spec": "4.10",
        "summary": "Explain the Haber process, NPK fertilisers, and evaluate sustainable use of resources.",
        "theory": [
            {"heading": "The Haber Process",
             "content": "Reaction: N₂ + 3H₂ ⇌ 2NH₃ (exothermic forward reaction).\nRaw materials: N₂ from fractional distillation of air; H₂ from natural gas + steam.\nConditions: ~450°C, ~200 atm, iron catalyst.\nYield: ~15% per pass — unreacted gases are recycled."},
            {"heading": "NPK Fertilisers",
             "content": "Plants need N (nitrogen for protein/growth), P (phosphorus for DNA/roots), K (potassium for enzymes).\nNPK fertilisers contain compounds supplying all three.\nExcessive use causes eutrophication: fertilisers wash into rivers → algal bloom → O₂ depleted → fish die.\nAmmonia → nitric acid + ammonia → ammonium nitrate (N-rich fertiliser)."},
            {"heading": "Life Cycle Assessment (LCA)",
             "content": "LCA evaluates the environmental impact of a product throughout its entire life.\nStages: obtaining raw materials → manufacturing → use → disposal.\nAll stages considered: energy use, water use, waste produced, CO₂ emissions.\nHelps compare products — e.g. is a reusable bag better than disposable?"},
            {"heading": "Water Treatment",
             "content": "Drinking water must be safe.\nSteps: sedimentation → filtration (sand/gravel) → chlorination (kills bacteria).\nDistilled water (pure): used in labs — but too expensive for drinking water at scale.\nFluoridation: some areas add fluoride to prevent tooth decay (controversial)."}
        ],
        "variables": [],
        "equations": ["N₂ + 3H₂ ⇌ 2NH₃"],
        "common_mistake": "Higher temperature reduces ammonia yield (exothermic forward reaction disfavoured at high temp). Lower temperature increases yield but slows rate. 450°C is the compromise.",
        "key_note": "Haber conditions: 450°C, 200 atm, iron catalyst, recycled unreacted gases.",
        "higher": "Atom economy of Haber process = 100% (only one product — NH₃). % yield is low (~15%) because equilibrium favours reactants at these conditions.",
        "triple_only": None, "rp": None, "matching": None,
        "fifas": [],
        "quiz": [
            {"q": "What are the conditions for the Haber process?",
             "opts": [("~450°C, ~200 atm, iron catalyst", True), ("~100°C, ~1 atm, platinum catalyst", False), ("~1000°C, ~500 atm, no catalyst", False), ("Room temperature, ~200 atm, iron catalyst", False)],
             "wrong_explanations": {1: "100°C and 1 atm would give very low yield and negligible rate.", 2: "1000°C shifts equilibrium strongly left (exothermic reaction) — almost no ammonia would form.", 3: "Room temperature is far too slow — the iron catalyst needs heat to work effectively."}},
            {"q": "Why does high temperature reduce ammonia yield in the Haber process?",
             "opts": [("The forward reaction is exothermic — high temp favours the endothermic reverse reaction", True), ("Iron catalyst doesn't work at high temperatures", False), ("High temperature increases pressure too much", False), ("Nitrogen and hydrogen don't react at high temperatures", False)],
             "wrong_explanations": {1: "Iron works fine at 450°C — the equilibrium shift is the real reason for lower yield.", 2: "Temperature and pressure are independent variables in the Haber process.", 3: "N₂ and H₂ DO react at high temperatures — the issue is that equilibrium favours the reverse reaction."}},
            {"q": "What causes eutrophication?",
             "opts": [("Excess fertiliser washes into water — algae bloom uses up all the oxygen", True), ("Burning fuels releases CO₂ into lakes", False), ("Industrial waste heats up rivers", False), ("Plastic waste blocks river flow", False)],
             "wrong_explanations": {1: "CO₂ from burning fuels contributes to acidification of oceans — not directly eutrophication.", 2: "Thermal pollution is different — it reduces dissolved oxygen but not through algal blooms.", 3: "Plastic causes habitat damage and wildlife harm — not eutrophication (nutrient excess)."}},
            {"q": "What is a Life Cycle Assessment (LCA)?",
             "opts": [("An evaluation of the environmental impact of a product from raw material to disposal", True), ("A test to see how long a product lasts", False), ("A calculation of profit over a product's lifetime", False), ("An assessment of worker safety during manufacturing", False)],
             "wrong_explanations": {1: "Product lifetime/durability is separate — LCA is about ENVIRONMENTAL impact at every stage.", 2: "LCA is environmental, not financial.", 3: "Worker safety is health and safety — LCA is about environmental sustainability."}},
            {"q": "Why are unreacted gases recycled in the Haber process?",
             "opts": [("Only ~15% converts per pass — recycling improves overall yield and efficiency", True), ("The gases are toxic and can't be released", False), ("Recycling lowers the temperature needed", False), ("It prevents the catalyst from being damaged", False)],
             "wrong_explanations": {1: "N₂ and H₂ are safe gases — they're recycled for economic reasons, not safety.", 2: "Recycling doesn't change the reaction temperature.", 3: "Gas recycling and catalyst maintenance are separate concerns."}}
        ]
    },
],

"energy-changes": [
    {
        "id": "exo-endo-reactions",
        "title": "Exothermic, Endothermic and Bond Energies",
        "spec": "4.5",
        "summary": "Classify reactions and calculate energy changes using bond energies.",
        "theory": [
            {"heading": "Exothermic Reactions",
             "content": "Release energy to surroundings — temperature of surroundings RISES.\nProducts have less energy than reactants.\nΔH is NEGATIVE.\nExamples: combustion, neutralisation, oxidation, respiration, hand warmers, displacement."},
            {"heading": "Endothermic Reactions",
             "content": "Absorb energy from surroundings — temperature of surroundings FALLS.\nProducts have more energy than reactants.\nΔH is POSITIVE.\nExamples: photosynthesis, thermal decomposition, dissolving ammonium nitrate, cold packs."},
            {"heading": "Bond Energies",
             "content": "Bond BREAKING absorbs energy (endothermic).\nBond FORMING releases energy (exothermic).\nΔH = energy absorbed (breaking bonds in reactants) − energy released (forming bonds in products).\nNegative ΔH = more energy released in forming bonds than absorbed breaking them = exothermic."},
            {"heading": "Reaction Profiles",
             "content": "Shows energy of reactants and products on a diagram.\nExothermic: products at lower energy than reactants.\nEndothermic: products at higher energy than reactants.\nActivation energy = energy from reactants to peak (transition state).\nCatalyst: lowers the peak — doesn't change reactant or product energy levels."}
        ],
        "variables": [],
        "equations": ["ΔH = energy in (bond breaking) − energy out (bond forming)"],
        "common_mistake": "Bond BREAKING absorbs energy. Bond FORMING releases energy. Students always get these backwards. Think: you have to put energy IN to break a bond apart, like pulling something apart.",
        "key_note": "ΔH negative = exothermic (releases heat). ΔH positive = endothermic (absorbs heat).",
        "higher": "Bond energy calculation: list every bond broken and formed, calculate total energy in and total energy out, then ΔH = in − out.",
        "triple_only": None,
        "rp": "RP3 — Measure temperature changes in neutralisation and displacement reactions using a polystyrene cup calorimeter.",
        "matching": {
            "title": "Exothermic or Endothermic?",
            "instruction": "Sort each reaction correctly.",
            "pairs": [
                ("Exothermic", "Combustion of methane"),
                ("Exothermic", "Neutralisation of HCl and NaOH"),
                ("Exothermic", "Respiration"),
                ("Endothermic", "Photosynthesis"),
                ("Endothermic", "Thermal decomposition of CaCO₃"),
                ("Endothermic", "Dissolving ammonium nitrate in water"),
            ]
        },
        "fifas": [
            {"label": "Example — Bond energy calculation",
             "question": "H₂ + Cl₂ → 2HCl. Bond energies: H−H = 436, Cl−Cl = 242, H−Cl = 431 kJ/mol. Calculate ΔH.",
             "steps": [("F","ΔH = energy in (bonds broken) − energy out (bonds formed)"), ("I","Energy in: 436 + 242 = 678 kJ. Energy out: 2 × 431 = 862 kJ"), ("F","ΔH = 678 − 862"), ("A","ΔH = −184 kJ/mol (exothermic — more energy released than absorbed)")]}
        ],
        "quiz": [
            {"q": "Which process RELEASES energy?",
             "opts": [("Bond forming", True), ("Bond breaking", False), ("Both equally", False), ("Neither", False)],
             "wrong_explanations": {1: "Bond BREAKING absorbs energy — you must PUT IN energy to pull bonds apart.", 2: "Both can't release equally — breaking absorbs, forming releases.", 3: "Both definitely involve energy transfer — just in opposite directions."}},
            {"q": "ΔH = −350 kJ/mol. What type of reaction?",
             "opts": [("Exothermic", True), ("Endothermic", False), ("Neutral", False), ("Reversible", False)],
             "wrong_explanations": {1: "Endothermic has POSITIVE ΔH. Negative ΔH = exothermic.", 2: "Neutral would mean ΔH = 0. −350 kJ/mol is clearly exothermic.", 3: "Reversibility is separate from ΔH sign. Many reversible reactions are exothermic in the forward direction."}},
            {"q": "On a reaction profile, what does a catalyst change?",
             "opts": [("It lowers the activation energy peak", True), ("It lowers the energy of the products", False), ("It raises the energy of the reactants", False), ("It changes the overall ΔH", False)],
             "wrong_explanations": {1: "A catalyst doesn't affect product energy — just the energy barrier (activation energy).", 2: "Reactant energy is unchanged — the catalyst just provides a lower-energy pathway.", 3: "ΔH = energy difference between reactants and products. A catalyst doesn't change either — only the peak."}},
            {"q": "Which of these is an endothermic process?",
             "opts": [("Thermal decomposition of calcium carbonate", True), ("Combustion of petrol", False), ("Neutralisation of HCl with NaOH", False), ("Rusting of iron", False)],
             "wrong_explanations": {1: "Combustion releases energy — exothermic.", 2: "Neutralisation releases heat — exothermic (temperature rises).", 3: "Rusting is oxidation — exothermic (though very slow)."}},
            {"q": "In a bond energy calculation: energy in = 600 kJ, energy out = 800 kJ. What is ΔH?",
             "opts": [("−200 kJ (exothermic)", True), ("+200 kJ (endothermic)", False), ("+1400 kJ", False), ("−1400 kJ", False)],
             "wrong_explanations": {1: "ΔH = in − out = 600 − 800 = −200 kJ. Positive because out > in means more energy released.", 2: "You subtracted the wrong way: ΔH = in − out = 600 − 800 = −200 kJ (negative = exothermic).", 3: "You added in + out = 1400. ΔH = in − out = 600 − 800 = −200 kJ."}}
        ]
    },
],
}
