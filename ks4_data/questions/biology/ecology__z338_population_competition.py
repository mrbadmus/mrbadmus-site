"""Biology · Ecology — the MRB-338 expansion, subtopic `population-competition`.

Spec 4.7.1. The weight falls on carrying capacity and on the density-dependent
against density-independent split, because those two ideas do the explaining in
every other row: why growth levels off, why a frost and a disease behave
differently, why relieving one limit simply moves the ceiling. Competition is
examined as intraspecific and interspecific side by side, through the lesson's
own named cases — robins holding territories, stags in the rut, oaks reaching
for light, grey squirrels against red — and the predator-prey lag is asked as a
reading of data rather than as the lesson's own question about it."""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ────────────────────────────────────────────────────────────
    {
        "id": "ks4-population-competition-e05",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the carrying capacity of a habitat.",
        "options": [
            "The largest population its resources can support",
            "The number of species the habitat contains altogether",
            "The total mass of all the organisms living in it",
            "The area of ground the habitat covers in total",
        ],
        "correct_index": 0,
        "why": "Carrying capacity is the maximum population size a habitat "
               "can sustain with the food, water and space it has available.",
    },
    {
        "id": "ks4-population-competition-e06",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of competition that takes place between two "
                "individuals of the same species.",
        "options": [
            "Interspecific competition",
            "Density-independent competition",
            "Intraspecific competition",
            "Indirect competition",
        ],
        "correct_index": 2,
        "why": "Intraspecific competition is competition within one species, "
               "and it is the most intense kind because the individuals need exactly "
               "the same things.",
    },
    {
        "id": "ks4-population-competition-e07",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two male robins each defend a patch of garden against the "
                "other. Name the resource they are competing for.",
        "options": [
            "Minerals",
            "Territory",
            "Oxygen",
            "Light",
        ],
        "correct_index": 1,
        "why": "A territory holds the food and nest sites a breeding pair "
               "needs, so holding one is what the two birds are contesting.",
    },
    {
        "id": "ks4-population-competition-e08",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a density-dependent factor?",
        "options": [
            "A disease spreading through a crowded colony",
            "A volcanic eruption covering a whole valley in ash",
            "A flood after a week of very heavy rainfall",
            "A forest fire started by a lightning strike",
        ],
        "correct_index": 0,
        "why": "A pathogen passes between individuals more easily the more "
               "crowded they are, so its effect grows with the density of the "
               "population.",
    },
    {
        "id": "ks4-population-competition-e09",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to a population when its death rate is "
                "greater than its birth rate.",
        "options": [
            "It grows steadily",
            "It stays constant",
            "It doubles in size each year",
            "It shrinks",
        ],
        "correct_index": 3,
        "why": "More individuals are dying than are being born, so the total "
               "number in the population falls.",
    },
    {
        "id": "ks4-population-competition-e10",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which resource do animals compete for but plants do not?",
        "options": [
            "Water",
            "Mates",
            "Space",
            "Minerals",
        ],
        "correct_index": 1,
        "why": "Animals compete for access to a mate as well as for food, "
               "water, territory and shelter; plants compete for light, water, "
               "minerals and space.",
    },
    {
        "id": "ks4-population-competition-e11",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A river floods and drowns most of the voles in a meadow. "
                "Classify this factor.",
        "options": [
            "Density-dependent on the vole numbers",
            "Intraspecific",
            "Interspecific",
            "Density-independent",
        ],
        "correct_index": 3,
        "why": "The flood drowns the same proportion of voles whether they "
               "are crowded or sparse, so its effect does not depend on the "
               "population's density.",
    },
    {
        "id": "ks4-population-competition-e12",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the term for a species brought into an area that then "
                "outcompetes the species already living there.",
        "options": [
            "An indicator species of the conditions",
            "A keystone species",
            "An invasive species",
            "A pioneer species",
        ],
        "correct_index": 2,
        "why": "An invasive species is one introduced to a new area where it "
               "outcompetes or preys on the native species, sometimes to local "
               "extinction.",
    },
    # ── standard ──────────────────────────────────────────────────────────
    {
        "id": "ks4-population-competition-s05",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Put these four events of a predator-prey relationship into "
                "the order in which they happen.",
        "options": [
            "Prey rise, predators rise, prey fall, predators fall",
            "Predators rise, then prey, then both fall",
            "Prey fall, predators rise, then both fall",
            "Predators fall, prey fall, then both rise",
        ],
        "correct_index": 0,
        "why": "More prey means more food for the predators, whose numbers "
               "then rise; the heavier hunting pushes the prey down, and the "
               "predators follow them down for want of food.",
    },
    {
        "id": "ks4-population-competition-s06",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why disease is classed as a density-dependent factor.",
        "options": [
            "A pathogen infects the same share of a given population every "
            "year",
            "Disease is caused by a living organism rather than by weather",
            "A pathogen spreads more easily when individuals are crowded",
            "Disease affects large populations rather than small ones",
        ],
        "correct_index": 2,
        "why": "Transmission depends on contact between individuals, so the "
               "denser the population the faster a pathogen moves through it.",
    },
    {
        "id": "ks4-population-competition-s07",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Yeast growing in a sealed flask stops increasing and then "
                "declines. Explain the part played by its own waste products.",
        "options": [
            "The waste is eaten by the yeast, which then runs out of food",
            "The waste builds up until the conditions become toxic",
            "The waste seals the flask, so no more oxygen can enter it",
            "The waste changes the yeast into a different species entirely",
        ],
        "correct_index": 1,
        "why": "Metabolic waste accumulates in a closed system, and once it "
               "reaches a high enough concentration it raises the death rate and the "
               "population falls.",
    },
    {
        "id": "ks4-population-competition-s08",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Red squirrels disappeared from a wood within ten years of "
                "grey squirrels arriving. Name the resources most likely contested.",
        "options": [
            "Sunlight and soil minerals",
            "Food and nesting sites",
            "Mates and drinking water",
            "Oxygen and carbon dioxide",
        ],
        "correct_index": 1,
        "why": "Two different species competing need the same limited "
               "resources, and for woodland squirrels those are the seed crop and "
               "the holes and branches they nest in.",
    },
    {
        "id": "ks4-population-competition-s09",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why light is a resource plants compete for but mates "
                "are not.",
        "options": [
            "Plants do not reproduce, so they have no need of a mate",
            "Plants need light to photosynthesise and are pollinated instead",
            "Light is a living resource, whereas a mate is a non-living "
            "resource",
            "Plants take in light through their roots rather than their leaves",
        ],
        "correct_index": 1,
        "why": "Light is the energy source for photosynthesis, so plants "
               "shade one another out, while their pollen is carried to other plants "
               "by wind or animals rather than by competing for a partner.",
    },
    {
        "id": "ks4-population-competition-s10",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A two-month drought kills about half the plants in a "
                "grassland, whether they were crowded or spaced out. Classify the "
                "factor and explain.",
        "options": [
            "Density-dependent, because more crowded plants dried out first",
            "Density-independent, because it hit the same share either way",
            "Density-dependent, because water is a resource plants compete for",
            "Density-independent, because a drought is caused by the weather",
        ],
        "correct_index": 1,
        "why": "A factor is density-independent when the proportion killed "
               "does not change with how crowded the population is, and that is what "
               "the observation shows.",
    },
    {
        "id": "ks4-population-competition-s11",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In theory a population could keep doubling. Explain why this "
                "does not happen in a real habitat.",
        "options": [
            "Organisms stop breeding once the numbers become very large",
            "Resources run short, so births fall and deaths rise",
            "Doubling is a mathematical idea that real populations cannot "
            "follow",
            "A population reaches the age at which it stops breeding",
        ],
        "correct_index": 1,
        "why": "Food, water and space are finite, so as numbers climb each "
               "individual gets less and the growth rate falls away to zero at the "
               "carrying capacity.",
    },
    {
        "id": "ks4-population-competition-s12",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two oak saplings grow one metre apart. Name the type of "
                "competition and the main resource involved.",
        "options": [
            "Interspecific competition, and the resource is soil minerals",
            "Interspecific competition, and the resource is light",
            "Intraspecific competition, and the resource is a mate",
            "Intraspecific competition, and the resource is light",
        ],
        "correct_index": 3,
        "why": "Both are the same species, so the competition is "
               "intraspecific, and two saplings side by side shade one another as "
               "they grow towards the light.",
    },
    {
        "id": "ks4-population-competition-s13",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pollutant kills young frogs but leaves the adults "
                "unharmed. Predict the effect on the frog population and explain.",
        "options": [
            "It falls, because too few young survive to replace the adults",
            "It rises, because the adults keep all the food for themselves",
            "It is unchanged, because the breeding adults are still alive",
            "It falls at once, because a population is counted by its young "
            "alone",
        ],
        "correct_index": 0,
        "why": "A population only stays level if losses are replaced, so "
               "removing the next generation makes numbers fall as the surviving "
               "adults die of old age.",
    },
    {
        "id": "ks4-population-competition-s14",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Half of a forest is felled. Explain the effect on the "
                "carrying capacity for a bird that nests in old trees.",
        "options": [
            "It rises, because the birds have more open space to fly through",
            "It stays the same, because the carrying capacity depends on the "
            "birds",
            "It falls, because fewer nest sites and less food are available",
            "It falls, because the felling frightens the birds away for a year",
        ],
        "correct_index": 2,
        "why": "Carrying capacity is set by the resources present, so "
               "removing half the habitat removes half the nest sites and feeding "
               "ground that supported the population.",
    },
    {
        "id": "ks4-population-competition-s15",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a predator does not usually hunt its prey to "
                "extinction.",
        "options": [
            "As prey become scarce the predators starve and their numbers fall",
            "Predators count their prey and stop hunting below a safe number",
            "Prey animals breed faster than a predator can ever catch them",
            "Predators switch to eating plants as soon as the prey run short",
        ],
        "correct_index": 0,
        "why": "The two populations are linked: fewer prey means less food, "
               "so the predator population declines and the hunting pressure eases "
               "before the prey is wiped out.",
    },
    {
        "id": "ks4-population-competition-s16",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pond's fish population rises and then settles at about "
                "250. Describe what is happening to its births and deaths.",
        "options": [
            "Births have fallen to zero, so deaths alone continue",
            "Births exceed deaths, but by a very small margin now",
            "The births and deaths are roughly equal to one another",
            "Deaths have stopped, and births continue at a low steady rate",
        ],
        "correct_index": 2,
        "why": "A population holds steady when the number added by birth "
               "matches the number lost by death, which is what happens at the "
               "carrying capacity.",
    },
    {
        "id": "ks4-population-competition-s17",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a severe frost is described as a "
                "density-independent factor.",
        "options": [
            "A frost happens in winter, and winter arrives each year",
            "A frost is caused by the weather, which no organism can control",
            "A frost kills more individuals when the population is very large",
            "The proportion killed does not depend on how crowded they are",
        ],
        "correct_index": 3,
        "why": "The cold acts on each individual regardless of its "
               "neighbours, so the same share of a dense population and a sparse one "
               "is lost.",
    },
    {
        "id": "ks4-population-competition-s18",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fishery lands 80% of the adult cod on a bank every year. "
                "Predict the effect on the cod population and explain.",
        "options": [
            "It falls, because too few adults are left to breed replacements",
            "It rises, because the remaining cod have far more food each",
            "It is unchanged, because cod produce millions of eggs each",
            "It falls, and then recovers within a year as the young cod mature",
        ],
        "correct_index": 0,
        "why": "Taking most of the breeding adults cuts the number of young "
               "produced, so the losses are no longer replaced and the stock "
               "declines year on year.",
    },
    {
        "id": "ks4-population-competition-s19",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the difference between a density-dependent and a "
                "density-independent factor.",
        "options": [
            "One becomes more limiting as the population becomes crowded",
            "One is caused by living things and one by the weather alone",
            "One acts on plants and the other on animal species",
            "One acts slowly over the years and the other acts within a week",
        ],
        "correct_index": 0,
        "why": "The distinction is whether the factor's effect strengthens as "
               "the population's density rises, as a food shortage or a disease "
               "does.",
    },
    {
        "id": "ks4-population-competition-s20",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A seabird colony nests so closely that the birds almost "
                "touch. Suggest one disadvantage of nesting this densely.",
        "options": [
            "The birds are unable to find their own nest among so many",
            "The colony as a whole is easier for a predator to detect",
            "Parasites and disease pass between the nests very easily",
            "The birds cannot take off because the nests are so crowded",
        ],
        "correct_index": 2,
        "why": "High density is exactly the condition in which a "
               "density-dependent factor bites, and close contact lets ticks, fleas "
               "and pathogens spread from nest to nest.",
    },
    {
        "id": "ks4-population-competition-s21",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two species needing exactly the same resources "
                "rarely survive together in one habitat.",
        "options": [
            "The better competitor takes the resource and excludes the other",
            "Two species cannot share one habitat under any condition",
            "The two species interbreed and become a single species in the end",
            "Both species starve, so neither of them survives in that habitat",
        ],
        "correct_index": 0,
        "why": "Interspecific competition for an identical requirement is won "
               "by whichever species is more efficient, and the loser is driven to "
               "local extinction.",
    },
    {
        "id": "ks4-population-competition-s22",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a territory is a resource worth the energy a "
                "robin spends defending it.",
        "options": [
            "It stops other species of bird from entering the garden",
            "It gives the robin somewhere to shelter from the cold weather",
            "It secures the food and nest site needed to raise young",
            "It makes the robin look larger to any predator watching it",
        ],
        "correct_index": 2,
        "why": "Holding a territory reserves the resources an individual "
               "needs to survive and breed, so the energy spent on defence buys a "
               "better chance of reproducing.",
    },
    {
        "id": "ks4-population-competition-s23",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A population of 200 mice has 40 births and 25 deaths in one "
                "year, with no mice entering or leaving. Calculate the population at "
                "the end of the year.",
        "options": [
            "165",
            "240",
            "265 mice",
            "215",
        ],
        "correct_index": 3,
        "why": "The population changes by births minus deaths: 200 + 40 - 25 "
               "= 215 mice.",
    },
    {
        "id": "ks4-population-competition-s24",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Japanese knotweed spreads along a riverbank and the native "
                "plants there disappear. Explain how the introduced plant did this.",
        "options": [
            "It released a gas into the air that the native plants cannot use",
            "It attracted herbivores that then ate all the native plants",
            "It raised the soil temperature above what the native plants stand",
            "It outcompeted them for light, water, minerals and space",
        ],
        "correct_index": 3,
        "why": "An invasive plant that grows faster and taller takes the "
               "resources first, and the species already there are left with too "
               "little to survive on.",
    },
    {
        "id": "ks4-population-competition-s25",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why space counts as a resource that plants compete "
                "for.",
        "options": [
            "Plants need empty space around them in order to respire freely",
            "A plant with space grows taller, and height is an advantage",
            "Space allows the wind to reach the plant and carry its pollen off",
            "Room to spread roots and leaves means more water and light",
        ],
        "correct_index": 3,
        "why": "Space is what lets a plant extend the root system and the "
               "leaf area it needs, so a crowded plant captures less water, fewer "
               "minerals and less light.",
    },
    {
        "id": "ks4-population-competition-s26",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a moorland, hare numbers and the numbers of the stoats "
                "that hunt them both rise and fall. State which population's change "
                "comes first.",
        "options": [
            "The stoats, because a predator controls its prey's numbers",
            "The hares, because the stoats respond to their food supply",
            "Both change at exactly the same moment as one another",
            "The stoats, because a predator breeds faster than its prey does",
        ],
        "correct_index": 1,
        "why": "The prey population changes first and the predator population "
               "follows it, because it takes time for the predators to breed in "
               "response to more food.",
    },
    # ── harder ────────────────────────────────────────────────────────────
    {
        "id": "ks4-population-competition-h05",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a valley, species A peaked in 2019 and again in 2029, "
                "while species B peaked in 2021 and again in 2031. Determine which is "
                "the predator and justify your answer.",
        "options": [
            "B, because its peaks come after those of the species it eats",
            "A, because a predator's numbers set the timing of the cycle",
            "A, because it peaked first and so must be the larger animal",
            "Neither, because a ten-year cycle is far too long to be real",
        ],
        "correct_index": 0,
        "why": "A predator's numbers respond to its food supply after a "
               "delay, so the population whose peaks come later in each cycle is the "
               "predator.",
    },
    {
        "id": "ks4-population-competition-h06",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pond X has an area of 20 m² and pond Y has an area of 200 "
                "m². Both are stocked with the same fish. Compare their carrying "
                "capacities and explain.",
        "options": [
            "Both are the same, because the species stocked is the same",
            "X's is higher, because the fish in it are closer to their food",
            "Y's is higher, because a larger pond is a deeper one",
            "Y's is higher, because it holds more food, space and oxygen",
        ],
        "correct_index": 3,
        "why": "Carrying capacity is set by the resources available, and a "
               "pond ten times the area supplies far more food, space and dissolved "
               "oxygen.",
    },
    {
        "id": "ks4-population-competition-h07",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement that a population sitting at its "
                "carrying capacity has stopped reproducing.",
        "options": [
            "It is sound, because a full habitat leaves no room for young",
            "It is unsound, because a population at capacity is still growing",
            "It is unsound: reproduction continues but is matched by deaths",
            "It is sound, because reproduction stops once the resources run "
            "short",
        ],
        "correct_index": 2,
        "why": "At the carrying capacity births and deaths are in balance, so "
               "individuals are still being born — they are simply replacing those "
               "that die.",
    },
    {
        "id": "ks4-population-competition-h08",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why removing a predator can eventually lower the "
                "prey population rather than raise it.",
        "options": [
            "The prey overgraze their food supply and then starve",
            "The prey lose the exercise that hunting pressure gave them",
            "The prey are unable to breed unless a predator is present",
            "The prey are then hunted harder by a different predator",
        ],
        "correct_index": 0,
        "why": "Unchecked growth carries the prey population past what the "
               "vegetation can supply, and destroying its own food source forces the "
               "numbers down again.",
    },
    {
        "id": "ks4-population-competition-h09",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bacterial culture in a sealed flask grows "
                "fast, levels off and then declines.",
        "options": [
            "Food runs down and waste builds up, so deaths overtake births",
            "The bacteria use up the flask's own glass and then have nowhere "
            "to live",
            "The bacteria mutate into a form that cannot divide any further",
            "The culture cools as it grows, and cold bacteria cannot divide",
        ],
        "correct_index": 0,
        "why": "A closed system has a fixed supply of nutrients and no way of "
               "removing waste, so growth first slows to the carrying capacity and "
               "then reverses.",
    },
    {
        "id": "ks4-population-competition-h10",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why competition between members of one species is "
                "what settles where a population levels off.",
        "options": [
            "They fight until the strongest individual alone is left",
            "They are the sole organisms present in any real habitat",
            "They breed with one another, so their numbers rise together",
            "They need identical resources, so each extra one takes a share",
        ],
        "correct_index": 3,
        "why": "Members of one species draw on exactly the same supply, so as "
               "numbers rise each individual's share falls until births and deaths "
               "balance.",
    },
    {
        "id": "ks4-population-competition-h11",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In sparse plots 5% of seedlings die and in crowded plots 40% "
                "die. Determine what this shows about the factor causing the deaths.",
        "options": [
            "It is density-dependent, since crowding raises the death rate",
            "It is density-independent, since some die in every plot",
            "It is density-dependent, since the sparse plots lost the fewest",
            "It is density-independent, since the two percentages are "
            "different",
        ],
        "correct_index": 0,
        "why": "The proportion dying rises eight-fold with density, which is "
               "exactly what defines a density-dependent factor.",
    },
    {
        "id": "ks4-population-competition-h12",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is abundant on one side of a wall and absent on the "
                "other, where the soil and light are the same. Suggest a competition "
                "explanation.",
        "options": [
            "The wall blocks the wind the plant needs",
            "A stronger competitor holds the ground on the other side",
            "Plants cannot spread across a wall",
            "The second side has no space left",
        ],
        "correct_index": 1,
        "why": "Where the abiotic conditions match, a biotic factor must be "
               "responsible, and a species already holding the resources can exclude "
               "a newcomer.",
    },
    {
        "id": "ks4-population-competition-h13",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A quota cuts this year's cod catch by a third. Explain how "
                "this can raise the total catch over the following ten years.",
        "options": [
            "Cod grow larger each year, so a delayed catch weighs more",
            "Fewer boats fishing means the cod are less frightened of nets",
            "More adults survive to breed, so the stock rebuilds itself",
            "The cod left behind eat the food the caught ones would have eaten",
        ],
        "correct_index": 2,
        "why": "Leaving more breeding adults raises the number of young "
               "produced, so the population recovers towards its carrying capacity "
               "and can sustain larger catches later.",
    },
    {
        "id": "ks4-population-competition-h14",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what a single hard frost does to a dense insect "
                "population and to a sparse one of the same species.",
        "options": [
            "It kills more of the dense one, as insects there are weaker",
            "It kills more of the sparse one, as they are more exposed",
            "It kills a similar proportion of each, as it ignores density",
            "It kills none of the dense one, as crowding keeps them warm",
        ],
        "correct_index": 2,
        "why": "A density-independent factor acts on each individual whatever "
               "its neighbours are doing, so the same share of both populations is "
               "lost.",
    },
    {
        "id": "ks4-population-competition-h15",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest how a population can rise above its habitat's "
                "carrying capacity for a short time.",
        "options": [
            "The carrying capacity rises with the population that lives there",
            "Numbers keep climbing before the shortage raises the death rate",
            "Extra individuals live without food until the supply improves",
            "A carrying capacity cannot be passed at any point",
        ],
        "correct_index": 1,
        "why": "The death rate responds after the resources run short rather "
               "than at the moment they do, so numbers can overshoot and then fall "
               "back.",
    },
    {
        "id": "ks4-population-competition-h16",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Trout in a lake fell after an unusually warm summer and "
                "again after a trout disease arrived. Determine which of the two was "
                "density-independent.",
        "options": [
            "The disease, because a pathogen acts on every individual equally",
            "The warm summer, because temperature ignores how crowded they are",
            "Both, because neither was caused by the trout themselves",
            "Neither, because both of them reduced the same trout population",
        ],
        "correct_index": 1,
        "why": "Temperature acts on each fish regardless of the population's "
               "density, while a disease spreads faster the more crowded the fish "
               "are, which makes it density-dependent.",
    },
    {
        "id": "ks4-population-competition-h17",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the build-up of waste products is a "
                "density-dependent factor.",
        "options": [
            "More individuals in a space produce waste faster than it clears",
            "Waste products appear once a population is very large",
            "Waste is a non-living substance, and those factors act on density",
            "Waste harms large organisms more than it harms small ones",
        ],
        "correct_index": 0,
        "why": "The rate at which waste accumulates depends on how many "
               "individuals are packed into the space, so its effect strengthens as "
               "density rises.",
    },
    {
        "id": "ks4-population-competition-h18",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the competition for light between a tall beech and a "
                "bluebell beneath it with that between two neighbouring beeches.",
        "options": [
            "Both are intraspecific: all three need light",
            "The first is intraspecific, the second not",
            "The first is interspecific and one-sided; the second is "
            "intraspecific",
            "Neither competes: the bluebell flowers first",
        ],
        "correct_index": 2,
        "why": "Different species competing is interspecific, and the beech "
               "wins outright by holding the canopy, while two beeches of the same "
               "species compete intraspecifically on more equal terms.",
    },
    {
        "id": "ks4-population-competition-h19",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a population of 20 individuals is at far greater "
                "risk from one severe winter than a population of 2000.",
        "options": [
            "Small populations feel the cold more keenly than large ones",
            "Large populations are able to move away from a bad winter",
            "Small populations breed more slowly than the large ones do",
            "Chance alone could remove all 20, but not all of the 2000",
        ],
        "correct_index": 3,
        "why": "A density-independent event kills a share of any population, "
               "and on a small one an unlucky share can take every individual, which "
               "ends the population entirely.",
    },
    {
        "id": "ks4-population-competition-h20",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the stronger competitor always "
                "excludes the weaker one.",
        "options": [
            "It is correct, because the weaker competitor cannot ever survive",
            "It is wrong, because competing species share a resource",
            "It is correct, because competition is settled by physical "
            "strength",
            "It depends on the conditions, which can favour either species",
        ],
        "correct_index": 3,
        "why": "Which species competes better depends on the abiotic "
               "conditions, so a change in temperature, pH or shade can reverse the "
               "outcome and let both persist.",
    },
    {
        "id": "ks4-population-competition-h21",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A population is counted each year as 50, 180, 330, 410, 420, "
                "418 and 421. Determine the carrying capacity of the habitat.",
        "options": [
            "About 50",
            "About 420",
            "About 330",
            "About 1000 individuals",
        ],
        "correct_index": 1,
        "why": "The numbers climb and then hold steady close to 420, and the "
               "level a population settles at is its habitat's carrying capacity.",
    },
    {
        "id": "ks4-population-competition-h22",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two warbler species eat the same insects but one feeds high "
                "in the canopy and the other near the ground. Suggest why both can "
                "survive in one wood.",
        "options": [
            "One species is stronger and tolerates the other",
            "They are not taking the same insects from the same place",
            "A wood has unlimited insects, so no competition",
            "The two interbreed, so they are one species",
        ],
        "correct_index": 1,
        "why": "Interspecific competition is only intense where two species "
               "draw on the same supply, and feeding at different heights means each "
               "takes a different share of it.",
    },
    {
        "id": "ks4-population-competition-h23",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a predator population cannot grow larger than "
                "its prey population will support.",
        "options": [
            "Predators stop breeding once their prey become hard to find",
            "Too little food raises the death rate until numbers fall back",
            "Prey animals learn to avoid a predator that is too numerous",
            "A predator is the larger animal, so fewer of them exist",
        ],
        "correct_index": 1,
        "why": "Food availability is a density-dependent limit on the "
               "predator, so once there is not enough prey to go round, deaths "
               "exceed births and the population falls back.",
    },
    {
        "id": "ks4-population-competition-h24",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pollutant in a river harms only fish in their first year. "
                "Suggest why the adult population still falls several years later.",
        "options": [
            "The pollutant becomes more toxic as the years go by",
            "Adults absorb the pollutant from the young that die",
            "The missing year classes reach adulthood in later years",
            "Adults move upstream, so fewer of them are counted each year",
        ],
        "correct_index": 2,
        "why": "The adults are the survivors of earlier years, so a "
               "generation lost as young shows up as a shortage of adults once that "
               "generation should have matured.",
    },
    {
        "id": "ks4-population-competition-h25",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the intensity of competition in a field of one wheat "
                "variety with that in a mixed meadow of thirty species.",
        "options": [
            "The meadow's is more intense, since thirty species need more",
            "Both are equally intense, since both fields are equally crowded",
            "The wheat field's is interspecific, since a crop is a single "
            "species",
            "The wheat field's is intraspecific and the more intense of the "
            "two",
        ],
        "correct_index": 3,
        "why": "Every wheat plant needs exactly the same resources at the "
               "same depth and height, so intraspecific competition is fiercer than "
               "competition between species with differing requirements.",
    },
    {
        "id": "ks4-population-competition-h26",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wood's hole-nesting birds are limited by a shortage of old "
                "trees. Determine which change would most raise their carrying "
                "capacity, and justify it.",
        "options": [
            "Putting up nest boxes, because nest sites are the limiting "
            "resource",
            "Feeding the birds, because more food means more birds",
            "Removing their predators, because predation limits every bird",
            "Planting young trees, because a wood needs more trees of any age",
        ],
        "correct_index": 0,
        "why": "A population is held at whichever resource runs out first, so "
               "supplying more of the scarce resource — nest holes — is what raises "
               "the ceiling.",
    },
]
