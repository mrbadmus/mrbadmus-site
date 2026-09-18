"""Chemistry · Using resources — the MRB-338 expansion for
`alternative-metal-extraction`.

The shipped rows already set out what phytomining and bioleaching are, one
advantage and one disadvantage each, and the two recovery routes from the
leachate. The weight here therefore falls on the working detail behind them:
crushing the ore and why it matters, what the bacteria are actually getting out
of the sulfide, why the leachate turns acidic, and why the ash and the leachate
both still need a traditional step before there is any metal.

Round that sits the evaluation this Higher-tier spec point asks for — the
carbon-neutral claim tested in practice rather than in principle, iron against
zinc for the displacement, a heap that stops working, and whether either method
could replace mining. Five rows carry ore-grade arithmetic, in both directions
between percentage grade and recovered mass.
"""

TOPIC = "resources"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": "ks4-alternative-metal-extraction-e06",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "What name is given to the metal-rich solution that drains "
                "out of a bioleaching heap?",
        "options": [
            "The leachate",
            "The slag",
            "The bio-ore",
            "The flux",
        ],
        "correct_index": 0,
        "why": "The solution carrying the dissolved metal ions away from the "
               "ore is called the leachate.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e07",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "In which part of a plant used for phytomining do the metal "
                "ions build up?",
        "options": [
            "Only in the outer bark of the stem",
            "In the shoots and the leaves",
            "In the seeds and nowhere else",
            "In the soil around the roots",
        ],
        "correct_index": 1,
        "why": "The plant draws the ions in through its roots and "
               "concentrates them in the shoots and leaves, which is the part "
               "that is harvested.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e08",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "What name is often given to the ash left after a "
                "phytomining crop has been burned?",
        "options": [
            "Leachate",
            "Slag",
            "Bio-ore",
            "Clinker",
        ],
        "correct_index": 2,
        "why": "The ash is a concentrated source of the metal compound, so it "
               "is treated as an ore and called a bio-ore.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e09",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State one environmental problem caused by digging a large "
                "open-cast mine.",
        "options": [
            "It raises the oxygen content of the local air",
            "It uses up the world's supply of fresh water",
            "It makes the surrounding soil a great deal more fertile",
            "It destroys habitats and scars the landscape",
        ],
        "correct_index": 3,
        "why": "Removing enormous volumes of rock strips the vegetation and "
               "leaves waste tips and a pit that the wildlife cannot use.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e10",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Give one drawback of smelting as a way of getting a metal "
                "out of its ore.",
        "options": [
            "It leaves the metal mixed in with the plant ash",
            "It needs a lot of energy and gives off carbon dioxide",
            "It works on an ore only when that ore contains no sulfur",
            "It takes several growing seasons to be completed",
        ],
        "correct_index": 1,
        "why": "A furnace has to be held at a very high temperature, and the "
               "carbon used as the reducing agent ends up as carbon dioxide.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e11",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "What is done to the rock before the bacteria are added to a "
                "bioleaching heap?",
        "options": [
            "It is melted down in a furnace",
            "It is dissolved in nitric acid",
            "It is crushed into small pieces",
            "It is dried out in a hot oven",
        ],
        "correct_index": 2,
        "why": "Crushing the rock is the first step, because the bacteria can "
               "only act on the surfaces they can reach.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e12",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Apart from producing metal, give one benefit of growing a "
                "phytomining crop on an old industrial site.",
        "options": [
            "It cleans metal out of contaminated soil",
            "It turns the site into a supply of fuel",
            "It raises the grade of the rock beneath",
            "It produces a crop that can be eaten",
        ],
        "correct_index": 0,
        "why": "The plants remove metal ions from the soil as they grow, so "
               "the land is left less contaminated than it was.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e13",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "What do the bacteria used in bioleaching get out of the ore?",
        "options": [
            "A place to shelter from sunlight",
            "The oxygen that they need in order to breathe",
            "A supply of fresh water to live in",
            "The energy that they need to live",
        ],
        "correct_index": 3,
        "why": "The bacteria use the oxidation of the metal sulfide as their "
               "energy source, which is why the process runs at all.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e14",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Which two conditions have to be kept right for the bacteria "
                "in a bioleaching heap to stay active?",
        "options": [
            "Temperature and pH",
            "Pressure and voltage",
            "Colour and hardness",
            "Density and volume",
        ],
        "correct_index": 0,
        "why": "The bacteria are living organisms, so they work only within a "
               "limited range of temperature and acidity.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e15",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "An ore contains 0.5% copper by mass. Calculate the mass of "
                "copper in 200 tonnes of this ore.",
        "options": [
            "0.1 tonnes",
            "1 tonne",
            "10 tonnes",
            "100 tonnes",
        ],
        "correct_index": 1,
        "why": "0.5% of 200 tonnes is 0.005 x 200 = 1 tonne of copper.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e16",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Give one reason why a bioleaching heap needs no furnace.",
        "options": [
            "The rock has already been melted once before",
            "The bacteria work at ordinary outdoor temperatures",
            "The copper is already a metal inside the rock",
            "The acid used boils at a very low temperature",
        ],
        "correct_index": 1,
        "why": "Bioleaching is driven by living bacteria rather than by heat, "
               "so the heap works at the temperature of the site.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e17",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what phytomining and bioleaching have in common as "
                "methods.",
        "options": [
            "Both melt the rock down before any metal is collected from it",
            "Both give the pure metal without a further step",
            "Both work faster than a furnace would work",
            "Both use living organisms to concentrate the metal",
        ],
        "correct_index": 3,
        "why": "One uses plants and the other bacteria, but in each case a "
               "living organism does the work of concentrating the metal.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e18",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State why a bioleaching heap is built on a sealed, "
                "waterproof base.",
        "options": [
            "To keep the solution in and collect it",
            "To keep the rock warm while it reacts",
            "To stop rainwater soaking up into the base of the heap",
            "To stop sunlight reaching the bacteria",
        ],
        "correct_index": 0,
        "why": "The base collects the metal-rich leachate for processing and "
               "stops the acidic solution soaking into the ground.",
    },
    # -------------------------------------------------------------- standard
    {
        "id": "ks4-alternative-metal-extraction-s07",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the rock is broken into small pieces before "
                "bioleaching begins.",
        "options": [
            "Small pieces have a greater surface area for the bacteria",
            "Small pieces hold a higher percentage of metal",
            "Small pieces dissolve completely in the acid",
            "Small pieces stop the bacteria from washing off the heap in rain",
        ],
        "correct_index": 0,
        "why": "The bacteria can only act on exposed surfaces, so crushing "
               "gives far more surface for the same mass and speeds the "
               "process up.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s08",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the ash from a phytomining crop still has to be "
                "smelted or electrolysed.",
        "options": [
            "The ash holds a compound of the metal, not the metal",
            "The ash is too hot to be handled until it is melted",
            "The ash contains the metal as a gas trapped inside its pores",
            "The ash has to be purified before it can be weighed",
        ],
        "correct_index": 0,
        "why": "The plant takes up metal ions, so what survives the fire is a "
               "metal compound, and a reduction step is still needed to "
               "release the metal.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s09",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why adding iron to a leachate causes copper to be "
                "deposited.",
        "options": [
            "Iron is denser, so it pushes the copper out of solution",
            "Iron is more reactive, so it takes the place of the copper",
            "Iron is magnetic, so it pulls the copper ions towards it",
            "Iron is softer, so the copper sticks to its surface easily",
        ],
        "correct_index": 1,
        "why": "Iron is above copper in the reactivity series, so it loses "
               "electrons to the copper ions and displaces copper as the "
               "metal.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s10",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A heap holds 5000 tonnes of ore containing 0.4% copper. "
                "Bioleaching recovers 80% of that copper. Calculate the mass "
                "of copper obtained.",
        "options": [
            "4 tonnes",
            "16 tonnes",
            "20 tonnes",
            "25 tonnes",
        ],
        "correct_index": 1,
        "why": "The ore holds 0.004 x 5000 = 20 tonnes of copper, and 80% of "
               "20 tonnes is 16 tonnes.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s11",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Suggest why a disused industrial site is a better place for "
                "a phytomining crop than good farmland.",
        "options": [
            "The site is already too polluted to grow food on",
            "The site has a deeper layer of topsoil to draw on",
            "The site receives a great deal more rain through the year",
            "The site has bacteria that help the plants to grow",
        ],
        "correct_index": 0,
        "why": "The metal in the ground is what makes the site unusable for "
               "food, and it is exactly what the crop is there to remove.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s12",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why phytomining and bioleaching are described as "
                "more sustainable than opening a new mine.",
        "options": [
            "They work on rock that would otherwise be left as waste",
            "They produce a purer metal than a new mine would produce",
            "They can be repeated on the same rock again and again",
            "They need no land, so no habitat anywhere is disturbed",
        ],
        "correct_index": 0,
        "why": "They make a resource of rock too poor to smelt, which "
               "stretches the remaining reserves and avoids excavating fresh "
               "ground.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s13",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Suggest why a company may choose bioleaching for a site even "
                "though it will take several years.",
        "options": [
            "The rock is worthless to smelt, so slow copper beats none",
            "The bacteria make the copper purer than smelting",
            "The rock itself would give a different metal if it were put "
            "in a smelter",
            "The bacteria work on without any supervision",
        ],
        "correct_index": 0,
        "why": "The alternative for a very low grade ore is not a faster "
               "method but no extraction at all, so a slow process that pays "
               "is still worth running.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s14",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Put the stages of phytomining into the correct order.",
        "options": [
            "Burn, grow, harvest, treat the ash",
            "Grow, harvest, burn, treat the ash",
            "Harvest, grow, treat the ash, burn",
            "Treat the ash, grow, burn, harvest",
        ],
        "correct_index": 1,
        "why": "The plants must grow and take up the metal first, then be cut "
               "and burned, and only then is the ash processed.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s15",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the solution draining from a bioleaching heap is "
                "acidic.",
        "options": [
            "Acid is sprayed onto the heap to kill off the bacteria",
            "Oxidising the sulfide in the ore produces sulfuric acid",
            "The crushed rock contains a natural acid that the rain washes "
            "out",
            "The copper ions react with water to release hydrogen gas",
        ],
        "correct_index": 1,
        "why": "The bacteria oxidise sulfide to sulfate, and sulfate in water "
               "with the hydrogen ions released gives a sulfuric acid "
               "solution.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s16",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A mine holds its zinc as a carbonate. Suggest why "
                "bioleaching is unlikely to work there.",
        "options": [
            "Zinc is too reactive to be released from any compound",
            "A carbonate is far too soluble for a heap to hold it",
            "The bacteria get their energy by oxidising a sulfide",
            "Carbonates decompose long before the bacteria can reach them",
        ],
        "correct_index": 2,
        "why": "The bacteria used in bioleaching feed on the oxidation of "
               "metal sulfides, so an ore with no sulfide gives them no "
               "energy source.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s17",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Ash from a phytomining crop is 12% copper by mass. Calculate "
                "the mass of ash needed to supply 60 kg of copper.",
        "options": [
            "7.2 kg",
            "72 kg",
            "500 kg",
            "720 kg",
        ],
        "correct_index": 2,
        "why": "The ash needed is 60 / 0.12 = 500 kg, of which 60 kg is "
               "copper.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s18",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why a bioleaching heap yields less copper each week "
                "through a cold winter.",
        "options": [
            "The copper sulfide freezes solid and stops reacting",
            "The acid in the heap is diluted by the winter rainfall",
            "The bacteria are less active at a lower temperature",
            "The bacteria need daylight, and the winter days are much shorter",
        ],
        "correct_index": 2,
        "why": "The bacteria are living organisms whose reactions slow as "
               "they cool, so the rate at which they release copper ions "
               "falls.",
    },
    # ---------------------------------------------------------------- harder
    {
        "id": "ks4-alternative-metal-extraction-h07",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A company owns one deposit of 2% copper sulfide ore and one "
                "of 0.2% copper sulfide ore. Explain which suits bioleaching.",
        "options": [
            "The 2% deposit, because there is more for the bacteria to eat",
            "The 0.2% deposit, because the richer one is worth smelting",
            "The 2% deposit, because bioleaching only works on rich rock",
            "Neither, because bioleaching cannot be used on a sulfide ore",
        ],
        "correct_index": 1,
        "why": "Bioleaching earns its place where smelting would cost more "
               "than the metal is worth, so it is the poorer deposit that "
               "needs it.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h08",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A plant treats 40 000 tonnes of ore a year. The ore is 0.25% "
                "copper and 70% of that copper is recovered. Calculate the "
                "mass of copper obtained in a year.",
        "options": [
            "30 tonnes",
            "70 tonnes",
            "100 tonnes",
            "700 tonnes",
        ],
        "correct_index": 1,
        "why": "The ore holds 0.0025 x 40 000 = 100 tonnes of copper, and 70% "
               "of 100 tonnes is 70 tonnes.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h09",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Evaluate the claim that phytomining as it is actually "
                "carried out releases no net carbon dioxide.",
        "options": [
            "Correct, because burning a plant releases no carbon dioxide",
            "Correct, because the ash locks the carbon away as a solid",
            "Overstated, because the machinery and the smelting burn fuel",
            "Wrong, because a growing plant takes in no carbon dioxide",
        ],
        "correct_index": 2,
        "why": "The growing and burning do balance, but ploughing, "
               "harvesting, transport and the final extraction from the ash "
               "all use fuel that the plants never absorbed.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h10",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Copper obtained by adding scrap iron to a leachate is not "
                "pure enough for electrical cable. Explain why, and state "
                "what is done next.",
        "options": [
            "It holds trapped iron, so it is purified by electrolysis",
            "It holds trapped sulfur, so it is washed in cold water",
            "It is too soft to draw into wire, so it is alloyed first",
            "It is coated in acid, so it is neutralised with powdered "
            "limestone",
        ],
        "correct_index": 0,
        "why": "Displacement leaves iron mixed through the copper, and even a "
               "small impurity lowers conductivity badly, so the copper is "
               "refined by electrolysis.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h11",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A bioleaching heap is built on rock containing a lot of "
                "limestone. Predict the effect on the process and explain it.",
        "options": [
            "The copper yield rises, because limestone is a good catalyst",
            "The copper yield falls, because the limestone neutralises the "
            "acid the bacteria need",
            "The copper yield is unchanged, because limestone takes no part "
            "in the reaction",
            "The copper yield rises, because limestone holds the leachate in "
            "the heap for longer",
        ],
        "correct_index": 1,
        "why": "The bacteria need acidic conditions; carbonate rock reacts "
               "with the acid as fast as it forms, so the pH rises and the "
               "bacteria slow or stop.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h12",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student says phytomining is pointless because one plant "
                "holds only a few grams of metal. Evaluate this.",
        "options": [
            "Correct, because a field of plants cannot hold enough metal",
            "Wrong, because a whole crop concentrates metal from a huge "
            "volume of poor soil",
            "Correct, because the metal is lost when the plants are burned",
            "Wrong, because each plant holds kilograms of metal in its roots",
        ],
        "correct_index": 1,
        "why": "The point is concentration rather than the mass in any one "
               "plant: a whole harvest reduces to a small mass of ash that is "
               "far richer than the ground it grew on.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h13",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "200 tonnes of harvested plants burn to give 8 tonnes of ash "
                "that is 15% copper. Calculate the percentage of the original "
                "crop mass that was copper.",
        "options": [
            "0.15%",
            "0.6%",
            "1.2%",
            "15%",
        ],
        "correct_index": 1,
        "why": "The ash holds 0.15 x 8 = 1.2 tonnes of copper, and 1.2 / 200 "
               "x 100 = 0.6%.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h14",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Suggest why a bioleaching operation can stay profitable in a "
                "year when the copper price falls and smelters close.",
        "options": [
            "Its running costs are low, so it still pays at a low price",
            "Its bacteria can be sold on for more than the copper is worth",
            "Its copper is a different grade that has a fixed price",
            "Its heaps produce more copper when the price is falling",
        ],
        "correct_index": 0,
        "why": "Once the heap is built there is little to pay for beyond "
               "pumping, so the price at which the operation breaks even is "
               "far below a smelter's.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h15",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Evaluate growing a phytomining crop on farmland that a "
                "factory contaminated with zinc.",
        "options": [
            "It recovers zinc and cleans the land, but grows no food for "
            "years",
            "It recovers zinc and leaves the land ready for food the next "
            "spring",
            "It leaves the zinc where it was, but the crop can still be "
            "sold as animal food",
            "It adds more zinc to the land, so the contamination gets "
            "steadily worse",
        ],
        "correct_index": 0,
        "why": "Repeated crops lower the zinc in the soil and yield a "
               "bio-ore, but each cycle takes a season and nothing edible can "
               "be grown meanwhile.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h16",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Zinc would displace copper from a leachate just as iron "
                "does. Suggest why iron is used instead.",
        "options": [
            "Zinc is not reactive enough to displace any copper",
            "Zinc would dissolve the copper as fast as it appeared",
            "Scrap iron is far cheaper and much easier to obtain",
            "Scrap iron is the only metal that works in an acid",
        ],
        "correct_index": 2,
        "why": "Both metals are above copper in the reactivity series, so the "
               "choice is made on cost, and scrap iron is abundant and nearly "
               "free.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h17",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A heap stops yielding copper after five years although "
                "analysis shows copper is still in the rock. Suggest why.",
        "options": [
            "The copper still there is sealed inside the rock particles",
            "The copper still there has turned into a different element",
            "The bacteria have used up all the oxygen in the atmosphere",
            "The copper still there has already dissolved and drained out of "
            "the heap",
        ],
        "correct_index": 0,
        "why": "Bacteria only reach exposed surfaces, so once the accessible "
               "sulfide has reacted the rest stays locked inside particles "
               "until the rock is crushed more finely.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h18",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Evaluate the claim that phytomining and bioleaching will "
                "soon replace mining and smelting altogether.",
        "options": [
            "Correct, because they are faster than mining and smelting are",
            "Correct, because every metal can be taken up by some plant",
            "Overstated, because both are slow and suit only some metals",
            "Wrong, because neither method can recover metal from an ore",
        ],
        "correct_index": 2,
        "why": "They extend what counts as an ore, but they take years, work "
               "for a limited set of metals, and still hand the metal over to "
               "a traditional step at the end.",
    },
]
