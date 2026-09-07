"""Chemistry · Quantitative Chemistry — the KS4 assignment pool (MRB-332).

Ten subtopics, twelve questions each: conservation of mass and balancing,
relative formula mass, mass changes, chemical measurements, percentage yield,
atom economy, concentration in g/dm³, the mole, amounts in equations, and
using moles (titration, limiting reactants, empirical formulae).

The distractors are built from the errors, not from noise. Recurring sources:
Mr found by adding atomic numbers or by ignoring a bracket subscript; the
percentage-yield fraction inverted; atom economy taken over the reactants or
with the equation's coefficients dropped; cm³ used where dm³ is needed; a
molar ratio ignored or applied upside down; mass left in kilograms before
dividing by Mr; molecules counted where atoms were asked for.

⚠️ TIER DISCIPLINE. Seven of these subtopics are tier='foundation' and a
Foundation Combined class sits them. Moles are Higher-only in AQA Combined,
so NO foundation-tier question in this file — including the two triple_only
ones, percentage yield and atom economy — uses a mole anywhere in a stem, an
option or a `why`. Those questions reach their answers through mass ratios
and Mr values instead, which is exactly how AQA asks them at Foundation.

⚠️ `conservation-of-mass` is byte-identical to a KS3 lesson slug. Every
question under it here is written on symbol equations, coefficients, state
symbols and mass ratios — KS4 content that could not be mistaken for the KS3
lesson of the same name.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── conservation-of-mass ────────────────────────────────────────────
    {
        "id": "ks4-conservation-of-mass-e01",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a student is allowed to change when balancing a "
                "symbol equation.",
        "options": [
            "The small subscript numbers written inside a formula",
            "The chemical symbols used for the elements",
            "The large numbers written in front of the formulae",
            "The state symbols written after each formula",
        ],
        "correct_index": 2,
        "why": "Only the large numbers in front of a formula may be changed — "
               "they say how many units react, while a subscript is part of "
               "what the substance is.",
    },
    {
        "id": "ks4-conservation-of-mass-e02",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the equation Mg(s) + 2HCl(aq) → MgCl2(aq) + H2(g), "
                "state what the symbol (aq) tells you about the "
                "hydrochloric acid.",
        "options": [
            "It is dissolved in water",
            "It is a pure liquid at room temperature",
            "It is a gas given off during the reaction",
            "It is an insoluble solid at the bottom of the flask",
        ],
        "correct_index": 0,
        "why": "(aq) means aqueous — the substance is dissolved in water, "
               "which is how acids are supplied in the laboratory.",
    },
    {
        "id": "ks4-conservation-of-mass-e03",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a sealed flask, 4.6 g of sodium reacts completely with "
                "7.1 g of chlorine to form sodium chloride. Calculate the "
                "mass of sodium chloride formed.",
        "options": [
            "2.5 g",
            "7.1 g",
            "32.7 g",
            "11.7 g",
        ],
        "correct_index": 3,
        "why": "Mass is conserved, so the product weighs what the reactants "
               "weighed: 4.6 + 7.1 = 11.7 g.",
    },
    {
        "id": "ks4-conservation-of-mass-e04",
        "subtopic_slug": "conservation-of-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the balanced equation for the complete combustion "
                "of methane.",
        "options": [
            "CH4 + O2 → CO2 + 2H2O",
            "CH4 + 2O2 → CO2 + 2H2O",
            "CH4 + 2O2 → CO2 + H2O",
            "2CH4 + 2O2 → 2CO2 + 4H2O",
        ],
        "correct_index": 1,
        "why": "Only this equation has 1 C, 4 H and 4 O on each side — the "
               "two O2 molecules supply exactly the oxygen the CO2 and the "
               "two H2O need.",
    },
    {
        "id": "ks4-conservation-of-mass-s01",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Propane burns according to C3H8 + xO2 → 3CO2 + 4H2O. "
                "Determine the value of x.",
        "options": [
            "5",
            "3",
            "7",
            "10",
        ],
        "correct_index": 0,
        "why": "The right-hand side holds 6 + 4 = 10 oxygen atoms, and each "
               "O2 molecule supplies two of them, so 5 are needed.",
    },
    {
        "id": "ks4-conservation-of-mass-s02",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper carbonate decomposes in a sealed tube: CuCO3 → "
                "CuO + CO2. The tube holds 12.4 g of copper carbonate, and "
                "after heating 8.0 g of copper oxide remains. Calculate the "
                "mass of carbon dioxide made.",
        "options": [
            "20.4 g",
            "8.0 g",
            "12.4 g",
            "4.4 g",
        ],
        "correct_index": 3,
        "why": "Nothing can leave a sealed tube, so the carbon dioxide is "
               "the part of the 12.4 g that is no longer solid: "
               "12.4 − 8.0 = 4.4 g.",
    },
    {
        "id": "ks4-conservation-of-mass-s03",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sulfuric acid is neutralised by sodium hydroxide: H2SO4 + "
                "NaOH → Na2SO4 + H2O. Determine the set of coefficients "
                "that balances this equation, written in the order H2SO4, "
                "NaOH, Na2SO4, H2O.",
        "options": [
            "1, 1, 1, 1",
            "1, 2, 1, 2",
            "2, 1, 2, 1",
            "1, 2, 2, 1",
        ],
        "correct_index": 1,
        "why": "Na2SO4 needs two sodium atoms, so two NaOH are required, and "
               "the four hydrogen atoms then left over form two H2O.",
    },
    {
        "id": "ks4-conservation-of-mass-s04",
        "subtopic_slug": "conservation-of-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the reaction 2H2 + O2 → 2H2O, 4 g of hydrogen "
                "reacts exactly with 32 g of oxygen. Predict the mass of "
                "water formed when 2 g of hydrogen reacts completely.",
        "options": [
            "16 g",
            "34 g",
            "18 g",
            "36 g",
        ],
        "correct_index": 2,
        "why": "Half the hydrogen takes half the oxygen, and mass is "
               "conserved, so 2 g + 16 g = 18 g of water is formed.",
    },
    {
        "id": "ks4-conservation-of-mass-h01",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student balances the reaction of hydrogen with oxygen "
                "to make water by writing H2 + O2 → H2O2. Explain what is "
                "wrong with this answer.",
        "options": [
            "Nothing is wrong, because the atoms balance on both sides",
            "The atoms do balance, but the changed subscript makes hydrogen "
            "peroxide rather than water",
            "The atoms do not balance, because there is an extra oxygen atom "
            "on the right-hand side",
            "Coefficients must always be added, so it should read 2H2 + 2O2 "
            "→ 2H2O2",
        ],
        "correct_index": 1,
        "why": "Balancing may only change the numbers in front of a formula; "
               "changing a subscript writes down a different substance, and "
               "H2O2 is hydrogen peroxide, not water.",
    },
    {
        "id": "ks4-conservation-of-mass-h02",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iron is extracted by Fe2O3 + CO → Fe + CO2. Determine "
                "the coefficients that balance it, written in the order "
                "Fe2O3, CO, Fe, CO2.",
        "options": [
            "1, 1, 2, 1",
            "2, 3, 4, 3",
            "1, 3, 2, 3",
            "1, 2, 2, 2",
        ],
        "correct_index": 2,
        "why": "Three CO molecules are needed to carry away the three oxygen "
               "atoms in Fe2O3, giving three CO2 and leaving the two iron "
               "atoms behind.",
    },
    {
        "id": "ks4-conservation-of-mass-h03",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "5.0 g of calcium carbonate is added to 50.0 g of dilute "
                "hydrochloric acid in an open beaker and all of it reacts. "
                "The beaker and its contents lose 2.2 g in mass. Determine "
                "the total mass of all the products formed, including any "
                "gas.",
        "options": [
            "55.0 g",
            "52.8 g",
            "45.0 g",
            "2.2 g",
        ],
        "correct_index": 0,
        "why": "Mass is conserved, so the products together weigh what the "
               "reactants weighed, 5.0 + 50.0 = 55.0 g — the 2.2 g simply "
               "left the beaker as carbon dioxide.",
    },
    {
        "id": "ks4-conservation-of-mass-h04",
        "subtopic_slug": "conservation-of-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "9.2 g of sodium is heated in a sealed container with 9.6 g "
                "of sulfur. Sodium sulfide is the only product, 15.6 g of it "
                "forms, and some sulfur is left over. Calculate the mass of "
                "sulfur that did not react.",
        "options": [
            "6.4 g",
            "9.6 g",
            "0 g, because all the sulfur reacted",
            "3.2 g",
        ],
        "correct_index": 3,
        "why": "Nothing leaves a sealed container, so 9.2 + 9.6 = 18.8 g is "
               "still present, and 18.8 − 15.6 = 3.2 g of it is "
               "unreacted sulfur.",
    },

    # ── relative-formula-mass ───────────────────────────────────────────
    {
        "id": "ks4-relative-formula-mass-e01",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the relative formula mass (Mr) of ammonia, NH3. "
                "Ar: N = 14, H = 1.",
        "options": [
            "14",
            "17",
            "15",
            "42",
        ],
        "correct_index": 1,
        "why": "Mr is the sum of the Ar of every atom in the formula: "
               "14 + (3 × 1) = 17.",
    },
    {
        "id": "ks4-relative-formula-mass-e02",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the relative formula mass (Mr) of a compound is.",
        "options": [
            "The sum of the atomic numbers of all the atoms in the formula",
            "The mass of one molecule of the compound, measured in grams",
            "The mass of compound made in a reaction, measured in grams",
            "The sum of the relative atomic masses of all the atoms in the "
            "formula",
        ],
        "correct_index": 3,
        "why": "Mr adds up the Ar values, not the atomic numbers, and because "
               "it compares masses it has no units of its own.",
    },
    {
        "id": "ks4-relative-formula-mass-e03",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the Mr of sodium hydroxide, NaOH. Ar: Na = 23, "
                "O = 16, H = 1.",
        "options": [
            "40",
            "39",
            "24",
            "20",
        ],
        "correct_index": 0,
        "why": "Every atom in the formula counts: 23 + 16 + 1 = 40.",
    },
    {
        "id": "ks4-relative-formula-mass-e04",
        "subtopic_slug": "relative-formula-mass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the Mr of magnesium hydroxide, Mg(OH)2. Ar: "
                "Mg = 24, O = 16, H = 1.",
        "options": [
            "41",
            "82",
            "58",
            "40",
        ],
        "correct_index": 2,
        "why": "The 2 outside the bracket doubles the OH only: 24 + (2 × "
               "16) + (2 × 1) = 58.",
    },
    {
        "id": "ks4-relative-formula-mass-s01",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the Mr of ammonium sulfate, (NH4)2SO4. Ar: "
                "N = 14, H = 1, S = 32, O = 16.",
        "options": [
            "114",
            "116",
            "132",
            "228",
        ],
        "correct_index": 2,
        "why": "There are 2 N, 8 H, 1 S and 4 O: 28 + 8 + 32 + 64 = 132.",
    },
    {
        "id": "ks4-relative-formula-mass-s02",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A metal oxide has the formula MO and a relative formula "
                "mass of 81. Ar of oxygen = 16. Determine the relative "
                "atomic mass of the metal M.",
        "options": [
            "97",
            "65",
            "40.5",
            "16",
        ],
        "correct_index": 1,
        "why": "Mr = Ar(M) + Ar(O), so Ar(M) = 81 − 16 = 65.",
    },
    {
        "id": "ks4-relative-formula-mass-s03",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Iron reacts with sulfur: Fe + S → FeS. Ar: Fe = 56, S = 32, so 56 g of iron always combines with 32 g of sulfur to give 88 g of iron sulfide. Calculate the mass of iron sulfide formed from 14 g of iron.",
        "options": [
            "8.0 g",
            "46 g",
            "88 g",
            "22 g",
        ],
        "correct_index": 3,
        "why": "14 g is a quarter of 56 g, so it makes a quarter of the 88 g of iron sulfide — 22 g.",
    },
    {
        "id": "ks4-relative-formula-mass-s04",
        "subtopic_slug": "relative-formula-mass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the Mr of potassium carbonate, K2CO3. Ar: K = 39, "
                "C = 12, O = 16.",
        "options": [
            "138",
            "99",
            "90",
            "67",
        ],
        "correct_index": 0,
        "why": "Two potassium atoms and three oxygen atoms are needed: "
               "(2 × 39) + 12 + (3 × 16) = 138.",
    },
    {
        "id": "ks4-relative-formula-mass-h01",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the relative formula mass of iron(III) sulfate, "
                "Fe2(SO4)3. Ar: Fe = 56, S = 32, O = 16.",
        "options": [
            "152",
            "208",
            "304",
            "400",
        ],
        "correct_index": 3,
        "why": "The 3 outside the bracket multiplies both the S and the four "
               "O inside it: (2 × 56) + (3 × 32) + (12 × 16) "
               "= 400.",
    },
    {
        "id": "ks4-relative-formula-mass-h02",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the difference between the relative formula mass "
                "of ammonium nitrate, NH4NO3, and that of urea, CO(NH2)2. "
                "Ar: H = 1, C = 12, N = 14, O = 16.",
        "options": [
            "20",
            "36",
            "140",
            "0",
        ],
        "correct_index": 0,
        "why": "NH4NO3 comes to 14 + 4 + 14 + 48 = 80 and CO(NH2)2 to "
               "12 + 16 + (2 × [14 + 2]) = 60, a difference of 20.",
    },
    {
        "id": "ks4-relative-formula-mass-h03",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hydrocarbon has the formula CnH2n and a relative formula "
                "mass of 70. Ar: C = 12, H = 1. Determine the value of n.",
        "options": [
            "6",
            "3",
            "5",
            "35",
        ],
        "correct_index": 2,
        "why": "Each CH2 unit has a mass of 12 + 2 = 14, and 70 ÷ 14 = "
               "5.",
    },
    {
        "id": "ks4-relative-formula-mass-h04",
        "subtopic_slug": "relative-formula-mass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Zinc oxide is reduced by carbon: ZnO + C → Zn + CO. "
                "Ar: Zn = 65, O = 16. Calculate the mass of zinc produced "
                "when 16.2 g of zinc oxide is reduced completely.",
        "options": [
            "3.2 g",
            "13.0 g",
            "16.2 g",
            "20.2 g",
        ],
        "correct_index": 1,
        "why": "The Mr of ZnO is 81, of which 65 is zinc, so 16.2 × "
               "(65 ÷ 81) = 13.0 g of the sample is zinc.",
    },

    # ── mass-changes-reactions ──────────────────────────────────────────
    {
        "id": "ks4-mass-changes-reactions-e01",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction is carried out in an open beaker and the balance reading changes. State what a chemist should look for to explain the change.",
        "options": [
            "A gas that has entered or left the beaker during the reaction",
            "A mistake in the balanced symbol equation for the reaction",
            "A change in the temperature of the beaker and its contents",
            "A solid that has changed colour during the reaction",
        ],
        "correct_index": 0,
        "why": "Mass is always conserved, so a changed reading in an open vessel means matter crossed the boundary — and the only thing that can is a gas.",
    },
    {
        "id": "ks4-mass-changes-reactions-e02",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the correct statement about mass changes in chemical reactions.",
        "options": [
            "Mass is destroyed whenever a gas escapes from an open container",
            "Mass is created whenever a gas is absorbed from the air",
            "Mass is always conserved; only the mass inside the container changes",
            "Mass is conserved only when a reaction is run in a sealed container",
        ],
        "correct_index": 2,
        "why": "Atoms are never created or destroyed, so the total mass is fixed — what changes is how much of it is still inside the vessel being weighed.",
    },
    {
        "id": "ks4-mass-changes-reactions-e03",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes 'mass was destroyed in my experiment "
                "because the balance reading went down'. State the correct "
                "explanation.",
        "options": [
            "Mass really can be lost whenever a gas is made in a reaction",
            "Mass was conserved — a gas was made and escaped from the open "
            "container",
            "Mass was conserved — the balance had not been zeroed before the "
            "experiment",
            "Mass rose first and then fell, so the reading was simply "
            "misread",
        ],
        "correct_index": 1,
        "why": "Atoms are rearranged, never destroyed — the missing mass left "
               "the container as a gas and is still there, just not on the "
               "balance.",
    },
    {
        "id": "ks4-mass-changes-reactions-e04",
        "subtopic_slug": "mass-changes-reactions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper is heated in a sealed tube of air until it has turned black. Predict the balance reading for the sealed tube and its contents afterwards.",
        "options": [
            "It rises, because oxygen has joined onto the copper",
            "It falls, because a gas has been used up inside the tube",
            "It falls, because black copper oxide is lighter than copper",
            "It is unchanged, because the oxygen was already inside the sealed tube",
        ],
        "correct_index": 3,
        "why": "The solid does gain mass, but the oxygen came from air that was already on the balance, so the sealed tube as a whole weighs exactly the same.",
    },
    {
        "id": "ks4-mass-changes-reactions-s01",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An empty crucible has a mass of 25.00 g. 2.40 g of copper "
                "is added and heated in air until all of it has turned to "
                "black copper oxide. The crucible and contents then have a "
                "mass of 28.00 g. Calculate the mass of oxygen that combined "
                "with the copper.",
        "options": [
            "3.00 g",
            "2.40 g",
            "25.60 g",
            "0.60 g",
        ],
        "correct_index": 3,
        "why": "The solid gained mass because oxygen joined it: the copper "
               "oxide weighs 28.00 − 25.00 = 3.00 g, and 3.00 − "
               "2.40 = 0.60 g of that is oxygen.",
    },
    {
        "id": "ks4-mass-changes-reactions-s02",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats blue hydrated copper(II) sulfate crystals in an open crucible until they turn white. The balance reading falls from 34.60 g to 32.80 g. State what the 1.80 g represents.",
        "options": [
            "The mass of copper sulfate that decomposed into copper oxide",
            "The mass of water driven off from the crystals as steam",
            "The mass of oxygen given off from the sulfate in the crystals",
            "The mass destroyed by the heat of the Bunsen burner flame",
        ],
        "correct_index": 1,
        "why": "Heating the blue crystals drives off their water of crystallisation as steam, and it is that 1.80 g of water that leaves the crucible.",
    },
    {
        "id": "ks4-mass-changes-reactions-s03",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the reaction 2Cu + O2 → 2CuO, 16 g of oxygen "
                "combines with 127 g of copper. A student heats 12.7 g of "
                "copper in air until it has all reacted. Calculate the "
                "increase in mass of the solid.",
        "options": [
            "12.7 g",
            "16 g",
            "1.6 g",
            "14.3 g",
        ],
        "correct_index": 2,
        "why": "The solid gains exactly the mass of oxygen added, and one "
               "tenth of 127 g of copper takes one tenth of 16 g of oxygen — "
               "1.6 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-s04",
        "subtopic_slug": "mass-changes-reactions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A candle burns in an open dish on a balance and the reading "
                "falls steadily. Explain why this does not break the law of "
                "conservation of mass.",
        "options": [
            "Carbon dioxide and water vapour drift away, so they are no "
            "longer weighed",
            "Burning turns some of the wax into energy, so that mass is "
            "genuinely lost",
            "The heat makes the balance read low, so the mass has not really "
            "changed",
            "Oxygen from the air is used up, so the total mass of the room "
            "falls",
        ],
        "correct_index": 0,
        "why": "The wax's atoms end up in carbon dioxide and water vapour "
               "that leave the dish — the mass still exists, it is just not "
               "on the balance.",
    },
    {
        "id": "ks4-mass-changes-reactions-h01",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium hydrogencarbonate is heated in a sealed rigid "
                "container: 2NaHCO3 → Na2CO3 + H2O + CO2. The container "
                "is weighed before heating, again while still sealed after "
                "heating, and again once the lid is removed. Predict the "
                "three readings.",
        "options": [
            "The reading falls during heating, then falls again when the lid "
            "is removed",
            "The reading rises during heating, then falls when the lid is "
            "removed",
            "The reading is unchanged during heating, then falls when the "
            "lid is removed",
            "The reading is unchanged during heating and unchanged when the "
            "lid is removed",
        ],
        "correct_index": 2,
        "why": "While sealed nothing can leave, so the mass holds; opening "
               "the lid releases the carbon dioxide and water vapour and the "
               "reading then drops.",
    },
    {
        "id": "ks4-mass-changes-reactions-h02",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats 10.00 g of green copper carbonate in an "
                "open crucible until no further change occurs and records a "
                "final mass of 6.40 g. The student concludes that 3.60 g of "
                "the sample must have been impurity. Evaluate this "
                "conclusion.",
        "options": [
            "Correct, because anything lost from an open crucible must be an "
            "impurity",
            "Correct, because copper carbonate itself does not decompose on "
            "heating",
            "Incorrect, because the mass should have risen as oxygen was "
            "absorbed from the air",
            "Incorrect, because the copper carbonate decomposes and the "
            "carbon dioxide escapes",
        ],
        "correct_index": 3,
        "why": "CuCO3 → CuO + CO2, and the carbon dioxide leaves the "
               "open crucible, so the missing 3.60 g is gas from the "
               "reaction, not impurity.",
    },
    {
        "id": "ks4-mass-changes-reactions-h03",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "6.20 g of a metal carbonate is heated in an open tube until "
                "it fully decomposes to the metal oxide and carbon dioxide. "
                "The tube and contents fall from 48.20 g to 45.98 g. "
                "Calculate the mass of metal oxide left in the tube.",
        "options": [
            "3.98 g",
            "2.22 g",
            "6.20 g",
            "45.98 g",
        ],
        "correct_index": 0,
        "why": "The 2.22 g lost is the carbon dioxide that escaped, so the "
               "oxide left behind is 6.20 − 2.22 = 3.98 g.",
    },
    {
        "id": "ks4-mass-changes-reactions-h04",
        "subtopic_slug": "mass-changes-reactions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same reaction between magnesium and dilute hydrochloric "
                "acid is run twice on a balance: once in an open conical "
                "flask, and once in a stoppered flask joined to a gas "
                "syringe. Compare the final balance readings.",
        "options": [
            "Both readings fall, because hydrogen is made in both "
            "experiments",
            "The open flask reading falls; the sealed apparatus reading is "
            "unchanged",
            "The open flask reading is unchanged; the sealed apparatus "
            "reading rises",
            "Both readings are unchanged, because mass is always conserved "
            "in a reaction",
        ],
        "correct_index": 1,
        "why": "Hydrogen escapes the open flask and stops being weighed, but "
               "in the sealed apparatus it is still inside and still on the "
               "balance.",
    },

    # ── chemical-measurements ───────────────────────────────────────────
    {
        "id": "ks4-chemical-measurements-e01",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student repeats a titration four times and records 24.10, "
                "24.15, 24.10 and 24.15 cm³. The true value is 25.00 cm³. "
                "Describe these results.",
        "options": [
            "Accurate and precise",
            "Accurate but not precise",
            "Neither accurate nor precise",
            "Precise but not accurate",
        ],
        "correct_index": 3,
        "why": "The readings agree closely with one another, which is "
               "precision, but they all sit well below the true value, which "
               "points to a systematic error.",
    },
    {
        "id": "ks4-chemical-measurements-e02",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student times the same reaction four times and records 42 s, 45 s, 41 s and 44 s. Identify the type of error that causes this scatter.",
        "options": [
            "A systematic error, because the stopwatch runs fast",
            "A random error, from starting and stopping the stopwatch by hand",
            "A reading error, because the stopwatch displays too many digits",
            "A zero error, because the stopwatch was not reset before the first run",
        ],
        "correct_index": 1,
        "why": "The readings scatter above and below a middle value rather than all shifting the same way, which is the signature of random error.",
    },
    {
        "id": "ks4-chemical-measurements-e03",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A balance reads 0.02 g with nothing on it and a student "
                "uses it without taring. Identify the type of error this "
                "produces.",
        "options": [
            "A random error, because the reading varies from trial to trial",
            "A reading error, because the scale is difficult to read "
            "accurately",
            "A systematic error, because every mass recorded is 0.02 g too "
            "high",
            "No error at all, because 0.02 g is too small to make a "
            "difference",
        ],
        "correct_index": 2,
        "why": "An unzeroed balance shifts every reading by the same amount "
               "in the same direction, and that is what makes an error "
               "systematic.",
    },
    {
        "id": "ks4-chemical-measurements-e04",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures out 250 cm³ of solution. State this "
                "volume in dm³.",
        "options": [
            "0.250 dm³",
            "2.50 dm³",
            "25.0 dm³",
            "250000 dm³",
        ],
        "correct_index": 0,
        "why": "1 dm³ is 1000 cm³, so a volume in cm³ is converted by "
               "dividing by 1000.",
    },
    {
        "id": "ks4-chemical-measurements-s01",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thermometer has an uncertainty of ±0.5 °C. A student "
                "records a temperature of 20.0 °C. Calculate the percentage "
                "uncertainty in this reading.",
        "options": [
            "0.025%",
            "2.5%",
            "25%",
            "40%",
        ],
        "correct_index": 1,
        "why": "Percentage uncertainty = (uncertainty ÷ measured value) × "
               "100 = (0.5 ÷ 20.0) × 100 = 2.5%.",
    },
    {
        "id": "ks4-chemical-measurements-s02",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A balance reads to ±0.01 g. A student can weigh out either "
                "0.20 g or 2.00 g of a solid for a reaction. Explain which "
                "mass gives the smaller percentage uncertainty.",
        "options": [
            "2.00 g, because the same ±0.01 g is a smaller fraction of a "
            "larger mass",
            "0.20 g, because a smaller mass is easier for the balance to "
            "weigh",
            "Both are the same, because the balance uncertainty is ±0.01 g "
            "either way",
            "0.20 g, because less solid means less of it can be spilled in "
            "transfer",
        ],
        "correct_index": 0,
        "why": "Percentage uncertainty is the uncertainty divided by the "
               "measurement, so a fixed ±0.01 g matters ten times less on "
               "2.00 g than on 0.20 g.",
    },
    {
        "id": "ks4-chemical-measurements-s03",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures the volume of gas produced four times "
                "and records 48 cm³, 50 cm³, 49 cm³ and 71 cm³. Describe how "
                "the mean should be calculated.",
        "options": [
            "Take the mean of all four results, giving 54.5 cm³",
            "Take the mean of the two smallest results, giving 48.5 cm³",
            "Take the largest result, 71 cm³, because gas can only be lost",
            "Discard 71 cm³ as anomalous and average the rest, giving 49 cm³",
        ],
        "correct_index": 3,
        "why": "An anomalous result lies far outside the others and is left "
               "out before averaging, so the mean of 48, 50 and 49 cm³ is "
               "49 cm³.",
    },
    {
        "id": "ks4-chemical-measurements-s04",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A burette is filled and the initial reading is 1.40 cm³. "
                "After the titration the final reading is 26.75 cm³. "
                "Calculate the volume of solution added.",
        "options": [
            "26.75 cm³",
            "28.15 cm³",
            "25.35 cm³",
            "1.40 cm³",
        ],
        "correct_index": 2,
        "why": "A burette gives a volume by difference: final reading minus "
               "initial reading, 26.75 − 1.40 = 25.35 cm³.",
    },
    {
        "id": "ks4-chemical-measurements-h01",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'I weighed 5.00 g on a balance of uncertainty ±0.02 g, so my percentage uncertainty is 0.02 ÷ 5.00 = 0.004%.' Identify the error in this working.",
        "options": [
            "The result was not multiplied by 100 — the uncertainty is 0.4%",
            "The uncertainty should be doubled first — the answer is 0.008%",
            "The mass should be divided by the uncertainty — the answer is 250%",
            "There is no error in the working — 0.004% is correct as written",
        ],
        "correct_index": 0,
        "why": "0.02 ÷ 5.00 = 0.004 is a fraction, and a fraction only becomes a percentage when it is multiplied by 100, giving 0.4%.",
    },
    {
        "id": "ks4-chemical-measurements-h02",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A balance displays masses to three decimal places, but "
                "repeated weighings of the same object give 4.512, 4.517, "
                "4.509 and 4.515 g. Explain what these results show.",
        "options": [
            "The balance is faulty, because a three decimal place balance "
            "should repeat exactly",
            "The balance has a systematic error, because all four readings "
            "differ from each other",
            "The balance has a fine resolution but the readings still carry "
            "a random uncertainty of about ±0.005 g",
            "The readings should be rounded to one decimal place, because "
            "the extra figures are meaningless",
        ],
        "correct_index": 2,
        "why": "A fine display shows small differences but does not remove "
               "them — the scatter of about ±0.005 g around the mean is "
               "random uncertainty, not a fault.",
    },
    {
        "id": "ks4-chemical-measurements-h03",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A method needs 1.00 g of a solid weighed to within 1%. The "
                "only balance available reads to ±0.02 g. Determine whether "
                "the balance is good enough, and state the percentage "
                "uncertainty.",
        "options": [
            "Yes — the percentage uncertainty is 0.2%, comfortably below 1%",
            "No — the percentage uncertainty is 2%, which is above 1%",
            "Yes — the percentage uncertainty is 0.02%, far below 1%",
            "No — the percentage uncertainty is 50%, far above 1%",
        ],
        "correct_index": 1,
        "why": "(0.02 ÷ 1.00) × 100 = 2%, twice what the method allows, "
               "so a more precise balance is needed.",
    },
    {
        "id": "ks4-chemical-measurements-h04",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student's percentage uncertainty in a mass measurement is "
                "too large and the balance cannot be changed. Suggest the "
                "change to the method that reduces it most.",
        "options": [
            "Record every mass to one more decimal place than the balance "
            "displays",
            "Repeat the weighing several times and take the mean of the "
            "readings",
            "Use a different balance of the same precision in another "
            "laboratory",
            "Scale the experiment up so that a larger mass of solid is "
            "weighed out",
        ],
        "correct_index": 3,
        "why": "The balance's ± uncertainty is fixed, so weighing a larger "
               "mass makes that fixed amount a smaller fraction of the "
               "reading.",
    },

    # ── percentage-yield ────────────────────────────────────────────────
    {
        "id": "ks4-percentage-yield-e01",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by the actual yield of a reaction.",
        "options": [
            "The largest mass of product the balanced equation predicts",
            "The mass of the reactants used at the start of the reaction",
            "The mass of product actually collected at the end of the "
            "experiment",
            "The mass of product written as a percentage of the reactants",
        ],
        "correct_index": 2,
        "why": "The actual yield is what is really collected and weighed, "
               "which is why it can be compared with the theoretical "
               "maximum.",
    },
    {
        "id": "ks4-percentage-yield-e02",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the equation used to calculate percentage yield.",
        "options": [
            "(theoretical yield ÷ actual yield) × 100",
            "(actual yield ÷ mass of reactants) × 100",
            "(theoretical yield − actual yield) ÷ 100",
            "(actual yield ÷ theoretical yield) × 100",
        ],
        "correct_index": 3,
        "why": "Percentage yield compares what was obtained with the most "
               "that could have been obtained, so the actual yield goes on "
               "top.",
    },
    {
        "id": "ks4-percentage-yield-e03",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction has a theoretical yield of 45.0 g of product and "
                "a student collects 36.0 g. Calculate the percentage yield.",
        "options": [
            "80.0%",
            "125.0%",
            "20.0%",
            "9.0%",
        ],
        "correct_index": 0,
        "why": "Percentage yield = (actual ÷ theoretical) × 100 = "
               "(36.0 ÷ 45.0) × 100 = 80.0%.",
    },
    {
        "id": "ks4-percentage-yield-e04",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a calculated percentage yield of 110% must mean "
                "a mistake has been made.",
        "options": [
            "Because a percentage can never be greater than 100 in any "
            "calculation",
            "Because you cannot collect more product than the reactants are "
            "able to make",
            "Because the balance would have to be broken to give such a "
            "reading",
            "Because the reaction would have to be reversible to make the "
            "extra product",
        ],
        "correct_index": 1,
        "why": "The theoretical yield is the most the atoms in the reactants "
               "can make, so exceeding it usually means the product was "
               "impure or still wet.",
    },
    {
        "id": "ks4-percentage-yield-s01",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The theoretical yield of aspirin in a preparation is 18.0 g "
                "and the percentage yield is 65%. Calculate the mass of "
                "aspirin collected.",
        "options": [
            "11.7 g",
            "27.7 g",
            "6.3 g",
            "1170 g",
        ],
        "correct_index": 0,
        "why": "Actual yield = theoretical × (percentage ÷ 100) = "
               "18.0 × 0.65 = 11.7 g.",
    },
    {
        "id": "ks4-percentage-yield-s02",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student obtains 21.0 g of copper sulfate crystals, which "
                "is a percentage yield of 70%. Calculate the theoretical "
                "yield.",
        "options": [
            "14.7 g",
            "30.0 g",
            "9.0 g",
            "6.3 g",
        ],
        "correct_index": 1,
        "why": "The 21.0 g is 70% of the theoretical yield, so the "
               "theoretical yield is 21.0 ÷ 0.70 = 30.0 g.",
    },
    {
        "id": "ks4-percentage-yield-s03",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student repeats a preparation twice, using the same masses and the same method, and obtains percentage yields of 61% and 84%. Suggest what this shows.",
        "options": [
            "The theoretical yield must have been different in the two experiments",
            "The second experiment made more product than the equation allows",
            "The chemistry was the same both times, so the difference is in the handling of the product",
            "The reaction is reversible, and reversibility varies at random between experiments",
        ],
        "correct_index": 2,
        "why": "The theoretical yield is fixed by the equation and the masses used, so a different result twice over comes from how the product was transferred, filtered and dried.",
    },
    {
        "id": "ks4-percentage-yield-s04",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Student A collects 8.0 g from a theoretical yield of "
                "10.0 g. Student B collects 12.0 g from a theoretical yield "
                "of 16.0 g. Determine who had the higher percentage yield.",
        "options": [
            "Student B, at 133%",
            "Student B, at 75%",
            "Student A, at 125%",
            "Student A, at 80%",
        ],
        "correct_index": 3,
        "why": "A collected 8.0 of a possible 10.0 g, which is 80%, while B "
               "collected 12.0 of a possible 16.0 g, which is only 75%.",
    },
    {
        "id": "ks4-percentage-yield-h01",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calcium carbonate decomposes: CaCO3 → CaO + CO2. The "
                "Mr values are CaCO3 = 100 and CaO = 56, so 100 g of "
                "calcium carbonate gives at most 56 g of calcium oxide. A "
                "student heats 25.0 g of calcium carbonate and collects "
                "11.2 g of calcium oxide. Calculate the percentage yield.",
        "options": [
            "44.8%",
            "20.0%",
            "125.0%",
            "80.0%",
        ],
        "correct_index": 3,
        "why": "25.0 g of the carbonate can give at most 25.0 × "
               "(56 ÷ 100) = 14.0 g of oxide, and (11.2 ÷ 14.0) × "
               "100 = 80.0%.",
    },
    {
        "id": "ks4-percentage-yield-h02",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A factory must supply 600 tonnes of a product each month and its process runs at a percentage yield of 75%. Calculate the mass of product the process must be capable of making on paper each month.",
        "options": [
            "450 tonnes",
            "675 tonnes",
            "800 tonnes",
            "750 tonnes",
        ],
        "correct_index": 2,
        "why": "The 600 tonnes collected is 75% of what the reaction could give, so the theoretical output must be 600 ÷ 0.75 = 800 tonnes.",
    },
    {
        "id": "ks4-percentage-yield-h03",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the Haber process, N2 + 3H2 ⇌ 2NH3, only about 15% of "
                "the gases are converted to ammonia on each pass through the "
                "reactor, yet the overall yield of the process is about 98%. "
                "Explain how both figures can be true.",
        "options": [
            "The 15% is the atom economy and the 98% is the percentage yield",
            "The unreacted nitrogen and hydrogen are separated and passed "
            "through again",
            "The reaction stops being reversible once 98% of the gas has "
            "reacted",
            "Adding a catalyst turns the 15% conversion into 98% in a single "
            "pass",
        ],
        "correct_index": 1,
        "why": "The reaction is reversible so it never completes in one pass, "
               "but recycling the unreacted gases means almost all of them "
               "eventually become ammonia.",
    },
    {
        "id": "ks4-percentage-yield-h04",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'My theoretical yield was 12.0 g and I "
                "collected 15.0 g, so my percentage yield is "
                "(12.0 ÷ 15.0) × 100 = 80%.' Evaluate this working.",
        "options": [
            "The fraction is upside down: it gives 125%, so the product must "
            "have been impure or still wet",
            "The working is correct, because 80% is a normal percentage "
            "yield for a school preparation",
            "The theoretical yield should be changed to 15.0 g, which gives "
            "a percentage yield of 100%",
            "Percentage yield is always the smaller mass divided by the "
            "larger one, so 80% is right",
        ],
        "correct_index": 0,
        "why": "Percentage yield is actual ÷ theoretical, giving "
               "(15.0 ÷ 12.0) × 100 = 125% — and a figure above 100% "
               "means the weighed product was not pure dry product.",
    },

    # ── atom-economy ────────────────────────────────────────────────────
    {
        "id": "ks4-atom-economy-e01",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the equation that gives the atom economy of a "
                "reaction.",
        "options": [
            "(Mr of desired product ÷ Mr of all reactants) × 100",
            "(Mr of desired product ÷ sum of Mr of all products) × 100",
            "(actual yield ÷ theoretical yield) × 100",
            "(Mr of waste products ÷ Mr of desired product) × 100",
        ],
        "correct_index": 1,
        "why": "Atom economy compares the mass of the useful product with the "
               "mass of everything the equation produces, waste included.",
    },
    {
        "id": "ks4-atom-economy-e02",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a reaction that forms two products can never have an atom economy of 100%.",
        "options": [
            "Some of the product mass is always the second product, which is waste",
            "Some of the reactant mass is always lost as heat energy in the reaction",
            "Two products always share the mass equally, so the answer is always 50%",
            "The second product always has a larger Mr than the desired product",
        ],
        "correct_index": 0,
        "why": "Atom economy is the desired product's share of the total product mass, and a second product always takes some of that share.",
    },
    {
        "id": "ks4-atom-economy-e03",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Hydrogen chloride is made by NaCl + H2SO4 → NaHSO4 + HCl. Mr: HCl = 36.5, NaHSO4 = 120. Calculate the atom economy for hydrogen chloride.",
        "options": [
            "76.7%",
            "30.4%",
            "329%",
            "23.3%",
        ],
        "correct_index": 3,
        "why": "Both products go on the bottom of the fraction: (36.5 ÷ (36.5 + 120)) × 100 = 23.3%.",
    },
    {
        "id": "ks4-atom-economy-e04",
        "subtopic_slug": "atom-economy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two reactions make the same desired product. Reaction 1 forms it on its own. Reaction 2 forms it together with a waste gas. Determine which has the higher atom economy.",
        "options": [
            "Reaction 2, because making a gas removes the waste from the mixture",
            "They are the same, because the desired product is the same in both",
            "Reaction 1, because all of the product mass is the useful product",
            "It cannot be decided without knowing the percentage yield of each",
        ],
        "correct_index": 2,
        "why": "With only one product, none of the product mass is waste, so the atom economy is as high as it can be.",
    },
    {
        "id": "ks4-atom-economy-s01",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Hydrogen is made by reacting methane with steam: CH4 + "
                "H2O → CO + 3H2. Mr: CO = 28, H2 = 2. Calculate the atom "
                "economy for hydrogen.",
        "options": [
            "5.9%",
            "7.1%",
            "82.4%",
            "17.6%",
        ],
        "correct_index": 3,
        "why": "Three H2 molecules are made, so the desired mass is 3 × 2 "
               "= 6 out of a total product mass of 28 + 6 = 34: "
               "(6 ÷ 34) × 100 = 17.6%.",
    },
    {
        "id": "ks4-atom-economy-s02",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Copper can be obtained two ways. Route A: 2CuO + C → "
                "2Cu + CO2. Route B: CuO + H2 → Cu + H2O. Mr: Cu = 63.5, "
                "CO2 = 44, H2O = 18. Determine which route has the higher "
                "atom economy for copper.",
        "options": [
            "Route A, at 74.3%",
            "Route A, at 25.7%",
            "Route B, at 77.9%",
            "Route B, at 22.1%",
        ],
        "correct_index": 2,
        "why": "Route B puts 63.5 of every 81.5 units of product mass into "
               "copper, which is 77.9%, against Route A's 127 out of 171, "
               "which is 74.3%.",
    },
    {
        "id": "ks4-atom-economy-s03",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Titanium is extracted by TiCl4 + 2Mg → Ti + 2MgCl2. "
                "Mr: Ti = 48, MgCl2 = 95. Calculate the atom economy for "
                "titanium.",
        "options": [
            "20.2%",
            "33.6%",
            "79.8%",
            "48.0%",
        ],
        "correct_index": 0,
        "why": "Two MgCl2 form for every Ti, so the total product mass is "
               "48 + (2 × 95) = 238, and (48 ÷ 238) × 100 = 20.2%.",
    },
    {
        "id": "ks4-atom-economy-s04",
        "subtopic_slug": "atom-economy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An industrial reaction has an atom economy of 32%. Explain "
                "what this means for the company running it.",
        "options": [
            "Only 32% of the product collected is pure, so it must be "
            "purified further",
            "About 68% of the mass of the products is waste that must be "
            "treated or sold",
            "The reaction only reaches 32% completion, so 68% of the "
            "reactants are left",
            "The reaction has to be repeated three times to use up all the "
            "reactants",
        ],
        "correct_index": 1,
        "why": "Atom economy is the share of the product mass that is useful, "
               "so 68% of what this reaction makes is by-product the company "
               "must deal with.",
    },
    {
        "id": "ks4-atom-economy-h01",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Hydrogen can be made two ways. Route 1: Mg + 2HCl → MgCl2 + H2 (Mr: MgCl2 = 95, H2 = 2). Route 2: 2H2O → 2H2 + O2 (Mr: H2 = 2, O2 = 32). Determine the atom economy of each route for hydrogen.",
        "options": [
            "Route 1 = 2.1%, Route 2 = 5.9%",
            "Route 1 = 97.9%, Route 2 = 88.9%",
            "Route 1 = 2.1%, Route 2 = 11.1%",
            "Route 1 = 11.1%, Route 2 = 2.1%",
        ],
        "correct_index": 2,
        "why": "Route 1 puts only 2 of every 97 units of product mass into hydrogen, which is 2.1%, while electrolysis puts 4 of every 36, which is 11.1%.",
    },
    {
        "id": "ks4-atom-economy-h02",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Reaction X has an atom economy of 95% and a percentage "
                "yield of 40%. Reaction Y has an atom economy of 50% and a "
                "percentage yield of 95%. Evaluate which statement about "
                "them is correct.",
        "options": [
            "Reaction X wastes more atoms as by-products, because its "
            "percentage yield is lower",
            "Reaction X wastes little as by-product but loses most of its "
            "product in practice",
            "Reaction Y is better in every way, because 95% is larger than "
            "40%",
            "Reaction Y has the higher atom economy in practice, because its "
            "yield is higher",
        ],
        "correct_index": 1,
        "why": "Atom economy counts atoms lost to by-products in the "
               "equation, while percentage yield counts product lost in the "
               "laboratory — X is efficient on paper but poor in practice.",
    },
    {
        "id": "ks4-atom-economy-h03",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student calculates the atom economy for hydrogen in Zn + "
                "2HCl → ZnCl2 + H2 as (2 ÷ (65 + 2)) × 100 = 3.0%. "
                "Mr: ZnCl2 = 136, H2 = 2. Identify the error.",
        "options": [
            "The Mr of hydrogen should be 1 rather than 2, so the answer is "
            "1.5%",
            "Zinc chloride is the desired product here, so the answer should "
            "be 98.6%",
            "The reaction has 100% atom economy, because hydrogen is the "
            "only gas made",
            "The Mr of zinc was used instead of the product ZnCl2: "
            "(2 ÷ 138) × 100 = 1.4%",
        ],
        "correct_index": 3,
        "why": "The bottom of the fraction is the total mass of the PRODUCTS, "
               "ZnCl2 (136) plus H2 (2) = 138, giving 1.4%.",
    },
    {
        "id": "ks4-atom-economy-h04",
        "subtopic_slug": "atom-economy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pharmaceutical company can make a drug by a route with "
                "88% atom economy that needs a rare, expensive catalyst, or "
                "by a route with 41% atom economy using cheap reagents. "
                "Evaluate the atom economy argument.",
        "options": [
            "The 88% route wastes far less raw material, though cost and "
            "safety also affect the choice",
            "The 41% route is better, because atom economy only matters when "
            "the waste is harmful",
            "The 88% route must have the higher percentage yield too, so it "
            "is better in every way",
            "Atom economy is irrelevant for medicines, because only the "
            "purity of the drug matters",
        ],
        "correct_index": 0,
        "why": "A high atom economy means less waste per unit of product, "
               "which is worth pursuing, but it is one factor alongside "
               "cost, safety and what the by-products are.",
    },

    # ── concentration-of-solutions ──────────────────────────────────────
    {
        "id": "ks4-concentration-of-solutions-e01",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the concentration of a solution measures.",
        "options": [
            "The mass of solute dissolved in each unit volume of solution",
            "The total mass of the solution, including all of the solvent",
            "The volume of solvent that was used to dissolve the solute",
            "The mass of solute that dissolves before the solution is "
            "saturated",
        ],
        "correct_index": 0,
        "why": "Concentration is mass of solute divided by volume of "
               "solution, so it says how much solute each dm³ carries.",
    },
    {
        "id": "ks4-concentration-of-solutions-e02",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 3.0 dm³ batch of squash contains 18 g of dissolved citric acid. Calculate its concentration in g/dm³.",
        "options": [
            "54 g/dm³",
            "0.17 g/dm³",
            "21 g/dm³",
            "6.0 g/dm³",
        ],
        "correct_index": 3,
        "why": "Concentration = mass ÷ volume = 18 ÷ 3.0 = 6.0 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-e03",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two beakers each hold 1 dm³ of copper sulfate solution. "
                "Beaker A contains 5 g of copper sulfate and beaker B "
                "contains 40 g. Compare the two solutions.",
        "options": [
            "A is more concentrated, because it has less solute in the way",
            "They are equally concentrated, because the volumes are the same",
            "B is more concentrated, because it holds more solute in the "
            "same volume",
            "B is more dilute, because more solute spreads the particles "
            "further apart",
        ],
        "correct_index": 2,
        "why": "With equal volumes, the beaker holding more dissolved solute "
               "is the more concentrated — 40 g/dm³ against 5 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-e04",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the mass of solute present in 2.0 dm³ of a solution whose concentration is 25 g/dm³.",
        "options": [
            "12.5 g",
            "50 g",
            "27 g",
            "0.08 g",
        ],
        "correct_index": 1,
        "why": "Mass = concentration × volume = 25 × 2.0 = 50 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-s01",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student weighs out 6.0 g of potassium nitrate and makes it up to 200 cm³ with water in a volumetric flask. Calculate the concentration of the solution in g/dm³.",
        "options": [
            "0.030 g/dm³",
            "1200 g/dm³",
            "30 g/dm³",
            "3.0 g/dm³",
        ],
        "correct_index": 2,
        "why": "200 cm³ is 0.200 dm³, so the concentration is 6.0 ÷ 0.200 = 30 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s02",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solution of concentration 15 g/dm³ contains 9.0 g of "
                "solute. Calculate the volume of the solution in cm³.",
        "options": [
            "600 cm³",
            "0.60 cm³",
            "135 cm³",
            "1670 cm³",
        ],
        "correct_index": 0,
        "why": "Volume = mass ÷ concentration = 9.0 ÷ 15 = 0.60 dm³, and "
               "0.60 dm³ is 600 cm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s03",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "200 cm³ of a solution of concentration 30 g/dm³ is diluted with water to a total volume of 800 cm³. Calculate the new concentration.",
        "options": [
            "10 g/dm³",
            "7.5 g/dm³",
            "30 g/dm³",
            "120 g/dm³",
        ],
        "correct_index": 1,
        "why": "Diluting adds no solute — the 30 × 0.200 = 6.0 g of solute now sits in 0.800 dm³, so the concentration is 7.5 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s04",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the mass of glucose needed to make 750 cm³ of a "
                "solution of concentration 12 g/dm³.",
        "options": [
            "9000 g",
            "0.016 g",
            "16 g",
            "9.0 g",
        ],
        "correct_index": 3,
        "why": "Mass = concentration × volume in dm³ = 12 × 0.750 = "
               "9.0 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-h01",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "24 g of copper sulfate is dissolved to make 400 cm³ of "
                "solution. 100 cm³ of this solution is then made up to "
                "500 cm³ with water. Calculate the concentration of the "
                "final solution.",
        "options": [
            "6.0 g/dm³",
            "12 g/dm³",
            "48 g/dm³",
            "60 g/dm³",
        ],
        "correct_index": 1,
        "why": "The stock is 24 ÷ 0.400 = 60 g/dm³, so 100 cm³ of it holds "
               "6.0 g, and spreading that through 0.500 dm³ gives "
               "12 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h02",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Solution P holds 18 g of solute in 300 cm³. Solution Q "
                "holds 30 g of solute in 600 cm³. Determine which is the "
                "more concentrated.",
        "options": [
            "Q, because it contains more solute than P does",
            "They are equally concentrated as solutions",
            "Q, at 50 g/dm³ against P's 18 g/dm³",
            "P, at 60 g/dm³ against Q's 50 g/dm³",
        ],
        "correct_index": 3,
        "why": "Concentration compares solute with volume: P is 18 ÷ 0.300 "
               "= 60 g/dm³ while Q is only 30 ÷ 0.600 = 50 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h03",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student evaporates 40 cm³ of a salt solution to dryness "
                "and is left with 1.2 g of salt. Calculate the concentration "
                "of the original solution in g/dm³.",
        "options": [
            "30 g/dm³",
            "0.030 g/dm³",
            "48 g/dm³",
            "33 g/dm³",
        ],
        "correct_index": 0,
        "why": "40 cm³ is 0.040 dm³, and all the solute is now weighed, so "
               "the concentration was 1.2 ÷ 0.040 = 30 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h04",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student has a 200 g/dm³ stock solution and must prepare "
                "250 cm³ of a 20 g/dm³ solution. Determine the volume of "
                "stock needed.",
        "options": [
            "2.5 cm³",
            "50 cm³",
            "25 cm³",
            "100 cm³",
        ],
        "correct_index": 2,
        "why": "250 cm³ of 20 g/dm³ needs 20 × 0.250 = 5.0 g of solute, and "
               "5.0 g is carried by 5.0 ÷ 200 = 0.025 dm³, that is "
               "25 cm³, of stock.",
    },

    # ── moles ───────────────────────────────────────────────────────────
    {
        "id": "ks4-moles-e01",
        "subtopic_slug": "moles",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the number of particles contained in one mole of any "
                "substance.",
        "options": [
            "1 000 000",
            "12",
            "6.02 × 10⁻²³",
            "6.02 × 10²³",
        ],
        "correct_index": 3,
        "why": "One mole always contains the Avogadro number of particles, "
               "6.02 × 10²³, whatever the substance is.",
    },
    {
        "id": "ks4-moles-e02",
        "subtopic_slug": "moles",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what the molar mass of a substance is.",
        "options": [
            "The mass of one molecule of the substance, measured in grams",
            "The mass of 12 g of the substance divided by its relative formula mass",
            "The mass in grams of one mole of the substance, equal to its Mr",
            "The number of particles contained in one gram of the substance",
        ],
        "correct_index": 2,
        "why": "One mole of a substance weighs its relative formula mass in grams, so an Mr of 58.5 means a molar mass of 58.5 g/mol.",
    },
    {
        "id": "ks4-moles-e03",
        "subtopic_slug": "moles",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A sample of calcium has a mass of 30 g. Ar of Ca = 40. Calculate the number of moles of calcium atoms in the sample.",
        "options": [
            "1.33 mol",
            "0.75 mol",
            "1200 mol",
            "40 mol",
        ],
        "correct_index": 1,
        "why": "Moles = mass ÷ Ar = 30 ÷ 40 = 0.75 mol.",
    },
    {
        "id": "ks4-moles-e04",
        "subtopic_slug": "moles",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate the mass of 0.25 mol of magnesium oxide, MgO. "
                "Mr = 40.",
        "options": [
            "10 g",
            "160 g",
            "40 g",
            "0.0063 g",
        ],
        "correct_index": 0,
        "why": "Mass = moles × Mr = 0.25 × 40 = 10 g.",
    },
    {
        "id": "ks4-moles-s01",
        "subtopic_slug": "moles",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A steel component contains 1.12 kg of iron. Ar of Fe = 56. Calculate the number of moles of iron atoms it contains.",
        "options": [
            "0.020 mol",
            "20 mol",
            "62.7 mol",
            "0.050 mol",
        ],
        "correct_index": 1,
        "why": "The mass must be in grams before dividing by Ar: 1.12 kg is 1120 g, and 1120 ÷ 56 = 20 mol.",
    },
    {
        "id": "ks4-moles-s02",
        "subtopic_slug": "moles",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate the number of molecules in 0.20 mol of oxygen "
                "gas, O2. The Avogadro constant is 6.02 × 10²³ mol⁻¹.",
        "options": [
            "3.01 × 10²⁴",
            "6.02 × 10²³",
            "2.41 × 10²³",
            "1.20 × 10²³",
        ],
        "correct_index": 3,
        "why": "Number of particles = moles × 6.02 × 10²³ = 0.20 × "
               "6.02 × 10²³ = 1.20 × 10²³ molecules.",
    },
    {
        "id": "ks4-moles-s03",
        "subtopic_slug": "moles",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "0.40 mol of a compound has a mass of 34 g. Calculate the "
                "relative formula mass of the compound.",
        "options": [
            "85",
            "13.6",
            "0.012",
            "136",
        ],
        "correct_index": 0,
        "why": "Rearranging moles = mass ÷ Mr gives Mr = mass ÷ moles = "
               "34 ÷ 0.40 = 85.",
    },
    {
        "id": "ks4-moles-s04",
        "subtopic_slug": "moles",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate the percentage by mass of oxygen in aluminium oxide, Al2O3. Ar: Al = 27, O = 16.",
        "options": [
            "15.7%",
            "26.5%",
            "47.1%",
            "52.9%",
        ],
        "correct_index": 2,
        "why": "There are three oxygen atoms in an Mr of 102, so (3 × 16 ÷ 102) × 100 = 47.1%.",
    },
    {
        "id": "ks4-moles-h01",
        "subtopic_slug": "moles",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate the total number of atoms in 3.6 g of water, H2O. "
                "Mr = 18 and the Avogadro constant is 6.02 × 10²³ mol⁻¹.",
        "options": [
            "3.61 × 10²³",
            "1.20 × 10²³",
            "6.02 × 10²³",
            "2.41 × 10²³",
        ],
        "correct_index": 0,
        "why": "3.6 ÷ 18 = 0.20 mol, which is 1.20 × 10²³ molecules, and "
               "each molecule holds 3 atoms — 3.61 × 10²³ atoms.",
    },
    {
        "id": "ks4-moles-h02",
        "subtopic_slug": "moles",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate the number of moles in 25.0 g of hydrated "
                "copper(II) sulfate, CuSO4.5H2O. Mr = 250.",
        "options": [
            "0.156 mol",
            "0.100 mol",
            "10.0 mol",
            "6250 mol",
        ],
        "correct_index": 1,
        "why": "The Mr of the hydrated crystals already includes the water of "
               "crystallisation, so moles = 25.0 ÷ 250 = 0.100 mol.",
    },
    {
        "id": "ks4-moles-h03",
        "subtopic_slug": "moles",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Determine which of these samples contains the greatest "
                "number of atoms: 12 g of carbon (Ar = 12), 4.0 g of helium "
                "(Ar = 4), 48 g of magnesium (Ar = 24) or 32 g of sulfur "
                "(Ar = 32).",
        "options": [
            "12 g of carbon",
            "4.0 g of helium",
            "48 g of magnesium",
            "32 g of sulfur",
        ],
        "correct_index": 2,
        "why": "The number of atoms follows the moles, not the mass: 48 ÷ 24 "
               "= 2 mol of magnesium, while each of the other three samples "
               "is only 1 mol.",
    },
    {
        "id": "ks4-moles-h04",
        "subtopic_slug": "moles",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Ammonia, NH3, and ammonium nitrate, NH4NO3, are both used "
                "as fertilisers. Ar: H = 1, N = 14, O = 16. Determine which "
                "supplies more nitrogen per 100 g, and by how much.",
        "options": [
            "Ammonium nitrate, by 47.4 g",
            "Ammonia, by 17.4 g",
            "Ammonia, by 82.4 g",
            "Ammonia, by 47.4 g",
        ],
        "correct_index": 3,
        "why": "Nitrogen is 14 of the 17 mass units in NH3, that is 82.4%, "
               "but only 28 of the 80 in NH4NO3, that is 35.0% — a "
               "difference of 47.4 g per 100 g.",
    },

    # ── amounts-in-equations ────────────────────────────────────────────
    {
        "id": "ks4-amounts-in-equations-e01",
        "subtopic_slug": "amounts-in-equations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "In the equation 2Al + 3Cl2 → 2AlCl3, state what the "
                "coefficient 3 tells you.",
        "options": [
            "Three grams of chlorine take part in the reaction",
            "Chlorine molecules each contain three atoms",
            "Three moles of chlorine react with every two moles of aluminium",
            "The reaction must be repeated three times to go to completion",
        ],
        "correct_index": 2,
        "why": "The numbers in front of the formulae give the ratio of moles "
               "in which the substances react, not their masses.",
    },
    {
        "id": "ks4-amounts-in-equations-e02",
        "subtopic_slug": "amounts-in-equations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "For 4Fe + 3O2 → 2Fe2O3, calculate the number of moles of iron(III) oxide produced from 0.80 mol of iron.",
        "options": [
            "0.80 mol",
            "0.40 mol",
            "1.60 mol",
            "0.60 mol",
        ],
        "correct_index": 1,
        "why": "Four moles of iron make two moles of Fe2O3, a 2 : 1 ratio, so 0.80 mol of iron gives 0.40 mol of oxide.",
    },
    {
        "id": "ks4-amounts-in-equations-e03",
        "subtopic_slug": "amounts-in-equations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "For 2H2 + O2 → 2H2O, calculate the number of moles of "
                "oxygen needed to react completely with 0.80 mol of "
                "hydrogen.",
        "options": [
            "0.40 mol",
            "0.80 mol",
            "1.60 mol",
            "0.20 mol",
        ],
        "correct_index": 0,
        "why": "The ratio H2 : O2 is 2 : 1, so 0.80 mol of hydrogen needs "
               "0.80 ÷ 2 = 0.40 mol of oxygen.",
    },
    {
        "id": "ks4-amounts-in-equations-e04",
        "subtopic_slug": "amounts-in-equations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A student must find the mass of product made from a given "
                "mass of reactant. State the correct order of steps.",
        "options": [
            "Multiply by Mr, apply the ratio, then divide by the Mr of the "
            "product",
            "Apply the ratio to the mass, then divide by the Mr of the "
            "product",
            "Divide by Mr, divide by the ratio, then divide by the Mr of the "
            "product",
            "Divide by Mr, apply the molar ratio, then multiply by the Mr of "
            "the product",
        ],
        "correct_index": 3,
        "why": "Masses of different substances can only be compared through "
               "moles, so you convert to moles, use the equation's ratio, "
               "then convert back.",
    },
    {
        "id": "ks4-amounts-in-equations-s01",
        "subtopic_slug": "amounts-in-equations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Calcium carbonate decomposes: CaCO3 → CaO + CO2. Mr: "
                "CaCO3 = 100, CaO = 56. Calculate the mass of calcium oxide "
                "made from 20.0 g of calcium carbonate.",
        "options": [
            "11.2 g",
            "20.0 g",
            "35.7 g",
            "8.8 g",
        ],
        "correct_index": 0,
        "why": "20.0 ÷ 100 = 0.200 mol of CaCO3 gives 0.200 mol of CaO, and "
               "0.200 × 56 = 11.2 g.",
    },
    {
        "id": "ks4-amounts-in-equations-s02",
        "subtopic_slug": "amounts-in-equations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "For 2Mg + O2 → 2MgO, Ar: Mg = 24, O = 16. Calculate the "
                "mass of oxygen needed to react completely with 7.2 g of "
                "magnesium.",
        "options": [
            "2.4 g",
            "9.6 g",
            "4.8 g",
            "12.0 g",
        ],
        "correct_index": 2,
        "why": "7.2 ÷ 24 = 0.30 mol of Mg needs half as many moles of O2, "
               "0.15 mol, and 0.15 × 32 = 4.8 g.",
    },
    {
        "id": "ks4-amounts-in-equations-s03",
        "subtopic_slug": "amounts-in-equations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Zinc reacts with sulfuric acid: Zn + H2SO4 → ZnSO4 + "
                "H2. Ar of Zn = 65 and Mr of ZnSO4 = 161. 13.0 g of zinc "
                "reacts and 25.76 g of zinc sulfate is collected. Calculate "
                "the percentage yield.",
        "options": [
            "125.0%",
            "198.2%",
            "20.0%",
            "80.0%",
        ],
        "correct_index": 3,
        "why": "13.0 ÷ 65 = 0.200 mol of zinc can make 0.200 × 161 = "
               "32.2 g of zinc sulfate, and (25.76 ÷ 32.2) × 100 = "
               "80.0%.",
    },
    {
        "id": "ks4-amounts-in-equations-s04",
        "subtopic_slug": "amounts-in-equations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Iron is made by Fe2O3 + 3CO → 2Fe + 3CO2. Mr of "
                "Fe2O3 = 160 and Ar of Fe = 56. Calculate the mass of "
                "iron(III) oxide needed to make 112 g of iron.",
        "options": [
            "80 g",
            "160 g",
            "320 g",
            "112 g",
        ],
        "correct_index": 1,
        "why": "112 ÷ 56 = 2.0 mol of iron, and the equation makes 2 Fe from "
               "1 Fe2O3, so 1.0 mol × 160 = 160 g is needed.",
    },
    {
        "id": "ks4-amounts-in-equations-h01",
        "subtopic_slug": "amounts-in-equations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Ammonia is made by N2 + 3H2 → 2NH3. Mr: NH3 = 17, "
                "N2 = 28. A plant runs at a percentage yield of 60%. "
                "Calculate the mass of nitrogen needed to produce 102 kg of "
                "ammonia.",
        "options": [
            "84 kg",
            "233 kg",
            "168 kg",
            "140 kg",
        ],
        "correct_index": 3,
        "why": "Only 60% is obtained, so 102 ÷ 0.60 = 170 kg must be "
               "possible on paper — that is 10 kmol of NH3, needing 5 kmol "
               "of N2, which is 140 kg.",
    },
    {
        "id": "ks4-amounts-in-equations-h02",
        "subtopic_slug": "amounts-in-equations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Sodium burns in excess chlorine: 2Na + Cl2 → 2NaCl. Ar "
                "of Na = 23 and Mr of NaCl = 58.5. Calculate the maximum "
                "mass of sodium chloride that can be made from 4.6 g of "
                "sodium.",
        "options": [
            "11.7 g",
            "5.85 g",
            "23.4 g",
            "4.6 g",
        ],
        "correct_index": 0,
        "why": "The ratio Na : NaCl is 2 : 2, which is 1 : 1, so 0.20 mol of "
               "sodium gives 0.20 mol of NaCl — 0.20 × 58.5 = 11.7 g.",
    },
    {
        "id": "ks4-amounts-in-equations-h03",
        "subtopic_slug": "amounts-in-equations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student calculates the mass of aluminium oxide made from "
                "5.4 g of aluminium using 4Al + 3O2 → 2Al2O3, with Ar of "
                "Al = 27 and Mr of Al2O3 = 102. They write: 5.4 ÷ 27 = "
                "0.2 mol Al, so 0.2 mol Al2O3, so 0.2 × 102 = 20.4 g. "
                "Identify the error.",
        "options": [
            "The moles of aluminium are wrong: 5.4 ÷ 27 = 0.5 mol, giving "
            "51.0 g",
            "The 4 : 2 ratio was ignored: only 0.1 mol of Al2O3 forms, "
            "giving 10.2 g",
            "The ratio was applied upside down: 0.4 mol of Al2O3 forms, "
            "giving 40.8 g",
            "Nothing is wrong, because the ratio of Al to Al2O3 in the "
            "equation is 1 : 1",
        ],
        "correct_index": 1,
        "why": "Four moles of aluminium make only two moles of Al2O3, so "
               "0.2 mol of Al gives 0.1 mol of oxide — 0.1 × 102 = 10.2 g.",
    },
    {
        "id": "ks4-amounts-in-equations-h04",
        "subtopic_slug": "amounts-in-equations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Copper(II) nitrate decomposes on heating: 2Cu(NO3)2 → "
                "2CuO + 4NO2 + O2. Mr: Cu(NO3)2 = 188, CuO = 80. Calculate "
                "the mass of copper oxide formed when 18.8 g of copper(II) "
                "nitrate decomposes completely.",
        "options": [
            "4.0 g",
            "16.0 g",
            "8.0 g",
            "18.8 g",
        ],
        "correct_index": 2,
        "why": "The ratio Cu(NO3)2 : CuO is 2 : 2, so 18.8 ÷ 188 = "
               "0.100 mol of the nitrate gives 0.100 mol of CuO — "
               "0.100 × 80 = 8.0 g.",
    },

    # ── using-moles-calculations ────────────────────────────────────────
    {
        "id": "ks4-using-moles-calculations-e01",
        "subtopic_slug": "using-moles-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Identify the equation that gives the concentration of a "
                "solution in mol/dm³.",
        "options": [
            "concentration = moles × volume in dm³",
            "concentration = moles ÷ volume in dm³",
            "concentration = mass ÷ volume in cm³",
            "concentration = volume in dm³ ÷ moles",
        ],
        "correct_index": 1,
        "why": "Concentration says how many moles are packed into each dm³, "
               "so the moles are divided by the volume.",
    },
    {
        "id": "ks4-using-moles-calculations-e02",
        "subtopic_slug": "using-moles-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate the number of moles of hydrochloric acid in "
                "500 cm³ of a 0.20 mol/dm³ solution.",
        "options": [
            "100 mol",
            "2.5 mol",
            "0.10 mol",
            "0.40 mol",
        ],
        "correct_index": 2,
        "why": "Moles = concentration × volume in dm³ = 0.20 × 0.500 = "
               "0.10 mol.",
    },
    {
        "id": "ks4-using-moles-calculations-e03",
        "subtopic_slug": "using-moles-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what is meant by the limiting reactant in a reaction.",
        "options": [
            "The reactant that is present in the smallest mass",
            "The reactant that has the largest relative formula mass",
            "The reactant that is left over once the reaction has stopped",
            "The reactant that is used up first, so it stops the reaction "
            "going further",
        ],
        "correct_index": 3,
        "why": "Once the limiting reactant has all reacted no more product "
               "can form, however much of the other reactant is still "
               "there.",
    },
    {
        "id": "ks4-using-moles-calculations-e04",
        "subtopic_slug": "using-moles-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A compound contains 0.20 mol of carbon and 0.40 mol of "
                "hydrogen. Determine its empirical formula.",
        "options": [
            "CH2",
            "C2H4",
            "C2H",
            "CH4",
        ],
        "correct_index": 0,
        "why": "An empirical formula is the simplest whole-number ratio, and "
               "0.20 : 0.40 simplifies to 1 : 2.",
    },
    {
        "id": "ks4-using-moles-calculations-s01",
        "subtopic_slug": "using-moles-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "5.85 g of sodium chloride, NaCl, is stirred into water and the solution made up to 250 cm³. Mr of NaCl = 58.5. Calculate the concentration in mol/dm³.",
        "options": [
            "0.00040 mol/dm³",
            "23.4 mol/dm³",
            "0.40 mol/dm³",
            "0.10 mol/dm³",
        ],
        "correct_index": 2,
        "why": "5.85 ÷ 58.5 = 0.10 mol of NaCl sits in 0.250 dm³, so the concentration is 0.10 ÷ 0.250 = 0.40 mol/dm³.",
    },
    {
        "id": "ks4-using-moles-calculations-s02",
        "subtopic_slug": "using-moles-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "In a titration, 25.0 cm³ of potassium hydroxide solution is exactly neutralised by 22.5 cm³ of 0.200 mol/dm³ nitric acid. KOH + HNO3 → KNO3 + H2O. Calculate the concentration of the potassium hydroxide.",
        "options": [
            "0.222 mol/dm³",
            "0.200 mol/dm³",
            "0.0900 mol/dm³",
            "0.180 mol/dm³",
        ],
        "correct_index": 3,
        "why": "The acid supplies 0.200 × 0.0225 = 0.00450 mol, the reaction is 1 : 1, so the alkali is 0.00450 ÷ 0.0250 = 0.180 mol/dm³.",
    },
    {
        "id": "ks4-using-moles-calculations-s03",
        "subtopic_slug": "using-moles-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A sodium hydroxide solution has a concentration of 20 g/dm³. Mr of NaOH = 40. Calculate its concentration in mol/dm³.",
        "options": [
            "800 mol/dm³",
            "0.50 mol/dm³",
            "2.0 mol/dm³",
            "20 mol/dm³",
        ],
        "correct_index": 1,
        "why": "Each mole of NaOH weighs 40 g, so 20 g in every dm³ is 20 ÷ 40 = 0.50 mol/dm³.",
    },
    {
        "id": "ks4-using-moles-calculations-s04",
        "subtopic_slug": "using-moles-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "2.8 g of iron combines with 1.2 g of oxygen to form an "
                "oxide. Ar: Fe = 56, O = 16. Determine the empirical formula "
                "of the oxide.",
        "options": [
            "Fe2O3",
            "FeO",
            "Fe3O4",
            "Fe3O2",
        ],
        "correct_index": 0,
        "why": "2.8 ÷ 56 = 0.050 mol of iron and 1.2 ÷ 16 = 0.075 mol of "
               "oxygen, a ratio of 2 : 3.",
    },
    {
        "id": "ks4-using-moles-calculations-h01",
        "subtopic_slug": "using-moles-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "25.0 cm³ of 0.100 mol/dm³ sodium hydroxide is exactly "
                "neutralised by 20.0 cm³ of sulfuric acid. H2SO4 + 2NaOH "
                "→ Na2SO4 + 2H2O. Calculate the concentration of the "
                "sulfuric acid.",
        "options": [
            "0.0625 mol/dm³",
            "0.125 mol/dm³",
            "0.250 mol/dm³",
            "0.0313 mol/dm³",
        ],
        "correct_index": 0,
        "why": "0.100 × 0.0250 = 0.00250 mol of NaOH, and two NaOH react "
               "with one H2SO4, so 0.00125 ÷ 0.0200 = 0.0625 mol/dm³.",
    },
    {
        "id": "ks4-using-moles-calculations-h02",
        "subtopic_slug": "using-moles-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "6.5 g of zinc is added to 50.0 cm³ of 2.00 mol/dm³ "
                "hydrochloric acid. Zn + 2HCl → ZnCl2 + H2, and Ar of "
                "Zn = 65. Calculate the maximum mass of hydrogen produced.",
        "options": [
            "0.200 g",
            "0.100 g",
            "0.0500 g",
            "2.00 g",
        ],
        "correct_index": 1,
        "why": "The acid supplies only 0.100 mol where 0.200 mol would be "
               "needed for all the zinc, so it limits the reaction: "
               "0.0500 mol of H2, a mass of 0.100 g.",
    },
    {
        "id": "ks4-using-moles-calculations-h03",
        "subtopic_slug": "using-moles-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A hydrocarbon has the empirical formula CH2 and a relative "
                "formula mass of 84. Ar: C = 12, H = 1. Determine its "
                "molecular formula.",
        "options": [
            "C3H6",
            "C7H14",
            "C6H12",
            "CH2",
        ],
        "correct_index": 2,
        "why": "The CH2 unit has a mass of 14, and 84 ÷ 14 = 6, so the "
               "molecule is six of those units.",
    },
    {
        "id": "ks4-using-moles-calculations-h04",
        "subtopic_slug": "using-moles-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A compound contains 40.0% carbon, 6.7% hydrogen and 53.3% "
                "oxygen by mass. Ar: C = 12, H = 1, O = 16. Determine its "
                "empirical formula.",
        "options": [
            "C2H4O2",
            "CHO",
            "C6H12O6",
            "CH2O",
        ],
        "correct_index": 3,
        "why": "Dividing each percentage by its Ar gives 3.33 : 6.7 : 3.33, "
               "which simplifies to 1 : 2 : 1.",
    },
]
