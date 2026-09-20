"""Biology · Ecology — the MRB-338 expansion, subtopic `abiotic-biotic-factors`.

Spec 4.7.1. The lesson's own common mistake is that pupils name one or two
abiotic factors and stop, so the weight falls on the full list — temperature,
light intensity, water availability, soil pH, soil mineral content, wind speed,
CO2 and O2 — and on saying HOW each one acts rather than only naming it. The
biotic half is examined through named real cases (myxomatosis, Dutch elm
disease, mistletoe, sheep ticks, red and grey squirrels) and the indicator
species of the lesson's own water-quality scale carry the "distribution tells
you the conditions" point."""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ────────────────────────────────────────────────────────────
    {
        "id": "ks4-abiotic-biotic-factors-e05",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the abiotic factor that affects the enzyme activity and "
                "the metabolic rate of an organism.",
        "options": [
            "Predation",
            "Parasitism",
            "Competition",
            "Temperature",
        ],
        "correct_index": 3,
        "why": "Enzymes work fastest within a narrow band of temperature, so "
               "the temperature of the surroundings sets how quickly an organism's "
               "reactions can run.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e06",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the biotic factor in which one organism hunts and eats "
                "another.",
        "options": [
            "Predation",
            "Pollination",
            "Parasitism",
            "Dispersal",
        ],
        "correct_index": 0,
        "why": "Predation is one organism killing and eating another, and it "
               "is a biotic factor because the effect comes from another living "
               "organism.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e07",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student maps a species across a habitat and marks every "
                "spot where it turns up. Identify what this map shows.",
        "options": [
            "Where in the habitat the species is found",
            "How many individuals of it are present across the whole area",
            "How quickly the species can reproduce there",
            "Which other species it is most closely related to",
        ],
        "correct_index": 0,
        "why": "Distribution is where a species occurs, while abundance is "
               "how many individuals there are.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e08",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the abiotic factor that decides which minerals are "
                "available to a plant's roots.",
        "options": [
            "Soil pH",
            "Wind speed",
            "Day length",
            "Predation",
        ],
        "correct_index": 0,
        "why": "The pH of a soil changes how soluble each mineral is, so it "
               "controls which nutrients a root can actually take up.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e09",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which abiotic factor acts most directly on the animals "
                "living in a pond?",
        "options": [
            "The herons that visit the pond each week",
            "The disease among the pond's snails",
            "The concentration of dissolved oxygen in the water",
            "The number of tadpoles competing for algae",
        ],
        "correct_index": 2,
        "why": "Dissolved oxygen is a non-living chemical feature of the "
               "water, and aquatic animals need it in order to respire.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e10",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the abiotic factor that raises the rate of water loss "
                "from a plant's leaves.",
        "options": [
            "Soil pH",
            "Wind speed",
            "Disease",
            "Predation",
        ],
        "correct_index": 1,
        "why": "Moving air carries water vapour away from the leaf surface, "
               "so a higher wind speed means faster water loss.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e11",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is an abiotic factor acting on the organisms "
                "in a freshwater stream?",
        "options": [
            "Trout feeding on the stream's insect larvae",
            "Water snails competing with each other for algae",
            "The temperature of the stream water",
            "A fungal disease spreading among the stream's water plants",
        ],
        "correct_index": 2,
        "why": "Water temperature is a non-living physical feature of the "
               "habitat; feeding, competition and disease are all effects of living "
               "organisms.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-e12",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a limiting factor in an ecosystem.",
        "options": [
            "The abiotic or biotic factor in shortest supply relative to "
            "demand, which caps how large a population can grow",
            "The factor that changes fastest over the course of one year",
            "The factor that a species can survive without for the longest "
            "time",
            "The factor that is easiest for an ecologist to measure in the "
            "field",
        ],
        "correct_index": 0,
        "why": "A population cannot grow beyond what its scarcest resource or "
               "harshest condition allows, so that factor sets the limit.",
    },
    # ── standard ──────────────────────────────────────────────────────────
    {
        "id": "ks4-abiotic-biotic-factors-s05",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mayfly larvae are found in one upland stream but are absent "
                "from a second stream that is more acidic. Name the abiotic factor "
                "responsible.",
        "options": [
            "Wind speed",
            "Water pH",
            "Day length",
            "Soil mineral content",
        ],
        "correct_index": 1,
        "why": "Mayfly larvae are sensitive to acid conditions, so a low pH "
               "excludes them from a stream that is otherwise suitable.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s06",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A stretch of river holds rat-tailed maggots but no mayfly "
                "larvae. State what this suggests about the water.",
        "options": [
            "It is clean, as rat-tailed maggots need pure water",
            "It is cold, because mayfly larvae need warmth to develop",
            "Its quality is very poor, because only tolerant species remain",
            "Its flow is too fast for mayfly larvae to hold on",
        ],
        "correct_index": 2,
        "why": "Rat-tailed maggots tolerate badly polluted water while mayfly "
               "larvae cannot, so that combination of species indicates very poor "
               "water quality.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s07",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a fall in air temperature slows a lizard down "
                "more than it slows a mouse.",
        "options": [
            "A lizard cannot warm itself, so its reactions slow with the air",
            "A lizard is smaller, so it loses its body heat much more slowly",
            "A lizard has no enzymes, so cold air stops its digestion at once",
            "A lizard has thinner skin, so cold air reaches its bones first",
        ],
        "correct_index": 0,
        "why": "A lizard's body temperature follows its surroundings, so a "
               "drop in air temperature lowers its metabolic rate, while a mammal "
               "holds its own temperature steady.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s08",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Foxgloves and brambles grow in a woodland clearing while ivy "
                "and mosses grow under the closed canopy. Explain this difference in "
                "distribution.",
        "options": [
            "The clearing has richer soil, because rainfall washes minerals "
            "down into it",
            "The canopy plants are younger, so they have not yet grown tall",
            "The clearing is warmer, and warmth is what brambles need to "
            "flower",
            "The two groups differ in the light intensity they need",
        ],
        "correct_index": 3,
        "why": "Light intensity is the abiotic factor that separates them: "
               "foxgloves and brambles need high light, while ivy and mosses "
               "tolerate deep shade.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s09",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Heather grows on one moorland soil while nettles and ash "
                "trees grow on the soil of the valley below. Name the abiotic factor "
                "most likely to separate them.",
        "options": [
            "Wind speed",
            "Carbon dioxide concentration",
            "Oxygen concentration",
            "Soil pH",
        ],
        "correct_index": 3,
        "why": "Heather is adapted to acidic soils while nettles and ash "
               "prefer alkaline ones, so soil pH is what decides which grows where.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s10",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An algal bloom in a lake dies back and decomposes, and the "
                "fish then die. Name the abiotic factor that changed and explain how.",
        "options": [
            "Oxygen concentration, because the decomposers used up the oxygen",
            "Light intensity, as the dead algae blocked the sunlight",
            "Temperature, as rotting algae warmed the water",
            "Soil pH, as the algae released acid into the lake",
        ],
        "correct_index": 0,
        "why": "Decomposers respire as they break the algae down, and that "
               "removes dissolved oxygen from the water until the fish can no longer "
               "respire.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s11",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Dutch elm disease kills most of the elm trees in a hedgerow. "
                "Name this factor and classify it.",
        "options": [
            "Disease, and it is a biotic factor",
            "Disease, and it is an abiotic factor",
            "Competition, and it is a biotic factor",
            "Parasitism, and that makes it an abiotic factor",
        ],
        "correct_index": 0,
        "why": "The disease is caused by a living pathogen acting on the "
               "trees, so it is a biotic factor.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s12",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Myxomatosis reduced the UK rabbit population sharply in the "
                "1950s. Classify the factor and state what it acted on.",
        "options": [
            "Abiotic, and it acted on the rabbits' food supply in the fields",
            "Biotic, and it acted on the abundance of the rabbit population",
            "Abiotic, and it acted on the range of temperature the rabbits "
            "could stand",
            "Biotic, and it acted on the rabbits' soil mineral requirements",
        ],
        "correct_index": 1,
        "why": "Disease is a biotic factor, and a pathogen sweeping through a "
               "population cuts the number of individuals — its abundance.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s13",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a shortage of nitrates in a soil limits which "
                "plants can grow there.",
        "options": [
            "Nitrates are the plant's only source of energy for respiration",
            "Nitrates lower the soil pH, which stops the roots taking water",
            "Nitrates are needed to absorb light energy inside the plant's "
            "chloroplasts",
            "Nitrates are needed to make proteins, so growth is restricted",
        ],
        "correct_index": 3,
        "why": "Plants use nitrate ions to build amino acids and then "
               "proteins, so a nitrate-poor soil supports only species that can "
               "manage on very little.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s14",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Red squirrels have largely disappeared from English woods "
                "where grey squirrels are present. Name the type of competition "
                "involved.",
        "options": [
            "Interspecific competition",
            "Intraspecific competition",
            "Parasitism",
            "Predation",
        ],
        "correct_index": 0,
        "why": "The two are different species competing for the same food and "
               "nest sites, which makes it interspecific competition.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s15",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two robins sing at each other across the boundary between "
                "their territories. Name the type of competition and the resource "
                "involved.",
        "options": [
            "Interspecific competition, and the resource is soil minerals",
            "Interspecific competition, and the resource is the dissolved "
            "oxygen",
            "Intraspecific competition, and the resource is territory",
            "Intraspecific competition, and the resource is sunlight",
        ],
        "correct_index": 2,
        "why": "Both birds are the same species, so the competition is "
               "intraspecific, and the resource being defended is the feeding and "
               "nesting territory.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s16",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two different ways in which wind speed acts as an "
                "abiotic factor.",
        "options": [
            "It changes the soil pH, and it changes the oxygen in the water",
            "It raises water loss, and it drives the wave action on a shore",
            "It raises the temperature, and it lowers the light intensity",
            "It carries disease, and it moves predators towards their prey",
        ],
        "correct_index": 1,
        "why": "Wind removes water vapour from leaves and skin, and at sea it "
               "generates the wave action that decides which shore organisms can "
               "hold on.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s17",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower raises both the temperature and the light in a "
                "greenhouse, but the tomato plants grow no faster. Suggest the "
                "reason.",
        "options": [
            "Plants grow at a fixed rate that no change in the conditions can "
            "alter",
            "Raising two factors at once cancels the effect of both of them",
            "Tomato plants stop growing whenever the temperature is raised",
            "A third factor, such as carbon dioxide, is now limiting growth",
        ],
        "correct_index": 3,
        "why": "Growth is held back by whichever factor is in shortest "
               "supply, so raising two factors changes nothing if a third is the one "
               "that limits it.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s18",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A survey finds bladderwrack seaweed only on the middle of a "
                "shore, where there are 30 plants per square metre. State which "
                "figure is the abundance.",
        "options": [
            "The middle part of the shore, where they grow",
            "The whole of the shore",
            "The name bladderwrack",
            "The 30 plants per square metre",
        ],
        "correct_index": 3,
        "why": "Abundance is the count of individuals present; where on the "
               "shore they are found is the distribution.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s19",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Badgers forage at night and blackbirds forage by day. Name "
                "the abiotic factor that these two patterns respond to.",
        "options": [
            "Light",
            "Soil pH",
            "Wind speed",
            "Soil minerals",
        ],
        "correct_index": 0,
        "why": "Light intensity acts on animal behaviour as well as on plant "
               "growth, dividing species into nocturnal and diurnal ones.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s20",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An insecticide sprayed along a hedgerow kills most of the "
                "pollinating insects. Predict the effect on the hedgerow plants and "
                "classify the factor.",
        "options": [
            "Fewer seeds are set, and the loss of pollinators is abiotic",
            "Fewer seeds are set, and the loss of pollinators is biotic",
            "More seeds are set, as the plants keep the nectar they made",
            "Seed numbers are unchanged, as every hedgerow plant pollinates "
            "itself",
        ],
        "correct_index": 1,
        "why": "Insect-pollinated plants depend on an animal to move their "
               "pollen, so losing the pollinators is a biotic factor that reduces "
               "seed production.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s21",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student lists predation as an abiotic factor. Identify the "
                "error and correct it.",
        "options": [
            "Predation is biotic, because a predator is a living organism",
            "Predation is biotic, because it takes place out in the open air",
            "There is no error, because predation acts on whole populations",
            "Predation is abiotic, because a predator does not live on or in "
            "its prey",
        ],
        "correct_index": 0,
        "why": "Abiotic means non-living, and a predator is another organism, "
               "so its effect on a population is a biotic factor.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s22",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sheep tick numbers rise on a moor and the red grouse chicks "
                "there grow more slowly. Name this biotic factor.",
        "options": [
            "Competition",
            "Predation",
            "Parasitism",
            "Pollination",
        ],
        "correct_index": 2,
        "why": "A tick feeds on its host without killing it outright, which "
               "harms the host's growth and survival — that is parasitism.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s23",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crop grows poorly in a strongly acidic soil even though "
                "fertiliser has been added. Explain why.",
        "options": [
            "Fertiliser turns into acid as soon as it is added to a soil",
            "Acidic soils hold no water, so the roots cannot absorb anything",
            "A low pH keeps some minerals in a form the roots cannot take up",
            "Crops stop respiring below pH 5, so they cannot release energy",
        ],
        "correct_index": 2,
        "why": "Soil pH controls how soluble each mineral is, so the "
               "nutrients can be present in the soil and still be unavailable to the "
               "plant.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s24",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Downstream of a sewage outfall a river holds leeches but no "
                "mayfly larvae. State the conclusion an ecologist would draw.",
        "options": [
            "The river is unpolluted, because leeches need clean water",
            "The river is moderately polluted, and the leeches tolerate it",
            "The river is too fast-flowing for the mayfly larvae to hold on",
            "The river has too little dissolved calcium for mayfly larvae",
        ],
        "correct_index": 1,
        "why": "Leeches tolerate moderate pollution while mayfly larvae do "
               "not, so the pair of observations places the water in the middle of "
               "the quality scale.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s25",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how food availability acts as a biotic factor "
                "limiting the number of barn owls in an area.",
        "options": [
            "Owls eat the plants of the field, and plants are living things",
            "Owls compete with the voles for the same seeds in the hedgerow",
            "Fewer voles means less food, so fewer owls can be supported",
            "Voles carry a disease that reduces the number of barn owls each "
            "year",
        ],
        "correct_index": 2,
        "why": "The owls' prey is another living organism, so its abundance "
               "is a biotic factor, and a smaller food supply supports a smaller "
               "predator population.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-s26",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A survey records 40 daisy plants per square metre in the "
                "sunny half of a lawn and 3 per square metre in the shaded half. "
                "State the conclusion these data support.",
        "options": [
            "Daisies grow at the same density wherever they are planted",
            "Daisy abundance is lower where the light intensity is lower",
            "Shade increases daisy growth by lowering the water loss from the "
            "leaves",
            "Daisies compete with grass only in the sunny half of the lawn",
        ],
        "correct_index": 1,
        "why": "The only recorded difference is the light, and the abundance "
               "falls with it, so the data support light intensity limiting daisy "
               "numbers.",
    },
    # ── harder ────────────────────────────────────────────────────────────
    {
        "id": "ks4-abiotic-biotic-factors-h05",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the northern hemisphere, the south-facing side of a "
                "valley carries far more flowering plants than the north-facing side. "
                "Explain this difference.",
        "options": [
            "The south-facing side is more sheltered from each of the "
            "prevailing winds",
            "The north-facing side has a much lower soil pH than the other "
            "side",
            "The north-facing side holds more herbivores, which graze it "
            "harder",
            "The south-facing side receives more light and is warmer",
        ],
        "correct_index": 3,
        "why": "A south-facing slope is tilted towards the sun, so it "
               "receives more light energy per square metre and warms up more, and "
               "both raise the rate of plant growth.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h06",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that disease must be an abiotic factor "
                "because the organism causing it is too small to see. Evaluate this "
                "argument.",
        "options": [
            "It is sound, because abiotic means anything not visible",
            "It is unsound, because bacteria and fungi are living organisms",
            "It is sound: a pathogen has no habitat of its own",
            "It is unsound: disease is neither abiotic nor biotic",
        ],
        "correct_index": 1,
        "why": "Biotic and abiotic divide factors by whether they come from "
               "something living, not by size — a pathogen is an organism, so "
               "disease is biotic.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h07",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why raising one abiotic factor stops improving the "
                "growth of a crop once a certain value is reached.",
        "options": [
            "Growth is limited by whichever factor is in shortest supply",
            "A plant can respond to one abiotic factor at a time and no more",
            "Every abiotic factor has the same maximum useful value in any "
            "crop plant",
            "A factor that has been raised twice begins to act in reverse",
        ],
        "correct_index": 0,
        "why": "Once the factor being raised is no longer the one in shortest "
               "supply, something else has become limiting, and raising the first "
               "has no further effect.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h08",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Stream X holds mayfly larvae, stream Y holds leeches and "
                "stream Z holds rat-tailed maggots only. Place the three in order "
                "from the cleanest water to the dirtiest.",
        "options": [
            "Z, then Y, then X",
            "Y, then X, then Z",
            "X, then Y, then Z",
            "X, then Z, then Y",
        ],
        "correct_index": 2,
        "why": "Mayfly larvae need clean water, leeches tolerate moderate "
               "pollution and rat-tailed maggots survive very poor water, so that is "
               "the order of decreasing quality.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h09",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a plant can be absent from a site whose "
                "temperature, light and soil all suit it perfectly.",
        "options": [
            "Perfect abiotic conditions stop a plant from making any seed",
            "A plant will not grow where the conditions match its needs "
            "exactly",
            "A biotic factor, such as grazing or a competitor, excludes it",
            "Abiotic factors act on animals rather than on plants at all",
        ],
        "correct_index": 2,
        "why": "Distribution is set by abiotic and biotic factors together, "
               "so a competitor, a grazer or a pathogen can keep a species out of a "
               "physically suitable site.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h10",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The dissolved oxygen in a weedy pond is lowest just before "
                "dawn. Explain why.",
        "options": [
            "The plants have respired all night without photosynthesising",
            "Cold night air dissolves less oxygen into the surface water",
            "Fish take in more oxygen at night because they hunt in the dark",
            "Oxygen sinks to the bottom of the pond overnight and is trapped",
        ],
        "correct_index": 0,
        "why": "All of the pond's organisms respire through the night, and "
               "with no light there is no photosynthesis to replace the oxygen they "
               "use.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h11",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Limestone weathers to give an alkaline soil. Predict whether "
                "heather or ash is more likely to colonise it, and explain.",
        "options": [
            "Heather, as it needs the calcium in limestone",
            "Ash, because ash grows on alkaline soils and heather on acidic",
            "Heather, as alkaline soils hold the most minerals",
            "Ash, because a tree tolerates any soil pH",
        ],
        "correct_index": 1,
        "why": "Soil pH decides which species can take up the minerals it "
               "needs, and ash is an alkaline-soil species while heather is an "
               "acid-soil one.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h12",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a useful indicator species has to be sensitive "
                "to a change rather than simply common in the habitat.",
        "options": [
            "A common species is harder to count accurately in a quadrat",
            "A tolerant species is present whatever the conditions are",
            "A sensitive species can be identified far more easily than the "
            "others are",
            "A common species is more likely to have been introduced by people",
        ],
        "correct_index": 1,
        "why": "An indicator works because it disappears when conditions "
               "worsen, so a species that survives anything tells an ecologist "
               "nothing about the conditions.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h13",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sea wall is built across the mouth of a bay and the wave "
                "action on the shore inside falls sharply. Predict how the zonation "
                "of the shore will change.",
        "options": [
            "The shore will hold no species at all once the waves have gone "
            "from it",
            "The upper shore will dry out faster, so more species will die",
            "Species needing shelter will spread further up the shore",
            "The zones will reverse, with the hardiest species lowest down",
        ],
        "correct_index": 2,
        "why": "Wave action is one of the abiotic factors that restricts "
               "delicate species to the lower shore, so reducing it lets them occupy "
               "ground they were excluded from.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h14",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pollutant enters a river and kills its mayfly larvae. "
                "Suggest why the number of trout then falls as well.",
        "options": [
            "Trout use mayfly larvae as prey, so their food supply has fallen",
            "Trout need mayfly larvae to keep the gravel clean",
            "The pollutant is toxic to trout but harmless to other fish",
            "Mayfly larvae add the oxygen the trout respire with",
        ],
        "correct_index": 0,
        "why": "An abiotic change at one level passes on as a biotic one: "
               "losing the prey removes the predator's food, so fewer trout can be "
               "supported.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h15",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Nitrate is a plant nutrient, yet nitrate fertiliser washing "
                "into a river reduces the number of species living in it. Explain "
                "how.",
        "options": [
            "Nitrate is toxic to fish at any concentration",
            "Algae grow, die and decompose, and the decomposers take the "
            "oxygen",
            "Nitrate warms the water, which kills the insects",
            "Nitrate lowers the river's pH until the animals die",
        ],
        "correct_index": 1,
        "why": "The nutrient triggers an algal bloom, and when the algae die "
               "the decomposers respiring on them strip the dissolved oxygen the "
               "animals need.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h16",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a UK woodland in January there is plenty of water and the "
                "soil is rich, but almost nothing is growing. Determine which abiotic "
                "factors are limiting growth.",
        "options": [
            "Light intensity and temperature, both of which are low",
            "Soil pH and the soil mineral content of the woodland floor",
            "Wind speed and the concentration of carbon dioxide in the winter "
            "air",
            "Water availability, because frozen water cannot be absorbed",
        ],
        "correct_index": 0,
        "why": "Short days give little light for photosynthesis and low "
               "temperatures slow every enzyme-controlled reaction, so growth is "
               "held back by both together.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h17",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two ponds have the same temperature, pH and oxygen "
                "concentration, yet one holds many newts and the other holds almost "
                "none. Suggest a biotic explanation.",
        "options": [
            "The second pond is deeper, so newts cannot reach its bottom",
            "The second pond receives less rainfall over the course of a year",
            "The second pond has a smaller surface area open to the sunlight",
            "The second pond holds fish that eat the newts' eggs and young",
        ],
        "correct_index": 3,
        "why": "With the abiotic conditions matched, the difference must come "
               "from another organism, and predation on eggs and larvae keeps newts "
               "out of fish-stocked ponds.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h18",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hawthorn standing alone in an exposed coastal field has "
                "branches on one side only. Suggest the abiotic factor and how it "
                "acts.",
        "options": [
            "Soil pH, because one side of the tree stands in more acidic soil",
            "Light, because the sun shines on one side of the tree all day",
            "Wind, because salt-laden wind dries out and kills new shoots",
            "Temperature, because one side of the trunk is warmer than the "
            "other side",
        ],
        "correct_index": 2,
        "why": "The prevailing wind carries salt spray and raises water loss "
               "on the windward side, killing the buds there so growth survives only "
               "in the lee.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h19",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why intraspecific competition becomes a stronger "
                "biotic factor as a population grows.",
        "options": [
            "A growing population changes its abiotic conditions",
            "A large population attracts far more predators",
            "Larger populations hold more varied individuals",
            "Individuals of one species need the same things, so shares shrink",
        ],
        "correct_index": 3,
        "why": "Members of one species have identical requirements, so as "
               "numbers rise each individual's share of a fixed resource falls and "
               "the competition intensifies.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h20",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Over thirty years a butterfly species is recorded 100 km "
                "further north than before. Suggest which factor drove the change and "
                "how.",
        "options": [
            "Temperature, because warming made the northern sites tolerable",
            "Soil pH, because northern soils have become steadily more "
            "alkaline",
            "Predation, because its northern predators have all been lost",
            "Wind speed, because stronger winds carried the adults northwards",
        ],
        "correct_index": 0,
        "why": "An abiotic factor sets the edge of a species' range, and a "
               "rise in temperature moves the band of tolerable conditions "
               "polewards.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h21",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest how removing a tall hedgerow changes the abiotic "
                "conditions in the strip of field beside it.",
        "options": [
            "The strip becomes cooler, because the hedge had been trapping "
            "the heat in",
            "The strip's soil pH rises sharply once the hedge roots are gone",
            "The strip receives more rainfall, because the hedge had drunk it",
            "The strip receives more wind and more light than it did before",
        ],
        "correct_index": 3,
        "why": "A hedge shelters the ground beside it and shades part of it, "
               "so taking it away raises both the wind speed and the light intensity "
               "in that strip.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h22",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student finds that grassland plots with a higher soil pH "
                "hold more plant species, and concludes that raising pH raises "
                "diversity. Explain why the data cannot show that.",
        "options": [
            "A correlation does not show which factor is causing the other",
            "Soil pH cannot be measured accurately enough in a field survey",
            "Plant species number has no relationship with soil pH at all",
            "The student should have measured pH in the laboratory instead",
        ],
        "correct_index": 0,
        "why": "The two rise together, but an unmeasured third factor could "
               "be raising both, so observation alone cannot establish the cause.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h23",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant can survive one frosty night but dies "
                "after a fortnight of hard frost.",
        "options": [
            "A brief frost is warmer than a long one at every point in the day",
            "A plant learns to tolerate cold weather after its first frost",
            "A long frost lowers the soil pH so the roots can absorb nothing",
            "Brief cold slows its reactions; prolonged cold damages its cells",
        ],
        "correct_index": 3,
        "why": "A short exposure only slows the plant's metabolism, but "
               "sustained freezing damages cells and tissues beyond repair.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h24",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mistletoe grows on the branches of a lime tree and draws "
                "water and minerals out of it. Compare this with competition between "
                "two lime trees.",
        "options": [
            "Both are the same factor, because both reduce the tree's growth",
            "Mistletoe is an abiotic factor and competition is a biotic one",
            "Mistletoe takes resources from the host; rivals take a shared "
            "pool",
            "Mistletoe competes with the lime for sunlight and for nothing "
            "else",
        ],
        "correct_index": 2,
        "why": "In parasitism one organism takes its resources directly out "
               "of the other, while in competition both draw on the same external "
               "supply.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h25",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that every factor limiting a population "
                "must be biotic, because populations are made of living things. "
                "Evaluate this claim.",
        "options": [
            "It is sound, because a factor acts only on something that lives",
            "It is unsound, because non-living conditions also limit numbers",
            "It is unsound, because biotic describes what the factor acts upon",
            "It is sound, because abiotic factors act on the habitat instead",
        ],
        "correct_index": 1,
        "why": "The classification describes the SOURCE of the factor, not "
               "what it acts on, so temperature, pH and rainfall are abiotic limits "
               "on living populations.",
    },
    {
        "id": "ks4-abiotic-biotic-factors-h26",
        "subtopic_slug": "abiotic-biotic-factors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which single change would most raise the number of "
                "plant species on the floor of a densely shaded conifer plantation, "
                "and explain why.",
        "options": [
            "Adding nitrate fertiliser, as minerals limit growth in shade",
            "Thinning the trees, because light is the factor limiting growth",
            "Fencing out the deer, because grazing is the limiting factor here",
            "Raising the soil pH with lime, as conifer soils are far too "
            "acidic",
        ],
        "correct_index": 1,
        "why": "Under a dense conifer canopy the light intensity at ground "
               "level is the factor in shortest supply, so opening the canopy is "
               "what lets more species grow.",
    },
]
