"""Chemistry · The atmosphere — the MRB-335 extension.

Every one of this topic's four subtopics is BASE, so Combined and Triple see
exactly the same pool and all four cells were short together: 48 at
Foundation and 32 at Higher on the 7 Sep table. That symmetry makes the fix
simple — every row added here counts for all four audiences — and it makes
the band split the only lever that matters, because Higher draws only on
`standard` and `harder`.

The topic is unusual in the KS4 pool for how much of it is EVALUATION rather
than recall: peer review, bias in reporting, the limits of climate models,
who should cut emissions. Those questions are written as evaluations with a
defensible single answer, not as opinions — the correct option is the one
that states both sides where both exist, and the distractors are the
one-sided readings a student actually offers.
"""

TOPIC = "atmosphere"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── composition-of-atmosphere ─────────────── BASE (5.9.1.1) ── +7 ──
    {
        "id": "ks4-composition-of-atmosphere-e05",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate percentage of oxygen in dry air "
                "today.",
        "options": [
            "About 0.04%",
            "About 0.9%",
            "About 21%",
            "About 78%",
        ],
        "correct_index": 2,
        "why": "Dry air is roughly four fifths nitrogen and one fifth "
               "oxygen, which is about 21% oxygen.",
    },
    {
        "id": "ks4-composition-of-atmosphere-s05",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the composition of the atmosphere has stayed "
                "roughly the same for the last 200 million years.",
        "options": [
            "The processes that add each gas and the processes that remove "
            "it have been closely balanced",
            "No chemical reactions have taken place in the atmosphere at "
            "all during that time",
            "The atmosphere has been sealed off from the oceans and the "
            "rocks",
            "Nitrogen has prevented any of the other gases from changing",
        ],
        "correct_index": 0,
        "why": "Photosynthesis and respiration, and dissolving and "
               "outgassing, run in opposite directions at about the same "
               "rate, so the totals hold steady.",
    },
    {
        "id": "ks4-composition-of-atmosphere-s06",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of air is passed repeatedly over hot copper until "
                "the volume stops changing. The volume falls by about one "
                "fifth. Explain what has happened.",
        "options": [
            "The copper absorbed the nitrogen, which makes up about one "
            "fifth of the air",
            "The copper reacted with the oxygen to form copper oxide, and "
            "oxygen is about one fifth of air",
            "The air expanded as it was heated and then contracted again as "
            "it cooled down",
            "The carbon dioxide reacted with the copper and was removed",
        ],
        "correct_index": 1,
        "why": "Hot copper takes oxygen out of the air as copper oxide, so "
               "the fall in volume measures how much of the air was oxygen.",
    },
    {
        "id": "ks4-composition-of-atmosphere-s07",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two human activities that have increased the "
                "amount of carbon dioxide in the atmosphere.",
        "options": [
            "Breathing out, and cutting grass on lawns",
            "Using aerosol sprays, and refrigerating food",
            "Burning fossil fuels for energy and transport, and clearing "
            "forests for farming",
            "Making steel from iron ore, and burning hydrogen as a vehicle "
            "fuel",
        ],
        "correct_index": 2,
        "why": "Combustion releases carbon that was locked underground, and "
               "removing trees takes away the photosynthesis that would have "
               "absorbed it.",
    },
    {
        "id": "ks4-composition-of-atmosphere-h05",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Dry air is about 78% nitrogen by volume. Calculate the "
                "volume of nitrogen, in cm3, in 2.5 dm3 of dry air. "
                "(1 dm3 = 1000 cm3.)",
        "options": [
            "195 cm3",
            "1950 cm3",
            "525 cm3",
            "2500 cm3",
        ],
        "correct_index": 1,
        "why": "2.5 dm3 is 2500 cm3, and 78% of 2500 cm3 is 1950 cm3.",
    },
    {
        "id": "ks4-composition-of-atmosphere-h06",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In an experiment 100 cm3 of air is passed over hot copper "
                "until no further change occurs, and 79 cm3 of gas remains. "
                "Determine the percentage of oxygen found, and evaluate how "
                "close it is to the accepted value.",
        "options": [
            "79%, which is very far from the accepted value",
            "1%, which shows the experiment failed",
            "21%, which is much lower than the accepted value of 78%",
            "21%, which matches the accepted value of about 21%",
        ],
        "correct_index": 3,
        "why": "The 21 cm3 lost was the oxygen, so the sample was 21% "
               "oxygen — the accepted figure for dry air.",
    },
    {
        "id": "ks4-composition-of-atmosphere-h07",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon dioxide makes up about 0.04% of air by volume. "
                "Calculate the volume of carbon dioxide, in cm3, in a room "
                "holding 60 m3 of air. (1 m3 = 1 000 000 cm3.)",
        "options": [
            "2400 cm3",
            "24 000 cm3",
            "240 000 cm3",
            "2 400 000 cm3",
        ],
        "correct_index": 1,
        "why": "60 m3 is 60 000 000 cm3, and 0.04% of that — multiplying by "
               "0.0004 — is 24 000 cm3.",
    },

    # ── early-atmosphere ──────────────────────── BASE (5.9.1.1) ── +8 ──
    {
        "id": "ks4-early-atmosphere-e05",
        "subtopic_slug": "early-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate age of the Earth.",
        "options": [
            "About 4.6 million years",
            "About 460 million years",
            "About 46 billion years",
            "About 4.6 billion years",
        ],
        "correct_index": 3,
        "why": "The Earth formed about 4.6 billion years ago, and its first "
               "billion years is the period the early atmosphere covers.",
    },
    {
        "id": "ks4-early-atmosphere-s05",
        "subtopic_slug": "early-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the amount of carbon dioxide in the atmosphere "
                "fell as the oceans formed.",
        "options": [
            "Carbon dioxide dissolved in the ocean water, which removed it "
            "from the air",
            "Carbon dioxide reacted with the nitrogen already in the air",
            "Sunlight broke the carbon dioxide down into carbon and oxygen",
            "Carbon dioxide escaped into space as the Earth cooled",
        ],
        "correct_index": 0,
        "why": "Carbon dioxide is soluble, so as soon as there was liquid "
               "water it began dissolving out of the atmosphere.",
    },
    {
        "id": "ks4-early-atmosphere-s06",
        "subtopic_slug": "early-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how carbon from the early atmosphere ended up in "
                "coal, oil and natural gas.",
        "options": [
            "Carbon dioxide dissolved in the oceans and then crystallised "
            "directly into seams of coal",
            "Plants and plankton took in carbon dioxide by photosynthesis, "
            "and their buried remains were compressed",
            "Volcanic carbon was cooled and pressed into oil inside the "
            "crust",
            "Nitrogen in the air reacted with buried rock to form natural "
            "gas",
        ],
        "correct_index": 1,
        "why": "Fossil fuels are the buried remains of organisms that had "
               "taken their carbon from the air, which is why burning them "
               "puts it back.",
    },
    {
        "id": "ks4-early-atmosphere-s07",
        "subtopic_slug": "early-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why there was almost no oxygen in the atmosphere "
                "for the Earth's first billion years.",
        "options": [
            "Oxygen escaped into space because it is such a light gas",
            "Volcanoes destroyed any oxygen as fast as it formed",
            "Nothing on Earth produced oxygen until photosynthesising "
            "organisms evolved",
            "All the oxygen was locked inside carbon dioxide and could not "
            "be released",
        ],
        "correct_index": 2,
        "why": "Oxygen is a product of photosynthesis, so there was no "
               "source of it at all until living things capable of "
               "photosynthesis appeared.",
    },
    {
        "id": "ks4-early-atmosphere-s08",
        "subtopic_slug": "early-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why layers of iron oxide in very old rocks are used "
                "as evidence about the early atmosphere.",
        "options": [
            "They show dissolved iron reacting with the first oxygen, which "
            "dates when oxygen began to build up",
            "They contain trapped bubbles of the early atmosphere itself, "
            "which can be analysed",
            "They show that the early atmosphere contained no carbon "
            "dioxide",
            "They are made of limestone, which only ever forms in an "
            "atmosphere rich in oxygen",
        ],
        "correct_index": 0,
        "why": "Iron only forms oxides once free oxygen exists, so the age of "
               "those layers marks when oxygen first appeared in quantity.",
    },
    {
        "id": "ks4-early-atmosphere-h05",
        "subtopic_slug": "early-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the early atmosphere with the atmosphere today, "
                "naming the main gas in each and one gas present now that "
                "was absent then.",
        "options": [
            "Nitrogen then and carbon dioxide now, with oxygen absent from "
            "the early atmosphere",
            "Carbon dioxide then and oxygen now, with nitrogen absent from "
            "the early atmosphere",
            "Carbon dioxide then and nitrogen now, with oxygen absent from "
            "the early atmosphere",
            "Water vapour then and nitrogen now, with carbon dioxide absent "
            "from the early atmosphere",
        ],
        "correct_index": 2,
        "why": "The early atmosphere was mostly carbon dioxide with no "
               "oxygen; today nitrogen dominates and oxygen is about a "
               "fifth.",
    },
    {
        "id": "ks4-early-atmosphere-h06",
        "subtopic_slug": "early-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Venus today has an atmosphere over 96% carbon dioxide and a "
                "surface temperature near 460 °C. Suggest what this "
                "contributes to the picture of the early Earth, and why the "
                "two planets ended up different.",
        "options": [
            "It supports a carbon dioxide-rich early Earth that then cooled "
            "enough for oceans to form and dissolve the gas",
            "It shows the early Earth was always cool, so Venus is no guide "
            "at all",
            "It shows that carbon dioxide cannot cause any warming",
            "It shows the Earth stayed hot until photosynthesis removed all "
            "of the carbon dioxide from the air",
        ],
        "correct_index": 0,
        "why": "Venus is what a planet looks like when its carbon dioxide is "
               "never removed; the Earth cooled enough for oceans, and the "
               "oceans took the carbon dioxide out.",
    },
    {
        "id": "ks4-early-atmosphere-h07",
        "subtopic_slug": "early-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Photosynthesis is 6CO2 + 6H2O → C6H12O6 + 6O2. Deduce the "
                "volume of oxygen released when 300 cm3 of carbon dioxide is "
                "used up, and state the assumption you have made.",
        "options": [
            "150 cm3, assuming that an oxygen molecule takes up twice the "
            "space of a carbon dioxide molecule",
            "600 cm3, assuming each carbon dioxide molecule releases two "
            "oxygen molecules",
            "300 cm3, assuming equal volumes of gases hold equal numbers of "
            "molecules at the same temperature and pressure",
            "50 cm3, assuming six carbon dioxide molecules make one oxygen "
            "molecule",
        ],
        "correct_index": 2,
        "why": "The equation is 6 molecules to 6 molecules, so under the "
               "same conditions the two gas volumes are equal.",
    },

    # ── greenhouse-gases ──────────────────────── BASE (5.9.2.1) ── +10 ──
    {
        "id": "ks4-greenhouse-gases-e05",
        "subtopic_slug": "greenhouse-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name two greenhouse gases other than carbon dioxide.",
        "options": [
            "Methane and water vapour",
            "Nitrogen and oxygen",
            "Argon and helium",
            "Hydrogen and neon",
        ],
        "correct_index": 0,
        "why": "Water vapour and methane both absorb infrared radiation; "
               "nitrogen, oxygen and the noble gases do not.",
    },
    {
        "id": "ks4-greenhouse-gases-e06",
        "subtopic_slug": "greenhouse-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of radiation the Earth's surface gives out "
                "after it has been warmed by the Sun.",
        "options": [
            "Ultraviolet radiation",
            "Visible light only",
            "Infrared radiation",
            "X-rays",
        ],
        "correct_index": 2,
        "why": "A warm surface emits infrared, and it is that infrared which "
               "the greenhouse gases absorb on its way out.",
    },
    {
        "id": "ks4-greenhouse-gases-s05",
        "subtopic_slug": "greenhouse-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why methane is described as a more powerful "
                "greenhouse gas than carbon dioxide, even though there is "
                "far less of it in the air.",
        "options": [
            "Each methane molecule absorbs far more infrared radiation than "
            "each carbon dioxide molecule",
            "Methane is heavier, so it settles nearer the ground where the "
            "air is warmest",
            "Methane reacts with oxygen to make even more carbon dioxide",
            "Methane blocks visible light from reaching the surface",
        ],
        "correct_index": 0,
        "why": "Warming depends on how strongly a molecule absorbs infrared "
               "as well as on how many molecules there are.",
    },
    {
        "id": "ks4-greenhouse-gases-s06",
        "subtopic_slug": "greenhouse-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two human activities that release methane into the "
                "atmosphere.",
        "options": [
            "Burning petrol in cars and making cement",
            "Livestock farming and rotting waste in landfill sites",
            "Using aerosol sprays and running refrigerators",
            "Quarrying limestone and smelting iron",
        ],
        "correct_index": 1,
        "why": "Methane comes from decay without oxygen — in the guts of "
               "cattle and in buried landfill waste.",
    },
    {
        "id": "ks4-greenhouse-gases-s07",
        "subtopic_slug": "greenhouse-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why scientists find it hard to predict exactly how "
                "much the Earth will warm.",
        "options": [
            "Nobody has ever measured the Earth's temperature accurately",
            "Greenhouse gases were only discovered a few years ago and are "
            "still being studied",
            "The climate has many interacting factors, so models must be "
            "simplified and carry uncertainty",
            "Scientists do not accept that the greenhouse effect exists",
        ],
        "correct_index": 2,
        "why": "A climate model has to leave things out to be usable, so its "
               "output is a range of likely outcomes rather than one exact "
               "figure.",
    },
    {
        "id": "ks4-greenhouse-gases-s08",
        "subtopic_slug": "greenhouse-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a newspaper article about climate change may "
                "give a biased account.",
        "options": [
            "It may be simplified, based on opinion rather than reviewed "
            "evidence, or written to suit an interest",
            "Newspapers are unable to print numbers accurately",
            "Scientists never share any of their results with journalists, "
            "so a newspaper has to guess",
            "Only peer-reviewed journals ever contain mistakes",
        ],
        "correct_index": 0,
        "why": "Evidence in science is checked by peer review; a newspaper "
               "has no such check and may have reasons to present one side.",
    },
    {
        "id": "ks4-greenhouse-gases-h05",
        "subtopic_slug": "greenhouse-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person's carbon footprint is 9.0 tonnes of carbon dioxide "
                "equivalent per year. They reduce it by 15%. Calculate their "
                "new footprint.",
        "options": [
            "1.35 tonnes",
            "8.85 tonnes",
            "10.35 tonnes",
            "7.65 tonnes",
        ],
        "correct_index": 3,
        "why": "15% of 9.0 is 1.35 tonnes, so the footprint falls to "
               "9.0 − 1.35 = 7.65 tonnes.",
    },
    {
        "id": "ks4-greenhouse-gases-h06",
        "subtopic_slug": "greenhouse-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why international agreements to cut greenhouse gas "
                "emissions are difficult to reach.",
        "options": [
            "The science of the greenhouse effect is still not understood",
            "No country yet has any technology capable of reducing the "
            "emissions it makes",
            "Greenhouse gases cross national borders too slowly for any "
            "agreement to matter",
            "Countries differ in wealth, energy needs and past emissions, "
            "so they disagree over who cuts most",
        ],
        "correct_index": 3,
        "why": "The obstacle is political and economic rather than "
               "scientific: a cut that is cheap for one country is "
               "expensive for another.",
    },
    {
        "id": "ks4-greenhouse-gases-h07",
        "subtopic_slug": "greenhouse-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Carbon dioxide levels and global average temperature have "
                "both risen over the last century. Explain why this "
                "correlation alone does not prove carbon dioxide caused the "
                "warming, and state what does support the link.",
        "options": [
            "A correlation can arise by chance or a third cause; the link "
            "rests on known infrared absorption and many models",
            "Correlation always proves cause, so the link is already proved",
            "Nothing supports the link, because temperature data are "
            "unreliable",
            "The link is proved because both quantities were measured over "
            "exactly the same period of time",
        ],
        "correct_index": 0,
        "why": "Two things rising together is a start, not a proof; the "
               "case rests on a known mechanism plus evidence from many "
               "independent lines.",
    },
    {
        "id": "ks4-greenhouse-gases-h08",
        "subtopic_slug": "greenhouse-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Water vapour is the most abundant "
                "greenhouse gas, so human carbon dioxide emissions cannot "
                "matter.'",
        "options": [
            "It is correct — water vapour makes carbon dioxide irrelevant",
            "It is wrong, because water vapour does not absorb infrared and "
            "is not a greenhouse gas",
            "It is correct, because carbon dioxide is only 0.04% of the air",
            "It is wrong: water vapour is set by temperature, and extra "
            "carbon dioxide raises both",
        ],
        "correct_index": 3,
        "why": "Water vapour follows the temperature rather than driving it, "
               "so it amplifies a carbon dioxide-driven warming instead of "
               "cancelling it.",
    },

    # ── atmospheric-pollutants ────────────────── BASE (5.9.3.1) ── +9 ──
    {
        "id": "ks4-atmospheric-pollutants-e05",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one problem caused by acid rain.",
        "options": [
            "It damages trees and makes lakes too acidic for fish",
            "It reduces the oxygen content of the air",
            "It causes global dimming",
            "It destroys the ozone layer",
        ],
        "correct_index": 0,
        "why": "Acid rain lowers the pH of soil and water, killing trees and "
               "the life in lakes, and it corrodes limestone buildings.",
    },
    {
        "id": "ks4-atmospheric-pollutants-e06",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what particulates are.",
        "options": [
            "Droplets of water formed when a fuel burns",
            "Tiny solid particles of carbon and unburnt fuel released into "
            "the air",
            "Molecules of carbon dioxide released by combustion",
            "Acidic gases dissolved in rain water",
        ],
        "correct_index": 1,
        "why": "Particulates are solid specks — soot and unburnt fuel — "
               "small enough to stay suspended in the air and be breathed "
               "in.",
    },
    {
        "id": "ks4-atmospheric-pollutants-s05",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a petrol engine produces nitrogen oxides but a "
                "candle burning hydrocarbon wax does not.",
        "options": [
            "The engine runs far hotter, and only that temperature makes "
            "nitrogen and oxygen in the air react",
            "The engine's fuel contains nitrogen compounds but the wax of a "
            "candle does not",
            "The candle burns with too little oxygen for nitrogen oxides to "
            "form",
            "The catalytic converter fitted to the engine is what creates "
            "the nitrogen oxides",
        ],
        "correct_index": 0,
        "why": "Nitrogen is very unreactive, and only the temperature inside "
               "an engine is high enough to make it combine with oxygen.",
    },
    {
        "id": "ks4-atmospheric-pollutants-s06",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the equation for the burning of sulfur in oxygen, "
                "and state the environmental problem the product causes.",
        "options": [
            "S + O2 → SO2, which causes global dimming",
            "2S + O2 → 2SO, which causes acid rain",
            "S + 2O2 → SO4, which causes acid rain",
            "S + O2 → SO2, which causes acid rain",
        ],
        "correct_index": 3,
        "why": "One sulfur atom takes one oxygen molecule to make SO2, and "
               "SO2 dissolving in cloud droplets is what acidifies the rain.",
    },
    {
        "id": "ks4-atmospheric-pollutants-s07",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why removing sulfur from a fuel at the refinery is "
                "better than removing sulfur dioxide from the flue gases "
                "afterwards.",
        "options": [
            "Sulfur dioxide cannot be removed from flue gases by any method "
            "that exists today",
            "The sulfur is removed once, so every engine and boiler using "
            "the fuel benefits, not only fitted chimneys",
            "Removing sulfur from the fuel also removes the carbon monoxide",
            "Flue gas scrubbing releases more sulfur dioxide into the air "
            "than it manages to remove",
        ],
        "correct_index": 1,
        "why": "Treating the fuel fixes the problem for every user; treating "
               "the chimney only fixes it for the chimneys that have the "
               "equipment.",
    },
    {
        "id": "ks4-atmospheric-pollutants-s08",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wood-burning stove is advertised as 'carbon neutral'. "
                "Describe the pollutants it still releases.",
        "options": [
            "It releases only water vapour",
            "It releases sulfur dioxide, because wood is high in sulfur",
            "It releases nothing at all, which is what carbon neutral means",
            "It still releases particulates, and carbon monoxide if the air "
            "supply is poor",
        ],
        "correct_index": 3,
        "why": "Carbon neutral is a claim about the carbon dioxide balance "
               "only; the soot and the carbon monoxide from incomplete "
               "burning are unaffected by it.",
    },
    {
        "id": "ks4-atmospheric-pollutants-h05",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fuel contains 1.5% sulfur by mass. Calculate the mass of "
                "sulfur in 200 kg of the fuel and name the pollutant it "
                "forms when burned.",
        "options": [
            "3.0 kg, forming sulfur dioxide",
            "30 kg, forming sulfur dioxide",
            "3.0 kg, forming sulfur trioxide",
            "0.30 kg, forming sulfur dioxide",
        ],
        "correct_index": 0,
        "why": "1.5% of 200 kg is 3.0 kg, and burning sulfur in air gives "
               "sulfur dioxide.",
    },
    {
        "id": "ks4-atmospheric-pollutants-h06",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the harm done by the carbon dioxide from an engine "
                "with the harm done by the carbon monoxide from the same "
                "engine.",
        "options": [
            "Both are toxic gases that act immediately on anyone standing "
            "near the exhaust pipe",
            "Carbon monoxide is a greenhouse gas and carbon dioxide is "
            "toxic",
            "Carbon dioxide is a greenhouse gas acting globally over "
            "decades; carbon monoxide is immediately toxic",
            "Neither does any harm as long as the engine is running "
            "outdoors",
        ],
        "correct_index": 2,
        "why": "The two do different kinds of damage on different "
               "timescales, which is why both are controlled but by "
               "different means.",
    },
    {
        "id": "ks4-atmospheric-pollutants-h07",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate a city's plan to cut air pollution by charging "
                "drivers of older diesel vehicles to enter the centre.",
        "options": [
            "It will remove all of the city's air pollution at once, and it "
            "carries no drawbacks of any kind",
            "It will have no effect at all, because older diesel engines do "
            "not produce any particulates",
            "It will cut carbon monoxide but increase sulfur dioxide",
            "It should cut particulates and nitrogen oxides, but may push "
            "traffic elsewhere and hits poorer drivers hardest",
        ],
        "correct_index": 3,
        "why": "The chemistry says it works where it applies; the "
               "evaluation has to weigh that against displacement and "
               "fairness.",
    },
]
