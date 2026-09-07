"""Chemistry · The atmosphere — composition, the early atmosphere, greenhouse
gases and pollutants from fuels.

Four BASE subtopics, so nothing here uses Higher-only vocabulary or a
rearrangement a Foundation Combined class would not meet.

Distractors come from the declared misconceptions: nitrogen and oxygen swapped
in the modern atmosphere; the early atmosphere described as oxygen-rich, or
oxygen credited to volcanoes rather than to cyanobacteria; the greenhouse
effect treated as harmful in itself rather than the ENHANCED effect being the
problem; greenhouse warming confused with ozone and UV; and carbon monoxide
given a smell or a colour it does not have.
"""

TOPIC = "atmosphere"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── composition-of-atmosphere ───────────────────────────────────────
    {
        "id": "ks4-composition-of-atmosphere-e01",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which gas is the most abundant in the Earth's atmosphere?",
        "options": [
            "Oxygen",
            "Carbon dioxide",
            "Nitrogen",
            "Argon",
        ],
        "correct_index": 2,
        "why": "Nitrogen is roughly four fifths of the air, at about 78%; "
               "oxygen is about one fifth.",
    },
    {
        "id": "ks4-composition-of-atmosphere-e02",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate percentage of carbon dioxide in the "
                "atmosphere today.",
        "options": [
            "0.04%",
            "0.90%",
            "4.00%",
            "21.0%",
        ],
        "correct_index": 0,
        "why": "CO2 is only about 0.04% of the air, yet it drives both "
               "photosynthesis and the greenhouse effect.",
    },
    {
        "id": "ks4-composition-of-atmosphere-e03",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which noble gas makes up about 0.9% of the atmosphere?",
        "options": [
            "Helium",
            "Argon",
            "Neon",
            "Krypton",
        ],
        "correct_index": 1,
        "why": "Argon is the third most abundant gas in the air, at roughly "
               "0.9%.",
    },
    {
        "id": "ks4-composition-of-atmosphere-e04",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which process releases carbon dioxide into the atmosphere?",
        "options": [
            "Photosynthesis in green plants",
            "Nitrogen fixation by bacteria in the soil",
            "Condensation of water vapour into clouds",
            "Respiration in living organisms",
        ],
        "correct_index": 3,
        "why": "Respiration releases CO2, balancing the CO2 that "
               "photosynthesis removes.",
    },
    {
        "id": "ks4-composition-of-atmosphere-s01",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the amount of water vapour in air can be given "
                "as a single fixed percentage. Explain why this is wrong.",
        "options": [
            "Water vapour is not a gas, so it cannot be given as a percentage "
            "of the air",
            "Water vapour is always exactly 1% of air, which is too small an "
            "amount to measure",
            "Water vapour reacts with nitrogen, so its amount falls to zero "
            "every night",
            "Water vapour varies from almost none in a desert to about 4% in "
            "humid air",
        ],
        "correct_index": 3,
        "why": "Water vapour is the one major component of air whose "
               "proportion changes with place and with weather.",
    },
    {
        "id": "ks4-composition-of-atmosphere-s02",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why nitrogen has remained the most abundant gas in "
                "the atmosphere.",
        "options": [
            "Nitrogen is denser than the other gases, so it settles near the "
            "ground and cannot escape",
            "Nitrogen is very unreactive, so few processes remove it from the "
            "air",
            "Nitrogen is released by volcanoes faster than living things can "
            "possibly use it up",
            "Nitrogen is produced by respiration in every living organism on "
            "Earth",
        ],
        "correct_index": 1,
        "why": "The bond in an N2 molecule is very strong, so nitrogen takes "
               "little part in reactions and simply accumulates.",
    },
    {
        "id": "ks4-composition-of-atmosphere-s03",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the proportions of oxygen and carbon dioxide in "
                "the air are kept roughly balanced in nature.",
        "options": [
            "Photosynthesis removes CO2 and releases O2, while respiration "
            "and combustion do the reverse",
            "Oxygen slowly turns into carbon dioxide in sunlight and back "
            "again during the night",
            "The oceans release oxygen and absorb carbon dioxide at exactly "
            "equal rates all year",
            "Nitrogen-fixing bacteria convert oxygen into carbon dioxide "
            "whenever levels get too high",
        ],
        "correct_index": 0,
        "why": "The carbon cycle balances the two: what photosynthesis takes "
               "out, respiration and combustion put back.",
    },
    {
        "id": "ks4-composition-of-atmosphere-s04",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why cutting down large areas of forest raises the "
                "amount of carbon dioxide in the atmosphere.",
        "options": [
            "Felled trees release the nitrogen they stored, which then reacts "
            "with oxygen to make CO2",
            "Bare soil reflects more sunlight, and the extra warmth drives "
            "CO2 out of the oceans",
            "Fewer trees means less photosynthesis, so less CO2 is removed "
            "from the air",
            "Trees are the only organisms that respire, so removing them "
            "stops CO2 being used up",
        ],
        "correct_index": 2,
        "why": "Photosynthesis is the main route by which CO2 leaves the air, "
               "so losing forests slows that removal.",
    },
    {
        "id": "ks4-composition-of-atmosphere-h01",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of dry air has a volume of 500 cm3. Calculate the "
                "volume of oxygen it contains.",
        "options": [
            "390 cm3",
            "105 cm3",
            "250 cm3",
            "4.5 cm3",
        ],
        "correct_index": 1,
        "why": "Oxygen is about 21% of dry air, and 21% of 500 cm3 is 105 cm3.",
    },
    {
        "id": "ks4-composition-of-atmosphere-h02",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why carbon dioxide is described as being present in a "
                "tiny proportion of the air and yet being critically "
                "important.",
        "options": [
            "It is the only gas plants can absorb, and it makes up most of "
            "their mass when grown",
            "It is the densest gas in the air, so it provides most of the "
            "atmospheric pressure",
            "It is the gas breathed in by animals and released by plants "
            "during the night",
            "At 0.04% it is the raw material for photosynthesis and an "
            "important greenhouse gas",
        ],
        "correct_index": 3,
        "why": "Small proportion, large role: CO2 feeds every food chain "
               "through photosynthesis and absorbs infrared radiation.",
    },
    {
        "id": "ks4-composition-of-atmosphere-h03",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the amounts of argon and carbon dioxide in the air, "
                "and suggest why argon is discussed far less often.",
        "options": [
            "Argon is less abundant than CO2, and far too rare to have any "
            "effect on the Earth",
            "Argon and CO2 are equally abundant, but argon is invisible while "
            "CO2 can be seen",
            "Argon is about 20 times more abundant than CO2, but it is "
            "unreactive and not a greenhouse gas",
            "Argon is about 20 times more abundant than CO2, and it is the "
            "main cause of the greenhouse effect",
        ],
        "correct_index": 2,
        "why": "Argon is 0.9% against CO2's 0.04%, but as an unreactive noble "
               "gas it takes no part in the carbon cycle or in warming.",
    },
    {
        "id": "ks4-composition-of-atmosphere-h04",
        "subtopic_slug": "composition-of-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Over the last 200 years the carbon dioxide level has risen "
                "from about 0.028% to about 0.042%. Calculate the percentage "
                "increase in the carbon dioxide level.",
        "options": [
            "50%",
            "1.4%",
            "0.014%",
            "150%",
        ],
        "correct_index": 0,
        "why": "The rise is 0.014 on a starting value of 0.028, and "
               "0.014 ÷ 0.028 = 0.50, which is a 50% increase.",
    },

    # ── early-atmosphere ────────────────────────────────────────────────
    {
        "id": "ks4-early-atmosphere-e01",
        "subtopic_slug": "early-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which gas is believed to have made up most of the Earth's "
                "early atmosphere?",
        "options": [
            "Carbon dioxide",
            "Oxygen",
            "Nitrogen",
            "Sulfur dioxide",
        ],
        "correct_index": 0,
        "why": "The early atmosphere is thought to have been mainly CO2, much "
               "like the atmospheres of Mars and Venus today.",
    },
    {
        "id": "ks4-early-atmosphere-e02",
        "subtopic_slug": "early-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the process that released the gases of the early "
                "atmosphere from the Earth's interior.",
        "options": [
            "Photosynthesis by the earliest bacteria",
            "Condensation of water vapour into oceans",
            "Weathering of the Earth's first rocks",
            "Volcanic activity, also called outgassing",
        ],
        "correct_index": 3,
        "why": "Intense volcanic activity released CO2, water vapour and "
               "nitrogen from inside the young Earth.",
    },
    {
        "id": "ks4-early-atmosphere-e03",
        "subtopic_slug": "early-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the organisms that first produced oxygen on Earth.",
        "options": [
            "Fungi",
            "Land plants",
            "Cyanobacteria",
            "Denitrifying bacteria",
        ],
        "correct_index": 2,
        "why": "Cyanobacteria evolved photosynthesis about 2.7 billion years "
               "ago and began releasing oxygen.",
    },
    {
        "id": "ks4-early-atmosphere-e04",
        "subtopic_slug": "early-atmosphere",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the Earth's oceans formed.",
        "options": [
            "Comets delivered liquid water to the surface over millions of "
            "years",
            "Water vapour condensed as the Earth cooled below 100 °C",
            "Oxygen and hydrogen in the atmosphere reacted together in "
            "sunlight",
            "Volcanoes erupted liquid water from beneath the Earth's crust",
        ],
        "correct_index": 1,
        "why": "While the Earth was very hot water could exist only as vapour; "
               "cooling below 100 °C let it condense into oceans.",
    },
    {
        "id": "ks4-early-atmosphere-s01",
        "subtopic_slug": "early-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Write the balanced equation for photosynthesis, the process "
                "that added oxygen to the early atmosphere.",
        "options": [
            "C6H12O6 + 6O2 → 6CO2 + 6H2O",
            "6CO2 + 6H2O → C6H12O6 + 3O2",
            "6CO2 + 6H2O → C6H12O6 + 6O2",
            "CO2 + H2O → C6H12O6 + O2",
        ],
        "correct_index": 2,
        "why": "Six CO2 and six H2O give one glucose and six O2, so both sides "
               "of the equation balance.",
    },
    {
        "id": "ks4-early-atmosphere-s02",
        "subtopic_slug": "early-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why oxygen did not build up in the atmosphere as soon "
                "as cyanobacteria appeared.",
        "options": [
            "Cyanobacteria used up all the oxygen they made during "
            "respiration at night",
            "The oxygen first reacted with iron dissolved in the oceans and "
            "with surface rocks",
            "Oxygen is lighter than air, so it escaped into space until the "
            "Earth had cooled",
            "Volcanoes released enough CO2 to react with all of the oxygen "
            "produced",
        ],
        "correct_index": 1,
        "why": "Oxygen was absorbed by sinks such as dissolved iron, forming "
               "banded iron formations, before it could accumulate.",
    },
    {
        "id": "ks4-early-atmosphere-s03",
        "subtopic_slug": "early-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how carbon from the atmosphere became locked away "
                "in limestone rock.",
        "options": [
            "Carbon dioxide reacted directly with the rocks of the sea bed to "
            "form carbonate",
            "Carbon dioxide was compressed by the weight of the oceans until "
            "it became a solid",
            "Carbon dioxide was buried by volcanic ash and crushed into rock "
            "over millions of years",
            "Marine organisms used dissolved CO2 to make shells that built up "
            "as sediment",
        ],
        "correct_index": 3,
        "why": "Shelled sea creatures made calcium carbonate from dissolved "
               "CO2, and their remains formed limestone.",
    },
    {
        "id": "ks4-early-atmosphere-s04",
        "subtopic_slug": "early-atmosphere",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the proportion of nitrogen in the atmosphere rose "
                "over billions of years, even though little extra nitrogen "
                "was added.",
        "options": [
            "Nitrogen is unreactive, so it stayed put while CO2 and water "
            "vapour were removed",
            "Nitrogen was released steadily by the cyanobacteria alongside "
            "the oxygen they made",
            "Nitrogen was formed when oxygen reacted with ammonia released by "
            "the volcanoes",
            "Nitrogen is the densest gas in air, so it sank and concentrated "
            "near the ground",
        ],
        "correct_index": 0,
        "why": "Removing the other gases raises nitrogen's share of what is "
               "left — nitrogen simply did not react away.",
    },
    {
        "id": "ks4-early-atmosphere-h01",
        "subtopic_slug": "early-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Scientists have no samples of the early atmosphere. Evaluate "
                "the evidence on which descriptions of it are based.",
        "options": [
            "There is no evidence at all, so any description is only ever a "
            "guess",
            "Ice cores hold trapped air from four billion years ago, giving "
            "direct evidence",
            "The early atmosphere can be recreated exactly in a laboratory, "
            "which proves the theory",
            "Evidence is indirect — ancient rocks and other planets — so "
            "theories may be revised",
        ],
        "correct_index": 3,
        "why": "No direct sample exists, so the model rests on indirect "
               "evidence and stays open to revision.",
    },
    {
        "id": "ks4-early-atmosphere-h02",
        "subtopic_slug": "early-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the formation of the ozone layer was important "
                "for the evolution of life on land.",
        "options": [
            "Ozone absorbs ultraviolet radiation, which would otherwise be "
            "lethal at the surface",
            "Ozone provided the oxygen that the first land animals needed in "
            "order to breathe",
            "Ozone trapped heat and warmed the land enough for living things "
            "to survive on it",
            "Ozone reacted with carbon dioxide, lowering its level so that "
            "plants could grow",
        ],
        "correct_index": 0,
        "why": "Ozone, O3, formed once oxygen levels rose, and it screens out "
               "the UV that would damage organisms at the surface.",
    },
    {
        "id": "ks4-early-atmosphere-h03",
        "subtopic_slug": "early-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The atmosphere of Mars today is about 95% carbon dioxide. "
                "Suggest what this contributes to scientists' understanding "
                "of the Earth's early atmosphere.",
        "options": [
            "It proves that the Earth's early atmosphere was also exactly 95% "
            "carbon dioxide",
            "It supports the idea of a CO2-rich early atmosphere, since Mars "
            "has no photosynthesis",
            "It shows that every planet keeps the same atmosphere for the "
            "whole of its existence",
            "It shows that the Earth's carbon dioxide escaped to Mars as the "
            "Earth slowly cooled",
        ],
        "correct_index": 1,
        "why": "Mars never developed photosynthesis or oceans, so its "
               "CO2-rich air is evidence of what an early atmosphere is like.",
    },
    {
        "id": "ks4-early-atmosphere-h04",
        "subtopic_slug": "early-atmosphere",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The early atmosphere was rich in carbon dioxide with almost "
                "no oxygen; today the reverse is true. Explain the two main "
                "changes that produced this reversal.",
        "options": [
            "Volcanoes switched from releasing carbon dioxide to releasing "
            "oxygen as the Earth cooled",
            "Ultraviolet light split carbon dioxide into carbon and oxygen "
            "throughout the atmosphere",
            "CO2 dissolved in the oceans and was locked into rock, while "
            "photosynthesis released O2",
            "Nitrogen replaced the carbon dioxide, and oxygen leaked in from "
            "space over billions of years",
        ],
        "correct_index": 2,
        "why": "Two processes did it: the oceans and limestone took CO2 out, "
               "and photosynthesis put O2 in.",
    },

    # ── greenhouse-gases ────────────────────────────────────────────────
    {
        "id": "ks4-greenhouse-gases-e01",
        "subtopic_slug": "greenhouse-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these gases is a greenhouse gas?",
        "options": [
            "Nitrogen",
            "Argon",
            "Oxygen",
            "Methane",
        ],
        "correct_index": 3,
        "why": "Methane absorbs infrared radiation; nitrogen, oxygen and argon "
               "do not.",
    },
    {
        "id": "ks4-greenhouse-gases-e02",
        "subtopic_slug": "greenhouse-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of radiation absorbed by greenhouse gases.",
        "options": [
            "Ultraviolet radiation arriving from the Sun",
            "Infrared radiation emitted by the Earth's surface",
            "Visible light on its way down through the atmosphere",
            "Radio waves reflected by the upper atmosphere",
        ],
        "correct_index": 1,
        "why": "Sunlight passes through, the warmed surface re-emits it as "
               "infrared, and it is that infrared the gases absorb.",
    },
    {
        "id": "ks4-greenhouse-gases-e03",
        "subtopic_slug": "greenhouse-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the main greenhouse gas released when fossil fuels are "
                "burned.",
        "options": [
            "Carbon dioxide",
            "Nitrogen",
            "Methane",
            "Sulfur dioxide",
        ],
        "correct_index": 0,
        "why": "Complete combustion of a hydrocarbon produces carbon dioxide; "
               "sulfur dioxide is also released, but it causes acid rain "
               "rather than warming.",
    },
    {
        "id": "ks4-greenhouse-gases-e04",
        "subtopic_slug": "greenhouse-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define the term carbon footprint.",
        "options": [
            "The mass of carbon contained inside a fuel before it is burned",
            "The area of forest that is needed to absorb a country's carbon "
            "dioxide",
            "The total greenhouse gases released over a product's whole life",
            "The percentage of carbon dioxide in the atmosphere at a given "
            "moment",
        ],
        "correct_index": 2,
        "why": "A carbon footprint totals all the greenhouse gases emitted, "
               "expressed as an equivalent mass of CO2.",
    },
    {
        "id": "ks4-greenhouse-gases-s01",
        "subtopic_slug": "greenhouse-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the greenhouse effect keeps the Earth warm.",
        "options": [
            "Greenhouse gases absorb the Earth's infrared radiation and "
            "re-emit some of it downwards",
            "Greenhouse gases reflect sunlight back to the surface, doubling "
            "the energy that arrives",
            "Greenhouse gases form a solid layer that stops warm air escaping "
            "upwards into space",
            "Greenhouse gases react with oxygen, and that reaction releases "
            "heat into the air",
        ],
        "correct_index": 0,
        "why": "The gases absorb outgoing infrared and re-emit it in all "
               "directions, so some energy returns to the surface.",
    },
    {
        "id": "ks4-greenhouse-gases-s02",
        "subtopic_slug": "greenhouse-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the difference between the natural greenhouse effect "
                "and the enhanced greenhouse effect.",
        "options": [
            "The natural effect warms the Earth; the enhanced effect cools it "
            "by reflecting sunlight",
            "The natural effect is caused by carbon dioxide; the enhanced "
            "effect is caused by the ozone layer",
            "The natural effect keeps the Earth habitable; the enhanced "
            "effect is extra warming from emissions",
            "The natural effect happens only at night; the enhanced effect "
            "happens only during the day",
        ],
        "correct_index": 2,
        "why": "Without the natural effect Earth would be about −18 °C; the "
               "problem is the extra warming from human-raised gas levels.",
    },
    {
        "id": "ks4-greenhouse-gases-s03",
        "subtopic_slug": "greenhouse-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why making cement adds carbon dioxide to the "
                "atmosphere even before any fuel is burned.",
        "options": [
            "Cement powder reacts with the oxygen in air to form carbon "
            "dioxide as it is made",
            "Cement absorbs carbon dioxide while it sets and releases it "
            "again when it dries out",
            "Cement is made from crude oil, which contains dissolved carbon "
            "dioxide within it",
            "Calcium carbonate is decomposed to calcium oxide, releasing CO2",
        ],
        "correct_index": 3,
        "why": "Thermal decomposition of limestone, CaCO3 → CaO + CO2, "
               "releases carbon dioxide from the rock itself.",
    },
    {
        "id": "ks4-greenhouse-gases-s04",
        "subtopic_slug": "greenhouse-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two effects of a rising global average temperature.",
        "options": [
            "Sea levels fall as water evaporates, and rainfall decreases "
            "everywhere on Earth",
            "Ice caps melt and sea levels rise, and extreme weather becomes "
            "more frequent",
            "The atmosphere loses its oxygen, and plants stop photosynthesising "
            "altogether",
            "The ozone layer thickens, and less ultraviolet radiation reaches "
            "the surface",
        ],
        "correct_index": 1,
        "why": "Warming melts land ice and expands sea water, raising sea "
               "level, and puts more energy into weather systems.",
    },
    {
        "id": "ks4-greenhouse-gases-h01",
        "subtopic_slug": "greenhouse-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student states: 'Climate change is caused by the greenhouse "
                "effect, so we should remove greenhouse gases from the air "
                "altogether.' Evaluate this statement.",
        "options": [
            "Sound — removing all greenhouse gases would return the Earth to "
            "its ideal temperature",
            "Unsound — with no greenhouse gases the Earth would be about "
            "−18 °C and uninhabitable",
            "Unsound — greenhouse gases cannot be removed because they are "
            "chemically unreactive",
            "Sound — the Earth was habitable long before greenhouse gases "
            "existed in the atmosphere",
        ],
        "correct_index": 1,
        "why": "The natural greenhouse effect makes Earth warm enough for "
               "life; the issue is the extra warming, not the effect itself.",
    },
    {
        "id": "ks4-greenhouse-gases-h02",
        "subtopic_slug": "greenhouse-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate replacing a petrol car with an electric car as a "
                "way of reducing a person's carbon footprint.",
        "options": [
            "It removes the footprint entirely, because an electric car "
            "produces no emissions anywhere",
            "It makes no difference at all, because electricity is generated "
            "by burning fossil fuels",
            "It increases the footprint, because the batteries release "
            "methane while they are charging",
            "It cuts exhaust emissions, but the saving depends on how the "
            "electricity is generated",
        ],
        "correct_index": 3,
        "why": "An electric car moves the emissions from the exhaust to the "
               "power station, so the benefit depends on the supply.",
    },
    {
        "id": "ks4-greenhouse-gases-h03",
        "subtopic_slug": "greenhouse-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a carbon footprint is expressed as a mass of "
                "'carbon dioxide equivalent' rather than by simply adding the "
                "masses of each gas released.",
        "options": [
            "Because every greenhouse gas has the same mass per molecule as "
            "carbon dioxide does",
            "Because carbon dioxide is the only greenhouse gas that can be "
            "measured accurately",
            "Because gases such as methane trap far more heat per gram than "
            "carbon dioxide does",
            "Because carbon dioxide is the only gas that stays in the "
            "atmosphere permanently",
        ],
        "correct_index": 2,
        "why": "Different gases warm by different amounts, so each is "
               "converted to the mass of CO2 that would have the same effect.",
    },
    {
        "id": "ks4-greenhouse-gases-h04",
        "subtopic_slug": "greenhouse-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A council plans to cut its carbon footprint by planting trees "
                "and by insulating its buildings. Evaluate which of the two "
                "is likely to have the more immediate effect.",
        "options": [
            "Insulation, because it cuts fuel use straight away while trees "
            "take years to grow",
            "Tree planting, because a newly planted tree absorbs a whole "
            "lifetime of CO2 at once",
            "Neither, because a single council's emissions are far too small "
            "to be measured",
            "Both equally, because every method of cutting a footprint works "
            "at the same rate",
        ],
        "correct_index": 0,
        "why": "Insulation cuts energy demand from the moment it is fitted, "
               "whereas a sapling's carbon uptake builds up slowly.",
    },

    # ── atmospheric-pollutants ──────────────────────────────────────────
    {
        "id": "ks4-atmospheric-pollutants-e01",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which pollutant is produced by the incomplete combustion of a "
                "fuel?",
        "options": [
            "Sulfur dioxide",
            "Nitrogen monoxide",
            "Carbon monoxide",
            "Water vapour",
        ],
        "correct_index": 2,
        "why": "With too little oxygen the carbon is only partly oxidised, "
               "giving carbon monoxide instead of carbon dioxide.",
    },
    {
        "id": "ks4-atmospheric-pollutants-e02",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where the sulfur comes from when burning a fuel "
                "produces sulfur dioxide.",
        "options": [
            "From the nitrogen in the air drawn into the engine",
            "From sulfur impurities present in the fuel itself",
            "From sulfur added to fuels as an anti-knock agent",
            "From the platinum inside the catalytic converter",
        ],
        "correct_index": 1,
        "why": "Fossil fuels contain sulfur compounds, and S + O2 → SO2 when "
               "they burn.",
    },
    {
        "id": "ks4-atmospheric-pollutants-e03",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which two pollutants are the main causes of acid rain?",
        "options": [
            "Carbon monoxide and particulates",
            "Carbon dioxide and water vapour",
            "Methane and nitrogen",
            "Sulfur dioxide and nitrogen oxides",
        ],
        "correct_index": 3,
        "why": "SO2 and the nitrogen oxides dissolve in rainwater to form "
               "sulfuric and nitric acids.",
    },
    {
        "id": "ks4-atmospheric-pollutants-e04",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one health effect of breathing in particulates.",
        "options": [
            "They lodge deep in the lungs and worsen asthma and other lung "
            "disease",
            "They bind to haemoglobin and stop the blood from carrying any "
            "oxygen",
            "They dissolve in the blood to form sulfuric acid inside the "
            "body",
            "They react with the water in the eyes to produce chlorine gas",
        ],
        "correct_index": 0,
        "why": "Particulates are small enough to reach deep into the lungs, "
               "where they irritate and damage the airways.",
    },
    {
        "id": "ks4-atmospheric-pollutants-s01",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how nitrogen oxides form inside a car engine, even "
                "though the fuel contains no nitrogen.",
        "options": [
            "Nitrogen in the exhaust pipe is oxidised by the catalytic "
            "converter as it passes",
            "Nitrogen and oxygen from the air react together at the high "
            "temperature in the engine",
            "Nitrogen impurities present in the petrol burn to give nitrogen "
            "oxides in the cylinder",
            "Nitrogen is added to petrol as an additive and burns along with "
            "the fuel itself",
        ],
        "correct_index": 1,
        "why": "The air drawn in is 78% nitrogen, and at engine temperatures "
               "N2 + O2 → 2NO.",
    },
    {
        "id": "ks4-atmospheric-pollutants-s02",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Write the equation for the reaction that damages a limestone "
                "statue when sulfuric acid falls on it as acid rain.",
        "options": [
            "CaCO3 + H2SO4 → CaSO4 + H2O + CO2",
            "CaCO3 + H2SO4 → CaO + H2SO3 + CO2",
            "CaO + H2SO4 → CaCO3 + H2O",
            "CaCO3 + 2HNO3 → CaCO3 + H2O + NO2",
        ],
        "correct_index": 0,
        "why": "Sulfuric acid reacts with the calcium carbonate of the "
               "limestone, dissolving the stone and releasing CO2.",
    },
    {
        "id": "ks4-atmospheric-pollutants-s03",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe why global dimming happens.",
        "options": [
            "Sulfur dioxide reacts with sunlight and converts it into "
            "infrared radiation",
            "Carbon dioxide high in the atmosphere absorbs the incoming "
            "visible light",
            "Particulates in the air block sunlight, so less reaches the "
            "surface",
            "Acid rain clouds the surface of the oceans, reducing the light "
            "they reflect",
        ],
        "correct_index": 2,
        "why": "Soot particles scatter and absorb incoming sunlight, cutting "
               "the amount that reaches the ground.",
    },
    {
        "id": "ks4-atmospheric-pollutants-s04",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why homes with a gas boiler are fitted with a carbon "
                "monoxide detector but not a carbon dioxide detector.",
        "options": [
            "Carbon dioxide cannot be detected by any instrument yet "
            "invented",
            "Carbon monoxide has a strong smell, and the alarm confirms it",
            "Carbon dioxide is only ever produced outdoors, so it is no risk "
            "inside",
            "Carbon monoxide is toxic and has no colour or smell, so nothing "
            "warns you",
        ],
        "correct_index": 3,
        "why": "CO is colourless and odourless but poisonous, so without a "
               "detector there is no warning that it is there.",
    },
    {
        "id": "ks4-atmospheric-pollutants-h01",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station sprays calcium hydroxide into its flue gases. "
                "Explain what this achieves.",
        "options": [
            "The alkaline spray neutralises acidic sulfur dioxide before it "
            "leaves the chimney",
            "The spray cools the gases so that the nitrogen oxides condense "
            "out as a liquid",
            "The spray reacts with carbon dioxide, removing the station's "
            "greenhouse emissions",
            "The spray adds oxygen so that any carbon monoxide burns to "
            "carbon dioxide",
        ],
        "correct_index": 0,
        "why": "SO2 is an acidic gas, so an alkali such as calcium hydroxide "
               "removes it and cuts acid rain.",
    },
    {
        "id": "ks4-atmospheric-pollutants-h02",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a catalytic converter, 2CO + 2NO → 2CO2 + N2. Explain why "
                "this reaction is said to make the exhaust less harmful even "
                "though a greenhouse gas is produced.",
        "options": [
            "Because carbon dioxide stops being a greenhouse gas once it has "
            "left the exhaust pipe",
            "Because nitrogen is highly toxic, and the reaction removes it "
            "from the exhaust gases",
            "Because a toxic gas and an acid-rain gas are replaced by two "
            "much less harmful ones",
            "Because the reaction destroys the carbon completely, leaving "
            "only nitrogen behind",
        ],
        "correct_index": 2,
        "why": "CO poisons and NO causes acid rain and smog; CO2 and N2 are "
               "far less harmful, though CO2 still adds to warming.",
    },
    {
        "id": "ks4-atmospheric-pollutants-h03",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fuel A contains 0.2% sulfur. Fuel B has been treated to "
                "reduce its sulfur to 0.001%. Predict and explain the "
                "difference in the pollution the two fuels cause.",
        "options": [
            "Fuel B produces more carbon monoxide, because removing sulfur "
            "leaves it short of oxygen",
            "The two produce identical pollutants, because the sulfur in a "
            "fuel does not burn at all",
            "Fuel A produces more nitrogen oxides, because sulfur raises the "
            "temperature of burning",
            "Fuel A produces far more sulfur dioxide, so contributes more to "
            "acid rain",
        ],
        "correct_index": 3,
        "why": "Sulfur in a fuel burns to SO2, so a low-sulfur fuel releases "
               "far less of the gas that acidifies rain.",
    },
    {
        "id": "ks4-atmospheric-pollutants-h04",
        "subtopic_slug": "atmospheric-pollutants",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lake downwind of a coal-fired power station has a pH of "
                "4.2, while a lake upwind has a pH of 6.4. Suggest and "
                "explain the cause of this difference.",
        "options": [
            "The downwind lake receives more carbon dioxide, which is far "
            "more acidic than sulfur dioxide",
            "Sulfur dioxide from the station blows downwind and dissolves in "
            "the rain, acidifying that lake",
            "The upwind lake has been treated with sulfuric acid in order to "
            "neutralise its alkalinity",
            "Nitrogen from the air dissolves directly into the downwind lake "
            "and forms nitric acid there",
        ],
        "correct_index": 1,
        "why": "SO2 released from the chimney is carried downwind, forms "
               "sulfuric acid in rain and lowers that lake's pH.",
    },
]
