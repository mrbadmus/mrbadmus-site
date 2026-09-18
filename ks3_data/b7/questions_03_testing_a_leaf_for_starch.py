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
            {"text": "A soluble sugar the plant makes inside its leaves and "
                     "then moves out to the rest of the growing plant.",
             "correct": False,
             "why": "That is glucose. Starch is what a leaf turns glucose "
                    "into, and being insoluble it stays exactly where it was "
                    "made."},
            {"text": "The green pigment inside a leaf's cells that it must "
                     "have before it can make any food.",
             "correct": False,
             "why": "That is chlorophyll, and it is dissolved out into the "
                    "ethanol before the iodine goes on. Starch is the store "
                    "you are testing for."},
            {"text": "A mineral a plant takes up from the soil into its "
                     "leaves.",
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
                     "to get while it is standing in the hot water bath.",
             "correct": False,
             "why": "That is the water bath, and it is a safety measure. A "
                    "control is the part of an investigation everything else "
                    "is compared against."},
            {"text": "The person in the group who decides which of the steps "
                     "the class will leave out.",
             "correct": False,
             "why": "A control is not a person. It is the part of the "
                    "investigation that everything else is compared with."},
            {"text": "The amount of iodine dropped on the leaf, kept the "
                     "same every time so the test is fair.",
             "correct": False,
             "why": "Keeping a quantity the same is a different idea. The "
                    "control is the thing your result is compared against."},
            {"text": "The part of the investigation everything else is "
                     "compared against.",
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
            {"text": "Keeping that half of the leaf warm under the metal, so "
                     "that temperature can be compared across the two "
                     "halves.",
             "correct": False,
             "why": "Both halves are on one leaf and share a temperature. The "
                    "foil is blocking light, which is the one thing being "
                    "changed."},
            {"text": "Stopping the iodine from reaching that half of the "
                     "leaf when the test is carried out at the end.",
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
                     "up the stem into the leaf in the water it drinks.",
             "correct": False,
             "why": "Nothing takes starch up from the soil. The leaf built "
                    "glucose from carbon dioxide and water, then converted it "
                    "into starch."},
            {"text": "From the iodine, which leaves starch behind wherever it "
                     "soaks in.",
             "correct": False,
             "why": "Iodine is a test and adds nothing to the leaf. It "
                    "reports the starch that was already there."},
            {"text": "From the store the plant was already holding in its "
                     "leaves before the experiment began.",
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
            {"text": "Skipping the ethanol gives you a result you cannot "
                     "use, while skipping the destarching gives no reading "
                     "at all.",
             "correct": False,
             "why": "It is the other way round. A green leaf hides the colour "
                    "completely, while an undestarched leaf gives a strong "
                    "blue-black nobody can date."},
            {"text": "Skipping the destarching gives an undatable result; "
                     "skipping the ethanol gives none.",
             "correct": True},
            {"text": "Both give no reading, since neither leaf can take up "
                     "the iodine.",
             "correct": False,
             "why": "The undestarched leaf takes up iodine perfectly well and "
                    "goes blue-black. Its problem is that you cannot say when "
                    "the starch was made."},
            {"text": "Both give readable results, and the only difference "
                     "between them is how strong the colour turns out.",
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
                     "skipping the destarching makes it undatable.",
             "correct": True},
            {"text": "Both faults make the result unreliable, since neither "
                     "class could repeat exactly what it saw the first time.",
             "correct": False,
             "why": "The undestarched class repeats its result exactly. "
                    "Repeatable and useless are not the same thing, which is "
                    "the whole point."},
            {"text": "Skipping the destarching makes the result unreliable; "
                     "skipping the boiling makes it repeatable but useless "
                     "as evidence.",
             "correct": False,
             "why": "That is the two swapped over. Live waxy cells let iodine "
                    "in unevenly, so that is what varies; old starch gives "
                    "the same strong reading every time."},
            {"text": "Neither is a fault, since both classes came away with "
                     "a result to write down.",
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
                     "anywhere on it, so nothing at all would go blue-black.",
             "correct": False,
             "why": "The green parts photosynthesise perfectly well and do go "
                    "blue-black. The criticism is about what else differs at "
                    "the edge."},
            {"text": "Because white tissue has no cells in it at all, so "
                     "there is nothing there for iodine to test.",
             "correct": False,
             "why": "White tissue is made of ordinary cells; what they lack "
                    "is chlorophyll. The problem is that the edge differs in "
                    "other ways too."},
            {"text": "Because iodine behaves differently on white tissue "
                     "than on green.",
             "correct": False,
             "why": "Iodine behaves identically wherever it is put. What "
                    "weakens this design is that the edge is not otherwise "
                    "identical to the middle."},
            {"text": "Because the edge differs from the middle in more than "
                     "just its chlorophyll.",
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
                     "no starch.",
             "correct": False,
             "why": "A red leaf has chlorophyll underneath the red pigment "
                    "and photosynthesises normally. The pigments come out "
                    "together in the ethanol."},
            {"text": "Yes, because the ethanol dissolves the pigments out "
                     "and leaves the leaf pale.",
             "correct": True},
            {"text": "Yes, but only with twice as long in the ethanol, since "
                     "red is harder to see through than green.",
             "correct": False,
             "why": "The method does not change for a red leaf. What matters "
                    "is that the ethanol removes the pigment, whatever colour "
                    "it was."},
            {"text": "No, because red is the colour of a positive result, "
                     "and the two colours could not be told apart at the "
                     "end.",
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
            {"text": "About half a day, since 12 mg is half of 24 mg, so the "
                     "usual two days in the dark is far longer than is "
                     "needed.",
             "correct": False,
             "why": "You have divided the wrong way round. A 24 mg store used "
                    "at 12 mg a day lasts two days, not half of one."},
            {"text": "About twelve days, since a leaf uses up 1 mg of starch "
                     "a day for each of the 12 mg in the rate.",
             "correct": False,
             "why": "The rate you are given is 12 mg a day, not 1 mg. "
                    "Twenty-four milligrams at 12 mg a day is two days."},
            {"text": "About two days, since 24 mg divided by 12 mg a day is "
                     "2 days — as the method says.",
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

    # ── MRB-338 night-3 expansion ────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b7-03-e14",
        "band": "easier",
        "text": "The minute the leaf spends in boiling water does more than "
                "kill the cells and open them up. What else does it do to the "
                "leaf?",
        "options": [
            {"text": "It also dissolves the chlorophyll, the same job "
                     "ethanol does later.",
             "correct": False,
             "why": "Water will not shift chlorophyll — that is the ethanol's "
                    "job later on, not the boiling water's."},
            {"text": "It also softens the leaf's waxy surface, on top of "
                     "killing the cells.",
             "correct": True},
            {"text": "It also dissolves the starch, so it spreads evenly "
                     "through the leaf.",
             "correct": False,
             "why": "Starch is insoluble and stays exactly where it was "
                    "made — boiling water cannot move it."},
            {"text": "It also stops the leaf losing any more water for the "
                     "rest of the test.",
             "correct": False,
             "why": "Nothing about this method controls water loss; the "
                    "boiling is about killing cells and softening the "
                    "surface."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e15",
        "band": "easier",
        "text": "In this practical, what is meant by a 'water bath'?",
        "options": [
            {"text": "A sink of cold water the used tubes are washed in "
                     "afterwards.",
             "correct": False,
             "why": "Cleaning up afterwards is not what a water bath is "
                    "for — it is part of running the method itself."},
            {"text": "A beaker the leaf itself sits in while it is being "
                     "tested.",
             "correct": False,
             "why": "The leaf is tested on a white tile, not in a beaker. "
                    "A water bath holds the tube of ethanol."},
            {"text": "A container of hot water that a tube stands in, so "
                     "it is heated without a flame.",
             "correct": True},
            {"text": "A carefully measured amount of extra water stirred "
                     "into the ethanol to dilute its concentration before "
                     "use.",
             "correct": False,
             "why": "Nothing is diluted. The ethanol is used as it is; the "
                    "water is only what it stands in to be heated."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e16",
        "band": "easier",
        "text": "About how long does the leaf spend in the hot-water dip "
                "before it is spread on the tile?",
        "options": [
            {"text": "About two days.",
             "correct": False,
             "why": "Two days is how long destarching takes, not this "
                    "brief dip in hot water."},
            {"text": "About an hour.",
             "correct": False,
             "why": "An hour is far longer than this quick dip is ever "
                    "left for."},
            {"text": "About a minute.",
             "correct": False,
             "why": "About a minute is how long the earlier boil in plain "
                    "water takes, not this final dip."},
            {"text": "A few seconds.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e17",
        "band": "easier",
        "text": "While the leaf sits in the hot ethanol, what happens to "
                "the ethanol itself?",
        "options": [
            {"text": "It turns green, as the chlorophyll dissolves out of "
                     "the leaf into it.",
             "correct": True},
            {"text": "It turns blue-black, as it reacts with the starch "
                     "in the leaf.",
             "correct": False,
             "why": "Blue-black only ever appears once iodine meets "
                    "starch, and no iodine is present at this stage."},
            {"text": "It turns orange-brown, the same colour iodine goes "
                     "without starch.",
             "correct": False,
             "why": "Nothing here involves iodine yet — that colour has "
                    "nothing to do with the ethanol stage."},
            {"text": "It stays completely colourless throughout.",
             "correct": False,
             "why": "The chlorophyll leaving the leaf gives the ethanol "
                    "its own colour; it does not stay colourless."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e18",
        "band": "easier",
        "text": "What does iodine solution test for, in this practical?",
        "options": [
            {"text": "Any sugar dissolved in the leaf's cells.",
             "correct": False,
             "why": "Iodine says nothing about sugar; that question is "
                    "Benedict's job, not iodine's."},
            {"text": "Starch, and starch alone.",
             "correct": True},
            {"text": "Whether the leaf still has its chlorophyll.",
             "correct": False,
             "why": "Iodine has no reaction with chlorophyll, present or "
                    "absent — it answers one question only."},
            {"text": "How much water is left in the leaf.",
             "correct": False,
             "why": "Iodine tests for one substance, and it is not water."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e19",
        "band": "easier",
        "text": "In the order the method is carried out, which comes "
                "first: destarching the plant, or boiling the leaf in "
                "water?",
        "options": [
            {"text": "Boiling in water, since the leaf must be killed "
                     "before it is picked.",
             "correct": False,
             "why": "The plant is destarched for two whole days before "
                    "the leaf is ever picked."},
            {"text": "Neither — both happen on the same morning, one "
                     "after the other.",
             "correct": False,
             "why": "Destarching takes two days and finishes long before "
                    "the boiling-water stage begins."},
            {"text": "Destarching, which finishes days before the leaf is "
                     "even picked.",
             "correct": True},
            {"text": "It makes no difference which comes first.",
             "correct": False,
             "why": "Doing it the wrong way round would mean testing a "
                    "leaf that still holds old starch."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e20",
        "band": "easier",
        "text": "Besides the fire risk from ethanol, what other hazard "
                "does this practical carry?",
        "options": [
            {"text": "The white tile can crack under hot apparatus.",
             "correct": False,
             "why": "A tile cracking is not a hazard the safety note "
                    "names — iodine itself is the other named hazard."},
            {"text": "The boiling water can dissolve through glass "
                     "tubing.",
             "correct": False,
             "why": "Boiling water does not dissolve glass; that is not "
                    "a real hazard of this practical."},
            {"text": "The leaf itself can release a harmful gas as it is "
                     "boiled.",
             "correct": False,
             "why": "A boiled leaf releases nothing harmful; the named "
                    "hazard beyond fire is the iodine solution."},
            {"text": "Iodine solution stains and irritates skin and eyes.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e21",
        "band": "easier",
        "text": "This practical uses boiling water and hot apparatus as well "
                "as flammable ethanol. What safety measures does that call "
                "for?",
        "options": [
            {"text": "Eye protection, and a teacher present.",
             "correct": True},
            {"text": "Gloves, since the water is treated as the sole "
                     "hazard.",
             "correct": False,
             "why": "Eye protection and a teacher present are what is called "
                    "for, not just gloves."},
            {"text": "Nothing extra, since water is not the flammable "
                     "substance in the room.",
             "correct": False,
             "why": "Hot apparatus and boiling water carry their own "
                    "risk, named separately from the ethanol."},
            {"text": "A fire extinguisher kept open on the bench "
                     "throughout.",
             "correct": False,
             "why": "What is called for is eye protection and a teacher "
                    "present, not equipment kept open on the bench."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e22",
        "band": "easier",
        "text": "A patch of the tested leaf stays orange-brown after the "
                "iodine is added. What does that patch contain?",
        "options": [
            {"text": "A small amount of starch, too little to show "
                     "blue-black.",
             "correct": False,
             "why": "Orange-brown is iodine's own unreacted colour — any "
                    "starch present would have turned it blue-black."},
            {"text": "No starch, in that part of the leaf.",
             "correct": True},
            {"text": "Chlorophyll that the ethanol failed to remove.",
             "correct": False,
             "why": "Chlorophyll has nothing to do with the iodine colour "
                    "change either way."},
            {"text": "Sugar rather than starch, which iodine cannot "
                     "detect.",
             "correct": False,
             "why": "Iodine is silent about sugar, but that is not why "
                    "this patch stays orange-brown — it simply has no "
                    "starch."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e23",
        "band": "easier",
        "text": "A plant goes into the dark cupboard at 9 am on Monday for "
                "its two days of destarching. At what point is it ready "
                "to come out?",
        "options": [
            {"text": "9 am on Tuesday.",
             "correct": False,
             "why": "That is only one day, half of the two needed."},
            {"text": "9 pm on Tuesday.",
             "correct": False,
             "why": "That is one and a half days, still short of the two "
                    "full days needed."},
            {"text": "9 am on Wednesday.",
             "correct": True},
            {"text": "9 am on Thursday.",
             "correct": False,
             "why": "That is three days, a day longer than the method "
                    "calls for."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e24",
        "band": "easier",
        "text": "A tube of ethanol is standing in its water bath. Why "
                "should it never be sealed with a bung while it heats?",
        "options": [
            {"text": "Because a bung would let the ethanol boil too "
                     "quickly.",
             "correct": False,
             "why": "Nothing about a bung speeds up boiling; the risk is "
                    "about pressure, not speed."},
            {"text": "Because a sealed tube would stop the chlorophyll "
                     "dissolving out.",
             "correct": False,
             "why": "A bung has no effect on how chlorophyll dissolves "
                    "into the ethanol."},
            {"text": "Because iodine cannot be added through a sealed "
                     "tube later.",
             "correct": False,
             "why": "The tube is unsealed and the leaf removed long "
                    "before iodine is ever added."},
            {"text": "Because the pressure inside a heated, sealed tube "
                     "has nowhere to go.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e25",
        "band": "easier",
        "text": "A drop of iodine is put onto a slice of white bread. "
                "What happens, and why?",
        "options": [
            {"text": "It turns blue-black, since bread contains starch "
                     "even though it was never green.",
             "correct": True},
            {"text": "Nothing happens, since bread has no chlorophyll to "
                     "react with.",
             "correct": False,
             "why": "Chlorophyll plays no part in the colour change — "
                    "iodine responds to starch, and bread has plenty."},
            {"text": "It turns orange-brown, since bread has no starch in "
                     "it at all.",
             "correct": False,
             "why": "Bread is full of starch, which is exactly why it "
                    "turns blue-black rather than staying orange-brown."},
            {"text": "It turns brick red, since that is the colour any "
                     "starchy food is supposed to give when iodine "
                     "reacts with it.",
             "correct": False,
             "why": "Brick red is Benedict's answer about sugar; "
                    "iodine's positive colour is blue-black."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e26",
        "band": "easier",
        "text": "After the ethanol step the ethanol in the tube is bright "
                "green. Iodine is added to the leaf and never to that "
                "ethanol. Why would testing the ethanol be no use?",
        "options": [
            {"text": "The ethanol would break the iodine down before it had "
                     "any chance to react with anything in the tube.",
             "correct": False,
             "why": "Ethanol does not break iodine down. The reason is that "
                    "the starch never left the leaf in the first place."},
            {"text": "Starch is insoluble, so none of it ever left the leaf "
                     "and passed into the ethanol.",
             "correct": True},
            {"text": "The ethanol is still far too hot for iodine to give any "
                     "colour change at all while it is in there.",
             "correct": False,
             "why": "Iodine reacts with starch at any temperature reached "
                    "here. The point is that there is no starch in the "
                    "ethanol for it to find."},
            {"text": "The chlorophyll now in the ethanol would turn the "
                     "iodine blue-black and give a false positive.",
             "correct": False,
             "why": "Chlorophyll gives no reaction with iodine at all. The "
                    "ethanol holds chlorophyll and no starch, so there is "
                    "nothing there to find."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e27",
        "band": "easier",
        "text": "The full method is carried out correctly on a leaf with "
                "foil over one half, after a day in bright light. What "
                "does the tile show?",
        "options": [
            {"text": "Orange-brown everywhere, since a healthy leaf holds "
                     "no starch until it is tested.",
             "correct": False,
             "why": "A leaf given light after destarching makes starch "
                    "wherever it was exposed to that light."},
            {"text": "Blue-black everywhere, foil included, since starch "
                     "spreads through the whole leaf.",
             "correct": False,
             "why": "Starch does not spread — it stays where light let "
                    "it be made, which is why the foil half differs."},
            {"text": "Blue-black in the exposed half and orange-brown "
                     "under the foil.",
             "correct": True},
            {"text": "Orange-brown in the exposed half and blue-black "
                     "under the foil.",
             "correct": False,
             "why": "That is the pattern reversed — light is what allows "
                    "starch to be made, not the foil."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e28",
        "band": "easier",
        "text": "In plain terms, what is this whole investigation trying "
                "to find out?",
        "options": [
            {"text": "Whether a leaf needs carbon dioxide to survive.",
             "correct": False,
             "why": "Carbon dioxide is not what this particular "
                    "investigation is varying."},
            {"text": "Whether iodine reacts with chlorophyll.",
             "correct": False,
             "why": "That belief is what the lesson corrects, not what "
                    "the investigation sets out to test."},
            {"text": "How long it takes a plant to destarch fully.",
             "correct": False,
             "why": "Destarching is preparation for the test, not the "
                    "question the test itself is answering."},
            {"text": "Whether light is needed for a leaf to make starch.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e29",
        "band": "easier",
        "text": "What colour is iodine solution itself, before it ever "
                "touches a leaf?",
        "options": [
            {"text": "Orange-brown.",
             "correct": True},
            {"text": "Blue-black.",
             "correct": False,
             "why": "Blue-black only appears once iodine meets starch — "
                    "it is not the reagent's own colour."},
            {"text": "Colourless.",
             "correct": False,
             "why": "Iodine solution has its own visible colour even "
                    "before it meets anything."},
            {"text": "Bright green.",
             "correct": False,
             "why": "Green is the leaf's own colour before the ethanol "
                    "removes it, not iodine's colour."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-e30",
        "band": "easier",
        "text": "Someone argues a naked flame under ethanol would be fine "
                "for a few seconds, since it hasn't reached 78 °C yet. "
                "Why is that argument wrong?",
        "options": [
            {"text": "Because ethanol only becomes flammable once it "
                     "starts to boil.",
             "correct": False,
             "why": "That is exactly the wrong belief — the vapour is "
                    "the hazard, and it forms well before boiling."},
            {"text": "Because ethanol gives off flammable vapour long "
                     "before it reaches its boiling point.",
             "correct": True},
            {"text": "Because a Bunsen flame cannot realistically be "
                     "turned down low enough to burn safely for a few "
                     "brief seconds.",
             "correct": False,
             "why": "The length of exposure is not the issue here — the "
                    "vapour is dangerous from the moment it forms."},
            {"text": "Because the boiling point of ethanol is not really "
                     "78 °C.",
             "correct": False,
             "why": "78 °C is genuinely where ethanol boils — the "
                    "problem is the vapour given off well before that "
                    "point."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b7-03-s14",
        "band": "standard",
        "text": "Destarching, boiling in water, and the hot-water dip "
                "before spreading all take different amounts of time. "
                "Put them in order from shortest to longest, and say "
                "what that tells you.",
        "options": [
            {"text": "Boiling in water, then the hot-water dip, then "
                     "destarching — treating the two heating steps as "
                     "similar in length just because both take under a "
                     "minute each.",
             "correct": False,
             "why": "The hot-water dip is a few seconds, shorter than "
                    "the full minute of boiling — this order swaps "
                    "those two."},
            {"text": "Destarching, then boiling in water, then the "
                     "hot-water dip — the two-day step is really the "
                     "shortest.",
             "correct": False,
             "why": "Destarching is the longest step by a wide margin, "
                    "not the shortest — two days dwarfs a minute or a "
                    "few seconds."},
            {"text": "The hot-water dip, then boiling in water, then "
                     "destarching — most of the method's time goes on "
                     "one preparation step, not on the test itself.",
             "correct": True},
            {"text": "All three take roughly the same time, since each "
                     "is described as 'a few' units.",
             "correct": False,
             "why": "Two days, about a minute and a few seconds are "
                    "three very different lengths of time, not similar "
                    "ones."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s15",
        "band": "standard",
        "text": "A student boils a leaf in ethanol before boiling it in "
                "water, reversing the usual order. The leaf comes out "
                "pale as expected. What has gone wrong?",
        "options": [
            {"text": "Nothing — the leaf is pale either way, so the "
                     "order made no difference.",
             "correct": False,
             "why": "Being pale is not the same as being ready to test; "
                    "the cells still need killing and opening up first."},
            {"text": "The starch has been dissolved out of the leaf's "
                     "cells along with the chlorophyll, since the "
                     "ethanol step happened first, before the water.",
             "correct": False,
             "why": "Ethanol dissolves chlorophyll, not starch, "
                    "whichever order the two steps are done in."},
            {"text": "The ethanol has evaporated away completely before "
                     "the water step even began, wasting all of it "
                     "needlessly.",
             "correct": False,
             "why": "Nothing about the order causes the ethanol itself "
                    "to be lost."},
            {"text": "The leaf's cells were never killed and opened up "
                     "by boiling water before the ethanol reached them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s16",
        "band": "standard",
        "text": "A student wipes a stray drop of iodine off their hand with a "
                "paper towel and carries on without telling anyone. Why does "
                "that matter?",
        "options": [
            {"text": "Because iodine solution stains and irritates skin "
                     "and eyes, and ought to be reported and washed off "
                     "properly.",
             "correct": True},
            {"text": "Because iodine reacts with skin to produce a "
                     "flammable gas.",
             "correct": False,
             "why": "The hazard from iodine is that it stains and "
                    "irritates, not that it reacts to release a gas."},
            {"text": "Because a stray drop of iodine left on a hand can "
                     "later be transferred onto the test leaf and set "
                     "off a false positive result.",
             "correct": False,
             "why": "Iodine on a hand has no effect on a separate leaf's "
                    "own result."},
            {"text": "Because the whole bottle of iodine solution needs "
                     "replacing straight away once even a single drop "
                     "of it has been spilled on someone's hand.",
             "correct": False,
             "why": "A spilled drop says nothing about the state of the "
                    "rest of the bottle."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s17",
        "band": "standard",
        "text": "Two students test leaves picked from the same destarched "
                "plant after the same day of light. One tile comes out "
                "strongly blue-black, the other only weakly. Give the most "
                "likely explanation that does not involve a mistake in the "
                "method.",
        "options": [
            {"text": "Iodine reacts more strongly with a younger leaf, and "
                     "the two students will have picked leaves of different "
                     "ages.",
             "correct": False,
             "why": "A leaf's age does not change how iodine reacts with "
                    "starch. What differs between two leaves on one plant is "
                    "how much light each of them caught."},
            {"text": "The two leaves were not equally lit — one spent part of "
                     "the day in the shade of the leaves above it.",
             "correct": True},
            {"text": "A plant makes starch in only some of its leaves, and "
                     "stores none at all in the rest of them.",
             "correct": False,
             "why": "Every green leaf on a lit plant makes and stores starch. "
                    "The difference between two of them is how much light "
                    "each one received."},
            {"text": "One leaf will have kept more of its chlorophyll, and "
                     "the green adds to the depth of the blue-black.",
             "correct": False,
             "why": "The ethanol removes the chlorophyll from both leaves "
                    "before any iodine is added, so none is left to affect "
                    "the colour."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s18",
        "band": "standard",
        "text": "A teacher swaps the white tile for a black one by "
                "mistake. What is lost, if anything?",
        "options": [
            {"text": "Nothing — the chemical reaction that turns the "
                     "leaf blue-black does not depend in any way on "
                     "what colour the tile underneath happens to be.",
             "correct": False,
             "why": "The chemistry is unaffected, but reading the "
                    "outcome depends on being able to see it, which the "
                    "tile's colour decides."},
            {"text": "The test fails completely, since black tiles react "
                     "with iodine.",
             "correct": False,
             "why": "Tiles are inert; nothing about a tile's colour "
                    "reacts with iodine."},
            {"text": "Blue-black would be very hard to see against "
                     "black, even though the leaf still changed colour "
                     "underneath.",
             "correct": True},
            {"text": "Orange-brown would show up far more clearly "
                     "against black than it does against the plain "
                     "white tile.",
             "correct": False,
             "why": "Orange-brown is close to iodine's own shade and is "
                    "easiest to read against a plain, contrasting "
                    "background such as white."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s19",
        "band": "standard",
        "text": "A tube of ethanol is stood in water that has gone cold "
                "rather than staying hot. After the usual time, the "
                "leaf is still faintly green. What has this cost the "
                "result?",
        "options": [
            {"text": "Nothing — a faintly green leaf still shows "
                     "blue-black clearly against it.",
             "correct": False,
             "why": "Any green left behind makes a colour change harder "
                    "to see, which is exactly the problem ethanol exists "
                    "to remove."},
            {"text": "The starch, which would have dissolved into the "
                     "cold ethanol instead of the warm.",
             "correct": False,
             "why": "Starch is insoluble in ethanol whatever its "
                    "temperature; nothing here has removed it."},
            {"text": "The safety of the practical, since cold ethanol is "
                     "more flammable than hot.",
             "correct": False,
             "why": "Temperature does not change whether ethanol's "
                    "vapour is flammable; the hazard is present either "
                    "way."},
            {"text": "Some of the colour change, since the remaining "
                     "green makes a positive harder to read.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s20",
        "band": "standard",
        "text": "Compare two mistakes: heating ethanol over a naked "
                "flame, and standing it in a water bath that has gone "
                "lukewarm. Which is worse, and why?",
        "options": [
            {"text": "The naked flame, because it can end the practical "
                     "outright rather than just weakening a reading.",
             "correct": True},
            {"text": "The lukewarm bath, because ending up with a weak, "
                     "hard-to-read result is worse than any risk a "
                     "water bath could pose.",
             "correct": False,
             "why": "A reading that is merely weaker can often still be "
                    "worked with; a fire cannot."},
            {"text": "Neither — both stop the leaf reaching a usable "
                     "result in exactly the same way.",
             "correct": False,
             "why": "A lukewarm bath at worst slows chlorophyll removal; "
                    "a naked flame is a genuine fire hazard."},
            {"text": "They are equally serious, since both involve "
                     "heating ethanol.",
             "correct": False,
             "why": "Heating ethanol is common to both, but only one of "
                    "the two methods is a fire hazard."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s21",
        "band": "standard",
        "text": "A student who cannot find a dark cupboard puts the plant "
                "inside a cardboard box with the lid taped down, and leaves "
                "the box in a bright classroom for two days. Is that an "
                "acceptable substitute?",
        "options": [
            {"text": "No — a plant shut in a box would run out of the carbon "
                     "dioxide it needs to empty its starch store.",
             "correct": False,
             "why": "Emptying a starch store is respiration, which uses "
                    "oxygen rather than carbon dioxide, and a taped cardboard "
                    "box is nowhere near airtight anyway."},
            {"text": "Yes — all that matters is that no light reaches the "
                     "plant, which a taped box does.",
             "correct": True},
            {"text": "No — a plant needs some light in order to use up the "
                     "starch it is holding in its leaves.",
             "correct": False,
             "why": "Light is what lets a plant make starch, not use it up. "
                    "The store is emptied in the dark, which is the whole "
                    "reason for the two days."},
            {"text": "No — only a cupboard is properly dark, and cardboard "
                     "lets far too much light through to work.",
             "correct": False,
             "why": "Cardboard with the lid taped down blocks light perfectly "
                    "well. It is darkness the method needs, not a particular "
                    "cupboard."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s22",
        "band": "standard",
        "text": "Instead of a dark cupboard, a plant is left in a dim "
                "corner of the classroom for its two 'destarching' "
                "days. What is the likely result of testing it "
                "afterwards?",
        "options": [
            {"text": "A clean, fully readable result, since dim light is "
                     "effectively the same as darkness.",
             "correct": False,
             "why": "Any light lets some photosynthesis continue, so dim "
                    "is not the same as dark for this purpose."},
            {"text": "No colour change anywhere on the leaf, since dim "
                     "light in a corner stops photosynthesis from "
                     "happening completely.",
             "correct": False,
             "why": "Dim light still allows some photosynthesis; it does "
                    "not switch it off."},
            {"text": "Some starch left over, because a little "
                     "photosynthesis in dim light keeps replacing what "
                     "is respired away.",
             "correct": True},
            {"text": "The leaf will not take up any of the iodine "
                     "afterwards, since it was never kept in full, "
                     "uninterrupted darkness.",
             "correct": False,
             "why": "Whether the leaf takes up iodine depends on the "
                    "boiling and ethanol steps, not on how dark the "
                    "cupboard was."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s23",
        "band": "standard",
        "text": "A student destarches a plant properly, puts it in "
                "bright light for a day, and only then tapes foil over "
                "half of one leaf just before testing. What will the "
                "foil half show?",
        "options": [
            {"text": "Orange-brown, since taping the foil on afterwards "
                     "has now blocked any further light reaching that "
                     "particular half of the leaf.",
             "correct": False,
             "why": "The light exposure already happened before the "
                    "foil went on — blocking it afterwards changes "
                    "nothing about the starch already made."},
            {"text": "A fainter blue-black than the exposed half, since "
                     "some light still got through beforehand.",
             "correct": False,
             "why": "Both halves had the identical whole day of light "
                    "before the foil was ever added, so there is no "
                    "reason for one half to be fainter."},
            {"text": "No result whatsoever, since the foil stops the "
                     "iodine reaching that half.",
             "correct": False,
             "why": "The foil comes off well before the iodine stage; it "
                    "cannot affect the test itself."},
            {"text": "Blue-black, the same as the exposed half, since "
                     "both halves had the same light before the foil "
                     "went on.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s24",
        "band": "standard",
        "text": "Instead of covering half of one leaf, a student "
                "compares a lit plant with an unlit plant of a "
                "different species. Why is that comparison weaker than "
                "the foil method?",
        "options": [
            {"text": "The two plants might differ in more than just "
                     "their light — species, age or size could all vary "
                     "too.",
             "correct": True},
            {"text": "Different plant species cannot ever be compared "
                     "fairly using the iodine starch test, whatever "
                     "precautions are taken.",
             "correct": False,
             "why": "Iodine's starch test works on leaves from any "
                    "species; that is not the issue here."},
            {"text": "A second plant grown separately would need roughly "
                     "twice as much iodine solution to test it properly "
                     "in the end.",
             "correct": False,
             "why": "The amount of iodine used has nothing to do with "
                    "how convincing the comparison is."},
            {"text": "A single leaf takes far longer to destarch "
                     "properly than a whole plant does.",
             "correct": False,
             "why": "A whole plant of any species can be destarched — "
                    "the problem is what else differs between two "
                    "different plants."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s25",
        "band": "standard",
        "text": "A student wants to skip picking the leaf and instead "
                "drip iodine directly onto a leaf still growing on the "
                "plant. Why won't that work as well as the usual "
                "method?",
        "options": [
            {"text": "A growing leaf has too little starch in it to "
                     "ever show a result.",
             "correct": False,
             "why": "A leaf on a lit, destarched plant can hold plenty "
                    "of starch — the amount is not the problem here."},
            {"text": "The leaf was never boiled or decolourised, so it "
                     "is still green, waxy and alive, and any colour "
                     "change would be hard to see or reach.",
             "correct": True},
            {"text": "Iodine only begins to work on a leaf's starch "
                     "once that leaf has been separated from its "
                     "parent plant for at least a full day.",
             "correct": False,
             "why": "Iodine's reaction with starch has nothing to do "
                    "with how long a leaf has been picked."},
            {"text": "The plant would be damaged and unable to "
                     "photosynthesise again.",
             "correct": False,
             "why": "A drop of iodine on one leaf does not stop the rest "
                    "of the plant photosynthesising."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s26",
        "band": "standard",
        "text": "A properly destarched plant is given a full day of bright "
                "light, tested correctly, and both halves stay orange-brown. "
                "A second, identical leaf from the same plant, tested with a "
                "fresh bottle of iodine, gives the usual clear two-tone "
                "result. What does the first result suggest?",
        "options": [
            {"text": "That light was not actually needed for this plant "
                     "to make starch.",
             "correct": False,
             "why": "The second leaf, tested properly, did show starch "
                    "where light fell — this plant does need light."},
            {"text": "That the plant had not really been destarched, "
                     "despite appearances.",
             "correct": False,
             "why": "The second leaf's result is exactly what a properly "
                    "destarched plant should show, so the destarching had "
                    "worked."},
            {"text": "That the first bottle of iodine may genuinely have "
                     "gone off.",
             "correct": True},
            {"text": "That the leaf used first must have torn during "
                     "preparation.",
             "correct": False,
             "why": "Nothing in the description mentions any tearing or "
                    "damage to that leaf."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s27",
        "band": "standard",
        "text": "One leaf gives a faint, patchy pattern that is "
                "different every time it is repeated; another gives a "
                "clear pattern with a ragged gap where the leaf tore. "
                "Which step was skipped in each case?",
        "options": [
            {"text": "Both the patchy pattern and the torn leaf are "
                     "caused by skipping the very same hot-water dip, "
                     "just to different degrees.",
             "correct": False,
             "why": "A torn leaf does match the dip being skipped, but a "
                    "patchy, unrepeatable pattern is a different fault "
                    "altogether."},
            {"text": "The patchy leaf skipped destarching; the torn one "
                     "skipped the ethanol.",
             "correct": False,
             "why": "Skipping destarching gives a strong, even "
                    "blue-black rather than a faint patchy one, and "
                    "skipping ethanol gives no reading at all."},
            {"text": "The patchy leaf skipped the ethanol; the torn one "
                     "skipped destarching.",
             "correct": False,
             "why": "Skipping ethanol leaves the leaf green with no "
                    "visible reading, and skipping destarching does not "
                    "make a leaf tear."},
            {"text": "The patchy leaf skipped the boil in water; the "
                     "torn one skipped the hot-water dip.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s28",
        "band": "standard",
        "text": "A student tapes foil in three different shapes onto "
                "three different leaves of the same plant, all "
                "destarched and then lit for a day together. Which part "
                "of this design is acting as the control?",
        "options": [
            {"text": "The covered parts of each leaf, since they show "
                     "what that leaf would look like without light.",
             "correct": True},
            {"text": "The three different shapes, since they let the "
                     "student compare shapes against each other.",
             "correct": False,
             "why": "Comparing shapes to each other is not what a "
                    "control does — a control is what a treated part is "
                    "compared against."},
            {"text": "The single plant all three leaves came from, since "
                     "using one plant keeps the species the same.",
             "correct": False,
             "why": "Using one plant helps keep conditions similar, but "
                    "that is not what makes something a control."},
            {"text": "The day of bright light that was given, since "
                     "that particular part of the design is kept the "
                     "same across every leaf involved in the test.",
             "correct": False,
             "why": "Keeping the light period the same is good "
                    "practice, but the control here is the unlit, "
                    "covered part each leaf is compared against."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s29",
        "band": "standard",
        "text": "A student writes up the practical and records the whole "
                "result as 'the leaf went blue-black'. What important detail "
                "has been left out of that record?",
        "options": [
            {"text": "The mass of the leaf before the test and its mass again "
                     "afterwards.",
             "correct": False,
             "why": "Nothing in this test is weighed; the result is a colour "
                    "and where it appears, not a change in mass."},
            {"text": "Which part of the leaf went blue-black, and which part "
                     "stayed orange-brown.",
             "correct": True},
            {"text": "The number of drops of iodine that were put onto the "
                     "leaf on the tile.",
             "correct": False,
             "why": "A drop or two is enough, and more drops do not change "
                    "what the test says. What the record needs is where the "
                    "colour appeared."},
            {"text": "Whether the plant was watered at all during its two "
                     "days in the dark.",
             "correct": False,
             "why": "Watering does not put starch into a leaf; light does, "
                    "and the two days in the dark are there to take the old "
                    "starch out."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-s30",
        "band": "standard",
        "text": "A student leaves the leaf in the hot-water dip for two "
                "full minutes instead of a few seconds. What is the "
                "likely consequence?",
        "options": [
            {"text": "The starch will start to dissolve out of the leaf "
                     "during those extra minutes.",
             "correct": False,
             "why": "Starch is insoluble in water at this temperature "
                    "and stays in place regardless of how long the dip "
                    "lasts."},
            {"text": "The leaf will slowly regain some of its original "
                     "green colour, since hot water is able to restore "
                     "dissolved chlorophyll.",
             "correct": False,
             "why": "Chlorophyll was removed by the ethanol and does not "
                    "return by soaking in water."},
            {"text": "Little extra harm, since the dip's job — "
                     "softening — happens quickly and staying in longer "
                     "does not undo it.",
             "correct": True},
            {"text": "The iodine will no longer be able to react with "
                     "the leaf afterwards.",
             "correct": False,
             "why": "A longer hot-water dip has no effect on whether "
                    "iodine can later react with any starch present."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b7-03-h14",
        "band": "harder",
        "text": "The same reasoning that explains why a leaf stores "
                "starch rather than glucose also explains why humans "
                "store glycogen rather than free glucose in their "
                "tissues. What is that shared reasoning?",
        "options": [
            {"text": "A store built of a soluble sugar would pull in "
                     "water by osmosis and swell the cell or tissue "
                     "holding it, so cells convert it to an insoluble "
                     "form instead.",
             "correct": True},
            {"text": "Glucose is too large and bulky a molecule to be "
                     "carried across a cell membrane, so it has to be "
                     "broken down into starch or glycogen before it "
                     "can be moved anywhere.",
             "correct": False,
             "why": "Glucose is small enough to be transported into "
                    "cells directly — the issue with storing it as-is "
                    "is osmotic, not one of size."},
            {"text": "Enzymes can only break down starch and glycogen, "
                     "never glucose itself, so storing glucose would be "
                     "a dead end.",
             "correct": False,
             "why": "Glucose is exactly what cells break down for "
                    "energy; it is the storage form that changes, not "
                    "what enzymes can act on."},
            {"text": "Glucose reacts with oxygen even when it is not "
                     "needed, wasting the store, unless it is converted "
                     "first.",
             "correct": False,
             "why": "Glucose does not spontaneously react with oxygen "
                    "in storage — the reason for conversion is osmotic."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h15",
        "band": "harder",
        "text": "Two classes test leaves from the same variegated plant. One "
                "class destarches the plant for two days and gives it a day "
                "of light first; the other tests a leaf straight off the "
                "plant. Both classes get the same pattern of colour on the "
                "tile. Does the second class's result still support the "
                "conclusion that chlorophyll is needed?",
        "options": [
            {"text": "No — the starch in the green parts could be weeks old, "
                     "which leaves the white parts' result meaningless too.",
             "correct": False,
             "why": "The green parts' result cannot be dated, and that is a "
                    "real limitation. The white parts' result does not depend "
                    "on dating: they never hold starch at all."},
            {"text": "Yes — the white tissue has no chlorophyll and no starch "
                     "whenever it is tested, so the comparison holds.",
             "correct": True},
            {"text": "No — a leaf tested straight off a plant always comes "
                     "out blue-black all over, whatever colour its tissue is.",
             "correct": False,
             "why": "Undestarched green tissue does go blue-black, but white "
                    "tissue has no chlorophyll and so never makes starch to "
                    "be found, whenever it is tested."},
            {"text": "Yes, but only because a variegated leaf empties its own "
                     "starch store within a few hours of being picked.",
             "correct": False,
             "why": "A picked leaf does not empty its store in hours, and "
                    "nothing here turns on that. The white tissue simply "
                    "never had any starch to begin with."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h16",
        "band": "harder",
        "text": "A single variegated leaf, tested once, shows starch in its "
                "green parts and none at all in its white parts. A critic "
                "says this alone does not fully prove chlorophyll is needed. "
                "What extra evidence would answer that criticism?",
        "options": [
            {"text": "Testing the exact same leaf a second time on the "
                     "same plant, days later, just to check that the "
                     "same two colours turn up again in the same "
                     "places.",
             "correct": False,
             "why": "Repeating the same comparison on the same leaf "
                    "does not address what else might differ between "
                    "the green and white tissue besides chlorophyll."},
            {"text": "Using a stronger iodine solution so the colours "
                     "show up more clearly.",
             "correct": False,
             "why": "The strength of the iodine has nothing to do with "
                    "whether the comparison itself is fair."},
            {"text": "Removing the white tissue entirely and testing "
                     "only the green.",
             "correct": False,
             "why": "That would remove the very comparison the evidence "
                    "depends on."},
            {"text": "Checking that the green and white tissue are "
                     "otherwise the same age, thickness and position, "
                     "so chlorophyll is the only real difference "
                     "between them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h17",
        "band": "harder",
        "text": "A leaf's starch store rises by 3 mg for every hour of "
                "bright light, starting from zero on a fully destarched "
                "plant. After how many hours of light does the store "
                "first reach 27 mg?",
        "options": [
            {"text": "3 hours, since 27 divided by 3 gives the rate "
                     "rather than the time.",
             "correct": False,
             "why": "Dividing 27 by 3 gives 9, not 3 — 3 mg per hour is "
                    "the rate to divide by, not the answer itself."},
            {"text": "24 hours, treating 27 minus 3 as the number of "
                     "hours needed.",
             "correct": False,
             "why": "Subtracting the rate from the total store is not "
                    "how a rate-and-time calculation works."},
            {"text": "9 hours, since 27 mg divided by 3 mg per hour "
                     "gives 9 hours.",
             "correct": True},
            {"text": "81 hours, since 27 multiplied by 3 gives the "
                     "number of hours.",
             "correct": False,
             "why": "Multiplying the store by the rate gives no "
                    "meaningful time at all; dividing gives the hours."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h18",
        "band": "harder",
        "text": "A student claims the starch test proves photosynthesis "
                "happened in a leaf. A teacher says it proves only that "
                "starch is present. Who is right, and what would close the "
                "gap between the two statements?",
        "options": [
            {"text": "The teacher — the test finds starch, and it takes a "
                     "destarched plant and a light-and-dark comparison to tie "
                     "that starch to photosynthesis.",
             "correct": True},
            {"text": "The student — a blue-black tile is a direct detection "
                     "of the photosynthesis reaction taking place in the "
                     "tissue under the iodine.",
             "correct": False,
             "why": "Iodine finds starch and nothing else. Starch is evidence "
                    "that photosynthesis happened, but it is not the reaction "
                    "being detected."},
            {"text": "The teacher, but only because iodine also turns "
                     "blue-black with the glucose that photosynthesis makes, "
                     "so the two cannot be told apart.",
             "correct": False,
             "why": "Iodine gives no colour change with glucose at all, which "
                    "is one of the reasons starch is the thing tested for."},
            {"text": "Neither — the test detects chlorophyll, and finding "
                     "chlorophyll is what proves photosynthesis happened in "
                     "that part of the leaf.",
             "correct": False,
             "why": "The ethanol removes every trace of chlorophyll before "
                    "the iodine goes on, so chlorophyll is not what is being "
                    "detected."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h19",
        "band": "harder",
        "text": "One leaf holds 30 mg of starch and empties it at 10 mg "
                "a day in the dark; a second, larger leaf holds 45 mg "
                "and empties at 15 mg a day. Which leaf finishes "
                "destarching first, and after how long?",
        "options": [
            {"text": "The second leaf, after 3 days, since it has more "
                     "starch to work with.",
             "correct": False,
             "why": "More starch does not mean a faster finish — 45 "
                    "divided by 15 also gives 3 days, the same as the "
                    "first leaf."},
            {"text": "Both finish after exactly 3 days, since 30÷10 and "
                     "45÷15 both equal 3.",
             "correct": True},
            {"text": "The first leaf, after 3 days, while the second "
                     "takes 4.5 days.",
             "correct": False,
             "why": "45 divided by 15 is 3, not 4.5 — the second leaf "
                    "actually finishes in the same time as the first."},
            {"text": "Neither can be worked out, since the two leaves "
                     "have different starting amounts.",
             "correct": False,
             "why": "Each leaf's own store divided by its own daily "
                    "rate gives its own destarching time, and both come "
                    "out the same."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h20",
        "band": "harder",
        "text": "A cactus has no leaves, but its green, "
                "photosynthesising stem is destarched, given a day of "
                "light with part of it covered, and tested with the "
                "standard method. Blue-black appears only in the "
                "exposed part. What does that show?",
        "options": [
            {"text": "Nothing, because the starch test only ever works "
                     "on true leaves.",
             "correct": False,
             "why": "The test responds to starch wherever it is found, "
                    "in a leaf or in any other photosynthesising "
                    "tissue."},
            {"text": "That the stem must be a modified leaf underneath "
                     "its outer green surface, disguised as something "
                     "else entirely.",
             "correct": False,
             "why": "A positive starch test tells you nothing about "
                    "what kind of organ the tissue is — only where "
                    "starch was made."},
            {"text": "That covering part of a stem has no effect on how "
                     "much starch it holds.",
             "correct": False,
             "why": "The result shows the opposite — the covered part "
                    "has less starch, exactly as it would in a leaf."},
            {"text": "That light is needed for starch to be made in "
                     "this tissue too, whatever the organ is called.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h21",
        "band": "harder",
        "text": "Two rules are broken in the same lesson: one group "
                "heats ethanol over a naked flame briefly before being "
                "stopped; another stoppers a tube of ethanol while it "
                "heats in a water bath, spotted just before pressure "
                "builds dangerously. Which incident carries the "
                "greater risk, and why?",
        "options": [
            {"text": "The stoppered tube, because a bung trapping rising "
                     "pressure inside hot glassware is more dangerous "
                     "than any flame could be in this practical.",
             "correct": False,
             "why": "A bung on its own is not the hazard here — even "
                    "so, a live flame near ethanol vapour is judged the "
                    "greater immediate risk."},
            {"text": "Neither — both were stopped before anything "
                     "happened, so neither carried any real risk.",
             "correct": False,
             "why": "How a mistake is stopped does not change how much "
                    "risk it carried while it was happening."},
            {"text": "The naked flame, because it can ignite ethanol "
                     "vapour that has already spread through the room, "
                     "not just from that one tube.",
             "correct": True},
            {"text": "The stoppered tube, because pressure building in "
                     "glass is always the more serious hazard in a "
                     "school laboratory.",
             "correct": False,
             "why": "A naked flame near flammable vapour is the more serious "
                    "hazard in this practical, which is why it is the one to "
                    "deal with first."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h22",
        "band": "harder",
        "text": "A student adds a second drop of iodine to the same "
                "already-tested leaf and gets the same blue-black "
                "pattern again. Does that show the result is reliable?",
        "options": [
            {"text": "Not fully — it shows the leaf's own pattern is "
                     "fixed, but says nothing about whether a different "
                     "leaf from the same plant would agree.",
             "correct": True},
            {"text": "Yes — repeating on the same leaf is exactly what "
                     "a reliable result requires.",
             "correct": False,
             "why": "A genuinely reliable result needs agreement across "
                    "independent leaves, not two readings of one leaf "
                    "that cannot have changed in between."},
            {"text": "No — a second drop of iodine always gives a "
                     "different pattern to the first.",
             "correct": False,
             "why": "Nothing about a starch pattern already fixed on a "
                    "dead leaf would change between one drop of iodine "
                    "and a second."},
            {"text": "Yes — iodine is supposed to only ever give the "
                     "same answer twice over, on any leaf whose result "
                     "can truly be called reliable.",
             "correct": False,
             "why": "Two readings of the same already-fixed leaf are "
                    "not a test of reliability — the pattern cannot "
                    "change between them regardless of anything else."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h23",
        "band": "harder",
        "text": "Destarching takes about two days. A separate plant is "
                "given exactly 30 hours of continuous bright light "
                "before testing. Which period is longer, and by how "
                "much?",
        "options": [
            {"text": "The 30 hours of light, by 6 hours, since two "
                     "days equals 24 hours.",
             "correct": False,
             "why": "Two days is 48 hours, not 24 — a day is 24 hours, "
                    "but two days doubles that."},
            {"text": "The two days of destarching, by 18 hours, since "
                     "two days equals 48 hours.",
             "correct": True},
            {"text": "The 30 hours of light, by 18 hours, since two "
                     "days is taken here to equal only 12 hours in "
                     "total.",
             "correct": False,
             "why": "Two days cannot be 12 hours — that is half of one "
                    "day, not the length of two."},
            {"text": "They are equal, since both round to about a day "
                     "and a half.",
             "correct": False,
             "why": "Two days is 48 hours and 30 hours is nowhere near "
                    "that — the two periods are not close to equal."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h24",
        "band": "harder",
        "text": "Two students each propose a way to destarch a plant in "
                "under a day: one suggests keeping it very cold instead "
                "of dark; the other suggests keeping it in total "
                "darkness as usual, but at a higher temperature. Which "
                "proposal has any real chance of working faster, and "
                "why?",
        "options": [
            {"text": "The cold proposal, because low temperature stops "
                     "any further starch being made.",
             "correct": False,
             "why": "Temperature affects the rate at which starch is "
                    "used up, not whether more is being made — light is "
                    "what allows more to be made, regardless of "
                    "temperature."},
            {"text": "Neither — destarching always takes exactly two "
                     "days no matter what temperature, lighting, or "
                     "other growing conditions the plant experiences "
                     "during that time.",
             "correct": False,
             "why": "Two days is typical under ordinary conditions; a "
                    "genuine change in the rate of respiration could in "
                    "principle change it."},
            {"text": "The cold proposal, because cold, dark conditions "
                     "are the fastest way to empty a starch store.",
             "correct": False,
             "why": "Cold slows respiration, which would use up the "
                    "store more slowly, not more quickly."},
            {"text": "The warmer, dark proposal, because a plant "
                     "respiring faster in the warmth uses up its "
                     "starch store more quickly, as long as it stays "
                     "fully in the dark.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h25",
        "band": "harder",
        "text": "Two different leaves both go blue-black under their "
                "foil as well as in the exposed half. On investigation, "
                "one plant was never destarched; the other's foil had "
                "a small tear letting a little light through all day. "
                "How could you tell the two causes apart without "
                "redoing the whole test?",
        "options": [
            {"text": "You could not — both faults look identical and "
                     "cannot be told apart afterwards.",
             "correct": False,
             "why": "A torn-foil leaf should show a real difference in "
                    "degree — the light leaking through a tear is far "
                    "less than the exposed half gets directly."},
            {"text": "By checking whether the leaf still has any of its "
                     "original chlorophyll left inside its cells, since "
                     "one incorrect assumption holds that only one of "
                     "the two possible faults would remove it.",
             "correct": False,
             "why": "Chlorophyll is removed by the ethanol in every "
                    "leaf regardless of which fault occurred."},
            {"text": "By comparing the strength of the blue-black on "
                     "each half: an undestarched leaf goes fully black "
                     "on both halves, while light through a tear would "
                     "usually give a fainter reading under the foil.",
             "correct": True},
            {"text": "By checking how long the leaf took to reach the "
                     "tile after the ethanol step.",
             "correct": False,
             "why": "The time taken to spread the leaf out has no "
                    "bearing on which of these two faults occurred "
                    "earlier in the process."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h26",
        "band": "harder",
        "text": "A student argues that because both starch and glycogen "
                "solve the same problem — an insoluble store built from "
                "glucose — plants and animals must use identical "
                "enzymes to build them. Is that a safe conclusion from "
                "just those two examples?",
        "options": [
            {"text": "No — sharing the same reason for existing does "
                     "not mean the two processes use the same "
                     "biological machinery.",
             "correct": True},
            {"text": "Yes — any two stores solving an identical problem "
                     "must be built the same way.",
             "correct": False,
             "why": "Solving the same underlying problem does not "
                    "require identical machinery — different organisms "
                    "can arrive at similar solutions independently."},
            {"text": "Yes — starch and glycogen are chemically "
                     "identical to one another as molecules, so the "
                     "same set of enzymes must surely be involved in "
                     "building both.",
             "correct": False,
             "why": "Starch and glycogen are both made of glucose units "
                    "but are not the same molecule, and nothing here "
                    "establishes shared enzymes."},
            {"text": "No — because plants do not use enzymes to build "
                     "starch in the first place.",
             "correct": False,
             "why": "Building starch from glucose is itself an "
                    "enzyme-driven process; that is not the flaw in "
                    "the student's argument."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h27",
        "band": "harder",
        "text": "On the same leaf, a student both skips the destarching and "
                "heats the ethanol over a naked flame. Which of the two "
                "faults should be dealt with first, and why?",
        "options": [
            {"text": "Because a destarching fault can always be fixed "
                     "afterwards, but a flame cannot.",
             "correct": False,
             "why": "Neither fault can be undone after the fact — "
                    "reporting the flame first is about safety, not "
                    "about which is easier to fix later."},
            {"text": "Because the flame ends the practical outright, so "
                     "nothing about the data quality matters until "
                     "safety is dealt with.",
             "correct": True},
            {"text": "Because skipping the destarching step is the more "
                     "dangerous of these two particular mistakes.",
             "correct": False,
             "why": "Skipping destarching produces bad data, not a "
                    "safety hazard — it is the less dangerous mistake."},
            {"text": "Because faults are dealt with in the order they "
                     "happened, and the destarching came first.",
             "correct": False,
             "why": "The order is a deliberate ranking of seriousness — "
                    "safety first, then result-destroying faults, then "
                    "result-weakening ones — not the order the mistakes "
                    "happened in."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h28",
        "band": "harder",
        "text": "A large leaf holds 4 mg of starch per gram of leaf "
                "tissue and weighs 15 g. A small leaf from the same "
                "plant holds the same concentration but weighs only "
                "6 g. How much starch does the small leaf hold?",
        "options": [
            {"text": "60 mg, by multiplying the large leaf's total mass "
                     "by the small leaf's concentration.",
             "correct": False,
             "why": "That mixes the two leaves' own figures together "
                    "rather than using the small leaf's own mass with "
                    "the shared concentration."},
            {"text": "4 mg, since the concentration given already is "
                     "the answer regardless of mass.",
             "correct": False,
             "why": "4 mg per gram is a concentration, not a total "
                    "amount — it still needs multiplying by the leaf's "
                    "own mass."},
            {"text": "9 mg, by subtracting the small leaf's mass from "
                     "the large leaf's mass.",
             "correct": False,
             "why": "Subtracting the two masses gives a difference in "
                    "size, not an amount of starch in either leaf."},
            {"text": "24 mg, by multiplying 4 mg per gram by the small "
                     "leaf's 6 g.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h29",
        "band": "harder",
        "text": "A leaf is holed by insect damage before it is even "
                "picked, then destarched, exposed to light with foil "
                "over half, and tested as usual. The holes themselves "
                "obviously show no colour at all. Does that damage the "
                "value of the test?",
        "options": [
            {"text": "Yes — a damaged leaf can never give a "
                     "trustworthy starch reading.",
             "correct": False,
             "why": "The intact tissue around the holes has gone "
                    "through the same steps as any other leaf and can "
                    "still be read normally."},
            {"text": "No — because insect damage always destroys a "
                     "leaf's ability to photosynthesise entirely.",
             "correct": False,
             "why": "The undamaged tissue around holes still "
                    "photosynthesises and can still make and hold "
                    "starch."},
            {"text": "No — the holes simply have no leaf tissue in "
                     "them to react with iodine, but the surrounding "
                     "tissue still gives a genuine reading.",
             "correct": True},
            {"text": "Yes — the insect's own saliva left behind in the "
                     "damaged tissue reacts directly with the iodine, "
                     "producing a false blue-black ring around each of "
                     "the holes.",
             "correct": False,
             "why": "Insect damage does not introduce anything that "
                    "reacts with iodine; the holes just have no tissue "
                    "there to react at all."},
        ],
        "figure": None,
    },
    {
        "id": "b7-03-h30",
        "band": "harder",
        "text": "A leaf starts a destarching period holding 40 mg of "
                "starch and loses it at 8 mg a day in full dark — but "
                "a faulty blind lets in enough light each day to let "
                "the leaf remake 3 mg of starch before night. What is "
                "the leaf's true net loss per day, and how many days "
                "until it reaches zero?",
        "options": [
            {"text": "5 mg a day net loss, so 8 days to reach zero.",
             "correct": True},
            {"text": "8 mg a day net loss, so 5 days to reach zero, "
                     "since the light leak can be ignored.",
             "correct": False,
             "why": "The light leak lets the leaf remake 3 mg each day, "
                    "so the true daily loss is less than the full 8 mg "
                    "respired."},
            {"text": "11 mg a day net loss, so about 3.6 days to reach "
                     "zero, since the light adds to what is lost.",
             "correct": False,
             "why": "The light leak makes the leaf remake starch, which "
                    "works against the loss, not alongside it — the two "
                    "figures should be subtracted, not added."},
            {"text": "3 mg a day net loss, so about 13.3 days to reach "
                     "zero, ignoring the respiration entirely.",
             "correct": False,
             "why": "Respiration is still removing 8 mg a day "
                    "regardless of the light leak; the light only "
                    "offsets part of that loss, not all of it."},
        ],
        "figure": None,
    },
]
