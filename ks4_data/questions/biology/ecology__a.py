"""Biology · Ecology (part A) — the twelve BASE subtopics of AQA 4.7.

Covers `ecosystems` through `carbon-cycle`: levels of organisation and
interdependence, abiotic and biotic factors, adaptations, food chains and
webs, populations and competition, biodiversity, and the six human-impact
subtopics (waste, land use, deforestation, global warming, maintaining
biodiversity, the carbon cycle).

Every subtopic here is BASE — a Foundation Combined class sits all of it —
so nothing in these stems or options reaches into the Higher extension
(indicator species, efficiency calculations, ocean acidification chemistry)
or into Triple-only material.

The distractors are built from the misconceptions the pages themselves
declare: community mistaken for ecosystem, food-chain arrows read as "eats"
rather than "energy flows to", adaptation treated as something an organism
chooses, predator and prey peaks drawn in phase, biodiversity read as
species count alone, peat destruction credited with only one of its two
harms, deforestation credited with only one of its two effects on CO2, the
greenhouse effect confused with ozone damage, and the belief that plants do
not respire. Nothing here restates a lesson page's own "Test yourself"
question or its matching block — those are a different pool, printed with
their answers on a page the child can open at will.

Part B (`ecology__b.py`) carries the remaining eleven ecology subtopics.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── ecosystems ──────────────────────────────────────────────────────
    {
        "id": "ks4-ecosystems-e01",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement describes a stable community?",
        "options": [
            "The populations in it stay roughly constant over time",
            "Every organism in it belongs to the same species",
            "Its non-living conditions never change at any point in the year",
            "No organism in it is ever eaten by another organism",
        ],
        "correct_index": 0,
        "why": "In a stable community the checks and balances — predation, "
               "competition and disease — hold each population within a "
               "narrow range, so numbers stay roughly constant.",
    },
    {
        "id": "ks4-ecosystems-e02",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a woodland, robins feed on earthworms and earthworms "
                "feed on fallen leaves. State the term for species relying "
                "on one another in this way.",
        "options": [
            "Competition",
            "Interdependence",
            "Adaptation",
            "Classification",
        ],
        "correct_index": 1,
        "why": "Interdependence is species depending on each other, directly "
               "or indirectly, for food, shelter, pollination or seed "
               "dispersal.",
    },
    {
        "id": "ks4-ecosystems-e03",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Give the correct order of these levels of organisation, "
                "from the smallest to the largest.",
        "options": [
            "Organism, then community, then population, then ecosystem",
            "Population, then organism, then community, then ecosystem",
            "Organism, then population, then ecosystem, then community",
            "Organism, then population, then community, then ecosystem",
        ],
        "correct_index": 3,
        "why": "One individual is an organism; all the individuals of one "
               "species are a population; all the populations together are "
               "a community; the community plus the non-living surroundings "
               "is the ecosystem.",
    },
    {
        "id": "ks4-ecosystems-e04",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a natural ecosystem rather than one "
                "created by humans?",
        "options": [
            "A trout fish farm",
            "An ornamental garden pond",
            "A tropical coral reef",
            "A ploughed wheat field",
        ],
        "correct_index": 2,
        "why": "A coral reef forms and maintains itself without human "
               "management; fish farms, garden ponds and arable fields are "
               "all built and kept going by people.",
    },
    {
        "id": "ks4-ecosystems-s01",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A disease kills most of the bees in an area. Predict the "
                "effect on the flowering plants the bees pollinate, and "
                "explain why.",
        "options": [
            "Plant numbers rise, because the bees are no longer taking "
            "nectar away from the flowers",
            "Plant numbers fall, because fewer flowers are pollinated so "
            "fewer seeds are produced",
            "Plant numbers stay the same, because plants make their own "
            "food by photosynthesis",
            "Plant numbers rise, because the dead bees add extra minerals "
            "to the soil",
        ],
        "correct_index": 1,
        "why": "Insect-pollinated plants depend on their pollinators to "
               "reproduce, so losing the bees means fewer seeds and, over "
               "time, fewer plants.",
    },
    {
        "id": "ks4-ecosystems-s02",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A soil pollutant kills most of the earthworms in a "
                "woodland. Shrews there feed mainly on earthworms. Predict "
                "what happens to the shrew population.",
        "options": [
            "It falls, because the shrews' main food supply has been reduced",
            "It rises, because the earthworms were competing with the "
            "shrews for food",
            "It rises, because more leaf litter is left uneaten for the "
            "shrews to feed on",
            "It stays the same, because a soil pollutant can only affect "
            "plants and soil organisms",
        ],
        "correct_index": 0,
        "why": "The shrews depend on earthworms as prey, so removing the "
               "prey removes the shrews' food and their numbers fall.",
    },
    {
        "id": "ks4-ecosystems-s03",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a stable community, describe what is true of the birth "
                "rate and the death rate of each population.",
        "options": [
            "The birth rate is always much higher than the death rate",
            "The death rate falls to zero once the community is stable",
            "The two are roughly balanced, so the population stays about "
            "the same",
            "The birth rate rises every year while the death rate stays "
            "fixed",
        ],
        "correct_index": 2,
        "why": "A population only stays constant when births and deaths "
               "cancel out; that balance is what makes the community stable.",
    },
    {
        "id": "ks4-ecosystems-s04",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'A robin's ecosystem is the tree canopy "
                "where it builds its nest.' Identify the error in this "
                "statement.",
        "options": [
            "There is no error — the canopy is exactly what is meant by an "
            "ecosystem",
            "The canopy is the robin's population, because only one species "
            "nests there",
            "The canopy is the robin's community, because many species live "
            "there",
            "The canopy is the robin's habitat, not its whole ecosystem",
        ],
        "correct_index": 3,
        "why": "A habitat is the particular place an organism lives; the "
               "ecosystem is the whole community plus all the non-living "
               "factors around it.",
    },
    {
        "id": "ks4-ecosystems-h01",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A conservation group states that protecting one rare "
                "orchid will also help several insect species survive. "
                "Suggest why this is a reasonable claim.",
        "options": [
            "Insects of every kind are unable to survive anywhere unless a "
            "rare orchid grows nearby",
            "Orchids release into the air a chemical that all of the local "
            "insect species need",
            "The orchid and the insects depend on each other, so protecting "
            "one protects both",
            "The insects and the orchid compete for the same resources, so "
            "both increase together",
        ],
        "correct_index": 2,
        "why": "Insects that feed on or pollinate the orchid are "
               "interdependent with it, so the measures that keep the "
               "orchid's habitat safe keep theirs safe too.",
    },
    {
        "id": "ks4-ecosystems-h02",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lake is stocked with a fish that feeds on water fleas. "
                "The water fleas feed on algae. Predict the effect on the "
                "algae in the lake.",
        "options": [
            "The algae decrease, because the new fish also feed directly on "
            "the algae",
            "The algae decrease, because water fleas eat more algae when "
            "they are being hunted",
            "The algae stay the same, because algae are producers and sit "
            "outside the food web",
            "The algae increase, because fewer water fleas are left to "
            "graze on them",
        ],
        "correct_index": 3,
        "why": "Removing a grazer releases what it grazed: fewer water "
               "fleas means less algae eaten, so the algae build up.",
    },
    {
        "id": "ks4-ecosystems-h03",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two years of unusually low rainfall reduce plant growth in "
                "a grassland. Explain how this can reduce the number of "
                "foxes, even though foxes do not depend on rainfall "
                "directly.",
        "options": [
            "Less plant growth means fewer rabbits, so foxes have less prey",
            "Foxes must drink rainwater directly, so a drought kills them "
            "within a few weeks",
            "Dry soil forces the foxes to move to a habitat where the "
            "ground is much softer",
            "Low rainfall reduces the oxygen in the air, so the foxes "
            "cannot respire properly",
        ],
        "correct_index": 0,
        "why": "Species are interdependent along the chain: an abiotic "
               "change at the producer level passes up through the "
               "herbivores to the predators.",
    },
    {
        "id": "ks4-ecosystems-h04",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An invasive plant covering most of a meadow is removed. "
                "Two years later the number of butterfly species has risen "
                "from 3 to 11. Which conclusion does this evidence best "
                "support?",
        "options": [
            "The butterflies had always been present but had simply been "
            "too well hidden to count",
            "The invasive plant had crowded out the native plants that most "
            "butterflies rely on",
            "Removing the plant lowered the temperature of the meadow, "
            "which suits butterfly larvae",
            "The butterflies had been feeding on the invasive plant and "
            "were being poisoned by it",
        ],
        "correct_index": 1,
        "why": "One dominant species suppresses the variety of food plants; "
               "removing it lets the native plants — and the butterflies "
               "that depend on them — return.",
    },

    # ── abiotic-biotic-factors ──────────────────────────────────────────
    {
        "id": "ks4-abiotic-biotic-factors-e01",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the abiotic factor in this list.",
        "options": [
            "Parasitism by ticks living on deer",
            "The availability of prey for a predator",
            "The wind speed across an open moor",
            "An outbreak of a fungal disease in wheat",
        ],
        "correct_index": 2,
        "why": "Wind speed is a non-living physical feature of the "
               "environment; parasitism, prey availability and disease are "
               "all effects of other organisms.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e02",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the abundance of a species in an "
                "area.",
        "options": [
            "How many individuals of that species are present",
            "The area of ground over which that species is found",
            "The number of different species living alongside it",
            "The variety of alleles carried within that species",
        ],
        "correct_index": 0,
        "why": "Abundance is a count — how many there are — while "
               "distribution is where they are found.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e03",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a biotic factor affecting a population "
                "of oak trees?",
        "options": [
            "The mineral content of the soil they grow in",
            "Squirrels burying and eating their acorns",
            "The average summer temperature of the wood",
            "The amount of rainfall the wood receives",
        ],
        "correct_index": 1,
        "why": "A biotic factor is the effect of another living organism, "
               "and the squirrels are living organisms acting on the oaks.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e04",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A field with very poor, thin soil supports far fewer "
                "plant species than the deep-soiled field next to it. Name "
                "the abiotic factor most likely to be responsible.",
        "options": [
            "Wind speed",
            "Predation",
            "Day length",
            "Soil mineral content",
        ],
        "correct_index": 3,
        "why": "Nitrates, phosphates and other soil minerals are essential "
               "for plant growth, so a mineral-poor soil supports fewer "
               "plant species.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s01",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a rocky shore, only limpets and lichens live on the "
                "highest rocks, while pools that stay underwater hold far "
                "more species. Explain this difference.",
        "options": [
            "The lowest rocks receive far more sunlight than the highest "
            "rocks do",
            "The highest rocks hold more predators, so fewer prey species "
            "can live there",
            "Species higher up the shore compete more strongly, so most of "
            "them die out",
            "The highest rocks dry out and swing in temperature, so only "
            "hardy species survive",
        ],
        "correct_index": 3,
        "why": "Conditions at the top of the shore are the harshest — "
               "desiccation, wave action and large temperature swings — so "
               "only species that tolerate them are found there.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s02",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heavy infestation of tapeworms reduces the growth and "
                "survival of sheep in a field. Name this factor and "
                "classify it.",
        "options": [
            "An abiotic factor, and the factor is parasitism",
            "A biotic factor, and the factor is competition for grass",
            "A biotic factor, and the factor is parasitism",
            "An abiotic factor, and the factor is food availability",
        ],
        "correct_index": 2,
        "why": "Tapeworms are living organisms that harm their host, so "
               "this is parasitism — a biotic factor.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s03",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Jays bury acorns well away from the parent tree. A "
                "woodland loses most of its jays. Suggest the effect on the "
                "distribution of oak trees, and state the type of factor.",
        "options": [
            "Oaks spread less widely, because fewer acorns are carried away "
            "- a biotic factor",
            "Oaks spread less widely, because fewer acorns are carried away "
            "- an abiotic factor",
            "Oaks spread further, because none of their acorns are now "
            "being eaten - a biotic factor",
            "Oak distribution is unchanged, because trees never depend on "
            "animals - an abiotic factor",
        ],
        "correct_index": 0,
        "why": "Many plants depend on animals for seed dispersal, so losing "
               "the disperser is a biotic factor that narrows where the "
               "plant can spread to.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s04",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student records light intensity and the number of plant "
                "species at three points in a wood: a clearing (52 000 lux, "
                "14 species), the woodland edge (18 000 lux, 9 species) and "
                "deep shade (900 lux, 3 species). State the conclusion "
                "these data support.",
        "options": [
            "Species number is not related to light intensity in this wood",
            "Fewer plant species are found where the light intensity is "
            "lower",
            "Light intensity is a biotic factor that controls plant growth",
            "Deep shade holds fewer species because that soil is more "
            "acidic",
        ],
        "correct_index": 1,
        "why": "The three readings fall together, so the data support light "
               "intensity limiting how many plant species can grow.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h01",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two greenhouses are kept at the same temperature and given "
                "the same water and light. Greenhouse X is given extra "
                "carbon dioxide, greenhouse Y is not. After six weeks the "
                "plants in X have twice the mass. Explain this result.",
        "options": [
            "The extra carbon dioxide killed the pests that were eating the "
            "plants in Y",
            "Carbon dioxide had been limiting photosynthesis, so raising it "
            "raised growth",
            "Carbon dioxide is a biotic factor, so it acts on plants more "
            "strongly than light",
            "The extra carbon dioxide warmed greenhouse X, and the warmth "
            "sped up the growth",
        ],
        "correct_index": 1,
        "why": "Everything else was kept the same, so the only factor left "
               "to explain the difference is the carbon dioxide "
               "concentration limiting the rate of photosynthesis.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h02",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ragwort grows far more densely along a sheltered hedge "
                "line than in the open middle of the same field. Suggest "
                "the abiotic factor most likely to explain this, and how it "
                "acts.",
        "options": [
            "Soil pH, because a hedge makes the soil beside it strongly "
            "alkaline",
            "Light intensity, because plants beside a hedge receive far "
            "more light",
            "Predation, because fewer insects can reach plants growing "
            "beside a hedge",
            "Wind speed, because shelter reduces water loss from the plants",
        ],
        "correct_index": 3,
        "why": "Shelter lowers wind speed, which lowers the rate of water "
               "loss from the leaves, so the plants grow better there.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h03",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a change in a single abiotic factor can reduce "
                "the number of species in a community, even when that "
                "factor kills no organism directly.",
        "options": [
            "Abiotic factors always kill organisms directly, so this cannot "
            "happen at all",
            "Every species has exactly the same tolerance range, so all of "
            "them respond",
            "It can change which species outcompete the others, so some are "
            "lost from the area",
            "It reduces the total area of the habitat, so fewer individuals "
            "can fit into it",
        ],
        "correct_index": 2,
        "why": "Abiotic conditions decide which species grow best, so a "
               "shift can hand the advantage to one competitor and squeeze "
               "the others out.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h04",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pond A holds 21 invertebrate species and its water is "
                "14 °C. Pond B holds 6 species, its water is 26 °C, and it "
                "also receives run-off from a car park. A student concludes "
                "that the higher temperature caused pond B's lower species "
                "number. Evaluate this conclusion.",
        "options": [
            "It is not safe, because the run-off is a second difference "
            "that could explain it",
            "It is safe, because temperature is the only difference "
            "recorded between the ponds",
            "It is not safe, because species number is never affected by "
            "water temperature",
            "It is safe, because warmer water always holds more oxygen and "
            "so more species",
        ],
        "correct_index": 0,
        "why": "Two variables differ between the ponds, so neither can be "
               "singled out as the cause from these data alone.",
    },

    # ── adaptations ─────────────────────────────────────────────────────
    {
        "id": "ks4-adaptations-e01",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which type of adaptation is a cactus having spines instead "
                "of broad leaves?",
        "options": [
            "Behavioural",
            "Structural",
            "Functional",
            "Environmental",
        ],
        "correct_index": 1,
        "why": "Spines are a physical feature of the plant's body, so they "
               "are a structural adaptation — they cut the surface area "
               "from which water is lost.",
    },
    {
        "id": "ks4-adaptations-e02",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A desert lizard is active only at night and shelters under "
                "rocks during the day. Name the type of adaptation this is.",
        "options": [
            "Structural",
            "Functional",
            "Genetic",
            "Behavioural",
        ],
        "correct_index": 3,
        "why": "It is something the animal does rather than a feature of "
               "its body or its internal chemistry, so it is behavioural.",
    },
    {
        "id": "ks4-adaptations-e03",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by an adaptation.",
        "options": [
            "A feature that makes an organism better suited to its "
            "environment",
            "A change an organism makes to its own body during its lifetime",
            "A decision an organism takes when its environment becomes "
            "harsh",
            "A feature that every member of a species must have to stay "
            "alive",
        ],
        "correct_index": 0,
        "why": "An adaptation is any feature that raises an organism's "
               "chance of surviving and reproducing where it lives.",
    },
    {
        "id": "ks4-adaptations-e04",
        "subtopic_slug": "adaptations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a functional adaptation?",
        "options": [
            "A hoverfly having black and yellow stripes like a wasp",
            "A wolf pack working together to bring down a large deer",
            "A deep-sea fish producing its own light in the darkness",
            "A deep-sea fish having unusually large eyes for its size",
        ],
        "correct_index": 2,
        "why": "Producing light is an internal chemical process, so it is a "
               "functional adaptation; stripes and large eyes are "
               "structural and pack hunting is behavioural.",
    },
    {
        "id": "ks4-adaptations-s01",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how having small ears and short limbs helps a "
                "mammal survive in the Arctic.",
        "options": [
            "It lowers the surface area to volume ratio, so less heat is "
            "lost",
            "It lowers the mass of the animal, so it needs less food each "
            "day",
            "It makes the animal harder for a predator to see against the "
            "snow",
            "It raises the surface area to volume ratio, so more heat is "
            "held in",
        ],
        "correct_index": 0,
        "why": "Compact shapes have less surface for their volume, so less "
               "of the animal's body heat escapes to the cold air.",
    },
    {
        "id": "ks4-adaptations-s02",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A camel's hump stores fat, not water. Explain how this "
                "helps the camel survive in the desert.",
        "options": [
            "The fat is turned into water, which the camel drinks from the "
            "hump when thirsty",
            "The fat is an energy store, so the camel can go a long time "
            "without food",
            "The fat insulates the camel so that its body stays cool during "
            "the daytime heat",
            "The fat makes the camel heavier, so predators find it harder "
            "to knock it over",
        ],
        "correct_index": 1,
        "why": "Food is scarce and unpredictable in a desert, so carrying "
               "an energy reserve lets the camel survive long gaps between "
               "meals.",
    },
    {
        "id": "ks4-adaptations-s03",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hoverfly is harmless but has the same black and yellow "
                "banding as a wasp. Explain how this helps it survive.",
        "options": [
            "The banding reflects sunlight so that the hoverfly does not "
            "overheat in summer",
            "The banding lets other hoverflies recognise it when they are "
            "looking for a mate",
            "The banding camouflages the hoverfly against the flowers that "
            "it feeds on",
            "Predators avoid it because they mistake it for a stinging "
            "species",
        ],
        "correct_index": 3,
        "why": "This is mimicry: a harmless species copies the warning "
               "colours of a dangerous one and gains the same protection.",
    },
    {
        "id": "ks4-adaptations-s04",
        "subtopic_slug": "adaptations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Poison dart frogs are brightly coloured rather than "
                "camouflaged. Explain how this helps them survive.",
        "options": [
            "The bright colours attract more insects for the frog to catch "
            "and eat",
            "The bright colours help the frog absorb more heat from the "
            "sunlight",
            "The colours warn predators that the frog is toxic, so it is "
            "not eaten",
            "The colours let other frogs avoid competing with it for the "
            "same food",
        ],
        "correct_index": 2,
        "why": "Warning colouration teaches predators to leave the species "
               "alone, so being conspicuous protects the frog rather than "
               "exposing it.",
    },
    {
        "id": "ks4-adaptations-h01",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Arctic foxes grew thicker fur because "
                "they needed it in the cold.' Explain what is wrong with "
                "this reasoning.",
        "options": [
            "Nothing is wrong — an animal grows whichever features it needs "
            "to survive",
            "Nothing is wrong, except that the fur is a functional rather "
            "than a structural feature",
            "Foxes with thicker fur survived and bred more, so the feature "
            "became common",
            "Foxes learn to grow thicker fur by copying the older foxes in "
            "their group",
        ],
        "correct_index": 2,
        "why": "Adaptations arise by natural selection across generations — "
               "no individual can grow a feature because it needs one.",
    },
    {
        "id": "ks4-adaptations-h02",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Foxes have forward-facing eyes and rabbits have eyes on "
                "the sides of the head. Compare the advantage each "
                "arrangement gives.",
        "options": [
            "The fox judges distance to prey; the rabbit sees predators "
            "over a wide field",
            "The rabbit judges distance as it runs; the fox needs only to "
            "see straight ahead",
            "The fox can see in the dark; the rabbit sees the colours that "
            "warn it of danger",
            "Both give the same field of view, but the eyes of the fox are "
            "considerably larger",
        ],
        "correct_index": 0,
        "why": "Predators need depth perception to strike accurately; prey "
               "need the widest possible view to spot an approach.",
    },
    {
        "id": "ks4-adaptations-h03",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fish living 2 km below the ocean surface has very large "
                "eyes and organs that produce light. Explain why a fish "
                "living on a shallow, sunlit reef would gain no advantage "
                "from these features.",
        "options": [
            "Reef fish are too small for large eyes and light-producing "
            "organs to fit inside",
            "There is already plenty of light on a reef, so neither feature "
            "would help",
            "Light-producing organs only work under the very high pressure "
            "of deep water",
            "Large eyes would let in too much sunlight and would blind the "
            "fish on the reef",
        ],
        "correct_index": 1,
        "why": "An adaptation is only an advantage in the conditions it "
               "suits — both of these solve the problem of darkness, which "
               "a sunlit reef does not have.",
    },
    {
        "id": "ks4-adaptations-h04",
        "subtopic_slug": "adaptations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a species that is highly adapted to one narrow "
                "set of conditions is at greater risk when its environment "
                "changes quickly.",
        "options": [
            "Species that are highly adapted always have very small "
            "populations to begin with",
            "An adapted species stops reproducing as soon as its conditions "
            "alter in any way",
            "Such species can change their adaptations quickly, but always "
            "in the wrong direction",
            "Its features suit only the old conditions, and new adaptations "
            "take many generations",
        ],
        "correct_index": 3,
        "why": "Natural selection works over generations, so a fast "
               "environmental change can outrun a specialist's ability to "
               "adapt to it.",
    },

    # ── food-chains-webs ────────────────────────────────────────────────
    {
        "id": "ks4-food-chains-webs-e01",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a food chain, state what an arrow between two organisms "
                "shows.",
        "options": [
            "Which of the two organisms is the larger one",
            "The direction in which the predator travels",
            "Which organism eats the other, pointing at the food",
            "The direction in which energy is transferred",
        ],
        "correct_index": 3,
        "why": "The arrow runs from the organism that is eaten to the "
               "organism that eats it, because that is the way the energy "
               "moves.",
    },
    {
        "id": "ks4-food-chains-webs-e02",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what all producers have in common.",
        "options": [
            "They are eaten by every consumer in the food chain",
            "They are the smallest organisms in the food chain",
            "They make their own food using light energy",
            "They break down dead material and release nutrients",
        ],
        "correct_index": 2,
        "why": "Producers photosynthesise, so they bring the energy into "
               "the food chain in the first place.",
    },
    {
        "id": "ks4-food-chains-webs-e03",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Approximately what percentage of the energy at one trophic "
                "level is transferred to the level above it?",
        "options": [
            "1%",
            "10%",
            "50%",
            "90%",
        ],
        "correct_index": 1,
        "why": "About 90% is lost as heat, faeces and uneaten parts, so "
               "only around 10% reaches the next level.",
    },
    {
        "id": "ks4-food-chains-webs-e04",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a reason that energy is lost between one "
                "trophic level and the next?",
        "options": [
            "Energy is released as heat when organisms respire",
            "Energy is destroyed each time one organism eats another",
            "Energy is used up entirely by the producer before it is eaten",
            "Energy leaks out of the food chain into the soil as light",
        ],
        "correct_index": 0,
        "why": "Respiration releases energy that the organism uses for "
               "movement and warmth, and that energy escapes to the "
               "surroundings as heat rather than passing on.",
    },
    {
        "id": "ks4-food-chains-webs-s01",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The grass in a field stores 40 000 kJ of energy. About 10% "
                "of the energy is transferred at each trophic level. "
                "Calculate the energy stored in the foxes that eat the "
                "rabbits that eat the grass.",
        "options": [
            "4000 kJ",
            "36 000 kJ",
            "400 kJ",
            "40 kJ",
        ],
        "correct_index": 2,
        "why": "Two transfers, each of 10%: 40 000 x 0.1 = 4000 kJ in the "
               "rabbits, and 4000 x 0.1 = 400 kJ in the foxes.",
    },
    {
        "id": "ks4-food-chains-webs-s02",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a moorland food web, heather is eaten by mountain hares "
                "and by red grouse, and foxes eat both the hares and the "
                "grouse. A disease kills most of the mountain hares. "
                "Predict the effect on the foxes.",
        "options": [
            "Fox numbers rise, because the hares had been competing with "
            "them for grouse",
            "Fox numbers stay the same, because foxes sit at the top of "
            "this food web",
            "Fox numbers rise, because there are now more dead hares for "
            "them to scavenge",
            "Fox numbers fall, because one of their two food sources has "
            "been reduced",
        ],
        "correct_index": 3,
        "why": "A predator that loses part of its prey supply has less "
               "food, so fewer individuals can be supported.",
    },
    {
        "id": "ks4-food-chains-webs-s03",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a food web gives a more realistic picture of "
                "an ecosystem than a single food chain does.",
        "options": [
            "Most organisms eat, and are eaten by, more than one species",
            "A food web shows the exact number of organisms at each level",
            "A food web always includes decomposers and a food chain cannot",
            "A food web shows which way the energy travels and a chain does "
            "not",
        ],
        "correct_index": 0,
        "why": "Feeding relationships in a real community branch in many "
               "directions, and a web shows those links where a single "
               "chain hides them.",
    },
    {
        "id": "ks4-food-chains-webs-s04",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two ways, other than respiration, in which "
                "biomass is lost between one trophic level and the next.",
        "options": [
            "Some energy is turned into light, and some is turned into "
            "sound",
            "Not all of an organism is eaten, and some material is lost as "
            "faeces",
            "Some organisms move about, and some organisms grow larger over "
            "time",
            "Water evaporates from the organisms, and minerals wash down "
            "into the soil",
        ],
        "correct_index": 1,
        "why": "Bones, roots and shells are often left uneaten, and "
               "material that is eaten but not digested leaves the body in "
               "the faeces.",
    },
    {
        "id": "ks4-food-chains-webs-h01",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student draws the chain 'owl to mouse to wheat' and says "
                "the arrows show what each animal eats. Explain the error.",
        "options": [
            "The arrows should run wheat to mouse to owl, showing energy "
            "flow",
            "The arrows are right, but the owl should be labelled as the "
            "producer",
            "The arrows are right, but the wheat belongs at the top of the "
            "chain",
            "The arrows should have two heads, because energy travels in "
            "both directions",
        ],
        "correct_index": 0,
        "why": "Arrows in a food chain show energy transfer, so they always "
               "point from the food towards whatever feeds on it.",
    },
    {
        "id": "ks4-food-chains-webs-h02",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sea otters eat sea urchins, and sea urchins graze on kelp. "
                "Otters are hunted almost to extinction along one stretch "
                "of coast. Predict what happens to the kelp there, and "
                "explain why.",
        "options": [
            "The kelp increases, because the urchins now have more "
            "predators to avoid",
            "The kelp decreases, because more urchins survive and graze it "
            "harder",
            "The kelp is unchanged, because kelp is a producer and makes "
            "its own food",
            "The kelp decreases, because the otters used to fertilise it "
            "with their waste",
        ],
        "correct_index": 1,
        "why": "Removing the predator releases its prey, and the released "
               "grazer eats more of the producer — the change travels two "
               "steps down the chain.",
    },
    {
        "id": "ks4-food-chains-webs-h03",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a food web a plant is eaten by an insect, the insect is "
                "eaten by a spider, and the spider is eaten by a bird. A "
                "pesticide kills all of the insects. Suggest the effect on "
                "the birds, and explain the delay before it is seen.",
        "options": [
            "The birds increase, because there are now fewer insects "
            "competing with them",
            "The birds are unaffected, because they never feed on the "
            "insects directly",
            "The birds fall, after a delay, because their prey the spiders "
            "decline first",
            "The birds fall immediately, because the pesticide is most "
            "toxic to birds",
        ],
        "correct_index": 2,
        "why": "The birds are two steps above the insects, so the shortage "
               "has to work its way up through the spiders before the birds "
               "feel it.",
    },
    {
        "id": "ks4-food-chains-webs-h04",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the biomass and the amount of energy at the "
                "producer level with those at the tertiary consumer level of "
                "the same food chain.",
        "options": [
            "Both are greater at the tertiary consumer level than at the "
            "producer level",
            "Energy is greater at the producer level, but the biomass is "
            "greater at the top",
            "Both are about the same, because energy is conserved along the "
            "whole chain",
            "Both are greater at the producer level, because energy is lost "
            "at every step",
        ],
        "correct_index": 3,
        "why": "Around 90% of the energy is lost at each transfer, so each "
               "level up holds less energy and less biomass than the one "
               "below it.",
    },

    # ── population-competition ──────────────────────────────────────────
    {
        "id": "ks4-population-competition-e01",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a resource that plants compete for?",
        "options": [
            "Light",
            "Mates",
            "Territory",
            "Shelter",
        ],
        "correct_index": 0,
        "why": "Plants compete for light, water, minerals and space; mates, "
               "territory and shelter are resources animals compete for.",
    },
    {
        "id": "ks4-population-competition-e02",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a density-independent factor limiting a "
                "population?",
        "options": [
            "A disease spreading through a crowded colony of birds",
            "A shortage of food when the numbers are very high",
            "A severe frost that kills insects across a whole region",
            "Predators gathering where their prey are most crowded",
        ],
        "correct_index": 2,
        "why": "A frost kills the same proportion of insects whether the "
               "population is dense or sparse, so it acts independently of "
               "density.",
    },
    {
        "id": "ks4-population-competition-e03",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A population grows when which of the following is true?",
        "options": [
            "The death rate is greater than the birth rate",
            "The birth rate is exactly equal to the death rate",
            "The birth rate and the death rate both fall together",
            "The birth rate is greater than the death rate",
        ],
        "correct_index": 3,
        "why": "More individuals are being born than are dying, so the "
               "total number rises.",
    },
    {
        "id": "ks4-population-competition-e04",
        "subtopic_slug": "population-competition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the resource two stags are competing for when they "
                "fight during the breeding season.",
        "options": [
            "Light",
            "Mates",
            "Minerals",
            "Oxygen",
        ],
        "correct_index": 1,
        "why": "Access to females is the resource in short supply during "
               "the rut, so the stags compete for mates.",
    },
    {
        "id": "ks4-population-competition-s01",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pond is stocked with 50 fish. Their numbers rise quickly "
                "at first, then level off at about 400 and stay there. "
                "Explain what the level of 400 represents.",
        "options": [
            "The number of fish that were originally put in to breed",
            "The largest number of fish the pond's resources can support",
            "The number of fish that the pond's predators are able to eat",
            "The point at which the fish stop reproducing altogether",
        ],
        "correct_index": 1,
        "why": "Once food, oxygen and space are fully used, births and "
               "deaths balance and the population settles at the carrying "
               "capacity of that pond.",
    },
    {
        "id": "ks4-population-competition-s02",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On an island with no predators, a rabbit population "
                "doubles every year for six years and then crashes. Suggest "
                "the most likely cause of the crash.",
        "options": [
            "Food and space ran out as numbers grew, so many rabbits "
            "starved",
            "The rabbits ran out of oxygen because there were so many of "
            "them",
            "Rabbits stop breeding once their population reaches an even "
            "number",
            "A predator must have arrived, because a population never "
            "crashes on its own",
        ],
        "correct_index": 0,
        "why": "Growth is limited by resources: once the population passes "
               "what the island can supply, competition for food and space "
               "raises the death rate sharply.",
    },
    {
        "id": "ks4-population-competition-s03",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how competition between individuals of the same "
                "species slows the growth of a population.",
        "options": [
            "It kills off the weakest individuals outright, so eventually "
            "the species dies out",
            "It makes individuals move elsewhere, so the total population "
            "never actually changes",
            "As numbers rise, fewer get enough resources, so births fall "
            "and deaths rise",
            "It has no effect on numbers, because members of a species "
            "always share resources",
        ],
        "correct_index": 2,
        "why": "The more crowded the population, the smaller each "
               "individual's share of food and space, so growth slows as "
               "the population approaches its limit.",
    },
    {
        "id": "ks4-population-competition-s04",
        "subtopic_slug": "population-competition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two species of barnacle live on the same rocks and both "
                "need space to attach to. Name the type of competition and "
                "suggest the outcome if one species is the stronger "
                "competitor.",
        "options": [
            "Intraspecific competition, and the weaker species will grow "
            "larger shells",
            "Intraspecific competition, and the two species will settle on "
            "separate rocks",
            "Interspecific competition, and both of the species will always "
            "survive equally",
            "Interspecific competition, and the weaker species may die out "
            "locally",
        ],
        "correct_index": 3,
        "why": "The two barnacles are different species competing for the "
               "same resource, and the stronger competitor can exclude the "
               "weaker one from that shore.",
    },
    {
        "id": "ks4-population-competition-h01",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Oak seedlings grow densely under a parent oak, but very "
                "few of them survive to become saplings. Explain this using "
                "competition.",
        "options": [
            "The parent tree poisons its own seedlings so that they cannot "
            "compete with it",
            "The seedlings compete with the parent tree, but never with one "
            "another at all",
            "Seedlings survive only if a predator removes the parent tree "
            "from above them",
            "The seedlings compete with each other and the parent for light "
            "and water",
        ],
        "correct_index": 3,
        "why": "Crowded seedlings under a large canopy are short of both "
               "light and water, so only a few can obtain enough to keep "
               "growing.",
    },
    {
        "id": "ks4-population-competition-h02",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lake is overfished until too few adult fish are left to "
                "find each other and breed. Suggest why the population may "
                "not recover even after fishing stops.",
        "options": [
            "Fish are only able to breed when a predator is present to "
            "disturb them",
            "Too few adults remain to produce enough young to replace the "
            "losses",
            "Fishing changes the water chemistry permanently, so that no "
            "eggs can hatch",
            "The remaining fish compete so hard for food that they stop "
            "growing at all",
        ],
        "correct_index": 1,
        "why": "Below a certain number, births cannot keep pace with "
               "natural deaths, so the population keeps shrinking even with "
               "the original pressure removed.",
    },
    {
        "id": "ks4-population-competition-h03",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two grassland plots are the same size. Plot 1 is grazed by "
                "20 sheep and plot 2 by 60 sheep. After one summer the mean "
                "mass of a sheep is 51 kg in plot 1 and 34 kg in plot 2. "
                "Explain the difference.",
        "options": [
            "Competition for grass was more intense in plot 2, so each "
            "sheep ate less",
            "The sheep in plot 2 were younger, so they had less time to put "
            "on any mass",
            "The sheep in plot 1 had more predators, so they grew larger to "
            "defend themselves",
            "Plot 2 had a lower soil pH, which stops sheep from digesting "
            "grass properly",
        ],
        "correct_index": 0,
        "why": "The same amount of grass shared between three times as many "
               "sheep gives each animal a smaller share, so they gain less "
               "mass.",
    },
    {
        "id": "ks4-population-competition-h04",
        "subtopic_slug": "population-competition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A conservationist plans to raise the deer population of a "
                "reserve by putting out extra food each winter. Evaluate "
                "this plan.",
        "options": [
            "It will fail, because deer will only ever eat food that they "
            "have found themselves",
            "It will work permanently, because food is the only factor that "
            "limits deer numbers",
            "It may raise numbers until another resource, such as space, "
            "runs short",
            "It will lower deer numbers, because the feeding stations "
            "attract more predators",
        ],
        "correct_index": 2,
        "why": "A population is held at whichever resource runs out first, "
               "so relieving one limit simply moves the ceiling to the "
               "next one.",
    },

    # ── biodiversity ────────────────────────────────────────────────────
    {
        "id": "ks4-biodiversity-e01",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by biodiversity.",
        "options": [
            "The total number of individual organisms living in an area",
            "The variety of different living things found in an area",
            "The number of predators an ecosystem is able to support",
            "The amount of energy stored in the producers of an area",
        ],
        "correct_index": 1,
        "why": "Biodiversity is about variety — how many different species "
               "there are, and how evenly common each of them is.",
    },
    {
        "id": "ks4-biodiversity-e02",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name a medicine that came originally from a wild species.",
        "options": [
            "Aspirin, from the bark of the willow tree",
            "Penicillin, from the bark of the Pacific yew",
            "A cancer drug, from a mould growing on fruit",
            "Insulin, from the leaves of a fern plant",
        ],
        "correct_index": 0,
        "why": "Aspirin was developed from a compound in willow bark — one "
               "of many drugs that began as a chemical found in a wild "
               "organism.",
    },
    {
        "id": "ks4-biodiversity-e03",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a threat to biodiversity?",
        "options": [
            "Restoring a drained wetland back to marsh",
            "Setting a quota that limits a fishing catch",
            "Draining a wetland to build a car park",
            "Planting a mixed hedge around a field",
        ],
        "correct_index": 2,
        "why": "Draining and building destroys the habitat, so the species "
               "that lived there are lost from that area.",
    },
    {
        "id": "ks4-biodiversity-e04",
        "subtopic_slug": "biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these changes would reduce the biodiversity of a "
                "farm?",
        "options": [
            "Leaving a wide, uncut margin around each field",
            "Planting a mixture of crop species in one field",
            "Digging a pond in the corner of a field",
            "Replacing a mixed hedge with a wire fence",
        ],
        "correct_index": 3,
        "why": "A hedge is a habitat that feeds and shelters many species; "
               "a wire fence is not, so removing it takes those species "
               "off the farm.",
    },
    {
        "id": "ks4-biodiversity-s01",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Wood A holds 30 plant species and no species makes up more "
                "than 8% of the plants present. Wood B also holds 30 "
                "species, but one of them makes up 92% of the plants "
                "present. Compare the biodiversity of the two woods.",
        "options": [
            "They are equal, because biodiversity counts only the number of "
            "species present",
            "Wood B is higher, because one of its species is clearly doing "
            "extremely well",
            "Wood B is higher, because it must contain more individual "
            "plants altogether",
            "Wood A is higher, because its species are present in more even "
            "numbers",
        ],
        "correct_index": 3,
        "why": "Biodiversity depends on relative abundance as well as "
               "species count, so a wood dominated by one species is less "
               "diverse in practice.",
    },
    {
        "id": "ks4-biodiversity-s02",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "About 75% of the world's food crops depend on animal "
                "pollinators. Suggest the effect on the human food supply "
                "if pollinator diversity falls sharply.",
        "options": [
            "Food supply rises, because crops then keep more of their "
            "energy for growth",
            "Food supply falls, because fewer crop plants are pollinated "
            "and set fruit",
            "Food supply is unchanged, because crop plants are all able to "
            "pollinate themselves",
            "Food supply rises, because farmers simply plant more crops to "
            "make up the loss",
        ],
        "correct_index": 1,
        "why": "Most crops need an animal to move pollen between flowers, "
               "so losing pollinators means fewer fruits and seeds are "
               "produced.",
    },
    {
        "id": "ks4-biodiversity-s03",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how an ecosystem with many species can be more "
                "resilient when one of those species declines.",
        "options": [
            "Other species can take over the role of the one that has "
            "declined",
            "The remaining species reproduce far faster to fill the empty "
            "space",
            "The declining species always recovers if enough others are "
            "present",
            "More species means less competition, so nothing is ever lost "
            "at all",
        ],
        "correct_index": 0,
        "why": "More species means more connections and more overlap in "
               "roles, so the loss of one does not break the whole web.",
    },
    {
        "id": "ks4-biodiversity-s04",
        "subtopic_slug": "biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A river runs through a wide belt of marsh plants before it "
                "reaches a town's water supply. Explain how this benefits "
                "the town.",
        "options": [
            "The marsh plants add extra minerals to the water for people to "
            "drink",
            "The marsh plants raise the temperature of the water before it "
            "arrives",
            "The marsh and its soil organisms filter pollutants out of the "
            "water",
            "The marsh plants release oxygen that kills the bacteria in the "
            "water",
        ],
        "correct_index": 2,
        "why": "Clean water is an ecosystem service: wetland plants and "
               "soil organisms trap and break down pollutants before the "
               "water moves on.",
    },
    {
        "id": "ks4-biodiversity-h01",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A new road is built through a wood, splitting it into two "
                "smaller pieces. Suggest why biodiversity may fall even "
                "though no trees are cut down beyond the line of the road.",
        "options": [
            "The road adds new species, which take resources from the "
            "original ones",
            "The two smaller pieces receive less rainfall than the whole "
            "wood once did",
            "Each piece is too small for some species, and populations "
            "cannot mix",
            "Splitting a wood halves the light reaching every tree in both "
            "of the pieces",
        ],
        "correct_index": 2,
        "why": "Species that need a large territory can no longer be "
               "supported, and separated populations lose the exchange of "
               "individuals that keeps them going.",
    },
    {
        "id": "ks4-biodiversity-h02",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country plans to reintroduce beavers to a river valley "
                "where they were once native. Suggest one way this could "
                "raise local biodiversity.",
        "options": [
            "Beavers eat the invasive plants that no other local species "
            "will touch",
            "Beavers hunt the predators that had been killing the birds of "
            "the valley",
            "Beavers carry the seeds of rare plants in their fur from other "
            "countries",
            "Beaver dams create ponds and wetland, giving habitats for more "
            "species",
        ],
        "correct_index": 3,
        "why": "By damming, beavers build new habitats, and new habitats "
               "give more species somewhere to live in the valley.",
    },
    {
        "id": "ks4-biodiversity-h03",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two plans for an endangered marsh bird are compared. Plan "
                "A breeds the birds in a zoo. Plan B protects and restores "
                "the marsh they live in. Evaluate which is more likely to "
                "keep the species alive in the wild in the long term.",
        "options": [
            "Plan A, because a zoo can raise far more chicks each year than "
            "a marsh can",
            "Plan B, because the birds need a habitat to return to and to "
            "live in",
            "Plan A, because birds bred in a zoo no longer need any wild "
            "habitat at all",
            "Plan B, because a restored marsh needs no further money once "
            "it is finished",
        ],
        "correct_index": 1,
        "why": "Breeding animals is pointless without somewhere to release "
               "them, so protecting the habitat is what keeps a wild "
               "population going.",
    },
    {
        "id": "ks4-biodiversity-h04",
        "subtopic_slug": "biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that an area holding 500 rabbits and "
                "nothing else has higher biodiversity than an area holding "
                "50 organisms from 12 different species. Evaluate this "
                "statement.",
        "options": [
            "It is wrong, because biodiversity is about variety of species, "
            "not total numbers",
            "It is right, because the area with 500 rabbits has far more "
            "living organisms in it",
            "It is right, because rabbits are a species and 500 is greater "
            "than 50 in every case",
            "It is wrong, because 12 species will always weigh more "
            "together than 500 rabbits do",
        ],
        "correct_index": 0,
        "why": "A large population of one species is still one species; "
               "biodiversity counts how many different species there are "
               "and how evenly they occur.",
    },

    # ── waste-management ────────────────────────────────────────────────
    {
        "id": "ks4-waste-management-e01",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Complete the sentence. Pollution reduces biodiversity "
                "because it...",
        "options": [
            "forces organisms to migrate for a season and then return",
            "raises the number of different species living in the area",
            "damages habitats and kills plants and animals",
            "only affects the appearance of a habitat, not its species",
        ],
        "correct_index": 2,
        "why": "Pollutants destroy habitats and kill organisms outright, so "
               "both the number of species and their numbers fall.",
    },
    {
        "id": "ks4-waste-management-e02",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas released by burning fuels that causes acid "
                "rain.",
        "options": [
            "Carbon dioxide",
            "Sulfur dioxide",
            "Nitrogen",
            "Oxygen",
        ],
        "correct_index": 1,
        "why": "Sulfur dioxide is the acidic gas released when fuels "
               "containing sulfur are burned, and it dissolves in rain "
               "water to make it acidic.",
    },
    {
        "id": "ks4-waste-management-e03",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which two changes together are increasing the amount of "
                "waste that humans produce?",
        "options": [
            "A growing population and a rising standard of living",
            "A falling population and a rising standard of living",
            "A growing population and a falling standard of living",
            "A falling population and a falling standard of living",
        ],
        "correct_index": 0,
        "why": "More people, each using more resources, means more waste — "
               "both factors push in the same direction.",
    },
    {
        "id": "ks4-waste-management-e04",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a way of reducing pollution rather than "
                "a source of it?",
        "options": [
            "Spraying more herbicide onto a crop field",
            "Releasing untreated sewage into a river",
            "Burying more household waste in landfill",
            "Treating sewage before it enters a river",
        ],
        "correct_index": 3,
        "why": "Treating sewage removes the material that would otherwise "
               "decay in the river and strip out its oxygen.",
    },
    {
        "id": "ks4-waste-management-s01",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fertiliser washes off a field into a lake. Describe the "
                "sequence of events that follows.",
        "options": [
            "Algae grow rapidly, then die and decay, using up oxygen so "
            "fish die",
            "Algae grow rapidly and release so much oxygen that the fish "
            "are poisoned",
            "The fertiliser sinks to the bottom, where it feeds the fish in "
            "the lake",
            "The fertiliser kills the algae first, so the fish then have "
            "nothing to eat",
        ],
        "correct_index": 0,
        "why": "The extra nutrients cause an algal bloom; when the algae "
               "die, the decomposers breaking them down use up the "
               "dissolved oxygen, and the fish suffocate.",
    },
    {
        "id": "ks4-waste-management-s02",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how acid rain can damage a forest that is many "
                "kilometres from the factory that released the gases.",
        "options": [
            "Acid rain is made inside the trees once they have absorbed the "
            "gases",
            "The gases travel through the soil from the factory to the "
            "forest roots",
            "Acid rain only ever forms over forests, and never over the "
            "towns nearby",
            "The gases are carried in the air and fall as acid rain far "
            "downwind",
        ],
        "correct_index": 3,
        "why": "Acidic gases mix into the atmosphere and travel with the "
               "wind, so the rain that carries them down can fall a long "
               "way from the source.",
    },
    {
        "id": "ks4-waste-management-s03",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a pesticide sprayed on a field can end up "
                "polluting a nearby river.",
        "options": [
            "Pesticides evaporate into the clouds and fall again as "
            "pesticide rain",
            "Rain washes the pesticide down through the soil and into the "
            "river",
            "Farm animals carry the pesticide down to the river on their "
            "feet",
            "Pesticides are made from river water, so they always return to "
            "it",
        ],
        "correct_index": 1,
        "why": "Chemicals sprayed on land do not stay there: rainfall "
               "carries them through the soil into streams and rivers.",
    },
    {
        "id": "ks4-waste-management-s04",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says pollution only matters when you can see it. "
                "Explain why this is wrong.",
        "options": [
            "Visible pollution is harmless, because organisms learn to "
            "avoid it",
            "All pollution can be seen if a habitat is looked at closely "
            "enough",
            "Sewage, fertiliser and acidic gases do harm without being seen",
            "Pollution matters only in water, where it cannot be seen from "
            "land",
        ],
        "correct_index": 2,
        "why": "The pollutants that do the most damage to biodiversity — "
               "dissolved sewage, fertiliser and acidic gases — are "
               "invisible in the water or the air.",
    },
    {
        "id": "ks4-waste-management-h01",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A town produces 40 000 tonnes of waste a year and recycles "
                "10% of it. Its population then doubles, and its recycling "
                "rate rises to 60%. Calculate the mass of waste now sent to "
                "landfill each year.",
        "options": [
            "16 000 tonnes",
            "48 000 tonnes",
            "36 000 tonnes",
            "32 000 tonnes",
        ],
        "correct_index": 3,
        "why": "Doubling gives 80 000 tonnes, and 40% of it is not "
               "recycled: 80 000 x 0.40 = 32 000 tonnes to landfill.",
    },
    {
        "id": "ks4-waste-management-h02",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Country X has a stable population but its waste per person "
                "has risen by 40% in ten years. Country Y's population has "
                "risen by 40% but its waste per person is unchanged. "
                "Compare the change in total waste in each country.",
        "options": [
            "Country X rose by more, because waste per person matters more "
            "than numbers",
            "Country Y rose by more, because population size matters more "
            "than habits",
            "Both rose by about the same, because 40% applies to one factor "
            "in each",
            "Neither total changed, because only one of the two factors "
            "changed in each",
        ],
        "correct_index": 2,
        "why": "Total waste is the number of people multiplied by the waste "
               "each produces, so a 40% rise in either factor raises the "
               "total by about 40%.",
    },
    {
        "id": "ks4-waste-management-h03",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A river below a sewage works holds far fewer species than "
                "the same river above it. The water temperature and pH are "
                "the same at both points. Suggest the cause of the drop in "
                "species number.",
        "options": [
            "Decay of the sewage uses up the oxygen, so species needing it "
            "die",
            "The sewage raises the water temperature, so most species move "
            "away",
            "The sewage lowers the pH, so most of the species are killed by "
            "acid",
            "There is no cause — species numbers vary at random along any "
            "river",
        ],
        "correct_index": 0,
        "why": "Microorganisms decaying the sewage respire and strip "
               "dissolved oxygen from the water, which the stem shows "
               "cannot be explained by temperature or pH.",
    },
    {
        "id": "ks4-waste-management-h04",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that recycling more household waste "
                "helps to protect biodiversity.",
        "options": [
            "The claim is wrong, because landfill sites are habitats for "
            "many species",
            "The claim is reasonable, because less land is buried under "
            "waste",
            "The claim is wrong, because recycling has no effect on land "
            "use at all",
            "The claim is reasonable, because recycling removes the gases "
            "causing acid rain",
        ],
        "correct_index": 1,
        "why": "Recycled material does not go to landfill, so less habitat "
               "is destroyed by burying waste and fewer toxic chemicals "
               "leak into the soil.",
    },

    # ── land-use ────────────────────────────────────────────────────────
    {
        "id": "ks4-land-use-e01",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why dead plants do not fully decay in a peat bog.",
        "options": [
            "The plants there are too tough for any decomposer to break "
            "down",
            "The temperature in a peat bog is too high for decomposers to "
            "survive",
            "There are no decomposer organisms present anywhere in a peat "
            "bog",
            "The ground is waterlogged, so there is too little oxygen for "
            "decay",
        ],
        "correct_index": 3,
        "why": "Decomposers need oxygen to respire, and waterlogged ground "
               "holds very little, so the plant material is only partly "
               "broken down.",
    },
    {
        "id": "ks4-land-use-e02",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what peat is mainly extracted and sold for.",
        "options": [
            "Compost for gardens and for growing food",
            "Building blocks for houses and for walls",
            "Making paper and cardboard packaging",
            "Filtering drinking water at treatment works",
        ],
        "correct_index": 0,
        "why": "Most extracted peat is sold as compost; burning it as a "
               "fuel is the smaller use.",
    },
    {
        "id": "ks4-land-use-e03",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Over what timescale does peat build up in a bog?",
        "options": [
            "A few days",
            "A few months",
            "Thousands of years",
            "A single decade",
        ],
        "correct_index": 2,
        "why": "Peat accumulates only as fast as partly-decayed plants pile "
               "up, which takes thousands of years — so a bog dug out today "
               "cannot be replaced in a lifetime.",
    },
    {
        "id": "ks4-land-use-e04",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas released into the atmosphere when drained "
                "peat decays.",
        "options": [
            "Oxygen",
            "Carbon dioxide",
            "Nitrogen",
            "Hydrogen",
        ],
        "correct_index": 1,
        "why": "The carbon locked in the partly-decayed plants is released "
               "as carbon dioxide once decay can finish in the air.",
    },
    {
        "id": "ks4-land-use-s01",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two different ways in which destroying a peat bog "
                "harms the environment.",
        "options": [
            "It releases carbon dioxide, and it lowers the water table of "
            "nearby rivers",
            "It reduces biodiversity, and it makes the soil around it more "
            "acidic",
            "It releases carbon dioxide, and it destroys a habitat so "
            "biodiversity falls",
            "It reduces biodiversity, and it stops sunlight reaching the "
            "plants below",
        ],
        "correct_index": 2,
        "why": "Peat destruction does two separate harms: the stored carbon "
               "escapes as carbon dioxide, and a specialised habitat and "
               "its species are lost.",
    },
    {
        "id": "ks4-land-use-s02",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A quarry is dug into a hillside that was rough grassland. "
                "Explain the effect on the species that lived there.",
        "options": [
            "Their numbers rise, because the quarry exposes new minerals "
            "for plants",
            "They lose their habitat, so their numbers and species variety "
            "fall",
            "They are unaffected, because animals simply walk to the next "
            "hillside",
            "Their numbers rise, because a quarry holds fewer predators "
            "than grassland",
        ],
        "correct_index": 1,
        "why": "Quarrying removes the ground the community lived on, and "
               "with the habitat gone the species that depended on it "
               "cannot stay.",
    },
    {
        "id": "ks4-land-use-s03",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why peat bogs hold a large store of carbon.",
        "options": [
            "Peat bogs absorb carbon dioxide straight from the air through "
            "the water",
            "Bog water holds dissolved carbon that soaks into the peat over "
            "time",
            "Peat is a rock, and all rocks contain large amounts of stored "
            "carbon",
            "Dead plants only partly decay, so the carbon in them stays "
            "locked up",
        ],
        "correct_index": 3,
        "why": "Carbon that plants took in during photosynthesis is never "
               "released, because the waterlogged conditions stop decay "
               "finishing.",
    },
    {
        "id": "ks4-land-use-s04",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A landfill site is opened on what had been farmland. "
                "Describe two effects this has on other species.",
        "options": [
            "Habitat is lost, and toxic chemicals may leak into soil and "
            "water",
            "Habitat is gained, and the buried waste feeds the local soil "
            "organisms",
            "Nothing changes, because the waste is buried below the level "
            "of the roots",
            "The soil becomes richer, so more plant species can grow on the "
            "surface",
        ],
        "correct_index": 0,
        "why": "Dumping waste takes the land out of use for wild species "
               "and adds toxic chemicals that can spread into the "
               "surrounding soil and water.",
    },
    {
        "id": "ks4-land-use-h01",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Destroying a peat bog only matters "
                "because it releases carbon dioxide.' Evaluate this "
                "statement.",
        "options": [
            "It is complete, because carbon dioxide release is by far the "
            "only real effect",
            "It is incomplete, because a rare habitat and its species are "
            "also lost",
            "It is wrong, because destroying a peat bog releases no carbon "
            "dioxide at all",
            "It is wrong, because peat bogs hold very few species that are "
            "worth protecting",
        ],
        "correct_index": 1,
        "why": "Peat destruction does two harms, and this statement names "
               "only one: the bog is also a specialised habitat whose "
               "biodiversity is lost with it.",
    },
    {
        "id": "ks4-land-use-h02",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A peat bog that was drained for farmland 40 years ago "
                "is deliberately re-wetted. Predict the effect on the "
                "carbon still stored in the remaining peat.",
        "options": [
            "Decay slows as oxygen is excluded, so the carbon left stays "
            "locked in",
            "Decay speeds up, because the water carries oxygen down into "
            "the peat",
            "The carbon already lost from the peat is drawn back out of "
            "the air",
            "Nothing changes at all, because peat decays at the same rate "
            "wet or dry",
        ],
        "correct_index": 0,
        "why": "Waterlogging keeps oxygen away from the decomposers, so "
               "the partly-decayed plant material stops breaking down and "
               "holds on to its carbon.",
    },
    {
        "id": "ks4-land-use-h03",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A council must build 200 homes either on a derelict "
                "brownfield site or on a meadow of the same area. Evaluate "
                "which choice does less harm to biodiversity.",
        "options": [
            "The meadow, because a derelict site holds species that a "
            "meadow does not",
            "Either one, because building the same number of homes has the "
            "same effect",
            "The meadow, because meadow species can simply move to the next "
            "field along",
            "The brownfield site, because the meadow is an established "
            "wildlife habitat",
        ],
        "correct_index": 3,
        "why": "Building on land that is already spoilt destroys far less "
               "living habitat than building on an intact community of "
               "meadow species.",
    },
    {
        "id": "ks4-land-use-h04",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A garden centre claims its peat compost is environmentally "
                "friendly 'because the bog is replanted afterwards'. "
                "Evaluate this claim.",
        "options": [
            "The claim is fair, because replanting replaces every species "
            "that was lost",
            "The claim is fair, because peat re-forms within a few years of "
            "replanting",
            "The claim is weak, because peat takes thousands of years to "
            "build up again",
            "The claim is weak, because replanting a bog releases even more "
            "carbon dioxide",
        ],
        "correct_index": 2,
        "why": "Replanting cannot undo the loss on any useful timescale: "
               "the carbon has already gone into the air and the peat "
               "itself takes millennia to reform.",
    },

    # ── deforestation ───────────────────────────────────────────────────
    {
        "id": "ks4-deforestation-e01",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of fuel made from crops grown on cleared "
                "tropical forest land.",
        "options": [
            "Biofuel",
            "Coal",
            "Natural gas",
            "Crude oil",
        ],
        "correct_index": 0,
        "why": "Biofuels such as ethanol are made from plants, so growing "
               "them takes land — and clearing forest is one way that land "
               "is found.",
    },
    {
        "id": "ks4-deforestation-e02",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is the richest habitat on Earth for "
                "species?",
        "options": [
            "A planted conifer plantation",
            "A managed orchard of fruit trees",
            "A row of trees along a road",
            "A tropical rainforest",
        ],
        "correct_index": 3,
        "why": "Tropical rainforests hold more species than any other "
               "habitat, which is why clearing them costs so much "
               "biodiversity.",
    },
    {
        "id": "ks4-deforestation-e03",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to biodiversity when a large area of "
                "tropical forest is cleared.",
        "options": [
            "It rises, because grassland species move in to replace forest "
            "ones",
            "It falls, because the habitat of very many species is "
            "destroyed",
            "It stays the same, because the species simply move to another "
            "forest",
            "It rises, because more sunlight reaches the ground once the "
            "trees are gone",
        ],
        "correct_index": 1,
        "why": "The forest is the habitat those species depend on, so "
               "removing it makes many of them locally extinct.",
    },
    {
        "id": "ks4-deforestation-e04",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process by which trees remove carbon dioxide from "
                "the air.",
        "options": [
            "Respiration",
            "Decomposition",
            "Photosynthesis",
            "Combustion",
        ],
        "correct_index": 2,
        "why": "Photosynthesis takes carbon dioxide in and locks the carbon "
               "into the tree's own biomass.",
    },
    {
        "id": "ks4-deforestation-s01",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the two separate ways in which deforestation "
                "raises the amount of carbon dioxide in the atmosphere.",
        "options": [
            "Fewer trees respire, and the soil under them stops absorbing "
            "the gas",
            "Trees stop producing oxygen, and burning uses up the oxygen "
            "that is left",
            "Less is absorbed by photosynthesis, and burning and decay "
            "release more",
            "Rainfall falls, so less carbon dioxide dissolves into the "
            "rivers below",
        ],
        "correct_index": 2,
        "why": "Removing the trees takes away a carbon sink, and burning or "
               "rotting the felled wood turns the carbon they had stored "
               "back into carbon dioxide.",
    },
    {
        "id": "ks4-deforestation-s02",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company replants a cleared area with a single "
                "fast-growing tree species. Explain why biodiversity there "
                "stays much lower than in the original rainforest.",
        "options": [
            "One tree species supports far fewer other species than a "
            "varied forest",
            "Fast-growing trees release chemicals that kill all the other "
            "forest plants",
            "Replanted trees are too young to take any carbon dioxide out "
            "of the air",
            "The soil is permanently destroyed, so nothing at all is able "
            "to grow there",
        ],
        "correct_index": 0,
        "why": "A rainforest's biodiversity rests on the variety of plants "
               "that feed and shelter everything else, and a single-species "
               "plantation cannot provide it.",
    },
    {
        "id": "ks4-deforestation-s03",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rice fields are one reason tropical forests are cleared. "
                "Suggest why the demand for this land is rising.",
        "options": [
            "Rice grows better on ground that has recently been burned over",
            "Rice cannot be grown anywhere except on former forest land",
            "Forest soil never needs any fertiliser adding to grow rice in",
            "The human population is growing and needs more food grown",
        ],
        "correct_index": 3,
        "why": "More people need more food, and the simplest way to grow "
               "more has often been to clear more land.",
    },
    {
        "id": "ks4-deforestation-s04",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why losing rainforest species may harm human "
                "medicine.",
        "options": [
            "Rainforest air is used to make antibiotics in hospital "
            "laboratories",
            "Species may be lost before their useful chemicals are ever "
            "found",
            "Doctors need rainforest soil to grow the bacteria used in "
            "vaccines",
            "Rainforest trees make the oxygen that hospital patients need "
            "to breathe",
        ],
        "correct_index": 1,
        "why": "Many drugs began as chemicals found in wild organisms, so "
               "every species lost is a possible medicine lost with it.",
    },
    {
        "id": "ks4-deforestation-h01",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A biofuel company says its fuel is 'carbon neutral, "
                "because the crops absorb carbon dioxide as they grow'. "
                "Evaluate this claim when the crops are grown on newly "
                "cleared rainforest.",
        "options": [
            "The claim holds, because the crops absorb exactly what the "
            "fuel releases",
            "The claim is weak, because clearing the forest first released "
            "stored carbon",
            "The claim holds, because forest and crops absorb carbon at "
            "exactly the same rate",
            "The claim is weak, because crop plants do not photosynthesise "
            "at all",
        ],
        "correct_index": 1,
        "why": "The accounting leaves out the clearing: burning and rotting "
               "the felled forest put a large store of carbon into the air "
               "before the first crop grew.",
    },
    {
        "id": "ks4-deforestation-h02",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In one region, 500 square kilometres of forest is cleared "
                "each year. Each square kilometre of that forest removes "
                "250 tonnes of carbon dioxide from the air per year. "
                "Calculate the mass of carbon dioxide no longer removed "
                "after one year of clearing.",
        "options": [
            "1250 tonnes",
            "12 500 tonnes",
            "125 000 tonnes",
            "1 250 000 tonnes",
        ],
        "correct_index": 2,
        "why": "500 x 250 = 125 000 tonnes of carbon dioxide a year that "
               "the cleared forest can no longer take out of the air.",
    },
    {
        "id": "ks4-deforestation-h03",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two cleared areas of equal size are compared 20 years "
                "later. Area P was left alone and has regrown as young "
                "forest. Area Q is still grazed by cattle. Predict which "
                "now holds more carbon, and explain.",
        "options": [
            "Area P, because regrown trees have taken carbon back into "
            "their biomass",
            "Area Q, because the cattle breathe out carbon dioxide that the "
            "grass absorbs",
            "Both hold the same, because carbon cannot be stored by young "
            "trees at all",
            "Area Q, because grassland is able to store far more carbon "
            "than any forest",
        ],
        "correct_index": 0,
        "why": "Growing trees photosynthesise faster than they respire, so "
               "carbon accumulates in their wood — grazed grassland stores "
               "very little by comparison.",
    },
    {
        "id": "ks4-deforestation-h04",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A government claims that planting 10 million trees will "
                "cancel out the effect of clearing an area of old "
                "rainforest. Evaluate this claim.",
        "options": [
            "The claim is right, because the number of trees is what "
            "matters most",
            "The claim is right, because new trees photosynthesise faster "
            "than old ones",
            "The claim is wrong, because young trees do not photosynthesise "
            "at all",
            "The claim is weak, because the rainforest's species cannot be "
            "replanted",
        ],
        "correct_index": 3,
        "why": "New trees may recover some of the carbon, but the lost "
               "biodiversity of an old rainforest cannot be planted back.",
    },

    # ── global-warming ──────────────────────────────────────────────────
    {
        "id": "ks4-global-warming-e01",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two greenhouse gases whose atmospheric levels are "
                "rising.",
        "options": [
            "Oxygen and nitrogen",
            "Carbon dioxide and methane",
            "Hydrogen and helium",
            "Argon and neon",
        ],
        "correct_index": 1,
        "why": "Carbon dioxide and methane are the two greenhouse gases "
               "human activity is adding to the atmosphere fastest.",
    },
    {
        "id": "ks4-global-warming-e02",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a greenhouse gas does in the atmosphere.",
        "options": [
            "It reflects all of the sunlight back into space before it "
            "arrives",
            "It destroys the ozone layer that shields the Earth from "
            "harmful rays",
            "It traps heat energy near the Earth's surface",
            "It reacts with oxygen and warms the air by burning",
        ],
        "correct_index": 2,
        "why": "Greenhouse gases hold heat energy near the surface instead "
               "of letting it escape, which is what raises the Earth's "
               "average temperature.",
    },
    {
        "id": "ks4-global-warming-e03",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which human activity releases carbon dioxide that adds to "
                "global warming?",
        "options": [
            "Planting a new woodland on farmland",
            "Restoring a drained peat bog to marsh",
            "Fitting a house with better insulation",
            "Burning coal in a power station",
        ],
        "correct_index": 3,
        "why": "Burning a fossil fuel releases carbon that had been locked "
               "underground; the other three all reduce emissions or store "
               "carbon.",
    },
    {
        "id": "ks4-global-warming-e04",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Spring is arriving earlier in the UK. Predict the effect "
                "on birds that migrate here to breed.",
        "options": [
            "They may arrive earlier, to match the earlier spring",
            "They stop migrating altogether and die out in one season",
            "They fly at a much higher altitude to keep cool on the way",
            "They change from eating insects to eating only plant seeds",
        ],
        "correct_index": 0,
        "why": "Migrating birds time their journey to the season, so a "
               "shifted season shifts their arrival with it.",
    },
    {
        "id": "ks4-global-warming-s01",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a species living near the top of a mountain "
                "may become extinct as the climate warms.",
        "options": [
            "Mountain tops receive more sunlight, which burns the plants "
            "growing there",
            "Warming makes the mountain rock unstable, so the habitat "
            "falls away",
            "The species can simply move downhill, where the conditions "
            "are cooler",
            "It can only move upwards to stay cool, and runs out of "
            "mountain",
        ],
        "correct_index": 3,
        "why": "Cooler conditions lie higher up, so a warming climate "
               "squeezes a mountain species into an ever-smaller area until "
               "there is none left.",
    },
    {
        "id": "ks4-global-warming-s02",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why rising sea levels reduce biodiversity.",
        "options": [
            "Coastal habitats are flooded, so the species living there are "
            "lost",
            "Salt water is heavier than fresh water, so it crushes the "
            "seabed below",
            "Deeper seas absorb more sunlight, so no marine plants are able "
            "to grow",
            "Sea level rise makes the air saltier, which kills plants far "
            "inland",
        ],
        "correct_index": 0,
        "why": "Coastal habitats such as salt marsh and mudflat are drowned "
               "as the sea rises, and the species that depended on them "
               "have nowhere else to go.",
    },
    {
        "id": "ks4-global-warming-s03",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says global warming is caused by a hole in the "
                "ozone layer. Explain the error.",
        "options": [
            "The ozone layer does trap heat, but the hole in it has now "
            "closed up",
            "Greenhouse gases trapping heat cause warming, not ozone loss",
            "The ozone layer is made of methane, which is a greenhouse gas",
            "There is no error, because ozone and carbon dioxide are the "
            "same gas",
        ],
        "correct_index": 1,
        "why": "Ozone damage and the greenhouse effect are two separate "
               "problems: warming comes from gases holding heat in, not "
               "from ozone letting rays through.",
    },
    {
        "id": "ks4-global-warming-s04",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a species that cannot move quickly, such as a "
                "tree, is at particular risk from rapid climate change.",
        "options": [
            "Trees do not respond to temperature at all, so they are killed "
            "at once",
            "Trees compete with each other, and warming puts a stop to that "
            "competition",
            "Its range can only shift as fast as its seeds are spread and "
            "grow",
            "Trees absorb carbon dioxide, so warming affects them more than "
            "animals",
        ],
        "correct_index": 2,
        "why": "A tree cannot walk to cooler ground: its distribution moves "
               "only at the speed its seeds disperse and germinate, which "
               "may be far slower than the climate changes.",
    },
    {
        "id": "ks4-global-warming-h01",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Different computer models of future warming do not all "
                "agree. A student concludes that global warming is "
                "therefore not really happening. Evaluate this conclusion.",
        "options": [
            "It is wrong: uncertainty in predictions does not undo the "
            "measured trend",
            "It is right, because scientists must all agree before anything "
            "is true",
            "It is wrong, because scientific models are never uncertain "
            "about anything",
            "It is right, because global temperature has not actually been "
            "measured",
        ],
        "correct_index": 0,
        "why": "Recorded temperature, carbon dioxide and ice data show the "
               "trend clearly; the models disagree about how much more "
               "warming is coming, not about whether it is happening.",
    },
    {
        "id": "ks4-global-warming-h02",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In 1980 a butterfly species was found no further north "
                "than 52 degrees north. By 2020 it was found as far north "
                "as 57 degrees north. State what has changed, and suggest "
                "the cause.",
        "options": [
            "Its abundance has risen, because more butterflies now hatch "
            "each year",
            "Its abundance has fallen, because it can no longer live in the "
            "south",
            "Its habitat has been destroyed, so it was forced to move "
            "northwards",
            "Its distribution has shifted north as warming made cooler "
            "areas suitable",
        ],
        "correct_index": 3,
        "why": "The data give the area the species occupies, not its "
               "numbers, and warming has made ground that was once too cold "
               "warm enough to live on.",
    },
    {
        "id": "ks4-global-warming-h03",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country cuts its own carbon dioxide emissions to zero, "
                "but global temperatures keep rising. Explain why.",
        "options": [
            "Cutting emissions in one place makes every other country emit "
            "far more",
            "Carbon dioxide is not actually a cause of the rise in global "
            "temperature",
            "Warming depends on emissions worldwide, not from one country",
            "Temperature always keeps rising for 100 years after emissions "
            "are stopped",
        ],
        "correct_index": 2,
        "why": "Greenhouse gases mix through the whole atmosphere, so the "
               "warming responds to total global emissions rather than to "
               "any one country's.",
    },
    {
        "id": "ks4-global-warming-h04",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two reserves protect the same rare plant. Reserve A is a "
                "small island. Reserve B is a long strip running south to "
                "north across a range of altitudes. Evaluate which is more "
                "likely to keep the plant as the climate warms.",
        "options": [
            "Reserve A, because an island is protected from the warming of "
            "the land",
            "Reserve B, because the plant can shift to cooler ground within "
            "it",
            "Reserve A, because a smaller reserve is easier to hold at one "
            "temperature",
            "Reserve B, because a longer reserve holds more individual "
            "plants in total",
        ],
        "correct_index": 1,
        "why": "A reserve that spans a range of latitudes and heights lets "
               "the species' distribution move as conditions change; an "
               "island offers nowhere cooler to go.",
    },

    # ── maintaining-biodiversity ────────────────────────────────────────
    {
        "id": "ks4-maintaining-biodiversity-e01",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a programme designed to maintain "
                "biodiversity?",
        "options": [
            "Draining a marsh so that it can be farmed",
            "Spraying a wider range of pesticides on crops",
            "Regenerating a rare habitat by replanting it",
            "Building a new road through a nature reserve",
        ],
        "correct_index": 2,
        "why": "Protecting and regenerating rare habitats is one of the "
               "active programmes used to keep species and their ecosystems "
               "going.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e02",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Complete the sentence. Governments can help maintain "
                "biodiversity by...",
        "options": [
            "increasing the rate at which forests are cleared",
            "removing the laws that protect rare species",
            "encouraging more waste to be sent to landfill",
            "reducing deforestation and carbon dioxide emissions",
        ],
        "correct_index": 3,
        "why": "Deforestation and rising carbon dioxide are two of the "
               "largest pressures on biodiversity, so cutting both protects "
               "ecosystems on a large scale.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e03",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one reason humans benefit from maintaining "
                "biodiversity.",
        "options": [
            "It protects services we rely on, such as pollination",
            "It guarantees that no new disease can ever appear",
            "It removes the need for farmers to grow any crops",
            "It stops the human population from growing further",
        ],
        "correct_index": 0,
        "why": "Ecosystem services such as pollination, clean water and "
               "clean air depend on a varied community of organisms.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e04",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rewilding a degraded area of land is an example of which "
                "kind of measure?",
        "options": [
            "A measure that reduces biodiversity",
            "A habitat restoration measure",
            "A measure that increases pollution",
            "A measure that adds land for farming",
        ],
        "correct_index": 1,
        "why": "Rewilding restores a damaged habitat so that its community "
               "can re-establish, which is habitat restoration.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s01",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farm plants a strip of wildflowers along one edge of a "
                "field of oilseed rape. Explain how this helps the farmer "
                "as well as wildlife.",
        "options": [
            "The wildflowers stop weeds growing anywhere in the whole field",
            "The wildflowers feed pollinators, which then pollinate the crop",
            "The wildflowers take minerals from the soil the crop cannot use",
            "The wildflowers shade the crop, which keeps the crop cooler",
        ],
        "correct_index": 1,
        "why": "Pollinators need food all season, and a farm that keeps them "
               "fed gets its own crop pollinated in return.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s02",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a programme that protects only one species is "
                "often less effective than one that protects a whole "
                "habitat.",
        "options": [
            "Single species are always too rare to be worth protecting at "
            "all",
            "A whole habitat costs far less money to protect than a species "
            "does",
            "The species depends on others in its habitat, which must "
            "survive too",
            "Protecting one species makes every other species in the area "
            "die out",
        ],
        "correct_index": 2,
        "why": "Species are interdependent, so a protected species still "
               "fails if the food, pollinators and shelter it relies on are "
               "lost.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s03",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ban on logging is introduced to protect a forest. "
                "Suggest why some local people may oppose it.",
        "options": [
            "They believe that forests remove oxygen from the air they "
            "breathe",
            "They want the forest cleared in order to reduce the local "
            "rainfall",
            "They think that logging has no effect on any of the forest "
            "species",
            "Many of them depend on logging work for their income",
        ],
        "correct_index": 3,
        "why": "Conservation measures often clash with livelihoods, and a "
               "ban that protects species can take away the jobs local "
               "people live on.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s04",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how recycling metals and paper helps to maintain "
                "biodiversity.",
        "options": [
            "Less land is quarried or felled, so more habitat is left "
            "intact",
            "Recycled materials release oxygen as they are broken down "
            "again",
            "Recycling makes rare species reproduce far more quickly than "
            "before",
            "Recycled metal is safer for wild animals to eat than newly "
            "mined metal",
        ],
        "correct_index": 0,
        "why": "Every tonne recycled is a tonne that does not have to be "
               "quarried or felled, so less habitat is destroyed to supply "
               "the raw material.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h01",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two plans for a large arable farm are compared. Plan A "
                "leaves 5% of the farm as narrow uncut margins. Plan B "
                "takes the same 5% out of production as one connected block "
                "of woodland. Suggest one advantage of plan B.",
        "options": [
            "Plan B needs no management at all once the trees are planted",
            "Plan B raises the yield of the other 95% of the farm's land",
            "Plan B keeps every species that the field margins would keep",
            "One larger block can support species that need a bigger area",
        ],
        "correct_index": 3,
        "why": "Some species cannot survive in a narrow strip at all, so a "
               "single larger patch of habitat supports a wider range of "
               "them.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h02",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why conservation decisions are usually described "
                "as a balance rather than as simple right answers.",
        "options": [
            "Protecting species brings benefits, but so do the uses of that "
            "land",
            "Scientists have not yet decided whether biodiversity matters "
            "at all",
            "Every conservation measure costs exactly the same as every "
            "other one",
            "The law forbids a government from ever choosing between two "
            "options",
        ],
        "correct_index": 0,
        "why": "Both sides of the decision are real gains — species and "
               "ecosystem services on one side, food, homes and jobs on the "
               "other — so it is a trade-off, not an obvious choice.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h03",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A supermarket promises to buy only fish caught under a "
                "quota system. Suggest how this helps maintain "
                "biodiversity, and name one group that may object.",
        "options": [
            "It removes the need for marine reserves, and scientists may "
            "object",
            "It lets fish stocks recover, and crews may object to smaller "
            "catches",
            "It raises the number of fish caught, and shoppers may object "
            "to the cost",
            "It has no effect on the stocks, and conservation groups may "
            "object",
        ],
        "correct_index": 1,
        "why": "A quota keeps the catch below the level at which the "
               "population can replace itself, but the same limit cuts what "
               "fishing crews are able to earn.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h04",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nature reserve is created but is surrounded on every "
                "side by intensive farmland. Suggest one reason why its "
                "biodiversity may still fall over time.",
        "options": [
            "Reserve species become too numerous and eat all of their food",
            "Farmland around a reserve raises the average temperature in it",
            "Species cannot move in or out, and pesticides drift in from "
            "outside",
            "The reserve boundary stops sunlight reaching the plants inside",
        ],
        "correct_index": 2,
        "why": "An isolated reserve loses the exchange of individuals "
               "between populations, and pollution from the land around it "
               "does not stop at the fence.",
    },

    # ── carbon-cycle ────────────────────────────────────────────────────
    {
        "id": "ks4-carbon-cycle-e01",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a long-term store of carbon?",
        "options": [
            "Carbon dioxide in the air above a field",
            "Glucose inside a plant leaf in summer",
            "Sugars stored in the body of an insect",
            "Coal buried deep underground",
        ],
        "correct_index": 3,
        "why": "Coal formed from ancient forests and has held its carbon "
               "underground for millions of years, unlike carbon passing "
               "through living organisms in days.",
    },
    {
        "id": "ks4-carbon-cycle-e02",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why carbon has to be recycled on Earth.",
        "options": [
            "Carbon is made in the atmosphere and must be moved into the "
            "ground",
            "The total amount of carbon is fixed, so the same atoms are "
            "reused",
            "Carbon is destroyed in respiration, so plants must make more "
            "of it",
            "Carbon would explode if it were left in one place for too long",
        ],
        "correct_index": 1,
        "why": "No new carbon is created, so every organism is built from "
               "atoms that have already been through the cycle many times.",
    },
    {
        "id": "ks4-carbon-cycle-e03",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which group of organisms carries out respiration?",
        "options": [
            "Only animals",
            "Only animals and fungi",
            "All living organisms",
            "Only bacteria and fungi",
        ],
        "correct_index": 2,
        "why": "Plants, animals, fungi and bacteria all respire to release "
               "energy from glucose, and all of them release carbon dioxide "
               "when they do.",
    },
    {
        "id": "ks4-carbon-cycle-e04",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the rock formed from the shells of ancient marine "
                "organisms.",
        "options": [
            "Limestone",
            "Granite",
            "Slate",
            "Sandstone",
        ],
        "correct_index": 0,
        "why": "Marine organisms build calcium carbonate shells from "
               "dissolved carbon, and those shells become limestone — a "
               "very long-term carbon store.",
    },
    {
        "id": "ks4-carbon-cycle-s01",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "During the day a plant takes in more carbon dioxide than "
                "it gives out. Explain what happens at night, and why.",
        "options": [
            "It gives out carbon dioxide, because it respires but cannot "
            "photosynthesise",
            "It takes in carbon dioxide, because photosynthesis continues "
            "in the dark",
            "It exchanges no gases at all, because a plant shuts down "
            "completely at night",
            "It gives out oxygen only, because plants never respire at any "
            "time of day",
        ],
        "correct_index": 0,
        "why": "Plants respire all the time; in the dark there is no "
               "photosynthesis to mask it, so the net movement of carbon "
               "dioxide is outwards.",
    },
    {
        "id": "ks4-carbon-cycle-s02",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the carbon in a dead oak leaf lying on a "
                "woodland floor returns to the atmosphere.",
        "options": [
            "Rain dissolves the carbon and washes it up into the clouds "
            "above",
            "The leaf slowly turns into carbon dioxide gas with no "
            "organisms involved",
            "Microorganisms break it down and release carbon dioxide as "
            "they respire",
            "The leaf is absorbed by the roots of the tree and used again "
            "next spring",
        ],
        "correct_index": 2,
        "why": "Decomposers feed on the dead material and respire as they "
               "do so, which is what puts the carbon back into the air as "
               "carbon dioxide.",
    },
    {
        "id": "ks4-carbon-cycle-s03",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon dioxide can leave the atmosphere by dissolving in "
                "seawater. Describe what marine organisms then do with that "
                "carbon.",
        "options": [
            "They breathe it straight back out as a gas as soon as they "
            "take it in",
            "They use it to build calcium carbonate shells",
            "They convert it into oxygen inside their own gills",
            "They store it as a layer of fat beneath their outer skin",
        ],
        "correct_index": 1,
        "why": "Shell-building organisms take dissolved carbon out of the "
               "water to make calcium carbonate, locking it away for a very "
               "long time.",
    },
    {
        "id": "ks4-carbon-cycle-s04",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why manufacturing cement adds carbon dioxide to "
                "the atmosphere.",
        "options": [
            "The workers who make the cement breathe out carbon dioxide as "
            "they work",
            "Cement absorbs carbon dioxide first, then releases it once the "
            "mixing stops",
            "Cement is made from crude oil, which is burned throughout the "
            "whole process",
            "Heating limestone breaks it down and releases carbon dioxide",
        ],
        "correct_index": 3,
        "why": "Limestone is a carbon store, and heating it drives the "
               "carbon off as carbon dioxide before the cement is even "
               "used.",
    },
    {
        "id": "ks4-carbon-cycle-h01",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A woodland absorbs 9 tonnes of carbon dioxide per hectare "
                "per year. A city plants 40 hectares of woodland to offset "
                "the 500 tonnes of carbon dioxide its buses release each "
                "year. Determine whether the planting is enough.",
        "options": [
            "Yes - the woodland absorbs 500 tonnes per year exactly",
            "Yes - the woodland absorbs 720 tonnes per year, with some to "
            "spare",
            "No - the woodland absorbs 360 tonnes per year, 140 tonnes "
            "short",
            "No - the woodland absorbs 49 tonnes per year, 451 tonnes short",
        ],
        "correct_index": 2,
        "why": "40 x 9 = 360 tonnes absorbed per year against 500 tonnes "
               "released, leaving a shortfall of 140 tonnes each year.",
    },
    {
        "id": "ks4-carbon-cycle-h02",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student draws a carbon cycle showing photosynthesis and "
                "respiration only. Identify what is missing, and explain "
                "why it matters.",
        "options": [
            "Nothing is missing - those two processes are the whole carbon "
            "cycle",
            "Combustion and decomposition are missing, and both return "
            "carbon",
            "Only photosynthesis is missing, because plants do not really "
            "respire",
            "Evaporation is missing, because it moves carbon out of the "
            "oceans",
        ],
        "correct_index": 1,
        "why": "Without combustion and decomposition the diagram cannot "
               "show how carbon leaves dead material or fossil fuels, which "
               "is where the human effect on the cycle happens.",
    },
    {
        "id": "ks4-carbon-cycle-h03",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The total amount of carbon on Earth does not change, yet "
                "the amount of carbon in the atmosphere is rising. Explain "
                "how both of these statements can be true.",
        "options": [
            "Carbon is being created inside power stations as the fuel is "
            "burned",
            "Some carbon is destroyed in the oceans, so the total does in "
            "fact fall",
            "The atmosphere is shrinking, so the same carbon is more "
            "concentrated",
            "Carbon is moving out of other stores into the atmosphere",
        ],
        "correct_index": 3,
        "why": "The cycle moves carbon between stores rather than making or "
               "destroying it, and burning fossil fuels shifts a huge store "
               "into the air.",
    },
    {
        "id": "ks4-carbon-cycle-h04",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed glass jar holds soil, a growing plant and a small "
                "snail, and is left in the light. Explain how carbon moves "
                "inside the jar.",
        "options": [
            "All three respire and release it, but the plant takes in more "
            "than it releases",
            "Only the plant releases carbon dioxide, because it cannot "
            "photosynthesise",
            "Carbon is used up by the plant and can never be returned to "
            "the air inside",
            "No carbon moves at all, because a sealed jar exchanges nothing "
            "with anything",
        ],
        "correct_index": 0,
        "why": "The plant respires as well as photosynthesising; in the "
               "light it takes in more carbon dioxide than it releases, while "
               "the snail and the soil organisms put the rest back.",
    },
]
