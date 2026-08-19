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
]
