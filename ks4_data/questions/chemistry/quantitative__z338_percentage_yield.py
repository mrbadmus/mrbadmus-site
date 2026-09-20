"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`percentage-yield`.

AQA 4.3.3.1, Chemistry only. The formula is worked in all three directions —
percentage from two masses, actual yield from a percentage, theoretical yield
from an actual yield and a percentage — and then pressed into the places a
yield actually goes wrong: product left on the filter paper or dissolved in
the wash water, a product weighed before it is dry, an impure reactant, a side
reaction, a reaction stopped too soon, a reversible reaction that never
finishes. Harder rows scale a yield up to industry, combine a yield with a
purity, and separate what a yield measures from what it does not.

⚠️ FOUNDATION TIER, triple only. No mole appears in any stem, option or `why` —
every theoretical yield is either given or derived from a mass ratio stated in
the stem, which is how AQA asks this at Foundation.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-percentage-yield-e05",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Before starting a preparation, a chemist works out its "
                "theoretical yield. Identify what that figure represents.",
        "options": [
            "The greatest mass of product the reactants used could make",
            "The mass of product a student manages to collect and dry",
            "The mass of the reactants that were weighed out at the start",
            "The mass of product a reaction makes in the first minute",
        ],
        "correct_index": 0,
        "why": "The theoretical yield is the maximum the balanced equation "
               "allows from the reactants supplied, before any practical "
               "losses.",
    },
    {
        "id": "ks4-percentage-yield-e06",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "The balanced equation predicts 20.0 g of product, but only "
                "15.0 g is recovered after filtering and drying. Calculate "
                "the percentage yield.",
        "options": [
            "5.0%",
            "75.0%",
            "133%",
            "35.0%",
        ],
        "correct_index": 1,
        "why": "(15.0 ÷ 20.0) × 100 = 75.0%.",
    },
    {
        "id": "ks4-percentage-yield-e07",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name one reason the mass of product collected is usually less "
                "than the theoretical yield.",
        "options": [
            "The balance used to weigh the product reads slightly low",
            "The reactants weigh less in total than the products do",
            "Some of the product is lost while it is being transferred",
            "The product takes in moisture from the air as it is made",
        ],
        "correct_index": 2,
        "why": "Product is left behind on glassware, in filter paper and in "
               "solution at every transfer, so less of it reaches the "
               "balance.",
    },
    {
        "id": "ks4-percentage-yield-e08",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the percentage yield of a reaction measures.",
        "options": [
            "How pure the product is once it has been dried thoroughly",
            "How quickly the reaction reaches the end of its course",
            "How much of the reactant mass ends up as useful product",
            "How much of the possible product was actually obtained",
        ],
        "correct_index": 3,
        "why": "Percentage yield compares what was collected with the maximum "
               "the reactants could have given.",
    },
    {
        "id": "ks4-percentage-yield-e09",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the calculation that gives the actual yield from a "
                "theoretical yield and a percentage yield.",
        "options": [
            "theoretical yield × percentage yield ÷ 100",
            "theoretical yield ÷ percentage yield × 100",
            "percentage yield ÷ theoretical yield × 100",
            "theoretical yield + percentage yield ÷ 100",
        ],
        "correct_index": 0,
        "why": "Rearranging percentage yield = (actual ÷ theoretical) × 100 "
               "gives actual = theoretical × percentage ÷ 100.",
    },
    {
        "id": "ks4-percentage-yield-e10",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student is told that 30.0 g of product is the most a "
                "reaction can make, and that it normally delivers four fifths "
                "of that. Calculate the mass expected.",
        "options": [
            "37.5 g",
            "24.0 g",
            "6.0 g",
            "7.5 g",
        ],
        "correct_index": 1,
        "why": "Four fifths of 30.0 g is 30.0 × 0.80 = 24.0 g, a percentage "
               "yield of 80%.",
    },
    {
        "id": "ks4-percentage-yield-e11",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the reason a reversible reaction gives a percentage "
                "yield below 100%.",
        "options": [
            "The products turn back into reactants, so it does not complete",
            "The reactants are used up before the reaction can begin properly",
            "The reaction gives out heat, which destroys some of the product",
            "The products dissolve in one another and cannot be separated",
        ],
        "correct_index": 0,
        "why": "In a reversible reaction the reverse change removes product as "
               "fast as the forward change makes it, so some reactant is "
               "always left.",
    },
    {
        "id": "ks4-percentage-yield-e12",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why a manufacturer prefers a reaction with a high "
                "percentage yield.",
        "options": [
            "A high yield makes the reaction finish in a shorter time",
            "A high yield removes the need to purify the product afterwards "
            "at all",
            "A high yield keeps the reaction at a lower temperature",
            "Less raw material is wasted, so the process costs less to run",
        ],
        "correct_index": 3,
        "why": "Raw materials cost money, so a process that turns more of them "
               "into saleable product is cheaper and less wasteful.",
    },
    {
        "id": "ks4-percentage-yield-e13",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student collects 5.0 g of product from a reaction that "
                "could at most have made 8.0 g. Calculate the percentage "
                "yield.",
        "options": [
            "62.5%",
            "37.5%",
            "160%",
            "40.0%",
        ],
        "correct_index": 0,
        "why": "(5.0 ÷ 8.0) × 100 = 62.5%.",
    },
    {
        "id": "ks4-percentage-yield-e14",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the stage of a salt preparation at which product is "
                "most easily lost.",
        "options": [
            "Filtering the crystals out of the solution",
            "Weighing out the solid reactant on a balance",
            "Stirring the mixture around in the beaker",
            "Reading the thermometer in the warm acid",
        ],
        "correct_index": 0,
        "why": "Crystals cling to the filter paper and stay behind in the "
               "solution that drains through, so mass is lost at that step.",
    },
    {
        "id": "ks4-percentage-yield-e15",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what must be done to a solid product before its mass is "
                "measured, if the percentage yield is to be correct.",
        "options": [
            "It must be warmed gently so that it weighs a little less",
            "It must be ground to a fine powder in a pestle and mortar",
            "It must be dried completely, so no water is weighed with it",
            "It must be dissolved again to check that it is a pure solid",
        ],
        "correct_index": 2,
        "why": "Water left on the crystals counts towards the mass on the "
               "balance, which makes the percentage yield look higher than it "
               "is.",
    },
    {
        "id": "ks4-percentage-yield-e16",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction gives an actual yield of 9.0 g at a percentage "
                "yield of 50%. Calculate the theoretical yield.",
        "options": [
            "4.5 g",
            "9.5 g",
            "45.0 g",
            "18.0 g",
        ],
        "correct_index": 3,
        "why": "The 9.0 g is half of the maximum, so the theoretical yield is "
               "9.0 × 100 ÷ 50 = 18.0 g.",
    },
    {
        "id": "ks4-percentage-yield-e17",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the pair of quantities needed to calculate a "
                "percentage yield.",
        "options": [
            "The actual yield and the theoretical yield",
            "The mass of reactant used and the time the reaction took",
            "The atom economy and the actual yield",
            "The product's mass and the temperature",
        ],
        "correct_index": 0,
        "why": "Percentage yield is the actual yield expressed as a percentage "
               "of the theoretical yield, and needs nothing else.",
    },
    {
        "id": "ks4-percentage-yield-e18",
        "subtopic_slug": "percentage-yield",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student repeats a preparation using twice the mass of every "
                "reactant and works just as carefully. Predict the effect on "
                "the percentage yield.",
        "options": [
            "It doubles, because twice as much product is now collected",
            "It stays about the same, because both yields have doubled",
            "It halves, because the reactants are shared between more product",
            "It rises towards 100%, because a larger batch loses less",
        ],
        "correct_index": 1,
        "why": "Percentage yield is a ratio, so doubling both the actual and "
               "the theoretical yield leaves it unchanged.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-percentage-yield-s05",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a preparation of copper sulfate crystals the theoretical "
                "yield is 25.0 g and a student collects 17.5 g. Calculate the "
                "percentage yield.",
        "options": [
            "7.5%",
            "143%",
            "70.0%",
            "30.0%",
        ],
        "correct_index": 2,
        "why": "(17.5 ÷ 25.0) × 100 = 70.0%.",
    },
    {
        "id": "ks4-percentage-yield-s06",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction has a theoretical yield of 12.5 g and a percentage "
                "yield of 92%. Calculate the mass of product collected.",
        "options": [
            "13.6 g",
            "1.15 g",
            "11.0 g",
            "11.5 g",
        ],
        "correct_index": 3,
        "why": "12.5 × 92 ÷ 100 = 11.5 g.",
    },
    {
        "id": "ks4-percentage-yield-s07",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "One student collects 4.5 g of a salt against a theoretical "
                "yield of 6.0 g; another collects 7.0 g against a theoretical "
                "yield of 10.0 g. Determine who achieved the higher "
                "percentage yield.",
        "options": [
            "The first student, at 75% against 70%",
            "The second student, at 70% against 45%",
            "The second student, because more product was collected",
            "Neither — both students achieved exactly 70%",
        ],
        "correct_index": 0,
        "why": "4.5 ÷ 6.0 is 75% while 7.0 ÷ 10.0 is 70%, so collecting less "
               "product can still be the better yield.",
    },
    {
        "id": "ks4-percentage-yield-s08",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student washes their crystals with a large volume of cold "
                "water before drying them. Explain the effect on the "
                "percentage yield.",
        "options": [
            "It rises, because the cold water rinses the impurities off the "
            "crystals",
            "It rises, because the damp crystals weigh more on the balance",
            "It falls, because some of the product dissolves in the wash water",
            "It is unchanged, because washing does not alter the chemistry",
        ],
        "correct_index": 2,
        "why": "The salt is soluble, so a large volume of wash water carries "
               "some of the collected product away down the sink.",
    },
    {
        "id": "ks4-percentage-yield-s09",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student weighs their crystals before they are fully dry. "
                "Explain the effect on the calculated percentage yield.",
        "options": [
            "It is too low, because wet crystals stick to the watch glass",
            "It is too high, because the water is weighed as though it were "
            "product",
            "It is unaffected, because the water will evaporate later anyway",
            "It is too low, because the water takes up room that the product "
            "could occupy",
        ],
        "correct_index": 1,
        "why": "The balance cannot tell product from water, so every gram of "
               "water left behind is counted as actual yield.",
    },
    {
        "id": "ks4-percentage-yield-s10",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction runs at a percentage yield of 60% and 18.0 g of "
                "product is needed. Calculate the theoretical yield the "
                "reaction must have.",
        "options": [
            "10.8 g",
            "108 g",
            "30.0 g",
            "36.0 g",
        ],
        "correct_index": 2,
        "why": "18.0 × 100 ÷ 60 = 30.0 g must be possible on paper for 18.0 g "
               "to be collected.",
    },
    {
        "id": "ks4-percentage-yield-s11",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a side reaction lowers the percentage yield of a "
                "preparation.",
        "options": [
            "It uses up reactant to make something other than the product "
            "wanted",
            "It uses up the product, turning it straight back into the "
            "reactants again",
            "It raises the theoretical yield without raising the actual yield",
            "It makes the product harder to dry, so it weighs less afterwards",
        ],
        "correct_index": 0,
        "why": "Reactant diverted into a by-product can no longer form the "
               "wanted product, so less of it is available to collect.",
    },
    {
        "id": "ks4-percentage-yield-s12",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A factory must supply 45 tonnes of a product each day from a "
                "process with a percentage yield of 90%. Calculate the "
                "theoretical yield needed each day.",
        "options": [
            "40.5 tonnes",
            "45.9 tonnes",
            "405 tonnes",
            "50 tonnes",
        ],
        "correct_index": 3,
        "why": "45 × 100 ÷ 90 = 50 tonnes must be possible on paper for "
               "45 tonnes to come out.",
    },
    {
        "id": "ks4-percentage-yield-s13",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A solid that is 80% pure is weighed out, and the "
                "theoretical yield is worked out from its full mass. Determine "
                "the effect on the percentage yield obtained.",
        "options": [
            "It rises, because the impurity adds to the mass of product made",
            "It is unaffected, since the impurity takes no part in the reaction "
            "at all",
            "It falls, because a fifth of the mass weighed out cannot react",
            "It rises, because the theoretical yield has been underestimated",
        ],
        "correct_index": 2,
        "why": "Only 80% of the solid can form product, so the actual yield is "
               "compared against a theoretical yield that was never "
               "reachable.",
    },
    {
        "id": "ks4-percentage-yield-s14",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student's percentage yield comes out at 104%. Suggest the "
                "most likely cause.",
        "options": [
            "The reaction went slightly further than it should have done",
            "The theoretical yield was worked out from too much reactant",
            "The balance was tared with the watch glass still on the pan",
            "The product was weighed before it had been dried properly",
        ],
        "correct_index": 3,
        "why": "A yield above 100% is impossible, so the extra mass is "
               "something other than product — most often water that has not "
               "been driven off.",
    },
    {
        "id": "ks4-percentage-yield-s15",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction can make at most 40 g of product from 50 g of "
                "reactant. A student uses 25 g of reactant and collects 16 g "
                "of product. Calculate the percentage yield.",
        "options": [
            "32%",
            "40%",
            "64%",
            "80%",
        ],
        "correct_index": 3,
        "why": "25 g of reactant could give 20 g of product, so the yield is "
               "(16 ÷ 20) × 100 = 80%.",
    },
    {
        "id": "ks4-percentage-yield-s16",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a percentage yield is worked out from masses "
                "rather than from the number of crystals collected.",
        "options": [
            "Because crystals are difficult to count once they are dry",
            "Because crystals vary in size, so a count says nothing about "
            "quantity",
            "Because a balance is the only piece of apparatus that a school "
            "laboratory has",
            "Because the number of crystals changes as the solution cools "
            "down",
        ],
        "correct_index": 1,
        "why": "Two preparations can give the same mass as a few large "
               "crystals or many small ones, so only mass measures how much "
               "product there is.",
    },
    {
        "id": "ks4-percentage-yield-s17",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student weighs 10.5 g of product against a theoretical "
                "yield of 15.0 g, then finds 1.5 g more of it left on the "
                "filter paper. Determine the percentage yield they would have "
                "had if none had been left behind.",
        "options": [
            "70%",
            "80%",
            "90%",
            "10%",
        ],
        "correct_index": 1,
        "why": "10.5 + 1.5 = 12.0 g of product actually formed, so "
               "(12.0 ÷ 15.0) × 100 = 80%.",
    },
    {
        "id": "ks4-percentage-yield-s18",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine the percentage yield of a preparation in which "
                "13.6 g of product is collected against a theoretical yield "
                "of 16.0 g.",
        "options": [
            "2.4%",
            "118%",
            "15.0%",
            "85%",
        ],
        "correct_index": 3,
        "why": "(13.6 ÷ 16.0) × 100 = 85%.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-percentage-yield-h05",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Magnesium carbonate decomposes on heating, and 84 g of it can "
                "give at most 40 g of magnesium oxide. A student heats 42.0 g "
                "and collects 15.0 g of the oxide. Calculate the percentage "
                "yield.",
        "options": [
            "17.9%",
            "75.0%",
            "37.5%",
            "133%",
        ],
        "correct_index": 1,
        "why": "42.0 g is half of 84 g, so the theoretical yield is 20.0 g, "
               "giving (15.0 ÷ 20.0) × 100 = 75.0%.",
    },
    {
        "id": "ks4-percentage-yield-h06",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two students carry out the same preparation with a "
                "theoretical yield of 36.0 g. One collects 27.0 g and the "
                "other 30.6 g. Determine the difference between their "
                "percentage yields.",
        "options": [
            "3.6 percentage points",
            "10 percentage points",
            "13 percentage points",
            "25 percentage points",
        ],
        "correct_index": 1,
        "why": "27.0 ÷ 36.0 is 75% and 30.6 ÷ 36.0 is 85%, a difference of 10 "
               "percentage points.",
    },
    {
        "id": "ks4-percentage-yield-h07",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An industrial process has a theoretical yield of 500 kg, runs "
                "at a percentage yield of 96%, and its product is 90% pure. "
                "Calculate the mass of pure product obtained.",
        "options": [
            "450 kg",
            "480 kg",
            "432 kg",
            "930 kg",
        ],
        "correct_index": 2,
        "why": "500 × 0.96 = 480 kg is collected, and 90% of that is pure "
               "product: 480 × 0.90 = 432 kg.",
    },
    {
        "id": "ks4-percentage-yield-h08",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A salt can be made by route A, which gives a 95% yield but "
                "needs a costly reagent, or by route B, which gives a 70% "
                "yield from cheap reagents. Evaluate what the yield figures "
                "alone say.",
        "options": [
            "Route B is better, since cheap reagents cost less",
            "Route A wastes less raw material, though cost may still favour B",
            "Route A is better, since a high yield means purity",
            "Neither can be judged, as yields depend on the chemist",
        ],
        "correct_index": 1,
        "why": "Percentage yield only says how much of the possible product is "
               "obtained, so it argues for A while saying nothing about the "
               "price of the reagents.",
    },
    {
        "id": "ks4-percentage-yield-h09",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction is heated for 30 minutes in one run and for 5 "
                "minutes in another, giving percentage yields of 88% and 41%. "
                "Suggest the reason for the difference.",
        "options": [
            "The shorter run was stopped before the reaction had finished",
            "The longer run made a different product from the shorter one",
            "The shorter run lost more product because it was handled twice",
            "The longer run had a larger theoretical yield to work towards",
        ],
        "correct_index": 0,
        "why": "An incomplete reaction leaves reactant unconverted, so far "
               "less of the possible product has been made when the mixture "
               "is worked up.",
    },
    {
        "id": "ks4-percentage-yield-h10",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student collects 14.0 g of crystals against a theoretical "
                "yield of 20.0 g, then discovers the crystals still held "
                "1.4 g of water. Determine the true percentage yield.",
        "options": [
            "70%",
            "77%",
            "63%",
            "80%",
        ],
        "correct_index": 2,
        "why": "Only 14.0 − 1.4 = 12.6 g was product, so the yield is "
               "(12.6 ÷ 20.0) × 100 = 63%.",
    },
    {
        "id": "ks4-percentage-yield-h11",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A preparation with a theoretical yield of 15.0 g gives 13.5 g "
                "of crude product, which falls to 12.0 g once recrystallised. "
                "Determine the difference between the two percentage yields.",
        "options": [
            "1.5 percentage points",
            "10 percentage points",
            "15 percentage points",
            "20 percentage points",
        ],
        "correct_index": 1,
        "why": "13.5 ÷ 15.0 is 90% and 12.0 ÷ 15.0 is 80%, so purifying the "
               "product costs 10 percentage points of yield.",
    },
    {
        "id": "ks4-percentage-yield-h12",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why buying a balance that reads to more decimal "
                "places cannot improve a preparation's percentage yield.",
        "options": [
            "A finer balance reads a smaller mass, which lowers the yield",
            "The loss happens in the chemistry and the handling, not the "
            "weighing",
            "A percentage yield is rounded, so it cannot change",
            "The theoretical yield would rise by the same amount",
        ],
        "correct_index": 1,
        "why": "The yield is set by how much product forms and survives to the "
               "end; a better balance only measures that mass more precisely.",
    },
    {
        "id": "ks4-percentage-yield-h13",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student weighs 9.6 g of solid against a theoretical yield "
                "of 12.0 g, but 0.6 g of the solid is unreacted starting "
                "material. Determine the percentage yield of the product "
                "itself.",
        "options": [
            "80%",
            "85%",
            "75%",
            "5%",
        ],
        "correct_index": 2,
        "why": "Only 9.6 − 0.6 = 9.0 g is product, so the yield is "
               "(9.0 ÷ 12.0) × 100 = 75%.",
    },
    {
        "id": "ks4-percentage-yield-h14",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A manufacturer raises its percentage yield from 72% to 90% "
                "while making the same mass of product. Determine the "
                "percentage reduction in the raw material it must supply.",
        "options": [
            "18%",
            "25%",
            "20%",
            "10%",
        ],
        "correct_index": 2,
        "why": "For 90 tonnes of product the theoretical yield falls from 125 "
               "to 100 tonnes, and 25 ÷ 125 = 20% less raw material.",
    },
    {
        "id": "ks4-percentage-yield-h15",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A preparation reliably gives an 85% yield. It is repeated on "
                "ten times the scale and 42.5 g of product is collected. "
                "Determine the theoretical yield of the large run.",
        "options": [
            "36.1 g",
            "47.5 g",
            "425 g",
            "50.0 g",
        ],
        "correct_index": 3,
        "why": "42.5 × 100 ÷ 85 = 50.0 g, so the large run could at most have "
               "made 50.0 g.",
    },
    {
        "id": "ks4-percentage-yield-h16",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate this statement: 'A reaction with a percentage yield "
                "of 100% wastes nothing.'",
        "options": [
            "Correct, because every gram of reactant has become product",
            "Correct, since a 100% yield means nothing was lost",
            "Wrong, because a high yield always means a high atom economy too",
            "Wrong, because by-products can still be made alongside the "
            "product",
        ],
        "correct_index": 3,
        "why": "Percentage yield only asks how much of the WANTED product was "
               "collected; a reaction can hand over all of it and still make a "
               "waste by-product as well.",
    },
    {
        "id": "ks4-percentage-yield-h17",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The same salt solution is worked up twice: in run 1 it is "
                "evaporated to dryness, and in run 2 it is cooled to "
                "crystallise and the crystals are filtered off. Determine "
                "which run gives the greater mass of solid.",
        "options": [
            "Run 1, because nothing is left behind in the solution",
            "Run 2, because crystals are denser than dried solid",
            "Run 1, because heating the solution makes more salt form",
            "Run 2, because filtering removes the water more thoroughly",
        ],
        "correct_index": 0,
        "why": "Evaporating to dryness leaves every dissolved solid in the "
               "dish, while filtering leaves some salt behind in the solution "
               "that drains away — though the dried solid is less pure.",
    },
    {
        "id": "ks4-percentage-yield-h18",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction makes at most 0.50 g of product per gram of "
                "reactant and runs at a percentage yield of 78%. Determine "
                "the mass of reactant needed to obtain 39.0 g of product.",
        "options": [
            "78 g",
            "50 g",
            "100 g",
            "156 g",
        ],
        "correct_index": 2,
        "why": "39.0 × 100 ÷ 78 = 50.0 g must be possible on paper, and at "
               "0.50 g per gram that needs 50.0 ÷ 0.50 = 100 g of reactant.",
    },

    # ── standard (top-up) ──────────────────────────────────────────────────
    {
        "id": "ks4-percentage-yield-s19",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two reactants are mixed in unequal amounts, and one of them "
                "runs out first. State which reactant's mass is used to "
                "calculate the theoretical yield.",
        "options": [
            "Whichever reactant was measured out to the greater mass at the start",
            "Whichever reactant happens to be the cheaper of the two to buy in bulk",
            "The reactant that runs out first and limits how much product "
            "can form",
            "Both reactants added together, taken as one single combined mass",
        ],
        "correct_index": 2,
        "why": "Once the limiting reactant is used up the reaction stops, so "
               "the maximum possible product is fixed by that reactant "
               "alone.",
    },
    {
        "id": "ks4-percentage-yield-s20",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A preparation of aspirin has a theoretical yield of 5.20 g, "
                "and a student collects 4.16 g. Calculate the percentage "
                "yield.",
        "options": [
            "12.5%",
            "80.0%",
            "9.36%",
            "125%",
        ],
        "correct_index": 1,
        "why": "(4.16 ÷ 5.20) × 100 = 80.0%.",
    },
    {
        "id": "ks4-percentage-yield-s21",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ethanoic acid reacts with ethanol to form an ester in a "
                "reversible reaction. Explain why the percentage yield of "
                "ester is below 100% even with a very careful technique.",
        "options": [
            "Some of the ester breaks back down into ethanoic acid and "
            "ethanol as fast as it forms",
            "The ester evaporates away entirely before it can ever be "
            "weighed on the balance",
            "Ethanol reacts with the glassware itself instead of with the "
            "ethanoic acid present",
            "The ethanoic acid used does not dissolve completely in the "
            "ethanol it is mixed with",
        ],
        "correct_index": 0,
        "why": "Because the reaction can run in both directions, some ester "
               "is always breaking down again, so the reaction never reaches "
               "completion.",
    },
    {
        "id": "ks4-percentage-yield-s22",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "60 g of a reactant can make at most 45 g of product. "
                "Calculate the theoretical yield possible from 24 g of the "
                "same reactant.",
        "options": [
            "15 g",
            "18 g",
            "32 g",
            "36 g",
        ],
        "correct_index": 1,
        "why": "24 g is 24/60 of the original amount, and 24/60 × 45 = 18 g.",
    },
    {
        "id": "ks4-percentage-yield-s23",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A reaction typically gives three quarters of its maximum "
                "possible product. Its theoretical yield from a given amount "
                "of reactant is 32 g. Calculate the mass of product expected.",
        "options": [
            "8.0 g",
            "24 g",
            "42.7 g",
            "28 g",
        ],
        "correct_index": 1,
        "why": "Three quarters is a percentage yield of 75%, and 75% of 32 g "
               "is 24 g.",
    },
    {
        "id": "ks4-percentage-yield-s24",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student weighs 12.5 g and 15.0 g, each to three significant "
                "figures, and calculates a percentage yield of 83.33%. "
                "Identify the value that should be reported.",
        "options": [
            "83%",
            "83.3%",
            "83.33%",
            "80%",
        ],
        "correct_index": 1,
        "why": "The answer cannot be more precise than the data it comes "
               "from, so a result from three-significant-figure masses is "
               "reported to three significant figures: 83.3%.",
    },
    {
        "id": "ks4-percentage-yield-s25",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student collects 15.0 g of solid from a reaction, but 3.0 g "
                "of it is an insoluble by-product mixed in with the wanted "
                "crystals. The theoretical yield of the crystals is 15.0 g. "
                "Calculate the percentage yield of the crystals alone.",
        "options": [
            "100%",
            "80%",
            "20%",
            "120%",
        ],
        "correct_index": 1,
        "why": "Only 15.0 − 3.0 = 12.0 g is the wanted crystals, so the yield "
               "is (12.0 ÷ 15.0) × 100 = 80%.",
    },
    {
        "id": "ks4-percentage-yield-s26",
        "subtopic_slug": "percentage-yield",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student calculates actual yield divided by theoretical "
                "yield as 0.85 and writes the percentage yield as '0.85%'. "
                "Identify the mistake.",
        "options": [
            "The fraction should have been inverted before it was reported",
            "The fraction should have been multiplied by 100 to give 85%",
            "The fraction should have been subtracted from 1 to give 0.15%",
            "There is no mistake, since 0.85% is a correct way to write it",
        ],
        "correct_index": 1,
        "why": "A percentage is the fraction multiplied by 100, so 0.85 "
               "becomes 85%, not 0.85%.",
    },

    # ── harder (top-up) ─────────────────────────────────────────────────────
    {
        "id": "ks4-percentage-yield-h19",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A product is made in two steps: the first step gives a 90% "
                "yield and the second step, carried out on the product of the "
                "first, gives an 85% yield. Calculate the overall percentage "
                "yield of the two-step route.",
        "options": [
            "87.5%",
            "76.5%",
            "175%",
            "90%",
        ],
        "correct_index": 1,
        "why": "The two yields multiply rather than average: 0.90 × 0.85 = "
               "0.765, which is 76.5%.",
    },
    {
        "id": "ks4-percentage-yield-h20",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A two-step synthesis has an overall percentage yield of 72%. "
                "The first step alone has a percentage yield of 90%. "
                "Determine the percentage yield of the second step.",
        "options": [
            "18%",
            "80%",
            "62%",
            "65%",
        ],
        "correct_index": 1,
        "why": "The two yields multiply to give the overall yield, so the "
               "second step is 72 ÷ 90 × 100 = 80%.",
    },
    {
        "id": "ks4-percentage-yield-h21",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Reactant P and reactant Q react in the mass ratio 2 : 3 with "
                "nothing left over, to give product R with no waste product "
                "formed. A student mixes 40 g of P with 90 g of Q. Determine "
                "the theoretical yield of R.",
        "options": [
            "60 g",
            "100 g",
            "130 g",
            "90 g",
        ],
        "correct_index": 1,
        "why": "40 g of P needs 60 g of Q, so Q (90 g) is in excess and P is "
               "the limiting reactant; the theoretical yield is 40 + 60 = "
               "100 g, since none of the mass is lost as waste.",
    },
    {
        "id": "ks4-percentage-yield-h22",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student weighs 12.5 g and a second mass of 8.0 g, "
                "measured only to two significant figures, and calculates a "
                "percentage yield of 65.625%. Determine the value that "
                "should be reported.",
        "options": [
            "65.625%",
            "65.6%",
            "66%",
            "65%",
        ],
        "correct_index": 2,
        "why": "The result cannot be more precise than the least precise "
               "measurement used, which has two significant figures, so the "
               "answer is rounded to 66%.",
    },
    {
        "id": "ks4-percentage-yield-h23",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A carbonate is heated and decomposes, releasing carbon "
                "dioxide gas that escapes into the air, leaving a solid "
                "product behind. Explain why the mass of solid remaining "
                "cannot be compared directly with the starting mass to find a "
                "percentage yield.",
        "options": [
            "A percentage yield always compares the actual mass with a "
            "theoretical yield calculated from the balanced equation, not "
            "with the starting mass",
            "A percentage yield cannot be found for a reaction whose "
            "products include a gas rather than a solid or a liquid alone",
            "The carbon dioxide given off has to be captured and weighed "
            "separately before a yield calculation of this kind becomes "
            "possible for the chemist to carry out",
            "The starting mass weighed out is generally smaller than the "
            "mass of solid product left behind once the heating is "
            "complete and the flask has cooled",
        ],
        "correct_index": 0,
        "why": "The theoretical yield is the maximum mass the equation "
               "predicts for the solid product, not the mass that was "
               "weighed out to begin with.",
    },
    {
        "id": "ks4-percentage-yield-h24",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A precipitation reaction is carried out with one reactant in "
                "slight excess, and the calculated percentage yield comes out "
                "at 108%. Suggest the most likely cause.",
        "options": [
            "Some of the unreacted excess reactant has precipitated out "
            "along with the product and been weighed as part of it",
            "The reaction ran further towards completion than the balanced "
            "chemical equation itself would normally seem to allow for",
            "The theoretical yield was calculated using too little of the "
            "reactant that limits the reaction",
            "The student's balance was reading exactly 8% too low for the "
            "whole of the weighing session",
        ],
        "correct_index": 0,
        "why": "A yield above 100% is impossible for the product alone, so "
               "the extra mass most likely comes from unreacted excess "
               "reactant carried down with the precipitate.",
    },
    {
        "id": "ks4-percentage-yield-h25",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student obtains a percentage yield of 95% but has not "
                "tested the purity of the crystals collected. Explain what "
                "the 95% figure alone does not tell them.",
        "options": [
            "Whether the crystals collected are the pure product or contain "
            "other substances mixed in",
            "How many grams of crystals were collected by the student at the very end of the preparation",
            "What the theoretical yield of the reaction had been calculated to be before the run began",
            "Whether the reaction that was carried out happens to be a reversible one or not",
        ],
        "correct_index": 0,
        "why": "Percentage yield measures how much mass was collected "
               "against the maximum possible, and says nothing about whether "
               "that mass is pure product or includes impurities.",
    },
    {
        "id": "ks4-percentage-yield-h26",
        "subtopic_slug": "percentage-yield",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Route 1 makes a product in a single step with a 65% yield. "
                "Route 2 makes the same product in two steps, each with a "
                "90% yield. Determine which route gives the greater overall "
                "yield from the same starting mass of reactant.",
        "options": [
            "Route 1, since a single-step route generally beats a two-step "
            "route of this kind",
            "Route 2, since adding 90% and 90% gives an overall yield of "
            "180% for the route",
            "The two routes are equal, since both of them start from the "
            "same reactant",
            "Route 2, since 0.90 × 0.90 gives an overall yield of 81%, "
            "higher than Route 1's 65%",
        ],
        "correct_index": 3,
        "why": "Multiplying the two step yields gives 81%, which beats "
               "Route 1's single 65% even though Route 2 takes an extra "
               "step.",
    },
]
