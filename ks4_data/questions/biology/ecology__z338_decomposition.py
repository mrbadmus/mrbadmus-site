"""Biology · Ecology — the MRB-338 expansion of `decomposition`.

One leaf only: AQA 8461 §4.7.2.1 and required practical 7. The original twelve
rows in `ecology__a.py` take extracellular digestion by name, the mineral ions
returned, salting and sugaring, pickling, the bog bodies, earthworms and
surface area, a waterlogged heap, a control variable in the milk experiment,
the rate curve that turns over at 40 degrees, a sealed bag against an open one,
ploughed-in stubble, and the 'plants make their own food' argument.

This file takes what they leave: which organisms decomposers actually are and
how they differ from detritivores, the full preservation set — refrigeration,
freezing, drying, vacuum packing — the applications the spec names in
composting, sewage treatment and biogas, and the practical skills the required
practical is built on: how a rate of decay is measured at all, why a water bath
and not a windowsill, repeats and a mean, and which measurement is the more
reliable. The misconception set is here in full: freezing imagined as killing
bacteria, drying imagined as stopping decay outright, a decomposer imagined as
eating the way an animal eats, lost mass imagined as having vanished, and more
decomposers imagined as the cure for an airless heap.

The weight follows the CONTENT. `easier` stays at eight because recall here is
a short list of organisms, gases and preservation methods, and a ninth way of
asking it is the same question in new words. The demand lives in the four
factors acting together on a real heap, soil or sample, and in arithmetic on
rates — decay is one of the few places at Foundation where a rate is a genuine
division with units. So `standard` and `harder` carry twenty-two each.

Numbers here are the ones the practical supplies: times to a fixed end point,
a pH falling as acids are produced, mass lost from leaf litter, and a
digester's yield scaled from one mass of waste to another.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # Which organisms decompose and which only shred, the four preservation
    # methods the spec names, the two gases, and why a heap is turned.
    {
        "id": "ks4-decomposition-e05",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two groups of microorganisms that act as "
                "decomposers.",
        "options": [
            "Bacteria and fungi",
            "Viruses and bacteria",
            "Fungi and protists",
            "Protists and viruses",
        ],
        "correct_index": 0,
        "why": "Decomposition is carried out by bacteria and fungi, which "
               "secrete enzymes onto dead material and absorb the products.",
    },
    {
        "id": "ks4-decomposition-e06",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Woodlice and millipedes feed on dead leaves and break them "
                "into smaller pieces. Name this group of organisms.",
        "options": [
            "Decomposers, because they release the enzymes that digest the "
                "dead leaves",
            "Producers, because they are the first organisms in the food "
                "chain of any woodland",
            "Detritivores",
            "Primary consumers, because dead leaves are plant material they "
                "feed on",
        ],
        "correct_index": 2,
        "why": "Detritivores feed on dead material and break it physically "
               "into smaller pieces, increasing the surface area available to "
               "decomposers.",
    },
    {
        "id": "ks4-decomposition-e07",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the effect of keeping food in a refrigerator on the "
                "rate of decay.",
        "options": [
            "It stops decay altogether, because no decomposer can live at a "
                "low temperature",
            "It slows decay down",
            "It speeds decay up, because decomposers prefer cool conditions",
            "It has no effect on decay, because decay depends on moisture "
                "rather than temperature",
        ],
        "correct_index": 1,
        "why": "A lower temperature slows the enzyme-controlled reactions in "
               "decomposers, so decay is slower but still happening.",
    },
    {
        "id": "ks4-decomposition-e08",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how drying food helps to preserve it.",
        "options": [
            "It raises the temperature of the food above the optimum for "
                "decomposer enzymes",
            "It removes the water that decomposers need in order to grow",
            "It removes the mineral ions that decomposers feed on as they "
                "break a food down into simpler substances",
            "It seals the surface of the food so that no decomposer can "
                "settle on it",
        ],
        "correct_index": 1,
        "why": "Decomposers need water to survive and to move dissolved "
               "substances, so removing it slows decay sharply.",
    },
    {
        "id": "ks4-decomposition-e09",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the factor that vacuum packing removes from around a "
                "food.",
        "options": [
            "Oxygen",
            "Water",
            "Warmth",
            "Acid",
        ],
        "correct_index": 0,
        "why": "Most decomposers respire aerobically, so removing the oxygen "
               "slows their respiration and therefore the decay.",
    },
    {
        "id": "ks4-decomposition-e10",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas released by decomposers respiring aerobically "
                "in a compost heap.",
        "options": [
            "Nitrogen",
            "Methane",
            "Hydrogen",
            "Carbon dioxide",
        ],
        "correct_index": 3,
        "why": "Aerobic respiration in decomposers releases carbon dioxide, "
               "which is why an active heap gives off that gas.",
    },
    {
        "id": "ks4-decomposition-e11",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas produced by some decomposers when there is no "
                "oxygen available.",
        "options": [
            "Methane",
            "Chlorine",
            "Sulfur dioxide",
            "Ammonia",
        ],
        "correct_index": 0,
        "why": "In anaerobic conditions some decomposers produce methane "
               "instead of carbon dioxide, which is what a biogas digester "
               "collects.",
    },
    {
        "id": "ks4-decomposition-e12",
        "subtopic_slug": "decomposition",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a gardener turns a compost heap over every few "
                "weeks.",
        "options": [
            "To cool the heap down, because decomposers are killed by the "
                "warmth they generate in it",
            "To mix in soil, which supplies the heap with the water its "
                "decomposers need",
            "To let air in, so the aerobic decomposers have the oxygen they "
                "need",
            "To break up the fungi, which would otherwise crowd out the "
                "bacteria in the heap",
        ],
        "correct_index": 2,
        "why": "Turning the heap brings fresh air into it, and aerobic "
               "decomposers work faster when oxygen is plentiful.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # The four factors on real heaps, soils and samples; the applications;
    # and the measurement skills behind the required practical.
    {
        "id": "ks4-decomposition-s05",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The middle of an active compost heap is noticeably warmer "
                "than the air around it. Explain where this warmth comes "
                "from.",
        "options": [
            "Sunlight is absorbed by the dark material and trapped inside "
                "the heap, which cannot lose it again",
            "Respiration in the decomposers releases energy, which warms the "
                "material around them",
            "The heap is insulated by its outer layer, so the ground beneath "
                "it warms the material above",
            "Water evaporating inside the heap releases energy, and that "
                "energy raises the temperature",
        ],
        "correct_index": 1,
        "why": "Decomposers respire as they break the material down, and "
               "respiration transfers energy to the surroundings, so the "
               "heap heats up.",
    },
    {
        "id": "ks4-decomposition-s06",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a decomposer must release its enzymes onto dead "
                "material rather than digesting it inside its cells.",
        "options": [
            "Its enzymes would be destroyed by the acid conditions that build "
                "up inside any living cell as it respires",
            "Enzymes work faster outside a cell, where they are not held back "
                "by the cell membrane",
            "The material is too large to be taken into the cell, so it must "
                "be digested where it lies",
            "Its cells have no membrane, so anything taken in would leak "
                "straight back out again",
        ],
        "correct_index": 2,
        "why": "Dead material is large and insoluble, so enzymes are secreted "
               "onto it and only the small soluble products are absorbed.",
    },
    {
        "id": "ks4-decomposition-s07",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cooked meal spoils in a few hours on a warm worktop but "
                "keeps for days in a fridge. Explain this difference.",
        "options": [
            "Fridges contain no decomposers, whereas a worktop carries large "
                "numbers of them on its surface",
            "A worktop is drier than a fridge, and dry conditions are what "
                "decomposers need",
            "Cold food holds its water more tightly, so the decomposers on "
                "it have nothing to dissolve",
            "Decomposer enzymes work slowly at a low temperature, so the "
                "cold food is broken down far more slowly",
        ],
        "correct_index": 3,
        "why": "Decay is enzyme-controlled, and enzyme reactions run more "
               "slowly at lower temperatures, so cold food keeps longer.",
    },
    {
        "id": "ks4-decomposition-s08",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Bread sealed in a plastic bag goes mouldy sooner than the "
                "same bread left in a paper bag. Suggest why.",
        "options": [
            "Plastic holds the moisture in, and mould needs water in order "
                "to grow",
            "Plastic is warmer than paper, so the bread inside it is held "
                "above room temperature",
            "Paper contains a preservative that passes into the crust of the "
                "bread and slows mould down",
            "Plastic supplies the mould with extra oxygen, which it needs for "
                "aerobic respiration",
        ],
        "correct_index": 0,
        "why": "A sealed plastic bag keeps water vapour in, and the damp "
               "conditions that follow suit the mould well.",
    },
    {
        "id": "ks4-decomposition-s09",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farmer spreads manure on a field instead of burning it. "
                "Explain the advantage for the soil.",
        "options": [
            "Burning would release all the mineral ions as gases, while "
                "spreading keeps them locked inside the manure for good",
            "Spreading warms the soil as the manure decays, and warm soil "
                "holds more mineral ions than cold soil",
            "Spreading kills the decomposers in the soil, so the mineral ions "
                "they hold are released into it",
            "Decomposers break the manure down and release mineral ions into "
                "the soil, where roots can absorb them",
        ],
        "correct_index": 3,
        "why": "Decomposers digest the manure and release nitrates and "
               "phosphates into the soil, which plant roots can then take "
               "up.",
    },
    {
        "id": "ks4-decomposition-s10",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compost made from kitchen waste is dug into a vegetable bed. "
                "Explain how this supplies the vegetables with nitrogen.",
        "options": [
            "The compost takes nitrogen gas out of the air and passes it "
                "straight into the roots of the vegetables",
            "Decomposers release nitrates from the compost, and the roots "
                "absorb those nitrates from the soil",
            "The compost holds nitrogen as a gas in the air spaces between "
                "its particles, which the root hair cells breathe in",
            "Nitrogen in compost dissolves in soil water as nitrogen gas and "
                "enters the plant through the xylem",
        ],
        "correct_index": 1,
        "why": "Decomposers break down the nitrogen-containing compounds in "
               "the compost and release nitrates, which roots absorb in "
               "solution.",
    },
    {
        "id": "ks4-decomposition-s11",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cool northern pine forest has a deep layer of dead "
                "needles on its floor. A warm wet tropical forest has almost "
                "none. Explain why.",
        "options": [
            "Pine needles are heavier than tropical leaves, so they sink down "
                "into the soil instead of lying on top of it",
            "Tropical trees drop far fewer leaves each year, so much less "
                "dead material ever reaches the forest floor",
            "Decay is faster in warm damp conditions, so dead material in "
                "the tropical forest is broken down quickly",
            "Tropical soils contain more mineral ions, and a soil rich in "
                "minerals dissolves dead leaves on contact",
        ],
        "correct_index": 2,
        "why": "Warmth and moisture both raise the rate of decay, so litter "
               "is broken down almost as fast as it falls in the tropics and "
               "accumulates in a cold forest.",
    },
    {
        "id": "ks4-decomposition-s12",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Air is bubbled through the tanks at a sewage treatment "
                "works. Explain why.",
        "options": [
            "To keep the sewage stirred, because decomposers cannot move "
                "through still liquid to reach their food",
            "To drive out the methane, which would otherwise poison the "
                "decomposers living in the tank",
            "To cool the sewage down, because the decomposers in it work best "
                "well below room temperature",
            "To supply oxygen, so that aerobic decomposers can respire and "
                "break the waste down quickly",
        ],
        "correct_index": 3,
        "why": "The works relies on aerobic decomposers, and they need a "
               "steady oxygen supply to respire and digest the organic waste "
               "fast.",
    },
    {
        "id": "ks4-decomposition-s13",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A biogas digester is kept tightly sealed while it is "
                "working. Explain why this is necessary.",
        "options": [
            "Sealing keeps oxygen out, so the decomposers work anaerobically "
                "and produce methane",
            "Sealing keeps the digester dry, and dry material gives a much "
                "larger yield of gas",
            "Sealing keeps light out, because the decomposers working inside "
                "a digester are killed by daylight",
            "Sealing keeps the pressure low, which is what forces the gas out "
                "of the waste inside",
        ],
        "correct_index": 0,
        "why": "Methane is produced by decomposers respiring anaerobically, "
               "so the digester must be sealed to exclude oxygen.",
    },
    {
        "id": "ks4-decomposition-s14",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Peas keep for a year in a freezer but for only a few days "
                "in a fridge. Explain the difference in terms of enzymes.",
        "options": [
            "A freezer denatures the decomposers' enzymes permanently, so "
                "they can never work again",
            "A freezer removes the water from the peas, and a fridge leaves "
                "all of that water in place",
            "A freezer is so cold that enzyme activity almost stops, while "
                "in a fridge it is merely slow",
            "A freezer kills each decomposer on the peas outright, while a "
                "fridge leaves them alive but inactive",
        ],
        "correct_index": 2,
        "why": "Enzyme activity falls as temperature falls, and at freezer "
               "temperatures it is so slow that decay is effectively "
               "halted.",
    },
    {
        "id": "ks4-decomposition-s15",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A compost heap has dried out in a hot summer and has "
                "stopped rotting. Explain why adding water restarts it.",
        "options": [
            "Water cools the heap, and decomposers cannot work at the "
                "temperature a dry heap reaches in summer",
            "Water washes the mineral ions out of the heap, and it was those "
                "ions that had been holding the decay back",
            "Water fills the air spaces, and decomposers work best when no "
                "air can reach the material",
            "Decomposers need water to survive and to carry dissolved "
                "substances, so without it they cannot work",
        ],
        "correct_index": 3,
        "why": "Water is one of the conditions decay needs: decomposers "
               "require it to live and to move dissolved substances, so a "
               "dry heap stops.",
    },
    {
        "id": "ks4-decomposition-s16",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cut slice of apple goes brown and begins to rot while the "
                "rest of the apple stays sound. Suggest two reasons.",
        "options": [
            "The slice is warmer than the whole apple, and its cells have "
                "already died",
            "The slice has lost its water, and dry material rots faster than "
                "moist material",
            "The slice has a larger exposed surface and no skin to keep "
                "decomposers out",
            "The slice contains more sugar, and sugar is what decomposers "
                "need in order to grow",
        ],
        "correct_index": 2,
        "why": "Cutting exposes a large moist surface for enzymes to act on "
               "and removes the skin that had been acting as a barrier.",
    },
    {
        "id": "ks4-decomposition-s17",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener is advised to mix woody prunings into a bin of "
                "grass cuttings rather than composting the grass on its own. "
                "Suggest why.",
        "options": [
            "The prunings supply the mineral ions that grass cuttings lack "
                "entirely",
            "The prunings absorb the water that grass cuttings would "
                "otherwise release",
            "The prunings lower the pH of the bin, which is the condition "
                "grass cuttings need in order to rot",
            "The prunings keep air spaces open in a bin that grass alone "
                "would pack solid",
        ],
        "correct_index": 3,
        "why": "Grass cuttings settle into a dense airless mass; coarse woody "
               "material holds open the spaces that keep the heap aerobic.",
    },
    {
        "id": "ks4-decomposition-s18",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a pile of rotting leaves gives off carbon "
                "dioxide.",
        "options": [
            "The leaves continue to photosynthesise for weeks after they "
                "fall, and carbon dioxide is one of the products",
            "The carbon in the leaves reacts with oxygen in the air without "
                "any living organism taking part",
            "Decomposers feeding on the leaves respire, and aerobic "
                "respiration releases carbon dioxide",
            "Water in the leaves breaks down into carbon dioxide once the "
                "leaves are no longer alive",
        ],
        "correct_index": 2,
        "why": "The gas comes from respiration in the bacteria and fungi "
               "feeding on the leaves, not from the leaves themselves.",
    },
    {
        "id": "ks4-decomposition-s19",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fallen tree trunk in a wood rots away over a few decades, "
                "but a plastic bag dropped beside it is still there. Suggest "
                "why.",
        "options": [
            "The bag is too light for decomposers to settle on, so nothing "
                "ever begins to break it down",
            "Decomposers have no enzymes that break the plastic down, so it "
                "is not digested",
            "The bag contains no water, and the trunk was full of water when "
                "it fell to the ground",
            "Decomposers are repelled by the smooth surface of the bag and "
                "so move away from it",
        ],
        "correct_index": 1,
        "why": "Decomposers make enzymes for the natural substances in dead "
               "organisms; plastic is not one of them, so it is not broken "
               "down.",
    },
    {
        "id": "ks4-decomposition-s20",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The soil directly beneath a long-standing compost heap is "
                "unusually rich in nitrates. Explain why.",
        "options": [
            "Nitrogen gas is pressed out of the air by the weight of the heap "
                "and forced down into the soil",
            "Nitrates released as the heap decays are washed down into the "
                "soil by rain",
            "The heap shades the soil, and shaded soil holds on to the "
                "nitrates that sunlight would destroy",
            "The soil is warmer under a heap, and warm soil makes its own "
                "nitrates out of the minerals already in it",
        ],
        "correct_index": 1,
        "why": "Decomposers in the heap release nitrates into solution, and "
               "water moving down through the heap carries them into the "
               "soil below.",
    },
    {
        "id": "ks4-decomposition-s21",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that a fungus 'eats' a dead leaf in the "
                "same way a rabbit eats grass. Explain how the two are "
                "different.",
        "options": [
            "A rabbit digests its food outside its body, while a fungus takes "
                "the whole leaf into a cell and digests it inside",
            "A rabbit does not digest grass at all, whereas a fungus digests "
                "every part of the leaf that it touches",
            "A fungus and a rabbit work in the same way, because both of them "
                "use enzymes to digest what they feed on",
            "A fungus digests the leaf where it lies and absorbs the soluble "
                "products, rather than taking solid food in",
        ],
        "correct_index": 3,
        "why": "Decomposers digest extracellularly: enzymes are secreted onto "
               "the material and only the dissolved products are absorbed, "
               "whereas a rabbit takes solid food into a gut.",
    },
    {
        "id": "ks4-decomposition-s22",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The pH of a sample of milk is recorded every 10 minutes as "
                "it is left in a warm room. Explain why the pH can be used "
                "to follow the rate of decay.",
        "options": [
            "Decomposers release alkaline substances, so the pH climbs as "
                "they work",
            "The pH rises and then falls again, so the turning point marks "
                "the moment decay begins",
            "Milk loses water as it decays, and the loss of water is what "
                "makes the reading change",
            "Bacteria in the milk produce acids as they break it down, so a "
                "falling pH shows decay happening",
        ],
        "correct_index": 3,
        "why": "The bacteria break lactose down to acids, so the pH falls as "
               "decay proceeds and the rate of that fall measures the rate of "
               "decay.",
    },
    {
        "id": "ks4-decomposition-s23",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student investigating the effect of temperature on decay "
                "is told to use water baths rather than a sunny windowsill "
                "and a fridge. Explain why.",
        "options": [
            "A water bath holds each sample at a known steady temperature, "
                "so the readings can be compared",
            "A water bath keeps the samples wet, and decay cannot happen in a "
                "dried sample",
            "A water bath keeps light off the samples, which would otherwise "
                "be bleached",
            "A water bath supplies the oxygen the decomposers need",
        ],
        "correct_index": 0,
        "why": "The independent variable has to be set to known values and "
               "held there; a windowsill drifts with the weather, so the "
               "comparison would mean nothing.",
    },
    {
        "id": "ks4-decomposition-s24",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student repeats a decay investigation three times at each "
                "temperature and calculates a mean. Explain why.",
        "options": [
            "Repeating changes the result each time, and the mean is the "
                "figure the examiner expects to see",
            "Repeating removes the need to control the other variables, "
                "because taking a mean cancels their effects out",
            "Repeating reduces the effect of random variation, so the mean is "
                "closer to the true value",
            "Repeating proves that the equipment is accurate, because three "
                "readings of one sample must agree",
        ],
        "correct_index": 2,
        "why": "Biological samples vary, so several measurements and a mean "
               "give a more reliable value than one reading.",
    },
    {
        "id": "ks4-decomposition-s25",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A compost bin has a dark lid that rests loosely on top "
                "rather than sealing. Explain the advantage of each of these "
                "two features.",
        "options": [
            "The dark lid keeps light out of the bin, and the loose fit lets "
                "the rain wash its mineral ions away",
            "The dark colour absorbs energy and keeps the bin warm, and the "
                "loose fit lets air in",
            "The dark colour hides the waste from flies, and the loose fit "
                "lets the heap cool at night",
            "The dark colour reflects the Sun so the bin cannot overheat, and "
                "the loose fit drains it",
        ],
        "correct_index": 1,
        "why": "Warmth and oxygen both speed decay, so a dark surface that "
               "absorbs energy and a lid that admits air each help the "
               "decomposers.",
    },
    {
        "id": "ks4-decomposition-s26",
        "subtopic_slug": "decomposition",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Conditions that are warm, moist and well aerated are "
                "described as the optimum for decay. Explain why all three "
                "matter together.",
        "options": [
            "Warmth speeds the enzymes, water lets the decomposers live and "
                "carry substances, and oxygen lets them respire",
            "Warmth kills competing organisms, water dissolves the material, "
                "and oxygen burns the rest",
            "Warmth dries the material out, water softens it, and oxygen then "
                "reacts with it",
            "Warmth raises the pH, water lowers it again, and oxygen holds it "
                "steady",
        ],
        "correct_index": 0,
        "why": "Each condition supports a different requirement of the living "
               "decomposers, so decay is fastest only when all three are "
               "met.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Rates with units, scaling a yield, then evaluation and prediction:
    # a shaded heap, liming an acid soil, the frozen-bacteria claim,
    # landfill against composting, a fungicide, controlling a second
    # variable, compound mass loss, an airless heap, aerobic against
    # anaerobic, a sealed jar, where lost mass goes, two soil pHs, a
    # doubling rule, the drying claim, two ways of measuring, two corpses,
    # and what a sewage works actually does.
    {
        "id": "ks4-decomposition-h05",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A milk sample reaches a fixed pH in 25 hours at 20 degrees "
                "Celsius and in 10 hours at 30 degrees Celsius. Calculate how "
                "many times faster the decay is at the higher temperature.",
        "options": [
            "1.5 times faster",
            "2.5 times faster",
            "15 times faster",
            "250 times faster",
        ],
        "correct_index": 1,
        "why": "Rate is inversely proportional to the time taken, so the "
               "ratio is 25 / 10 = 2.5.",
    },
    {
        "id": "ks4-decomposition-h06",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The pH of a milk sample falls from 6.8 to 5.0 over 90 "
                "minutes. Calculate the mean rate of pH change in pH units "
                "per hour.",
        "options": [
            "0.02 pH units per hour",
            "1.2 pH units per hour",
            "1.8 pH units per hour",
            "2.7 pH units per hour",
        ],
        "correct_index": 1,
        "why": "The change is 6.8 - 5.0 = 1.8 pH units over 1.5 hours, and "
               "1.8 / 1.5 = 1.2 pH units per hour.",
    },
    {
        "id": "ks4-decomposition-h07",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of leaf litter has a dry mass of 80 g. After 20 "
                "days its dry mass is 50 g. Calculate the mean rate of mass "
                "loss in grams per day.",
        "options": [
            "1.5 g per day",
            "0.7 g per day",
            "2.5 g per day",
            "4.0 g per day",
        ],
        "correct_index": 0,
        "why": "The mass lost is 80 - 50 = 30 g over 20 days, so the rate is "
               "30 / 20 = 1.5 g per day.",
    },
    {
        "id": "ks4-decomposition-h08",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of leaf litter falls from a dry mass of 80 g to a "
                "dry mass of 50 g. Calculate the percentage of the original "
                "mass that has been lost.",
        "options": [
            "37.5%",
            "30.0%",
            "60.0%",
            "62.5%",
        ],
        "correct_index": 0,
        "why": "The loss is 30 g out of the original 80 g, and 30 / 80 is "
               "37.5%.",
    },
    {
        "id": "ks4-decomposition-h09",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A biogas digester yields 24 cubic metres of gas from 400 kg "
                "of food waste. Calculate the yield expected from 1500 kg of "
                "the same waste.",
        "options": [
            "36 cubic metres",
            "64 cubic metres",
            "90 cubic metres",
            "375 cubic metres",
        ],
        "correct_index": 2,
        "why": "24 / 400 = 0.06 cubic metres per kilogram, and 0.06 x 1500 = "
               "90 cubic metres.",
    },
    {
        "id": "ks4-decomposition-h10",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical compost bins are filled on the same day. One "
                "stands in full sun, the other in deep shade under a north "
                "wall. Predict which is ready first, and explain.",
        "options": [
            "The shaded bin, because decomposer enzymes are denatured by the "
                "warmth that a sunny bin reaches",
            "Neither, because the rate of decay in a bin is set by the "
                "material in it and not by its surroundings",
            "The sunny bin, because it is warmer, so its decomposers' enzyme "
                "reactions run faster",
            "The shaded bin, because it stays damper, and moisture matters "
                "far more to decay than warmth ever does",
        ],
        "correct_index": 2,
        "why": "A warmer bin raises decomposer enzyme activity, and in a UK "
               "summer neither bin comes near the temperature at which those "
               "enzymes denature.",
    },
    {
        "id": "ks4-decomposition-h11",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lime is added to a woodland soil, raising its pH from 4.5 to "
                "6.5. Predict the effect on the rate at which the leaf litter "
                "on that soil decays.",
        "options": [
            "It falls, because decomposer enzymes work best in strongly "
                "acidic soil",
            "It falls, because lime coats the leaf litter and keeps the "
                "decomposers off it",
            "It is unchanged, because pH affects plants but not the bacteria "
                "and fungi in soil",
            "It rises, because the pH has moved closer to the optimum for "
                "decomposer enzymes",
        ],
        "correct_index": 3,
        "why": "Decomposers have an optimum pH near neutral, so moving an "
               "acidic soil towards it raises enzyme activity and speeds "
               "decay.",
    },
    {
        "id": "ks4-decomposition-h12",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that freezing food kills the bacteria on "
                "it. Evaluate this claim.",
        "options": [
            "Correct, because water expanding as it freezes bursts every "
                "bacterial cell in the food",
            "Correct, because no living organism of any kind can survive "
                "below the freezing point of water",
            "Wrong, because bacteria multiply faster in a freezer than they "
                "do at room temperature",
            "Wrong: freezing slows their enzymes so far that decay stops, but "
                "they revive on thawing",
        ],
        "correct_index": 3,
        "why": "Freezing is a preservation method, not a sterilisation one: "
               "the bacteria become inactive because their enzymes work so "
               "slowly, and they resume when the food thaws.",
    },
    {
        "id": "ks4-decomposition-h13",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A council says burying food waste in landfill is as good as "
                "composting it. Evaluate this in terms of the gases each "
                "produces.",
        "options": [
            "Weak: buried waste decays anaerobically and gives off methane, "
                "while a compost heap works aerobically",
            "Sound: the two produce the same gas, because decomposers respire "
                "in the same way wherever they are",
            "Weak: buried waste gives off no gas at all, whereas a compost "
                "heap releases large volumes of it",
            "Sound: buried waste produces carbon dioxide and compost produces "
                "methane, so landfill is the better of the two",
        ],
        "correct_index": 0,
        "why": "Deep landfill becomes anaerobic, so its decomposers release "
               "methane; a turned compost heap stays aerobic and releases "
               "carbon dioxide.",
    },
    {
        "id": "ks4-decomposition-h14",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fungicide applied to a woodland soil kills most of the "
                "fungi in it. Predict the effect on the nitrate content of "
                "that soil over the following year.",
        "options": [
            "It rises, because the dead fungi release their own nitrates into "
                "the soil around them",
            "It rises, because fungi had been taking nitrates out of the soil "
                "for their own growth",
            "It falls, because less dead material is broken down, so fewer "
                "nitrates are released",
            "It is unchanged, because nitrates in soil come from the rock "
                "below and not from decay",
        ],
        "correct_index": 2,
        "why": "Fungi are major decomposers, so removing them slows the "
               "breakdown of dead material and the release of nitrates that "
               "goes with it.",
    },
    {
        "id": "ks4-decomposition-h15",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student plans to investigate the effect of pH on the rate "
                "of decay. Explain why temperature must be controlled, and "
                "suggest how.",
        "options": [
            "Temperature changes the pH of a sample, so it must be held "
                "steady by standing the tubes in a draught",
            "Temperature affects the rate as well, so it must be held steady "
                "by standing all the tubes in one water bath",
            "Temperature affects the colour of the indicator, so every tube "
                "must be read at once",
            "Temperature has no effect on decay, so it need only be recorded "
                "rather than controlled in any way",
        ],
        "correct_index": 1,
        "why": "Temperature is a second factor affecting decomposer enzymes, "
               "so it must be kept the same for every pH; one water bath "
               "holding all the tubes does that.",
    },
    {
        "id": "ks4-decomposition-h16",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A compost heap starts at 200 kg. It loses 40% of its mass in "
                "the first month and then 25% of what is left in the second. "
                "Calculate its mass after two months.",
        "options": [
            "90 kg",
            "70 kg",
            "110 kg",
            "130 kg",
        ],
        "correct_index": 0,
        "why": "After the first month 200 - 80 = 120 kg remains, and losing "
               "25% of 120 kg leaves 90 kg.",
    },
    {
        "id": "ks4-decomposition-h17",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener whose heap has gone slimy and airless decides to "
                "buy more decomposer bacteria to add to it. Evaluate this "
                "plan.",
        "options": [
            "Sound, because a wet heap is slow for want of enough decomposers",
            "Weak, because the aerobic decomposers added cannot respire in an "
                "airless heap; it needs turning",
            "Sound, because bacteria bought for the purpose can respire "
                "without any oxygen at all",
            "Weak, because bacteria added to a heap are eaten by the fungi "
                "already growing in it",
        ],
        "correct_index": 1,
        "why": "The limiting condition is oxygen, not the number of "
               "organisms, so the heap must be opened up and turned rather "
               "than restocked.",
    },
    {
        "id": "ks4-decomposition-h18",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare aerobic and anaerobic decay in terms of the gas "
                "released and one use humans make of each.",
        "options": [
            "Aerobic gives methane for composting; anaerobic gives carbon "
                "dioxide for digesters",
            "Both give methane, but aerobic decay is used for compost while "
                "anaerobic decay is used for silage",
            "Aerobic gives carbon dioxide and is used to make compost; "
                "anaerobic gives methane and is used for biogas",
            "Both give carbon dioxide, but only anaerobic decay is fast "
                "enough to be of any use to humans",
        ],
        "correct_index": 2,
        "why": "Aerobic decomposers release carbon dioxide and are what a "
               "compost heap relies on; anaerobic ones release methane, "
               "which a biogas digester collects as fuel.",
    },
    {
        "id": "ks4-decomposition-h19",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An apple is sealed inside a glass jar and left to rot for a "
                "month. The whole jar is weighed before and after. Predict "
                "the result, and explain.",
        "options": [
            "The mass falls, because the apple has been broken down into "
                "simpler substances during the month",
            "The mass rises, because the decomposers growing on the apple add "
                "their own mass to the jar",
            "The mass is unchanged, because nothing can leave a sealed jar "
                "however far the decay goes",
            "The mass falls, because the water in the apple turns to vapour "
                "and vapour weighs less than liquid",
        ],
        "correct_index": 2,
        "why": "Decay rearranges the substances inside the jar but nothing "
               "enters or leaves it, so the total mass is the same.",
    },
    {
        "id": "ks4-decomposition-h20",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An open tray of leaves loses two thirds of its mass as it "
                "rots. A student says the lost mass has disappeared. Explain "
                "where it has gone.",
        "options": [
            "Into the gases released by respiring decomposers, and into the "
                "decomposers' own bodies",
            "Into the tray itself, which absorbs the substances released as "
                "the leaves break down",
            "It has been destroyed, because decay breaks matter down into "
                "nothing at all",
            "Into the light and warmth given out by the heap as the leaves "
                "are broken apart",
        ],
        "correct_index": 0,
        "why": "The carbon leaves as carbon dioxide and water vapour from "
               "respiration, and some of the material is built into the "
               "bodies of the decomposers themselves.",
    },
    {
        "id": "ks4-decomposition-h21",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two woodland soils have the same temperature and moisture. "
                "Soil A is at pH 4.0 and soil B is at pH 6.5. Predict which "
                "has the deeper layer of undecayed litter.",
        "options": [
            "Soil B, because a soil nearer neutral holds its litter together "
                "rather than letting it break apart",
            "Soil A, because its acidity slows decomposer enzymes, so litter "
                "builds up faster than it rots",
            "Neither, because pH has no effect once temperature and moisture "
                "are the same in both soils",
            "Soil B, because decomposers are killed outright by a pH as high "
                "as 6.5 and so cannot work at all",
        ],
        "correct_index": 1,
        "why": "Strongly acidic conditions are well away from the "
               "decomposers' optimum pH, so decay is slow and dead material "
               "accumulates.",
    },
    {
        "id": "ks4-decomposition-h22",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Between 0 and 40 degrees Celsius the rate of decay roughly "
                "doubles for every 10 degree rise. Calculate how many times "
                "faster decay is at 24 degrees than at 4 degrees.",
        "options": [
            "4 times faster",
            "2 times faster",
            "6 times faster",
            "20 times faster",
        ],
        "correct_index": 0,
        "why": "The rise is 20 degrees, which is two steps of 10, so the rate "
               "doubles twice: 2 x 2 = 4 times faster.",
    },
    {
        "id": "ks4-decomposition-h23",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A packet of dried fruit is labelled 'never goes off, because "
                "drying stops decay completely'. Evaluate this claim.",
        "options": [
            "Sound, because decomposers die permanently as soon as the water "
                "around them has been removed",
            "Weak, because dried fruit decays faster than fresh fruit as its "
                "sugars are more concentrated",
            "Sound, because a dried food contains no decomposers at all once "
                "the drying is finished",
            "Weak, because drying slows decay greatly but the fruit rots once "
                "it takes up moisture again",
        ],
        "correct_index": 3,
        "why": "Drying removes a condition decay needs rather than removing "
               "the decomposers, so decay resumes as soon as water returns.",
    },
    {
        "id": "ks4-decomposition-h24",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One student follows decay by counting mould patches on "
                "bread; another follows it by measuring the loss in dry mass. "
                "Suggest why the second method is more reliable.",
        "options": [
            "Counting patches takes longer, and a long method gives a less "
                "reliable answer than a quick one",
            "Dry mass can be measured on a balance to a known precision, "
                "while patches merge and are judged by eye",
            "Patches only appear once decay is finished, so counting them "
                "gives no information while it is going on",
            "Dry mass rises as decay proceeds, and a rising measurement is "
                "easier to read than a falling one",
        ],
        "correct_index": 1,
        "why": "Mass loss is a quantitative measurement with a stated "
               "resolution; counting patches that overlap and spread is a "
               "subjective judgement.",
    },
    {
        "id": "ks4-decomposition-h25",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dead mouse on a damp woodland floor in July is reduced to "
                "bones within weeks. Another in a cold dry attic is still "
                "recognisable years later. Explain the difference.",
        "options": [
            "The attic mouse is protected by the dust that settles on it, "
                "which no decomposer is able to penetrate",
            "The woodland mouse is eaten by predators, whereas nothing living "
                "ever reaches a mouse in an attic",
            "The woodland floor is warm and damp, so decay is fast; the attic "
                "is cold and dry, so it is very slow",
            "The attic air holds no oxygen, and decomposers cannot begin work "
                "on a body until oxygen reaches it",
        ],
        "correct_index": 2,
        "why": "Warmth and moisture both raise decomposer activity, so a damp "
               "summer woodland decays a body quickly while cold dry "
               "conditions nearly halt it.",
    },
    {
        "id": "ks4-decomposition-h26",
        "subtopic_slug": "decomposition",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A visitor to a sewage works says it 'just filters the water "
                "clean'. Evaluate this description.",
        "options": [
            "Sound, because the organic matter in sewage is removed entirely "
                "by passing it through fine screens",
            "Weak, because sewage is cleaned by adding acid to it rather than "
                "by filtering or by any living process",
            "Sound, because the aeration tanks are there to help the solids "
                "settle rather than to supply any organism",
            "Weak, because the works relies on aerobic decomposers digesting "
                "the dissolved organic matter",
        ],
        "correct_index": 3,
        "why": "Screens remove solids, but the dissolved organic matter is "
               "broken down by aerobic decomposers, which is why the tanks "
               "are aerated.",
    },
]
