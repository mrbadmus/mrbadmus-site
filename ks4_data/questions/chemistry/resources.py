"""Chemistry · Using resources (AQA 8462, 5.10 / 4.10) — assignment pool.

Ten subtopics: the Earth's resources and sustainable development, potable
water, life cycle assessment, reducing the use of resources, corrosion,
alloys, ceramics/polymers/composites, the Haber process, NPK fertilisers and
the alternative extraction routes.

Distractors are built on the misconceptions this topic actually produces:
that potable water means pure water, that an LCA is an objective number, that
recycling is always the greenest option, that rusting needs only oxygen, that
sacrificial protection works by the coating being LESS reactive, that an alloy
is a compound, that a catalyst raises the equilibrium yield, that NPK is one
compound, and that bioleaching hands you copper metal rather than a solution
of copper ions.

The first four subtopics are BASE (Foundation Combined sit them), so nothing
in them reaches into the Higher extension prose: no atom-economy arithmetic,
no Le Chatelier vocabulary, no ozone/UV evaluation, no bioplastics. The five
4.10.3–4.10.4 subtopics are Triple-only at foundation tier; alternative metal
extraction is Higher tier and not Triple-only.
"""

TOPIC = "resources"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── earths-resources ── BASE (foundation, not triple) ────────────────
    {
        "id": "ks4-earths-resources-e01",
        "subtopic_slug": "earths-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which one of these of the Earth's resources is non-renewable?",
        "options": [
            "Timber from a sustainably managed forest",
            "Wind used to drive a turbine on a hillside",
            "Crude oil pumped from a rock formation",
            "Fresh water collected in a reservoir",
        ],
        "correct_index": 2,
        "why": "Crude oil is a fossil fuel that took millions of years to "
               "form, so it cannot be replaced on a human timescale.",
    },
    {
        "id": "ks4-earths-resources-e02",
        "subtopic_slug": "earths-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Nitrogen and oxygen are obtained from which of the Earth's "
                "natural resources?",
        "options": [
            "Air",
            "Crude oil",
            "Metal ores",
            "Sea water",
        ],
        "correct_index": 0,
        "why": "Air is about 78% nitrogen and 21% oxygen, and the two are "
               "separated from liquefied air by fractional distillation.",
    },
    {
        "id": "ks4-earths-resources-e03",
        "subtopic_slug": "earths-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement describes a finite resource?",
        "options": [
            "It can be re-formed as quickly as it is being used up",
            "It is only found in the Earth's crust and never in the sea",
            "It can always be replaced by recycling the same material",
            "It is being used up faster than it can be replaced",
        ],
        "correct_index": 3,
        "why": "A finite resource is one whose natural supply is not "
               "replenished on any useful timescale, so it will run out.",
    },
    {
        "id": "ks4-earths-resources-e04",
        "subtopic_slug": "earths-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a biological resource taken from the "
                "natural environment?",
        "options": [
            "Iron ore quarried out of rock",
            "Timber grown in a forest",
            "Natural gas from a well",
            "Sand dredged from a river",
        ],
        "correct_index": 1,
        "why": "Biological resources come from living things, and timber is "
               "wood grown by trees rather than dug from the ground.",
    },
    {
        "id": "ks4-earths-resources-s01",
        "subtopic_slug": "earths-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company redesigns a manufacturing process. Which change "
                "best follows the principles of green chemistry?",
        "options": [
            "Switching to a plant-based feedstock and a lower reaction "
            "temperature",
            "Increasing production so that each item costs less to make",
            "Moving the factory to a country with weaker pollution laws",
            "Replacing recycled packaging with new packaging that looks "
            "better",
        ],
        "correct_index": 0,
        "why": "Green chemistry aims to cut waste and energy use and to "
               "replace finite feedstocks with renewable ones.",
    },
    {
        "id": "ks4-earths-resources-s02",
        "subtopic_slug": "earths-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The global population is growing. Which consequence for the "
                "Earth's resources follows directly from this?",
        "options": [
            "Fossil fuels will re-form more quickly to meet the extra demand",
            "Less agricultural land will be needed as farming becomes "
            "more efficient",
            "More ore must be mined, so finite reserves run out sooner",
            "Metal ores will become renewable because more of them are found",
        ],
        "correct_index": 2,
        "why": "More people need more materials, and every extra tonne of "
               "metal comes from an ore reserve that is not replaced.",
    },
    {
        "id": "ks4-earths-resources-s03",
        "subtopic_slug": "earths-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why timber is described as a renewable resource only "
                "when forests are managed.",
        "options": [
            "Timber is renewable because wood can always be recycled as paper",
            "New trees must be planted at least as fast as mature trees are "
            "felled",
            "Timber is renewable because trees remove carbon dioxide from "
            "the air",
            "Timber is renewable because it is a biological rather than a "
            "mineral resource",
        ],
        "correct_index": 1,
        "why": "A resource is only renewable if it is replaced at least as "
               "fast as it is used, which for timber means replanting.",
    },
    {
        "id": "ks4-earths-resources-s04",
        "subtopic_slug": "earths-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which action would NOT help to use metals more sustainably?",
        "options": [
            "Recycling metal from products at the end of their life",
            "Developing extraction processes that use less energy",
            "Replacing a scarce metal with a more abundant material",
            "Extracting ore faster so that reserves are cleared sooner",
        ],
        "correct_index": 3,
        "why": "Sustainable use means making a finite reserve last, so "
               "speeding up its depletion works against every other measure.",
    },
    {
        "id": "ks4-earths-resources-h01",
        "subtopic_slug": "earths-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Sustainable development means closing "
                "every mine and factory so that nothing is used up.' Suggest "
                "what is wrong with this statement.",
        "options": [
            "It is correct, because any use of a finite resource is "
            "unsustainable",
            "It is wrong, because mining does no environmental damage at all",
            "It is wrong, because factories do not use finite resources",
            "It is wrong, because present needs must still be met",
        ],
        "correct_index": 3,
        "why": "Sustainable development balances today's economic and social "
               "needs against protecting resources for the future.",
    },
    {
        "id": "ks4-earths-resources-h02",
        "subtopic_slug": "earths-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper can be obtained by mining new ore or by recycling "
                "scrap. Which comparison is a fair judgement of the two?",
        "options": [
            "Mining is always better because recycled copper conducts "
            "electricity poorly",
            "Recycling saves ore and energy, but scrap must be collected "
            "and sorted",
            "Recycling has no environmental impact of any kind, so it is "
            "always best",
            "Mining and recycling use identical amounts of energy per tonne "
            "of copper",
        ],
        "correct_index": 1,
        "why": "Recycling avoids mining and uses far less energy than "
               "extraction, but collecting and sorting scrap still costs "
               "energy.",
    },
    {
        "id": "ks4-earths-resources-h03",
        "subtopic_slug": "earths-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon capture and storage is fitted to some power stations. "
                "Explain how it supports sustainable development.",
        "options": [
            "It stops carbon dioxide from the burnt fuel reaching the air",
            "It turns the fossil fuel being burnt back into a renewable "
            "resource",
            "It removes all of the sulfur dioxide produced when fuel burns",
            "It allows a fossil fuel to be re-formed underground within a "
            "few years",
        ],
        "correct_index": 0,
        "why": "Capturing and storing the carbon dioxide released reduces "
               "the build-up of a greenhouse gas without cutting off supply.",
    },
    {
        "id": "ks4-earths-resources-h04",
        "subtopic_slug": "earths-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two routes make the same product. Route A converts 90% of "
                "the mass of its reactants into the desired product; route B "
                "converts 40%. Which statement about route A is correct?",
        "options": [
            "Route A must also use less energy than route B in every case",
            "Route A must give a faster reaction because more product forms",
            "Route A has the higher atom economy, so makes less waste",
            "Route A must have a higher percentage yield than route B does",
        ],
        "correct_index": 2,
        "why": "Atom economy measures how much of the reactant mass ends up "
               "in the useful product, so a high value means little waste.",
    },
    # ── potable-water ── BASE (foundation, not triple) ───────────────────
    {
        "id": "ks4-potable-water-e01",
        "subtopic_slug": "potable-water",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In UK fresh water treatment, in which order are the three "
                "main stages carried out?",
        "options": [
            "Filtration, then chlorination, then sedimentation",
            "Sedimentation, then filtration, then chlorination",
            "Chlorination, then sedimentation, then filtration",
            "Filtration, then sedimentation, then chlorination",
        ],
        "correct_index": 1,
        "why": "Large solids settle out first, finer particles are filtered "
               "next, and the water is only sterilised once it is clear.",
    },
    {
        "id": "ks4-potable-water-e02",
        "subtopic_slug": "potable-water",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What is added to water in the final stage of treatment, and "
                "why?",
        "options": [
            "Sand, to trap the smallest solid particles still present",
            "Aluminium sulfate, to make fine particles clump together",
            "Sodium chloride, to improve the taste of the treated water",
            "Chlorine, to kill harmful microorganisms in the water",
        ],
        "correct_index": 3,
        "why": "A small dose of chlorine sterilises the water and goes on "
               "protecting it as it travels through the pipes.",
    },
    {
        "id": "ks4-potable-water-e03",
        "subtopic_slug": "potable-water",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the purpose of passing water through beds of sand and "
                "gravel.",
        "options": [
            "To remove fine solid particles that did not settle out",
            "To remove dissolved salts such as sodium chloride",
            "To kill bacteria and viruses in the water supply",
            "To lower the temperature of the water before it is stored",
        ],
        "correct_index": 0,
        "why": "Filtration traps the small suspended particles that are too "
               "light to sink during sedimentation.",
    },
    {
        "id": "ks4-potable-water-e04",
        "subtopic_slug": "potable-water",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium sulfate is sometimes added to water in the "
                "settling tanks. What does it do?",
        "options": [
            "It dissolves the sand so that the water passes through more "
            "quickly",
            "It kills any bacteria that survive the filtration stage",
            "It makes fine particles clump together so they settle faster",
            "It removes the taste of chlorine from the finished water",
        ],
        "correct_index": 2,
        "why": "A coagulant makes suspended particles stick together into "
               "larger clumps, which sink far more quickly.",
    },
    {
        "id": "ks4-potable-water-s01",
        "subtopic_slug": "potable-water",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Seawater is forced at high pressure through a membrane that "
                "lets water through but blocks dissolved salts. Name this "
                "process.",
        "options": [
            "Filtration through sand",
            "Simple distillation",
            "Reverse osmosis",
            "Fractional distillation",
        ],
        "correct_index": 2,
        "why": "Reverse osmosis uses pressure to push water through a "
               "semi-permeable membrane, leaving the dissolved salts behind.",
    },
    {
        "id": "ks4-potable-water-s02",
        "subtopic_slug": "potable-water",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why desalination of seawater is not widely used to "
                "supply drinking water in the UK.",
        "options": [
            "Desalination cannot remove all of the salt dissolved in seawater",
            "It uses a lot of energy, and cheaper fresh water is available",
            "There is no coastline in the UK close enough to the largest "
            "cities",
            "Desalinated water is not safe to drink without further treatment",
        ],
        "correct_index": 1,
        "why": "Distillation and reverse osmosis both need large amounts of "
               "energy, so they are only worth the cost where water is "
               "scarce.",
    },
    {
        "id": "ks4-potable-water-s03",
        "subtopic_slug": "potable-water",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In sewage treatment, air is pumped through the liquid "
                "effluent. Explain why.",
        "options": [
            "The oxygen reacts with the chlorine to sterilise the effluent",
            "The bubbles lift the remaining solids so they can be skimmed off",
            "The oxygen dissolves the sludge so it does not have to be "
            "removed",
            "Aerobic bacteria need oxygen to break down the organic matter",
        ],
        "correct_index": 3,
        "why": "Aerobic digestion relies on bacteria that use dissolved "
               "oxygen to break organic matter down into carbon dioxide and "
               "water.",
    },
    {
        "id": "ks4-potable-water-s04",
        "subtopic_slug": "potable-water",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student distils a sample of pond water and collects the "
                "distillate. Which observation shows the distillate is pure "
                "water?",
        "options": [
            "It boils at exactly 100 °C at normal atmospheric pressure",
            "It is colourless and has no smell when it is collected",
            "It leaves a white solid behind when a drop is evaporated",
            "It has a pH of 7 when tested with universal indicator",
        ],
        "correct_index": 0,
        "why": "A pure substance boils at a single fixed temperature, which "
               "for water at atmospheric pressure is 100 °C.",
    },
    {
        "id": "ks4-potable-water-h01",
        "subtopic_slug": "potable-water",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Distillation and reverse osmosis are both used to make fresh "
                "water from seawater. Which comparison is correct?",
        "options": [
            "Both need a lot of energy - one to boil water, one to pump it",
            "Distillation needs energy but reverse osmosis needs almost none",
            "Reverse osmosis removes salt but distillation leaves salt behind",
            "Neither method can give water fit to drink without added "
            "minerals",
        ],
        "correct_index": 0,
        "why": "Distillation costs energy as heat and reverse osmosis costs "
               "energy as pressure, which is why both are expensive.",
    },
    {
        "id": "ks4-potable-water-h02",
        "subtopic_slug": "potable-water",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the chlorination stage could be carried out "
                "before sedimentation without changing the final result. "
                "Explain why this is wrong.",
        "options": [
            "Chlorine reacts with sand and gravel, so the filters would be "
            "destroyed",
            "Chlorine only works on water that has already been boiled and "
            "cooled",
            "Suspended solids would shield microbes and use up the chlorine",
            "Sedimentation only works in water that contains no chlorine "
            "at all",
        ],
        "correct_index": 2,
        "why": "Chlorine must act on clear water: solids left in suspension "
               "protect microorganisms and consume the chlorine first.",
    },
    {
        "id": "ks4-potable-water-h03",
        "subtopic_slug": "potable-water",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sewage works digest the liquid effluent aerobically but the "
                "sludge anaerobically. Which statement explains this choice?",
        "options": [
            "Anaerobic bacteria cannot survive anywhere that liquid water is "
            "present",
            "Air cannot be pumped through thick sludge, but it can through "
            "effluent",
            "The effluent contains no organic matter, so aerobic bacteria "
            "are enough",
            "Aerobic digestion of sludge would produce a poisonous gas in "
            "the tanks",
        ],
        "correct_index": 1,
        "why": "Aerobic digestion needs oxygen mixed right through the "
               "material, which is practical for liquid effluent but not "
               "for dense sludge.",
    },
    {
        "id": "ks4-potable-water-h04",
        "subtopic_slug": "potable-water",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water from a borehole contains harmful bacteria but only "
                "safe, low levels of dissolved minerals. Which treatment is "
                "sufficient to make it potable?",
        "options": [
            "Distil it, so that all of the dissolved minerals are removed",
            "Pass it through a reverse osmosis membrane at high pressure",
            "Add aluminium sulfate and allow the minerals to settle out",
            "Sterilise it, for example with a small dose of chlorine",
        ],
        "correct_index": 3,
        "why": "Potable water only has to be safe to drink, so with the "
               "minerals already at acceptable levels only the microbes "
               "must go.",
    },
    # ── life-cycle-assessment ── BASE (foundation, not triple) ───────────
    {
        "id": "ks4-life-cycle-assessment-e01",
        "subtopic_slug": "life-cycle-assessment",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is NOT one of the four stages assessed in a "
                "life cycle assessment?",
        "options": [
            "Extracting and processing the raw materials",
            "Manufacturing the product and its packaging",
            "Disposal of the product at the end of its life",
            "The advertising used to sell the finished product",
        ],
        "correct_index": 3,
        "why": "An LCA covers raw materials, manufacture, use and disposal - "
               "marketing is not a stage in the product's physical life.",
    },
    {
        "id": "ks4-life-cycle-assessment-e02",
        "subtopic_slug": "life-cycle-assessment",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A life cycle assessment is often described as 'cradle to "
                "grave'. What does this mean?",
        "options": [
            "Only the manufacturing stage is examined in detail",
            "Every stage from raw material to disposal is included",
            "Only the impacts after the product is sold are counted",
            "The product is followed for exactly its guaranteed lifetime",
        ],
        "correct_index": 1,
        "why": "The phrase means the assessment runs from the first "
               "extraction of raw material to the final disposal.",
    },
    {
        "id": "ks4-life-cycle-assessment-e03",
        "subtopic_slug": "life-cycle-assessment",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Mining bauxite to obtain aluminium belongs to which stage of "
                "a life cycle assessment?",
        "options": [
            "Manufacturing and packaging the product",
            "Use over the product's lifetime",
            "Extracting the raw materials",
            "Disposal at the end of its life",
        ],
        "correct_index": 2,
        "why": "Digging the ore out of the ground is the first stage, before "
               "any manufacturing has begun.",
    },
    {
        "id": "ks4-life-cycle-assessment-e04",
        "subtopic_slug": "life-cycle-assessment",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these would be recorded under the 'use' stage of an "
                "LCA for a washing machine?",
        "options": [
            "The electricity and water it consumes over its lifetime",
            "The energy used to smelt the steel for its drum",
            "The fuel burnt by the lorry that delivers it to the shop",
            "The landfill space taken up when it is finally scrapped",
        ],
        "correct_index": 0,
        "why": "The use stage counts the resources the product consumes "
               "while it is doing its job in the customer's home.",
    },
    {
        "id": "ks4-life-cycle-assessment-s01",
        "subtopic_slug": "life-cycle-assessment",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Paper bags are made from a renewable material. Which "
                "statement is supported by a full LCA of paper and plastic "
                "bags?",
        "options": [
            "Paper bags always have a lower total impact than plastic bags",
            "Paper bags take more energy to make and are heavier to move",
            "Plastic bags cannot be reused, so they are used only once each",
            "Paper bags cause no environmental impact because they biodegrade",
        ],
        "correct_index": 1,
        "why": "A renewable raw material does not guarantee a lower total "
               "impact - paper's manufacturing and transport costs are "
               "higher.",
    },
    {
        "id": "ks4-life-cycle-assessment-s02",
        "subtopic_slug": "life-cycle-assessment",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An LCA of a kettle finds that 8% of its lifetime energy is "
                "used in manufacture and 89% while it is boiling water. Which "
                "stage is the 'hot spot'?",
        "options": [
            "The use stage, because it dominates the lifetime energy",
            "The manufacturing stage, because that is where energy is bought",
            "The disposal stage, because the remaining 3% is hardest to "
            "control",
            "The raw materials stage, because metals must first be extracted",
        ],
        "correct_index": 0,
        "why": "The hot spot is the stage carrying the largest share of the "
               "impact, so improving efficiency in use matters most here.",
    },
    {
        "id": "ks4-life-cycle-assessment-s03",
        "subtopic_slug": "life-cycle-assessment",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Give one reason why the harm caused to wildlife by plastic "
                "litter is difficult to include in an LCA.",
        "options": [
            "Plastic litter has no effect on wildlife that can be observed",
            "Litter belongs to the manufacturing stage, which is never "
            "assessed",
            "Wildlife harm is measured in kilograms, so it cannot be compared",
            "It is hard to put a number on, unlike energy used or mass of "
            "waste",
        ],
        "correct_index": 3,
        "why": "LCAs compare quantities that can be measured, and some real "
               "impacts cannot easily be reduced to a number.",
    },
    {
        "id": "ks4-life-cycle-assessment-s04",
        "subtopic_slug": "life-cycle-assessment",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company publishes an LCA of its drinks bottle covering "
                "only manufacture and disposal. What is the main criticism of "
                "this LCA?",
        "options": [
            "It should have used a different unit for measuring energy",
            "Manufacture and disposal are the only stages worth assessing",
            "It leaves out raw materials and use, so is not cradle to grave",
            "Only an independent laboratory is permitted to publish LCA data",
        ],
        "correct_index": 2,
        "why": "A life cycle assessment must cover all four stages; missing "
               "one out can hide the largest impact of all.",
    },
    {
        "id": "ks4-life-cycle-assessment-h01",
        "subtopic_slug": "life-cycle-assessment",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student concludes: 'Recycling a material always gives the "
                "lowest environmental impact.' Evaluate this statement.",
        "options": [
            "Correct, because recycling never uses energy or produces waste",
            "Correct, because recycled material is identical to new material",
            "Wrong, because recycling uses energy too - reducing use can beat "
            "it",
            "Wrong, because recycled products are always of a much poorer "
            "quality",
        ],
        "correct_index": 2,
        "why": "Recycling still needs collecting, sorting and reprocessing, "
               "so using less in the first place can have a smaller total "
               "impact.",
    },
    {
        "id": "ks4-life-cycle-assessment-h02",
        "subtopic_slug": "life-cycle-assessment",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An LCA shows a new phone uses 20% less electricity in use "
                "but needs a rarer metal mined from deeper ore. Which "
                "conclusion is justified?",
        "options": [
            "The new phone is definitely better, because it uses less "
            "electricity",
            "The new phone is definitely worse, because mining is the worst "
            "stage",
            "The two phones must have identical impacts because the changes "
            "cancel",
            "The two changes must be weighed against each other before "
            "deciding",
        ],
        "correct_index": 3,
        "why": "An LCA compares total impact across all stages, so a saving "
               "at one stage only counts if it outweighs the extra cost at "
               "another.",
    },
    {
        "id": "ks4-life-cycle-assessment-h03",
        "subtopic_slug": "life-cycle-assessment",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Kettle A uses 1.2 kWh per week and lasts 3 years. Kettle B "
                "uses 1.0 kWh per week and lasts 6 years. Which further "
                "information is most needed before choosing between them?",
        "options": [
            "The energy used to manufacture and dispose of each kettle",
            "The colour and the shape of each kettle's plastic casing",
            "The price that the shop paid for each of the two kettles",
            "The number of homes in the country that already own a kettle",
        ],
        "correct_index": 0,
        "why": "Kettle B saves energy in use and lasts longer, so only the "
               "manufacturing and disposal impacts can complete the "
               "cradle-to-grave comparison.",
    },
    {
        "id": "ks4-life-cycle-assessment-h04",
        "subtopic_slug": "life-cycle-assessment",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An LCA identifies packaging as the largest source of waste "
                "for a cereal product. Which change targets that hot spot "
                "most directly?",
        "options": [
            "Sourcing the grain from farms that are closer to the factory",
            "Redesigning the box to use less card and no plastic liner",
            "Printing the recycling instructions in larger type on the box",
            "Running the factory ovens for a shorter time at a higher heat",
        ],
        "correct_index": 1,
        "why": "An LCA is used to find the stage with the biggest impact so "
               "that redesign effort goes where it saves the most.",
    },
    # ── reducing-use-of-resources ── BASE (foundation, not triple) ───────
    {
        "id": "ks4-reducing-use-of-resources-e01",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is an example of reuse rather than recycling?",
        "options": [
            "Refilling a glass bottle with milk and using it again",
            "Melting glass bottles down to make new glass jars",
            "Crushing glass bottles to make aggregate for roads",
            "Burning waste glass packaging to generate electricity",
        ],
        "correct_index": 0,
        "why": "Reuse keeps the object itself in service, whereas recycling "
               "breaks the material down and remakes it into something new.",
    },
    {
        "id": "ks4-reducing-use-of-resources-e02",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which material can be recycled again and again without any "
                "loss of quality?",
        "options": [
            "Paper, because the fibres are replaced each time",
            "Poly(ethene), because it melts at a low temperature",
            "Glass, because it can be melted and re-formed",
            "Cardboard, because it is made from renewable trees",
        ],
        "correct_index": 2,
        "why": "Glass can be melted down and re-formed indefinitely, unlike "
               "paper whose fibres shorten with every cycle.",
    },
    {
        "id": "ks4-reducing-use-of-resources-e03",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Give the main reason why mixed plastic waste is difficult to "
                "recycle.",
        "options": [
            "Plastics cannot be melted once they have been moulded",
            "There are many different polymers that must be sorted first",
            "Plastics are made from renewable materials, so it is not worth "
            "it",
            "All plastics decompose in landfill within a few months anyway",
        ],
        "correct_index": 1,
        "why": "Different polymers behave differently when melted, so mixed "
               "plastics must be separated by type before reprocessing.",
    },
    {
        "id": "ks4-reducing-use-of-resources-e04",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Metal ores are described as finite. What does this mean for "
                "recycling metals?",
        "options": [
            "Recycling is unnecessary, because more ore forms all the time",
            "Recycling is impossible, because metals corrode in the ground",
            "Recycling is only worthwhile for metals that are cheap to mine",
            "Recycling matters, because ore reserves will eventually run out",
        ],
        "correct_index": 3,
        "why": "Ores took millions of years to form and are not replaced, so "
               "every tonne recycled is a tonne that need not be mined.",
    },
    {
        "id": "ks4-reducing-use-of-resources-s01",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cafe replaces disposable cups with cups that customers "
                "return, wash and use again. Which of the three Rs does this "
                "best describe?",
        "options": [
            "Recycle, because the cups are collected after use",
            "Reduce, because each cup is made from less material",
            "Neither - washing the cups uses more water than it saves",
            "Reuse, because the same cup is used many times over",
        ],
        "correct_index": 3,
        "why": "Reuse means the same object serves again and again without "
               "being broken down and reprocessed.",
    },
    {
        "id": "ks4-reducing-use-of-resources-s02",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Recycled paper cannot be recycled endlessly. Explain why.",
        "options": [
            "The fibres get shorter each time, so the paper gets weaker",
            "The ink cannot be removed, so the paper darkens each time",
            "Paper is a finite resource, so supplies of it soon run out",
            "Recycling paper needs more energy than making it from trees",
        ],
        "correct_index": 0,
        "why": "Each cycle shortens the cellulose fibres, so recycled paper "
               "eventually becomes too weak to be useful.",
    },
    {
        "id": "ks4-reducing-use-of-resources-s03",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one problem that makes recycling metals from "
                "electronic devices difficult.",
        "options": [
            "Metals lose their conductivity once they have been melted down",
            "Recycled metals cannot be used in any structural application",
            "A device contains many different metals that must be separated",
            "Metals extracted from ore are cheaper than any recycled metal",
        ],
        "correct_index": 2,
        "why": "Recycling needs the metals sorted, and a circuit board mixes "
               "many different metals in very small amounts.",
    },
    {
        "id": "ks4-reducing-use-of-resources-s04",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Biodegradable packaging that ends up buried in landfill can "
                "still cause a problem. Suggest what it is.",
        "options": [
            "It takes up more landfill space than ordinary plastic packaging",
            "It decomposes without air and releases methane, a greenhouse gas",
            "It cannot decompose at all once it is buried below the surface",
            "It releases the carbon dioxide it absorbed while it was growing",
        ],
        "correct_index": 1,
        "why": "Buried waste breaks down anaerobically, and the methane this "
               "releases is a powerful greenhouse gas.",
    },
    {
        "id": "ks4-reducing-use-of-resources-h01",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'The greenest thing a shopper can do is "
                "put everything in the recycling bin.' Evaluate this claim.",
        "options": [
            "Correct - recycling is the top of the three Rs hierarchy",
            "Wrong - buying less saves more than recycling does",
            "Wrong - recycling is worse for the environment than sending "
            "waste to landfill",
            "Correct - recycling uses no energy, so nothing can beat it",
        ],
        "correct_index": 1,
        "why": "Reduce comes first in the hierarchy because waste that is "
               "never created needs no energy to deal with at all.",
    },
    {
        "id": "ks4-reducing-use-of-resources-h02",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A council can either fund a campaign to cut packaging or "
                "open more recycling centres. Which is likely to cut "
                "environmental impact most, and why?",
        "options": [
            "More recycling centres, because recycling has no impact of its "
            "own",
            "More recycling centres, because they save the cost of collection",
            "Neither, because packaging and recycling have equal impacts",
            "The campaign, because reducing waste avoids making it at all",
        ],
        "correct_index": 3,
        "why": "Reducing avoids both the manufacturing impact and the "
               "reprocessing impact, while recycling only avoids the first.",
    },
    {
        "id": "ks4-reducing-use-of-resources-h03",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drinks maker redesigns a bottle so it uses 20% less "
                "plastic and can be returned and refilled ten times. Explain "
                "why this beats simply recycling the old bottle.",
        "options": [
            "Because refilled bottles never need to be washed or transported",
            "Because recycling plastic is impossible once a bottle is used",
            "Because it reduces AND reuses, and both come before recycling",
            "Because thinner plastic decomposes completely in landfill sites",
        ],
        "correct_index": 2,
        "why": "The redesign cuts the material used and keeps the same bottle "
               "in service, avoiding the reprocessing energy recycling needs.",
    },
    {
        "id": "ks4-reducing-use-of-resources-h04",
        "subtopic_slug": "reducing-use-of-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a car manufacturer may still prefer newly "
                "extracted aluminium to recycled aluminium for some parts.",
        "options": [
            "Recycled metal may contain other metals that alter its "
            "properties",
            "Recycled aluminium always costs more per tonne than new "
            "aluminium",
            "Recycled aluminium cannot be melted, so it cannot be cast into "
            "shape",
            "New aluminium is a renewable resource, so supply is never "
            "limited",
        ],
        "correct_index": 0,
        "why": "Scrap is rarely one pure metal, and the traces left after "
               "sorting can change the strength a safety part depends on.",
    },
    # ── corrosion-prevention ── TRIPLE ONLY (foundation tier) ────────────
    {
        "id": "ks4-corrosion-prevention-e01",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which two substances must BOTH be present for iron to rust?",
        "options": [
            "Oxygen and carbon dioxide",
            "Water and carbon dioxide",
            "Oxygen and water",
            "Water and dissolved salt",
        ],
        "correct_index": 2,
        "why": "Rusting is the reaction of iron with oxygen and water "
               "together; neither one on its own is enough.",
    },
    {
        "id": "ks4-corrosion-prevention-e02",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the substance formed when iron rusts.",
        "options": [
            "Iron(II) hydroxide only",
            "Anhydrous iron(III) oxide",
            "Iron(II) carbonate",
            "Hydrated iron(III) oxide",
        ],
        "correct_index": 3,
        "why": "Rust is hydrated iron(III) oxide, Fe2O3.xH2O, formed when "
               "iron reacts with oxygen and water together.",
    },
    {
        "id": "ks4-corrosion-prevention-e03",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which method of preventing rust works only as a barrier, "
                "with no sacrificial protection?",
        "options": [
            "Galvanising a steel bucket with zinc",
            "Greasing the chain on a bicycle",
            "Bolting magnesium blocks to a ship's hull",
            "Attaching zinc blocks to an underground pipe",
        ],
        "correct_index": 1,
        "why": "Grease keeps oxygen and water off the metal, but it does not "
               "corrode in the iron's place.",
    },
    {
        "id": "ks4-corrosion-prevention-e04",
        "subtopic_slug": "corrosion-prevention",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Aluminium is more reactive than iron, yet aluminium window "
                "frames do not corrode away. Explain why.",
        "options": [
            "A thin oxide layer forms and seals the surface",
            "Aluminium does not react with oxygen at all",
            "Aluminium is always painted before it is sold",
            "Aluminium reacts with water but not with oxygen",
        ],
        "correct_index": 0,
        "why": "Aluminium forms a dense, impermeable layer of aluminium "
               "oxide that stops oxygen and water reaching the metal below.",
    },
    {
        "id": "ks4-corrosion-prevention-s01",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Three iron nails are set up: A in boiled water covered by a "
                "layer of oil, B in dry air over a drying agent, C in "
                "ordinary tap water open to the air. Which nail rusts?",
        "options": [
            "Only nail C",
            "Only nail A",
            "Nails A and B",
            "All three nails",
        ],
        "correct_index": 0,
        "why": "Only C has oxygen and water together: boiling drives the air "
               "out of A, and the drying agent removes the water from B.",
    },
    {
        "id": "ks4-corrosion-prevention-s02",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Magnesium blocks are bolted to a buried steel pipeline. "
                "Explain how they protect the steel.",
        "options": [
            "The magnesium forms a paint-like film across the whole pipe",
            "Magnesium is more reactive, so it corrodes instead of the iron",
            "Magnesium is less reactive, so the iron corrodes away first",
            "The magnesium removes dissolved oxygen from the surrounding soil",
        ],
        "correct_index": 1,
        "why": "In sacrificial protection the more reactive metal is "
               "oxidised in place of the iron, and is replaced when used up.",
    },
    {
        "id": "ks4-corrosion-prevention-s03",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A tin-plated steel food can is badly dented and the tin "
                "layer is broken. Explain why the steel then rusts quickly.",
        "options": [
            "Tin is more reactive than iron, so it speeds up the rusting",
            "The dent traps food acids that dissolve the iron directly",
            "Tin reacts with iron to form an alloy that rusts very fast",
            "Tin is less reactive than iron, so the iron corrodes first",
        ],
        "correct_index": 3,
        "why": "Tin only works as a barrier - once it is broken the exposed "
               "iron is the more reactive metal and is attacked first.",
    },
    {
        "id": "ks4-corrosion-prevention-s04",
        "subtopic_slug": "corrosion-prevention",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a sacrificial magnesium block on a ship's hull "
                "must be inspected and replaced regularly.",
        "options": [
            "The block dissolves in seawater without reacting at all",
            "The block becomes coated in paint and stops working",
            "The block is used up as it corrodes in place of the steel",
            "The block turns into iron once all the magnesium has reacted",
        ],
        "correct_index": 2,
        "why": "Sacrificial protection works by consuming the more reactive "
               "metal, so the block is gradually destroyed and must be "
               "renewed.",
    },
    {
        "id": "ks4-corrosion-prevention-h01",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Galvanising works because zinc is less "
                "reactive than iron, so the iron is protected.' Identify the "
                "error.",
        "options": [
            "There is no error - zinc is less reactive than iron",
            "The error is that zinc is a barrier only, never sacrificial",
            "The error is that galvanising uses tin rather than zinc metal",
            "The error is that zinc is more reactive than iron, not less",
        ],
        "correct_index": 3,
        "why": "Sacrificial protection only works if the coating metal is "
               "above iron in the reactivity series, and zinc is.",
    },
    {
        "id": "ks4-corrosion-prevention-h02",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two steel bars are coated, one with zinc and one with "
                "copper. Both coatings are then scratched. Predict what "
                "happens at each scratch.",
        "options": [
            "Zinc-coated: the zinc corrodes; copper-coated: the steel "
            "corrodes",
            "Both bars corrode at the same rate, because both are scratched",
            "Zinc-coated: the steel corrodes; copper-coated: the copper "
            "corrodes",
            "Neither bar corrodes, because a scratch is too small to matter",
        ],
        "correct_index": 0,
        "why": "Zinc is more reactive than iron so it is attacked first, but "
               "copper is less reactive so the exposed iron goes instead.",
    },
    {
        "id": "ks4-corrosion-prevention-h03",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An engineer proposes bolting tin blocks to a steel oil rig "
                "leg to prevent corrosion. Evaluate this proposal.",
        "options": [
            "It will work, because any metal in contact protects the steel",
            "It will work, because tin forms an oxide layer over the steel",
            "It will not work - tin is less reactive, so the steel corrodes",
            "It will not work - tin melts in cold seawater and washes away",
        ],
        "correct_index": 2,
        "why": "A sacrificial block must be more reactive than iron; tin is "
               "less reactive, so it would make the steel corrode faster.",
    },
    {
        "id": "ks4-corrosion-prevention-h04",
        "subtopic_slug": "corrosion-prevention",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Forth Bridge is repainted continuously, while modern "
                "bridges are often built from galvanised steel. Compare the "
                "two approaches.",
        "options": [
            "Paint lasts longer than zinc outdoors, so repainting is cheaper",
            "Galvanising costs more at first but needs far less maintenance",
            "Both methods stop working completely as soon as they are damaged",
            "Galvanising can only be used indoors, so bridges must be painted",
        ],
        "correct_index": 1,
        "why": "A zinc coating both blocks oxygen and water and protects "
               "sacrificially, so it outlasts a paint film that must be "
               "renewed.",
    },
    # ── alloys-useful-materials ── TRIPLE ONLY (foundation tier) ─────────
    {
        "id": "ks4-alloys-useful-materials-e01",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Bronze is an alloy of copper and which other metal?",
        "options": [
            "Zinc",
            "Tin",
            "Nickel",
            "Chromium",
        ],
        "correct_index": 1,
        "why": "Bronze is copper with tin added, which makes it much harder "
               "than copper on its own.",
    },
    {
        "id": "ks4-alloys-useful-materials-e02",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Brass, used for trumpets and for taps, is an alloy of copper "
                "and which metal?",
        "options": [
            "Zinc",
            "Tin",
            "Lead",
            "Nickel",
        ],
        "correct_index": 0,
        "why": "Brass is copper and zinc; the zinc makes it harder than pure "
               "copper and gives it good acoustic properties.",
    },
    {
        "id": "ks4-alloys-useful-materials-e03",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Steel is made by adding a small amount of which element to "
                "iron?",
        "options": [
            "Chromium",
            "Nickel",
            "Tungsten",
            "Carbon",
        ],
        "correct_index": 3,
        "why": "Steel is iron with a little carbon, typically 0.1-1.5%, "
               "which makes it far harder and stronger than pure iron.",
    },
    {
        "id": "ks4-alloys-useful-materials-e04",
        "subtopic_slug": "alloys-useful-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which element is added to steel to make it stainless, so "
                "that it resists corrosion?",
        "options": [
            "Carbon",
            "Tin",
            "Chromium",
            "Zinc",
        ],
        "correct_index": 2,
        "why": "Stainless steel contains about 18% chromium along with "
               "nickel, and it is the chromium that gives the corrosion "
               "resistance.",
    },
    {
        "id": "ks4-alloys-useful-materials-s01",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A manufacturer needs steel for a drill bit that must be hard "
                "enough to cut metal. Which steel should be chosen?",
        "options": [
            "Low carbon steel, containing less than 0.3% carbon",
            "Pure iron, containing no carbon at all",
            "Stainless steel, containing 18% chromium and 8% nickel",
            "High carbon steel, containing more than 0.6% carbon",
        ],
        "correct_index": 3,
        "why": "Raising the carbon content makes steel harder, which is what "
               "a cutting tool needs even though it becomes more brittle.",
    },
    {
        "id": "ks4-alloys-useful-materials-s02",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why 9 carat gold is chosen for a ring worn every day, "
                "rather than 24 carat gold.",
        "options": [
            "9 carat gold contains more gold, so it lasts longer",
            "24 carat gold reacts with the skin and tarnishes quickly",
            "24 carat gold is pure and too soft, so it scratches easily",
            "9 carat gold has a higher melting point, so it is easier to cast",
        ],
        "correct_index": 2,
        "why": "Pure gold is soft because its identical atoms slide over one "
               "another easily; alloying it makes it hard enough to wear.",
    },
    {
        "id": "ks4-alloys-useful-materials-s03",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Aircraft bodies are made from aluminium alloyed with copper "
                "and magnesium rather than from pure aluminium. Suggest why.",
        "options": [
            "The alloy is much stronger while staying low in density",
            "The alloy is heavier, which makes the aircraft more stable",
            "The alloy conducts electricity better than pure aluminium",
            "The alloy melts at a lower temperature, so it is easy to shape",
        ],
        "correct_index": 0,
        "why": "Alloying gives the strength that pure aluminium lacks "
               "without adding much mass, which is what an airframe needs.",
    },
    {
        "id": "ks4-alloys-useful-materials-s04",
        "subtopic_slug": "alloys-useful-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Nitinol, an alloy of nickel and titanium, returns to its "
                "original shape when it is heated. Which use does this "
                "property suit?",
        "options": [
            "The cutting edge of a chisel used on hardwood",
            "A stent that is opened inside a blood vessel",
            "The heating element inside an electric kettle",
            "A weight used on a laboratory balance in school",
        ],
        "correct_index": 1,
        "why": "A shape memory alloy can be put in compressed and then "
               "spring back to its designed shape at body temperature.",
    },
    {
        "id": "ks4-alloys-useful-materials-h01",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A ring is stamped '9 carat'. Calculate the percentage of "
                "gold it contains.",
        "options": [
            "9.0%",
            "24.0%",
            "37.5%",
            "75.0%",
        ],
        "correct_index": 2,
        "why": "Carats are parts out of 24, so the gold content is "
               "9/24 × 100 = 37.5%.",
    },
    {
        "id": "ks4-alloys-useful-materials-h02",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'An alloy is a compound formed when two "
                "metals bond together in a fixed ratio.' Identify the error.",
        "options": [
            "Alloys are elements, not compounds, because they contain metals",
            "An alloy is a mixture - the proportions can be varied",
            "An alloy contains only one metal plus a non-metal such as carbon",
            "Alloys form ionic bonds, not covalent bonds, between the metals",
        ],
        "correct_index": 1,
        "why": "The atoms in an alloy are simply mixed into the metallic "
               "lattice, so the composition can be adjusted to tune the "
               "properties.",
    },
    {
        "id": "ks4-alloys-useful-materials-h03",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Stainless steel contains 18% chromium and 8% nickel by mass, "
                "with the rest iron. Calculate the percentage of iron.",
        "options": [
            "74%",
            "26%",
            "82%",
            "92%",
        ],
        "correct_index": 0,
        "why": "The percentages by mass must total 100, so the iron content "
               "is 100 - 18 - 8 = 74%.",
    },
    {
        "id": "ks4-alloys-useful-materials-h04",
        "subtopic_slug": "alloys-useful-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Surgical instruments must be hard, must keep a sharp edge "
                "and must not corrode when sterilised in steam. Which "
                "material is the best choice?",
        "options": [
            "Pure iron, because it is easily shaped into blades",
            "Bronze, because it is harder than pure copper is",
            "High carbon steel, because it is harder than any other steel",
            "Stainless steel, because it is hard and resists corrosion",
        ],
        "correct_index": 3,
        "why": "Chromium in stainless steel forms a protective oxide layer, "
               "so the instrument stays hard and sharp without rusting in "
               "steam.",
    },
    # ── ceramics-polymers-composites ── TRIPLE ONLY (foundation tier) ────
    {
        "id": "ks4-ceramics-polymers-composites-e01",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Soda-lime glass is made by heating a mixture of which three "
                "substances?",
        "options": [
            "Sand, boron trioxide and limestone",
            "Clay, limestone and sodium chloride",
            "Sand, boron trioxide and sodium chloride",
            "Sand, sodium carbonate and limestone",
        ],
        "correct_index": 3,
        "why": "Soda-lime glass comes from silicon dioxide (sand), sodium "
               "carbonate and limestone heated together.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e02",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which polymer is used for rigid milk bottles and drainpipes?",
        "options": [
            "Low density poly(ethene), which has branched chains",
            "A thermosetting polymer, which has cross-links",
            "High density poly(ethene), which has unbranched chains",
            "Poly(ethene) that has been reinforced with glass fibres",
        ],
        "correct_index": 2,
        "why": "Unbranched chains pack closely, so HDPE is denser, stiffer "
               "and stronger than the branched LDPE.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e03",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "What is a composite material?",
        "options": [
            "One material embedded in a second that binds it",
            "Two different metals melted together to give a harder solid",
            "A polymer that has been heated until it decomposes",
            "A ceramic made by firing wet clay in a hot kiln",
        ],
        "correct_index": 0,
        "why": "A composite has a reinforcement that carries the load held "
               "in a matrix, and it outperforms either part on its own.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-e04",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "How are clay ceramics such as bricks and tiles made?",
        "options": [
            "Molten clay is poured into a mould and left to set",
            "Wet clay is shaped and then fired in a hot kiln",
            "Powdered clay is compressed under very high pressure",
            "Clay is dissolved in acid and the solid is filtered off",
        ],
        "correct_index": 1,
        "why": "Firing drives out the water and fuses the particles "
               "together, leaving a hard, rigid ceramic.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s01",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why low density poly(ethene) is chosen for cling "
                "film rather than high density poly(ethene).",
        "options": [
            "LDPE has cross-links, which make it stretch further",
            "LDPE has a much higher melting point than HDPE has",
            "LDPE has branched chains, so it is soft and flexible",
            "LDPE chains pack more closely, so the film is much thinner",
        ],
        "correct_index": 2,
        "why": "Branches stop the chains packing closely, so the forces "
               "between them are weaker and the plastic is flexible.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s02",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Concrete is strong when squashed but weak when stretched. "
                "Explain why steel rods are set into concrete beams.",
        "options": [
            "Steel is strong under tension, so the beam resists both",
            "Steel makes the concrete set faster when it is poured",
            "Steel stops water reaching the concrete and cracking it",
            "Steel makes the beam heavier, so it is harder to bend",
        ],
        "correct_index": 0,
        "why": "The composite combines concrete's resistance to compression "
               "with steel's resistance to tension, which neither has alone.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s03",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Racing bicycle frames are made from carbon fibre reinforced "
                "plastic. Which pair of properties explains this choice?",
        "options": [
            "High density and high electrical conductivity",
            "High strength and low density",
            "Low melting point and high transparency",
            "High flexibility and high thermal conductivity",
        ],
        "correct_index": 1,
        "why": "CFRP is stronger than steel yet far less dense, so a frame "
               "can be both stiff and light.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-s04",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Bone is described as a natural composite. Name its two "
                "parts.",
        "options": [
            "Cellulose fibres held in a matrix of starch",
            "Carbon fibres held in a matrix of polymer",
            "Glass fibres held in a matrix of hard resin",
            "Collagen fibres in a mineral matrix",
        ],
        "correct_index": 3,
        "why": "Bone's protein fibres give it flexibility while the calcium "
               "phosphate mineral around them gives stiffness.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h01",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'A composite is a mixture, so its "
                "properties are always halfway between those of its two "
                "parts.' Identify the error.",
        "options": [
            "Composites are compounds, not mixtures, so this is wrong",
            "A composite beats both parts in at least one property",
            "A composite is always weaker than the stronger of its parts",
            "Composites have only one component, so the claim makes no sense",
        ],
        "correct_index": 1,
        "why": "The reinforcement and the matrix work together, so CFRP is "
               "stronger than either the fibres or the polymer alone.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h02",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A saucepan handle must stay rigid when the pan is hot. "
                "Explain which type of polymer must be used.",
        "options": [
            "A thermoplastic, because it softens and reshapes when hot",
            "A thermoplastic, because it has no cross-links between chains",
            "Either type, because a polymer does not conduct heat to the hand",
            "A thermosetting polymer - cross-links stop it melting",
        ],
        "correct_index": 3,
        "why": "Cross-links lock the chains into a rigid three-dimensional "
               "network, so a thermoset decomposes rather than softening.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h03",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of structure, why high density "
                "poly(ethene) has a higher melting point than low density "
                "poly(ethene).",
        "options": [
            "HDPE has cross-links between all of its chains, so they cannot "
            "move",
            "HDPE has shorter chains, so there are more chain ends to hold",
            "HDPE chains pack closely, so the forces between them are "
            "stronger",
            "HDPE chains are branched, which lets them lock into each other",
        ],
        "correct_index": 2,
        "why": "Unbranched chains lie close together, and the more contact "
               "between chains the more energy is needed to separate them.",
    },
    {
        "id": "ks4-ceramics-polymers-composites-h04",
        "subtopic_slug": "ceramics-polymers-composites",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An overhead power line needs an insulator that is hard, does "
                "not conduct electricity and copes with hot sun and frost. "
                "Which material best meets all three?",
        "options": [
            "A clay ceramic, which is hard and an electrical insulator",
            "A thermoplastic polymer, which softens on a hot summer day",
            "An aluminium alloy, which is light and resists corrosion well",
            "Soda-lime glass, which cracks when the temperature changes fast",
        ],
        "correct_index": 0,
        "why": "Ceramics are hard, chemically resistant and both thermal and "
               "electrical insulators, which is what an overhead insulator "
               "needs.",
    },
    # ── haber-process ── TRIPLE ONLY (foundation tier) ───────────────────
    {
        "id": "ks4-haber-process-e01",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "From which raw materials are the nitrogen and the hydrogen "
                "for the Haber process obtained?",
        "options": [
            "Nitrogen from the air and hydrogen from natural gas",
            "Nitrogen from natural gas and hydrogen from the air",
            "Both from the air, by fractional distillation of liquid air",
            "Both from natural gas, by heating it with steam and a catalyst",
        ],
        "correct_index": 0,
        "why": "Air is 78% nitrogen, while the hydrogen is made by reforming "
               "methane from natural gas with steam.",
    },
    {
        "id": "ks4-haber-process-e02",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which equation correctly represents the reaction in the "
                "Haber process?",
        "options": [
            "N2 + H2 ⇌ NH3",
            "N2 + 3H2 ⇌ 2NH3",
            "N2 + 2H2 ⇌ 2NH3",
            "2N2 + 3H2 ⇌ 2NH3",
        ],
        "correct_index": 1,
        "why": "One nitrogen molecule reacts with three hydrogen molecules "
               "to give two of ammonia, balancing 2 N and 6 H on each side.",
    },
    {
        "id": "ks4-haber-process-e03",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the temperature used in the Haber process.",
        "options": [
            "About 100 °C",
            "About 250 °C",
            "About 450 °C",
            "About 1500 °C",
        ],
        "correct_index": 2,
        "why": "About 450 °C is the compromise temperature: hot "
               "enough for a useful rate, cool enough for an acceptable "
               "yield.",
    },
    {
        "id": "ks4-haber-process-e04",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which catalyst is used in the Haber process?",
        "options": [
            "Nickel",
            "Platinum",
            "Vanadium(V) oxide",
            "Iron",
        ],
        "correct_index": 3,
        "why": "An iron catalyst speeds the reaction up and is cheap; "
               "vanadium(V) oxide belongs to the Contact process instead.",
    },
    {
        "id": "ks4-haber-process-s01",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The gases leaving the Haber reactor contain ammonia, "
                "nitrogen and hydrogen. Describe how the ammonia is "
                "separated.",
        "options": [
            "The mixture is filtered, and the ammonia is trapped by the "
            "filter",
            "The mixture is heated, and the ammonia boils off before the "
            "others",
            "The mixture is cooled, and the ammonia condenses to a liquid",
            "Water is added, and the nitrogen and hydrogen dissolve away in "
            "it",
        ],
        "correct_index": 2,
        "why": "Ammonia has a much higher boiling point than nitrogen or "
               "hydrogen, so cooling liquefies it while the others stay "
               "gases.",
    },
    {
        "id": "ks4-haber-process-s02",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the unreacted nitrogen and hydrogen leaving the "
                "reactor are pumped back in rather than released into the "
                "air.",
        "options": [
            "Releasing them would raise the equilibrium yield of the next "
            "pass through the reactor",
            "Releasing them would leave no catalyst inside the reactor for "
            "the next batch of gas",
            "Releasing them is impossible, because ammonia will not "
            "condense while they are present",
            "Releasing them would waste raw materials that cost energy and "
            "money to prepare",
        ],
        "correct_index": 3,
        "why": "The nitrogen was separated from liquefied air and the "
               "hydrogen made from natural gas, so venting either one throws "
               "away everything spent on making it.",
    },
    {
        "id": "ks4-haber-process-s03",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why nitrogen for the Haber process is obtained by "
                "fractional distillation of liquefied air.",
        "options": [
            "Nitrogen and oxygen have different boiling points",
            "Nitrogen is the only gas in air that can be liquefied",
            "Nitrogen reacts with the oxygen and is left behind pure",
            "Nitrogen dissolves in the liquid while oxygen stays a gas",
        ],
        "correct_index": 0,
        "why": "Cooling air until it liquefies and warming it slowly lets "
               "nitrogen boil off first, because it boils at a lower "
               "temperature.",
    },
    {
        "id": "ks4-haber-process-s04",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a temperature much lower than 450 °C is "
                "not used in the Haber process.",
        "options": [
            "Ammonia would decompose back into nitrogen and hydrogen",
            "The reaction would be too slow to be worth running",
            "The iron catalyst would react with the ammonia produced",
            "The equilibrium yield of ammonia would fall to almost zero",
        ],
        "correct_index": 1,
        "why": "A lower temperature would give a better yield, but the rate "
               "would be too slow for the plant to be economic.",
    },
    {
        "id": "ks4-haber-process-h01",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Running the Haber process at 100 degrees "
                "C would give both the highest yield and the fastest "
                "reaction.' Evaluate this claim.",
        "options": [
            "Correct - a lower temperature improves both the yield and the "
            "rate",
            "Wrong - a lower temperature would lower the yield of ammonia",
            "Wrong - the yield and the rate are not affected by temperature",
            "Wrong - the yield would rise but the rate would be far too slow",
        ],
        "correct_index": 3,
        "why": "The forward reaction is exothermic, so cooling favours "
               "ammonia, but the same cooling slows the reaction down - "
               "hence the 450 °C compromise.",
    },
    {
        "id": "ks4-haber-process-h02",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A company is offered a new catalyst that gives the same rate "
                "as iron does, but at 350 °C instead of 450 °C. "
                "Evaluate the benefit.",
        "options": [
            "No benefit - a catalyst cannot change the rate of the reaction",
            "No benefit - a lower temperature always lowers the yield of "
            "ammonia",
            "A benefit - a lower temperature gives a higher yield of ammonia",
            "A benefit - the new catalyst would shift the equilibrium to the "
            "right",
        ],
        "correct_index": 2,
        "why": "The forward reaction is exothermic, so running cooler raises "
               "the yield, and the new catalyst keeps the rate acceptable.",
    },
    {
        "id": "ks4-haber-process-h03",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Only about 15% of the gas is converted to ammonia each time "
                "it passes through the reactor, yet the plant's overall yield "
                "is about 98%. Explain how both figures can be true.",
        "options": [
            "The 98% figure counts the mass of nitrogen used, not of ammonia",
            "Unreacted gas is passed through the reactor again and again",
            "The catalyst raises the single-pass conversion to 98% over time",
            "The 15% figure is measured before the catalyst has warmed up",
        ],
        "correct_index": 1,
        "why": "Equilibrium limits each pass, but recycling the unreacted "
               "nitrogen and hydrogen converts almost all of it in the end.",
    },
    {
        "id": "ks4-haber-process-h04",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ammonia plants usually make their hydrogen from natural gas. "
                "Evaluate replacing this with hydrogen made by electrolysis "
                "of water using wind power.",
        "options": [
            "It cuts carbon dioxide emissions, but electricity is expensive",
            "It cuts carbon dioxide emissions and costs nothing to run at all",
            "It makes no difference, because the ammonia produced is the same",
            "It raises carbon dioxide emissions, because electrolysis burns "
            "fuel",
        ],
        "correct_index": 0,
        "why": "Steam reforming of methane releases carbon dioxide, so "
               "renewable hydrogen removes that emission - but the "
               "electricity still has to be paid for.",
    },
    # ── npk-fertilisers ── TRIPLE ONLY (foundation tier) ─────────────────
    {
        "id": "ks4-npk-fertilisers-e01",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which element in an NPK fertiliser is needed mainly for root "
                "development?",
        "options": [
            "Nitrogen",
            "Potassium",
            "Phosphorus",
            "Sulfur",
        ],
        "correct_index": 2,
        "why": "Phosphorus is used for root growth and for energy transfer "
               "inside the plant.",
    },
    {
        "id": "ks4-npk-fertilisers-e02",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which acid is reacted with ammonia to make ammonium sulfate "
                "fertiliser?",
        "options": [
            "Nitric acid",
            "Sulfuric acid",
            "Phosphoric acid",
            "Hydrochloric acid",
        ],
        "correct_index": 1,
        "why": "Ammonia is a base, so sulfuric acid neutralises it to give "
               "that acid's ammonium salt, (NH4)2SO4.",
    },
    {
        "id": "ks4-npk-fertilisers-e03",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Where does the potassium in an NPK fertiliser come from?",
        "options": [
            "It is made from potassium gas separated out of the air",
            "It is a by-product of the Haber process reactor",
            "It is made by reacting ammonia with potassium hydroxide",
            "It is mined as potassium chloride or potassium sulfate",
        ],
        "correct_index": 3,
        "why": "Potassium salts occur in natural mineral deposits, so they "
               "are extracted and purified rather than synthesised.",
    },
    {
        "id": "ks4-npk-fertilisers-e04",
        "subtopic_slug": "npk-fertilisers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A crop has yellow leaves and stunted growth. Which element "
                "is it most likely to be short of?",
        "options": [
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Calcium",
        ],
        "correct_index": 0,
        "why": "Nitrogen is needed to make proteins for leaves and stems, so "
               "a shortage shows first as yellowing and poor growth.",
    },
    {
        "id": "ks4-npk-fertilisers-s01",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which equation shows the manufacture of ammonium sulfate?",
        "options": [
            "NH3 + H2SO4 → NH4SO4",
            "2NH3 + H2SO4 → (NH4)2SO4",
            "NH3 + HNO3 → (NH4)2SO4",
            "2NH3 + 2H2SO4 → (NH4)2SO4",
        ],
        "correct_index": 1,
        "why": "Sulfuric acid supplies two hydrogen ions, so two ammonia "
               "molecules are needed and the equation then balances.",
    },
    {
        "id": "ks4-npk-fertilisers-s02",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fertiliser bag is labelled 20:10:10. What does this tell a "
                "farmer?",
        "options": [
            "The bag contains 20 kg of fertiliser in total",
            "The fertiliser should be applied 20 times a year",
            "The fertiliser contains only nitrogen and no other element",
            "It has twice as much nitrogen as phosphorus or potassium",
        ],
        "correct_index": 3,
        "why": "The three numbers give the N:P:K ratio, so the farmer can "
               "match the fertiliser to what the soil and crop need.",
    },
    {
        "id": "ks4-npk-fertilisers-s03",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Phosphate rock is treated with sulfuric acid before it is "
                "used in a fertiliser. Suggest why.",
        "options": [
            "It converts the insoluble rock into soluble compounds",
            "It removes the phosphorus so that only calcium is left",
            "It dries the rock so that it can be ground into a powder",
            "It neutralises the rock, which is strongly alkaline",
        ],
        "correct_index": 0,
        "why": "Plants take up mineral ions dissolved in soil water, so the "
               "phosphorus must be in a soluble form to be any use.",
    },
    {
        "id": "ks4-npk-fertilisers-s04",
        "subtopic_slug": "npk-fertilisers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "NPK fertilisers are made using integrated industrial "
                "processes. Explain what this means.",
        "options": [
            "Every compound in the fertiliser is made in one single reaction",
            "The fertiliser is made only from materials mined at one site",
            "Linked processes on one site feed products into each other",
            "The same catalyst is used for every reaction in the whole plant",
        ],
        "correct_index": 2,
        "why": "Ammonia from the Haber plant is fed straight into the acid "
               "reactions on the same site, saving transport and energy.",
    },
    {
        "id": "ks4-npk-fertilisers-h01",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'An NPK fertiliser is a single compound "
                "containing nitrogen, phosphorus and potassium.' Identify the "
                "error.",
        "options": [
            "NPK fertiliser is a blend of several different salts",
            "NPK fertiliser contains only nitrogen and phosphorus",
            "NPK fertiliser is an element, not a compound at all",
            "The K in NPK stands for calcium, not for potassium",
        ],
        "correct_index": 0,
        "why": "The three elements come from different salts, made or mined "
               "separately and then blended to the ratio required.",
    },
    {
        "id": "ks4-npk-fertilisers-h02",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer spreads fertiliser on a field the day before heavy "
                "rain is forecast. Predict the consequence and explain it.",
        "options": [
            "The rain will fix the fertiliser into the soil, so more of it is "
            "absorbed",
            "The rain will decompose the fertiliser into harmless nitrogen "
            "gas",
            "The fertiliser will be washed into the river, causing an algal "
            "bloom",
            "The rain will make the fertiliser more concentrated in the "
            "topsoil",
        ],
        "correct_index": 2,
        "why": "Soluble nitrate and phosphate leach out of soil in heavy "
               "rain, and the extra nutrients let algae grow rapidly.",
    },
    {
        "id": "ks4-npk-fertilisers-h03",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest how a buffer strip of grass and trees planted along "
                "a river bank reduces the impact of fertiliser use.",
        "options": [
            "It stops rain falling on the field, so no leaching can happen",
            "It reacts with nitrate in the river to turn it into nitrogen gas",
            "It raises the oxygen content of the river so that fish survive",
            "It takes up nutrients from run-off before they reach the water",
        ],
        "correct_index": 3,
        "why": "The plants absorb dissolved nitrate and phosphate from the "
               "run-off, so less nutrient reaches the river to feed algae.",
    },
    {
        "id": "ks4-npk-fertilisers-h04",
        "subtopic_slug": "npk-fertilisers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A soil test shows plenty of nitrate but very little "
                "potassium. The crop has brown leaf edges and poor fruit. "
                "Which fertiliser should be applied?",
        "options": [
            "Ammonium nitrate, to supply more nitrogen to the leaves",
            "Potassium sulfate, to supply the missing potassium",
            "Ammonium sulfate, to supply nitrogen and sulfur together",
            "Phosphoric acid, to supply phosphorus for root growth",
        ],
        "correct_index": 1,
        "why": "Brown leaf edges and poor fruit are signs of potassium "
               "deficiency, and the soil already has plenty of nitrogen.",
    },
    # ── alternative-metal-extraction ── HIGHER TIER (not triple) ─────────
    {
        "id": "ks4-alternative-metal-extraction-e01",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Which organisms are used in bioleaching?",
        "options": [
            "Hyperaccumulator plants",
            "Bacteria",
            "Fungi grown on the ore",
            "Algae in a shallow pond",
        ],
        "correct_index": 1,
        "why": "Bacteria oxidise the metal sulfide compounds in the ore, "
               "using them as their source of energy.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e02",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Bioleaching and phytomining are used on which kind of ore?",
        "options": [
            "High-grade ore that is rich in the metal",
            "Ore that contains no metal compounds at all",
            "Low-grade ore that is uneconomical to smelt",
            "Ore that has already been smelted once before",
        ],
        "correct_index": 2,
        "why": "Both methods concentrate metal from rock too poor for "
               "traditional smelting to be worth the fuel it would burn.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e03",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "What is a hyperaccumulator plant?",
        "options": [
            "A plant that takes up and concentrates metal ions",
            "A plant that grows faster than any other crop plant",
            "A plant that releases acid to dissolve rock around it",
            "A plant that survives without any water in dry soil",
        ],
        "correct_index": 0,
        "why": "Hyperaccumulators absorb metal ions through their roots and "
               "store them at high concentration in their shoots and leaves.",
    },
    {
        "id": "ks4-alternative-metal-extraction-e04",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Give the main reason why alternative extraction methods are "
                "being developed.",
        "options": [
            "Traditional smelting has been banned in most countries",
            "Bacteria and plants extract metals faster than smelting",
            "Low-grade ores contain more metal than high-grade ores",
            "High-grade ores are running out, leaving low-grade ores",
        ],
        "correct_index": 3,
        "why": "The rich ores are close to depletion, so metals must "
               "increasingly be won from rock with very little metal in it.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s01",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "State one significant disadvantage of phytomining.",
        "options": [
            "It cannot be used on land that is contaminated with metal",
            "It produces large amounts of acidic waste that must be treated",
            "It uses more electrical energy than electrolysis of the ore does",
            "It is very slow, because the plants must be grown and harvested",
        ],
        "correct_index": 3,
        "why": "A phytomining crop takes whole growing seasons, so the metal "
               "comes out far more slowly than from a conventional mine.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s02",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "State one significant disadvantage of bioleaching.",
        "options": [
            "It produces acidic waste that could reach groundwater",
            "It can only be used on ores that contain no sulfur at all",
            "It needs a higher temperature than smelting the ore does",
            "It produces the metal in a form that cannot be purified",
        ],
        "correct_index": 0,
        "why": "The leachate is an acidic solution, so it must be contained "
               "and treated or it will pollute the water around the site.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s03",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why phytomining can be described as carbon neutral "
                "in principle.",
        "options": [
            "Burning the plants releases no carbon dioxide at all",
            "The metal in the ash locks the carbon into a solid form",
            "The plants absorbed carbon dioxide as they were growing",
            "The bacteria in the soil take in the carbon dioxide given off",
        ],
        "correct_index": 2,
        "why": "The carbon dioxide given off when the crop is burnt is the "
               "carbon dioxide the crop took from the air while it grew.",
    },
    {
        "id": "ks4-alternative-metal-extraction-s04",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "In bioleaching of a copper sulfide ore, what do the bacteria "
                "actually do?",
        "options": [
            "They reduce the copper ions to copper metal in the ore",
            "They oxidise the sulfide, so copper ions dissolve in solution",
            "They eat the rock so that the copper is left behind as a solid",
            "They raise the temperature of the heap until the ore melts",
        ],
        "correct_index": 1,
        "why": "The bacteria oxidise the metal sulfide for energy, which "
               "releases the copper as ions into the acidic leachate.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h01",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student writes: 'Bioleaching produces pure copper metal "
                "directly from the ore.' Identify the error.",
        "options": [
            "It produces a solution of copper ions, not copper metal",
            "It produces copper oxide, which must then be electrolysed",
            "It produces copper sulfide, which must then be roasted in air",
            "It produces no copper at all - bioleaching only cleans the ore",
        ],
        "correct_index": 0,
        "why": "The bacteria only get the copper into solution as ions; the "
               "metal still has to be recovered from that leachate.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h02",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A former mine site has soil lightly contaminated with "
                "nickel, and no sulfide ore body. Which method suits it, and "
                "why?",
        "options": [
            "Bioleaching, because bacteria work on any soil containing metal",
            "Phytomining, because plants take up nickel and clean the soil",
            "Smelting, because the soil can simply be dug up and heated",
            "Neither, because nickel cannot be recovered once it is in soil",
        ],
        "correct_index": 1,
        "why": "Bioleaching bacteria need a sulfide ore, whereas "
               "hyperaccumulators lift nickel ions out of soil and "
               "remediate the land as they go.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h03",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Compare bioleaching with smelting for an ore containing only "
                "0.3% copper. Which comparison is correct?",
        "options": [
            "Smelting is cheaper, because the ore does not need crushing "
            "first",
            "Bioleaching is faster, because bacteria act on the whole heap "
            "at once",
            "Smelting produces no carbon dioxide, so it is the greener "
            "choice",
            "Bioleaching uses less energy, but takes much longer to work",
        ],
        "correct_index": 3,
        "why": "With so little metal per tonne, heating the rock is not worth "
               "the fuel, so the slow but low-energy biological route wins.",
    },
    {
        "id": "ks4-alternative-metal-extraction-h04",
        "subtopic_slug": "alternative-metal-extraction",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A metal occurs as an oxide in low-grade rock, and no plant "
                "is known that accumulates it. Predict which extraction route "
                "must be used.",
        "options": [
            "Phytomining, because any plant will take the metal up eventually",
            "Bioleaching, because bacteria will oxidise oxides as well as "
            "sulfides",
            "Traditional extraction, because neither alternative applies",
            "Neither, because a low-grade oxide ore can never be processed",
        ],
        "correct_index": 2,
        "why": "Bioleaching bacteria oxidise sulfides and phytomining needs "
               "a hyperaccumulator, so with neither available the ore must "
               "be reduced conventionally.",
    },
]
