"""Biology · Ecology — the MRB-338 expansion of `farming-techniques`.

One leaf only: AQA 8461 §4.7.5.2, Biology-only. The original twelve rows in
`ecology__b.py` take pesticide against herbicide, what a greenhouse controls,
monoculture by definition, high-protein feed, the antibiotic-resistance
restriction, fertiliser run-off, why biological control never clears a pest,
why a farmer may reach for a spray instead, an introduced beetle evaluated,
organic against intensive, insecticide reaching pollinators, and wheat from
hedge to hedge.

This file takes what they leave, and the first thing it takes is the spec
point's own centre, which the baseline never asks at all: efficiency is raised
by reducing the ENERGY LOST FROM the animal — movement and warmth — not by
some other route. That is the named misconception for this subtopic, and four
rows here approach it from four sides. Around it sit the named biological
control agents (ladybirds, Bacillus thuringiensis, parasitic wasps, sterile
males), NPK, the greenhouse's extended season, and the ethical and
environmental costs the specification asks pupils to weigh rather than list.

The weight is even at fourteen a band: this is a Triple-only spec point where
even the recall is a named example a pupil must be able to place.

⚠️ Trophic efficiency arithmetic belongs to `transfer-of-biomass`, and what
threatens a country's food supply to `factors-affecting-food-security`. This
leaf stays on the TECHNIQUES and what they cost.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # The energy argument, the named agents of biological control, NPK, and
    # the named welfare concerns.
    {
        "id": "ks4-farming-techniques-e05",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why restricting a farm animal's movement increases the "
                "mass of meat produced.",
        "options": [
            "The animal's muscles swell because they are not being used",
            "Standing still makes an animal's bones grow heavier over the "
                "months",
            "Less energy is used in respiration, so more is stored as "
                "biomass",
            "The animal is forced to eat a great deal more food than it "
                "otherwise would",
        ],
        "correct_index": 2,
        "why": "Movement is powered by respiration, so an animal that moves "
               "less respires less of its food and retains more of it as body "
               "mass.",
    },
    {
        "id": "ks4-farming-techniques-e06",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why farm animals are kept in a heated building in "
                "winter.",
        "options": [
            "Less energy is spent keeping warm, so more goes into growth",
            "Warm animals drink less water, which lowers the farm's costs",
            "Heat kills the bacteria on the animals' skin and in their gut",
            "Warmth makes the animals sleep, and the sleeping animals eat "
                "much more",
        ],
        "correct_index": 0,
        "why": "Maintaining body temperature costs energy from food; supply "
               "the warmth and that energy is available for growth instead.",
    },
    {
        "id": "ks4-farming-techniques-e07",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the three mineral elements supplied by an NPK "
                "fertiliser.",
        "options": [
            "Nitrogen, platinum and potassium",
            "Nickel, phosphorus and potassium",
            "Nitrogen, phosphorus and palladium",
            "Nitrogen, phosphorus and potassium",
        ],
        "correct_index": 3,
        "why": "N, P and K are the three elements crops need in the largest "
               "quantities, and a compound fertiliser supplies all three.",
    },
    {
        "id": "ks4-farming-techniques-e08",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the insect released into a greenhouse to control aphids.",
        "options": [
            "The mayfly",
            "The ladybird",
            "The honey bee",
            "The dragonfly",
        ],
        "correct_index": 1,
        "why": "Ladybirds and lacewings are the standard biological control "
               "agents for aphids, because both adults and larvae eat them.",
    },
    {
        "id": "ks4-farming-techniques-e09",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the bacterium whose toxin is used to kill caterpillars "
                "on a crop.",
        "options": [
            "Bacillus thuringiensis",
            "Escherichia coli",
            "Lactobacillus bulgaricus",
            "Salmonella enterica",
        ],
        "correct_index": 0,
        "why": "Bacillus thuringiensis produces a protein toxic to "
               "caterpillars but harmless to most other organisms, which is "
               "why it is used in both sprays and GM crops.",
    },
    {
        "id": "ks4-farming-techniques-e10",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by biological control.",
        "options": [
            "Spraying a chemical made from a plant rather than from crude "
                "oil",
            "Breeding a crop that grows faster than any of its pests can "
                "eat",
            "Removing all the pests from a crop by hand rather than by "
                "using a machine",
            "Using a natural predator or parasite to reduce a pest's "
                "numbers",
        ],
        "correct_index": 3,
        "why": "Biological control uses a living organism — a predator, a "
               "parasite or a pathogen — in place of a chemical pesticide.",
    },
    {
        "id": "ks4-farming-techniques-e11",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one welfare objection raised against keeping laying "
                "hens in small cages.",
        "options": [
            "They are kept in the dark for the whole of the day and night",
            "They cannot spread their wings or behave naturally",
            "They lay eggs that are much smaller than usual",
            "They are fed a diet made entirely of dried grass seed",
        ],
        "correct_index": 1,
        "why": "The objection is to the restriction itself: a caged hen cannot "
               "stretch, dust-bathe, perch or nest, which are its natural "
               "behaviours.",
    },
    {
        "id": "ks4-farming-techniques-e12",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one thing an organic farm does not use.",
        "options": [
            "Crop rotation",
            "Hand weeding",
            "Artificial fertiliser",
            "Animal manure",
        ],
        "correct_index": 2,
        "why": "Organic systems exclude artificial fertilisers, most "
               "pesticides and routine antibiotics, relying on manure, "
               "rotation and mechanical weeding instead.",
    },
    {
        "id": "ks4-farming-techniques-e13",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the process by which fertiliser washed into a river "
                "causes the fish to die.",
        "options": [
            "Transpiration",
            "Photosynthesis",
            "Sedimentation",
            "Eutrophication",
        ],
        "correct_index": 3,
        "why": "Nutrient enrichment causes an algal bloom, and the decomposers "
               "that break the dead algae down strip the oxygen from the "
               "water.",
    },
    {
        "id": "ks4-farming-techniques-e14",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one advantage of biological control over a chemical "
                "pesticide.",
        "options": [
            "It works equally well against the weeds and against all of "
                "the insects",
            "It leaves no chemical residue on the crop that is harvested",
            "It clears the pest from the whole crop within just a single "
                "day",
            "It kills every insect species present in the field",
        ],
        "correct_index": 1,
        "why": "No residue, specificity to the target pest, and no pesticide "
               "resistance developing are the three advantages the "
               "specification names.",
    },
    {
        "id": "ks4-farming-techniques-e15",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one reason a greenhouse raises a grower's yield over a "
                "whole year.",
        "options": [
            "It stops the crop from respiring during the night",
            "It allows the crop to grow without any mineral ions",
            "It extends the growing season beyond the outdoor one",
            "It removes the need for the crop to be watered during the "
                "season",
        ],
        "correct_index": 2,
        "why": "Controlled warmth and light let a crop be grown earlier and "
               "later than the outdoor season allows, so more crops are taken "
               "from the same ground.",
    },
    {
        "id": "ks4-farming-techniques-e16",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the technique in which sterile male insects are released "
                "to reduce a pest population.",
        "options": [
            "The sterile insect technique",
            "The selective breeding technique used on insects",
            "The tissue culture technique",
            "The crop rotation technique",
        ],
        "correct_index": 0,
        "why": "Females that mate with a sterile male produce no offspring, so "
               "releasing enough sterile males makes the next generation much "
               "smaller.",
    },
    {
        "id": "ks4-farming-techniques-e17",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one drawback a grower accepts when choosing ladybirds "
                "instead of an aphid spray.",
        "options": [
            "It can be used on a greenhouse crop but not an outdoor one",
            "It acts more slowly, because the predator's numbers must "
                "build up",
            "It leaves a residue on the crop that has to be washed off",
            "It causes the pest to become resistant within one season",
        ],
        "correct_index": 1,
        "why": "Biological control is slower and less predictable than a "
               "spray, is not available for every pest, and an introduced "
               "agent can itself become a problem.",
    },
    {
        "id": "ks4-farming-techniques-e18",
        "subtopic_slug": "farming-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the gas a grower adds to a greenhouse to raise the rate "
                "of photosynthesis.",
        "options": [
            "Helium",
            "Methane",
            "Carbon dioxide",
            "Nitrogen",
        ],
        "correct_index": 2,
        "why": "Carbon dioxide is often the limiting factor in an enclosed "
               "greenhouse, so enriching the air raises the rate of "
               "photosynthesis and the yield.",
    },
    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # The energy argument applied, the named agents in context, and the
    # environmental costs traced to their mechanism.
    {
        "id": "ks4-farming-techniques-s05",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a pig kept indoors reaches slaughter weight "
                "sooner than one kept in an outdoor field.",
        "options": [
            "Indoor pigs absorb heat through their skin and so need to eat "
                "much less food",
            "Indoor pigs digest their food twice over, which takes twice "
                "as much energy from it",
            "It uses less energy on moving and on keeping warm, so more "
                "goes into growth",
            "It is given a completely different type of food from the pig "
                "kept outdoors",
        ],
        "correct_index": 2,
        "why": "Movement and thermoregulation are both paid for by "
               "respiration; removing both costs leaves a greater share of the "
               "food's energy available for building tissue.",
    },
    {
        "id": "ks4-farming-techniques-s06",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why keeping animals at high density makes disease "
                "spread quickly between them.",
        "options": [
            "Animals are close together, so a pathogen passes easily from "
                "one to the next",
            "Crowded animals stop producing antibodies while they are "
                "indoors",
            "High density lowers the temperature, and cold animals catch "
                "disease",
            "Crowded animals eat more, and more food weakens the immune "
                "system",
        ],
        "correct_index": 0,
        "why": "Transmission depends on contact, so packing animals together "
               "raises the number of contacts each animal has and the speed an "
               "outbreak spreads.",
    },
    {
        "id": "ks4-farming-techniques-s07",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why giving antibiotics to healthy animals used to "
                "make them grow faster.",
        "options": [
            "The antibiotics were digested and absorbed as an extra source "
                "of protein",
            "Antibiotics killed the gut bacteria that had been digesting "
                "all the animals' food",
            "The drugs raised the animals' body temperature, which speeded "
                "up growth",
            "Less energy went into fighting infection, so more went into "
                "growth",
        ],
        "correct_index": 3,
        "why": "An immune response is metabolically expensive; preventing "
               "low-level infection left more of the food's energy for "
               "building biomass.",
    },
    {
        "id": "ks4-farming-techniques-s08",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A parasitic wasp is released into a tomato greenhouse to "
                "control whitefly. Explain why this suits a greenhouse better "
                "than an open field.",
        "options": [
            "Open fields are too cold for whitefly, so no control is "
                "needed there",
            "The wasps are contained, so they stay with the pest they were "
                "released for",
            "Wasps are unable to fly once they have been released outdoors",
            "Greenhouse whitefly are a great deal larger, so the wasps can "
                "find them more easily",
        ],
        "correct_index": 1,
        "why": "An enclosed space keeps the control agent where the pest is "
               "and stops it dispersing, which is why glasshouse crops are "
               "where biological control works best.",
    },
    {
        "id": "ks4-farming-techniques-s09",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A field yields 6.5 tonnes of wheat per hectare and covers 24 "
                "hectares. Calculate the total yield.",
        "options": [
            "156 tonnes",
            "30.5 tonnes",
            "3.7 tonnes",
            "1560 tonnes",
        ],
        "correct_index": 0,
        "why": "6.5 tonnes per hectare × 24 hectares = 156 tonnes of wheat.",
    },
    {
        "id": "ks4-farming-techniques-s10",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a herbicide raises a crop's yield without killing "
                "any pest insects.",
        "options": [
            "It kills the insects' eggs, which are laid on the weeds",
            "It adds nitrogen to the soil as the dead weeds break down",
            "It makes the crop's leaves grow much larger than usual",
            "It removes the weeds competing with the crop for light and "
                "minerals",
        ],
        "correct_index": 3,
        "why": "Weeds take light, water and mineral ions the crop would "
               "otherwise have, so removing them raises the crop's growth "
               "without touching the insects.",
    },
    {
        "id": "ks4-farming-techniques-s11",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a single fungal disease can destroy a whole field "
                "of one potato variety.",
        "options": [
            "A fungus can infect a monoculture but not a mixed crop",
            "The plants are genetically identical, so none of them can "
                "resist it",
            "Potatoes grown together share a root system that carries the "
                "fungus around",
            "One variety of potato grows more slowly than a mixture of "
                "varieties",
        ],
        "correct_index": 1,
        "why": "A monoculture of one variety has no genetic variation, so a "
               "pathogen that defeats one plant defeats every plant in the "
               "field.",
    },
    {
        "id": "ks4-farming-techniques-s12",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fewer wild bird species are found on a farm that "
                "has replaced its hedges with wire fences.",
        "options": [
            "The birds are unable to see a wire fence and so they collide "
                "with it in flight",
            "Removing hedges raises the temperature of the whole farm "
                "quite sharply",
            "Hedges provided nesting sites, shelter and food that a fence "
                "does not",
            "Wire fences give off a metal dust that is toxic to nesting "
                "birds",
        ],
        "correct_index": 2,
        "why": "A hedge is a habitat in its own right — berries, insects, nest "
               "sites and cover — and a fence performs the same farming job "
               "while providing none of it.",
    },
    {
        "id": "ks4-farming-techniques-s13",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "1 kg of high-protein feed costs 40 pence and a pig eats 240 "
                "kg before slaughter. Calculate the feed cost per pig.",
        "options": [
            "9.60 pounds",
            "600 pounds",
            "60 pounds",
            "96 pounds",
        ],
        "correct_index": 3,
        "why": "240 kg × 40 p = 9600 p, and 9600 p ÷ 100 = 96 pounds per pig.",
    },
    {
        "id": "ks4-farming-techniques-s14",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a farmer rotates crops rather than growing wheat "
                "in the same field every year.",
        "options": [
            "Rotation means the field can be left unploughed for many "
                "years",
            "Rotation breaks pest and disease cycles and rests the soil's "
                "minerals",
            "Rotation lets the farmer use a much heavier machine on each "
                "of the same fields",
            "Rotation raises the temperature of the soil between the "
                "harvests",
        ],
        "correct_index": 1,
        "why": "Pests and pathogens specific to one crop build up in the soil "
               "when it is grown continuously, and different crops draw "
               "different minerals from the soil.",
    },
    {
        "id": "ks4-farming-techniques-s15",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an organic farm's produce usually costs the "
                "shopper more.",
        "options": [
            "Organic crops have to be stored for a year before they are "
                "sold",
            "Organic farms pay a tax that other farms do not pay",
            "Yields are lower and more labour is needed, so each kilogram "
                "costs more",
            "Organic produce is flown in, while other produce is not",
        ],
        "correct_index": 2,
        "why": "Without artificial fertiliser and most pesticides, yield per "
               "hectare falls and weeding and pest management take more work, "
               "so the cost per kilogram rises.",
    },
    {
        "id": "ks4-farming-techniques-s16",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a pesticide sprayed on a crop can reduce the "
                "number of insect-eating birds on the farm.",
        "options": [
            "It removes the insects the birds feed on, so their food "
                "supply falls",
            "It coats the birds' feathers and stops them being able to fly",
            "It is absorbed by the birds' feet as they walk on the sprayed "
                "crop leaves",
            "It makes the crop grow tall enough to keep every bird out of "
                "the whole field of it",
        ],
        "correct_index": 0,
        "why": "The spray works on the pest, but insect-eating birds depend on "
               "that same invertebrate supply, so the effect travels up the "
               "food chain.",
    },
    {
        "id": "ks4-farming-techniques-s17",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a grower would rather release a predator that "
                "eats one pest species than one that eats many.",
        "options": [
            "A specialist predator reproduces far faster than a generalist "
                "does",
            "A specialist predator leaves the crop's other insects "
                "untouched",
            "A specialist predator can be bought a great deal more cheaply "
                "than a generalist",
            "A generalist predator is unable to survive inside a "
                "greenhouse",
        ],
        "correct_index": 1,
        "why": "Specificity is the main advantage of biological control: a "
               "generalist would also eat the pollinators and the other "
               "beneficial insects.",
    },
    {
        "id": "ks4-farming-techniques-s18",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A greenhouse crop yields 18 kg per square metre and an "
                "outdoor crop 6 kg per square metre. Calculate how many times "
                "greater the greenhouse yield is.",
        "options": [
            "24 times",
            "0.33 times",
            "3 times",
            "12 times",
        ],
        "correct_index": 2,
        "why": "18 ÷ 6 = 3, so the greenhouse yields three times as much per "
               "square metre.",
    },
    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # The trade-offs weighed, not listed, and the arithmetic that decides
    # whether a technique is worth its cost.
    {
        "id": "ks4-farming-techniques-h05",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that restricting movement is justified "
                "because it feeds more people from the same land.",
        "options": [
            "The claim holds completely, because feeding people outweighs "
                "every other concern",
            "The claim fails, because animals that cannot move produce no "
                "usable meat",
            "The efficiency gain is real, but it is bought at a cost in "
                "animal welfare",
            "The claim fails, because restricting movement does not raise "
                "yield",
        ],
        "correct_index": 2,
        "why": "Both halves are true at once, which is exactly why the "
               "specification asks pupils to weigh the gain against the "
               "welfare cost rather than choose a side.",
    },
    {
        "id": "ks4-farming-techniques-h06",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why heating a shed is worth doing for chickens but "
                "not for a field of wheat.",
        "options": [
            "A chicken spends food energy keeping warm; a wheat plant does "
                "not",
            "Wheat grows in winter, so a heated field would make no "
                "difference",
            "Chickens are smaller than wheat plants, so they are cheaper "
                "to heat",
            "Wheat takes in all of its heat through its roots, so warming "
                "the air is useless",
        ],
        "correct_index": 0,
        "why": "Only an endotherm pays an energy cost to hold its body "
               "temperature, so only an endotherm's growth is improved by "
               "supplying that warmth.",
    },
    {
        "id": "ks4-farming-techniques-h07",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain the sequence by which routine antibiotic use in "
                "livestock leads to infections in people that are hard to "
                "treat.",
        "options": [
            "The antibiotic remains in the meat and destroys a person's "
                "gut bacteria",
            "People who eat treated meat become resistant to the "
                "antibiotic themselves",
            "The antibiotic makes the bacteria in a person's gut mutate "
                "once eaten",
            "Resistant bacteria are selected on the farm, then reach "
                "people through food or contact",
        ],
        "correct_index": 3,
        "why": "Constant exposure selects for resistant bacteria in the herd; "
               "those bacteria, or the resistance genes they carry, then move "
               "to bacteria that infect people.",
    },
    {
        "id": "ks4-farming-techniques-h08",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare a broad-spectrum insecticide with a Bacillus "
                "thuringiensis spray, for a cabbage crop attacked by "
                "caterpillars.",
        "options": [
            "The spray works more quickly than the insecticide and leaves "
                "a larger residue behind",
            "The spray kills caterpillars and spares bees; the insecticide "
                "kills both",
            "The spray kills every insect that is present, while the "
                "insecticide kills the caterpillars alone",
            "The two have identical effects, because both are applied to "
                "the crop as a liquid",
        ],
        "correct_index": 1,
        "why": "The bacterial toxin acts on caterpillars specifically, so "
               "pollinators and natural enemies survive; a broad-spectrum "
               "chemical does not distinguish between them.",
    },
    {
        "id": "ks4-farming-techniques-h09",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farm's yield rises from 5.0 to 6.2 tonnes per hectare when "
                "fertiliser is used. Determine the percentage increase.",
        "options": [
            "24%",
            "12%",
            "19%",
            "62%",
        ],
        "correct_index": 0,
        "why": "The rise is 6.2 − 5.0 = 1.2, and 1.2 ÷ 5.0 × 100 = 24%.",
    },
    {
        "id": "ks4-farming-techniques-h10",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict what happens to a pest population in the years after "
                "a farm switches from spraying to biological control.",
        "options": [
            "It is wiped out entirely within the first season of the "
                "change",
            "It rises without limit, because a predator cannot reduce a "
                "pest",
            "It stays exactly where it was, because control does nothing",
            "It falls to a low level and then fluctuates around it with "
                "the predator",
        ],
        "correct_index": 3,
        "why": "Predator and prey numbers oscillate around each other: the "
               "pest is held down but never removed, because the predator "
               "needs it to survive.",
    },
    {
        "id": "ks4-farming-techniques-h11",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why repeatedly spraying the same insecticide stops "
                "working after several seasons.",
        "options": [
            "The crop absorbs the insecticide and stops it reaching the "
                "insects",
            "Resistant individuals survive and breed, so the population "
                "becomes resistant",
            "The insecticide breaks down in the soil and cannot be used a "
                "second time",
            "Each insect that survives learns to avoid the spray and then "
                "teaches all of the others",
        ],
        "correct_index": 1,
        "why": "This is natural selection: variation for resistance already "
               "exists, the spray removes the susceptible individuals, and the "
               "survivors pass the resistance on.",
    },
    {
        "id": "ks4-farming-techniques-h12",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate a farmer's decision to leave a 6 metre wildflower "
                "strip along each field edge on an intensive arable farm.",
        "options": [
            "It is pointless, because the wildflowers compete with the "
                "crop for the minerals",
            "It removes the need for any fertiliser to be applied to the "
                "field",
            "It costs some cropped area, but supports pollinators and pest "
                "predators",
            "It costs nothing and raises the yield of every field on the "
                "farm",
        ],
        "correct_index": 2,
        "why": "The strip is land taken out of production, and it returns "
               "pollination and natural pest control — which is the trade-off "
               "a pupil is asked to weigh.",
    },
    {
        "id": "ks4-farming-techniques-h13",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A greenhouse costs 9000 pounds a year to heat and raises the "
                "crop's value by 15 000 pounds. Determine the net gain and one "
                "further cost to consider.",
        "options": [
            "24 000 pounds; the extra water the warmed crop will need",
            "6000 pounds; the wages that are saved by no longer having to "
                "weed the crop",
            "1.7 times; the greenhouse glass must all be replaced each "
                "year",
            "6000 pounds; the carbon dioxide released by burning the fuel",
        ],
        "correct_index": 3,
        "why": "15 000 − 9000 = 6000 pounds, but the heating burns fuel, so "
               "the environmental cost sits alongside the financial gain.",
    },
    {
        "id": "ks4-farming-techniques-h14",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an intensively farmed animal can be described as "
                "efficient and poorly treated at the same time.",
        "options": [
            "An efficient animal is well treated, so the description is a "
                "contradiction",
            "Efficiency measures food converted to meat; welfare measures "
                "how the animal lives",
            "The two words mean exactly the same thing, so one of the two "
                "descriptions must be wrong",
            "Efficiency is measured by the farmer and welfare by the "
                "animal itself",
        ],
        "correct_index": 1,
        "why": "They are measurements of different things, which is why a "
               "system can score highly on one and badly on the other and both "
               "statements be true.",
    },
    {
        "id": "ks4-farming-techniques-h15",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a biological control agent that worked in a "
                "greenhouse may fail when tried in an open field.",
        "options": [
            "Field pests are a different species, so the agent cannot "
                "recognise any of them",
            "An open field contains no pests of that kind, so the agent "
                "there has nothing to eat",
            "It disperses away, and the weather and native predators act "
                "on it outdoors",
            "It is unable to reproduce anywhere except inside a heated "
                "greenhouse",
        ],
        "correct_index": 2,
        "why": "A greenhouse holds the agent with the pest at a controlled "
               "temperature; outdoors it spreads out, is eaten and meets "
               "conditions it is not suited to.",
    },
    {
        "id": "ks4-farming-techniques-h16",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the environmental effect of spreading fertiliser in "
                "autumn with spreading it in spring, on a field beside a "
                "stream.",
        "options": [
            "Autumn spreading is worse, because winter rain washes nitrate "
                "into the stream before the crop uses it",
            "Spring spreading is worse, because crops absorb no nitrate "
                "during the spring months",
            "The two are identical, because the same mass of fertiliser is "
                "spread in either case",
            "Autumn spreading is better, because cold soil holds nitrate "
                "in place permanently",
        ],
        "correct_index": 0,
        "why": "Nitrate is soluble and the crop takes it up while growing; "
               "applied before a wet winter with no growing crop, most of it "
               "leaches straight into the water.",
    },
    {
        "id": "ks4-farming-techniques-h17",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate a supermarket's decision to stock only free-range "
                "eggs.",
        "options": [
            "It lowers the price of eggs, because free-range hens lay far "
                "more of them",
            "It improves hen welfare, but the eggs cost more and some "
                "shoppers cannot afford them",
            "It improves hen welfare at no cost, because free-range eggs "
                "are cheaper to produce than others",
            "It has no effect on welfare, because free-range hens are kept "
                "in the same cages",
        ],
        "correct_index": 1,
        "why": "The welfare gain is real and so is the price rise, and the "
               "people the price affects most are those with the least to "
               "spend on food.",
    },
    {
        "id": "ks4-farming-techniques-h18",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farm of 80 hectares yields 4.8 tonnes per hectare "
                "organically or 7.2 tonnes per hectare intensively. Determine "
                "the extra land organic farming would need to match the "
                "intensive total.",
        "options": [
            "120 hectares",
            "32 hectares",
            "40 hectares",
            "24 hectares",
        ],
        "correct_index": 2,
        "why": "Intensively the farm yields 80 × 7.2 = 576 tonnes; organically "
               "that needs 576 ÷ 4.8 = 120 hectares, which is 40 hectares more "
               "than 80.",
    },

    # ══ standard/harder · s19-s26, h19-h26 (MRB-338 night 3 top-up) ══
    {
        "id": "ks4-farming-techniques-s19",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer grows clover instead of wheat in one field every third "
                "year, as part of a crop rotation. Explain how this reduces how much "
                "nitrogen fertiliser the next wheat crop needs.",
        "options": [
            "Clover roots release nitrate directly into the air above the field, feeding the next crop through its leaves",
            "Clover crowds out weeds so thoroughly that the following crop needs far less herbicide that year",
            "Bacteria in clover roots fix nitrogen from the air into the soil, reducing the fertiliser the next crop needs",
            "Clover roots break up compacted soil, letting the next crop's roots grow deeper than they otherwise would",
        ],
        "correct_index": 2,
        "why": "Bacteria living in clover roots fix nitrogen gas from the air into "
               "the soil, so less nitrogen fertiliser has to be bought for the crop "
               "grown there next.",
    },
    {
        "id": "ks4-farming-techniques-s20",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Fertiliser costs 80 pence per kg and is applied at a rate of 250 kg "
                "per hectare to a 36-hectare field. Calculate the total cost of the "
                "fertiliser for the whole field.",
        "options": [
            "288 pounds, from applying the rate to just one hectare rather than the whole field",
            "9 000 pounds, from treating the rate in kg as though it were already a cost in pounds",
            "2 880 kg, the total mass of fertiliser needed, mistaken here for its cost",
            "7 200 pounds, from 9 000 kg of fertiliser across the field at 80 pence per kg",
        ],
        "correct_index": 3,
        "why": "250 kg per hectare across 36 hectares is 9 000 kg, and at 80 pence "
               "per kg that costs 7 200 pounds.",
    },
    {
        "id": "ks4-farming-techniques-s21",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a farm's costs may rise, at least at first, when routine "
                "antibiotic use in healthy livestock is stopped.",
        "options": [
            "Costs fall immediately, because a healthy flock typically needs less feed than one raised on routine antibiotics",
            "Costs may rise at first, since more animals can fall ill without routine antibiotics protecting the whole flock",
            "Costs stay exactly the same, since antibiotics were not really a meaningful part of a farm's running costs",
            "Costs fall immediately, because withdrawing antibiotics instantly removes any risk of disease on the farm",
        ],
        "correct_index": 1,
        "why": "Without routine antibiotics protecting the whole flock, more animals "
               "can fall ill, which can raise costs before the benefits of reduced "
               "antibiotic use are felt.",
    },
    {
        "id": "ks4-farming-techniques-s22",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a greenhouse grower's running costs include buying "
                "carbon dioxide gas, something an outdoor grower never has to pay "
                "for.",
        "options": [
            "Without extra carbon dioxide, photosynthesis inside the sealed greenhouse can become limited by its supply",
            "Carbon dioxide gas is added mainly to stop weeds from growing anywhere inside the greenhouse itself",
            "Carbon dioxide gas replaces the need for watering the crop for the rest of the growing season entirely",
            "Carbon dioxide gas is added mainly to keep pests such as whitefly and aphids away from the growing crop itself",
        ],
        "correct_index": 0,
        "why": "In a sealed greenhouse, carbon dioxide can otherwise become a "
               "limiting factor for photosynthesis, so adding more keeps growth from "
               "being held back.",
    },
    {
        "id": "ks4-farming-techniques-s23",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why keeping hens free-range does not automatically make them "
                "safer from disease than keeping them in intensive housing.",
        "options": [
            "Free-range hens face very little disease risk, since fresh air tends to keep a flock completely healthy",
            "Free-range hens can pick up diseases carried by wild birds that intensively housed hens rarely encounter",
            "Intensive housing removes every disease risk, since a sealed building keeps out all possible infection",
            "Disease risk is identical either way, since housing type makes no real difference to a flock's health",
        ],
        "correct_index": 1,
        "why": "Free-range hens mix with wild birds and can pick up diseases that "
               "intensively housed hens rarely meet, even though crowding brings its "
               "own separate risk.",
    },
    {
        "id": "ks4-farming-techniques-s24",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State two reasons, besides warmth, why keeping livestock indoors can "
                "make it easier for a farmer to control disease.",
        "options": [
            "Indoor animals need far less vaccination, since housing alone is widely said to remove most of the risk of infection",
            "Indoor animals eat less feed overall, which by itself is what keeps a flock free of disease",
            "Indoor animals grow to slaughter weight faster, which is why they catch fewer infections",
            "An enclosed building keeps out wild animals that could carry disease, and can be cleaned and disinfected easily",
        ],
        "correct_index": 3,
        "why": "An enclosed building keeps out wild animals that could carry "
               "disease, and its surfaces can be cleaned and disinfected far more "
               "easily than an open field.",
    },
    {
        "id": "ks4-farming-techniques-s25",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how rotating crops from one field to another each year helps "
                "to control a pest that lives in the soil and attacks only one type "
                "of crop.",
        "options": [
            "The new crop repels the pest directly with a smell the old crop simply did not produce",
            "The pest simply dies out completely over the winter months, regardless of which crop is grown there the following year",
            "Growing a different crop removes the pest's food source, so its numbers in the soil fall before it returns",
            "Rotating crops changes the soil's pH so sharply that the pest can no longer ever survive there",
        ],
        "correct_index": 2,
        "why": "Growing a different crop removes the pest's usual food source for a "
               "season, so its numbers in the soil fall before the original crop "
               "returns.",
    },
    {
        "id": "ks4-farming-techniques-s26",
        "subtopic_slug": "farming-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest one reason a consumer might be willing to pay more for free- "
                "range eggs despite the higher price.",
        "options": [
            "They may value the higher animal welfare standards that free-range hens are kept under",
            "Free-range eggs typically contain measurably more protein than eggs from caged hens",
            "Free-range eggs take far longer to spoil once bought than eggs from caged hens",
            "Free-range hens are the main hens permitted to be sold as eggs in the United Kingdom",
        ],
        "correct_index": 0,
        "why": "Some buyers are willing to pay more because they value the higher "
               "welfare standards free-range hens are kept under.",
    },
    {
        "id": "ks4-farming-techniques-h19",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Fertilising a 36-hectare field costs 2 880 pounds in total and "
                "raises the wheat yield by 2 tonnes per hectare across the whole "
                "field. Wheat sells for 180 pounds per tonne. Determine whether the "
                "fertiliser was a profitable investment, and by how much.",
        "options": [
            "It was not profitable, since the fertiliser cost more than the value of any extra wheat it produced",
            "It broke even exactly, since the cost of the fertiliser matched the value of the extra yield produced",
            "It was profitable, but just once the field's full 36 hectares are converted into a single tonne figure",
            "It was profitable by 10 080 pounds, once the extra 72 tonnes of wheat are sold at 180 pounds a tonne",
        ],
        "correct_index": 3,
        "why": "The extra 2 tonnes per hectare across 36 hectares is 72 tonnes, "
               "worth 12 960 pounds at 180 pounds a tonne, which is 10 080 pounds "
               "more than the 2 880 pounds spent on fertiliser.",
    },
    {
        "id": "ks4-farming-techniques-h20",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer is choosing between free-range and intensive housing for a "
                "new flock of hens, considering disease risk alone. Evaluate the "
                "claim that free-range housing is always the safer choice.",
        "options": [
            "The claim holds without exception, because free-range hens are widely said to be rarely exposed to any wild-bird disease whatsoever at all",
            "The claim oversimplifies; free-range hens meet wild-bird diseases intensive hens rarely face, while crowding brings its own separate disease risk",
            "The claim holds without exception, because crowding is said to be the main disease risk that matters on any farm",
            "The claim is meaningless, because disease risk cannot really be compared between the two housing systems",
        ],
        "correct_index": 1,
        "why": "Free-range hens face wild-bird diseases that intensive hens rarely "
               "meet, while intensive hens face their own separate risk from "
               "crowding, so neither system is safer without qualification.",
    },
    {
        "id": "ks4-farming-techniques-h21",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the long-term reliability of chemical pest control with "
                "biological control, given that a pest can evolve resistance to a "
                "chemical but rarely evolves resistance to being eaten by a natural "
                "predator.",
        "options": [
            "Neither method is reliable in the long term, since both pests and predators evolve resistance at the same rate",
            "Chemical control is the more reliable of the two, since a stronger chemical can typically be developed in time",
            "Biological control becomes steadily less reliable over time, since predators are widely said to eventually run out of pests to eat completely",
            "Biological control tends to stay reliable, since resistance to being eaten evolves far less readily than resistance to a chemical",
        ],
        "correct_index": 3,
        "why": "Resistance to being eaten by a predator evolves far less readily in "
               "a pest population than resistance to a chemical does, so biological "
               "control tends to stay effective for longer.",
    },
    {
        "id": "ks4-farming-techniques-h22",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Fertiliser A costs 60 pounds per hectare and raises yield by 1.2 "
                "tonnes per hectare. Fertiliser B costs 90 pounds per hectare and "
                "raises yield by 2.1 tonnes per hectare. Determine which fertiliser "
                "gives the farmer more extra yield per pound spent.",
        "options": [
            "Fertiliser A gives more extra yield per pound spent, at roughly 0.02 tonnes per pound against 0.0233",
            "Fertiliser B gives more extra yield per pound spent, at roughly 0.0233 tonnes per pound against 0.02",
            "Both fertilisers give exactly the same extra yield per pound spent, once the totals are compared fairly",
            "Fertiliser A gives more extra yield per pound spent, simply because it costs less per hectare overall",
        ],
        "correct_index": 1,
        "why": "Fertiliser A gives 1.2 divided by 60, about 0.02 tonnes per pound, "
               "while Fertiliser B gives 2.1 divided by 90, about 0.0233 tonnes per "
               "pound, so B gives more extra yield per pound spent.",
    },
    {
        "id": "ks4-farming-techniques-h23",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer who used to buy 4 tonnes of nitrogen fertiliser a year for "
                "a field switches to growing nitrogen-fixing clover in that field "
                "every third year instead. Evaluate the likely effect on the farmer's "
                "fertiliser costs over a three-year period, compared with buying "
                "fertiliser every year.",
        "options": [
            "Costs should fall over the three years, since one year needs little or no purchased nitrogen fertiliser",
            "Costs should rise over the three years, since clover itself is far more expensive to plant than fertiliser",
            "Costs should stay exactly the same, since clover fixes no more nitrogen than the field already contained",
            "Costs cannot really be judged, because clover and fertiliser affect completely different parts of a crop",
        ],
        "correct_index": 0,
        "why": "Fertiliser only has to be bought for two years out of every three "
               "once clover supplies the field's nitrogen naturally in the third "
               "year, so costs should fall over the cycle.",
    },
    {
        "id": "ks4-farming-techniques-h24",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A grower compares two seasons: one using biological control alone "
                "against aphids, and one using a chemical pesticide alone. In the "
                "biological-control season, some aphid damage is still visible on the "
                "crop; in the pesticide season, none is visible. Evaluate whether the "
                "pesticide season should be judged the more successful of the two.",
        "options": [
            "Yes, since a crop with any visible pest damage must be judged a market failure regardless of the cause",
            "Yes, since visible damage is the main factor a grower should consider when judging a season's success",
            "No, since biological control typically produces a higher yield than any chemical pesticide could",
            "Not necessarily; some visible damage may be an acceptable trade-off given the pesticide's costs and side effects",
        ],
        "correct_index": 3,
        "why": "Some visible damage under biological control can still be an "
               "acceptable outcome once the pesticide's costs and side effects, such "
               "as harm to useful insects, are weighed against a completely clean "
               "crop.",
    },
    {
        "id": "ks4-farming-techniques-h25",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Organic wheat yields 4.5 tonnes per hectare and sells for 220 pounds "
                "per tonne. Intensive wheat yields 7.5 tonnes per hectare and sells "
                "for 150 pounds per tonne. Determine which farming method gives the "
                "greater revenue per hectare, and by how much.",
        "options": [
            "Organic wheat gives the greater revenue per hectare, by roughly 135 pounds once both prices are applied",
            "Both methods give exactly the same revenue per hectare, since a higher price offsets a lower yield precisely here",
            "Intensive wheat gives the greater revenue per hectare, but just because organic wheat cannot legally be sold",
            "Intensive wheat gives the greater revenue per hectare, by roughly 135 pounds once both prices are applied",
        ],
        "correct_index": 3,
        "why": "Organic wheat gives 4.5 times 220, which is 990 pounds per hectare, "
               "and intensive wheat gives 7.5 times 150, which is 1 125 pounds per "
               "hectare, a difference of 135 pounds in intensive wheat's favour.",
    },
    {
        "id": "ks4-farming-techniques-h26",
        "subtopic_slug": "farming-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A large farm has grown wheat in monoculture on the same land for "
                "fifteen consecutive years without any rotation, relying entirely on "
                "fertiliser and pesticide to maintain yield. Evaluate the long-term "
                "sustainability of this approach.",
        "options": [
            "It is fully sustainable, since fertiliser and pesticide alone are widely said to replace most of the benefit that rotation provides",
            "It is fully sustainable, since a single crop grown for years eventually stops needing much fertiliser",
            "It is unlikely to be sustainable, since specific nutrients, soil-borne pests and rising input costs tend to build up over time",
            "Sustainability cannot be judged without first knowing the exact wheat variety the farm has chosen to grow",
        ],
        "correct_index": 2,
        "why": "Continuous monoculture tends to deplete specific soil nutrients, "
               "build up soil-borne pests and diseases suited to that one crop, and "
               "raise costs as more fertiliser and pesticide are needed to keep "
               "yield up.",
    },
]
