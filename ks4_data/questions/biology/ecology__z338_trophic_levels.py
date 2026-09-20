"""Biology · Ecology — the MRB-338 expansion, trophic levels (4.7.4.1).

Triple-only content. The weight here follows the spec point's two halves: the
numbered levels themselves (producer, primary, secondary and tertiary consumer,
the place of decomposers, the meaning of a food-chain arrow) and the one-way
flow of energy through them, including the approximate tenth that survives
each transfer. The harder band works that flow arithmetically in both
directions and in unfamiliar contexts — a parasitic wasp, a hoverfly whose
larva and adult feed at different levels, an island that cannot support a
fourth level at all.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-trophic-levels-e05",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a trophic level.",
        "options": [
            "The total number of organisms found at one stage of a food chain",
            "The position an organism occupies in a food chain",
            "The area of habitat in which one species feeds and breeds",
            "The mass of food an organism eats in a single day",
        ],
        "correct_index": 1,
        "why": "A trophic level is a feeding position — how many steps an "
               "organism sits from the producers that captured the light.",
    },
    {
        "id": "ks4-trophic-levels-e06",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the name given to a consumer at trophic level 4.",
        "options": [
            "A primary consumer",
            "A secondary consumer",
            "A tertiary consumer",
            "A producer",
        ],
        "correct_index": 2,
        "why": "Level 2 is the primary consumer and level 3 the secondary, so "
               "the carnivore at level 4 is the tertiary consumer.",
    },
    {
        "id": "ks4-trophic-levels-e07",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the food chain seaweed → limpet → crab → "
                "herring gull, identify the producer.",
        "options": [
            "The limpet",
            "The crab",
            "The seaweed",
            "The herring gull",
        ],
        "correct_index": 2,
        "why": "Seaweed is an alga and photosynthesises, so it is the producer "
               "and occupies trophic level 1.",
    },
    {
        "id": "ks4-trophic-levels-e08",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of consumer that eats only plants.",
        "options": [
            "A herbivore, or primary consumer",
            "A carnivore, or secondary consumer",
            "A producer, or photosynthesiser",
            "A decomposer",
        ],
        "correct_index": 0,
        "why": "An animal whose food is producers is a herbivore, and a "
               "herbivore is the primary consumer of its food chain.",
    },
    {
        "id": "ks4-trophic-levels-e09",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the process by which energy enters an ecosystem at "
                "trophic level 1.",
        "options": [
            "Respiration",
            "Decomposition",
            "Digestion",
            "Photosynthesis",
        ],
        "correct_index": 3,
        "why": "Producers transfer light energy into chemical stores in "
               "glucose, and that is the only route energy takes into a "
               "food chain.",
    },
    {
        "id": "ks4-trophic-levels-e10",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how many times biomass has been transferred by the time "
                "it reaches trophic level 3.",
        "options": [
            "Once",
            "Twice",
            "Three times",
            "Four times",
        ],
        "correct_index": 1,
        "why": "Level 1 to level 2 is one transfer and level 2 to level 3 is "
               "the second, so biomass reaching level 3 has moved twice.",
    },
    {
        "id": "ks4-trophic-levels-e11",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A rabbit feeds only on grass. State the rabbit's trophic level.",
        "options": [
            "Level 1",
            "Level 3",
            "Level 2",
            "Level 4",
        ],
        "correct_index": 2,
        "why": "A herbivore eats producers, so it is the first consumer in the "
               "chain and sits at level 2.",
    },
    {
        "id": "ks4-trophic-levels-e12",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ground beetle eats grain aphids, which feed on barley. A shrew "
                "eats the beetles. Name the secondary consumer.",
        "options": [
            "The ground beetle",
            "The barley",
            "The grain aphids",
            "The shrew",
        ],
        "correct_index": 0,
        "why": "The aphids are the primary consumers of the barley, so the "
               "beetle that eats them is the secondary consumer at level 3.",
    },
    {
        "id": "ks4-trophic-levels-e13",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a food chain rarely has more than five trophic "
                "levels.",
        "options": [
            "Too little biomass is left at the top to support another level of consumers",
            "Few habitats contain more than five different animal or plant species",
            "Arrows cannot be drawn clearly in a chain of more than five",
            "Producers photosynthesise for only five months of each year",
        ],
        "correct_index": 0,
        "why": "About nine tenths of the biomass is lost at every transfer, so "
               "after four or five steps there is too little left to feed "
               "another level.",
    },
    {
        "id": "ks4-trophic-levels-e14",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how a consumer differs from a producer.",
        "options": [
            "A consumer lives on the land, whereas a producer lives in water or in damp soil",
            "A consumer has to respire, whereas a producer photosynthesises instead",
            "A consumer is larger than the producer it takes its food from",
            "A consumer eats other organisms; a producer makes its own food",
        ],
        "correct_index": 3,
        "why": "A producer builds its own glucose by photosynthesis, while a "
               "consumer has to take ready-made biomass from another organism.",
    },
    {
        "id": "ks4-trophic-levels-e15",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the type of organism found at trophic level 3 in "
                "most food chains.",
        "options": [
            "A herbivore that eats producers",
            "A plant that photosynthesises",
            "A fungus that decays dead matter",
            "A carnivore that eats herbivores",
        ],
        "correct_index": 3,
        "why": "Level 3 is the secondary consumer, a carnivore whose food is "
               "the herbivores at level 2.",
    },
    {
        "id": "ks4-trophic-levels-e16",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the original source of all the energy held at every "
                "trophic level.",
        "options": [
            "Mineral ions in the soil",
            "The Sun",
            "Heat from the Earth's core",
            "The decomposers",
        ],
        "correct_index": 1,
        "why": "Producers capture light from the Sun, and every consumer above "
               "them holds a share of that same captured energy.",
    },
    {
        "id": "ks4-trophic-levels-e17",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what an omnivore's diet means for its trophic level.",
        "options": [
            "It has no trophic level in any food chain",
            "It is placed at trophic level 1 alongside the producers of its chain",
            "It is placed at the top trophic level of its chain",
            "It feeds at more than one trophic level",
        ],
        "correct_index": 3,
        "why": "An omnivore eats both plants and animals, so it takes biomass "
               "from level 1 and from level 2 and occupies more than one "
               "level.",
    },
    {
        "id": "ks4-trophic-levels-e18",
        "subtopic_slug": "trophic-levels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason why decomposers matter in an ecosystem.",
        "options": [
            "They raise the amount of energy stored at the top of the food chain each year",
            "They return mineral ions from dead material to the soil",
            "They pass energy from the consumers back to the producers",
            "They increase the number of levels a food chain can support",
        ],
        "correct_index": 1,
        "why": "Without decomposers the mineral ions in dead bodies and wastes "
               "would stay locked up, so producers could not take them up "
               "again.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-trophic-levels-s05",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An ecologist lists a pond chain's members alphabetically: "
                "algae, diving beetle, heron, pond snail. Determine the trophic "
                "level of each.",
        "options": [
            "Algae 1, pond snail 2, diving beetle 3, heron 4",
            "Pond snail 1, algae 2, diving beetle 3, heron 4",
            "Algae 1, diving beetle 2, pond snail 3, heron 4",
            "Heron 1, algae 2, pond snail 3, diving beetle 4",
        ],
        "correct_index": 0,
        "why": "Only the algae photosynthesise, so they are level 1; the snail "
               "grazes them, the beetle eats the snail and the heron eats the "
               "beetle.",
    },
    {
        "id": "ks4-trophic-levels-s06",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a woodland web, sparrowhawks eat both blue tits and voles. "
                "Explain how a disease that killed all the voles could affect "
                "the blue tits.",
        "options": [
            "Blue tit numbers would rise, because voles are the chief predator of blue tits",
            "Blue tits would move to level 4 and start to eat the sparrowhawks",
            "Sparrowhawks would eat more blue tits, so blue tit numbers fall",
            "Blue tit numbers would not change, because blue tits eat voles",
        ],
        "correct_index": 2,
        "why": "Losing one of two prey species concentrates the predator's "
               "feeding on the other, so predation pressure on blue tits "
               "rises.",
    },
    {
        "id": "ks4-trophic-levels-s07",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Producers in a woodland fix 80 000 kJ/m²/year. 15% of "
                "this reaches trophic level 2, and 10% of that reaches "
                "trophic level 3. Calculate the energy at trophic level 3.",
        "options": [
            "1200 kJ/m²/year",
            "12 000 kJ/m²/year",
            "8000 kJ/m²/year",
            "20 000 kJ/m²/year",
        ],
        "correct_index": 0,
        "why": "80 000 × 0.15 = 12 000 kJ/m²/year at level 2, and "
               "12 000 × 0.10 = 1200 kJ/m²/year at level 3.",
    },
    {
        "id": "ks4-trophic-levels-s08",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer clears a hedgerow that supported ladybirds, "
                "lacewings and spiders. Explain why aphid numbers on the "
                "neighbouring crop may then rise.",
        "options": [
            "Aphids gain a trophic level, so more energy now reaches them",
            "Hedge plants release a chemical that killed aphids on the crop",
            "Ladybirds are producers, so losing them adds energy to level 2",
            "Several predators of aphids have lost their habitat, so fewer aphids are eaten",
        ],
        "correct_index": 3,
        "why": "The hedge held the level 3 predators that fed on the aphids, so "
               "removing it removes the check on the aphid population.",
    },
    {
        "id": "ks4-trophic-levels-s09",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why energy is described as flowing through an "
                "ecosystem while mineral ions are described as cycling.",
        "options": [
            "Energy moves one way because the arrows on the diagram point one way",
            "Energy is lost as heat and can never be reused, but ions return to the soil",
            "Mineral ions are made fresh by producers, whereas energy is captured",
            "Energy is destroyed by the consumers, while mineral ions cannot be",
        ],
        "correct_index": 1,
        "why": "Heat transferred to the surroundings cannot be recaptured by a "
               "producer, but decomposers return mineral ions to the soil for "
               "reuse.",
    },
    {
        "id": "ks4-trophic-levels-s10",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Phytoplankton in the open ocean are microscopic. Explain why "
                "they are still placed at trophic level 1.",
        "options": [
            "They are the smallest organisms there, and level 1 is the smallest",
            "They float near the surface, and level 1 is the level nearest the sunlight",
            "They photosynthesise, and every level 1 organism makes its own food",
            "They are eaten by zooplankton, and anything eaten is at level 1",
        ],
        "correct_index": 2,
        "why": "Trophic level is set by how an organism feeds, not by its size: "
               "anything that photosynthesises is a producer at level 1.",
    },
    {
        "id": "ks4-trophic-levels-s11",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an Arctic food chain the producers hold 40 000 "
                "kJ/m²/year and the primary consumers hold 3600 "
                "kJ/m²/year. Calculate the percentage transferred.",
        "options": [
            "9%",
            "11%",
            "0.09%",
            "91%",
        ],
        "correct_index": 0,
        "why": "(3600 ÷ 40 000) × 100 = 9%, a little below the "
               "tenth that is usually quoted.",
    },
    {
        "id": "ks4-trophic-levels-s12",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "People eat cod, cod eat herring, herring eat zooplankton and "
                "zooplankton eat phytoplankton. Explain why this chain leaves "
                "very little energy for people.",
        "options": [
            "Cod and herring respire in cold sea water, which wastes far more of their energy",
            "The people are at level 5, so biomass is lost at four transfers",
            "Zooplankton are too small to hold biomass, so level 2 passes none on",
            "Fish are ectothermic, so they pass on less biomass than mammals do",
        ],
        "correct_index": 1,
        "why": "Four transfers at roughly a tenth each leave about one "
               "ten-thousandth of the energy the phytoplankton captured.",
    },
    {
        "id": "ks4-trophic-levels-s13",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The figure of one tenth for energy transfer between trophic "
                "levels is an approximation. Explain why the real value differs "
                "between food chains.",
        "options": [
            "The figure applies only to chains that hold exactly four levels",
            "Producers capture different amounts of light, which alters the transfer figure",
            "The figure was measured in one grassland, so it fits nowhere else",
            "Losses in respiration, egestion and movement differ between species",
        ],
        "correct_index": 3,
        "why": "How much of a meal becomes biomass depends on the animal — an "
               "ectotherm that moves little keeps far more of it than a "
               "running mammal.",
    },
    {
        "id": "ks4-trophic-levels-s14",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an animal at trophic level 4 usually has to hunt "
                "over a much larger area than one at trophic level 2.",
        "options": [
            "Its prey all live at trophic level 1, and level 1 grows in only a few patches",
            "Biomass is lost as heat, and the escaping heat drives its prey apart",
            "A top predator has no predator of its own, so nothing stops it roaming",
            "Little biomass reaches its level per square metre, so its food is thin",
        ],
        "correct_index": 3,
        "why": "Three transfers leave roughly a thousandth of the producers' "
               "biomass, so a level 4 animal must search a far wider area to "
               "find a meal.",
    },
    {
        "id": "ks4-trophic-levels-s15",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a herbivore is at the same trophic level whether "
                "it grazes grass or browses tree leaves.",
        "options": [
            "Tree leaves are at level 2 and grass at level 1, so the two levels average",
            "Grass is a producer but a tree is a consumer, so only grass gives 2",
            "Both grass and tree leaves are producers, so anything eating either is at level 2",
            "A herbivore takes no numbered level, because its diet changes",
        ],
        "correct_index": 2,
        "why": "Grasses and trees both photosynthesise, so both are level 1 and "
               "anything eating either of them is a primary consumer.",
    },
    {
        "id": "ks4-trophic-levels-s16",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer asks why feeding grain to chickens supplies less food "
                "for people than selling the grain. Explain the answer in terms "
                "of trophic levels.",
        "options": [
            "Chickens turn grain into protein, and protein holds more energy",
            "Grain must be cooked before people can eat it, and cooking wastes the energy",
            "Chickens sit at level 2, so the grain passes through three transfers",
            "Eating the grain is one transfer; through chickens it is two",
        ],
        "correct_index": 3,
        "why": "Every extra transfer loses about nine tenths of the biomass, so "
               "eating nearer the producers feeds far more people from the same "
               "field.",
    },
    {
        "id": "ks4-trophic-levels-s17",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says that a food web shows energy moving in more "
                "than one direction. Explain why this is wrong.",
        "options": [
            "Energy does move both ways, but just in the places where decomposers are drawn",
            "Every arrow points from the eaten to the eater, so energy moves one way",
            "A web shows numbers rather than energy, so it marks no direction",
            "Energy moves one way in a chain, but a web marks no direction at all",
        ],
        "correct_index": 1,
        "why": "A web is many chains joined together, and every arrow in it "
               "still runs from prey to predator, so the flow stays one-way.",
    },
    {
        "id": "ks4-trophic-levels-s18",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the amount of light energy captured by the "
                "producers sets a limit on the whole ecosystem.",
        "options": [
            "Producers store energy through the winter and share it out in the spring",
            "All the energy at the other levels came through the producers",
            "Consumers can capture sunlight, but only once the producers have",
            "Producers set the limit because they occupy the widest bar drawn",
        ],
        "correct_index": 1,
        "why": "Photosynthesis is the only entry point for energy, so no level "
               "above can hold more than the fraction that survives the "
               "transfers.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-trophic-levels-h05",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Of the 250 000 kJ/m²/year a grassland captures, 8% "
                "becomes herbivore biomass. A twentieth of that becomes "
                "secondary consumer biomass, and a tenth of that reaches the "
                "top predators. Determine the energy at the top.",
        "options": [
            "1000 kJ/m²/year",
            "100 kJ/m²/year",
            "20 000 kJ/m²/year",
            "2000 kJ/m²/year",
        ],
        "correct_index": 1,
        "why": "250 000 × 0.08 = 20 000; 20 000 ÷ 20 = 1000; "
               "1000 ÷ 10 = 100 kJ/m²/year.",
    },
    {
        "id": "ks4-trophic-levels-h06",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two chains share producers fixing 50 000 kJ/m²/year. "
                "Chain P has three levels and chain Q has five. Taking a tenth "
                "per transfer, calculate how much more energy reaches the top "
                "of P than the top of Q.",
        "options": [
            "500 kJ/m²/year",
            "4950 kJ/m²/year",
            "495 kJ/m²/year",
            "45 kJ/m²/year",
        ],
        "correct_index": 2,
        "why": "P's top holds 50 000 × 0.1 × 0.1 = 500 and Q's top "
               "holds 50 000 × 0.1 four times over = 5, so the "
               "difference is 495 kJ/m²/year.",
    },
    {
        "id": "ks4-trophic-levels-h07",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a lake, algae feed insect larvae, larvae feed roach, roach "
                "feed perch and perch feed pike. The pike hold 1.2 g/m². "
                "Estimate the biomass of the insect larvae at a tenth per "
                "transfer.",
        "options": [
            "1200 g/m²",
            "12 g/m²",
            "120 g/m²",
            "12 000 g/m²",
        ],
        "correct_index": 0,
        "why": "Working back up the chain by a factor of ten each step: pike "
               "1.2, perch 12, roach 120, larvae 1200 g/m².",
    },
    {
        "id": "ks4-trophic-levels-h08",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes that nine tenths of the biomass at each "
                "trophic level is 'used up and destroyed'. Evaluate this "
                "statement.",
        "options": [
            "Correct — biomass is destroyed at each level, so the pyramid narrows",
            "Wrong — biomass is never destroyed; it passes to the surroundings and to decomposers",
            "Wrong — all of it passes to decomposers and none is lost to the air",
            "Correct — the tenth that moves up a level is the part that survives",
        ],
        "correct_index": 1,
        "why": "Biomass is not destroyed: it leaves as heat from respiration, "
               "as faeces and urine for the decomposers, and as water vapour.",
    },
    {
        "id": "ks4-trophic-levels-h09",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a rock pool the limpets are the only primary consumers. "
                "Predict the consequences for the pool if a disease removed "
                "every limpet.",
        "options": [
            "The seaweed dies out, because limpet waste had supplied all its mineral ions",
            "The crabs drop to level 2 and begin to photosynthesise instead",
            "Nothing above level 2 changes, because a web can bypass a lost level",
            "Consumers above them lose their food, and the grazed seaweed spreads",
        ],
        "correct_index": 3,
        "why": "With no alternative route from level 1, everything above level 2 "
               "loses its supply, while the ungrazed producers increase.",
    },
    {
        "id": "ks4-trophic-levels-h10",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the energy reaching trophic level 4 varies more "
                "between ecosystems than the energy captured at trophic "
                "level 1.",
        "options": [
            "Level 4 organisms migrate, so their energy is counted in two places",
            "Level 1 energy is set by the Sun, which is the same across the Earth",
            "Each of the three transfers below it varies, and those variations multiply together",
            "Level 4 holds the least energy, and small quantities measure badly",
        ],
        "correct_index": 2,
        "why": "Three transfers each of which might be 5% or 20% compound, so "
               "level 4 can differ by a factor of tens between two ecosystems.",
    },
    {
        "id": "ks4-trophic-levels-h11",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Biomass at four levels of a chain measures 4000, 500, 60 and "
                "5 g/m². Determine which transfer was the least "
                "efficient.",
        "options": [
            "Level 3 to level 4, at about 8%",
            "Level 1 to level 2, at about 13%",
            "Level 2 to level 3, at about 12%",
            "Level 3 to level 4, at about 92%",
        ],
        "correct_index": 0,
        "why": "500 ÷ 4000 = 12.5%, 60 ÷ 500 = 12% and 5 ÷ 60 = "
               "8.3%, so the top transfer is the least efficient.",
    },
    {
        "id": "ks4-trophic-levels-h12",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two ecologists disagree over whether a hoverfly is at trophic "
                "level 2 or level 3. The adult drinks nectar and the larva eats "
                "aphids. Resolve the disagreement.",
        "options": [
            "Only level 2 is right, because an insect takes the trophic level it feeds at as an adult",
            "Both are right — the larva feeds at level 3 and the adult at level 2",
            "Only level 3 is right, because an insect keeps the level it fed at as a larva",
            "Neither is right — an insect that changes diet is left out of the chain",
        ],
        "correct_index": 1,
        "why": "Trophic level describes a feeding relationship, not a species, "
               "so an animal whose diet changes with its life stage occupies "
               "both.",
    },
    {
        "id": "ks4-trophic-levels-h13",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An owl reaches its food by two routes: grass → vole "
                "→ owl, and grass → beetle → shrew → owl. "
                "Compare the energy the owl obtains by each route.",
        "options": [
            "The longer route supplies more, because it passes two consumers",
            "Both supply the same, because both routes begin with the same grass",
            "The shorter route supplies about a hundred times as much energy as the longer",
            "The shorter route supplies about ten times as much as the longer one",
        ],
        "correct_index": 3,
        "why": "The vole route reaches the owl after two transfers and the "
               "beetle route after three, so one extra tenfold loss separates "
               "them.",
    },
    {
        "id": "ks4-trophic-levels-h14",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A tropical reef and an Arctic sea both have four trophic "
                "levels, but the reef supports far more biomass at level 4. "
                "Suggest an explanation.",
        "options": [
            "Warmth and strong light raise photosynthesis, so far more energy enters at level 1",
            "Arctic animals are larger, so each holds a greater share of the biomass",
            "Cold water holds more oxygen, and oxygen limits how much biomass forms",
            "The reef has fewer transfers, so less of its biomass is lost as heat",
        ],
        "correct_index": 0,
        "why": "The number of levels is the same, so the difference must come "
               "from the energy entering at level 1, which light and warmth "
               "raise.",
    },
    {
        "id": "ks4-trophic-levels-h15",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine the trophic level of a parasitic wasp whose larvae "
                "feed inside caterpillars that eat cabbage leaves.",
        "options": [
            "Level 2, because it lives on the body of a plant-eating insect",
            "Level 4, because a parasite always feeds one level above its host",
            "Level 3, because its food is a primary consumer",
            "No level at all, because a parasite does not kill and eat its host outright",
        ],
        "correct_index": 2,
        "why": "The wasp larva takes its biomass from the caterpillar, a level 2 "
               "herbivore, so the wasp is a secondary consumer at level 3.",
    },
    {
        "id": "ks4-trophic-levels-h16",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fire destroys all the heather on a moor. Predict the order in "
                "which the trophic levels above the heather are affected, and "
                "explain why.",
        "options": [
            "Level 4 first, because a top predator holds the smallest store of biomass of all",
            "All levels at the same moment, because the whole web is joined by arrows",
            "Level 3 first, because level 2 can switch to feeding on decomposers",
            "Level 2 first, then 3, then 4 — each loses the level that feeds it",
        ],
        "correct_index": 3,
        "why": "Biomass only travels upwards, so the loss works up the chain "
               "from the level that fed directly on the heather.",
    },
    {
        "id": "ks4-trophic-levels-h17",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two grasslands fix 30 000 and 300 kJ/m²/year. Taking a "
                "tenth per transfer and 0.5 kJ/m²/year as the least a "
                "level needs, determine how many trophic levels each can "
                "support.",
        "options": [
            "Five levels for the first grassland and four for the second",
            "Five levels for the first grassland and three for the second",
            "Six levels for the first grassland and three for the second",
            "Both support four levels, because exactly the same transfer rule applies",
        ],
        "correct_index": 1,
        "why": "30 000 falls to 3 at level 5 and 0.3 at level 6, so five "
               "levels; 300 falls to 3 at level 3 and 0.3 at level 4, so "
               "three.",
    },
    {
        "id": "ks4-trophic-levels-h18",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A small island has no large predators. Suggest why introducing "
                "a species that feeds at trophic level 4 is likely to fail.",
        "options": [
            "Too little biomass reaches level 4 there to support a breeding population",
            "A level 4 species cannot survive without a level 5 predator above it",
            "An island's producers capture no light, so no biomass reaches level 2",
            "A new species raises every other species by one level, which no ecosystem survives",
        ],
        "correct_index": 0,
        "why": "A small area fixes little energy at level 1, and three "
               "transfers leave far too little for a viable population of top "
               "predators.",
    },

    # ══ standard/harder · s19-s26, h19-h26 (MRB-338 night 3 top-up) ══
    {
        "id": "ks4-trophic-levels-s19",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pack of wolves in a national park is reintroduced after being "
                "absent for many decades. Explain why ecologists predict this "
                "will change both the deer population (trophic level 2) and the "
                "amount of vegetation the deer eat (trophic level 1).",
        "options": [
            "Deer numbers stay exactly the same, because wolves mainly hunt the oldest and weakest animals in a herd",
            "Wolves reduce the deer population directly, which in turn allows more vegetation to survive and grow back",
            "Vegetation increases because wolves trample and clear new ground as they move through the park",
            "Deer numbers rise at first, because wolves initially compete with deer for the same plant food",
        ],
        "correct_index": 1,
        "why": "Removing a predator's grip on a herbivore population changes "
               "grazing pressure, so the effect reaches down to the producers as "
               "well as the herbivores.",
    },
    {
        "id": "ks4-trophic-levels-s20",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A brown bear eats berries for part of the year and voles, which "
                "eat only plant roots and seeds, for the rest of the year. State "
                "the bear's trophic level while eating each food, and explain why "
                "the two differ.",
        "options": [
            "Trophic level 2 for both foods, because a bear's own trophic level is fixed for life once it has first been set",
            "Trophic level 3 for both foods, because a large predator like a bear is classed as a tertiary consumer by size",
            "Trophic level 2 when eating berries and level 3 when eating voles, because the voles are themselves primary consumers",
            "Trophic level 4 for both foods, because bears sit above every other mammal in a food web",
        ],
        "correct_index": 2,
        "why": "Berries come straight from a producer, making the bear a primary "
               "consumer; voles are themselves primary consumers, so eating them "
               "makes the bear a secondary consumer instead.",
    },
    {
        "id": "ks4-trophic-levels-s21",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest what would eventually happen to the recycling of "
                "nutrients in a woodland if every decomposer species were "
                "removed.",
        "options": [
            "Nutrients would move faster between organisms, because nothing would be left decaying on the woodland floor",
            "Producers would grow faster at first, absorbing the extra dead matter directly through their roots",
            "Little would change, because most of a woodland's minerals come from rainfall rather than from decay",
            "Nutrients would stay locked inside dead matter and waste, so they could no longer be recycled back to producers",
        ],
        "correct_index": 3,
        "why": "With nothing left to break down dead matter and waste, the "
               "nutrients inside it would stay locked away rather than being "
               "released back to producers.",
    },
    {
        "id": "ks4-trophic-levels-s22",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a lake, algae are eaten by water fleas, which are eaten by "
                "minnows, which are eaten by pike. A disease wipes out the water "
                "fleas. Explain the likely effect on the algae and on the "
                "minnows.",
        "options": [
            "Algae increase because they are grazed less, while minnows decline because their main food source has gone",
            "Algae decrease because water fleas release nutrients as they die, while minnows are wholly unaffected",
            "Algae stay the same, because pike then start feeding on algae directly to make up the shortfall",
            "Minnows increase at first, because they switch to eating the dead water fleas left in the lake",
        ],
        "correct_index": 0,
        "why": "Removing the grazer lets the algae increase, while the minnows "
               "lose the food source they depended on and decline.",
    },
    {
        "id": "ks4-trophic-levels-s23",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Producers in a reedbed capture 60 000 kJ/m²/year. A tenth of "
                "this energy is transferred at each of the next two trophic "
                "transfers. Calculate how much energy is LOST between trophic "
                "level 1 and trophic level 3, not how much remains.",
        "options": [
            "600 kJ/m²/year, the energy that reaches trophic level 3 after both transfers",
            "6 000 kJ/m²/year, the energy transferred at the first step alone",
            "59 400 kJ/m²/year, once the 600 kJ/m²/year that does reach level 3 is subtracted from 60 000",
            "54 000 kJ/m²/year, assuming a tenth of the producers' energy is lost at each step of the whole chain",
        ],
        "correct_index": 2,
        "why": "600 kJ/m²/year reaches level 3, so the energy lost is 60 000 "
               "minus 600, which is 59 400 kJ/m²/year.",
    },
    {
        "id": "ks4-trophic-levels-s24",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A food chain in a hedgerow habitat has producers holding 95 000 "
                "kJ/m²/year. Grasshoppers at trophic level 2 hold 9 500 "
                "kJ/m²/year. Calculate the percentage of the producers' energy "
                "that was NOT transferred to the grasshoppers.",
        "options": [
            "10%, since that is the standard transfer efficiency assumed for every food chain",
            "10.5%, allowing for a small rounding correction on the raw figures given",
            "9 500%, from dividing the larger figure by the smaller one instead of the other way round",
            "90%, since only 9 500 of the original 95 000 kJ/m²/year reached the grasshoppers",
        ],
        "correct_index": 3,
        "why": "9 500 out of 95 000 is 10%, so the percentage not transferred is "
               "100% minus 10%, which is 90%.",
    },
    {
        "id": "ks4-trophic-levels-s25",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A young child says a decomposer 'eats' dead plants and animals "
                "in the same way a fox eats a rabbit. Explain one way in which "
                "what a decomposer does is different.",
        "options": [
            "There is no real difference; a decomposer breaks down food inside its body exactly as a fox does",
            "A decomposer releases digestive substances onto its food and absorbs the products, rather than swallowing it whole first",
            "A decomposer breaks down plant matter alone, while a fox is able to digest both plants and animals too",
            "A decomposer works far more slowly than a fox, but otherwise digests its food in the same way",
        ],
        "correct_index": 1,
        "why": "A decomposer releases substances onto its food and absorbs the "
               "digested products, rather than swallowing solid food and "
               "digesting it internally as a fox does.",
    },
    {
        "id": "ks4-trophic-levels-s26",
        "subtopic_slug": "trophic-levels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the trophic level of a scavenger that only eats the bodies "
                "of animals already killed by other predators, and explain your "
                "reasoning.",
        "options": [
            "The same trophic level as the predator that killed the animal, because trophic level depends on what was eaten, not how",
            "One trophic level lower than that predator, because scavenging counts as its own separate form of primary consumption",
            "One trophic level higher than that predator, because eating an already-dead body needs no active hunting",
            "No fixed trophic level, because a scavenger is classed in the same way as a decomposer instead",
        ],
        "correct_index": 0,
        "why": "Trophic level depends on what an organism has eaten, not on how "
               "it obtained its food, so a scavenger sits at the same level as a "
               "predator that ate the same prey.",
    },
    {
        "id": "ks4-trophic-levels-h19",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student claims that removing sea otters, which eat sea "
                "urchins, from a coastal ecosystem can only ever affect the sea "
                "urchin population and nothing further down the food chain. "
                "Evaluate this claim, given that sea urchins graze on kelp.",
        "options": [
            "The claim holds, because sea urchin numbers are the one part of a reef ecosystem otters really influence",
            "The claim fails; more urchins would graze more heavily on kelp, so the effect reaches trophic level 1 as well",
            "The claim holds, because kelp forests recover fully within days regardless of how many urchins are grazing",
            "The claim fails, because sea otters graze on kelp directly and so bypass the urchins altogether",
        ],
        "correct_index": 1,
        "why": "More urchins graze more heavily on the kelp forest, so the "
               "effect of losing the otters reaches trophic level 1, not just "
               "the level directly below the otters.",
    },
    {
        "id": "ks4-trophic-levels-h20",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wetland's producers fix 64 000 kJ/m²/year. The first transfer "
                "captures 25% of this energy, the second transfer captures 20% of "
                "that, and the third transfer captures 25% of that. Determine the "
                "energy reaching trophic level 4.",
        "options": [
            "800 kJ/m²/year, from 64 000 falling to 16 000, then 3 200, then 800 across the three transfers",
            "80 kJ/m²/year, from applying all three percentages to the original 64 000 kJ/m²/year separately",
            "4 000 kJ/m²/year, from applying just the first two transfers and stopping one level early",
            "3 200 kJ/m²/year, the energy already reached at trophic level 3, treated as the final answer",
        ],
        "correct_index": 0,
        "why": "64 000 falls to 16 000, then 3 200, then 800 kJ/m²/year across "
               "the three transfers in turn.",
    },
    {
        "id": "ks4-trophic-levels-h21",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A sparrow eats only seeds for a week, then switches to eating "
                "only caterpillars, which feed on leaves, for the following week. "
                "Compare the sparrow's trophic level in each week.",
        "options": [
            "The trophic level stays at 3 throughout, because a sparrow is generally classed as a secondary consumer",
            "The trophic level falls from 3 to 2, because caterpillars are easier prey than seeds are to gather",
            "The trophic level stays at 2 throughout, because a sparrow's body size, not its diet, sets its trophic level",
            "The trophic level rises from 2 to 3, because seeds come directly from a producer but caterpillars do not",
        ],
        "correct_index": 3,
        "why": "Seeds come directly from a producer, so eating them makes the "
               "sparrow a primary consumer; caterpillars are themselves primary "
               "consumers, so eating them raises the sparrow to a secondary "
               "consumer.",
    },
    {
        "id": "ks4-trophic-levels-h22",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In one estuary, phytoplankton fix 500 000 kJ/m²/year and only 2% "
                "is transferred to zooplankton because so much energy is lost in "
                "the fast-moving current. In a nearby calm lagoon, phytoplankton "
                "fix the same 500 000 kJ/m²/year and 10% is transferred to "
                "zooplankton. Determine how many times more energy reaches the "
                "zooplankton in the lagoon than in the estuary.",
        "options": [
            "Twice as much energy reaches the lagoon's zooplankton, from doubling the estuary's transfer efficiency",
            "The same amount of energy reaches both, because the producers fix an identical 500 000 kJ/m²/year in each",
            "Half as much energy reaches the lagoon's zooplankton, since calm water usually slows every biological process",
            "Five times as much energy reaches the lagoon's zooplankton, from 50 000 kJ/m²/year against 10 000 kJ/m²/year",
        ],
        "correct_index": 3,
        "why": "10 000 kJ/m²/year reaches the estuary's zooplankton and 50 000 "
               "kJ/m²/year reaches the lagoon's, which is five times as much.",
    },
    {
        "id": "ks4-trophic-levels-h23",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An island had only birds as predators until rats were "
                "accidentally introduced by a ship. The rats prey on birds' eggs "
                "and on insects, both of which sit at trophic level 2. Suggest "
                "why the rats are difficult to place at a single, fixed trophic "
                "level.",
        "options": [
            "It cannot be placed, because an introduced species is not assigned a trophic level of its own",
            "It sits permanently at trophic level 4, because any predator that hunts birds is automatically classed as a top predator",
            "It switches trophic level depending on which food source it is using at a given time, rather than holding one fixed level",
            "It sits permanently at trophic level 1, because eggs are not considered a form of living prey",
        ],
        "correct_index": 2,
        "why": "The rats switch between different food sources rather than "
               "feeding at one fixed point in the food web, so no single trophic "
               "level describes them fully.",
    },
    {
        "id": "ks4-trophic-levels-h24",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A textbook states that no food chain can ever have more than "
                "five trophic levels. Evaluate this rule, given that the number "
                "of levels a chain can support depends on how much energy "
                "remains available at each one.",
        "options": [
            "The rule overstates the case; the real limit is set by how much energy is available, making it a typical maximum rather than an absolute one",
            "The rule is entirely correct, because a sixth trophic level has not been recorded in any ecosystem studied so far",
            "The rule understates the case, because in reality most food chains struggle to reach even three trophic levels",
            "The rule is meaningless, because trophic levels merely describe artificial food chains drawn for a textbook",
        ],
        "correct_index": 0,
        "why": "Five is the usual maximum because of how much energy is "
               "available, not a fixed law, so a chain with an unusually "
               "large energy supply could in principle go further.",
    },
    {
        "id": "ks4-trophic-levels-h25",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An upwelling zone off the coast, where nutrient-rich water rises "
                "to the surface, supports a food chain with five trophic levels. "
                "The open ocean far from any coast, where nutrients are scarce, "
                "rarely supports a food chain beyond three trophic levels. "
                "Suggest why the difference in nutrient supply leads to this "
                "difference in chain length.",
        "options": [
            "The two chains capture the same total energy between them, and the upwelling zone simply spreads it across more organisms",
            "Nutrient supply affects the taste of the producers, not how much energy a food chain can support",
            "The open ocean simply loses more energy at each transfer than the upwelling zone does, for reasons unrelated to nutrients",
            "More nutrients allow greater photosynthesis, so more producer energy is captured and enough remains to sustain extra levels",
        ],
        "correct_index": 3,
        "why": "More nutrients allow greater photosynthesis at trophic level 1, "
               "so more energy is captured and enough remains, even after the "
               "usual losses, to sustain extra levels above it.",
    },
    {
        "id": "ks4-trophic-levels-h26",
        "subtopic_slug": "trophic-levels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A national park bans hunting of a large herbivore at trophic "
                "level 2 that had previously been controlled by culling. Predict "
                "the short-term effect on the vegetation at trophic level 1, and "
                "the knock-on effect this could have on the herbivore's predators "
                "at trophic level 3.",
        "options": [
            "Vegetation is grazed more heavily and may decline, which could later reduce food for both the herbivore and its predators",
            "Nothing changes at any level, because a hunting ban affects how the herbivore population is counted, not its actual size",
            "Predators decline immediately, because more herbivores tends to frighten predators away from a habitat",
            "Vegetation increases at first, because herbivores spread out and graze a wider, less concentrated area",
        ],
        "correct_index": 0,
        "why": "More herbivores graze more vegetation, which may decline; less "
               "vegetation can then reduce the food available to both the "
               "herbivores and, in turn, their predators.",
    },
]
