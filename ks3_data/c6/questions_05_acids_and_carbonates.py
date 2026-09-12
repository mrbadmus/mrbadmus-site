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

    # ── MRB-338 expansion ───────────
    {
        "id": "c6-05-e09",
        "band": "easier",
        "text": "When an acid reacts with a carbonate, where does the carbon dioxide "
                "come from?",
        "options": [
            {"text": "From the carbonate", "correct": True},
            {"text": "From the acid", "correct": False,
             "why": "The acid brings the hydrogen. The carbon and the oxygen were "
                    "locked into the carbonate."},
            {"text": "From the air above the tube", "correct": False,
             "why": "Nothing is drawn from the air. The same gas is produced in a "
                    "sealed flask."},
            {"text": "From the water in the acid", "correct": False,
             "why": "Water contains no carbon at all, so it cannot be the source of "
                    "carbon dioxide."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e10",
        "band": "easier",
        "text": "What is the chemical name of baking soda?",
        "options": [
            {"text": "Sodium chloride", "correct": False,
             "why": "That is table salt, which does not fizz with acid at all."},
            {"text": "Calcium carbonate", "correct": False,
             "why": "That is chalk, limestone and marble. Baking soda is a different"
                    " compound."},
            {"text": "Sodium hydroxide solution", "correct": False,
             "why": "That is the strong alkali in oven cleaner, and nobody puts it "
                    "in a cake."},
            {"text": "Sodium hydrogencarbonate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e11",
        "band": "easier",
        "text": "A carbonate is reacted with hydrochloric acid. Which family does the"
                " salt belong to?",
        "options": [
            {"text": "The sulfates", "correct": False,
             "why": "Sulfates come from sulfuric acid. The ending always comes from "
                    "the acid used."},
            {"text": "The nitrates", "correct": False,
             "why": "Nitrates come from nitric acid, which is a third acid again."},
            {"text": "The chlorides", "correct": True},
            {"text": "The carbonates", "correct": False,
             "why": "The carbonate is broken open by the acid. Its carbon leaves as "
                    "gas rather than staying in the salt."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e12",
        "band": "easier",
        "text": "Copper carbonate is added to hydrochloric acid. What colour is the "
                "solution that forms?",
        "options": [
            {"text": "Blue-green", "correct": True},
            {"text": "Colourless", "correct": False,
             "why": "Copper compounds carry a strong colour into solution, so the "
                    "liquid does not stay clear."},
            {"text": "Pale green", "correct": False,
             "why": "Pale green is what an iron salt gives. Copper is a deeper blue-"
                    "green."},
            {"text": "Bright orange", "correct": False,
             "why": "Nothing here is orange. Orange-brown is the colour of rust, "
                    "which is a different compound."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e13",
        "band": "easier",
        "text": "Four solids are tested with dilute acid. Which one gives no fizzing "
                "at all?",
        "options": [
            {"text": "Marble chips", "correct": False,
             "why": "Marble is calcium carbonate and fizzes steadily from every "
                    "surface."},
            {"text": "Baking soda", "correct": False,
             "why": "Baking soda is a carbonate and fizzes violently, because the "
                    "powder has a large surface."},
            {"text": "Copper carbonate", "correct": False,
             "why": "It is a carbonate, and it fizzes hard to give a blue-green "
                    "solution."},
            {"text": "Table salt", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e14",
        "band": "easier",
        "text": "Baking soda powder fizzes far more violently in acid than a marble "
                "chip does. Why?",
        "options": [
            {"text": "The powder has a far larger surface in contact with the acid", "correct": True},
            {"text": "The powder is a carbonate and the marble chip is not one at all", "correct": False,
             "why": "Both are carbonates. Both give a salt, water and carbon "
                    "dioxide."},
            {"text": "The powder makes a different gas, which escapes more quickly "
                      "than the other", "correct": False,
             "why": "Both give carbon dioxide, and both turn limewater milky."},
            {"text": "The powder dissolves in the acid without reacting with it at "
                      "all", "correct": False,
             "why": "It reacts, which is what the fizzing is. Simply dissolving "
                    "gives no gas."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e15",
        "band": "easier",
        "text": "Limewater is an alkali. What does that mean for a spill of it on the"
                " bench?",
        "options": [
            {"text": "It can be left, since alkalis do no harm to anything", "correct": False,
             "why": "Alkalis attack skin, and the strongest of them are the most "
                    "dangerous bottles in a laboratory."},
            {"text": "It should be washed off the bench and off skin", "correct": True},
            {"text": "It should be neutralised with the acid from the reaction tube", "correct": False,
             "why": "That adds a second corrosive liquid to the mess. Water is what "
                    "is used."},
            {"text": "It should be wiped up dry and put in the bin", "correct": False,
             "why": "Wiping spreads it and leaves alkali behind on the surface and "
                    "on the cloth."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e16",
        "band": "easier",
        "text": "What is the piece of apparatus that carries the gas from the "
                "reaction across to the limewater?",
        "options": [
            {"text": "A filter funnel", "correct": False,
             "why": "A funnel separates a solid from a liquid. It carries no gas "
                    "anywhere."},
            {"text": "A delivery tube", "correct": True},
            {"text": "A burette", "correct": False,
             "why": "A burette measures out a liquid a drop at a time and has no "
                    "part in collecting a gas."},
            {"text": "An evaporating basin", "correct": False,
             "why": "That is for driving water off a solution, which happens at the "
                    "end of a different experiment."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e17",
        "band": "easier",
        "text": "A marble chip is dropped into dilute acid. What happens to the chip?",
        "options": [
            {"text": "It floats to the surface and stays there unchanged", "correct": False,
             "why": "Marble is far denser than the acid and sinks, and it does not "
                    "stay unchanged."},
            {"text": "It swells up as the acid soaks into it", "correct": False,
             "why": "Nothing soaks in. The surface is reacted away, so the chip gets"
                    " smaller rather than larger."},
            {"text": "It gets smaller and streams bubbles", "correct": True},
            {"text": "It turns black but keeps its original size", "correct": False,
             "why": "There is no colour change, and the chip loses mass as the "
                    "reaction runs."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e18",
        "band": "easier",
        "text": "Sodium carbonate is added to hydrochloric acid. Which salt is made?",
        "options": [
            {"text": "Sodium chloride", "correct": True},
            {"text": "Sodium sulfate", "correct": False,
             "why": "Sulfates come from sulfuric acid. This reaction used "
                    "hydrochloric acid."},
            {"text": "Calcium chloride", "correct": False,
             "why": "The metal comes from the carbonate, and there is no calcium in "
                    "sodium carbonate."},
            {"text": "Sodium carbonate", "correct": False,
             "why": "That is the starting solid. The acid breaks it open and makes "
                    "something new."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e19",
        "band": "easier",
        "text": "Why is eye protection worn throughout the carbonate experiment?",
        "options": [
            {"text": "Because the fizzing throws liquid up the tube", "correct": True},
            {"text": "Because the carbon dioxide given off attacks the eyes", "correct": False,
             "why": "Carbon dioxide is the gas you breathe out. It is not what the "
                    "protection is for."},
            {"text": "Because the limewater glows brightly enough to dazzle", "correct": False,
             "why": "Limewater is a clear liquid and gives out no light whatever."},
            {"text": "Because the reaction gives off a bright flash at the start", "correct": False,
             "why": "There is no flash. The hazard is liquid being thrown about by "
                    "the bubbling."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e20",
        "band": "easier",
        "text": "Which of these would fizz if vinegar were poured onto it?",
        "options": [
            {"text": "A glass marble", "correct": False,
             "why": "Glass holds no carbonate and is not attacked by a weak acid "
                    "like vinegar."},
            {"text": "A plastic spoon", "correct": False,
             "why": "Plastic contains no carbonate, and vinegar does nothing to it "
                    "at all."},
            {"text": "A crushed eggshell", "correct": True},
            {"text": "A pebble of granite", "correct": False,
             "why": "Granite contains no carbonate, which is why granite gravestones"
                    " stay sharp in the rain."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s09",
        "band": "standard",
        "text": "An acid reacts with a carbonate and carbon dioxide is given off. "
                "Explain how you know the gas did not come out of the acid.",
        "options": [
            {"text": "Because the acid contains no carbon, and the carbonate carries "
                      "carbon and oxygen in it", "correct": True},
            {"text": "Because acids never take part in the reactions they are added "
                      "to at all", "correct": False,
             "why": "The acid is a reactant here and is used up. It simply does not "
                    "supply the carbon."},
            {"text": "Because carbon dioxide is always the gas an acid gives off, "
                      "whatever it meets", "correct": False,
             "why": "An acid gives hydrogen with a metal and no gas at all with an "
                    "alkali."},
            {"text": "Because the gas comes from the air that was dissolved in the "
                      "acid before the solid went in", "correct": False,
             "why": "Far more gas is produced than could ever have been dissolved in"
                    " a tube of liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s10",
        "band": "standard",
        "text": "Marble chips are crushed to a powder before being added to the same "
                "acid. Predict what changes.",
        "options": [
            {"text": "It fizzes faster and also gives much more gas in total", "correct": False,
             "why": "The same marble can only give the same gas. Crushing changes "
                    "the speed, not the amount."},
            {"text": "It fizzes at the same rate but gives more gas in total", "correct": False,
             "why": "Crushing has its whole effect on the rate. The total is set by "
                    "how much marble there is."},
            {"text": "It fizzes faster but gives the same gas in total", "correct": True},
            {"text": "It fizzes more slowly, because the powder packs down at the "
                      "bottom", "correct": False,
             "why": "A powder has far more surface exposed to the acid, so it reacts"
                    " faster rather than slower."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s11",
        "band": "standard",
        "text": "A carbonate and acid are reacted inside a stoppered flask standing "
                "on a balance. Predict the reading.",
        "options": [
            {"text": "It falls, because a gas always weighs less than the solid it "
                      "came from", "correct": False,
             "why": "The gas is still in the flask. Nothing has left, so nothing can"
                    " be missing."},
            {"text": "It rises, because a gas has been created that was not there "
                      "before", "correct": False,
             "why": "The gas is made from atoms that were already in the flask, so "
                    "no mass is added."},
            {"text": "It falls at first and then returns to where it started", "correct": False,
             "why": "There is no stage at which mass leaves a sealed flask and comes"
                    " back."},
            {"text": "It stays the same, because the gas cannot leave", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s12",
        "band": "standard",
        "text": "Why is the limewater tube the one to watch rather than the tube "
                "where the fizzing is?",
        "options": [
            {"text": "Because the fizzing tube is too dangerous to look at closely", "correct": False,
             "why": "It is watched perfectly safely behind eye protection. The "
                    "reason is where the result appears."},
            {"text": "Because the result of the test appears in the limewater, not in"
                      " the fizzing", "correct": True},
            {"text": "Because the fizzing tube changes colour as well, which is "
                      "confusing", "correct": False,
             "why": "Most carbonates give a colourless solution, and colour there is"
                    " not what the test reports."},
            {"text": "Because the fizzing stops before the limewater has begun to "
                      "react", "correct": False,
             "why": "The limewater changes while the fizzing is still going. That is"
                    " exactly why it must be watched."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s13",
        "band": "standard",
        "text": "Limescale in a kettle is calcium carbonate. Predict what happens "
                "when vinegar is poured in.",
        "options": [
            {"text": "Nothing, because vinegar is a food acid and too weak to attack "
                      "a solid", "correct": False,
             "why": "Vinegar attacks carbonates readily, which is exactly why it is "
                    "sold for descaling."},
            {"text": "The limescale hardens as the acid dries onto it", "correct": False,
             "why": "Nothing hardens. The deposit is reacted away and carried off in"
                    " the liquid."},
            {"text": "It fizzes and the limescale is reacted away", "correct": True},
            {"text": "The limescale turns to a black powder that can be poured out", "correct": False,
             "why": "There is no black powder. The carbonate becomes a soluble salt,"
                    " water and gas."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s14",
        "band": "standard",
        "text": "On a limestone gravestone the lettering goes first and the flat "
                "faces last. Suggest why.",
        "options": [
            {"text": "The letters were cut with a tool that weakened the stone along "
                      "the cuts", "correct": False,
             "why": "The same stone reacts at the same rate everywhere. What differs"
                    " is how much of it there is."},
            {"text": "The letters are the thinnest part, so they are lost first as "
                      "the surface reacts away", "correct": True},
            {"text": "Rain collects in the letters and dilutes the acid there, which "
                      "speeds it up", "correct": False,
             "why": "Diluting an acid slows an attack rather than speeding it, so "
                    "this cannot be the reason."},
            {"text": "The paint in the letters reacts with acid faster than stone "
                      "does", "correct": False,
             "why": "The stone itself is what is being lost, painted or not."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s15",
        "band": "standard",
        "text": "Sodium carbonate is added to dilute sulfuric acid. Name all three "
                "products.",
        "options": [
            {"text": "Sodium sulfate, water and carbon dioxide", "correct": True},
            {"text": "Sodium chloride, water and carbon dioxide", "correct": False,
             "why": "Chlorides come from hydrochloric acid. Sulfuric acid gives a "
                    "sulfate."},
            {"text": "Sodium sulfate, water and hydrogen", "correct": False,
             "why": "Hydrogen is what a metal gives. A carbonate gives carbon "
                    "dioxide instead."},
            {"text": "Sodium sulfate and carbon dioxide only", "correct": False,
             "why": "Water is made as well. A carbonate always gives all three."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s16",
        "band": "standard",
        "text": "Why is it fizzed, on its own, not enough to call an unknown solid a "
                "carbonate?",
        "options": [
            {"text": "Because fizzing only shows that the solid dissolved in the acid", "correct": False,
             "why": "Dissolving on its own gives no bubbles. Fizzing does mean a gas"
                    " is being produced."},
            {"text": "Because a reactive metal fizzes in acid too, and gives a "
                      "different gas", "correct": True},
            {"text": "Because carbonates do not always fizz, so the test can miss "
                      "them", "correct": False,
             "why": "Every carbonate on the bench fizzes with acid. The trouble is "
                    "what else does."},
            {"text": "Because fizzing means the acid was far too concentrated for a "
                      "fair test", "correct": False,
             "why": "Concentration changes the rate. Bubbles are the reaction, not a"
                    " fault in the method."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s17",
        "band": "standard",
        "text": "A marble chip and a magnesium strip are each dropped into dilute "
                "acid. What is the same and what is different?",
        "options": [
            {"text": "Both fizz and shrink, but the gases are different", "correct": True},
            {"text": "Both fizz and give off the same gas, which pops with a lit "
                      "splint", "correct": False,
             "why": "Only the magnesium gives hydrogen. The marble gives carbon "
                    "dioxide, which puts a splint out."},
            {"text": "Only the magnesium fizzes, because marble is a rock and rocks "
                      "do not react", "correct": False,
             "why": "Marble fizzes readily, which is why limestone buildings are "
                    "damaged by acid rain."},
            {"text": "Both fizz, and both leave a solid behind that can be filtered "
                      "off", "correct": False,
             "why": "Both solids disappear into solution. There is nothing left to "
                    "filter in either tube."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s18",
        "band": "standard",
        "text": "Baking soda is a carbonate with hydrogen in it. What does it do with"
                " an acid?",
        "options": [
            {"text": "Nothing, because the hydrogen makes it an acid rather than a "
                      "carbonate", "correct": False,
             "why": "It fizzes violently with acid, which no acid does with another "
                    "acid."},
            {"text": "It gives hydrogen, because the hydrogen in it is released as "
                      "gas", "correct": False,
             "why": "The gas turns limewater milky, so it is carbon dioxide rather "
                    "than hydrogen."},
            {"text": "The same as any carbonate: a salt, water and carbon dioxide", "correct": True},
            {"text": "It neutralises the acid without producing any gas at all", "correct": False,
             "why": "It does neutralise the acid, but the fizzing shows that gas is "
                    "produced as well."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s19",
        "band": "standard",
        "text": "A student bubbles the gas through a tube of plain water instead of "
                "limewater. What do they learn?",
        "options": [
            {"text": "That the gas is carbon dioxide, since water is what limewater "
                      "is made from", "correct": False,
             "why": "Limewater contains a dissolved alkali, and that is what "
                    "responds to the gas."},
            {"text": "That the gas is not carbon dioxide, since nothing happened in "
                      "the tube", "correct": False,
             "why": "Nothing would happen whatever the gas was, so no conclusion can"
                    " be drawn."},
            {"text": "That the gas dissolves, which identifies it well enough on its "
                      "own", "correct": False,
             "why": "Plenty of gases dissolve in water, so that would separate "
                    "nothing."},
            {"text": "Nothing about which gas it is, because plain water does not "
                      "change", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s20",
        "band": "standard",
        "text": "Crushed eggshell fizzes in vinegar and a glass marble does not. "
                "Explain the difference.",
        "options": [
            {"text": "Eggshell is a carbonate and glass is not", "correct": True},
            {"text": "Eggshell is softer, and soft solids always react with acid "
                      "while hard ones do not", "correct": False,
             "why": "Marble is hard and fizzes hard. Hardness does not decide "
                    "whether a solid reacts."},
            {"text": "Eggshell is porous, so the acid soaks in and pushes the air "
                      "back out as bubbles", "correct": False,
             "why": "The bubbles are carbon dioxide made by a reaction, not air "
                    "being displaced."},
            {"text": "Eggshell comes from a living thing and glass does not", "correct": False,
             "why": "Marble is rock and fizzes. Where a carbonate came from makes no"
                    " difference."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h09",
        "band": "harder",
        "text": "Explain why a carbonate gives an acid three products while a metal "
                "gives only two.",
        "options": [
            {"text": "Because a carbonate brings carbon and oxygen with it, and those"
                      " leave as a gas as well as making water", "correct": True},
            {"text": "Because a carbonate is a much bigger molecule, so it always "
                      "breaks into more pieces than a metal does", "correct": False,
             "why": "Size is not the reason. What matters is which atoms were "
                    "brought to the reaction."},
            {"text": "Because a metal reacts only once, while a carbonate reacts "
                      "twice over with the same acid", "correct": False,
             "why": "Each is one reaction. The difference is in what the atoms can "
                    "form."},
            {"text": "Because a metal makes no water, and water is what splits into "
                      "the third product", "correct": False,
             "why": "Water does not split into carbon dioxide. The carbon came from "
                    "the carbonate."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h10",
        "band": "harder",
        "text": "A limestone building has lost several millimetres of its surface "
                "over two hundred years. Explain where the stone has gone.",
        "options": [
            {"text": "It has been worn away by wind, which is why only exposed faces "
                      "are affected", "correct": False,
             "why": "Granite in the same weather keeps its detail, so the loss is "
                    "chemical rather than physical."},
            {"text": "It has reacted with slightly acidic rain into a soluble salt, "
                      "and been washed away", "correct": True},
            {"text": "It has crumbled because the stone dries out and cracks over "
                      "that length of time", "correct": False,
             "why": "Drying does not consume stone, and sheltered limestone keeps "
                    "its surface."},
            {"text": "It has been dissolved by rainwater, because calcium carbonate "
                      "dissolves in plain water", "correct": False,
             "why": "Calcium carbonate barely dissolves in water. It is the acid in "
                    "the rain that reacts with it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h11",
        "band": "harder",
        "text": "5.0 g of marble chips is added to a measured amount of acid. When "
                "the fizzing stops, 3.5 g of chips remain. What does that show?",
        "options": [
            {"text": "That marble only ever reacts to a fixed depth and then stops on"
                      " its own", "correct": False,
             "why": "A chip in plenty of acid is reacted away completely. Nothing "
                    "stops it part-way."},
            {"text": "That the acid ran out before the marble did", "correct": True},
            {"text": "That 1.5 g of the marble escaped as carbon dioxide and the rest"
                      " cannot react", "correct": False,
             "why": "Part of the lost mass did leave as gas, but the remaining chips"
                    " could still react if more acid were added."},
            {"text": "That the marble was only 30 per cent carbonate and the rest is "
                      "an impurity", "correct": False,
             "why": "Adding more acid would carry on dissolving the chips, which an "
                    "impurity would not allow."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h12",
        "band": "harder",
        "text": "A student says the acid must supply the carbon dioxide, because "
                "acids are what fizz. Evaluate that.",
        "options": [
            {"text": "Correct, because every acid gives off carbon dioxide when it "
                      "reacts with a solid", "correct": False,
             "why": "An acid with a metal gives hydrogen, and with an alkali it "
                    "gives no gas at all."},
            {"text": "Correct, because the fizzing stops as soon as the acid is used "
                      "up", "correct": False,
             "why": "The fizzing also stops when the carbonate is used up, so that "
                    "settles nothing."},
            {"text": "Wrong, because the same acid gives no gas at all with an "
                      "alkali, so the gas must come from the solid", "correct": True},
            {"text": "Wrong, because acids do not fizz and the bubbling comes from "
                      "the solid dissolving", "correct": False,
             "why": "Dissolving gives no bubbles. The fizzing is a real reaction "
                    "between the two."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h13",
        "band": "harder",
        "text": "Gas from marble chips and acid is collected in a syringe and the "
                "volume recorded every half minute. Describe how the volume changes.",
        "options": [
            {"text": "It rises steadily at the same rate until it suddenly stops", "correct": False,
             "why": "The rate falls off as the reactants are used up rather than "
                    "holding steady to the end."},
            {"text": "It rises slowly at first and then faster and faster until the "
                      "end", "correct": False,
             "why": "The fastest fizzing is at the start, when there is most acid "
                    "and most surface."},
            {"text": "It rises quickly at first, then more slowly, then stops", "correct": True},
            {"text": "It rises and then falls back as the gas is reabsorbed by the "
                      "liquid", "correct": False,
             "why": "The collected volume does not go down. Nothing pulls the gas "
                    "back out of the syringe."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h14",
        "band": "harder",
        "text": "The acid is warmed before the marble chips are added. What happens "
                "to the rate, and what happens to the total gas?",
        "options": [
            {"text": "The rate rises and the total gas rises with it", "correct": False,
             "why": "The total is set by how much marble and acid there are, and "
                    "warming changes neither."},
            {"text": "The rate is unchanged and the total gas rises", "correct": False,
             "why": "Warming has its whole effect on the rate. It cannot create "
                    "extra gas."},
            {"text": "The rate falls and the total gas falls with it", "correct": False,
             "why": "Warming speeds a reaction up rather than slowing it down."},
            {"text": "The rate rises and the total gas is unchanged", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h15",
        "band": "harder",
        "text": "An eggshell is left in a jar of vinegar for a week. Predict what is "
                "found, and explain it.",
        "options": [
            {"text": "The shell is unchanged, because vinegar is too weak an acid to "
                      "attack it", "correct": False,
             "why": "Vinegar attacks a carbonate steadily, and a week is a long time"
                    " for a thin shell."},
            {"text": "The shell has reacted away, with carbon dioxide given off along"
                      " the way", "correct": True},
            {"text": "The shell has hardened, because the acid has dried into its "
                      "surface", "correct": False,
             "why": "Nothing dries in a full jar, and the shell loses material "
                    "rather than gaining it."},
            {"text": "The shell has turned into limestone, since both are made of the"
                      " same thing", "correct": False,
             "why": "It starts out as the same compound as limestone. The acid takes"
                    " it apart rather than converting it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h16",
        "band": "harder",
        "text": "Crushed limestone is spread in a stream that carries acidic run-off."
                " Predict what happens, and explain why.",
        "options": [
            {"text": "Nothing, because limestone is a rock and rocks do not react "
                      "with acid at all", "correct": False,
             "why": "Limestone is calcium carbonate, and it is one of the most "
                    "readily attacked rocks there is."},
            {"text": "The stream turns more acidic, because the limestone adds carbon"
                      " dioxide to the water", "correct": False,
             "why": "The carbonate consumes acid. Any gas given off leaves the water"
                    " rather than acidifying it."},
            {"text": "The limestone sets hard and seals the bed of the stream against"
                      " the acid", "correct": False,
             "why": "The limestone is consumed by the acid rather than forming a "
                    "seal over it."},
            {"text": "The acid is neutralised, fizzing as carbon dioxide is given off", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e21",
        "band": "easier",
        "text": "Limewater is a solution of one compound in water. Which compound?",
        "options": [
            {"text": "Calcium hydroxide", "correct": True},
            {"text": "Calcium carbonate", "correct": False,
             "why": "Calcium carbonate is the rock being tested rather than the "
                    "liquid doing the testing."},
            {"text": "Sodium chloride", "correct": False,
             "why": "Salt water has no effect on any gas bubbled through it."},
            {"text": "Hydrochloric acid", "correct": False,
             "why": "Limewater is alkaline, which an acid could not be."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e22",
        "band": "easier",
        "text": "A gas is bubbled through limewater for a while and the limewater stays"
                " perfectly clear. What does that show?",
        "options": [
            {"text": "That the gas is hydrogen", "correct": False,
             "why": "The test rules one gas out; it does not name the one you "
                    "have."},
            {"text": "That the limewater has gone off", "correct": False,
             "why": "Clear limewater is exactly what fresh limewater looks like "
                    "before a test."},
            {"text": "That the gas is not carbon dioxide", "correct": True},
            {"text": "That the test has failed and must be repeated",
             "correct": False,
             "why": "A test that correctly reports nothing has worked, not "
                    "failed."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e23",
        "band": "easier",
        "text": "What does limewater look like in the tube before any gas is bubbled"
                " through it?",
        "options": [
            {"text": "Milky white and cloudy", "correct": False,
             "why": "Milky white is the result of the test, so it cannot be the "
                    "starting state."},
            {"text": "Clear and colourless", "correct": True},
            {"text": "Pale green", "correct": False,
             "why": "Pale green belongs to an iron solution, not to limewater."},
            {"text": "Blue-green", "correct": False,
             "why": "Blue-green belongs to a copper solution, not to limewater."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e24",
        "band": "easier",
        "text": "A carbonate holds an element inside it that a metal does not, and that"
                " element leaves in the gas. Which element is it?",
        "options": [
            {"text": "Hydrogen", "correct": False,
             "why": "Hydrogen comes out of the acid, and it leaves as a gas only "
                    "when a metal is used instead."},
            {"text": "Carbon", "correct": True},
            {"text": "Sulfur", "correct": False,
             "why": "Sulfur comes in with sulfuric acid, and it stays behind in "
                    "the salt."},
            {"text": "Chlorine", "correct": False,
             "why": "Chlorine comes in with hydrochloric acid, and it stays "
                    "behind in the salt."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e25",
        "band": "easier",
        "text": "Calcium carbonate reacts with hydrochloric acid. Name the salt that"
                " is made.",
        "options": [
            {"text": "Calcium chloride", "correct": True},
            {"text": "Calcium sulfate", "correct": False,
             "why": "Sulfates come from sulfuric acid, which is not the acid "
                    "here."},
            {"text": "Calcium carbonate", "correct": False,
             "why": "That is the solid that was added rather than the new "
                    "substance made."},
            {"text": "Hydrogen chloride", "correct": False,
             "why": "The metal from the carbonate has to be the first part of the "
                    "salt's name."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e26",
        "band": "easier",
        "text": "Water is one of the three products of this reaction. Where is that"
                " water at the end?",
        "options": [
            {"text": "It has left the tube along with the gas", "correct": False,
             "why": "Only the carbon dioxide leaves; the water is a liquid and "
                    "stays."},
            {"text": "It is in the tube, with the salt dissolved in it",
             "correct": True},
            {"text": "It has turned into the carbon dioxide", "correct": False,
             "why": "They are two separate products, and neither becomes the "
                    "other."},
            {"text": "It has been absorbed by the solid that is left",
             "correct": False,
             "why": "Nothing soaks the water up; it joins the liquid already "
                    "there."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e27",
        "band": "easier",
        "text": "A carbonate is reacting steadily in a tube of dilute acid. What is"
                " happening to the acid while that goes on?",
        "options": [
            {"text": "It is gradually used up", "correct": True},
            {"text": "It is left completely unchanged", "correct": False,
             "why": "The acid is a reactant, so it is consumed along with the "
                    "carbonate."},
            {"text": "It is turned into more carbonate", "correct": False,
             "why": "The carbonate is being broken open rather than made."},
            {"text": "It becomes more concentrated as the reaction runs",
             "correct": False,
             "why": "Water is made by the reaction, so if anything the acid ends "
                    "more dilute."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e28",
        "band": "easier",
        "text": "Marble chips are left in plenty of acid until every chip has gone."
                " What is in the tube at the end?",
        "options": [
            {"text": "Nothing at all, because everything left as gas",
             "correct": False,
             "why": "Only one of the three products is a gas; two of them stay in "
                    "the tube."},
            {"text": "A solution of the salt in water", "correct": True},
            {"text": "A layer of solid salt under clear water", "correct": False,
             "why": "The salt made here dissolves as it forms rather than sitting "
                    "at the bottom."},
            {"text": "Pure water, with the salt gone with the bubbles",
             "correct": False,
             "why": "The salt cannot leave with a gas; it stays dissolved in the "
                    "tube."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e29",
        "band": "easier",
        "text": "A geologist drips dilute acid onto a rock in the field and it fizzes."
                " What does the rock contain?",
        "options": [
            {"text": "A metal that is above hydrogen", "correct": False,
             "why": "A metal would give a gas that pops with a lit splint rather "
                    "than one that turns limewater milky."},
            {"text": "An alkali", "correct": False,
             "why": "An alkali neutralises an acid without giving off any gas at "
                    "all."},
            {"text": "A carbonate", "correct": True},
            {"text": "A salt such as sodium chloride", "correct": False,
             "why": "Table salt sits in acid and does nothing but dissolve."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e30",
        "band": "easier",
        "text": "Baking soda is put into a cake mixture and the cake rises in the oven."
                " Which gas lifts it?",
        "options": [
            {"text": "Hydrogen", "correct": False,
             "why": "Hydrogen comes from a metal and an acid, and there is no "
                    "metal in a cake."},
            {"text": "Oxygen", "correct": False,
             "why": "No oxygen is released by a carbonate reacting with an acid."},
            {"text": "Steam and nothing else", "correct": False,
             "why": "Steam is made by the heat, but the baking soda is there for "
                    "a gas of its own."},
            {"text": "Carbon dioxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e31",
        "band": "easier",
        "text": "Name the salt made when copper carbonate is added to hydrochloric"
                " acid.",
        "options": [
            {"text": "Copper carbonate", "correct": False,
             "why": "That is the green powder that was added rather than the new "
                    "substance made."},
            {"text": "Copper chloride", "correct": True},
            {"text": "Copper nitrate", "correct": False,
             "why": "Nitrates come from nitric acid, which is not the acid used "
                    "here."},
            {"text": "Copper hydroxide", "correct": False,
             "why": "A hydroxide is an alkali rather than the salt an acid "
                    "makes."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-e32",
        "band": "easier",
        "text": "The reaction is run in a flask sealed with a stopper and no delivery"
                " tube. Where does the carbon dioxide go?",
        "options": [
            {"text": "It is pushed back into the liquid and disappears",
             "correct": False,
             "why": "A little dissolves, but the gas is not destroyed by being "
                    "kept in."},
            {"text": "It escapes through the glass of the flask", "correct": False,
             "why": "Glass does not let a gas through, which is why a stopper "
                    "works at all."},
            {"text": "It stays inside the flask", "correct": True},
            {"text": "It stops being made once the flask is sealed",
             "correct": False,
             "why": "The reaction carries on and goes on producing gas inside the "
                    "flask."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s21",
        "band": "standard",
        "text": "Marble chips are added to dilute hydrochloric acid. Name all "
                "three products.",
        "options": [
            {"text": "Calcium sulfate, water and carbon dioxide", "correct": False,
             "why": "A sulfate would need sulfuric acid, and this tube holds "
                    "hydrochloric."},
            {"text": "Calcium chloride, water and hydrogen", "correct": False,
             "why": "Hydrogen is what a metal gives; a carbonate gives carbon "
                    "dioxide instead."},
            {"text": "Calcium carbonate, water and carbon dioxide", "correct": False,
             "why": "The carbonate is a reactant here, not one of the "
                    "products."},
            {"text": "Calcium chloride, water and carbon dioxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s22",
        "band": "standard",
        "text": "Geologists carry a small bottle of dilute acid into the field. Explain"
                " what it is for.",
        "options": [
            {"text": "To clean the dirt off a rock so its colour can be seen",
             "correct": False,
             "why": "Acid would attack some of the rocks it was meant to be "
                    "cleaning."},
            {"text": "To find out in seconds whether a rock holds a carbonate",
             "correct": True},
            {"text": "To measure how hard a rock is by how fast it dissolves",
             "correct": False,
             "why": "Hardness is tested by scratching, and it is a physical "
                    "property rather than a chemical one."},
            {"text": "To find out whether a rock contains any metal at all",
             "correct": False,
             "why": "Most rocks hold metal compounds that do not react with acid "
                    "in this way."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s23",
        "band": "standard",
        "text": "Three of the four solids on the bench look almost identical in the"
                " bottle. Explain why looking at them cannot sort them.",
        "options": [
            {"text": "Because the bottles are not labelled clearly enough",
             "correct": False,
             "why": "A label would settle it, which shows the trouble is that "
                    "looking tells you nothing."},
            {"text": "Because white powders have to be warmed before they can be "
                      "told apart", "correct": False,
             "why": "Warming is no more revealing than looking; the acid is what "
                    "separates them."},
            {"text": "Because what a substance looks like says nothing about what "
                      "it will do", "correct": True},
            {"text": "Because all white powders are chemically the same",
             "correct": False,
             "why": "Two of these fizz and one does nothing, so they are plainly "
                    "not the same."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s24",
        "band": "standard",
        "text": "A gas syringe reads 24 cm³ after 30 seconds and 36 cm³ after 60"
                " seconds. Calculate the volume collected during the second 30"
                " seconds.",
        "options": [
            {"text": "36 cm³", "correct": False,
             "why": "36 cm³ is the running total after a minute, not the amount "
                    "added in the second half of it."},
            {"text": "24 cm³", "correct": False,
             "why": "That repeats the first half minute instead of working out "
                    "the second."},
            {"text": "60 cm³", "correct": False,
             "why": "That adds the two readings, but the second already includes "
                    "the first."},
            {"text": "12 cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s25",
        "band": "standard",
        "text": "The gas given off when magnesium is dropped into dilute acid "
                "is bubbled through limewater. Predict what happens to it.",
        "options": [
            {"text": "It turns milky, because all gases from acids do", "correct": False,
             "why": "Only carbon dioxide does that, and this gas is not carbon "
                    "dioxide."},
            {"text": "It turns milky and then clears again straight away", "correct": False,
             "why": "That happens with a great deal of carbon dioxide, and "
                    "none is present here."},
            {"text": "It turns blue, because the gas is slightly alkaline", "correct": False,
             "why": "Limewater has no blue stage, and hydrogen is not "
                    "alkaline."},
            {"text": "It stays clear", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s26",
        "band": "standard",
        "text": "The limewater tube is watched from the moment the bubbling starts"
                " rather than only at the end. Explain why.",
        "options": [
            {"text": "Because the limewater is clear again by the end if bubbling "
                      "continues", "correct": True},
            {"text": "Because limewater only works during the first few seconds "
                      "of a test", "correct": False,
             "why": "It goes on reporting the gas throughout; it is the milky "
                    "stage that can be passed."},
            {"text": "Because the gas arrives before the reaction has properly "
                      "started", "correct": False,
             "why": "Gas cannot arrive before the reaction that makes it."},
            {"text": "Because the fizzing stops as soon as the limewater changes",
             "correct": False,
             "why": "The two tubes are independent; the reaction carries on "
                    "regardless."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s27",
        "band": "standard",
        "text": "A student uses a small test tube rather than a boiling tube for the"
                " carbonate and acid. Predict what happens.",
        "options": [
            {"text": "The reaction gives a different gas in a smaller tube",
             "correct": False,
             "why": "The gas is set by the chemistry, not by the size of the "
                    "glassware."},
            {"text": "The fizzing throws liquid out of the top of the tube",
             "correct": True},
            {"text": "The reaction is slower, because there is less room for it",
             "correct": False,
             "why": "The space above the liquid does not change how fast the "
                    "solid and the acid meet."},
            {"text": "The limewater turns milky more quickly than it should",
             "correct": False,
             "why": "The limewater reports the gas that reaches it, at whatever "
                    "rate it arrives."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s28",
        "band": "standard",
        "text": "Marble and acid give a colourless solution, while copper carbonate"
                " and the same acid give a blue-green one. Explain the difference.",
        "options": [
            {"text": "The copper reaction gives off a coloured gas that stains the "
                      "liquid", "correct": False,
             "why": "The gas is carbon dioxide in both, and it is colourless."},
            {"text": "The copper carbonate has not fully reacted and is still colouring the water it sits in", "correct": False,
             "why": "The colour appears even when every grain of the powder has "
                    "gone."},
            {"text": "The metal from the carbonate ends up in the salt, and "
                      "copper salts are coloured", "correct": True},
            {"text": "The acid changes colour when it meets a green powder",
             "correct": False,
             "why": "The acid is colourless before and after; it is the new salt "
                    "that carries the colour."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s29",
        "band": "standard",
        "text": "Acid is dripped on two rocks. One fizzes steadily for a minute; the"
                " other gives a few bubbles that stop almost at once. Compare them.",
        "options": [
            {"text": "Only the first holds a carbonate; the second holds none",
             "correct": False,
             "why": "Bubbles at all mean a carbonate is present, however few of "
                    "them there are."},
            {"text": "The first holds far more carbonate than the second",
             "correct": True},
            {"text": "The second holds more carbonate, released more quickly",
             "correct": False,
             "why": "A reaction that stops at once has run out of carbonate, "
                    "which means there was less of it."},
            {"text": "Both hold the same carbonate, and the acid was weaker on "
                      "the second", "correct": False,
             "why": "The same acid was dripped on both, so the rock is what "
                    "differs."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s30",
        "band": "standard",
        "text": "A class follows this reaction with a gas syringe rather than by"
                " standing the flask on a balance. Suggest why.",
        "options": [
            {"text": "Because a balance cannot be used while a reaction is running",
             "correct": False,
             "why": "A balance works perfectly well during a reaction; it is what "
                    "it reports that is small."},
            {"text": "Because the gas escapes a balance but not a syringe",
             "correct": False,
             "why": "Gas escapes an open flask either way; the syringe catches it "
                    "because it is connected."},
            {"text": "Because the volume changes are large and easy to read",
             "correct": True},
            {"text": "Because a syringe measures the mass of gas directly",
             "correct": False,
             "why": "A syringe reports a volume; mass is what a balance would "
                    "give."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s31",
        "band": "standard",
        "text": "A bathroom cleaner carries the warning: do not use on marble"
                " worktops. Suggest what the cleaner contains and why the warning is"
                " there.",
        "options": [
            {"text": "An alkali, which would dissolve the polish on the marble",
             "correct": False,
             "why": "It is the stone itself that is at risk, and an alkali does "
                    "not attack a carbonate."},
            {"text": "An acid, which would react with the carbonate in the marble",
             "correct": True},
            {"text": "A salt, which would leave white marks as it dried",
             "correct": False,
             "why": "Drying marks wipe off; the warning is about damage that "
                    "cannot be undone."},
            {"text": "A carbonate, which would build up as a layer on the "
                      "surface", "correct": False,
             "why": "Marble is already a carbonate, and nothing builds up on it "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-s32",
        "band": "standard",
        "text": "The gas from an unknown white solid turns limewater milky. State what"
                " that settles and what it leaves open.",
        "options": [
            {"text": "It settles that the solid is calcium carbonate and leaves "
                      "nothing open", "correct": False,
             "why": "Every carbonate gives the same gas, so the metal in it is "
                    "not identified."},
            {"text": "It settles the gas but not which carbonate it came from",
             "correct": True},
            {"text": "It settles the mass of solid used but not what it was",
             "correct": False,
             "why": "A colour change reports nothing about how much solid was "
                    "taken."},
            {"text": "It settles nothing, because limewater responds to several "
                      "gases", "correct": False,
             "why": "Turning limewater milky is specific to carbon dioxide, which "
                    "is why the test is used."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h17",
        "band": "harder",
        "text": "An acid and a base make a salt and water. Explain how an acid and a"
                " carbonate fit that rule while giving three products.",
        "options": [
            {"text": "A carbonate is not a base, so the rule does not apply to it",
             "correct": False,
             "why": "It plainly cancels acid out, which is what being a base "
                    "means."},
            {"text": "A carbonate is a base, and it brings carbon and oxygen that "
                      "leave as a gas", "correct": True},
            {"text": "A carbonate is an acid, so the extra product comes from it", "correct": False,
             "why": "A carbonate raises the pH rather than lowering it, so it is "
                    "not an acid."},
            {"text": "A carbonate makes no water, so the third product replaces "
                      "it", "correct": False,
             "why": "Water is made here as well; the gas is an addition rather "
                    "than a substitution."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h18",
        "band": "harder",
        "text": "Water is made when an acid meets a carbonate. State where the atoms"
                " in that water come from.",
        "options": [
            {"text": "All of them come out of the acid", "correct": False,
             "why": "The acid supplies the hydrogen, and the oxygen has to come "
                    "from somewhere else."},
            {"text": "All of them come out of the carbonate", "correct": False,
             "why": "The carbonate carries no free hydrogen for the water to be "
                    "built from."},
            {"text": "Hydrogen from the acid and oxygen from the carbonate",
             "correct": True},
            {"text": "They come from the water the acid was dissolved in",
             "correct": False,
             "why": "That water was already there; the reaction makes water of "
                    "its own."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h19",
        "band": "harder",
        "text": "Limewater is calcium hydroxide and the gas bubbled through it "
                "is carbon dioxide. Suggest what the fine white solid is.",
        "options": [
            {"text": "Undissolved calcium hydroxide falling out of solution", "correct": False,
             "why": "The solid appears because of the gas, not in spite of it; "
                    "clear limewater held its hydroxide perfectly well."},
            {"text": "Calcium chloride", "correct": False,
             "why": "No chloride is present in either the limewater or the "
                    "gas."},
            {"text": "Carbon, left behind as the gas breaks up", "correct": False,
             "why": "Carbon dioxide is not broken apart by limewater, and "
                    "carbon would be black."},
            {"text": "Calcium carbonate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h20",
        "band": "harder",
        "text": "A student writes that a gas is carbon dioxide because a lit splint"
                " held in it went out. Explain why that reasoning fails.",
        "options": [
            {"text": "Because a splint going out is a sign the gas is hydrogen",
             "correct": False,
             "why": "Hydrogen burns with a squeak rather than putting a flame "
                    "out."},
            {"text": "Because several gases put a flame out, and only one turns "
                      "limewater milky", "correct": True},
            {"text": "Because a lit splint goes out in every gas, including air",
             "correct": False,
             "why": "A splint burns on happily in air, which is why the result "
                    "means anything at all."},
            {"text": "Because the splint has to be glowing rather than lit before this gas shows up", "correct": False,
             "why": "A glowing splint is the test for a different gas and would "
                    "not identify this one either."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h21",
        "band": "harder",
        "text": "Table salt is already a salt, and it does nothing at all in dilute"
                " acid. Explain why not.",
        "options": [
            {"text": "Because it dissolves too quickly for a reaction to start",
             "correct": False,
             "why": "Dissolving brings its particles into contact rather than "
                    "preventing anything."},
            {"text": "Because it holds no carbonate for the acid to break open",
             "correct": True},
            {"text": "Because a salt is neutral, so acid cannot touch it at all",
             "correct": False,
             "why": "Being neutral is not a shield; plenty of neutral substances "
                    "react with acid."},
            {"text": "Because the acid is already full of the same chloride",
             "correct": False,
             "why": "A fresh acid reacts with a carbonate whatever chloride is "
                    "dissolved in it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h22",
        "band": "harder",
        "text": "A stoppered flask of marble and acid holds its mass exactly while the"
                " reaction runs. The stopper is then removed and the flask reweighed."
                " Predict the reading.",
        "options": [
            {"text": "Unchanged, because the reaction had already finished",
             "correct": False,
             "why": "The gas had been held in, and removing the stopper lets it "
                    "go."},
            {"text": "Lower, because the carbon dioxide escapes when it can",
             "correct": True},
            {"text": "Higher, because air rushes into the flask", "correct": False,
             "why": "Air moving in and out does not add weighable mass of that "
                    "kind."},
            {"text": "Lower, because the salt evaporates once the flask is open",
             "correct": False,
             "why": "The salt stays dissolved in the liquid; only the gas can "
                    "leave."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h23",
        "band": "harder",
        "text": "Bubbling is stopped the moment the limewater turns milky, and the tube"
                " is left standing on the bench. Predict what the limewater looks like"
                " an hour later.",
        "options": [
            {"text": "Clear again, because the white solid always redissolves",
             "correct": False,
             "why": "It redissolves only when more carbon dioxide is bubbled "
                    "through, and none is."},
            {"text": "Still milky", "correct": True},
            {"text": "Clear, because the test only lasts a few minutes",
             "correct": False,
             "why": "A chemical change does not undo itself after a set time."},
            {"text": "Milky, and then clear as soon as it is shaken",
             "correct": False,
             "why": "Shaking stirs the solid about; it does not dissolve it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h24",
        "band": "harder",
        "text": "A student needs to know how much carbonate a rock contains, not merely"
                " whether it has any. Suggest how the test would have to change.",
        "options": [
            {"text": "Use a stronger acid and see whether the fizzing lasts longer",
             "correct": False,
             "why": "A stronger acid changes the pace rather than how much gas "
                    "there is altogether."},
            {"text": "Bubble the gas through more limewater and see how milky it "
                      "gets", "correct": False,
             "why": "The milkiness reports that the gas arrived, not how much of "
                    "it there was."},
            {"text": "Take a known mass of rock and measure the total volume of "
                      "gas", "correct": True},
            {"text": "Repeat the drip test on several parts of the same rock",
             "correct": False,
             "why": "Repeats tell you the rock is the same throughout, not how "
                    "much carbonate it holds."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h25",
        "band": "harder",
        "text": "Sodium carbonate and sodium hydrogencarbonate are different compounds,"
                " yet both give the same salt with hydrochloric acid. Explain.",
        "options": [
            {"text": "Because both carry a carbonate group and both supply sodium",
             "correct": True},
            {"text": "Because the acid decides both parts of the salt's name",
             "correct": False,
             "why": "The acid decides only the second part; the metal comes from "
                    "the solid."},
            {"text": "Because sodium hydrogencarbonate turns into sodium carbonate "
                      "first", "correct": False,
             "why": "It reacts with the acid directly rather than converting into "
                    "the other compound."},
            {"text": "Because both compounds are really the same substance under "
                      "two names", "correct": False,
             "why": "They are different compounds, as their different formulae "
                    "and uses show."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h26",
        "band": "harder",
        "text": "An open flask of marble chips and acid loses 0.88 g over the course of"
                " the reaction. State what that 0.88 g is a measure of.",
        "options": [
            {"text": "The mass of marble that reacted", "correct": False,
             "why": "Most of the marble stayed in the flask as dissolved salt; "
                    "only the gas left."},
            {"text": "The mass of acid that was used up", "correct": False,
             "why": "The acid that reacted is still in the flask, as part of the "
                    "salt and the water."},
            {"text": "The mass of carbon dioxide that escaped", "correct": True},
            {"text": "The mass of water made by the reaction", "correct": False,
             "why": "The water made is a liquid and stays in the flask with "
                    "everything else."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h27",
        "band": "harder",
        "text": "Marble chips are dropped into a beaker of pure water and left for an"
                " hour. Predict what is seen, and explain.",
        "options": [
            {"text": "Steady fizzing, because marble reacts with any liquid",
             "correct": False,
             "why": "Marble is untouched by most liquids; it takes an acid to "
                    "break the carbonate open."},
            {"text": "Nothing, because water is not an acid", "correct": True},
            {"text": "Nothing at first, then fizzing once the water warms up",
             "correct": False,
             "why": "Warming a liquid that cannot react does not start a "
                    "reaction."},
            {"text": "The chips dissolve quietly, giving no gas at all",
             "correct": False,
             "why": "Calcium carbonate barely dissolves in water, which is why "
                    "rock made of it lasts."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h28",
        "band": "harder",
        "text": "From one fizzing rock a student concludes that every rock fizzes in"
                " acid. Evaluate.",
        "options": [
            {"text": "Sound, because all rock is made from the same materials",
             "correct": False,
             "why": "Rocks are made of many different compounds, only some of "
                    "which are carbonates."},
            {"text": "Sound, because acid attacks anything it is dripped onto",
             "correct": False,
             "why": "Acid leaves a great many substances entirely untouched."},
            {"text": "Unsound, because a rock with no carbonate in it does "
                      "nothing", "correct": True},
            {"text": "Unsound, because rocks fizz only when they have been "
                      "crushed first", "correct": False,
             "why": "A solid lump of marble fizzes perfectly well without being "
                    "crushed."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h29",
        "band": "harder",
        "text": "A chalk tablet is swallowed to treat indigestion. Describe what "
                "the chalk does to the acid it meets, and name the gas produced.",
        "options": [
            {"text": "The chalk makes the acid stronger, giving off oxygen", "correct": False,
             "why": "It cancels acid out rather than strengthening it, and "
                    "oxygen is not a product here."},
            {"text": "The chalk coats the stomach lining, giving off hydrogen", "correct": False,
             "why": "It reacts with the acid rather than coating anything, and "
                    "no hydrogen is made."},
            {"text": "The chalk dissolves without reacting, giving off no gas", "correct": False,
             "why": "A carbonate meeting stomach acid reacts, which is the "
                    "whole reason for taking it."},
            {"text": "The chalk neutralises the acid, giving off carbon "
                      "dioxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h30",
        "band": "harder",
        "text": "Acid dripped on a soil sample gives no fizz, and a student concludes"
                " the soil is acidic. Evaluate.",
        "options": [
            {"text": "Sound, because acidic soil cannot fizz with more acid",
             "correct": False,
             "why": "An acidic soil could still hold a carbonate and fizz; the "
                    "two are separate questions."},
            {"text": "Unsound, because the test reports carbonate rather than pH",
             "correct": True},
            {"text": "Sound, because fizzing is how alkaline soil is recognised",
             "correct": False,
             "why": "Fizzing reports a carbonate, and plenty of alkaline "
                    "substances do not fizz."},
            {"text": "Unsound, because no fizzing means the acid was too dilute",
             "correct": False,
             "why": "Dilute acid fizzes readily on a carbonate, which is why "
                    "geologists carry it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h31",
        "band": "harder",
        "text": "Rain that has fallen through perfectly clean air is still slightly"
                " acidic. Explain why limestone buildings are lost even far from any"
                " city.",
        "options": [
            {"text": "Because clean rain is alkaline, and alkalis are what attack carbonate",
             "correct": False,
             "why": "Clean rain sits just below 7, and it is acid rather than "
                    "alkali that reacts with a carbonate."},
            {"text": "Because even a slight acidity reacts with carbonate, year "
                      "after year", "correct": True},
            {"text": "Because rain washes the loose grains off a soft stone",
             "correct": False,
             "why": "Washing is physical, and it would take the same toll on "
                    "granite, which survives."},
            {"text": "Because limestone absorbs water and cracks apart in winter",
             "correct": False,
             "why": "Frost damage is a separate effect and is not what the "
                    "chemistry here describes."},
        ],
        "figure": None,
    },
    {
        "id": "c6-05-h32",
        "band": "harder",
        "text": "A works treating acidic water uses crushed limestone rather than large"
                " blocks of it. Explain why.",
        "options": [
            {"text": "Because crushed limestone contains more carbonate than a "
                      "block does", "correct": False,
             "why": "The same mass holds the same carbonate however it is broken "
                    "up."},
            {"text": "Because crushed limestone neutralises the acid without any "
                      "gas", "correct": False,
             "why": "Carbon dioxide is given off whatever the size of the "
                    "pieces."},
            {"text": "Because crushed limestone dissolves in water and blocks do "
                      "not", "correct": False,
             "why": "Calcium carbonate barely dissolves in water at any size."},
            {"text": "Because far more of its surface is in contact with the "
                      "water", "correct": True},
        ],
        "figure": None,
    },
]
