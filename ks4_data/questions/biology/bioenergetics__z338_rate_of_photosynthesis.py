"""Biology · Bioenergetics — the MRB-338 expansion of `rate-of-photosynthesis`.

One leaf only: AQA 8461 §4.4.1.2. The original twelve rows in
`bioenergetics.py` take the definition of a limiting factor, the three
named factors, RP5's bubble-counting method, sodium hydrogencarbonate,
the paraffin-heater double effect, slow cold enzymes, the water bath
control, CO2 as the scarce factor on a warm bright day, an earlier
plateau at low CO2, permanent denaturation at 45 °C, light saturating at
low vs high CO2, and two temperatures both pushed past the optimum.

This file takes what they leave: RP5's own method as a piece of science
— its variables, its repeats, its reliability, a genuinely better
measurement than counting bubbles — reading a rate from numbers given in
the stem rather than a picture, rate-from-count-and-time arithmetic in
both directions, isolating one factor at a time as the reason scientists
never change two together, and the economic reasoning a grower actually
weighs when light, CO2 and heat all cost money. Nothing here names the
inverse-square law, which belongs to the Higher extension this base
subtopic does not reach.

Numbers here are rate arithmetic — bubbles or cm3 of oxygen over a given
time — never mole-style equation ratios, which are `photosynthesis`'s own
territory.
"""

TOPIC = "bioenergetics"
SUBJECT = "biology"
QUESTIONS = [
    # ══ easier · e05–e12 ═══════════════════════════════════════
    {
        "id": "ks4-rate-of-photosynthesis-e05",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the rate of photosynthesis as light intensity "
               "increases, provided nothing else is limiting.",
        "options": [
            "It increases",
            "It decreases",
            "It stays exactly the same",
            "It stops completely",
        ],
        "correct_index": 0,
        "why": "More light energy drives a faster reaction while light remains the factor in "
               "shortest supply.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e06",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the apparatus item that lets a scientist change the light intensity "
               "reaching an aquatic plant in RP5.",
        "options": [
            "A thermometer",
            "A lamp",
            "A gas syringe",
            "A water bath",
        ],
        "correct_index": 1,
        "why": "Moving a lamp closer to or further from the plant changes the light "
               "intensity it receives.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e07",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a water bath is used to control in RP5.",
        "options": [
            "Light intensity",
            "Carbon dioxide concentration",
            "Temperature",
            "pH",
        ],
        "correct_index": 2,
        "why": "A water bath keeps the temperature steady, so that only light intensity "
               "changes between readings.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e08",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a scientist repeats the bubble count at each light intensity in "
               "RP5.",
        "options": [
            "To use up the extra sodium hydrogencarbonate",
            "To let the plant recover between readings",
            "To warm the water before the next distance",
            "To get a reliable average result",
        ],
        "correct_index": 3,
        "why": "Repeating a measurement and averaging it reduces the effect of any one "
               "anomalous count.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e09",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the independent variable in RP5, when investigating light "
               "intensity.",
        "options": [
            "Light intensity",
            "Bubble rate",
            "Temperature",
            "Carbon dioxide concentration",
        ],
        "correct_index": 0,
        "why": "Light intensity is the variable the scientist deliberately changes between "
               "readings.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e10",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the dependent variable measured in RP5.",
        "options": [
            "The distance from the lamp",
            "The number of bubbles released per minute",
            "The temperature of the water",
            "The concentration of sodium hydrogencarbonate",
        ],
        "correct_index": 1,
        "why": "Bubble rate is the outcome measured as light intensity is changed.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e11",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the rate of photosynthesis once temperature rises "
               "above a plant's optimum.",
        "options": [
            "It keeps rising steadily",
            "It stays exactly the same",
            "It falls sharply",
            "It rises, then falls back to the original rate",
        ],
        "correct_index": 2,
        "why": "Above the optimum temperature, enzymes begin to denature, so the rate falls "
               "sharply.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e12",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State an alternative to counting bubbles for measuring the rate of "
               "photosynthesis in RP5.",
        "options": [
            "Weighing the aquatic plant every minute",
            "Testing the water's pH every minute",
            "Measuring the plant's height at the end",
            "Collecting the gas and measuring its volume",
        ],
        "correct_index": 3,
        "why": "Collecting the oxygen released over a set time and measuring its volume "
               "avoids the unreliable job of counting bubbles.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════
    {
        "id": "ks4-rate-of-photosynthesis-s05",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why collecting and measuring the volume of gas released is more "
               "reliable than counting bubbles.",
        "options": [
            "Bubbles vary in size, so counting them does not measure the volume of gas "
            "accurately",
            "Bubbles cannot be seen clearly enough to count for the reaction taking "
            "place",
            "Bubbles form once the plant has already stopped photosynthesising",
            "Bubbles are carbon dioxide, not oxygen, so counting them proves nothing",
        ],
        "correct_index": 0,
        "why": "A count treats every bubble as equal, but bubbles differ in size, so the "
               "count is a poor stand-in for the true volume of gas produced.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s06",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student repeats a bubble count three times at one light intensity and gets "
               "18, 19 and 31 bubbles per minute. Suggest what the student should do with "
               "the anomalous result.",
        "options": [
            "Include the anomaly, since every reading must be kept",
            "Repeat that reading, and leave the anomaly out of the average",
            "Average all three results exactly as they stand, since every value collected "
            "must count",
            "Stop the experiment, since one strange result ends it",
        ],
        "correct_index": 1,
        "why": "An anomalous result should be checked with a repeat and excluded from the "
               "average, rather than treated as reliable data.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s07",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sodium hydrogencarbonate solution, rather than plain water, is "
               "used in RP5.",
        "options": [
            "It keeps the water at a fixed pH, so the plant's enzymes are not denatured",
            "It provides the extra oxygen the plant needs to photosynthesise",
            "It keeps carbon dioxide concentration constant, so only light intensity "
            "varies",
            "It stops the water evaporating as the lamp warms the beaker",
        ],
        "correct_index": 2,
        "why": "Sodium hydrogencarbonate releases CO2 into the water, holding that variable "
               "steady while light intensity is changed.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s08",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a student places the beaker of pondweed in a large water bath "
               "during RP5, rather than on the bench.",
        "options": [
            "It keeps the sodium hydrogencarbonate concentration from changing",
            "It stops the bubbles escaping before they can be counted",
            "It stops the pondweed floating up to the water's surface",
            "It keeps the temperature constant as light intensity is varied",
        ],
        "correct_index": 3,
        "why": "Without a water bath, the lamp would warm the water and change the "
               "temperature as well as the light intensity.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s09",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist records rates of 4, 8 and 8 bubbles per minute at light "
               "intensities of 10, 20 and 30 units. Determine the intensity at which another "
               "factor first becomes limiting.",
        "options": [
            "20 units",
            "30 units",
            "10 units",
            "None of the three, since the rate keeps rising throughout",
        ],
        "correct_index": 0,
        "why": "The rate stops rising between 20 and 30 units, so a factor other than light "
               "has taken over from that point.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s10",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a grower providing extra carbon dioxide to a greenhouse crop "
               "would see little benefit if the crop is already grown in dim light.",
        "options": [
            "Extra carbon dioxide slows photosynthesis down in any light",
            "Light, not carbon dioxide, is the factor limiting the rate in dim light",
            "Extra carbon dioxide reacts with dim light to stop the reaction",
            "Extra carbon dioxide works once a crop's leaves have died back",
        ],
        "correct_index": 1,
        "why": "Raising a factor that is not currently scarce cannot raise the rate further, "
               "because a different factor is holding it back.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s11",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant's rate of photosynthesis, measured through the day, "
               "tends to be highest around midday.",
        "options": [
            "Temperature is at its coolest around midday, suiting the plant's enzymes",
            "Carbon dioxide concentration is highest around midday",
            "Light intensity is greatest around midday, and light is often limiting",
            "The plant's stomata close completely around midday",
        ],
        "correct_index": 2,
        "why": "Light intensity peaks around midday, and for much of the day light is the "
               "factor most likely to be in short supply.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s12",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "During RP5 a plant releases 42 bubbles over 3 minutes at one light "
               "intensity. Work out its rate of photosynthesis.",
        "options": [
            "126 bubbles per minute",
            "45 bubbles per minute",
            "39 bubbles per minute",
            "14 bubbles per minute",
        ],
        "correct_index": 3,
        "why": "42 bubbles divided by 3 minutes gives 14 bubbles per minute.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s13",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rate is 150 bubbles in 5 minutes at one light intensity, and 90 bubbles in "
               "3 minutes at another. Compare the two rates.",
        "options": [
            "Both rates are 30 bubbles per minute, so they are equal",
            "The first is faster, at 30 bubbles per minute against 27",
            "The second is faster, at 90 bubbles per minute against 30",
            "The rates cannot be compared without knowing the temperature",
        ],
        "correct_index": 0,
        "why": "150 / 5 = 30 and 90 / 3 = 30, so the two rates are in fact equal once time "
               "is taken into account.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s14",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a scientist keeps the same species and a similar-sized piece of "
               "pondweed for every reading in RP5.",
        "options": [
            "So that the sodium hydrogencarbonate lasts equally long each time",
            "So that only light intensity differs between one reading and the next",
            "So that the water bath does not need refilling between readings",
            "So that the lamp can be moved to the same distances each time",
        ],
        "correct_index": 1,
        "why": "Using different plants would introduce a second changing variable, making it "
               "unclear whether light intensity alone explains any difference in rate.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s15",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant kept warm and supplied with plenty of carbon dioxide shows no "
               "further rise in rate once the lamp is moved past a certain distance. Explain "
               "what this shows.",
        "options": [
            "Beyond that distance, the plant has run out of chlorophyll",
            "Beyond that distance, the water bath has cooled the plant down, changing the "
            "plant's temperature as well",
            "Beyond that distance, light intensity has become the limiting factor",
            "Beyond that distance, respiration has stopped completely",
        ],
        "correct_index": 2,
        "why": "Dimming the light past that point limits the rate directly, since neither "
               "temperature nor carbon dioxide has changed.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s16",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a grower who heats a greenhouse in winter, but leaves the CO2 "
               "and light unchanged, may see only a small rise in yield.",
        "options": [
            "Heating a greenhouse always destroys any benefit gained from the crop's "
            "yield",
            "Heating slows enzyme activity, cancelling out the benefit",
            "Heating reduces the carbon dioxide concentration in the greenhouse",
            "Once temperature is no longer limiting, another factor takes over",
        ],
        "correct_index": 3,
        "why": "Solving one limiting factor only helps until a different factor becomes the "
               "new bottleneck.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s17",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants to know whether a new fertiliser changes the RATE of "
               "photosynthesis, not just the plant's final size. Suggest a suitable "
               "measurement to take.",
        "options": [
            "The number of oxygen bubbles released per minute",
            "The height of the plant after a month",
            "The colour of the plant's leaves after a week",
            "The total mass of the plant at the end of the experiment",
        ],
        "correct_index": 0,
        "why": "Bubble rate measures how quickly photosynthesis is happening, unlike height "
               "or mass, which build up over the whole experiment.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s18",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant's rate of photosynthesis in a cold greenhouse rises when "
               "the heating is switched on, even though the light and CO2 supply stay the "
               "same.",
        "options": [
            "Warmer conditions increase the amount of light entering the greenhouse",
            "Warmer conditions let the enzymes work faster, up towards their optimum",
            "Warmer conditions raise the carbon dioxide concentration automatically",
            "Warmer conditions stop the plant respiring, leaving more energy for growth",
        ],
        "correct_index": 1,
        "why": "Temperature affects the enzymes driving photosynthesis, so warming a cold "
               "plant towards its optimum raises the rate.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s19",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A different trial of RP5 counts 210 bubbles released over 7 minutes. "
               "Determine the rate of photosynthesis this shows.",
        "options": [
            "1,470 bubbles per minute",
            "203 bubbles per minute",
            "30 bubbles per minute",
            "217 bubbles per minute",
        ],
        "correct_index": 2,
        "why": "210 divided by 7 gives a rate of 30 bubbles per minute.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s20",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why moving a lamp twice as close to an aquatic plant does not always "
               "double its rate of photosynthesis.",
        "options": [
            "Moving a lamp closer halves the plant's rate instead",
            "A lamp's light intensity does not change with distance",
            "Doubling the light exactly quadruples the rate under any conditions",
            "Once another factor becomes limiting, extra light makes no further "
            "difference",
        ],
        "correct_index": 3,
        "why": "The rate keeps rising with light only while light itself is the scarcest "
               "factor; once something else limits it, extra light has no further effect.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s21",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that raising carbon dioxide concentration will speed up "
               "photosynthesis, whatever the conditions. Correct this statement.",
        "options": [
            "Only while CO2 is the limiting factor; once it is not, extra CO2 has no "
            "effect",
            "This is correct, since CO2 is the factor that limits the rate the most",
            "This is wrong, since carbon dioxide has no effect on the rate at any "
            "concentration",
            "This is correct, but just once the light has been switched off entirely",
        ],
        "correct_index": 0,
        "why": "Raising CO2 helps only when it is genuinely the scarcest factor; once light "
               "or temperature is limiting instead, extra CO2 changes nothing.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s22",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pondweed releases 6 bubbles in a 15-second window. Express this as a "
               "rate in bubbles per minute.",
        "options": [
            "6 bubbles per minute",
            "24 bubbles per minute",
            "90 bubbles per minute",
            "15 bubbles per minute",
        ],
        "correct_index": 1,
        "why": "6 bubbles in 15 seconds is 6 x 4 = 24 bubbles across a full 60-second "
               "minute.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s23",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a scientist plots rate of photosynthesis against light intensity "
               "as a graph, rather than comparing just two readings.",
        "options": [
            "A graph is needed because two readings are hard to compare directly",
            "A graph removes the need to control temperature or carbon dioxide, which a "
            "single pair of readings cannot show",
            "A graph shows the whole pattern of how the rate changes, not just two points",
            "A graph is what allows the bubbles to be counted accurately",
        ],
        "correct_index": 2,
        "why": "A full set of readings, plotted together, reveals the rising part of the "
               "pattern and where it levels off, which two isolated points cannot.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s24",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener notices tomato plants grown at 15°C photosynthesise more slowly "
               "than identical plants grown at 25°C, with everything else the same. Explain "
               "why.",
        "options": [
            "The warmer plants receive more carbon dioxide from the warmer air, which "
            "speeds up every one of its reactions",
            "The warmer plants absorb more light, since warmth attracts it",
            "The cooler plants have already begun to denature their enzymes",
            "The warmer plants' enzymes work faster, closer to their optimum temperature",
        ],
        "correct_index": 3,
        "why": "A higher temperature closer to the optimum speeds up the enzyme-controlled "
               "reactions of photosynthesis.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s25",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a commercial grower might choose to enrich a greenhouse with CO2 "
               "rather than install more artificial lighting to raise yield.",
        "options": [
            "CO2 enrichment can be cheaper to run than powerful additional lighting",
            "CO2 enrichment raises the rate more than extra light could manage, "
            "regardless of the cost of running either system",
            "Extra lighting has no effect on the rate of photosynthesis",
            "CO2 enrichment is the simplest method a greenhouse can use",
        ],
        "correct_index": 0,
        "why": "A grower weighs cost as well as effect, and CO2 enrichment is often the "
               "cheaper route to raising yield.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s26",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rate of photosynthesis rises steadily as light intensity increases from 0 "
               "to 20 units, then stays constant from 20 to 40 units. Explain the second "
               "part of the pattern.",
        "options": [
            "Above 20 units, the plant has run out of light-absorbing pigment",
            "Above 20 units, a factor other than light has become limiting",
            "Above 20 units, the plant stops respiring",
            "Above 20 units, the rate falls back to zero",
        ],
        "correct_index": 1,
        "why": "Once the rate stops rising with more light, light is no longer the scarcest "
               "factor, so something else is now holding the rate back.",
    },

    # ══ harder · h05–h26 ═══════════════════════════════════════
    {
        "id": "ks4-rate-of-photosynthesis-h05",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical aquatic plants are kept under the same bright light and CO2, "
               "but one at 12°C and one at 28°C, with the species' optimum at 30°C. Predict "
               "which photosynthesises faster, and explain.",
        "options": [
            "The 12°C plant, because cold conditions speed up enzyme activity",
            "Both equally, since temperature has no effect below the optimum",
            "The 28°C plant, because it is closer to the optimum temperature",
            "The 28°C plant, because warmth alone increases its chlorophyll",
        ],
        "correct_index": 2,
        "why": "Closer to the optimum, the enzymes controlling photosynthesis work faster, "
               "so the 28°C plant photosynthesises more quickly.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h06",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A greenhouse grower raises CO2 concentration tenfold, but the rate of "
               "photosynthesis only doubles rather than rising tenfold too. Explain why.",
        "options": [
            "CO2 concentration has no real bearing on the rate of photosynthesis",
            "The extra CO2 must have leaked out before reaching the plant",
            "Raising CO2 tenfold raises the rate by that same amount too",
            "Once CO2 is no longer the limiting factor, extra CO2 has a smaller effect",
        ],
        "correct_index": 3,
        "why": "CO2 keeps raising the rate only while it is the scarcest factor; once "
               "another factor starts to limit the rate instead, extra CO2 achieves much "
               "less.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h07",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist tests the same aquatic plant at 20 different light intensities "
               "in one afternoon, without changing the water. Evaluate whether the results "
               "are likely to be reliable.",
        "options": [
            "They may not be, since the plant could tire or the water could warm as the "
            "afternoon goes on",
            "They are reliable, because every plant behaves identically all day long",
            "They are reliable, since light intensity is the variable that matters here, "
            "regardless of how long the plant sits in the same water",
            "They cannot be reliable, because a plant can be tested just the one time",
        ],
        "correct_index": 0,
        "why": "Leaving the same water and plant in place for a whole afternoon risks a slow "
               "drift in temperature or condition that a short, controlled test avoids.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h08",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a scientist would criticise an experiment that measured the rate "
               "of photosynthesis by bubble counting for just 10 seconds at each light "
               "intensity.",
        "options": [
            "Ten seconds is too long a time to measure any reaction",
            "Such a short time gives too few bubbles for an accurate count",
            "Bubble counting works over a time of exactly one minute",
            "A short measuring time stops the plant photosynthesising",
        ],
        "correct_index": 1,
        "why": "A very short counting window magnifies the effect of rounding a single "
               "bubble, making the calculated rate far less precise.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h09",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant's rate is 15 bubbles per minute at 20°C and 27 bubbles per minute at "
               "30°C, with an optimum of 35°C. Predict the rate at 40°C, and explain.",
        "options": [
            "Around 39, continuing the same steady increase seen so far, well past where "
            "the enzymes would already be under strain",
            "Exactly 27, because the rate levels off above 30°C",
            "Much lower than 27, because the enzymes denature above the optimum",
            "Around 54, because heat doubles the rate of any reaction",
        ],
        "correct_index": 2,
        "why": "Past the optimum, the enzymes controlling photosynthesis begin to denature, "
               "so the rate falls sharply rather than continuing to rise.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h10",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the rate of photosynthesis, in cm3 of oxygen per minute, from a "
               "volume of 45 cm3 collected over 9 minutes.",
        "options": [
            "54 cm3 per minute",
            "36 cm3 per minute",
            "0.2 cm3 per minute",
            "5 cm3 per minute",
        ],
        "correct_index": 3,
        "why": "45 cm3 divided by 9 minutes gives a rate of 5 cm3 per minute.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h11",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rate is 8 bubbles per minute at light intensity 1 and 32 bubbles per "
               "minute at intensity 4, but only 34 bubbles per minute at intensity 8. "
               "Explain the change in pattern between the two increases.",
        "options": [
            "Between intensity 4 and 8, a factor other than light has become limiting",
            "Between intensity 4 and 8, the bubbles became too small to count",
            "Between intensity 4 and 8, the plant began photosynthesising in reverse",
            "Between intensity 4 and 8, the light intensity itself fell",
        ],
        "correct_index": 0,
        "why": "The rate rose in step with light up to intensity 4, but barely rose from 4 "
               "to 8, showing that something other than light is now holding it back.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h12",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower doubles both light intensity and CO2 concentration in a greenhouse "
               "at the same time, and the rate of photosynthesis roughly doubles too. "
               "Explain what this suggests about which factor was limiting beforehand.",
        "options": [
            "This proves light alone was limiting, since CO2 changes are too small to "
            "detect",
            "Either factor could have been limiting; changing both at once does not "
            "identify which",
            "This proves CO2 alone was limiting, since light changes are too small to "
            "detect",
            "This proves temperature was the true limiting factor throughout, even though "
            "neither light nor CO2 was changed",
        ],
        "correct_index": 1,
        "why": "Changing two factors together cannot separate their individual effects; only "
               "varying one at a time, with the other held constant, can show which was "
               "limiting.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h13",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a plant's rate of photosynthesis can be raised "
               "without limit simply by supplying enough carbon dioxide.",
        "options": [
            "It is correct; CO2 is the factor that most often limits photosynthesis",
            "It is correct, provided the plant is also kept in complete darkness",
            "It is wrong; once CO2 is no longer scarce, light or temperature will limit "
            "the rate instead",
            "It is wrong; carbon dioxide has no effect on the rate at any concentration, "
            "however much of it the plant is given",
        ],
        "correct_index": 2,
        "why": "A rate can never rise past the ceiling set by whichever factor is scarcest, "
               "and CO2 will eventually stop being that factor.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h14",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A researcher wants to identify which of light, CO2 and temperature is "
               "limiting a crop's photosynthesis in a particular greenhouse. Suggest a "
               "suitable method.",
        "options": [
            "Raise all three factors together, since their combined effect is what "
            "matters",
            "Lower the temperature until photosynthesis stops, then work backwards from "
            "there",
            "Measure the crop's height instead, assuming a taller crop is the one "
            "photosynthesising faster",
            "Raise each factor in turn, keeping the other two constant, and see which "
            "raises the rate",
        ],
        "correct_index": 3,
        "why": "Varying one factor while holding the others steady is the only way to "
               "isolate which of the three is currently holding the rate back.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h15",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rate rises from 10 to 20 bubbles per minute as light intensity doubles "
               "from 200 to 400 lux, but rises only to 22 as it doubles again to 800 lux. "
               "Determine the range in which light is most clearly the limiting factor.",
        "options": [
            "200 to 400 lux, where the rate roughly doubled with the light",
            "400 to 800 lux, where the rate barely changed",
            "Both ranges equally, since the rate rose throughout",
            "Neither range, since light does not limit photosynthesis here",
        ],
        "correct_index": 0,
        "why": "The rate tracked the light closely between 200 and 400 lux, which is where "
               "light was still the scarcest factor.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h16",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Greenhouse A has bright light and low CO2; greenhouse B has dim light and "
               "high CO2. Compare which is more likely to have the higher rate of "
               "photosynthesis, and explain your reasoning.",
        "options": [
            "Greenhouse A, since light is the more important factor",
            "It cannot be determined without knowing which factor is more limiting in "
            "each greenhouse",
            "Greenhouse B, since CO2 is the more important factor",
            "Both are identical, since bright light and high CO2 cancel out, so neither "
            "greenhouse can be assumed better than the other",
        ],
        "correct_index": 1,
        "why": "Without knowing how scarce each factor actually is in each greenhouse, it is "
               "impossible to say which one is holding the rate back the most.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h17",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rate is 320 bubbles in 8 minutes at one light intensity, and 15 bubbles in "
               "30 seconds at a second, brighter intensity. Compare the two rates in bubbles "
               "per minute.",
        "options": [
            "40 at the first intensity and 15 at the second — the first is faster",
            "320 at the first intensity and 30 at the second — the first is faster",
            "40 at the first intensity and 30 at the second — the first is actually "
            "faster",
            "40 at both intensities — the rates are equal",
        ],
        "correct_index": 2,
        "why": "320 / 8 = 40 bubbles per minute, and 15 bubbles in 30 seconds is 30 per "
               "minute, so the brighter condition is actually the slower one.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h18",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why scientists studying limiting factors usually keep two of the "
               "three factors constant while varying the third, rather than changing all "
               "three together.",
        "options": [
            "Changing all three together gives a more impressive-looking final result",
            "Keeping factors constant is required because plants cannot survive any "
            "change",
            "It removes the need to repeat any reading more than once",
            "Changing only one factor at a time shows clearly what effect that factor "
            "alone has",
        ],
        "correct_index": 3,
        "why": "Isolating one variable at a time is the only way to be sure which factor "
               "caused a change in rate.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h19",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist claims that a graph showing rate of photosynthesis levelling off "
               "at high light intensity proves the plant has run out of chlorophyll. "
               "Evaluate this claim.",
        "options": [
            "It is wrong; chlorophyll is a pigment, not consumed, so another factor must "
            "be limiting",
            "It is correct, since chlorophyll is gradually used up as light intensity "
            "keeps rising",
            "It is correct, because a plant holds a fixed, tiny amount of chlorophyll",
            "It is wrong, because light intensity cannot cause a graph to level off",
        ],
        "correct_index": 0,
        "why": "Chlorophyll absorbs light repeatedly rather than being consumed by it, so a "
               "plateau shows a different factor has become limiting.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h20",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures the rate of photosynthesis of the same pondweed on two "
               "different days, getting very different results despite following an "
               "identical method both times. Suggest a factor that was probably not properly "
               "controlled.",
        "options": [
            "The species of pondweed, since it must have changed overnight",
            "Room temperature, which may not have been checked or controlled on either "
            "day",
            "The colour of the pondweed, which directly determines the rate",
            "The time of year, which has no possible effect on a lab experiment",
        ],
        "correct_index": 1,
        "why": "An unmonitored room temperature could easily differ between the two days, "
               "changing the rate even though the written method stayed the same.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h21",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Over a timed window of 2 minutes 30 seconds, a plant gives off 51 "
               "bubbles. Convert this into a rate per minute.",
        "options": [
            "25.5 bubbles per minute",
            "127.5 bubbles per minute",
            "20.4 bubbles per minute",
            "51 bubbles per minute",
        ],
        "correct_index": 2,
        "why": "2 minutes 30 seconds is 2.5 minutes, and 51 / 2.5 = 20.4 bubbles per minute.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h22",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crop grown in a well-lit, CO2-enriched greenhouse still photosynthesises "
               "slowly on a cold winter morning. Suggest the most likely limiting factor, "
               "and explain your reasoning.",
        "options": [
            "Light, since a winter morning has zero light of any kind",
            "CO2, since enrichment struggles to raise its concentration indoors",
            "None of the three; the crop must be diseased instead",
            "Temperature, since it is the one factor that has not been improved",
        ],
        "correct_index": 3,
        "why": "Light and CO2 have already been improved, so an unaddressed cold temperature "
               "is the most likely cause of the low rate.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h23",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a graph of rate of photosynthesis against carbon dioxide "
               "concentration would be expected to level off eventually, even in bright "
               "light and warm conditions.",
        "options": [
            "Eventually light or temperature takes over as the limiting factor instead",
            "Carbon dioxide stops affecting the rate after exactly one minute",
            "The plant's chlorophyll is used up once enough CO2 has been supplied",
            "A graph cannot level off if conditions are warm and bright",
        ],
        "correct_index": 0,
        "why": "No single factor can raise the rate forever; once CO2 stops being the "
               "scarcest factor, another one takes over the limit.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h24",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rate of photosynthesis is given as 3.6 cm3 of oxygen per minute. Calculate "
               "the volume of oxygen collected over 25 minutes at this steady rate.",
        "options": [
            "28.6 cm3",
            "90 cm3",
            "21.4 cm3",
            "9 cm3",
        ],
        "correct_index": 1,
        "why": "3.6 cm3 per minute multiplied by 25 minutes gives 90 cm3 of oxygen.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h25",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A commercial grower has a limited budget and must choose between extra "
               "grow-lights or a CO2 enrichment system. Suggest what information they would "
               "need before deciding.",
        "options": [
            "Nothing further, since CO2 enrichment gives the greater benefit in every "
            "case",
            "Nothing further, since extra lighting gives the greater benefit in every "
            "case",
            "Which factor, light or CO2, is currently more limiting in their greenhouse",
            "The price of electricity alone, since that decides plant growth",
        ],
        "correct_index": 2,
        "why": "Money is best spent raising whichever factor is currently the scarcest one, "
               "so the grower needs to know which that is before choosing.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h26",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why doubling both light intensity and temperature (while staying "
               "below the optimum) usually raises the rate of photosynthesis by more than "
               "doubling either one alone.",
        "options": [
            "Doubling two factors together exactly quadruples the rate every time",
            "Temperature affects the rate here; light makes no difference to it",
            "Doubling two factors together cancels out, leaving the rate unchanged",
            "Both factors were limiting to some degree, so improving both removes more of "
            "the restriction",
        ],
        "correct_index": 3,
        "why": "When more than one factor is holding the rate back, relieving more than one "
               "of them at once removes more of the overall restriction.",
    },
]
