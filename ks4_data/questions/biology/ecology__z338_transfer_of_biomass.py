"""Biology · Ecology — the MRB-338 expansion, transfer of biomass (4.7.4.3).

Triple-only content. The spec point carries an equation, so roughly half of
these rows are calculations: the efficiency of one transfer, its reverse, the
feed needed per kilogram of body mass gained, and the compounded efficiency of a
whole chain. The rest work the four loss routes the lesson names — respiration,
movement, egestion and excretion — plus the fifth the arithmetic keeps running
into, which is that a herbivore never eats the whole of the plant.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-transfer-of-biomass-e05",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the equation used to calculate the efficiency of a "
                "biomass transfer.",
        "options": [
            "(biomass at the next level ÷ biomass at this level) × 100",
            "(biomass at this level ÷ biomass at the next level) × 100",
            "(biomass at the next level − biomass at this level) × 100",
            "(biomass at this level + biomass at the next level) ÷ 100",
        ],
        "correct_index": 0,
        "why": "Efficiency is the share of what was there that made it to the "
               "level above, so the next level is divided by the current one.",
    },
    {
        "id": "ks4-transfer-of-biomass-e06",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the difference between egestion and excretion.",
        "options": [
            "Egestion removes body wastes; excretion removes undigested food",
            "Egestion removes undigested food; excretion removes wastes made by the body",
            "Egestion removes water; excretion removes gut solids",
            "Egestion happens in plants, whereas excretion happens in animals",
        ],
        "correct_index": 1,
        "why": "Egested material never entered the body's cells, whereas "
               "excreted urea was made by the body's own reactions.",
    },
    {
        "id": "ks4-transfer-of-biomass-e07",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State where the energy released by respiration in a consumer "
                "ends up.",
        "options": [
            "In the consumer's new body tissue",
            "In the consumer's faeces and in its urine",
            "In the surroundings, as heat",
            "In the next trophic level up",
        ],
        "correct_index": 2,
        "why": "Energy released in respiration is used for life processes and "
               "transferred to the surroundings as heat, so it leaves the chain.",
    },
    {
        "id": "ks4-transfer-of-biomass-e08",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the part of a plant that a human is unable to digest.",
        "options": [
            "The starch that is stored inside the leaf cells",
            "The glucose being carried in the phloem",
            "The protein dissolved in the cytoplasm",
            "The cellulose of the cell walls",
        ],
        "correct_index": 3,
        "why": "Humans make no enzyme that breaks down cellulose, so it passes "
               "through the gut and is egested as fibre in the faeces.",
    },
    {
        "id": "ks4-transfer-of-biomass-e09",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why an animal that moves a great deal transfers less "
                "biomass to its predator.",
        "options": [
            "Energy used for movement is lost as heat instead of becoming tissue",
            "A moving animal is harder to catch, so less of it is ever eaten",
            "Movement wears the animal's own muscles away and so reduces its total mass",
            "A moving animal egests more, because food passes through it faster",
        ],
        "correct_index": 0,
        "why": "Muscle contraction is powered by respiration, and the energy it "
               "releases leaves as heat rather than being built into tissue.",
    },
    {
        "id": "ks4-transfer-of-biomass-e10",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by the efficiency of a biomass transfer.",
        "options": [
            "The speed at which one organism eats another in a food chain",
            "The share of one level's biomass that becomes biomass at the next",
            "The mass of food an organism has to eat in order to survive for a single day",
            "The number of organisms that can be fed at the next level up",
        ],
        "correct_index": 1,
        "why": "Efficiency is a proportion, not a rate or a count: it compares "
               "the biomass gained above with the biomass available below.",
    },
    {
        "id": "ks4-transfer-of-biomass-e11",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A cow gains 1 kg of body mass for every 10 kg of grass it "
                "eats. State the efficiency of this transfer.",
        "options": [
            "1%",
            "90%",
            "10%",
            "100%",
        ],
        "correct_index": 2,
        "why": "(1 ÷ 10) × 100 = 10%, which is the usual figure quoted "
               "for a transfer between trophic levels.",
    },
    {
        "id": "ks4-transfer-of-biomass-e12",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the organisms that receive the biomass an animal loses in "
                "its faeces and urine.",
        "options": [
            "The producers",
            "The primary consumers of the chain",
            "The apex predators",
            "The decomposers",
        ],
        "correct_index": 3,
        "why": "Bacteria and fungi break down faeces and urine, so that biomass "
               "leaves the chain rather than passing to the next level.",
    },
    {
        "id": "ks4-transfer-of-biomass-e13",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State approximately what share of the biomass taken in at a "
                "trophic level is used in respiration.",
        "options": [
            "Between about 60% and 70%",
            "Between about 20% and 30% of the total",
            "Between about 10% and 20%",
            "Less than about 5%",
        ],
        "correct_index": 0,
        "why": "Respiration is by far the largest loss route, taking roughly two "
               "thirds, with egestion accounting for most of the rest.",
    },
    {
        "id": "ks4-transfer-of-biomass-e14",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the part of an animal's food intake that becomes "
                "available to the next trophic level.",
        "options": [
            "The part that passes out of it as faeces",
            "The part built into its own body tissue",
            "The part it uses in respiration each day",
            "The part it loses as urine and as water vapour",
        ],
        "correct_index": 1,
        "why": "Only the biomass that becomes the animal's own tissue is still "
               "there to be eaten, so only that part can move upwards.",
    },
    {
        "id": "ks4-transfer-of-biomass-e15",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why a plant's roots are usually not counted as biomass "
                "transferred to a grazing animal.",
        "options": [
            "Roots contain no living material, so they hold no biomass at all",
            "Roots are made of cellulose, and cellulose holds no usable energy at all",
            "A grazing animal eats only the parts above the ground",
            "Roots count as part of the soil rather than as part of the plant",
        ],
        "correct_index": 2,
        "why": "Biomass that is never eaten cannot be transferred, and a grazer "
               "leaves the whole root system behind in the soil.",
    },
    {
        "id": "ks4-transfer-of-biomass-e16",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A trophic level holds 900 g/m² and passes 90 "
                "g/m² to the level above. State the mass that was not "
                "transferred.",
        "options": [
            "90 g/m²",
            "990 g/m²",
            "10 g/m²",
            "810 g/m²",
        ],
        "correct_index": 3,
        "why": "900 − 90 = 810 g/m², which was respired, egested "
               "or excreted rather than passed upwards.",
    },
    {
        "id": "ks4-transfer-of-biomass-e17",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason why a predator gains less than 100% of its "
                "prey's biomass even when it eats all of it.",
        "options": [
            "The predator respires, so some of the meal is lost as heat",
            "The predator's gut absorbs only the water from the whole of the meal",
            "The prey's biomass falls as soon as it stops respiring",
            "The predator stores the meal without changing any part of it",
        ],
        "correct_index": 0,
        "why": "Even a completely eaten meal is mostly respired to power the "
               "predator's own life processes, and that energy leaves as heat.",
    },
    {
        "id": "ks4-transfer-of-biomass-e18",
        "subtopic_slug": "transfer-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why a biomass transfer is described as a percentage "
                "rather than as a mass.",
        "options": [
            "A mass cannot be measured accurately in a wild habitat",
            "A percentage lets transfers of very different sizes be compared",
            "A percentage is the only figure a pyramid can be drawn from",
            "A mass would change every time that the organism was weighed all over again",
        ],
        "correct_index": 1,
        "why": "A percentage is independent of the size of the ecosystem, so a "
               "pond and a prairie can be set side by side.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-transfer-of-biomass-s05",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A trophic level holds 5400 g/m² and transfers 8% of it "
                "upwards. Calculate the biomass at the level above.",
        "options": [
            "4968 g/m²",
            "675 g/m²",
            "432 g/m²",
            "43.2 g/m²",
        ],
        "correct_index": 2,
        "why": "5400 × 0.08 = 432 g/m²; the other 4968 g/m² "
               "was respired, egested or excreted.",
    },
    {
        "id": "ks4-transfer-of-biomass-s06",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Over one summer a sheep eats 350 kg of grass and puts on 14 kg. "
                "Calculate the transfer efficiency.",
        "options": [
            "25%",
            "0.04%",
            "96%",
            "4%",
        ],
        "correct_index": 3,
        "why": "(14 ÷ 350) × 100 = 4%, well below the tenth usually "
               "quoted, because a sheep both grazes and walks.",
    },
    {
        "id": "ks4-transfer-of-biomass-s07",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a carnivore usually transfers a greater share of "
                "its food into biomass than a herbivore of the same size.",
        "options": [
            "Meat is easier to digest than plant material, so less is egested",
            "Meat contains rather less energy, so the carnivore needs to respire less",
            "A carnivore moves less than a herbivore, so it loses less heat",
            "A carnivore eats less often, so it spends fewer days digesting",
        ],
        "correct_index": 0,
        "why": "Plant cell walls are largely indigestible, so a herbivore loses "
               "a far larger share of every meal as faeces.",
    },
    {
        "id": "ks4-transfer-of-biomass-s08",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A bullock eats 2800 kg of feed and gains 200 kg of body mass. "
                "Calculate the mass of feed needed for each kilogram of body "
                "mass gained.",
        "options": [
            "0.071 kg of feed per kilogram of mass gained",
            "14 kg of feed per kilogram gained",
            "7 kg of feed per kilogram gained",
            "2600 kg of feed per kilogram gained",
        ],
        "correct_index": 1,
        "why": "2800 ÷ 200 = 14, so every kilogram of beef required 14 kg "
               "of feed — an efficiency of about 7%.",
    },
    {
        "id": "ks4-transfer-of-biomass-s09",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an animal kept in a cold field transfers less of "
                "its feed into biomass than the same animal in a warm barn.",
        "options": [
            "Cold feed passes through the gut a lot faster, so much more of it is egested",
            "A cold animal eats less, so it has less feed to convert to mass",
            "More of its food is respired to keep its body temperature up",
            "Cold air carries biomass off the animal's skin as water vapour",
        ],
        "correct_index": 2,
        "why": "A mammal holds its body temperature constant, so a cold "
               "environment forces it to respire more just to stay warm.",
    },
    {
        "id": "ks4-transfer-of-biomass-s10",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the efficiency of transfer into a growing lamb is "
                "higher than into a fully grown sheep.",
        "options": [
            "A lamb eats less, so a smaller mass of feed has to be converted",
            "A lamb's gut is shorter, so it egests less of its food",
            "A grown sheep respires less, so more feed is left for growth",
            "A growing animal builds new tissue, while a grown one maintains itself",
        ],
        "correct_index": 3,
        "why": "Efficiency counts tissue gained, and an adult at a steady mass "
               "gains none — nearly all its feed goes into maintenance.",
    },
    {
        "id": "ks4-transfer-of-biomass-s11",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fish farm converts 25% of its feed into fish, and a pig farm "
                "10%. Calculate how much more feed the pig farm needs to produce "
                "500 kg of meat.",
        "options": [
            "3000 kg",
            "1500 kg",
            "7000 kg",
            "75 kg",
        ],
        "correct_index": 0,
        "why": "500 ÷ 0.25 = 2000 kg of feed for the fish and 500 ÷ "
               "0.10 = 5000 kg for the pigs, a difference of 3000 kg.",
    },
    {
        "id": "ks4-transfer-of-biomass-s12",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a pig kept in a small pen produces more pork per "
                "kilogram of feed than one kept in an open field.",
        "options": [
            "A penned pig eats a great deal more feed, so it has more material to build with",
            "Less energy goes into movement, so more of the feed becomes tissue",
            "A penned pig egests less, because a small pen keeps its gut warm",
            "A penned pig absorbs extra biomass from the floor of the pen",
        ],
        "correct_index": 1,
        "why": "Movement is powered by respiration, so an animal that walks less "
               "transfers a larger share of its feed into body tissue.",
    },
    {
        "id": "ks4-transfer-of-biomass-s13",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the transfer from producers to herbivores in a "
                "woodland is often nearer 5% than the usual tenth.",
        "options": [
            "Woodland herbivores respire faster than grassland ones of that size",
            "Trees hold their biomass as cellulose, which contains no energy",
            "Woodland is shaded, so the producers build less biomass in each square metre",
            "Much of a tree is wood and root, which the herbivores never eat",
        ],
        "correct_index": 3,
        "why": "Efficiency is measured against all the producer biomass present, "
               "and most of a tree's mass is trunk and root that nothing grazes.",
    },
    {
        "id": "ks4-transfer-of-biomass-s14",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person eats 2 kg of beef. Determine the mass of grain the "
                "cattle had to eat to produce it, taking a tenth as the "
                "transfer.",
        "options": [
            "0.2 kg",
            "200 kg",
            "2000 kg",
            "20 kg",
        ],
        "correct_index": 3,
        "why": "Working backwards through one transfer multiplies by ten, so "
               "2 kg of beef required about 20 kg of grain.",
    },
    {
        "id": "ks4-transfer-of-biomass-s15",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an efficiency figure worked out from one animal on "
                "one farm may not apply to the whole herd.",
        "options": [
            "Age, activity and health differ between animals, so each converts differently",
            "Efficiency can be measured for a whole herd but never for one animal",
            "A single animal's mass cannot be measured accurately enough to use",
            "Efficiency changes with the weather, so no figure lasts beyond a day",
        ],
        "correct_index": 0,
        "why": "A young, healthy, penned animal converts feed far better than an "
               "old or sick one, so one figure is not the herd's mean.",
    },
    {
        "id": "ks4-transfer-of-biomass-s16",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the biomass of a woodland's decomposers is not "
                "counted as biomass transferred up the food chain.",
        "options": [
            "Decomposers hold no biomass of their own, because they are microscopic",
            "They take biomass that has already left the chain, so it goes no higher",
            "Decomposers pass their biomass back to the producers, not up the chain",
            "Decomposers sit at trophic level 1, so the whole of their biomass is already counted",
        ],
        "correct_index": 1,
        "why": "Decomposers feed on dead remains and wastes, which had already "
               "been lost from the chain before they reached them.",
    },
    {
        "id": "ks4-transfer-of-biomass-s17",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what happens to the biomass an animal uses for growth "
                "with the biomass it uses for movement.",
        "options": [
            "Both become tissue, but growth builds the bone while movement builds the muscle",
            "Both leave as heat, but growth releases it more slowly than movement",
            "Growth becomes tissue a predator can eat; movement leaves as heat",
            "Growth leaves the body as heat; movement is stored in the muscles",
        ],
        "correct_index": 2,
        "why": "Growth is the only route that keeps biomass inside the chain; "
               "energy spent on movement is transferred to the surroundings.",
    },
    {
        "id": "ks4-transfer-of-biomass-s18",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an efficiency above about 25% would be surprising "
                "for any farm animal.",
        "options": [
            "No animal eats more than a quarter of the feed offered",
            "A balance cannot measure a gain above a quarter accurately",
            "An efficiency above a quarter means the animal stopped growing",
            "Respiration alone takes well over half of the biomass in any animal's food",
        ],
        "correct_index": 3,
        "why": "Roughly two thirds of an animal's intake is respired before "
               "egestion and excretion are counted, which caps the rest.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-transfer-of-biomass-h05",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A food chain has three transfers above the producers, each "
                "one less efficient than the last: 15%, then 10%, then 5%. "
                "Starting from 400 000 kJ/m²/year fixed by the producers, work "
                "out how much energy reaches the top of this chain, at "
                "trophic level 4.",
        "options": [
            "6000 kJ/m²/year",
            "60 000 kJ/m²/year",
            "120 000 kJ/m²/year",
            "300 kJ/m²/year",
        ],
        "correct_index": 3,
        "why": "400 000 × 0.15 = 60 000; × 0.10 = 6000; × 0.05 = "
               "300 kJ/m²/year.",
    },
    {
        "id": "ks4-transfer-of-biomass-h06",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Beef needs 25 kg of grain for each kilogram produced, and "
                "chicken needs 4 kg. Determine how much more grain 300 kg of "
                "beef requires than 300 kg of chicken.",
        "options": [
            "6300 kg",
            "7500 kg",
            "8700 kg",
            "21 kg",
        ],
        "correct_index": 0,
        "why": "25 × 300 = 7500 kg against 4 × 300 = 1200 kg, so the "
               "beef needs 6300 kg more grain.",
    },
    {
        "id": "ks4-transfer-of-biomass-h07",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student divides one biomass by another, gets 0.085 and writes "
                "the efficiency as 0.085%. Explain the error and give the "
                "correct value.",
        "options": [
            "The ratio should be divided by 100 — the efficiency is 0.00085%",
            "The ratio was not multiplied by 100 — the efficiency is 8.5%",
            "The ratio is already a percentage, so 0.085% is correct exactly as written",
            "The ratio should be inverted — the efficiency is about 11.8%",
        ],
        "correct_index": 1,
        "why": "The equation ends in × 100, which turns the ratio 0.085 "
               "into 8.5%.",
    },
    {
        "id": "ks4-transfer-of-biomass-h08",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Producers hold 90 000 g/m² and the tertiary consumers "
                "of the same chain hold 9 g/m². Determine the efficiency "
                "of the whole chain.",
        "options": [
            "10%",
            "1%",
            "0.01%",
            "0.1%",
        ],
        "correct_index": 2,
        "why": "(9 ÷ 90 000) × 100 = 0.01%, which is what three "
               "transfers of roughly a fifth each multiply out to.",
    },
    {
        "id": "ks4-transfer-of-biomass-h09",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says a transfer efficiency of 10% means the predator "
                "eats a tenth of the prey population. Evaluate this.",
        "options": [
            "Correct — efficiency counts the individuals eaten per level",
            "Wrong — it means the predator eats a tenth of each prey animal",
            "Correct — a tenth is eaten and a tenth of that is then digested",
            "Wrong — it means a tenth of the prey's biomass becomes predator biomass",
        ],
        "correct_index": 3,
        "why": "Efficiency is about mass, not headcount: a predator may eat most "
               "of a prey population and still build only a tenth of its mass.",
    },
    {
        "id": "ks4-transfer-of-biomass-h10",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two herbivores of equal mass eat the same grass, but the cow "
                "transfers more of it into tissue than the horse does. Suggest "
                "an explanation.",
        "options": [
            "Its gut microorganisms digest more of the cellulose, so less is egested",
            "A cow respires less, because it has a slower heart rate than a horse",
            "A horse moves a great deal more, so a greater share of its food leaves as faeces",
            "A cow's stomach is larger, so it can hold more grass at any one time",
        ],
        "correct_index": 0,
        "why": "A ruminant's four-chambered stomach houses microorganisms that "
               "break cellulose down, recovering biomass a horse egests.",
    },
    {
        "id": "ks4-transfer-of-biomass-h11",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farm uses 120 000 kg of feed and the herd gains 7200 kg. "
                "Determine the efficiency, and the feed that would be needed to "
                "double the mass gained.",
        "options": [
            "6%, and 120 000 kg of feed",
            "6%, and 240 000 kg of feed",
            "16.7%, and 240 000 kg of feed instead",
            "6%, and 480 000 kg of feed",
        ],
        "correct_index": 1,
        "why": "(7200 ÷ 120 000) × 100 = 6%, and at the same efficiency "
               "twice the gain needs twice the feed.",
    },
    {
        "id": "ks4-transfer-of-biomass-h12",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student calculates an efficiency using the wet mass of the "
                "prey and the dry mass of the predator. Explain the effect on "
                "the answer.",
        "options": [
            "Both errors cancel out, so the efficiency is about right",
            "The efficiency reads high, because dry mass is always the larger",
            "The predator's figure is too small beside the prey's, so efficiency reads low",
            "The efficiency is unaffected — both masses change alike",
        ],
        "correct_index": 2,
        "why": "Drying removes most of an organism's mass, so dividing a dried "
               "predator by an undried prey understates the transfer badly.",
    },
    {
        "id": "ks4-transfer-of-biomass-h13",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Producers hold 50 000 g/m². The first transfer is 12% "
                "efficient and the second is half as efficient as the first. "
                "Determine the biomass at trophic level 3.",
        "options": [
            "720 g/m²",
            "3000 g/m²",
            "36 g/m²",
            "360 g/m²",
        ],
        "correct_index": 3,
        "why": "50 000 × 0.12 = 6000 g/m², and 6% of 6000 is "
               "360 g/m².",
    },
    {
        "id": "ks4-transfer-of-biomass-h14",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the food biomass a person gains from 1000 kg of soya "
                "eaten directly with the biomass gained if the soya is fed to "
                "salmon that transfer 30% of it.",
        "options": [
            "1000 kg directly against 300 kg through the salmon",
            "1000 kg directly against 700 kg through the salmon",
            "300 kg directly against 1000 kg through the salmon",
            "Both routes give 300 kg, because the soya is the same in each",
        ],
        "correct_index": 0,
        "why": "Eating the soya keeps all 1000 kg as human food, whereas the "
               "extra transfer through the salmon leaves only 300 kg.",
    },
    {
        "id": "ks4-transfer-of-biomass-h15",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a long food chain is more vulnerable to a fall in "
                "producer biomass than a short one is.",
        "options": [
            "A long chain has more organisms, so a greater number of them starve",
            "Each transfer multiplies the loss, so a small fall at level 1 is magnified",
            "The top of a long chain is furthest from the Sun, so it is the one that warms least",
            "A long chain holds more biomass in total, so it loses more of it",
        ],
        "correct_index": 1,
        "why": "The top of a five-level chain receives a fixed fraction of level "
               "1, so a 20% fall there removes 20% of an already tiny amount.",
    },
    {
        "id": "ks4-transfer-of-biomass-h16",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Better housing raises the efficiency of transfer into a herd "
                "from 6% to 7.5%. Determine the percentage increase in the beef "
                "produced from the same feed.",
        "options": [
            "1.5%",
            "125%",
            "25%",
            "20%",
        ],
        "correct_index": 2,
        "why": "The rise is 1.5 percentage points on a starting figure of 6, and "
               "(1.5 ÷ 6) × 100 = 25%.",
    },
    {
        "id": "ks4-transfer-of-biomass-h17",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the usefulness of the one-tenth transfer figure to a "
                "farmer deciding how much feed to buy for a season.",
        "options": [
            "Fully reliable, because every animal transfers about a tenth of its feed",
            "Useless, because farm animals do not transfer biomass as wild ones do",
            "Reliable for cattle alone, because the figure was first measured on grazing herds",
            "Too rough — the herd's own figure must be measured, as it may be half that",
        ],
        "correct_index": 3,
        "why": "Real herds record 4% to 8%, so buying feed on a tenth "
               "would leave a farmer well short of the mass expected.",
    },
    {
        "id": "ks4-transfer-of-biomass-h18",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why measuring the biomass transferred between two wild "
                "trophic levels is far harder than measuring it on a farm.",
        "options": [
            "Neither the food eaten nor the tissue gained can be weighed in the wild",
            "Wild animals respire a great deal faster, so their biomass changes as they are weighed",
            "Wild biomass is recorded in joules, which cannot be compared with grams",
            "Wild chains have no fixed number of levels, so no transfer can be defined",
        ],
        "correct_index": 0,
        "why": "A farm records every kilogram of feed in and every kilogram of "
               "mass gained; in the wild both figures have to be estimated.",
    },

    # ══ standard/harder · s19-s26, h19-h26 (MRB-338 night 3 top-up) ══
    {
        "id": "ks4-transfer-of-biomass-s19",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A trophic level loses biomass in the usual three ways: 65% to "
                "respiration, 22% to egestion, and the rest to excretion. Calculate "
                "the percentage lost to excretion.",
        "options": [
            "35%, from adding the two given percentages and subtracting the total from 100",
            "43%, from mistakenly treating egestion as the largest share instead of respiration",
            "13%, from subtracting 65% and 22% from the total of 100%",
            "87%, from adding the respiration and egestion percentages together directly",
        ],
        "correct_index": 2,
        "why": "100% minus 65% minus 22% leaves 13% lost to excretion.",
    },
    {
        "id": "ks4-transfer-of-biomass-s20",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pig converts 20% of its feed into body mass and a chicken converts "
                "30% of its feed into body mass. Both animals are fed 100 kg of feed "
                "each. Calculate the total biomass gained by the pig and the chicken "
                "combined.",
        "options": [
            "20 kg, counting only the pig's own share of the total feed given to both animals",
            "60 kg, from adding both efficiency percentages to the total feed given to one animal",
            "30 kg, counting only the chicken's own share of the total feed given to both animals",
            "50 kg, from 20 kg gained by the pig plus 30 kg gained by the chicken",
        ],
        "correct_index": 3,
        "why": "20 kg from the pig plus 30 kg from the chicken gives a combined "
               "total of 50 kg.",
    },
    {
        "id": "ks4-transfer-of-biomass-s21",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two sheep of the same size are kept outdoors through winter. One has "
                "a thick fleece and one has just been sheared. Suggest which sheep is "
                "likely to show the more efficient transfer of feed into body mass, "
                "and why.",
        "options": [
            "The sheared sheep, because a lighter animal always converts feed into mass more efficiently",
            "The fleeced sheep, because its fleece cuts heat loss, leaving more energy free for growth rather than warmth",
            "Neither sheep, because fleece has no measurable effect on how a sheep actually uses the energy in its feed",
            "The sheared sheep, because clipped wool regrows using biomass that would otherwise be lost as heat",
        ],
        "correct_index": 1,
        "why": "A fleece cuts heat loss, so less energy is needed to keep the sheep "
               "warm and more is left free for growth.",
    },
    {
        "id": "ks4-transfer-of-biomass-s22",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two pigs are fed the same mass of feed. Pig A's feed is a highly "
                "digestible processed pellet and pig B's feed is unprocessed raw "
                "grain. Suggest which pig is likely to show the higher transfer "
                "efficiency, and why.",
        "options": [
            "Pig A, since a more digestible pellet leaves less undigested material to be lost as faeces",
            "Pig B, since raw grain provides a richer source of energy than any processed pellet can",
            "Neither pig, since digestibility only changes how quickly feed is eaten, not how much is absorbed",
            "Pig B, since unprocessed grain is always closer to a pig's natural diet and so suits it better",
        ],
        "correct_index": 0,
        "why": "A more digestible feed is absorbed more completely, leaving less "
               "undigested material lost as faeces.",
    },
    {
        "id": "ks4-transfer-of-biomass-s23",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A goat eats 40 kg of feed and gains 3.2 kg of body mass. Of the "
                "biomass that was NOT converted into body mass, 70% is lost to "
                "respiration. Calculate the mass lost to respiration.",
        "options": [
            "36.8 kg, the mass of feed that was not converted into the goat's own body mass",
            "2.24 kg, from taking 70% of the goat's 3.2 kg gain rather than of the unconverted mass",
            "28 kg, from taking 70% of the full 40 kg of feed rather than of the unconverted mass",
            "25.76 kg, from taking 70% of the 36.8 kg of feed that was not converted into body mass",
        ],
        "correct_index": 3,
        "why": "40 kg minus 3.2 kg leaves 36.8 kg not converted into body mass, and "
               "70% of that is 25.76 kg.",
    },
    {
        "id": "ks4-transfer-of-biomass-s24",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the transfer efficiency you would expect from a young salmon "
                "that is still growing quickly with that of a fully mature salmon of "
                "the same species.",
        "options": [
            "Efficiency is identical at every stage, because a salmon's biology never changes at any stage throughout its life",
            "A mature salmon converts feed more efficiently, because its larger gut can hold and process much more food at once",
            "A young salmon typically converts feed more efficiently, because more of its energy goes into growth rather than maintenance",
            "A mature salmon converts feed more efficiently, because it needs far less energy for active swimming than a much younger fish does",
        ],
        "correct_index": 2,
        "why": "A young, still-growing salmon puts more of its energy into growth "
               "and less into simply maintaining its body, giving it the higher "
               "transfer efficiency.",
    },
    {
        "id": "ks4-transfer-of-biomass-s25",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student calculates a transfer efficiency of 250% for one trophic "
                "transfer. Identify the likely error in the calculation.",
        "options": [
            "The student divided the current level's biomass by the next level's, giving a result above 100%",
            "The student forgot to convert both biomass figures into the same units before dividing",
            "The student used the correct method, and an efficiency close to 100% is entirely normal",
            "The student added the two biomass figures together instead of finding a ratio between them",
        ],
        "correct_index": 0,
        "why": "An efficiency above 100% is impossible, since a predator cannot gain "
               "more biomass than its prey provided; the biomass figures were most "
               "likely divided the wrong way round.",
    },
    {
        "id": "ks4-transfer-of-biomass-s26",
        "subtopic_slug": "transfer-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Farmed mussels convert the feed they filter from the water into body "
                "mass with unusually high efficiency. Explain why mussels achieve "
                "this.",
        "options": [
            "Mussels convert feed efficiently mainly because filtering plankton straight from the water needs almost no active hunting",
            "Mussels convert feed efficiently because they barely move, are supported by water and do not spend energy staying warm at all",
            "Mussels convert feed inefficiently, since filter feeding wastes most of the plankton that passes over the gills",
            "Mussels convert feed efficiently only because farmed mussels are given a specially concentrated feed pellet",
        ],
        "correct_index": 1,
        "why": "A mussel barely moves, is held up by the water around it and, being "
               "cold-blooded, spends none of its energy keeping warm, so very little "
               "feed energy is lost before it becomes body mass.",
    },
    {
        "id": "ks4-transfer-of-biomass-h19",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fish farm converts feed into fish biomass at 22% efficiency. A "
                "chicken farm converts feed into chicken biomass at 12% efficiency. "
                "Both need to produce 300 kg of extra biomass. Determine how much "
                "less feed the fish farm needs than the chicken farm, to the nearest "
                "kg.",
        "options": [
            "The fish farm needs 100 kg less feed, from a flat difference between the two given percentages",
            "The fish farm needs 250 kg more feed, from dividing 300 kg by the difference between the percentages",
            "The two farms need the same amount of feed, since both are producing the same 300 kg of new biomass",
            "The fish farm needs roughly 1136 kg less feed, from comparing 300 kg ÷ 0.22 with 300 kg ÷ 0.12",
        ],
        "correct_index": 3,
        "why": "300 kg divided by 0.22 is about 1 364 kg for the fish farm, and 300 "
               "kg divided by 0.12 is 2 500 kg for the chicken farm, a difference of "
               "roughly 1 136 kg.",
    },
    {
        "id": "ks4-transfer-of-biomass-h20",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wetland's producers fix 40 000 kJ/m²/year. Energy is transferred "
                "through three steps: 12%, then 8% of that, then 15% of that. "
                "Determine the energy reaching the final trophic level.",
        "options": [
            "4 800 kJ/m²/year, from applying only the first transfer efficiency to the producers' energy",
            "384 kJ/m²/year, from stopping after only the first two of the three given transfers",
            "14 000 kJ/m²/year, from adding the three percentages together and applying that as one 35% transfer",
            "57.6 kJ/m²/year, from 40 000 kJ/m²/year falling in turn through 12%, then 8%, then 15%",
        ],
        "correct_index": 3,
        "why": "40 000 kJ/m²/year falls to 4 800 at 12%, then to 384 at 8% of "
               "that, then to 57.6 at 15% of that — the value after all three "
               "transfers, not just the first two.",
    },
    {
        "id": "ks4-transfer-of-biomass-h21",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A feed company advertises a new formula that gives '100% transfer "
                "efficiency' from feed into farmed animal biomass. Evaluate this "
                "claim.",
        "options": [
            "It is impossible, because every living organism loses some energy to respiration, so some biomass is always lost",
            "It is entirely possible for a genetically improved breed with an unusually efficient digestive system and diet",
            "It is impossible only because farms are never able to measure feed and growth precisely enough",
            "It is possible in theory, but has simply never yet been achieved by any farmed species",
        ],
        "correct_index": 0,
        "why": "Every living organism loses some energy to respiration, so some "
               "biomass is always lost; a true 100% transfer is not physically "
               "possible.",
    },
    {
        "id": "ks4-transfer-of-biomass-h22",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Cattle convert 4% of their feed into body mass, and farmed mussels "
                "convert 35% of their feed into body mass. Both are given 90 kg of "
                "feed. Determine how much more biomass the mussels gain than the "
                "cattle.",
        "options": [
            "The two animals gain the same amount of biomass, since both are given exactly the same mass of feed",
            "The cattle gain roughly 28 kg more biomass than the mussels do, from the two given percentages",
            "The mussels gain roughly 28 kg more biomass than the cattle do, from 35% against 4% of the same feed mass",
            "The difference cannot be found, because mussels and cattle cannot be compared using the same feed mass",
        ],
        "correct_index": 2,
        "why": "Cattle gain 3.6 kg from 90 kg of feed and mussels gain 31.5 kg, a "
               "difference of roughly 27.9 kg in the mussels' favour.",
    },
    {
        "id": "ks4-transfer-of-biomass-h23",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A trophic transfer works at an overall efficiency of 14%, and the "
                "final trophic level ends up with 70 kg of biomass. Determine the "
                "mass of feed that must have been consumed at the level below to "
                "produce this.",
        "options": [
            "The feed mass cannot be recovered from this information, since respiration and egestion are unrelated figures",
            "182 kg, from applying the respiration proportion directly to the final biomass without reversing the transfer",
            "700 kg, from dividing the final biomass by the respiration proportion instead of by the overall efficiency",
            "500 kg, from reversing the 14% overall efficiency to recover the feed mass behind a 70 kg gain in biomass",
        ],
        "correct_index": 3,
        "why": "70 kg is 14% of the original feed mass, so the feed mass is 70 "
               "divided by 0.14, which is 500 kg.",
    },
    {
        "id": "ks4-transfer-of-biomass-h24",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Goats eat 5 000 kg of feed and convert 12% of it into their own body "
                "mass. A predator then eats the goats and converts 15% of the goats' "
                "biomass into its own body mass. Determine the predator's final "
                "biomass gain.",
        "options": [
            "1 250 kg, from applying only the first of the two given transfer efficiencies to the goats' own feed supply",
            "90 kg, from a 12% transfer from 5 000 kg of feed into goats, then a 15% transfer from the goats into the predator",
            "600 kg, from applying the predator's transfer efficiency directly to the original 5 000 kg of feed",
            "750 kg, from adding the two given transfer percentages together before applying them once",
        ],
        "correct_index": 1,
        "why": "5 000 kg of feed gives the goats 600 kg of biomass at 12%, and 15% "
               "of that 600 kg gives the predator 90 kg.",
    },
    {
        "id": "ks4-transfer-of-biomass-h25",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer begins selectively breeding cattle for a more efficient "
                "digestive system, alongside the existing housing and feed already "
                "used to raise transfer efficiency. Evaluate the likely effect of "
                "this new breeding programme on the farm's overall transfer "
                "efficiency.",
        "options": [
            "It would make little difference, because feed-conversion efficiency is fixed and cannot be inherited",
            "It would only ever affect an animal's final size, not how much of its feed becomes biomass",
            "It would raise costs without any real benefit, since a more efficient breed still eats the same total mass of feed",
            "It could raise the farm's overall transfer efficiency, since the trait for efficient feed conversion can be passed to offspring",
        ],
        "correct_index": 3,
        "why": "Breeding for a more efficient digestive system adds a genetic route "
               "to raising efficiency on top of housing and feed, and that trait can "
               "be passed on to the next generation.",
    },
    {
        "id": "ks4-transfer-of-biomass-h26",
        "subtopic_slug": "transfer-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A predator's final biomass is 360 kg, produced from goats it ate at "
                "an overall transfer efficiency of 12%. Determine the original "
                "biomass of the goats' own feed that this chain ultimately depended "
                "on.",
        "options": [
            "3 000 kg, from reversing the 12% transfer efficiency behind the goats' final 360 kg of biomass",
            "43.2 kg, from applying the 12% efficiency to the goats' final biomass a second time",
            "360 kg, treating the goats' own final biomass as though it were the producers' original figure",
            "30 kg, from dividing the goats' final biomass by 12 rather than reversing a percentage",
        ],
        "correct_index": 0,
        "why": "360 kg is 12% of the feed mass behind the whole chain, so the feed "
               "mass is 360 divided by 0.12, which is 3 000 kg.",
    },
]
