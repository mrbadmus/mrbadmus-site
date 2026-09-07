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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-05-e05",
        "band": "easier",
        "text": "What is limewater used for?",
        "options": [
            {"text": "Testing for carbon dioxide — it turns milky when the "
                     "gas is bubbled through it",
             "correct": True},
            {"text": "Neutralising an acid spill on a bench, because it is an "
                     "alkali and will bring the pH back up to somewhere near "
                     "7 wherever it is poured",
             "correct": False,
             "why": "It is alkaline, and that is not what it is on the bench "
                    "for. It is the test for carbon dioxide"},
            {"text": "Testing for hydrogen",
             "correct": False,
             "why": "Hydrogen leaves limewater clear. It is tested with a lit "
                    "splint"},
            {"text": "Dissolving limestone",
             "correct": False,
             "why": "Acid dissolves limestone. Limewater is the detector, not "
                    "the solvent"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e06",
        "band": "easier",
        "text": "What is a specific test?",
        "options": [
            {"text": "A test that gives the same result every time it is "
                     "repeated, so that a single run can be trusted without "
                     "having to do it again",
             "correct": False,
             "why": "That is repeatability. A specific test is one that only "
                    "ONE substance can pass"},
            {"text": "A test only one substance can pass",
             "correct": True},
            {"text": "A test that has to be done in a particular order",
             "correct": False,
             "why": "Order matters in a method, and it is not what the word "
                    "means here"},
            {"text": "A test that measures how much of something there is",
             "correct": False,
             "why": "That is a quantitative measurement. Specific is about "
                    "identifying, not counting"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e07",
        "band": "easier",
        "text": "The end of the delivery tube has to go below the surface of "
                "the limewater. What goes wrong if it does not?",
        "options": [
            {"text": "The limewater would be sucked back up the tube into the "
                     "reaction, which is why the tube is always kept clear of "
                     "the liquid",
             "correct": False,
             "why": "Suck-back is a real hazard when a reaction is cooling, "
                    "and it is not this. The gas has to reach the limewater "
                    "at all"},
            {"text": "The limewater would go milky whatever gas was made",
             "correct": False,
             "why": "Limewater is specific to carbon dioxide, whatever the "
                    "tube does"},
            {"text": "The gas passes over the top and into the room, so "
                     "nothing is tested",
             "correct": True},
            {"text": "The gas would dissolve in the wrong part of the "
                     "limewater",
             "correct": False,
             "why": "Anywhere in the limewater will do. The problem is that "
                    "it never gets there"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e08",
        "band": "easier",
        "text": "A carbonate is dropped into acid. Which of the three "
                "products is the one you can see?",
        "options": [
            {"text": "The salt, which appears as a solid on the bottom of the "
                     "tube almost as soon as the acid is poured on",
             "correct": False,
             "why": "The salt dissolves in the water and is invisible. It "
                    "appears only if you evaporate the liquid"},
            {"text": "The water",
             "correct": False,
             "why": "It joins the water already in the tube, so nothing about "
                    "it can be seen"},
            {"text": "None of them",
             "correct": False,
             "why": "The fizzing is one of the three products leaving the "
                    "tube, and it is the giveaway"},
            {"text": "The carbon dioxide, as fizzing",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c6-05-s05",
        "band": "standard",
        "text": "Two students bubble the same gas through limewater. One "
                "stops as soon as it goes milky; the other carries on for two "
                "minutes and it goes clear. Who has the gas wrong?",
        "options": [
            {"text": "Neither — the change to milky is the result, and it "
                     "clears again if you keep going",
             "correct": True},
            {"text": "The second one, since a gas that leaves limewater clear "
                     "at the end of the test cannot have been carbon dioxide "
                     "at any point during it",
             "correct": False,
             "why": "It went milky first, which is the result. Extra gas "
                    "dissolves the white solid again"},
            {"text": "The first one, for stopping too early",
             "correct": False,
             "why": "Stopping at the milky stage is exactly right. That IS "
                    "the positive result"},
            {"text": "Both, because limewater is not a reliable test",
             "correct": False,
             "why": "It is the specific test for carbon dioxide. Nothing else "
                    "on a school bench turns it milky"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s06",
        "band": "standard",
        "text": "A boiling tube is specified rather than a test tube. Why?",
        "options": [
            {"text": "Because a boiling tube is thicker glass and will not "
                     "crack when it warms",
             "correct": False,
             "why": "Neither tube would crack here. The problem is the "
                    "fizzing throwing liquid up the sides"},
            {"text": "Because the fizzing throws liquid up the sides, and a "
                     "small tube delivers acid spray to whoever is holding it",
             "correct": True},
            {"text": "Because a boiling tube gives more gas",
             "correct": False,
             "why": "The gas depends on the amounts of carbonate and acid, "
                    "not on the glassware"},
            {"text": "Because a bung only fits a boiling tube",
             "correct": False,
             "why": "Bungs are made for both. The reason is what happens at "
                    "the top of a small tube"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s07",
        "band": "standard",
        "text": "Acid is dripped onto a field's soil and it fizzes steadily. "
                "What has the farmer learnt?",
        "options": [
            {"text": "That the soil is too acidic for a crop, since only an "
                     "acidic soil has anything in it that will react with "
                     "acid at all",
             "correct": False,
             "why": "Fizzing shows a CARBONATE, which is a base. If anything "
                    "it points the other way"},
            {"text": "That the soil holds a reactive metal",
             "correct": False,
             "why": "A metal would give hydrogen, which pops with a splint "
                    "and leaves limewater clear"},
            {"text": "That there is a carbonate — chalk or limestone — in the "
                     "soil",
             "correct": True},
            {"text": "That the soil is neutral",
             "correct": False,
             "why": "The test says what is in the soil rather than its pH. A "
                    "pH reading is a different measurement"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s08",
        "band": "standard",
        "text": "The bung with the delivery tube is fitted straight away "
                "rather than after the fizzing has settled down. Why?",
        "options": [
            {"text": "Because the acid would otherwise evaporate out of the "
                     "open tube",
             "correct": False,
             "why": "Almost no acid evaporates in that time. What is lost is "
                    "the gas"},
            {"text": "Because the bung is what starts the reaction",
             "correct": False,
             "why": "The reaction starts as soon as the acid touches the "
                    "carbonate. The bung only catches what it makes"},
            {"text": "Because an open tube lets air in and spoils the "
                     "limewater",
             "correct": False,
             "why": "Air in the tube does not spoil anything. Losing the gas "
                    "does"},
            {"text": "Because the reaction gives off its gas fastest at the "
                     "start, and anything that escapes first cannot be "
                     "tested",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-05-h05",
        "band": "harder",
        "text": "Limestone pavement above ground and cave systems below it "
                "are made by the same process. What is it?",
        "options": [
            {"text": "Slightly acidic rain reacting with the calcium "
                     "carbonate and dissolving it away along cracks",
             "correct": True},
            {"text": "Rain freezing in cracks and splitting the rock a little "
                     "each winter",
             "correct": False,
             "why": "Frost does shatter rock, and it is not what makes a cave "
                    "system. Slightly acidic rain reacts the limestone away"},
            {"text": "Rivers grinding the rock down with the sand they carry",
             "correct": False,
             "why": "Grinding widens a channel that already exists. The "
                    "channels themselves are opened chemically"},
            {"text": "Limestone melting in warm weather",
             "correct": False,
             "why": "Limestone melts at over 800 °C. Nothing outdoors melts "
                    "it"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h06",
        "band": "harder",
        "text": "A stalactite is described as the same reaction running "
                "backwards. What does that mean?",
        "options": [
            {"text": "The dripping water is alkaline, so it neutralises the "
                     "acid in the cave roof and leaves a solid behind as it "
                     "does so",
             "correct": False,
             "why": "There is no acid in the roof to neutralise. What is "
                    "happening is dissolved carbonate coming back out"},
            {"text": "Water carrying dissolved calcium carbonate dries out "
                     "and leaves the carbonate behind",
             "correct": True},
            {"text": "The carbon dioxide in the cave turns back into "
                     "limestone on the ceiling",
             "correct": False,
             "why": "The gas alone does not rebuild rock. The calcium "
                    "carbonate is carried there dissolved in water"},
            {"text": "The rock grows because acid is added to it",
             "correct": False,
             "why": "Acid takes limestone away. A stalactite grows where "
                    "water leaves it behind"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h07",
        "band": "harder",
        "text": "Carbon dioxide dissolving in the sea makes it slightly more "
                "acidic, and shells are calcium carbonate. Why does a change "
                "of a few tenths of a pH unit matter?",
        "options": [
            {"text": "Because a few tenths of a unit is a change of several "
                     "thousand times in acidity, which no living thing could "
                     "possibly survive",
             "correct": False,
             "why": "A whole unit is ten times, so a few tenths is far less "
                    "than that. It matters for what it does to carbonate"},
            {"text": "Because fish cannot live in acidic water of any kind",
             "correct": False,
             "why": "The sea stays alkaline overall. The problem is what the "
                    "shift does to carbonate structures"},
            {"text": "Because acid reacts with carbonate, so shells and coral "
                     "thicken more slowly or thin",
             "correct": True},
            {"text": "Because the carbon dioxide would otherwise stay in the "
                     "air",
             "correct": False,
             "why": "That is about climate rather than about shells. This "
                    "question is about the carbonate"},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h08",
        "band": "harder",
        "text": "A grey powder fizzes with acid, and the gas leaves "
                "limewater clear and pops with a lit splint. What is the "
                "powder?",
        "options": [
            {"text": "A carbonate, since fizzing with acid is what carbonates "
                     "do and no other kind of solid gives bubbles when acid "
                     "is poured on",
             "correct": False,
             "why": "A reactive metal fizzes too. The gas tests are what "
                    "separate the two, and this gas is hydrogen"},
            {"text": "An alkali",
             "correct": False,
             "why": "An alkali neutralises acid quietly. There is no gas at "
                    "all"},
            {"text": "Nothing can be said — two tests disagree",
             "correct": False,
             "why": "They agree perfectly. Clear limewater rules carbon "
                    "dioxide out and the pop identifies hydrogen"},
            {"text": "A reactive metal",
             "correct": True},
        ],
        "figure": None,
    },
]
