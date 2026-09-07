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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-03-e05",
        "band": "easier",
        "text": "What is starch?",
        "options": [
            {"text": "An insoluble carbohydrate made of many glucose "
                     "molecules joined together.",
             "correct": True},
            {"text": "A sugar the plant makes and then moves out of the "
                     "leaf.",
             "correct": False,
             "why": "That is glucose. Starch is what a leaf turns glucose "
                    "into, and being insoluble it stays exactly where it was "
                    "made."},
            {"text": "The green pigment a leaf needs before it can make "
                     "food.",
             "correct": False,
             "why": "That is chlorophyll, and it is dissolved out into the "
                    "ethanol before the iodine goes on. Starch is the store "
                    "you are testing for."},
            {"text": "A mineral a plant takes up from the soil and keeps in "
                     "its leaves.",
             "correct": False,
             "why": "Minerals come from the soil. Starch is built by the "
                    "plant itself, out of the glucose it made."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e06",
        "band": "easier",
        "text": "The decolourised leaf is spread on a white tile before the "
                "iodine is added. Why a white tile?",
        "options": [
            {"text": "Because iodine attacks metal, so china is the only safe "
                     "surface to use.",
             "correct": False,
             "why": "Nothing here turns on what the tile is made of. It is "
                    "white so that the colours can be read."},
            {"text": "Because a white surface bleaches the last of the green "
                     "out of the leaf.",
             "correct": False,
             "why": "The ethanol took the green out back at step 3. The tile "
                    "is white so the colours show against a neutral "
                    "background."},
            {"text": "Because the colour has to be read against a neutral "
                     "background.",
             "correct": True},
            {"text": "Because a cold tile stops the leaf changing any further "
                     "while you look at it.",
             "correct": False,
             "why": "There is nothing left to stop; the cells were killed at "
                    "step 2. The tile is white so blue-black and orange-brown "
                    "can be told apart."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e07",
        "band": "easier",
        "text": "Before the experiment starts, what goes into the dark, and "
                "for how long?",
        "options": [
            {"text": "The picked leaf, for about an hour.",
             "correct": False,
             "why": "It is the whole plant, and for about two days. A leaf "
                    "shut in a drawer for an hour would still be holding all "
                    "the starch it had."},
            {"text": "The whole plant, for about two days.",
             "correct": True},
            {"text": "The whole plant, for about two hours.",
             "correct": False,
             "why": "Two hours is nowhere near long enough. It takes about "
                    "two days of respiring in the dark for the leaves to "
                    "empty their store."},
            {"text": "The picked leaf, for about two days.",
             "correct": False,
             "why": "The plant goes in whole. A leaf cut off the plant will "
                    "not empty its store the way a living plant's leaves do."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e08",
        "band": "easier",
        "text": "This investigation uses the word control. What does a "
                "control mean here?",
        "options": [
            {"text": "The step that controls how hot the ethanol is allowed "
                     "to get.",
             "correct": False,
             "why": "That is the water bath, and it is a safety measure. A "
                    "control is the part of an investigation everything else "
                    "is compared against."},
            {"text": "The person who decides which steps the class will leave "
                     "out.",
             "correct": False,
             "why": "A control is not a person. It is the part of the "
                    "investigation that everything else is compared with."},
            {"text": "The amount of iodine dropped on the leaf, kept exactly "
                     "the same every time so the test is fair.",
             "correct": False,
             "why": "Keeping a quantity the same is a different idea. The "
                    "control is the thing your result is compared against."},
            {"text": "The part of the investigation everything else is "
                     "compared against, such as the half of the leaf under "
                     "the foil.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e09",
        "band": "easier",
        "text": "Which comes first in the method, the ethanol or the iodine, "
                "and what happens between them?",
        "options": [
            {"text": "The ethanol at step 3 and the iodine at step 5, with "
                     "the hot water dip in between.",
             "correct": True},
            {"text": "The iodine first, so the colour is fixed before the "
                     "green is taken out.",
             "correct": False,
             "why": "The iodine goes on last of all. On a green leaf nothing "
                    "it did would be visible."},
            {"text": "The two together, so the ethanol carries the iodine "
                     "into the cells.",
             "correct": False,
             "why": "They are separate steps with the hot water dip between "
                    "them. The ethanol removes the green long before the "
                    "iodine arrives."},
            {"text": "The ethanol at step 3 and the iodine straight after it, "
                     "with nothing in between.",
             "correct": False,
             "why": "The hot water dip comes between them, to soften a leaf "
                    "that the ethanol has left brittle and shrivelled."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e10",
        "band": "easier",
        "text": "What is the leaf like when it comes out of the ethanol?",
        "options": [
            {"text": "Bright green and limp, since the ethanol has soaked "
                     "into every cell.",
             "correct": False,
             "why": "The green has gone into the ethanol, which is why the "
                    "ethanol turns green and the leaf goes pale."},
            {"text": "Soft and stretchy, so it can be spread on the tile "
                     "straight away.",
             "correct": False,
             "why": "It is the opposite — brittle and shrivelled, which is "
                    "why it is dipped in hot water before it is spread out."},
            {"text": "Pale, brittle and shrivelled, which is why it is dipped "
                     "in hot water next.",
             "correct": True},
            {"text": "Blue-black in patches, wherever the ethanol has found "
                     "starch.",
             "correct": False,
             "why": "Ethanol tests for nothing. Only the iodine, at step 5, "
                    "turns anything blue-black."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e11",
        "band": "easier",
        "text": "Why is the leaf spread out flat before the iodine goes on?",
        "options": [
            {"text": "So the ethanol left in it can evaporate away before the "
                     "test.",
             "correct": False,
             "why": "Nothing is waiting for the ethanol to go. The leaf is "
                    "spread out so the pattern of colour across it can be "
                    "seen."},
            {"text": "So the whole leaf is exposed and the pattern across it "
                     "can be seen.",
             "correct": True},
            {"text": "So the leaf dries out and takes up the iodine more "
                     "strongly.",
             "correct": False,
             "why": "A dried-out leaf is not what is wanted — it was softened "
                    "on purpose. Spreading it flat is about seeing the whole "
                    "of it."},
            {"text": "So the leaf weighs less and floats on top of the "
                     "iodine.",
             "correct": False,
             "why": "Nothing is floated or weighed here. Flat means the whole "
                    "surface can be read at once."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e12",
        "band": "easier",
        "text": "Half of one leaf is covered with foil before the plant goes "
                "into the light. What is the foil doing?",
        "options": [
            {"text": "Keeping that half warm, so temperature can be compared "
                     "across the leaf.",
             "correct": False,
             "why": "Both halves are on one leaf and share a temperature. The "
                    "foil is blocking light, which is the one thing being "
                    "changed."},
            {"text": "Stopping the iodine from reaching that half during the "
                     "test.",
             "correct": False,
             "why": "The foil comes off long before the test. It was on the "
                    "leaf while the plant was in the light."},
            {"text": "Holding the leaf flat so that it does not curl in the "
                     "sunshine.",
             "correct": False,
             "why": "Nothing needs holding flat at that stage. The foil is "
                    "there to keep light off one half."},
            {"text": "Keeping light off that half, so light is the only "
                     "difference between the two halves.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e13",
        "band": "easier",
        "text": "A destarched plant spends a day in bright light. Where has "
                "the starch in its leaves come from?",
        "options": [
            {"text": "From glucose the leaf built by photosynthesis and then "
                     "converted for storage.",
             "correct": True},
            {"text": "From the soil, taken up through the roots and carried "
                     "into the leaf.",
             "correct": False,
             "why": "Nothing takes starch up from the soil. The leaf built "
                    "glucose from carbon dioxide and water, then converted it "
                    "into starch."},
            {"text": "From the iodine, which leaves starch behind wherever it "
                     "soaks in.",
             "correct": False,
             "why": "Iodine is a test and adds nothing to the leaf. It "
                    "reports the starch that was already there."},
            {"text": "From the store the plant was holding before the "
                     "experiment began.",
             "correct": False,
             "why": "That store is exactly what the two days in the dark got "
                    "rid of. Anything found now was made during the "
                    "experiment."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-03-s05",
        "band": "standard",
        "text": "Two destarched plants are set up. One goes into bright light "
                "for a day; the other stays in the dark. A leaf from the dark "
                "one is tested in full and the tile stays orange-brown "
                "everywhere. Has the test failed?",
        "options": [
            {"text": "Yes — a test that has been run properly should give "
                     "some blue-black somewhere.",
             "correct": False,
             "why": "Orange-brown is a real reading rather than a failure. "
                    "This plant had no light, so it made no starch, and the "
                    "test says so."},
            {"text": "No — orange-brown is a real result, and it says no "
                     "starch was made in the dark.",
             "correct": True},
            {"text": "No — but nothing can be concluded, because there was "
                     "nothing to compare this leaf against.",
             "correct": False,
             "why": "There is a comparison: the identical plant that was "
                    "given light. That is what makes this reading worth "
                    "having."},
            {"text": "Yes — the iodine must be too old, since a whole leaf "
                     "gave no colour at all.",
             "correct": False,
             "why": "The reagent is not at fault. A destarched plant kept in "
                    "the dark is exactly the case where no starch is "
                    "expected."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s06",
        "band": "standard",
        "text": "A student stands the tube of ethanol in a beaker of water "
                "that was boiled in a kettle and poured out, with no Bunsen "
                "alight anywhere in the room. Is that acceptable?",
        "options": [
            {"text": "Yes — that is what a water bath is, and the point of it "
                     "is that no flame goes near the ethanol.",
             "correct": True},
            {"text": "No — the water has to be kept boiling by a Bunsen "
                     "underneath, or the ethanol will not warm through.",
             "correct": False,
             "why": "Water straight off the boil carries plenty of heat, and "
                    "ethanol boils at 78 °C. A Bunsen under it would put back "
                    "the hazard the bath removes."},
            {"text": "No — the ethanol has to reach a full boil, and that "
                     "needs a flame directly under the tube.",
             "correct": False,
             "why": "A naked flame under ethanol is the one mistake that ends "
                    "the practical. Hot water carries the heat perfectly "
                    "well."},
            {"text": "Yes — but only because ethanol is not flammable once it "
                     "is inside a tube.",
             "correct": False,
             "why": "Ethanol is flammable in a tube, in a beaker and anywhere "
                    "else. What makes this safe is that there is no flame in "
                    "the room."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s07",
        "band": "standard",
        "text": "Several things can go wrong during this practical. Which one "
                "ends it, rather than spoiling the data?",
        "options": [
            {"text": "Skipping the destarching, so the covered half goes "
                     "blue-black as well.",
             "correct": False,
             "why": "That gives a result you can see and cannot use, which is "
                    "bad — but the practical ran. The one that ends it is "
                    "heating ethanol over a flame."},
            {"text": "Skipping the ethanol, so the leaf is still green when "
                     "the iodine goes on.",
             "correct": False,
             "why": "That leaves you with no reading at all, and it is still "
                    "a problem with the data. Heating ethanol over a flame "
                    "stops everything."},
            {"text": "Heating the ethanol over a Bunsen instead of standing "
                     "the tube in hot water.",
             "correct": True},
            {"text": "Skipping the hot water dip, so the leaf tears as it is "
                     "spread on the tile.",
             "correct": False,
             "why": "That is the mildest fault of the lot — the chemistry "
                    "worked and only the pattern is damaged. The one that "
                    "ends the practical is the naked flame."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s08",
        "band": "standard",
        "text": "A destarched plant has a strip of black paper taped across "
                "one leaf and spends a day in bright light. Tested in full, "
                "the leaf shows the strip's shape in orange-brown against "
                "blue-black. What has been shown?",
        "options": [
            {"text": "That black paper stops starch moving along inside a "
                     "leaf.",
             "correct": False,
             "why": "Starch does not move — it is insoluble and stays where "
                    "it was made. What the paper stopped was the light."},
            {"text": "That the paper damaged the tissue underneath it, so "
                     "that part of the leaf could not work.",
             "correct": False,
             "why": "The leaf under the paper is healthy and would have made "
                    "starch given light. What it was denied was the light "
                    "itself."},
            {"text": "Nothing, because one leaf can never be a fair "
                     "comparison.",
             "correct": False,
             "why": "One leaf is the best comparison available: both parts "
                    "share water, temperature, carbon dioxide and age, so "
                    "light is the only difference."},
            {"text": "That starch was made only where light fell, on a plant "
                     "that started with none.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s09",
        "band": "standard",
        "text": "A destarched plant goes back into bright light for only "
                "twenty minutes before a leaf is picked and tested. The tile "
                "is orange-brown all over. What is the fair conclusion?",
        "options": [
            {"text": "That light is not needed for a leaf to make starch "
                     "after all.",
             "correct": False,
             "why": "You cannot conclude that from a plant given almost no "
                    "time. Twenty minutes is not long enough to build starch "
                    "you could see."},
            {"text": "That too little time was allowed, so this run says "
                     "almost nothing about light.",
             "correct": True},
            {"text": "That the plant was not properly destarched to begin "
                     "with.",
             "correct": False,
             "why": "A plant that was not properly destarched gives the "
                    "opposite problem: blue-black everywhere, including where "
                    "there should be none."},
            {"text": "That the iodine has failed, since a healthy plant "
                     "always holds some starch.",
             "correct": False,
             "why": "A destarched plant holds none, which is the whole point "
                    "of destarching it. The iodine is reporting honestly."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s10",
        "band": "standard",
        "text": "A drop of iodine on a slice of raw potato turns blue-black "
                "at once. What does that tell you about the question iodine "
                "is answering?",
        "options": [
            {"text": "That it responds to starch, in something that has never "
                     "had chlorophyll in it.",
             "correct": True},
            {"text": "That it responds to anything a plant has made, sugar "
                     "and starch alike.",
             "correct": False,
             "why": "Iodine says nothing about sugar. Benedict's solution "
                    "answers that question, and it answers in brick red "
                    "rather than blue-black."},
            {"text": "That a potato is green under its skin, so the pigment "
                     "is what is reacting.",
             "correct": False,
             "why": "A potato tuber has no chlorophyll at all, which is "
                    "exactly what makes it such useful evidence about what "
                    "iodine finds."},
            {"text": "That the test works on food but not on a living leaf.",
             "correct": False,
             "why": "It works on both. What matters is whether starch is "
                    "present, and a leaf that has been in the light has "
                    "plenty."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s11",
        "band": "standard",
        "text": "A student says the two days in the dark are what keep the "
                "covered half of the leaf orange-brown. What have they mixed "
                "up?",
        "options": [
            {"text": "Nothing — the dark days and the foil do the same job in "
                     "two different ways.",
             "correct": False,
             "why": "They are two different controls. The dark days empty the "
                    "whole plant before you start; the foil keeps light off "
                    "one half during the run."},
            {"text": "The dark days keep the whole leaf orange-brown, so the "
                     "foil is what turns the other half black.",
             "correct": False,
             "why": "The foil turns nothing black — light is what lets starch "
                    "be made. The foil keeps one half in the dark while the "
                    "rest of the leaf is lit."},
            {"text": "The two days empty the whole plant before the run; the "
                     "foil keeps light off one half during it.",
             "correct": True},
            {"text": "The two days are what remove the chlorophyll, and the "
                     "foil is what removes the starch.",
             "correct": False,
             "why": "Chlorophyll comes out in the ethanol at step 3. The dark "
                    "days empty the starch store, and the foil keeps light "
                    "off one half."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s12",
        "band": "standard",
        "text": "A class is finding out why each step of the starch test "
                "matters, by leaving steps out. Why leave one step out at a "
                "time rather than several at once?",
        "options": [
            {"text": "Because leaving two out takes twice as long to work "
                     "through.",
             "correct": False,
             "why": "It takes no longer at all. The reason is that you could "
                    "not then say which of the two faults produced what you "
                    "saw."},
            {"text": "Because a leaf with two steps missing gives no result "
                     "at all to look at.",
             "correct": False,
             "why": "It gives a result, and a damaged one. The trouble is "
                    "that you cannot say which of the two faults did the "
                    "damage."},
            {"text": "Because two faults cancel each other out and give a "
                     "normal-looking result.",
             "correct": False,
             "why": "They do not cancel. Each damages the result in its own "
                    "way, and together you cannot say which did what."},
            {"text": "Because with two things missing you cannot tell which "
                     "of them caused the result.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s13",
        "band": "standard",
        "text": "One mistake gives a result you can read but cannot use; "
                "another gives no reading at all. Which mistake is which?",
        "options": [
            {"text": "Skipping the ethanol gives a result you cannot use; "
                     "skipping the destarching gives no reading.",
             "correct": False,
             "why": "It is the other way round. A green leaf hides the colour "
                    "completely, while an undestarched leaf gives a strong "
                    "blue-black nobody can date."},
            {"text": "Skipping the destarching gives a readable result you "
                     "cannot date; skipping the ethanol gives no reading.",
             "correct": True},
            {"text": "Both give no reading, since neither leaf can take up "
                     "the iodine.",
             "correct": False,
             "why": "The undestarched leaf takes up iodine perfectly well and "
                    "goes blue-black. Its problem is that you cannot say when "
                    "the starch was made."},
            {"text": "Both give readable results, and the only difference is "
                     "how strong the colour is.",
             "correct": False,
             "why": "A still-green leaf gives nothing readable at all. The "
                    "colour change is hidden completely rather than "
                    "weakened."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-03-h05",
        "band": "harder",
        "text": "A student plans to destarch a plant by shutting it in a "
                "cupboard for two days with a bright lamp left on inside, so "
                "that it stays healthy. What will happen?",
        "options": [
            {"text": "It will destarch faster, because the lamp keeps the "
                     "plant respiring more quickly.",
             "correct": False,
             "why": "Respiring the store away is only half of it. With a lamp "
                    "on, the plant goes on photosynthesising and keeps "
                    "replacing the starch."},
            {"text": "It will destarch as usual, because a cupboard lamp is "
                     "far weaker than daylight.",
             "correct": False,
             "why": "Weaker is not off. Even a dim lamp keeps some "
                    "photosynthesis going, so the store is not reliably "
                    "emptied."},
            {"text": "It will not destarch, because the plant goes on making "
                     "starch while there is light.",
             "correct": True},
            {"text": "It will destarch, but its leaves will lose their "
                     "chlorophyll and go pale.",
             "correct": False,
             "why": "Chlorophyll is not lost in a lit cupboard. The problem "
                    "is that the plant is still photosynthesising, and so "
                    "still making starch."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h06",
        "band": "harder",
        "text": "Why is the whole plant destarched, rather than only the leaf "
                "that is going to be tested?",
        "options": [
            {"text": "A leaf left on a lit plant is supplied with sugar from "
                     "the other leaves through the phloem.",
             "correct": True},
            {"text": "A single leaf would dry out and die before the two days "
                     "were up.",
             "correct": False,
             "why": "A leaf on a plant in a cupboard is fine for two days. "
                    "The plant goes in whole because its other leaves would "
                    "keep supplying that one."},
            {"text": "Iodine only works on a leaf that has been off the plant "
                     "for two days.",
             "correct": False,
             "why": "Iodine works on a leaf picked minutes earlier. The two "
                    "days are about emptying the store, not about the "
                    "reagent."},
            {"text": "The starch would drain out of the leaf into the stem if "
                     "the plant were left in the light.",
             "correct": False,
             "why": "Starch is insoluble and drains nowhere. What travels in "
                    "the phloem is dissolved sugar, and that is exactly the "
                    "problem."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h07",
        "band": "harder",
        "text": "Someone says a leaf goes blue-black because its cells were "
                "killed in the boiling water. Every part of that leaf was "
                "killed at step 2, and only some of it goes blue-black. What "
                "does that show?",
        "options": [
            {"text": "That the boiling was uneven, so parts of the leaf are "
                     "still alive.",
             "correct": False,
             "why": "A minute in boiling water kills the whole leaf. The "
                    "pattern must come from something that differed before "
                    "the leaf was picked."},
            {"text": "That the iodine reached some parts of the leaf and not "
                     "others.",
             "correct": False,
             "why": "The cells were opened up everywhere at step 2, so the "
                    "iodine gets in everywhere. What differs is whether there "
                    "was starch to find."},
            {"text": "That dying cells release a substance which turns dark "
                     "in some parts of the leaf.",
             "correct": False,
             "why": "Nothing is released by dying. The blue-black appears "
                    "where starch is present, and nowhere else."},
            {"text": "That iodine is responding to the starch that is there, "
                     "not to the cells being dead.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h08",
        "band": "harder",
        "text": "A leaf could hold a whole day's production as glucose "
                "instead of converting it. Why is starch the better store for "
                "the plant itself?",
        "options": [
            {"text": "Because the iodine would break the glucose down before "
                     "it could ever be used.",
             "correct": False,
             "why": "Iodine is something the student adds at the end, not "
                    "something in the leaf. The plant's own reason is about "
                    "water and space."},
            {"text": "Because glucose is soluble, and a cell full of "
                     "dissolved sugar would pull water in and swell hard "
                     "against its wall.",
             "correct": True},
            {"text": "Because glucose cannot be broken back down once a plant "
                     "has made it.",
             "correct": False,
             "why": "Glucose is exactly what a cell breaks down for energy. "
                    "It is starch that gets broken back down into glucose "
                    "when the plant needs it."},
            {"text": "Because starch holds far more energy per gram than "
                     "glucose does, so a leaf can store a whole day's "
                     "production in less space.",
             "correct": False,
             "why": "Starch is many glucose molecules joined together, so the "
                    "energy per gram is much the same. Its advantage is being "
                    "insoluble."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h09",
        "band": "harder",
        "text": "A tube of ethanol tips over into the hot water bath and "
                "spills across the bench. What is the hazard, and what would "
                "make it far worse?",
        "options": [
            {"text": "The ethanol will burn the bench top, and pouring water "
                     "on it would spread the damage.",
             "correct": False,
             "why": "Ethanol does not attack a bench. The hazard is the "
                    "flammable vapour rising off the spill."},
            {"text": "The ethanol will dissolve the chlorophyll on the bench, "
                     "and iodine would stain what is left.",
             "correct": False,
             "why": "Neither of those is a hazard to a person. What matters "
                    "is the vapour coming off the spill, and whether it finds "
                    "a flame."},
            {"text": "Warm ethanol gives off flammable vapour that spreads "
                     "along the bench, and any lit Bunsen in the room could "
                     "set it alight.",
             "correct": True},
            {"text": "The ethanol will boil away harmlessly, and only a "
                     "stopper in the tube could have prevented the spill in "
                     "the first place.",
             "correct": False,
             "why": "It does evaporate, and that is the problem rather than "
                    "the cure — the vapour is what catches fire. Never "
                    "stopper a tube you are heating."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h10",
        "band": "harder",
        "text": "One class skips the boiling water and gets a different "
                "blotchy pattern every time. Another skips the destarching "
                "and gets the same strong blue-black every time. Which fault "
                "is which?",
        "options": [
            {"text": "Skipping the boiling makes the result unreliable; "
                     "skipping the destarching makes a repeatable result that "
                     "still proves nothing.",
             "correct": True},
            {"text": "Both faults make the result unreliable, since neither "
                     "class can repeat what it saw.",
             "correct": False,
             "why": "The undestarched class repeats its result exactly. "
                    "Repeatable and useless are not the same thing, which is "
                    "the whole point."},
            {"text": "Skipping the destarching makes the result unreliable; "
                     "skipping the boiling makes it repeatable but useless.",
             "correct": False,
             "why": "That is the two swapped over. Live waxy cells let iodine "
                    "in unevenly, so that is what varies; old starch gives "
                    "the same strong reading every time."},
            {"text": "Neither is a fault, since both classes came away with a "
                     "result they could write down.",
             "correct": False,
             "why": "Writing a result down is not the test of it. One class "
                    "cannot trust what it saw, and the other cannot say when "
                    "the starch was made."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h11",
        "band": "harder",
        "text": "A class uses a variegated plant to show that chlorophyll is "
                "needed, but on their plant the white tissue is a narrow band "
                "at the very edge of each leaf, where the leaves are thin and "
                "often torn. Why might a critic not accept the result?",
        "options": [
            {"text": "Because a variegated leaf cannot photosynthesise "
                     "anywhere, so nothing at all would go blue-black.",
             "correct": False,
             "why": "The green parts photosynthesise perfectly well and do go "
                    "blue-black. The criticism is about what else differs at "
                    "the edge."},
            {"text": "Because white tissue has no cells in it at all, so "
                     "there is nothing there to test.",
             "correct": False,
             "why": "White tissue is made of ordinary cells; what they lack "
                    "is chlorophyll. The problem is that the edge differs in "
                    "other ways too."},
            {"text": "Because iodine behaves differently on white tissue than "
                     "it does on green.",
             "correct": False,
             "why": "Iodine behaves identically wherever it is put. What "
                    "weakens this design is that the edge is not otherwise "
                    "identical to the middle."},
            {"text": "Because the edge differs from the middle in more than "
                     "chlorophyll, so chlorophyll is not the only variable.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h12",
        "band": "harder",
        "text": "A student wants to test a plant whose leaves are deep red "
                "rather than green. Will the starch test work on it?",
        "options": [
            {"text": "No, because a red leaf has no chlorophyll and so makes "
                     "no starch at all.",
             "correct": False,
             "why": "A red leaf has chlorophyll underneath the red pigment "
                    "and photosynthesises normally. The pigments come out "
                    "together in the ethanol."},
            {"text": "Yes, because the pigments dissolve out in the ethanol "
                     "and the leaf is pale before the iodine arrives.",
             "correct": True},
            {"text": "Yes, but only with twice as long in the ethanol, since "
                     "red is harder to see through.",
             "correct": False,
             "why": "The method does not change for a red leaf. What matters "
                    "is that the ethanol removes the pigment, whatever colour "
                    "it was."},
            {"text": "No, because red is the colour of a positive result and "
                     "the two could not be told apart.",
             "correct": False,
             "why": "A positive result is blue-black rather than red — and in "
                    "any case the leaf's own colour has gone before the "
                    "iodine goes on."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h13",
        "band": "harder",
        "text": "Each leaf of a plant is holding about 24 mg of starch, and "
                "in the dark a leaf uses up about 12 mg of it a day. How long "
                "must the plant stay in the dark, and does that agree with "
                "the usual instruction?",
        "options": [
            {"text": "About half a day, since 12 is half of 24 — so two days "
                     "is far longer than is needed.",
             "correct": False,
             "why": "You have divided the wrong way round. A 24 mg store used "
                    "at 12 mg a day lasts two days, not half of one."},
            {"text": "About twelve days, since a leaf uses 1 mg a day for "
                     "each of its 12 mg.",
             "correct": False,
             "why": "The rate you are given is 12 mg a day, not 1 mg. "
                    "Twenty-four milligrams at 12 mg a day is two days."},
            {"text": "About two days, since 24 mg divided by 12 mg a day is "
                     "2 days — which is what the method says.",
             "correct": True},
            {"text": "About 288 days, since 24 multiplied by 12 gives the "
                     "time it takes.",
             "correct": False,
             "why": "Multiplying a store by a rate gives no time at all. To "
                    "find how long a store lasts, divide the store by the "
                    "rate it is used at."},
        ],
        "figure": None,
    },
]
