# -*- coding: utf-8 -*-
"""B1 lesson 01 — Life processes and what living things are made of: twelve
questions (MRB-269).

The lesson's whole shape is one claim: the seven life processes describe what
living things *do*, and being made of cells is what decides whether a thing is
living. Every question here probes some part of that split, and the twelve
between them work all four of the lesson's specimens (flame, oak seed, robot
vacuum, yeast), all three sort boxes, and the stretch note on viruses.

The distractors are built from the lesson's two declared misconceptions.
LIFE-01 ("if it moves on its own it must be alive, and if it never moves it
must not be") supplies the options that reach for behaviour — the acorn that
"is not alive yet", the spoon that "never moved or grew", the virus that
"cannot move or feed itself". LIFE-02 ("doing one of the life processes is
enough") supplies every option that counts lamps: six beats three, three is
enough, reproduction is the strongest test, add movement and food and you get
there. Two further errors the lesson's own activities exist to correct are
worked as well: that a gas swap is respiration (the flame), and that "no cells
left in it now" means "never living" (coal, chalk).

No question restates a ladder rung. The rungs already own "true of every living
thing", the robot vacuum's verdict, the flame explanation and the Mars-probe
test design, so the bank works around all four: the robot appears only over
what excretion means, and the transfer questions go to a 3D printer, a virus
and a stick of chalk instead of a Mars probe.

`figure` is `None` throughout. The lesson holds one figure, `b1-candle-flame`,
and it is decorative CSS art (`aria-hidden` on Design's page); no question here
needs to be looked at to be answered, and every stem is self-contained.
"""

UNIT = "B1"
LESSON = "life-processes"
LESSON_NUMBER = 1

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-01-e01",
        "band": "easier",
        "text": "MRS GREN is a way of remembering the seven life processes. "
                "What does the E stand for?",
        "options": [
            {"text": "Energy", "correct": False,
             "why": "Energy is not one of the seven. The E is excretion — "
                    "getting rid of the waste your own chemistry makes."},
            {"text": "Eating", "correct": False,
             "why": "Eating is closest to nutrition, which is the N. The E is "
                    "excretion — getting rid of your own waste."},
            {"text": "Excretion", "correct": True},
            {"text": "Environment", "correct": False,
             "why": "Responding to the environment is sensitivity, the S. The "
                    "E is excretion — getting rid of your own waste."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e02",
        "band": "easier",
        "text": "This unit calls a living thing an organism. What does the "
                "word organism mean?",
        "options": [
            {"text": "A single living thing — one cell, or trillions.",
             "correct": True},
            {"text": "A living thing built from many cells working together.",
             "correct": False,
             "why": "That leaves yeast out, and yeast is one cell and a whole "
                    "organism on its own. One cell is enough."},
            {"text": "A part of a living thing that does one particular job.",
             "correct": False,
             "why": "That describes an organ. An organism is the whole living "
                    "thing, not one part of it."},
            {"text": "Anything that moves and grows without being pushed.",
             "correct": False,
             "why": "A candle flame moves and grows on its own and is not an "
                    "organism. What a thing does never settles it — cells do."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e03",
        "band": "easier",
        "text": "On the seven tests the candle flame lit six lamps and the oak "
                "seed lit three. Which one of the two is alive?",
        "options": [
            {"text": "The candle flame, because it passed more of the tests.",
             "correct": False,
             "why": "The score is not the test. A flame is hot glowing gas "
                    "with no cells in it, so it is not alive whatever it "
                    "scores."},
            {"text": "The oak seed, because it is made of cells.",
             "correct": True},
            {"text": "Both of them — three out of seven is enough to count.",
             "correct": False,
             "why": "No number out of seven counts. What settles it is cells, "
                    "and a flame has none at all."},
            {"text": "Neither — you would need all seven to call it alive.",
             "correct": False,
             "why": "The seed scores three and is alive. The seven are things "
                    "an organism can do across its life, not a checklist for "
                    "this second."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e04",
        "band": "easier",
        "text": "Where does a wooden spoon belong — living, once living, or "
                "never living?",
        "options": [
            {"text": "Living — wood is made of cells, so the spoon is alive.",
             "correct": False,
             "why": "Wood is the leftover walls of tree cells. Those cells "
                    "died when the tree was cut, so nothing in the spoon is "
                    "working now."},
            {"text": "Never living — a spoon has never moved, fed or grown.",
             "correct": False,
             "why": "Moving and feeding are not the test. The spoon was part "
                    "of a tree, and a tree is built from cells."},
            {"text": "Never living — it was shaped in a workshop, not grown.",
             "correct": False,
             "why": "Being shaped by people does not decide it. A leather "
                    "boot is made by people too, and it was once part of a "
                    "living animal."},
            {"text": "Once living — it came from a tree built from cells.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-01-s01",
        "band": "standard",
        "text": "Respiration is the one test out of seven that the candle "
                "flame fails. Why does burning not count as respiration?",
        "options": [
            {"text": "Because a flame gives heat out rather than taking any "
                     "heat in.", "correct": False,
             "why": "Respiration releases energy too — that is what it is "
                    "for. What burning is missing is cells to do it inside."},
            {"text": "Because respiration is a controlled set of reactions "
                     "inside cells.", "correct": True},
            {"text": "It does count — the flame takes in oxygen and gives out "
                     "carbon dioxide.", "correct": False,
             "why": "That gas swap is real, which is exactly what makes this "
                    "a near miss. But swapping gases is not respiration; "
                    "respiration happens inside cells."},
            {"text": "Because there is nothing going into a flame for it to "
                     "respire.", "correct": False,
             "why": "Wax and oxygen do go in, which is why the flame passes "
                    "the nutrition test. The problem is that there are no "
                    "cells."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s02",
        "band": "standard",
        "text": "An acorn has sat in a drawer for four years. It does not "
                "move, it does not grow and it takes in no food. Why is it "
                "still alive?",
        "options": [
            {"text": "It is made of cells, and those cells are still "
                     "respiring slowly.", "correct": True},
            {"text": "It is not alive yet — it becomes alive once it is "
                     "planted and starts growing.", "correct": False,
             "why": "Nothing switches on when you plant it. The acorn is "
                    "already respiring, and it already responds to water and "
                    "warmth."},
            {"text": "It is alive because one day it will grow into a full "
                     "oak tree.", "correct": False,
             "why": "What it might become does not decide it. What it is "
                    "right now — cells, ticking over slowly — does."},
            {"text": "It is alive because it still has a food store packed "
                     "inside it.", "correct": False,
             "why": "A bag of flour holds a food store and is not alive. The "
                    "store is what the cells live on, not what makes it "
                    "living."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s03",
        "band": "standard",
        "text": "A robot vacuum tips out the dust it has collected. That does "
                "not count as excretion. Why not?",
        "options": [
            {"text": "Because excretion has to happen by itself, and a person "
                     "empties the bin.", "correct": False,
             "why": "Who empties it is not the point. Even if it tipped "
                    "itself out, that dust was never its own waste."},
            {"text": "Because the dust is solid, and excretion means getting "
                     "rid of gases.", "correct": False,
             "why": "Excretion is about where the waste came from, not what "
                    "state it is in. The acorn's waste happens to be a gas; "
                    "the vacuum's dust was never its waste at all."},
            {"text": "It does count — the dust leaves the machine, so the "
                     "machine excretes.", "correct": False,
             "why": "The dust was never part of the machine. Excretion means "
                    "getting rid of waste your own chemistry made."},
            {"text": "Because excretion means waste your own chemistry "
                     "made.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s04",
        "band": "standard",
        "text": "A lump of coal has no cells left in it at all. So why does it "
                "go in the “Once living” box rather than “Never living”?",
        "options": [
            {"text": "Because it gives out carbon dioxide when you burn it.",
             "correct": False,
             "why": "So does a candle flame, and the flame sits in “Never "
                    "living”. What a thing gives out never decides the box."},
            {"text": "Because it was buried underground, the way a dead "
                     "animal is buried.", "correct": False,
             "why": "Granite sits underground too and was never alive. Where "
                    "something ends up is not the test."},
            {"text": "Because it formed from plants, and plants are made of "
                     "cells.", "correct": True},
            {"text": "It should be “Never living” — nothing with no cells "
                     "left was ever alive.", "correct": False,
             "why": "Then a wooden spoon and a leather boot would go there "
                    "too. The box asks what it came from, not what it holds "
                    "now."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-01-h01",
        "band": "harder",
        "text": "A virus is not made of cells, and on its own it does none of "
                "the seven — it cannot even copy itself unless it gets inside "
                "a cell. Which reason for calling a virus “not living” "
                "matches this lesson's rule?",
        "options": [
            {"text": "It fails to do all seven of the life processes.",
             "correct": False,
             "why": "The oak seed does three of the seven and is alive. A "
                    "score out of seven has never settled a case in this "
                    "lesson."},
            {"text": "It is far too small for anything to be alive at that "
                     "size.", "correct": False,
             "why": "A single yeast cell is a whole living organism and you "
                    "cannot see one either. Size is not the test."},
            {"text": "It cannot move or feed itself without help from "
                     "something else.", "correct": False,
             "why": "An acorn in a drawer does neither and is alive. "
                    "Behaviour is what the seven measure, and the seven do "
                    "not decide it."},
            {"text": "It is not made of cells, and being made of cells "
                     "settles it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h02",
        "band": "harder",
        "text": "A 3D printer can print the parts for a second 3D printer. "
                "Deni says that means it reproduces, so it must be alive. "
                "What is the best reply?",
        "options": [
            {"text": "The seven never settle it — and the printer has no "
                     "cells.", "correct": True},
            {"text": "It is alive, because reproduction is the strongest test "
                     "of the seven.", "correct": False,
             "why": "No one of the seven outranks the others, and none of "
                    "them decides it. An acorn will not reproduce for decades "
                    "and is alive today."},
            {"text": "It does not really reproduce, because a person still "
                     "assembles the second one.", "correct": False,
             "why": "True, but that is not why it is not alive. A flame "
                    "lights a second wick with nobody's help and is still not "
                    "alive."},
            {"text": "It would be alive if it could feed and move as well as "
                     "reproduce.", "correct": False,
             "why": "Adding processes never gets you there. A candle flame "
                    "does six of the seven, including all three of those, and "
                    "is not alive."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h03",
        "band": "harder",
        "text": "Yeast is one cell. A woodlouse is built from millions. A "
                "student says the woodlouse must be “more alive” than the "
                "yeast. Which reply is right?",
        "options": [
            {"text": "The woodlouse is more alive, because more cells means "
                     "more life.", "correct": False,
             "why": "There is no scale. A thing is made of cells or it is "
                    "not, and one cell is enough to be a whole organism."},
            {"text": "The yeast is more alive, because it passed all seven of "
                     "the tests.", "correct": False,
             "why": "The seven do not rank living things any more than they "
                    "decide which things are living."},
            {"text": "Neither is more alive — one cell is enough to be a "
                     "whole organism.", "correct": True},
            {"text": "The yeast is not an organism at all, because one cell "
                     "cannot be a living thing.", "correct": False,
             "why": "A single yeast cell feeds, grows, respires and buds into "
                    "two. That is an organism doing every job on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h04",
        "band": "harder",
        "text": "Blackboard chalk is a soft white rock made from the crushed "
                "shells of tiny sea creatures. Which box does a stick of "
                "chalk belong in?",
        "options": [
            {"text": "Never living — chalk is a rock, and rocks were never "
                     "alive.", "correct": False,
             "why": "Granite is a rock that grew from cooling molten "
                    "rock, so it never was. Chalk is a rock built out of "
                    "animal shells, so it was."},
            {"text": "Once living — the shells were built by animals made of "
                     "cells.", "correct": True},
            {"text": "Living — anything that came from an animal still counts "
                     "as living.", "correct": False,
             "why": "A leather boot came from an animal and nothing in it is "
                    "alive. The cells that built those shells stopped working "
                    "long ago."},
            {"text": "Never living — there is not one cell left in a stick of "
                     "chalk.", "correct": False,
             "why": "There is not one left in a lump of coal either, and coal "
                    "is “Once living”. The box asks what it came from, not "
                    "what it holds now."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-01-e05",
        "band": "easier",
        "text": "Sensitivity is the S in MRS GREN. What does an organism do "
                "when it shows sensitivity?",
        "options": [
            {"text": "It moves from one place to another under its own "
                     "power.", "correct": False,
             "why": "That is movement, the M. Sensitivity is noticing a "
                    "change and reacting to it, and a plant that never "
                    "travels still does it."},
            {"text": "It takes in the food that it needs to stay alive.",
             "correct": False,
             "why": "That is nutrition, the N. Sensitivity is picking up a "
                    "change around you and responding to it."},
            {"text": "It senses a change around it and responds to it.",
             "correct": True},
            {"text": "It grows towards whatever happens to be nearest to "
                     "it.", "correct": False,
             "why": "Growing towards the light is one example of a response, "
                    "not what the word means. Growth is a separate one of "
                    "the seven."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e06",
        "band": "easier",
        "text": "Every living thing is made of cells. What is a cell?",
        "options": [
            {"text": "The smallest living unit, and the thing every living "
                     "thing is built from.", "correct": True},
            {"text": "The smallest part of a living thing that a microscope "
                     "can show you.", "correct": False,
             "why": "A microscope shows plenty of things smaller than a whole "
                    "cell. A cell is the smallest unit that is itself alive, "
                    "not the smallest thing you can see."},
            {"text": "A bag of chemicals that keeps a living thing working "
                     "from the outside.", "correct": False,
             "why": "Cells are not outside the organism — they are what it is "
                    "made of. You are somewhere near thirty trillion of "
                    "them."},
            {"text": "A part of an organism that carries out one of the seven "
                     "life processes.", "correct": False,
             "why": "That would make a cell a job rather than a unit. One "
                    "yeast cell carries out all seven on its own, and it is "
                    "still one cell."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e07",
        "band": "easier",
        "text": "Where does a granite pebble belong — living, once living, "
                "or never living?",
        "options": [
            {"text": "Once living — every rock is built from the remains of "
                     "living things.", "correct": False,
             "why": "Chalk and coal are, which is why they sit in that box. "
                    "Granite formed from molten rock cooling, and nothing "
                    "living was ever part of it."},
            {"text": "Never living — it is far too hard for anything alive to "
                     "have been in it.", "correct": False,
             "why": "Hardness decides nothing. A seashell is hard and was "
                    "built by an animal made of cells, which puts it in "
                    "“Once living”."},
            {"text": "Once living — it was dug out of the ground, where dead "
                     "things end up.", "correct": False,
             "why": "Where a thing is found is not the test. Coal and granite "
                    "come out of the same ground and belong in different "
                    "boxes."},
            {"text": "Never living — granite formed from molten rock, not "
                     "from anything with cells.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e08",
        "band": "easier",
        "text": "Respiration is the first R in MRS GREN. What happens when "
                "an organism respires?",
        "options": [
            {"text": "Air is drawn in through the lungs and pushed out "
                     "again.", "correct": False,
             "why": "That is breathing, and most living things never do it. "
                    "Respiration is a set of reactions inside cells that "
                    "releases energy from food."},
            {"text": "Energy is released from food, by reactions inside the "
                     "cells.", "correct": True},
            {"text": "Food is broken down into pieces small enough to be "
                     "taken in.", "correct": False,
             "why": "That is digestion, which is part of nutrition. "
                    "Respiration comes afterwards, once the food is inside "
                    "the cells."},
            {"text": "Waste gases are swapped for the gases the organism "
                     "needs.", "correct": False,
             "why": "A candle flame swaps gases and does not respire. The "
                    "swap happens because of respiration; it is not "
                    "respiration itself."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e09",
        "band": "easier",
        "text": "Which one of these is one of the seven life processes?",
        "options": [
            {"text": "Breathing", "correct": False,
             "why": "Breathing is not one of the seven, and plenty of "
                    "living things never do it. The one you are reaching for "
                    "is respiration, which happens inside cells."},
            {"text": "Digestion", "correct": False,
             "why": "Digestion is one part of nutrition, and nutrition is "
                    "the one that counts. Digestion on its own is not one of "
                    "the seven."},
            {"text": "Nutrition", "correct": True},
            {"text": "Photosynthesis", "correct": False,
             "why": "Photosynthesis is one way of carrying out nutrition, and "
                    "only some organisms do it. Nutrition is the process that "
                    "covers every living thing."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-01-s05",
        "band": "standard",
        "text": "Frost spreads across a window overnight and by morning it "
                "has branched right across the glass. Why does that not "
                "count as growth?",
        "options": [
            {"text": "It does count — it got bigger on its own, and that is "
                     "what growth is.", "correct": False,
             "why": "This is the trap the candle flame sets too. Getting "
                    "bigger on its own is a behaviour; growth means a living "
                    "thing building more of itself."},
            {"text": "Growth means a living thing making more of itself from "
                     "materials it takes in.", "correct": True},
            {"text": "It does not count, because growth has to happen slowly "
                     "rather than overnight.", "correct": False,
             "why": "Speed decides nothing. A seedling shoots up in a week "
                    "and an oak takes a century, and both of them are "
                    "growing."},
            {"text": "It does not count, because the frost melts again as "
                     "soon as the sun is on it.", "correct": False,
             "why": "What happens to it afterwards is not the test. Frost is "
                    "water freezing onto more water, with nothing alive doing "
                    "any of it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s06",
        "band": "standard",
        "text": "You breathe out carbon dioxide, and you also pass out food "
                "that was never digested. Which of the two is excretion?",
        "options": [
            {"text": "Both of them, because both are waste leaving the "
                     "body.", "correct": False,
             "why": "Only one of them is your own waste. The undigested food "
                    "passed through you without ever being part of your "
                    "chemistry."},
            {"text": "The undigested food, because it is by far the larger "
                     "amount of waste.", "correct": False,
             "why": "Amount has nothing to do with it. That food went in one "
                    "end and out of the other, and your cells never made any "
                    "of it."},
            {"text": "Neither, because excretion means getting rid of waste "
                     "gases only.", "correct": False,
             "why": "Urine is excretion too, and it is a liquid. What matters "
                    "is where the waste came from, not what state it is in."},
            {"text": "The carbon dioxide, because your own cells made it "
                     "while respiring.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s07",
        "band": "standard",
        "text": "An oak tree stands in the same spot for two hundred years. "
                "How can movement still be one of its life processes?",
        "options": [
            {"text": "Movement can happen inside it — roots push down, "
                     "leaves turn to the light.", "correct": True},
            {"text": "It cannot. A tree fails that one, and a living thing "
                     "is allowed to fail one of the seven "
                     "processes.", "correct": False,
             "why": "No allowance is being made anywhere. The tree really "
                    "does move — the movement is inside it, rather than "
                    "across the ground."},
            {"text": "The wind moves its branches and its leaves for it, and "
                     "being moved counts as movement.", "correct": False,
             "why": "Being pushed by something else is not the organism's "
                    "own doing. A wooden fence panel moves in the wind as "
                    "well."},
            {"text": "A tree does travel, very slowly, over the two hundred "
                     "years.", "correct": False,
             "why": "It does not travel at all — the trunk stands where the "
                    "acorn landed. What moves is inside it: water up the "
                    "stem, roots down into the soil."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s08",
        "band": "standard",
        "text": "A wool jumper and a nylon jumper look and feel much the "
                "same. Which box does each of them belong in?",
        "options": [
            {"text": "Both are once living, because both are "
                     "clothing.", "correct": False,
             "why": "Being made into something decides nothing. Nylon is "
                    "built in a factory from chemicals that were never part "
                    "of anything alive."},
            {"text": "Both are never living, because neither has a working "
                     "cell left in it.", "correct": False,
             "why": "Then a wooden spoon would go there too. The box asks "
                    "what a thing came from, not what it holds now."},
            {"text": "Wool is once living, and nylon is never living.",
             "correct": True},
            {"text": "Wool is living, because its fibres are still made of "
                     "cells.", "correct": False,
             "why": "The cells that grew that wool stopped working when it "
                    "was cut from the sheep. Wool came from something living; "
                    "it is not living itself."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s09",
        "band": "standard",
        "text": "A worker bee never reproduces in its whole life. Does that "
                "stop it being alive?",
        "options": [
            {"text": "Yes — reproduction is one of the seven life processes, "
                     "so anything that never does it is not "
                     "alive.", "correct": False,
             "why": "An acorn does three of the seven and is alive. A score "
                    "out of seven settles nothing; being made of cells "
                    "settles it."},
            {"text": "No — it is made of cells, and the seven only describe "
                     "what it does.", "correct": True},
            {"text": "No — it counts because the queen reproduces on behalf "
                     "of every worker in the colony.", "correct": False,
             "why": "What another bee does cannot make this one alive. What "
                    "settles it is that this bee is built from cells."},
            {"text": "Yes, until it lays eggs — then it would count as "
                     "alive.", "correct": False,
             "why": "Nothing switches on. An acorn that never sprouts is "
                    "alive the whole time it sits in the drawer, for the "
                    "same reason."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-01-h05",
        "band": "harder",
        "text": "MRS GREN lists respiration and nutrition separately. A "
                "student says they are really one process, because both are "
                "about food. What is the difference?",
        "options": [
            {"text": "There is none — MRS GREN splits one process into two "
                     "so that the letters spell out a word you can "
                     "remember.", "correct": False,
             "why": "The letters are a memory trick, not the reason the two "
                    "are separate. Taking food in and releasing energy from "
                    "it are different jobs."},
            {"text": "Nutrition is for animals and respiration is for "
                     "plants.", "correct": False,
             "why": "Every living thing does both. A plant makes its own "
                    "food and then respires to release the energy from it, "
                    "exactly as you do."},
            {"text": "Respiration means breathing air in and out, and "
                     "nutrition means eating and digesting your "
                     "food.", "correct": False,
             "why": "Breathing is not one of the seven at all. Respiration "
                    "is the reactions inside cells, and it happens in things "
                    "that never breathe."},
            {"text": "Nutrition is taking in or making food; respiration "
                     "releases energy from it in cells.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h06",
        "band": "harder",
        "text": "A forest fire moves, grows, feeds on wood, gives out smoke "
                "and starts new fires. A student asks what the seven life "
                "processes are for, if that passes most of them.",
        "options": [
            {"text": "They are out of date, and biologists no longer use "
                     "them.", "correct": False,
             "why": "They are used constantly, because a description of what "
                    "living things do is exactly what a biologist needs. "
                    "They were never meant to be a test."},
            {"text": "They describe what living things do, not what is "
                     "alive.", "correct": True},
            {"text": "The fire only appears to do them, and really carries "
                     "out none of the seven processes.", "correct": False,
             "why": "It genuinely does several, in the plain sense of the "
                    "words — which is why the candle flame lights six lamps. "
                    "Denying that dodges the point."},
            {"text": "They work perfectly well as a test, but only on "
                     "animals, which is how a fire slips through "
                     "them.", "correct": False,
             "why": "They apply to an oak, a yeast cell and you alike. What "
                    "lets a fire through is that the seven were never a test "
                    "of what is alive."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h07",
        "band": "harder",
        "text": "The rule is that every living thing is made of cells. A "
                "student writes it down as “Anything made of cells is "
                "alive.” Is that the same rule?",
        "options": [
            {"text": "No — it is turned round: a wooden spoon is made of "
                     "cells and is not alive.", "correct": True},
            {"text": "Yes — it is the same rule, just written the other way "
                     "round, so it claims the same thing.", "correct": False,
             "why": "Turning a rule round changes what it claims. “Every "
                    "living thing is made of cells” says nothing about a "
                    "spoon or a lump of coal, and neither is alive."},
            {"text": "No — the rule is really that a thing is alive if it "
                     "carries out enough of the seven life "
                     "processes.", "correct": False,
             "why": "That is the idea the whole lesson exists to kill. Six "
                    "out of seven does not make a candle flame alive."},
            {"text": "No — nothing that is not alive contains any cells at "
                     "all.", "correct": False,
             "why": "Wood, leather and coal all came from cells and none of "
                    "them is alive. That is exactly why there is a “Once "
                    "living” box."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h08",
        "band": "harder",
        "text": "Two acorns look identical. One has been boiled for ten "
                "minutes and cooled again. How would you tell them apart, "
                "and what would that show?",
        "options": [
            {"text": "Weigh them — the living one is heavier, because living "
                     "things are full of water.", "correct": False,
             "why": "Both are full of water, and boiling adds some. Mass "
                    "tells you nothing about whether the cells inside are "
                    "working."},
            {"text": "Neither is alive yet, because an acorn only becomes "
                     "alive once it sprouts.", "correct": False,
             "why": "An acorn in a drawer is alive, respiring slowly the "
                    "whole time. Nothing switches on at sprouting."},
            {"text": "Plant both — only the one with working cells grows, and "
                     "the boiled one is now once living.", "correct": True},
            {"text": "Neither test would work, because the boiled one is "
                     "still made of cells and so still alive.",
             "correct": False,
             "why": "Its cells are still there and have stopped working, "
                    "which is the difference between an oak and a wooden "
                    "spoon. Cells have to be working, not just present."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h09",
        "band": "harder",
        "text": "Candle wax is made from crude oil, which formed underground "
                "from the remains of tiny sea creatures. Does that change "
                "which box a candle flame goes in?",
        "options": [
            {"text": "Yes — the flame is once living, because everything it "
                     "burns came from living things.", "correct": False,
             "why": "The flame is not the wax. It is hot glowing gas made "
                    "while the wax burns, and there was never a cell in it."},
            {"text": "No — the flame is never living, though the wax itself "
                     "would go in “Once living”.", "correct": True},
            {"text": "No — the wax was never living either, since oil comes "
                     "out of rock underground.", "correct": False,
             "why": "So does coal, and coal is “Once living”. Both formed "
                    "from the remains of things built out of cells."},
            {"text": "Yes — the wax and the flame cannot be separated, so "
                     "both go in “Once living”.", "correct": False,
             "why": "They are two different things. The wax came from living "
                    "organisms; the flame is a reaction at the wick, and a "
                    "reaction was never alive."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-01-e10",
        "band": "easier",
        "text": "In MRS GREN, the G stands for one of the seven life "
                "processes. Which one?",
        "options": [
            {"text": "Gases", "correct": False,
             "why": "Swapping gases is not one of the seven, and no letter "
                    "stands for it. The G is growth."},
            {"text": "Growth", "correct": True},
            {"text": "Germs", "correct": False,
             "why": "Germs are living things that make you ill, not a life "
                    "process. The G is growth."},
            {"text": "Genes", "correct": False,
             "why": "Genes are not one of the seven either. The G is growth — "
                    "building more of yourself and getting bigger."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e11",
        "band": "easier",
        "text": "Two of the letters in MRS GREN are R. One of them stands for "
                "respiration. What does the other R stand for?",
        "options": [
            {"text": "Reaction", "correct": False,
             "why": "Reacting to what is around you is sensitivity, the S. "
                    "The other R is reproduction."},
            {"text": "Repairing", "correct": False,
             "why": "Mending yourself is part of growth rather than a process "
                    "of its own. The other R is reproduction."},
            {"text": "Resting", "correct": False,
             "why": "Resting is not one of the seven, and plenty of living "
                    "things never do it. The other R is reproduction."},
            {"text": "Reproduction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e12",
        "band": "easier",
        "text": "Reproduction is one of the seven. What is an organism doing "
                "when it reproduces?",
        "options": [
            {"text": "Growing until it is big enough to look after itself.",
             "correct": False,
             "why": "That is growth, the G. Reproduction is making a whole "
                    "new living thing of the same kind."},
            {"text": "Making a new living thing of the same kind as itself.",
             "correct": True},
            {"text": "Replacing the parts of itself that have worn out.",
             "correct": False,
             "why": "Mending yourself keeps one organism going. Reproduction "
                    "makes a second one."},
            {"text": "Passing its food store on to the one that comes next.",
             "correct": False,
             "why": "A food store is packed into a seed, but that is not what "
                    "the word means. Reproduction is making the new organism "
                    "in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e13",
        "band": "easier",
        "text": "Which of these is the best description of nutrition?",
        "options": [
            {"text": "Breaking food down into pieces small enough to take in.",
             "correct": False,
             "why": "That is digestion, which is one part of nutrition rather "
                    "than the whole of it."},
            {"text": "Getting rid of the waste left once food has been used.",
             "correct": False,
             "why": "That is excretion, the E. Nutrition is about the food "
                    "coming in, not the waste going out."},
            {"text": "Taking in food, or making it, so that a thing can live.",
             "correct": True},
            {"text": "Releasing the energy held in food, inside the cells.",
             "correct": False,
             "why": "That is respiration, the first R. Nutrition gets the "
                    "food; respiration gets the energy out of it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e14",
        "band": "easier",
        "text": "A candle flame is not alive. What is a flame made of?",
        "options": [
            {"text": "Hot gas, glowing because it is so hot.", "correct": True},
            {"text": "Tiny drops of melted wax, thrown upwards by the heat.",
             "correct": False,
             "why": "Melted wax sits in a pool at the top of the candle and "
                    "does not glow. The flame itself is hot gas."},
            {"text": "Very small cells, far too small to be seen without a "
                     "microscope.", "correct": False,
             "why": "There is nothing to find down a microscope. A flame has "
                    "no cells in it at all, which is what settles it."},
            {"text": "Pure light, with nothing solid in it.",
             "correct": False,
             "why": "Light is what a flame gives out, not what it is made of. "
                    "What glows is hot gas."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e15",
        "band": "easier",
        "text": "A candle flame takes in wax and oxygen, and both are used "
                "up. Which of the seven is that?",
        "options": [
            {"text": "Respiration", "correct": False,
             "why": "Respiration is a controlled set of reactions inside "
                    "cells, and a flame has none. Material going in is "
                    "nutrition."},
            {"text": "Excretion", "correct": False,
             "why": "Excretion is waste leaving. The soot and gases leaving "
                    "the flame are excretion; the wax going in is nutrition."},
            {"text": "Growth", "correct": False,
             "why": "The flame grows when the wick is longer, which is a "
                    "different test. Material going in and being used up is "
                    "nutrition."},
            {"text": "Nutrition", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e16",
        "band": "easier",
        "text": "A robot vacuum plugs itself into its charger when the "
                "battery runs low. Why does that not count as nutrition?",
        "options": [
            {"text": "Because somebody had to plug the charger into the wall "
                     "in the first place.", "correct": False,
             "why": "Who set it up is not the point. A machine that wired "
                    "itself in would still be taking in electricity rather "
                    "than food."},
            {"text": "Because no food goes in and nothing is digested.",
             "correct": True},
            {"text": "Because it does it far too often for the word to mean "
                     "anything.", "correct": False,
             "why": "How often something happens never decides which process "
                    "it is. The problem is that electricity is not food."},
            {"text": "Because a battery stores electricity, not energy.",
             "correct": False,
             "why": "A battery does store energy — that part is right. What "
                    "is missing is food going in and being broken down."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e17",
        "band": "easier",
        "text": "Moss grows as a green patch on a damp wall and stays in that "
                "one spot. Which of the three boxes does it belong in?",
        "options": [
            {"text": "Never living — anything that stays in one spot for its "
                     "whole life is not alive.", "correct": False,
             "why": "An oak tree stays in one spot for two hundred years. "
                    "Staying put has never settled anything."},
            {"text": "Once living — it is the leftover green coating of "
                     "something that has gone.", "correct": False,
             "why": "Nothing has gone. The moss is growing where it is, out "
                    "of cells that are working today."},
            {"text": "Living — it is made of cells, and they are working now.",
             "correct": True},
            {"text": "Living — it is damp, and damp things are alive.",
             "correct": False,
             "why": "Damp is water and nothing more; a wet stone is damp too. "
                    "What settles it is the cells."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e18",
        "band": "easier",
        "text": "A leather boot has stood at the back of a cupboard for "
                "twenty years. Which of the three boxes does it belong in?",
        "options": [
            {"text": "Once living — leather is skin, and skin is built from "
                     "cells.", "correct": True},
            {"text": "Never living — a boot is put together in a factory "
                     "rather than grown.", "correct": False,
             "why": "A wooden spoon is shaped in a workshop and still goes in "
                    "“Once living”. Who made it is not the question."},
            {"text": "Never living — there is nothing alive left anywhere in "
                     "it.", "correct": False,
             "why": "There is nothing alive left in a lump of coal either, "
                    "and coal is “Once living”. The box asks what it came "
                    "from."},
            {"text": "Living — leather is still made of cells, so it counts "
                     "as alive.", "correct": False,
             "why": "Those cells stopped working when the hide was taken from "
                    "the animal. Leather came from something living; it is "
                    "not living itself."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e19",
        "band": "easier",
        "text": "Paper is made from wood pulp — tree fibres mashed up and "
                "pressed flat. Which box does a sheet of paper go in?",
        "options": [
            {"text": "Never living — the pulping mashes it so finely that no "
                     "cell can survive it.", "correct": False,
             "why": "Coal has no cells left in it at all and is still “Once "
                    "living”. The box asks what a thing came from."},
            {"text": "Once living — the fibres came from a tree, and a tree "
                     "is built from cells.", "correct": True},
            {"text": "Living — the fibres still have working cells, which is "
                     "why paper can be recycled.", "correct": False,
             "why": "Recycling is mashing and pressing the fibres again, not "
                    "growth. Those cells stopped when the tree was felled."},
            {"text": "Never living — paper is a material people make, not a "
                     "thing that grew.", "correct": False,
             "why": "People make wooden spoons and leather boots too, and "
                    "both came from something built from cells."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e20",
        "band": "easier",
        "text": "An iron nail is made from iron ore, dug out of the ground "
                "and melted down. Which box does the nail go in?",
        "options": [
            {"text": "Once living — anything dug out of the ground was "
                     "buried, and burying is for dead things.", "correct": False,
             "why": "Granite comes out of the same ground and was never "
                    "alive. Where a thing is found is not the test."},
            {"text": "Once living — iron is in your blood, so iron must come "
                     "from living things.", "correct": False,
             "why": "Your blood does carry iron, and the iron in a nail was "
                    "never inside anybody. It came out of rock."},
            {"text": "Never living — iron ore is rock, and no cell was ever "
                     "part of it.", "correct": True},
            {"text": "Never living — nothing once alive could be made into a "
                     "nail.", "correct": False,
             "why": "You could — bone and horn have both been carved into "
                    "tools. What settles it is where the iron came from."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e21",
        "band": "easier",
        "text": "A mushroom pushes up through the bark of a fallen log "
                "overnight. Which box does the mushroom go in?",
        "options": [
            {"text": "Living — its cells are working, which is how it grew "
                     "overnight.", "correct": True},
            {"text": "Once living — it is growing out of dead wood, so it is "
                     "part of the dead log.", "correct": False,
             "why": "It is feeding on the log, not made out of it. The "
                    "mushroom's own cells are working."},
            {"text": "Never living — a mushroom is neither a plant nor an "
                     "animal.", "correct": False,
             "why": "There are more kinds of living thing than those two. "
                    "What settles it is cells, and a mushroom is built from "
                    "them."},
            {"text": "Once living — it has no leaves, so it cannot feed "
                     "itself.", "correct": False,
             "why": "It takes its food from the log instead of making it, and "
                    "taking food in is nutrition."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e22",
        "band": "easier",
        "text": "Bread dough rises because it fills with bubbles of gas. "
                "Where does that gas come from?",
        "options": [
            {"text": "From air that was beaten into the dough while it was "
                     "being mixed.", "correct": False,
             "why": "Beaten-in air does not keep making more bubbles for an "
                    "hour. The gas is made by the yeast as it respires."},
            {"text": "From the water in the dough boiling in the warmth of "
                     "the kitchen.", "correct": False,
             "why": "A warm kitchen is nowhere near hot enough to boil water. "
                    "The gas comes from the yeast respiring the sugar."},
            {"text": "From the flour breaking down once it is wet.",
             "correct": False,
             "why": "Wet flour with no yeast in it makes no gas at all. It is "
                    "the yeast that is respiring."},
            {"text": "From the yeast respiring the sugar in the dough.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e23",
        "band": "easier",
        "text": "An acorn sitting in a drawer fails the nutrition test. Why "
                "does it fail that one?",
        "options": [
            {"text": "No food is going in — it lives off the store packed "
                     "inside it.", "correct": True},
            {"text": "The food inside it ran out long before it went into the "
                     "drawer.", "correct": False,
             "why": "The store is still there, and that is what it lives on. "
                    "What it is not doing is taking any new food in."},
            {"text": "A seed has no mouth, and nothing without a mouth can "
                     "feed.", "correct": False,
             "why": "A plant feeds with no mouth at all, by making its own "
                    "food. The acorn fails because nothing is going in."},
            {"text": "Nutrition happens during growth, and this acorn is not "
                     "growing.",
             "correct": False,
             "why": "Nutrition and growth are two separate tests. This one "
                    "turns on whether food is going in."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e24",
        "band": "easier",
        "text": "As a candle burns, carbon dioxide, water vapour and soot "
                "leave the flame. Which of the seven is that?",
        "options": [
            {"text": "Respiration", "correct": False,
             "why": "Respiration is reactions inside cells, and a flame has "
                    "none. Waste leaving something is excretion."},
            {"text": "Nutrition", "correct": False,
             "why": "Nutrition is the wax and the oxygen going in. What "
                    "leaves as waste is excretion."},
            {"text": "Excretion", "correct": True},
            {"text": "Sensitivity", "correct": False,
             "why": "Sensitivity is responding to a change, such as leaning "
                    "away from a draught. Waste leaving is excretion."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e25",
        "band": "easier",
        "text": "What does it mean when something is put in the box “Once "
                "living”?",
        "options": [
            {"text": "It was moving and feeding until quite recently, and has "
                     "died since.", "correct": False,
             "why": "A lump of coal has not moved for three hundred million "
                    "years and belongs there. The box is about cells, not "
                    "about recent behaviour."},
            {"text": "It came from something built from cells, and those "
                     "cells have stopped.", "correct": True},
            {"text": "It has a few cells left in it that are still working, "
                     "but slowly.", "correct": False,
             "why": "Then it would be Living. In this box the cells have "
                    "stopped working, or are gone altogether."},
            {"text": "It spent long enough underground to change into "
                     "something else.", "correct": False,
             "why": "Granite spent longer underground than coal and belongs "
                    "in “Never living”. Where it has been is not the test."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e26",
        "band": "easier",
        "text": "Yeast feeding on sugar in bread dough gets rid of two waste "
                "substances. What are they?",
        "options": [
            {"text": "Oxygen and water.", "correct": False,
             "why": "Oxygen is used up rather than made, and the water was "
                    "already in the dough. The waste is carbon dioxide and "
                    "alcohol."},
            {"text": "Sugar and flour.", "correct": False,
             "why": "Those are what goes in, not what comes out. What leaves "
                    "the yeast is carbon dioxide and alcohol."},
            {"text": "Soot and steam.", "correct": False,
             "why": "That is what leaves a candle flame as it burns. Yeast "
                    "gives out carbon dioxide and alcohol."},
            {"text": "Carbon dioxide and alcohol.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e27",
        "band": "easier",
        "text": "A robot vacuum runs on a battery. Why does it fail the "
                "respiration test?",
        "options": [
            {"text": "Nothing is broken down inside it to release energy.",
             "correct": True},
            {"text": "A battery gives out no heat while it is being used.", "correct": False,
             "why": "A battery does warm up in use. What is missing is food "
                    "being broken down inside cells."},
            {"text": "It stops moving the moment the battery goes flat.",
             "correct": False,
             "why": "An acorn does not move at all and respires all the same. "
                    "Stopping is not the point; having no cells is."},
            {"text": "Respiration means breathing, and a machine has no "
                     "lungs.", "correct": False,
             "why": "Breathing is not one of the seven. Respiration is "
                    "reactions inside cells, and most living things have no "
                    "lungs."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e28",
        "band": "easier",
        "text": "This unit uses the phrase “life process”. What is a life "
                "process?",
        "options": [
            {"text": "Any change that happens inside a living thing during "
                     "its life.", "correct": False,
             "why": "That would cover almost anything. There are seven named "
                    "processes, and each one is a job an organism does."},
            {"text": "One of the seven parts that every living thing is built "
                     "from.", "correct": False,
             "why": "The seven are things an organism does, not parts it is "
                    "made of. What it is built from is cells."},
            {"text": "One of the seven jobs that every living thing does.",
             "correct": True},
            {"text": "A job that needs a big organism to carry out.", "correct": False,
             "why": "A single yeast cell does all seven on its own. Size has "
                    "nothing to do with it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e29",
        "band": "easier",
        "text": "Touch a second wick to a burning candle and there are now "
                "two flames. Which of the seven does that count as?",
        "options": [
            {"text": "Growth", "correct": False,
             "why": "Growth is one flame getting bigger, which is what a "
                    "longer wick does. A second flame counts as "
                    "reproduction."},
            {"text": "Reproduction", "correct": True},
            {"text": "Movement", "correct": False,
             "why": "Movement is the flame climbing and leaning. A new flame "
                    "appearing is reproduction."},
            {"text": "Sensitivity", "correct": False,
             "why": "Sensitivity is the flame bending away from a draught. "
                    "Starting a second flame is reproduction."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-e30",
        "band": "easier",
        "text": "A candle flame passes the sensitivity test. Which of these "
                "is what it does that counts?",
        "options": [
            {"text": "It gives out more soot as the wax runs low.",
             "correct": False,
             "why": "Soot leaving the flame is excretion. Sensitivity is "
                    "responding to a change around it."},
            {"text": "It climbs above the wick rather than down.",
             "correct": False,
             "why": "That is movement — hot gas rising. Sensitivity is the "
                    "flame reacting to something that changes around it."},
            {"text": "It gets bigger when the wick is made longer.",
             "correct": False,
             "why": "That is growth. Sensitivity is responding to a change, "
                    "such as a draught reaching it."},
            {"text": "It leans away when a door opens and a draught reaches "
                     "it.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-01-s10",
        "band": "standard",
        "text": "Which of these is a plant carrying out sensitivity?",
        "options": [
            {"text": "Roots taking in water and minerals from the soil.",
             "correct": False,
             "why": "That is nutrition — material coming in. Sensitivity is "
                    "responding to a change around it."},
            {"text": "Pollen being carried from one flower to another.",
             "correct": False,
             "why": "That leads to reproduction. Sensitivity is the plant "
                    "itself responding to something outside it."},
            {"text": "A shoot bending towards the window it is nearest to.",
             "correct": True},
            {"text": "A seed splitting open and pushing a shoot out.",
             "correct": False,
             "why": "That is growth. Sensitivity is the plant responding to "
                    "something outside it, such as light."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s11",
        "band": "standard",
        "text": "A student decides the seven processes are a checklist: score "
                "four or more and you count as alive. Which one example "
                "destroys that rule?",
        "options": [
            {"text": "A candle flame, which does six of them and is not "
                     "alive.", "correct": True},
            {"text": "An acorn in a drawer, which does three of them and is "
                     "alive.", "correct": False,
             "why": "The rule says that four or more means alive. It claims "
                    "nothing about a thing that scores three, so this case "
                    "leaves it standing."},
            {"text": "A robot vacuum, which does two of them and is not "
                     "alive.", "correct": False,
             "why": "The rule already calls that one not alive, so it agrees "
                    "with the student. It cannot break the rule."},
            {"text": "A woodlouse, which does all seven of them and is "
                     "alive.", "correct": False,
             "why": "The rule agrees with that case too. To break a rule you "
                    "need a case where it gives the wrong answer."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s12",
        "band": "standard",
        "text": "A robot vacuum crosses the kitchen on its own and is exactly "
                "the size it was the day it left the factory. Which two of "
                "the seven does that tell you about?",
        "options": [
            {"text": "It fails movement, since somebody switched it on, and "
                     "fails growth.", "correct": False,
             "why": "Once it is on it crosses the room under its own power, "
                    "so movement is the one it passes."},
            {"text": "It passes growth, since it fills up with dust, and "
                     "passes movement.", "correct": False,
             "why": "Collecting dust is not building more of itself, so "
                    "growth is the one it fails."},
            {"text": "It passes movement and fails sensitivity, having no "
                     "feelings of its own.", "correct": False,
             "why": "Its sensors find the wall, the stairs and the dog, so "
                    "sensitivity is another it passes. Never getting bigger "
                    "is what fails growth."},
            {"text": "It passes movement and fails growth.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s13",
        "band": "standard",
        "text": "Thousands of identical robot vacuums exist. Why does the "
                "machine still fail the reproduction test?",
        "options": [
            {"text": "Because the copies are identical, and reproduction has "
                     "to make something different.", "correct": False,
             "why": "One yeast cell buds into two that are the same as each "
                    "other, and that is reproduction. The point is that the "
                    "machine does none of it."},
            {"text": "Because it plays no part in it — a factory makes the "
                     "next one.", "correct": True},
            {"text": "Because a machine cannot pass any one of the seven "
                     "tests.", "correct": False,
             "why": "It passes two of them: it moves, and it responds to what "
                    "is around it. This one it fails because a factory does "
                    "the work."},
            {"text": "It does pass it, because more of them keep being made "
                     "each year.", "correct": False,
             "why": "Something else is making them. Reproduction is the thing "
                    "itself producing the next one."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s14",
        "band": "standard",
        "text": "A mouse is found dead in the shed, with no mark on it. Which "
                "of the three boxes does it belong in now?",
        "options": [
            {"text": "Living — all of its cells are still there, so the mouse"
                     " still counts.", "correct": False,
             "why": "They are there and they have stopped working, which is "
                    "exactly what separates the two boxes."},
            {"text": "Once living — it was built from cells, and those cells "
                     "have stopped.", "correct": True},
            {"text": "Never living — it is a body now rather than an animal.",
             "correct": False,
             "why": "It was an animal built from cells, and that is what the "
                    "box asks about. Coal is not a plant any more either."},
            {"text": "Once living — it moved boxes the moment it stopped "
                     "moving.", "correct": False,
             "why": "Moving is not what settles it. What changed is that its "
                    "cells stopped working."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s15",
        "band": "standard",
        "text": "A cotton T-shirt and a glass bottle go into the same "
                "recycling bin. Glass is made by melting sand. Which box does "
                "each of them belong in?",
        "options": [
            {"text": "Both are never living, since neither has a working cell "
                     "in it.", "correct": False,
             "why": "The cotton grew on a cotton plant, so it came from "
                    "something built from cells. The glass did not."},
            {"text": "The cotton is once living and the glass is never "
                     "living.", "correct": True},
            {"text": "Both are once living, since both are made from natural "
                     "materials.", "correct": False,
             "why": "Sand is ground-up rock and nothing living was ever part "
                    "of it. Natural is not the same as once alive."},
            {"text": "The cotton is living, since cotton fibres are made of "
                     "cells.", "correct": False,
             "why": "Those cells stopped working when the cotton was picked. "
                    "The shirt came from something living; it is not living."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s16",
        "band": "standard",
        "text": "A dry acorn respires slowly enough to last four years in a "
                "drawer. Yeast in warm dough respires fast enough to fill the "
                "dough with gas inside an hour. What does that show?",
        "options": [
            {"text": "Both are respiring — what differs is the rate, not "
                     "whether they are alive.", "correct": True},
            {"text": "The yeast is respiring, and the acorn is not — it is "
                     "going stale.", "correct": False,
             "why": "The acorn respires the whole time, which is how it stays "
                    "alive for years. Going stale is not one of the seven."},
            {"text": "The yeast is more alive than the acorn, since it does "
                     "more in an hour.", "correct": False,
             "why": "There is no scale of aliveness. Both are built from "
                    "cells and both of those sets of cells are working."},
            {"text": "The acorn is saving its energy for later, and the yeast "
                     "is wasting its own.", "correct": False,
             "why": "Neither one is choosing anything. Each respires at the "
                    "rate its conditions allow."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s17",
        "band": "standard",
        "text": "Cork is the bark of a cork oak, cut away without killing the "
                "tree. Which box does a cork mat belong in?",
        "options": [
            {"text": "Living — the tree it came off is still alive, so the "
                     "cork is too.", "correct": False,
             "why": "The tree is alive; the cork is not part of it any more, "
                    "and its cells have stopped working."},
            {"text": "Never living — bark is the tree's outer covering rather "
                     "than part of the tree.", "correct": False,
             "why": "It is part of the tree, and the tree built it out of "
                    "cells. That is why it goes in “Once living”."},
            {"text": "Once living — a tree built the cork out of cells.",
             "correct": True},
            {"text": "Never living — anything taken off a plant without "
                     "killing it cannot count.", "correct": False,
             "why": "Wool is cut off a sheep without killing it and is “Once "
                    "living” all the same."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s18",
        "band": "standard",
        "text": "A student says a car must be alive: it takes in fuel, moves, "
                "senses obstacles and gives out exhaust gases. What is the "
                "best reply?",
        "options": [
            {"text": "It is not alive, because four of the seven is not "
                     "enough.", "correct": False,
             "why": "No number is enough. A candle flame does six and is not "
                    "alive; an acorn does three and is."},
            {"text": "It is not alive, because a person has to be driving it "
                     "for any of that to happen.", "correct": False,
             "why": "A car that drove itself would still not be alive. What "
                    "settles it is what the car is made of."},
            {"text": "It is not doing any of those things — it just looks as "
                     "though it is.", "correct": False,
             "why": "It genuinely does them, in the plain sense of the words. "
                    "Denying that dodges the point, which is that there is "
                    "not a cell in it."},
            {"text": "It does several of the seven, and none of that settles "
                     "it — a car has no cells.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s19",
        "band": "standard",
        "text": "Moss grows in one patch on a wall and never moves off it. A "
                "student says that means it cannot be alive. What is wrong "
                "with that reasoning?",
        "options": [
            {"text": "Moss does travel, as its patch spreads over the years.", "correct": False,
             "why": "A spreading patch is growth rather than travel — and "
                    "either way, movement is not what decides it."},
            {"text": "Nothing is wrong: a living thing has to be able to "
                     "move.", "correct": False,
             "why": "An oak tree stays put for two hundred years. What "
                    "settles it is that the moss is built from cells."},
            {"text": "Movement is one of the seven, and the seven do not "
                     "settle it — the moss has cells.", "correct": True},
            {"text": "The wind and the rain move the moss about, so it does "
                     "move.", "correct": False,
             "why": "Being pushed by something else is not the organism's own "
                    "doing, and it is not what makes moss alive."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s20",
        "band": "standard",
        "text": "A student says a tree cannot respire, because it has no "
                "lungs. What is wrong with that?",
        "options": [
            {"text": "A tree has lungs of a kind — the tiny holes on the "
                     "underside of each leaf.", "correct": False,
             "why": "Those holes let gases in and out, which is not what "
                    "lungs are, and respiration needs neither."},
            {"text": "Respiration happens inside cells, and breathing is not "
                     "one of the seven.", "correct": True},
            {"text": "Nothing: a tree takes its energy straight from sunlight "
                     "instead of respiring.", "correct": False,
             "why": "It makes food using light, then respires to release the "
                    "energy from that food, exactly as you do."},
            {"text": "A tree respires at night and photosynthesises instead "
                     "by day.", "correct": False,
             "why": "It respires day and night without a break. Respiration "
                    "is not an alternative to anything."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s21",
        "band": "standard",
        "text": "A robot vacuum's sensors find the wall, the stairs and the "
                "dog. A student says machines cannot be sensitive, so it "
                "fails that test. Is the student right?",
        "options": [
            {"text": "No — it genuinely responds to what is around it, and "
                     "responding never settles it.", "correct": True},
            {"text": "Yes — sensitivity means feeling, and a machine feels "
                     "nothing.", "correct": False,
             "why": "Sensitivity is detecting a change and responding to it. "
                    "The machine does exactly that, and is still not alive, "
                    "because it has no cells."},
            {"text": "Yes — people fitted those sensors, so the responding is"
                     " not its own.", "correct": False,
             "why": "Who fitted them does not change what the machine does. "
                    "The response is real."},
            {"text": "No — and passing sensitivity would make it alive.", "correct": False,
             "why": "Passing one of the seven has never made anything alive. "
                    "A candle flame passes six of them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s22",
        "band": "standard",
        "text": "A lump of coal formed about three hundred million years ago. "
                "A student says that is far too long ago for it still to "
                "count as “Once living”. What is the best reply?",
        "options": [
            {"text": "Three hundred million years is not long in the history "
                     "of the Earth.", "correct": False,
             "why": "Whether it counts as long is beside the point. The box "
                    "asks what the coal came from, not when."},
            {"text": "The student is right: after that long it should be "
                     "moved to “Never living”.", "correct": False,
             "why": "Then a wooden spoon would change boxes as it aged. Time "
                    "does not undo what something came from."},
            {"text": "It counts because the shapes of leaves can still be "
                     "found in some of it.", "correct": False,
             "why": "Coal with no leaf prints in it belongs in the same box. "
                    "It came from plants either way."},
            {"text": "How long ago it formed makes no difference to what it "
                     "came from.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s23",
        "band": "standard",
        "text": "Bread is baked at over two hundred degrees Celsius, which "
                "kills every yeast cell in the dough. Which box does a slice "
                "of the baked loaf belong in?",
        "options": [
            {"text": "Never living — the baking destroyed the cells, so "
                     "nothing living is left in it.", "correct": False,
             "why": "Coal has no cells left in it either and is “Once "
                    "living”. The box asks what a thing came from."},
            {"text": "Once living — it is made of flour and yeast, both built "
                     "from cells.", "correct": True},
            {"text": "Living — the yeast is asleep, and warm water would "
                     "start it again.", "correct": False,
             "why": "Baking kills it for good, which is why a baked loaf "
                    "never rises again. Those cells have stopped."},
            {"text": "Never living — cooking turns the ingredients into a "
                     "completely new material.", "correct": False,
             "why": "A cooked thing is still what it came from. Coal was "
                    "cooked underground for millions of years and is “Once "
                    "living”."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s24",
        "band": "standard",
        "text": "A bird's feather is picked up off the path. Which box does "
                "the feather belong in, and why?",
        "options": [
            {"text": "Once living — a bird built it out of cells, which then "
                     "died and hardened.", "correct": True},
            {"text": "Living — a feather carries on growing after it is shed, "
                     "the way a fingernail does.", "correct": False,
             "why": "Neither goes on growing once it is off the animal. The "
                    "cells in a feather stopped before it was even shed."},
            {"text": "Never living — the bird was the living part, and the "
                     "feather was not.", "correct": False,
             "why": "The bird built the feather out of cells, which is "
                    "exactly what “Once living” means."},
            {"text": "Once living — it counts because the bird it came from "
                     "must be dead.", "correct": False,
             "why": "Birds shed feathers and carry on living. What matters is "
                    "that the feather came from something built from cells."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s25",
        "band": "standard",
        "text": "A student writes: “The acorn passed three of the tests and "
                "the robot vacuum passed two, so the acorn is only just "
                "alive.” What is wrong with that?",
        "options": [
            {"text": "The acorn passed four of them, not three, so the gap is "
                     "wider than that.", "correct": False,
             "why": "Recounting does not help. Even on one test out of seven, "
                    "being built from cells would settle it."},
            {"text": "The vacuum passed three as well, so the two of them are "
                     "level on the tests.", "correct": False,
             "why": "It passes two. And either way, the scores are not what "
                    "decides which of them is alive."},
            {"text": "There is no “only just” — a score out of seven does not "
                     "decide the case.", "correct": True},
            {"text": "Nothing, except that the vacuum is the one that is only "
                     "just alive.", "correct": False,
             "why": "The vacuum is not alive at all. It is plastic, metal and "
                    "a battery, with no cells anywhere in it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s26",
        "band": "standard",
        "text": "Which pair of things would both go in the “Never living” "
                "box?",
        "options": [
            {"text": "A lump of coal and a wooden spoon.", "correct": False,
             "why": "Both of those are “Once living” — the coal formed from "
                    "plants and the spoon came from a tree."},
            {"text": "A robot vacuum and a leather boot.", "correct": False,
             "why": "The vacuum belongs there, but leather is skin, and skin "
                    "came from an animal built from cells."},
            {"text": "A stick of chalk and a candle flame.", "correct": False,
             "why": "The flame belongs there, but chalk is made from the "
                    "shells of sea creatures, so it is “Once living”."},
            {"text": "A granite pebble and a candle flame.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s27",
        "band": "standard",
        "text": "A daisy makes its own food out of light. A woodlouse eats "
                "dead leaves. Are both of them carrying out nutrition?",
        "options": [
            {"text": "Yes — nutrition covers taking food in and making your "
                     "own.", "correct": True},
            {"text": "No — just the woodlouse is, because nutrition means "
                     "food going in.", "correct": False,
             "why": "Making your own food is nutrition too. It is how every "
                    "green plant feeds itself."},
            {"text": "No — just the daisy is, because eating something dead "
                     "cannot count.", "correct": False,
             "why": "Where the food came from makes no difference at all. "
                    "Taking food in is nutrition."},
            {"text": "Yes, though it is the respiring afterwards that makes "
                     "it count.", "correct": False,
             "why": "Respiration is a separate one of the seven. Both are "
                    "carrying out nutrition in their own right."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s28",
        "band": "standard",
        "text": "An acorn in a drawer takes in no food, and yet something "
                "leaves it as waste. Where has that waste come from?",
        "options": [
            {"text": "From the food store inside it, leaking out slowly "
                     "through the shell.", "correct": False,
             "why": "The store is being used up, not leaking. The waste is "
                    "carbon dioxide, made when the acorn respires."},
            {"text": "From dust and damp that the shell picks up as it sits "
                     "in the drawer.", "correct": False,
             "why": "That was never part of the acorn, so losing it would not "
                    "be excretion at all."},
            {"text": "From its own slow respiration — carbon dioxide leaves "
                     "it.", "correct": True},
            {"text": "Nowhere: something that takes nothing in can give "
                     "nothing out.", "correct": False,
             "why": "It is respiring the store packed inside it, and that "
                    "makes carbon dioxide, which leaves it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s29",
        "band": "standard",
        "text": "Why is “it moves on its own” a poor test for deciding "
                "whether something is alive?",
        "options": [
            {"text": "Because movement is the hardest of the seven to watch "
                     "for in the first place.", "correct": False,
             "why": "It is the easiest to watch for. The trouble is that "
                    "watching it says nothing about what the thing is made "
                    "of."},
            {"text": "Because living things move far too slowly for anyone to "
                     "catch them at it.", "correct": False,
             "why": "A woodlouse under a lifted stone is quick enough. Speed "
                    "is not the problem; the test itself is."},
            {"text": "Because it is the moving of a living thing that counts "
                     "as movement.", "correct": False,
             "why": "That answer assumes what you are trying to find out. The "
                    "test fails because non-living things move too."},
            {"text": "Because a flame and a machine both do it, and an oak "
                     "tree does not.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-s30",
        "band": "standard",
        "text": "Which pair names something alive that never moves off its "
                "spot, and something that moves and is not alive?",
        "options": [
            {"text": "A woodlouse under a stone, and a granite pebble.",
             "correct": False,
             "why": "The woodlouse moves about, and a granite pebble does not "
                    "move at all. Neither one fits."},
            {"text": "Moss on a wall, and a candle flame.", "correct": True},
            {"text": "A candle flame, and a robot vacuum in a kitchen.",
             "correct": False,
             "why": "Neither of those is alive, so neither can be the first "
                    "of the two."},
            {"text": "Yeast in dough, and a wooden spoon.",
             "correct": False,
             "why": "Yeast moves through the dough as it grows, and a wooden "
                    "spoon does not move at all."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-01-h10",
        "band": "harder",
        "text": "A computer virus copies itself onto every machine it "
                "reaches. A biological virus copies itself once it is inside "
                "a cell. Which of the two is alive?",
        "options": [
            {"text": "The biological one, because it uses a real living cell "
                     "to do the copying.", "correct": False,
             "why": "Using a cell is not the same as being made of one, which "
                    "is why most biologists do not count viruses as living."},
            {"text": "Both, because anything that can make copies of itself "
                     "is reproducing.", "correct": False,
             "why": "A candle flame lights a second wick and a 3D printer "
                    "prints its own parts. Copying settles nothing."},
            {"text": "The computer one, because it spreads without needing "
                     "help from anything.", "correct": False,
             "why": "It needs a computer to run on, and it is a set of "
                    "instructions rather than a thing made of cells."},
            {"text": "Neither — copying is a behaviour, and neither one is "
                     "made of cells.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h11",
        "band": "harder",
        "text": "A salt crystal in a jar of drying salt water gets steadily "
                "bigger. A student says that growth proves it is alive. What "
                "is the difference between that and a living thing growing?",
        "options": [
            {"text": "Salt is settling onto the outside of the crystal; a "
                     "living thing builds itself.", "correct": True},
            {"text": "There is no difference — the crystal is growing, so the"
                     " crystal is alive.", "correct": False,
             "why": "It is growing, in the plain sense of the word. Growing "
                    "has never made anything alive, because no one of the "
                    "seven settles a case."},
            {"text": "The crystal grows while the water dries, so it stops "
                     "being alive once the jar is dry.", "correct": False,
             "why": "Nothing was alive in the jar to stop being alive. The "
                    "difference is in what the growing is, not in when it "
                    "happens."},
            {"text": "The crystal is not getting bigger; more crystals are "
                     "forming beside it.", "correct": False,
             "why": "One crystal genuinely does get bigger. Denying it dodges "
                    "the point, which is that a crystal has no cells."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h12",
        "band": "harder",
        "text": "Which rule would correctly sort a candle flame, an acorn in "
                "a drawer and a robot vacuum, all three at once?",
        "options": [
            {"text": "Ask whether it does at least three of the seven life "
                     "processes.", "correct": False,
             "why": "The flame does six and is not alive, so any rule that "
                    "counts processes gets the flame wrong."},
            {"text": "Ask whether it can move and respond without anybody "
                     "helping it.", "correct": False,
             "why": "The flame and the machine both can, and the acorn does "
                    "neither. That rule gets two of the three wrong."},
            {"text": "Ask whether it is built from cells.", "correct": True},
            {"text": "Ask whether it would still be there in a year if it "
                     "were left alone.", "correct": False,
             "why": "The acorn and the machine both would, and so would a "
                    "block of wax. Lasting is not one of the seven."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h13",
        "band": "harder",
        "text": "A student suggests a new rule: anything that makes waste is "
                "alive. Which single example shows the rule is wrong?",
        "options": [
            {"text": "An acorn in a drawer, which gives out carbon dioxide.", "correct": False,
             "why": "That case fits the rule rather than breaking it. To "
                    "break it you need something that makes waste and is not "
                    "alive."},
            {"text": "A candle flame, which gives out soot, water vapour and "
                     "carbon dioxide.", "correct": True},
            {"text": "A wooden spoon, which makes no waste and is not alive "
                     "either.", "correct": False,
             "why": "The rule says nothing about things that make no waste, "
                    "so this case cannot break it."},
            {"text": "A robot vacuum, which tips out the dust that it "
                     "collected off the floor.", "correct": False,
             "why": "That dust was never the machine's own waste, so it does "
                    "not even meet the rule."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h14",
        "band": "harder",
        "text": "“If it cannot move itself, it is not alive.” Which one of "
                "these breaks that idea?",
        "options": [
            {"text": "A candle flame, which moves about and is not alive.",
             "correct": False,
             "why": "That breaks the opposite idea — that whatever moves is "
                    "alive. This one it leaves standing."},
            {"text": "A granite pebble, which does not move and is not alive.",
             "correct": False,
             "why": "That case fits the idea. To break it you need something "
                    "that does not move and is alive."},
            {"text": "A robot vacuum, which moves and is not made of cells.",
             "correct": False,
             "why": "It moves, so the idea says nothing about it either way."},
            {"text": "An acorn in a drawer, which does not move and is "
                     "alive.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h15",
        "band": "harder",
        "text": "Most biologists do not count viruses as living things. How "
                "settled is that?",
        "options": [
            {"text": "Completely settled, because a virus is not made of "
                     "cells and the rule is clear enough.", "correct": False,
             "why": "The rule is clear. Where the line round “living” should "
                    "be drawn is the part that is argued about."},
            {"text": "Not settled, because a virus carries out the seven "
                     "processes once it is inside a cell.",
             "correct": False,
             "why": "It does not carry out all seven even then, and the seven "
                    "were never what settles a case."},
            {"text": "It is the usual view, but some argue the line is in the "
                     "wrong place.", "correct": True},
            {"text": "Settled the other way: viruses reproduce, so they are "
                     "alive.", "correct": False,
             "why": "Most biologists do not count them as living, and "
                    "reproducing has never settled anything on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h16",
        "band": "harder",
        "text": "Coal and granite are both dug out of the ground, and they go "
                "in different boxes. What makes the difference?",
        "options": [
            {"text": "Coal formed from squashed plants; granite formed from "
                     "molten rock as it cooled.", "correct": True},
            {"text": "Coal burns and granite does not, and burning is what "
                     "shows a thing was alive.", "correct": False,
             "why": "Plenty of things that were never alive will burn, and "
                    "burning is not one of the seven anyway."},
            {"text": "Coal is black and granite is speckled, which is how you "
                     "tell what each came from.", "correct": False,
             "why": "Colour tells you nothing about that. Chalk is white and "
                    "came from the shells of sea creatures."},
            {"text": "Coal is found nearer the surface, and shallow things "
                     "were the last to be buried.", "correct": False,
             "why": "Coal is mined from deep underground. Depth decides "
                    "nothing; what each one formed from does."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h17",
        "band": "harder",
        "text": "A wooden spoon and a steel spoon lie side by side in a "
                "drawer. Both were shaped in a factory. Why do they belong in "
                "different boxes?",
        "options": [
            {"text": "The wooden one is older, and anything old enough ends "
                     "up in “Once living”.", "correct": False,
             "why": "Age changes nothing. A spoon carved from a tree "
                    "yesterday is “Once living” from the moment it is cut."},
            {"text": "The wood came from a tree built from cells; the steel "
                     "came from rock.", "correct": True},
            {"text": "The wooden one still has working cells in it, and the "
                     "steel one has none.", "correct": False,
             "why": "Neither has a working cell. The wood's cells died when "
                    "the tree was cut, and where it came from is what puts it "
                    "in “Once living”."},
            {"text": "Being shaped in a factory should put them both in the "
                     "same box anyway.", "correct": False,
             "why": "Being shaped by people decides nothing — a leather boot "
                    "is made by people and came from an animal."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h18",
        "band": "harder",
        "text": "A woodlouse and a wooden spoon are both built out of cells. "
                "Why does only one of them go in the “Living” box?",
        "options": [
            {"text": "The woodlouse moves about, and the spoon has to be "
                     "carried.", "correct": False,
             "why": "Moving is one of the seven and the seven do not decide "
                    "it. What differs is whether the cells are working."},
            {"text": "A woodlouse has far more cells in it than a wooden "
                     "spoon has.", "correct": False,
             "why": "A single yeast cell is a whole living organism. Counting "
                    "cells settles nothing; whether they work does."},
            {"text": "The spoon's are plant cells, and plant cells are not "
                     "properly alive.", "correct": False,
             "why": "Plant cells are as alive as any other. The ones in that "
                    "spoon were alive until the tree was cut down."},
            {"text": "The woodlouse's cells are working; the spoon's stopped "
                     "when the tree was cut.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h19",
        "band": "harder",
        "text": "The candle flame passes six of the seven tests and the robot "
                "vacuum passes two. Neither is alive. What does comparing "
                "those two scores show?",
        "options": [
            {"text": "That the flame is a good deal closer to being alive "
                     "than the machine is.", "correct": False,
             "why": "There is no closer. Neither is made of cells, and there "
                    "is no scale between living and not living."},
            {"text": "That the seven tests work better on machines than they "
                     "do on flames.", "correct": False,
             "why": "They describe both perfectly well. Describing is all "
                    "they do, and neither score decides a case."},
            {"text": "That behaviour is a poor test in both directions.",
             "correct": True},
            {"text": "That a machine would have to pass four of them before "
                     "it counted as alive.", "correct": False,
             "why": "No number counts. A candle flame passes six and is still "
                    "not alive."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h20",
        "band": "harder",
        "text": "Yeast in dough and a candle flame both use up oxygen and "
                "both give out carbon dioxide. Why does only one of them "
                "count as respiring?",
        "options": [
            {"text": "Respiration is a controlled set of reactions in cells, "
                     "and only yeast has any.", "correct": True},
            {"text": "The yeast gives out alcohol too, and respiration must "
                     "make alcohol.", "correct": False,
             "why": "Respiration in your own cells produces no alcohol at "
                    "all. What matters is where the reactions happen."},
            {"text": "The flame uses up far more oxygen every second than the "
                     "yeast does.", "correct": False,
             "why": "How much is used makes no difference to what the process "
                    "is called."},
            {"text": "The yeast takes its oxygen from the dough, not from the"
                     " air.", "correct": False,
             "why": "The oxygen is in air trapped in the dough either way. "
                    "Where it comes from does not decide it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h21",
        "band": "harder",
        "text": "A candle flame gives out soot, and a robot vacuum tips out "
                "dust. Only one of those two counts as excretion. Which, and "
                "why?",
        "options": [
            {"text": "The vacuum — it gets rid of far more than the flame "
                     "does, and it does it on purpose.", "correct": False,
             "why": "Amount and intention do not come into it. That dust was "
                    "never made by the machine."},
            {"text": "The flame — the soot is made by the burning, while the "
                     "dust was only collected.", "correct": True},
            {"text": "The flame — because soot is solid, and excretion means "
                     "getting rid of solids.", "correct": False,
             "why": "Excretion covers gases and liquids too. What matters is "
                    "that the waste is the thing's own."},
            {"text": "The vacuum — because the flame's soot leaves on its "
                     "own, with nothing pushing it.", "correct": False,
             "why": "Waste leaving by itself is still excretion. The real "
                    "difference is where the waste came from."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h22",
        "band": "harder",
        "text": "Which pair shows both of these at once: something made of "
                "cells that is not alive, and something alive that fails most "
                "of the seven tests?",
        "options": [
            {"text": "A candle flame and an acorn that has been in a drawer "
                     "for years.", "correct": False,
             "why": "The flame is not made of cells at all, so it cannot be "
                    "the first of the two."},
            {"text": "A wooden spoon and a candle flame from the same "
                     "kitchen.", "correct": False,
             "why": "Neither of them is alive, so neither can be the second "
                    "of the two."},
            {"text": "A lump of coal and a robot vacuum in a kitchen.",
             "correct": False,
             "why": "Coal has no cells left in it and the vacuum never had "
                    "any. Neither one is alive."},
            {"text": "A wooden spoon and an acorn in a drawer.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h23",
        "band": "harder",
        "text": "A student puts a lump of coal in “Never living” and a candle "
                "flame in “Once living”. Both are the wrong way round. Which "
                "correction is right?",
        "options": [
            {"text": "Coal is once living because it burns; the flame is "
                     "never living because it burns things.", "correct": False,
             "why": "Burning decides neither one. The coal came from plants; "
                    "the flame came from nothing that had cells."},
            {"text": "Coal is living because it still holds energy; the flame "
                     "is never living because it gives energy out.",
             "correct": False,
             "why": "Holding energy is not being alive — a battery holds "
                    "energy. The coal's cells are long gone."},
            {"text": "Coal is once living because it formed from plants; the "
                     "flame is never living because it is hot gas.",
             "correct": True},
            {"text": "Coal is once living because it is very old; the flame "
                     "is never living because it lasts only minutes.",
             "correct": False,
             "why": "How long something lasts decides nothing. What each one "
                    "came from does."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h24",
        "band": "harder",
        "text": "What has to happen for something to move out of the "
                "“Living” box and into “Once living”?",
        "options": [
            {"text": "Its cells stop working, for good.", "correct": True},
            {"text": "It stops carrying out every one of the seven life "
                     "processes.", "correct": False,
             "why": "An acorn fails four of them and is alive. A process "
                    "stopping is not the same as the cells stopping."},
            {"text": "It stops moving and stops feeding.",
             "correct": False,
             "why": "A seed in a drawer does neither of those and is alive. "
                    "What changes is the cells."},
            {"text": "It is taken apart, so that it is no longer one whole "
                     "organism.", "correct": False,
             "why": "A leaf falls off a tree without the tree changing box. "
                    "What matters is whether the cells are working."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h25",
        "band": "harder",
        "text": "Two students disagree. One says the seven life processes are "
                "a test for life; the other says they only describe what "
                "living things do. Which evidence settles it?",
        "options": [
            {"text": "Every living thing carries out all seven of them at "
                     "some point in its life.", "correct": False,
             "why": "Even if that were so, it would not tell you that "
                    "whatever does them is alive. A flame does six."},
            {"text": "A candle flame does six of them and is not alive; an "
                     "acorn does three and is.", "correct": True},
            {"text": "Biologists have been using the seven processes for a "
                     "very long time indeed.", "correct": False,
             "why": "How long a list has been in use says nothing about what "
                    "it is able to decide."},
            {"text": "Seven of them is far too few to test anything properly.", "correct": False,
             "why": "The number is not the problem. A list of seventy "
                    "behaviours still would not say what a thing is made of."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h26",
        "band": "harder",
        "text": "Coal has no cells left in it, and living things are the "
                "things built from cells. So how can coal go in “Once "
                "living”?",
        "options": [
            {"text": "Because a few cells must be left somewhere in it, too "
                     "small for anyone to find.", "correct": False,
             "why": "There are none left at all. The box does not need any — "
                    "it asks what the coal came from."},
            {"text": "Because there is an exception for things that are "
                     "millions of years old.", "correct": False,
             "why": "There is no exception. The rule is about living things, "
                    "and coal is not one."},
            {"text": "Because coal would turn back into plants if it were "
                     "left underground for long enough.", "correct": False,
             "why": "Nothing turns back. Coal formed from plants and stays "
                    "coal."},
            {"text": "Because the box asks where it came from, and the rule "
                     "is about what is alive.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h27",
        "band": "harder",
        "text": "A student says: “The acorn is alive but it is doing nothing, "
                "so life must be able to pause and start again.” Is that "
                "right?",
        "options": [
            {"text": "Yes — the acorn's life pauses in the drawer and starts "
                     "again once it is planted.", "correct": False,
             "why": "Nothing starts again. The acorn is respiring from the "
                    "day it falls to the day it sprouts."},
            {"text": "Yes — and a wooden spoon would start again too, if "
                     "somebody planted it.", "correct": False,
             "why": "A spoon's cells are dead and nothing would start. That "
                    "is why it is “Once living” and the acorn is not."},
            {"text": "No — it is respiring the whole time it sits there, "
                     "slowly enough to last years.", "correct": True},
            {"text": "No — because the acorn is not alive until it is planted "
                     "and begins to grow.", "correct": False,
             "why": "It is alive in the drawer. Nothing switches on at "
                    "planting; the growing simply becomes visible."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h28",
        "band": "harder",
        "text": "Someone suggests adding an eighth life process to MRS GREN: "
                "being made of cells. What is wrong with that suggestion?",
        "options": [
            {"text": "The seven are things an organism does, and this is what "
                     "it is.", "correct": True},
            {"text": "Nothing, except that the initials would no longer spell"
                     " out a word.", "correct": False,
             "why": "The initials are only a memory trick. The real trouble "
                    "is that the list is of actions and this is not one."},
            {"text": "It is on the list already, because respiration happens "
                     "inside cells.", "correct": False,
             "why": "Respiration is a process; being made of cells is not. "
                    "There is no eighth item on the list."},
            {"text": "Cells belong on it, but then organs would need a ninth "
                     "place on the list.", "correct": False,
             "why": "Organs are parts rather than processes, exactly as cells "
                    "are. Neither belongs on a list of actions."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h29",
        "band": "harder",
        "text": "You are told that an object carries out all seven of the "
                "life processes. Can you be sure that it is alive?",
        "options": [
            {"text": "Yes — seven out of seven is the top score, so there is "
                     "nothing left to check.", "correct": False,
             "why": "A score has never settled it. A candle flame manages six "
                    "without a cell anywhere in it."},
            {"text": "No — you would still have to know whether it is built "
                     "from cells.", "correct": True},
            {"text": "Yes — nothing but a living thing could manage all seven"
                     " at once.", "correct": False,
             "why": "Nothing stops a non-living thing doing all seven; a "
                    "flame already does six. What it cannot have is cells."},
            {"text": "No — because nothing does all seven at once, so you "
                     "have been told something false.", "correct": False,
             "why": "Yeast in warm dough does all seven at once. The question "
                    "is still what it is made of."},
        ],
        "figure": None,
    },
    {
        "id": "b1-01-h30",
        "band": "harder",
        "text": "You are told that an object is built from cells, and that "
                "those cells are working. Can you be sure that it is alive?",
        "options": [
            {"text": "No — it would also have to carry out at least some of "
                     "the seven processes.", "correct": False,
             "why": "An acorn fails four of the seven and is alive. Cells "
                    "that are working settle it on their own."},
            {"text": "Yes, provided there are enough of them to make a whole "
                     "organism.", "correct": False,
             "why": "One working cell is a whole organism. Yeast manages on "
                    "exactly one."},
            {"text": "Yes — working cells are what being alive means.",
             "correct": True},
            {"text": "No — a wooden spoon is made of cells.", "correct": False,
             "why": "The spoon's cells stopped working long ago, which is the "
                    "difference this question turns on."},
        ],
        "figure": None,
    },
]
