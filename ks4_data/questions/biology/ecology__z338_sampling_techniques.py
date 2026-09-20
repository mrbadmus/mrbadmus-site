"""Biology · Ecology — the MRB-338 expansion of `sampling-techniques`.

One leaf only: AQA 8461 §4.7.1, and the required practical RP6 behind it. The
original twelve rows in `ecology__b.py` take the quadrat by name, the area of a
0.5 m frame, why a quadrat cannot hold a grasshopper, `m` in the Lincoln index,
one scale-up, one mark-recapture, why fifteen readings beat two, random
coordinates, two ponds compared, `m` found by rearrangement, a marked snail
eaten, and a belt transect judged against a total count.

This file takes what they leave. The recall band finishes the vocabulary the
baseline never names — the line transect against the belt transect, `n₁`,
percentage cover, the mean as the step before scaling up, and what a mark has
to be. The demand then lives where this spec point really lives: in arithmetic
that carries a unit conversion (a hectare is ten thousand square metres, a
0.25 m² frame is a quarter of one), and in the five assumptions of the Lincoln
index, each one approached from the side on which a real investigation breaks
it — trap-happy animals, a fading mark, an open population, a sample taken all
down one footpath.

The weight follows the CONTENT. `easier` stays at eight because the recall here
is a short closed list of names, and a ninth way of asking it is the eighth in
new words. `standard` and `harder` carry twenty-two each, because every
sampling method in the spec generates a fresh calculation and a fresh way of
being done badly.

Numbers are the ones fieldwork supplies: quadrat sides in metres, areas in
square metres and hectares, counts as whole individuals, cover as a percentage
of a hundred-square grid.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The vocabulary the baseline leaves unnamed: line and belt transects,
    # n₁, percentage cover, the reason for randomness, one scale factor, the
    # mean, and the requirement on a mark.
    {
        "id": "ks4-sampling-techniques-e05",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a line transect records about the species along "
                "the line.",
        "options": [
            "The total population of the habitat either side of the line",
            "The mass of every organism along the line, weighed at each "
                "metre mark",
            "Which species touch the line, and so are present or absent",
            "The number of young produced by each species that year",
        ],
        "correct_index": 2,
        "why": "A line transect records only which species touch the line at "
               "each point, giving presence or absence rather than abundance.",
    },
    {
        "id": "ks4-sampling-techniques-e06",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a belt transect is.",
        "options": [
            "A strip across a habitat with quadrats placed at intervals "
                "along it",
            "A ring of quadrats laid around the edge of a habitat",
            "A rope marking out the boundary a class is allowed to work "
                "inside",
            "A single large quadrat covering one side of a field",
        ],
        "correct_index": 0,
        "why": "A belt transect is a strip along the transect line with "
               "quadrats at set intervals, so abundance as well as presence is "
               "recorded.",
    },
    {
        "id": "ks4-sampling-techniques-e07",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ecologists catch 40 beetles, mark them and release them, then "
                "take a second sample a week later. State which quantity of "
                "the Lincoln index the number 40 is.",
        "options": [
            "N, the estimated size of the whole beetle population",
            "n₂, the total number of beetles caught in the second sample",
            "m, the number of marked beetles found in the second sample",
            "n₁, the number caught and marked in the first sample",
        ],
        "correct_index": 3,
        "why": "n₁ is the size of the first sample, every member of which is "
               "marked before being released.",
    },
    {
        "id": "ks4-sampling-techniques-e08",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the percentage cover of a plant in a "
                "quadrat.",
        "options": [
            "How much of the whole habitat has been sampled so far",
            "The proportion of the quadrat's area that the plant covers",
            "The percentage of the quadrat's plants belonging to one "
                "species",
            "The percentage of the plants inside the frame that are "
                "flowering",
        ],
        "correct_index": 1,
        "why": "Percentage cover is how much of the quadrat's area the species "
               "covers, which suits plants that cannot be counted as separate "
               "individuals.",
    },
    {
        "id": "ks4-sampling-techniques-e09",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why the positions of quadrats in a habitat must be "
                "chosen at random.",
        "options": [
            "It avoids bias, so the sample represents the whole habitat",
            "It guarantees that every individual present is counted once",
            "Random placement makes the counting itself much quicker and "
                "easier to do",
            "Random placement means fewer quadrats are needed altogether",
        ],
        "correct_index": 0,
        "why": "Choosing positions at random removes the investigator's bias, "
               "so the sample reflects the whole habitat rather than the "
               "patches somebody chose.",
    },
    {
        "id": "ks4-sampling-techniques-e10",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lawn has an area of 200 m². Calculate how many 1 m × 1 m "
                "quadrat areas fit into it.",
        "options": [
            "400 quadrat areas",
            "800 quadrat areas",
            "50 quadrat areas",
            "200 quadrat areas",
        ],
        "correct_index": 3,
        "why": "A 1 m × 1 m quadrat covers 1 m², so 200 m² ÷ 1 m² = 200 "
               "quadrat areas.",
    },
    {
        "id": "ks4-sampling-techniques-e11",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the value an ecologist calculates from many quadrat "
                "counts before scaling up to the whole habitat.",
        "options": [
            "The range of the counts, found by subtracting the lowest "
                "count from the highest",
            "The mean count per quadrat, found by dividing total by number",
            "The largest single count, because that quadrat is most "
                "typical",
            "The total of all the counts, used as the population directly",
        ],
        "correct_index": 1,
        "why": "The mean count per quadrat is what gets scaled up, because one "
               "quadrat on its own may be unusually crowded or empty.",
    },
    {
        "id": "ks4-sampling-techniques-e12",
        "subtopic_slug": "sampling-techniques",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one requirement of the mark used in a mark–recapture "
                "investigation.",
        "options": [
            "The mark is renewed on every animal on each day of the study",
            "It must be a different colour on every individual that is "
                "marked",
            "It must not harm the animal or make it easier for predators "
                "to see",
            "It must be visible from a distance so animals need not be "
                "caught again",
        ],
        "correct_index": 2,
        "why": "If the mark harms the animal or makes it conspicuous, marked "
               "individuals survive less well and the estimate is wrong.",
    },
    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Applying each method: means, scale-ups, densities, percentage cover,
    # the Lincoln index on fresh numbers, and the causes behind the rules.
    {
        "id": "ks4-sampling-techniques-s05",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Five quadrats hold 4, 9, 5, 7 and 5 plantains. Calculate the "
                "mean count per quadrat.",
        "options": [
            "30.0 plantains",
            "5.0 plantains",
            "6.0 plantains",
            "7.0 plantains",
        ],
        "correct_index": 2,
        "why": "The counts total 30, and 30 ÷ 5 quadrats gives a mean of 6.0 "
               "plantains per quadrat.",
    },
    {
        "id": "ks4-sampling-techniques-s06",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The mean count in a 1 m² quadrat is 12 buttercups. The field "
                "has an area of 450 m². Estimate the buttercup population.",
        "options": [
            "5400 buttercups",
            "37.5 buttercups",
            "450 buttercups",
            "462 buttercups",
        ],
        "correct_index": 0,
        "why": "12 buttercups per square metre × 450 square metres = 5400 "
               "buttercups.",
    },
    {
        "id": "ks4-sampling-techniques-s07",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a quadrat should be put down before the "
                "investigator looks at what is growing there.",
        "options": [
            "Choosing after looking takes time that the survey cannot "
                "spare",
            "Looking first would trample the plants, so the count is too "
                "low",
            "Looking first would make the plants close up and be missed",
            "Looking first lets the frame be laid where the species is, "
                "biasing the sample",
        ],
        "correct_index": 3,
        "why": "If the position is chosen after seeing the plants, the "
               "investigator tends to place the frame on good patches and the "
               "estimate comes out too high.",
    },
    {
        "id": "ks4-sampling-techniques-s08",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1 m² quadrat is divided into 100 small squares. Moss fills "
                "37 of them. State the percentage cover of the moss.",
        "options": [
            "3.7%",
            "37%",
            "63%",
            "137%",
        ],
        "correct_index": 1,
        "why": "37 squares out of 100 is 37% of the quadrat's area covered by "
               "moss.",
    },
    {
        "id": "ks4-sampling-techniques-s09",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "120 woodlice are caught, marked and released. A second sample "
                "of 90 woodlice contains 18 marked individuals. Estimate the "
                "population.",
        "options": [
            "600 woodlice",
            "1080 woodlice",
            "60 woodlice",
            "210 woodlice",
        ],
        "correct_index": 0,
        "why": "N = (120 × 90) ÷ 18 = 10 800 ÷ 18 = 600 woodlice.",
    },
    {
        "id": "ks4-sampling-techniques-s10",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why time is left between releasing the marked animals "
                "and taking the second sample.",
        "options": [
            "The marks need time to dry before the animals can be caught "
                "again",
            "The population needs time to grow back to its original size",
            "The marked animals need time to breed, so that their young "
                "carry the mark too",
            "The marked animals need time to mix evenly with the unmarked "
                "ones",
        ],
        "correct_index": 3,
        "why": "The formula assumes the marked individuals are spread evenly "
               "through the population, and that only happens once they have "
               "had time to mix.",
    },
    {
        "id": "ks4-sampling-techniques-s11",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two meadows are compared for daisy abundance. Explain why the "
                "same size of quadrat must be used in both.",
        "options": [
            "Different sizes of frame would need different numbers of "
                "investigators",
            "Counts from different frame areas cannot be compared directly",
            "Only one size of quadrat is allowed in a scientific survey",
            "A larger frame in one meadow would let more daisies escape it",
        ],
        "correct_index": 1,
        "why": "A count is a number per frame area, so two different frame "
               "areas give numbers that mean different things and cannot be "
               "compared.",
    },
    {
        "id": "ks4-sampling-techniques-s12",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants to show how plant species change from the sea "
                "to the top of a sand dune. Explain why a transect suits this "
                "better than randomly placed quadrats.",
        "options": [
            "A transect counts every plant, while random quadrats only "
                "sample",
            "A transect needs fewer readings than random quadrats would "
                "need",
            "A transect follows the gradient, so change with distance is "
                "seen",
            "Random quadrats cannot be used on sand, only on firm soil",
        ],
        "correct_index": 2,
        "why": "A transect is laid along the direction in which conditions "
               "change, so it shows how the species present alter with "
               "distance up the dune.",
    },
    {
        "id": "ks4-sampling-techniques-s13",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student places quadrats by throwing the frame over one "
                "shoulder. Explain why this is not truly random.",
        "options": [
            "The throw always lands the frame in exactly the same position",
            "The throw often means the frame lands upside down and cannot "
                "be read",
            "The throw damages the plants, so the count is always too low",
            "The throw favours open ground the student can face and reach",
        ],
        "correct_index": 3,
        "why": "The student is still choosing where to stand and which way to "
               "face, so some parts of the habitat can never be reached and "
               "the sample is biased.",
    },
    {
        "id": "ks4-sampling-techniques-s14",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what a belt transect running up a rocky shore shows "
                "that a single quadrat at the top could not.",
        "options": [
            "The exact total number of every species on the shore",
            "How the abundance of each species changes with height up "
                "shore",
            "The mass of each seaweed on the lower shore",
            "Which species reproduce during the summer months",
        ],
        "correct_index": 1,
        "why": "Quadrats at intervals along the line record abundance at each "
               "height, so the pattern of change up the shore can be seen.",
    },
    {
        "id": "ks4-sampling-techniques-s15",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the number produced by scaling up quadrat counts "
                "is called an estimate.",
        "options": [
            "The number is rounded, and a rounded number is an estimate",
            "The area is measured with a tape, which is never exact",
            "Only a sample was counted, so the true total is not known "
                "exactly",
            "The counting is done by eye, which is never accurate",
        ],
        "correct_index": 2,
        "why": "The figure comes from scaling up a small sample, so it is a "
               "best value for the whole habitat rather than a true count.",
    },
    {
        "id": "ks4-sampling-techniques-s16",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Small mammals are trapped in baited traps. Some learn that "
                "the traps hold food and enter them again willingly. Predict "
                "the effect on the estimated population size.",
        "options": [
            "The estimate is too low, because m is larger than it should "
                "be",
            "The estimate is unaffected, because the bait attracts every "
                "animal in the area equally",
            "The estimate is too high, because the trapped animals stop "
                "breeding",
            "The estimate is too high, because n₂ is larger than it should "
                "be",
        ],
        "correct_index": 0,
        "why": "Marked animals are recaptured more often than their true "
               "share, so m is too large and dividing by it makes N too small.",
    },
    {
        "id": "ks4-sampling-techniques-s17",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why quadrats are spread over a whole field rather "
                "than all placed in one corner of it.",
        "options": [
            "Placing them together means counting some plants twice",
            "One corner may differ from the rest, so the sample is not "
                "typical",
            "Spreading them out means fewer quadrats are counted",
            "Plants in one corner grow more slowly than elsewhere",
        ],
        "correct_index": 1,
        "why": "Conditions such as shade, wetness and trampling vary across a "
               "field, so a sample from one corner does not represent the "
               "whole of it.",
    },
    {
        "id": "ks4-sampling-techniques-s18",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a quadrat laid on the surface cannot be used to "
                "estimate the earthworm population of a field.",
        "options": [
            "Earthworms are found only at the very edges of a field that "
                "has been ploughed",
            "Earthworms move far too quickly to be counted inside a frame",
            "Earthworms live in the soil below, so they are not seen at "
                "all",
            "Earthworms are too small to be seen without a hand lens",
        ],
        "correct_index": 2,
        "why": "The frame samples the surface, and earthworms are in the soil "
               "beneath it, so a surface count records almost none of them.",
    },
    {
        "id": "ks4-sampling-techniques-s19",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The mean count in a 0.25 m² quadrat is 3 clover plants. "
                "Calculate the density of clover in plants per square metre.",
        "options": [
            "12 plants per m²",
            "0.25 plants per m²",
            "0.75 plants per m²",
            "3 plants per m²",
        ],
        "correct_index": 0,
        "why": "A 0.25 m² frame is a quarter of a square metre, so 3 ÷ 0.25 = "
               "12 plants per square metre.",
    },
    {
        "id": "ks4-sampling-techniques-s20",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what a belt transect records that a line transect "
                "does not.",
        "options": [
            "The direction in which each species is spreading year by year",
            "The depth of soil beneath each species along the whole line",
            "The identity of each species, which a line transect is unable "
                "to give",
            "The abundance of each species, not only whether it is present",
        ],
        "correct_index": 3,
        "why": "Quadrats along the belt let the number or cover of each "
               "species be recorded, while a line transect gives only presence "
               "or absence.",
    },
    {
        "id": "ks4-sampling-techniques-s21",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students judge percentage cover of grass in the same "
                "quadrat by eye and get 60% and 75%. Suggest how the method "
                "could be improved.",
        "options": [
            "Count individual grass plants instead, which is faster to do",
            "Use a larger quadrat, because a larger frame is always read "
                "more easily by eye",
            "Use a frame divided into a grid and count the squares filled",
            "Ask a third student and take whichever value is in the middle",
        ],
        "correct_index": 2,
        "why": "Counting gridded squares replaces a judgement by eye with a "
               "number, so different people get the same result.",
    },
    {
        "id": "ks4-sampling-techniques-s22",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why mark–recapture gives a poor estimate for a bird "
                "species that flies in and out of the study area freely.",
        "options": [
            "Individuals leave and arrive, so the population is not closed",
            "Birds always avoid any place where they have once been caught",
            "Birds cannot be marked in any way that lasts for more than a "
                "few hours",
            "Birds are counted more accurately by listening for their song",
        ],
        "correct_index": 0,
        "why": "The formula assumes no animals enter or leave between the two "
               "catches, and a freely moving bird population breaks that "
               "assumption.",
    },
    {
        "id": "ks4-sampling-techniques-s23",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a student should sample to compare dandelion "
                "abundance in a mown lawn with a nearby uncut meadow.",
        "options": [
            "Count every dandelion in the lawn and sample the meadow",
            "Place quadrats where dandelions are growing in each area",
            "Place all the quadrats in the lawn, then judge the meadow",
            "Use the same frame size and the same number of random "
                "quadrats in each",
        ],
        "correct_index": 3,
        "why": "Only the habitat should differ between the two sets of "
               "readings, so frame size, placement method and number of "
               "quadrats are all kept the same.",
    },
    {
        "id": "ks4-sampling-techniques-s24",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Twenty quadrats of 0.5 m × 0.5 m hold 140 daisies in total. "
                "Calculate the density of daisies per square metre.",
        "options": [
            "14 daisies per m²",
            "28 daisies per m²",
            "35 daisies per m²",
            "7 daisies per m²",
        ],
        "correct_index": 1,
        "why": "The mean is 140 ÷ 20 = 7 per quadrat, and each quadrat is 0.25 "
               "m², so 7 ÷ 0.25 = 28 daisies per square metre.",
    },
    {
        "id": "ks4-sampling-techniques-s25",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ecologists sample rather than count every "
                "individual of a grass species in a nature reserve.",
        "options": [
            "Counting every plant across so large an area is not practical",
            "Counting them all would leave no plants for the next survey",
            "Grass plants change species during the year, so counts drift",
            "Grasses are protected by law, so counting all of them is not "
                "permitted",
        ],
        "correct_index": 0,
        "why": "The reserve is far too large and the plants far too numerous "
               "for a full count, so a sample is counted and scaled up.",
    },
    {
        "id": "ks4-sampling-techniques-s26",
        "subtopic_slug": "sampling-techniques",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ten quadrats are used in a 10 m² plot and ten in a 10 000 m² "
                "field. Explain which estimate is likely to be more reliable.",
        "options": [
            "Both equally, because ten quadrats were used in each of them",
            "The field, because a larger area evens out any unusual "
                "patches",
            "The field, because a larger area of habitat always holds more "
                "individuals",
            "The plot, because a far greater share of its area was sampled",
        ],
        "correct_index": 3,
        "why": "Ten 0.25 m² frames sample a large fraction of a 10 m² plot but "
               "a tiny fraction of a 10 000 m² field, so the plot's mean "
               "represents its habitat far better.",
    },
    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Rearranged Lincoln index, hectare conversions, judgement on sampling
    # designs, and the assumptions met from the side that breaks them.
    {
        "id": "ks4-sampling-techniques-h05",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A frog population is estimated at 800. In the first catch 100 "
                "frogs were marked, and 15 marked frogs appeared in the second "
                "catch. Determine the size of the second catch.",
        "options": [
            "533 frogs",
            "80 frogs",
            "120 frogs",
            "150 frogs",
        ],
        "correct_index": 2,
        "why": "Rearranging N = (n₁ × n₂) ÷ m gives n₂ = (N × m) ÷ n₁ = (800 × "
               "15) ÷ 100 = 120 frogs.",
    },
    {
        "id": "ks4-sampling-techniques-h06",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The mean count in a 0.25 m² quadrat is 5 thistles. The field "
                "has an area of one hectare, which is 10 000 m². Estimate the "
                "thistle population of the field.",
        "options": [
            "200 000 thistles",
            "12 500 thistles",
            "2500 thistles",
            "50 000 thistles",
        ],
        "correct_index": 0,
        "why": "There are 10 000 ÷ 0.25 = 40 000 quadrat areas in the field, "
               "and 40 000 × 5 = 200 000 thistles.",
    },
    {
        "id": "ks4-sampling-techniques-h07",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Heather covers a mean 40% of the quadrats placed on a 2 "
                "hectare moor, where one hectare is 10 000 m². Determine the "
                "area of moor covered by heather.",
        "options": [
            "20 000 m²",
            "800 m²",
            "4000 m²",
            "8000 m²",
        ],
        "correct_index": 3,
        "why": "The moor is 20 000 m², and 40% of 20 000 m² is 8000 m² covered "
               "by heather.",
    },
    {
        "id": "ks4-sampling-techniques-h08",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One group estimates a population from 5 quadrats and another "
                "from 50 quadrats of the same size in the same field. Compare "
                "how much confidence can be placed in the two estimates.",
        "options": [
            "Both are equally good, as the same size of frame was used",
            "The 50-quadrat estimate is better, because odd patches matter "
                "less",
            "Neither can be trusted, as sampling gives no truly real value "
                "at all",
            "The 5-quadrat estimate is better, as fewer errors are made",
        ],
        "correct_index": 1,
        "why": "A mean of 50 readings is much less affected by one unusually "
               "crowded or empty quadrat than a mean of 5, so it is closer to "
               "the true density.",
    },
    {
        "id": "ks4-sampling-techniques-h09",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student places all 20 quadrats along a well-used footpath "
                "and reports the plant density of the whole meadow. Evaluate "
                "this method.",
        "options": [
            "It is poor, because trampled ground is not typical of the "
                "meadow",
            "It is poor, because quadrats may never be placed on bare "
                "ground",
            "It is sound, because a footpath crosses the whole of the "
                "meadow",
            "It is sound, because twenty quadrats is a large enough sample",
        ],
        "correct_index": 0,
        "why": "Trampling changes which plants grow, so a sample taken only on "
               "a path is biased and cannot represent the meadow as a whole, "
               "however many quadrats are used.",
    },
    {
        "id": "ks4-sampling-techniques-h10",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a mark–recapture study the second catch contains no marked "
                "individuals at all. Explain what an ecologist should "
                "conclude.",
        "options": [
            "The estimate should be taken as equal to the first catch size",
            "The population is exactly zero, since no marked animals "
                "remain",
            "The population is very small, so marked animals were all "
                "caught",
            "No estimate can be made, as the calculation would divide by "
                "zero",
        ],
        "correct_index": 3,
        "why": "m = 0 cannot be divided by, so the study gives no estimate; it "
               "suggests the population is large or the samples were taken in "
               "different places.",
    },
    {
        "id": "ks4-sampling-techniques-h11",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two ponds are sampled with the same first and second catch "
                "sizes, but twice as many marked newts are recaptured in pond "
                "B as in pond A. Predict how the two estimates compare.",
        "options": [
            "Pond B's estimate is four times pond A's estimate",
            "Pond B's estimate is half of pond A's estimate",
            "Pond B's estimate is twice pond A's estimate",
            "The two estimates are the same, as the catch sizes match",
        ],
        "correct_index": 1,
        "why": "N is divided by m, so doubling the number of marked recaptures "
               "halves the estimated population.",
    },
    {
        "id": "ks4-sampling-techniques-h12",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Marked butterflies are released, and a week later a third of "
                "them have flown out of the study meadow altogether. Predict "
                "the effect on the estimated population.",
        "options": [
            "It is too low, because fewer butterflies remain to be caught",
            "It is correct, because emigration affects both catches "
                "equally",
            "It is too high, because fewer marked individuals are "
                "recaptured",
            "It is too low, because the first catch was much larger than "
                "the second one",
        ],
        "correct_index": 2,
        "why": "Emigration removes marked individuals, so m falls; dividing by "
               "a smaller m makes the estimated population larger than it "
               "really is.",
    },
    {
        "id": "ks4-sampling-techniques-h13",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dye used to mark tadpoles fades completely within three "
                "days, and the second catch is taken two weeks later. Evaluate "
                "the investigation.",
        "options": [
            "It is valid, because a faded mark can still be seen under a "
                "lens",
            "It is invalid, because the dye kills tadpoles within three "
                "days",
            "It is valid, because the tadpoles were certainly still marked "
                "when released",
            "It is invalid, because marks are lost so m is far too small",
        ],
        "correct_index": 3,
        "why": "Marked tadpoles can no longer be recognised, so m is far below "
               "its true value and the estimate is far too high.",
    },
    {
        "id": "ks4-sampling-techniques-h14",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A field of 5000 m² is to be sampled with 0.25 m² quadrats "
                "covering 1% of its area in total. Determine how many quadrats "
                "are needed.",
        "options": [
            "125 quadrats",
            "200 quadrats",
            "500 quadrats",
            "50 quadrats",
        ],
        "correct_index": 1,
        "why": "1% of 5000 m² is 50 m², and 50 ÷ 0.25 = 200 quadrats.",
    },
    {
        "id": "ks4-sampling-techniques-h15",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rare orchid grows at about one plant per 20 m². Compare a "
                "0.25 m² quadrat with a 4 m² quadrat for estimating its "
                "population.",
        "options": [
            "Either works, because scaling up corrects for the frame's "
                "area",
            "The small frame is better, because it is quicker to count",
            "The large frame is better, because most small frames hold "
                "none",
            "The small frame is better, because it can be placed many more "
                "times over",
        ],
        "correct_index": 2,
        "why": "With a plant this sparse, almost every 0.25 m² frame records "
               "zero, so the mean is dominated by chance; a larger frame "
               "catches enough plants to give a usable mean.",
    },
    {
        "id": "ks4-sampling-techniques-h16",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reserve is half woodland and half grassland. A student "
                "samples only the woodland and reports the bramble density of "
                "the whole reserve. Evaluate this conclusion.",
        "options": [
            "It is invalid, because the sample covers only one of two "
                "habitats",
            "It is invalid, because a density figure can never be reported "
                "for a reserve",
            "It is valid, because bramble grows in woodland and in "
                "grassland",
            "It is valid, because half the reserve is a very large sample",
        ],
        "correct_index": 0,
        "why": "The sample is not representative: a figure for the whole "
               "reserve needs quadrats placed at random across both habitats.",
    },
    {
        "id": "ks4-sampling-techniques-h17",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A belt transect runs from the centre of a well-used footpath "
                "out into an untrampled meadow. Predict what the quadrat "
                "records will show along it.",
        "options": [
            "No plants until the far end of the transect is reached",
            "Few species on the path, rising as distance from it increases",
            "Most species on the path, where the soil has been broken open",
            "The same species throughout, since the meadow is one habitat",
        ],
        "correct_index": 1,
        "why": "Trampling is a condition that changes with distance from the "
               "path, so the number of species rises as the transect moves "
               "away from it.",
    },
    {
        "id": "ks4-sampling-techniques-h18",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The mean count of a plant in a meadow was 8 per quadrat in "
                "2020 and 6 per quadrat in 2025, using the same method. "
                "Calculate the percentage change.",
        "options": [
            "A fall of 75%",
            "A fall of 2%",
            "A fall of 25%",
            "A fall of 33%",
        ],
        "correct_index": 2,
        "why": "The change is 8 − 6 = 2, and 2 ÷ 8 × 100 = 25%, so the mean "
               "count has fallen by 25%.",
    },
    {
        "id": "ks4-sampling-techniques-h19",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ten 0.25 m² quadrats on a 400 m² shore hold 60 limpets in "
                "total. Estimate the number of limpets on the whole shore.",
        "options": [
            "9600 limpets",
            "960 limpets",
            "2400 limpets",
            "24 000 limpets",
        ],
        "correct_index": 0,
        "why": "The mean is 60 ÷ 10 = 6 per quadrat, and each quadrat is 0.25 "
               "m², so the density is 24 per m²; 24 × 400 m² = 9600 limpets.",
    },
    {
        "id": "ks4-sampling-techniques-h20",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One group used 1 m² quadrats and another used 0.25 m² "
                "quadrats in the same field, then added all their counts "
                "together. Explain the error.",
        "options": [
            "The groups should have counted the same species as each other",
            "The smaller frames should have been used twice as many times",
            "Adding counts is wrong, because the mean should be taken "
                "instead",
            "Counts from unequal frame areas must be converted to density "
                "first",
        ],
        "correct_index": 3,
        "why": "A count means nothing without its frame area, so each set must "
               "be turned into individuals per square metre before the two can "
               "be combined.",
    },
    {
        "id": "ks4-sampling-techniques-h21",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the reliability of mark–recapture used on snails in a "
                "walled garden with the same method used on minnows in a "
                "river.",
        "options": [
            "The river is more reliable, because the population is larger",
            "The river is more reliable, because fish are easier to catch",
            "The garden is more reliable, because few animals enter or "
                "leave",
            "Both are equally reliable, because the same formula is used",
        ],
        "correct_index": 2,
        "why": "A walled garden is close to a closed population, while minnows "
               "move freely along a river, breaking the assumption that "
               "nothing enters or leaves between the catches.",
    },
    {
        "id": "ks4-sampling-techniques-h22",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reserve is surveyed every July rather than in a different "
                "month each year. Explain why.",
        "options": [
            "Plants differ between months, so only like years can be "
                "compared",
            "July has long days, so more quadrats can be counted",
            "July is the only month quadrats can be laid flat",
            "Surveying in one month means fewer surveys are done",
        ],
        "correct_index": 0,
        "why": "Abundance changes through the year, so sampling in the same "
               "month each time means a difference between years is a real "
               "change rather than a seasonal one.",
    },
    {
        "id": "ks4-sampling-techniques-h23",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Seven of a student's twelve quadrats contain no plants of the "
                "target species. Evaluate the suggestion that these seven "
                "should be left out of the mean.",
        "options": [
            "They should be left out, because they make the mean too small",
            "They should be kept, but counted as one plant each instead",
            "They should be left out, because a zero is not a real reading",
            "They should be kept, because the zeros are part of the "
                "pattern",
        ],
        "correct_index": 3,
        "why": "A zero is a genuine measurement of how sparse the species is; "
               "dropping the zeros would raise the mean and give a badly "
               "inflated population estimate.",
    },
    {
        "id": "ks4-sampling-techniques-h24",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One student counts only plants wholly inside the frame; "
                "another counts every plant the frame touches. Predict how "
                "their estimates will differ, and explain.",
        "options": [
            "The second gets a lower estimate, as each edge plant is "
                "counted only once",
            "The second gets a higher estimate, as edge plants are "
                "included",
            "The first gets a higher estimate, as fewer plants are missed",
            "Their estimates will match, because the frame area is the "
                "same",
        ],
        "correct_index": 1,
        "why": "Counting every plant the frame touches effectively samples an "
               "area larger than the frame, so the mean count and the scaled "
               "estimate both come out higher.",
    },
    {
        "id": "ks4-sampling-techniques-h25",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A seabird colony on a small island holds about 300 nests, all "
                "visible from one clifftop. Evaluate the use of quadrat "
                "sampling here.",
        "options": [
            "Counting all is better, because a full count avoids sampling "
                "error",
            "Sampling is better, because an estimate beats a direct count",
            "Sampling is better, because counting 300 nests takes too long",
            "Counting all is better, because sampling a colony is banned",
        ],
        "correct_index": 0,
        "why": "Sampling is only used when a full count is impractical; here "
               "the whole colony can be counted, which removes the uncertainty "
               "a scaled-up estimate carries.",
    },
    {
        "id": "ks4-sampling-techniques-h26",
        "subtopic_slug": "sampling-techniques",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "To detect a slow change in a meadow over ten years, compare "
                "sampling 40 random quadrats once a year with sampling 4 "
                "quadrats every month.",
        "options": [
            "The monthly plan is better, as four quadrats count everything",
            "Both are equal, as 48 quadrats a year are counted",
            "The monthly plan gives more readings each year",
            "The yearly plan is better, because a large annual mean is "
                "comparable",
        ],
        "correct_index": 3,
        "why": "Forty quadrats give a reliable mean for one point in the "
               "season, and repeating it at the same time each year makes a "
               "ten-year trend visible without seasonal variation hiding it.",
    },
]
