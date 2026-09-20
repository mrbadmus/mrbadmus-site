"""Chemistry · Organic chemistry — crude oil through to naturally occurring polymers.

Twelve subtopics, 144 questions. The first four (crude oil, fractional
distillation, properties of hydrocarbons, cracking) are BASE and are
deliberately kept clear of alkene reaction conditions, alcohols and polymer
chemistry — a Foundation Combined class sits them. The remaining eight are
Triple-only, and condensation polymerisation and amino acids are Higher too.

Distractors are built from the declared misconceptions: the alkane/alkene
general formulae swapped (CnH2n+2 vs CnH2n), the fractionating column read
upside down, cracking said to give only alkanes, the bromine water result
inverted, fractional distillation called a chemical change, addition and
condensation polymerisation confused over whether a small molecule is lost,
and the ester link mistaken for the amide link. Calculation distractors come
from the error — counting hydrogen atoms instead of water molecules, rounding
3.5 O2 up to 4, forgetting the water lost when a dipeptide forms.
"""

TOPIC = "organic"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── crude-oil-hydrocarbons ──────────────────────────────────────────
    {
        "id": "ks4-crude-oil-hydrocarbons-e01",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what crude oil is.",
        "options": [
            "A single pure compound made of carbon, hydrogen and oxygen atoms",
            "A renewable fuel formed by living plants over a few years",
            "A mixture of hydrocarbons formed from ancient marine organisms",
            "An element that contains only carbon atoms bonded together",
        ],
        "correct_index": 2,
        "why": "Crude oil is a mixture of hydrocarbons — compounds of carbon "
               "and hydrogen only — formed from the buried remains of "
               "ancient marine organisms.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-e02",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these compounds is a hydrocarbon?",
        "options": [
            "C3H8",
            "CO2",
            "H2SO4",
            "C6H12O6",
        ],
        "correct_index": 0,
        "why": "A hydrocarbon contains carbon and hydrogen and nothing else — "
               "C3H8 is the only formula here without a third element.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-e03",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which molecular formula fits the general formula for "
                "alkanes, CnH2n+2?",
        "options": [
            "C6H12",
            "C4H8",
            "C7H14",
            "C6H14",
        ],
        "correct_index": 3,
        "why": "For n = 6, 2n + 2 = 14, so C6H14 is an alkane; the other "
               "three all fit CnH2n, which is the alkene formula.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-e04",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two products of the complete combustion of a "
                "hydrocarbon fuel.",
        "options": [
            "Carbon monoxide and soot",
            "Carbon dioxide and water",
            "Hydrogen gas and carbon dioxide",
            "Carbon monoxide and water only",
        ],
        "correct_index": 1,
        "why": "With plenty of oxygen every carbon atom becomes carbon "
               "dioxide and every hydrogen atom becomes water.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-s01",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why alkanes are described as relatively unreactive.",
        "options": [
            "Their molecules are too large for other substances to reach the "
            "carbon atoms",
            "Their C–C and C–H bonds are all strong single covalent bonds "
            "that are hard to break",
            "They contain a C=C double bond, which is much stronger than any "
            "single covalent bond",
            "They are non-polar molecules, which is why they cannot burn in "
            "oxygen at all",
        ],
        "correct_index": 1,
        "why": "Alkanes are saturated: every bond is a strong single covalent "
               "bond, so there is nothing easy for a reagent to attack.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-s02",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethane burns in a plentiful supply of oxygen. Which equation "
                "correctly represents its complete combustion?",
        "options": [
            "C2H6 + O2 → CO2 + H2O",
            "C2H6 + 4O2 → 2CO2 + 3H2O",
            "2C2H6 + 5O2 → 4CO + 6H2O",
            "2C2H6 + 7O2 → 4CO2 + 6H2O",
        ],
        "correct_index": 3,
        "why": "Only this one balances (4 C, 12 H and 14 O on each side) and "
               "gives the complete-combustion products CO2 and H2O.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-s03",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A camping stove burns butane with a yellow, sooty flame. "
                "Suggest what this shows about the combustion taking place.",
        "options": [
            "There is not enough oxygen, so combustion is incomplete and "
            "carbon particles form",
            "The butane is impure and contains sulfur compounds that colour "
            "the flame yellow",
            "There is more oxygen than is needed, so combustion is more "
            "complete than usual",
            "The butane is burning as an alkene rather than as an alkane in "
            "the hot flame",
        ],
        "correct_index": 0,
        "why": "Soot is unburnt carbon: a yellow, smoky flame means the "
               "oxygen supply is limited, so combustion is incomplete.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-s04",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Crude oil is described as both a fuel and a feedstock. Which "
                "use is an example of it acting as a feedstock?",
        "options": [
            "Burning diesel in a lorry engine so that the lorry can move",
            "Burning heating oil in a boiler to warm up a large building",
            "Using hydrocarbons as raw materials to make plastics and medicines",
            "Storing it in large underground tanks until the price of fuel rises again",
        ],
        "correct_index": 2,
        "why": "A feedstock is a raw material for making other chemicals, not "
               "something burnt for its energy.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-h01",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Crude oil must be a compound, because it "
                "can be separated into substances with different boiling "
                "points.' Explain the error in this reasoning.",
        "options": [
            "Separating by boiling point is a physical process, which shows "
            "crude oil is a mixture",
            "Crude oil is a compound, but its covalent bonds break as it is "
            "heated in the column",
            "Compounds cannot be separated at all, so crude oil must in fact "
            "be a single element",
            "Crude oil is a mixture because all of its molecules have exactly "
            "the same boiling point",
        ],
        "correct_index": 0,
        "why": "A compound could only be split by a chemical reaction; "
               "separating by boiling point is physical, so crude oil is a "
               "mixture.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-h02",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alkane with n carbon atoms burns completely in oxygen. "
                "Deduce the number of water molecules formed from one "
                "molecule of the alkane.",
        "options": [
            "n",
            "2n",
            "n + 1",
            "2n + 2",
        ],
        "correct_index": 2,
        "why": "The alkane is CnH2n+2, so it has 2n + 2 hydrogen atoms, and "
               "two hydrogen atoms make one H2O — giving n + 1 molecules.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-h03",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the products of burning methane in a plentiful "
                "supply of air with the products of burning it in a limited "
                "supply of air.",
        "options": [
            "Both give only carbon dioxide and water, but the limited supply "
            "releases much more energy",
            "Both give carbon dioxide and water; the limited supply also gives "
            "carbon monoxide and soot",
            "The plentiful supply gives carbon monoxide; the limited supply "
            "gives carbon dioxide",
            "The limited supply gives hydrogen gas in place of the water "
            "vapour normally formed",
        ],
        "correct_index": 1,
        "why": "Without enough oxygen some carbon is only partly oxidised to "
               "carbon monoxide, or not at all, leaving soot.",
    },
    {
        "id": "ks4-crude-oil-hydrocarbons-h04",
        "subtopic_slug": "crude-oil-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Methane, CH4, needs 2 molecules of oxygen for complete "
                "combustion but propane, C3H8, needs 5. Explain why propane "
                "needs more oxygen per molecule of fuel.",
        "options": [
            "Propane molecules are heavier, so more energy is needed to make "
            "them ignite at all",
            "Propane contains a carbon–carbon double bond that has to be "
            "broken before it can burn",
            "Propane has fewer hydrogen atoms for each carbon atom, so much "
            "less water is produced",
            "Propane has more carbon and hydrogen atoms, so more CO2 and H2O "
            "are formed",
        ],
        "correct_index": 3,
        "why": "Each carbon atom needs one O2 to become CO2 and each pair of "
               "hydrogen atoms needs half an O2, so a longer chain needs "
               "more oxygen.",
    },

    # ── fractional-distillation ─────────────────────────────────────────
    {
        "id": "ks4-fractional-distillation-e01",
        "subtopic_slug": "fractional-distillation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a 'fraction' in fractional "
                "distillation.",
        "options": [
            "A single pure hydrocarbon separated from all of the others",
            "A group of hydrocarbons with similar chain lengths and boiling "
            "points",
            "The part of the crude oil that never vaporises in the column",
            "A hydrocarbon that has been chemically changed into an entirely "
            "new compound",
        ],
        "correct_index": 1,
        "why": "A fraction is not a pure substance — it is a group of "
               "hydrocarbons whose boiling points are close enough to "
               "condense together.",
    },
    {
        "id": "ks4-fractional-distillation-e02",
        "subtopic_slug": "fractional-distillation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which fraction leaves the very top of the fractionating "
                "column as a gas?",
        "options": [
            "Bitumen",
            "Diesel oil",
            "Kerosene",
            "Refinery gases",
        ],
        "correct_index": 3,
        "why": "Refinery gases have the shortest chains and the lowest "
               "boiling points, so they never condense on the way up.",
    },
    {
        "id": "ks4-fractional-distillation-e03",
        "subtopic_slug": "fractional-distillation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fractional distillation separates crude oil without making "
                "any new substances. State what type of change this is.",
        "options": [
            "A physical change — the molecules are separated but not altered",
            "A chemical change — new hydrocarbon molecules are made in the "
            "column",
            "A chemical change — covalent bonds inside the molecules are "
            "broken",
            "A physical change — the hydrocarbons react to form larger "
            "molecules",
        ],
        "correct_index": 0,
        "why": "Only the forces between molecules are overcome; every "
               "molecule leaves the column exactly as it entered, so the "
               "change is physical.",
    },
    {
        "id": "ks4-fractional-distillation-e04",
        "subtopic_slug": "fractional-distillation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which property of the hydrocarbons in crude oil allows them "
                "to be separated by fractional distillation?",
        "options": [
            "They have different densities",
            "They have different colours",
            "They have different boiling points",
            "They have different reactivities",
        ],
        "correct_index": 2,
        "why": "Each fraction condenses at its own boiling point, which is "
               "what sorts the mixture into layers up the column.",
    },
    {
        "id": "ks4-fractional-distillation-s01",
        "subtopic_slug": "fractional-distillation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fraction condenses low down in the fractionating column. "
                "Describe what this tells you about its molecules.",
        "options": [
            "They have short chains and are very volatile at room "
            "temperature",
            "They have short chains and only weak forces between the "
            "molecules",
            "They have long chains and strong forces between the molecules",
            "They have long chains but unusually low boiling points",
        ],
        "correct_index": 2,
        "why": "Condensing low down means a high boiling point, and that "
               "means long chains with strong intermolecular forces.",
    },
    {
        "id": "ks4-fractional-distillation-s02",
        "subtopic_slug": "fractional-distillation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Kerosene contains hydrocarbons with 10 to 16 carbon atoms; "
                "refinery gases contain 1 to 4. Predict how their "
                "viscosities compare.",
        "options": [
            "Kerosene is more viscous, because longer chains tangle and flow "
            "less easily",
            "Kerosene is less viscous, because longer molecules slide past "
            "each other more easily",
            "They have the same viscosity, because both are mixtures of "
            "alkane molecules",
            "Kerosene is less viscous, because it condenses higher up the "
            "column than gases",
        ],
        "correct_index": 0,
        "why": "Viscosity rises with chain length: longer molecules tangle "
               "together and resist flowing.",
    },
    {
        "id": "ks4-fractional-distillation-s03",
        "subtopic_slug": "fractional-distillation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the fractionating column is kept much hotter at "
                "the bottom than at the top.",
        "options": [
            "So that the heaviest fractions are chemically broken down into "
            "smaller molecules",
            "So that every fraction condenses at the same level and can be "
            "collected together",
            "So that the vapours are cooled as they sink downwards, "
            "condensing near the hot base",
            "So that rising vapours cool and each condenses at its own "
            "boiling point",
        ],
        "correct_index": 3,
        "why": "The temperature gradient means each vapour meets the "
               "temperature equal to its boiling point at a different "
               "height, so it condenses there.",
    },
    {
        "id": "ks4-fractional-distillation-s04",
        "subtopic_slug": "fractional-distillation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bitumen does not vaporise at the temperature used in the "
                "fractionating column. Explain what happens to it.",
        "options": [
            "It rises to the top of the column and leaves the plant as a gas",
            "It stays as a liquid residue and is drawn off from the base of "
            "the column",
            "It condenses in the middle of the column along with the diesel "
            "fraction",
            "It is burnt inside the column to help heat the incoming crude "
            "oil",
        ],
        "correct_index": 1,
        "why": "Bitumen's chains are so long that its boiling point is above "
               "the column temperature, so it never leaves the liquid.",
    },
    {
        "id": "ks4-fractional-distillation-h01",
        "subtopic_slug": "fractional-distillation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The demand for petrol is greater than the amount obtained "
                "from crude oil by fractional distillation. Explain why "
                "distillation alone cannot meet that demand.",
        "options": [
            "Fractional distillation destroys some of the petrol fraction as "
            "it passes up the hot column",
            "Fractional distillation can only be carried out on a small "
            "scale in a laboratory",
            "Fractional distillation turns short-chain molecules into "
            "long-chain ones",
            "It only separates the molecules already present, and cannot "
            "make more short chains",
        ],
        "correct_index": 3,
        "why": "Distillation is a physical separation, so the amount of "
               "petrol it can yield is fixed by what the crude oil already "
               "contains.",
    },
    {
        "id": "ks4-fractional-distillation-h02",
        "subtopic_slug": "fractional-distillation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fraction A boils between 25 °C and 75 °C; fraction B boils "
                "between 220 °C and 350 °C. Deduce which is the better fuel "
                "for a portable camping stove and explain why.",
        "options": [
            "B, because a higher boiling point means more energy is released "
            "when it burns",
            "A, because its shorter chains are more volatile and ignite "
            "easily",
            "B, because its longer chains are more volatile and so ignite "
            "very easily",
            "A, because its longer chains make it less viscous and easier to "
            "pour out",
        ],
        "correct_index": 1,
        "why": "A boils at a low temperature, so it has short chains, is "
               "volatile and produces flammable vapour that lights easily.",
    },
    {
        "id": "ks4-fractional-distillation-h03",
        "subtopic_slug": "fractional-distillation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that a fraction with a higher boiling point "
                "must contain molecules with stronger covalent bonds. "
                "Evaluate this claim.",
        "options": [
            "Correct — longer chains contain more covalent bonds, so each "
            "bond must be stronger",
            "Correct — boiling always breaks the covalent bonds inside each "
            "molecule",
            "Incorrect — boiling overcomes the forces between molecules, not "
            "the covalent bonds",
            "Incorrect — boiling point depends only on the mass of the "
            "molecule and nothing else",
        ],
        "correct_index": 2,
        "why": "Boiling separates whole molecules from one another; the "
               "covalent bonds inside them stay intact, which is why the "
               "fractions are unchanged.",
    },
    {
        "id": "ks4-fractional-distillation-h04",
        "subtopic_slug": "fractional-distillation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fraction X is collected higher up the column than fraction "
                "Y. Predict how X compares with Y for chain length, "
                "viscosity and flammability.",
        "options": [
            "X: shorter chains, less viscous, more flammable than Y",
            "X: shorter chains, more viscous, less flammable than Y",
            "X: longer chains, less viscous, more flammable than Y",
            "X: longer chains, more viscous, less flammable than Y",
        ],
        "correct_index": 0,
        "why": "Higher up means a lower boiling point, so shorter chains — "
               "and short chains are runnier and easier to ignite.",
    },

    # ── properties-of-hydrocarbons ──────────────────────────────────────
    {
        "id": "ks4-properties-of-hydrocarbons-e01",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hydrocarbon has 12 carbon atoms in its chain. State its "
                "most likely state at room temperature.",
        "options": [
            "Gas, because every hydrocarbon is a gas at room temperature",
            "Gas, because its chain is longer than four carbon atoms",
            "Liquid, because chains of 5 to 17 carbons are liquids",
            "Solid, because any chain of more than 10 carbons is a solid",
        ],
        "correct_index": 2,
        "why": "Chains of 1–4 carbons are gases, 5–17 are liquids and 18 or "
               "more are solids, so a 12-carbon chain is a liquid.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-e02",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the viscosity of a hydrocarbon changes as its "
                "chain length increases.",
        "options": [
            "Viscosity decreases steadily",
            "Viscosity increases steadily",
            "Viscosity stays exactly the same",
            "Viscosity increases and then decreases",
        ],
        "correct_index": 1,
        "why": "Longer molecules tangle around one another and flow less "
               "easily, so the liquid gets thicker.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-e03",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the volatility of a hydrocarbon.",
        "options": [
            "How easily it dissolves in cold water",
            "How much energy it releases when it burns",
            "How thick and sticky it is when poured",
            "How easily it evaporates at room temperature",
        ],
        "correct_index": 3,
        "why": "Volatility is the tendency to evaporate — the more volatile "
               "a fuel, the more vapour it forms above the liquid.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-e04",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of these hydrocarbons ignites most easily.",
        "options": [
            "Pentane, C5H12",
            "Decane, C10H22",
            "Hexadecane, C16H34",
            "Icosane, C20H42",
        ],
        "correct_index": 0,
        "why": "The shortest chain is the most volatile, so it produces "
               "flammable vapour most readily and ignites most easily.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-s01",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two fuels are spilled on a bench. Fuel P smells strongly; "
                "fuel Q has almost no smell. Explain what this suggests "
                "about their chain lengths.",
        "options": [
            "P has shorter chains — it is more volatile, so more of it "
            "evaporates into the air",
            "P has longer chains — long molecules escape into the air far "
            "more readily than short ones",
            "Q has shorter chains — short molecules are held inside the "
            "liquid much more strongly",
            "They have the same chain length — how strongly a fuel smells "
            "depends only on the amount spilled",
        ],
        "correct_index": 0,
        "why": "You can only smell a substance that has evaporated, so a "
               "strong smell means high volatility and therefore short "
               "chains.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-s02",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Octane burns completely: 2C8H18 + 25O2 → 16CO2 + 18H2O. "
                "Calculate the number of oxygen molecules needed to burn 4 "
                "molecules of octane completely.",
        "options": [
            "25 molecules",
            "32 molecules",
            "50 molecules",
            "100 molecules",
        ],
        "correct_index": 2,
        "why": "The equation is for 2 octane molecules, so 4 molecules need "
               "twice as much oxygen: 2 × 25 = 50.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-s03",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hydrocarbons with longer chains have higher "
                "boiling points.",
        "options": [
            "The covalent bonds inside longer molecules are stronger and "
            "harder to break apart",
            "Stronger forces act between longer molecules, so more energy "
            "separates them",
            "Longer molecules contain more hydrogen, and hydrogen atoms are "
            "very hard to boil",
            "Longer molecules are denser, so they sink and cannot escape "
            "from the liquid surface",
        ],
        "correct_index": 1,
        "why": "Boiling separates molecules from each other, and the longer "
               "the chain the stronger the intermolecular forces holding "
               "them together.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-s04",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same fuel burns with a clean blue flame in one burner "
                "and a smoky yellow flame in another. Explain the "
                "difference.",
        "options": [
            "The yellow flame is hotter, so it produces more carbon dioxide",
            "The blue flame has less oxygen available, so soot is produced",
            "The yellow flame must be burning a completely different fuel "
            "with a longer chain",
            "The yellow flame has limited oxygen, so incomplete combustion "
            "makes soot",
        ],
        "correct_index": 3,
        "why": "Soot is unburnt carbon, and it only forms when there is not "
               "enough oxygen for every carbon atom to become CO2.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-h01",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrocarbon R boils at -0.5 °C and hydrocarbon S boils at "
                "174 °C. Deduce which is more suitable as a lubricating oil "
                "and explain why.",
        "options": [
            "R, because a low boiling point means it flows easily and so "
            "lubricates well",
            "S, because its longer chains make it a viscous liquid that "
            "stays in place",
            "R, because gases spread out and coat all the moving surfaces "
            "evenly",
            "S, because a high boiling point means it is more flammable when "
            "it gets hot",
        ],
        "correct_index": 1,
        "why": "A high boiling point means long chains, which give a viscous "
               "liquid that stays on the surfaces it is meant to lubricate.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-h02",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Longer hydrocarbon chains are more "
                "flammable because they contain more carbon and hydrogen to "
                "burn.' Explain the error.",
        "options": [
            "There is no error — having more atoms to burn really does mean "
            "easier ignition",
            "The error is that longer chains contain less hydrogen, so there "
            "is less of them to burn",
            "The error is that longer chains cannot be made to burn in air "
            "under any conditions",
            "Ease of ignition depends on volatility, and longer chains "
            "evaporate less readily",
        ],
        "correct_index": 3,
        "why": "A fuel burns as a vapour, so what matters is how easily it "
               "evaporates — and long chains evaporate poorly.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-h03",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pentane, C5H12, burns completely in oxygen. Determine the "
                "balanced equation for the reaction.",
        "options": [
            "C5H12 + 8O2 → 5CO2 + 6H2O",
            "C5H12 + 5O2 → 5CO2 + 6H2O",
            "C5H12 + 8O2 → 5CO2 + 12H2O",
            "C5H12 + 6O2 → 5CO + 6H2O",
        ],
        "correct_index": 0,
        "why": "5 carbons give 5 CO2 and 12 hydrogens give 6 H2O, which "
               "needs 10 + 6 = 16 oxygen atoms, so 8 O2.",
    },
    {
        "id": "ks4-properties-of-hydrocarbons-h04",
        "subtopic_slug": "properties-of-hydrocarbons",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why complete combustion of a fuel releases more "
                "energy per gram than incomplete combustion of the same "
                "fuel.",
        "options": [
            "Incomplete combustion produces water, which absorbs the energy "
            "as it is released",
            "Complete combustion needs less oxygen, so less energy is used "
            "up during the reaction",
            "In incomplete combustion the carbon is not fully oxidised, so "
            "less energy is released",
            "Complete combustion happens at a lower temperature, so far less "
            "energy escapes as heat",
        ],
        "correct_index": 2,
        "why": "Carbon monoxide and soot still contain chemical energy that "
               "would have been released had the carbon burnt fully to CO2.",
    },

    # ── cracking-alkenes ────────────────────────────────────────────────
    {
        "id": "ks4-cracking-alkenes-e01",
        "subtopic_slug": "cracking-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the general formula for the alkenes.",
        "options": [
            "CnH2n+2",
            "CnH2n-2",
            "CnHn",
            "CnH2n",
        ],
        "correct_index": 3,
        "why": "An alkene has one C=C double bond, so it carries two fewer "
               "hydrogen atoms than the alkane CnH2n+2, giving CnH2n.",
    },
    {
        "id": "ks4-cracking-alkenes-e02",
        "subtopic_slug": "cracking-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cracking a long-chain alkane always produces at least one of "
                "which type of molecule?",
        "options": [
            "An alkene",
            "Only smaller alkanes",
            "Carbon dioxide and water",
            "A hydrocarbon with more carbon atoms than the original",
        ],
        "correct_index": 0,
        "why": "There are not enough hydrogen atoms to saturate both "
               "fragments, so at least one product must contain a C=C double "
               "bond.",
    },
    {
        "id": "ks4-cracking-alkenes-e03",
        "subtopic_slug": "cracking-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the catalyst used in catalytic cracking.",
        "options": [
            "Nickel",
            "Iron",
            "Zeolite",
            "Platinum",
        ],
        "correct_index": 2,
        "why": "Catalytic cracking passes hot hydrocarbon vapour over a "
               "zeolite catalyst at about 500 °C.",
    },
    {
        "id": "ks4-cracking-alkenes-e04",
        "subtopic_slug": "cracking-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is observed when bromine water is shaken with an "
                "alkene.",
        "options": [
            "It stays orange, with no change at all",
            "It changes from orange to colourless",
            "It changes from colourless to orange",
            "It turns from orange to a milky white",
        ],
        "correct_index": 1,
        "why": "The bromine is used up as it adds across the C=C double "
               "bond, so the orange colour disappears.",
    },
    {
        "id": "ks4-cracking-alkenes-s01",
        "subtopic_slug": "cracking-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Decane, C10H22, is cracked to give octane, C8H18, and one "
                "other product. Determine the formula of that product.",
        "options": [
            "C2H6",
            "C2H2",
            "C2H4",
            "CH4",
        ],
        "correct_index": 2,
        "why": "Atoms are conserved: 10 - 8 = 2 carbons and 22 - 18 = 4 "
               "hydrogens, giving C2H4, ethene.",
    },
    {
        "id": "ks4-cracking-alkenes-s02",
        "subtopic_slug": "cracking-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the conditions used in thermal cracking with those "
                "used in catalytic cracking.",
        "options": [
            "Thermal: about 500 °C with a zeolite catalyst; catalytic: high "
            "temperature and high pressure",
            "Thermal: high temperature and high pressure; catalytic: about "
            "500 °C with a zeolite catalyst",
            "Thermal: room temperature with a catalyst; catalytic: high "
            "temperature and no catalyst",
            "Both use a zeolite catalyst, but thermal cracking is carried "
            "out at a much lower pressure",
        ],
        "correct_index": 1,
        "why": "Thermal cracking relies on heat and pressure alone; the "
               "catalyst in catalytic cracking lowers the activation energy "
               "so less pressure is needed.",
    },
    {
        "id": "ks4-cracking-alkenes-s03",
        "subtopic_slug": "cracking-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cracking is a chemical change but fractional distillation is "
                "a physical change. Explain the difference.",
        "options": [
            "Cracking separates molecules by boiling point; distillation "
            "breaks covalent bonds",
            "Cracking changes the state of the hydrocarbons; distillation "
            "changes their formulae",
            "Both break covalent bonds inside the molecules, but cracking "
            "needs a much higher temperature",
            "Cracking breaks covalent bonds and makes new molecules; "
            "distillation only separates them",
        ],
        "correct_index": 3,
        "why": "New substances are only made when bonds within molecules "
               "break and re-form, which is what cracking does and "
               "distillation does not.",
    },
    {
        "id": "ks4-cracking-alkenes-s04",
        "subtopic_slug": "cracking-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A refinery has a surplus of fuel oil and a shortage of "
                "petrol. Explain how cracking helps.",
        "options": [
            "It breaks long fuel-oil molecules into shorter ones in the "
            "petrol range",
            "It joins petrol molecules together to make more fuel oil for "
            "storage",
            "It removes the sulfur from fuel oil so that it can be sold as "
            "petrol",
            "It raises the boiling point of fuel oil so that it condenses as "
            "petrol",
        ],
        "correct_index": 0,
        "why": "Cracking converts long chains that are in surplus into short "
               "chains that are in demand, changing the balance of the "
               "products.",
    },
    {
        "id": "ks4-cracking-alkenes-h01",
        "subtopic_slug": "cracking-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hydrocarbon of formula C15H32 is cracked into exactly two "
                "molecules, one of which is C10H22. Determine the formula of "
                "the other.",
        "options": [
            "C5H12",
            "C5H10",
            "C5H8",
            "C25H54",
        ],
        "correct_index": 1,
        "why": "15 - 10 = 5 carbons and 32 - 22 = 10 hydrogens, giving "
               "C5H10 — an alkene, as cracking always requires.",
    },
    {
        "id": "ks4-cracking-alkenes-h02",
        "subtopic_slug": "cracking-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cracking a long alkane produces one shorter alkane and one "
                "alkene. Explain why an alkene must always be formed.",
        "options": [
            "The catalyst adds a double bond to one of the two products",
            "Alkenes have lower boiling points, so they escape from the "
            "reactor first",
            "There are not enough hydrogen atoms to saturate both fragments, "
            "so one gains a C=C",
            "Alkanes are unstable at high temperature and always turn into "
            "alkenes on heating",
        ],
        "correct_index": 2,
        "why": "Splitting CnH2n+2 into two pieces leaves too few hydrogens "
               "for both to be saturated, so one fragment forms a double "
               "bond instead.",
    },
    {
        "id": "ks4-cracking-alkenes-h03",
        "subtopic_slug": "cracking-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Cracking is worth doing because it "
                "turns a low-value product into higher-value ones.'",
        "options": [
            "Supported — surplus long-chain fractions become petrol and "
            "ethene, both in demand",
            "Not supported — cracking uses up long-chain fractions that are "
            "already in short supply",
            "Not supported — cracking produces only carbon dioxide and "
            "water, which have no value",
            "Supported — cracking removes the need to carry out fractional "
            "distillation altogether",
        ],
        "correct_index": 0,
        "why": "Long-chain fractions are in surplus and the petrol and "
               "ethene made from them are in short supply, so the value "
               "rises.",
    },
    {
        "id": "ks4-cracking-alkenes-h04",
        "subtopic_slug": "cracking-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the reactivity of ethane, C2H6, and ethene, C2H4, "
                "and explain the difference between them.",
        "options": [
            "Ethane is more reactive, because it contains more hydrogen "
            "atoms that it can give away",
            "They are equally reactive, because both are hydrocarbons made "
            "only of carbon and hydrogen",
            "Ethene is less reactive, because its double bond is stronger "
            "than any single bond",
            "Ethene is more reactive, because its C=C bond can open and add "
            "other atoms",
        ],
        "correct_index": 3,
        "why": "The C=C double bond gives alkenes a site where other atoms "
               "can add on; the saturated alkane has no such site.",
    },

    # ── structure-of-alkenes ────────────────────────────────────────────
    {
        "id": "ks4-structure-of-alkenes-e01",
        "subtopic_slug": "structure-of-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the functional group present in every alkene.",
        "options": [
            "The carbon–carbon double bond, C=C",
            "The hydroxyl group, –OH",
            "The carboxyl group, –COOH",
            "The carbon–carbon single bond, C–C",
        ],
        "correct_index": 0,
        "why": "The C=C double bond is the functional group that gives all "
               "alkenes their characteristic reactions.",
    },
    {
        "id": "ks4-structure-of-alkenes-e02",
        "subtopic_slug": "structure-of-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "An alkene is named from the alkane with the same number of "
                "carbon atoms. Name the alkene with the formula C3H6.",
        "options": [
            "Propane",
            "Ethene",
            "Propene",
            "Butene",
        ],
        "correct_index": 2,
        "why": "C3H6 fits CnH2n with n = 3, so it is the three-carbon "
               "alkene — propene.",
    },
    {
        "id": "ks4-structure-of-alkenes-e03",
        "subtopic_slug": "structure-of-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by an unsaturated hydrocarbon.",
        "options": [
            "One that contains only single bonds between its carbon atoms",
            "One that contains at least one carbon–carbon double bond",
            "One that contains the maximum possible number of hydrogen atoms",
            "One that dissolves completely in water at room temperature",
        ],
        "correct_index": 1,
        "why": "Unsaturated means the molecule holds fewer hydrogen atoms "
               "than it could, because a C=C double bond has taken their "
               "place.",
    },
    {
        "id": "ks4-structure-of-alkenes-e04",
        "subtopic_slug": "structure-of-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the first member of the alkene homologous series.",
        "options": [
            "Methene",
            "Methane",
            "Ethane",
            "Ethene",
        ],
        "correct_index": 3,
        "why": "A C=C bond needs two carbon atoms, so the smallest possible "
               "alkene is ethene, C2H4.",
    },
    {
        "id": "ks4-structure-of-alkenes-s01",
        "subtopic_slug": "structure-of-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ethane is C2H6 and ethene is C2H4. Explain why ethene has "
                "two fewer hydrogen atoms.",
        "options": [
            "Ethene has lost two hydrogen atoms as hydrogen gas during "
            "cracking",
            "Ethene has one carbon atom fewer, so it needs fewer hydrogen "
            "atoms to fill it",
            "Ethene contains an extra carbon–carbon bond in place of two of "
            "its carbon atoms",
            "Two bonds are used in the C=C double bond instead of bonding to "
            "hydrogen",
        ],
        "correct_index": 3,
        "why": "Each carbon still makes four bonds, but two of them are used "
               "on the double bond, leaving two fewer places for hydrogen.",
    },
    {
        "id": "ks4-structure-of-alkenes-s02",
        "subtopic_slug": "structure-of-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Alkenes form a homologous series. State what all members of "
                "a homologous series have in common.",
        "options": [
            "They all have exactly the same molecular formula",
            "The same general formula and functional group, differing by CH2 "
            "each step",
            "They all have identical boiling points and densities",
            "They all react in completely different ways from every other "
            "member of the family",
        ],
        "correct_index": 1,
        "why": "A homologous series shares a general formula and a functional "
               "group, so its members react alike and differ by CH2.",
    },
    {
        "id": "ks4-structure-of-alkenes-s03",
        "subtopic_slug": "structure-of-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hydrocarbon has the molecular formula C5H10. Deduce what "
                "type of hydrocarbon it is and why.",
        "options": [
            "An alkane, because it fits the formula CnH2n+2",
            "An alkane, because it has more than four carbon atoms",
            "An alkene, because it fits the formula CnH2n",
            "An alkene, because it has an odd number of carbon atoms",
        ],
        "correct_index": 2,
        "why": "For n = 5 the alkane would be C5H12; C5H10 has two hydrogens "
               "fewer, which fits CnH2n and means a C=C bond.",
    },
    {
        "id": "ks4-structure-of-alkenes-s04",
        "subtopic_slug": "structure-of-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why cracking, rather than fractional distillation, "
                "is the main industrial source of ethene.",
        "options": [
            "Crude oil contains almost no alkenes; cracking makes them from "
            "long alkanes",
            "Alkenes boil at exactly the same temperature as alkanes, so "
            "they cannot be distilled apart",
            "Fractional distillation converts alkanes into alkenes but only "
            "at a very low yield",
            "Crude oil is rich in alkenes, but they are all destroyed by the "
            "heat of distillation",
        ],
        "correct_index": 0,
        "why": "Distillation can only separate what is already there, and "
               "crude oil is a mixture of alkanes — the alkenes have to be "
               "made.",
    },
    {
        "id": "ks4-structure-of-alkenes-h01",
        "subtopic_slug": "structure-of-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "There is more than one molecule with the molecular formula "
                "C4H8. Explain how this is possible.",
        "options": [
            "The molecules contain different numbers of hydrogen atoms",
            "Some of the molecules contain two double bonds instead of one",
            "The C=C double bond can be in different positions along the "
            "carbon chain",
            "Butene can exist as either a saturated or an unsaturated "
            "molecule",
        ],
        "correct_index": 2,
        "why": "The same atoms can be arranged differently — the double bond "
               "may sit between the first and second carbons or the second "
               "and third.",
    },
    {
        "id": "ks4-structure-of-alkenes-h02",
        "subtopic_slug": "structure-of-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give the molecular formulae of the alkane and the alkene "
                "that each contain five carbon atoms, with the general "
                "formula each one follows.",
        "options": [
            "Pentane C5H12 (CnH2n+2) and pentene C5H10 (CnH2n)",
            "Pentane C5H10 (CnH2n) and pentene C5H12 (CnH2n+2)",
            "Pentane C5H12 (CnH2n+2) and pentene C5H8 (CnH2n-2)",
            "Pentane C5H11 (CnH2n+1) and pentene C5H10 (CnH2n)",
        ],
        "correct_index": 0,
        "why": "The alkane is saturated at CnH2n+2; one C=C bond removes two "
               "hydrogens, giving the alkene CnH2n.",
    },
    {
        "id": "ks4-structure-of-alkenes-h03",
        "subtopic_slug": "structure-of-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of bonding, why alkenes react much more "
                "readily than alkanes.",
        "options": [
            "Alkenes have more hydrogen atoms available to be replaced by "
            "other atoms",
            "Alkenes have larger molecules, so they collide with other "
            "particles far more often",
            "Alkanes contain polar bonds that hold other molecules away from "
            "the carbon chain",
            "The C=C bond can open so atoms add across it; a C–C bond "
            "cannot",
        ],
        "correct_index": 3,
        "why": "One of the two bonds in C=C can break and let atoms join on, "
               "so alkenes have a reaction route that saturated alkanes lack.",
    },
    {
        "id": "ks4-structure-of-alkenes-h04",
        "subtopic_slug": "structure-of-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says: 'C3H6 must be an alkane, because every "
                "hydrocarbon with only single bonds fits CnH2n.' Identify "
                "the two errors.",
        "options": [
            "CnH2n is the alkane formula, and C3H6 has too few carbons to be "
            "an alkene",
            "CnH2n is the alkene formula, and C3H6 has a C=C bond, not only "
            "single bonds",
            "CnH2n is correct for alkanes, but C3H6 is not in fact a "
            "hydrocarbon at all",
            "CnH2n applies only to alkanes with more than four carbon atoms, "
            "so C3H6 is an alkene",
        ],
        "correct_index": 1,
        "why": "CnH2n is the alkene formula — the alkane with three carbons "
               "is C3H8 — so C3H6 must contain a double bond.",
    },

    # ── reactions-of-alkenes ────────────────────────────────────────────
    {
        "id": "ks4-reactions-of-alkenes-e01",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of reaction in which a small molecule joins "
                "across the C=C double bond of an alkene.",
        "options": [
            "Substitution",
            "Addition",
            "Neutralisation",
            "Combustion",
        ],
        "correct_index": 1,
        "why": "In an addition reaction the double bond opens and the whole "
               "of the small molecule joins on, giving a single product.",
    },
    {
        "id": "ks4-reactions-of-alkenes-e02",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the catalyst used to add hydrogen to an alkene.",
        "options": [
            "Zeolite",
            "Iron",
            "Phosphoric acid",
            "Nickel",
        ],
        "correct_index": 3,
        "why": "Hydrogenation is carried out over a nickel catalyst at about "
               "200 °C; phosphoric acid is used for hydration instead.",
    },
    {
        "id": "ks4-reactions-of-alkenes-e03",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the product formed when ethene reacts with bromine.",
        "options": [
            "Bromoethane, C2H5Br",
            "Ethane and bromine gas",
            "1,2-dibromoethane, CH2BrCH2Br",
            "Ethanol and hydrogen bromide",
        ],
        "correct_index": 2,
        "why": "Both bromine atoms add on, one to each carbon of the old "
               "double bond, giving CH2BrCH2Br.",
    },
    {
        "id": "ks4-reactions-of-alkenes-e04",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the C=C double bond during an addition "
                "reaction.",
        "options": [
            "It becomes a single bond as atoms add to the two carbons",
            "It stays as a double bond and a hydrogen atom is removed",
            "It becomes a triple bond as more atoms join the chain",
            "It breaks completely, splitting the molecule into two halves",
        ],
        "correct_index": 0,
        "why": "One of the two bonds opens so each carbon can take a new "
               "atom, leaving a single C–C bond behind.",
    },
    {
        "id": "ks4-reactions-of-alkenes-s01",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Hydrogenation is used to turn vegetable oils into "
                "margarine. Explain what happens to the oil molecules.",
        "options": [
            "Hydrogen adds across their C=C bonds, making the molecules more "
            "saturated",
            "Hydrogen is removed from the molecules, making them more "
            "unsaturated than before",
            "Water adds across their C=C bonds, turning the oil into an "
            "alcohol instead",
            "The oil molecules are cracked into shorter, saturated "
            "hydrocarbon chains",
        ],
        "correct_index": 0,
        "why": "Vegetable oils contain C=C bonds; adding hydrogen across "
               "them saturates the molecules and raises the melting point.",
    },
    {
        "id": "ks4-reactions-of-alkenes-s02",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Propene, C3H6, reacts with hydrogen over a nickel catalyst. "
                "Determine the formula of the product.",
        "options": [
            "C3H6",
            "C3H7",
            "C3H8",
            "C6H12",
        ],
        "correct_index": 2,
        "why": "Two hydrogen atoms add across the double bond, so C3H6 + H2 "
               "gives the saturated alkane C3H8.",
    },
    {
        "id": "ks4-reactions-of-alkenes-s03",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of the reaction taking place, why bromine "
                "water loses its colour when it is shaken with ethene.",
        "options": [
            "The bromine dissolves in the ethene, so its colour is spread "
            "too thinly to be seen",
            "The ethene evaporates and carries the coloured bromine out of "
            "the solution with it",
            "The bromine is reduced to bromide ions by the hydrogen atoms in "
            "the ethene molecule",
            "Bromine adds across the C=C bond to form a colourless product, "
            "so none is left",
        ],
        "correct_index": 3,
        "why": "The colour comes from bromine molecules, and the addition "
               "reaction uses them up to make colourless dibromoethane.",
    },
    {
        "id": "ks4-reactions-of-alkenes-s04",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Alkenes tend to burn with a smokier flame than alkanes with "
                "the same number of carbon atoms. Suggest why.",
        "options": [
            "Alkenes contain oxygen atoms, which make the flame turn yellow",
            "Alkenes have a higher proportion of carbon, so combustion is "
            "more often incomplete",
            "Alkenes have a higher proportion of hydrogen, so much more "
            "water vapour is made",
            "The C=C bond releases soot directly as it breaks apart during "
            "the burning",
        ],
        "correct_index": 1,
        "why": "An alkene has two fewer hydrogens than the matching alkane, "
               "so it is richer in carbon and more of that carbon escapes as "
               "soot.",
    },
    {
        "id": "ks4-reactions-of-alkenes-h01",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict the product formed when propene, CH3CH=CH2, reacts "
                "with bromine.",
        "options": [
            "CH3CH2CH2Br",
            "CH3CHBrCH3",
            "CH2BrCH2CH2Br",
            "CH3CHBrCH2Br",
        ],
        "correct_index": 3,
        "why": "One bromine atom joins each of the two carbons that shared "
               "the double bond, so the second and third carbons each gain "
               "a Br.",
    },
    {
        "id": "ks4-reactions-of-alkenes-h02",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare an addition reaction with a substitution reaction.",
        "options": [
            "Addition swaps one atom for another; substitution joins two "
            "molecules into one",
            "Addition joins two molecules into one; substitution swaps an "
            "atom and makes a by-product",
            "Both reactions make only one product, so they cannot be told "
            "apart from their products",
            "Addition reactions always require a catalyst, whereas "
            "substitution reactions never require one at all",
        ],
        "correct_index": 1,
        "why": "Addition combines everything into a single product, while "
               "substitution replaces an atom and releases what it displaced.",
    },
    {
        "id": "ks4-reactions-of-alkenes-h03",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An unknown hydrocarbon decolourises bromine water, and when "
                "it is passed over nickel at 200 °C with hydrogen it gives "
                "butane. Deduce its identity.",
        "options": [
            "Butene, C4H8",
            "Butane, C4H10",
            "Propene, C3H6",
            "Butanol, C4H9OH",
        ],
        "correct_index": 0,
        "why": "Decolourising bromine water shows a C=C bond, and "
               "hydrogenation to butane fixes the chain at four carbons — so "
               "it is butene.",
    },
    {
        "id": "ks4-reactions-of-alkenes-h04",
        "subtopic_slug": "reactions-of-alkenes",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate this claim: 'Addition reactions of alkenes give a "
                "single product, so the yield of that product is always "
                "100%.'",
        "options": [
            "Correct — forming only one product means all the reactants must "
            "be converted",
            "Correct — the catalyst guarantees that every alkene molecule "
            "reacts in the end",
            "Incorrect — atom economy is 100%, but yield depends on how much "
            "actually reacts",
            "Incorrect — addition reactions always produce water as a second "
            "product as well",
        ],
        "correct_index": 2,
        "why": "Atom economy describes where the atoms go if the reaction "
               "happens; yield describes how much reaction happens, and the "
               "two are different measures.",
    },

    # ── alcohols ────────────────────────────────────────────────────────
    {
        "id": "ks4-alcohols-e01",
        "subtopic_slug": "alcohols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the functional group found in every alcohol.",
        "options": [
            "The carboxyl group, –COOH",
            "The amine group, –NH2",
            "The hydroxyl group, –OH",
            "The carbon–carbon double bond, C=C",
        ],
        "correct_index": 2,
        "why": "All alcohols share the –OH hydroxyl group, which is why they "
               "all react in the same characteristic ways.",
    },
    {
        "id": "ks4-alcohols-e02",
        "subtopic_slug": "alcohols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the molecular formula of ethanol.",
        "options": [
            "C2H5OH",
            "CH3OH",
            "C3H7OH",
            "C2H4",
        ],
        "correct_index": 0,
        "why": "Ethanol has two carbon atoms and one –OH group, following "
               "the alcohol formula CnH2n+1OH with n = 2.",
    },
    {
        "id": "ks4-alcohols-e03",
        "subtopic_slug": "alcohols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the alcohol present in alcoholic drinks.",
        "options": [
            "Methanol",
            "Ethanol",
            "Propanol",
            "Butanol",
        ],
        "correct_index": 1,
        "why": "Ethanol is the alcohol produced by fermentation and found in "
               "drinks; methanol is highly toxic.",
    },
    {
        "id": "ks4-alcohols-e04",
        "subtopic_slug": "alcohols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the gas produced when sodium metal is added to "
                "ethanol.",
        "options": [
            "Oxygen",
            "Carbon dioxide",
            "Chlorine",
            "Hydrogen",
        ],
        "correct_index": 3,
        "why": "Sodium reacts with the –OH group in the same way as it does "
               "with water, releasing hydrogen gas.",
    },
    {
        "id": "ks4-alcohols-s01",
        "subtopic_slug": "alcohols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why ethanol mixes completely with water but ethane "
                "does not dissolve in it at all.",
        "options": [
            "Ethanol is a smaller molecule than ethane, so it fits between "
            "the water molecules",
            "Ethanol is an ionic compound, so it splits into ions as soon as "
            "it is added to water",
            "Ethanol has a lower boiling point than ethane, so it mixes with "
            "water more easily",
            "The –OH group of ethanol hydrogen bonds to water; ethane has no "
            "such group",
        ],
        "correct_index": 3,
        "why": "The hydroxyl group can form hydrogen bonds with water "
               "molecules, and a hydrocarbon with no polar group cannot.",
    },
    {
        "id": "ks4-alcohols-s02",
        "subtopic_slug": "alcohols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which equation correctly represents the complete combustion "
                "of ethanol?",
        "options": [
            "C2H5OH + O2 → CO2 + H2O",
            "C2H5OH + 2O2 → 2CO2 + 3H2O",
            "C2H5OH + 3O2 → 2CO2 + 3H2O",
            "C2H5OH + 3O2 → 2CO + 3H2O",
        ],
        "correct_index": 2,
        "why": "The oxygen in the –OH group counts too: 1 + 6 = 7 oxygen "
               "atoms on the left match 4 + 3 = 7 on the right.",
    },
    {
        "id": "ks4-alcohols-s03",
        "subtopic_slug": "alcohols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bottle of wine left open slowly turns sour. Name the "
                "product formed and explain what causes it.",
        "options": [
            "Ethanoic acid — bacteria oxidise the ethanol, which is why wine "
            "turns to vinegar",
            "Ethene — the ethanol loses water in the air to form an "
            "unsaturated molecule",
            "Methanol — oxygen in the air breaks a carbon atom off the "
            "ethanol chain",
            "Ethane — oxygen removes the –OH group and replaces it with a "
            "hydrogen atom",
        ],
        "correct_index": 0,
        "why": "Oxidation of an alcohol gives the carboxylic acid with the "
               "same number of carbons, so ethanol becomes ethanoic acid.",
    },
    {
        "id": "ks4-alcohols-s04",
        "subtopic_slug": "alcohols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which equation correctly represents the fermentation of "
                "glucose to ethanol?",
        "options": [
            "C6H12O6 → C2H5OH + CO2",
            "C6H12O6 → 2C2H5OH + 2CO2",
            "C6H12O6 + O2 → 2C2H5OH + 2CO2",
            "2C6H12O6 → 2C2H5OH + 2CO2",
        ],
        "correct_index": 1,
        "why": "Only this balances — 6 C, 12 H and 6 O on each side — and "
               "fermentation is anaerobic, so no oxygen appears.",
    },
    {
        "id": "ks4-alcohols-h01",
        "subtopic_slug": "alcohols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A company needs very pure ethanol for use as a laboratory "
                "solvent. Evaluate which production method gives the purer "
                "product and explain why.",
        "options": [
            "Fermentation — the yeast filters out all other substances as it "
            "works on the sugar",
            "Hydration — it gives pure ethanol directly, while fermentation "
            "gives a dilute mixture",
            "Fermentation — the ethanol it produces is already more than 90% "
            "pure when collected",
            "Neither — both methods give ethanol of exactly the same purity "
            "in the end",
        ],
        "correct_index": 1,
        "why": "Hydration of ethene converts the whole reactant into "
               "ethanol, whereas fermentation leaves ethanol diluted in a "
               "watery mixture that must be distilled.",
    },
    {
        "id": "ks4-alcohols-h02",
        "subtopic_slug": "alcohols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the ethanol concentration produced by "
                "fermentation cannot rise above about 15%.",
        "options": [
            "The glucose supply always runs out at about the point where 15% "
            "ethanol has formed",
            "Ethanol boils away from the mixture as soon as its "
            "concentration reaches about 15%",
            "Carbon dioxide dissolves in the mixture and prevents the yeast "
            "from working above 15%",
            "Ethanol is toxic to yeast, so above about 15% the yeast dies "
            "and fermentation stops",
        ],
        "correct_index": 3,
        "why": "The yeast makes the ethanol and is then killed by it, so the "
               "reaction stops itself once the concentration gets high "
               "enough.",
    },
    {
        "id": "ks4-alcohols-h03",
        "subtopic_slug": "alcohols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Butanol, C4H9OH, boils at 118 °C but butane, C4H10, boils "
                "at -1 °C, even though the molecules are a similar size. "
                "Explain the difference.",
        "options": [
            "Butanol has a higher relative formula mass, and mass alone sets "
            "the boiling point",
            "Butanol contains oxygen, and oxygen atoms form covalent bonds "
            "that must be broken",
            "Butanol molecules hydrogen bond to each other through their "
            "–OH groups",
            "Butane molecules are branched, so they pack together far more "
            "loosely than butanol",
        ],
        "correct_index": 2,
        "why": "The –OH group lets butanol molecules hydrogen bond to one "
               "another, and those forces need far more energy to overcome.",
    },
    {
        "id": "ks4-alcohols-h04",
        "subtopic_slug": "alcohols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Methanol and ethanol are both alcohols, "
                "so both are safe to drink in small amounts.' Explain the "
                "error.",
        "options": [
            "Methanol is highly toxic — even small amounts can cause "
            "blindness or death",
            "Methanol is safe, but ethanol is toxic and should never be "
            "drunk in any amount",
            "Neither is an alcohol, because only ethanol contains the "
            "hydroxyl –OH group",
            "Both are equally toxic, because every compound containing an "
            "–OH group is a poison",
        ],
        "correct_index": 0,
        "why": "Sharing a functional group does not make two compounds "
               "equally safe — methanol is metabolised to a poison and "
               "ethanol is not.",
    },

    # ── carboxylic-acids ────────────────────────────────────────────────
    {
        "id": "ks4-carboxylic-acids-e01",
        "subtopic_slug": "carboxylic-acids",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the functional group present in every carboxylic acid.",
        "options": [
            "The hydroxyl group, –OH",
            "The amine group, –NH2",
            "The carbon–carbon double bond, C=C",
            "The carboxyl group, –COOH",
        ],
        "correct_index": 3,
        "why": "The –COOH carboxyl group is what releases H+ ions in water "
               "and gives every carboxylic acid its acidic behaviour.",
    },
    {
        "id": "ks4-carboxylic-acids-e02",
        "subtopic_slug": "carboxylic-acids",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the carboxylic acid that is the main acid in vinegar.",
        "options": [
            "Methanoic acid",
            "Ethanoic acid",
            "Propanoic acid",
            "Butanoic acid",
        ],
        "correct_index": 1,
        "why": "Vinegar is a dilute solution of ethanoic acid, CH3COOH, "
               "usually about 4–8% by volume.",
    },
    {
        "id": "ks4-carboxylic-acids-e03",
        "subtopic_slug": "carboxylic-acids",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the formula of methanoic acid.",
        "options": [
            "HCOOH",
            "CH3COOH",
            "CH3OH",
            "C2H5COOH",
        ],
        "correct_index": 0,
        "why": "Methanoic acid has just one carbon atom, and that carbon is "
               "part of the –COOH group itself.",
    },
    {
        "id": "ks4-carboxylic-acids-e04",
        "subtopic_slug": "carboxylic-acids",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the products formed when a carboxylic acid reacts with "
                "a metal carbonate.",
        "options": [
            "A salt and hydrogen only",
            "A salt and water only",
            "A salt, water and carbon dioxide",
            "An ester, water and carbon dioxide",
        ],
        "correct_index": 2,
        "why": "Carboxylic acids follow the same pattern as mineral acids "
               "with carbonates, fizzing as carbon dioxide is released.",
    },
    {
        "id": "ks4-carboxylic-acids-s01",
        "subtopic_slug": "carboxylic-acids",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ethanoic acid reacts with sodium carbonate. Name the salt "
                "that is formed.",
        "options": [
            "Sodium ethanol",
            "Sodium ethanoate",
            "Sodium methanoate",
            "Sodium ethanide",
        ],
        "correct_index": 1,
        "why": "The salt of ethanoic acid is an ethanoate, so with sodium "
               "carbonate it is sodium ethanoate, CH3COONa.",
    },
    {
        "id": "ks4-carboxylic-acids-s02",
        "subtopic_slug": "carboxylic-acids",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A spatula of sodium carbonate is added to dilute ethanoic "
                "acid. Describe and explain what is seen.",
        "options": [
            "Bubbles of gas — carbon dioxide is released as the acid reacts "
            "with the carbonate",
            "The mixture turns a bright orange colour as an ester is slowly "
            "formed in the tube",
            "No change at all — carboxylic acids are far too weak to react "
            "with any carbonate",
            "A white precipitate forms as insoluble sodium ethanoate settles "
            "out of the mixture",
        ],
        "correct_index": 0,
        "why": "Even a weak acid provides enough H+ ions to react with a "
               "carbonate, and the carbon dioxide produced is seen as "
               "effervescence.",
    },
    {
        "id": "ks4-carboxylic-acids-s03",
        "subtopic_slug": "carboxylic-acids",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Esterification is a reversible reaction. Explain what this "
                "means for the mixture left in the flask.",
        "options": [
            "The ester decomposes completely back to acid and alcohol as "
            "soon as it has formed",
            "The reaction stops as soon as any water is made, so no ester is "
            "ever present at all",
            "Ester and water form, but acid and alcohol are also still "
            "present at equilibrium",
            "The ester and the water react to form a completely different "
            "acid and a new alcohol",
        ],
        "correct_index": 2,
        "why": "In a reversible reaction the forward and backward changes "
               "both happen, so all four substances are present together.",
    },
    {
        "id": "ks4-carboxylic-acids-s04",
        "subtopic_slug": "carboxylic-acids",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Magnesium ribbon is added to dilute ethanoic acid. Predict "
                "what is observed and name the gas given off.",
        "options": [
            "No reaction at all — carboxylic acids do not react with metals",
            "Fizzing, giving off carbon dioxide, and the magnesium slowly "
            "dissolves away",
            "Fizzing, giving off oxygen, and a white precipitate forms in "
            "the tube",
            "Fizzing, giving off hydrogen, and the magnesium slowly "
            "dissolves",
        ],
        "correct_index": 3,
        "why": "Acid plus metal always gives a salt and hydrogen — here "
               "magnesium ethanoate and hydrogen gas.",
    },
    {
        "id": "ks4-carboxylic-acids-h01",
        "subtopic_slug": "carboxylic-acids",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two solutions have the same concentration: one is ethanoic "
                "acid, the other hydrochloric acid. Predict which reacts "
                "faster with magnesium ribbon, and explain.",
        "options": [
            "Ethanoic acid, because its molecules are larger and so collide "
            "more often with the metal",
            "They react at exactly the same rate, because both solutions "
            "contain the same concentration of acid",
            "Hydrochloric acid — it fully ionises, giving a higher "
            "concentration of H+ ions",
            "Ethanoic acid, because each carboxylic acid molecule releases "
            "two H+ ions rather than one",
        ],
        "correct_index": 2,
        "why": "Rate depends on the concentration of H+ ions, and a strong "
               "acid ionises fully while a weak acid only partly ionises.",
    },
    {
        "id": "ks4-carboxylic-acids-h02",
        "subtopic_slug": "carboxylic-acids",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A perfume manufacturer needs a compound with a fruity smell. "
                "Suggest which two families of compound should be reacted "
                "together, and name the product type.",
        "options": [
            "Two alcohols, giving an ether as the product",
            "Two carboxylic acids, giving a longer-chain acid",
            "An alkene and an alcohol, giving a polymer",
            "A carboxylic acid and an alcohol, giving an ester",
        ],
        "correct_index": 3,
        "why": "Esters are the compounds with characteristic fruity smells, "
               "and they are made from a carboxylic acid and an alcohol.",
    },
    {
        "id": "ks4-carboxylic-acids-h03",
        "subtopic_slug": "carboxylic-acids",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ethanol can be converted into ethanoic acid in the "
                "laboratory. Describe the type of reaction and name a "
                "reagent that brings it about.",
        "options": [
            "Reduction, using hydrogen gas over a nickel catalyst",
            "Oxidation, using an oxidising agent such as potassium "
            "dichromate",
            "Hydration, using steam with a phosphoric acid catalyst",
            "Neutralisation, using dilute sodium hydroxide solution",
        ],
        "correct_index": 1,
        "why": "An alcohol is oxidised to the carboxylic acid with the same "
               "number of carbons, which is what an oxidising agent such as "
               "potassium dichromate does.",
    },
    {
        "id": "ks4-carboxylic-acids-h04",
        "subtopic_slug": "carboxylic-acids",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student states: 'Ethanoic acid is a weak acid, so a "
                "solution of it must be dilute.' Explain the error.",
        "options": [
            "Strength is how far it ionises; concentration is how much is "
            "dissolved",
            "There is no error — a weak acid can only ever be made up as a "
            "dilute solution",
            "The error is that ethanoic acid is in fact a strong acid, just "
            "like hydrochloric acid",
            "The error is that a weak acid must always be more concentrated "
            "than a strong acid is",
        ],
        "correct_index": 0,
        "why": "Strength and concentration are separate ideas: a weak acid "
               "can be very concentrated, and a strong acid very dilute.",
    },

    # ── addition-polymerisation ─────────────────────────────────────────
    {
        "id": "ks4-addition-polymerisation-e01",
        "subtopic_slug": "addition-polymerisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the feature a monomer must have to take part in "
                "addition polymerisation.",
        "options": [
            "A carbon–carbon double bond",
            "Two –OH groups, one at each end",
            "One –COOH group and one –NH2 group",
            "A ring of six carbon atoms",
        ],
        "correct_index": 0,
        "why": "The C=C bond opens up so that each monomer can bond to the "
               "next, which is what builds the chain.",
    },
    {
        "id": "ks4-addition-polymerisation-e02",
        "subtopic_slug": "addition-polymerisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the polymer formed from the monomer propene.",
        "options": [
            "Poly(propane)",
            "Poly(ethene)",
            "Propanol",
            "Poly(propene)",
        ],
        "correct_index": 3,
        "why": "An addition polymer is named 'poly' plus the monomer, so "
               "propene gives poly(propene).",
    },
    {
        "id": "ks4-addition-polymerisation-e03",
        "subtopic_slug": "addition-polymerisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Chloroethene, CH2=CHCl, polymerises to make a common "
                "plastic. Name it.",
        "options": [
            "PTFE, poly(tetrafluoroethene)",
            "PVC, poly(chloroethene)",
            "Poly(ethene)",
            "Polyester",
        ],
        "correct_index": 1,
        "why": "Chloroethene was once called vinyl chloride, so its polymer "
               "is polyvinyl chloride — PVC, or poly(chloroethene).",
    },
    {
        "id": "ks4-addition-polymerisation-e04",
        "subtopic_slug": "addition-polymerisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how many products are formed in an addition "
                "polymerisation reaction.",
        "options": [
            "Two — the polymer and water",
            "Two — the polymer and hydrogen",
            "One — the polymer only",
            "Three — the polymer, water and carbon dioxide",
        ],
        "correct_index": 2,
        "why": "Every atom of every monomer ends up in the chain, so the "
               "polymer is the only product.",
    },
    {
        "id": "ks4-addition-polymerisation-s01",
        "subtopic_slug": "addition-polymerisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Poly(propene) is made from the monomer CH2=CHCH3. Which is "
                "its repeat unit?",
        "options": [
            "(–CH2=CHCH3–)n",
            "(–CH2–CH2–CH3–)n",
            "(–CH2–CH(CH3)–)n",
            "(–CH3–CH2–)n",
        ],
        "correct_index": 2,
        "why": "The double bond opens to leave two single bonds continuing "
               "the chain; the CH3 side group stays where it was.",
    },
    {
        "id": "ks4-addition-polymerisation-s02",
        "subtopic_slug": "addition-polymerisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A polymer has the repeat unit (–CF2–CF2–)n. Determine the "
                "monomer it was made from.",
        "options": [
            "CF3–CF3",
            "CF2=CF2",
            "CF2–CF2",
            "CHF=CHF",
        ],
        "correct_index": 1,
        "why": "Putting the C=C double bond back between the two backbone "
               "carbons of the repeat unit gives the monomer, "
               "tetrafluoroethene.",
    },
    {
        "id": "ks4-addition-polymerisation-s03",
        "subtopic_slug": "addition-polymerisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why poly(ethene) does not decolourise bromine water "
                "even though it is made from ethene.",
        "options": [
            "The polymer chains are far too long for bromine molecules to "
            "reach them at all",
            "Bromine water reacts only with gases, and the polymer is a "
            "solid at room temperature",
            "The polymer still contains C=C bonds, but they are hidden away "
            "inside the coiled chain",
            "All the C=C bonds opened during polymerisation, so the polymer "
            "is saturated",
        ],
        "correct_index": 3,
        "why": "The double bonds are used up in forming the chain, leaving "
               "only single C–C bonds — and saturated molecules do not react "
               "with bromine.",
    },
    {
        "id": "ks4-addition-polymerisation-s04",
        "subtopic_slug": "addition-polymerisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why most addition polymers cause long-lasting "
                "environmental problems.",
        "options": [
            "Their C–C backbones are unreactive, so microorganisms cannot "
            "break them down",
            "They dissolve slowly in rainwater, releasing toxic monomers "
            "into the rivers",
            "They decompose very quickly, releasing large amounts of carbon "
            "dioxide gas",
            "They react with oxygen in the air to form poisonous carbon "
            "monoxide gas",
        ],
        "correct_index": 0,
        "why": "The saturated carbon chain has no group an enzyme can "
               "attack, so the polymer is non-biodegradable and persists for "
               "centuries.",
    },
    {
        "id": "ks4-addition-polymerisation-h01",
        "subtopic_slug": "addition-polymerisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "2800 ethene molecules polymerise completely into one chain. "
                "The relative formula mass of ethene is 28. Calculate the "
                "relative formula mass of the polymer chain.",
        "options": [
            "28",
            "2800",
            "39 200",
            "78 400",
        ],
        "correct_index": 3,
        "why": "No atoms are lost in addition polymerisation, so the chain "
               "mass is simply 2800 × 28 = 78 400.",
    },
    {
        "id": "ks4-addition-polymerisation-h02",
        "subtopic_slug": "addition-polymerisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the atom economy of making poly(ethene) from ethene "
                "with that of making ethanol from ethene and steam.",
        "options": [
            "Both are 100%, because in each case every atom ends up in the "
            "single product",
            "Polymerisation is 100%, but making ethanol is lower because "
            "water is lost as a by-product",
            "Polymerisation is lower, because a small molecule is released "
            "at every join in the chain",
            "Making ethanol is 100%, but polymerisation is lower because "
            "some monomer is always left over",
        ],
        "correct_index": 0,
        "why": "Both are addition reactions with a single product, so all "
               "the reactant atoms are in the desired product either way.",
    },
    {
        "id": "ks4-addition-polymerisation-h03",
        "subtopic_slug": "addition-polymerisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate incineration as a way of disposing of waste "
                "addition polymers.",
        "options": [
            "Ideal — the polymers break down into harmless monomers that can "
            "be collected and reused",
            "Ideal — no carbon dioxide can be released, because addition "
            "polymers contain no carbon",
            "Mixed — energy is recovered, but carbon dioxide and toxic gases "
            "are released",
            "Useless — addition polymers simply cannot be burnt at any "
            "temperature that is reachable",
        ],
        "correct_index": 2,
        "why": "Burning waste plastic does recover useful energy, but it "
               "also adds carbon dioxide and, from polymers such as PVC, "
               "toxic gases.",
    },
    {
        "id": "ks4-addition-polymerisation-h04",
        "subtopic_slug": "addition-polymerisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why poly(ethene) is a solid at room temperature "
                "while ethene itself is a gas.",
        "options": [
            "The polymer contains ionic bonds, which hold it together as a "
            "solid lattice",
            "The polymer's very long chains have much stronger forces "
            "between them",
            "The polymer's covalent bonds are stronger than the covalent "
            "bonds in ethene",
            "The polymer contains no double bonds, and only a double bond "
            "allows a gas to form",
        ],
        "correct_index": 1,
        "why": "Intermolecular forces grow with chain length, and a polymer "
               "chain of thousands of carbons has forces far too strong for "
               "it to be a gas.",
    },

    # ── condensation-polymerisation ─────────────────────────────────────
    {
        "id": "ks4-condensation-polymerisation-e01",
        "subtopic_slug": "condensation-polymerisation",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the small molecule usually lost during condensation "
                "polymerisation.",
        "options": [
            "Carbon dioxide",
            "Water",
            "Hydrogen",
            "Oxygen",
        ],
        "correct_index": 1,
        "why": "Each join takes an –OH from one monomer and an H from the "
               "other, so a molecule of water is released.",
    },
    {
        "id": "ks4-condensation-polymerisation-e02",
        "subtopic_slug": "condensation-polymerisation",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the type of link found in a polyamide.",
        "options": [
            "The ester link, –COO–",
            "The carbon–carbon link, –C–C–",
            "The amide link, –CO–NH–",
            "The hydroxyl link, –O–H–",
        ],
        "correct_index": 2,
        "why": "A polyamide is built from –COOH and –NH2 groups, and joining "
               "them gives the –CO–NH– amide link.",
    },
    {
        "id": "ks4-condensation-polymerisation-e03",
        "subtopic_slug": "condensation-polymerisation",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State how many functional groups each monomer must have for "
                "condensation polymerisation.",
        "options": [
            "Two, one at each end of the molecule",
            "One, positioned in the middle of the molecule",
            "Three, spaced evenly along the chain",
            "None — a C=C double bond is enough",
        ],
        "correct_index": 0,
        "why": "A monomer needs a reactive group at both ends, so the chain "
               "can keep growing in both directions.",
    },
    {
        "id": "ks4-condensation-polymerisation-e04",
        "subtopic_slug": "condensation-polymerisation",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the polymer used to make drinks bottles, made from a "
                "diol and a dicarboxylic acid.",
        "options": [
            "PVC",
            "Nylon-6,6",
            "PTFE",
            "PET, a polyester",
        ],
        "correct_index": 3,
        "why": "A diol plus a dicarboxylic acid gives ester links, so the "
               "polymer is a polyester — PET.",
    },
    {
        "id": "ks4-condensation-polymerisation-s01",
        "subtopic_slug": "condensation-polymerisation",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Silk and wool are natural polyamides. Deduce what their "
                "monomers must contain.",
        "options": [
            "An –NH2 group and a –COOH group in the same molecule",
            "Two –OH groups in the same molecule",
            "A C=C double bond and an –OH group",
            "Two –COOH groups and no other functional group",
        ],
        "correct_index": 0,
        "why": "Amide links form between –COOH and –NH2, so a single monomer "
               "carrying both can build the whole chain.",
    },
    {
        "id": "ks4-condensation-polymerisation-s02",
        "subtopic_slug": "condensation-polymerisation",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a polyester can be broken down by hydrolysis but "
                "poly(ethene) cannot.",
        "options": [
            "Poly(ethene) chains are longer, so water cannot reach the "
            "middle of them",
            "The polyester dissolves readily in water, so it simply washes "
            "away instead",
            "Poly(ethene) contains oxygen atoms that repel the water "
            "molecules away",
            "Ester links can be split by water; poly(ethene)'s C–C backbone "
            "cannot",
        ],
        "correct_index": 3,
        "why": "Hydrolysis reverses the condensation that made the ester "
               "link; an unreactive carbon–carbon backbone offers water "
               "nothing to attack.",
    },
    {
        "id": "ks4-condensation-polymerisation-s03",
        "subtopic_slug": "condensation-polymerisation",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why some condensation polymers are easier to recycle "
                "than addition polymers.",
        "options": [
            "They melt at much lower temperatures, so they can be remoulded "
            "far more cheaply",
            "They dissolve in cold water, so the monomers can simply be "
            "filtered off afterwards",
            "Their links can be hydrolysed back to the monomers, which are "
            "then re-polymerised",
            "They contain no carbon at all, so they leave no residue when "
            "they are broken down",
        ],
        "correct_index": 2,
        "why": "Hydrolysing the ester or amide links recovers the original "
               "monomers, which can then be used to make new polymer.",
    },
    {
        "id": "ks4-condensation-polymerisation-s04",
        "subtopic_slug": "condensation-polymerisation",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Nylon is often described as a plastic like poly(ethene). "
                "Explain why chemists classify the two differently.",
        "options": [
            "Nylon is a natural polymer, whereas poly(ethene) is entirely "
            "synthetic",
            "Nylon is a condensation polymer with amide links; poly(ethene) "
            "is an addition polymer",
            "Nylon is a monomer, whereas poly(ethene) is a polymer made from "
            "many monomers",
            "Nylon contains only carbon and hydrogen, whereas poly(ethene) "
            "also contains nitrogen",
        ],
        "correct_index": 1,
        "why": "Nylon's monomers join through amide links with water lost; "
               "ethene's join by opening C=C bonds with nothing lost.",
    },
    {
        "id": "ks4-condensation-polymerisation-h01",
        "subtopic_slug": "condensation-polymerisation",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "1 mole of a diol reacts completely with 1 mole of a "
                "dicarboxylic acid to make a long polyester chain. Calculate "
                "the approximate amount of water released, in moles.",
        "options": [
            "0.5 mol",
            "1 mol",
            "2 mol",
            "4 mol",
        ],
        "correct_index": 2,
        "why": "Each monomer has two reactive groups, so each pair of "
               "monomers makes two ester links and releases two moles of "
               "water.",
    },
    {
        "id": "ks4-condensation-polymerisation-h02",
        "subtopic_slug": "condensation-polymerisation",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student draws a polyester repeat unit in which an –OH "
                "group and a –COOH group are still shown between the two "
                "monomer units. Explain what is wrong.",
        "options": [
            "Nothing is wrong — both groups stay unchanged inside the repeat "
            "unit of the polymer",
            "Those groups should have joined, losing water and forming an "
            "ester link",
            "The –OH should have been replaced by an amide link, –CO–NH–, "
            "instead of an ester link",
            "The two monomers should have been joined by a C=C double bond "
            "in place of the groups",
        ],
        "correct_index": 1,
        "why": "The whole point of condensation is that the two groups react "
               "together: –OH plus –COOH gives –COO– and a molecule of water.",
    },
    {
        "id": "ks4-condensation-polymerisation-h03",
        "subtopic_slug": "condensation-polymerisation",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a monomer with only one –COOH group and no other "
                "functional group cannot form a condensation polymer.",
        "options": [
            "It has no C=C double bond, so there is nothing that can open to "
            "start a chain",
            "One –COOH group is too acidic and would destroy the growing "
            "polymer chain",
            "It would form a ring instead, closing the chain before it had a "
            "chance to grow",
            "It can join at one end only, so the chain stops instead of "
            "growing",
        ],
        "correct_index": 3,
        "why": "A chain only grows if each unit can bond on both sides, so a "
               "monomer with a single reactive group is a chain-stopper.",
    },
    {
        "id": "ks4-condensation-polymerisation-h04",
        "subtopic_slug": "condensation-polymerisation",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "PET bottles can be depolymerised by hydrolysis and then "
                "remade into new PET. Evaluate this as a way of dealing with "
                "plastic waste.",
        "options": [
            "Good — the monomers are recovered and reused, so less crude oil "
            "is needed",
            "Poor — hydrolysis destroys the monomers, so nothing at all can "
            "be recovered from it",
            "Poor — PET is an addition polymer and so it cannot be "
            "hydrolysed under any conditions",
            "Good — hydrolysis converts the PET directly into a clean fuel "
            "with no waste at all",
        ],
        "correct_index": 0,
        "why": "Recovering the original monomers closes the loop: new PET "
               "can be made without drawing fresh feedstock from crude oil.",
    },

    # ── amino-acids ─────────────────────────────────────────────────────
    {
        "id": "ks4-amino-acids-e01",
        "subtopic_slug": "amino-acids",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the two functional groups present in every amino acid.",
        "options": [
            "–OH and –COOH",
            "–NH2 and –OH",
            "–NH2 and –COOH",
            "C=C and –COOH",
        ],
        "correct_index": 2,
        "why": "Every amino acid carries a basic amine group and an acidic "
               "carboxyl group, which is how it can join at both ends.",
    },
    {
        "id": "ks4-amino-acids-e02",
        "subtopic_slug": "amino-acids",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Amino acids differ from one another in only one way. State "
                "what it is.",
        "options": [
            "The number of –COOH groups that they contain",
            "The number of nitrogen atoms in the backbone",
            "Whether they contain a carbon–carbon double bond",
            "The R group, the side chain on the central carbon",
        ],
        "correct_index": 3,
        "why": "All amino acids share the same H2N–CH–COOH backbone; only "
               "the R side chain changes from one to the next.",
    },
    {
        "id": "ks4-amino-acids-e03",
        "subtopic_slug": "amino-acids",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the simplest amino acid, in which the R group is a "
                "single hydrogen atom.",
        "options": [
            "Alanine",
            "Glycine",
            "Cysteine",
            "Ethanoic acid",
        ],
        "correct_index": 1,
        "why": "Glycine is H2NCH2COOH — its side chain is just a hydrogen "
               "atom, making it the smallest amino acid.",
    },
    {
        "id": "ks4-amino-acids-e04",
        "subtopic_slug": "amino-acids",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Proteins are natural polymers. Name their monomers.",
        "options": [
            "Amino acids",
            "Nucleotides",
            "Glucose molecules",
            "Alkene molecules",
        ],
        "correct_index": 0,
        "why": "A protein is a long chain of amino acids joined end to end "
               "by peptide bonds.",
    },
    {
        "id": "ks4-amino-acids-s01",
        "subtopic_slug": "amino-acids",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why amino acids are described as amphoteric.",
        "options": [
            "They contain two acidic groups, so they can donate two protons "
            "each",
            "They contain an acidic –COOH group and a basic –NH2 group",
            "They dissolve in both water and organic solvents equally well",
            "They can act as either a monomer or a polymer, depending on pH",
        ],
        "correct_index": 1,
        "why": "Amphoteric means behaving as both an acid and a base, and an "
               "amino acid carries one group of each kind.",
    },
    {
        "id": "ks4-amino-acids-s02",
        "subtopic_slug": "amino-acids",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Two amino acids join together. Name the product and state "
                "how many peptide bonds it contains.",
        "options": [
            "A dipeptide, containing one peptide bond",
            "A dipeptide, containing two peptide bonds",
            "A polypeptide, containing one peptide bond",
            "A protein, containing two peptide bonds",
        ],
        "correct_index": 0,
        "why": "Two units make one join, so a dipeptide contains exactly one "
               "peptide bond.",
    },
    {
        "id": "ks4-amino-acids-s03",
        "subtopic_slug": "amino-acids",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Three amino acids join to form a single chain. Calculate the "
                "number of water molecules released.",
        "options": [
            "Zero",
            "One",
            "Three",
            "Two",
        ],
        "correct_index": 3,
        "why": "Three units in a chain need two joins, and each join "
               "releases one molecule of water.",
    },
    {
        "id": "ks4-amino-acids-s04",
        "subtopic_slug": "amino-acids",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the reaction that breaks a protein back down into amino "
                "acids, and state what is added.",
        "options": [
            "Condensation, and water is added",
            "Oxidation, and oxygen is added",
            "Hydrolysis, and water is added",
            "Hydrolysis, and hydrogen is added",
        ],
        "correct_index": 2,
        "why": "Hydrolysis is the reverse of condensation: water is put back "
               "across each peptide bond to split it.",
    },
    {
        "id": "ks4-amino-acids-h01",
        "subtopic_slug": "amino-acids",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Glycine, H2NCH2COOH, has a relative formula mass of 75. Two "
                "glycine molecules join to form a dipeptide. Calculate the "
                "relative formula mass of the dipeptide.",
        "options": [
            "132",
            "150",
            "168",
            "75",
        ],
        "correct_index": 0,
        "why": "A water molecule of mass 18 is lost as the peptide bond "
               "forms, so 75 + 75 - 18 = 132.",
    },
    {
        "id": "ks4-amino-acids-h02",
        "subtopic_slug": "amino-acids",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "One amino acid in a protein's sequence is replaced by a "
                "different one. Explain how this may change the protein's "
                "function.",
        "options": [
            "The protein gains an extra peptide bond, which makes the whole "
            "chain longer",
            "The protein loses all of its –COOH groups, so it can no longer "
            "act as an acid",
            "A different R group changes how the chain folds, altering the "
            "3D shape",
            "The number of amino acids available in the body falls from 20 "
            "down to 19",
        ],
        "correct_index": 2,
        "why": "A protein works by its shape, and the shape comes from how "
               "the R side chains interact as the chain folds.",
    },
    {
        "id": "ks4-amino-acids-h03",
        "subtopic_slug": "amino-acids",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A dipeptide is hydrolysed. Predict the products and explain "
                "how they are formed.",
        "options": [
            "One amino acid and one water molecule, as the chain simply "
            "shortens by a unit",
            "A polypeptide and carbon dioxide, as the peptide bond "
            "decomposes on heating",
            "Two amino acids and one water molecule, both released together "
            "from the chain",
            "Two amino acids, formed as water adds across the peptide bond",
        ],
        "correct_index": 3,
        "why": "Hydrolysis puts the lost water back: the –OH goes to one "
               "fragment and the –H to the other, regenerating both amino "
               "acids.",
    },
    {
        "id": "ks4-amino-acids-h04",
        "subtopic_slug": "amino-acids",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare the biodegradability of a protein with that of "
                "poly(ethene), and explain the difference.",
        "options": [
            "Both break down quickly, because every polymer is attacked by "
            "microorganisms",
            "The protein breaks down, because enzymes can hydrolyse its "
            "peptide bonds",
            "Poly(ethene) breaks down faster, because its chains are shorter "
            "than a protein's",
            "Neither breaks down at all, because both are made of very long "
            "polymer chains",
        ],
        "correct_index": 1,
        "why": "Peptide bonds can be split by water with an enzyme, whereas "
               "poly(ethene)'s carbon–carbon backbone offers no such point "
               "of attack.",
    },

    # ── dna-naturally-occurring-polymers ────────────────────────────────
    {
        "id": "ks4-dna-naturally-occurring-polymers-e01",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the monomers from which DNA is built.",
        "options": [
            "Amino acids",
            "Glucose molecules",
            "Alkene molecules",
            "Nucleotides",
        ],
        "correct_index": 3,
        "why": "DNA is a polymer of nucleotide monomers, joined into two "
               "long strands.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-e02",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the number of different nucleotide monomers found in "
                "DNA.",
        "options": [
            "Four",
            "Two",
            "Twenty",
            "Sixty-four",
        ],
        "correct_index": 0,
        "why": "There are four nucleotides, differing in their base — A, T, "
               "G and C.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-e03",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the shape formed by a DNA molecule.",
        "options": [
            "A single straight chain of monomers",
            "A branched network of many chains",
            "A double helix of two strands",
            "A flat ring of joined monomers",
        ],
        "correct_index": 2,
        "why": "Two polymer strands twist around one another, held together "
               "by complementary base pairs, forming a double helix.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-e04",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the monomer from which both starch and cellulose are "
                "built.",
        "options": [
            "Fructose",
            "Glucose",
            "Amino acids",
            "Nucleotides",
        ],
        "correct_index": 1,
        "why": "Both are polymers of glucose; they differ in how those "
               "glucose units are linked together.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-s01",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Natural rubber is made from isoprene monomers, which contain "
                "carbon–carbon double bonds. Deduce the type of "
                "polymerisation involved.",
        "options": [
            "Condensation polymerisation, because every natural polymer must "
            "lose water as it forms",
            "Addition polymerisation, because the double bonds open and join "
            "directly",
            "Hydrolysis, because rubber is broken down from much larger "
            "molecules made by the plant",
            "Neutralisation, because the isoprene units behave as weak acids "
            "when they join",
        ],
        "correct_index": 1,
        "why": "A monomer with a C=C bond polymerises by addition — the "
               "double bond opens and no small molecule is lost.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-s02",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give one reason why natural polymers such as starch and "
                "protein cause fewer environmental problems than "
                "poly(ethene).",
        "options": [
            "They are made in much smaller quantities than poly(ethene) ever "
            "is",
            "They dissolve completely in cold water, so they simply wash "
            "away harmlessly",
            "Enzymes can break them down, so they are biodegradable",
            "They contain no carbon at all, so they cannot add to greenhouse "
            "gases",
        ],
        "correct_index": 2,
        "why": "Their condensation links can be hydrolysed by enzymes, so "
               "living organisms return them to their monomers instead of "
               "leaving them to persist.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-s03",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The order of the nucleotides along a strand of DNA "
                "determines something important. State what.",
        "options": [
            "Which proteins the cell makes, and so the amino acid sequence "
            "in them",
            "How many nucleotide monomers the DNA molecule contains "
            "altogether",
            "The colour that the DNA molecule turns when it is stained in a "
            "laboratory",
            "Whether the DNA behaves as an addition or a condensation "
            "polymer",
        ],
        "correct_index": 0,
        "why": "As with any polymer, the sequence of monomers sets the "
               "function — here, the amino acid order in the protein made "
               "from it.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-s04",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "PLA is a biodegradable polymer made from corn starch. "
                "Suggest one advantage and one disadvantage of using it "
                "instead of poly(ethene) for food packaging.",
        "options": [
            "Advantage: it is much stronger; disadvantage: it is made from "
            "crude oil",
            "Advantage: it never breaks down at all; disadvantage: it is "
            "expensive to manufacture",
            "Advantage: it is made from crude oil; disadvantage: it is not "
            "at all biodegradable",
            "Advantage: it is biodegradable; disadvantage: it uses land "
            "needed for food",
        ],
        "correct_index": 3,
        "why": "A plant-based polymer decomposes rather than persisting, but "
               "growing the crop competes with growing food.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-h01",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Both DNA and nylon are condensation polymers. Explain what "
                "this tells you about the way their monomers join.",
        "options": [
            "Each join releases a small molecule, so not every monomer atom "
            "is in the chain",
            "Each monomer contains a C=C bond that opens as the chain grows "
            "longer",
            "Each join takes in a water molecule from the surroundings as it "
            "is formed",
            "Each monomer can only ever join to one other monomer, so the "
            "chains always stay short",
        ],
        "correct_index": 0,
        "why": "Condensation means a small molecule — usually water — is "
               "lost at every join, so the atom economy is below 100%.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-h02",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student claims that because DNA is a polymer, it must be "
                "non-biodegradable like poly(ethene). Evaluate this claim.",
        "options": [
            "Correct — all polymers resist being broken down by living "
            "things",
            "Correct — DNA persists completely unchanged for millions of "
            "years in any conditions",
            "Incorrect — DNA is not really a polymer at all, so the "
            "comparison cannot be made",
            "Incorrect — DNA's condensation links can be hydrolysed by "
            "enzymes",
        ],
        "correct_index": 3,
        "why": "Being a polymer says nothing about biodegradability; what "
               "matters is whether the links between monomers can be broken.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-h03",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the monomer needed to make natural rubber with the "
                "monomer needed to make a protein.",
        "options": [
            "Both need a monomer carrying two functional groups at opposite "
            "ends",
            "Rubber needs a monomer with a C=C bond; a protein needs two "
            "functional groups",
            "Rubber needs two functional groups; a protein needs a "
            "carbon–carbon double bond",
            "Both need a monomer with a C=C double bond that opens as the "
            "chain forms",
        ],
        "correct_index": 1,
        "why": "Rubber is an addition polymer, so its monomer needs a double "
               "bond; a protein is a condensation polymer, so its monomer "
               "needs a group at each end.",
    },
    {
        "id": "ks4-dna-naturally-occurring-polymers-h04",
        "subtopic_slug": "dna-naturally-occurring-polymers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A plant-based plastic is advertised as 'made from plants, so "
                "it is carbon neutral'. Suggest one reason why this claim "
                "may not be fully justified.",
        "options": [
            "Plants take in carbon dioxide, so no carbon is involved in the "
            "process at all",
            "Biodegradable plastics release no carbon dioxide at all when "
            "they decompose",
            "Energy from fossil fuels is used to grow, harvest and process "
            "the crop",
            "Plant-based plastics contain no carbon atoms, so they cannot "
            "possibly be neutral",
        ],
        "correct_index": 2,
        "why": "Carbon neutrality has to account for the whole process, and "
               "farming, transport and manufacture usually burn fossil "
               "fuels.",
    },
]
