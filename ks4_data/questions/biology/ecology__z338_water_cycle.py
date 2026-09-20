"""Biology · Ecology — the MRB-338 expansion of `water-cycle`.

One leaf only: AQA 8461 §4.7.2.2. The original twelve rows in `ecology__a.py`
take exhaled water vapour, the fixed total, stomata as the route out, the
groundwater store, urbanisation and runoff, irrigation depleting an aquifer,
transpiration against evaporation, warmer oceans, a reservoir replacing
farmland, the 'deforestation makes more water' error, a wooded valley against
a bare one, and a raindrop's two fates.

This file takes what they leave: condensation and the cooling that drives it,
the Sun as the energy source, the forms precipitation actually takes, why rain
is fresh when the ocean is salty, the route through a plant from root hair cell
to xylem, the animal routes other than breathing, water as solvent and as
reactant, and then the human seam — compaction, drainage, salinisation, snow as
a delayed store, wetlands, permeable paving and the measurement of rainfall
itself. The misconception set is here in full: transpiration imagined as taking
water OUT of the cycle, precipitation imagined as rain alone, 'recycled'
imagined as 'never short', and midday watering imagined as faster.

The weight follows the CONTENT. `easier` stays at eight because recall here is
a short list of named stages, stores and structures, and a ninth way of asking
it is the same question in new words. The demand lives in tracing a mechanism
through a named catchment and in arithmetic on real depths and areas — a
millimetre of rain over a hectare is ten cubic metres, and that one conversion
carries most of the harder band. So `standard` and `harder` carry twenty-two
each.

Numbers here are the ones the hydrology supplies: rainfall in millimetres,
areas in hectares and square metres, a rain gauge's funnel, an aquifer's
recharge against a town's draw, and a roof against a water butt.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # Condensation and its cause, the Sun as the driver, the forms of
    # precipitation, fresh rain from a salty ocean, the route through a
    # plant, sweating as an animal route, and water as a reactant.
    {
        "id": "ks4-water-cycle-e05",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the stage of the water cycle in which rising water "
                "vapour cools and turns back into tiny liquid droplets.",
        "options": [
            "Precipitation, which is the falling of those droplets as rain",
            "Condensation, which forms the clouds seen in the sky",
            "Evaporation, which lifts the droplets up from the ocean",
            "Transpiration, which pushes the droplets out of a leaf",
        ],
        "correct_index": 1,
        "why": "Cooling makes water vapour condense back to liquid droplets, "
               "and those droplets are what clouds and mist are made of.",
    },
    {
        "id": "ks4-water-cycle-e06",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the source of the energy that evaporates water from "
                "the oceans.",
        "options": [
            "Heat released by decomposers living in the ocean sediment",
            "Heat produced inside the Earth and conducted up through the "
                "ocean floor",
            "Energy transferred from the Sun to the water surface",
            "Energy released as salt dissolves in the surface sea water",
        ],
        "correct_index": 2,
        "why": "The Sun heats the water surface, and that energy is what "
               "turns liquid water into water vapour.",
    },
    {
        "id": "ks4-water-cycle-e07",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Precipitation is not only rain. Name another form in which "
                "precipitation reaches the ground.",
        "options": [
            "Hail",
            "Low mist",
            "Morning dew",
            "Ground fog",
        ],
        "correct_index": 0,
        "why": "Precipitation is water falling from cloud, and it falls as "
               "rain, snow, sleet or hail.",
    },
    {
        "id": "ks4-water-cycle-e08",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Most of the water on Earth is salty sea water. State why "
                "the rain that falls from clouds is fresh water.",
        "options": [
            "The salt is broken down into harmless gases inside the cloud",
            "Fresh river water evaporates while salty sea water cannot",
            "Rain collects fresh water from the air as it falls to the ground",
            "Only the water evaporates, and the dissolved salts stay behind",
        ],
        "correct_index": 3,
        "why": "Only the water evaporates; the dissolved salts stay behind in "
               "the sea, so the vapour and the rain formed from it are fresh.",
    },
    {
        "id": "ks4-water-cycle-e09",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the plant cells that take water into a plant from the "
                "soil.",
        "options": [
            "Guard cells, which sit on either side of a stoma",
            "Root hair cells, which have a long thin extension",
            "Palisade cells, which are packed with chloroplasts",
            "Phloem cells, which form long columns in the stem",
        ],
        "correct_index": 1,
        "why": "Root hair cells have a long extension that reaches between "
               "soil particles, giving a large surface for absorbing water.",
    },
    {
        "id": "ks4-water-cycle-e10",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mammal loses water through its skin on a hot day. Name "
                "this route by which water is returned to the environment.",
        "options": [
            "Osmosis",
            "Sweating",
            "Digestion",
            "Diffusion",
        ],
        "correct_index": 1,
        "why": "Sweat is water released onto the skin, where it evaporates "
               "and so returns water to the air.",
    },
    {
        "id": "ks4-water-cycle-e11",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the plant tissue that carries water upwards from the "
                "roots to the leaves.",
        "options": [
            "The waxy cuticle covering the upper leaf surface",
            "The phloem, which carries dissolved sugars around",
            "Xylem",
            "The spongy mesophyll in the middle of a leaf",
        ],
        "correct_index": 2,
        "why": "Xylem vessels form continuous tubes from root to leaf and "
               "carry water and dissolved mineral ions upwards.",
    },
    {
        "id": "ks4-water-cycle-e12",
        "subtopic_slug": "water-cycle",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some of the water a crop takes up is used in "
                "photosynthesis. State how water is used in that reaction.",
        "options": [
            "It is a catalyst, speeding the reaction up without itself "
                "changing",
            "It is a waste product, released from the leaf as a vapour",
            "It acts as a solvent, and none of it is chemically changed",
            "It is a reactant, combined with carbon dioxide to make glucose",
        ],
        "correct_index": 3,
        "why": "Photosynthesis uses water as a raw material: water and carbon "
               "dioxide are the reactants that form glucose and oxygen.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # The human seam and the mechanisms behind it: transpiration lost to
    # deforestation, salinisation, compaction, closed stomata, air forced
    # to rise, snow held back, a groundwater-fed river in drought, water as
    # a solvent, sweating, a bagged plant, a lost hedgerow, watering time,
    # a rain gauge, urban drains, biomass, Sun and gravity, a wetland, root
    # depth, a cold can, two routes to the sea, a puddle, and a salty sea.
    {
        "id": "ks4-water-cycle-s05",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rainfall over a tropical region falls in the years after "
                "its forest is cleared. Explain how removing the trees "
                "brings this about.",
        "options": [
            "Bare soil reflects more sunlight, which cools the air above it "
                "and stops clouds forming",
            "Fewer trees transpire, so less water vapour enters the air and "
                "less is available to fall",
            "Felled timber absorbs the rain that does fall, keeping it out "
                "of the rivers and the soil",
            "Cleared land is warmer, so the rain that does form evaporates "
                "again before it can reach the ground",
        ],
        "correct_index": 1,
        "why": "Trees return large volumes of water to the air by "
               "transpiration; with fewer trees there is less vapour to "
               "condense, so local rainfall falls.",
    },
    {
        "id": "ks4-water-cycle-s06",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A field in a hot dry region is irrigated for many years "
                "with water pumped from a well. The soil slowly becomes "
                "salty. Explain why.",
        "options": [
            "Water evaporates from the soil surface and leaves its dissolved "
                "salts behind in the soil",
            "Irrigation water reacts with the minerals in the soil and forms "
                "new salts as a product of that reaction",
            "Well water carries no salt, so the salt in the soil must have "
                "been released by the growing crop itself",
            "Salt is drawn upwards out of the rock below whenever a field is "
                "watered from above it",
        ],
        "correct_index": 0,
        "why": "The water evaporates but its dissolved salts cannot, so each "
               "watering leaves a little more salt in the surface soil.",
    },
    {
        "id": "ks4-water-cycle-s07",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a field that has been compacted by heavy "
                "machinery loses more of its rainfall as surface flow than a "
                "field that has been ploughed.",
        "options": [
            "Compacted soil is warmer, so most of the rain landing on it "
                "evaporates straight back into the air",
            "Compacted soil holds more mineral ions, and these push the "
                "arriving rainwater back to the surface",
            "Compacted soil has fewer air spaces, so water cannot soak in "
                "and flows across the surface instead",
            "Ploughed soil is left in ridges by the plough, so any water "
                "running across its surface travels downhill faster",
        ],
        "correct_index": 2,
        "why": "Compaction crushes the air spaces that water soaks into, so "
               "less infiltrates and more runs off the surface.",
    },
    {
        "id": "ks4-water-cycle-s08",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "During a drought a plant closes its stomata. Explain the "
                "effect this has on the plant's contribution to the water "
                "cycle.",
        "options": [
            "It rises, because the closed stomata force water back out "
                "through the roots into the soil",
            "It rises, because water builds up in the leaf and is pushed "
                "out through the cuticle",
            "It is unchanged, because water leaves a plant through its "
                "cuticle and not its stomata",
            "It falls, because water vapour escapes through the stomata and "
                "that route is now shut",
        ],
        "correct_index": 3,
        "why": "Transpiration is the loss of water vapour through the "
               "stomata, so closing them cuts the amount of water the plant "
               "returns to the air.",
    },
    {
        "id": "ks4-water-cycle-s09",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cloud often forms on the side of a mountain "
                "range where moist air is forced to rise.",
        "options": [
            "Rising air cools, so the water vapour in it condenses into "
                "droplets",
            "Rising air is squeezed by the rock, which presses vapour into "
                "droplets",
            "Rising air warms, so it can hold far more water vapour than "
                "before",
            "Rising air collects dust from the mountain, and the dust turns "
                "into droplets",
        ],
        "correct_index": 0,
        "why": "Air cools as it rises, and cooling is what makes water "
               "vapour condense into the droplets that form cloud.",
    },
    {
        "id": "ks4-water-cycle-s10",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two equal amounts of precipitation fall on a hillside in "
                "January, one as rain and one as snow. Explain why the snow "
                "reaches the river much later.",
        "options": [
            "Snow is absorbed by the plants on the hillside and released to "
                "the river in the spring",
            "Snow contains less water than rain, so the river takes longer "
                "to show any rise",
            "Snow evaporates straight into the air and comes back to the "
                "hillside as rain much later on",
            "Snow is held on the ground as a store of frozen water until it "
                "warms enough to melt",
        ],
        "correct_index": 3,
        "why": "Snow stays on the ground as a store of solid water, so its "
               "water only joins the runoff once temperatures rise and it "
               "melts.",
    },
    {
        "id": "ks4-water-cycle-s11",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A river is fed mainly by water seeping out of the rock "
                "beneath its valley. Explain why its flow drops after a long "
                "hot dry spell.",
        "options": [
            "Little rain has soaked down to replace what seeps out, and more "
                "is lost by evaporation",
            "Hot weather makes the rock expand and close up, so the water "
                "inside it cannot escape",
            "The river water has become warmer, and warm water flows far "
                "more slowly than cold water does",
            "Plants along the bank have died back, so nothing is holding the "
                "river water in place",
        ],
        "correct_index": 0,
        "why": "The rock store is only topped up by rain soaking in; with "
               "little precipitation and high evaporation, less water is "
               "available to seep into the river.",
    },
    {
        "id": "ks4-water-cycle-s12",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water is described as the solvent of life. Explain what "
                "this means for the reactions inside a cell.",
        "options": [
            "Water is broken down inside the cell, and this releases the "
                "energy that its reactions need",
            "Water coats each enzyme in a waterproof layer that keeps the "
                "reactions apart",
            "Water dissolves the substances involved, so they can mix and "
                "react and be transported",
            "Water raises the temperature inside the cell, so that the "
                "reactions taking place there go faster",
        ],
        "correct_index": 2,
        "why": "Substances must be in solution to move and to meet, so cell "
               "reactions and transport both depend on water as the solvent.",
    },
    {
        "id": "ks4-water-cycle-s13",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how sweat cools the skin, and name the stage of the "
                "water cycle this involves.",
        "options": [
            "Sweat blocks the pores in the skin, which traps heat and stops "
                "it escaping — this is condensation",
            "Sweat takes energy from the skin as it evaporates, cooling it "
                "— this is evaporation",
            "Sweat forms a cold layer of liquid on the skin, chilling it "
                "— this is precipitation",
            "Sweat is drawn back into the body carrying heat with it "
                "— this is transpiration",
        ],
        "correct_index": 1,
        "why": "Evaporating water needs energy, and it takes that energy "
               "from the skin, which is why the skin cools as sweat dries.",
    },
    {
        "id": "ks4-water-cycle-s14",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A clear plastic bag is tied over the leafy shoot of a "
                "healthy plant. Droplets of liquid collect on the inside of "
                "the bag. Explain how they got there.",
        "options": [
            "Rain has passed through the plastic and gathered on its inner "
                "surface",
            "Liquid water has been forced out of the leaves and run down the "
                "plastic",
            "Water vapour from the leaves has condensed on the cooler "
                "plastic",
            "Oxygen from the leaves has turned into water on meeting the "
                "plastic",
        ],
        "correct_index": 2,
        "why": "The leaves lose water as vapour through their stomata, and "
               "that vapour condenses to liquid on the cooler bag.",
    },
    {
        "id": "ks4-water-cycle-s15",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thick hedge at the bottom of a sloping field is grubbed "
                "out. Explain the effect on how quickly rainwater reaches "
                "the stream below.",
        "options": [
            "It arrives more slowly, because the bare strip of soil left "
                "behind soaks up all of the water",
            "It arrives at the same speed, because a hedge has no effect on "
                "water flowing over the ground",
            "It arrives more slowly, because the hedge had been channelling "
                "water straight into the stream",
            "It arrives more quickly, because the roots and stems that "
                "slowed the water down have gone",
        ],
        "correct_index": 3,
        "why": "A hedge's stems and roots slow surface flow and help water "
               "soak in; without it the water reaches the stream faster.",
    },
    {
        "id": "ks4-water-cycle-s16",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower waters a crop either at midday or at dusk. "
                "Explain which timing loses less of the water to the "
                "atmosphere.",
        "options": [
            "Midday, because the warm soil absorbs the water before it has "
                "any chance to evaporate",
            "Dusk, because it is cooler, so less of the water evaporates "
                "before soaking into the soil",
            "Midday, because the crop is transpiring fastest then and so "
                "pulls the water straight down to its roots",
            "Dusk, because water poured onto cold soil condenses instead of "
                "soaking down to the roots",
        ],
        "correct_index": 1,
        "why": "Evaporation is faster when it is warmer, so watering in the "
               "cool of the evening leaves more water in the soil.",
    },
    {
        "id": "ks4-water-cycle-s17",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A class measures daily rainfall with a rain gauge. Explain "
                "why the gauge must be emptied and read at the same time "
                "each day.",
        "options": [
            "So that every reading covers the same length of time and the "
                "days can be compared",
            "So that the water inside has time to reach the temperature of "
                "the air around it",
            "So that the same person makes each reading and no one else can "
                "change the results",
            "So that any water that has evaporated out of the gauge can be "
                "replaced before the reading is taken",
        ],
        "correct_index": 0,
        "why": "Rainfall is a depth collected over a time interval, so the "
               "intervals must be equal for the daily figures to be "
               "comparable.",
    },
    {
        "id": "ks4-water-cycle-s18",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Drains in a town are built to carry storm water away as "
                "fast as possible. Suggest one problem this causes for a "
                "village further down the river.",
        "options": [
            "Its river dries up, because the drains send the storm water "
                "away underground instead of into it",
            "Its river runs clearer, because the drains filter the storm "
                "water on the way",
            "Its rainfall increases, because the water the drains remove "
                "evaporates again upstream of it",
            "Its river rises suddenly, because a large volume arrives all "
                "at once rather than slowly",
        ],
        "correct_index": 3,
        "why": "Fast drainage concentrates the storm water into a short "
               "period, giving a sharp rise in the river downstream and a "
               "greater flood risk.",
    },
    {
        "id": "ks4-water-cycle-s19",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Nearly all of the water a crop absorbs is returned to the "
                "air, but not quite all of it. Suggest where the rest of it "
                "goes.",
        "options": [
            "It is destroyed in the leaf during photosynthesis, so none of "
                "it can ever be recovered",
            "It stays in the plant's cells and is built into the substances "
                "the plant makes",
            "It is passed out through the roots and back into the soil "
                "around the plant",
            "It is converted into oxygen gas, which then leaves through the "
                "stomata",
        ],
        "correct_index": 1,
        "why": "A small fraction of the water taken up stays in the plant, "
               "filling its cells and supplying the water used as a reactant "
               "in photosynthesis.",
    },
    {
        "id": "ks4-water-cycle-s20",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The water cycle is often described as being driven by the "
                "Sun and by gravity. Explain the part each of them plays.",
        "options": [
            "The Sun makes water condense into cloud; gravity lifts the "
                "vapour up to the cloud",
            "The Sun warms the rivers so they flow; gravity holds the water "
                "vapour inside the clouds",
            "The Sun evaporates water into the air; gravity brings "
                "precipitation and runoff back down",
            "The Sun draws water up out of the soil; gravity spreads the "
                "clouds out across the sky",
        ],
        "correct_index": 2,
        "why": "The Sun's energy lifts water into the air as vapour, and "
               "gravity returns it as precipitation and then as runoff down "
               "to the sea.",
    },
    {
        "id": "ks4-water-cycle-s21",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A boggy wetland lies between a large field and a river. "
                "Explain how it reduces the height the river reaches after a "
                "storm.",
        "options": [
            "It evaporates the whole storm's rainfall before any of it can "
                "reach the river channel",
            "It warms the storm water, and warm water takes up less room in "
                "the river channel",
            "It sends the storm water straight down into the rock, where it "
                "can never reach a river",
            "It holds the storm water and releases it slowly, so the river "
                "rises less at any moment",
        ],
        "correct_index": 3,
        "why": "The wetland acts as a temporary store, spreading the same "
               "volume of water over a longer time so the peak flow is "
               "lower.",
    },
    {
        "id": "ks4-water-cycle-s22",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a dry summer the grass in a park turns brown while the "
                "large trees around it stay green. Suggest why the trees "
                "keep taking up water.",
        "options": [
            "Their leaves take in water vapour from the air, so they need no "
                "soil water at all",
            "Their thicker bark stops them losing any water, so they need "
                "none from the soil",
            "Their roots reach down to moist soil and rock that the shallow "
                "grass roots cannot",
            "Their larger leaves collect dew each night, which supplies all "
                "the water they need",
        ],
        "correct_index": 2,
        "why": "Deep tree roots reach water still held well below the "
               "surface, while shallow grass roots only reach soil that has "
               "already dried.",
    },
    {
        "id": "ks4-water-cycle-s23",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water collects on the outside of a cold can taken from a "
                "fridge. Explain how this is the same process that forms "
                "cloud.",
        "options": [
            "Water is escaping through the metal of the can, just as it "
                "escapes upwards from the sea",
            "Air touching the can is cooled, so its vapour condenses, just "
                "as rising air cools and forms cloud",
            "The cold can is pulling rain out of the air towards it, just as "
                "a cloud pulls rain towards the ground",
            "The can is warming the air near it, so vapour forms on it, just "
                "as warm air forms cloud",
        ],
        "correct_index": 1,
        "why": "In both cases air is cooled and the water vapour it carries "
               "condenses into liquid droplets.",
    },
    {
        "id": "ks4-water-cycle-s24",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare runoff and groundwater as routes by which "
                "precipitation returns to the sea.",
        "options": [
            "Runoff flows over the surface and arrives quickly; groundwater "
                "moves through rock and arrives slowly",
            "Runoff flows through the rock and arrives slowly; groundwater "
                "flows over the surface and arrives quickly",
            "Both flow across the land surface, but runoff carries dissolved "
                "salts while groundwater carries none",
            "Both move through the rock below ground, but runoff does so in "
                "winter and groundwater in summer",
        ],
        "correct_index": 0,
        "why": "Runoff is surface flow into streams and rivers and is fast; "
               "groundwater seeps through rock and reaches rivers and the "
               "sea slowly.",
    },
    {
        "id": "ks4-water-cycle-s25",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shallow puddle and a deep pond have the same surface "
                "area. After a warm week the puddle has gone and the pond "
                "has not. Explain why.",
        "options": [
            "Water evaporates faster from a thin layer, because each "
                "molecule is nearer the surface",
            "The pond is fed by rain while the puddle is not, so the pond is "
                "being topped up",
            "Similar depths of water are lost from each, but the puddle held "
                "far less to begin with",
            "The pond water is colder, and cold water cannot evaporate at "
                "all until it has warmed right through",
        ],
        "correct_index": 2,
        "why": "Evaporation removes a similar depth from each equal surface, "
               "so the shallow puddle is emptied while the deep pond is "
               "barely lowered.",
    },
    {
        "id": "ks4-water-cycle-s26",
        "subtopic_slug": "water-cycle",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rivers carry fresh water into the sea, yet the sea stays "
                "salty. Explain how the water cycle keeps the salt there.",
        "options": [
            "Sea water makes its own salt, so the fresh water flowing into "
                "it from rivers cannot dilute it",
            "River water is salty too by the time it arrives, so nothing "
                "about the sea changes",
            "Salt sinks to the sea bed, so it does not mix with the fresh "
                "water arriving at the surface above",
            "Only water leaves the sea by evaporating, so the salts carried "
                "in by rivers stay behind",
        ],
        "correct_index": 3,
        "why": "Rivers deliver dissolved salts and only the water leaves "
               "again by evaporation, so salt accumulates in the sea.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Arithmetic on real depths and areas, then evaluation: a millimetre
    # over a hectare, a car park's runoff, an aquifer's deficit, a gauge's
    # funnel, woodland against a flood wall, desalination, drainage
    # ditches, the 'transpiration removes water' error, drip against flood
    # irrigation, salt water intrusion, an evaporation rate, reservoir
    # shape, a cover crop, a catchment balance, 'recycled so never short',
    # permeable paving, two rivers in drought, midday watering, a roof and
    # a butt, a mass-loss method, gauge siting, and sustainable extraction.
    {
        "id": "ks4-water-cycle-h05",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A depth of 1 mm of water over an area of 1 hectare is a "
                "volume of 10 cubic metres. A forest of 25 hectares "
                "transpires a depth of 4 mm each day. Calculate the volume "
                "of water it returns to the air each day.",
        "options": [
            "100 cubic metres",
            "250 cubic metres",
            "1000 cubic metres",
            "4000 cubic metres",
        ],
        "correct_index": 2,
        "why": "4 mm over 25 hectares is 4 x 25 x 10 = 1000 cubic metres per "
               "day.",
    },
    {
        "id": "ks4-water-cycle-h06",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car park has an area of 20 000 square metres. In one year "
                "0.85 m of rain falls on it and 90% of that runs off the "
                "surface. Calculate the volume of runoff in one year.",
        "options": [
            "1530 cubic metres",
            "15 300 cubic metres",
            "17 000 cubic metres",
            "18 700 cubic metres",
        ],
        "correct_index": 1,
        "why": "0.85 x 20 000 = 17 000 cubic metres of rainfall, and 90% of "
               "that is 15 300 cubic metres.",
    },
    {
        "id": "ks4-water-cycle-h07",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A town draws 4.5 million litres of water a day from the "
                "rock beneath it. Rainfall soaking down replaces 3.0 million "
                "litres a day. Calculate the fall in the stored volume over "
                "200 days.",
        "options": [
            "150 million litres",
            "300 million litres",
            "600 million litres",
            "900 million litres",
        ],
        "correct_index": 1,
        "why": "The daily shortfall is 4.5 - 3.0 = 1.5 million litres, and "
               "1.5 x 200 = 300 million litres over the period.",
    },
    {
        "id": "ks4-water-cycle-h08",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rain gauge has a collecting funnel of area 21 square "
                "centimetres. In one day it collects 63 cubic centimetres of "
                "water. Calculate the day's rainfall in millimetres.",
        "options": [
            "3 mm",
            "21 mm",
            "30 mm",
            "63 mm",
        ],
        "correct_index": 2,
        "why": "Depth = volume / area = 63 / 21 = 3 cm, and 3 cm is 30 mm.",
    },
    {
        "id": "ks4-water-cycle-h09",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A town at risk of flooding can either raise its flood wall "
                "or plant woodland across the hills upstream. Evaluate the "
                "woodland option.",
        "options": [
            "It is pointless, because trees have no effect on how rainwater "
                "moves across a hillside",
            "It is certain to work at once, because a newly planted wood "
                "absorbs every storm completely",
            "It helps, because trees slow the water and help it soak in, but "
                "it takes years to be effective",
            "It is better in every way, because planting a wood costs the "
                "town nothing at all",
        ],
        "correct_index": 2,
        "why": "Woodland raises infiltration and slows surface flow, "
               "lowering the flood peak, but the trees must grow before the "
               "effect is large, and the land is taken out of other use.",
    },
    {
        "id": "ks4-water-cycle-h10",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company says its desalination plant means a dry country "
                "'no longer depends on the water cycle'. Evaluate this "
                "claim.",
        "options": [
            "Fair, because desalination makes new water rather than moving "
                "water between stores",
            "Weak, because the plant only moves water from one store to "
                "another and needs energy to do it",
            "Fair, because sea water is a store that the water cycle never "
                "refills or draws from",
            "Weak, because a desalination plant cannot separate dissolved "
                "salts out of sea water",
        ],
        "correct_index": 1,
        "why": "Desalination takes water out of the ocean store and puts it "
               "into the freshwater store, using energy to do it; no water "
               "is created and the cycle still supplies everything else.",
    },
    {
        "id": "ks4-water-cycle-h11",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deep ditches are cut across a waterlogged field to carry "
                "water off it into a stream. Predict the effect on the level "
                "of water held in the soil.",
        "options": [
            "It rises, because the ditches fill with water and that water "
                "soaks sideways into the field",
            "It stays where it was, because ditches only move water that is "
                "already on the surface",
            "It rises, because water flowing in a ditch is pushed back up "
                "into the soil on either side",
            "It falls, because water now drains out of the soil and away "
                "into the stream",
        ],
        "correct_index": 3,
        "why": "The ditches give the soil water a route out, so it drains "
               "away and the level of water stored in the soil drops.",
    },
    {
        "id": "ks4-water-cycle-h12",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'A plant that transpires a lot is taking "
                "water out of the water cycle.' Identify the error in this "
                "reasoning.",
        "options": [
            "Transpiration destroys the water in the leaf, so the loss is "
                "even larger than the student suggests",
            "Transpiration is part of the cycle, and it puts water back into "
                "the air rather than removing it",
            "Transpiration moves water down into rock, so it is lost from "
                "the cycle for good",
            "Transpiration happens in animals rather than plants, so a plant "
                "removes nothing",
        ],
        "correct_index": 1,
        "why": "Transpiration is one of the routes that returns water to the "
               "atmosphere, so it moves water round the cycle instead of "
               "taking any out of it.",
    },
    {
        "id": "ks4-water-cycle-h13",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare flooding a field with water and delivering the same "
                "volume through drip pipes laid under the soil surface.",
        "options": [
            "Flooding loses less to the air, because a layer of water on the "
                "surface seals the soil below it",
            "Both lose the same, because the volume delivered to the field "
                "is identical in the two cases",
            "Drip pipes lose more to the air, because water under the soil "
                "is warmed by the ground around it",
            "Drip pipes lose less to the air, because the water is released "
                "below the surface where it cannot evaporate",
        ],
        "correct_index": 3,
        "why": "Evaporation happens at exposed surfaces, so water delivered "
               "below the soil surface loses much less to the atmosphere "
               "than a flooded field does.",
    },
    {
        "id": "ks4-water-cycle-h14",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A coastal town pumps fresh water from the rock beneath it "
                "faster than rain can replace it. Its wells slowly turn "
                "salty. Suggest why.",
        "options": [
            "Pumping the rock so hard grinds it up and releases salts that "
                "were locked inside it",
            "The fresh water in the rock reacts with the metal of the pump "
                "and is turned into a salt solution",
            "Sea water moves inland into the rock as the fresh water stored "
                "there is drawn down",
            "Rain falling on a coastal town is salty, so the water soaking "
                "down is salty from the start",
        ],
        "correct_index": 2,
        "why": "Over-extraction lowers the fresh groundwater, and sea water "
               "moves into the rock to take its place, so the wells draw up "
               "salt water.",
    },
    {
        "id": "ks4-water-cycle-h15",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An open tray of water with a surface area of 0.5 square "
                "metres loses 1200 g of water in 8 hours. Calculate the rate "
                "of evaporation in grams per hour per square metre.",
        "options": [
            "75 g per hour per square metre",
            "150 g per hour per square metre",
            "300 g per hour per square metre",
            "600 g per hour per square metre",
        ],
        "correct_index": 2,
        "why": "1200 / 8 = 150 g per hour, and dividing by 0.5 square metres "
               "gives 300 g per hour per square metre.",
    },
    {
        "id": "ks4-water-cycle-h16",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two reservoirs hold the same volume of water. One is deep "
                "and narrow, the other shallow and wide. Predict which loses "
                "more water over a hot summer, and explain.",
        "options": [
            "The deep one, because water under pressure at depth evaporates "
                "more readily than shallow water",
            "The shallow one, because it has a larger surface area exposed "
                "to the Sun and the air",
            "Neither, because the volume of water held is what decides how "
                "much of it evaporates",
            "The deep one, because it holds a taller column of water and so "
                "a greater mass can escape",
        ],
        "correct_index": 1,
        "why": "Evaporation happens at the surface, so the reservoir with "
               "the larger exposed surface area loses more water for the "
               "same volume stored.",
    },
    {
        "id": "ks4-water-cycle-h17",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two fields of the same soil receive the same winter "
                "rainfall. One is left as bare ploughed earth, the other is "
                "sown with a leafy cover crop. Compare how much of the rain "
                "soaks into each.",
        "options": [
            "More soaks into the covered field, because the plants slow the "
                "water and their roots open channels",
            "More soaks into the bare field, because there are no plant "
                "roots left in its soil to block up the spaces",
            "The same soaks into each, because it is the type of soil in a "
                "field that decides infiltration",
            "None soaks into the covered field, because the leaves catch "
                "every drop before it lands",
        ],
        "correct_index": 0,
        "why": "Leaves and stems slow the rain reaching the surface and "
               "roots keep the soil open, so a covered field takes in more "
               "water and sheds less as runoff.",
    },
    {
        "id": "ks4-water-cycle-h18",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A catchment receives 1200 mm of rain in a year. Of that, "
                "300 mm returns to the air by evaporation and transpiration "
                "and the rest leaves in the river. Calculate the river's "
                "share as a percentage of the rainfall.",
        "options": [
            "25%",
            "40%",
            "75%",
            "80%",
        ],
        "correct_index": 2,
        "why": "1200 - 300 = 900 mm leaves in the river, and 900 / 1200 is "
               "75% of the rainfall.",
    },
    {
        "id": "ks4-water-cycle-h19",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues: 'Water is recycled, so a country can "
                "never run short of it.' Evaluate this argument.",
        "options": [
            "Sound, because recycling guarantees that the same depth of rain "
                "falls on each country each year",
            "Unsound, because living organisms use water up, so the total "
                "amount on Earth falls year by year",
            "Sound, because the amount of water on Earth is fixed and cannot "
                "be reduced by any means",
            "Unsound, because the cycle does not deliver water to every "
                "place at the time it is needed",
        ],
        "correct_index": 3,
        "why": "The global total is fixed, but shortage is about where and "
               "when water arrives, and a region can receive far less than "
               "it uses.",
    },
    {
        "id": "ks4-water-cycle-h20",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A city replaces a third of its paving with a surface that "
                "lets water pass through into the soil beneath. Predict the "
                "effect on the peak flow of its river after a storm.",
        "options": [
            "It rises, because water passing down into the soil reaches the "
                "river faster than water on the surface does",
            "It falls, because more of the storm water soaks in and reaches "
                "the river slowly instead",
            "It is unchanged, because the same total volume of rain must "
                "still reach the river in the end",
            "It rises, because the new surface holds heat and so melts any "
                "snow falling with the storm",
        ],
        "correct_index": 1,
        "why": "Letting water infiltrate diverts part of the storm from fast "
               "surface flow into slow groundwater flow, so the river's peak "
               "is lower even though the total is the same.",
    },
    {
        "id": "ks4-water-cycle-h21",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "River P is fed mainly by water seeping out of porous rock. "
                "River Q is fed mainly by surface flow off steep clay "
                "hillsides. Predict which keeps flowing longer in a drought.",
        "options": [
            "River Q, because surface flow continues even when no rain has "
                "fallen for many weeks",
            "Neither, because the flow of any river is decided by how much "
                "rain fell during the previous day",
            "River P, because the rock holds a store of water that keeps "
                "seeping out between rainfalls",
            "River Q, because clay hillsides hold far more water than porous "
                "rock does and release it slowly",
        ],
        "correct_index": 2,
        "why": "Porous rock stores water and releases it slowly, so a "
               "groundwater-fed river keeps flowing; a river fed by runoff "
               "falls away as soon as the rain stops.",
    },
    {
        "id": "ks4-water-cycle-h22",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower says watering at midday is best 'because the water "
                "gets to the roots faster in the heat'. Evaluate this.",
        "options": [
            "Weak: soaking in is not much faster when warm, and far more of "
                "the water is lost by evaporation",
            "Sound: warm water is thinner than cold water, so it passes down "
                "through the soil several times faster",
            "Sound: the crop transpires hardest at midday, so it pulls the "
                "water straight down to its own roots",
            "Weak: water poured onto hot soil bakes into a hard crust on the "
                "surface and cannot reach the roots",
        ],
        "correct_index": 0,
        "why": "Any small gain in how fast the water soaks in is outweighed "
               "by the much larger evaporation loss from warm soil in full "
               "sun.",
    },
    {
        "id": "ks4-water-cycle-h23",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A flat roof of area 1200 square metres drains into a water "
                "butt holding 1500 litres. A storm drops 5 mm of rain. "
                "Determine whether the butt overflows. One cubic metre is "
                "1000 litres.",
        "options": [
            "No, because only 60 litres of rain lands on the roof in total",
            "No, because 1500 litres of rain lands on the roof, which just "
                "fills it",
            "Yes, because 6000 litres lands on the roof, four times what the "
                "butt holds",
            "Yes, because 600 litres lands on the roof, which is more than "
                "the butt holds",
        ],
        "correct_index": 2,
        "why": "5 mm is 0.005 m, so 0.005 x 1200 = 6 cubic metres = 6000 "
               "litres, and the 1500 litre butt overflows.",
    },
    {
        "id": "ks4-water-cycle-h24",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures how much water a potted plant returns to "
                "the air by weighing the whole pot each hour, leaving the "
                "soil surface open. Explain the effect of this on the "
                "result.",
        "options": [
            "The figure is too low, because water lost from the soil is not "
                "recorded by the balance",
            "The figure is too high, because water evaporating from the soil "
                "is counted as well as the plant's",
            "The figure is unaffected, because soil loses no water once a "
                "plant has been growing in it",
            "The figure is too low, because an open surface lets the soil "
                "draw water back from the air",
        ],
        "correct_index": 1,
        "why": "The balance records every loss of water from the pot, so "
               "evaporation from the exposed soil is added to the plant's "
               "own loss and the result is an overestimate.",
    },
    {
        "id": "ks4-water-cycle-h25",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two rain gauges record the same storm. One stands in open "
                "grass, the other beneath a spreading tree. Evaluate which "
                "gives the better measure of the storm's rainfall.",
        "options": [
            "The one under the tree, because its branches shelter the gauge "
                "from the wind that would blow rain out of it",
            "Either, because water collected in a gauge of known area gives "
                "the same depth of rainfall wherever it stands",
            "The one under the tree, because its reading also includes the "
                "water that drips down to it from the leaves",
            "The one in the open, because the tree's leaves intercept part "
                "of the rain before it can be collected",
        ],
        "correct_index": 3,
        "why": "A canopy catches and holds part of the rain, so a sheltered "
               "gauge under-records; an open site receives the full depth "
               "falling on the ground.",
    },
    {
        "id": "ks4-water-cycle-h26",
        "subtopic_slug": "water-cycle",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A water company says its supply is safe for ever because it "
                "takes out of the rock only as much as an average year's rain "
                "puts back. Evaluate this.",
        "options": [
            "Sound in principle, but dry years put back less, and others "
                "drawing on the same rock reduce it further",
            "Unsound, because rain that soaks into rock never returns to the "
                "store it came from",
            "Sound without qualification, because an average over many years "
                "removes the risk entirely",
            "Unsound, because water taken out of rock cannot be replaced by "
                "rainfall at any useful rate",
        ],
        "correct_index": 0,
        "why": "Balancing extraction against average recharge is the right "
               "principle, but recharge varies year to year and other users "
               "draw on the same store, so the balance can still fail.",
    },
]
