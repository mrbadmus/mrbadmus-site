"""Biology · Ecology — the MRB-338 expansion, subtopic `food-chains-webs`.

Spec 4.7.1. Two strands carry the weight. The first is the lesson's own common
mistake — that an arrow shows what an animal eats rather than which way the
energy travels — so several rows come at the arrow from the wrong side. The
second is the arithmetic of the roughly 10% transfer, worked on clean numbers
in named chains (oak leaves to caterpillar to blue tit, phytoplankton to
zooplankton to herring to seal, grass to vole to stoat) with the working kept
in the `why` and never in an option. Web reasoning is examined through real
consequences — a lost prey species, a removed predator, an omnivore that will
not sit on one level."""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ────────────────────────────────────────────────────────────
    {
        "id": "ks4-food-chains-webs-e05",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Oak leaves are eaten by caterpillars, caterpillars by blue "
                "tits and blue tits by sparrowhawks. Name the primary consumer.",
        "options": [
            "The caterpillar",
            "The oak leaves",
            "The blue tit",
            "The sparrowhawk",
        ],
        "correct_index": 0,
        "why": "The primary consumer is whatever eats the producer, and the "
               "caterpillar is the organism feeding directly on the oak leaves.",
    },
    {
        "id": "ks4-food-chains-webs-e06",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Grass is eaten by rabbits and rabbits are eaten by foxes. "
                "State what the fox is in this chain.",
        "options": [
            "The producer",
            "The decomposer",
            "The secondary consumer",
            "The primary consumer",
        ],
        "correct_index": 2,
        "why": "The fox eats the primary consumer, which makes it the "
               "secondary consumer — the third trophic level of the chain.",
    },
    {
        "id": "ks4-food-chains-webs-e07",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the kind of organism at which every food chain begins.",
        "options": [
            "A predator",
            "A producer",
            "A decomposer",
            "A herbivore",
        ],
        "correct_index": 1,
        "why": "A producer photosynthesises, which is how the energy gets "
               "into the chain in the first place, so every chain must start with "
               "one.",
    },
    {
        "id": "ks4-food-chains-webs-e08",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the term for each separate feeding level in a food "
                "chain.",
        "options": [
            "A carbon store",
            "A niche",
            "A trophic level",
            "A quadrat",
        ],
        "correct_index": 2,
        "why": "Each step of a chain — producer, primary consumer, secondary "
               "consumer and so on — is called a trophic level.",
    },
    {
        "id": "ks4-food-chains-webs-e09",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the form in which energy first enters a food chain.",
        "options": [
            "Heat from the soil",
            "Light from the Sun",
            "Minerals taken up by roots",
            "Oxygen from the air",
        ],
        "correct_index": 1,
        "why": "Producers absorb light energy and store it as chemical energy "
               "in glucose, and that is the only way energy enters the chain.",
    },
    {
        "id": "ks4-food-chains-webs-e10",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which organisms break down the dead material produced at "
                "every level of a food chain?",
        "options": [
            "Herbivores and omnivores",
            "Insects and worms",
            "Algae and mosses",
            "Bacteria and fungi",
        ],
        "correct_index": 3,
        "why": "Bacteria and fungi are the decomposers, and they feed on dead "
               "material from producers and consumers alike.",
    },
    {
        "id": "ks4-food-chains-webs-e11",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which trophic level of a food chain holds the most "
                "biomass.",
        "options": [
            "The producers",
            "The primary consumers",
            "The secondary consumers",
            "The tertiary consumers",
        ],
        "correct_index": 0,
        "why": "Energy and biomass are lost at every transfer, so the level "
               "that has lost the least — the producers — holds the most.",
    },
    {
        "id": "ks4-food-chains-webs-e12",
        "subtopic_slug": "food-chains-webs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Phytoplankton are eaten by zooplankton, zooplankton by "
                "herring and herring by seals. Name the tertiary consumer.",
        "options": [
            "The phytoplankton",
            "The zooplankton",
            "The herring",
            "The seal",
        ],
        "correct_index": 3,
        "why": "The seal eats the secondary consumer, which makes it the "
               "tertiary consumer at the fourth trophic level.",
    },
    # ── standard ──────────────────────────────────────────────────────────
    {
        "id": "ks4-food-chains-webs-s05",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Oak leaves store 25 000 kJ of energy. Caterpillars eat the "
                "leaves and blue tits eat the caterpillars. Taking 10% as the "
                "transfer at each step, calculate the energy in the blue tits.",
        "options": [
            "250 kJ",
            "2500 kJ",
            "25 kJ",
            "20 250 kJ per year",
        ],
        "correct_index": 0,
        "why": "Two transfers of 10%: 25 000 x 0.1 = 2500 kJ in the "
               "caterpillars, and 2500 x 0.1 = 250 kJ in the blue tits.",
    },
    {
        "id": "ks4-food-chains-webs-s06",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a garden web, blackbirds eat both ladybirds and "
                "caterpillars, and the ladybirds eat aphids. A spray kills every "
                "aphid. Predict the effect on the blackbirds.",
        "options": [
            "They increase: more caterpillars are left",
            "They fall somewhat, because one of their two food sources "
            "declines",
            "They are unchanged: blackbirds eat no aphids",
            "They fall to nothing: their food has gone",
        ],
        "correct_index": 1,
        "why": "Losing the aphids reduces the ladybirds, so one branch of the "
               "blackbird's diet shrinks while the caterpillar branch is left, and "
               "numbers fall without collapsing.",
    },
    {
        "id": "ks4-food-chains-webs-s07",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the arrow in a food chain is drawn from the "
                "rabbit to the fox rather than from the fox to the rabbit.",
        "options": [
            "The fox is the larger animal, so it is placed at the head of the "
            "arrow",
            "The arrow shows the direction the fox travels to find the rabbit",
            "Energy passes from the rabbit into the fox when the fox feeds",
            "The arrow points towards whichever organism is eaten",
        ],
        "correct_index": 2,
        "why": "An arrow in a food chain shows the direction of energy "
               "transfer, and the energy moves out of the organism that is eaten "
               "into the one that eats it.",
    },
    {
        "id": "ks4-food-chains-webs-s08",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a field supports far fewer foxes than rabbits.",
        "options": [
            "Foxes are bigger, so they breed far more slowly",
            "Foxes need much more space each, and space is what limits their "
            "numbers",
            "Rabbits breed quickly, and quick breeding gives more adults in "
            "the end",
            "Only about a tenth of the rabbits' energy reaches the foxes",
        ],
        "correct_index": 3,
        "why": "Most of the energy at one trophic level is lost as heat, "
               "faeces and uneaten material, so the level above it can support far "
               "fewer individuals.",
    },
    {
        "id": "ks4-food-chains-webs-s09",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fox kills and eats a rabbit but leaves some of it. Name "
                "the parts most likely to be left behind.",
        "options": [
            "The bones and the fur",
            "The muscle and the liver",
            "The blood and the fat",
            "The heart and the two kidneys",
        ],
        "correct_index": 0,
        "why": "Hard, indigestible parts such as bone and fur are usually not "
               "eaten, and the energy they hold never reaches the next trophic "
               "level.",
    },
    {
        "id": "ks4-food-chains-webs-s10",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the faeces an animal produces count as a loss of "
                "biomass from the food chain.",
        "options": [
            "The material was eaten but not absorbed, so it is not passed on",
            "Faeces hold no energy once they have left the body",
            "The material is destroyed by the gut, so its energy disappears",
            "Faeces are washed into the soil, where nothing can ever use them",
        ],
        "correct_index": 0,
        "why": "Material that is eaten but not digested leaves the body "
               "again, so the energy and biomass it holds never becomes part of the "
               "consumer.",
    },
    {
        "id": "ks4-food-chains-webs-s11",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chain has six trophic levels. Predict which level will "
                "support the fewest organisms and explain why.",
        "options": [
            "The first, because the producers are the smallest organisms "
            "present",
            "The sixth, because the least energy is left by that level",
            "The third, because the middle of a chain is its narrowest point",
            "The first, because the producers are eaten by every other level",
        ],
        "correct_index": 1,
        "why": "Around 90% of the energy is lost at each of the five "
               "transfers, so the amount reaching the top level is tiny and can "
               "support very few individuals.",
    },
    {
        "id": "ks4-food-chains-webs-s12",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A seal is a secondary consumer in one chain and a tertiary "
                "consumer in another. Explain how both can be true.",
        "options": [
            "A seal changes its trophic level as it grows from a pup to an "
            "adult",
            "Its trophic level depends on which chain is being followed",
            "Seals are omnivores, and an omnivore has no trophic level",
            "One of the two chains must have been drawn the wrong way round",
        ],
        "correct_index": 1,
        "why": "A trophic level counts the steps from the producer, so an "
               "animal that feeds on more than one kind of prey sits at different "
               "levels in different chains.",
    },
    {
        "id": "ks4-food-chains-webs-s13",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pond web has one producer, the algae. Predict what happens "
                "to the whole web if a herbicide kills all of the algae.",
        "options": [
            "The animals that eat the algae are the ones affected",
            "The web continues, because the animals go on feeding on one "
            "another instead",
            "The top predator is unaffected, as it eats no algae",
            "The whole web collapses, because no energy now enters it",
        ],
        "correct_index": 3,
        "why": "The producer is the only route by which energy enters the "
               "web, so removing it removes the supply that every consumer "
               "ultimately depends on.",
    },
    {
        "id": "ks4-food-chains-webs-s14",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a web, wolves eat elk and elk eat willow shoots. The "
                "wolves are removed. Predict the effect on the willow.",
        "options": [
            "The willow increases, as the wolves had been trampling the young "
            "shoots",
            "The willow is unchanged, as wolves and willow do not interact",
            "The willow decreases, because more elk survive to browse it",
            "The willow decreases, because the wolves had fertilised the soil",
        ],
        "correct_index": 2,
        "why": "Removing the predator releases its prey, and the released "
               "herbivore eats more of the producer — the change travels two steps "
               "down the chain.",
    },
    {
        "id": "ks4-food-chains-webs-s15",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Grass on a bank stores 9000 kJ. Voles eat the grass and a "
                "stoat eats the voles. Taking 10% as the transfer at each step, "
                "calculate the energy reaching the stoat.",
        "options": [
            "900 kJ",
            "9 kJ",
            "8100 kJ in total",
            "90 kJ",
        ],
        "correct_index": 3,
        "why": "Two transfers of 10%: 9000 x 0.1 = 900 kJ in the voles, and "
               "900 x 0.1 = 90 kJ in the stoat.",
    },
    {
        "id": "ks4-food-chains-webs-s16",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why decomposers are not usually drawn as the top "
                "level of a food chain.",
        "options": [
            "They feed on the dead material from every level, not just the top",
            "They are too small to count as part of a food chain",
            "They are producers, so they sit at the bottom",
            "They release energy as heat and pass none on",
        ],
        "correct_index": 0,
        "why": "Decomposers take dead material from producers and consumers "
               "alike, so they sit alongside the whole chain rather than on top of "
               "it.",
    },
    {
        "id": "ks4-food-chains-webs-s17",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a food web helps an ecologist work out which "
                "species is most at risk if one species is lost.",
        "options": [
            "It records how many individuals each species has",
            "It shows which species are largest, and size decides the risk",
            "It lists the species in the order in which they were first "
            "discovered",
            "It shows how many alternative food sources each species has",
        ],
        "correct_index": 3,
        "why": "A species with several arrows into it has alternatives if one "
               "prey is lost, while a species with only one is left with nothing.",
    },
    {
        "id": "ks4-food-chains-webs-s18",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Phytoplankton begin a marine food chain. Explain what they "
                "do that no other organism in the chain does.",
        "options": [
            "They make their own food from light, so they bring energy in",
            "They are the organisms in the chain with the least need for "
            "oxygen",
            "They are the only organisms in the chain that can move about",
            "They break down the dead remains of every other organism in the "
            "sea",
        ],
        "correct_index": 0,
        "why": "Phytoplankton are the producers, so they are the only step at "
               "which light energy is captured and made available to the rest of the "
               "chain.",
    },
    {
        "id": "ks4-food-chains-webs-s19",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A caterpillar eats 60 g of leaf material and gains 6 g of "
                "body mass. Calculate the percentage of the biomass transferred.",
        "options": [
            "6%",
            "10%",
            "60%",
            "90%",
        ],
        "correct_index": 1,
        "why": "Percentage transferred = (6 / 60) x 100 = 10%, which is the "
               "usual figure for a transfer between trophic levels.",
    },
    {
        "id": "ks4-food-chains-webs-s20",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a deer that walks several kilometres a day "
                "passes less energy on to a wolf than one that stays still.",
        "options": [
            "Walking makes the deer tougher, so less of it can be digested",
            "Walking uses energy in respiration, which is then lost as heat",
            "A deer that walks eats less, so it takes in less energy overall",
            "Energy is used up by the ground the deer walks across each day",
        ],
        "correct_index": 1,
        "why": "Energy released in respiration to power movement escapes to "
               "the surroundings as heat, so it is no longer stored in the deer's "
               "body to be eaten.",
    },
    {
        "id": "ks4-food-chains-webs-s21",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thrush eats snails, worms and berries. Explain the "
                "advantage this gives the thrush over a bird that eats snails alone.",
        "options": [
            "It digests three foods more efficiently than one",
            "It needs less energy in total because its diet is so varied",
            "It can switch food if one of the three becomes scarce",
            "It can be placed at three separate trophic levels at the very "
            "same moment",
        ],
        "correct_index": 2,
        "why": "Having several arrows into it in the web means a shortage of "
               "any one food does not leave the thrush without anything to eat.",
    },
    {
        "id": "ks4-food-chains-webs-s22",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cave community feeds on plant material washed in from "
                "outside. Explain why the cave itself has no producers.",
        "options": [
            "Caves are too cold for a producer to survive in for very long",
            "Producers are washed away by the same water that brings the food",
            "There is no light in the cave for photosynthesis to take place",
            "The consumers in the cave eat the producers faster than they can "
            "grow",
        ],
        "correct_index": 2,
        "why": "A producer needs light to photosynthesise, so in permanent "
               "darkness the community's energy has to arrive from a lit habitat "
               "elsewhere.",
    },
    {
        "id": "ks4-food-chains-webs-s23",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Algae are eaten by insect larvae, the larvae by minnows and "
                "the minnows by a heron. State the heron's trophic level.",
        "options": [
            "The fourth",
            "The second",
            "The third",
            "The fifth",
        ],
        "correct_index": 0,
        "why": "Counting from the producer: algae are level 1, larvae level "
               "2, minnows level 3 and the heron level 4.",
    },
    {
        "id": "ks4-food-chains-webs-s24",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the number of organisms usually falls at each "
                "step up a food chain.",
        "options": [
            "Organisms higher up the chain live considerably longer lives",
            "Predators kill each other, so their own numbers are kept down",
            "Organisms at the top of a chain reproduce more slowly than the "
            "rest do",
            "Less energy is available, so fewer individuals can be supported",
        ],
        "correct_index": 3,
        "why": "Each transfer passes on only about a tenth of the energy, so "
               "there is progressively less to share among the organisms at each "
               "higher level.",
    },
    {
        "id": "ks4-food-chains-webs-s25",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A field holds about 2 000 000 grass plants, 5000 rabbits and "
                "3 foxes. State what this pattern of numbers shows.",
        "options": [
            "Rabbits are the field's most important species",
            "Foxes must be feeding on the grass of the field as well as the "
            "rabbits",
            "Energy is lost at each step, so each level supports fewer",
            "The field is too small for more than three foxes",
        ],
        "correct_index": 2,
        "why": "The steep fall in numbers at each level follows from the "
               "roughly 90% of energy lost at every transfer.",
    },
    {
        "id": "ks4-food-chains-webs-s26",
        "subtopic_slug": "food-chains-webs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how removing one species from a food web can change "
                "the numbers of a species that never eats it.",
        "options": [
            "Every species in a web feeds on every other species in it",
            "The change passes along the web through their shared species",
            "Removing a species raises the oxygen available to all the rest",
            "Species that do not meet are still competing for territory",
        ],
        "correct_index": 1,
        "why": "The species are linked indirectly: a change in one alters the "
               "species it is joined to, and that alteration passes on along the "
               "web.",
    },
    # ── harder ────────────────────────────────────────────────────────────
    {
        "id": "ks4-food-chains-webs-h05",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Producers in a meadow store 12 000 kJ per square metre each "
                "year. Taking 10% as the transfer at each step, calculate the energy "
                "reaching trophic level 4.",
        "options": [
            "1200 kJ per square metre",
            "12 kJ",
            "120 kJ",
            "1.2 kJ",
        ],
        "correct_index": 1,
        "why": "Level 4 is three transfers above the producers: 12 000 x 0.1 "
               "= 1200, x 0.1 = 120, x 0.1 = 12 kJ per square metre per year.",
    },
    {
        "id": "ks4-food-chains-webs-h06",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a garden web ladybirds eat aphids and blue tits eat "
                "ladybirds. A disease kills most of the ladybirds. Predict the effect "
                "on the aphids and on the blue tits.",
        "options": [
            "Aphids rise and blue tits fall, as one loses a predator",
            "Both rise, because the ladybirds competed with each of them",
            "Both fall, because the ladybirds were central to the whole web",
            "Aphids fall and blue tits rise, since the blue tits eat the "
            "aphids too",
        ],
        "correct_index": 0,
        "why": "The species below the ladybird loses its predator and "
               "increases, while the species above it loses its prey and declines — "
               "the two effects run in opposite directions.",
    },
    {
        "id": "ks4-food-chains-webs-h07",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A desert's producers fix very little energy each year. "
                "Suggest why its food chains are shorter than a rainforest's.",
        "options": [
            "Less energy enters, so it runs out after fewer transfers",
            "Desert animals are larger, so each chain needs fewer of them",
            "Desert producers are eaten whole, so no energy is lost",
            "The heat of a desert destroys the energy as it passes up through "
            "the chain",
        ],
        "correct_index": 0,
        "why": "The length of a chain is limited by how much energy is left, "
               "so starting with less means the supply becomes too small to support "
               "another level sooner.",
    },
    {
        "id": "ks4-food-chains-webs-h08",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement that an arrow in a food web shows "
                "what an animal eats.",
        "options": [
            "It is sound: the arrow points from food to animal",
            "It is wrong: an arrow shows how species are related",
            "It is partly right: the arrow shows energy moving from food to "
            "feeder",
            "It is wrong: web arrows point both ways",
        ],
        "correct_index": 2,
        "why": "The arrow does connect food to feeder, but what it represents "
               "is the transfer of energy, which is why it never points back the "
               "other way.",
    },
    {
        "id": "ks4-food-chains-webs-h09",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a single food chain and a food web as models of the "
                "same woodland community.",
        "options": [
            "The chain is more accurate; the web adds species that are not "
            "there",
            "Both show the same information, but the web uses more paper",
            "The chain is simpler to read; the web shows the real alternatives",
            "The chain shows energy flow; the web shows just who eats whom",
        ],
        "correct_index": 2,
        "why": "A chain is a clear but partial picture, while a web shows "
               "that most organisms eat and are eaten by several species, which is "
               "what really happens.",
    },
    {
        "id": "ks4-food-chains-webs-h10",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Starfish are removed from a rocky shore and mussels spread "
                "until they cover almost all of it, crowding out other species. "
                "Explain what this shows about the starfish.",
        "options": [
            "It had an effect on the shore far larger than its numbers suggest",
            "It was the one predator the mussels on that shore had",
            "It was the shore's producer, so the web ended",
            "It had eaten the species the mussels crowded out",
        ],
        "correct_index": 0,
        "why": "A keystone species holds a community's structure in place: "
               "removing the starfish let one competitor dominate, and the variety "
               "of the whole shore fell with it.",
    },
    {
        "id": "ks4-food-chains-webs-h11",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An island's only herbivore is removed. Predict the effect on "
                "the island's plants and on its one carnivore.",
        "options": [
            "Both the plants and the carnivore increase, as competition falls",
            "The plants decline, as the herbivore had been spreading their "
            "seed",
            "Neither changes, since one single species cannot alter a whole "
            "island at once",
            "The plants increase and the carnivore declines for want of prey",
        ],
        "correct_index": 3,
        "why": "The producer loses its grazer and spreads, while the "
               "carnivore loses the only prey it had and its numbers fall.",
    },
    {
        "id": "ks4-food-chains-webs-h12",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a hectare of land feeds more people if it is "
                "sown with wheat than if it is grazed by cattle.",
        "options": [
            "Wheat grows faster than grass does in almost every climate",
            "Cattle need more water, and water limits the food a farm produces",
            "Wheat contains more energy per kilogram than beef does",
            "Wheat is eaten at level 2, so one fewer transfer loses energy",
        ],
        "correct_index": 3,
        "why": "Eating the producer directly avoids a transfer at which about "
               "90% of the energy would have been lost, so far more of the crop's "
               "energy reaches people.",
    },
    {
        "id": "ks4-food-chains-webs-h13",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student draws the chain grass to rabbit and then an arrow "
                "back from the rabbit to the grass. Identify the error.",
        "options": [
            "Energy travels one way only, so the second arrow is wrong",
            "There is no error, because the rabbit's droppings feed the grass",
            "The first arrow is the wrong one, and the second is correct",
            "A chain must have at least three levels, so one is missing",
        ],
        "correct_index": 0,
        "why": "Energy is transferred from the eaten to the eater and is then "
               "lost as heat, so it never returns to a lower level of the chain.",
    },
    {
        "id": "ks4-food-chains-webs-h14",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Producers in a lake store 8000 kJ and the primary consumers "
                "store 640 kJ. Calculate the percentage of energy transferred between "
                "the two levels.",
        "options": [
            "8%",
            "6.4%",
            "10%",
            "12.5% of it",
        ],
        "correct_index": 0,
        "why": "Percentage transferred = (640 / 8000) x 100 = 8%, a little "
               "below the usual 10% figure.",
    },
    {
        "id": "ks4-food-chains-webs-h15",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the 10% figure for energy transfer between "
                "trophic levels is described as an approximation.",
        "options": [
            "The figure was measured once and has not been checked since",
            "The real figure varies with the species and the conditions",
            "Ecologists have no way of measuring energy in an organism",
            "The figure is exact for plants but not for any animal group",
        ],
        "correct_index": 1,
        "why": "How much is lost as heat, in faeces and in uneaten parts "
               "differs between species and habitats, so 10% is a typical value "
               "rather than a fixed one.",
    },
    {
        "id": "ks4-food-chains-webs-h16",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two chains begin with producers storing 50 000 kJ. One has "
                "three trophic levels and the other has five. Taking 10% per step, "
                "compare the energy at the top of each.",
        "options": [
            "500 kJ and 50 kJ, so the longer chain's top level has ten times "
            "less",
            "500 kJ and 5 kJ, so the longer chain's top level has far less",
            "5000 kJ and 500 kJ, so the difference is a single transfer",
            "Both hold 500 kJ, because they start from the same producer "
            "energy",
        ],
        "correct_index": 1,
        "why": "Three levels means two transfers: 50 000 x 0.1 x 0.1 = 500 "
               "kJ. Five levels means four: 50 000 x 0.1 four times over = 5 kJ.",
    },
    {
        "id": "ks4-food-chains-webs-h17",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a food web drawn for a real oak wood contains "
                "hundreds of arrows.",
        "options": [
            "An arrow has to be drawn between every pair of species present",
            "Arrows are drawn in both directions between each pair of species",
            "Every species in a wood feeds at three trophic levels at once",
            "Most species there eat, and are eaten by, several other species",
        ],
        "correct_index": 3,
        "why": "Real feeding relationships branch in many directions, so each "
               "species needs an arrow for every organism it eats and every organism "
               "that eats it.",
    },
    {
        "id": "ks4-food-chains-webs-h18",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the loss of a top predator from a woodland web "
                "can reduce the number of plant species growing there.",
        "options": [
            "The predator's droppings had been the main source of soil "
            "minerals",
            "Released herbivores graze harder, and sensitive plants are lost",
            "Plants need a predator present in order to set seed successfully",
            "The predator had been eating the herbivores' competitors as well",
        ],
        "correct_index": 1,
        "why": "Without the predator the herbivore population rises, and "
               "heavy grazing removes the plant species least able to recover from "
               "being eaten.",
    },
    {
        "id": "ks4-food-chains-webs-h19",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a food chain on the deep ocean floor can begin "
                "with dead material sinking from above.",
        "options": [
            "Deep-sea animals are unable to digest any living material",
            "Dead material holds more energy than a living producer does",
            "There is no light down there, so no producer can grow",
            "The pressure on the sea floor stops photosynthesis working",
        ],
        "correct_index": 2,
        "why": "A community with no light has no producers of its own, so the "
               "energy it uses must be fixed elsewhere and arrive as dead organic "
               "matter.",
    },
    {
        "id": "ks4-food-chains-webs-h20",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the total biomass at trophic level 1 with that at "
                "level 3 of the same chain, and explain the difference.",
        "options": [
            "Level 3 holds far more, as its organisms are larger individually",
            "Both hold the same, as biomass cannot be lost",
            "Level 1 holds far more, as biomass is lost at every transfer",
            "Level 3 holds more, as it draws on two levels below",
        ],
        "correct_index": 2,
        "why": "Only about a tenth of the biomass passes on at each step, so "
               "two transfers leave level 3 with roughly a hundredth of the biomass "
               "of level 1.",
    },
    {
        "id": "ks4-food-chains-webs-h21",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a food web shows that every species "
                "in a community depends on every other species.",
        "options": [
            "It is correct, because a web joins each species to all the others",
            "It is wrong, because a web shows no dependence between species",
            "It overstates it: links are common, but not every pair is joined",
            "It is correct, because every species shares the same habitat",
        ],
        "correct_index": 2,
        "why": "A web shows many indirect connections, but a species can "
               "genuinely have no link, direct or indirect, to another part of the "
               "community.",
    },
    {
        "id": "ks4-food-chains-webs-h22",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a badger, which eats earthworms, beetles, young "
                "rabbits and fruit, is hard to place at one trophic level.",
        "options": [
            "It has no trophic level, because it is neither predator nor prey",
            "Its trophic level changes with the season rather than the food",
            "It belongs at level 1, because part of its diet is plant material",
            "It feeds at several levels, so its level depends on the meal",
        ],
        "correct_index": 3,
        "why": "Trophic level counts the steps from the producer, and an "
               "omnivore eats at more than one distance from the producer, so no "
               "single number describes it.",
    },
    {
        "id": "ks4-food-chains-webs-h23",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon atoms are used over and over in an ecosystem, but "
                "energy has to be supplied continuously. Explain why.",
        "options": [
            "Energy is destroyed each time one organism eats another one",
            "Carbon atoms are made by producers and energy atoms are not",
            "Energy is stored in the soil, where no organism can reach it",
            "Energy leaves the chain as heat, which organisms cannot reuse",
        ],
        "correct_index": 3,
        "why": "The atoms stay within the ecosystem and are recycled, but the "
               "energy released in respiration passes to the surroundings as heat "
               "and is not available again.",
    },
    {
        "id": "ks4-food-chains-webs-h24",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a web, heather feeds grouse and mountain hares; foxes eat "
                "both; eagles eat only hares. Determine which species' loss would "
                "disrupt the web most, and justify it.",
        "options": [
            "The grouse, because it is eaten by more species than the hare",
            "The heather, because it is the only producer in the whole web",
            "The eagle, because it sits at the top of the whole web",
            "The fox, because it is the only species with two food sources",
        ],
        "correct_index": 1,
        "why": "Every other species in the web ultimately draws its energy "
               "from the heather, so losing the single producer removes the supply "
               "that all of them depend on.",
    },
    {
        "id": "ks4-food-chains-webs-h25",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-food-chain-reversed-arrows",
        "text": "A student draws this food chain. Explain why the species are in the right order but the science is wrong.",
        "options": [
            "The feeding links are correct, but the energy flow is reversed",
            "The species are in the wrong order as well as the arrows",
            "The arrows are correct, because a predator seeks out its prey",
            "Nothing is wrong, since an arrow may be drawn either way round",
        ],
        "correct_index": 0,
        "why": "The chain shows the right feeding relationships, but an arrow stands for energy transfer, and energy moves from the organism eaten to the one eating it. Every arrow here points the wrong way.",
    },
    {
        "id": "ks4-food-chains-webs-h26",
        "subtopic_slug": "food-chains-webs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A large predatory fish is introduced to a lake where small "
                "fish eat water fleas and water fleas eat algae. Suggest the effect "
                "on the algae.",
        "options": [
            "The algae increase, because fewer small fish leave more fleas",
            "The algae decrease, because fewer small fish leave more fleas",
            "The algae are unchanged, as the new fish does not eat algae",
            "The algae decrease, because the new fish grazes on them too",
        ],
        "correct_index": 1,
        "why": "The new predator reduces the small fish, so more water fleas "
               "survive, and the larger population of grazers eats more of the "
               "algae.",
    },
]
