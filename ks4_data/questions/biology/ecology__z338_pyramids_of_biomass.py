"""Biology · Ecology — the MRB-338 expansion, pyramids of biomass (4.7.4.2).

Triple-only content. The spec point asks students to CONSTRUCT as well as
interpret, so the weight falls on the drawing skills the existing rows do not
reach: the units, the scale, converting between a biomass and a bar width in
both directions, and scaling a quadrat sample up to a square metre. The harder
band handles the genuinely unusual shapes — an ocean chain whose level 1 bar is
narrower than its level 2 because the phytoplankton are replaced within days —
and the limits of what a pyramid is evidence for.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-pyramids-of-biomass-e05",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the units in which biomass is usually recorded for a "
                "pyramid of biomass.",
        "options": [
            "g/m² or kg/m²",
            "kJ/m²/year",
            "individuals per m²",
            "centimetres of bar width",
        ],
        "correct_index": 0,
        "why": "Biomass is a mass per unit area of ground or water, so it is "
               "quoted in grams or kilograms per square metre.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e06",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the trophic level whose bar is drawn at the bottom of "
                "every pyramid of biomass.",
        "options": [
            "The producers",
            "The top predators",
            "The decomposers",
            "The primary consumers alone",
        ],
        "correct_index": 0,
        "why": "Level 1 is always the base of the pyramid, because all the "
               "biomass above it passed through the producers first.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e07",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the group of organisms that can make the upper bar of a "
                "pyramid of biomass the wider one.",
        "options": [
            "Parasites feeding on a much larger host",
            "Decomposers living in the soil",
            "Producers growing in a deeply shaded woodland habitat",
            "Apex predators at the top of a chain",
        ],
        "correct_index": 0,
        "why": "A very large number of small parasites feeding on one host can "
               "together hold more biomass than the single host below them.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e08",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the diagram that shows how many organisms live at each "
                "trophic level.",
        "options": [
            "A pyramid of energy per year",
            "A pyramid of numbers",
            "A pyramid of biomass",
            "A food web",
        ],
        "correct_index": 1,
        "why": "A pyramid of numbers counts individuals, whereas a pyramid of "
               "biomass weighs the living material they are made of.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e09",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give one reason why biomass decreases at each higher trophic "
                "level.",
        "options": [
            "The organisms at the higher levels are smaller than those below them",
            "Energy is lost in respiration, so less biomass can be built above",
            "Producers take back some of the biomass they passed to the level above",
            "Decomposers strip biomass away from the upper levels but not from the lower ones",
        ],
        "correct_index": 1,
        "why": "Most of the biomass eaten is respired or egested, so only a "
               "small part of it becomes new tissue at the level above.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e10",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what biomass measures.",
        "options": [
            "The number of organisms living in one square metre of a given habitat",
            "The volume of space that the organisms at one level take up",
            "The mass of living material in an organism or a trophic level",
            "The energy released when a dried organism is burned completely",
        ],
        "correct_index": 2,
        "why": "Biomass is a mass of living material, which is why it is "
               "recorded in grams rather than in joules or in counts.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e11",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a pyramid of biomass is a more reliable model than "
                "a numbers pyramid.",
        "options": [
            "It is drawn to a proper scale, whereas a pyramid of numbers has no scale at all",
            "It counts the decomposers, which a pyramid of numbers leaves out",
            "It shows the energy at each level, which a count of individuals cannot",
            "It takes the size of each organism into account, not just how many",
        ],
        "correct_index": 3,
        "why": "One oak tree and one aphid count as one organism each, but their "
               "biomass differs by a factor of millions.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e12",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of pyramid that is a true pyramid shape for every "
                "food chain without exception.",
        "options": [
            "A pyramid of numbers",
            "A pyramid of biomass",
            "A pyramid of energy",
            "A pyramid of individuals counted",
        ],
        "correct_index": 2,
        "why": "Energy is lost at every transfer and none is added back, so the "
               "energy available must fall at each level up the chain.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e13",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Besides the mass of the samples, state one measurement needed "
                "before a pyramid of biomass can be drawn.",
        "options": [
            "The number of different species living at each of the trophic levels",
            "The area of ground the samples were collected from",
            "The length of time the organisms had lived in the habitat",
            "The temperature of the habitat on the day of collection",
        ],
        "correct_index": 1,
        "why": "Biomass is quoted per square metre, so the sampled area is "
               "needed to turn a sample mass into a figure for the level.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e14",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how the bars of a pyramid of biomass are arranged on "
                "the page.",
        "options": [
            "Level 1 at the bottom, with each bar above it centred on the one below",
            "Level 1 at the very top, with each bar below it centred on the one above",
            "The widest bar in the very middle, with the narrower bars above it and below it",
            "The bars side by side in a row, from the widest to the narrowest",
        ],
        "correct_index": 0,
        "why": "Producers form the base and each level is stacked centrally "
               "above it, so the narrowing shape can be read at a glance.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e15",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the top bar of a pyramid of biomass is sometimes "
                "too narrow to see.",
        "options": [
            "The top bar is drawn at half the scale used for the bars beneath it",
            "So little biomass reaches the top that the bar is a fraction of a millimetre",
            "Top predators are not counted, so their bar is left off the diagram",
            "The top level holds no biomass, so there is nothing at all to draw",
        ],
        "correct_index": 1,
        "why": "Three transfers can reduce the biomass to about a thousandth of "
               "the producers', which at a workable scale is well under 1 mm.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e16",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of biomass uses a scale of 1 cm to 50 "
                "g/m². Calculate the width of the bar for a level "
                "holding 400 g/m².",
        "options": [
            "4 cm",
            "20 cm",
            "8 cm",
            "50 cm",
        ],
        "correct_index": 2,
        "why": "400 ÷ 50 = 8, so the bar is 8 cm wide.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e17",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what every pyramid of biomass has in common, whatever the "
                "food chain.",
        "options": [
            "Every one has exactly four bars, one for each of the trophic levels",
            "Every one is drawn from the number of organisms that were counted at each level",
            "Every one has its widest bar in the middle of the finished diagram",
            "The producers are at the bottom and the bars are drawn to a scale",
        ],
        "correct_index": 3,
        "why": "The number of levels and the shape can vary, but level 1 is "
               "always the base and the widths always follow a stated scale.",
    },
    {
        "id": "ks4-pyramids-of-biomass-e18",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the shape of a true pyramid of biomass.",
        "options": [
            "Each bar is exactly the same width as the bar immediately below it",
            "Each bar is wider than the bar immediately below it",
            "The widest bar sits in the middle of the diagram",
            "Each bar is narrower than the bar immediately below it",
        ],
        "correct_index": 3,
        "why": "A true pyramid tapers upwards, which is what a falling biomass "
               "at each higher level produces.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-pyramids-of-biomass-s05",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A heathland pyramid of biomass has bars 10 cm, 1.4 cm and "
                "0.2 cm wide. Calculate the approximate percentage of the "
                "producers' biomass held by the secondary consumers.",
        "options": [
            "14%",
            "2%",
            "0.2%",
            "20%",
        ],
        "correct_index": 1,
        "why": "Bar width is proportional to biomass, so 0.2 ÷ 10 × 100 = "
               "2% without the scale being needed at all.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s06",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a hedgerow pyramid the level 2 bar is one twelfth the width "
                "of the level 1 bar. State what this tells you.",
        "options": [
            "About one twelfth of the producers' biomass became herbivore biomass",
            "One twelfth of the herbivores' own biomass had come from the producers below them",
            "Each herbivore is one twelfth the size of an individual producer",
            "One twelfth of the producers were eaten by herbivores that year",
        ],
        "correct_index": 0,
        "why": "Width stands for biomass, so the ratio of the widths is the "
               "share of the producers' biomass that the herbivores now hold.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s07",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student draws all four bars of a pyramid of biomass the same "
                "width. Explain what this diagram fails to show.",
        "options": [
            "Which of the four trophic levels the producers of the chain occupy",
            "The names of the organisms that belong at each of the four levels",
            "That the biomass falls at every level, which the pyramid exists to show",
            "The number of individual organisms that happen to live at each of the four levels",
        ],
        "correct_index": 2,
        "why": "Equal bars say that every level holds the same biomass, which "
               "hides the loss at each transfer that the diagram is drawn for.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s08",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A 0.25 m² sample of grassland yields 130 g of dried "
                "grass. Calculate the producer biomass in g/m².",
        "options": [
            "32.5 g/m²",
            "130 g/m²",
            "0.52 g/m²",
            "520 g/m²",
        ],
        "correct_index": 3,
        "why": "0.25 m² is a quarter of a square metre, so 130 × 4 = "
               "520 g/m².",
    },
    {
        "id": "ks4-pyramids-of-biomass-s09",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what a biomass pyramid and an energy pyramid each show "
                "for the same food chain.",
        "options": [
            "Biomass shows the flow over a year; energy shows the mass at one moment",
            "Biomass shows the mass present at one moment; energy shows the flow per year",
            "Both show exactly the same quantity, so either one can be drawn from the other's data",
            "Biomass counts the organisms and energy counts the joules in each one",
        ],
        "correct_index": 1,
        "why": "A biomass pyramid is a snapshot of standing mass, while an "
               "energy pyramid records how much energy passed through in a year.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s10",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a pyramid of biomass narrows upwards even though "
                "each level eats far more mass than its bar shows.",
        "options": [
            "Most of what is eaten is respired or egested, and little becomes tissue",
            "Each level eats far less mass than the level immediately below it holds in total",
            "Biomass is recorded once the organisms have finished digesting their meal",
            "The mass eaten is not counted, because only producers are ever weighed",
        ],
        "correct_index": 0,
        "why": "The bar records tissue built, not food consumed, and only about "
               "a tenth of a meal ends up as new tissue.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s11",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Biomass for a pyramid is found by drying samples. Suggest one "
                "reason the figure is an estimate rather than an exact value.",
        "options": [
            "Drying removes some of the living material along with all the water",
            "A balance is quite unable to weigh a dried sample to better than the nearest gram",
            "Only a few samples are dried, and the whole level is scaled up from them",
            "The organisms carry on respiring while they dry out inside the oven",
        ],
        "correct_index": 2,
        "why": "A quadrat covers a tiny fraction of a habitat, so scaling its "
               "mass up assumes the rest of the habitat matches the sample.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s12",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Producers hold 600 g/m², herbivores 60 g/m² and "
                "carnivores 9 g/m². Determine the three bar widths at a "
                "scale of 1 cm to 100 g/m².",
        "options": [
            "6 cm, 0.6 cm and 0.9 cm",
            "0.6 cm, 6 cm and 90 cm",
            "60 cm, 6 cm and 0.9 cm",
            "6 cm, 0.6 cm and 0.09 cm",
        ],
        "correct_index": 3,
        "why": "Each biomass is divided by 100: 600 gives 6 cm, 60 gives "
               "0.6 cm and 9 gives 0.09 cm.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s13",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why an ecologist studying a rare habitat may draw a "
                "numbers pyramid rather than a biomass pyramid.",
        "options": [
            "A pyramid of numbers gives the biomass of each level once it is drawn",
            "No organism has to be killed and dried, so the habitat is left intact",
            "A pyramid of numbers is the only diagram that puts producers first",
            "A pyramid of numbers works for a whole food web, whereas biomass needs a chain",
        ],
        "correct_index": 1,
        "why": "Measuring dry biomass means killing and drying the organisms, "
               "which is unacceptable where a population is already small.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s14",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of biomass shows the producers holding 95% of the "
                "whole chain's biomass. Explain what this tells you about the "
                "chain.",
        "options": [
            "Only a small share of the producers' biomass became consumer biomass",
            "The producers are the largest individual organisms that are present in the chain",
            "The chain has just two levels, because 95% leaves room for one more",
            "The producers respire about 95% of all the biomass they make each year",
        ],
        "correct_index": 0,
        "why": "If the producers hold 95%, every consumer level together holds "
               "only 5%, which is the loss at the transfers made visible.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s15",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why an ecologist draws a pyramid of biomass instead of "
                "simply listing the biomass value for each level.",
        "options": [
            "A list cannot be drawn to a scale, so the values would carry no units",
            "A pyramid gives the exact biomass, whereas a list of values is only an estimate",
            "The bar widths show the size of the drop between levels at a glance",
            "A pyramid includes the decomposers, which a list of values leaves out",
        ],
        "correct_index": 2,
        "why": "Drawing the values to scale turns a set of numbers into a shape "
               "that can be compared between levels and between habitats.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s16",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student's pyramid of biomass for a field has a level 2 bar "
                "wider than its level 1 bar. Suggest the two checks the student "
                "should make.",
        "options": [
            "Check the bars are centred and that the top bar is labelled",
            "Check the units are grams and that the organisms were weighed fresh",
            "Check the decomposers were included and that no fourth bar was left out",
            "Check the scale was applied correctly and that level 1 really is the producers",
        ],
        "correct_index": 3,
        "why": "On land the level 1 bar is almost always the widest, so an "
               "inverted base points to an arithmetic slip or a misplaced level.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s17",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a pyramid of biomass can be built for a marine food "
                "chain, where organisms cannot be collected from a fixed square "
                "of ground.",
        "options": [
            "Marine biomass is estimated from the number of fish caught in one net",
            "Samples are taken from a known volume of water and scaled to each square metre",
            "Marine pyramids carry no scale, because no area can be measured at sea",
            "The sea water is weighed along with the organisms and then subtracted",
        ],
        "correct_index": 1,
        "why": "A measured volume of water beneath a known area of surface gives "
               "the same per-square-metre figure a quadrat gives on land.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s18",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the bars of a pyramid of biomass are centred on one "
                "another rather than lined up along one edge.",
        "options": [
            "It makes the narrowing shape obvious, so the levels compare quickly",
            "It keeps the producers at the bottom, which edge-aligned bars cannot",
            "It is the only way to draw the bars to a scale that a reader is able to measure",
            "It leaves room for the decomposers to be drawn down one side of it",
        ],
        "correct_index": 0,
        "why": "Centring the bars produces the symmetrical taper that makes the "
               "fall in biomass between levels immediately readable.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-pyramids-of-biomass-h05",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An ocean pyramid of biomass shows phytoplankton at 4 "
                "g/m² and zooplankton at 21 g/m². Explain how this "
                "is possible.",
        "options": [
            "Zooplankton photosynthesise too, so they add biomass of their own",
            "Sea water supports extra mass, so an inverted pyramid is normal at sea",
            "The phytoplankton are eaten and regrown so fast that little is present at once",
            "The samples must have been mislabelled, as level 2 cannot exceed level 1",
        ],
        "correct_index": 2,
        "why": "A biomass pyramid is a snapshot: phytoplankton divide within a "
               "day, so a small standing mass can still feed a much larger one.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h06",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four levels hold 4500, 520, 48 and 3 g/m². Determine the "
                "scale needed if the widest bar is to be drawn 9 cm across.",
        "options": [
            "1 cm to 50 g/m²",
            "1 cm to 4500 g/m²",
            "1 cm to 9 g/m²",
            "1 cm to 500 g/m²",
        ],
        "correct_index": 3,
        "why": "4500 ÷ 9 = 500, so each centimetre must stand for 500 "
               "g/m².",
    },
    {
        "id": "ks4-pyramids-of-biomass-h07",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student concludes from a pyramid of biomass that the "
                "producers 'hold the most energy per gram'. Evaluate this "
                "conclusion.",
        "options": [
            "Unsupported — the pyramid shows the total mass at each level, not energy per gram",
            "Correct — the widest bar holds the most energy in every gram of its tissue",
            "Unsupported — energy per gram cannot be measured for any living organism",
            "Correct — producers store glucose, and glucose holds far more energy per gram than fat does",
        ],
        "correct_index": 0,
        "why": "A wide bar means a large total mass; it says nothing about how "
               "much energy one gram of that tissue would release.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h08",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of biomass is built from samples taken only in the "
                "sunniest corner of a meadow. Explain the effect on the producer "
                "bar and on the conclusions drawn.",
        "options": [
            "The producer bar is too narrow, because a sunny corner holds less water",
            "The producer bar is too wide, so every transfer looks less efficient than it is",
            "The producer bar is not affected in any way, because biomass is recorded per square metre",
            "Only the consumer bars are affected, because consumers move between areas",
        ],
        "correct_index": 1,
        "why": "The sunniest corner grows the most plant material, so scaling it "
               "up overstates level 1 and understates every transfer above it.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h09",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that a pyramid of biomass proves a tenth of "
                "the biomass is transferred between every pair of levels.",
        "options": [
            "It proves the tenth exactly, because the bar widths have all been drawn to a true scale",
            "It proves nothing, because a pyramid of biomass carries no numbers at all",
            "It shows the drop but not its cause, and the real fraction differs at each step",
            "It proves the tenth for water chains alone, where every transfer has been measured",
        ],
        "correct_index": 2,
        "why": "The bars give the standing mass at each level; the ratio between "
               "two of them is a measurement, not a confirmation of a rule.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h10",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid holds 8000 g/m² at level 1 and 20 g/m² "
                "at level 3, and both transfers were equally efficient. "
                "Determine the biomass at level 2.",
        "options": [
            "4010 g/m²",
            "800 g/m²",
            "80 g/m²",
            "400 g/m²",
        ],
        "correct_index": 3,
        "why": "Equal efficiency means level 2 squared equals 8000 × 20 = "
               "160 000, so level 2 holds 400 g/m² and each transfer is "
               "5%.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h11",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare a pyramid of biomass for one habitat drawn in "
                "kg/m² with the same pyramid drawn in g/m².",
        "options": [
            "The same shape — the units change the numbers on the scale, not the proportions",
            "The kg/m² pyramid is a thousand times narrower at every one of its levels",
            "The g/m² pyramid is a true pyramid, but the kg/m² one is inverted",
            "The kg/m² pyramid has to be drawn upside down to fit the larger unit",
        ],
        "correct_index": 0,
        "why": "Changing the unit multiplies every value by the same factor, so "
               "the ratios between the bars — and the shape — are unchanged.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h12",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An ecologist has the biomass of levels 1, 2 and 3 but not of "
                "level 4. Suggest how the level 4 bar could be estimated, and "
                "give one limitation.",
        "options": [
            "Halve the level 3 value, because every level is known to hold half of the one below",
            "Apply the transfer measured from level 2 to level 3, which may itself differ",
            "Leave the bar out, because an estimated bar cannot be drawn to a scale",
            "Copy the level 1 bar, because the top and bottom levels always balance",
        ],
        "correct_index": 1,
        "why": "The measured transfer is the best available guide, but efficiency "
               "varies between steps, so the estimate carries real uncertainty.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h13",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pond's biomass is recorded every month for a year. Explain "
                "why the producer bar changes far more than the top predator "
                "bar does.",
        "options": [
            "Top predators are recorded once a year, so their bar is unable to change",
            "The producer bar is the widest of them, and a wide bar is measured least accurately",
            "Algae grow and die within days, but a predator's biomass builds over years",
            "Predators respire less than producers, so they lose almost no biomass",
        ],
        "correct_index": 2,
        "why": "A short-lived level responds to light and temperature within "
               "days, whereas a long-lived fish carries its mass across seasons.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h14",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the usefulness of a pyramid of biomass for deciding "
                "whether an ecosystem is in good condition.",
        "options": [
            "It is decisive, because a true pyramid shape is proof of a healthy ecosystem",
            "It is useless, because biomass has no connection at all with an ecosystem's state",
            "It is useful for water habitats alone, where every level can be sampled",
            "It shows the proportions between levels, but not the species or the trend",
        ],
        "correct_index": 3,
        "why": "A single pyramid gives one snapshot of mass; judging condition "
               "needs species data and repeat measurements over several years.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h15",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an inverted pyramid of biomass can be measured on "
                "one day but cannot persist for years.",
        "options": [
            "Level 2 could not go on taking more biomass than level 1 produces",
            "The organisms at level 2 would grow larger until they had become producers themselves",
            "A pyramid is redrawn each year, and the new drawing corrects the inversion",
            "Inverted pyramids are drawn upside down, so they right themselves in time",
        ],
        "correct_index": 0,
        "why": "Over a long period the consumers cannot take out more biomass "
               "than the producers make, whatever the standing mass on one day.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h16",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Level 1 of a chain holds 9000 g/m² and each transfer "
                "passes on a tenth. Determine the width of the level 4 bar at a "
                "scale of 1 cm to 250 g/m².",
        "options": [
            "0.36 cm",
            "0.036 cm",
            "3.6 cm",
            "0.0036 cm",
        ],
        "correct_index": 1,
        "why": "Level 4 holds 9000 ÷ 1000 = 9 g/m², and 9 ÷ 250 = "
               "0.036 cm.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h17",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student samples the plants of a garden but takes the animals' "
                "biomass from a textbook. Evaluate the pyramid that results.",
        "options": [
            "It is sound, because published values beat a school's own samples",
            "It is sound, because the shape is what matters and the exact values do not",
            "It cannot be used, because a pyramid must not mix biomass with numbers",
            "Only the producer bar rests on measurement, so the bars above are not evidence",
        ],
        "correct_index": 3,
        "why": "Published figures come from other habitats, so the transfers "
               "shown are not those of this garden and cannot be concluded from.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h18",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Three pyramids are drawn for one food chain: numbers, biomass "
                "and energy. State what each one measures.",
        "options": [
            "All three give the same shape, so any one of them can replace another",
            "Numbers gives mass, biomass gives counts, energy gives heat",
            "Energy alone has a scale, so energy alone carries information",
            "Numbers gives counts, biomass the mass at one moment, energy the flow per year",
        ],
        "correct_index": 3,
        "why": "The three answer different questions: how many, how much mass "
               "now, and how much energy passed through over a whole year.",
    },

    # ══ standard/harder · s19-s26, h19-h26 (MRB-338 night 3 top-up) ══
    {
        "id": "ks4-pyramids-of-biomass-s19",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a hedgerow, an oak tree's own biomass is far greater than the "
                "combined biomass of the many small insects feeding on it, even "
                "though the insects vastly outnumber the tree. Explain why the "
                "pyramid of biomass for this chain stays a true pyramid shape, while "
                "a pyramid of NUMBERS for the same chain would be inverted.",
        "options": [
            "It stays a true pyramid because the tree's own biomass is still far greater than the combined biomass of its insects",
            "It stays a true pyramid because insects are not counted as consumers in a biomass diagram in the first place",
            "It stays a true pyramid because a numbers pyramid and a biomass pyramid measure exactly the same thing",
            "It becomes inverted too, because so many insects together must outweigh one single tree",
        ],
        "correct_index": 2,
        "why": "The tree's own biomass still dwarfs the insects' combined biomass, "
               "so the bars still narrow going up even though the insects are far "
               "more numerous.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s20",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why you would expect the producer bar of a pyramid of "
                "biomass drawn for a tropical rainforest to be far wider than the "
                "producer bar drawn for a desert.",
        "options": [
            "The rainforest's bar is far wider, since warmth, light and rainfall there support much greater plant growth",
            "The rainforest's bar is narrower, since dense shade there tends to limit how much a plant can photosynthesise",
            "Both bars end up the same width, since every habitat captures roughly the same amount of sunlight each year",
            "The desert's bar is wider, since desert plants store unusually large amounts of biomass in their roots",
        ],
        "correct_index": 0,
        "why": "Warmth, light and rainfall in a rainforest support much greater "
               "plant growth, so far more producer biomass builds up than in a "
               "desert.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s21",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Besides the bars themselves, state three things that should be shown "
                "on a fully labelled pyramid of biomass.",
        "options": [
            "The date the sample was collected, the name of the ecologist, and the total area of the habitat surveyed",
            "The scale used, the organism or trophic level at each bar, and the units the biomass was measured in",
            "The weather conditions on the day, the equipment used, and a photograph of the habitat itself",
            "The Latin name of every species present, the depth of soil sampled, and the time samples were taken",
        ],
        "correct_index": 1,
        "why": "A complete diagram needs the scale used, the organism or trophic "
               "level named at each bar, and the units the biomass was measured in.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s22",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of biomass is accidentally drawn using wet, undried "
                "biomass at every level instead of dry biomass. Explain the effect "
                "this has on how reliably the bars can be compared with one another.",
        "options": [
            "Nothing changes, because water makes up a fixed, identical proportion of every organism's mass",
            "Every bar becomes exactly the same width, since a wet sample tends to weigh close to the same amount",
            "The pyramid becomes impossible to draw, since wet samples cannot be measured on a balance in this way",
            "The bars no longer reliably compare levels, since organisms hold very different proportions of water",
        ],
        "correct_index": 3,
        "why": "Organisms hold different proportions of water, so bars based on wet "
               "mass no longer reliably reflect the actual living material at each "
               "level.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s23",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A heron has a biomass of 0.6 g/m², and a scale of 1 cm to 0.2 g/m² "
                "is used. Calculate the width of the heron's bar.",
        "options": [
            "3 cm, from dividing the heron's 0.6 g/m² by the scale of 0.2 g/m² per centimetre",
            "0.12 cm, from multiplying 0.6 g/m² by the scale of 0.2 g/m² per centimetre instead of dividing",
            "1.2 cm, from doubling the heron's biomass before applying the scale",
            "30 cm, from misreading the scale as 0.02 g/m² per centimetre rather than 0.2",
        ],
        "correct_index": 0,
        "why": "0.6 g/m² divided by the scale of 0.2 g/m² per centimetre gives a bar "
               "3 cm wide.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s24",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a single pyramid of biomass cannot easily be drawn for a "
                "whole food WEB in the way it can for one food chain.",
        "options": [
            "It can be drawn just as easily, since every organism in a web still has exactly one trophic level",
            "It cannot easily be drawn, because an organism feeding at more than one level cannot be placed in a single bar",
            "It can be drawn, but just for a web that contains fewer than four different species in total",
            "It cannot be drawn, because a food web does not include any producers in the first place",
        ],
        "correct_index": 1,
        "why": "An organism in a web can feed at more than one trophic level, so it "
               "cannot be placed in a single bar the way a food chain's organisms "
               "can.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s25",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid uses a scale of 1 cm to 15 g/m². Level 2 has a biomass of "
                "45 g/m² and level 3 has a biomass of 9 g/m². Calculate the "
                "difference in width between the two bars.",
        "options": [
            "2 cm, from dividing 45 g/m² by 9 g/m² directly using the two biomass values",
            "5.4 cm, from adding the two bar widths together instead of subtracting them",
            "2.4 cm, from a 3 cm bar for level 2 and a 0.6 cm bar for level 3 at the given scale",
            "0.4 cm, from dividing the scale itself by the difference in biomass",
        ],
        "correct_index": 2,
        "why": "45 g/m² gives a 3 cm bar and 9 g/m² gives a 0.6 cm bar at this "
               "scale, a difference of 2.4 cm.",
    },
    {
        "id": "ks4-pyramids-of-biomass-s26",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A school draws a pyramid of biomass for a pond using ten quadrats. A "
                "professional ecologist draws one for the same pond, using exactly "
                "the same method but two hundred quadrats. Suggest why the school's "
                "version might be less reliable.",
        "options": [
            "It would not be, because using the same method guarantees the same reliability regardless of sample size",
            "It would not be, because a school's equipment is generally far less accurate than a professional ecologist's",
            "It would be more reliable, because fewer samples are quicker to take and therefore contain fewer mistakes",
            "It could be less reliable, because fewer samples are more easily skewed by natural small-scale variation",
        ],
        "correct_index": 3,
        "why": "Fewer samples are more easily skewed by natural small-scale "
               "variation, even when the sampling method itself is identical.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h19",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of biomass has a producer bar 14 cm wide, representing 700 "
                "g/m². Determine the width of a consumer bar representing 84 g/m², "
                "using the same scale.",
        "options": [
            "0.28 cm, from applying the original scale to 84 g/m² without first working out the scale from the producer bar",
            "8.4 cm, from treating the consumer's biomass as though it used the same bar width as the producer",
            "1.4 cm, from halving the producer bar's width to estimate the consumer bar",
            "1.68 cm, from a scale of 0.02 cm per g/m² worked out from the 14 cm producer bar, applied to 84 g/m²",
        ],
        "correct_index": 3,
        "why": "The scale works out at 0.02 cm per g/m² from the producer bar, and "
               "applying that to 84 g/m² gives a width of 1.68 cm.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h20",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says that because the level 2 bar in a pyramid of biomass "
                "is much narrower than level 1, only a small number of individual "
                "organisms can be present at level 2. Evaluate this reasoning.",
        "options": [
            "The reasoning holds, because bar width in a pyramid of biomass represents the number of organisms present",
            "The reasoning is flawed; bar width shows total biomass, and level 2 could hold far more individual organisms than level 1 if each one is tiny",
            "The reasoning holds, because a narrower bar can just mean fewer organisms are present at that level",
            "The reasoning is flawed because trophic level 2 is not expected to appear narrower than trophic level 1",
        ],
        "correct_index": 1,
        "why": "Bar width shows total biomass, not a count of organisms, so a "
               "narrower bar can still represent far more individual organisms if "
               "each one is small.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h21",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the width you would expect for the producer bar of a pyramid "
                "of biomass drawn for a freshly ploughed arable field in early spring "
                "with one drawn for the same field in high summer.",
        "options": [
            "The spring producer bar is much narrower, since little vegetation has grown back after ploughing by that point",
            "The two bars come out the same width, because ploughing has no lasting effect on plant growth by spring",
            "The spring producer bar is wider, since freshly ploughed soil briefly holds more biomass than a grown crop does",
            "Neither bar can be drawn, because an arable field is not considered a proper ecosystem",
        ],
        "correct_index": 0,
        "why": "Little vegetation has regrown by early spring after ploughing, so "
               "the producer bar is far narrower than once the crop has grown "
               "through summer.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h22",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid shows producers at 12 000 g/m², primary consumers at 900 "
                "g/m² and secondary consumers at 100 g/m². Determine which of the two "
                "transfers, level 1 to 2 or level 2 to 3, lost the SMALLER proportion "
                "of biomass, and state that proportion as a percentage.",
        "options": [
            "The first transfer lost the smaller proportion, at roughly 89% against 92.5% for the second",
            "Both transfers lost exactly the same proportion, since the same tenth-per-transfer rule applies at every step",
            "Neither transfer can be compared this way, because the two transfers involve different biomass units",
            "The second transfer lost the smaller proportion, at roughly 89% against 92.5% for the first",
        ],
        "correct_index": 3,
        "why": "The first transfer loses 11 100 out of 12 000 g/m² (92.5%), and the "
               "second loses 800 out of 900 g/m² (about 89%), so the second transfer "
               "is the more efficient of the two.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h23",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of biomass built from a single 1 m² quadrat gives an "
                "unusual, slightly inverted shape at one level. A second ecologist "
                "repeats the same measurements across fifty quadrats and finds a "
                "normal true-pyramid shape. Suggest why the two results differ.",
        "options": [
            "The two results cannot genuinely differ, because a single quadrat and fifty quadrats give the same reading",
            "The single quadrat was likely affected by small-scale natural variation, while fifty quadrats average this out into a more representative result",
            "The second ecologist must have measured a completely different habitat by mistake",
            "The first ecologist's result is the more trustworthy one, since fewer quadrats means less room for human error",
        ],
        "correct_index": 1,
        "why": "A single quadrat can be skewed by natural small-scale variation, "
               "while fifty quadrats average this out into a far more representative "
               "picture of the habitat.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h24",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A conservation report claims that because a rainforest's pyramid of "
                "biomass has an enormous producer bar, the rainforest must therefore "
                "support more trophic levels than a desert does. Evaluate this claim.",
        "options": [
            "The claim is certainly true, because a wider producer bar guarantees more trophic levels above it",
            "The claim is certainly false, because the number of trophic levels a habitat supports has nothing to do with producer biomass",
            "The claim is not proven by the bar alone, since supporting more levels also depends on how efficiently energy is transferred at each step",
            "The claim cannot be judged, because pyramids of biomass are not designed to compare two different habitats",
        ],
        "correct_index": 2,
        "why": "A wider producer bar shows more biomass is captured, but supporting "
               "extra trophic levels also depends on how efficiently that biomass is "
               "passed on at each transfer.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h25",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pyramid of biomass is redrawn at a new scale so the diagram fits "
                "on a smaller page: the old scale was 1 cm to 200 g/m² and the new "
                "scale is 1 cm to 500 g/m². A bar was 8 cm wide under the old scale. "
                "Determine its width under the new scale.",
        "options": [
            "5 cm, from applying the new scale directly to the bar's original 8 cm width",
            "3.2 cm, from recovering the actual biomass of 1 600 g/m² under the old scale, then reapplying it under the new one",
            "20 cm, from multiplying the old width by the ratio of the two scales the wrong way round",
            "8 cm, since a bar's width does not change when a pyramid is redrawn to a new scale",
        ],
        "correct_index": 1,
        "why": "The bar represented 1 600 g/m² under the old scale, and 1 600 g/m² "
               "under the new scale of 1 cm to 500 g/m² gives a width of 3.2 cm.",
    },
    {
        "id": "ks4-pyramids-of-biomass-h26",
        "subtopic_slug": "pyramids-of-biomass",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two pyramids of biomass are drawn for the same lake: one from ten "
                "years ago and one from this year, after an invasive plant became the "
                "dominant producer. The producer bar is far wider in this year's "
                "pyramid. Suggest what this does, and does not, tell you about the "
                "lake's biodiversity.",
        "options": [
            "It shows the invasive plant now captures more biomass, but not whether the lake's biodiversity has risen or fallen",
            "It proves the lake's biodiversity has increased, since more total producer biomass means more species too present",
            "It proves the lake's biodiversity has fallen, since a wider producer bar can just come from a single dominant species",
            "It shows nothing useful, since a pyramid of biomass is not meant to be compared between two different years",
        ],
        "correct_index": 0,
        "why": "A wider bar shows more producer biomass has built up, but says "
               "nothing about whether more or fewer species are present at that "
               "level.",
    },
]
