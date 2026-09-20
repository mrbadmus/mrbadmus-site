"""Biology · Ecology — the MRB-338 expansion of `carbon-cycle`.

One leaf only: AQA 8461 §4.7.3. The original twelve rows in `ecology__a.py`
take coal as a long-term store, the fixed total, respiration in all organisms,
limestone from shells, a plant at night, a rotting oak leaf, carbonate shells,
cement, one offset calculation, the cycle drawn with two arrows missing, a
fixed total against a rising atmosphere, and a sealed jar.

This file takes what they leave. The recall band finishes the stores and forms
the baseline never names — methane, humus, carbonic acid, the sink, and the
route from plant to animal by eating. The demand then falls where the spec's
real difficulty is: the RATE imbalance. Carbon has always moved between stores;
what is new is that it now leaves the fossil store thousands of times faster
than it entered it, and almost every harder row here is that idea approached
from a different side — a mature wood against a growing one, decay against
combustion, an offset arithmetic that does not close, the seasonal wobble in
the atmospheric record, a warming soil respiring faster.

The weight follows the CONTENT. `easier` stays at eight: the stores and
processes are a closed list, and a ninth recall row is the eighth reworded.
`standard` and `harder` carry twenty-two each, because every arrow on the cycle
generates its own context and its own arithmetic in tonnes.

Numbers are the ones this topic supplies: tonnes of carbon and of carbon
dioxide, hectares of woodland, parts per million in the atmosphere, kilograms
of methane from a herd.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The stores and forms the baseline leaves unnamed: methane, humus,
    # carbonic acid, fossilisation, volcanic release, the sink, and the
    # feeding route from plant to animal.
    {
        "id": "ks4-carbon-cycle-e05",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the form in which carbon is held inside a plant after "
                "photosynthesis.",
        "options": [
            "As pure carbon powder stored in the spaces between the cells",
            "As carbon dioxide gas held permanently in the air spaces of "
                "the leaf",
            "As glucose and the other organic molecules built from it",
            "As carbonate crystals deposited in the walls of the root "
                "cells",
        ],
        "correct_index": 2,
        "why": "Photosynthesis builds the carbon from carbon dioxide into "
               "glucose, and the plant then builds that glucose into starch, "
               "cellulose, proteins and fats.",
    },
    {
        "id": "ks4-carbon-cycle-e06",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the greenhouse gas other than carbon dioxide that "
                "carries carbon in the atmosphere.",
        "options": [
            "Methane",
            "Nitrogen",
            "Ozone",
            "Argon",
        ],
        "correct_index": 0,
        "why": "Methane, CH4, holds a carbon atom and is a greenhouse gas "
               "whose atmospheric level is rising.",
    },
    {
        "id": "ks4-carbon-cycle-e07",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the carbon-containing material in soil that is formed "
                "from decaying plant and animal remains.",
        "options": [
            "Limestone",
            "Gravel",
            "Clay",
            "Humus",
        ],
        "correct_index": 3,
        "why": "Humus is the dark, carbon-rich material formed as decomposers "
               "break down dead remains in the soil.",
    },
    {
        "id": "ks4-carbon-cycle-e08",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how carbon passes from a grass plant into a sheep.",
        "options": [
            "The sheep absorbs carbon dioxide from the grass through its "
                "skin",
            "The sheep eats the grass, taking in the carbon in its "
                "molecules",
            "The sheep breathes in the carbon that the grass gives off as "
                "a gas at night",
            "The sheep takes up carbon from the soil in the water it "
                "drinks",
        ],
        "correct_index": 1,
        "why": "Feeding is the route carbon takes along a food chain: the "
               "sheep digests and absorbs the organic molecules the grass "
               "built.",
    },
    {
        "id": "ks4-carbon-cycle-e09",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process by which the remains of ancient forests "
                "became coal over millions of years.",
        "options": [
            "Fossilisation",
            "Photosynthesis",
            "Condensation",
            "Evaporation",
        ],
        "correct_index": 0,
        "why": "Fossilisation compressed the partly decayed remains of ancient "
               "plants into coal, locking their carbon away underground.",
    },
    {
        "id": "ks4-carbon-cycle-e10",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one natural process, involving no human activity, that "
                "returns carbon dioxide from underground to the air.",
        "options": [
            "Earthquakes, which crush limestone and turn all of it into "
                "gas",
            "Wind erosion, which lifts carbon from the rock into the air",
            "Rain soaking down through the soil and washing the gas back "
                "up again",
            "Volcanic activity, which releases carbon dioxide in its gases",
        ],
        "correct_index": 3,
        "why": "Volcanoes release carbon dioxide from underground stores "
               "directly into the atmosphere, and have done so throughout "
               "Earth's history.",
    },
    {
        "id": "ks4-carbon-cycle-e11",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a carbon sink.",
        "options": [
            "A place where carbon is destroyed so that it leaves the cycle "
                "for good",
            "A store that takes in more carbon than it gives back out",
            "A gas that traps heat energy close to the Earth's surface",
            "A rock in which carbon has been buried for millions of years",
        ],
        "correct_index": 1,
        "why": "A sink absorbs more carbon than it releases, so carbon "
               "accumulates in it — a growing forest and the oceans are both "
               "sinks.",
    },
    {
        "id": "ks4-carbon-cycle-e12",
        "subtopic_slug": "carbon-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the acid formed when carbon dioxide dissolves in "
                "seawater.",
        "options": [
            "Sulfuric acid",
            "Ethanoic acid",
            "Carbonic acid",
            "Nitric acid",
        ],
        "correct_index": 2,
        "why": "Dissolved carbon dioxide forms carbonic acid, which is why "
               "rising carbon dioxide levels make the oceans more acidic.",
    },
    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # The arrows of the cycle in named contexts, and the first arithmetic in
    # tonnes and parts per million.
    {
        "id": "ks4-carbon-cycle-s05",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the carbon in a rabbit's droppings returns to the "
                "atmosphere.",
        "options": [
            "Plant roots take the carbon up and breathe it out of the "
                "stomata",
            "The droppings dry out and the carbon evaporates away as a gas",
            "Decomposers feed on the droppings and release carbon dioxide "
                "as they respire",
            "Rain dissolves the carbon and carries it up into the clouds",
        ],
        "correct_index": 2,
        "why": "Bacteria and fungi break down the organic matter in the "
               "droppings and release carbon dioxide during their own aerobic "
               "respiration.",
    },
    {
        "id": "ks4-carbon-cycle-s06",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why burning coal is described as adding old carbon to "
                "the atmosphere.",
        "options": [
            "Its carbon was taken from the air by plants millions of years "
                "ago",
            "Coal is burned in old power stations that were built long ago",
            "The carbon in coal has been through the cycle more times than "
                "any other carbon has",
            "The coal itself is old, so the gas it gives off is also very "
                "old",
        ],
        "correct_index": 0,
        "why": "The carbon in coal was removed from the atmosphere by plants "
               "in ancient forests and has been locked underground ever since; "
               "burning returns it in moments.",
    },
    {
        "id": "ks4-carbon-cycle-s07",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the route a carbon atom takes from the air into a "
                "cow and back to the air again.",
        "options": [
            "Air to the cow by breathing in, to the grass by grazing, to "
                "the air by evaporation",
            "Air to soil by rainfall, to the cow through its hooves, to "
                "the air by transpiration",
            "Air to grass by absorption, to the cow by drinking, to the "
                "air by sweating it out",
            "Air to grass by photosynthesis, to the cow by eating, to the "
                "air by respiration",
        ],
        "correct_index": 3,
        "why": "Photosynthesis fixes the carbon into grass, feeding moves it "
               "into the cow, and the cow's respiration releases it as carbon "
               "dioxide.",
    },
    {
        "id": "ks4-carbon-cycle-s08",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a flooded rice paddy releases methane rather than "
                "carbon dioxide.",
        "options": [
            "The rice plants make methane during their photosynthesis",
            "Flooded soil has little oxygen, so decay there is anaerobic",
            "The water dissolves every molecule of carbon dioxide produced "
                "in the mud",
            "Methane is lighter than carbon dioxide, so it escapes from "
                "the water",
        ],
        "correct_index": 1,
        "why": "Waterlogging excludes oxygen, and the microorganisms that "
               "decay organic matter without oxygen produce methane instead of "
               "carbon dioxide.",
    },
    {
        "id": "ks4-carbon-cycle-s09",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the oceans are described as a store of carbon as "
                "well as a route by which carbon leaves the air.",
        "options": [
            "Carbon dioxide dissolves in, and stays as dissolved gas and "
                "in shells",
            "Sea water is deep, and depth alone stops any gas escaping "
                "again",
            "The oceans cover most of the planet's surface, so they must "
                "hold most of its carbon",
            "Sea water is salty, and salt holds carbon in place "
                "permanently",
        ],
        "correct_index": 0,
        "why": "Carbon dioxide dissolves at the surface and much of it stays "
               "in the water or is built into calcium carbonate shells, so the "
               "ocean both absorbs and holds carbon.",
    },
    {
        "id": "ks4-carbon-cycle-s10",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why rising carbon dioxide in the air is a problem for "
                "animals that build shells.",
        "options": [
            "Shelled animals breathe in carbon dioxide and are poisoned by "
                "the extra amount of it",
            "The extra gas warms the sea so much that every shelled animal "
                "boils in it",
            "The gas coats the shells and stops the animals growing any "
                "bigger",
            "More dissolves in the sea, making it more acidic and shells "
                "harder to build",
        ],
        "correct_index": 3,
        "why": "More dissolved carbon dioxide means more carbonic acid, and "
               "the more acidic water makes it harder for organisms to form "
               "and keep calcium carbonate shells.",
    },
    {
        "id": "ks4-carbon-cycle-s11",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a young growing woodland removes more carbon from "
                "the air each year than an old woodland of the same area.",
        "options": [
            "Young trees are able to photosynthesise at night as well as "
                "by day",
            "Young trees are adding biomass fast, so more carbon is being "
                "stored",
            "Old trees have stopped photosynthesising completely once they "
                "mature",
            "Old trees give out more carbon dioxide than they take in "
                "during every hour of the day",
        ],
        "correct_index": 1,
        "why": "Net removal depends on biomass being added; a fast-growing "
               "wood locks carbon into new wood, while a mature wood's growth "
               "and decay are close to balanced.",
    },
    {
        "id": "ks4-carbon-cycle-s12",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a soil rich in humus holds more carbon than a "
                "bare sandy soil.",
        "options": [
            "Humus attracts carbon dioxide out of the air and traps it in "
                "the gaps",
            "Sand is made of carbon, so sandy soils release it instead",
            "Humus is partly decayed organic matter, which is full of "
                "carbon",
            "Sandy soil is warmer, and warmth destroys the carbon in the "
                "ground",
        ],
        "correct_index": 2,
        "why": "Humus is the undecayed remains of organisms, and those remains "
               "are built from carbon-containing molecules.",
    },
    {
        "id": "ks4-carbon-cycle-s13",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why burning wood from a replanted forest affects the "
                "atmosphere differently from burning coal.",
        "options": [
            "Wood burns at a lower temperature, so less gas is given off",
            "Coal releases methane when it burns, while wood releases only "
                "steam",
            "Wood contains no carbon, so burning it releases no gas",
            "Replanted trees take that carbon back within years, not ages",
        ],
        "correct_index": 3,
        "why": "The carbon from the wood was in the air recently and the "
               "replanted trees absorb it again quickly, while coal's carbon "
               "has been out of circulation for millions of years.",
    },
    {
        "id": "ks4-carbon-cycle-s14",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One tree absorbs 22 kg of carbon dioxide in a year. Calculate "
                "the mass absorbed by 150 trees in one year.",
        "options": [
            "1100 kg",
            "3300 kg",
            "3300 g",
            "172 kg",
        ],
        "correct_index": 1,
        "why": "22 kg × 150 trees = 3300 kg of carbon dioxide absorbed in the "
               "year.",
    },
    {
        "id": "ks4-carbon-cycle-s15",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the part fungi play in the carbon cycle.",
        "options": [
            "They feed on carbon dioxide dissolved in the water in the "
                "soil",
            "They photosynthesise, so they take carbon dioxide straight "
                "out of the air",
            "They decay dead material and respire, returning carbon as gas",
            "They store carbon permanently in their threads under the "
                "ground",
        ],
        "correct_index": 2,
        "why": "Fungi are decomposers: they break down dead organisms and "
               "release carbon dioxide as they respire.",
    },
    {
        "id": "ks4-carbon-cycle-s16",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the carbon dioxide concentration in a wood is "
                "highest just before dawn.",
        "options": [
            "All night the wood has respired without photosynthesising, so "
                "it has built up",
            "Carbon dioxide sinks to the ground overnight and rises in "
                "daylight",
            "Trees release stored carbon dioxide at dawn to begin "
                "photosynthesis",
            "Cold night air holds far more carbon dioxide than warm air "
                "can",
        ],
        "correct_index": 0,
        "why": "Every organism in the wood respires all night, and with no "
               "light there is no photosynthesis to remove the gas, so it "
               "accumulates until sunrise.",
    },
    {
        "id": "ks4-carbon-cycle-s17",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to the carbon in a fish that dies and "
                "sinks to the deep seabed.",
        "options": [
            "All of it turns straight into limestone within a few weeks",
            "Some is released by decomposers, some stays in the sediment",
            "It is destroyed by the pressure at the bottom of the ocean",
            "It floats back to the surface and escapes into the air as a "
                "gas",
        ],
        "correct_index": 1,
        "why": "Decomposers release part of the carbon back into the water, "
               "and the rest is buried in sediment, where over very long times "
               "it can become part of a rock or a fossil fuel.",
    },
    {
        "id": "ks4-carbon-cycle-s18",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a garden compost heap loses mass and gives off "
                "carbon dioxide as it rots.",
        "options": [
            "Worms carry the material down into the soil beneath the heap",
            "The heap dries out, and the mass that is lost is the water "
                "evaporating away",
            "Decomposers respire the material away, releasing it as gas",
            "The heap is compressed by its own weight, so it merely seems "
                "smaller",
        ],
        "correct_index": 2,
        "why": "Microorganisms break down the organic matter and respire it, "
               "so carbon leaves the heap as carbon dioxide gas and the solid "
               "mass falls.",
    },
    {
        "id": "ks4-carbon-cycle-s19",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the difference between a carbon source and a carbon "
                "sink.",
        "options": [
            "A source releases more carbon than it absorbs; a sink does "
                "the reverse",
            "A source holds carbon underground; a sink holds it in the sea",
            "A source is a gas and a sink is a solid form of that carbon",
            "A source is natural and a sink is made by human activity",
        ],
        "correct_index": 0,
        "why": "The words describe the net direction: a source puts more "
               "carbon into the atmosphere than it takes out, and a sink takes "
               "out more than it puts in.",
    },
    {
        "id": "ks4-carbon-cycle-s20",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Atmospheric carbon dioxide has risen from 280 parts per "
                "million to 420 parts per million. Calculate the percentage "
                "increase.",
        "options": [
            "140%",
            "14%",
            "33%",
            "50%",
        ],
        "correct_index": 3,
        "why": "The rise is 420 − 280 = 140 ppm, and 140 ÷ 280 × 100 = 50%.",
    },
    {
        "id": "ks4-carbon-cycle-s21",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A charity says planting a tree removes carbon from the air. "
                "Explain why this is only true while the tree is alive and "
                "growing.",
        "options": [
            "Carbon dioxide leaks back out of living wood through the bark",
            "A dead tree draws carbon dioxide back out of the air as it "
                "rots",
            "Once it dies, decay or burning returns that carbon to the air",
            "A tree stops photosynthesising long before it finally dies",
        ],
        "correct_index": 2,
        "why": "The carbon is stored in the tree's biomass; when the tree dies "
               "and decomposes or is burned, that carbon is released again as "
               "carbon dioxide.",
    },
    {
        "id": "ks4-carbon-cycle-s22",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why keeping large herds of cattle adds a "
                "carbon-containing greenhouse gas other than carbon dioxide.",
        "options": [
            "Microorganisms in their digestive systems produce methane",
            "Cattle absorb methane from the grass and release it unchanged",
            "Their hides give off methane steadily throughout their lives",
            "Cattle breathe out methane instead of carbon dioxide when "
                "they rest",
        ],
        "correct_index": 0,
        "why": "The microorganisms that digest grass in a cow's gut break it "
               "down without oxygen, and that anaerobic process produces "
               "methane.",
    },
    {
        "id": "ks4-carbon-cycle-s23",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the carbon held in a limestone cliff is described "
                "as a long-term store.",
        "options": [
            "Carbon in rock is chemically different and cannot ever be "
                "moved",
            "Limestone is underground, and nothing underground can reach "
                "the air",
            "Limestone formed quite recently, so its carbon is still new",
            "It stays locked in the rock for millions of years unless "
                "heated",
        ],
        "correct_index": 3,
        "why": "Carbon in limestone remains there over geological timescales, "
               "returning only when the rock is weathered, heated in cement "
               "making, or erupted by a volcano.",
    },
    {
        "id": "ks4-carbon-cycle-s24",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how carbon returns from a living badger to the "
                "atmosphere without the badger dying.",
        "options": [
            "It leaves through the skin as the badger loses heat to the "
                "air",
            "Respiration breaks down glucose and releases carbon dioxide",
            "The badger's fur takes carbon from the body and sheds it "
                "outside",
            "Carbon leaves in the water that the badger drinks and then "
                "passes out again",
        ],
        "correct_index": 1,
        "why": "Aerobic respiration in every cell breaks down glucose, and the "
               "carbon dioxide produced is breathed out.",
    },
    {
        "id": "ks4-carbon-cycle-s25",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One hectare of woodland stores 180 tonnes of carbon. "
                "Calculate the mass of carbon stored in 12 hectares.",
        "options": [
            "2160 tonnes",
            "15 tonnes",
            "1800 tonnes",
            "192 tonnes",
        ],
        "correct_index": 0,
        "why": "180 tonnes per hectare × 12 hectares = 2160 tonnes of carbon.",
    },
    {
        "id": "ks4-carbon-cycle-s26",
        "subtopic_slug": "carbon-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the carbon in a plastic bottle made from crude "
                "oil was once part of a living organism.",
        "options": [
            "Plastic absorbs carbon from the air during the moulding "
                "process",
            "The carbon in oil was formed by volcanoes and never was alive",
            "Plastic is made in a factory, so its carbon is manufactured "
                "there",
            "Crude oil formed from the buried remains of marine organisms",
        ],
        "correct_index": 3,
        "why": "Crude oil is a fossil fuel formed over millions of years from "
               "the remains of marine organisms, so its carbon was fixed by "
               "photosynthesis long ago.",
    },
    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # The rate imbalance from every side: offset arithmetic that does not
    # close, fast against slow cycles, the seasonal wobble, a warming soil.
    {
        "id": "ks4-carbon-cycle-h05",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that burning wood is carbon neutral, for a "
                "plantation that is replanted and for a forest that is not.",
        "options": [
            "It holds for the unreplanted forest, as the cleared ground "
                "absorbs the gas",
            "It holds in both cases, because wood always regrows somewhere "
                "else",
            "It holds for the replanted plantation only, as regrowth "
                "reabsorbs the carbon",
            "It fails in both cases, because burning wood releases carbon "
                "that was never in the air",
        ],
        "correct_index": 2,
        "why": "Only regrowth takes the released carbon back out of the air; "
               "with no replanting the carbon stays in the atmosphere and the "
               "store is permanently smaller.",
    },
    {
        "id": "ks4-carbon-cycle-h06",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station burns 2000 tonnes of coal a day, and the coal "
                "is 80% carbon by mass. Calculate the mass of carbon burned in "
                "365 days.",
        "options": [
            "584 000 tonnes",
            "730 000 tonnes",
            "1600 tonnes",
            "58 400 tonnes",
        ],
        "correct_index": 0,
        "why": "2000 × 0.80 = 1600 tonnes of carbon per day, and 1600 × 365 = "
               "584 000 tonnes in a year.",
    },
    {
        "id": "ks4-carbon-cycle-h07",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 25 hectare woodland absorbs 8 tonnes of carbon per hectare "
                "each year. Determine how many years it needs to absorb 4000 "
                "tonnes.",
        "options": [
            "160 years",
            "500 years",
            "5 years",
            "20 years",
        ],
        "correct_index": 3,
        "why": "The wood absorbs 25 × 8 = 200 tonnes a year, and 4000 ÷ 200 = "
               "20 years.",
    },
    {
        "id": "ks4-carbon-cycle-h08",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Measured atmospheric carbon dioxide rises each winter and "
                "falls each summer, on top of a long-term rise. Suggest the "
                "cause of this yearly pattern.",
        "options": [
            "More fuel is burned in summer and hardly any in the winter",
            "Northern forests photosynthesise strongly in summer and not "
                "in winter",
            "Cold winter air holds more carbon dioxide than warm summer "
                "air can",
            "Ocean currents carry the gas north in winter and south in "
                "summer",
        ],
        "correct_index": 1,
        "why": "Most of the world's land plants are in the northern "
               "hemisphere, so their summer photosynthesis draws the "
               "atmospheric concentration down and their winter dormancy lets "
               "it rise.",
    },
    {
        "id": "ks4-carbon-cycle-h09",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the timescale on which carbon moves through living "
                "organisms with the timescale on which it moves through rocks "
                "and fossil fuels.",
        "options": [
            "Living organisms cycle it in years; rocks and fuels take "
                "millions of years",
            "Rocks cycle it fastest, as weathering happens whenever it "
                "rains",
            "Living organisms take ages; rock stores turn over each decade",
            "Both move over a few years, since carbon is one element",
        ],
        "correct_index": 0,
        "why": "Photosynthesis, feeding, respiration and decay move carbon "
               "within years, while burial, fossilisation and rock formation "
               "work over millions of years.",
    },
    {
        "id": "ks4-carbon-cycle-h10",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that planting trees on its own will return "
                "atmospheric carbon dioxide to its old level.",
        "options": [
            "It will not help, because trees release as much as they "
                "absorb",
            "It will, as soon as enough trees are planted anywhere in the "
                "world",
            "It will, because trees absorb carbon dioxide faster than any "
                "process releases it",
            "It helps, but the land needed and the rate of emission both "
                "limit it",
        ],
        "correct_index": 3,
        "why": "Trees are a genuine sink, but the area of land required is "
               "enormous and emissions continue meanwhile, so planting alone "
               "cannot close the gap.",
    },
    {
        "id": "ks4-carbon-cycle-h11",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the effect of the oceans warming on the amount of "
                "carbon dioxide they can hold dissolved.",
        "options": [
            "It rises, because warm water molecules move faster and trap "
                "more gas",
            "It falls, because a gas is less soluble in warmer water",
            "It stays the same, because solubility does not depend on "
                "temperature",
            "It rises, because warm seas support more shell-building life",
        ],
        "correct_index": 1,
        "why": "Gases dissolve less readily as temperature rises, so a warming "
               "ocean holds less carbon dioxide and its value as a sink falls.",
    },
    {
        "id": "ks4-carbon-cycle-h12",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lake bed holds deep, waterlogged sediment full of dead "
                "plant material. Predict what happens to its carbon if the "
                "lake is drained.",
        "options": [
            "It becomes limestone once the sediment dries out",
            "It stays put, since sediment carbon cannot reach the air",
            "Oxygen reaches it, decay speeds up and carbon dioxide is "
                "released",
            "It is washed away as solid carbon when the water drains",
        ],
        "correct_index": 2,
        "why": "Waterlogging had excluded the oxygen decomposers need; "
               "draining lets aerobic decay resume, and the stored carbon is "
               "respired back into the atmosphere.",
    },
    {
        "id": "ks4-carbon-cycle-h13",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how one carbon atom can be part of the air, then of a "
                "leaf, then of a limestone cliff.",
        "options": [
            "Each store makes its own carbon, which is why the forms "
                "differ",
            "The atom changes into a different element in each of the "
                "stores",
            "Carbon atoms are made and destroyed as they pass between "
                "stores",
            "The same atoms are recycled; carbon is never created or "
                "destroyed",
        ],
        "correct_index": 3,
        "why": "The total amount of carbon is fixed; atoms are not created or "
               "destroyed but moved between stores by photosynthesis, feeding, "
               "respiration, decay and burial.",
    },
    {
        "id": "ks4-carbon-cycle-h14",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A forest holding 500 tonnes of carbon loses 35% of it when "
                "part of the forest is cleared and burned. Determine the mass "
                "of carbon released.",
        "options": [
            "35 tonnes",
            "175 tonnes",
            "325 tonnes",
            "465 tonnes",
        ],
        "correct_index": 1,
        "why": "35% of 500 tonnes is 0.35 × 500 = 175 tonnes of carbon "
               "released.",
    },
    {
        "id": "ks4-carbon-cycle-h15",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the effect on the carbon cycle if soils across the "
                "world warm by two degrees Celsius.",
        "options": [
            "Soils absorb more carbon dioxide, because warm soil holds gas "
                "better",
            "Decomposers work more slowly, so soil carbon is locked in "
                "tighter",
            "Decomposers respire faster, so soils release more carbon "
                "dioxide",
            "Soil carbon is unaffected, because the rate of decay depends "
                "only on moisture",
        ],
        "correct_index": 2,
        "why": "Decay is an enzyme-driven process that speeds up with "
               "temperature, so warmer soils respire their stored carbon back "
               "into the air more quickly.",
    },
    {
        "id": "ks4-carbon-cycle-h16",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says animals are not really part of the carbon "
                "cycle because they cannot photosynthesise. Evaluate this.",
        "options": [
            "Wrong, because animals take carbon in by feeding and release "
                "it by respiring",
            "Correct, because animals release only water vapour and not "
                "carbon dioxide",
            "Wrong, because animals photosynthesise slowly using the "
                "chlorophyll in their food",
            "Correct, since organisms that photosynthesise move the carbon "
                "about",
        ],
        "correct_index": 0,
        "why": "Animals occupy two arrows of the cycle: they take carbon in as "
               "food and return it as carbon dioxide from respiration, and "
               "their remains feed decomposers.",
    },
    {
        "id": "ks4-carbon-cycle-h17",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a deeply buried landfill site gives off methane "
                "while a shallow compost heap gives off carbon dioxide.",
        "options": [
            "Landfill waste is plastic, and plastic gives off methane as "
                "it rots",
            "Buried waste has no oxygen, so decay there is anaerobic",
            "Compost heaps are turned, and turning converts methane to "
                "carbon dioxide",
            "Landfill is colder, and cold decay produces methane",
        ],
        "correct_index": 1,
        "why": "Decomposers deep in landfill work without oxygen and produce "
               "methane, while a shallow, aerated compost heap supports "
               "aerobic decay, which gives carbon dioxide.",
    },
    {
        "id": "ks4-carbon-cycle-h18",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One dairy cow releases about 100 kg of methane a year. "
                "Determine the mass, in tonnes, released by a herd of 250 cows "
                "in one year.",
        "options": [
            "2500 tonnes",
            "2.5 tonnes",
            "25 tonnes",
            "250 tonnes",
        ],
        "correct_index": 2,
        "why": "250 × 100 kg = 25 000 kg, and 25 000 kg ÷ 1000 = 25 tonnes.",
    },
    {
        "id": "ks4-carbon-cycle-h19",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare planting fast-growing conifers with restoring native "
                "broadleaved woodland, as ways of storing carbon.",
        "options": [
            "Conifers store carbon faster at first; native woodland stores "
                "it longer and holds more species",
            "Native woodland stores carbon faster and supports fewer "
                "species than conifers do",
            "Conifers store more carbon in every year of their life and "
                "also hold more species",
            "Neither stores any carbon, because trees give out as much as "
                "they take in",
        ],
        "correct_index": 0,
        "why": "Fast growth means quick uptake, but conifer plantations are "
               "often felled young, while a native wood keeps its carbon for "
               "far longer and carries far more biodiversity.",
    },
    {
        "id": "ks4-carbon-cycle-h20",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The mass of carbon held in living organisms has changed "
                "little while atmospheric carbon has risen sharply. Explain "
                "what this shows about the source of the extra gas.",
        "options": [
            "Living organisms have released carbon they created themselves",
            "The atmosphere has shrunk, so the same carbon is more crowded",
            "The extra carbon has been created in the atmosphere from "
                "nothing",
            "It has come mainly from fossil stores, not from living things",
        ],
        "correct_index": 3,
        "why": "If the living store is unchanged, the extra atmospheric carbon "
               "must have come out of another store — the fossil fuels and, to "
               "a lesser extent, soils being emptied by human activity.",
    },
    {
        "id": "ks4-carbon-cycle-h21",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to the carbon in an oak beam built into "
                "a house that stands for 200 years.",
        "options": [
            "It turns into coal within the wall over the two centuries",
            "It escapes slowly as a gas, because dry wood goes on "
                "breathing out carbon",
            "It stays locked in the timber until the wood decays or is "
                "burned",
            "It is drawn back into living trees through the ground beneath",
        ],
        "correct_index": 2,
        "why": "Seasoned timber is dry enough to resist decomposers, so the "
               "carbon fixed by that tree stays in the beam and only returns "
               "when the wood finally rots or burns.",
    },
    {
        "id": "ks4-carbon-cycle-h22",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why global carbon dioxide levels are monitored from a "
                "remote mountain observatory rather than from a city centre.",
        "options": [
            "A remote site avoids local traffic and industry, so it shows "
                "the global level",
            "Carbon dioxide rises, so its true level is only found high up",
            "City readings may not be published, so remote data is used "
                "instead",
            "Mountain air is thinner, so the instruments read more "
                "accurately",
        ],
        "correct_index": 0,
        "why": "Nearby sources would swamp the measurement; a remote site "
               "samples air that has mixed across the whole atmosphere, so the "
               "trend is a global one.",
    },
    {
        "id": "ks4-carbon-cycle-h23",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the carbon dioxide released when a fallen log decays "
                "with that released when the same log is burned.",
        "options": [
            "Decay releases more in total, because microorganisms add "
                "their own carbon to it",
            "Neither releases any, because the carbon stays in the ash and "
                "in the soil",
            "Burning releases far more in total, since decay releases none",
            "A similar total is released, but burning releases it far "
                "faster",
        ],
        "correct_index": 3,
        "why": "Both routes oxidise the same carbon back to carbon dioxide; "
               "the difference is rate, decay taking years and combustion "
               "minutes.",
    },
    {
        "id": "ks4-carbon-cycle-h24",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a coal seam is described as a carbon store while "
                "a field of wheat is better described as part of a flow.",
        "options": [
            "Coal holds more carbon per kilogram than any crop plant does",
            "Coal's carbon sits still for ages; the crop's returns within "
                "a year",
            "Coal is underground, and only underground carbon counts as "
                "stored",
            "A crop takes in no carbon, so it cannot store any of it",
        ],
        "correct_index": 1,
        "why": "A store holds carbon over long periods; the wheat's carbon is "
               "fixed, eaten and respired within a season, so it is moving "
               "through the cycle rather than being held.",
    },
    {
        "id": "ks4-carbon-cycle-h25",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One hectare of new woodland absorbs 6 tonnes of carbon "
                "dioxide a year. Determine the area needed to offset 480 "
                "tonnes a year.",
        "options": [
            "80 hectares",
            "8 hectares",
            "474 hectares",
            "2880 hectares",
        ],
        "correct_index": 0,
        "why": "480 tonnes ÷ 6 tonnes per hectare = 80 hectares of new "
               "woodland.",
    },
    {
        "id": "ks4-carbon-cycle-h26",
        "subtopic_slug": "carbon-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company calls itself carbon neutral because it pays for "
                "trees to be planted while continuing to burn natural gas. "
                "Evaluate this claim.",
        "options": [
            "It is sound, because any carbon released is cancelled out by "
                "the carbon the trees absorb",
            "It is weak, because trees release more carbon dioxide than "
                "they ever take in",
            "It is sound, because the trees remove the gas as fast as it "
                "is burned",
            "It is weak, because the gas releases fossil carbon now and "
                "the trees absorb it slowly",
        ],
        "correct_index": 3,
        "why": "Burning gas moves carbon out of a fossil store immediately, "
               "while the planted trees take decades to absorb it — and only "
               "if they are never felled or burned.",
    },
]
