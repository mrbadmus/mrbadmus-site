"""Biology · Ecology — the MRB-338 expansion of `environmental-change`.

One leaf only: AQA 8461 §4.7.4, Biology-only and Higher tier. The original
twelve rows in `ecology__b.py` take the indicator species by definition,
rat-tailed maggots, monitoring by population and distribution, coral bleaching,
the oxygen crash after an algal bloom dies, oiled feathers, a moth running out
of mountain, a motorway splitting a wood, two emergence cues compared, three
river sites ranked, lichens read as water quality, and a planted corridor.

This file takes what they leave, and it deliberately steers away from the
indicator-species rows that `abiotic-biotic-factors` already carries. The
recall band finishes the framework the baseline never states: change is natural
OR anthropogenic, and an organism meeting it moves, adapts, dies out locally or
dies out altogether. The demand then falls on mechanism — why fragmentation
costs gene flow and not only area, why a warm-edge population contracts while a
cool-edge one expands, why an invasive species can empty a habitat that no
pollutant has touched, and what a monitoring programme has to measure before a
change can be called a change.

The weight is even at fourteen a band because this is a higher-tier spec point
with no shallow end: even the recall here is a definition a pupil has to apply.

⚠️ Coral bleaching, the mayfly/bloodworm/rat-tailed sequence and the
lichen-air-quality reading are all held by rows that already exist; where this
file touches those subjects it takes a different question about them.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # Natural against anthropogenic, the four outcomes, what monitoring
    # measures, and the named pollutants.
    {
        "id": "ks4-environmental-change-e05",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by an anthropogenic environmental change.",
        "options": [
            "A change that affects plants",
            "Any change reversing itself within a year",
            "A change caused by human activity",
            "A change that happens over a very long period of time",
        ],
        "correct_index": 2,
        "why": "Anthropogenic means caused by people — deforestation, "
               "agriculture, pollution, climate change and introduced species "
               "are the examples the specification names.",
    },
    {
        "id": "ks4-environmental-change-e06",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name one natural cause of environmental change.",
        "options": [
            "A volcanic eruption",
            "A new motorway",
            "An oil spill",
            "A drained wetland",
        ],
        "correct_index": 0,
        "why": "Volcanic eruptions, floods, droughts, ice ages and disease "
               "outbreaks all change conditions without any human involvement.",
    },
    {
        "id": "ks4-environmental-change-e07",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the three outcomes, other than adapting by natural "
                "selection, for an organism whose conditions change beyond "
                "what it can tolerate.",
        "options": [
            "It hibernates, it migrates, or it changes its species",
            "It grows larger, it breeds much faster, or it eats a "
                "different food",
            "It stops respiring, it stops growing, or it stops moving",
            "It moves, it dies out locally, or it becomes extinct",
        ],
        "correct_index": 3,
        "why": "An organism meeting intolerable conditions either shifts its "
               "range, adapts across generations, is lost from that place, or "
               "is lost everywhere.",
    },
    {
        "id": "ks4-environmental-change-e08",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by habitat fragmentation.",
        "options": [
            "A habitat is replaced entirely by buildings and by hard "
                "surfaces",
            "A continuous habitat is divided into separated smaller "
                "patches",
            "A habitat is made larger by joining it to the habitat lying "
                "just beside it",
            "A habitat loses its topsoil and becomes bare rock and gravel",
        ],
        "correct_index": 1,
        "why": "Fragmentation leaves the same habitat type in isolated pieces, "
               "which costs movement between populations as well as total "
               "area.",
    },
    {
        "id": "ks4-environmental-change-e09",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the gas from burning fossil fuels that causes acid rain "
                "and to which lichens are sensitive.",
        "options": [
            "Sulfur dioxide",
            "Carbon monoxide",
            "Helium",
            "Neon",
        ],
        "correct_index": 0,
        "why": "Sulfur dioxide released when fossil fuels burn dissolves in "
               "atmospheric water to give acid rain.",
    },
    {
        "id": "ks4-environmental-change-e10",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the ions whose run-off from farmland causes "
                "eutrophication.",
        "options": [
            "Chloride and sodium ions",
            "Copper and zinc ions",
            "Carbonate and sulfate ions",
            "Nitrate and phosphate ions",
        ],
        "correct_index": 3,
        "why": "Nitrate and phosphate are the plant nutrients in fertiliser, "
               "and it is their enrichment of the water that triggers an algal "
               "bloom.",
    },
    {
        "id": "ks4-environmental-change-e11",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by an invasive species.",
        "options": [
            "A species whose numbers fall sharply after it is introduced",
            "A species introduced to an area where it spreads and does "
                "harm",
            "A species that moves between two different habitats as the "
                "seasons change",
            "A species that has lived in an area for far longer than any "
                "other",
        ],
        "correct_index": 1,
        "why": "An invasive species establishes outside its natural range and "
               "outcompetes, eats or infects the species already there.",
    },
    {
        "id": "ks4-environmental-change-e12",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Give the term for the timing of a species' seasonal events, "
                "such as flowering, emerging or migrating.",
        "options": [
            "Distribution",
            "Adaptation",
            "Phenology",
            "Morphology",
        ],
        "correct_index": 2,
        "why": "Phenology is the calendar of a species' life — when it buds, "
               "flowers, emerges, migrates or breeds — and warming is shifting "
               "those dates earlier.",
    },
    {
        "id": "ks4-environmental-change-e13",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what happens to the coral animal's own food supply when "
                "it expels its symbiotic algae.",
        "options": [
            "It gains the food that the algae had been taking for "
                "themselves",
            "It switches to absorbing its minerals directly from the "
                "surrounding sea water",
            "It is unaffected, because the algae provided no food",
            "It loses the sugars the algae made for it and slowly starves",
        ],
        "correct_index": 3,
        "why": "The symbiotic algae supply most of the coral's nutrition, so a "
               "bleached coral is starving as well as colourless.",
    },
    {
        "id": "ks4-environmental-change-e14",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the two things a monitoring programme records to detect "
                "a change in a species.",
        "options": [
            "The temperature and the rainfall in the place where it lives",
            "Its population size and where it is found",
            "Its body mass and the colour of its young",
            "Its number of chromosomes and its life span",
        ],
        "correct_index": 1,
        "why": "Abundance and distribution are the two measures, and they can "
               "move independently, so both are needed.",
    },
    {
        "id": "ks4-environmental-change-e15",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the effect of nitrogen oxides from vehicle exhausts on "
                "the soils and rivers the rain carrying them reaches.",
        "options": [
            "They warm them, so cool-condition species are lost",
            "They make them alkaline, so the acid-loving species spread "
                "widely",
            "They acidify them, so acid-sensitive species are lost",
            "They have no effect, because the gases break down before the "
                "rain falls",
        ],
        "correct_index": 2,
        "why": "Nitrogen oxides dissolve in atmospheric water to give acid "
               "rain, which lowers the pH of soils and fresh water and removes "
               "the species that cannot tolerate it.",
    },
    {
        "id": "ks4-environmental-change-e16",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State one way in which plastic waste in the sea harms marine "
                "animals.",
        "options": [
            "Animals become entangled in it, or swallow it as if it were "
                "food",
            "It dissolves in the water and lowers the concentration of "
                "salt",
            "It floats on the surface and reflects the sunlight straight "
                "back out to space",
            "It reacts with sea water to produce a gas that the fish then "
                "breathe",
        ],
        "correct_index": 0,
        "why": "Entanglement and ingestion are the two direct routes; "
               "swallowed plastic fills the gut so the animal takes in less "
               "real food.",
    },
    {
        "id": "ks4-environmental-change-e17",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the coastal habitats most at risk from rising sea "
                "levels.",
        "options": [
            "Hedgerows, orchards and arable field margins inland",
            "Salt marshes, mangroves and coral atolls",
            "Chalk grassland, heathland and pine forest",
            "Upland bog, scree slopes and mountain tops",
        ],
        "correct_index": 1,
        "why": "These are the low-lying habitats that sit within the range of "
               "the rising water and have limited room to move inland.",
    },
    {
        "id": "ks4-environmental-change-e18",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what happens to a grassland region as its rainfall "
                "falls steadily over many decades.",
        "options": [
            "It becomes a wetland, because less rain means less drainage",
            "It is unaffected, because grasses do not depend on rainfall",
            "It can become desert as drought-prone conditions expand",
            "It becomes woodland, because trees need much less water than "
                "grass does",
        ],
        "correct_index": 2,
        "why": "Changed rainfall patterns expand drought-prone areas, and a "
               "grassland that loses its rain loses its plant cover with it.",
    },
    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # The mechanisms behind each change, applied to a named situation.
    {
        "id": "ks4-environmental-change-s05",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why habitat fragmentation reduces the genetic "
                "variation within a species.",
        "options": [
            "Fragmentation causes mutations in the individuals living "
                "nearest to the new edges",
            "Individuals in small patches stop reproducing sexually and "
                "reproduce asexually from then on",
            "Isolated patches cannot exchange individuals, so gene flow "
                "between them stops",
            "Each patch becomes colder than the continuous habitat was, "
                "which alters the genes",
        ],
        "correct_index": 2,
        "why": "Without movement between patches each population breeds only "
               "within itself, so alleles are lost by chance and cannot be "
               "replaced from outside.",
    },
    {
        "id": "ks4-environmental-change-s06",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a population at the warm edge of a species' range "
                "declines while one at the cool edge expands.",
        "options": [
            "The warm edge passes the species' upper tolerance; the cool "
                "edge becomes suitable",
            "The warm edge receives far more sunlight, and sunlight is "
                "what limits the population there",
            "The cool edge holds fewer predators, and predation is the "
                "factor that limits a range",
            "The warm edge has poorer soil, and soil quality changes as a "
                "climate warms up",
        ],
        "correct_index": 0,
        "why": "A range edge marks where conditions stop being tolerable, so "
               "warming pushes the warm edge outside tolerance and brings the "
               "cool edge inside it.",
    },
    {
        "id": "ks4-environmental-change-s07",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain how an introduced grey squirrel population can remove "
                "a native red squirrel population without killing any of them.",
        "options": [
            "It eats the red squirrels' young during the first week of "
                "each spring",
            "It changes the species of tree growing in the wood within a "
                "few seasons",
            "It makes the whole wood far colder, which the red squirrels "
                "are unable to tolerate",
            "It outcompetes them for food and carries a virus they cannot "
                "survive",
        ],
        "correct_index": 3,
        "why": "Competition for the same food and a disease the invader "
               "carries but tolerates are the two routes by which an invasive "
               "species displaces a native one.",
    },
    {
        "id": "ks4-environmental-change-s08",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Aluminium ions are washed into an upland stream once the "
                "surrounding soil has been acidified. Explain why trout in "
                "that stream then die.",
        "options": [
            "The ions dissolve the fish's scales, so water floods into the "
                "body",
            "The ions damage the gill surface, so the trout cannot take in "
                "enough oxygen",
            "The ions block the light, so the stream's plants stop growing",
            "The ions raise the temperature above what a trout can "
                "tolerate",
        ],
        "correct_index": 1,
        "why": "Acidification mobilises aluminium from catchment soils, and "
               "those ions damage and clog the gill surface so gas exchange "
               "fails.",
    },
    {
        "id": "ks4-environmental-change-s09",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A survey records a species in 46 grid squares in 1990 and in "
                "69 squares in 2020. Calculate the percentage increase in the "
                "number of squares occupied.",
        "options": [
            "50%",
            "23%",
            "33%",
            "67%",
        ],
        "correct_index": 0,
        "why": "The increase is 69 − 46 = 23 squares, and 23 ÷ 46 × 100 = 50%.",
    },
    {
        "id": "ks4-environmental-change-s10",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why an algal bloom blocks light from the plants "
                "rooted on a lake bed.",
        "options": [
            "The algae dissolve in the water and turn it opaque",
            "The algae settle on the lake bed and bury the rooted plants",
            "The algae absorb the water, so the lake becomes shallower",
            "The algae multiply at the surface and form a dense layer "
                "above them",
        ],
        "correct_index": 3,
        "why": "Nutrient enrichment lets surface algae multiply to a dense "
               "mat, and the plants beneath are shaded out before the bloom "
               "dies and the oxygen crashes.",
    },
    {
        "id": "ks4-environmental-change-s11",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a bird species that eats only one kind of prey is "
                "more vulnerable to environmental change than one that eats "
                "many.",
        "options": [
            "Eating one prey species means a bird breeds once in a life",
            "If that prey declines, the specialist has no alternative food",
            "Specialist bird species are smaller, and the smaller birds "
                "die out first",
            "A specialist bird is unable to fly to another feeding ground",
        ],
        "correct_index": 1,
        "why": "A generalist absorbs the loss of one prey species by "
               "switching; a specialist's population tracks a single food "
               "supply.",
    },
    {
        "id": "ks4-environmental-change-s12",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a pollutant that is not itself lethal can still "
                "remove a top predator from a food chain.",
        "options": [
            "It makes the prey species move away, and the predators follow "
                "their prey",
            "It changes the predator into a different species over a few "
                "generations of breeding",
            "It accumulates along the chain, so predators receive the "
                "greatest dose",
            "It reacts with the predator's food and turns that food into a "
                "poison",
        ],
        "correct_index": 2,
        "why": "A persistent pollutant is passed on with the biomass and "
               "concentrated at each transfer, so the highest trophic level "
               "carries the highest concentration.",
    },
    {
        "id": "ks4-environmental-change-s13",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a change recorded at a single site cannot on its "
                "own show that a species' distribution has shifted.",
        "options": [
            "A single site is measured with a different method each year",
            "Distribution must be measured from satellite images, not on "
                "the ground",
            "One site holds far too few individuals for any conclusion to "
                "be drawn from it",
            "One site can change for local reasons, so many sites are "
                "needed",
        ],
        "correct_index": 3,
        "why": "Local disturbance, management or chance can move a count at "
               "one place; a shift in distribution is a pattern across many "
               "sites.",
    },
    {
        "id": "ks4-environmental-change-s14",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why oil is described as harming seabirds in two "
                "separate ways.",
        "options": [
            "It stains the feathers dark, and it makes the bird a great "
                "deal easier for predators to see",
            "It destroys the feathers' insulation, and it is toxic when "
                "the bird preens",
            "It makes the bird heavier, and it lowers the salt content of "
                "the sea",
            "It blocks the bird's nostrils, and it reduces the oxygen in "
                "the water around it",
        ],
        "correct_index": 1,
        "why": "Matted feathers no longer trap air, so the bird loses heat; "
               "and preening to clean them takes the oil into the gut, where "
               "it is poisonous.",
    },
    {
        "id": "ks4-environmental-change-s15",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A stretch of water holds 8.4 mg per dm³ of dissolved oxygen "
                "upstream of a farm and 5.6 mg per dm³ downstream of it. "
                "Determine what fraction has been lost.",
        "options": [
            "Two thirds",
            "One quarter",
            "One third",
            "Two fifths",
        ],
        "correct_index": 2,
        "why": "The loss is 8.4 − 5.6 = 2.8 mg per dm³, and 2.8 ÷ 8.4 is one "
               "third of the original concentration.",
    },
    {
        "id": "ks4-environmental-change-s16",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a species can adapt to a slow environmental "
                "change but not to a fast one.",
        "options": [
            "Adaptation needs many generations of natural selection to act",
            "Fast changes are much larger in size than slow changes are in "
                "every case",
            "A species can adapt during the warmer half of each year",
            "Fast changes remove the habitat, while slow changes do not",
        ],
        "correct_index": 0,
        "why": "Natural selection works across generations, so a change faster "
               "than the species can breed leaves no time for advantageous "
               "alleles to spread.",
    },
    {
        "id": "ks4-environmental-change-s17",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a mangrove forest protects the coast behind it as "
                "well as holding its own species.",
        "options": [
            "It reflects the waves back out to sea without slowing them",
            "Its roots trap sediment and absorb wave energy before it "
                "reaches the shore",
            "It absorbs the salt from the sea water so the land stays "
                "fresh",
            "It raises the water temperature, which stops storms forming",
        ],
        "correct_index": 1,
        "why": "The dense root network dissipates wave energy and holds "
               "sediment, so losing mangrove to sea level rise costs the land "
               "behind it as well.",
    },
    {
        "id": "ks4-environmental-change-s18",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why an environmental change that removes one plant "
                "species can remove several animal species with it.",
        "options": [
            "Plants supply the oxygen, so one fewer species means less "
                "oxygen",
            "Removing a plant raises the temperature of the whole habitat "
                "sharply",
            "Animals that feed on or shelter in that plant lose their food "
                "and their home",
            "Every animal in a habitat depends on exactly the same plant "
                "species",
        ],
        "correct_index": 2,
        "why": "Specialist herbivores, their parasites and their predators are "
               "all tied to that plant, so its loss cascades up the food web.",
    },
    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Evidence weighed, mechanisms compared, and change judged over time.
    {
        "id": "ks4-environmental-change-h05",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A wood is split into four equal patches by roads. Explain why "
                "the risk of losing a species from the wood rises even though "
                "the total area is unchanged.",
        "options": [
            "Species in small patches stop breeding until the patches are "
                "rejoined again",
            "Splitting a wood lowers the temperature inside each of the "
                "four patches",
            "Four small populations each risk chance extinction, and none "
                "can be rescued from the others",
            "The roads take up area, so the total habitat has fallen by "
                "three quarters",
        ],
        "correct_index": 2,
        "why": "Small populations are lost to chance events that a large one "
               "absorbs, and with no movement between patches a local loss "
               "cannot be made good.",
    },
    {
        "id": "ks4-environmental-change-h06",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare a drought lasting one year with a permanent fall in "
                "mean rainfall, for a grassland community.",
        "options": [
            "A drought is survived from seed and root; a permanent fall "
                "replaces the community",
            "A drought does more damage, because it arrives without "
                "warning",
            "The two are identical, because both reduce the water for "
                "plants",
            "A permanent fall does less damage, because species grow used "
                "to it",
        ],
        "correct_index": 0,
        "why": "Grassland is adapted to occasional drought and recovers from "
               "the seed bank and root stock; a lasting change moves "
               "conditions outside the community's tolerance altogether.",
    },
    {
        "id": "ks4-environmental-change-h07",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A reef is bleached in one hot summer and the temperature then "
                "returns to normal. Predict what happens to the coral, and "
                "explain.",
        "options": [
            "It is certain to die, because bleaching destroys the entire "
                "coral skeleton beneath",
            "It regains its colour at once, because the algae did not "
                "leave it",
            "It becomes permanently white but is otherwise entirely "
                "unaffected",
            "It can regain its algae and recover if the bleaching was "
                "brief enough",
        ],
        "correct_index": 3,
        "why": "Bleaching is reversible while the coral animal is still alive; "
               "it is prolonged or repeated heat, giving no time to recover, "
               "that kills the reef.",
    },
    {
        "id": "ks4-environmental-change-h08",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Evaluate the use of an indicator species rather than a "
                "chemical test to assess a river's water quality.",
        "options": [
            "The species is cheaper, and it names the exact pollutant "
                "present in the water",
            "The species integrates conditions over weeks, while a test "
                "samples one instant",
            "The species is more accurate, because living organisms are "
                "not affected by chance events",
            "A chemical test is better, because it gives a number and the "
                "species does not",
        ],
        "correct_index": 1,
        "why": "A single chemical sample misses an intermittent discharge; the "
               "invertebrate community reflects everything the water has "
               "carried since it colonised.",
    },
    {
        "id": "ks4-environmental-change-h09",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A species' range edge has moved north 220 km in 55 years. "
                "Determine the mean rate, and state one reason the true rate "
                "may be higher.",
        "options": [
            "4 km per year; barriers may have delayed the shift in some "
                "places",
            "4 km per year; the species may have been counted twice in the "
                "same year",
            "0.25 km per year; recording effort has risen over the period",
            "12 100 km per year; the survey covered part of the range",
        ],
        "correct_index": 0,
        "why": "220 ÷ 55 = 4 km per year, and the climate may already be "
               "suitable further north than the species has managed to reach "
               "across a fragmented landscape.",
    },
    {
        "id": "ks4-environmental-change-h10",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a species introduced to an island often does more "
                "damage than the same species does on a continent.",
        "options": [
            "Islands are a great deal warmer than continents, so an "
                "introduced species grows faster",
            "An island has far more space, so an introduced species can "
                "spread further",
            "Island species reproduce more quickly, so the damage spreads "
                "sooner",
            "Island species evolved without it, so they have no defences "
                "against it",
        ],
        "correct_index": 3,
        "why": "Island communities have often evolved with no mammal predators "
               "or no grazing pressure, so an introduced rat or goat meets "
               "prey with no avoidance behaviour at all.",
    },
    {
        "id": "ks4-environmental-change-h11",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why removing the source of a pollutant does not "
                "always restore the community that was lost.",
        "options": [
            "Species that have been lost from a site become extinct "
                "worldwide at the very same time",
            "The pollutant may persist, and lost species need a route back "
                "to recolonise",
            "A community once lost cannot return to a site under any "
                "circumstances",
            "Removing a pollutant changes the temperature, which the "
                "species cannot tolerate",
        ],
        "correct_index": 1,
        "why": "Sediments and soils hold pollutants for years, and even in "
               "clean water a species returns only if a source population can "
               "reach the site.",
    },
    {
        "id": "ks4-environmental-change-h12",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare planting a hedgerow corridor with enlarging one of "
                "two isolated reserves by the same area.",
        "options": [
            "The corridor is worse, because a narrow strip holds no "
                "species of any kind",
            "The two are identical, because the same area of habitat is "
                "created either way",
            "The corridor restores gene flow between them; enlargement "
                "helps only one population",
            "Enlargement is better in every case, because a larger reserve "
                "will hold many more species",
        ],
        "correct_index": 2,
        "why": "Connectivity solves the problem fragmentation created; adding "
               "area to one site leaves the other isolated and both still "
               "unable to exchange individuals.",
    },
    {
        "id": "ks4-environmental-change-h13",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A lake's algal population rises from 400 to 9600 cells per "
                "cm³. Determine the factor by which it has increased.",
        "options": [
            "9200 times",
            "4 times",
            "2400 times",
            "24 times",
        ],
        "correct_index": 3,
        "why": "9600 ÷ 400 = 24, so the algal population is twenty-four times "
               "its original size.",
    },
    {
        "id": "ks4-environmental-change-h14",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Evaluate the claim that an environmental change is natural "
                "because similar changes have happened before in Earth's "
                "history.",
        "options": [
            "It is sound, because natural and human causes produce "
                "identical rates",
            "It is weak: the present rate is far faster than the past "
                "changes it is compared with",
            "It is sound: a change that happened before cannot have a "
                "human cause",
            "It is weak, because no environmental change has happened "
                "before",
        ],
        "correct_index": 1,
        "why": "Past climate has certainly changed, but over millennia; what "
               "makes the present change dangerous is the speed, which leaves "
               "no time for species to adapt or move.",
    },
    {
        "id": "ks4-environmental-change-h15",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Suggest why a long-running volunteer recording scheme can "
                "show a distribution shift that a short professional survey "
                "cannot.",
        "options": [
            "Volunteers may record species that professionals may not "
                "record",
            "A long scheme uses one observer, so there is no variation",
            "It covers decades and many sites, so a slow trend rises above "
                "yearly variation",
            "Volunteers count far more accurately than the professional "
                "surveyors do",
        ],
        "correct_index": 2,
        "why": "A shift of a few kilometres a year is invisible against "
               "year-to-year noise until the record is long enough and wide "
               "enough to average it out.",
    },
    {
        "id": "ks4-environmental-change-h16",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why controlling an invasive species is usually much "
                "harder once it is widespread than when it first arrives.",
        "options": [
            "A small founding population can be removed entirely; a spread "
                "one cannot",
            "An invasive species becomes resistant to every form of "
                "control within one generation",
            "A widespread species has changed into a native species by "
                "then",
            "Control is abandoned once a species is rare in a country",
        ],
        "correct_index": 0,
        "why": "Eradication needs every individual removed, which is possible "
               "at a single introduction site and effectively impossible once "
               "the species is established across a region.",
    },
    {
        "id": "ks4-environmental-change-h17",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Predict what happens to a salt marsh between a rising sea and "
                "a fixed flood wall, and explain the term for it.",
        "options": [
            "It becomes a freshwater marsh, because the wall excludes the "
                "salt",
            "It is squeezed into an ever-narrower strip and is eventually "
                "lost",
            "It moves inland over the top of the wall and re-establishes "
                "on the far side",
            "It grows upwards at the same rate as the sea and is "
                "unaffected",
        ],
        "correct_index": 1,
        "why": "Coastal squeeze: the marsh would normally migrate landwards as "
               "the sea rises, and a hard defence removes the ground it would "
               "migrate onto.",
    },
    {
        "id": "ks4-environmental-change-h18",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why two species responding to the same warming at "
                "different rates can cause one of them to decline.",
        "options": [
            "Species responding at different rates become different "
                "species",
            "The slower species is the larger one, and larger species die "
                "out first",
            "A predator, prey or pollination link is broken when the two "
                "separate in time or place",
            "The faster species uses up all the warmth, leaving none for "
                "the slower one",
        ],
        "correct_index": 2,
        "why": "Relationships depend on the partners overlapping; if a "
               "caterpillar peaks three weeks before the chicks hatch, or a "
               "plant flowers before its pollinator emerges, the dependent "
               "species fails.",
    },
]
