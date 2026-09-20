"""Biology · Ecology — the MRB-338 expansion of `waste-management`.

One leaf only: AQA 8461 §4.7.3.2. The original twelve rows in `ecology__a.py`
take pollution damaging habitats, sulfur dioxide by name, the two factors
driving waste upwards, treated sewage as the remedy, the eutrophication
sequence, acid rain falling downwind, a pesticide washed into a river, the
'only what you can see' misconception, a landfill calculation, two countries
changing one factor each, a river below a sewage works, and recycling set
against biodiversity.

This file takes what they leave: the three places pollution happens as a named
set, herbicides and pesticides told apart, what landfill actually is, the
individual steps inside a bloom rather than the sequence as a whole, what acid
rain does to a lake and to a soil, smoke particles on a leaf, leachate from a
tip, and the management side the spec names — filtering gases, treating sewage,
recycling, and reducing what is bought in the first place. The misconception
set is here in full: clear water read as clean water, a taller chimney read as
a solution, recycling read as zero waste, population read as the whole story,
and a lined tip read as a permanently safe one.

The weight follows the CONTENT. `easier` stays at eight because recall here is
a short list of places, chemicals and remedies, and a ninth way of asking it is
the same question in new words. The demand lives in tracing a pollutant from
its source to the species it removes, and in arithmetic on two factors moving
at once — a population and a per-person figure, which is where the spec's own
'more people AND higher living standards' lives. So `standard` and `harder`
carry twenty-two each.

Numbers here are the ones the subject supplies: masses of waste in tonnes,
waste per person per year, recycling rates before and after, dissolved oxygen
in milligrams per cubic decimetre, and a tip's remaining capacity.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The three places pollution happens, herbicide against pesticide, what
    # landfill is, fertiliser and a bloom, recycling, smoke, and sorting a
    # land pollutant from a water or air one.
    {
        "id": "ks4-waste-management-e05",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the three parts of the environment in which human "
                "pollution occurs.",
        "options": [
            "Water, air and land",
            "Rivers, lakes and seas",
            "Soil, rock and sand",
            "Towns, farms and factories",
        ],
        "correct_index": 0,
        "why": "The specification treats pollution as occurring in water, in "
               "air and on land, each with its own named sources.",
    },
    {
        "id": "ks4-waste-management-e06",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of chemical sprayed on a field to kill "
                "unwanted plants.",
        "options": [
            "A fertiliser, which is spread on a field to supply mineral ions "
                "to the crop growing there",
            "A herbicide",
            "A pesticide, which is sprayed on a crop in order to kill the "
                "insects feeding on it",
            "A fungicide, which is applied to a crop to control the moulds "
                "growing on its leaves",
        ],
        "correct_index": 1,
        "why": "A herbicide is a weedkiller: it is applied to destroy "
               "unwanted plants growing among a crop.",
    },
    {
        "id": "ks4-waste-management-e07",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower sprays a crop to control aphids eating its leaves. "
                "Name the type of chemical used.",
        "options": [
            "Herbicide",
            "Fertiliser",
            "Pesticide",
            "Compost",
        ],
        "correct_index": 2,
        "why": "A pesticide is applied to kill the animal pests feeding on a "
               "crop, and aphids are insect pests.",
    },
    {
        "id": "ks4-waste-management-e08",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to household waste that is sent to "
                "landfill.",
        "options": [
            "It is burned at a very high temperature and the ash is spread "
                "on nearby farmland",
            "It is sorted into materials, which are then sold on to be made "
                "into new products",
            "It is treated with enzymes until it dissolves and can be poured "
                "away into the sewers",
            "It is buried in the ground",
        ],
        "correct_index": 3,
        "why": "Landfill means burying waste in the ground, which takes up "
               "land and can leak chemicals into soil and water.",
    },
    {
        "id": "ks4-waste-management-e09",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the substance washed off farmland that makes algae in a "
                "lake grow rapidly.",
        "options": [
            "Fertiliser",
            "Sulfur dioxide",
            "Vinegar",
            "Sand",
        ],
        "correct_index": 0,
        "why": "Fertiliser supplies nitrates and phosphates, and once these "
               "reach a lake the algae in it can grow very quickly.",
    },
    {
        "id": "ks4-waste-management-e10",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one way of reducing the amount of household waste that "
                "has to be buried.",
        "options": [
            "Recycling materials such as glass, metal and paper",
            "Spraying more pesticide onto the crops grown on the farmland "
                "beside the tip",
            "Digging the tip deeper so that a greater mass of waste fits "
                "into the same area",
            "Releasing the waste into a river so that it is carried away "
                "downstream to the sea",
        ],
        "correct_index": 0,
        "why": "Recycling sends materials back into manufacture instead of "
               "into the ground, so less land is buried under waste.",
    },
    {
        "id": "ks4-waste-management-e11",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Smoke particles are released when a fuel is burned. Name the "
                "type of pollution this causes.",
        "options": [
            "Water pollution, because the particles dissolve in rain and are "
                "carried into the rivers",
            "Land pollution, because the particles are buried in the ground "
                "along with other waste",
            "Air pollution",
            "No pollution, because smoke particles are too small to affect a "
                "living thing",
        ],
        "correct_index": 2,
        "why": "Smoke and smoke particles are released into the atmosphere, "
               "so they are a form of air pollution.",
    },
    {
        "id": "ks4-waste-management-e12",
        "subtopic_slug": "waste-management",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is pollution of the land rather than of water "
                "or of air?",
        "options": [
            "Sulfur dioxide released from the chimney of a coal-fired power "
                "station",
            "Untreated sewage released into the tidal stretch of a river "
                "mouth",
            "Smoke drifting from a garden bonfire",
            "Herbicide soaking into the soil of a sprayed field",
        ],
        "correct_index": 3,
        "why": "Herbicides and pesticides applied to a field enter the soil "
               "itself, which is why the spec lists them as land pollution.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # From a source to the species it removes, and the remedies.
    {
        "id": "ks4-waste-management-s05",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country's population has stopped growing, yet the mass of "
                "waste it produces each year is still rising. Suggest why.",
        "options": [
            "Its standard of living is rising, so each person buys and "
                "discards more than before",
            "Waste grows heavier as it is stored, because it takes up water "
                "from the air around it and from the rain that falls on it",
            "A population that has stopped growing contains more adults, and "
                "adults produce no waste",
            "Recycling raises the total mass of waste a country has to deal "
                "with each year",
        ],
        "correct_index": 0,
        "why": "The spec names two drivers, and only one of them has "
               "stalled: a rising standard of living means more resources "
               "used and more thrown away per person.",
    },
    {
        "id": "ks4-waste-management-s06",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fish in a lake die after an algal bloom. State the stage at "
                "which the oxygen is used up, and explain why.",
        "options": [
            "While the algae are growing, because a growing alga respires "
                "but cannot yet photosynthesise",
            "After the algae die, because decomposers feeding on them respire "
                "and use the dissolved oxygen up",
            "While the algae are growing, because algae take oxygen out of "
                "water in order to build their cell walls",
            "Before the algae appear, because the fertiliser reaching the lake "
                "reacts with the oxygen dissolved in it",
        ],
        "correct_index": 1,
        "why": "The bloom itself adds oxygen by photosynthesis; the oxygen "
               "crash comes from the decomposers that multiply on the dead "
               "algae afterwards.",
    },
    {
        "id": "ks4-waste-management-s07",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thick algal bloom covers the surface of a pond. Explain why "
                "the rooted plants on the pond bed die.",
        "options": [
            "The algae release a poison into the water that kills any rooted "
                "plant it reaches",
            "The algae take up the water in the pond and leave the rooted "
                "plants dry",
            "The algae raise the temperature of the pond until the rooted "
                "plants are scalded",
            "The algae shade the bed, so the plants below cannot get the "
                "light they need to photosynthesise",
        ],
        "correct_index": 3,
        "why": "A surface bloom blocks the light, and plants on the bed "
               "cannot photosynthesise enough to survive without it.",
    },
    {
        "id": "ks4-waste-management-s08",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Acid rain falls on an upland lake for many years. Explain "
                "why fewer fish species are found in it.",
        "options": [
            "The rain lowers the lake's pH, and species that cannot tolerate "
                "acidic water die out",
            "The rain adds so much water that the lake overflows and carries "
                "most of its fish away downstream",
            "The rain cools the lake, and fish cannot survive at that "
                "temperature",
            "The rain washes the fish eggs onto the shore, where they dry out "
                "before they can hatch",
        ],
        "correct_index": 0,
        "why": "Acid rain acidifies the water, and species with a narrow pH "
               "tolerance are lost, so the number of species falls.",
    },
    {
        "id": "ks4-waste-management-s09",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain two ways in which acid rain damages the trees of a "
                "conifer forest.",
        "options": [
            "It burns the bark off the trunk, and it raises the pH of the "
                "soil so far that the roots cannot function at all",
            "It freezes on the needles overnight, and it seals the stomata so "
                "that no carbon dioxide can enter the needle",
            "It damages the needles, and it washes mineral ions out of the "
                "soil so the roots take up fewer of them",
            "It dissolves the wood of the trunk, and it kills the insects "
                "that the trees rely on for pollination",
        ],
        "correct_index": 2,
        "why": "Acid rain harms the leaves directly and also leaches mineral "
               "ions from the soil, so the trees are damaged and "
               "underfed.",
    },
    {
        "id": "ks4-waste-management-s10",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sulfur dioxide is removed from the waste gases of a power "
                "station before they leave the chimney. Explain the benefit.",
        "options": [
            "It stops the waste gases from carrying smoke particles out over "
                "the countryside around the station",
            "It raises the temperature of the waste gases, which makes the "
                "chimney draw the gases upwards faster",
            "It removes the carbon dioxide too, so the station stops adding "
                "to global warming",
            "Less of the gas reaches the atmosphere, so less acid rain forms "
                "downwind of the station",
        ],
        "correct_index": 3,
        "why": "Sulfur dioxide dissolves in cloud water to make acid rain, so "
               "capturing it at the chimney is what prevents the rain "
               "forming.",
    },
    {
        "id": "ks4-waste-management-s11",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Leaves of trees beside a busy road are coated with a layer "
                "of soot. Explain the effect on the growth of those trees.",
        "options": [
            "Growth slows, because less light reaches the leaf, so less "
                "photosynthesis takes place",
            "Growth speeds up, because the dark coating absorbs energy and "
                "warms the leaf through",
            "Growth is unchanged, because a tree takes the substances it "
                "needs in through its roots",
            "Growth speeds up, because soot is a source of the carbon a tree "
                "needs to build new wood",
        ],
        "correct_index": 0,
        "why": "Soot on the leaf surface blocks light reaching the "
               "chloroplasts, so the rate of photosynthesis and therefore "
               "growth falls.",
    },
    {
        "id": "ks4-waste-management-s12",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A herbicide is sprayed along the edges of a crop field. "
                "Suggest why the number of insect species there falls.",
        "options": [
            "The herbicide is designed to kill insects as well as plants, so "
                "it poisons them directly",
            "The wild plants the insects fed on are killed, so the insects "
                "lose their food supply",
            "The herbicide makes the soil too acidic for the insects to lay "
                "their eggs in it",
            "The crop grows taller once the weeds are gone, and the insects "
                "cannot fly that high",
        ],
        "correct_index": 1,
        "why": "A herbicide removes the wild plants; the insects that depend "
               "on those plants for food and shelter go with them.",
    },
    {
        "id": "ks4-waste-management-s13",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how recycling aluminium drinks cans reduces the "
                "pressure humans put on land.",
        "options": [
            "Recycled cans are lighter, so a lorry carries more and burns "
                "less fuel",
            "Recycled aluminium releases mineral ions into the soil, which "
                "makes the land around a recycling plant more fertile",
            "Recycling turns the cans into a gas, so no land is needed for "
                "them",
            "Less ore has to be quarried and fewer cans are buried, so less "
                "land is dug up or filled in",
        ],
        "correct_index": 3,
        "why": "Recycling cuts demand at both ends: less quarrying to get new "
               "metal and less landfill to bury the old, so less habitat is "
               "destroyed.",
    },
    {
        "id": "ks4-waste-management-s14",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rain falls on an unlined tip for years. Explain how the "
                "buried waste can pollute the water in the rock below.",
        "options": [
            "Water soaking through the waste dissolves chemicals out of it "
                "and carries them downwards",
            "The waste gives off a gas that sinks through the rock and "
                "dissolves in the water held there",
            "The weight of the waste squeezes the rock, and squeezed rock "
                "releases its own toxic chemicals",
            "The waste warms the rock beneath it, and warm rock cannot hold "
                "clean water for very long",
        ],
        "correct_index": 0,
        "why": "Rain percolating through buried waste picks up dissolved "
               "chemicals and carries them down into the groundwater.",
    },
    {
        "id": "ks4-waste-management-s15",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Untreated sewage enters a river. Explain why the dissolved "
                "oxygen in the water falls.",
        "options": [
            "Sewage is warmer than river water, and warm water holds less "
                "dissolved gas",
            "Sewage reacts chemically with the oxygen in the water, with no "
                "living organism taking any part",
            "Decomposers multiply on the organic waste and use the dissolved "
                "oxygen up as they respire",
            "Sewage forms a skin across the river that stops the water "
                "beneath it from flowing downstream",
        ],
        "correct_index": 2,
        "why": "Sewage is rich in organic matter, so decomposer numbers rise "
               "sharply and their aerobic respiration strips the oxygen out "
               "of the water.",
    },
    {
        "id": "ks4-waste-management-s16",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A factory doubles the height of its chimney and the air in "
                "the town nearby becomes cleaner. Explain why this is not a "
                "solution to the pollution.",
        "options": [
            "A taller chimney makes the gases hotter, and hot gases do more "
                "damage to a habitat than cool ones do",
            "A taller chimney costs the factory money, so it has less left to "
                "spend on treating its waste water",
            "Nothing has been removed at all; the same mass of gas now "
                "travels further before it does harm",
            "A taller chimney draws in more air, so the factory has to burn "
                "more fuel to keep working",
        ],
        "correct_index": 2,
        "why": "Nothing has been removed from the waste gas, so the "
               "pollutants are simply spread over a wider area and harm "
               "habitats further away.",
    },
    {
        "id": "ks4-waste-management-s17",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a drinks carton dropped in a town centre can end "
                "up polluting the sea.",
        "options": [
            "Rain washes it into a drain, and the drain empties into a river "
                "that runs to the sea",
            "It evaporates in warm weather and the vapour condenses again as "
                "rain falling over the sea",
            "Decomposers carry pieces of it through the soil until they reach "
                "the salt water at the coast",
            "It is buried by street cleaners in a tip, and the tip is always "
                "dug on the sea bed itself",
        ],
        "correct_index": 0,
        "why": "Street litter is carried by surface water into drains and "
               "then into rivers, and rivers discharge into the sea.",
    },
    {
        "id": "ks4-waste-management-s18",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A town's population grew by a tenth over ten years, but the "
                "mass of waste it produced grew by a third. Suggest why the "
                "second figure is the larger.",
        "options": [
            "Waste is always measured less carefully than population, so the "
                "larger figure is a measuring error",
            "Population figures count adults only, whereas waste figures "
                "include the waste produced by children",
            "Each person now throws away more than before, so the two "
                "increases add together",
            "Waste gains mass while it is stored, so a tip weighs more than "
                "the material that was put into it",
        ],
        "correct_index": 2,
        "why": "Total waste is population multiplied by waste per person, and "
               "both have risen, so the total rises faster than the "
               "population alone.",
    },
    {
        "id": "ks4-waste-management-s19",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Treating sewage is expensive. Suggest why a water company is "
                "still required to do it.",
        "options": [
            "Because treated sewage can be sold on as a fuel, and the sale "
                "covers the whole cost of the works",
            "Because untreated sewage would strip the oxygen from rivers and "
                "kill the species living in them",
            "Because untreated sewage would evaporate and form acid rain over "
                "the countryside downwind",
            "Because the law requires every river in the country to be kept "
                "at exactly the same temperature",
        ],
        "correct_index": 1,
        "why": "Untreated sewage causes decomposers to use up the dissolved "
               "oxygen, killing fish and invertebrates and reducing "
               "biodiversity.",
    },
    {
        "id": "ks4-waste-management-s20",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A landfill site has been closed, capped with clay and sown "
                "with grass. Suggest why it must still be monitored for many "
                "years.",
        "options": [
            "Because the grass sown on it will die unless it is fertilised "
                "again each spring",
            "Because the waste beneath it goes on decaying, releasing gas and "
                "liquid that could escape",
            "Because clay caps dissolve in rainwater within a few years and "
                "then have to be replaced",
            "Because the buried waste will begin to grow once the grass above "
                "it is established",
        ],
        "correct_index": 1,
        "why": "Decay continues underground for decades, so gas and leachate "
               "are still being produced and can escape if the cap fails.",
    },
    {
        "id": "ks4-waste-management-s21",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Pollution in a stream reduces the number of different "
                "species, not just the total number of animals. Explain why.",
        "options": [
            "Pollution kills the largest animals first, and it is the largest "
                "animals that make a habitat varied",
            "Pollution reduces the space available, and fewer species can fit "
                "into a smaller area of stream",
            "Species differ in what they can tolerate, so the sensitive ones "
                "are lost from the stream altogether",
            "Pollution makes the animals in a stream look alike, so fewer "
                "species can be counted",
        ],
        "correct_index": 2,
        "why": "Tolerance varies between species, so a pollutant removes some "
               "species completely while others survive, and the variety "
               "falls.",
    },
    {
        "id": "ks4-waste-management-s22",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A river holds very few species just below a sewage outfall "
                "but many again ten kilometres downstream. Explain the "
                "recovery.",
        "options": [
            "The sewage sinks to the bed within ten kilometres and so has no "
                "further effect on the water above it",
            "The river has been diluted by rain, so its water is warmer than "
                "at the outfall",
            "The species downstream are a different set that does not need "
                "dissolved oxygen",
            "The organic waste has been broken down and oxygen has dissolved "
                "back in as the water flows",
        ],
        "correct_index": 3,
        "why": "Decomposers finish the organic matter and the flowing water "
               "takes up oxygen from the air again, so oxygen-needing "
               "species can live there once more.",
    },
    {
        "id": "ks4-waste-management-s23",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Buying less is often described as better for the environment "
                "than recycling more. Explain why.",
        "options": [
            "Recycling produces more waste than it removes, because every "
                "recycling plant throws away more than it takes in",
            "Buying less avoids the resources and land used to make the item "
                "at all, while recycling only deals with it afterwards",
            "Recycled materials are of poor quality, so an item made from "
                "them has to be replaced far sooner",
            "Buying less reduces the population, and a smaller population "
                "produces less waste of every kind",
        ],
        "correct_index": 1,
        "why": "Recycling still needs resources, energy and transport; not "
               "using the resource in the first place avoids all of that as "
               "well as the waste.",
    },
    {
        "id": "ks4-waste-management-s24",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two pesticides kill the same pest equally well, but one "
                "breaks down in the soil within weeks and the other lasts for "
                "years. Explain which pollutes less.",
        "options": [
            "The long-lasting one, because a chemical that lasts longer needs "
                "to be sprayed far less often on the crop",
            "Neither, because a pesticide stops being a pollutant as soon as "
                "it has landed on the soil of a field",
            "The quick-breakdown one, because it is present in the soil and "
                "water for a much shorter time",
            "The long-lasting one, because it stays in the field rather than "
                "being carried into the river by rain",
        ],
        "correct_index": 2,
        "why": "The shorter a pesticide persists, the less time it has to "
               "reach soil organisms and watercourses, so it does less "
               "harm.",
    },
    {
        "id": "ks4-waste-management-s25",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two towns have populations of the same size but send very "
                "different masses of waste to landfill. Suggest two reasons.",
        "options": [
            "One has a higher standard of living, and one recycles a greater "
                "share of what it throws out",
            "One has more adults in it, and one has been measuring its waste "
                "for a greater number of years",
            "One is closer to its landfill site, and one uses lorries that "
                "are able to carry heavier loads",
            "One has warmer weather, and one has a river running through it "
                "that carries some waste away",
        ],
        "correct_index": 0,
        "why": "How much each person discards and how much of it is recycled "
               "are the two things that separate towns of the same size.",
    },
    {
        "id": "ks4-waste-management-s26",
        "subtopic_slug": "waste-management",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same volume of sewage is released into a fast tumbling "
                "river and into a still pond. Explain where it does less "
                "harm.",
        "options": [
            "The pond, because still water holds more dissolved oxygen than "
                "moving water can ever hold",
            "The river, because tumbling water takes up oxygen from the air "
                "and replaces what the decomposers use",
            "The pond, because the sewage settles on the bed and so cannot "
                "affect the water above it",
            "Neither, because the effect of a given volume of sewage is the "
                "same in any body of water",
        ],
        "correct_index": 1,
        "why": "Turbulent water dissolves oxygen from the air quickly, so the "
               "oxygen the decomposers use is replaced and fewer species are "
               "lost.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Two factors moving at once, masses and rates, then evaluation.
    {
        "id": "ks4-waste-management-h05",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A city produces 60 000 tonnes of household waste a year and "
                "recycles 35% of it. Calculate the mass sent to landfill each "
                "year.",
        "options": [
            "21 000 tonnes",
            "25 000 tonnes",
            "45 000 tonnes",
            "39 000 tonnes",
        ],
        "correct_index": 3,
        "why": "65% of the waste is not recycled, and 0.65 x 60 000 = 39 000 "
               "tonnes.",
    },
    {
        "id": "ks4-waste-management-h06",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A town of 25 000 people produces 420 kg of waste per person "
                "each year. Calculate the town's total annual waste in "
                "tonnes. One tonne is 1000 kg.",
        "options": [
            "105 tonnes",
            "1050 tonnes",
            "5950 tonnes",
            "10 500 tonnes",
        ],
        "correct_index": 3,
        "why": "25 000 x 420 = 10 500 000 kg, and dividing by 1000 gives "
               "10 500 tonnes.",
    },
    {
        "id": "ks4-waste-management-h07",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A city produces 80 000 tonnes of waste a year. Its recycling "
                "rate rises from 25% to 60%. Calculate the fall in the mass "
                "sent to landfill.",
        "options": [
            "28 000 tonnes",
            "32 000 tonnes",
            "48 000 tonnes of waste",
            "60 000 tonnes",
        ],
        "correct_index": 0,
        "why": "Landfill falls from 0.75 x 80 000 = 60 000 tonnes to 0.40 x "
               "80 000 = 32 000 tonnes, a fall of 28 000 tonnes.",
    },
    {
        "id": "ks4-waste-management-h08",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station released 4000 tonnes of sulfur dioxide a "
                "year. Equipment fitted to its chimneys now removes 92% of "
                "it. Calculate the mass still released each year.",
        "options": [
            "32 tonnes",
            "320 tonnes",
            "368 tonnes",
            "3680 tonnes",
        ],
        "correct_index": 1,
        "why": "8% of the sulfur dioxide escapes, and 0.08 x 4000 = 320 "
               "tonnes.",
    },
    {
        "id": "ks4-waste-management-h09",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Dissolved oxygen in a river falls from 9.0 mg per cubic "
                "decimetre above a sewage outfall to 2.7 mg per cubic "
                "decimetre below it. Calculate the percentage fall.",
        "options": [
            "6.3%",
            "30%",
            "70%",
            "233%",
        ],
        "correct_index": 2,
        "why": "The fall is 9.0 - 2.7 = 6.3, and 6.3 / 9.0 is 70% of the "
               "original value.",
    },
    {
        "id": "ks4-waste-management-h10",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An operator says its tip cannot pollute because the hole was "
                "lined with plastic before any waste went in. Evaluate this "
                "claim.",
        "options": [
            "Sound, because a plastic liner stops the buried waste decaying, "
                "so nothing is produced to escape",
            "Weak, because a liner can tear or perish, and gas produced by "
                "the decaying waste escapes upwards anyway",
            "Sound, because waste that cannot reach the rock below a tip "
                "cannot reach any habitat at all",
            "Weak, because a plastic liner dissolves in rainwater within a "
                "few months of being laid in the hole",
        ],
        "correct_index": 1,
        "why": "A liner reduces leaching while it holds, but it can fail over "
               "decades, and it does nothing about the methane and carbon "
               "dioxide the waste produces.",
    },
    {
        "id": "ks4-waste-management-h11",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Detergents containing phosphates are banned in a lake's "
                "catchment. Predict the effect on the algae in the lake, and "
                "explain.",
        "options": [
            "Algal growth falls, because less of a mineral ion they need is "
                "now reaching the lake",
            "Algal growth rises, because the detergent had been killing the "
                "algae as well as the fish",
            "Algal growth is unchanged, because algae take the ions they need "
                "from the air rather than the water",
            "Algal growth rises, because the lake now has more dissolved "
                "oxygen for the algae to respire",
        ],
        "correct_index": 0,
        "why": "Phosphate is one of the ions that allows a bloom to form, so "
               "cutting the supply limits algal growth.",
    },
    {
        "id": "ks4-waste-management-h12",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A factory owner argues that acid rain is not his concern "
                "because there is no forest within fifty kilometres of his "
                "works. Evaluate this argument.",
        "options": [
            "Sound, because acid rain falls within a few hundred metres of "
                "the chimney that released the gases",
            "Sound, because a factory is only responsible for the habitats "
                "that lie inside its own boundary fence",
            "Unsound, because the gases are carried by wind and fall as acid "
                "rain on habitats far away",
            "Unsound, because acid rain forms only over land that has no "
                "trees growing on it at all",
        ],
        "correct_index": 2,
        "why": "The acidic gases travel in the atmosphere before dissolving "
               "and falling, so the damage happens wherever the wind carries "
               "them.",
    },
    {
        "id": "ks4-waste-management-h13",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare burning household waste in an incinerator with "
                "burying it, in terms of the land used and the pollution "
                "produced.",
        "options": [
            "Burning uses more land but releases nothing at all, while "
                "burying uses less land and releases gases",
            "Both use the same area of land and release the same gases, so "
                "the choice between them makes no difference",
            "Burning uses less land and releases no gases, while burying uses "
                "more land and releases none either",
            "Burning uses less land but releases gases that must be cleaned; "
                "burying uses more land and can leak",
        ],
        "correct_index": 3,
        "why": "Incineration cuts the volume to be buried but produces waste "
               "gases needing treatment; landfill takes land and can release "
               "gas and leachate.",
    },
    {
        "id": "ks4-waste-management-h14",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A deposit is added to the price of every drinks bottle and "
                "repaid when the bottle is returned. Predict the effect on "
                "litter, and explain.",
        "options": [
            "Litter rises, because a bottle that has been paid for twice is "
                "worth less to the person who bought it",
            "Litter falls, because returning the bottle is now worth money to "
                "whoever picks it up",
            "Litter is unchanged, because the price of a bottle has no "
                "bearing on where it is finally dropped",
            "Litter falls, because the deposit makes each bottle heavier to "
                "carry",
        ],
        "correct_index": 1,
        "why": "The deposit gives the empty bottle a value, so people return "
               "it or collect discarded ones, and less is left as litter.",
    },
    {
        "id": "ks4-waste-management-h15",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A council advertises that its new recycling scheme means the "
                "town 'produces no waste'. Evaluate this statement.",
        "options": [
            "Sound, because any material that is recycled has stopped being "
                "waste at the moment it is collected",
            "Weak, because the same mass is still thrown away; recycling only "
                "changes where it goes, not whether it exists",
            "Sound, because a town that recycles everything has no need of a "
                "landfill site of any kind",
            "Weak, because recycling a material creates twice as much waste "
                "as burying that material would have done",
        ],
        "correct_index": 1,
        "why": "Recycling diverts waste from landfill but the material is "
               "still discarded, and collecting and reprocessing it uses "
               "resources of its own.",
    },
    {
        "id": "ks4-waste-management-h16",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A city's population rises by 20% while the waste each person "
                "produces falls by 10%. Calculate the percentage change in "
                "its total waste.",
        "options": [
            "a fall of 10%",
            "no change",
            "a rise of 8%",
            "a rise of 10%",
        ],
        "correct_index": 2,
        "why": "Total waste scales as 1.20 x 0.90 = 1.08, which is a rise of "
               "8%.",
    },
    {
        "id": "ks4-waste-management-h17",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A factory says the water it returns to a river is clean "
                "'because you can see straight through it'. Evaluate this "
                "reasoning.",
        "options": [
            "Sound, because water that light passes through cannot be "
                "carrying anything harmful in it",
            "Sound, because the only pollutants that damage a river are the "
                "ones that make its water cloudy",
            "Weak, because clear water always contains more dissolved "
                "chemicals than cloudy water does",
            "Weak, because dissolved substances such as fertilisers and toxic "
                "chemicals leave water perfectly clear",
        ],
        "correct_index": 3,
        "why": "Clarity says nothing about what is dissolved: nitrate, "
               "phosphate and many toxic chemicals are invisible in "
               "solution.",
    },
    {
        "id": "ks4-waste-management-h18",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same total mass of fertiliser reaches a lake either in a "
                "single spill or spread evenly through the year. Suggest "
                "which does more damage.",
        "options": [
            "Neither, because the damage a fertiliser does depends on the "
                "total mass reaching the water",
            "The spread supply, because the algae are fed continuously and so "
                "never stop growing at any point in the year",
            "The single spill, because a sudden excess lets a bloom form that "
                "then dies and strips the oxygen",
            "The single spill, because fertiliser delivered quickly is more "
                "concentrated and therefore poisonous to fish",
        ],
        "correct_index": 2,
        "why": "A bloom needs a sudden surplus of nutrient; a slow supply is "
               "taken up gradually, so no mass of algae dies at once to "
               "trigger the oxygen crash.",
    },
    {
        "id": "ks4-waste-management-h19",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An old tip is capped, covered with soil and planted with "
                "trees and wildflowers. Predict the effect on the "
                "biodiversity of the site, and explain.",
        "options": [
            "It falls, because planting a site prevents the species that had "
                "colonised the bare waste from living there",
            "It is unchanged, because the buried waste decides what lives "
                "above it",
            "It rises, because the buried waste supplies mineral ions no "
                "soil has",
            "It rises, because a varied plant cover provides habitats and "
                "food for many more species",
        ],
        "correct_index": 3,
        "why": "Restoring a plant community gives food and shelter for "
               "insects, birds and mammals, so the number of species living "
               "on the site rises.",
    },
    {
        "id": "ks4-waste-management-h20",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A campaign calls for every pesticide to be banned "
                "immediately. Evaluate this proposal.",
        "options": [
            "It would remove a source of land and water pollution, but crop "
                "losses would rise and food would be scarcer",
            "It would have no effect either way, because pesticides do not "
                "reach the soil or the water at all",
            "It would raise crop yields, because pesticides damage the crop "
                "as much as they damage the pest",
            "It would end land pollution, because pesticides are the one "
                "chemical applied to a field",
        ],
        "correct_index": 0,
        "why": "The environmental gain is real, but pesticides protect yield, "
               "so a ban has a cost in food production that has to be "
               "weighed against it.",
    },
    {
        "id": "ks4-waste-management-h21",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A landfill site has 500 000 cubic metres of space left and "
                "receives 25 000 cubic metres of waste a year. Calculate how "
                "long it will last at that rate.",
        "options": [
            "20 years",
            "2 years",
            "25 years",
            "200 years",
        ],
        "correct_index": 0,
        "why": "500 000 / 25 000 = 20 years at the current rate of filling.",
    },
    {
        "id": "ks4-waste-management-h22",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A report states that rising waste is caused by population "
                "growth. Evaluate this explanation.",
        "options": [
            "Complete, because the mass of waste a country produces depends "
                "on the number of people in it",
            "Wrong, because a larger population produces less waste per "
                "person and so less waste in total",
            "Incomplete, because a rising standard of living raises the waste "
                "each person produces as well",
            "Wrong, because population growth has no bearing on how much "
                "waste a country has to deal with",
        ],
        "correct_index": 2,
        "why": "The spec names two drivers, and the report gives only one: "
               "waste per person is rising alongside the number of "
               "people.",
    },
    {
        "id": "ks4-waste-management-h23",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare making a glass bottle from recycled glass with "
                "making one from newly quarried sand, in terms of the "
                "pressure each puts on habitats.",
        "options": [
            "The recycled route puts more pressure on habitats, because "
                "collecting old glass disturbs far more land than a quarry",
            "Both put the same pressure on habitats, because the bottle "
                "produced at the end of each route is identical",
            "The new-sand route puts less pressure on habitats, because a "
                "quarry can be filled in once the sand has gone",
            "The recycled route puts less pressure on habitats, because less "
                "land is quarried and less is buried",
        ],
        "correct_index": 3,
        "why": "Recycling avoids opening new quarries and avoids burying the "
               "old bottle, so less habitat is destroyed at either end.",
    },
    {
        "id": "ks4-waste-management-h24",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sewage works is upgraded so that far less organic matter "
                "leaves it. Predict what a survey of the river below it will "
                "find a year later, and explain.",
        "options": [
            "Fewer species, because the decomposers on the organic matter "
                "are gone",
            "More species, because the dissolved oxygen has risen once the "
                "organic load was removed",
            "The same species, because a river's community is set by its "
                "rock and not by its water quality",
            "Fewer species, because the water has become too clean for river "
                "animals to find any food",
        ],
        "correct_index": 1,
        "why": "Less organic matter means fewer decomposers using oxygen, so "
               "dissolved oxygen recovers and oxygen-sensitive species can "
               "return.",
    },
    {
        "id": "ks4-waste-management-h25",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that invisible pollution cannot be a "
                "problem because it cannot be measured. Evaluate this "
                "argument.",
        "options": [
            "Sound, because a pollutant that cannot be seen leaves no trace "
                "of itself in the habitat it enters",
            "Unsound, because invisible pollution is measured by counting the "
                "species that have left a habitat",
            "Sound, because the harm a pollutant does is proportional to how "
                "cloudy it makes the water it enters",
            "Unsound: oxygen, pH and nitrate are measured routinely, and it "
                "is the pollution you never see that does most harm",
        ],
        "correct_index": 3,
        "why": "Invisibility is not immeasurability: oxygen, pH and nutrient "
               "concentrations are standard measurements, and it is the "
               "unseen pollutants that do most damage.",
    },
    {
        "id": "ks4-waste-management-h26",
        "subtopic_slug": "waste-management",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lake's catchment delivers 1200 kg of nitrate a year. A "
                "strip of rough grass planted along the streams removes 65% "
                "of it. Calculate the mass now reaching the lake.",
        "options": [
            "78 kg",
            "420 kg",
            "780 kg",
            "1135 kg",
        ],
        "correct_index": 1,
        "why": "35% still gets through, and 0.35 x 1200 = 420 kg a year.",
    },
]
