"""Chemistry · Atomic structure and the periodic table — atoms, elements and
compounds · the MRB-338 expansion.

Fifty-two rows on the classification itself and on what follows from it: element
against compound against mixture, reading a chemical formula (subscripts,
brackets and coefficients, which are three different things), the balanced
symbol equation, and the conservation of mass that a balanced equation is a
statement of. The weight falls on the two places the existing twelve rows only
touch — atom counting inside brackets and coefficients, and mass conservation
read in an open vessel, where the reading on the balance changes and the mass of
matter does not.

Separation techniques belong to the `mixtures` leaf and nothing here asks for
one; the inside of the atom belongs to four further leaves and nothing here
mentions a proton.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-atoms-elements-compounds-e05",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many different elements are present in one formula "
                "unit of calcium carbonate, CaCO3.",
        "options": [
            "Three different elements",
            "Two different elements",
            "Five different elements",
            "Six different elements",
        ],
        "correct_index": 0,
        "why": "The formula names calcium, carbon and oxygen, so three "
               "different elements are chemically bonded together in it.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e06",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these substances is a compound?",
        "options": [
            "Nitrogen gas, N2",
            "Ammonia, NH3",
            "Neon gas, Ne",
            "Bronze, which is copper melted together with tin",
        ],
        "correct_index": 1,
        "why": "Ammonia contains nitrogen and hydrogen chemically bonded "
               "together, which is what makes a substance a compound.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e07",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the law of conservation of mass says happens to "
                "the atoms during a chemical reaction.",
        "options": [
            "They shrink a little, which is why the products weigh less",
            "They appear from nothing as the products are formed",
            "They are rearranged, and none is destroyed",
            "They are destroyed, and brand-new atoms of the products are "
            "built to replace them",
        ],
        "correct_index": 2,
        "why": "A chemical reaction only rearranges the atoms that were "
               "already there, so the total mass cannot change.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e08",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which symbol represents the element potassium?",
        "options": [
            "P",
            "Po",
            "Pt",
            "K",
        ],
        "correct_index": 3,
        "why": "Potassium has the symbol K, from its Latin name kalium; P is "
               "phosphorus, Po is polonium and Pt is platinum.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e09",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a small number written just after a symbol in a "
                "chemical formula tells you.",
        "options": [
            "How many atoms of that element are present",
            "The mass of that element in the compound",
            "How many bonds that element has formed",
            "The order in which that element was added",
        ],
        "correct_index": 0,
        "why": "The subscript counts the atoms of the symbol it follows, so "
               "the 2 in H2O means two hydrogen atoms.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e10",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a mixture rather than a pure substance?",
        "options": [
            "Carbon dioxide",
            "Crude oil",
            "Sulfuric acid",
            "Magnesium oxide, the white powder left after burning magnesium",
        ],
        "correct_index": 1,
        "why": "Crude oil is many different hydrocarbons stirred together "
               "without being chemically bonded, so it is a mixture.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e11",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many oxygen atoms are present in one formula unit "
                "of aluminium oxide, Al2O3.",
        "options": [
            "2 oxygen atoms",
            "6 oxygen atoms",
            "3 oxygen atoms",
            "5 oxygen atoms",
        ],
        "correct_index": 2,
        "why": "The subscript 3 after the O counts the oxygen atoms, so one "
               "formula unit of Al2O3 holds three of them.",
    },
    {
        "id": "ks4-atoms-elements-compounds-e12",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a chemical change rather than a physical "
                "change?",
        "options": [
            "Ice melting to form water",
            "Salt dissolving in warm water",
            "Iodine crystals turning straight into a purple vapour on a "
            "warm gauze",
            "Green copper carbonate turning black",
        ],
        "correct_index": 3,
        "why": "A new substance with new properties is made when copper "
               "carbonate decomposes, which is the mark of a chemical change.",
    },
    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-atoms-elements-compounds-s05",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the total number of atoms in one formula unit of "
                "calcium hydroxide, Ca(OH)2.",
        "options": [
            "5 atoms",
            "3 atoms",
            "4 atoms",
            "6 atoms",
        ],
        "correct_index": 0,
        "why": "The bracket is multiplied by 2, giving one calcium, two "
               "oxygen and two hydrogen atoms, which is five in total.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s06",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which set of numbers balances the burning of magnesium, "
                "__Mg + __O2 -> __MgO?",
        "options": [
            "1, 1, 1",
            "2, 1, 2",
            "1, 2, 2",
            "2, 2, 1",
        ],
        "correct_index": 1,
        "why": "2Mg + O2 -> 2MgO gives two magnesium atoms and two oxygen "
               "atoms on each side of the arrow.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s07",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A strip of magnesium is burned in an open crucible and the "
                "mass of the crucible and its contents increases. Explain "
                "why.",
        "options": [
            "Heating any metal adds energy to it, and added energy has mass "
            "of its own",
            "The flame deposits soot onto the crucible, and soot is denser "
            "than magnesium is",
            "Oxygen from the air has joined the magnesium to make a heavier "
            "product",
            "Burning turns light magnesium atoms into much heavier atoms of "
            "another element altogether",
        ],
        "correct_index": 2,
        "why": "Magnesium oxide contains the oxygen that was taken from the "
               "air, so the solid in the crucible gains that oxygen's mass.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s08",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bronze is made by melting copper and tin together. Explain "
                "why bronze is classed as a mixture.",
        "options": [
            "Because two metals can never bond to each other",
            "Because melting is a physical change, so nothing that has been "
            "made by melting is ever a compound of any kind",
            "Because bronze conducts electricity, and no compound of any "
            "kind is able to conduct",
            "Because the two metals are not bonded and the proportions can "
            "be varied",
        ],
        "correct_index": 3,
        "why": "The copper and tin atoms sit side by side without bonding, so "
               "a bronze can be made to any chosen composition.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s09",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Oxygen gas has the formula O2. Explain why oxygen is an "
                "element and not a compound.",
        "options": [
            "Because both of the atoms in each molecule are oxygen atoms",
            "Because two atoms is too few to count",
            "Because the atoms are not really bonded",
            "Because every compound is a solid",
        ],
        "correct_index": 0,
        "why": "A compound needs at least two different elements, and O2 "
               "contains only one type of atom however many are bonded.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s10",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what the formulae 2H2O and H2O2 each describe.",
        "options": [
            "Both describe water, because each has twice as much hydrogen as "
            "oxygen",
            "2H2O is two water molecules; H2O2 is one molecule of a "
            "different substance",
            "Both describe hydrogen peroxide, because the total atom count "
            "is the same in each",
            "2H2O is a single substance holding four hydrogen atoms; H2O2 is "
            "two separate water molecules",
        ],
        "correct_index": 1,
        "why": "A big number in front multiplies whole molecules, while a "
               "subscript changes the substance itself.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s11",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium chloride contains magnesium and chlorine in a "
                "1 : 2 ratio of atoms. State its formula.",
        "options": [
            "MgCl",
            "Mg2Cl",
            "MgCl2",
            "Mg2Cl2",
        ],
        "correct_index": 2,
        "why": "One magnesium atom to two chlorine atoms is written MgCl2, "
               "with the subscript 2 placed after the chlorine.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s12",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a compound has one fixed formula while a mixture "
                "does not.",
        "options": [
            "A compound is made in a factory to a fixed recipe, while a "
            "mixture is simply thrown together by hand in a laboratory",
            "A compound is pure, and purity is counted in atoms",
            "A compound's atoms are all the same size, so there is only one "
            "way for them to pack",
            "A compound's atoms are bonded in a set ratio, and a mixture's "
            "are not bonded",
        ],
        "correct_index": 3,
        "why": "Chemical bonding fixes the ratio in which the atoms combine, "
               "whereas anything unbonded can be mixed in any proportion.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s13",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iron rusts according to __Fe + __O2 -> __Fe2O3. Determine "
                "the numbers needed to balance it.",
        "options": [
            "4, 3, 2",
            "2, 3, 1",
            "2, 1, 1",
            "4, 6, 2",
        ],
        "correct_index": 0,
        "why": "4Fe + 3O2 -> 2Fe2O3 gives four iron atoms and six oxygen "
               "atoms on both sides of the arrow.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s14",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a sealed flask, 4.0 g of hydrogen reacts completely with "
                "32.0 g of oxygen. Calculate the mass of water formed.",
        "options": [
            "28.0 g",
            "36.0 g",
            "32.0 g",
            "128.0 g",
        ],
        "correct_index": 1,
        "why": "No matter can leave a sealed flask, so the mass of water "
               "equals 4.0 g + 32.0 g.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s15",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Zinc reacts with hydrochloric acid to give zinc chloride "
                "and hydrogen. Which balanced symbol equation shows this?",
        "options": [
            "Zn + HCl -> ZnCl + H",
            "Zn + HCl2 -> ZnCl2 + H2",
            "Zn + 2HCl -> ZnCl2 + H2",
            "2Zn + 2HCl -> 2ZnCl + H2",
        ],
        "correct_index": 2,
        "why": "Two molecules of HCl supply the two chlorine atoms of ZnCl2 "
               "and the two hydrogen atoms of H2.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s16",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the state symbol (aq) after a formula in an "
                "equation tells you.",
        "options": [
            "The substance is a pure liquid at room temperature",
            "The substance is a gas bubbling out of a solution",
            "The substance is a solid that has settled at the bottom of the "
            "reaction vessel",
            "The substance is dissolved in water",
        ],
        "correct_index": 3,
        "why": "The symbol (aq) stands for aqueous, meaning the substance is "
               "in solution in water rather than present on its own.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s17",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the total number of atoms that 3CaCO3 represents "
                "in an equation.",
        "options": [
            "15 atoms",
            "5 atoms",
            "9 atoms",
            "27 atoms",
        ],
        "correct_index": 0,
        "why": "One CaCO3 unit holds 1 + 1 + 3 = 5 atoms, and the 3 in front "
               "multiplies the whole unit.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s18",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Green copper carbonate is heated and turns into black "
                "copper oxide and a gas. Classify the black solid.",
        "options": [
            "An element, because heating has broken all of its bonds",
            "A compound, because copper and oxygen are still bonded in it",
            "A mixture, because two different substances were made inside "
            "the same container at the very same moment",
            "An element, because only one colour of solid can be seen in the "
            "tube at the end",
        ],
        "correct_index": 1,
        "why": "Copper oxide contains two different elements bonded together, "
               "so it is a compound even though a gas was driven off.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s19",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of stainless steel contains iron, chromium, nickel "
                "and carbon. Classify the sample and justify the choice.",
        "options": [
            "A compound, because four elements are present at once",
            "An element, because it behaves as a single metal",
            "A mixture, because the elements are not bonded to one another "
            "and the recipe can be varied",
            "A compound, because it was made in a hot furnace",
        ],
        "correct_index": 2,
        "why": "An alloy is a mixture: the added elements sit among the iron "
               "atoms without chemical bonding, in proportions that can be "
               "chosen.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s20",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hydrogen and oxygen cannot be obtained from "
                "water by any physical method.",
        "options": [
            "The two gases are too small to be caught",
            "The two gases share one boiling point, so no physical method "
            "can ever tell them apart",
            "The two gases are already pure, so a physical method of any "
            "sort would be left with nothing further to remove from them",
            "The two gases are held together by chemical bonds that only a "
            "reaction can break",
        ],
        "correct_index": 3,
        "why": "Water is a compound, and breaking the bonds within it needs a "
               "chemical process such as electrolysis.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s21",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the ratio of iron atoms to oxygen atoms in iron(III) "
                "oxide, Fe2O3.",
        "options": [
            "2 : 3",
            "1 : 1",
            "3 : 2",
            "2 : 6",
        ],
        "correct_index": 0,
        "why": "The subscripts give two iron atoms for every three oxygen "
               "atoms.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s22",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Propane burns completely in oxygen. Determine the four "
                "numbers that balance __C3H8 + __O2 -> __CO2 + __H2O.",
        "options": [
            "1, 3, 3, 4",
            "1, 5, 3, 4",
            "1, 4, 3, 4",
            "2, 5, 6, 8",
        ],
        "correct_index": 1,
        "why": "C3H8 + 5O2 -> 3CO2 + 4H2O balances at three carbon, eight "
               "hydrogen and ten oxygen atoms on each side.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s23",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium nitrate is Mg(NO3)2. Deduce the number of atoms "
                "present in one formula unit.",
        "options": [
            "6 atoms",
            "7 atoms",
            "9 atoms",
            "12 atoms",
        ],
        "correct_index": 2,
        "why": "Everything inside the bracket is doubled, giving one "
               "magnesium, two nitrogen and six oxygen atoms.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s24",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sodium chloride does not behave like either of "
                "the elements it is made from.",
        "options": [
            "The elements have been diluted by each other until their own "
            "properties are too weak to notice",
            "The elements have swapped some of their properties with each "
            "other during the reaction",
            "The elements are present in amounts so small that only the "
            "crystal shape can be observed",
            "The elements have bonded, and the compound has properties of "
            "its own",
        ],
        "correct_index": 3,
        "why": "Bonding produces a new substance, so a compound's properties "
               "are not those of its elements or an average of them.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s25",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sulfur exists as molecules with the formula S8. Classify "
                "sulfur and justify the choice.",
        "options": [
            "An element, because every atom in the molecule is sulfur",
            "A compound, eight atoms being bonded",
            "A mixture, because eight separate particles are travelling "
            "along together inside every single molecule of it",
            "A compound, because a molecule this large cannot be built from "
            "one element alone",
        ],
        "correct_index": 0,
        "why": "Only one type of atom is present, so sulfur is an element no "
               "matter how many atoms are bonded in each molecule.",
    },
    {
        "id": "ks4-atoms-elements-compounds-s26",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the 2 in 2NaOH must not be written as a "
                "subscript instead.",
        "options": [
            "A subscript would look untidy on the page",
            "A subscript would change the substance, while the number in "
            "front counts whole units",
            "A subscript would double the mass, while the number in front "
            "doubles only the volume of it",
            "A subscript would turn the formula into an element, while the "
            "number written in front of it keeps the formula a compound",
        ],
        "correct_index": 1,
        "why": "A coefficient says how many formula units there are, but a "
               "subscript changes the ratio of atoms and so names a different "
               "substance.",
    },
    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-atoms-elements-compounds-h05",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A technician writes the combustion of ethane as "
                "__C2H6 + __O2 -> __CO2 + __H2O. State the coefficients that "
                "balance it.",
        "options": [
            "1, 3, 2, 3",
            "2, 5, 4, 6",
            "2, 7, 4, 6",
            "1, 7, 2, 6",
        ],
        "correct_index": 2,
        "why": "2C2H6 + 7O2 -> 4CO2 + 6H2O gives four carbon, twelve "
               "hydrogen and fourteen oxygen atoms on each side.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h06",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crucible holding 0.48 g of magnesium is heated until the "
                "metal has fully reacted, and the solid left has a mass of "
                "0.80 g. Calculate the mass of oxygen that reacted.",
        "options": [
            "0.16 g",
            "0.48 g",
            "1.28 g",
            "0.32 g",
        ],
        "correct_index": 3,
        "why": "The gain in mass is the oxygen taken in, so 0.80 g - 0.48 g "
               "is the oxygen that reacted.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h07",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A white solid softens and then melts gradually between "
                "48 degrees C and 61 degrees C. Deduce what this shows.",
        "options": [
            "It is a mixture, because a pure substance melts at one fixed "
            "temperature",
            "It is a compound, because the bonds inside a compound give way "
            "a few at a time as it warms",
            "It is an element, because elements have the widest melting "
            "ranges of any substances",
            "It is a compound, because every compound melts across a range "
            "of temperatures",
        ],
        "correct_index": 0,
        "why": "A pure substance, element or compound, melts sharply; a "
               "melting range is the standard evidence for a mixture.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h08",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two samples of air are collected, one in a city street and "
                "one on a hilltop, and their compositions differ slightly. "
                "Deduce what this shows about air.",
        "options": [
            "That one sample must have been contaminated",
            "That air is a mixture, because the proportions in a mixture are not fixed",
            "That air is a compound whose formula varies with height",
            "That air is an element, being a single substance",
        ],
        "correct_index": 1,
        "why": "A compound has a fixed composition, so composition that "
               "varies from place to place is evidence of a mixture.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h09",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Analysis of a compound of calcium and chlorine finds one "
                "calcium atom for every two chlorine atoms. Determine its "
                "formula.",
        "options": [
            "CaCl",
            "Ca2Cl",
            "CaCl2",
            "Ca2Cl4",
        ],
        "correct_index": 2,
        "why": "The formula of a compound is written with the simplest whole "
               "number ratio of its atoms.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h10",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Anything made of molecules must be a "
                "compound.' Evaluate this statement.",
        "options": [
            "Correct, because a molecule is by definition two or more "
            "elements bonded together",
            "Correct, because a lone atom can never be described as a "
            "molecule of anything at all",
            "Incorrect, because compounds are held together by weak forces "
            "rather than by any true bond",
            "Incorrect, because molecules such as N2 and S8 hold one type "
            "of atom",
        ],
        "correct_index": 3,
        "why": "A molecule is simply two or more atoms bonded together, and "
               "those atoms may all be of the same element.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h11",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes N2 + H2 -> NH3 and says it is balanced "
                "because two elements appear on each side. Explain the error.",
        "options": [
            "Balancing counts the atoms of each element, and both are wrong "
            "here",
            "Balancing counts the molecules on each side, and there are two "
            "on the left against one on the right",
            "Balancing counts the elements on each side, so the equation is "
            "already correct as it stands",
            "Balancing counts the bonds on each side, and ammonia holds more "
            "bonds than the reactants do",
        ],
        "correct_index": 0,
        "why": "As written there are two nitrogen and two hydrogen atoms on "
               "the left but one nitrogen and three hydrogen on the right, so "
               "it needs N2 + 3H2 -> 2NH3.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h12",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Substance X melts sharply at 1085 degrees C, conducts "
                "electricity, and cannot be broken down into anything "
                "simpler by a chemical reaction. Classify X.",
        "options": [
            "A mixture, because two properties were measured on one sample",
            "An element, because nothing simpler can be got from it",
            "A compound, because only a compound can melt at so high a "
            "temperature as that",
            "A compound, because conducting means charged particles are "
            "bonded together inside it",
        ],
        "correct_index": 1,
        "why": "An element is the substance a chemical reaction cannot "
               "simplify further, and the sharp melting point rules out a "
               "mixture.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h13",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a sealed vessel 12.0 g of one reactant and 18.0 g of "
                "another react to give 25.0 g of a solid plus one gas. "
                "Calculate the mass of gas produced.",
        "options": [
            "5.0 g",
            "7.0 g",
            "13.0 g",
            "43.0 g",
        ],
        "correct_index": 0,
        "why": "All 30.0 g of reactants must still be in the vessel, so the "
               "gas accounts for the difference from the solid's mass.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h14",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an equation is balanced by changing the big "
                "numbers in front of formulae and never the small numbers "
                "within them.",
        "options": [
            "The small numbers are harder to alter once an equation has been "
            "written out in full",
            "The big numbers are the ones that affect the mass in a reaction, "
            "and balancing is a question about mass alone",
            "The small numbers set the state of the substance, and the state "
            "has to be left alone",
            "The small numbers fix the compound's identity, while the big "
            "numbers only count units",
        ],
        "correct_index": 3,
        "why": "Altering a subscript names a different substance, so only the "
               "coefficients may be adjusted to make the atoms match.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h15",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sample P is iron and sulfur powders stirred together with "
                "one iron atom per sulfur atom. Sample Q is iron sulfide of "
                "the same composition. Compare the two samples.",
        "options": [
            "P keeps the properties of both powders; Q is one bonded compound",
            "They are the same substance, because the two elements are "
            "present in the very same ratio in each",
            "P is a compound; Q is a mixture",
            "Both are compounds",
        ],
        "correct_index": 0,
        "why": "Composition alone does not decide the class: what matters is "
               "whether the atoms are chemically bonded, and only in Q are "
               "they.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h16",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium sulfate is Al2(SO4)3. Determine how many oxygen "
                "atoms one formula unit contains.",
        "options": [
            "4 oxygen atoms",
            "12 oxygen atoms",
            "7 oxygen atoms",
            "9 oxygen atoms",
        ],
        "correct_index": 1,
        "why": "The bracket holds four oxygen atoms and is multiplied by 3, "
               "giving twelve oxygen atoms in the formula unit.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h17",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that distilling water would separate it "
                "into hydrogen and oxygen. Evaluate this claim.",
        "options": [
            "Correct, because boiling breaks every bond",
            "Incorrect, because water boils long before the hydrogen inside "
            "it could find time to escape",
            "Incorrect, because distillation is physical and cannot break "
            "bonds within a compound",
            "Correct, because the two gases have quite different boiling "
            "points and so come off the apparatus at different times",
        ],
        "correct_index": 2,
        "why": "Distillation only separates substances that were never "
               "bonded, so it returns water, not its elements.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h18",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper powder is heated strongly in an open dish of air "
                "until it stops changing. Predict how the mass of the dish "
                "and its contents changes.",
        "options": [
            "It stays the same, mass being conserved",
            "It falls, because the copper gives off a gas as the black solid "
            "forms in the dish",
            "It falls, because some of the copper has been turned straight "
            "into energy by the strength of the heating it was given",
            "It rises, because oxygen from the air joins the solid",
        ],
        "correct_index": 3,
        "why": "Copper oxide contains oxygen drawn from the air, and that "
               "oxygen's mass stays in the dish.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h19",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why CO and Co do not mean the same thing.",
        "options": [
            "CO is two elements bonded; Co is the element cobalt",
            "CO is carbon monoxide gas, while Co is that very same gas "
            "written down in a shorter style used in laboratories",
            "CO belongs in equations, while Co is the form used when writing "
            "the name out in prose",
            "CO is one carbon with one oxygen; Co is two carbons",
        ],
        "correct_index": 0,
        "why": "A second capital letter starts a new element, so CO is a "
               "compound of carbon and oxygen while Co is one element.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h20",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium reduces copper oxide in __Al + __CuO -> __Al2O3 "
                "+ __Cu. Determine the balancing numbers.",
        "options": [
            "1, 3, 1, 3",
            "2, 3, 1, 3",
            "2, 2, 1, 2",
            "3, 2, 1, 2",
        ],
        "correct_index": 1,
        "why": "2Al + 3CuO -> Al2O3 + 3Cu balances at two aluminium, three "
               "copper and three oxygen atoms on each side.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h21",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student predicts that a compound of a soft metal and a "
                "brittle non-metal will itself be moderately hard. Evaluate "
                "this prediction.",
        "options": [
            "Sound, because a compound's properties lie between those of the "
            "elements that formed it",
            "Sound, because hardness depends on how many different elements "
            "a substance happens to contain",
            "Unsound, because a compound's properties are new and cannot be "
            "averaged",
            "Unsound, because a compound made from any metal turns out "
            "harder than that metal was",
        ],
        "correct_index": 2,
        "why": "Bonding makes a new substance whose properties must be "
               "measured, not interpolated between those of its elements.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h22",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Silver nitrate solution and sodium chloride solution are "
                "mixed in a stoppered flask, and a white solid appears. "
                "Predict the total mass after mixing.",
        "options": [
            "Greater, because a solid weighs more",
            "Smaller, because the solid takes up less room",
            "Smaller, because forming a solid gives off mass",
            "Unchanged, because every atom present at the start is still "
            "inside the flask",
        ],
        "correct_index": 3,
        "why": "The flask is stoppered and the atoms have only been "
               "rearranged, so the total mass is conserved exactly.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h23",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium reacts with sulfur so that two sodium atoms combine "
                "with each sulfur atom. Determine the formula of the "
                "compound.",
        "options": [
            "Na2S",
            "NaS",
            "NaS2",
            "Na2S2",
        ],
        "correct_index": 0,
        "why": "The subscript follows the symbol it counts, so two sodium to "
               "one sulfur is written this way.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h24",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats a hydrated salt in an open boiling tube and "
                "the mass falls. Explain how this is consistent with the "
                "conservation of mass.",
        "options": [
            "Heating turned salt into energy",
            "The water vapour left the tube, so the missing mass is outside "
            "the apparatus",
            "Mass is conserved just inside sealed vessels, so the law does "
            "not cover an open boiling tube of this particular kind",
            "The salt grew less dense on heating, so the balance reports a "
            "smaller mass than before",
        ],
        "correct_index": 1,
        "why": "Mass is conserved overall; it only appears to fall because "
               "one product escaped from the open tube as a gas.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h25",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two brass samples are analysed: one is 63% copper by mass "
                "and the other 70%. Deduce whether brass is a compound.",
        "options": [
            "It is a compound, holding two metals",
            "It is a compound, because a percentage composition can be "
            "written down for either sample",
            "It is not a compound, because a compound's composition is fixed "
            "and this varies",
            "It is not a compound, because no compound made of two metals "
            "can possibly exist at any composition a chemist picks",
        ],
        "correct_index": 2,
        "why": "A compound has one fixed composition by mass, so two "
               "different percentages show brass to be a mixture.",
    },
    {
        "id": "ks4-atoms-elements-compounds-h26",
        "subtopic_slug": "atoms-elements-compounds",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of hydrogen atoms represented by 3NH3 "
                "with the number represented by 2H2SO4.",
        "options": [
            "2H2SO4 has more, with eight against three",
            "They are equal, at six hydrogen atoms each",
            "3NH3 has more, with three against two",
            "3NH3 has more, with nine hydrogen atoms against four",
        ],
        "correct_index": 3,
        "why": "3NH3 holds 3 x 3 = 9 hydrogen atoms while 2H2SO4 holds "
               "2 x 2 = 4, so the ammonia supplies more.",
    },
]
