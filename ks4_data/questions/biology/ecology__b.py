"""Biology · Ecology (part B) — cycling, trophic levels, sampling and food production.

Eleven subtopics: the water cycle, decomposition and sampling techniques (BASE —
every class, so nothing higher-tier appears in stem or option), the trophic-level
and biomass-transfer chain (Triple only), environmental change (Triple, higher),
and the four food-production subtopics 4.7.5.1-4.

Distractors come from the brief's declared mistakes: transpiration confused with
evaporation, detritivores treated as decomposers, arrows read backwards, a numbers
pyramid assumed always pyramid-shaped, the 10% treated as the mass eaten rather
than the mass built into tissue, quadrat counts scaled by the wrong area, m and n2
swapped in the Lincoln index, lichens read as a water-quality indicator, and GM
treated as a synonym for selective breeding. The calculation subtopics
(transfer-of-biomass, sampling-techniques) take their distractors from the
arithmetic slip itself, never from noise.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── water-cycle ─────────────────────────────────────────────────────
    {
        "id": "ks4-water-cycle-e01",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a way that animals return water to the "
                "environment?",
        "options": [
            "Absorbing water vapour directly from the air through their skin",
            "Producing water as a product of photosynthesis in their cells",
            "Exhaling water vapour from their lungs when they breathe out",
            "Converting the water they drink into oxygen gas in their lungs",
        ],
        "correct_index": 2,
        "why": "Air breathed out is saturated with water vapour, so breathing "
               "returns water from an animal's body to the atmosphere.",
    },
    {
        "id": "ks4-water-cycle-e02",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why water is described as being continuously recycled "
                "rather than continuously produced.",
        "options": [
            "The total amount of water on Earth is fixed — it only moves "
            "between stores such as ocean and air",
            "Water is made by plants during photosynthesis at the same rate "
            "as it is used up by animals during respiration",
            "Water is destroyed each day by evaporation and replaced by an "
            "equal quantity formed during condensation",
            "New water reaches the Earth from space, exactly balancing the "
            "water that is lost into the deep oceans",
        ],
        "correct_index": 0,
        "why": "Earth holds a fixed quantity of water that is repeatedly moved "
               "between stores — none of it is created or destroyed.",
    },
    {
        "id": "ks4-water-cycle-e03",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the leaf structures through which water vapour is lost "
                "from a plant during transpiration.",
        "options": [
            "Root hair cells",
            "Xylem vessels",
            "Phloem sieve tubes",
            "Stomata",
        ],
        "correct_index": 3,
        "why": "Water vapour diffuses out of the leaf through the stomata — "
               "the pores in the epidermis.",
    },
    {
        "id": "ks4-water-cycle-e04",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Precipitation that soaks into the ground rather than flowing "
                "over the surface forms which store of water?",
        "options": [
            "Runoff",
            "Groundwater",
            "Water vapour",
            "Cloud droplets",
        ],
        "correct_index": 1,
        "why": "Water that infiltrates the soil and rock is stored as "
               "groundwater, which plant roots take up or which seeps slowly "
               "to rivers.",
    },
    {
        "id": "ks4-water-cycle-s01",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A city replaces a large area of grassland with roads and car "
                "parks. Explain the effect this has on the water cycle there.",
        "options": [
            "Less water evaporates from the city, so the air above it dries "
            "out and clouds stop forming over it",
            "Less water soaks into the ground, so surface runoff increases "
            "and the risk of flooding rises",
            "More water soaks into the ground, so groundwater levels rise and "
            "the local rivers begin to dry up",
            "Transpiration increases, because the warm hard surfaces heat the "
            "few remaining plants in the city",
        ],
        "correct_index": 1,
        "why": "Roads and buildings are impermeable, so rainfall cannot "
               "infiltrate and instead runs quickly off the surface into "
               "drains and rivers.",
    },
    {
        "id": "ks4-water-cycle-s02",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Farmers in a dry region pump large volumes of groundwater to "
                "irrigate crops. Suggest one consequence over many years.",
        "options": [
            "Rainfall over the region increases sharply, because far more "
            "water evaporates from the irrigated crops",
            "The groundwater is replaced immediately, because water vapour "
            "condenses back into the rock below the soil",
            "Precipitation over the region stops completely, because the "
            "clouds above it have no water left in them",
            "Underground water reserves are depleted, because water is "
            "removed faster than precipitation can refill them",
        ],
        "correct_index": 3,
        "why": "Groundwater is refilled only slowly by infiltrating "
               "precipitation, so extraction beyond that rate steadily empties "
               "the store.",
    },
    {
        "id": "ks4-water-cycle-s03",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why transpiration and evaporation are not the same "
                "process, even though both add water vapour to the air.",
        "options": [
            "Transpiration is vapour lost from leaves through stomata; "
            "evaporation is liquid water becoming vapour",
            "Transpiration happens only during the night, whereas evaporation "
            "happens only during the hours of daylight",
            "Transpiration adds liquid water droplets to the air, whereas "
            "evaporation adds water in the form of a vapour",
            "Transpiration is driven by the plant's respiration, whereas "
            "evaporation is driven by condensation in the clouds",
        ],
        "correct_index": 0,
        "why": "Transpiration is a biological loss of vapour through a leaf's "
               "stomata; evaporation is the physical change of liquid water to "
               "vapour from any wet surface.",
    },
    {
        "id": "ks4-water-cycle-s04",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Global warming raises the average temperature of the oceans. "
                "Explain the effect this has on the water cycle.",
        "options": [
            "Evaporation slows, because warmer water molecules are held more "
            "tightly at the surface of the ocean",
            "Condensation stops, because the atmosphere becomes too warm for "
            "any cloud droplets to form within it",
            "Evaporation increases, so more water enters the atmosphere and "
            "rainfall events become more intense",
            "Precipitation becomes evenly spread through the year across "
            "every part of the planet's surface",
        ],
        "correct_index": 2,
        "why": "Warmer oceans evaporate faster, so the atmosphere carries more "
               "water vapour and releases it in heavier downpours.",
    },
    {
        "id": "ks4-water-cycle-h01",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A river valley is dammed to create a large reservoir where "
                "there was farmland. Evaluate the effect on the water cycle.",
        "options": [
            "Evaporation from the area rises, because a large open water "
            "surface has replaced soil and growing crops",
            "Evaporation from the area falls, because still water evaporates "
            "more slowly than the moving water of a river",
            "Transpiration from the area rises, because the reservoir waters "
            "all of the trees growing around its edge",
            "Runoff into the reservoir stops, because the dam wall blocks "
            "precipitation from reaching the valley floor",
        ],
        "correct_index": 0,
        "why": "An open water surface exposes far more water directly to the "
               "sun than soil or a crop does, so evaporation from the area "
               "increases.",
    },
    {
        "id": "ks4-water-cycle-h02",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Deforestation increases the total amount "
                "of water on Earth, because the trees no longer hold any of "
                "it.' Identify the error in this reasoning.",
        "options": [
            "Trees hold no water at all, so cutting them down cannot change "
            "any part of the water cycle",
            "The total amount of water on Earth falls, because water is "
            "carried away inside the felled timber",
            "The total amount of water on Earth is fixed — deforestation "
            "changes how water is shared between stores",
            "The total amount rises, but only because bare soil receives more "
            "direct rainfall than a canopy does",
        ],
        "correct_index": 2,
        "why": "The water cycle moves a fixed quantity of water between "
               "stores; deforestation shifts the balance between them but "
               "creates no new water.",
    },
    {
        "id": "ks4-water-cycle-h03",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two neighbouring valleys receive the same rainfall. Valley A "
                "is wooded; valley B is bare compacted soil. After a storm, "
                "B's river rises much faster than A's. Explain why.",
        "options": [
            "The trees in A absorb the storm water and release it again as "
            "oxygen gas during photosynthesis",
            "Roots and leaf litter in A slow the water and help it soak in, "
            "so it reaches the river gradually",
            "The bare soil in B is warmer, so most of the rain evaporates "
            "again before it can reach the river",
            "The trees in A make the rain fall more slowly, so less water "
            "arrives in the valley during the storm",
        ],
        "correct_index": 1,
        "why": "Vegetation and its roots break the fall of rain and open up "
               "the soil, so infiltration is greater and runoff reaches the "
               "river far more slowly.",
    },
    {
        "id": "ks4-water-cycle-h04",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the fate of a raindrop falling on a steep rocky "
                "hillside with one falling on deep permeable soil.",
        "options": [
            "Both return to the atmosphere at once, because rock and soil are "
            "equally impermeable to water",
            "The hillside drop soaks in as groundwater; the soil drop runs "
            "straight off the surface into a stream",
            "Both drops take the same path, because gravity acts in the same "
            "way on all precipitation everywhere",
            "The hillside drop mostly runs off into a stream; the soil drop "
            "mostly infiltrates to become groundwater",
        ],
        "correct_index": 3,
        "why": "Infiltration depends on permeability — impermeable rock forces "
               "water to run off, while permeable soil lets it percolate down "
               "to the groundwater store.",
    },

    # ── decomposition ───────────────────────────────────────────────────
    {
        "id": "ks4-decomposition-e01",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bacteria and fungi digest dead material by secreting enzymes "
                "onto it and absorbing the products. Name this type of "
                "digestion.",
        "options": [
            "Intracellular digestion",
            "Extracellular digestion",
            "Egestion",
            "Excretion",
        ],
        "correct_index": 1,
        "why": "Decomposers release enzymes out of their cells onto the dead "
               "material and then absorb the soluble products — digestion "
               "outside the cell.",
    },
    {
        "id": "ks4-decomposition-e02",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which mineral ions decomposers return to the soil when "
                "they break down dead plants and animals.",
        "options": [
            "Chloride ions and hydrogen ions, which lower the pH of the soil",
            "Carbon dioxide and oxygen, which dissolve in the water in soil",
            "Glucose and starch, which plant roots then absorb directly",
            "Nitrates and phosphates, which plants absorb through their roots",
        ],
        "correct_index": 3,
        "why": "Decomposition releases the mineral ions locked in dead "
               "organisms — nitrates and phosphates — back into the soil for "
               "plants to reabsorb.",
    },
    {
        "id": "ks4-decomposition-e03",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Salting and sugaring preserve food. State how these methods "
                "slow decomposition.",
        "options": [
            "They draw water out of the food and out of decomposer cells by "
            "osmosis",
            "They kill every bacterium present in the food within a few "
            "minutes",
            "They remove all of the oxygen from around the surface of the "
            "food",
            "They raise the temperature of the food above its decomposers' "
            "optimum",
        ],
        "correct_index": 0,
        "why": "Water moves out of the decomposers by osmosis into the "
               "concentrated salt or sugar around them, so they dry out and "
               "cannot function.",
    },
    {
        "id": "ks4-decomposition-e04",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pickling food in vinegar slows decomposition. State the "
                "factor that the vinegar changes.",
        "options": [
            "The oxygen concentration around the food",
            "The temperature of the food in the jar",
            "The pH of the conditions around the food",
            "The surface area of the food in the jar",
        ],
        "correct_index": 2,
        "why": "Vinegar is acidic, and a pH far from the decomposers' optimum "
               "slows their enzymes down.",
    },
    {
        "id": "ks4-decomposition-s01",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bog bodies thousands of years old have been found almost "
                "intact in peat bogs. Explain why decomposition there has been "
                "so slow.",
        "options": [
            "Peat contains natural antibiotics that kill decomposer bacteria "
            "as soon as they touch it",
            "The bodies were frozen at the moment they were buried and have "
            "never thawed out since",
            "The bog is strongly acidic and waterlogged, so decomposer "
            "enzymes work extremely slowly",
            "Peat holds no nitrates or phosphates, so the decomposers have no "
            "food source available",
        ],
        "correct_index": 2,
        "why": "A very low pH inhibits decomposer enzymes and waterlogging "
               "removes the oxygen aerobic decomposers need, so breakdown "
               "almost stops.",
    },
    {
        "id": "ks4-decomposition-s02",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why earthworms in a compost heap increase the rate at "
                "which the material rots, even though they do not chemically "
                "digest it.",
        "options": [
            "They shred the material into smaller pieces, increasing the "
            "surface area available to decomposers",
            "They secrete enzymes onto the material that break down the "
            "cellulose in the plant cell walls",
            "They raise the temperature of the heap by respiring, which "
            "denatures the decomposers' enzymes",
            "They eat the bacteria and fungi, leaving more nutrients for the "
            "decomposers that are left",
        ],
        "correct_index": 0,
        "why": "Detritivores physically break dead material up, and the larger "
               "surface area lets decomposer enzymes act on far more of it at "
               "once.",
    },
    {
        "id": "ks4-decomposition-s03",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener's compost heap has begun to smell strongly and to "
                "rot very slowly after weeks of heavy rain. Suggest the "
                "reason.",
        "options": [
            "The heap has become too warm, so all of the decomposers' enzymes "
            "have now denatured",
            "The rain has washed out the nitrates, so the decomposers have no "
            "source of oxygen left",
            "The heap has become too dry for the decomposers to transport "
            "dissolved nutrients around",
            "The heap has become waterlogged and anaerobic, so aerobic "
            "decomposers cannot respire",
        ],
        "correct_index": 3,
        "why": "Water fills the air spaces in a soaked heap, and without "
               "oxygen the aerobic decomposers slow right down while anaerobic "
               "ones produce smelly gases.",
    },
    {
        "id": "ks4-decomposition-s04",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student investigating the effect of temperature on decay "
                "leaves milk samples at 5 °C, 20 °C and 35 °C. "
                "State one variable that must be kept the same.",
        "options": [
            "The time before the first reading, which should be longer at the "
            "higher temperatures",
            "The volume of milk placed in each of the three containers",
            "The temperature of the water bath that each container stands in",
            "The mass of bacteria added, which should be greater at the lower "
            "temperatures",
        ],
        "correct_index": 1,
        "why": "Only temperature may differ between the samples — volume, and "
               "every other variable, must be controlled or the comparison is "
               "not a fair test.",
    },
    {
        "id": "ks4-decomposition-h01",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The rate of decay of leaf litter rises steadily from "
                "5 °C to 40 °C, then falls sharply between "
                "40 °C and 60 °C. Explain this pattern.",
        "options": [
            "Decomposers stop reproducing above 40 °C, although their "
            "enzymes carry on working normally",
            "Above 40 °C the leaf litter breaks down chemically without "
            "any organisms being involved",
            "Rising temperature speeds enzymes up throughout, so the fall "
            "above 40 °C must be an anomaly",
            "Rising temperature speeds enzyme reactions up, but above about "
            "40 °C the enzymes denature",
        ],
        "correct_index": 3,
        "why": "Decomposition is enzyme-controlled, so it speeds up with "
               "temperature until the enzymes' active sites are denatured and "
               "the rate collapses.",
    },
    {
        "id": "ks4-decomposition-h02",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical bags of grass cuttings are left for a month. "
                "Bag A is sealed airtight; bag B is open and turned every few "
                "days. Compare the gases produced in the two bags.",
        "options": [
            "Bag A gives carbon dioxide and bag B gives methane, because "
            "sealing a bag supplies extra oxygen",
            "Bag B's aerobic decomposers release carbon dioxide; bag A turns "
            "anaerobic and methane is produced",
            "Both bags release carbon dioxide only, because decomposers "
            "always respire aerobically in a heap",
            "Neither bag releases any gas, because decomposers only ever "
            "release mineral ions into the soil",
        ],
        "correct_index": 1,
        "why": "Aerobic decomposers use oxygen and release carbon dioxide, but "
               "with no oxygen anaerobic organisms take over and methane is "
               "produced instead.",
    },
    {
        "id": "ks4-decomposition-h03",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a farmer who ploughs crop stubble into a field in "
                "autumn finds the soil's nitrate level higher the following "
                "spring.",
        "options": [
            "Ploughing forces nitrogen gas from the air into the soil, where "
            "it is stored as nitrate",
            "Cold winter soil converts plant protein into nitrate without any "
            "organisms being involved",
            "Decomposers break the buried plant material down over winter, "
            "releasing nitrates into the soil",
            "The stubble dissolves in rainwater, releasing the nitrate "
            "fertiliser it absorbed last summer",
        ],
        "correct_index": 2,
        "why": "The nitrogen in dead stubble stays locked in organic molecules "
               "until decomposers digest them and release it as soluble "
               "nitrate ions.",
    },
    {
        "id": "ks4-decomposition-h04",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'If all decomposers disappeared, plants "
                "would still grow normally, because they make their own food "
                "by photosynthesis.'",
        "options": [
            "Wrong — plants also need mineral ions, and without decomposers "
            "these stay locked in dead organisms",
            "Correct — plants make glucose from carbon dioxide and water, so "
            "they need nothing at all from soil",
            "Correct — plants absorb all the nitrate they need directly from "
            "the air through their stomata",
            "Wrong — plants would die because decomposers supply them with "
            "the oxygen they use in respiration",
        ],
        "correct_index": 0,
        "why": "Photosynthesis supplies carbohydrate, but proteins and DNA "
               "need nitrates and phosphates, and only decomposition returns "
               "those to the soil.",
    },

    # ── trophic-levels ──────────────────────────────────────────────────
    {
        "id": "ks4-trophic-levels-e01",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the food chain phytoplankton → zooplankton → herring → "
                "seal, state the trophic level of the herring.",
        "options": [
            "Trophic level 3 — a secondary consumer",
            "Trophic level 2 — a primary consumer",
            "Trophic level 4 — a tertiary consumer",
            "Trophic level 1 — a photosynthesising producer",
        ],
        "correct_index": 0,
        "why": "The herring eats zooplankton, which are the primary consumers "
               "at level 2, so the herring is a secondary consumer at "
               "level 3.",
    },
    {
        "id": "ks4-trophic-levels-e02",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what all organisms at trophic level 1 have in common.",
        "options": [
            "They are all eaten by more than one predator in the ecosystem",
            "They are all microscopic organisms living in soil or in water",
            "They all make their own food using energy transferred from the "
            "Sun",
            "They all break down dead material and release mineral ions",
        ],
        "correct_index": 2,
        "why": "Level 1 is the producers — plants and algae that "
               "photosynthesise — and every joule in the ecosystem enters "
               "through them.",
    },
    {
        "id": "ks4-trophic-levels-e03",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A great white shark is not eaten by any other organism in its "
                "ecosystem. State the term used for such an organism.",
        "options": [
            "A primary consumer",
            "An apex predator",
            "A producer",
            "A detritivore",
        ],
        "correct_index": 1,
        "why": "An apex predator sits at the top of its food chain and has no "
               "predator of its own within that ecosystem.",
    },
    {
        "id": "ks4-trophic-levels-e04",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the food chain wheat → aphid → ladybird → sparrow, "
                "identify the primary consumer.",
        "options": [
            "The sparrow",
            "The ladybird",
            "The wheat",
            "The aphid",
        ],
        "correct_index": 3,
        "why": "The primary consumer is the herbivore that eats the producer, "
               "and the aphid feeds directly on the wheat.",
    },
    {
        "id": "ks4-trophic-levels-s01",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A gardener sprays a crop with insecticide, killing all the "
                "aphids. Explain, using trophic levels, why the number of "
                "ladybirds in the garden then falls.",
        "options": [
            "The ladybirds move up a trophic level and start feeding on the "
            "crop plants themselves",
            "The insecticide raises the ladybirds to a higher level, so less "
            "energy now reaches them",
            "Ladybirds are producers, so anything sprayed onto a crop plant "
            "affects them directly",
            "Ladybirds are at level 3 and take all their biomass from level "
            "2, which has been removed",
        ],
        "correct_index": 3,
        "why": "Ladybirds are secondary consumers that depend entirely on "
               "level 2 for biomass, so removing the primary consumers removes "
               "their food supply.",
    },
    {
        "id": "ks4-trophic-levels-s02",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the trophic level or levels occupied by a person eating "
                "a meal of bread, cheese and beef.",
        "options": [
            "Level 1 only, because the meal originally began as wheat and "
            "grass grown in a field",
            "Levels 2 and 3 — bread comes from a producer, and cheese and "
            "beef from a herbivore",
            "Level 4 only, because humans are the apex predator in every food "
            "chain that they belong to",
            "No level at all, because humans are omnivores and omnivores sit "
            "outside all food chains",
        ],
        "correct_index": 1,
        "why": "Trophic level describes what is being eaten — eating a plant "
               "makes you a primary consumer, eating a herbivore makes you a "
               "secondary consumer.",
    },
    {
        "id": "ks4-trophic-levels-s03",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why decomposers are usually drawn to one side of a "
                "food chain rather than being given a trophic level number.",
        "options": [
            "They are microscopic, so they contribute almost no biomass to "
            "the ecosystem as a whole",
            "They feed only on producers, so numbering them would simply "
            "duplicate trophic level 2",
            "They obtain biomass from the dead remains and wastes of every "
            "trophic level at once",
            "They release energy back to the Sun, so they sit outside the "
            "flow of energy altogether",
        ],
        "correct_index": 2,
        "why": "Decomposers draw on dead material from all levels "
               "simultaneously, so no single position in the chain describes "
               "them.",
    },
    {
        "id": "ks4-trophic-levels-s04",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Grasses in a grassland capture 8500 kJ/m²/year. Grasshoppers "
                "eat the grass and birds eat the grasshoppers. Predict roughly "
                "how much energy reaches the birds.",
        "options": [
            "About 85 kJ/m²/year",
            "About 850 kJ/m²/year",
            "About 8.5 kJ/m²/year",
            "About 4250 kJ/m²/year",
        ],
        "correct_index": 0,
        "why": "About a tenth passes on at each transfer: 8500 → 850 kJ in "
               "the grasshoppers → 85 kJ in the birds that eat them.",
    },
    {
        "id": "ks4-trophic-levels-h01",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Phytoplankton are eaten by copepods, copepods by sand eels, "
                "sand eels by mackerel and mackerel by tuna. Determine the "
                "tuna's trophic level and the number of feeding transfers "
                "below it.",
        "options": [
            "Level 4, with three feeding transfers below it",
            "Level 5, with five feeding transfers below it",
            "Level 5, with four feeding transfers below it",
            "Level 4, with four feeding transfers below it",
        ],
        "correct_index": 2,
        "why": "Phytoplankton are level 1 and each consumer adds one level, "
               "placing tuna at level 5 with four feeding steps between it and "
               "the producers.",
    },
    {
        "id": "ks4-trophic-levels-h02",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student states that a fox is 'always a tertiary consumer'. "
                "Evaluate this statement.",
        "options": [
            "Wrong — a fox eating a rabbit is a secondary consumer, but a fox "
            "eating a stoat is a tertiary consumer",
            "Correct — trophic level is a fixed property of a species, set by "
            "its body size and by its diet",
            "Wrong — a fox is always a secondary consumer, because it is a "
            "mammal that eats other mammals",
            "Correct — every carnivore is a tertiary consumer and every "
            "herbivore is a primary consumer",
        ],
        "correct_index": 0,
        "why": "Trophic level describes a feeding relationship, not a species, "
               "so an animal eating at different levels occupies different "
               "levels in different chains.",
    },
    {
        "id": "ks4-trophic-levels-h03",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two chains start from the same 12 000 kJ/m²/year captured by "
                "producers. Chain A is producer → herbivore → human; chain B "
                "is producer → human. Compare the energy reaching the human.",
        "options": [
            "Chain A supplies about 1200 kJ/m²/year and chain B about "
            "120 kJ/m²/year",
            "Both chains supply about 1200 kJ/m²/year, because the producers "
            "are identical",
            "Chain A supplies about 6000 kJ/m²/year and chain B about "
            "12 000 kJ/m²/year",
            "Chain A supplies about 120 kJ/m²/year and chain B about "
            "1200 kJ/m²/year",
        ],
        "correct_index": 3,
        "why": "Each transfer passes on roughly a tenth, so the extra step in "
               "chain A costs a further 90% and leaves ten times less energy "
               "for the human.",
    },
    {
        "id": "ks4-trophic-levels-h04",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a food web is a more useful model of an ecosystem "
                "than a single food chain, referring to trophic levels.",
        "options": [
            "A web gives the exact number of organisms at each trophic level, "
            "which a chain cannot show",
            "Most organisms feed at more than one trophic level, and a web "
            "shows all those links at once",
            "A web includes the decomposers, which are never shown anywhere "
            "on a food chain diagram",
            "A web shows energy flowing in both directions, whereas a chain "
            "shows only one direction",
        ],
        "correct_index": 1,
        "why": "Real organisms have several food sources and several "
               "predators, so only an interconnected web captures the feeding "
               "relationships a single chain leaves out.",
    },

    # ── pyramids-of-biomass ─────────────────────────────────────────────
    {
        "id": "ks4-pyramids-of-biomass-e01",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what must be measured in order to build a pyramid of "
                "biomass for a food chain.",
        "options": [
            "The number of individual organisms found at each trophic level",
            "The volume of space occupied by the organisms at each level",
            "The energy released by burning one organism from each level",
            "The total mass of living material at each level in a given area",
        ],
        "correct_index": 3,
        "why": "A pyramid of biomass compares the total mass of living "
               "material at each level, measured per unit area of ground.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e02",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a grassland the biomass is: grass 900 g/m², rabbits "
                "90 g/m², foxes 9 g/m². Describe the shape of the pyramid of "
                "biomass.",
        "options": [
            "Inverted — the narrowest bar of the three is at the bottom",
            "A true pyramid — each bar is narrower than the one below it",
            "A rectangle — all three of the bars are the same width",
            "An hourglass — the middle bar is the narrowest of the three",
        ],
        "correct_index": 1,
        "why": "Biomass falls at every level here, so each bar is narrower "
               "than the one beneath it and the diagram is a true pyramid.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e03",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of numbers is narrow at the bottom and much wider "
                "at the level above. Identify the kind of producer this "
                "suggests.",
        "options": [
            "A large number of tiny algae floating in a pond",
            "A dense carpet of moss across a woodland floor",
            "A single large tree supporting many small herbivores",
            "A field of grass grazed by a small herd of cattle",
        ],
        "correct_index": 2,
        "why": "A numbers pyramid counts individuals, so one huge producer "
               "supporting hundreds of small consumers gives a narrow bottom "
               "bar.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e04",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of biomass is drawn without the scale being stated. "
                "Explain why this is a problem.",
        "options": [
            "The reader cannot work out what biomass each bar width stands "
            "for",
            "The bars will not be centred on one another in the correct way",
            "The producers can no longer be identified as trophic level 1",
            "The whole pyramid will end up being drawn upside down instead",
        ],
        "correct_index": 0,
        "why": "The widths only carry meaning once the reader knows how many "
               "grams per square metre one centimetre represents.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s01",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A food chain runs: one rose bush → 2000 greenfly → 40 "
                "ladybirds. Compare the pyramid of numbers with the pyramid of "
                "biomass for this chain.",
        "options": [
            "Numbers is inverted at the base; biomass is a true pyramid, "
            "because the bush outweighs the greenfly",
            "Both are inverted at the base, because there is only a single "
            "producer organism in the chain",
            "Numbers is a true pyramid; biomass is inverted, because 2000 "
            "greenfly weigh more than one bush",
            "Both are true pyramids, because producers are always placed at "
            "the bottom of any pyramid",
        ],
        "correct_index": 0,
        "why": "Counting individuals gives a base of one plant, but the bush's "
               "mass far exceeds the combined mass of the greenfly, so the "
               "biomass pyramid is a proper pyramid.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s02",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A food chain is: grass → 30 sheep → 60 000 ticks feeding on "
                "the sheep. Describe the pyramid of numbers and the pyramid of "
                "biomass for this chain.",
        "options": [
            "Both are true pyramids, because grass is the producer at the "
            "bottom of each of them",
            "Numbers is a true pyramid; biomass is inverted, because the "
            "ticks outnumber the sheep",
            "Numbers is inverted at the top; biomass is a true pyramid, "
            "because the sheep outweigh the ticks",
            "Numbers is inverted at the base; biomass is inverted at the top "
            "for exactly the same reason",
        ],
        "correct_index": 2,
        "why": "Parasites are far more numerous than their hosts, so the top "
               "bar of the numbers pyramid is widest, but their combined mass "
               "is tiny so the biomass pyramid is normal.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s03",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student draws a pyramid of biomass with foxes at the "
                "bottom, then rabbits, then grass at the top. Identify the "
                "error.",
        "options": [
            "The bars should all be drawn the same width unless a scale is "
            "stated alongside them",
            "Producers must be at the bottom — the whole diagram has been "
            "drawn upside down",
            "Foxes and rabbits should be combined together into a single "
            "consumer bar",
            "A pyramid of biomass should only ever show two of the trophic "
            "levels at a time",
        ],
        "correct_index": 1,
        "why": "Trophic level 1 is always the base of the pyramid, because all "
               "the ecosystem's biomass originates with the producers.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s04",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why biomass is recorded per square metre rather than "
                "as a total mass for the whole habitat.",
        "options": [
            "Because organisms are always spread perfectly evenly across "
            "every habitat that is studied",
            "Because a total mass would be far too large for students to "
            "measure in a school laboratory",
            "Because a total mass would include the mass of the water held "
            "inside each of the organisms",
            "Because it lets the levels — and different habitats — be "
            "compared with one another fairly",
        ],
        "correct_index": 3,
        "why": "Expressing biomass per unit area removes the effect of habitat "
               "size, so bars and whole ecosystems can be compared on the same "
               "footing.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h01",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a meadow, producers hold 3200 g/m², primary consumers "
                "260 g/m² and secondary consumers 22 g/m². Calculate the total "
                "biomass lost between trophic level 1 and trophic level 3.",
        "options": [
            "238 g/m²",
            "3178 g/m²",
            "2940 g/m²",
            "282 g/m²",
        ],
        "correct_index": 1,
        "why": "Of the 3200 g/m² present at level 1, only 22 g/m² remains at "
               "level 3, so 3200 − 22 = 3178 g/m² has been lost on the way.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h02",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two pyramids of biomass are drawn for the same field, one in "
                "June and one in December. The producer bar is much narrower "
                "in December. Suggest why.",
        "options": [
            "The scale chosen for the December pyramid must have been drawn "
            "incorrectly by the student",
            "Decomposers have moved into trophic level 1 and taken the place "
            "of the producers there",
            "The area of the field shrinks in winter, so the biomass per "
            "square metre falls with it",
            "Less light and lower temperatures reduce photosynthesis, so less "
            "plant biomass is present",
        ],
        "correct_index": 3,
        "why": "A pyramid of biomass is a snapshot in time, and in winter the "
               "producers hold far less living material because photosynthesis "
               "has slowed.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h03",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate this statement: 'A pyramid of numbers can never be a "
                "true pyramid, so it should never be used.'",
        "options": [
            "Wrong — numbers pyramids are often true pyramids, and counting "
            "individuals is quick to do",
            "Correct — a numbers pyramid is always inverted, so it can carry "
            "no useful information",
            "Correct — only biomass pyramids can be drawn to a scale, so only "
            "biomass pyramids are valid",
            "Wrong — numbers pyramids are always true pyramids, and biomass "
            "pyramids are the unreliable ones",
        ],
        "correct_index": 0,
        "why": "A numbers pyramid is a true pyramid whenever the organisms at "
               "each level are of similar size, and counting is far quicker "
               "than measuring mass.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h04",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "To find the biomass of a trophic level, samples are dried in "
                "an oven until their mass stops changing. Explain why dry mass "
                "is used rather than fresh mass.",
        "options": [
            "Drying kills the organisms, and an organism must be dead before "
            "its mass can be measured",
            "Drying concentrates the minerals present, which gives a larger "
            "and more precise reading",
            "Water content varies a great deal, so dry mass compares the "
            "living material more fairly",
            "Fresh organisms carry on respiring while being weighed, which "
            "steadily reduces their mass",
        ],
        "correct_index": 2,
        "why": "Water makes up a variable fraction of an organism, so only the "
               "dry mass gives a comparable measure of the biological material "
               "actually present.",
    },

    # ── transfer-of-biomass ─────────────────────────────────────────────
    {
        "id": "ks4-transfer-of-biomass-e01",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a meadow the producers hold 6300 g/m² of biomass, and 10% "
                "of this is transferred to the primary consumers. Calculate "
                "the biomass of the primary consumers.",
        "options": [
            "63 g/m²",
            "5670 g/m²",
            "630 g/m²",
            "63 000 g/m²",
        ],
        "correct_index": 2,
        "why": "10% of 6300 g/m² is 6300 ÷ 10 = 630 g/m² built into the "
               "primary consumers' own biomass.",
    },
    {
        "id": "ks4-transfer-of-biomass-e02",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A cow eats 100 kg of grass. State what happens to most of "
                "this biomass.",
        "options": [
            "All of it is built into the cow's own body mass as new tissue",
            "Most is lost in respiration, faeces and urine; a little becomes "
            "cow biomass",
            "Most is stored inside the cow's stomach until the cow is eaten "
            "by a predator",
            "Most is converted directly into the milk that the cow produces "
            "each day",
        ],
        "correct_index": 1,
        "why": "Only the biomass built into the cow's own tissues passes on — "
               "the rest is respired away as heat or leaves as faeces and "
               "urine.",
    },
    {
        "id": "ks4-transfer-of-biomass-e03",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by egestion.",
        "options": [
            "The removal of indigestible material from the gut as faeces",
            "The removal of the waste products of metabolism, such as urea",
            "The release of energy from glucose inside every living cell",
            "The absorption of digested food molecules into the blood",
        ],
        "correct_index": 0,
        "why": "Egestion is the loss of food that was never absorbed — "
               "indigestible material such as cellulose and bone, passed out "
               "as faeces.",
    },
    {
        "id": "ks4-transfer-of-biomass-e04",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which process accounts for the largest share of the "
                "biomass lost at a trophic level.",
        "options": [
            "Egestion of the undigested food material that leaves the gut as "
            "faeces",
            "Excretion of urea dissolved in the urine",
            "Evaporation of water from the body surface",
            "Respiration, which releases energy as heat to the surroundings",
        ],
        "correct_index": 3,
        "why": "Around 60–70% of the biomass taken in is used in respiration "
               "and lost as heat, far more than is lost in faeces or urine.",
    },
    {
        "id": "ks4-transfer-of-biomass-s01",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pond holds algae at 80 000 kJ/m²/year, small fish at "
                "6000 kJ/m²/year and pike at 480 kJ/m²/year. Calculate the "
                "efficiency of transfer from the small fish to the pike.",
        "options": [
            "0.6%",
            "8.0%",
            "7.5%",
            "92.0%",
        ],
        "correct_index": 1,
        "why": "Efficiency = (480 ÷ 6000) × 100 = 8.0%, using the two levels "
               "either side of the transfer being asked about.",
    },
    {
        "id": "ks4-transfer-of-biomass-s02",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A beef herd eats 24 000 kg of grass in a year and gains "
                "1800 kg of body mass. Calculate the percentage of the grass "
                "biomass that is NOT transferred into the cattle.",
        "options": [
            "92.5%",
            "7.5%",
            "13.3%",
            "0.925%",
        ],
        "correct_index": 0,
        "why": "(1800 ÷ 24 000) × 100 = 7.5% is transferred, so 100 − 7.5 = "
               "92.5% is lost in respiration, faeces and urine.",
    },
    {
        "id": "ks4-transfer-of-biomass-s03",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an endothermic (warm-blooded) animal transfers a "
                "smaller percentage of its food into biomass than an "
                "ectothermic animal of the same size.",
        "options": [
            "Endotherms egest a far larger share of their food as faeces than "
            "ectotherms of the same size do",
            "Endotherms excrete far more urea, because they eat a much higher "
            "protein diet than ectotherms",
            "Ectotherms do not respire at all, so none of their biomass is "
            "ever lost from the food chain",
            "Endotherms respire more to keep their body temperature constant, "
            "losing more energy as heat",
        ],
        "correct_index": 3,
        "why": "Holding a constant body temperature costs energy that is "
               "released as heat, so less of the food eaten is left over to "
               "build new biomass.",
    },
    {
        "id": "ks4-transfer-of-biomass-s04",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "On a fish farm 500 kg of feed produces 160 kg of extra fish. "
                "On a chicken farm 500 kg of feed produces 90 kg of extra "
                "chicken. Compare the efficiency of the two systems.",
        "options": [
            "The chicken farm is more efficient, at 18% against the fish "
            "farm's 32%",
            "Both are equally efficient, because both of them used 500 kg of "
            "feed",
            "The fish farm is more efficient, at 32% against the chicken "
            "farm's 18%",
            "The fish farm is more efficient, at 3.2% against the chicken "
            "farm's 1.8%",
        ],
        "correct_index": 2,
        "why": "(160 ÷ 500) × 100 = 32% for the fish and (90 ÷ 500) × 100 = "
               "18% for the chickens — fish spend no energy keeping warm or "
               "supporting their own weight.",
    },
    {
        "id": "ks4-transfer-of-biomass-h01",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hectare yields 6000 kg of wheat. A farmer can sell it as "
                "food or feed it to pigs, which transfer 12% of it into meat. "
                "Calculate how much more food biomass the wheat supplies.",
        "options": [
            "720 kg",
            "6720 kg",
            "500 kg",
            "5280 kg",
        ],
        "correct_index": 3,
        "why": "The pigs convert only 12% of the 6000 kg into meat — 720 kg — "
               "so eating the wheat directly supplies 6000 − 720 = 5280 kg "
               "more.",
    },
    {
        "id": "ks4-transfer-of-biomass-h02",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A food chain begins with producers at 45 000 kJ/m²/year and "
                "transfers 10% at each step. Calculate the energy reaching a "
                "tertiary consumer at trophic level 4.",
        "options": [
            "4500 kJ/m²/year",
            "450 kJ/m²/year",
            "45 kJ/m²/year",
            "4.5 kJ/m²/year",
        ],
        "correct_index": 2,
        "why": "Three transfers at 10% each: 45 000 → 4500 → 450 → "
               "45 kJ/m²/year at level 4.",
    },
    {
        "id": "ks4-transfer-of-biomass-h03",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student calculates the efficiency of a biomass transfer as "
                "140% and writes it down without comment. Explain what this "
                "value tells you.",
        "options": [
            "Nothing unusual — an efficiency above 100% is common near the "
            "base of a food chain",
            "There is an error, because a level cannot hold more biomass than "
            "the level supplying it",
            "The transfer is unusually good, so this ecosystem must be an "
            "exceptionally productive one",
            "The student measured energy rather than biomass, and energy "
            "transfers can exceed 100%",
        ],
        "correct_index": 1,
        "why": "Biomass is always lost in respiration, egestion and excretion, "
               "so a value above 100% means the fraction has been divided the "
               "wrong way round.",
    },
    {
        "id": "ks4-transfer-of-biomass-h04",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pig eats 800 g of feed. Of this, 120 g leaves as faeces, "
                "60 g is lost in urine and 550 g is used in respiration. "
                "Calculate the percentage of the feed that becomes pig "
                "biomass.",
        "options": [
            "8.75%",
            "15.0%",
            "68.8%",
            "91.3%",
        ],
        "correct_index": 0,
        "why": "Only 800 − 120 − 60 − 550 = 70 g is built into the pig, and "
               "(70 ÷ 800) × 100 = 8.75%.",
    },

    # ── sampling-techniques ─────────────────────────────────────────────
    {
        "id": "ks4-sampling-techniques-e01",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the piece of equipment used to mark out a known sample "
                "area of ground when counting plants.",
        "options": [
            "A transect line",
            "A quadrat",
            "A pooter",
            "A measuring cylinder",
        ],
        "correct_index": 1,
        "why": "A quadrat is a square frame of known area, so the organisms "
               "counted inside it can be scaled up to the whole habitat.",
    },
    {
        "id": "ks4-sampling-techniques-e02",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A quadrat measures 0.5 m by 0.5 m. Calculate its area.",
        "options": [
            "1.00 m²",
            "0.50 m²",
            "0.25 m²",
            "2.00 m²",
        ],
        "correct_index": 2,
        "why": "Area = 0.5 m × 0.5 m = 0.25 m².",
    },
    {
        "id": "ks4-sampling-techniques-e03",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a quadrat cannot be used to estimate the population "
                "of grasshoppers in a meadow.",
        "options": [
            "Grasshoppers are too small to be seen inside a quadrat frame",
            "Grasshoppers live below the soil, where a quadrat cannot reach",
            "Quadrats can only be used on rocky shores, never in a meadow",
            "Grasshoppers move quickly and jump out before being counted",
        ],
        "correct_index": 3,
        "why": "Quadrats only work for organisms that stay put — a mobile "
               "animal escapes the frame, so mark–recapture is used instead.",
    },
    {
        "id": "ks4-sampling-techniques-e04",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the mark–recapture equation N = (n₁ × n₂) ÷ m, state what "
                "m represents.",
        "options": [
            "The number of marked individuals found in the second sample",
            "The total number of individuals caught in the second sample",
            "The number of individuals caught and marked in the first sample",
            "The estimated size of the whole population being studied",
        ],
        "correct_index": 0,
        "why": "m is the marked recaptures, and the fraction m ÷ n₂ tells you "
               "what proportion of the whole population had been marked.",
    },
    {
        "id": "ks4-sampling-techniques-s01",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student places 12 quadrats, each 0.25 m², at random on a "
                "lawn of area 300 m². The mean number of daisy plants per "
                "quadrat is 7. Estimate the daisy population of the lawn.",
        "options": [
            "8400",
            "2100",
            "84",
            "525",
        ],
        "correct_index": 0,
        "why": "Estimated population = mean per quadrat × (total area ÷ "
               "quadrat area) = 7 × (300 ÷ 0.25) = 8400.",
    },
    {
        "id": "ks4-sampling-techniques-s02",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "60 snails are marked and released. In a second sample of 45 "
                "snails, one in every five is marked. Estimate the population "
                "size.",
        "options": [
            "24 300",
            "60",
            "12",
            "300",
        ],
        "correct_index": 3,
        "why": "One in five of 45 is 9 marked recaptures, so N = (60 × 45) ÷ 9 "
               "= 300.",
    },
    {
        "id": "ks4-sampling-techniques-s03",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a student takes 15 quadrat readings in a field "
                "rather than only two.",
        "options": [
            "Two quadrats would take longer to place accurately than fifteen "
            "quadrats would",
            "The more quadrats are used, the larger the final estimated "
            "population becomes",
            "A mean of many readings reduces the effect of an unusually "
            "crowded or empty patch",
            "Fifteen readings guarantee that every dandelion in the field has "
            "now been counted",
        ],
        "correct_index": 2,
        "why": "Organisms are patchily distributed, so a mean taken from many "
               "random quadrats lies far closer to the true density than one "
               "or two readings.",
    },
    {
        "id": "ks4-sampling-techniques-s04",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a student should decide where to place each "
                "quadrat in a 20 m by 20 m field.",
        "options": [
            "Place them in a straight line across the middle of the field, "
            "one metre apart from each other",
            "Use random numbers as coordinates along two tape measures laid "
            "at right angles to each other",
            "Place them wherever the plant being studied happens to be "
            "growing most densely in the field",
            "Space them evenly around the edge of the field, where access "
            "over the fence is easiest",
        ],
        "correct_index": 1,
        "why": "Random coordinates give every part of the field an equal "
               "chance of being sampled, which removes the bias that choosing "
               "positions would introduce.",
    },
    {
        "id": "ks4-sampling-techniques-h01",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In pond A, 80 sticklebacks are marked and 12 of the 48 caught "
                "later are marked. In pond B, 80 are marked and 24 of the 48 "
                "caught later are marked. Compare the two estimates.",
        "options": [
            "Both ponds hold about 320 fish, because the same number was "
            "marked in each of them",
            "Pond A holds about 160 fish and pond B holds about 320 fish",
            "Pond A holds about 320 fish and pond B holds about 160 fish",
            "Pond A holds about 640 fish and pond B holds about 320 fish",
        ],
        "correct_index": 2,
        "why": "A higher proportion of marked recaptures means a smaller "
               "population: (80 × 48) ÷ 12 = 320, while (80 × 48) ÷ 24 = 160.",
    },
    {
        "id": "ks4-sampling-techniques-h02",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ecologists estimate a beetle population as 450. They marked "
                "90 beetles in the first catch and caught 75 in the second. "
                "Determine how many marked beetles were in the second catch.",
        "options": [
            "5",
            "15",
            "6",
            "45",
        ],
        "correct_index": 1,
        "why": "Rearranging N = (n₁ × n₂) ÷ m gives m = (n₁ × n₂) ÷ N = "
               "(90 × 75) ÷ 450 = 15.",
    },
    {
        "id": "ks4-sampling-techniques-h03",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student marks 50 snails with bright white paint. Many "
                "marked snails are eaten by thrushes before the second catch. "
                "Predict the effect on the estimated population size.",
        "options": [
            "The estimate will be too high, because m is smaller than it "
            "should be",
            "The estimate will be too low, because m is smaller than it "
            "should be",
            "The estimate will be unaffected, because the formula corrects "
            "for predation",
            "The estimate will be too low, because n₂ is smaller than it "
            "should be",
        ],
        "correct_index": 0,
        "why": "N is divided by m, so losing marked individuals lowers m and "
               "pushes the calculated population above the true value.",
    },
    {
        "id": "ks4-sampling-techniques-h04",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A belt transect runs from the low-water mark to the top of a "
                "rocky shore, with a 0.25 m² quadrat every 2 m. Evaluate this "
                "method for finding the shore's total limpet population.",
        "options": [
            "It is ideal, because a transect samples every part of the shore "
            "at random",
            "It is ideal, because limpets are mobile and only a transect can "
            "follow them",
            "It is poor, because quadrats can be used on soil but never on "
            "bare rock",
            "It is poor for a total, because the line is not random and "
            "samples only one strip",
        ],
        "correct_index": 3,
        "why": "A transect deliberately follows an environmental gradient, so "
               "it shows how distribution changes but is not a random sample "
               "of the whole shore.",
    },

    # ── environmental-change ────────────────────────────────────────────
    {
        "id": "ks4-environmental-change-e01",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by an indicator species.",
        "options": [
            "A species introduced to a habitat in order to control a pest",
            "A species found in every habitat on Earth, whatever the "
            "conditions",
            "A species counted in order to work out the total biodiversity",
            "A species whose presence or absence reveals environmental "
            "quality",
        ],
        "correct_index": 3,
        "why": "Indicator species are so sensitive to particular conditions "
               "that whether they are present tells you about pollution "
               "without any chemical measurement.",
    },
    {
        "id": "ks4-environmental-change-e02",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Rat-tailed maggots are found in large numbers in a stretch of "
                "river. State what this indicates about the water.",
        "options": [
            "It is heavily polluted and has a very low oxygen concentration",
            "It is clean, cold and well oxygenated throughout the year",
            "It is contaminated with sulfur dioxide from a nearby power "
            "station",
            "It contains no dissolved mineral ions of any kind at all",
        ],
        "correct_index": 0,
        "why": "Rat-tailed maggots take oxygen from the air through a "
               "breathing tube, so they thrive where the dissolved oxygen is "
               "too low for most species.",
    },
    {
        "id": "ks4-environmental-change-e03",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State one way in which scientists monitor whether "
                "environmental change is affecting a species.",
        "options": [
            "By measuring the mass of a single individual once every ten "
            "years",
            "By recording population size and mapping where the species is "
            "found",
            "By counting the number of chromosomes in the species' cells each "
            "season",
            "By comparing the species with a related species kept in a "
            "laboratory",
        ],
        "correct_index": 1,
        "why": "Repeated surveys of abundance and distribution show whether a "
               "species' range or numbers are shifting as conditions change.",
    },
    {
        "id": "ks4-environmental-change-e04",
        "subtopic_slug": "environmental-change",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what happens to a coral during coral bleaching.",
        "options": [
            "The coral absorbs pale sediment, which stains its skeleton white",
            "The coral's skeleton dissolves in the acidified sea water",
            "The coral expels the symbiotic algae in its tissues and turns "
            "white",
            "The coral migrates into deeper water, leaving its skeleton "
            "behind",
        ],
        "correct_index": 2,
        "why": "Warm water makes the polyps expel the algae that supply most "
               "of their food, so the white skeleton shows through and the "
               "coral eventually starves.",
    },
    {
        "id": "ks4-environmental-change-s01",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "In a eutrophic lake, dissolved oxygen falls sharply after the "
                "algal bloom has died rather than during it. Explain why the "
                "fall comes at that point.",
        "options": [
            "The dead algae release carbon dioxide, which displaces the "
            "oxygen dissolved in the water",
            "The living algae had been absorbing oxygen, and dead algae stop "
            "releasing it again",
            "Decomposers multiply on the dead algae and use up oxygen in "
            "aerobic respiration",
            "The dead algae float and form a layer that stops oxygen "
            "dissolving in at the surface",
        ],
        "correct_index": 2,
        "why": "The bloom itself photosynthesises and adds oxygen; it is the "
               "huge population of aerobic decomposers feeding on the dead "
               "algae that strips the oxygen out.",
    },
    {
        "id": "ks4-environmental-change-s02",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "An oil tanker spills its cargo near a seabird colony. Explain "
                "why many of the birds then die of cold.",
        "options": [
            "The oil dissolves the layer of fat beneath the skin, removing "
            "the birds' insulation",
            "The oil mats the feathers together, so they can no longer trap a "
            "layer of air",
            "The oil evaporates from the feathers, cooling the birds down by "
            "evaporation",
            "The oil blocks the birds' pores, stopping them sweating to "
            "control their temperature",
        ],
        "correct_index": 1,
        "why": "A bird's insulation is the air trapped between its feathers, "
               "and oil destroys the waterproof structure that holds that air "
               "in place.",
    },
    {
        "id": "ks4-environmental-change-s03",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A moth species living on a mountainside shifts its range "
                "further up the mountain each decade as the climate warms. "
                "Explain what will eventually happen to this population.",
        "options": [
            "It will decline and may become extinct, because there is no "
            "higher ground left to move to",
            "It will expand steadily, because higher altitudes always contain "
            "more food resources",
            "It will stabilise, because temperature stops rising above a "
            "certain altitude on a mountain",
            "It will move back down the mountain once it has adapted to the "
            "warmer conditions there",
        ],
        "correct_index": 0,
        "why": "A species tracking its temperature range upwards eventually "
               "runs out of mountain, so its available habitat shrinks to "
               "nothing — this is range contraction.",
    },
    {
        "id": "ks4-environmental-change-s04",
        "subtopic_slug": "environmental-change",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A motorway is built across a wood, splitting it into two "
                "halves of equal total area. Explain why the dormouse "
                "population is now at greater risk.",
        "options": [
            "The total area of woodland has halved, so half of the dormice "
            "have lost their habitat entirely",
            "Dormice are unable to survive in any patch of woodland smaller "
            "than one hectare in area",
            "The noise of the motorway prevents the dormice from finding food "
            "during the night",
            "Two small isolated populations are each more easily wiped out "
            "than one large population",
        ],
        "correct_index": 3,
        "why": "Splitting a population leaves smaller, isolated groups, and a "
               "small population is far more easily destroyed by a single bad "
               "year or a disease outbreak.",
    },
    {
        "id": "ks4-environmental-change-h01",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Two moths share a wood. Species A emerges when temperature "
                "first exceeds 10 °C; species B emerges when day length "
                "reaches 14 hours. Predict which is more at risk as the "
                "climate warms.",
        "options": [
            "Species B — day length does not change with warming, so it may "
            "emerge too late for its food",
            "Species A — a temperature cue is unreliable, so it will emerge "
            "before any warming happens",
            "Neither — both cues respond to the climate, so the two species "
            "will simply shift together",
            "Both equally — emergence date has no effect on an insect's "
            "chance of survival at all",
        ],
        "correct_index": 0,
        "why": "Day length is fixed by the calendar while temperature-driven "
               "events such as leaf burst arrive earlier, so a day-length-cued "
               "species falls out of step with its food.",
    },
    {
        "id": "ks4-environmental-change-h02",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A river survey finds mayfly larvae abundant at site 1, "
                "bloodworms at site 2 and rat-tailed maggots at site 3. Rank "
                "the sites from cleanest to most polluted.",
        "options": [
            "Site 2, then site 1, then site 3",
            "Site 3, then site 2, then site 1",
            "Site 1, then site 3, then site 2",
            "Site 1, then site 2, then site 3",
        ],
        "correct_index": 3,
        "why": "Mayfly larvae need clean well-oxygenated water, bloodworms "
               "tolerate moderate pollution, and rat-tailed maggots survive "
               "where oxygen is almost absent.",
    },
    {
        "id": "ks4-environmental-change-h03",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Lichens are absent from a town centre but abundant on trees "
                "20 km away. A student concludes that the town's river must be "
                "polluted. Evaluate this conclusion.",
        "options": [
            "Valid — lichens take their water from rivers, so their absence "
            "indicates river pollution",
            "Valid — anything that kills lichens will certainly have polluted "
            "the local river water too",
            "Invalid — lichens indicate air quality, so the data show air "
            "pollution, not water pollution",
            "Invalid — lichens are absent from all towns, for reasons that "
            "have nothing to do with pollution",
        ],
        "correct_index": 2,
        "why": "Lichens absorb dissolved gases straight from the air, so they "
               "indicate air quality; water quality needs an aquatic indicator "
               "such as mayfly larvae.",
    },
    {
        "id": "ks4-environmental-change-h04",
        "subtopic_slug": "environmental-change",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A conservation team plants a 30 m wide strip of woodland "
                "joining two isolated woods. Explain how this helps the "
                "populations of woodland species.",
        "options": [
            "It doubles the area of each wood, so each population is able to "
            "double in size as well",
            "It restores movement between the woods, so the populations mix "
            "and gene flow resumes",
            "It shelters both woods from the wind, which raises the "
            "temperature inside each of them",
            "It draws predators away from the two woods and into the "
            "connecting strip of trees",
        ],
        "correct_index": 1,
        "why": "A wildlife corridor reconnects fragmented habitat so "
               "individuals — and their alleles — move between patches, "
               "keeping the combined population genetically varied.",
    },

    # ── factors-affecting-food-security ─────────────────────────────────
    {
        "id": "ks4-factors-affecting-food-security-e01",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by food security.",
        "options": [
            "All people having reliable access to enough safe and nutritious "
            "food",
            "A country producing more food each year than it produced the "
            "year before",
            "Storing food safely so that it cannot be stolen or contaminated",
            "Growing all of a country's food inside its own national borders",
        ],
        "correct_index": 0,
        "why": "Food security is about enough food being available and "
               "accessible to everyone, not simply about the total quantity "
               "produced.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e02",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason why global demand for food is rising.",
        "options": [
            "Crops are becoming less nutritious, so people have to eat more "
            "of them",
            "Food is transported more slowly now, so more must be held in "
            "storage",
            "Farmland is becoming more fertile, which encourages people to "
            "eat more",
            "The world population is over 8 billion and is still increasing",
        ],
        "correct_index": 3,
        "why": "Every additional person needs feeding, so a growing population "
               "raises total food demand even if each person eats the same "
               "amount.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e03",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of organism that causes wheat rust, a disease "
                "that destroys wheat harvests.",
        "options": [
            "A virus",
            "A protist",
            "A fungus",
            "A bacterium",
        ],
        "correct_index": 2,
        "why": "Wheat rust is a fungal pathogen, and fungal crop diseases can "
               "destroy an entire harvest across a whole region.",
    },
    {
        "id": "ks4-factors-affecting-food-security-e04",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why improved storage and refrigeration raise a "
                "country's food security.",
        "options": [
            "They increase the nutritional value of the food that is stored",
            "They reduce the amount of food lost to spoilage before it is "
            "eaten",
            "They allow farmers to grow two separate harvests in one season",
            "They reduce the world population's overall demand for meat",
        ],
        "correct_index": 1,
        "why": "Food that rots before reaching anyone is food produced for "
               "nothing, so cutting waste raises the amount actually available "
               "to eat.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s01",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a year when the global grain harvest is the largest ever "
                "recorded, millions of people still go hungry. Explain how "
                "this is possible.",
        "options": [
            "The grain harvested that year had a far lower nutritional "
            "content than grain usually has",
            "Grain cannot be eaten by humans at all until it has first been "
            "fed to livestock animals",
            "A record harvest always drives prices upwards, beyond what most "
            "families are able to pay",
            "Food is distributed unequally — poverty, conflict and poor "
            "infrastructure all block access",
        ],
        "correct_index": 3,
        "why": "Food security depends on access as much as on supply, so food "
               "can be plentiful globally and still fail to reach the people "
               "who need it.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s02",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A new insect pest arrives in a country on imported plants and "
                "spreads rapidly. Explain why it may cause more damage than a "
                "native pest.",
        "options": [
            "Imported pests are always physically larger than native pests "
            "and so eat more each day",
            "Imported pests reproduce sexually, whereas native pests only "
            "ever reproduce asexually",
            "The local crops and predators have no history with it, so "
            "nothing limits its numbers",
            "Imported pests carry chemicals from their country of origin that "
            "poison the crop directly",
        ],
        "correct_index": 2,
        "why": "A newly arrived pest meets crops with no resistance and "
               "predators that do not recognise it, so its population can grow "
               "unchecked.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s03",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why rising sea levels threaten food security in "
                "low-lying countries such as Bangladesh.",
        "options": [
            "Salt water is required to irrigate rice, and sea level rise "
            "removes the supply of it",
            "Farmland is flooded and the soil becomes salty, so less land can "
            "be used for crops",
            "Higher sea levels cool the air, which shortens the growing "
            "season for every crop",
            "Fish move further out to sea, so the coastal fisheries can no "
            "longer catch them",
        ],
        "correct_index": 1,
        "why": "Sea level rise removes agricultural land outright and drives "
               "salt into the soil that remains, cutting the area that can be "
               "farmed.",
    },
    {
        "id": "ks4-factors-affecting-food-security-s04",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a smallholder farmer in a developing country may "
                "produce far less food per hectare than a farmer in the UK.",
        "options": [
            "They may be unable to afford fertilisers, pesticides and farm "
            "machinery",
            "Their soil contains no mineral ions at all, so no crop is able "
            "to grow in it",
            "Crops grown near the equator cannot photosynthesise in strong "
            "sunlight",
            "They are legally prevented from growing more than one crop in "
            "each year",
        ],
        "correct_index": 0,
        "why": "Agricultural inputs are expensive, and without fertiliser, "
               "pest control and machinery a farmer cannot reach the yields "
               "those inputs make possible.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h01",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the suggestion that farming insects for protein "
                "could improve global food security.",
        "options": [
            "It cannot help, because insects contain no protein that the "
            "human gut is able to digest",
            "It could help — insects convert plant material into protein far "
            "more efficiently than cattle",
            "It could help, because insects need no food at all and can be "
            "farmed on bare soil",
            "It cannot help, because insect farming needs more land per "
            "kilogram of protein than beef",
        ],
        "correct_index": 1,
        "why": "Insects are ectothermic and waste little energy as heat, so a "
               "far greater share of what they eat becomes edible protein.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h02",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A government must choose between funding higher-yield seed "
                "varieties and funding better roads and storage. Explain why "
                "the second option may raise food security more.",
        "options": [
            "Producing more food does not help if the extra food spoils or "
            "cannot reach the people",
            "Higher-yield varieties always fail in their first season and so "
            "cannot be relied upon",
            "Roads and storage increase the nutritional value of the food "
            "that travels along them",
            "Higher-yield crop varieties are illegal in most developing "
            "countries around the world",
        ],
        "correct_index": 0,
        "why": "Food security depends on distribution and access, so removing "
               "a bottleneck between field and plate can deliver more food "
               "than growing more of it.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h03",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the land needed to feed one person on a diet of "
                "cereals with the land needed to feed them on a diet of beef.",
        "options": [
            "The beef diet needs slightly less land, because cattle graze "
            "ground unsuitable for crops",
            "The two diets need the same area of land, because the beef comes "
            "from the same cereals",
            "The beef diet needs about twice as much land as the cereal diet "
            "requires",
            "The beef diet needs roughly ten times as much land as the cereal "
            "diet requires",
        ],
        "correct_index": 3,
        "why": "Feeding cereals to cattle adds a trophic level, and only about "
               "a tenth of the biomass passes on, so the same nutrition needs "
               "around ten times the area.",
    },
    {
        "id": "ks4-factors-affecting-food-security-h04",
        "subtopic_slug": "factors-affecting-food-security",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A drought cuts a region's maize harvest by 40%. The "
                "government responds by banning maize exports. Evaluate this "
                "decision.",
        "options": [
            "It is certain to fail, because no government can control what "
            "its own farmers choose to sell",
            "It will raise the harvest itself, because farmers work harder "
            "when exports have been banned",
            "It keeps food in the region, but may raise prices elsewhere and "
            "worsen shortages there",
            "It has no effect on food security anywhere, because exports are "
            "a tiny part of total trade",
        ],
        "correct_index": 2,
        "why": "Export bans protect the domestic supply but shift the shortage "
               "abroad — food security is a global distribution problem as "
               "well as a local production one.",
    },

    # ── farming-techniques ──────────────────────────────────────────────
    {
        "id": "ks4-farming-techniques-e01",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the difference between a pesticide and a herbicide.",
        "options": [
            "A pesticide is sprayed onto the soil; a herbicide is sprayed "
            "onto the leaves",
            "A pesticide is organic in origin; a herbicide is manufactured "
            "artificially",
            "A pesticide kills organisms that damage a crop; a herbicide "
            "kills weeds",
            "A pesticide is used on farm animals; a herbicide is used on "
            "their feed",
        ],
        "correct_index": 2,
        "why": "Herbicides target the weeds competing with a crop for light "
               "and minerals; pesticides target the insects and other pests "
               "that eat or infect it.",
    },
    {
        "id": "ks4-farming-techniques-e02",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one condition that a greenhouse allows a grower to "
                "control.",
        "options": [
            "The number of hours of daylight that the whole region receives",
            "The genetic make-up of the crop variety that is being grown",
            "The mineral ion content of the seeds before they are planted",
            "The temperature and carbon dioxide concentration around the crop",
        ],
        "correct_index": 3,
        "why": "A greenhouse holds temperature and carbon dioxide at the "
               "levels that make photosynthesis fastest, and so extends the "
               "growing season.",
    },
    {
        "id": "ks4-farming-techniques-e03",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by monoculture.",
        "options": [
            "Growing crops without any artificial fertilisers or pesticides",
            "Growing a single type of crop over a large area of land",
            "Keeping one breed of animal indoors throughout the whole year",
            "Growing crops inside a greenhouse rather than in an open field",
        ],
        "correct_index": 1,
        "why": "Monoculture means one crop across a whole area — economical to "
               "sow and harvest, but it supports very few other species.",
    },
    {
        "id": "ks4-farming-techniques-e04",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why farm animals are given high-protein feed.",
        "options": [
            "Protein is used to build new tissue, so the animals grow faster",
            "Protein keeps the animals warm, reducing the need for heating",
            "Protein is cheaper to produce than carbohydrate-based feed is",
            "Protein stops the animals moving around their enclosure so much",
        ],
        "correct_index": 0,
        "why": "Growth means making new protein, so a concentrated protein "
               "supply lets an animal add body mass more quickly.",
    },
    {
        "id": "ks4-farming-techniques-s01",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the routine use of antibiotics in intensively "
                "farmed livestock is now restricted in many countries.",
        "options": [
            "Antibiotics slow the animals' growth rate, which reduces the "
            "farmer's overall yield",
            "It selects for antibiotic-resistant bacteria, which can then go "
            "on to infect humans",
            "Antibiotics build up in the soil and cause eutrophication of the "
            "rivers nearby",
            "Antibiotics kill the useful decomposers that break down the "
            "animals' waste",
        ],
        "correct_index": 1,
        "why": "Constant low-level antibiotic exposure kills the susceptible "
               "bacteria and leaves resistant ones to multiply, and those "
               "strains can spread to people.",
    },
    {
        "id": "ks4-farming-techniques-s02",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Fertiliser is spread on a field beside a stream during heavy "
                "rain. Describe the effect on the stream.",
        "options": [
            "The fertiliser neutralises the stream, raising its pH until the "
            "fish are killed",
            "The fertiliser coats the fishes' gills, which prevents gas "
            "exchange taking place",
            "Nitrates run off, algae bloom, and decomposers then strip the "
            "oxygen from the water",
            "The fertiliser makes the water plants grow so large that they "
            "block the whole stream",
        ],
        "correct_index": 2,
        "why": "Soluble nitrates wash straight into the water and trigger "
               "eutrophication: an algal bloom, then decomposition that leaves "
               "too little oxygen for fish.",
    },
    {
        "id": "ks4-farming-techniques-s03",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a farmer using biological control may still find "
                "some pest insects on the crop.",
        "options": [
            "The predator's numbers depend on the pest's, so the pest is "
            "reduced but never wiped out",
            "Biological control agents only feed at night, so any pests "
            "active by day will survive",
            "The predators become resistant to the pest after only a single "
            "generation has passed",
            "Biological control works only against weeds, so insect pests are "
            "left entirely unaffected",
        ],
        "correct_index": 0,
        "why": "A predator that wiped out its prey would starve, so predator "
               "and prey settle together at low numbers rather than the pest "
               "disappearing.",
    },
    {
        "id": "ks4-farming-techniques-s04",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a farmer might choose an insecticide over "
                "biological control when an aphid outbreak is already damaging "
                "a crop.",
        "options": [
            "Insecticides are specific to aphids alone and harm no other "
            "insect species at all",
            "Insecticides leave no residue on the crop, unlike biological "
            "control agents do",
            "Aphid predators are unable to survive outdoors anywhere in the "
            "United Kingdom",
            "Insecticides act quickly, whereas a predator population takes "
            "time to build up",
        ],
        "correct_index": 3,
        "why": "Biological control is slower because the predator must "
               "multiply before it has an effect, so an outbreak already "
               "causing losses may need a faster treatment.",
    },
    {
        "id": "ks4-farming-techniques-h01",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the introduction of a non-native beetle to control a "
                "weed in a new country.",
        "options": [
            "It may control the weed, but the beetle could itself become an "
            "invasive pest species",
            "It is entirely safe, because a beetle chosen to eat one weed "
            "will only ever eat that weed",
            "It cannot work at all, because introduced species always die in "
            "an unfamiliar climate",
            "It is preferable to herbicides in every case, because no "
            "chemicals at all are involved",
        ],
        "correct_index": 0,
        "why": "A control organism released where it has no predators of its "
               "own can spread beyond its target — the risk that must be "
               "weighed against avoiding herbicides.",
    },
    {
        "id": "ks4-farming-techniques-h02",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the yield and the environmental impact of organic "
                "farming with those of intensive farming.",
        "options": [
            "Organic gives higher yields and lower environmental impact, so "
            "it is better in every way",
            "Organic gives lower yields, but reduces fertiliser and pesticide "
            "pollution",
            "Organic gives the same yields as intensive farming, but costs "
            "more to run each year",
            "Organic gives lower yields and greater pollution, so it offers "
            "no advantages at all",
        ],
        "correct_index": 1,
        "why": "Refusing artificial fertilisers and pesticides removes their "
               "run-off and non-target effects, at the cost of producing less "
               "food from the same land.",
    },
    {
        "id": "ks4-farming-techniques-h03",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Insecticide is sprayed on an oilseed rape crop. The following "
                "year the farmer finds the crop's seed yield has fallen. "
                "Suggest an explanation.",
        "options": [
            "The insecticide was absorbed by the seeds, making them too heavy "
            "to develop properly",
            "The insecticide killed the crop's own root cells, which reduced "
            "its uptake of minerals",
            "The insecticide raised the soil pH, so nitrate ions could no "
            "longer be absorbed by roots",
            "The insecticide harmed bees and other pollinators, so fewer "
            "flowers were pollinated",
        ],
        "correct_index": 3,
        "why": "Insecticides are rarely specific, and killing the pollinators "
               "alongside the pests removes the pollination the crop depends "
               "on to set seed.",
    },
    {
        "id": "ks4-farming-techniques-h04",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A large arable farm grows only wheat, field after field. "
                "Explain why this reduces the biodiversity of the area.",
        "options": [
            "Wheat releases chemicals into the soil that are toxic to every "
            "other species of plant",
            "Wheat uses all the carbon dioxide in the local air, so nothing "
            "else is able to photosynthesise",
            "One crop offers only one habitat and one food source, so very "
            "few species can live there",
            "Wheat fields are ploughed each year, and ploughing sterilises "
            "the soil permanently",
        ],
        "correct_index": 2,
        "why": "Biodiversity depends on a variety of habitats and food "
               "sources, and a monoculture — with herbicides removing every "
               "other plant — supplies almost none.",
    },

    # ── sustainable-fisheries ───────────────────────────────────────────
    {
        "id": "ks4-sustainable-fisheries-e01",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what makes a fish stock sustainable.",
        "options": [
            "The stock is left completely unfished for at least ten years",
            "Fish are caught no faster than the population can reproduce",
            "Only the largest and oldest fish in the population are caught",
            "The same number is caught each year, whatever the stock size",
        ],
        "correct_index": 1,
        "why": "A stock is sustainable when the catch is replaced by breeding, "
               "so it can be harvested indefinitely without declining.",
    },
    {
        "id": "ks4-sustainable-fisheries-e02",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by aquaculture.",
        "options": [
            "Growing fish commercially in tanks, ponds or sea cages",
            "Catching wild fish using large nets towed behind a boat",
            "Studying the migration routes of wild fish populations",
            "Restoring a seabed after it has been damaged by trawling",
        ],
        "correct_index": 0,
        "why": "Aquaculture is fish farming — raising fish under controlled "
               "conditions rather than catching them from the wild.",
    },
    {
        "id": "ks4-sustainable-fisheries-e03",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why banning fishing during the breeding season helps a "
                "fish stock recover.",
        "options": [
            "Fish are easier to catch during the breeding season, so the ban "
            "makes fishing fairer",
            "Fish are unsafe for people to eat during the weeks of the "
            "breeding season",
            "Adults can spawn before they are caught, so the next generation "
            "is produced",
            "Fishing boats need a set period each year for maintenance and "
            "for repairs",
        ],
        "correct_index": 2,
        "why": "Letting the adults reproduce first means their offspring "
               "replace them, which is exactly what keeps a catch sustainable.",
    },
    {
        "id": "ks4-sustainable-fisheries-e04",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason why the collapse of a fish stock matters "
                "beyond the fishing industry itself.",
        "options": [
            "It raises the temperature of the ocean where that stock used to "
            "live",
            "It causes the sea level to rise across the region that was "
            "fished",
            "It reduces the amount of oxygen dissolved in the surface water",
            "Billions of people rely on fish as their main source of protein",
        ],
        "correct_index": 3,
        "why": "Fish is the primary protein for a large share of the world's "
               "population, so a collapsing stock is a food security problem "
               "as well as an economic one.",
    },
    {
        "id": "ks4-sustainable-fisheries-s01",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how scientists decide what a year's fishing quota for "
                "cod should be.",
        "options": [
            "They set it at exactly the same figure as the previous year's "
            "actual recorded catch",
            "They divide the total area of sea by the number of fishing boats "
            "holding a licence",
            "They ask the fishing crews how many fish they expect to be able "
            "to catch that year",
            "They survey the stock's size and breeding rate, then set a catch "
            "it can replace",
        ],
        "correct_index": 3,
        "why": "Quotas are calculated from population data so that the number "
               "of fish removed is no greater than the number the stock can "
               "produce.",
    },
    {
        "id": "ks4-sustainable-fisheries-s02",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Farmed salmon escape from a damaged sea cage into a loch "
                "containing wild salmon. Suggest one problem this may cause.",
        "options": [
            "The escaped fish interbreed with the wild salmon, altering the "
            "wild population's genes",
            "The escaped fish are unable to swim, so they sink and pollute "
            "the bed of the loch",
            "The escaped fish raise the temperature of the loch water around "
            "the damaged cage",
            "The escaped fish are all sterile, so the wild population stops "
            "breeding altogether",
        ],
        "correct_index": 0,
        "why": "Farmed fish are selectively bred for growth in captivity, so "
               "their alleles entering a wild population can reduce its "
               "fitness in the wild.",
    },
    {
        "id": "ks4-sustainable-fisheries-s03",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fish farm can cause water pollution in the loch "
                "around it.",
        "options": [
            "The cages release the antibiotics used to treat the fish "
            "straight into the air",
            "Uneaten feed and fish faeces sink beneath the cages and enrich "
            "the water there",
            "The metal cages corrode in sea water and release toxic metal "
            "ions into the loch",
            "The fish remove all of the oxygen from the loch by respiring "
            "inside the cages",
        ],
        "correct_index": 1,
        "why": "A cage concentrates thousands of fish in one place, so "
               "nutrients from waste and surplus feed accumulate beneath it "
               "and can cause eutrophication.",
    },
    {
        "id": "ks4-sustainable-fisheries-s04",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why farming a carnivorous fish such as salmon does "
                "not fully remove pressure from wild fish stocks.",
        "options": [
            "Farmed salmon escape in such numbers that the wild stocks are "
            "outcompeted for food",
            "Farmed salmon are released back into the open sea once they have "
            "reached full size",
            "Salmon are fed on fishmeal that is made from wild-caught fish",
            "Salmon farms are always built directly on the breeding grounds "
            "of the wild stocks",
        ],
        "correct_index": 2,
        "why": "A carnivorous farmed fish has to be fed other fish, so wild "
               "stocks are still harvested in order to supply the feed.",
    },
    {
        "id": "ks4-sustainable-fisheries-h01",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country doubles the size of its fishing fleet but leaves "
                "its quota unchanged. Predict the effect on the fish stock and "
                "on the fishing industry.",
        "options": [
            "The stock will fall, because a larger fleet always lands more "
            "fish than a quota allows",
            "The stock will rise, because the boats compete and so each of "
            "them catches far less",
            "The stock should hold steady, but each boat's share and its "
            "income will be smaller",
            "The stock and the industry are both unaffected by the number of "
            "boats that are fishing",
        ],
        "correct_index": 2,
        "why": "The quota, not the fleet, sets the total catch — so the stock "
               "is protected while the same catch has to be divided between "
               "twice as many boats.",
    },
    {
        "id": "ks4-sustainable-fisheries-h02",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fishing quotas are difficult to enforce in "
                "international waters.",
        "options": [
            "Fish populations cannot be counted once they have left a "
            "country's own coastal waters",
            "Quotas apply only to farmed fish, and there are no fish farms in "
            "the open ocean",
            "Fish caught in international waters cannot legally be sold in "
            "any country at all",
            "No single government has authority there, so the rules depend on "
            "countries co-operating",
        ],
        "correct_index": 3,
        "why": "Open ocean lies outside any nation's jurisdiction, so a quota "
               "is only as effective as the international agreement and "
               "inspection that back it.",
    },
    {
        "id": "ks4-sustainable-fisheries-h03",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fishery uses nets whose mesh lets fish below 30 cm escape. "
                "Cod do not mature until they reach 50 cm. Evaluate this "
                "rule.",
        "options": [
            "It is too weak — cod between 30 cm and 50 cm are caught before "
            "they can breed",
            "It is too strict — no cod at all would be caught, so the fishery "
            "would have to close",
            "It is exactly right, because a cod of 30 cm is already old "
            "enough to reproduce",
            "Mesh size makes no difference, because cod are caught on lines "
            "rather than in nets",
        ],
        "correct_index": 0,
        "why": "A mesh only protects fish smaller than its holes, so setting "
               "it below the size at which the species matures still removes "
               "fish that have never spawned.",
    },
    {
        "id": "ks4-sustainable-fisheries-h04",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare a closed recirculating fish farm on land with a sea "
                "cage farm, in terms of environmental impact.",
        "options": [
            "The land system pollutes more, because its water is never "
            "exchanged with the open sea",
            "The land system contains its waste and its escapes, but uses far "
            "more energy to run",
            "The two systems have identical impacts, because both hold their "
            "fish at high density",
            "The sea cage system is cleaner, because the tidal currents "
            "remove the waste completely",
        ],
        "correct_index": 1,
        "why": "A closed system stops waste, disease and escapes reaching wild "
               "water, but pumping and filtering costs energy that a sea cage "
               "gets from the tide for free.",
    },

    # ── role-of-biotechnology ───────────────────────────────────────────
    {
        "id": "ks4-role-of-biotechnology-e01",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one example of traditional biotechnology used in food "
                "production.",
        "options": [
            "Inserting a bacterial gene into a growing maize plant",
            "Growing thousands of identical plants from one plant's tissue",
            "Producing human insulin from genetically modified bacteria",
            "Using yeast to make bread rise and to brew beer",
        ],
        "correct_index": 3,
        "why": "Traditional biotechnology uses whole organisms in familiar "
               "processes such as fermentation, long before genes could be "
               "transferred between species.",
    },
    {
        "id": "ks4-role-of-biotechnology-e02",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is inserted into a plant in order to make it "
                "genetically modified.",
        "options": [
            "A chemical fertiliser that changes the way the plant grows",
            "A protein taken from a different species of flowering plant",
            "A gene from another organism, carrying a useful characteristic",
            "A dose of radiation that alters the plant's characteristics",
        ],
        "correct_index": 2,
        "why": "Genetic engineering transfers a specific gene into the plant's "
               "cells, so the plant then makes the protein that gene codes "
               "for.",
    },
    {
        "id": "ks4-role-of-biotechnology-e03",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the process used to produce large numbers of genetically "
                "identical plants from a small piece of tissue.",
        "options": [
            "Micropropagation, also called tissue culture",
            "Selective breeding over many generations",
            "Fermentation in a large industrial fermenter",
            "Genetic engineering using a bacterial vector",
        ],
        "correct_index": 0,
        "why": "Tissue culture grows many clones from a few cells of one "
               "plant, so a high-yield variety can be multiplied very "
               "quickly.",
    },
    {
        "id": "ks4-role-of-biotechnology-e04",
        "subtopic_slug": "role-of-biotechnology",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason why mycoprotein is described as an efficient "
                "source of protein.",
        "options": [
            "The fungus needs no food source, growing on air and water alone",
            "The fungus converts carbohydrate into protein faster than farm "
            "animals do",
            "The fungus can be harvested straight from woodland without being "
            "grown",
            "The fungus grows only in warm countries, so it needs no heating "
            "at all",
        ],
        "correct_index": 1,
        "why": "The fungus is grown on glucose syrup and builds protein far "
               "more rapidly, and with far less waste, than an animal fed the "
               "same carbohydrate.",
    },
    {
        "id": "ks4-role-of-biotechnology-s01",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain the difference between selective breeding and genetic "
                "engineering.",
        "options": [
            "Selective breeding chooses parents with existing variation; "
            "engineering inserts a gene",
            "Selective breeding changes the genes directly; genetic "
            "engineering changes only the environment",
            "Selective breeding works on animals only; genetic engineering "
            "works on plants only",
            "Selective breeding is much faster than genetic engineering, but "
            "far less precise than it",
        ],
        "correct_index": 0,
        "why": "Selective breeding can only work with alleles the species "
               "already has and takes many generations, while genetic "
               "engineering moves one specific gene in a single step.",
    },
    {
        "id": "ks4-role-of-biotechnology-s02",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how growing Bt maize can reduce a farmer's use of "
                "chemical insecticide.",
        "options": [
            "The gene makes the maize taste unpleasant, so no insect will "
            "ever choose to feed on it",
            "The maize makes a bacterial toxin that kills the caterpillars "
            "feeding on it",
            "The gene attracts ladybirds and other predators, which then eat "
            "the pests on the crop",
            "The gene makes the maize grow faster than the pests are able to "
            "damage it",
        ],
        "correct_index": 1,
        "why": "The transferred gene from Bacillus thuringiensis makes the "
               "plant produce its own insecticidal protein, so the pest is "
               "killed as it feeds.",
    },
    {
        "id": "ks4-role-of-biotechnology-s03",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why some seed companies do not allow farmers to save "
                "and replant seed from a GM crop.",
        "options": [
            "The saved seed would all be sterile and would fail to germinate "
            "the following year",
            "Saved GM seed becomes toxic to humans after a single season "
            "spent in storage",
            "The law requires all GM seed to be destroyed after one harvest "
            "has been taken",
            "The company holds a patent on the variety and sells new seed "
            "each year",
        ],
        "correct_index": 3,
        "why": "The modification is commercial property, so growers buy the "
               "seed under licence rather than owning the variety — which "
               "makes them dependent on the supplier.",
    },
    {
        "id": "ks4-role-of-biotechnology-s04",
        "subtopic_slug": "role-of-biotechnology",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain one health concern that has been raised about GM "
                "crops.",
        "options": [
            "GM crops contain no vitamins at all, so a diet based on them "
            "causes deficiency disease",
            "The DNA in a GM crop is absorbed into human cells and changes "
            "the person's own genes",
            "A new protein made by the crop may act as an allergen in the "
            "people who eat it",
            "GM crops contain artificial chemicals that build up inside the "
            "human liver over time",
        ],
        "correct_index": 2,
        "why": "Adding a gene makes the plant produce a protein it never made "
               "before, and any unfamiliar protein carries some risk of "
               "triggering an allergic reaction.",
    },
    {
        "id": "ks4-role-of-biotechnology-h01",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Golden Rice was engineered to make beta-carotene. Evaluate "
                "its potential to reduce childhood blindness.",
        "options": [
            "It cannot help at all, because beta-carotene has no connection "
            "with human vision",
            "It could help where rice is the staple food, but only if it is "
            "accepted and grown there",
            "It will end vitamin A deficiency worldwide as soon as it has "
            "been approved for sale",
            "It cannot help, because the human body is unable to absorb "
            "beta-carotene from plants",
        ],
        "correct_index": 1,
        "why": "Beta-carotene is converted into vitamin A in the body, so the "
               "science is sound — the limit on the benefit is whether farmers "
               "grow it and communities eat it.",
    },
    {
        "id": "ks4-role-of-biotechnology-h02",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Pollen from a Bt maize crop is blown onto milkweed plants "
                "growing at the field margin. Suggest the concern that this "
                "raises.",
        "options": [
            "The pollen fertilises the milkweed, producing a maize–milkweed "
            "hybrid plant",
            "The pollen makes the milkweed herbicide-resistant, creating a "
            "so-called superweed",
            "Caterpillars of butterflies feeding on the milkweed may be "
            "killed by the toxin",
            "The pollen coats the milkweed leaves and stops the plant "
            "photosynthesising",
        ],
        "correct_index": 2,
        "why": "The Bt toxin kills caterpillars in general, so pollen carrying "
               "it onto plants outside the field puts non-target species at "
               "risk.",
    },
    {
        "id": "ks4-role-of-biotechnology-h03",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare producing 1 kg of protein as mycoprotein with "
                "producing 1 kg of protein as beef.",
        "options": [
            "Beef needs less land and water, because cattle graze on grass "
            "that grows there naturally",
            "The two use similar resources, because both organisms must be "
            "fed and must be kept warm",
            "Mycoprotein needs more land, because the fermenters occupy a "
            "large area per kilogram",
            "Mycoprotein needs far less land and water, and produces less "
            "greenhouse gas",
        ],
        "correct_index": 3,
        "why": "The fungus is grown in fermenters on glucose and adds only one "
               "step to the food chain, whereas beef needs grazing land, feed "
               "crops and a whole animal's respiration.",
    },
    {
        "id": "ks4-role-of-biotechnology-h04",
        "subtopic_slug": "role-of-biotechnology",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A campaigner argues that GM crops should be banned because "
                "their long-term effects are not fully known. Evaluate this "
                "argument.",
        "options": [
            "It is a fair concern, but GM crops are tested and regulated, and "
            "a ban would have costs too",
            "It is decisive — any technology whose effects are not fully "
            "known should always be banned",
            "It is worthless, because every effect of every GM crop grown "
            "anywhere is already known",
            "It is worthless, because GM crops are identical in every way to "
            "selectively bred crops",
        ],
        "correct_index": 0,
        "why": "Uncertainty is a real reason for caution and for regulation, "
               "but it must be weighed against the yields, nutrition and "
               "reduced pesticide use that would be given up.",
    },
]
