"""B7 lesson 03 — Testing a leaf for starch: twelve questions (MRB-269).

The lesson teaches five steps and one habit of mind: every step exists because
leaving it out produces a result you cannot read, and a positive result is only
worth something if you can say when the starch was made. The bank probes both.
The easier band checks that each step is paired with its own reason — the two
dark days with emptying the store, the boiling water with killing and opening
the cells, the water bath with the flammability — and that blue-black and
orange-brown are both real readings. The standard band puts the student in
front of the situations the bench already showed them: the leaf that went in
green, the plant that was never destarched, the leaf that crumbled on the tile,
and the half-and-half design that makes light the only difference. The harder
band works backwards from a symptom to the missing step, tests a variegated
leaf the lesson only mentions in passing, asks why the practical hunts starch
rather than the glucose photosynthesis actually makes, and puts the safety rule
in a room where somebody else is holding the flame.

Both declared misconceptions supply distractors throughout. PLANT-05 ("the leaf
goes black because the iodine reacts with the chlorophyll") drives the
blue-black-across-the-green option in s01, the "no green left to hide it"
option in h02, and the bright-green and brick-red readings in e01. PLANT-06
("just pick a leaf and test it — the destarching is a waste of two days")
drives every wrong option in s02 and the shortened-destarch option in h01.
Three further errors the lesson exists to correct supply the rest: that a step
does a neighbouring step's job (e02, e03, s03), that a result you cannot see is
a negative result (s01), and that an unreliable result means the reagent has
gone off rather than the method (h01). e04 and h04 are built on the two ways
students defuse a flammability rule — a gauze, and "it is only about my own
tube".

`figure` is None throughout: this lesson declares no figures.
"""

UNIT = "B7"
LESSON = "testing-a-leaf-for-starch"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-03-e01",
        "band": "easier",
        "text": "The leaf is spread out on a white tile and the iodine goes "
                "on. Which colour tells you there is starch in that part of "
                "the leaf?",
        "options": [
            {"text": "Orange-brown, spreading out from each drop.",
             "correct": False,
             "why": "Orange-brown is iodine's own colour, and it is what you "
                    "see where there is no starch. A patch that has not "
                    "changed is a real reading, not a failed test."},
            {"text": "Blue-black, showing up against the pale leaf.",
             "correct": True},
            {"text": "Bright green, the colour the leaf started as.",
             "correct": False,
             "why": "The green went into the ethanol back in step 3, long "
                    "before the iodine arrived. There is no chlorophyll left "
                    "in the leaf for anything to happen to."},
            {"text": "Brick red, the same as a positive in Food tests.",
             "correct": False,
             "why": "Brick red is Benedict's answering a question about sugar. "
                    "Iodine answers one question only — starch — and it "
                    "answers it in blue-black."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e02",
        "band": "easier",
        "text": "Two days in a dark cupboard come before anything else "
                "happens. What is going on inside the plant while it sits "
                "there?",
        "options": [
            {"text": "It respires away the starch it was holding, so it "
                     "starts empty.",
             "correct": True},
            {"text": "It stops photosynthesising, which takes an hour or two "
                     "at most.",
             "correct": False,
             "why": "Photosynthesis does stop the moment the light goes, but "
                    "that is not what the two days are for. The store already "
                    "sitting in the leaves is what has to go, and using that "
                    "up is what takes so long."},
            {"text": "The starch drains out of the leaves and down into the "
                     "roots.",
             "correct": False,
             "why": "Starch is insoluble and cannot travel anywhere as starch. "
                    "The plant has to break its store down and use it up, and "
                    "that is the work the two days are doing."},
            {"text": "It loses its chlorophyll, so the leaves are pale before "
                     "you start.",
             "correct": False,
             "why": "The green comes out later, in the ethanol at step 3. The "
                    "dark cupboard is about emptying the starch store, not "
                    "about the colour of the leaf."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e03",
        "band": "easier",
        "text": "Step 2 is about a minute in a beaker of boiling water. What "
                "does that minute do to the leaf?",
        "options": [
            {"text": "It softens the leaf so it can be spread flat on the "
                     "tile.",
             "correct": False,
             "why": "That is step 4, after the ethanol, when the leaf comes "
                    "out brittle and shrivelled. At step 2 the leaf still "
                    "bends perfectly well."},
            {"text": "It dissolves the chlorophyll out of the cells so the "
                     "leaf goes pale.",
             "correct": False,
             "why": "Water will not shift chlorophyll — that is the job "
                    "ethanol is there for. Boiling water is about what the "
                    "cells are doing, not about the colour."},
            {"text": "It kills the cells and breaks down the membranes so "
                     "iodine gets in.",
             "correct": True},
            {"text": "It dissolves the starch, so the iodine can reach it more "
                     "easily.",
             "correct": False,
             "why": "That would destroy the very thing you are testing for. "
                    "Starch is insoluble and stays exactly where it was — the "
                    "iodine is what has to travel."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e04",
        "band": "easier",
        "text": "The ethanol has to be heated. How is it heated, and what is "
                "the reason for heating it that way?",
        "options": [
            {"text": "Straight over a Bunsen, because it has to reach 78 °C "
                     "to boil.",
             "correct": False,
             "why": "78 °C is below the boiling point of water, so a naked "
                    "flame is far more heat than you need — and ethanol "
                    "vapour ignites. This is the one choice on this bench that "
                    "ends the practical instead of spoiling it."},
            {"text": "Over a Bunsen with a gauze, so no flame touches the "
                     "glass.",
             "correct": False,
             "why": "A gauze protects nothing here. It is the vapour coming "
                    "off the ethanol that catches fire, not the tube, so the "
                    "answer is no naked flame at all."},
            {"text": "Stood in hot water, because ethanol would evaporate away "
                     "too fast.",
             "correct": False,
             "why": "Right method, wrong reason. Losing a little ethanol would "
                    "not matter to anyone; the water bath is there because the "
                    "vapour catches fire easily."},
            {"text": "Stood in hot water, because ethanol vapour catches fire "
                     "easily.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-03-s01",
        "band": "standard",
        "text": "A student decides the ethanol is a waste of time and drops "
                "iodine straight onto the boiled, still-green leaf. What do "
                "they end up with?",
        "options": [
            {"text": "No colour change anywhere, so this leaf had no starch in "
                     "it.",
             "correct": False,
             "why": "The starch is there and the iodine is finding it. You "
                    "simply cannot see blue-black against a dark green leaf, "
                    "and a result you cannot see is not a negative result."},
            {"text": "A stained green leaf and no information at all.",
             "correct": True},
            {"text": "Blue-black across the leaf, where iodine met the "
                     "chlorophyll.",
             "correct": False,
             "why": "Iodine tests for starch and for nothing else. A slice of "
                    "potato has never had a scrap of chlorophyll in it and "
                    "turns blue-black instantly."},
            {"text": "The same pattern as the full method, only fainter and "
                     "harder to read.",
             "correct": False,
             "why": "Nothing has taken the green out, so the leaf is as dark "
                    "as it started. The colour change is hidden completely, "
                    "not weakened."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s02",
        "band": "standard",
        "text": "A plant comes straight off a bright windowsill with no dark "
                "cupboard first, and one leaf wears foil over half of it for a "
                "day. Tested properly, both halves go blue-black. What has "
                "been shown?",
        "options": [
            {"text": "That light is not needed, since the covered half made "
                     "starch too.",
             "correct": False,
             "why": "The covered half made no starch that day. It was already "
                    "holding starch from before the foil went on, which is "
                    "precisely what two days in the dark would have removed."},
            {"text": "That the foil had been letting light through to the half "
                     "underneath.",
             "correct": False,
             "why": "Foil blocks light completely. The starch under it is "
                    "older than the foil — it was in the leaf before the "
                    "experiment started."},
            {"text": "Nothing about light — that starch could be days old.",
             "correct": True},
            {"text": "That the test failed, because the two halves should have "
                     "differed.",
             "correct": False,
             "why": "The test worked and reported the starch that was there. "
                    "The fault is in the preparation, not the chemistry: the "
                    "result is real, and it is unusable."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s03",
        "band": "standard",
        "text": "Straight out of the ethanol and onto the tile with no dip in "
                "hot water, a leaf tears into three pieces as it is spread. "
                "What has that cost the student?",
        "options": [
            {"text": "The starch, which came away with the pieces that tore "
                     "off.",
             "correct": False,
             "why": "The starch is inside the cells and goes wherever the "
                    "pieces go — none of it has been lost. What has been lost "
                    "is the arrangement of those pieces."},
            {"text": "Nothing at all — the pieces still turn blue-black, so "
                     "the result stands.",
             "correct": False,
             "why": "The chemistry did work, which is why this is the mildest "
                    "fault on the bench. But this experiment is about where "
                    "the starch is, and where is exactly what has torn."},
            {"text": "The iodine, which cannot soak into a brittle, shrivelled "
                     "leaf.",
             "correct": False,
             "why": "Iodine reaches the fragments perfectly well — the cells "
                    "were killed and opened up back at step 2. The damage here "
                    "is not chemical."},
            {"text": "The pattern — the boundary between the two halves is in "
                     "pieces.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s04",
        "band": "standard",
        "text": "The foil covers half of one leaf, rather than a whole second "
                "plant being shut in the dark. Why is one leaf the better "
                "comparison?",
        "options": [
            {"text": "Its two halves share the same water, temperature, carbon "
                     "dioxide and age.",
             "correct": True},
            {"text": "One leaf is as much as a single tile and a few drops of "
                     "iodine will cover.",
             "correct": False,
             "why": "Nobody is short of tile or iodine. The reason is that the "
                    "two halves of one leaf differ in light and in nothing "
                    "else at all."},
            {"text": "The two halves can then be put through the test in "
                     "different ways.",
             "correct": False,
             "why": "Both halves go through the identical five steps. A "
                    "comparison only works if the treatment is the same and "
                    "light is the single difference."},
            {"text": "A second plant would need destarching as well, and that "
                     "takes days.",
             "correct": False,
             "why": "It would, and that would be no problem — you destarch "
                    "before every run anyway. The reason for one leaf is that "
                    "its halves shared everything except light."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-03-h01",
        "band": "harder",
        "text": "A class runs the test three times on identical leaves from "
                "one destarched plant and gets a faint blotchy pattern that "
                "comes out differently every time. Which step is being left "
                "out?",
        "options": [
            {"text": "The destarching — two days in the dark cannot have been "
                     "enough.",
             "correct": False,
             "why": "A plant that was not properly destarched gives a strong, "
                    "even blue-black, including under the foil. It does not "
                    "make the pattern come out differently each run."},
            {"text": "The ethanol, so the leaves were still green when the "
                     "iodine went on.",
             "correct": False,
             "why": "A green leaf gives you nothing readable at all rather "
                    "than something faint — and it fails the same way every "
                    "single time, which is not what is happening here."},
            {"text": "The boil in water, so the cells are alive and the "
                     "surface still waxy.",
             "correct": True},
            {"text": "None of them — the iodine has gone off and the bottle "
                     "needs replacing.",
             "correct": False,
             "why": "Blaming the reagent is the wrong instinct here. One "
                    "bottle gave three different patterns, so what is varying "
                    "is inside the leaves, not inside the bottle."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h02",
        "band": "harder",
        "text": "A variegated leaf — green at the edges, white down the middle "
                "— comes off a destarched plant after a day in bright light "
                "and is tested in full. What does the tile show?",
        "options": [
            {"text": "Blue-black at the edges, orange-brown down the white "
                     "middle.",
             "correct": True},
            {"text": "Blue-black all over, as starch spreads out through the "
                     "leaf.",
             "correct": False,
             "why": "Starch does not travel — it is insoluble and sits as "
                    "grains where it was made. That is the whole reason it is "
                    "still there to be found the next morning."},
            {"text": "Blue-black down the middle, where no green is left to "
                     "hide it.",
             "correct": False,
             "why": "No green is left anywhere by then; the ethanol took it "
                    "all out at step 3. Nothing is being hidden — the white "
                    "parts have no chlorophyll, so they made no starch."},
            {"text": "No change anywhere, since a variegated leaf cannot "
                     "photosynthesise.",
             "correct": False,
             "why": "The green parts have chlorophyll and photosynthesise "
                    "perfectly well. Only the white parts, with nothing to "
                    "absorb the light, make nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h03",
        "band": "harder",
        "text": "Photosynthesis makes glucose, yet this practical goes hunting "
                "for starch. What makes starch the thing worth testing for?",
        "options": [
            {"text": "There is no reliable test for glucose inside the "
                     "cells of a leaf.",
             "correct": False,
             "why": "There is one — Benedict's, from Food tests. The problem "
                    "is not the test. It is that glucose is soluble, so it "
                    "does not stay where it was made."},
            {"text": "Glucose is only in a leaf at night, once starch is "
                     "broken down.",
             "correct": False,
             "why": "That is the wrong way round. Glucose is made in the light "
                    "and stored as starch, and the starch is broken back down "
                    "to glucose at night."},
            {"text": "Iodine finds glucose too, so starch is just the easier "
                     "one to see.",
             "correct": False,
             "why": "Iodine answers one question and one only, and that "
                    "question is starch. It tells you nothing whatever about "
                    "glucose."},
            {"text": "Starch is insoluble, so it stays where it was made "
                     "until you look.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h04",
        "band": "harder",
        "text": "Your ethanol is standing in its water bath and your own "
                "Bunsen is turned off. The group at the next bench have theirs "
                "lit. What does the safety rule actually require?",
        "options": [
            {"text": "Nothing more — the rule is about the flame under your "
                     "own tube.",
             "correct": False,
             "why": "The rule is written about the room, not about your tube. "
                    "Ethanol vapour drifts along a bench and will find a flame "
                    "that is nowhere near you."},
            {"text": "No naked flame anywhere in the room while ethanol is "
                     "heated.",
             "correct": True},
            {"text": "Nothing more, as long as your tube is stoppered while it "
                     "heats.",
             "correct": False,
             "why": "Never seal a tube you are heating — the pressure has to "
                    "go somewhere. The control for ethanol is no naked flame "
                    "in the room, not a bung."},
            {"text": "Nothing more, since a water bath holds the ethanol below "
                     "78 °C.",
             "correct": False,
             "why": "Ethanol gives off flammable vapour long before it boils, "
                    "so keeping the liquid cool is not the protection. It is "
                    "the flame that has to go."},
        ],
        "figure": None,
    },
]
