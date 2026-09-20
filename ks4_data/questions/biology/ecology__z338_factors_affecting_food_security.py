"""Biology · Ecology — the MRB-338 expansion, food security (4.7.5.1).

Triple-only content. The spec point lists threats and solutions, so the rows
are organised around the biotic / abiotic split the lesson draws and then the
three things the existing rows barely touch: the cost of agricultural inputs,
conflict, and the sustainability of a diet. The harder band puts numbers on a
shortfall — a percentage of need, a fall in food per person as a population
grows, the net gain from a variety that yields more but demands more — and
weighs two policies against each other.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-factors-affecting-food-security-e05",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one biotic factor that threatens food security.",
        "options": [
            "A new crop pathogen arriving in the country",
            "A fall in the average annual rainfall",
            "A rise in the mean summer temperature over several decades",
            "A rise in the price of diesel for farm tractors",
        ],
        "correct_index": 0,
        "why": "Biotic means living, and a pathogen is a living organism; "
               "rainfall, temperature and price are not.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e06",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of factor that a change in rainfall pattern is an "
                "example of.",
        "options": [
            "A biotic factor",
            "An abiotic factor",
            "A political factor",
            "An economic factor",
        ],
        "correct_index": 1,
        "why": "Rainfall is a non-living feature of the environment, so a change "
               "in it is an abiotic factor.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e07",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of pathogen that causes foot-and-mouth disease in "
                "cattle.",
        "options": [
            "A fungus",
            "A parasitic worm",
            "A virus",
            "A protist",
        ],
        "correct_index": 2,
        "why": "Foot-and-mouth is a viral disease of cattle, sheep and pigs, and "
               "an outbreak can destroy a national livestock herd.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e08",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason why changing diets in wealthier countries "
                "threaten global food security.",
        "options": [
            "More food is eaten raw, so more of it has to be imported fresh",
            "More meals are eaten away from home, which moves food off the farms",
            "More food is eaten during the winter, when fewer crops are harvested",
            "More meat and dairy are eaten, which use far more land and grain",
        ],
        "correct_index": 3,
        "why": "Animal products need several times the land, water and grain per "
               "kilogram, so the same farmland feeds fewer people.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e09",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why the cost of fertiliser affects a country's food "
                "security.",
        "options": [
            "Fertiliser has to be bought before a farmer is allowed to sell a crop",
            "Farmers who cannot afford it grow a smaller crop per hectare",
            "Expensive fertiliser is weaker, so it has to be applied far more often",
            "Fertiliser makes up most of the mass of the harvested grain",
        ],
        "correct_index": 1,
        "why": "Fertiliser supplies the mineral ions a crop needs, so a farmer "
               "priced out of it harvests less from the same land.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e10",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why war in a farming region reduces food security.",
        "options": [
            "Soldiers eat more food per person each day than farmers do",
            "War raises the temperature of the region, so the crops fail",
            "Farming and food transport are both disrupted, so less food reaches people",
            "Crops cannot be planted in a war because seed becomes sterile",
        ],
        "correct_index": 2,
        "why": "Conflict stops people planting, harvesting and moving food, so "
               "supply collapses even where the land itself is undamaged.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e11",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how better irrigation raises food production in a dry "
                "region.",
        "options": [
            "Water supplies the mineral ions the crop needs for making protein",
            "Wet soil stops insect pests reaching the roots of the growing crop",
            "Crops receive the water they need for photosynthesis and growth",
            "Water cools the crop, which slows respiration and saves biomass",
        ],
        "correct_index": 2,
        "why": "Water is a raw material for photosynthesis and carries mineral "
               "ions through the plant, so a dry crop cannot build biomass.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e12",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a high-yield crop variety.",
        "options": [
            "A variety that can be harvested in any month of the whole year",
            "A variety that needs no fertiliser or pesticide applied to it",
            "A variety whose seeds are larger than those of any other kind",
            "A variety that produces more food from each hectare of land",
        ],
        "correct_index": 3,
        "why": "Yield is food produced per unit area, so a high-yield variety "
               "feeds more people from the same farmland.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e13",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why global travel and trade make a new crop pest a greater "
                "threat than in the past.",
        "options": [
            "Pests breed faster inside an aeroplane than they do out in a field",
            "Pests are carried between continents in days rather than not at all",
            "Trade agreements oblige countries to accept plants that are infected",
            "Travel raises the temperature of the air, which helps pests spread",
        ],
        "correct_index": 1,
        "why": "A pest that once could not cross an ocean now arrives on "
               "imported plants, in a country whose crops have never met it.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e14",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a sustainable diet.",
        "options": [
            "One that contains the same foods every day of the year",
            "One that can be produced year after year without using up resources",
            "One grown entirely inside a country's own borders",
            "One that supplies more energy than a person needs",
        ],
        "correct_index": 1,
        "why": "A sustainable diet can be supplied indefinitely, because it does "
               "not exhaust the soil, the water or the fish stocks behind it.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e15",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Besides enough food existing, state the two things a population "
                "needs in order to be food secure.",
        "options": [
            "A warm climate and a large area of fertile land to farm",
            "A large fishing fleet and a large area of managed forest",
            "A way to distribute the food and prices people can afford",
            "A high birth rate and a young farming workforce",
        ],
        "correct_index": 2,
        "why": "Food security depends on access as well as supply: food that "
               "cannot be reached or afforded does not feed anybody.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e16",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one political action that can improve food security in a "
                "poorer country.",
        "options": [
            "Raising the tax on imported food so that less of it arrives",
            "Banning the sale of any food that happens to be grown abroad",
            "Requiring every farmer to grow exactly the same crop each year",
            "Reforming trade so its farmers can sell at a fair price",
        ],
        "correct_index": 3,
        "why": "Trade reform raises farm incomes, which lets farmers invest and "
               "lets families afford the food that is available.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e17",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the effect of a flood on a region's food security.",
        "options": [
            "A harvest can be destroyed, so less food is available that year",
            "Flooding raises the oxygen in the soil, so roots grow faster",
            "Flooding kills the crop pests, which raises the following yield",
            "There is no effect, because crops are grown under cover",
        ],
        "correct_index": 0,
        "why": "Floodwater drowns roots and washes crops away, so an extreme "
               "weather event can remove a whole year's production.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e18",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the approach to farming that aims to maximise the yield "
                "taken from each unit area of land.",
        "options": [
            "Organic farming",
            "Intensive farming",
            "Subsistence farming",
            "Extensive grazing",
        ],
        "correct_index": 1,
        "why": "Intensive farming uses fertilisers, pesticides and controlled "
               "conditions to take the largest possible yield per hectare.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-factors-affecting-food-security-s05",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country's population grows by 2% a year while its food "
                "production grows by 1% a year. Explain the effect on its food "
                "security over ten years.",
        "options": [
            "Food security improves, because production is growing every single year",
            "Food security is unchanged, because both of the figures are growing",
            "Food per person falls each year, so food security steadily worsens",
            "Food security worsens for one year only, after which the figures balance",
        ],
        "correct_index": 2,
        "why": "Demand is rising faster than supply, so the food available per "
               "person shrinks a little more every year.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s06",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fungal disease can spread through a field of one "
                "wheat variety faster than through a mixed hedgerow.",
        "options": [
            "Wheat has no cell walls, so the fungus can enter its cells easily",
            "A hedgerow is taller, so the fungal spores cannot reach the top of it",
            "Wheat is irrigated, and a fungus is able to spread only in dry air",
            "The crop plants are genetically identical and grown close together",
        ],
        "correct_index": 3,
        "why": "One variety means every plant has the same susceptibility, and "
               "close spacing carries spores from plant to plant.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s07",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a sharp rise in the price of diesel reduces a "
                "country's food production.",
        "options": [
            "Machinery, irrigation and transport all cost more, so farmers do less of each",
            "Diesel is used as a fertiliser, so crops receive fewer mineral ions",
            "Expensive diesel makes seed germinate more slowly in the field",
            "Diesel fumes raise the carbon dioxide in the air, harming crops",
        ],
        "correct_index": 0,
        "why": "Modern farming runs on fuel at every stage, so a fuel price rise "
               "raises the cost of every hectare planted and every load moved.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s08",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a drought in one major grain-exporting country "
                "raises food prices worldwide.",
        "options": [
            "Drought spreads from one country to another along the trade routes",
            "Less grain reaches the world market, so buyers compete for what is left",
            "Importing countries have to pay for extra storage while they wait",
            "Grain grown in a drought holds less energy, so more of it must be bought",
        ],
        "correct_index": 1,
        "why": "Grain is traded globally, so a shortfall in one large exporter "
               "reduces world supply and drives the price up everywhere.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s09",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why rising mean temperatures can reduce crop yields even "
                "in a region that stays wet.",
        "options": [
            "Heat raises photosynthesis, so the crop ripens before it has grown",
            "Warm air holds more carbon dioxide, which poisons the crop's leaves",
            "Heat above the crop's optimum damages enzymes and slows photosynthesis",
            "Higher temperatures shorten the day length, so less light is received",
        ],
        "correct_index": 2,
        "why": "Enzymes work fastest at an optimum temperature and denature above "
               "it, so heat past that point cuts the rate of photosynthesis.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s10",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A region's growing season shortens by three weeks as its climate "
                "changes. Explain how this reduces the harvest.",
        "options": [
            "A shorter season means the crop is harvested before it has germinated",
            "Less time in the ground means the crop takes up far fewer pesticides",
            "A shorter season raises the number of pests that attack the crop",
            "The crop has less time to photosynthesise, so it builds less biomass",
        ],
        "correct_index": 3,
        "why": "Yield is biomass built, and biomass accumulates over the days a "
               "crop spends photosynthesising in the field.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s11",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why producing 1 kg of chicken uses more grain and water "
                "than producing 1 kg of wheat flour.",
        "options": [
            "A bird holds more water in its body than a grain of wheat holds",
            "Chicken must be washed before sale, which uses most of the water",
            "The bird has to be fed grain and watered, and most of its feed is respired",
            "Wheat grows in winter, when no irrigation water is needed at all",
        ],
        "correct_index": 2,
        "why": "The chicken adds a trophic level: the grain and water go into the "
               "bird first, and only about a tenth of it becomes meat.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s12",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a smallholder given free high-yield seed may still "
                "fail to raise the harvest.",
        "options": [
            "Free seed is always of lower quality than seed that has been bought",
            "A smallholder is not permitted to plant seed that was given free",
            "Free seed germinates more slowly, because it is older when supplied",
            "Without fertiliser, water and pest control the seed cannot reach its yield",
        ],
        "correct_index": 3,
        "why": "A high-yield variety only outperforms a local one when its other "
               "needs are met, so seed alone leaves the real limit in place.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s13",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a new crop pathogen threatens food security more "
                "than a new weed does.",
        "options": [
            "A weed cannot spread between fields, but a pathogen is carried by the wind",
            "Weeds are all removed by herbicides, but no pathogen can be controlled",
            "A pathogen can destroy a whole crop, while a weed only competes with it",
            "A weed takes only water from the crop, and water is easily replaced",
        ],
        "correct_index": 2,
        "why": "A weed reduces a yield by competing for resources; a pathogen can "
               "kill the plants outright and remove the harvest completely.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s14",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why reducing the food thrown away by households raises "
                "food security.",
        "options": [
            "Waste food releases methane, which raises the yield of the next harvest",
            "Thrown-away food takes mineral ions out of the soil permanently",
            "Less waste lowers the birth rate, so there are fewer people to feed",
            "Food already grown then feeds more people, with no extra land or water",
        ],
        "correct_index": 3,
        "why": "Waste is food that has already cost land, water and fuel, so "
               "saving it raises supply without raising production at all.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s15",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A government subsidises fertiliser for smallholders. Suggest one "
                "benefit and one risk of the policy.",
        "options": [
            "Yields rise, but run-off into rivers can cause eutrophication",
            "Yields rise, and there is no risk, because fertiliser is a natural product",
            "Yields fall, because subsidised fertiliser is weaker than fertiliser sold",
            "Yields rise, but the fertiliser makes the harvested grain unsafe to eat",
        ],
        "correct_index": 0,
        "why": "Mineral ions raise yield, but nitrate washed into a river feeds "
               "algae, whose decay strips the oxygen from the water.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s16",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a country with plenty of food can still have a high "
                "rate of malnutrition.",
        "options": [
            "Food loses all of its protein once it has been stored for a month",
            "People may afford only one cheap staple, so their diet lacks variety",
            "Malnutrition is caused by eating too much, not by an unbalanced diet",
            "Such a country exports all of its fruit and all of its vegetables",
        ],
        "correct_index": 1,
        "why": "Food security means safe and nutritious food, and a diet of one "
               "cheap staple can supply energy while lacking protein and "
               "vitamins.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s17",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how the arrival of a new competitor plant species can "
                "threaten a crop.",
        "options": [
            "It releases a pathogen that goes on to infect the crop's roots",
            "It raises the temperature of the soil above the crop's own optimum",
            "It competes for light, water and mineral ions, so the crop grows less",
            "It takes up the carbon dioxide the crop needs, leaving none in the air",
        ],
        "correct_index": 2,
        "why": "A competitor is a biotic threat: it takes the resources the crop "
               "needs, so less biomass is built and the yield falls.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s18",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a country may choose a lower-yielding crop that "
                "needs less water.",
        "options": [
            "A lower-yielding crop is always more nutritious than a high-yielding one",
            "Crops that need less water can be harvested twice in every season",
            "A lower yield means less storage, so nothing at all is ever wasted",
            "A crop that survives a dry year gives a more reliable harvest overall",
        ],
        "correct_index": 3,
        "why": "Food security depends on reliability as well as size: a crop that "
               "fails in one year in three leaves people hungry in that year.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-factors-affecting-food-security-h05",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country harvests 18 million tonnes of grain but needs 21 "
                "million tonnes. Determine the shortfall as a percentage of its "
                "need.",
        "options": [
            "About 3%",
            "About 17%",
            "About 86%",
            "About 14%",
        ],
        "correct_index": 3,
        "why": "The shortfall is 3 million tonnes, and (3 ÷ 21) × 100 = "
               "14.3%.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h06",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the use of a drought-tolerant maize variety in a region "
                "whose rainfall has fallen by a third.",
        "options": [
            "It could restore yields, but seed cost and local acceptance may limit it",
            "It would restore yields fully, because such a variety needs no water",
            "It could not help, because maize is unable to grow without heavy rain",
            "It would not help, because new varieties are banned in every country",
        ],
        "correct_index": 0,
        "why": "Drought tolerance addresses the abiotic limit directly, but a "
               "variety that farmers cannot buy or will not plant changes "
               "nothing.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h07",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare sending food aid with building grain stores, for a "
                "country hit by repeated droughts.",
        "options": [
            "Aid raises the harvest, while stores have no effect on production",
            "Aid feeds people now; stores let a surplus be carried into a bad year",
            "Stores are cheaper, because food aid is paid for by the receiving country",
            "Aid works only once, whereas stores remove the need for any harvest",
        ],
        "correct_index": 1,
        "why": "Aid answers an emergency but leaves the country no better "
               "prepared; a store turns a good year into insurance for a bad "
               "one.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h08",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A region's population rises from 6.0 million to 7.5 million "
                "while food production stays the same. Determine the percentage "
                "fall in food available per person.",
        "options": [
            "15%",
            "25%",
            "20%",
            "80%",
        ],
        "correct_index": 2,
        "why": "Food per person falls to 6.0 ÷ 7.5 = 0.80 of its old value, "
               "which is a fall of 20%.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h09",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the suggestion that every country should aim to grow "
                "all of its own food.",
        "options": [
            "It would work everywhere, because any crop can be grown under glass",
            "It is pointless, because trade always supplies food more cheaply",
            "It is essential, because imported food carries pathogens into a country",
            "It reduces reliance on trade, but no country can grow every crop it needs",
        ],
        "correct_index": 3,
        "why": "Self-sufficiency protects a country from trade shocks, but "
               "climate limits what any one country can grow at all.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h10",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Wheat rust destroys 35% of a 40 million tonne wheat crop. "
                "Determine the mass lost and the mass remaining.",
        "options": [
            "14 million tonnes lost, 26 million remaining",
            "26 million tonnes lost, 14 million remaining",
            "1.4 million tonnes lost, 38.6 million remaining",
            "35 million tonnes lost, 5 million remaining",
        ],
        "correct_index": 0,
        "why": "40 × 0.35 = 14 million tonnes lost, leaving 40 − 14 = "
               "26 million tonnes.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h11",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a threat that is classified as abiotic can create a "
                "biotic threat as well.",
        "options": [
            "Abiotic factors turn into living organisms once the soil has warmed",
            "A warmer climate lets pests and pathogens survive in new regions",
            "Any abiotic change kills the crop's predators, and those are all biotic",
            "Abiotic threats are measured in exactly the same units as biotic ones",
        ],
        "correct_index": 1,
        "why": "Warming shifts the range in which an insect or fungus can "
               "overwinter, so an abiotic change delivers a new living pest.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h12",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "One family spends 70% of its income on food and another spends "
                "10%. Explain why a 20% rise in food prices threatens the first "
                "family far more.",
        "options": [
            "The poorer family's food spoils faster, because it cannot be stored",
            "Food prices rise more steeply for a family that already buys a lot",
            "It has far less income left over, so it has to buy less food to get by",
            "The richer family eats more, so a price rise costs it more in total",
        ],
        "correct_index": 2,
        "why": "A 20% rise on 70% of income takes 14% of everything the family "
               "has, against 2% for the other — so the first must cut back.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h13",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the effect on food security of a single year's drought "
                "with a gradual fall in average rainfall over twenty years.",
        "options": [
            "Both have the same effect, because both reduce the water reaching a crop",
            "The drought is worse, because a gradual change gives no warning at all",
            "The gradual fall is harmless, because plants adapt within a generation",
            "A drought is survived from stores; a lasting fall means the crop must change",
        ],
        "correct_index": 3,
        "why": "A one-off shortfall can be bridged; a permanent shift makes the "
               "existing crop unsuitable and forces a change of variety or land "
               "use.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h14",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A government must choose between subsidising fertiliser and "
                "subsidising irrigation in a dry, nutrient-poor region. Evaluate "
                "the two options.",
        "options": [
            "Without water the fertiliser cannot be taken up, so irrigation comes first",
            "Fertiliser comes first, because mineral ions supply the crop's energy",
            "Neither helps, because a dry region cannot grow a crop at all",
            "Both are equal, because either one on its own doubles the yield",
        ],
        "correct_index": 0,
        "why": "Mineral ions are absorbed in solution, so water is the limiting "
               "factor and fertiliser spread on dry soil does very little.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h15",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A region's food production is limited by water in summer and by "
                "temperature in winter. Explain why raising only the water supply "
                "helps less than expected.",
        "options": [
            "Extra water in summer lowers the temperature, so the winter crop fails",
            "Water and temperature are unable to limit one crop in the same region",
            "Temperature still limits the winter crop, so only part of the year improves",
            "Raising the water raises the number of pests, which cancels out the gain",
        ],
        "correct_index": 2,
        "why": "Removing one limiting factor only lifts production until the next "
               "one binds, and in winter that is still temperature.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h16",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that food security is an economic problem "
                "rather than a biological one.",
        "options": [
            "Purely economic, because enough food is already grown for everyone",
            "Purely biological, because prices have no effect on how much is grown",
            "Both — poverty blocks access, but pests, climate and yield are biological",
            "Neither, because food security depends on a country's politics alone",
        ],
        "correct_index": 2,
        "why": "Distribution and affordability are economic, but yield, pests, "
               "pathogens and climate set how much food there is to distribute.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h17",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country's wheat imports are cut off by a conflict abroad. "
                "Suggest the steps it could take in the following year, and the "
                "limit on each.",
        "options": [
            "Plant more wheat at once, which needs no extra land, seed or water",
            "Raise the price of bread, which increases the mass of wheat grown",
            "Ban all food exports, which raises the total mass of wheat harvested",
            "Plant more wheat, buy elsewhere or change diets — each costs time or money",
        ],
        "correct_index": 3,
        "why": "All three routes exist, but land and seed take a season, other "
               "suppliers charge more, and diets change slowly.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h18",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A new variety raises a 5 tonne per hectare yield by 40%, but "
                "needs 1.5 tonnes' worth of extra fertiliser per hectare. "
                "Determine the net gain per hectare.",
        "options": [
            "A net gain of 0.5 tonnes per hectare",
            "A net gain of 2 tonnes per hectare",
            "A net loss of 1.5 tonnes per hectare",
            "A net gain of 3.5 tonnes per hectare",
        ],
        "correct_index": 0,
        "why": "40% of 5 tonnes is 2 tonnes of extra yield, and 2 − 1.5 "
               "= 0.5 tonnes of net gain.",
    },

    # ══ standard/harder · s19-s26, h19-h26 (MRB-338 night 3 top-up) ══
    {
        "id": "ks4-factors-affecting-food-security-s19",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A region produces 730 000 000 kg of grain a year for a population of "
                "2 000 000 people. Calculate the average grain available per person "
                "per year.",
        "options": [
            "7.3 kg per person per year, from dividing the population by the tonnes produced instead of the reverse",
            "36.5 kg per person per year, from mistakenly treating the harvest as though it were ten times smaller",
            "1 460 kg per person per year, from multiplying the two given figures rather than dividing them",
            "365 kg per person per year, from dividing 730 000 000 kg by a population of 2 000 000 people",
        ],
        "correct_index": 3,
        "why": "730 000 000 kg divided by 2 000 000 people gives 365 kg available "
               "per person each year.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s20",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A locust swarm crossing a region can destroy an entire season's crop "
                "within days. Suggest why this makes food security especially "
                "difficult to plan for, compared with a slow-developing threat such "
                "as a gradually changing climate.",
        "options": [
            "It makes little difference, because both a locust swarm and a changing climate develop at roughly the same steady rate",
            "A locust swarm strikes with almost no warning, leaving far less time to prepare than a threat that develops over years",
            "It makes planning easier, since a locust swarm always follows a fixed, predictable yearly route",
            "It makes little difference, because both threats are equally easy to prevent with modern pesticides",
        ],
        "correct_index": 1,
        "why": "A sudden threat like a locust swarm leaves almost no time to "
               "prepare, unlike a threat that develops gradually over years.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s21",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Vertical farming grows crops in stacked layers inside a controlled "
                "building, often within a city. Suggest one way this could improve "
                "food security in a densely populated country with little farmland.",
        "options": [
            "It can produce food without using any of the country's scarce farmland, often close to where people live",
            "It removes the need for any energy input at all, since the crops are grown entirely indoors",
            "It works only for grain crops such as wheat and rice, which are the foods most needed in a crowded country",
            "It increases the amount of farmland available, by converting existing buildings directly into open fields",
        ],
        "correct_index": 0,
        "why": "Growing food in stacked layers indoors avoids using scarce farmland "
               "and can be sited close to where people actually live.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s22",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Prolonged drought forces many farming families in a region to "
                "migrate to cities in search of work. Suggest the effect this has on "
                "the region's future food production.",
        "options": [
            "Production would stay unaffected, since crops do not really need any farm workers once they have first been planted",
            "Production would rise, because fewer people remaining would mean more food is left for each of them",
            "Production could fall further, since fewer people remain to farm the land, deepening the original shortage",
            "Production would move entirely to the cities, where the migrating families have now settled instead",
        ],
        "correct_index": 2,
        "why": "With fewer people left to work the land, the region's own food "
               "production can fall further, deepening the shortage that caused the "
               "migration.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s23",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a country that receives enough rainfall overall can "
                "still suffer from water shortages that threaten its food security.",
        "options": [
            "It cannot happen; a country with enough total rainfall always has enough water exactly where and when it is needed",
            "Rainfall may be very uneven across the year or across regions, so farms can still lack water when crops need it most",
            "It happens only because rain falling on cities is wasted and never reaches any farmland at all",
            "It cannot happen unless the country's total rainfall figure has been measured completely wrongly",
        ],
        "correct_index": 1,
        "why": "National totals can hide uneven rainfall across the year or across "
               "regions, so farms can still be short of water exactly when crops "
               "need it.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s24",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why people living in a remote rural area of a developing "
                "country may be less food secure than people in the country's capital "
                "city, even when national food production is high.",
        "options": [
            "Poor roads and lower rural incomes can make it harder to move food to remote areas and harder to afford it there",
            "Rural areas always produce far less food than a capital city does, whatever the country's total production",
            "City food is grown locally within city limits, while rural food always has to be transported in from elsewhere",
            "Rural populations need less food overall, so national production figures matter less for them",
        ],
        "correct_index": 0,
        "why": "Poorer roads and lower incomes in remote areas make it both harder "
               "to move food there and harder for people to afford it once it "
               "arrives.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s25",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country imports most of its staple grain from a single trading "
                "partner. Suggest why this makes the country's food security more "
                "vulnerable than if it imported from several different countries.",
        "options": [
            "It makes no real difference at all, since every trading partner in the world faces exactly the same risks anyway",
            "It would only matter if the country produced no food of its own at all",
            "Depending on one partner creates a single point of failure; several partners spread the risk if one is disrupted",
            "Importing from several countries is always more expensive, whatever the risk involved",
        ],
        "correct_index": 2,
        "why": "Relying on one partner creates a single point of failure, whereas "
               "several partners mean a disruption to one still leaves others "
               "supplying food.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s26",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State two features, other than yield, that would make a crop variety "
                "more suitable for a region that is becoming hotter and drier because "
                "of climate change.",
        "options": [
            "Resistance to common pests, and a shorter growing season than any existing variety",
            "Tolerance of higher temperatures, and the ability to grow with less available water",
            "A larger overall size, and a sweeter taste than the varieties already grown in the region",
            "A brighter colour when ripe, and a longer shelf life once it has been harvested",
        ],
        "correct_index": 1,
        "why": "A hotter, drier climate calls for a variety that tolerates higher "
               "temperatures and needs less available water to grow.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h19",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A region produces enough grain to supply 1 kg per person per day, "
                "comfortably above the recommended minimum of 400 g per person per "
                "day. A government official claims the region must therefore be food "
                "secure. Evaluate this claim.",
        "options": [
            "The claim is fully supported, because a production figure above the recommended minimum always guarantees food security",
            "The claim is not proven; distribution, affordability and access also decide whether people actually get that food",
            "The claim is fully supported, because the recommended minimum already allows for uneven distribution",
            "The claim is false, because no country has ever produced enough grain to reach 1 kg per person per day",
        ],
        "correct_index": 1,
        "why": "A production figure above the minimum shows there is enough food in "
               "total, but distribution, affordability and access still decide "
               "whether people actually receive it.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h20",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A government invests heavily in long-term drought-resistant crop "
                "breeding programmes but sets up no early-warning system for locust "
                "swarms. Evaluate this strategy.",
        "options": [
            "It is a sound strategy, because drought and locust swarms are really the same underlying threat",
            "It is a sound strategy, since breeding programmes also protect against sudden pest outbreaks automatically",
            "It cannot be judged, because breeding programmes and early-warning systems both always take the very same time to set up",
            "It is a mismatched strategy; a slow response suits the slow threat, but leaves the fast-developing locust threat unaddressed",
        ],
        "correct_index": 3,
        "why": "A slow response suits a slow-developing threat like drought, but "
               "leaves the fast-developing locust threat with no warning system at "
               "all.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h21",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A region currently produces exactly enough grain to meet its 400 g "
                "per person per day minimum for its 3 000 000 people. Population "
                "grows by 5% the following year while production stays exactly the "
                "same. Determine the new average grain available per person per day, "
                "and state whether the minimum is still met.",
        "options": [
            "381 g per person per day, still comfortably above the minimum once the new population is accounted for",
            "400 g per person per day, since fixed production always keeps pace with a growing population automatically",
            "420 g per person per day, from applying the 5% growth figure to the daily minimum instead of to the population itself",
            "About 381 g per person per day, which falls below the 400 g minimum now that more people share the same fixed total",
        ],
        "correct_index": 3,
        "why": "The fixed total divided among 3 150 000 people (a 5% rise on 3 000 "
               "000) works out at about 381 g per person per day, which is below the "
               "400 g minimum.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h22",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A city council proposes replacing all of its remaining traditional "
                "farmland with vertical farms, arguing this will make the city fully "
                "food secure while using far less land. Evaluate this proposal.",
        "options": [
            "The proposal is fully justified, because vertical farms can already grow every single staple crop just as cheaply as an open field can",
            "The proposal is fully justified, because vertical farms need no energy input once they have been built",
            "The proposal is not straightforward; vertical farms suit crops like leafy greens well, but bulk staples and running costs remain a problem",
            "The proposal cannot work at all, because no useful crop has ever been grown successfully in a vertical farm",
        ],
        "correct_index": 2,
        "why": "Vertical farms suit crops like leafy greens well, but bulk staple "
               "crops and high running costs mean they cannot simply replace all "
               "traditional farmland.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h23",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two countries each import 80% of their staple food. Country A "
                "imports from five different trading partners across three "
                "continents. Country B imports 80% from a single neighbouring "
                "country. A regional conflict disrupts trade across the whole "
                "continent that Country B's neighbour is on. Compare the effect on "
                "each country's food security.",
        "options": [
            "Country A is more resilient, since only some of its five partners are affected, while Country B loses its one main supplier entirely",
            "Both countries are affected in exactly the same way, because a regional conflict always disrupts every trading partner worldwide",
            "Country B is more resilient, because relying on a single neighbour makes supply arrangements far simpler to manage",
            "Neither country is affected, since a regional conflict never disrupts food imports specifically",
        ],
        "correct_index": 0,
        "why": "Country A still has other partners largely unaffected by a conflict "
               "on one continent, while Country B loses its one main supplier "
               "entirely.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h24",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A drought forces 15% of a farming region's workforce to migrate "
                "away, and production falls in proportion to the workforce lost. The "
                "region originally produced 800 000 tonnes of grain a year, feeding "
                "an original population of 2 000 000 people at 400 kg of grain per "
                "person per year. Determine the new production level, and the number "
                "of people this new level can still feed.",
        "options": [
            "800 000 tonnes and 2 000 000 people, since a 15% loss of workers has no measurable effect on total production",
            "680 000 tonnes and 2 000 000 people, since the same population can always be fed once any harvest is brought in",
            "120 000 tonnes and 300 000 people, from treating the 15% figure as the new production level directly",
            "680 000 tonnes, feeding 1 700 000 people, leaving 300 000 of the original population without enough grain",
        ],
        "correct_index": 3,
        "why": "800 000 tonnes falls by 15% to 680 000 tonnes, which at 400 kg per "
               "person feeds 1 700 000 people, leaving 300 000 of the original "
               "population short.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h25",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country diversifies its grain imports across five trading "
                "partners, but all five partners buy their own grain from the same "
                "single global exporter. Evaluate whether this import diversification "
                "genuinely reduces the country's food security risk.",
        "options": [
            "It genuinely reduces the risk, because five entirely separate trading partners can never all be affected by the very same event",
            "It does not genuinely reduce the risk, since a disruption to the shared original exporter still affects all five partners at once",
            "It genuinely reduces the risk, but only if all five partners are based on five different continents",
            "It cannot be evaluated, because it is impossible to know where a trading partner's own grain originally comes from",
        ],
        "correct_index": 1,
        "why": "If all five partners ultimately source from the same exporter, a "
               "disruption there still affects every partner at once, so the "
               "diversification is only superficial.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h26",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country receives plenty of rainfall nationally, but 90% of it "
                "falls in just three months of the year, and the country has very "
                "little water storage infrastructure such as reservoirs. Evaluate the "
                "country's food security risk from this pattern of rainfall.",
        "options": [
            "The risk is low, because a country's total yearly rainfall is what matters most for food security, not when it falls",
            "The risk is low, because crops only need water during the three wettest months of the year in any country",
            "The risk cannot be judged without knowing the exact crop varieties the country is currently growing",
            "The risk is high; without storage, water is unavailable for nine months of the year regardless of the yearly total",
        ],
        "correct_index": 3,
        "why": "Without storage, the water is unavailable for the other nine months "
               "of the year regardless of how much falls in total, so the shortage "
               "risk stays high.",
    },
]
