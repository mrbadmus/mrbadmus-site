"""Biology · Ecology — the MRB-338 expansion, subtopic `ecosystems`.

Spec 4.7.1. The weight falls on the four levels of organisation (organism,
population, community, ecosystem) and on interdependence, because those are the
two things every later part of ecology is built from and the two a pupil
confuses most: a habitat is read as an ecosystem, and a community is read as
including the rainfall. Named ecosystems — temperate woodland, tundra, coral
reef, deep ocean floor — carry the "characterised by its abiotic conditions"
point, and the artificial/natural line is examined through real managed places
(salmon pens, coppiced woods, fenced reserves, ornamental ponds) rather than in
the abstract.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-ecosystems-e05",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "All of the grey squirrels living in one wood are an example of "
                "which level of organisation?",
        "options": [
            "A community",
            "A population",
            "An ecosystem",
            "A habitat",
        ],
        "correct_index": 1,
        "why": "A population is all the individuals of one species living in "
               "the same area at the same time, which is exactly what all the "
               "grey squirrels in one wood are.",
    },
    {
        "id": "ks4-ecosystems-e06",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the level of organisation that includes all of the "
                "different species living together in one area.",
        "options": [
            "The population",
            "The habitat",
            "The organism",
            "The community",
        ],
        "correct_index": 3,
        "why": "A community is all of the populations of different species — "
               "animals, plants, fungi and microorganisms — living together in "
               "the same area.",
    },
    {
        "id": "ks4-ecosystems-e07",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A common frog lives in a garden pond. State the term for the "
                "particular place where an organism lives.",
        "options": [
            "Its habitat",
            "Its ecosystem",
            "Its community",
            "Its population",
        ],
        "correct_index": 0,
        "why": "A habitat is the specific place within an ecosystem where an "
               "organism lives, such as a pond, a woodland floor or a tree "
               "canopy.",
    },
    {
        "id": "ks4-ecosystems-e08",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what ecologists study.",
        "options": [
            "The non-living conditions of an area, such as its rainfall and pH",
            "The structure of cells and the reactions that take place in them",
            "How organisms interact with each other and with their environment",
            "The sorting of organisms into kingdoms, phyla, classes and orders",
        ],
        "correct_index": 2,
        "why": "Ecology is the study of the interactions between organisms, "
               "and between organisms and their physical surroundings.",
    },
    {
        "id": "ks4-ecosystems-e09",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a natural ecosystem found in the UK?",
        "options": [
            "A reservoir built to supply a city with drinking water",
            "A field of oilseed rape sown in the autumn",
            "A trout hatchery attached to a river",
            "A temperate deciduous woodland",
        ],
        "correct_index": 3,
        "why": "A temperate deciduous woodland forms and maintains itself "
               "without human management, while reservoirs, sown fields and "
               "hatcheries are built and kept going by people.",
    },
    {
        "id": "ks4-ecosystems-e10",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the term for a change in one species rippling outwards "
                "through a whole ecosystem.",
        "options": [
            "The carrying capacity",
            "The cascade effect",
            "The trophic level",
            "The carbon cycle",
        ],
        "correct_index": 1,
        "why": "A cascade effect is the knock-on change that spreads through a "
               "community because all of its species are interdependent.",
    },
    {
        "id": "ks4-ecosystems-e11",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Besides the animals and the plants, name two other groups of "
                "organisms that make up a woodland community.",
        "options": [
            "Rocks and soil",
            "Rainfall and wind",
            "Fungi and bacteria",
            "Minerals and gases",
        ],
        "correct_index": 2,
        "why": "A community is every living organism in the area, so fungi and "
               "bacteria belong to it alongside the animals and the plants.",
    },
    {
        "id": "ks4-ecosystems-e12",
        "subtopic_slug": "ecosystems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one thing that an ecosystem contains but a community "
                "does not.",
        "options": [
            "The non-living factors of the area",
            "The animals that live in the area",
            "The plants that grow in the area",
            "The fungi that grow in the area",
        ],
        "correct_index": 0,
        "why": "An ecosystem is the community plus all of the abiotic factors "
               "of the same area — temperature, rainfall, light, soil pH and "
               "the rest.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-ecosystems-s05",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Beavers fell trees and dam a stream to make a pond. State "
                "what the beavers, the trees, the fish and the pond water "
                "make up when taken together.",
        "options": [
            "A habitat",
            "An ecosystem",
            "A food web",
            "A population",
        ],
        "correct_index": 1,
        "why": "Living organisms taken together with the non-living water they "
               "live in make an ecosystem; the organisms on their own would be "
               "only the community.",
    },
    {
        "id": "ks4-ecosystems-s06",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bees visit apple blossom to collect nectar. Describe how the "
                "apple tree benefits from the visit.",
        "options": [
            "Pollen is carried between flowers, so the tree can set seed",
            "Nectar is removed, so the tree keeps the sugar it would otherwise "
            "have lost",
            "The bee's weight bends the stalk, so the petals open more widely",
            "The bee warms the flower, so the seeds inside ripen more quickly",
        ],
        "correct_index": 0,
        "why": "The bee transfers pollen from flower to flower as it feeds, "
               "and that pollination is what allows the tree to produce seeds "
               "and fruit.",
    },
    {
        "id": "ks4-ecosystems-s07",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A salmon farm's pens hold one species only. Name the type of "
                "planting or stocking that an ecosystem dominated by a single "
                "species in this way is called.",
        "options": [
            "A belt transect",
            "A monoculture",
            "A quadrat",
            "A trophic level",
        ],
        "correct_index": 1,
        "why": "A monoculture is one species grown or stocked across a whole "
               "area, and it is why artificial ecosystems tend to hold fewer "
               "species than natural ones.",
    },
    {
        "id": "ks4-ecosystems-s08",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the abiotic conditions that characterise a tundra "
                "ecosystem.",
        "options": [
            "High temperatures throughout the year and heavy rainfall spread "
            "evenly",
            "Warm summers, mild winters and rain falling mostly in winter",
            "Very high light intensity, high temperatures and little rain",
            "Low temperatures, a short growing season and low rainfall",
        ],
        "correct_index": 3,
        "why": "Tundra is cold for most of the year, so plants have only a "
               "brief growing season, and its precipitation is low.",
    },
    {
        "id": "ks4-ecosystems-s09",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grassland fixes more energy from sunlight each year than a "
                "desert of the same area. Name the feature of an ecosystem "
                "that this difference describes.",
        "options": [
            "Its overall carrying capacity",
            "Its species diversity",
            "Its productivity",
            "Its interdependence",
        ],
        "correct_index": 2,
        "why": "Productivity is how much energy the producers of an ecosystem "
               "fix by photosynthesis in a given time.",
    },
    {
        "id": "ks4-ecosystems-s10",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pond is drained and covered with tarmac for a car park. "
                "Describe what happens to the pond community.",
        "options": [
            "It is lost, because its organisms have nowhere left to live",
            "It survives underground, because pond species live in damp soil",
            "It moves to the nearest pond, because organisms migrate if moved",
            "It is unchanged, because a community is defined by its species "
            "and not by its place",
        ],
        "correct_index": 0,
        "why": "Destroying the habitat removes the conditions the community "
               "needed, so the populations that made it up disappear from "
               "that area.",
    },
    {
        "id": "ks4-ecosystems-s11",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a field of wheat sown each spring and harvested "
                "each autumn is not a stable community.",
        "options": [
            "Wheat plants are producers, and a community needs consumers too",
            "The wheat competes with itself, which stops a community forming",
            "Wheat is a single species, and one species cannot be a community",
            "Its populations are removed and replanted rather than staying "
            "constant",
        ],
        "correct_index": 3,
        "why": "A stable community's populations stay roughly constant over "
               "time, and an arable field is cleared and re-sown every year so "
               "nothing in it is constant.",
    },
    {
        "id": "ks4-ecosystems-s12",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two sets of factors that have to be described in "
                "order to characterise any ecosystem.",
        "options": [
            "Its producers and the consumers that feed on each of them",
            "Its abiotic conditions and its biotic factors",
            "Its predators and its prey",
            "Its habitats and its trophic levels",
        ],
        "correct_index": 1,
        "why": "An ecosystem is defined by its non-living conditions — "
               "temperature, rainfall, light, soil — together with the living "
               "organisms present and how they interact.",
    },
    {
        "id": "ks4-ecosystems-s13",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nature reserve holds wild species but is fenced, grazed and "
                "managed by wardens. Explain why it counts as an artificial "
                "ecosystem.",
        "options": [
            "Each species living inside it was introduced there deliberately",
            "Wild species stop being wild once a fence is put around them",
            "Its conditions are created and maintained by human management",
            "It is smaller than the natural ecosystem that surrounded it",
        ],
        "correct_index": 2,
        "why": "An ecosystem is artificial when people create or maintain its "
               "conditions, and a reserve's fencing, grazing and scrub "
               "clearance are all human management.",
    },
    {
        "id": "ks4-ecosystems-s14",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Shrews eat earthworms and earthworms eat fallen beech leaves. "
                "Describe how shrews depend on beech trees.",
        "options": [
            "Indirectly, because the trees feed the worms the shrews eat",
            "Directly, because shrews eat the beech nuts that fall each autumn",
            "They do not, because shrews are carnivores rather than herbivores",
            "Directly, because shrews shelter inside the hollow trunks of old "
            "beech trees",
        ],
        "correct_index": 0,
        "why": "Interdependence can run through an intermediate species: "
               "without leaf litter there are no earthworms, and without "
               "earthworms there are no shrews.",
    },
    {
        "id": "ks4-ecosystems-s15",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the rainfall of an area is part of its ecosystem "
                "but not part of its community.",
        "options": [
            "Rainfall varies each year, whereas a community is fixed",
            "Rainfall is a non-living factor, and a community is the living part",
            "Rainfall is measured by people, a community by species",
            "Rainfall affects plants but not animals, so it is outside",
        ],
        "correct_index": 1,
        "why": "A community is all of the organisms in an area; adding the "
               "abiotic factors, rainfall included, is what makes it an "
               "ecosystem.",
    },
    {
        "id": "ks4-ecosystems-s16",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name three processes that hold the populations of a stable "
                "community within narrow limits.",
        "options": [
            "Photosynthesis, respiration and the decomposition of waste",
            "Pollination, seed dispersal and germination",
            "Migration, hibernation and camouflage",
            "Predation, competition and disease",
        ],
        "correct_index": 3,
        "why": "Predators, rivals and pathogens each raise the death rate as a "
               "population grows, which is what holds it at a roughly "
               "constant size.",
    },
    {
        "id": "ks4-ecosystems-s17",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A coral reef is built from the skeletons of living coral "
                "animals. Explain why it is still called a natural ecosystem.",
        "options": [
            "Corals are animals, so a reef counts as a community rather than an "
            "ecosystem",
            "Reefs were natural once but are now maintained by dive teams",
            "It forms and keeps going without any human management",
            "The skeletons are non-living, so a reef is an abiotic structure",
        ],
        "correct_index": 2,
        "why": "Natural and artificial describe whether people create and "
               "maintain an ecosystem, not whether organisms shaped it.",
    },
    {
        "id": "ks4-ecosystems-s18",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A garden pond and the whole Atlantic Ocean are both described "
                "as ecosystems. Explain how this can be correct.",
        "options": [
            "An ecosystem is any defined area with its community and abiotic "
            "factors",
            "Ecosystems are all the same size, so the ocean is many of them",
            "The ocean alone is a true ecosystem; a pond is too small to count",
            "A pond is an ecosystem in summer and part of a larger one later",
        ],
        "correct_index": 0,
        "why": "The term describes a relationship — a community together with "
               "its non-living surroundings — and that relationship holds at "
               "whatever scale the ecologist defines.",
    },
    {
        "id": "ks4-ecosystems-s19",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Blackbirds eat rowan berries and pass the seeds out some "
                "distance away. Describe the benefit to the rowan tree.",
        "options": [
            "The bird's gut fertilises each seed before it is dropped",
            "Its seeds are spread away from the parent tree's shade",
            "The berries that are left behind ripen faster once some are taken",
            "The tree loses less water once the berries have been taken",
        ],
        "correct_index": 1,
        "why": "Seed dispersal moves offspring away from the parent, where "
               "they would otherwise compete with it for light, water and "
               "minerals.",
    },
    {
        "id": "ks4-ecosystems-s20",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wood contains 4000 bluebell plants, 200 oak trees and 30 "
                "badgers. State what the 4000 bluebells are.",
        "options": [
            "The community of the wood",
            "The habitat of the wood",
            "The ecosystem of the wood",
            "One population in the wood",
        ],
        "correct_index": 3,
        "why": "All of the individuals of one species in one area form a "
               "population, so the bluebells are one population among several "
               "in that community.",
    },
    {
        "id": "ks4-ecosystems-s21",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the loss of one bee species can reduce the "
                "numbers of an animal that does not visit flowers.",
        "options": [
            "The animal breathes the same air as the bee, so its oxygen falls",
            "Bees give off a scent the animal uses to navigate its habitat",
            "Fewer plants are pollinated, so it has fewer plants to feed on",
            "The bee's predators switch to hunting the animal instead",
        ],
        "correct_index": 2,
        "why": "Interdependence is indirect as well as direct: losing a "
               "pollinator reduces the plants, and that shortage passes up to "
               "every consumer depending on them.",
    },
    {
        "id": "ks4-ecosystems-s22",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rabbit numbers in a meadow rise and fall a little each year "
                "but show no long-term trend. State what this shows about the "
                "meadow.",
        "options": [
            "It is a stable community",
            "It has no predators left",
            "It has an unlimited food supply",
            "It contains a single species",
        ],
        "correct_index": 0,
        "why": "A stable community is one whose populations stay roughly "
               "constant over time, fluctuating around a steady level rather "
               "than rising or falling.",
    },
    {
        "id": "ks4-ecosystems-s23",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Myxomatosis kills most of the rabbits grazing a chalk "
                "grassland. Predict the effect on the grassland plants over "
                "the next few years.",
        "options": [
            "The grassland becomes bare, as droppings no longer fertilise it",
            "Taller grasses and shrubs spread and shade out the small plants",
            "Plant numbers hold steady, as rabbits feed on insects not plants",
            "Every plant species increases in number, as grazing pressure has "
            "been removed",
        ],
        "correct_index": 1,
        "why": "Grazing keeps the taller, faster-growing plants in check, so "
               "removing the grazer lets them take over and crowd out the "
               "low-growing chalk species.",
    },
    {
        "id": "ks4-ecosystems-s24",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the light available in a tropical rainforest canopy "
                "with the light on the deep ocean floor.",
        "options": [
            "Both are brightly lit, but the ocean floor for fewer hours a day",
            "The ocean floor receives more, as water focuses light downwards",
            "The canopy is brightly lit; the deep ocean floor is always dark",
            "Both are dark, as the canopy is shaded by the leaves above it",
        ],
        "correct_index": 2,
        "why": "Sunlight does not penetrate more than a few hundred metres of "
               "seawater, so the deep floor is dark, while the canopy is the "
               "brightest layer of the forest.",
    },
    {
        "id": "ks4-ecosystems-s25",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an ornamental garden pond needs regular clearing "
                "but a natural lake does not.",
        "options": [
            "A garden pond holds no decomposers, so dead matter cannot rot",
            "A natural lake is larger, so its water evaporates before it stales",
            "A garden pond is lined, so nothing can colonise its bottom",
            "The pond is stocked and planted by people rather than self-balancing",
        ],
        "correct_index": 3,
        "why": "An artificial ecosystem is assembled by people and lacks the "
               "full set of checks and balances, so it needs human input to "
               "stay as its owner wants it.",
    },
    {
        "id": "ks4-ecosystems-s26",
        "subtopic_slug": "ecosystems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single wildflower species is lost from a meadow and the "
                "number of insect species there falls. Explain this result.",
        "options": [
            "Insects that fed on or pollinated that flower lost their food",
            "The remaining flowers spread and crowded the insects out",
            "Insects need a fixed number of plant species in order to survive",
            "Removing a plant raises the meadow's temperature and kills insects",
        ],
        "correct_index": 0,
        "why": "Specialist insects depend on particular plants for nectar, "
               "pollen or somewhere to lay their eggs, so losing the plant "
               "removes those species too.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-ecosystems-h05",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lynx are reintroduced to a forest where roe deer had been "
                "browsing every young rowan sapling. Predict what happens to "
                "the rowan trees, and explain why.",
        "options": [
            "They decline, because lynx strip bark from rowan in the winter",
            "They recover, because fewer deer survive to browse the saplings",
            "They are unchanged, because a predator acts only on its own prey",
            "They decline, because the deer move into the rowan for shelter",
        ],
        "correct_index": 1,
        "why": "A cascade effect runs down the chain: fewer browsing "
               "herbivores means the young trees survive long enough to grow.",
    },
    {
        "id": "ks4-ecosystems-h06",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that a community and an ecosystem are the same "
                "thing provided every species present is listed. Evaluate "
                "this claim.",
        "options": [
            "It is correct, because a full species list describes the area",
            "It is wrong, because an ecosystem holds just the animals present",
            "It is wrong, because an ecosystem also includes abiotic factors",
            "It is correct, because abiotic factors count as part of a community",
        ],
        "correct_index": 2,
        "why": "However complete the species list, it describes only the "
               "living part; the ecosystem is that community together with "
               "temperature, water, light, pH and the other non-living "
               "factors.",
    },
    {
        "id": "ks4-ecosystems-h07",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A visitor says a fenced nature reserve must hold the highest "
                "biodiversity possible because it is protected. Evaluate this.",
        "options": [
            "It is unsound, because managing for some species excludes others",
            "It is sound, because protection removes the threats to a habitat",
            "It is unsound, because a fence stops any species entering at all",
            "It is sound, because wardens introduce each species a site can hold",
        ],
        "correct_index": 0,
        "why": "A reserve is managed for chosen habitats and species, so its "
               "biodiversity reflects those choices rather than being "
               "automatically at a maximum.",
    },
    {
        "id": "ks4-ecosystems-h08",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Farm A grows one crop in every field. Farm B has mixed crops, "
                "hedges and a pond. Compare how each would cope with an "
                "outbreak of a crop pest.",
        "options": [
            "Farm A copes better, as a pest cannot spread within one species",
            "Both cope equally, as a pest outbreak depends on the weather alone",
            "Farm B copes worse, as mixed crops draw in the pests of a region",
            "Farm B copes better, as the pest cannot reach every field's crop",
        ],
        "correct_index": 3,
        "why": "A monoculture offers a pest an unbroken supply of its host "
               "plant, while a mixed farm breaks the crop up so an outbreak "
               "cannot spread through all of it.",
    },
    {
        "id": "ks4-ecosystems-h09",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a cascade effect caused by the loss of one "
                "species may take several years to become obvious.",
        "options": [
            "Each species takes years to notice that another has gone",
            "Populations take generations to grow or shrink, so steps are slow",
            "The effect begins once the lost species has decomposed",
            "Ecologists count the populations of a habitat once a decade",
        ],
        "correct_index": 1,
        "why": "A change in one population alters birth and death rates rather "
               "than numbers instantly, so each step in the chain takes "
               "generations to work through.",
    },
    {
        "id": "ks4-ecosystems-h10",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An island's one pollinating bird becomes extinct. Three of "
                "its four flowering plant species decline but the fourth does "
                "not. Suggest why that one is unaffected.",
        "options": [
            "It grows from seed faster than the other three species can",
            "Its flowers were pollinated by the bird's droppings rather than by "
            "its beak",
            "It is pollinated by the wind rather than by an animal",
            "It holds enough seed in the soil to last for the next century",
        ],
        "correct_index": 2,
        "why": "Wind-pollinated plants do not depend on an animal to carry "
               "their pollen, so the loss of the island's pollinator does not "
               "affect their reproduction.",
    },
    {
        "id": "ks4-ecosystems-h11",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drained marsh is re-flooded in order to restore it. "
                "Suggest why the original community may not return.",
        "options": [
            "Species lost from the area have to arrive from elsewhere first",
            "Water cannot fill the same channels twice, so the habitat differs",
            "Marsh plants need a dry first year before any flooding begins",
            "A restored marsh is artificial, so wild species will not settle",
        ],
        "correct_index": 0,
        "why": "Restoring the abiotic conditions is only half of the job — the "
               "community can reassemble only if the species themselves can "
               "still reach the site from surviving populations.",
    },
    {
        "id": "ks4-ecosystems-h12",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tundra community holds few species and a rainforest "
                "community holds thousands. Suggest which is more likely to be "
                "destabilised by the loss of one species, and why.",
        "options": [
            "The rainforest, as it holds far more species that could be "
            "affected by it",
            "Both equally, as each species matters as much as any other one",
            "The rainforest, as its species are larger and grow more slowly",
            "The tundra, as fewer species can take over the lost one's role",
        ],
        "correct_index": 3,
        "why": "Resilience comes from overlap: where many species share a "
               "role, losing one is absorbed, but in a species-poor community "
               "there may be no replacement.",
    },
    {
        "id": "ks4-ecosystems-h13",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement that a community whose population "
                "sizes stay constant must have no births and no deaths.",
        "options": [
            "It is sound, as a constant number means nothing enters or leaves",
            "It is unsound, because births and deaths can balance each other",
            "It is unsound, as the numbers of a stable community rise yearly",
            "It is sound, as births and deaths stop at the carrying capacity",
        ],
        "correct_index": 1,
        "why": "A population is constant when its birth rate and death rate "
               "are equal, not when both are zero — individuals are being "
               "replaced continuously.",
    },
    {
        "id": "ks4-ecosystems-h14",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pond dries out completely each August and refills each "
                "November. Evaluate whether it holds a stable community.",
        "options": [
            "Yes, because a pond that refills cannot lose any of its species",
            "No, because a community counts as stable if its water level is set",
            "No, because its populations crash and recolonise each year",
            "Yes, because drying out is natural, and natural conditions are "
            "stable",
        ],
        "correct_index": 2,
        "why": "Stability means populations remaining roughly constant, and a "
               "habitat that disappears every year forces its populations to "
               "zero and back — the opposite of constant.",
    },
    {
        "id": "ks4-ecosystems-h15",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student defines a population as all of the animals living "
                "in a wood. Identify the two errors in this definition.",
        "options": [
            "It should be one species, and need not be limited to animals",
            "It should be several species, and should be limited to plants",
            "It should be one species, and should cover a single season",
            "It should be several woods, and should include abiotic factors",
        ],
        "correct_index": 0,
        "why": "A population is all of the individuals of ONE species in an "
               "area, and that species can be a plant, a fungus or a bacterium "
               "as readily as an animal.",
    },
    {
        "id": "ks4-ecosystems-h16",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wheat field fixes more energy per hectare each year than "
                "the woodland it replaced, yet holds far fewer species. "
                "Explain how both of these can be true.",
        "options": [
            "Species number and energy fixed are one measure under two names",
            "Productivity measures energy fixed, not the variety of organisms",
            "Wheat fixes more energy because it holds more species than trees",
            "Woodland fixes less because trees do not photosynthesise in winter",
        ],
        "correct_index": 1,
        "why": "Productivity and biodiversity are different properties: a "
               "dense monoculture can capture a great deal of energy while "
               "supporting very few species.",
    },
    {
        "id": "ks4-ecosystems-h17",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deer in a fenced reserve increase for five years; the "
                "woodland understorey then disappears and the deer population "
                "crashes. Explain the sequence.",
        "options": [
            "The fence itself raised the deer's death rate, and that crashed "
            "the whole herd",
            "The deer ate the understorey, and that released more deer food",
            "Understorey plants poisoned the deer once grazed hard",
            "Rising deer numbers overgrazed their own food supply until it ran "
            "out",
        ],
        "correct_index": 3,
        "why": "Without predators a herbivore population passes what the "
               "vegetation can supply, and destroying its own food source then "
               "forces a crash.",
    },
    {
        "id": "ks4-ecosystems-h18",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a food shortage for one species can raise the "
                "numbers of a second species that eats something different.",
        "options": [
            "The two share the air they breathe, so one gains as one loses",
            "A food shortage raises each population, since fewer animals are "
            "competing",
            "Their shared predator declines, so the second is eaten less",
            "The shortage passes through the soil and fertilises the second",
        ],
        "correct_index": 2,
        "why": "A food web branches: the first species declines, the predator "
               "that ate it declines with it, and that predator's other prey "
               "is then hunted less.",
    },
    {
        "id": "ks4-ecosystems-h19",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Waste from a fish farm enriches the water of the sea loch "
                "around it and one seaweed species grows much more than "
                "before. Suggest what this shows about ecosystem boundaries.",
        "options": [
            "An artificial ecosystem can alter the natural one around it",
            "A natural ecosystem turns artificial once any waste reaches it",
            "Artificial and natural ecosystems cannot exchange materials",
            "The seaweed's growth proves the loch's own community has gone",
        ],
        "correct_index": 0,
        "why": "Ecosystem boundaries are drawn for convenience rather than "
               "being sealed, so materials and their effects pass between an "
               "artificial ecosystem and the natural one beside it.",
    },
    {
        "id": "ks4-ecosystems-h20",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the more species an ecosystem "
                "contains, the more stable it is.",
        "options": [
            "It holds in every case, as species number is how stability is set",
            "It broadly holds, because more species means more shared roles",
            "It is false, as a species-rich ecosystem has more to go wrong",
            "It is false, as stability depends on the number of individuals",
        ],
        "correct_index": 1,
        "why": "More species usually means more species able to fill each "
               "role, so the loss of any one is absorbed rather than breaking "
               "the web — though relative abundance matters too.",
    },
    {
        "id": "ks4-ecosystems-h21",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Wood A is coppiced on a fifteen-year cycle. Wood B has been "
                "left untouched for two hundred years. Compare the "
                "communities the two are likely to hold.",
        "options": [
            "Both hold the same community, as their tree species are the same",
            "Wood B holds more light-loving flowers, as its canopy is old",
            "Wood A holds more light-demanding plants; B more deadwood species",
            "Wood A holds no real community, as it is managed rather than wild",
        ],
        "correct_index": 2,
        "why": "Coppicing repeatedly opens the canopy, which favours "
               "light-demanding ground flora, while an unmanaged wood builds "
               "up standing and fallen deadwood and the specialists that need "
               "it.",
    },
    {
        "id": "ks4-ecosystems-h22",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an ecologist must decide where a rocky shore "
                "ecosystem begins and ends before starting to sample it.",
        "options": [
            "An ecosystem cannot be studied unless its edge is marked",
            "A shore has one fixed natural boundary that must be found",
            "Sampling gear is calibrated for a boundary of a set size",
            "Abundance estimates are scaled to the area, so the area must be "
            "fixed",
        ],
        "correct_index": 3,
        "why": "A population estimate is a mean count scaled up by the total "
               "area, so the total area has to be defined before any number "
               "can be produced.",
    },
    {
        "id": "ks4-ecosystems-h23",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to a woodland community if all of "
                "its decomposers were removed, and explain why.",
        "options": [
            "Dead material would pile up and its minerals stay locked away",
            "Nothing would change, as decomposers sit outside the community",
            "The trees would grow faster, as nothing would take the minerals",
            "The wood would become cleaner, as decomposers cause the decay",
        ],
        "correct_index": 0,
        "why": "Decomposers release the minerals held in dead organisms back "
               "into the soil, so without them the nutrients the plants need "
               "are never returned.",
    },
    {
        "id": "ks4-ecosystems-h24",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because removing one species can cause "
                "a cascade, every species in an ecosystem must be essential. "
                "Evaluate this argument.",
        "options": [
            "It is sound, as a cascade follows the removal of any species",
            "It overstates it: some species have a far larger effect than others",
            "It is sound, as interdependence makes each depend on the rest",
            "It is unsound, as no single species has a measurable effect",
        ],
        "correct_index": 1,
        "why": "Keystone species have effects out of all proportion to their "
               "numbers, while the loss of others is absorbed, so 'essential' "
               "is not equally true of every species.",
    },
    {
        "id": "ks4-ecosystems-h25",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pond holds 600 water fleas, 40 sticklebacks and one grey "
                "heron that visits it daily. Determine whether the heron can "
                "be called a population.",
        "options": [
            "No, because a population must contain two breeding individuals",
            "No, because a visitor belongs to the community but not the pond",
            "Yes, a population can be a single individual in that area",
            "Yes, for as long as it is standing inside the pond's boundary",
        ],
        "correct_index": 2,
        "why": "A population is all of the individuals of one species in the "
               "area, so where there is one individual the population size is "
               "simply one.",
    },
    {
        "id": "ks4-ecosystems-h26",
        "subtopic_slug": "ecosystems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hedge between two fields is removed and replaced with a "
                "wire fence. The crops in both fields are unchanged. Suggest "
                "how the habitats available have changed.",
        "options": [
            "Nothing has changed, as the crop provides the habitat",
            "More habitat is available, as the fields are now larger",
            "The habitat is the same in extent but now shared by two fields",
            "A nesting and sheltering habitat for many species has been lost",
        ],
        "correct_index": 3,
        "why": "A hedge is itself a habitat — a strip of woody cover that many "
               "birds, insects and small mammals nest and feed in — and a wire "
               "fence provides none of that.",
    },
]
