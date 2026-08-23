"""C6 lesson 05 — Acids and carbonates: twelve questions (MRB-269).

The lesson's argument is that there are THREE products rather than two, that
the third one is the gas, and that a test worth anything has exactly one
answer. These twelve probe the angles the mastery ladder leaves alone.

The distractors are built from the lesson's declared misconception.

`ACID-08` (a gas that puts out a splint is carbon dioxide) drives e02, e04,
s01 and h01. s01 is the one that matters: it asks what a splint going out has
PROVED, and the honest answer — "not oxygen" — is the smallest claim on the
list, which is the point. h01 makes the student use two different gas tests on
two powders that behave identically until they are tested.

A second strand, everywhere on the page and in no register entry, is that the
apparatus has reasons. s02 puts the delivery tube above the limewater and asks
why a hard-fizzing tube produces no result, and s03 is Design's flag-10 step:
the limewater clearing again is honest behaviour and not a failure.

A third strand is that CARBONATES ARE A FAMILY. s04 and e03 are built on it —
the green one is still a carbonate, and marble, chalk and limestone are one
compound with three names.

A fourth strand is that a negative result is a result: h04's soil does not
fizz, and that is an answer about the soil.

h02 is the conservation question the unit has now asked three times in three
places, because an open flask losing mass is the one place a student can watch
"nothing is destroyed" appear to be false.

Every question here is new prose, and the bar is §13's. No correct answer is
strictly the longest in its set by four words or by 1.4x, and the twelve are
authored level across the four answer positions — three apiece (MRB-278).
"""

UNIT = "C6"
LESSON = "acids-and-carbonates"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-05-e01",
        "band": "easier",
        "text": "What three things does an acid make when it reacts with a "
                "carbonate?",
        "options": [
            {"text": "A salt, water and carbon dioxide", "correct": True},
            {"text": "A salt, water and hydrogen", "correct": False,
             "why": "Hydrogen is what a METAL gives with an acid. A carbonate "
                    "gives off carbon dioxide instead."},
            {"text": "A salt, hydrogen and carbon dioxide", "correct": False,
             "why": "There is no hydrogen here at all. The third product is "
                    "water, formed alongside the salt."},
            {"text": "Carbon dioxide, water and nothing else", "correct":
             False,
             "why": "The metal from the carbonate has to end up somewhere. It "
                    "becomes the salt, dissolved in the water."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e02",
        "band": "easier",
        "text": "Which test shows that a gas really is carbon dioxide?",
        "options": [
            {"text": "Holding a lit splint in it and watching it go out",
             "correct": False,
             "why": "Almost every gas puts a splint out. That narrows the "
                    "answer to 'not oxygen' and no further."},
            {"text": "Bubbling it through limewater and watching it turn "
                     "milky", "correct": True},
            {"text": "Holding damp red litmus paper in it until it turns blue",
             "correct": False,
             "why": "That is the test for ammonia. Carbon dioxide does not "
                    "turn red litmus blue."},
            {"text": "Holding a glowing splint in it and seeing it relight",
             "correct": False,
             "why": "A splint that relights is the test for oxygen. Carbon "
                    "dioxide does the opposite."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e03",
        "band": "easier",
        "text": "Marble, chalk and limestone are all the same compound. Which "
                "compound is it?",
        "options": [
            {"text": "Calcium chloride", "correct": False,
             "why": "That is the SALT made when the rock meets hydrochloric "
                    "acid. It is a product, not the rock."},
            {"text": "Calcium oxide", "correct": False,
             "why": "Calcium oxide is what is left after the carbonate has "
                    "been heated hard. The rock itself is the carbonate."},
            {"text": "Calcium carbonate", "correct": True},
            {"text": "Calcium hydroxide", "correct": False,
             "why": "Calcium hydroxide dissolved in water IS limewater. It "
                    "tests the gas rather than being the rock."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e04",
        "band": "easier",
        "text": "Dilute acid is dripped on a white powder and it fizzes. What "
                "makes sure the gas is carbon dioxide?",
        "options": [
            {"text": "Nothing — the fizzing is enough on its own",
             "correct": False,
             "why": "A metal fizzes with acid too, and that gas is hydrogen. "
                    "Fizzing says a reaction, not which gas."},
            {"text": "Holding a lit splint over the powder and listening",
             "correct": False,
             "why": "A splint can tell you whether it is hydrogen. It cannot "
                    "tell you the gas is carbon dioxide."},
            {"text": "Smelling the gas as it comes off the powder",
             "correct": False,
             "why": "Carbon dioxide has no smell, and no gas in a laboratory "
                    "is ever identified by smelling it."},
            {"text": "Collecting the gas and bubbling it through limewater",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-05-s01",
        "band": "standard",
        "text": "A gas is tested with a lit splint and the splint goes out. "
                "What has that proved?",
        "options": [
            {"text": "That the gas is carbon dioxide", "correct": False,
             "why": "Nitrogen and argon put a splint out as well. The test "
                    "cannot separate them from carbon dioxide."},
            {"text": "That the gas is not oxygen", "correct": True},
            {"text": "That no gas was given off at all", "correct": False,
             "why": "A splint going out is a result about the gas that was "
                    "there, not about there being none."},
            {"text": "That the gas must be hydrogen instead", "correct": False,
             "why": "Hydrogen announces itself with a squeaky pop. A splint "
                    "that goes out silently is not hydrogen."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s02",
        "band": "standard",
        "text": "A tube of marble and acid is fizzing hard, but the limewater "
                "never goes milky. What is the most likely reason?",
        "options": [
            {"text": "The acid was too dilute to make any gas", "correct":
             False,
             "why": "The tube is fizzing hard, so gas is certainly being "
                    "made. The problem is further along the apparatus."},
            {"text": "Limewater only works on gases that are warm",
             "correct": False,
             "why": "Temperature is no part of this test. Cold carbon dioxide "
                    "turns limewater milky just as well."},
            {"text": "The end of the delivery tube is above the limewater",
             "correct": True},
            {"text": "Marble gives off hydrogen rather than carbon dioxide",
             "correct": False,
             "why": "Carbonates give carbon dioxide. Hydrogen comes from a "
                    "metal, and there is no metal in the tube."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s03",
        "band": "standard",
        "text": "The limewater turns milky and then goes clear again while "
                "the bubbling carries on. What has happened?",
        "options": [
            {"text": "The test failed and has to be set up again",
             "correct": False,
             "why": "Nothing failed. The change to milky already happened, "
                    "and that change was the result."},
            {"text": "The reaction in the first tube has stopped making gas",
             "correct": False,
             "why": "The first tube is still bubbling. What changed is the "
                    "limewater, not the reaction feeding it."},
            {"text": "The limewater has been used up and is now plain water",
             "correct": False,
             "why": "Nothing has turned into water. The white solid has "
                    "dissolved again, into something colourless."},
            {"text": "Extra carbon dioxide has dissolved the white solid "
                     "again", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s04",
        "band": "standard",
        "text": "Copper carbonate is a green powder rather than a white one. "
                "What does that tell you about carbonates?",
        "options": [
            {"text": "They are a family of compounds, not one substance",
             "correct": True},
            {"text": "Copper carbonate is not really a carbonate at all",
             "correct": False,
             "why": "It fizzes with acid and gives carbon dioxide, which is "
                    "exactly what makes something a carbonate."},
            {"text": "The green colour means it will not react with acid",
             "correct": False,
             "why": "It fizzes hard and gives a blue-green solution. Colour "
                    "does not decide whether something reacts."},
            {"text": "Carbonates are white unless they have been contaminated",
             "correct": False,
             "why": "Nothing has contaminated it. The copper is part of the "
                    "compound, and copper compounds are coloured."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-05-h01",
        "band": "harder",
        "text": "Two white powders both fizz with acid. One gas turns "
                "limewater milky; the other pops with a lit splint. What are "
                "the powders?",
        "options": [
            {"text": "Both are carbonates, reacting at different speeds",
             "correct": False,
             "why": "Only one of them gave carbon dioxide. The other gave "
                    "hydrogen, and hydrogen comes from a metal."},
            {"text": "Both are metals, and one of them is impure",
             "correct": False,
             "why": "A metal gives hydrogen. The powder that turned limewater "
                    "milky gave carbon dioxide instead."},
            {"text": "One is a carbonate and the other is a metal",
             "correct": True},
            {"text": "One is a carbonate and the other is an alkali",
             "correct": False,
             "why": "An acid and an alkali give a salt and water and no gas "
                    "at all, so nothing would have fizzed."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h02",
        "band": "harder",
        "text": "Marble chips react with acid in an open flask standing on a "
                "balance, and the reading falls. Why?",
        "options": [
            {"text": "The marble has been destroyed by the acid",
             "correct": False,
             "why": "Nothing is destroyed in a reaction. The calcium is still "
                    "in the flask, dissolved as a salt."},
            {"text": "The acid evaporates away as the flask warms up",
             "correct": False,
             "why": "Far too little to weigh, and it would happen without the "
                    "marble too. What left is the gas."},
            {"text": "Solids weigh more than the liquids they dissolve into",
             "correct": False,
             "why": "Dissolving changes no mass at all. Sealed, this flask "
                    "would read the same at the end."},
            {"text": "Carbon dioxide has escaped from the open flask",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h03",
        "band": "harder",
        "text": "A granite statue and a limestone statue stand in the same "
                "rain, and only the limestone one loses its features. Why?",
        "options": [
            {"text": "Granite contains no carbonate for the rain to react "
                     "with", "correct": True},
            {"text": "Granite is harder, so the rain cannot wear it away",
             "correct": False,
             "why": "This is a chemical difference, not a physical one. The "
                    "same rain runs off granite and does nothing."},
            {"text": "Rainwater is only acidic where there is limestone "
                     "nearby", "correct": False,
             "why": "Rain is slightly acidic everywhere, because carbon "
                    "dioxide from the air dissolves into it."},
            {"text": "The granite statue was carved more recently than the "
                     "other", "correct": False,
             "why": "Age is not what decides it. A granite statue of the same "
                    "age still keeps its features."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h04",
        "band": "harder",
        "text": "A student drips acid onto a sample of soil and nothing "
                "fizzes. What is the honest conclusion?",
        "options": [
            {"text": "The acid must have been too weak to work",
             "correct": False,
             "why": "The same acid fizzes on marble in the dish beside it. "
                    "The result is about the soil."},
            {"text": "There is no carbonate in that sample of soil",
             "correct": True},
            {"text": "The gas came off too slowly for anyone to see it",
             "correct": False,
             "why": "A carbonate fizzes within seconds. Nothing appearing "
                    "means nothing was made."},
            {"text": "The soil has to be dried out before acid is added",
             "correct": False,
             "why": "Damp soil still fizzes if there is chalk in it. Drying "
                    "is not what is stopping this."},
        ],
        "figure": None,
    },
]
