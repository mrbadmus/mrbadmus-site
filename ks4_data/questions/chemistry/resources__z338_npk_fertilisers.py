"""Chemistry · Using resources — the MRB-338 expansion for `npk-fertilisers`.

The shipped rows already name the sulfuric acid route, the 20:10:10 label and
the algal bloom, so the weight here falls on the chemistry that sits under them:
ammonia as the base that every nitrogen salt is neutralised from, the nitric and
phosphoric acid routes, why a fertiliser compound has to be soluble at all, and
what each of the three nutrients is actually used for inside the plant.

Round that sits the environmental strand the spec asks to be evaluated rather
than recited — the oxygen, not the algae, being what kills the fish; nitrate in
groundwater and the limit set on it; slow release, spring application and
precision dosing against manure. Seven rows carry arithmetic: percentage by
mass of nitrogen and of phosphorus, bag-label percentages, a dose per hectare
and two mass-from-equation calculations.
"""

TOPIC = "resources"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": "ks4-npk-fertilisers-e05",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Nitric acid is neutralised by ammonia. Name the fertiliser "
                "salt that forms.",
        "options": [
            "Ammonium nitrate",
            "Ammonium sulfate",
            "Sodium nitrate",
            "Calcium nitrate",
        ],
        "correct_index": 0,
        "why": "An acid neutralised by ammonia gives the ammonium salt of "
               "that acid, so nitric acid gives ammonium nitrate.",
    },
    {
        "id": "ks4-npk-fertilisers-e06",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which element in an NPK fertiliser is needed so that a "
                "plant's enzymes work properly?",
        "options": [
            "Nitrogen",
            "Potassium",
            "Phosphorus",
            "Magnesium",
        ],
        "correct_index": 1,
        "why": "Potassium is required for enzyme function and for "
               "photosynthesis, which is why a shortage of it shows up in "
               "poor growth.",
    },
    {
        "id": "ks4-npk-fertilisers-e07",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Plants need one of the three NPK nutrients mainly for making "
                "proteins. Which is it?",
        "options": [
            "Potassium",
            "Phosphorus",
            "Nitrogen",
            "Sodium",
        ],
        "correct_index": 2,
        "why": "Proteins contain nitrogen, so a plant building new protein "
               "needs a supply of nitrogen compounds from the soil.",
    },
    {
        "id": "ks4-npk-fertilisers-e08",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the salt made when ammonia reacts with phosphoric acid.",
        "options": [
            "Ammonium sulfate",
            "Potassium phosphate",
            "Calcium phosphate",
            "Ammonium phosphate",
        ],
        "correct_index": 3,
        "why": "Ammonia supplies the ammonium ion and phosphoric acid the "
               "phosphate ion, so the salt is ammonium phosphate.",
    },
    {
        "id": "ks4-npk-fertilisers-e09",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ammonia dissolves in water. What sort of solution does it "
                "make?",
        "options": [
            "A strongly acidic solution",
            "An alkaline solution",
            "A neutral solution",
            "A solution that is a bleach",
        ],
        "correct_index": 1,
        "why": "Ammonia solution is alkaline, which is why it neutralises an "
               "acid to give an ammonium salt.",
    },
    {
        "id": "ks4-npk-fertilisers-e10",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "What type of reaction takes place when ammonia reacts with "
                "an acid to make a fertiliser salt?",
        "options": [
            "Neutralisation",
            "Combustion",
            "Electrolysis",
            "Thermal decomposition",
        ],
        "correct_index": 0,
        "why": "An alkali reacting with an acid to give a salt and nothing "
               "else is a neutralisation.",
    },
    {
        "id": "ks4-npk-fertilisers-e11",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which industrial process supplies the ammonia that "
                "fertiliser factories use?",
        "options": [
            "The contact process",
            "The Haber process",
            "Fractional distillation",
            "The blast furnace",
        ],
        "correct_index": 1,
        "why": "The Haber process makes ammonia from nitrogen and hydrogen, "
               "and fertiliser manufacture is where most of it goes.",
    },
    {
        "id": "ks4-npk-fertilisers-e12",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give the reason why a farmer adds fertiliser to a field each "
                "year.",
        "options": [
            "To kill the weeds that grow between the crop rows",
            "To replace the minerals that the last crop took out",
            "To lower the pH of the soil before the seed for the crop is sown",
            "To hold water in the soil during a dry summer",
        ],
        "correct_index": 1,
        "why": "Harvesting removes the mineral ions the crop took up, so "
               "without replacement the soil is depleted and yields fall.",
    },
    {
        "id": "ks4-npk-fertilisers-e13",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which property must a fertiliser compound have so that roots "
                "can take it up?",
        "options": [
            "It has to be a gas at room temperature",
            "It must be dense enough to sink in soil",
            "It must dissolve in the water in the soil",
            "It must be coloured so it can be seen",
        ],
        "correct_index": 2,
        "why": "Roots take up mineral ions in solution, so a compound that "
               "does not dissolve is of no use to the plant.",
    },
    {
        "id": "ks4-npk-fertilisers-e14",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the acid that is manufactured from phosphate rock and "
                "then used in fertilisers.",
        "options": [
            "Nitric acid",
            "Hydrochloric acid",
            "Ethanoic acid",
            "Phosphoric acid",
        ],
        "correct_index": 3,
        "why": "Phosphate rock treated with sulfuric acid gives phosphoric "
               "acid, which is then neutralised to make phosphate "
               "fertilisers.",
    },
    {
        "id": "ks4-npk-fertilisers-e15",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Fish die in a pond after fertiliser has washed into it. What "
                "kills them?",
        "options": [
            "The water runs out of dissolved oxygen",
            "The fertiliser poisons them on contact",
            "The water becomes too warm for them",
            "The algae eat the fish eggs in the pond",
        ],
        "correct_index": 0,
        "why": "Bacteria decomposing the dead algae use up the dissolved "
               "oxygen, and the fish suffocate.",
    },
    {
        "id": "ks4-npk-fertilisers-e16",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one way a farmer can cut the amount of fertiliser that "
                "is wasted.",
        "options": [
            "Spread twice as much so some is left over",
            "Spread only as much as the crop actually needs",
            "Spread it in the middle of a heavy rain shower",
            "Spread it on the field paths instead of onto the crop rows",
        ],
        "correct_index": 1,
        "why": "Matching the dose to what the crop will take up is the "
               "central idea of precision farming and leaves little behind to "
               "be washed away.",
    },
    {
        "id": "ks4-npk-fertilisers-e17",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the name given to the washing of soluble fertiliser "
                "out of the soil by rain.",
        "options": [
            "Filtration",
            "Leaching",
            "Evaporation",
            "Condensation",
        ],
        "correct_index": 1,
        "why": "Leaching is the movement of dissolved substances out of the "
               "soil with water draining through it.",
    },
    {
        "id": "ks4-npk-fertilisers-e18",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which compound is the starting material for every nitrogen "
                "salt in an NPK fertiliser?",
        "options": [
            "Nitric acid",
            "Calcium carbonate",
            "Sodium hydroxide",
            "Ammonia",
        ],
        "correct_index": 3,
        "why": "Every ammonium salt in the blend is made by neutralising an "
               "acid with ammonia.",
    },
    # -------------------------------------------------------------- standard
    {
        "id": "ks4-npk-fertilisers-s05",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why ammonia is described as a base in fertiliser "
                "manufacture.",
        "options": [
            "It burns in air to give a salt and water as products",
            "It dissolves metals to give a salt and hydrogen gas",
            "It neutralises an acid to give a salt and nothing else",
            "It gives away hydrogen ions to whichever acid it is mixed with",
        ],
        "correct_index": 2,
        "why": "A base is a substance that neutralises an acid to form a "
               "salt, which is exactly what ammonia does in every fertiliser "
               "route.",
    },
    {
        "id": "ks4-npk-fertilisers-s06",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why plants rooted on the bed of a river die when a "
                "thick layer of algae grows on the surface.",
        "options": [
            "The algae block the light the plants need",
            "The algae take the fertiliser from the plants",
            "The algae release a poison into the water",
            "The algae raise the pH of the river sharply",
        ],
        "correct_index": 0,
        "why": "A dense surface bloom shades everything below it, so the "
               "rooted plants cannot photosynthesise and die.",
    },
    {
        "id": "ks4-npk-fertilisers-s07",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why water companies measure the nitrate "
                "concentration of the water they supply.",
        "options": [
            "Nitrate above the legal limit is a health risk",
            "Nitrate makes the water taste strongly of metal",
            "Nitrate stops chlorine killing bacteria in the water",
            "Nitrate turns the water a deep blue-green colour",
        ],
        "correct_index": 0,
        "why": "There is a legal maximum for nitrate in drinking water "
               "because high concentrations are harmful, particularly to "
               "infants.",
    },
    {
        "id": "ks4-npk-fertilisers-s08",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how coating fertiliser granules so that they "
                "dissolve slowly reduces pollution.",
        "options": [
            "The nutrient is released as the crop takes it up",
            "The coating reacts with the nitrate in the soil to make nitrogen "
            "gas",
            "The coating stops rain reaching the soil underneath",
            "The nutrient is released all at once after harvest",
        ],
        "correct_index": 0,
        "why": "Slow release keeps the concentration in the soil water low, "
               "so far less is available to be carried away before the crop "
               "uses it.",
    },
    {
        "id": "ks4-npk-fertilisers-s09",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the percentage by mass of nitrogen in ammonium "
                "nitrate. Relative formula mass of NH4NO3 = 80; relative "
                "atomic mass of N = 14.",
        "options": [
            "17.5%",
            "35%",
            "28%",
            "57%",
        ],
        "correct_index": 1,
        "why": "There are two nitrogen atoms, giving 28 out of 80, and "
               "28 / 80 x 100 = 35%.",
    },
    {
        "id": "ks4-npk-fertilisers-s10",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A crop needs 60 kg of nitrogen per hectare. The fertiliser "
                "available is 30% nitrogen by mass. Calculate the mass of "
                "fertiliser needed per hectare.",
        "options": [
            "18 kg",
            "90 kg",
            "200 kg",
            "2 kg",
        ],
        "correct_index": 2,
        "why": "The fertiliser mass needed is 60 / 0.30 = 200 kg, of which "
               "60 kg is nitrogen.",
    },
    {
        "id": "ks4-npk-fertilisers-s11",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest one advantage of spreading animal manure instead of "
                "a manufactured fertiliser.",
        "options": [
            "It supplies a far higher nitrogen content per tonne",
            "It releases nutrients slowly and adds organic matter",
            "It can be spread in a much thinner layer on the soil",
            "It contains no phosphorus, so no river nearby can be polluted by "
            "it",
        ],
        "correct_index": 1,
        "why": "Manure breaks down gradually, so nutrients are released over "
               "time, and the organic matter left behind improves the "
               "structure of the soil.",
    },
    {
        "id": "ks4-npk-fertilisers-s12",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A 25 kg bag of fertiliser is labelled 20:10:10, meaning 20% "
                "of its mass is nitrogen. Calculate the mass of nitrogen in "
                "the bag.",
        "options": [
            "2.0 kg",
            "2.5 kg",
            "5.0 kg",
            "20 kg",
        ],
        "correct_index": 2,
        "why": "20% of 25 kg is 0.20 x 25 = 5.0 kg of nitrogen.",
    },
    {
        "id": "ks4-npk-fertilisers-s13",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A school makes a few grams of an ammonium salt by titration. "
                "Suggest why a factory does not use the same method.",
        "options": [
            "A titration gives a salt that plants cannot take up",
            "A titration cannot be done with ammonia solution at all",
            "A factory needs thousands of tonnes, so it runs continuously",
            "A factory is not allowed to use acids on that scale",
        ],
        "correct_index": 2,
        "why": "Batch titration is accurate but tiny; industrial output "
               "demands a continuous process feeding acid and ammonia in "
               "together all day.",
    },
    {
        "id": "ks4-npk-fertilisers-s14",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a farmer spreads fertiliser in spring rather "
                "than in late autumn.",
        "options": [
            "The growing crop takes it up before rain removes it",
            "Fertiliser will not dissolve in cold winter soil water",
            "Autumn soil already holds all of the nitrate that a crop needs",
            "Spreading in autumn would burn the leaves of the crop",
        ],
        "correct_index": 0,
        "why": "Applied in spring the nutrients are used by an actively "
               "growing crop, while autumn application leaves them in the "
               "soil through months of winter rain.",
    },
    {
        "id": "ks4-npk-fertilisers-s15",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why repeated use of an ammonium fertiliser can make "
                "a soil more acidic.",
        "options": [
            "The ammonium ion is oxidised in soil, releasing H+ ions",
            "The ammonium ion dissolves the limestone in the subsoil",
            "The ammonium ion turns straight into hydrochloric acid",
            "The ammonium ion removes every hydroxide ion from the soil water",
        ],
        "correct_index": 0,
        "why": "Soil bacteria oxidise ammonium to nitrate, and that process "
               "releases hydrogen ions, which lowers the pH over time.",
    },
    {
        "id": "ks4-npk-fertilisers-s16",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fertiliser supplies three nutrients rather "
                "than just the one a crop needs most.",
        "options": [
            "Three nutrients dissolve faster than one on its own",
            "Each does a different job, so a shortage of any one limits "
            "growth",
            "Three nutrients react together in the soil to make a fourth",
            "Each one cancels out the harm the other two would do",
        ],
        "correct_index": 1,
        "why": "Growth is held back by whichever nutrient runs out first, so "
               "supplying only one leaves the crop limited by another.",
    },
    {
        "id": "ks4-npk-fertilisers-s17",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the maximum mass of ammonium sulfate that could be "
                "made from 34 tonnes of ammonia. Relative formula masses: "
                "NH3 = 17, (NH4)2SO4 = 132.",
        "options": [
            "66 tonnes",
            "132 tonnes",
            "264 tonnes",
            "17 tonnes",
        ],
        "correct_index": 1,
        "why": "Two moles of ammonia give one of ammonium sulfate, so 2 x 17 "
               "= 34 tonnes of ammonia gives 132 tonnes of the salt.",
    },
    {
        "id": "ks4-npk-fertilisers-s18",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a fertiliser company makes its own sulfuric acid "
                "on the same site.",
        "options": [
            "Sulfuric acid cannot be carried by road in any tanker",
            "Sulfuric acid is needed for two of the routes on that site",
            "Sulfuric acid would evaporate away during a long journey",
            "Sulfuric acid is a waste product of the ammonia reactor",
        ],
        "correct_index": 1,
        "why": "Sulfuric acid is used both to treat phosphate rock and to "
               "make ammonium sulfate, so producing it on site feeds two "
               "processes at once.",
    },
    # ---------------------------------------------------------------- harder
    {
        "id": "ks4-npk-fertilisers-h05",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine whether a fertiliser spill into a still pond does "
                "more harm in July or in January, and explain why.",
        "options": [
            "More harm in July, because warmth and light let the algae grow "
            "much faster",
            "More harm in January, because cold water is able to hold far "
            "less oxygen",
            "The same in both, because the algae take up the nutrients at a "
            "fixed rate",
            "No harm in either, because the pond dilutes the nutrients beyond "
            "any effect",
        ],
        "correct_index": 0,
        "why": "Algae need warmth and light to multiply, so a summer spill "
               "builds a far larger bloom; cold water holds more dissolved "
               "oxygen rather than less.",
    },
    {
        "id": "ks4-npk-fertilisers-h06",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate replacing manufactured NPK fertiliser with manure "
                "across a large arable farm.",
        "options": [
            "Better soil and less run-off, but its nutrient content varies",
            "Better in every way, because manure cannot pollute a river",
            "Worse in every way, because manure holds no useful nutrients",
            "Worse soil but higher yields, because manure acts a great deal "
            "faster",
        ],
        "correct_index": 0,
        "why": "Manure adds organic matter and releases nutrients slowly, but "
               "the amount of each nutrient is unpredictable and huge "
               "quantities are needed for the same effect.",
    },
    {
        "id": "ks4-npk-fertilisers-h07",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer applies 250 kg per hectare of a fertiliser that is "
                "12% phosphorus by mass. Calculate the mass of phosphorus "
                "applied per hectare.",
        "options": [
            "12 kg",
            "21 kg",
            "30 kg",
            "3 kg",
        ],
        "correct_index": 2,
        "why": "12% of 250 kg is 0.12 x 250 = 30 kg of phosphorus.",
    },
    {
        "id": "ks4-npk-fertilisers-h08",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Nitrate ions are very soluble while phosphate ions bind "
                "tightly to soil particles. Predict which reaches a river "
                "more readily, and explain.",
        "options": [
            "Phosphate, because it is heavier and sinks through the soil",
            "Nitrate, because water carries dissolved ions through the soil",
            "Phosphate, because it dissolves faster than nitrate does",
            "Nitrate, because it evaporates and falls again as rainfall",
        ],
        "correct_index": 1,
        "why": "An ion that stays in solution travels with the water moving "
               "through the soil, while one held on the surfaces of soil "
               "particles is left behind.",
    },
    {
        "id": "ks4-npk-fertilisers-h09",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A grower doubles the amount of nitrogen fertiliser applied "
                "but the yield does not rise. Suggest an explanation.",
        "options": [
            "Nitrogen fertiliser stops working once it is doubled",
            "The crop cannot take up any fertiliser that is applied twice "
            "over",
            "Another nutrient is now the one holding growth back",
            "The extra nitrogen turns the first dose back into ammonia",
        ],
        "correct_index": 2,
        "why": "Growth is set by whichever requirement is in shortest supply, "
               "so once nitrogen is plentiful adding more cannot help until "
               "the next shortage is met.",
    },
    {
        "id": "ks4-npk-fertilisers-h10",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A works has an order for 400 tonnes of ammonium nitrate. "
                "Work out the mass of ammonia it must start with. Relative "
                "formula masses: NH3 = 17, NH4NO3 = 80.",
        "options": [
            "34 tonnes",
            "42.5 tonnes",
            "85 tonnes",
            "170 tonnes",
        ],
        "correct_index": 2,
        "why": "400 tonnes is five lots of 80, and each lot comes from one "
               "lot of 17, so 5 x 17 = 85 tonnes of ammonia is needed.",
    },
    {
        "id": "ks4-npk-fertilisers-h11",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Nitrate in a village well is still rising twenty years after "
                "the farm above it changed its practices. Suggest why.",
        "options": [
            "Nitrate in the well is being made by bacteria in the pipes",
            "Nitrate takes twenty years to dissolve in cold groundwater",
            "Nitrate applied long ago moves through rock very slowly",
            "Nitrate levels are measured differently now than they were",
        ],
        "correct_index": 2,
        "why": "Water moves through rock at metres per year, so nitrate that "
               "leached decades ago is only now arriving at the depth the "
               "well draws from.",
    },
    {
        "id": "ks4-npk-fertilisers-h12",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that banning all manufactured fertiliser "
                "would be good for the environment.",
        "options": [
            "Correct, because crops grow just as well without fertiliser",
            "Correct, because no farm would then need any land",
            "Mixed, because rivers would recover but far more land "
            "would have to be farmed",
            "Wrong, because fertiliser has no effect on rivers in the "
            "first place",
        ],
        "correct_index": 2,
        "why": "Cutting the nutrient load would help waterways, but yields "
               "would fall sharply and feeding the same population would "
               "mean clearing more habitat.",
    },
    {
        "id": "ks4-npk-fertilisers-h13",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A field has grown a crop every year for five years. Explain "
                "which is the better choice for it, a 15:15:15 fertiliser or "
                "a 30:0:0 one.",
        "options": [
            "30:0:0, because it supplies twice as much of the useful part",
            "15:15:15, because five harvests have removed all three nutrients",
            "30:0:0, because the other two nutrients are never removed",
            "15:15:15, because a lower number always means less pollution",
        ],
        "correct_index": 1,
        "why": "Every harvest takes nitrogen, phosphorus and potassium off "
               "the field, so after five years all three need replacing, not "
               "nitrogen alone.",
    },
    {
        "id": "ks4-npk-fertilisers-h14",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Sulfuric acid is used to treat phosphate rock, yet no "
                "sulfuric acid is found in the fertiliser. Explain why.",
        "options": [
            "It evaporates away completely during the treatment",
            "It is filtered out again once the treatment is finished",
            "It reacts, and its sulfate ends up in the products",
            "It decomposes into sulfur dioxide as the mixture warms",
        ],
        "correct_index": 2,
        "why": "The acid is a reactant: its hydrogen ions go to the phosphate "
               "and its sulfate ions end up in calcium sulfate, so none of "
               "the acid itself remains.",
    },
    {
        "id": "ks4-npk-fertilisers-h15",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ammonium sulfate is 21% nitrogen by mass. Calculate the mass "
                "of nitrogen a grower spreads if eight 50 kg bags are used.",
        "options": [
            "10.5 kg",
            "42 kg",
            "84 kg",
            "168 kg",
        ],
        "correct_index": 2,
        "why": "Eight bags is 400 kg, and 21% of 400 kg is 0.21 x 400 = 84 "
               "kg of nitrogen.",
    },
    {
        "id": "ks4-npk-fertilisers-h16",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why spreading fertiliser onto frozen ground is poor "
                "practice.",
        "options": [
            "It cannot soak in, so meltwater carries it off the surface",
            "It reacts with the ice to give ammonia gas straight away",
            "It freezes solid and can never dissolve again afterwards",
            "It makes the ground thaw sooner than the crop can handle",
        ],
        "correct_index": 0,
        "why": "Frozen soil takes in no water, so the granules sit on top "
               "until the thaw washes them into ditches rather than into the "
               "root zone.",
    },
    {
        "id": "ks4-npk-fertilisers-h17",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a usable fertiliser cannot be made simply by "
                "stirring ammonia, phosphate rock and potassium chloride "
                "together.",
        "options": [
            "Ammonia is a gas and the rock will not dissolve in water",
            "Potassium chloride reacts violently with the ammonia when they "
            "mix",
            "The three would react together to give an unusable gas",
            "Ammonia is an acid, so it cannot be mixed with a rock",
        ],
        "correct_index": 0,
        "why": "Ammonia has to be neutralised into a solid salt and the "
               "phosphate rock has to be made soluble with acid, so both need "
               "a reaction before blending.",
    },
    {
        "id": "ks4-npk-fertilisers-h18",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The legal limit for nitrate in drinking water is set with "
                "infants in mind rather than adults. Suggest why.",
        "options": [
            "Infants drink far more water each day than an adult does",
            "Infants are more affected because nitrate lowers oxygen "
            "carriage in the blood",
            "Infants cannot taste nitrate, so they would not notice it "
            "in the water",
            "Infants are given water that is not treated with chlorine",
        ],
        "correct_index": 1,
        "why": "In an infant, nitrate taken in with water interferes with the "
               "blood's ability to carry oxygen, so the safe concentration is "
               "set by their tolerance and not an adult's.",
    },
]
