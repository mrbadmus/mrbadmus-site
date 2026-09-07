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
            {"text": "Movement can happen inside an organism — roots push "
                     "down, leaves turn to the light.", "correct": True},
            {"text": "It cannot. A tree fails that one, and a living thing is "
                     "allowed to fail one.", "correct": False,
             "why": "No allowance is being made anywhere. The tree really "
                    "does move — the movement is inside it, rather than "
                    "across the ground."},
            {"text": "The wind moves its branches for it, and being moved "
                     "counts as movement.", "correct": False,
             "why": "Being pushed by something else is not the organism's own "
                    "doing. A wooden fence panel moves in the wind as well."},
            {"text": "A tree does travel, very slowly, over the whole two "
                     "hundred years.", "correct": False,
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
            {"text": "Both are once living, because both were made into "
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
            {"text": "Yes — reproduction is one of the seven, so anything "
                     "that never does it is not alive.", "correct": False,
             "why": "An acorn does three of the seven and is alive. A score "
                    "out of seven settles nothing; being made of cells "
                    "settles it."},
            {"text": "No — it is made of cells, and the seven describe what "
                     "living things do rather than deciding it.",
             "correct": True},
            {"text": "No — it counts because the queen reproduces on behalf "
                     "of the whole colony.", "correct": False,
             "why": "What another bee does cannot make this one alive. What "
                    "settles it is that this bee is built from cells."},
            {"text": "Yes, until it lays eggs — then it would count as fully "
                     "alive.", "correct": False,
             "why": "Nothing switches on. An acorn that never sprouts is "
                    "alive the whole time it sits in the drawer, for the same "
                    "reason."},
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
            {"text": "There is none — MRS GREN splits one process in two so "
                     "that the letters spell a word.", "correct": False,
             "why": "The letters are a memory trick, not the reason the two "
                    "are separate. Taking food in and releasing energy from "
                    "it are different jobs."},
            {"text": "Nutrition is what animals do, and respiration is what "
                     "plants do.", "correct": False,
             "why": "Every living thing does both. A plant makes its own food "
                    "and then respires to release the energy from it, exactly "
                    "as you do."},
            {"text": "Respiration means breathing air in and out; nutrition "
                     "means eating.", "correct": False,
             "why": "Breathing is not one of the seven at all. Respiration "
                    "is the reactions inside cells, and it happens in things "
                    "that never breathe."},
            {"text": "Nutrition is taking in or making food; respiration is "
                     "releasing energy from it inside cells.", "correct": True},
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
                    "living things do is exactly what a biologist needs. They "
                    "were never meant to be a test."},
            {"text": "They describe what living things do. They were never "
                     "what decides whether something is alive.",
             "correct": True},
            {"text": "The fire only appears to do them, and really does none "
                     "of the seven.", "correct": False,
             "why": "It genuinely does several, in the plain sense of the "
                    "words — which is why the candle flame lights six lamps. "
                    "Denying that dodges the point."},
            {"text": "They work perfectly well, but only on animals, which is "
                     "how a fire slips through them.", "correct": False,
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
            {"text": "No — it has been turned round, and a wooden spoon is "
                     "made of cells and is not alive.", "correct": True},
            {"text": "Yes — it is the same rule, written the other way "
                     "round.", "correct": False,
             "why": "Turning a rule round changes what it claims. “Every "
                    "living thing is made of cells” says nothing about a "
                    "spoon or a lump of coal, and neither is alive."},
            {"text": "No — the rule is that a thing is alive if it carries "
                     "out enough of the seven.", "correct": False,
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
]
