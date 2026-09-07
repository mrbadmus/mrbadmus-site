"""Chemistry · Bonding, structure and the properties of matter (5.2).

Twelve assignment questions for each of the topic's twelve subtopics, written
around the lesson pages' own "Test yourself" items rather than from them.

The distractors are built on the misconceptions the brief declares for each
subtopic: that melting a simple molecular substance breaks its covalent bonds;
that the ionic bond IS the electron transfer rather than the attraction it
leaves behind; that a solid full of ions ought to conduct; that a metallic bond
joins neighbouring atoms rather than ions to an electron sea; that diamond and
graphite should behave alike because both are giant covalent carbon; that a
polymer chain is a giant covalent structure; and that a nanoparticle of gold
must be a different substance from bulk gold.

Where a lesson question already tests a misconception head-on, the assignment
question comes at it from the other direction — spot the error, evaluate the
claim, predict the counterfactual, or work the numbers.
"""

TOPIC = "bonding"
SUBJECT = "chemistry"

QUESTIONS = [

    # ── chemical-bonds ────────────────────────────────────────────────────
    {
        "id": "ks4-chemical-bonds-e01",
        "subtopic_slug": "chemical-bonds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the reason atoms form chemical bonds with one another.",
        "options": [
            "To increase the number of protons held in their nuclei",
            "To become heavier, because heavier atoms are more stable",
            "To achieve a full outer shell of electrons and become more "
            "stable",
            "To lose all of their electrons and end up completely neutral",
        ],
        "correct_index": 2,
        "why": "Bonding lets an atom reach a full outer shell, the stable "
               "arrangement the noble gases already have.",
    },
    {
        "id": "ks4-chemical-bonds-e02",
        "subtopic_slug": "chemical-bonds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the pair of elements that would bond covalently.",
        "options": [
            "Sulfur and oxygen, because both of them are non-metals",
            "Potassium and bromine, because they sit in different groups",
            "Magnesium and oxygen, because both need a full outer shell",
            "Copper and zinc, because both are shiny solid elements",
        ],
        "correct_index": 0,
        "why": "Covalent bonding happens between non-metals only, and sulfur "
               "and oxygen are both non-metals, so they share electron pairs.",
    },
    {
        "id": "ks4-chemical-bonds-e03",
        "subtopic_slug": "chemical-bonds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of bonding present in a block of pure "
                "aluminium.",
        "options": [
            "Ionic, because aluminium atoms form ions with a 3+ charge",
            "Covalent, because the atoms share their three outer electrons "
            "with each other",
            "None, because a single element cannot contain chemical bonds",
            "Metallic, because positive ions sit in a sea of delocalised "
            "electrons",
        ],
        "correct_index": 3,
        "why": "A pure metal has metallic bonding: positive metal ions held "
               "by their attraction to a shared sea of delocalised electrons.",
    },
    {
        "id": "ks4-chemical-bonds-e04",
        "subtopic_slug": "chemical-bonds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the electrons that are free to move throughout a metal "
                "structure.",
        "options": [
            "Shared electrons",
            "Delocalised electrons",
            "Transferred electrons",
            "Bonding pairs",
        ],
        "correct_index": 1,
        "why": "Metal atoms release their outer electrons, which become "
               "delocalised — no longer belonging to any one atom.",
    },
    {
        "id": "ks4-chemical-bonds-s01",
        "subtopic_slug": "chemical-bonds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that when solid iodine melts, the covalent "
                "bonds inside its molecules break. Explain why this is wrong.",
        "options": [
            "Melting overcomes only the weak forces between whole I2 "
            "molecules; the covalent bonds inside them stay intact",
            "Melting breaks the covalent bonds first, and the weak forces "
            "between whole molecules are overcome afterwards",
            "Iodine is held together by ionic bonds, so it contains no "
            "covalent bonds that could break",
            "The covalent bonds in iodine are weak, which is why so little "
            "energy is needed to melt it",
        ],
        "correct_index": 0,
        "why": "Melting separates whole molecules from one another; the "
               "strong covalent bonds inside each molecule are untouched.",
    },
    {
        "id": "ks4-chemical-bonds-s02",
        "subtopic_slug": "chemical-bonds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the bonding in potassium bromide with the bonding in "
                "bromine.",
        "options": [
            "Both are covalent, with the bromine atoms sharing pairs of "
            "electrons in each substance",
            "Both are ionic, because any substance containing bromine "
            "contains bromide ions",
            "Potassium bromide is covalent (shared pairs); bromine is ionic "
            "(transferred electrons)",
            "Potassium bromide is ionic (electrons transferred); bromine is "
            "covalent (electrons shared)",
        ],
        "correct_index": 3,
        "why": "Potassium is a metal and bromine a non-metal, so electrons "
               "transfer; bromine alone is two non-metal atoms, so they "
               "share.",
    },
    {
        "id": "ks4-chemical-bonds-s03",
        "subtopic_slug": "chemical-bonds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hydrogen and chlorine form a covalent bond "
                "rather than an ionic bond.",
        "options": [
            "Hydrogen behaves as a metal, so it transfers its single electron "
            "across to the chlorine atom instead",
            "Both are non-metals, so neither loses electrons to the other and "
            "they share a pair instead",
            "Chlorine is a non-metal, so it releases electrons into a sea "
            "that hydrogen shares",
            "Hydrogen has only one electron, so it must form an ionic bond to "
            "fill its shell",
        ],
        "correct_index": 1,
        "why": "Ionic bonding needs a metal to give electrons away; between "
               "two non-metals the only route to full shells is sharing.",
    },
    {
        "id": "ks4-chemical-bonds-s04",
        "subtopic_slug": "chemical-bonds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A substance conducts electricity as a solid and also when "
                "molten. Deduce the type of bonding it contains.",
        "options": [
            "Ionic, because ions are present in the solid and in the liquid",
            "Simple molecular, because molecules can move in both states",
            "Metallic, because delocalised electrons move in the solid and in "
            "the liquid",
            "Giant covalent, because covalent bonds carry the current in both "
            "states",
        ],
        "correct_index": 2,
        "why": "Only metallic bonding supplies charge carriers — delocalised "
               "electrons — that are already mobile in the solid state.",
    },
    {
        "id": "ks4-chemical-bonds-h01",
        "subtopic_slug": "chemical-bonds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium chloride melts at 801 °C but chlorine melts at -101 "
                "°C. Explain why the melting points differ so much, although "
                "both substances contain chlorine.",
        "options": [
            "Chlorine's covalent bonds are far weaker than the covalent bonds "
            "inside sodium chloride",
            "Chlorine molecules are heavier than sodium chloride particles, "
            "so they separate from one another more easily",
            "Sodium chloride is a mixture, and mixtures always melt higher "
            "than pure elements do",
            "Sodium chloride is a giant ionic lattice with strong forces; "
            "chlorine is small molecules with weak forces",
        ],
        "correct_index": 3,
        "why": "Melting NaCl means separating billions of strongly attracting "
               "ions; melting Cl2 only overcomes weak forces between "
               "molecules.",
    },
    {
        "id": "ks4-chemical-bonds-h02",
        "subtopic_slug": "chemical-bonds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Magnesium oxide must be covalent, because "
                "magnesium and oxygen both need to fill their outer shells by "
                "sharing.' Evaluate this statement.",
        "options": [
            "It is correct: both atoms need a full outer shell, and sharing "
            "pairs of electrons is how each of them gets one",
            "It is wrong: magnesium is a metal, so it loses its two outer "
            "electrons rather than sharing, and the bonding is ionic",
            "It is wrong: oxygen is the metal here, so it gives electrons "
            "away and the bonding is metallic",
            "It is wrong: neither atom needs a full outer shell, so magnesium "
            "oxide contains no bonds",
        ],
        "correct_index": 1,
        "why": "A metal bonded to a non-metal transfers electrons, giving "
               "Mg2+ and O2- ions held by electrostatic attraction.",
    },
    {
        "id": "ks4-chemical-bonds-h03",
        "subtopic_slug": "chemical-bonds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how electron transfer and electron sharing can both "
                "give every atom a full outer shell, even though only one of "
                "them produces ions.",
        "options": [
            "In both cases the electrons move permanently from one atom to "
            "the other, so charged ions are produced by sharing just as they "
            "are by transfer",
            "In both cases the electrons are shared, but only ionic bonding "
            "involves a metal, so ions form",
            "Transfer moves electrons from one atom to the other, so charged "
            "ions form; sharing lets both atoms count the same pair, so both "
            "stay neutral",
            "Transfer gives both atoms extra electrons, while sharing removes "
            "electrons from both atoms",
        ],
        "correct_index": 2,
        "why": "A shared pair is counted by both atoms at once, so neither "
               "gains or loses charge — unlike a transfer, which creates "
               "ions.",
    },
    {
        "id": "ks4-chemical-bonds-h04",
        "subtopic_slug": "chemical-bonds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Silicon dioxide is made of two non-metals, yet it melts at "
                "about 1710 °C. Suggest why its melting point is so high.",
        "options": [
            "It is giant covalent, so melting it means breaking strong "
            "covalent bonds throughout the structure",
            "It is simple molecular, so unusually strong intermolecular "
            "forces have to be overcome",
            "It is ionic, so electrostatic forces between silicon ions and "
            "oxide ions have to be broken",
            "It is metallic, so a sea of delocalised electrons holds the "
            "silicon atoms in place",
        ],
        "correct_index": 0,
        "why": "In a giant covalent structure the covalent bonds run right "
               "through the solid, so melting really does break them.",
    },

    # ── ionic-bonding ─────────────────────────────────────────────────────
    {
        "id": "ks4-ionic-bonding-e01",
        "subtopic_slug": "ionic-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the charge on the ion formed by an element in Group 6.",
        "options": [
            "A charge of 2+",
            "A charge of 2-",
            "A charge of 6-",
            "A charge of 6+",
        ],
        "correct_index": 1,
        "why": "A Group 6 atom has six outer electrons and gains two to fill "
               "its shell, so the ion carries a 2- charge.",
    },
    {
        "id": "ks4-ionic-bonding-e02",
        "subtopic_slug": "ionic-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A magnesium atom has the electronic structure 2.8.2. State "
                "the electronic structure of a magnesium ion, Mg2+.",
        "options": [
            "2.8.2",
            "2.8.4",
            "2.8.1",
            "2.8",
        ],
        "correct_index": 3,
        "why": "Losing both outer electrons empties the third shell, leaving "
               "the full 2.8 arrangement of neon.",
    },
    {
        "id": "ks4-ionic-bonding-e03",
        "subtopic_slug": "ionic-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the force that holds the two ions together in an ionic "
                "bond.",
        "options": [
            "Electrostatic attraction between oppositely charged ions",
            "A shared pair of electrons attracted to both nuclei",
            "Attraction between positive ions and delocalised electrons",
            "Weak intermolecular forces between neighbouring ions",
        ],
        "correct_index": 0,
        "why": "The ionic bond is the electrostatic attraction between the "
               "positive and negative ions that the transfer created.",
    },
    {
        "id": "ks4-ionic-bonding-e04",
        "subtopic_slug": "ionic-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lithium (Group 1) reacts with fluorine (Group 7). State the "
                "ions each element forms.",
        "options": [
            "Li- and F+",
            "Li2+ and F2-",
            "Li+ and F-",
            "Li+ and F2-",
        ],
        "correct_index": 2,
        "why": "A Group 1 atom loses one electron to give a 1+ ion and a "
               "Group 7 atom gains one to give a 1- ion.",
    },
    {
        "id": "ks4-ionic-bonding-s01",
        "subtopic_slug": "ionic-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium is 2.8.2. Explain why it loses two electrons when "
                "it forms an ion, rather than gaining six.",
        "options": [
            "Gaining six electrons would make the magnesium ion far too heavy "
            "to fit into the lattice of chloride ions around it",
            "Magnesium already has six outer electrons, so there is no room "
            "to gain any more",
            "Metal atoms are physically unable to gain electrons under any "
            "circumstances",
            "Losing two empties the outer shell, leaving a full shell "
            "beneath, and needs far less energy than gaining six",
        ],
        "correct_index": 3,
        "why": "Emptying an outer shell that holds only two electrons is much "
               "easier than filling it with six more.",
    },
    {
        "id": "ks4-ionic-bonding-s02",
        "subtopic_slug": "ionic-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to the electronic structure of a "
                "chlorine atom (2.8.7) when it becomes a chloride ion.",
        "options": [
            "It loses one electron from its outer shell to become 2.8.6, "
            "which is the arrangement of sulfur",
            "It shares one electron with a sodium atom so that both become "
            "2.8.8",
            "It gains one electron into its outer shell to become 2.8.8, the "
            "arrangement of argon",
            "It gains eight electrons so that its outer shell holds sixteen",
        ],
        "correct_index": 2,
        "why": "One extra electron completes chlorine's outer shell, giving "
               "the stable 2.8.8 arrangement and a 1- charge.",
    },
    {
        "id": "ks4-ionic-bonding-s03",
        "subtopic_slug": "ionic-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes the formula of lithium oxide as LiO. "
                "Explain the error in this formula.",
        "options": [
            "Li+ carries 1+ and the oxide ion carries 2-, so two lithium ions "
            "are needed: the formula is Li2O",
            "Lithium forms Li2+ ions, so the formula should be written LiO2",
            "The oxide ion carries 1-, so the formula should be written Li2O2",
            "Nothing is wrong, because the charges on the ions do not affect "
            "the formula of an ionic compound in any way",
        ],
        "correct_index": 0,
        "why": "The total positive and negative charges must cancel, so one "
               "O2- needs two Li+ ions.",
    },
    {
        "id": "ks4-ionic-bonding-s04",
        "subtopic_slug": "ionic-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the ionic bonding in a compound acts in all "
                "directions, rather than only between the two atoms that "
                "exchanged electrons.",
        "options": [
            "Each ion is bonded only to the one atom that it exchanged its "
            "electrons with, and to nothing else",
            "Each ion's charge attracts every oppositely charged ion around "
            "it, not just one partner",
            "The ions are joined by shared pairs of electrons pointing in all "
            "directions",
            "Delocalised electrons spread the attraction evenly through the "
            "whole lattice",
        ],
        "correct_index": 1,
        "why": "A charge attracts every opposite charge near it, so each ion "
               "is held by all of its neighbours in the lattice.",
    },
    {
        "id": "ks4-ionic-bonding-h01",
        "subtopic_slug": "ionic-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A compound has the formula M2O3, where M is a metal. Deduce "
                "the charge on the M ion and the group M belongs to.",
        "options": [
            "M forms 3+ ions, so M is in Group 3",
            "M forms 2+ ions, so M is in Group 2",
            "M forms 3- ions, so M is in Group 5",
            "M forms 6+ ions, so M is in Group 6",
        ],
        "correct_index": 0,
        "why": "Three O2- ions carry 6- in total, so two M ions must carry 6+ "
               "between them — that is 3+ each, a Group 3 metal.",
    },
    {
        "id": "ks4-ionic-bonding-h02",
        "subtopic_slug": "ionic-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Potassium bromide and potassium iodide both have a 1:1 ratio "
                "of ions, although bromine and iodine atoms are different "
                "sizes. Explain why the ratio is the same.",
        "options": [
            "Bromide ions carry 1- but iodide ions carry 2-, so the ratios "
            "only appear to be the same",
            "Potassium changes its charge to match the size of the halide ion "
            "in each compound",
            "Both bromide and iodide are Group 7 ions carrying 1-, so one K+ "
            "balances one of either",
            "The larger iodide ion needs two potassium ions, but the formula "
            "is simplified to 1:1",
        ],
        "correct_index": 2,
        "why": "The ratio is fixed by charge, not size, and every Group 7 ion "
               "carries the same 1- charge.",
    },
    {
        "id": "ks4-ionic-bonding-h03",
        "subtopic_slug": "ionic-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a dot-and-cross diagram for magnesium chloride "
                "has to show two chloride ions but only one magnesium ion.",
        "options": [
            "Chlorine atoms always come in pairs, so two are drawn whatever "
            "metal they react with",
            "Magnesium loses two electrons and each chlorine can accept only "
            "one, so two chlorine atoms are needed",
            "Magnesium loses one electron to each chlorine atom, so it ends "
            "up with a 1+ charge",
            "Each chlorine gains two electrons, so the diagram shows two "
            "chloride ions that each carry a 2- charge in the compound",
        ],
        "correct_index": 1,
        "why": "Both of magnesium's outer electrons have to go somewhere, and "
               "one chlorine atom can take only one of them.",
    },
    {
        "id": "ks4-ionic-bonding-h04",
        "subtopic_slug": "ionic-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium and magnesium both react with oxygen. Compare the "
                "number of electrons each metal atom loses and deduce the "
                "formula of each oxide.",
        "options": [
            "Both lose two electrons per atom, so both oxides have the "
            "formula MO",
            "Sodium loses two electrons and magnesium loses one, giving the "
            "formulas NaO and Mg2O in turn",
            "Both lose one electron per atom, giving the formulas Na2O and "
            "Mg2O",
            "Sodium loses one, so Na2O; magnesium loses two, so MgO balances "
            "with a single oxide ion",
        ],
        "correct_index": 3,
        "why": "One O2- needs 2+ of positive charge: two Na+ ions supply it, "
               "but a single Mg2+ ion does so on its own.",
    },

    # ── ionic-compounds ───────────────────────────────────────────────────
    {
        "id": "ks4-ionic-compounds-e01",
        "subtopic_slug": "ionic-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many chloride ions surround each sodium ion in a "
                "sodium chloride lattice.",
        "options": [
            "1 chloride ion",
            "2 chloride ions",
            "4 chloride ions",
            "6 chloride ions",
        ],
        "correct_index": 3,
        "why": "In the sodium chloride lattice every Na+ is surrounded by six "
               "Cl- ions, and every Cl- by six Na+ ions.",
    },
    {
        "id": "ks4-ionic-compounds-e02",
        "subtopic_slug": "ionic-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the term used for a substance that conducts electricity "
                "when molten or dissolved because it contains mobile ions.",
        "options": [
            "A conductor",
            "An electrolyte",
            "An alloy",
            "A precipitate",
        ],
        "correct_index": 1,
        "why": "An electrolyte conducts because its ions are free to move and "
               "carry charge once it is molten or in solution.",
    },
    {
        "id": "ks4-ionic-compounds-e03",
        "subtopic_slug": "ionic-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is seen when a solution of silver nitrate is "
                "mixed with a solution of sodium chloride.",
        "options": [
            "Both solutions stay clear, because all ionic compounds dissolve",
            "A grey metal forms as silver is displaced from its solution",
            "A white precipitate of silver chloride forms, because it is "
            "insoluble",
            "A gas is released as the chloride ions escape from the solution",
        ],
        "correct_index": 2,
        "why": "Ag+ and Cl- ions meet and form silver chloride, whose lattice "
               "is too strongly held for water to dissolve it.",
    },
    {
        "id": "ks4-ionic-compounds-e04",
        "subtopic_slug": "ionic-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what the word 'giant' means in the phrase 'giant "
                "ionic lattice'.",
        "options": [
            "The structure contains an enormous number of ions repeating in a "
            "regular pattern",
            "Each ion in the structure is unusually large compared with an "
            "ordinary atom",
            "The crystal must be big enough to be seen without a microscope",
            "The compound is built from elements with large relative atomic "
            "masses",
        ],
        "correct_index": 0,
        "why": "'Giant' describes the number of particles, not their size — "
               "the pattern repeats through billions of ions.",
    },
    {
        "id": "ks4-ionic-compounds-s01",
        "subtopic_slug": "ionic-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crystal of sodium chloride splits cleanly along a flat "
                "face when it is struck sharply. Explain why.",
        "options": [
            "The blow melts a thin layer of the crystal, which separates as "
            "it cools again",
            "The covalent bonds running along one plane of the crystal are "
            "weaker than those elsewhere, so it splits there first",
            "A whole layer of ions shifts, bringing like charges together, "
            "and the repulsion splits the crystal along that plane",
            "The delocalised electrons are knocked out of one layer, leaving "
            "nothing to hold it in place",
        ],
        "correct_index": 2,
        "why": "Shifting a layer by one ion lines up like charges, and their "
               "repulsion breaks the crystal apart along that plane.",
    },
    {
        "id": "ks4-ionic-compounds-s02",
        "subtopic_slug": "ionic-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Molten lithium chloride is electrolysed. State which "
                "particles move towards the negative electrode, and explain "
                "why.",
        "options": [
            "The Li+ ions, because they are positive and are attracted to the "
            "negative electrode",
            "The Cl- ions, because negative ions always travel to the "
            "negative electrode",
            "Delocalised electrons, because they carry the charge in any "
            "molten substance",
            "Both ions equally, because an electrode attracts every charged "
            "particle near it",
        ],
        "correct_index": 0,
        "why": "Opposite charges attract, so the positive lithium ions are "
               "pulled towards the negative electrode.",
    },
    {
        "id": "ks4-ionic-compounds-s03",
        "subtopic_slug": "ionic-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium chloride is a solid at room temperature but hydrogen "
                "chloride is a gas, although both contain chlorine. Explain "
                "the difference.",
        "options": [
            "Hydrogen chloride has much weaker covalent bonds than the bonds "
            "inside sodium chloride, so far less energy is needed to break "
            "them apart when it is warmed",
            "Sodium chloride is a giant ionic lattice with strong forces "
            "between its ions, while hydrogen chloride is small molecules "
            "with weak forces between them",
            "Sodium chloride contains chlorine ions and hydrogen chloride "
            "contains chlorine atoms, and atoms are always gases",
            "Hydrogen chloride is lighter, and lighter substances are always "
            "gases at room temperature",
        ],
        "correct_index": 1,
        "why": "It is the structure, not the element present, that decides "
               "the state: a giant lattice needs far more energy to break up.",
    },
    {
        "id": "ks4-ionic-compounds-s04",
        "subtopic_slug": "ionic-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lead bromide must be melted before it will conduct "
                "electricity in an electrolysis experiment. Explain why.",
        "options": [
            "Melting raises the temperature so that the ions react faster at "
            "the electrodes",
            "Melting turns the ions into atoms, and only atoms can carry a "
            "current",
            "Melting creates the ions in the first place, because solid lead "
            "bromide contains only neutral lead and bromine atoms",
            "In the solid the ions are held in fixed positions and cannot "
            "move, so no charge can flow until it melts",
        ],
        "correct_index": 3,
        "why": "A current is moving charge, and the ions can only move once "
               "the lattice has been broken up by melting.",
    },
    {
        "id": "ks4-ionic-compounds-h01",
        "subtopic_slug": "ionic-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium chloride dissolves readily in water but not in "
                "hexane, a non-polar solvent. Suggest why.",
        "options": [
            "Hexane molecules are too large to fit between the closely packed "
            "ions of the lattice and pull them away from it one by one",
            "Water molecules are polar, so they attract the ions and pull "
            "them out of the lattice; hexane molecules cannot",
            "Water reacts chemically with sodium chloride to make new soluble "
            "compounds",
            "Hexane is a liquid, and ionic compounds dissolve only in solids",
        ],
        "correct_index": 1,
        "why": "Dissolving needs the solvent to attract the ions strongly "
               "enough to overcome the lattice, and only polar water does.",
    },
    {
        "id": "ks4-ionic-compounds-h02",
        "subtopic_slug": "ionic-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crystal of aluminium oxide, Al2O3, contains 2000 aluminium "
                "ions. Calculate the total number of ions in the crystal.",
        "options": [
            "4000 ions",
            "3000 ions",
            "6000 ions",
            "5000 ions",
        ],
        "correct_index": 3,
        "why": "The formula fixes a 2:3 ratio, so 2000 Al3+ ions come with "
               "3000 O2- ions — 5000 ions altogether.",
    },
    {
        "id": "ks4-ionic-compounds-h03",
        "subtopic_slug": "ionic-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Molten sodium chloride conducts electricity but molten "
                "candle wax does not. Explain the difference.",
        "options": [
            "The molten ionic compound has free ions that carry charge, while "
            "molten wax contains only uncharged molecules",
            "The molten ionic compound has free electrons, while molten wax "
            "has none at all that could carry a charge through it",
            "Wax molecules are too large to move, so they cannot carry the "
            "current through the liquid",
            "Wax has to be heated much hotter before its own ions are "
            "released",
        ],
        "correct_index": 0,
        "why": "Conduction needs mobile charged particles; wax melts into "
               "neutral molecules, so nothing carries the charge.",
    },
    {
        "id": "ks4-ionic-compounds-h04",
        "subtopic_slug": "ionic-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Salt solution conducts electricity well, but pure water "
                "conducts very poorly. Explain what this shows about which "
                "particles carry the charge.",
        "options": [
            "The water molecules themselves carry the charge once salt has "
            "been added to them",
            "The salt makes the water warmer, and warm water conducts "
            "electricity well",
            "The charge is carried by the Na+ and Cl- ions released from the "
            "lattice, not by the water",
            "The charge is carried by electrons released from sodium atoms as "
            "the salt dissolves",
        ],
        "correct_index": 2,
        "why": "Adding the salt is the only change, so the ions it releases "
               "must be what carries the current.",
    },

    # ── covalent-bonding ──────────────────────────────────────────────────
    {
        "id": "ks4-covalent-bonding-e01",
        "subtopic_slug": "covalent-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrogen chloride, HCl, is a covalent molecule. State the "
                "number of covalent bonds between its two atoms.",
        "options": [
            "1 covalent bond",
            "2 covalent bonds",
            "3 covalent bonds",
            "4 covalent bonds",
        ],
        "correct_index": 0,
        "why": "Hydrogen needs one more electron and chlorine needs one more, "
               "so a single shared pair completes both shells.",
    },
    {
        "id": "ks4-covalent-bonding-e02",
        "subtopic_slug": "covalent-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Silicon is in Group 4, like carbon. State the number of "
                "covalent bonds a silicon atom forms in silane, SiH4.",
        "options": [
            "1 covalent bond",
            "2 covalent bonds",
            "4 covalent bonds",
            "6 covalent bonds",
        ],
        "correct_index": 2,
        "why": "Silicon has four outer electrons and needs four more, so it "
               "forms four shared pairs.",
    },
    {
        "id": "ks4-covalent-bonding-e03",
        "subtopic_slug": "covalent-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrogen peroxide has the structure H-O-O-H. State the total "
                "number of covalent bonds in one molecule.",
        "options": [
            "2 covalent bonds",
            "3 covalent bonds",
            "4 covalent bonds",
            "5 covalent bonds",
        ],
        "correct_index": 1,
        "why": "Each dash is one shared pair: two O-H bonds plus the O-O bond "
               "makes three.",
    },
    {
        "id": "ks4-covalent-bonding-e04",
        "subtopic_slug": "covalent-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why neon exists as single atoms rather than as Ne2 "
                "molecules.",
        "options": [
            "Neon atoms repel one another too strongly to join together",
            "Neon is a metal, so it forms a giant lattice instead of separate "
            "small molecules",
            "Neon atoms have only two outer electrons, too few to share",
            "Neon already has a full outer shell, so it has no need to share "
            "electrons",
        ],
        "correct_index": 3,
        "why": "Atoms bond to reach a full outer shell, and neon's is already "
               "full, so it gains nothing by bonding.",
    },
    {
        "id": "ks4-covalent-bonding-s01",
        "subtopic_slug": "covalent-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethene has the formula C2H4, and every carbon atom forms "
                "four bonds. Deduce the type of bond joining the two carbon "
                "atoms.",
        "options": [
            "A single bond, with each carbon's remaining electrons left "
            "unused",
            "A double bond, because each carbon uses only two of its four "
            "bonds for hydrogen atoms",
            "A triple bond, because carbon has four outer electrons and each "
            "hydrogen has only one to offer",
            "An ionic bond, because the two carbon atoms transfer electrons "
            "between them",
        ],
        "correct_index": 1,
        "why": "Each carbon bonds to two hydrogens, so its other two bonds "
               "must both go to the other carbon — a double bond.",
    },
    {
        "id": "ks4-covalent-bonding-s02",
        "subtopic_slug": "covalent-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why methane contains four covalent bonds rather than "
                "four ionic bonds.",
        "options": [
            "Carbon is a metal, so it would have to transfer electrons to "
            "form an ionic bond",
            "Hydrogen has only one electron, so it cannot form ions of any "
            "kind",
            "Ionic bonds form only between atoms of the same element, so they "
            "cannot form between carbon and hydrogen",
            "Both carbon and hydrogen are non-metals, so neither transfers "
            "electrons and they share instead",
        ],
        "correct_index": 3,
        "why": "Two non-metals have no metal to donate electrons, so full "
               "shells can only be reached by sharing pairs.",
    },
    {
        "id": "ks4-covalent-bonding-s03",
        "subtopic_slug": "covalent-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A molecule of sulfur dioxide, SO2, contains two double "
                "bonds. Determine the total number of electrons shared in the "
                "molecule.",
        "options": [
            "4 electrons",
            "6 electrons",
            "8 electrons",
            "12 electrons",
        ],
        "correct_index": 2,
        "why": "Each double bond is two shared pairs, so it holds four "
               "electrons — two double bonds share eight in all.",
    },
    {
        "id": "ks4-covalent-bonding-s04",
        "subtopic_slug": "covalent-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student's dot-and-cross diagram of ammonia shows the "
                "nitrogen atom with only six electrons in its outer shell. "
                "Explain what has gone wrong.",
        "options": [
            "Nitrogen should end with eight outer electrons, so one bonding "
            "pair has been left out",
            "Nitrogen should end with six outer electrons, so the diagram is "
            "correct as drawn",
            "Nitrogen should end with two outer electrons, so two pairs have "
            "been added by mistake",
            "Nitrogen transfers its electrons in ammonia, so it should have "
            "been drawn as an ion",
        ],
        "correct_index": 0,
        "why": "Every atom in a correct dot-and-cross diagram ends with a "
               "full outer shell, and nitrogen's needs eight.",
    },
    {
        "id": "ks4-covalent-bonding-h01",
        "subtopic_slug": "covalent-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Nitrogen gas is very unreactive. Explain why, in terms of "
                "the bonding in an N2 molecule.",
        "options": [
            "Nitrogen molecules are too small to collide with other molecules",
            "Nitrogen atoms have a full outer shell before they bond, so the "
            "molecule has no need to react with anything else",
            "The two atoms are joined by a triple bond of three shared pairs, "
            "which takes a great deal of energy to break",
            "The weak forces between nitrogen molecules stop them reaching "
            "other substances",
        ],
        "correct_index": 2,
        "why": "Three shared pairs must be broken before nitrogen can react, "
               "and that needs a very large amount of energy.",
    },
    {
        "id": "ks4-covalent-bonding-h02",
        "subtopic_slug": "covalent-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of covalent bonds formed by an atom of "
                "carbon, nitrogen, oxygen and fluorine, and explain the "
                "pattern.",
        "options": [
            "4, 3, 2 and 1 - each forms one bond for every electron it still "
            "needs to fill its outer shell",
            "1, 2, 3 and 4 - each forms one bond for every outer electron it "
            "already has",
            "4, 5, 6 and 7 - each forms one bond for every electron in its "
            "outer shell",
            "All four form four bonds, because every atom needs eight "
            "electrons in its outer shell to become stable",
        ],
        "correct_index": 0,
        "why": "An atom forms one bond per electron short of a full shell, so "
               "the number falls by one across the period.",
    },
    {
        "id": "ks4-covalent-bonding-h03",
        "subtopic_slug": "covalent-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Silicon (Group 4) reacts with chlorine (Group 7). Deduce the "
                "formula of the compound formed and justify it in terms of "
                "shared pairs.",
        "options": [
            "SiCl2, because silicon needs only two more electrons in order to "
            "fill up its outer shell completely",
            "Si2Cl, because two silicon atoms share one chlorine atom between "
            "them",
            "SiCl, because a single shared pair is enough to join the two "
            "atoms together",
            "SiCl4, because silicon needs four more electrons and each "
            "chlorine can share only one",
        ],
        "correct_index": 3,
        "why": "Silicon needs four shared pairs and each chlorine can supply "
               "just one, so four chlorine atoms are required.",
    },
    {
        "id": "ks4-covalent-bonding-h04",
        "subtopic_slug": "covalent-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student states: 'A covalent bond forms because the two "
                "nuclei attract each other.' Evaluate this statement.",
        "options": [
            "It is correct: the two positive nuclei attract each other across "
            "the bond, and that attraction holds the molecule together",
            "It is wrong: the nuclei repel each other, and the bond is their "
            "shared attraction to the electron pair between them",
            "It is wrong: nuclei carry no charge, so they neither attract nor "
            "repel one another",
            "It is correct: the bond is the attraction between the nuclei and "
            "the electrons they transferred",
        ],
        "correct_index": 1,
        "why": "Both nuclei are positive and repel; what holds them together "
               "is their attraction to the shared pair sitting between them.",
    },

    # ── metallic-bonding ──────────────────────────────────────────────────
    {
        "id": "ks4-metallic-bonding-e01",
        "subtopic_slug": "metallic-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the charge on the metal particles held in a metallic "
                "lattice.",
        "options": [
            "Negative, because they have gained the delocalised electrons",
            "Neutral, because metal atoms do not lose any electrons",
            "Positive, because each atom has released its outer electrons",
            "Positive and negative in equal numbers, as in an ionic lattice",
        ],
        "correct_index": 2,
        "why": "Losing negative electrons leaves each metal atom as a "
               "positive ion in the lattice.",
    },
    {
        "id": "ks4-metallic-bonding-e02",
        "subtopic_slug": "metallic-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the outer electrons of a metal atom "
                "when a metallic lattice forms.",
        "options": [
            "They are transferred permanently to a neighbouring metal atom",
            "They are shared in pairs between neighbouring metal atoms",
            "They stay in their own shells but vibrate more quickly than they "
            "did before bonding",
            "They leave their atoms and become free to move throughout the "
            "whole structure",
        ],
        "correct_index": 3,
        "why": "The outer electrons become delocalised — they belong to the "
               "whole lattice rather than to any one atom.",
    },
    {
        "id": "ks4-metallic-bonding-e03",
        "subtopic_slug": "metallic-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the alloy made from copper and zinc.",
        "options": [
            "Brass",
            "Bronze",
            "Steel",
            "Stainless steel",
        ],
        "correct_index": 0,
        "why": "Brass is copper alloyed with zinc; bronze is the copper-tin "
               "alloy it is most often confused with.",
    },
    {
        "id": "ks4-metallic-bonding-e04",
        "subtopic_slug": "metallic-bonding",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the pair of properties that nearly all metals share.",
        "options": [
            "A high melting point and shattering when they are struck",
            "A high melting point and good electrical conductivity",
            "A low density and poor thermal conductivity",
            "Brittleness and good electrical conductivity",
        ],
        "correct_index": 1,
        "why": "Strong attraction to the electron sea gives a high melting "
               "point, and the mobile electrons give good conductivity.",
    },
    {
        "id": "ks4-metallic-bonding-s01",
        "subtopic_slug": "metallic-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mercury is a liquid at room temperature, unlike most metals. "
                "Suggest what this shows about its metallic bonding.",
        "options": [
            "The attraction between its ions and the electron sea is weaker "
            "than in most metals, so less energy separates them",
            "Mercury has no metallic bonding at all, which is why it flows "
            "like a liquid",
            "Mercury's atoms are joined by weak covalent bonds rather than "
            "metallic bonds, so its particles separate at room temperature",
            "Mercury's delocalised electrons have escaped, leaving its ions "
            "free to move",
        ],
        "correct_index": 0,
        "why": "A low melting point means less energy is needed to overcome "
               "the attraction between the ions and the electron sea.",
    },
    {
        "id": "ks4-metallic-bonding-s02",
        "subtopic_slug": "metallic-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium is soft and melts at 98 °C, while iron is hard and "
                "melts at 1538 °C. Suggest, in terms of the electron sea, why "
                "sodium's metallic bonding is weaker.",
        "options": [
            "Sodium has no delocalised electrons at all, so there is nothing "
            "holding its positive ions together in the lattice",
            "Each sodium atom releases only one electron, so the attraction "
            "between its ions and the electron sea is weaker",
            "Sodium is held together by weak intermolecular forces rather "
            "than by metallic bonds",
            "Sodium's ions are larger, so they are held by covalent bonds "
            "instead",
        ],
        "correct_index": 1,
        "why": "Fewer delocalised electrons and a smaller ionic charge mean a "
               "weaker electrostatic attraction holding the lattice together.",
    },
    {
        "id": "ks4-metallic-bonding-s03",
        "subtopic_slug": "metallic-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the metallic bond is described as an "
                "electrostatic attraction, even though a metal contains no "
                "negative ions.",
        "options": [
            "There are negative ions present; they are simply too small to "
            "show in the model",
            "The attraction acts between neighbouring metal atoms, which "
            "become slightly charged when they are packed closely together",
            "The attraction acts between the delocalised electrons themselves",
            "The attraction acts between the positive metal ions and the "
            "negatively charged sea of delocalised electrons",
        ],
        "correct_index": 3,
        "why": "The electron sea is negatively charged, so the ions are held "
               "by electrostatic attraction to it rather than to each other.",
    },
    {
        "id": "ks4-metallic-bonding-s04",
        "subtopic_slug": "metallic-bonding",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what actually moves through a copper wire when it "
                "carries an electric current.",
        "options": [
            "The positive copper ions drift along the wire to the negative "
            "terminal",
            "Whole copper atoms move through the wire, carrying their "
            "electrons with them",
            "The delocalised electrons drift through the lattice while the "
            "positive ions stay in place",
            "Nothing moves at all; the current is passed on by the ions "
            "vibrating against one another in place",
        ],
        "correct_index": 2,
        "why": "Only the delocalised electrons are free to move; the lattice "
               "of positive ions stays where it is.",
    },
    {
        "id": "ks4-metallic-bonding-h01",
        "subtopic_slug": "metallic-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict how hard an alloy would be if the atoms added to the "
                "pure metal were exactly the same size as the metal's own "
                "atoms, and explain your prediction.",
        "options": [
            "It would be much harder, because adding any second element "
            "always blocks the layers of ions from sliding past each other",
            "It would stay about as soft as the pure metal, because the "
            "layers would still be regular and able to slide",
            "It would melt at a far lower temperature, because the lattice "
            "would still be disrupted",
            "It would stop conducting electricity, because the electron sea "
            "would be broken up",
        ],
        "correct_index": 1,
        "why": "Alloys are hard because different-sized atoms distort the "
               "layers; same-sized atoms leave the layers free to slide.",
    },
    {
        "id": "ks4-metallic-bonding-h02",
        "subtopic_slug": "metallic-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Tungsten melts at 3422 °C and sodium at 98 °C, although both "
                "have metallic bonding. Deduce what this difference shows.",
        "options": [
            "Tungsten's atoms are held by covalent bonds while sodium's are "
            "held by metallic bonds",
            "Sodium has more delocalised electrons than tungsten does, which "
            "weakens the attraction within its lattice",
            "Tungsten's positive ions and electron sea attract far more "
            "strongly, so much more energy is needed",
            "Tungsten is a mixture rather than a pure metal, so it melts over "
            "a much higher range",
        ],
        "correct_index": 2,
        "why": "Melting point measures how much energy is needed to overcome "
               "the ion-to-electron-sea attraction, so tungsten's is "
               "stronger.",
    },
    {
        "id": "ks4-metallic-bonding-h03",
        "subtopic_slug": "metallic-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says a metal conducts electricity because its "
                "positive ions move towards the negative terminal. Evaluate "
                "this statement.",
        "options": [
            "It is wrong: the positive ions stay in fixed positions and it is "
            "the delocalised electrons that move",
            "It is correct: positive ions carry the current in any conducting "
            "solid",
            "It is partly correct: the ions move, but only once the metal has "
            "been melted",
            "It is wrong: neither ions nor electrons move, and the current "
            "passes as vibrations through the lattice",
        ],
        "correct_index": 0,
        "why": "The lattice of ions is fixed; the current is the drift of the "
               "delocalised electrons through it.",
    },
    {
        "id": "ks4-metallic-bonding-h04",
        "subtopic_slug": "metallic-bonding",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an alloy is classed as a mixture rather than a "
                "compound, and why its properties still differ from the pure "
                "metal's.",
        "options": [
            "It is a compound, because the two metals are chemically bonded "
            "to each other in a fixed whole-number ratio, as in any compound",
            "It is a mixture, and mixing therefore has no effect on the "
            "properties of either metal",
            "It is a compound, because a new lattice with new properties has "
            "been formed",
            "It is a mixture, because the atoms are not chemically combined, "
            "but their different sizes stop the layers sliding",
        ],
        "correct_index": 3,
        "why": "No new compound forms — the added atoms simply sit in the "
               "same lattice and distort the layers, so it is harder.",
    },

    # ── states-of-matter ──────────────────────────────────────────────────
    {
        "id": "ks4-states-of-matter-e01",
        "subtopic_slug": "states-of-matter",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Solid carbon dioxide turns directly into a gas when it "
                "warms. Name this change of state.",
        "options": [
            "Evaporation",
            "Sublimation",
            "Condensation",
            "Melting",
        ],
        "correct_index": 1,
        "why": "Sublimation is the change straight from solid to gas, with no "
               "liquid stage in between.",
    },
    {
        "id": "ks4-states-of-matter-e02",
        "subtopic_slug": "states-of-matter",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the equation CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l) + "
                "CO2(g), state which product is a gas.",
        "options": [
            "Carbon dioxide, CO2",
            "Water, H2O",
            "Calcium chloride, CaCl2",
            "Hydrochloric acid, HCl",
        ],
        "correct_index": 0,
        "why": "The state symbol (g) marks carbon dioxide as the gas; (aq) "
               "means dissolved in water and (l) means a pure liquid.",
    },
    {
        "id": "ks4-states-of-matter-e03",
        "subtopic_slug": "states-of-matter",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which state of matter has a definite volume but no "
                "definite shape.",
        "options": [
            "A solid",
            "A gas",
            "A liquid",
            "Any substance that has been dissolved",
        ],
        "correct_index": 2,
        "why": "A liquid's particles touch, fixing its volume, but they can "
               "flow past one another, so it takes the container's shape.",
    },
    {
        "id": "ks4-states-of-matter-e04",
        "subtopic_slug": "states-of-matter",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process in which a liquid turns into a gas from its "
                "surface, below its boiling point.",
        "options": [
            "Boiling",
            "Sublimation",
            "Condensation",
            "Evaporation",
        ],
        "correct_index": 3,
        "why": "Evaporation happens at the surface at any temperature, while "
               "boiling happens throughout the liquid at one temperature.",
    },
    {
        "id": "ks4-states-of-matter-s01",
        "subtopic_slug": "states-of-matter",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water melts at 0 °C and boils at 100 °C. Predict its state, "
                "with the state symbol, at 150 °C and at -20 °C.",
        "options": [
            "Liquid (l) at 150 °C and liquid (l) at -20 °C",
            "Gas (g) at 150 °C and liquid (l) at -20 °C",
            "Solid (s) at 150 °C and gas (g) at -20 °C",
            "Gas (g) at 150 °C and solid (s) at -20 °C",
        ],
        "correct_index": 3,
        "why": "Above the boiling point a substance is a gas; below the "
               "melting point it is a solid.",
    },
    {
        "id": "ks4-states-of-matter-s02",
        "subtopic_slug": "states-of-matter",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a liquid takes the shape of its container but a "
                "solid keeps its own shape.",
        "options": [
            "A liquid's particles are further apart than a gas's, so they "
            "spread out to fill all the space available",
            "A liquid's particles have no forces between them, so each one "
            "moves independently",
            "A liquid's particles can move past one another, while a solid's "
            "only vibrate about fixed positions",
            "A liquid's particles are smaller than a solid's, so they flow "
            "into the gaps",
        ],
        "correct_index": 2,
        "why": "Shape depends on whether the particles can change places, and "
               "only a liquid's can while still touching.",
    },
    {
        "id": "ks4-states-of-matter-s03",
        "subtopic_slug": "states-of-matter",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the equation NaCl(s) -> Na+(aq) + Cl-(aq), explain what "
                "the change from (s) to (aq) tells you has happened.",
        "options": [
            "The solid has reacted with the water to make two new compounds, "
            "one for each of the ions shown",
            "The lattice has separated into individual ions, each surrounded "
            "by water molecules",
            "The solid has melted, so its ions are now in the liquid state",
            "The ions have broken down into neutral sodium and chlorine atoms",
        ],
        "correct_index": 1,
        "why": "(aq) means dissolved in water: the ions have been pulled out "
               "of the lattice and are surrounded by water molecules.",
    },
    {
        "id": "ks4-states-of-matter-s04",
        "subtopic_slug": "states-of-matter",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that boiling a kettle makes a new substance, "
                "because steam looks different from water. Explain why the "
                "student is wrong.",
        "options": [
            "Boiling is a physical change: the steam is still H2O and only "
            "the spacing and movement of the particles has changed",
            "Boiling is a chemical change, because a gas has been produced "
            "from a liquid",
            "Boiling is a chemical change, because the strong covalent bonds "
            "inside the water molecules are broken as it turns to steam",
            "Boiling splits water into hydrogen and oxygen, which then join "
            "again to form steam",
        ],
        "correct_index": 0,
        "why": "No new substance is made in a change of state — ice, water "
               "and steam are all H2O.",
    },
    {
        "id": "ks4-states-of-matter-h01",
        "subtopic_slug": "states-of-matter",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iron melts at 1538 °C and oxygen boils at -183 °C. Deduce "
                "which substance has the stronger forces between its "
                "particles, and explain how you know.",
        "options": [
            "Iron, because far more energy must be supplied before its "
            "particles separate",
            "Oxygen, because gases have the strongest forces between their "
            "particles",
            "Iron, because its particles are heavier, and heavier particles "
            "always attract more strongly",
            "They are the same, because both substances are pure elements",
        ],
        "correct_index": 0,
        "why": "The temperature needed for a change of state measures how "
               "much energy the forces between the particles demand.",
    },
    {
        "id": "ks4-states-of-matter-h02",
        "subtopic_slug": "states-of-matter",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pure substance is cooled steadily from a gas to a solid. "
                "Predict how many flat sections its temperature-time graph "
                "would show, and explain what happens during each.",
        "options": [
            "One flat section, because cooling only involves freezing",
            "Three flat sections, one for each of the three states the "
            "substance passes through as it cools from a gas to a solid",
            "None, because flat sections appear only when a substance is "
            "being heated",
            "Two flat sections - condensing and freezing - where energy is "
            "released but the temperature stays the same",
        ],
        "correct_index": 3,
        "why": "Each change of state holds the temperature steady, and "
               "cooling from gas to solid passes through two of them.",
    },
    {
        "id": "ks4-states-of-matter-h03",
        "subtopic_slug": "states-of-matter",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The particle model shows particles as solid spheres. Suggest "
                "why it still predicts correctly that a gas can be "
                "compressed.",
        "options": [
            "Because it shows gas particles as larger than solid particles, "
            "and large particles squash easily",
            "Because it shows gas particles as having no mass, so they take "
            "up no space at all",
            "Because it correctly shows large spaces between gas particles, "
            "and it is those spaces that close up",
            "Because it shows the particles as soft spheres that can be "
            "squashed to a smaller size",
        ],
        "correct_index": 2,
        "why": "Compression closes the gaps between particles, and the model "
               "gets those gaps right even though the spheres are simplified.",
    },
    {
        "id": "ks4-states-of-matter-h04",
        "subtopic_slug": "states-of-matter",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a boiling point can be used to identify a "
                "substance only if that substance is pure.",
        "options": [
            "A pure substance boils over a wide range, and that range is "
            "characteristic of it",
            "A pure substance boils at one fixed temperature, whereas a "
            "mixture boils over a range",
            "A mixture boils at one fixed temperature, so a range shows that "
            "the substance is pure",
            "Boiling point depends only on the pressure, so it identifies "
            "nothing at all",
        ],
        "correct_index": 1,
        "why": "Only a pure substance has a single sharp boiling point that "
               "can be compared with a known value.",
    },

    # ── properties-ionic-compounds ────────────────────────────────────────
    {
        "id": "ks4-properties-ionic-compounds-e01",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the electrostatic forces in an ionic "
                "lattice as the charges on the ions increase.",
        "options": [
            "They become weaker, because the ions repel each other more",
            "They stay the same, because charge does not affect attraction",
            "They disappear once the charge is greater than 1",
            "They become stronger, so more energy is needed to separate the "
            "ions",
        ],
        "correct_index": 3,
        "why": "The attraction depends on the charges, so bigger charges pull "
               "the ions together more strongly.",
    },
    {
        "id": "ks4-properties-ionic-compounds-e02",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether a solution of potassium nitrate in water "
                "conducts electricity, and give the reason.",
        "options": [
            "No, because the ions are destroyed when the compound dissolves",
            "No, because the water molecules block the ions from moving",
            "Yes, because the ions become free to move through the solution",
            "Yes, because the water releases delocalised electrons",
        ],
        "correct_index": 2,
        "why": "Dissolving frees the ions from the lattice, and moving "
               "charged particles are what carry a current.",
    },
    {
        "id": "ks4-properties-ionic-compounds-e03",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the particles that carry the charge through molten "
                "aluminium oxide.",
        "options": [
            "Delocalised electrons released by the aluminium",
            "Ions, which move through the liquid",
            "Neutral atoms of aluminium and oxygen",
            "Whole molecules of aluminium oxide",
        ],
        "correct_index": 1,
        "why": "An ionic compound has no free electrons; its charge is "
               "carried by the ions themselves once they can move.",
    },
    {
        "id": "ks4-properties-ionic-compounds-e04",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by describing an ionic compound as "
                "brittle.",
        "options": [
            "It shatters or cracks when a force is applied, instead of "
            "bending",
            "It bends easily into a new shape without breaking or cracking "
            "apart",
            "It melts at a low temperature when it is heated gently",
            "It dissolves quickly when it is placed into water",
        ],
        "correct_index": 0,
        "why": "Brittle means it breaks rather than bends — the lattice "
               "cannot shift without like charges meeting and repelling.",
    },
    {
        "id": "ks4-properties-ionic-compounds-s01",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calcium oxide can be heated in a kiln to 1400 °C without "
                "melting, but sodium chloride cannot. Suggest why, using the "
                "charges on their ions.",
        "options": [
            "Calcium oxide contains covalent bonds, which are much stronger "
            "than the ionic bonds in sodium chloride and need more energy to "
            "break",
            "Calcium oxide has 2+ and 2- ions, so its electrostatic forces "
            "are far stronger than in sodium chloride, which melts at 801 °C",
            "Sodium chloride has larger ions, so its lattice collapses at a "
            "lower temperature",
            "Calcium oxide is a mixture, so it has no single melting point to "
            "reach",
        ],
        "correct_index": 1,
        "why": "Doubling both charges makes the attraction much stronger, so "
               "calcium oxide's melting point is far above 1400 °C.",
    },
    {
        "id": "ks4-properties-ionic-compounds-s02",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a solution of an ionic compound can be used as "
                "an electrolyte but a sugar solution cannot.",
        "options": [
            "The ionic compound releases ions that move and carry charge, "
            "while sugar dissolves as uncharged molecules",
            "The ionic compound releases electrons that flow through the "
            "solution, while sugar releases none of its own",
            "Sugar solution does conduct, but far too slowly to be measured "
            "in a lesson",
            "Sugar molecules are too heavy to move, so no current can pass "
            "through them",
        ],
        "correct_index": 0,
        "why": "Conduction needs mobile charged particles, and sugar "
               "dissolves into neutral molecules rather than ions.",
    },
    {
        "id": "ks4-properties-ionic-compounds-s03",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how an ionic compound can be described as hard, "
                "given that a sharp blow will shatter it.",
        "options": [
            "It is not really hard; it only seems hard because the crystal is "
            "large",
            "Its covalent bonds resist scratching, but they snap suddenly "
            "when the crystal is struck, so it splits cleanly instead of "
            "bending",
            "Many strong attractions act in all directions and resist "
            "scratching, but a blow that shifts a layer lines up like "
            "charges, which repel",
            "The delocalised electrons make it hard, but they are knocked out "
            "when it is struck",
        ],
        "correct_index": 2,
        "why": "Hardness comes from the many strong attractions; brittleness "
               "comes from what happens when a whole layer is displaced.",
    },
    {
        "id": "ks4-properties-ionic-compounds-s04",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A great deal of energy is released when magnesium oxide "
                "forms from its elements. Suggest what this shows about the "
                "compound.",
        "options": [
            "It shows magnesium oxide is less stable than the separate "
            "elements, which is why the energy escapes from it",
            "It shows the energy was stored in the magnesium metal and has "
            "simply been passed on",
            "It shows the ionic bonds in magnesium oxide are weak, since "
            "energy leaves the compound",
            "It shows magnesium oxide is more stable, because energy is "
            "released as its strong ionic attractions form",
        ],
        "correct_index": 3,
        "why": "Energy released on forming strong 2+/2- attractions leaves "
               "the compound at a lower, more stable energy than the "
               "elements.",
    },
    {
        "id": "ks4-properties-ionic-compounds-h01",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In school electrolysis experiments sodium chloride is "
                "usually dissolved rather than melted. Suggest why.",
        "options": [
            "Dissolved sodium chloride conducts far better than molten sodium "
            "chloride does, at any temperature you choose",
            "Melting destroys the ions, so no current could pass through the "
            "molten compound",
            "Dissolving frees the ions at room temperature, whereas melting "
            "would need a temperature above 800 °C",
            "Solid sodium chloride already conducts, so neither step is "
            "really necessary",
        ],
        "correct_index": 2,
        "why": "Both routes free the ions, but only dissolving does it at a "
               "temperature a school laboratory can reach.",
    },
    {
        "id": "ks4-properties-ionic-compounds-h02",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the charges on its ions help you predict which "
                "of two ionic compounds melts at the higher temperature, "
                "while the formula on its own does not.",
        "options": [
            "The formula gives the melting point directly, once the ions in "
            "it have been counted",
            "The melting point depends on the strength of the attractions, "
            "which the charges show; the formula gives only the ion ratio",
            "The melting point depends only on how many ions the formula "
            "contains, so the compound with the larger formula melts higher "
            "every time",
            "Neither the formula nor the charges give any clue, because "
            "melting points can only be measured",
        ],
        "correct_index": 1,
        "why": "Melting point tracks the strength of the electrostatic "
               "attraction, and that is set by the ionic charges.",
    },
    {
        "id": "ks4-properties-ionic-compounds-h03",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that because molten sodium chloride conducts "
                "electricity, electrons must flow through it just as they do "
                "through a copper wire. Evaluate this statement.",
        "options": [
            "It is correct: every conductor carries current using delocalised "
            "electrons",
            "It is correct, but the electrons come from the chloride ions "
            "rather than from the sodium ions in the melt",
            "It is wrong: the current is carried by heat rather than by any "
            "charged particle",
            "It is wrong: an ionic compound has no delocalised electrons, so "
            "its moving ions carry the charge",
        ],
        "correct_index": 3,
        "why": "Ionic compounds have no free electrons at all; conduction "
               "happens only because the ions themselves can move.",
    },
    {
        "id": "ks4-properties-ionic-compounds-h04",
        "subtopic_slug": "properties-ionic-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium oxide is used as an abrasive for grinding, while "
                "sodium chloride is not. Suggest why, in terms of ionic "
                "charge.",
        "options": [
            "Al3+ and O2- give very strong attractions throughout the "
            "lattice, making it extremely hard",
            "Aluminium oxide is a metal, so its sliding layers of ions grind "
            "other materials away as it is rubbed",
            "Sodium chloride is harder, but it is far too valuable to use as "
            "an abrasive",
            "Aluminium oxide contains covalent bonds, which are always harder "
            "than ionic bonds",
        ],
        "correct_index": 0,
        "why": "High ionic charges make the lattice attractions very strong, "
               "so the solid is hard enough to grind other materials.",
    },

    # ── properties-small-molecules ────────────────────────────────────────
    {
        "id": "ks4-properties-small-molecules-e01",
        "subtopic_slug": "properties-small-molecules",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Chlorine, ammonia and methane are all made of small "
                "molecules. Describe what this structure usually means for a "
                "substance's physical state at room temperature.",
        "options": [
            "Most are gases or liquids at room temperature",
            "Most are hard solids with high melting points",
            "Most are solids that conduct electricity well",
            "Most are liquids that dissolve readily in water",
        ],
        "correct_index": 0,
        "why": "Only weak intermolecular forces hold small molecules to one "
               "another, so most such substances have already melted or "
               "boiled well below room temperature.",
    },
    {
        "id": "ks4-properties-small-molecules-e02",
        "subtopic_slug": "properties-small-molecules",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the weak forces that act between separate molecules.",
        "options": [
            "Covalent bonds",
            "Intermolecular forces",
            "Electrostatic attractions between ions",
            "Metallic bonds",
        ],
        "correct_index": 1,
        "why": "Intermolecular forces act between whole molecules and are far "
               "weaker than the covalent bonds inside them.",
    },
    {
        "id": "ks4-properties-small-molecules-e03",
        "subtopic_slug": "properties-small-molecules",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of atoms in one molecule of ammonia, NH3.",
        "options": [
            "2 atoms",
            "3 atoms",
            "5 atoms",
            "4 atoms",
        ],
        "correct_index": 3,
        "why": "One nitrogen atom and three hydrogen atoms make four atoms in "
               "the molecule.",
    },
    {
        "id": "ks4-properties-small-molecules-e04",
        "subtopic_slug": "properties-small-molecules",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether the covalent bonds inside a carbon dioxide "
                "molecule are strong or weak.",
        "options": [
            "Weak, which is why carbon dioxide is a gas at room temperature",
            "Weak, because the molecule contains only three atoms",
            "Strong, even though carbon dioxide is a gas at room temperature",
            "Strong only while the carbon dioxide is frozen as a solid",
        ],
        "correct_index": 2,
        "why": "Covalent bonds inside a molecule are strong; the low boiling "
               "point comes from the weak forces between molecules.",
    },
    {
        "id": "ks4-properties-small-molecules-s01",
        "subtopic_slug": "properties-small-molecules",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Propane boils at -42 °C and butane, whose molecules are one "
                "carbon atom longer, boils at -1 °C. Explain the difference.",
        "options": [
            "Butane has stronger covalent bonds inside its molecules than "
            "propane does, so more energy is needed to break them apart on "
            "boiling",
            "Propane molecules are heavier, so they escape from the liquid "
            "more slowly",
            "Butane molecules are larger with more electrons, so the forces "
            "between them are stronger and need more energy to overcome",
            "Butane is ionic while propane is covalent, so butane boils at a "
            "higher temperature",
        ],
        "correct_index": 2,
        "why": "Bigger molecules attract each other more strongly, so more "
               "energy is needed to separate them.",
    },
    {
        "id": "ks4-properties-small-molecules-s02",
        "subtopic_slug": "properties-small-molecules",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why carbon dioxide gas does not conduct electricity "
                "but molten sodium chloride does.",
        "options": [
            "Carbon dioxide's covalent bonds trap all of its electrons, while "
            "the bonds in sodium chloride do not at all",
            "Carbon dioxide is a gas, and a gas can never conduct electricity",
            "Carbon dioxide molecules are too light to carry a charge across "
            "the gap",
            "Carbon dioxide is made of uncharged molecules, while molten "
            "sodium chloride has ions free to move",
        ],
        "correct_index": 3,
        "why": "Conduction needs mobile charged particles, and a molecule "
               "carries no overall charge.",
    },
    {
        "id": "ks4-properties-small-molecules-s03",
        "subtopic_slug": "properties-small-molecules",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrogen chloride is a covalent gas, yet its solution in "
                "water conducts electricity. Explain how this is possible.",
        "options": [
            "Dissolving splits the molecules into H+ and Cl- ions, which are "
            "free to move and carry charge",
            "The water adds extra electrons to the molecules, and it is those "
            "electrons that carry the charge",
            "Hydrogen chloride was ionic all along, so the solution simply "
            "releases its ions",
            "The molecules stay whole but line up so that charge can hop "
            "along the chain",
        ],
        "correct_index": 0,
        "why": "Dissolving in water ionises hydrogen chloride, and it is "
               "those new ions that carry the current.",
    },
    {
        "id": "ks4-properties-small-molecules-s04",
        "subtopic_slug": "properties-small-molecules",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two simple molecular substances are compared: A boils at 78 "
                "°C and B at -25 °C. Deduce which has the stronger "
                "intermolecular forces.",
        "options": [
            "B, because a lower boiling point shows its molecules are harder "
            "to separate",
            "A, because more energy must be supplied before its molecules "
            "separate",
            "A, because its covalent bonds must be much stronger than B's",
            "They are equal, because both are simple molecular substances",
        ],
        "correct_index": 1,
        "why": "Boiling point measures the energy needed to pull the "
               "molecules apart, so the higher value means stronger forces.",
    },
    {
        "id": "ks4-properties-small-molecules-h01",
        "subtopic_slug": "properties-small-molecules",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Melting 1 kg of ice needs about 330 kJ, but breaking all the "
                "covalent bonds in 1 kg of water would need about 52 000 kJ. "
                "Explain what this comparison shows about melting.",
        "options": [
            "It shows that melting breaks about one covalent bond in every "
            "160",
            "It shows that the covalent bonds in water are unusually weak "
            "compared with those in other substances, so ice melts easily",
            "It shows that ice contains far fewer covalent bonds than liquid "
            "water does",
            "It shows melting overcomes only the weak forces between "
            "molecules and breaks no covalent bonds at all",
        ],
        "correct_index": 3,
        "why": "Melting costs a tiny fraction of the bond-breaking energy, so "
               "the covalent bonds cannot be what is being broken.",
    },
    {
        "id": "ks4-properties-small-molecules-h02",
        "subtopic_slug": "properties-small-molecules",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student concludes that because carbon dioxide is a gas but "
                "silicon dioxide melts above 1600 °C, the Si-O bond must be "
                "far stronger than the C=O bond. Evaluate this conclusion.",
        "options": [
            "It does not follow: boiling carbon dioxide overcomes only weak "
            "intermolecular forces, while melting silicon dioxide breaks "
            "covalent bonds",
            "It is correct: the melting point of any substance is a direct "
            "measure of the strength of the covalent bonds that it contains, "
            "whatever its structure",
            "It does not follow, because silicon dioxide is ionic rather than "
            "covalent",
            "It is correct, because silicon atoms are larger and larger atoms "
            "always form stronger bonds",
        ],
        "correct_index": 0,
        "why": "The two substances change state by breaking different things, "
               "so their melting points cannot be compared bond for bond.",
    },
    {
        "id": "ks4-properties-small-molecules-h03",
        "subtopic_slug": "properties-small-molecules",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why increasing the pressure on a gas made of small "
                "molecules can turn it into a liquid.",
        "options": [
            "Pressing the molecules together makes their covalent bonds join "
            "up into a liquid",
            "Pressing the molecules closer lets the weak intermolecular "
            "forces hold them together as a liquid",
            "Pressure adds energy to the molecules, so they move faster and "
            "become a liquid",
            "Pressure turns the molecules into ions, which then attract each "
            "other strongly and form a liquid together",
        ],
        "correct_index": 1,
        "why": "Intermolecular forces only act over short distances, so "
               "forcing the molecules close enough lets them take hold.",
    },
    {
        "id": "ks4-properties-small-molecules-h04",
        "subtopic_slug": "properties-small-molecules",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the phrase 'weak covalent bonds' should never be "
                "used to explain the low boiling point of a simple molecular "
                "substance.",
        "options": [
            "Because the covalent bonds are indeed weak, but they are not the "
            "bonds that are broken when the substance boils away",
            "Because the phrase should say 'weak ionic bonds' instead",
            "Because the covalent bonds are strong and are not broken on "
            "boiling; it is the forces between molecules that are weak",
            "Because a covalent bond has no strength that can be compared "
            "with anything else",
        ],
        "correct_index": 2,
        "why": "Boiling separates whole molecules, so it is the "
               "intermolecular forces — not the covalent bonds — that are "
               "weak.",
    },

    # ── polymers ──────────────────────────────────────────────────────────
    {
        "id": "ks4-polymers-e01",
        "subtopic_slug": "polymers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the monomer used to make poly(propene).",
        "options": [
            "Propane",
            "Propene",
            "Ethene",
            "Chloroethene",
        ],
        "correct_index": 1,
        "why": "An addition polymer is named after its monomer, and "
               "poly(propene) is made from propene molecules.",
    },
    {
        "id": "ks4-polymers-e02",
        "subtopic_slug": "polymers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether polymers conduct electricity, and give the "
                "reason.",
        "options": [
            "Yes, because their long chains carry charge from end to end",
            "Yes, but only once they have been melted",
            "No, because they contain no free electrons and no ions",
            "No, because their covalent bonds are too weak to hold a current",
        ],
        "correct_index": 2,
        "why": "A polymer is made of uncharged molecules, so it has no mobile "
               "charged particles and acts as an insulator.",
    },
    {
        "id": "ks4-polymers-e03",
        "subtopic_slug": "polymers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the monomer that joins together to make PVC.",
        "options": [
            "Ethene",
            "Chlorine",
            "Propene",
            "Chloroethene",
        ],
        "correct_index": 3,
        "why": "PVC is poly(chloroethene): its monomer is chloroethene, which "
               "carries a chlorine atom on the C=C double bond.",
    },
    {
        "id": "ks4-polymers-e04",
        "subtopic_slug": "polymers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the small repeating section of a polymer chain that is "
                "written in brackets with an n outside.",
        "options": [
            "The repeating unit",
            "The monomer",
            "The polymer chain",
            "The double bond",
        ],
        "correct_index": 0,
        "why": "The repeating unit is the section that repeats along the "
               "chain; the monomer is the separate molecule it came from.",
    },
    {
        "id": "ks4-polymers-s01",
        "subtopic_slug": "polymers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A poly(ethene) chain is built from 2000 ethene monomers. "
                "Calculate the number of carbon atoms in the chain.",
        "options": [
            "4000 carbon atoms",
            "2000 carbon atoms",
            "1000 carbon atoms",
            "6000 carbon atoms",
        ],
        "correct_index": 0,
        "why": "Each ethene monomer contributes two carbon atoms, so 2000 "
               "monomers give 4000 carbons.",
    },
    {
        "id": "ks4-polymers-s02",
        "subtopic_slug": "polymers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a whole polymer chain is described as one very "
                "large molecule rather than as many small molecules held "
                "together.",
        "options": [
            "Because the units inside a chain are held to each other by the "
            "same weak forces that act between the separate chains themselves",
            "Because the chain carries a charge, and a charged particle "
            "counts as a single molecule",
            "Because the units within a chain are joined by strong covalent "
            "bonds, while the weak forces act only between separate chains",
            "Because the chain is a giant covalent structure, and those "
            "always count as one molecule",
        ],
        "correct_index": 2,
        "why": "Covalent bonds run along the chain, so the whole chain is one "
               "molecule; only the chains themselves are weakly attracted.",
    },
    {
        "id": "ks4-polymers-s03",
        "subtopic_slug": "polymers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the relative formula mass of one repeating unit of "
                "poly(ethene), -CH2-CH2-. (Ar: C = 12, H = 1)",
        "options": [
            "24",
            "26",
            "30",
            "28",
        ],
        "correct_index": 3,
        "why": "Two carbons give 24 and four hydrogens give 4, so the "
               "repeating unit has a relative formula mass of 28.",
    },
    {
        "id": "ks4-polymers-s04",
        "subtopic_slug": "polymers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethene is a gas at room temperature, but the poly(ethene) "
                "made from it is a solid. Explain why.",
        "options": [
            "The polymer's covalent bonds are much stronger than those in "
            "ethene",
            "The polymer's molecules are thousands of times longer, so the "
            "forces between them are far stronger",
            "The polymer contains ions, while ethene contains only molecules",
            "The polymer has lost its double bonds, and it is double bonds "
            "that make a substance a gas at room temperature",
        ],
        "correct_index": 1,
        "why": "Longer chains touch over a far greater area, so the total "
               "intermolecular force between them is much greater.",
    },
    {
        "id": "ks4-polymers-h01",
        "subtopic_slug": "polymers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Propene has the formula CH2=CHCH3. Deduce the repeating unit "
                "of poly(propene).",
        "options": [
            "-CH2-CH2-",
            "-CH2=CH(CH3)-",
            "-CH2-CH(CH3)-",
            "-CH3-CH3-",
        ],
        "correct_index": 2,
        "why": "The double bond opens to a single bond and every atom of the "
               "monomer stays, so the unit is -CH2-CH(CH3)-.",
    },
    {
        "id": "ks4-polymers-h02",
        "subtopic_slug": "polymers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the relative formula mass of an addition polymer "
                "is always a whole-number multiple of its monomer's.",
        "options": [
            "Because a small molecule is lost each time, and its mass is "
            "subtracted evenly along the chain",
            "Because every atom of each monomer ends up in the chain, so n "
            "monomers give n times the mass",
            "Because the double bond adds two extra hydrogen atoms to every "
            "unit as it opens",
            "Because an addition polymer always contains exactly one thousand "
            "monomer units",
        ],
        "correct_index": 1,
        "why": "Addition polymerisation loses no atoms at all, so the masses "
               "simply add up.",
    },
    {
        "id": "ks4-polymers-h03",
        "subtopic_slug": "polymers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says poly(ethene) is a giant covalent structure "
                "because its molecules contain thousands of atoms. Evaluate "
                "this statement.",
        "options": [
            "It is wrong: the covalent bonds run only along each separate "
            "chain, and weak forces hold the chains to one another",
            "It is correct: any molecule that contains many thousands of "
            "atoms counts as a giant covalent structure, however it is bonded",
            "It is wrong: the chains are held to each other by ionic bonds "
            "rather than covalent ones",
            "It is correct, because the chains are joined end to end into one "
            "continuous network",
        ],
        "correct_index": 0,
        "why": "In a giant covalent structure the bonds run through the whole "
               "solid; in a polymer they stop at the end of each chain.",
    },
    {
        "id": "ks4-polymers-h04",
        "subtopic_slug": "polymers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some polymers have chains joined to each other by covalent "
                "cross-links. Suggest why such a polymer does not soften on "
                "heating, unlike poly(ethene).",
        "options": [
            "The cross-links add extra weak forces, which simply take longer "
            "to overcome",
            "The cross-links make the chains shorter, so there is less "
            "material to melt",
            "The cross-links remove the intermolecular forces, so heating the "
            "polymer has nothing left to act on",
            "The chains are joined by strong covalent bonds, so heating "
            "cannot let them slide past each other",
        ],
        "correct_index": 3,
        "why": "Softening depends on chains sliding apart, and covalent "
               "cross-links are far too strong for heating to break.",
    },

    # ── giant-covalent-structures ─────────────────────────────────────────
    {
        "id": "ks4-giant-covalent-structures-e01",
        "subtopic_slug": "giant-covalent-structures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of carbon atoms in each ring of a layer of "
                "graphite.",
        "options": [
            "3 carbon atoms",
            "4 carbon atoms",
            "6 carbon atoms",
            "8 carbon atoms",
        ],
        "correct_index": 2,
        "why": "Each carbon bonds to three others, which builds flat sheets "
               "of six-membered hexagonal rings.",
    },
    {
        "id": "ks4-giant-covalent-structures-e02",
        "subtopic_slug": "giant-covalent-structures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the giant covalent substance that makes up sand and "
                "quartz.",
        "options": [
            "Calcium carbonate",
            "Silicon dioxide",
            "Sodium chloride",
            "Carbon dioxide",
        ],
        "correct_index": 1,
        "why": "Sand and quartz are silicon dioxide, a giant covalent network "
               "of silicon and oxygen atoms.",
    },
    {
        "id": "ks4-giant-covalent-structures-e03",
        "subtopic_slug": "giant-covalent-structures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one use of diamond that depends on its hardness.",
        "options": [
            "The tips of drill bits and cutting tools",
            "The electrodes used in electrolysis",
            "A dry lubricant for machine parts",
            "The 'lead' inside a pencil",
        ],
        "correct_index": 0,
        "why": "Diamond's rigid three-dimensional network of covalent bonds "
               "makes it hard enough to cut other materials.",
    },
    {
        "id": "ks4-giant-covalent-structures-e04",
        "subtopic_slug": "giant-covalent-structures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by an allotrope.",
        "options": [
            "A mixture of two elements that have different properties",
            "A compound of carbon with another non-metal element",
            "An element that has been heated until its properties change",
            "A different structural form of the same element",
        ],
        "correct_index": 3,
        "why": "Diamond and graphite are allotropes: the same element, "
               "carbon, with its atoms arranged differently.",
    },
    {
        "id": "ks4-giant-covalent-structures-s01",
        "subtopic_slug": "giant-covalent-structures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Diamond melts above 3500 °C but methane melts at -182 °C, "
                "although both contain carbon atoms joined by covalent bonds. "
                "Explain the difference.",
        "options": [
            "Methane's covalent bonds are far weaker than the ones in "
            "diamond, so they break at a much lower temperature when the "
            "solid is heated gently",
            "Methane is ionic, so its lattice collapses long before diamond's "
            "does",
            "Diamond contains more carbon atoms in total, so more heat is "
            "needed to warm it up",
            "Diamond's covalent bonds run through the whole structure and "
            "must be broken; methane is separate molecules with weak forces "
            "between them",
        ],
        "correct_index": 3,
        "why": "Melting diamond breaks covalent bonds; melting methane only "
               "separates molecules that are weakly attracted.",
    },
    {
        "id": "ks4-giant-covalent-structures-s02",
        "subtopic_slug": "giant-covalent-structures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Graphite is used to make the electrodes for electrolysis. "
                "Explain two properties that make it suitable.",
        "options": [
            "It conducts electricity through its delocalised electrons, and "
            "its very high melting point lets it survive the hot electrolyte",
            "It is soft, so the electrodes can be shaped, and it dissolves "
            "slowly into the electrolyte",
            "It has a low melting point, so it makes good contact, and it is "
            "an insulator, so it is safe",
            "It contains free ions that carry the current through the "
            "electrode, and it is unreactive towards the electrolyte around "
            "it as well",
        ],
        "correct_index": 0,
        "why": "The delocalised electron from each carbon carries the "
               "current, and the covalent network stands the temperature.",
    },
    {
        "id": "ks4-giant-covalent-structures-s03",
        "subtopic_slug": "giant-covalent-structures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why writing with a graphite pencil leaves a grey "
                "mark on the paper.",
        "options": [
            "The graphite melts slightly under the pressure of writing and "
            "sets again on the paper",
            "The clay in the pencil glues individual carbon atoms onto the "
            "paper surface",
            "Layers of carbon atoms slide off, because only weak forces hold "
            "one layer to the next",
            "The delocalised electrons are rubbed onto the paper, leaving the "
            "grey mark",
        ],
        "correct_index": 2,
        "why": "The forces between graphite's layers are weak, so whole "
               "layers slide off onto the paper.",
    },
    {
        "id": "ks4-giant-covalent-structures-s04",
        "subtopic_slug": "giant-covalent-structures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why silicon dioxide does not conduct electricity, "
                "even though it has a giant structure like graphite.",
        "options": [
            "Its covalent bonds are too weak to hold any electrons in place",
            "All the outer electrons of its atoms are used in covalent bonds, "
            "so none are delocalised and there are no ions",
            "It does contain ions, but they are locked into fixed positions "
            "in the structure until the solid has been melted down",
            "It contains delocalised electrons, but they are too heavy to "
            "move through the structure",
        ],
        "correct_index": 1,
        "why": "Conduction needs a spare charged particle, and silicon "
               "dioxide uses every outer electron in bonding.",
    },
    {
        "id": "ks4-giant-covalent-structures-h01",
        "subtopic_slug": "giant-covalent-structures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the way graphite conducts electricity with the way a "
                "metal does.",
        "options": [
            "Both use delocalised electrons that move through the structure; "
            "graphite's come from the fourth outer electron of each carbon",
            "Graphite uses moving ions, while a metal uses moving electrons",
            "Both use moving positive ions, but graphite's can move only "
            "within a layer",
            "Graphite conducts along its covalent bonds, while a metal "
            "conducts through the sea of delocalised electrons around its "
            "ions instead",
        ],
        "correct_index": 0,
        "why": "Both conduct by delocalised electrons, even though graphite "
               "is a covalent network rather than a lattice of metal ions.",
    },
    {
        "id": "ks4-giant-covalent-structures-h02",
        "subtopic_slug": "giant-covalent-structures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the use of silicon dioxide to make a crucible for "
                "heating substances to high temperatures.",
        "options": [
            "Unsuitable, because it is simple molecular and would melt long "
            "before the substance inside it did",
            "Unsuitable, because its delocalised electrons would let the heat "
            "escape too quickly",
            "Suitable, because it is ionic and its lattice spreads heat "
            "evenly through the sample",
            "Suitable, because it is giant covalent, so many strong Si-O "
            "bonds give it a very high melting point",
        ],
        "correct_index": 3,
        "why": "A giant covalent network must have many strong bonds broken "
               "to melt, so it survives very high temperatures.",
    },
    {
        "id": "ks4-giant-covalent-structures-h03",
        "subtopic_slug": "giant-covalent-structures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says graphite must be a metal, because it conducts "
                "electricity and looks grey and shiny. Evaluate this "
                "statement.",
        "options": [
            "It is a metal, because any substance that conducts electricity "
            "has to contain metallic bonding of some kind, whatever it looks "
            "like",
            "It is not a metal: it is a giant covalent structure, and it "
            "conducts only because one electron per carbon is delocalised",
            "It is not a metal: it conducts using free ions rather than free "
            "electrons",
            "It is a metal, but a weak one, because its layers slide over "
            "each other as a metal's do",
        ],
        "correct_index": 1,
        "why": "Conducting does not make something a metal — graphite's "
               "carbon atoms are covalently bonded, not held in an ion sea.",
    },
    {
        "id": "ks4-giant-covalent-structures-h04",
        "subtopic_slug": "giant-covalent-structures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Buckminsterfullerene is a soft solid that melts far below "
                "diamond's melting point, although both are made only of "
                "carbon. Explain why.",
        "options": [
            "Buckminsterfullerene contains much weaker covalent bonds than "
            "diamond, so far less energy is needed to break them when it is "
            "heated",
            "Buckminsterfullerene is ionic, so its lattice breaks apart more "
            "easily than diamond's",
            "Buckminsterfullerene is made of separate cage-shaped molecules "
            "held by weak forces, while diamond's covalent bonds run "
            "throughout",
            "Buckminsterfullerene has fewer carbon atoms in total, so there "
            "is less of it to melt",
        ],
        "correct_index": 2,
        "why": "C60 is molecular, so melting only separates whole cages; "
               "melting diamond means breaking the covalent network itself.",
    },

    # ── metals-alloys ─────────────────────────────────────────────────────
    {
        "id": "ks4-metals-alloys-e01",
        "subtopic_slug": "metals-alloys",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two elements that bronze is made from.",
        "options": [
            "Copper and zinc",
            "Iron and carbon",
            "Iron and chromium",
            "Copper and tin",
        ],
        "correct_index": 3,
        "why": "Bronze is copper alloyed with tin; copper with zinc gives "
               "brass instead.",
    },
    {
        "id": "ks4-metals-alloys-e02",
        "subtopic_slug": "metals-alloys",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the element added to iron to make steel.",
        "options": [
            "Carbon",
            "Copper",
            "Zinc",
            "Tin",
        ],
        "correct_index": 0,
        "why": "Steel is iron with a small percentage of carbon, whose "
               "differently sized atoms stop the layers sliding.",
    },
    {
        "id": "ks4-metals-alloys-e03",
        "subtopic_slug": "metals-alloys",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what type of substance an alloy is.",
        "options": [
            "A compound of two metals combined in a fixed ratio",
            "A mixture of a metal with one or more other elements",
            "An element that has been purified by melting",
            "A molecule that contains metal atoms",
        ],
        "correct_index": 1,
        "why": "An alloy is a mixture — the added atoms sit in the same "
               "lattice without forming a compound.",
    },
    {
        "id": "ks4-metals-alloys-e04",
        "subtopic_slug": "metals-alloys",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name two metals commonly used to carry electricity in wires "
                "and overhead cables.",
        "options": [
            "Sulfur and carbon",
            "Zinc and tin",
            "Copper and aluminium",
            "Iron and lead",
        ],
        "correct_index": 2,
        "why": "Both conduct well through their delocalised electrons and "
               "both are ductile enough to be drawn into wire.",
    },
    {
        "id": "ks4-metals-alloys-s01",
        "subtopic_slug": "metals-alloys",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium is used for overhead power cables even though "
                "copper conducts slightly better. Suggest why.",
        "options": [
            "Aluminium becomes a better conductor than copper at the high "
            "voltages used",
            "Aluminium has a much lower density, so the cables are lighter "
            "and need fewer supporting pylons",
            "Aluminium is an insulator, which makes the cables safer above a "
            "road",
            "Aluminium melts at a lower temperature than copper, so lengths "
            "of cable are much easier to join together",
        ],
        "correct_index": 1,
        "why": "Aluminium's low density lets long spans hang between pylons "
               "without the cable's own weight bringing it down.",
    },
    {
        "id": "ks4-metals-alloys-s02",
        "subtopic_slug": "metals-alloys",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A saucepan has a copper base and a plastic handle. Explain "
                "both choices in terms of structure and bonding.",
        "options": [
            "Both are chosen for their delocalised electrons, which spread "
            "the heat evenly through the pan",
            "The copper insulates the food from the heat of the ring, while "
            "the plastic carries heat away from the cook's hand, keeping it "
            "cool",
            "Copper's delocalised electrons transfer thermal energy quickly, "
            "while the plastic has no free electrons or ions, so it stays "
            "cool",
            "Copper contains free ions that carry the heat, and the plastic "
            "contains ions that are fixed in place",
        ],
        "correct_index": 2,
        "why": "Thermal conduction needs mobile electrons; a polymer has "
               "none, so it insulates the hand.",
    },
    {
        "id": "ks4-metals-alloys-s03",
        "subtopic_slug": "metals-alloys",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a metal can be melted down and re-cast without "
                "losing its metallic properties.",
        "options": [
            "Melting only separates the ions; on cooling, the positive ions "
            "and the electron sea reform the same structure",
            "Melting destroys the metallic bonding permanently, so recycled "
            "metal is always weaker than the original metal was",
            "Melting turns the metal into a compound, which then has to be "
            "reduced back again",
            "Melting removes the delocalised electrons, which are replaced "
            "from the air as it cools",
        ],
        "correct_index": 0,
        "why": "Melting is a physical change: the same ions and the same "
               "delocalised electrons rebuild the same lattice on cooling.",
    },
    {
        "id": "ks4-metals-alloys-s04",
        "subtopic_slug": "metals-alloys",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Steel has a density of 7.9 g/cm3 and an aluminium alloy 2.8 "
                "g/cm3. Calculate how many times heavier a steel panel is "
                "than an aluminium-alloy panel of the same volume.",
        "options": [
            "5.1 times heavier",
            "0.35 times heavier",
            "10.7 times heavier",
            "2.8 times heavier",
        ],
        "correct_index": 3,
        "why": "Same volume, so the masses are in the ratio of the densities: "
               "7.9 divided by 2.8 is 2.8.",
    },
    {
        "id": "ks4-metals-alloys-h01",
        "subtopic_slug": "metals-alloys",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says alloys are harder than pure metals because "
                "the added atoms form extra bonds. Evaluate this statement.",
        "options": [
            "It is wrong: no new bonds form, and the hardness comes from "
            "differently sized atoms stopping the layers sliding",
            "It is correct: the added atoms form extra covalent bonds between "
            "the layers of ions",
            "It is correct: the added atoms release more delocalised "
            "electrons, which strengthens the bonding throughout the lattice",
            "It is wrong: alloys are actually softer than the pure metals "
            "they are made from",
        ],
        "correct_index": 0,
        "why": "An alloy is a mixture, not a new compound — its hardness is a "
               "geometry effect on sliding layers, not extra bonding.",
    },
    {
        "id": "ks4-metals-alloys-h02",
        "subtopic_slug": "metals-alloys",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what carries the charge when electricity is passed "
                "through solid copper, molten copper chloride and solid "
                "copper chloride.",
        "options": [
            "Delocalised electrons in all three, though they move most easily "
            "in the molten compound and least easily in the two solids",
            "Delocalised electrons in solid copper; moving ions in molten "
            "copper chloride; nothing moves in the solid compound",
            "Moving ions in all three, because every solid contains charged "
            "particles somewhere",
            "Moving ions in solid copper; delocalised electrons in both forms "
            "of copper chloride",
        ],
        "correct_index": 1,
        "why": "A metal's electrons are mobile even in the solid; an ionic "
               "compound's ions are not, until it melts or dissolves.",
    },
    {
        "id": "ks4-metals-alloys-h03",
        "subtopic_slug": "metals-alloys",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to a metal's malleability if its "
                "delocalised electrons could not move between the layers of "
                "ions, and explain your prediction.",
        "options": [
            "It would become more malleable, because nothing would then "
            "resist the layers of ions moving past one another at all",
            "It would be unchanged, because malleability depends only on the "
            "size of the ions",
            "It would become brittle, because nothing would hold the shifted "
            "layers of positive ions together and they would repel",
            "It would melt at a much lower temperature but stay just as "
            "malleable",
        ],
        "correct_index": 2,
        "why": "The electron sea is what re-surrounds displaced ions; without "
               "it, shifted layers of positive ions would simply repel.",
    },
    {
        "id": "ks4-metals-alloys-h04",
        "subtopic_slug": "metals-alloys",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the use of an aluminium alloy rather than pure "
                "aluminium for the body of an aircraft, giving one advantage "
                "and one disadvantage.",
        "options": [
            "Advantage: the alloy conducts electricity better than pure "
            "aluminium; disadvantage: it is much denser and therefore heavier",
            "Advantage: it is a pure substance; disadvantage: it melts at a "
            "single fixed temperature",
            "Advantage: it is more malleable; disadvantage: its layers of "
            "ions slide far too easily",
            "Advantage: it is harder and stronger for the same low density; "
            "disadvantage: it costs more and is harder to recycle",
        ],
        "correct_index": 3,
        "why": "Alloying buys strength without weight, at the price of cost "
               "and of separating the mixture again at end of life.",
    },

    # ── nanoparticles ─────────────────────────────────────────────────────
    {
        "id": "ks4-nanoparticles-e01",
        "subtopic_slug": "nanoparticles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the range of sizes that defines a nanoparticle.",
        "options": [
            "1 nm to 100 nm",
            "100 nm to 1000 nm",
            "0.01 nm to 0.1 nm",
            "1000 nm to 10 000 nm",
        ],
        "correct_index": 0,
        "why": "Nanoparticles are between 1 nm and 100 nm across — bigger "
               "than a single atom, far smaller than a speck of dust.",
    },
    {
        "id": "ks4-nanoparticles-e02",
        "subtopic_slug": "nanoparticles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the length, in metres, of 1 nanometre.",
        "options": [
            "0.001 m",
            "0.000 001 m",
            "0.000 000 000 001 m",
            "0.000 000 001 m",
        ],
        "correct_index": 3,
        "why": "A nanometre is one thousand-millionth of a metre, so 1 nm is "
               "0.000 000 001 m.",
    },
    {
        "id": "ks4-nanoparticles-e03",
        "subtopic_slug": "nanoparticles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the fullerene whose 60 carbon atoms form a hollow "
                "sphere.",
        "options": [
            "Graphene",
            "A carbon nanotube",
            "Buckminsterfullerene",
            "Graphite",
        ],
        "correct_index": 2,
        "why": "Buckminsterfullerene, C60, is the football-shaped cage of "
               "hexagons and pentagons.",
    },
    {
        "id": "ks4-nanoparticles-e04",
        "subtopic_slug": "nanoparticles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether silver nanoparticles and a bar of silver are "
                "the same substance.",
        "options": [
            "They are different substances, because the nanoparticles contain "
            "different atoms",
            "They are the same substance: the same silver atoms, differing "
            "only in particle size",
            "They are different substances, because the nanoparticles have "
            "lost some of their electrons",
            "They are the same substance, and their properties are therefore "
            "identical",
        ],
        "correct_index": 1,
        "why": "Nothing chemical changes at the nanoscale — it is the same "
               "silver, in far smaller pieces.",
    },
    {
        "id": "ks4-nanoparticles-s01",
        "subtopic_slug": "nanoparticles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Carbon nanotubes are mixed into the composite material used "
                "to make bicycle frames. Suggest why this makes the frame "
                "stronger without making it much heavier.",
        "options": [
            "The nanotubes conduct electricity, which carries stress away "
            "from the weakest points of the frame",
            "The nanotubes melt during manufacture and fill the gaps between "
            "the other particles",
            "A nanotube is a rolled sheet of covalently bonded carbon, so it "
            "is very strong for its very small mass",
            "The nanotubes are ionic, so they attract the surrounding "
            "composite and lock it in place",
        ],
        "correct_index": 2,
        "why": "Covalent bonds run right along a nanotube's rolled carbon "
               "sheet, giving very high strength, while the hollow tube adds "
               "almost no mass.",
    },
    {
        "id": "ks4-nanoparticles-s02",
        "subtopic_slug": "nanoparticles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Gold nanoparticles appear red, while a bar of gold appears "
                "yellow. Explain what this shows about the effect of particle "
                "size.",
        "options": [
            "The nanoparticles have reacted with the oxygen in the air to "
            "form a different compound, which happens to be red in colour",
            "It is the same gold, but at the nanoscale its properties, "
            "including how it interacts with light, are different",
            "The nanoparticles contain a different element, which is what "
            "gives them the red colour",
            "The nanoparticles are hotter than bulk gold, and hot metals glow "
            "red",
        ],
        "correct_index": 1,
        "why": "Scale, not composition, changes at the nanoscale — the same "
               "element can look and behave completely differently.",
    },
    {
        "id": "ks4-nanoparticles-s03",
        "subtopic_slug": "nanoparticles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Silver nanoparticles are added to sports socks to stop them "
                "smelling. Suggest how they work, and give one environmental "
                "concern.",
        "options": [
            "They mask the smell with a scent, and that scent may irritate "
            "the skin",
            "They kill bacteria because they are heavy and settle into the "
            "fabric, and they may make the socks too heavy to wear "
            "comfortably",
            "They absorb sweat because they are porous, and they may block "
            "drains when the socks are washed",
            "Their large surface area makes them very reactive so they kill "
            "bacteria, but washing may release them into waterways",
        ],
        "correct_index": 3,
        "why": "A huge surface area makes a tiny mass of silver strongly "
               "antibacterial — and just as able to escape into the "
               "environment.",
    },
    {
        "id": "ks4-nanoparticles-s04",
        "subtopic_slug": "nanoparticles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Self-cleaning glass is coated with nanoparticles. Suggest "
                "why only an extremely thin layer is needed.",
        "options": [
            "Their huge surface area for such a tiny volume means a very "
            "small amount acts over the whole surface",
            "They are transparent, so a thicker layer would be invisible and "
            "therefore wasted",
            "A thicker layer would make the glass conduct electricity, which "
            "would be unsafe in a window frame outdoors",
            "They are so heavy that a thicker layer would crack the glass "
            "under its own weight",
        ],
        "correct_index": 0,
        "why": "Because so much of a nanoparticle's material sits on its "
               "surface, a tiny mass provides an enormous working area.",
    },
    {
        "id": "ks4-nanoparticles-h01",
        "subtopic_slug": "nanoparticles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solid is ground from cubes of side 1 mm into cubes of side "
                "1 micrometre, one thousand times smaller. Deduce by what "
                "factor the total surface area of the sample increases.",
        "options": [
            "10 times greater",
            "100 times greater",
            "1 000 000 times greater",
            "1000 times greater",
        ],
        "correct_index": 3,
        "why": "For a fixed total volume the surface area is proportional to "
               "1 divided by the side length, so dividing the side by 1000 "
               "multiplies the surface area by 1000.",
    },
    {
        "id": "ks4-nanoparticles-h02",
        "subtopic_slug": "nanoparticles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the use of nanoparticles in cosmetics, giving one "
                "benefit and one risk.",
        "options": [
            "Benefit: they make the product cheaper; risk: they change colour "
            "over time",
            "Benefit: they are heavier, so they stay on the skin for longer; "
            "risk: they wash off into drains and then into rivers",
            "Benefit: they work in tiny amounts and stay transparent on the "
            "skin; risk: their size may let them pass into cells",
            "Benefit: they are a safer element than the bulk material; risk: "
            "they reflect ultraviolet light",
        ],
        "correct_index": 2,
        "why": "The huge surface area makes tiny amounts effective, but that "
               "same tiny size is what may let them cross cell membranes.",
    },
    {
        "id": "ks4-nanoparticles-h03",
        "subtopic_slug": "nanoparticles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the very property that makes nanoparticles "
                "useful is also what makes them potentially hazardous.",
        "options": [
            "Their tiny size and huge surface area make them very reactive "
            "and able to enter cells - useful in medicine, risky for health",
            "Their large mass makes them settle out quickly - useful in "
            "surface coatings, but risky if they are inhaled deep into the "
            "lungs",
            "Their low reactivity makes them safe to handle - useful in "
            "sunscreen, risky in food",
            "Their electrical conductivity makes them useful in electronics "
            "and dangerous in water",
        ],
        "correct_index": 0,
        "why": "High reactivity and the ability to slip into cells are one "
               "property seen from two sides.",
    },
    {
        "id": "ks4-nanoparticles-h04",
        "subtopic_slug": "nanoparticles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why scientists say more research is needed before "
                "nanoparticles are used widely in food packaging.",
        "options": [
            "Because nanoparticles are already known to be completely "
            "harmless inside the body, so any further testing would be no "
            "more than a formality",
            "Because their long-term effects on the body and the environment "
            "are not yet understood, and they may build up in food chains",
            "Because they are far too expensive to use in packaging at "
            "present",
            "Because they would make the packaging conduct electricity, which "
            "has never been tested",
        ],
        "correct_index": 1,
        "why": "The health and environmental effects of nanoparticles are "
               "still being investigated, so the risk cannot yet be judged.",
    },
]
