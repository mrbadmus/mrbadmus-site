"""Biology · Ecology — the MRB-338 expansion of `global-warming`.

One leaf only: AQA 8461 §4.7.3.5, which is the BIOLOGY of global warming — what
it does to where species live, when they breed and migrate, and how many of
them there are. The original twelve rows in `ecology__a.py` take the two gases,
what a greenhouse gas does, one emitting activity, migrating birds arriving
earlier, a mountain-top species, flooded coast, the ozone-hole error, a tree
that cannot move fast, disagreeing models, a butterfly's range shifting north,
one country cutting to zero, and an island reserve against a long strip.

This file takes what they leave. The recall band finishes the sources of
methane and the vocabulary the baseline never separates — distribution against
abundance, which is the single commonest lost mark on this spec point. The
demand then falls on the two mechanisms of sea level rise (melting ice AND
water expanding as it warms, and pupils reliably give only the first), on
reading the evidence honestly, and on the difference between weather and
climate.

The weight follows the CONTENT. `easier` stays at eight: the causes and the
named consequences are a short list. `standard` and `harder` carry twenty-two
each, because each biological consequence generates a fresh context and the
data this topic supplies — degrees, millimetres a year, parts per million,
percentages — carries its own arithmetic.

⚠️ This leaf is the BASE tier. Coral bleaching, indicator species and
phenological mismatch belong to `environmental-change`, which is triple-only;
they are deliberately absent here.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # Distribution against abundance, the sources of methane, the two causes
    # of sea level rise, and what happens to a species that cannot move.
    {
        "id": "ks4-global-warming-e05",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Besides burning fossil fuels, name the two human activities "
                "AQA gives as causes of rising greenhouse gas levels.",
        "options": [
            "Recycling paper and insulating the walls and lofts of houses",
            "Planting new woodland and restoring drained peat bogs to "
                "marsh",
            "Deforestation and farming livestock",
            "Cycling to work and travelling by bus rather than by car",
        ],
        "correct_index": 2,
        "why": "Clearing forest removes a carbon sink and releases stored "
               "carbon, and livestock produce methane, so both add greenhouse "
               "gases to the atmosphere.",
    },
    {
        "id": "ks4-global-warming-e06",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name one farming activity that raises the amount of methane "
                "in the atmosphere.",
        "options": [
            "Keeping cattle",
            "Pruning orchards",
            "Baling straw",
            "Weeding by hand",
        ],
        "correct_index": 0,
        "why": "Microorganisms digesting grass in a cow's gut work without "
               "oxygen and produce methane, which the animal then releases.",
    },
    {
        "id": "ks4-global-warming-e07",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two causes of rising sea levels.",
        "options": [
            "Heavier rainfall, and rivers carrying more water to the sea",
            "Melting sea ice, and more water evaporating from the land",
            "Stronger winds, and the tides being pulled a lot higher by "
                "the Moon",
            "Melting land ice, and sea water expanding as it warms",
        ],
        "correct_index": 3,
        "why": "Water added from melting ice sheets and glaciers is only half "
               "the story; warmer water also takes up more space, and that "
               "expansion is a large part of the rise.",
    },
    {
        "id": "ks4-global-warming-e08",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to a species that can neither move nor "
                "adapt as its habitat warms.",
        "options": [
            "It changes into a new species at once",
            "It becomes extinct in that area",
            "It reproduces far more quickly",
            "It grows to a much larger size",
        ],
        "correct_index": 1,
        "why": "If conditions move outside what a species can tolerate and it "
               "cannot shift its range, its numbers fall until it is lost from "
               "that area.",
    },
    {
        "id": "ks4-global-warming-e09",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the direction in which many species are shifting their "
                "range as the climate warms.",
        "options": [
            "Towards the poles and to higher ground",
            "Towards the equator and to lower ground",
            "Towards the east, following the prevailing wind direction",
            "Downwards into the soil and into deep caves",
        ],
        "correct_index": 0,
        "why": "Cooler conditions lie towards the poles and higher up a "
               "mountain, so a species tracking its temperature range moves in "
               "those directions.",
    },
    {
        "id": "ks4-global-warming-e10",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name one kind of measurement scientists collect as evidence "
                "that the Earth is warming.",
        "options": [
            "The number of hours of daylight each year",
            "The height of the highest mountains",
            "The distance from the Earth to the Sun",
            "The area of the Earth covered by ice",
        ],
        "correct_index": 3,
        "why": "Ice cover, mean global temperature, sea level and carbon "
               "dioxide concentration are all measured worldwide and all point "
               "the same way.",
    },
    {
        "id": "ks4-global-warming-e11",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the source of methane that comes from buried household "
                "waste.",
        "options": [
            "Sewage pipes",
            "Landfill sites",
            "Recycling plants",
            "Wind turbines",
        ],
        "correct_index": 1,
        "why": "Waste buried deep in landfill decays without oxygen, and "
               "anaerobic decay produces methane.",
    },
    {
        "id": "ks4-global-warming-e12",
        "subtopic_slug": "global-warming",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the difference between weather and climate.",
        "options": [
            "Weather is what forecasters study; climate is what farmers "
                "study",
            "Weather is the temperature; climate is the rainfall",
            "Weather is conditions now; climate is the long-term pattern",
            "Weather is measured on land; climate is measured out at sea",
        ],
        "correct_index": 2,
        "why": "Climate is the average of the weather over decades, which is "
               "why one cold winter says nothing about whether the climate is "
               "warming.",
    },
    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Each biological consequence in a named context, and the first
    # arithmetic on degrees, millimetres and percentages.
    {
        "id": "ks4-global-warming-s05",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sea levels would still rise even if no land ice "
                "melted at all.",
        "options": [
            "Warmer air presses down harder on the ocean surface and "
                "pushes it outwards",
            "Rivers flow faster in warm weather and deliver water much "
                "more quickly to the sea",
            "Sea water expands as it warms, so the same mass takes up more "
                "space",
            "Warmer water dissolves the seabed, making the ocean deeper",
        ],
        "correct_index": 2,
        "why": "Thermal expansion means a warmer ocean occupies a greater "
               "volume, and that alone raises sea level.",
    },
    {
        "id": "ks4-global-warming-s06",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ice melting at the North Pole, which floats on "
                "the sea, adds almost nothing to sea level.",
        "options": [
            "Floating ice already displaces its own mass of water",
            "Sea ice is made of salt water, which does not expand",
            "Melted sea ice sinks straight to the bottom of the ocean",
            "Sea ice evaporates as it melts, so the water stays out of the "
                "sea",
        ],
        "correct_index": 0,
        "why": "Floating ice is already supported by the water it pushes "
               "aside, so melting it changes the sea level very little; "
               "melting ice that sits on LAND adds water that was not in the "
               "sea before.",
    },
    {
        "id": "ks4-global-warming-s07",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sea level is rising at 3.5 mm per year. Calculate the rise "
                "over 40 years.",
        "options": [
            "1.4 cm",
            "140 cm",
            "0.875 cm",
            "14 cm",
        ],
        "correct_index": 3,
        "why": "3.5 mm × 40 = 140 mm, and 140 mm ÷ 10 = 14 cm.",
    },
    {
        "id": "ks4-global-warming-s08",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A seal species hunts from floating sea ice. Explain how "
                "warming reduces its numbers.",
        "options": [
            "The seals lose their fur in warm weather and sink to the "
                "seabed",
            "The ice it hunts from disappears, so it cannot catch enough "
                "food",
            "The seals overheat in the water, which they are unable to "
                "leave",
            "Warm water contains no fish, so there is nothing left to hunt",
        ],
        "correct_index": 1,
        "why": "The ice is the platform the seal hunts and rests from; "
               "shrinking ice cover removes the habitat that its feeding "
               "depends on.",
    },
    {
        "id": "ks4-global-warming-s09",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why one unusually cold winter is not evidence against "
                "global warming.",
        "options": [
            "Climate is the average over decades, and one winter is "
                "weather",
            "Cold winters cannot happen while the climate is warming",
            "A single winter is too warm to be measured with any accuracy",
            "Winter temperatures are not included in the global average",
        ],
        "correct_index": 0,
        "why": "The warming signal is a long-term trend in a mean; individual "
               "seasons vary a great deal around that mean without changing "
               "it.",
    },
    {
        "id": "ks4-global-warming-s10",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a change in a species' distribution is not the "
                "same as a change in its abundance.",
        "options": [
            "Distribution is counted in summer; abundance is counted in "
                "the winter",
            "Distribution applies to plants, while abundance applies to "
                "animals",
            "Distribution is measured by scientists, while abundance is "
                "estimated by farmers",
            "Distribution is where it is found; abundance is how many "
                "there are",
        ],
        "correct_index": 3,
        "why": "A species can spread into new ground while its total numbers "
               "fall, or become more numerous within an unchanged range, so "
               "the two must be reported separately.",
    },
    {
        "id": "ks4-global-warming-s11",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why insect species are often the first to show a "
                "shift in range as the climate warms.",
        "options": [
            "They have no way of controlling their own body temperature",
            "They breed quickly and fly, so their range can move within a "
                "few years",
            "They are unable to survive any change in the temperature "
                "around them",
            "They are counted more often than any other group of living "
                "organisms",
        ],
        "correct_index": 1,
        "why": "Short generations and flight mean an insect population can "
               "colonise newly suitable ground far faster than a tree or a "
               "slow-moving animal.",
    },
    {
        "id": "ks4-global-warming-s12",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The mean global temperature has risen by 1.2 degrees Celsius "
                "from a 1850 baseline of 13.7 degrees Celsius. Calculate the "
                "current mean.",
        "options": [
            "16.4 degrees Celsius",
            "13.8 degrees Celsius",
            "14.9 degrees Celsius",
            "12.5 degrees Celsius",
        ],
        "correct_index": 2,
        "why": "13.7 + 1.2 = 14.9 degrees Celsius.",
    },
    {
        "id": "ks4-global-warming-s13",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how warming can reduce biodiversity even in a habitat "
                "where no species is killed by heat.",
        "options": [
            "Heat removes the soil from the habitat, so nothing is able to "
                "grow in it",
            "Warming makes every species in the habitat grow to exactly "
                "the same size as each other",
            "Warmth stops all photosynthesis, so the habitat runs out of "
                "oxygen completely",
            "Species arrive, leave or fail to breed, so the community "
                "loses members",
        ],
        "correct_index": 3,
        "why": "Ranges shift, breeding fails and competitors move in; the "
               "species that leave or stop breeding are lost from that "
               "community without anything dying of heat.",
    },
    {
        "id": "ks4-global-warming-s14",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why flooding a coastal salt marsh reduces the number "
                "of bird species that feed there.",
        "options": [
            "Rising water washes every insect out of the air above the "
                "whole marsh",
            "The mud the birds feed on is lost beneath permanent sea water",
            "Sea water is too salty for a wading bird species to drink",
            "Birds are unable to fly over water that is deeper than a "
                "metre",
        ],
        "correct_index": 1,
        "why": "Wading birds feed on invertebrates in exposed mud, so "
               "permanently flooding the marsh removes the feeding ground "
               "rather than the birds themselves.",
    },
    {
        "id": "ks4-global-warming-s15",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why insulating homes and switching to renewable "
                "electricity both slow global warming.",
        "options": [
            "Both lower the temperature of the air around the building",
            "Both reduce the amount of methane produced by farm livestock",
            "Both reduce the fossil fuel burned, so less carbon dioxide is "
                "released",
            "Both absorb carbon dioxide from the air inside a building",
        ],
        "correct_index": 2,
        "why": "Insulation cuts the fuel needed for heating and renewables "
               "replace fuel burned for electricity, so both reduce emissions.",
    },
    {
        "id": "ks4-global-warming-s16",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bird that arrives from Africa on the same date "
                "each year may find less food than it used to.",
        "options": [
            "Warmth has moved the caterpillar peak earlier, before the "
                "birds arrive",
            "Warmth has killed every caterpillar in the wood before the "
                "spring",
            "The birds now fly more slowly, so they use up their energy on "
                "the way",
            "Caterpillars have moved to a different wood and taken all "
                "their food with them",
        ],
        "correct_index": 0,
        "why": "Spring events are happening earlier, so a bird whose arrival "
               "date is fixed by day length can miss the short peak of "
               "caterpillars its chicks need.",
    },
    {
        "id": "ks4-global-warming-s17",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why permafrost thawing in the Arctic adds to global "
                "warming.",
        "options": [
            "Thawed ground absorbs methane from the air and releases it as "
                "carbon",
            "Frozen plant remains thaw and decay, releasing carbon dioxide "
                "and methane",
            "Thawed soil reflects far more sunlight, which heats the air "
                "above it",
            "Melting permafrost releases the oxygen that had been frozen "
                "inside it for ages",
        ],
        "correct_index": 1,
        "why": "Permafrost holds thousands of years of undecayed organic "
               "matter; once it thaws, decomposers respire it and release "
               "greenhouse gases that were locked away.",
    },
    {
        "id": "ks4-global-warming-s18",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country emits 320 million tonnes of carbon dioxide and cuts "
                "this by 25%. Calculate the new figure.",
        "options": [
            "295 million tonnes",
            "400 million tonnes",
            "240 million tonnes",
            "80 million tonnes",
        ],
        "correct_index": 2,
        "why": "25% of 320 is 80, and 320 − 80 = 240 million tonnes.",
    },
    {
        "id": "ks4-global-warming-s19",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why eating less beef reduces a person's contribution "
                "to global warming.",
        "options": [
            "Cattle release methane, and rearing them uses land and fuel",
            "Beef must be cooked for longer, which uses more electricity",
            "Cattle absorb carbon dioxide, so eating them releases it "
                "again",
            "Beef is transported by air, and no other food ever is",
        ],
        "correct_index": 0,
        "why": "Ruminant digestion produces methane, and the land cleared and "
               "the feed grown for cattle carry their own emissions, so less "
               "beef means fewer emissions.",
    },
    {
        "id": "ks4-global-warming-s20",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why scientists publish their climate data and let "
                "other scientists check it.",
        "options": [
            "Publishing is required before a measurement may be taken",
            "It allows the public to vote on which conclusion is the "
                "correct one",
            "It proves the data are right, because published work cannot "
                "be wrong",
            "Peer review tests the method and the conclusions, so errors "
                "are found",
        ],
        "correct_index": 3,
        "why": "Independent checking of method, data and reasoning is what "
               "makes a scientific claim trustworthy, and it is why the "
               "overall conclusion is held with confidence.",
    },
    {
        "id": "ks4-global-warming-s21",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a species living on a small low-lying island is "
                "at particular risk from rising seas.",
        "options": [
            "Islands warm faster than mainlands because they are "
                "surrounded by sea",
            "Salt spray blows a great deal further inland on an island "
                "than on a mainland coast",
            "Its whole habitat can be flooded, and there is nowhere higher "
                "to go",
            "Island species are unable to swim, unlike species on a "
                "mainland",
        ],
        "correct_index": 2,
        "why": "Range shift needs somewhere to shift to; on a low island the "
               "whole of the habitat is within reach of the rising water.",
    },
    {
        "id": "ks4-global-warming-s22",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why planting trees in a city is described as helping "
                "with global warming in two ways.",
        "options": [
            "They absorb carbon dioxide, and their shade reduces the need "
                "for cooling",
            "They absorb methane, and their roots take carbon out of the "
                "soil",
            "They release oxygen, and oxygen cancels out the greenhouse "
                "gases",
            "They block the wind, and still air holds less carbon dioxide",
        ],
        "correct_index": 0,
        "why": "The carbon fixed into the wood is one effect; shading "
               "buildings and streets so that less energy is spent on cooling "
               "is the second.",
    },
    {
        "id": "ks4-global-warming-s23",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a species that depends on one food plant is at "
                "greater risk from warming than a species that eats many.",
        "options": [
            "Specialists are smaller, and small species die out first",
            "Eating one plant means the species reproduces once a year",
            "A specialist cannot move, while a generalist can fly",
            "If that plant's range moves, the specialist has nothing else "
                "to eat",
        ],
        "correct_index": 3,
        "why": "A generalist can switch to whatever is available as the "
               "community changes; a specialist's survival is tied to one "
               "species that may not shift with it.",
    },
    {
        "id": "ks4-global-warming-s24",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why methane matters even though there is far less of "
                "it in the air than carbon dioxide.",
        "options": [
            "Methane blocks sunlight, so the ground below it cannot cool "
                "down",
            "Each methane molecule traps far more heat than a carbon "
                "dioxide one",
            "Methane is heavier, so it settles close to the Earth's "
                "surface",
            "Methane reacts with oxygen and produces heat directly in the "
                "air",
        ],
        "correct_index": 1,
        "why": "Methane is a much stronger greenhouse gas per molecule, so "
               "even a small rise in its concentration has a large warming "
               "effect.",
    },
    {
        "id": "ks4-global-warming-s25",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Arctic sea ice in September fell from 7.0 million square "
                "kilometres to 4.2 million. Calculate the percentage fall.",
        "options": [
            "40%",
            "28%",
            "60%",
            "2.8%",
        ],
        "correct_index": 0,
        "why": "The fall is 7.0 − 4.2 = 2.8, and 2.8 ÷ 7.0 × 100 = 40%.",
    },
    {
        "id": "ks4-global-warming-s26",
        "subtopic_slug": "global-warming",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a warmer climate can let a disease-carrying "
                "insect live in places it could not live before.",
        "options": [
            "Warm air carries the insect much further than cold air is "
                "able to",
            "Warmth makes the insect larger, so it is able to fly a great "
                "deal further north",
            "The insect changes into a new species whenever the climate "
                "warms up",
            "Winters are no longer cold enough to kill it, so it survives "
                "all year",
        ],
        "correct_index": 3,
        "why": "Cold winters set the northern limit for many insects; as that "
               "limit weakens, the insect and any pathogen it carries can "
               "become established further north.",
    },
    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Evidence handled honestly, multi-step arithmetic, and claims about
    # warming weighed against what the data can actually support.
    {
        "id": "ks4-global-warming-h05",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a mean rise of 1.5 degrees Celsius can be "
                "described as serious when a day-to-day change of 1.5 degrees "
                "is not noticed.",
        "options": [
            "Daily changes are weather and have no effect on any living "
                "organism",
            "A one-degree change lasts a day, a mean change lasts a year",
            "A shift in the mean moves the extremes, so heatwaves and "
                "floods become far more common",
            "A mean is measured more accurately, so a small change in it "
                "is bigger",
        ],
        "correct_index": 2,
        "why": "The whole distribution shifts, so events that used to be rare "
               "at the hot end become ordinary — and it is the extremes that "
               "kill organisms and destroy habitats.",
    },
    {
        "id": "ks4-global-warming-h06",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sea level rose 1.4 mm per year from 1900 to 1990 and 3.6 mm "
                "per year since. Determine how many times faster the recent "
                "rate is.",
        "options": [
            "About 2.6 times",
            "About 2.2 times",
            "About 5.0 times",
            "About 0.4 times",
        ],
        "correct_index": 0,
        "why": "3.6 ÷ 1.4 = 2.57, so the recent rate is about 2.6 times the "
               "earlier one.",
    },
    {
        "id": "ks4-global-warming-h07",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that because climate models cannot predict "
                "2100 exactly, no action should be taken now.",
        "options": [
            "It is sound, because an uncertain prediction carries no "
                "information",
            "It is sound, because models will be exact within a few more "
                "years of research",
            "It is weak, because climate models are known to be exact in "
                "every one of their predictions",
            "It is weak, because the direction of the change is clear even "
                "where the size is uncertain",
        ],
        "correct_index": 3,
        "why": "Uncertainty is about how much and how fast, not about whether; "
               "waiting for certainty means acting only once the change has "
               "happened.",
    },
    {
        "id": "ks4-global-warming-h08",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant's northern limit moved 120 km north in 40 years. "
                "Determine the mean rate in kilometres per year.",
        "options": [
            "4800 km per year",
            "3 km per year",
            "0.3 km per year",
            "30 km per year",
        ],
        "correct_index": 1,
        "why": "120 km ÷ 40 years = 3 km per year.",
    },
    {
        "id": "ks4-global-warming-h09",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two species share a wood. One shifts its range 3 km a year "
                "and the other 0.2 km a year. Predict what happens to the "
                "relationship between them.",
        "options": [
            "They separate, so a predator, prey or pollinator link is "
                "broken",
            "They move together, because species in one wood shift at one "
                "rate",
            "Both stop moving, because neither is able to survive without "
                "the other beside it",
            "The slower species speeds up to match, so the link is kept "
                "intact",
        ],
        "correct_index": 0,
        "why": "Species track climate at their own rates, so partners in a "
               "food chain or a pollination relationship can end up in "
               "different places.",
    },
    {
        "id": "ks4-global-warming-h10",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why warming reduces the amount of carbon dioxide the "
                "oceans can absorb, and why this matters.",
        "options": [
            "Warm water holds more gas, so the ocean removes the problem "
                "itself",
            "Warming makes sea water acidic, which drives the dissolved "
                "gas out",
            "Warm oceans grow more algae, and algae release carbon dioxide",
            "Gases are less soluble in warm water, so a weakening sink "
                "leaves more in the air",
        ],
        "correct_index": 3,
        "why": "A warmer ocean dissolves less carbon dioxide, so a sink that "
               "has been absorbing part of our emissions takes up less — which "
               "speeds the rise rather than slowing it.",
    },
    {
        "id": "ks4-global-warming-h11",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why thawing permafrost is described as a process that "
                "makes itself worse.",
        "options": [
            "Thawed soil absorbs methane from the atmosphere and locks it "
                "back away",
            "Thawing releases gases that warm the air, which thaws more "
                "permafrost",
            "Thawed ground freezes again each winter, which releases the "
                "gas twice a year",
            "Thawing cools the Arctic, so more ice forms and reflects more "
                "sunlight",
        ],
        "correct_index": 1,
        "why": "The greenhouse gases released by decay warm the atmosphere, "
               "and the warmer atmosphere thaws more permafrost — a loop that "
               "reinforces itself.",
    },
    {
        "id": "ks4-global-warming-h12",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the risk to a species living on a large continent "
                "with one living on an isolated island, as the climate warms.",
        "options": [
            "The two are at equal risk, because the global mean rises the "
                "same",
            "The island species is safer, because the sea around it keeps "
                "the island permanently cool",
            "The island species is at greater risk, as it has nowhere to "
                "shift its range to",
            "The continental species is at greater risk, because a "
                "continent warms faster than an island",
        ],
        "correct_index": 2,
        "why": "Range shift needs somewhere to shift to; a continent offers "
               "land in every direction, an island offers none.",
    },
    {
        "id": "ks4-global-warming-h13",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a species arriving in a new area as the climate "
                "warms can reduce the biodiversity there.",
        "options": [
            "It brings extra carbon dioxide with it, which harms the "
                "resident species",
            "New arrivals are sterile, so they take the space but leave no "
                "young",
            "A new species cools the habitat, which the resident species "
                "are unable to survive",
            "It may outcompete resident species for food or space and "
                "displace them",
        ],
        "correct_index": 3,
        "why": "An arrival that competes strongly, or that brings a disease "
               "the residents have not met, can push resident species out even "
               "as the species count briefly rises.",
    },
    {
        "id": "ks4-global-warming-h14",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wetland of 4000 hectares loses 15% of its area to the sea, "
                "then 10% of what is left. Determine the area remaining.",
        "options": [
            "2600 hectares",
            "3060 hectares",
            "3000 hectares",
            "3400 hectares",
        ],
        "correct_index": 1,
        "why": "15% of 4000 is 600, leaving 3400; 10% of 3400 is 340, leaving "
               "3060 hectares.",
    },
    {
        "id": "ks4-global-warming-h15",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why building a sea wall along a coast can destroy a "
                "salt marsh even though it stops the flooding.",
        "options": [
            "The wall keeps out the fresh water that the salt marsh plants "
                "need to survive",
            "Concrete releases a chemical that kills the invertebrates in "
                "the marsh mud",
            "The marsh is squeezed against the wall as the sea rises and "
                "cannot move inland",
            "A sea wall shades the marsh so completely that no plant can "
                "photosynthesise",
        ],
        "correct_index": 2,
        "why": "A salt marsh normally migrates inland as the sea rises; a "
               "fixed wall behind it leaves no room, so the habitat is lost "
               "between the wall and the water.",
    },
    {
        "id": "ks4-global-warming-h16",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the argument that an individual's choices cannot "
                "matter because global emissions are so large.",
        "options": [
            "It is weak, because individual choices sum and shape what is "
                "produced and sold",
            "It is sound, because one person's emissions are too small to "
                "measure",
            "It is sound, because emissions are set by governments and by "
                "nobody else",
            "It is weak, because one person's choices can halve a "
                "country's total emissions",
        ],
        "correct_index": 0,
        "why": "Individual decisions aggregate into demand, and demand is what "
               "determines how much is produced — though policy and industry "
               "change matter alongside it.",
    },
    {
        "id": "ks4-global-warming-h17",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the record of species ranges is stronger evidence "
                "of warming when it covers many species than when it covers "
                "one.",
        "options": [
            "One species moves at random, while several move in a straight "
                "line",
            "One species could move for its own reasons; many moving the "
                "same way needs a shared cause",
            "A single species is not counted accurately enough to be "
                "evidence",
            "Many species make the total number of records larger, and "
                "larger is more exact",
        ],
        "correct_index": 1,
        "why": "Disease, land-use change or a new predator can move one "
               "species; a consistent poleward shift across many unrelated "
               "species points to climate.",
    },
    {
        "id": "ks4-global-warming-h18",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Emissions must fall from 40 to 10 billion tonnes a year. "
                "Determine the percentage reduction required.",
        "options": [
            "30%",
            "400%",
            "75%",
            "25%",
        ],
        "correct_index": 2,
        "why": "The fall is 40 − 10 = 30, and 30 ÷ 40 × 100 = 75%.",
    },
    {
        "id": "ks4-global-warming-h19",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to a mountain species whose range has "
                "already reached the summit.",
        "options": [
            "It has no cooler ground left, so its population declines "
                "towards extinction",
            "It begins to move downhill again, having adapted to the "
                "warmer conditions",
            "It leaves the mountain and flies to the next mountain range "
                "along",
            "Its numbers rise, because the summit has the most space "
                "available on the mountain",
        ],
        "correct_index": 0,
        "why": "Moving uphill works only while there is more mountain; at the "
               "summit the range can shrink but cannot shift, so the "
               "population is squeezed out.",
    },
    {
        "id": "ks4-global-warming-h20",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cutting methane emissions has a faster effect on "
                "warming than cutting carbon dioxide emissions.",
        "options": [
            "Methane is heavier, so it falls out of the air within a few "
                "days",
            "Methane traps less heat, so removing it changes things sooner",
            "Methane is produced only by farms, which can be closed "
                "quickly",
            "Methane is removed from the atmosphere within about a decade",
        ],
        "correct_index": 3,
        "why": "Methane breaks down in the atmosphere in roughly a decade, "
               "while carbon dioxide persists for centuries, so a methane cut "
               "shows up in the temperature record far sooner.",
    },
    {
        "id": "ks4-global-warming-h21",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare protecting an existing forest with planting a new "
                "one, as responses to global warming.",
        "options": [
            "The two are identical, because both leave exactly the same "
                "area of land covered in trees",
            "Protection has no effect, because a forest that already "
                "exists absorbs nothing",
            "Protection keeps a large store now; new planting takes "
                "decades to build one",
            "New planting works faster, because young trees hold more "
                "carbon than old ones",
        ],
        "correct_index": 2,
        "why": "Felling an old forest releases a large store immediately, so "
               "preventing that is a quicker win than growing a replacement "
               "store from seedlings.",
    },
    {
        "id": "ks4-global-warming-h22",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why global temperature records from before 1900 are "
                "harder to rely on than modern ones.",
        "options": [
            "Fewer places were measured, with less consistent instruments "
                "and methods",
            "Temperatures were not written down until the year 1900",
            "The Earth was not warming then, so nobody bothered to record "
                "it",
            "Older thermometers measured in a different unit that cannot "
                "be converted",
        ],
        "correct_index": 0,
        "why": "Sparse coverage and varying instruments and siting make early "
               "records less certain, which is why scientists state "
               "uncertainties alongside the trend.",
    },
    {
        "id": "ks4-global-warming-h23",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reserve records 60 species. Warming brings 8 new species "
                "and removes 14. Determine the percentage change in the "
                "species count.",
        "options": [
            "A fall of 6%",
            "A rise of 13%",
            "A fall of 23%",
            "A fall of 10%",
        ],
        "correct_index": 3,
        "why": "The net change is 8 − 14 = −6 species, and 6 ÷ 60 × 100 = 10%, "
               "so the count falls by 10%.",
    },
    {
        "id": "ks4-global-warming-h24",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a species may fail to shift its range even when "
                "suitable climate exists further north.",
        "options": [
            "The new area is colder, and no species is able to tolerate a "
                "colder place",
            "Roads, farmland and cities can block the route between the "
                "two areas",
            "Species are unable to travel north, because they navigate by "
                "the Sun",
            "A species must be given permission before it may enter a new "
                "county",
        ],
        "correct_index": 1,
        "why": "A shift needs a continuous route of usable habitat; a "
               "fragmented landscape can leave a species stranded in a place "
               "that is becoming unsuitable.",
    },
    {
        "id": "ks4-global-warming-h25",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the suggestion that global warming will be good for "
                "the United Kingdom because its summers will be warmer.",
        "options": [
            "It is weak, because flooding, drought and lost species come "
                "with the warmer summers",
            "It is sound, because a warmer summer is the only change that "
                "warming will bring",
            "It is sound, because crops always grow better in every warmer "
                "climate",
            "It is weak, because the United Kingdom will become colder "
                "rather than warmer",
        ],
        "correct_index": 0,
        "why": "The same warming brings heavier winter rainfall, summer "
               "drought, coastal flooding and the loss of species adapted to a "
               "cooler climate.",
    },
    {
        "id": "ks4-global-warming-h26",
        "subtopic_slug": "global-warming",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why global emissions can keep rising even while many "
                "countries are cutting their own.",
        "options": [
            "Cutting emissions in one country forces every other country "
                "to raise theirs",
            "Carbon dioxide already in the air is counted again in each "
                "and every new year's total",
            "A country that cuts its emissions stops reporting them, so "
                "they vanish",
            "Emissions elsewhere are growing by more than those countries "
                "are cutting",
        ],
        "correct_index": 3,
        "why": "The total is a global sum, so reductions in some countries can "
               "be outweighed by growth in others — which is why the problem "
               "needs agreement between them.",
    },
]
