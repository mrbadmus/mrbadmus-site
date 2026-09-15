"""P1 lesson 07 — Insulation: twelve questions.

⊕ RUN 1's TWELVE WERE USED AS RAW MATERIAL, NOT ADOPTED (MRB-223).

Run 1's own provenance audit flags `s01`, `s02` and `h02` as quoting figures
off a lagging bench it invented — 64.4, 59.4, 70.3, 37.9, 9.7, 32.4 and
"95% trapped air". Measured against Design's page, the problem is wider than
those three: her bench is FOUR BEAKERS with different wrappings — nothing,
shiny foil, wool at one layer, wool at three layers with a lid — all at
80 °C in a 20 °C room. It does not compare several materials at one layer
against the same materials at three, so `s04` ("every material on the bench
did better at 3 layers than at 1") describes a bench that does not exist
either.

    CHANGED — five stems kept, option sets rewritten (5):
        e01  what an insulator does
        e02  what does the insulating in wool
        e03  why the bare beaker stays on the bench
        e04  which one thing is deliberately changed
        h03  the snowman in a coat

    NEW — her page's own material, untested by the inherited set (7):
        s01  what the cooling curves do NOT prove
        s02  why the ice trial is the one that decides it
        s03  the fridge-cold bottle in a jumper
        s04  why the lid matters on the best beaker
        h01  the "keeps a tank hot for ever" claim
        h02  the foam box used for both chips and ice cream
        h04  why a thick loose duvet beats a thin packed one

    DROPPED — invented bench data (4):
        run 1's s01, s02, s04 and h02.

⚠️ THE SET'S CENTRE OF GRAVITY MOVED. Run 1's questions were mostly about
which material insulates best. Design's lesson is about what the trial can
and cannot prove — her `#s-trial` close says the curves are equally
consistent with insulation ADDING warmth, and `#s-ice` is what rules that
out. Four of the seven new questions are about that argument rather than
about materials, because that is what her page teaches.

⚠️ Answer positions are 0,1,2,3 · 1,2,3,0 · 1,2,3,0 — three of each index.
⚠️ Every distractor is written to the correct answer's own length (MRB-177).

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P1"
LESSON = "insulation"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-07-e01",
        "band": "easier",
        "text": "What does an insulator do?",
        "options": [
            {"text": "It slows the transfer of energy through it",
             "correct": True},
            {"text": "It adds warmth to whatever it is wrapped around",
             "correct": False,
             "why": "Nothing adds warmth without an energy supply, and a "
                    "blanket has none."},
            {"text": "It stops energy moving through it completely",
             "correct": False,
             "why": "Slowed, not stopped. Given long enough everything "
                    "reaches room temperature."},
            {"text": "It keeps the cold out of whatever it surrounds",
             "correct": False,
             "why": "There is no cold to keep out. Only energy moves, and "
                    "the insulator slows it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e02",
        "band": "easier",
        "text": "What does most of the insulating in a woollen jumper?",
        "options": [
            {"text": "The wool fibres themselves, which are warm to begin "
                     "with",
             "correct": False,
             "why": "Fibres have no warmth of their own. They come out of "
                    "the drawer at room temperature."},
            {"text": "The air trapped between the fibres, which conducts "
                     "very badly",
             "correct": True},
            {"text": "The colour of the wool, which stops radiation getting "
                     "out",
             "correct": False,
             "why": "Colour affects radiation a little. Almost all of a "
                    "jumper's effect is trapped air."},
            {"text": "The tightness of the weave, which blocks the cold "
                     "coming in",
             "correct": False,
             "why": "A tight weave traps LESS air and insulates worse. And "
                    "nothing comes in."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e03",
        "band": "easier",
        "text": "Why is an unwrapped beaker kept on the bench throughout the "
                "trial?",
        "options": [
            {"text": "To use up the spare space so the other beakers stay "
                     "steady",
             "correct": False,
             "why": "It is not a spacer. It is carrying information the "
                    "others cannot."},
            {"text": "To warm the room slightly so the conditions stay the "
                     "same",
             "correct": False,
             "why": "It is not there to change the room. The room is a "
                    "control variable, not a target."},
            {"text": "As the control, to show what happens with no wrapping "
                     "at all",
             "correct": True},
            {"text": "To check that the thermometers all agree with one "
                     "another",
             "correct": False,
             "why": "That would be a separate calibration step. This beaker "
                    "is a comparison, not a check."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e04",
        "band": "easier",
        "text": "In the trial, which one thing is deliberately changed "
                "between the beakers?",
        "options": [
            {"text": "The volume of water that each of the beakers holds",
             "correct": False,
             "why": "That is held the same. More water cools more slowly "
                    "whatever the wrapping."},
            {"text": "The temperature that each beaker starts the trial at",
             "correct": False,
             "why": "That is held the same. A hotter start would look like "
                    "worse insulation."},
            {"text": "The times at which each thermometer is read off",
             "correct": False,
             "why": "That is held the same. Readings have to be simultaneous "
                    "to compare."},
            {"text": "The wrapping that is put around each of the beakers",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-07-s01",
        "band": "standard",
        "text": "Every wrapped beaker stayed hotter than the control. What "
                "does that NOT prove?",
        "options": [
            {"text": "That the wrappings slowed the energy leaving the water",
             "correct": False,
             "why": "It does support that. The question is what it fails to "
                    "rule out."},
            {"text": "That the wool was not adding warmth of its own to the "
                     "water",
             "correct": True},
            {"text": "That the three-layer beaker was the best insulator of "
                     "the four",
             "correct": False,
             "why": "It shows that clearly. Ranking the wrappings is exactly "
                    "what the curves do well."},
            {"text": "That an unwrapped beaker cools faster than a wrapped "
                     "one does",
             "correct": False,
             "why": "That is the plainest thing the curves show, and nobody "
                    "disputes it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s02",
        "band": "standard",
        "text": "Why is the ICE trial the one that settles the argument?",
        "options": [
            {"text": "Because ice is easier to measure accurately than hot "
                     "water is",
             "correct": False,
             "why": "It is not about accuracy. It is about which "
                    "explanations the result can rule out."},
            {"text": "Because it runs for longer, so any difference has more "
                     "time to show",
             "correct": False,
             "why": "Length is not the point. A short ice trial would decide "
                    "it just as well."},
            {"text": "Because a warmth-adding blanket would make wrapped ice "
                     "melt FASTER",
             "correct": True},
            {"text": "Because ice is colder than the room, so the energy has "
                     "further to travel",
             "correct": False,
             "why": "The gap is smaller than the hot water's, not larger. "
                    "The direction is what matters."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s03",
        "band": "standard",
        "text": "You wrap a jumper tightly round a bottle of fridge-cold "
                "water and leave it in a warm room. What happens?",
        "options": [
            {"text": "It warms up faster, because the jumper is a warm thing "
                     "to be wrapped in",
             "correct": False,
             "why": "This is the misconception exactly. The jumper has no "
                    "warmth of its own to give."},
            {"text": "It warms up at the same rate as an unwrapped bottle "
                     "standing beside it",
             "correct": False,
             "why": "Insulation works in both directions. The wrapped one is "
                    "slower."},
            {"text": "It stays cold for ever, because the jumper seals the "
                     "warmth out completely",
             "correct": False,
             "why": "Slowed, never stopped. Given long enough it reaches "
                    "room temperature."},
            {"text": "It warms up more slowly than an unwrapped bottle would "
                     "have done",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s04",
        "band": "standard",
        "text": "The best beaker had three layers of wool AND a lid. What "
                "does the lid add that the wool cannot?",
        "options": [
            {"text": "It blocks convection, the route straight up out of the "
                     "open top",
             "correct": True},
            {"text": "It blocks conduction through the glass sides of the "
                     "beaker itself",
             "correct": False,
             "why": "The wool already handles the sides. The lid covers a "
                    "route the wool never touched."},
            {"text": "It adds another layer of trapped air on top of the "
                     "three below it",
             "correct": False,
             "why": "A lid is not mainly about trapped air. It closes an "
                    "opening the wrapping left."},
            {"text": "It stops the water evaporating and taking its mass "
                     "away with it",
             "correct": False,
             "why": "Evaporation does cool it a little, but the lid's main "
                    "job is the rising warm air."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-07-h01",
        "band": "harder",
        "text": "A company claims its lagging “keeps a tank hot for "
                "ever”. What result would disprove it?",
        "options": [
            {"text": "Showing that a lagged tank cools more slowly than an "
                     "unlagged one does",
             "correct": False,
             "why": "That supports the lagging working. It does not touch "
                    "the word “for ever”."},
            {"text": "Showing the tank eventually reaches room temperature "
                     "if left long enough",
             "correct": True},
            {"text": "Showing that the lagging itself becomes warm while the "
                     "tank is cooling",
             "correct": False,
             "why": "The lagging warming is expected — energy passes through "
                    "it on the way out."},
            {"text": "Showing that a thicker layer of the same lagging works "
                     "better than a thin one",
             "correct": False,
             "why": "That is about how well it works, not about whether it "
                    "works for ever."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h02",
        "band": "harder",
        "text": "A takeaway uses the same foam boxes for hot chips and for "
                "ice cream. Why does one box do both jobs?",
        "options": [
            {"text": "Because foam is warm for the chips and cold for the "
                     "ice cream at the same time",
             "correct": False,
             "why": "It is neither. It sits at room temperature and adds "
                    "nothing to either."},
            {"text": "Because the box is thick enough to stop the transfer "
                     "of energy completely",
             "correct": False,
             "why": "Nothing stops it completely. Both eventually reach room "
                    "temperature."},
            {"text": "Because it slows the transfer, and does not care which "
                     "way the flow is going",
             "correct": True},
            {"text": "Because trapped air conducts warmth outwards but not "
                     "inwards through the wall",
             "correct": False,
             "why": "No material is one-way. Conduction has no preferred "
                    "direction."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h03",
        "band": "harder",
        "text": "A snowman is dressed in a thick coat on a mild day. What "
                "happens compared with an undressed one?",
        "options": [
            {"text": "It melts faster, because the coat is warm in itself "
                     "and passes that warmth in",
             "correct": False,
             "why": "The coat has no warmth of its own. This is the ice "
                    "trial in a different hat."},
            {"text": "It melts at the same rate, because coats can only "
                     "work on living bodies",
             "correct": False,
             "why": "Nothing about insulation requires a body. It slows a "
                    "flow either way."},
            {"text": "It melts more quickly at first and then more slowly, "
                     "because the coat warms up",
             "correct": False,
             "why": "There is no crossover. It is slower throughout, for "
                    "the same reason all the way."},
            {"text": "It melts more slowly, because the coat slows the "
                     "energy reaching the snow",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h04",
        "band": "harder",
        "text": "Why is a thick loose duvet warmer than a thin packed one "
                "made of the same filling?",
        "options": [
            {"text": "Because the loose one traps far more air, and air is "
                     "the poor conductor",
             "correct": True},
            {"text": "Because the loose one contains more filling in total "
                     "than the packed one",
             "correct": False,
             "why": "They can hold the same filling. What differs is how "
                    "much air is held between it."},
            {"text": "Because packing the filling squeezes the warmth out of "
                     "it before use",
             "correct": False,
             "why": "There is no warmth stored in the filling to squeeze "
                    "out."},
            {"text": "Because a thicker duvet is heavier and presses closer "
                     "against the sleeper",
             "correct": False,
             "why": "Pressing closer would help conduction AWAY from you. "
                    "Weight is not the mechanism."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p1-07-e05",
        "band": "easier",
        "text": "Does wrapping something in an insulator add warmth to it?",
        "options": [
            {"text": "Yes — that is why a coat makes you warmer",
             "correct": False,
             "why": "A coat adds nothing. It slows the energy leaving YOU, "
                    "which is where the warmth comes from."},
            {"text": "No — it only slows energy passing in or out",
             "correct": True},
            {"text": "Yes, but only for objects warmer than the room",
             "correct": False,
             "why": "It adds nothing at any temperature. Wrapped ice lasts "
                    "longer rather than melting sooner."},
            {"text": "No — an insulator has no effect on energy transfer at "
                     "all",
             "correct": False,
             "why": "It has a large effect: it makes the transfer much "
                    "slower, in either direction."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e06",
        "band": "easier",
        "text": "In a cooling trial, which measurement is taken at regular "
                "intervals?",
        "options": [
            {"text": "The mass of the beaker in grams", "correct": False,
             "why": "The mass barely changes, and it is not what the trial "
                    "is following."},
            {"text": "The thickness of the wrapping in centimetres",
             "correct": False,
             "why": "The wrapping is set at the start and left alone; it is "
                    "what you changed, not what you measure."},
            {"text": "The temperature in degrees Celsius", "correct": True},
            {"text": "The volume of water in cubic centimetres",
             "correct": False,
             "why": "The volume is kept the same throughout, so measuring it "
                    "repeatedly tells you nothing."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p1-07-s05",
        "band": "standard",
        "text": "Two beakers start at 80 °C. After twenty minutes one is at "
                "62 °C and the other at 44 °C. Which one was lagged?",
        "options": [
            {"text": "The 44 °C one, because it has changed the most",
             "correct": False,
             "why": "Changing most means cooling fastest, which is what an "
                    "unwrapped beaker does."},
            {"text": "The 62 °C one, which lost 18 °C rather than 36 °C",
             "correct": True},
            {"text": "Neither — lagging does not change a cooling curve",
             "correct": False,
             "why": "It changes it a great deal, which is the whole point of "
                    "the trial."},
            {"text": "It cannot be told without knowing the room temperature",
             "correct": False,
             "why": "Both stood in the same room, so the one that stayed "
                    "hotter is the wrapped one."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s06",
        "band": "standard",
        "text": "Why does a cooling curve become less steep as the minutes go "
                "on?",
        "options": [
            {"text": "Because the insulation gets better as it warms up",
             "correct": False,
             "why": "The wrapping does not change. The temperature difference "
                    "does."},
            {"text": "Because the water runs out of energy to give away",
             "correct": False,
             "why": "It still holds plenty; it simply gives it away more "
                    "slowly as it nears room temperature."},
            {"text": "Because the thermometer becomes less accurate at lower "
                     "temperatures",
             "correct": False,
             "why": "A thermometer reads just as well cool as hot. The shape "
                    "is real, not an instrument fault."},
            {"text": "Because the gap between the water and the room gets "
                     "smaller",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p1-07-h05",
        "band": "harder",
        "text": "Why is loft insulation usually the first thing fitted when a "
                "house is being made cheaper to heat?",
        "options": [
            {"text": "Because warm air rises, so the roof is the biggest "
                     "escape route to block",
             "correct": True},
            {"text": "Because a loft is the coldest part of a house, so it "
                     "needs warming first of all",
             "correct": False,
             "why": "Insulation warms nothing. It is fitted there because "
                    "that is where most energy leaves."},
            {"text": "Because insulation only works where there is no "
                     "furniture in the way",
             "correct": False,
             "why": "Walls and floors are insulated too; the loft is chosen "
                    "for the size of the loss, not for access."},
            {"text": "Because energy always travels upwards and never "
                     "sideways",
             "correct": False,
             "why": "Radiation goes in every direction and walls lose plenty; "
                    "it is the rising WARM AIR that goes up."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h06",
        "band": "harder",
        "text": "A beaker wrapped in shiny foil cools more slowly than a bare "
                "one. Which route has been slowed most?",
        "options": [
            {"text": "Conduction, because foil is a metal", "correct": False,
             "why": "Metal foil is a good conductor, so if anything that "
                    "route is helped, not slowed."},
            {"text": "Radiation, because a shiny surface emits infrared "
                     "poorly",
             "correct": True},
            {"text": "Convection, because the foil is airtight",
             "correct": False,
             "why": "A loose wrap slows some air movement, but the striking "
                    "change comes from the shiny surface."},
            {"text": "None of the three — the foil simply adds warmth of its "
                     "own",
             "correct": False,
             "why": "No wrapping adds warmth. The foil changes how fast "
                    "energy leaves."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · easier ─────────────────────────────────
    {
        "id": "p1-07-e07",
        "band": "easier",
        "text": "What is a control variable?",
        "options": [
            {"text": "Something you deliberately keep the same so a "
                     "difference can be blamed on one thing",
             "correct": True},
            {"text": "The one thing you deliberately change between the "
                     "beakers in the trial",
             "correct": False,
             "why": "That is the independent variable. A control variable is "
                    "held still."},
            {"text": "The measurement you write down at each of the moments "
                     "you read the thermometer",
             "correct": False,
             "why": "That is the dependent variable — the thing the trial is "
                    "watching, not holding."},
            {"text": "The person in charge of running the trial",
             "correct": False,
             "why": "A variable is a quantity, not a person. It is something "
                    "that could change but is held."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e08",
        "band": "easier",
        "text": "What is the independent variable in a beaker-lagging trial?",
        "options": [
            {"text": "The temperature of the room that the beakers all stand "
                     "in",
             "correct": False,
             "why": "That is held the same for every beaker, so it is a "
                    "control variable."},
            {"text": "The volume of water poured into each beaker",
             "correct": False,
             "why": "That is held the same throughout, which makes it a "
                    "control variable."},
            {"text": "The temperature read off each thermometer",
             "correct": False,
             "why": "That is what the trial measures, so it is the dependent "
                    "variable."},
            {"text": "The wrapping put around each of the beakers",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e09",
        "band": "easier",
        "text": "Which quantity is the dependent variable in a cooling trial?",
        "options": [
            {"text": "The wrapping chosen for each beaker before the trial "
                     "starts",
             "correct": False,
             "why": "That is the one thing deliberately changed, so it is the "
                    "independent variable."},
            {"text": "The size of the beaker used each time",
             "correct": False,
             "why": "That is held the same so the comparison stays fair, "
                    "which makes it a control."},
            {"text": "The temperature of the water as time goes on",
             "correct": True},
            {"text": "The room the beakers are standing in",
             "correct": False,
             "why": "The room is held the same for every beaker, so it is a "
                    "control variable too."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e10",
        "band": "easier",
        "text": "Why must every beaker start at the same temperature?",
        "options": [
            {"text": "Because a hotter start gives a faster fall, which would "
                     "look like poor insulation",
             "correct": True},
            {"text": "Because water at different temperatures cannot be "
                     "compared on the same thermometer at all",
             "correct": False,
             "why": "One thermometer reads any temperature. The problem is "
                    "with the comparison, not the instrument."},
            {"text": "Because a beaker that starts cooler will never cool "
                     "down any further at all",
             "correct": False,
             "why": "It cools until it reaches room temperature, like every "
                    "other beaker."},
            {"text": "Because the wrapping only works at one temperature",
             "correct": False,
             "why": "Insulation works at any temperature. The trouble is that "
                    "two starts give two different curves."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e11",
        "band": "easier",
        "text": "Why must every beaker hold the same volume of water?",
        "options": [
            {"text": "Because more water cools more slowly whatever the "
                     "wrapping is",
             "correct": True},
            {"text": "Because a beaker with less water in it would tip over "
                     "before the trial finished",
             "correct": False,
             "why": "Stability is not the issue. The volume changes the "
                    "cooling rate on its own."},
            {"text": "Because the thermometer has to be covered by water to "
                     "give any reading at all",
             "correct": False,
             "why": "That is a practical detail, and a small volume would "
                    "still cover a bulb."},
            {"text": "Because water only cools at a fixed rate",
             "correct": False,
             "why": "Its rate depends on several things, which is exactly why "
                    "all but one are held still."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e12",
        "band": "easier",
        "text": "Why must all the beakers stand in the same room?",
        "options": [
            {"text": "Because cooling depends on the difference between the "
                     "water and its surroundings",
             "correct": True},
            {"text": "Because a beaker standing in another room would be much "
                     "harder to reach in time",
             "correct": False,
             "why": "Convenience is not the reason. A different room means a "
                    "different temperature difference."},
            {"text": "Because water behaves differently in different rooms of "
                     "a building",
             "correct": False,
             "why": "Water behaves the same everywhere. What differs is the "
                    "temperature it is cooling towards."},
            {"text": "Because the wrappings need to be kept together",
             "correct": False,
             "why": "The wrappings are on the beakers. The room matters "
                    "because of its temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e13",
        "band": "easier",
        "text": "Why must the thermometers all be read at the same moments?",
        "options": [
            {"text": "Because readings taken at different times are two "
                     "unrelated numbers rather than a comparison",
             "correct": True},
            {"text": "Because a thermometer becomes less accurate the longer "
                     "it has been left standing in water",
             "correct": False,
             "why": "A thermometer does not drift like that. The problem is "
                    "that the readings would not match up."},
            {"text": "Because water stops cooling altogether between one "
                     "reading and the next one",
             "correct": False,
             "why": "It cools continuously whether anybody is looking or "
                    "not."},
            {"text": "Because the beakers are all the same size",
             "correct": False,
             "why": "Beaker size is a separate control. Simultaneous readings "
                    "are about comparing fairly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e14",
        "band": "easier",
        "text": "What does trapped air do in an insulating material?",
        "options": [
            {"text": "It conducts very badly, so energy passes through it "
                     "slowly",
             "correct": True},
            {"text": "It warms up and gives that warmth back to what is "
                     "wrapped",
             "correct": False,
             "why": "It has no warmth of its own to give. It only slows the "
                    "flow passing through it."},
            {"text": "It carries energy quickly away from the surface",
             "correct": False,
             "why": "That would be a conductor's job. Trapped air does the "
                    "opposite."},
            {"text": "It stops energy moving through it completely",
             "correct": False,
             "why": "Slowed, never stopped. Given long enough everything "
                    "reaches room temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e15",
        "band": "easier",
        "text": "Which of these is the better insulator?",
        "options": [
            {"text": "Aluminium foil wrapped tightly", "correct": False,
             "why": "Aluminium is a metal and conducts well, so it is a poor "
                    "insulator against conduction."},
            {"text": "A loose layer of wool", "correct": True},
            {"text": "A sheet of copper", "correct": False,
             "why": "Copper is the best conductor on the bench, which makes "
                    "it the worst insulator."},
            {"text": "A steel plate", "correct": False,
             "why": "Steel is a metal too, so energy passes through it far "
                    "faster than through wool."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e16",
        "band": "easier",
        "text": "Does a thicker layer of the same insulating material work "
                "better than a thin one?",
        "options": [
            {"text": "No, because thickness makes no difference",
             "correct": False,
             "why": "Thickness makes a large difference, which is why loft "
                    "insulation is laid deep."},
            {"text": "No, because a thick layer traps less air",
             "correct": False,
             "why": "A thicker layer traps more air, not less, so it "
                    "insulates better."},
            {"text": "Yes — energy has further to travel, so it takes longer",
             "correct": True},
            {"text": "Yes, but only when the material is a metal",
             "correct": False,
             "why": "Metals are poor insulators however thick. Thickness "
                    "helps most with a good insulator."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e17",
        "band": "easier",
        "text": "What happens to a well-wrapped beaker of hot water if it is "
                "left for a whole day?",
        "options": [
            {"text": "It stays hot, because good insulation stops the "
                     "transfer altogether",
             "correct": False,
             "why": "Insulation slows a flow; it never stops one. A day is "
                    "ample."},
            {"text": "It always reaches room temperature, just later than "
                     "an unwrapped one would",
             "correct": True},
            {"text": "It becomes colder than the room, because the wrapping "
                     "keeps drawing energy out",
             "correct": False,
             "why": "Nothing draws energy below room temperature. The flow "
                    "stops when the two match."},
            {"text": "It warms up, because the wrapping adds its warmth",
             "correct": False,
             "why": "A wrapping has no energy supply and adds nothing at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e18",
        "band": "easier",
        "text": "Why is a lid put on a beaker in a cooling trial?",
        "options": [
            {"text": "To stop warm air rising straight out of the open top",
             "correct": True},
            {"text": "To stop the thermometer falling over into the water "
                     "below it",
             "correct": False,
             "why": "A lid may hold a thermometer, but that is not what it "
                    "does for the cooling."},
            {"text": "To keep the wrapping pressed tightly against the sides "
                     "of the beaker",
             "correct": False,
             "why": "The wrapping stays on by itself. The lid closes a route "
                    "out of the top."},
            {"text": "To make the beaker heavier so that it cannot slide about",
             "correct": False,
             "why": "Weight has nothing to do with it. The lid blocks the "
                    "rising warm air."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e19",
        "band": "easier",
        "text": "Which route does shiny foil mainly block?",
        "options": [
            {"text": "Conduction, because foil is a metal and metals conduct "
                     "very well indeed",
             "correct": False,
             "why": "Metal conducts well, so foil is a poor barrier against "
                    "conduction. Its shine is what helps."},
            {"text": "Convection, because it is wrapped tightly round the "
                     "outside of the beaker",
             "correct": False,
             "why": "A loose wrap slows some air movement, but the striking "
                    "effect comes from the shine."},
            {"text": "Radiation, because a shiny surface is a poor emitter",
             "correct": True},
            {"text": "All three at once, because it is a complete wrapping",
             "correct": False,
             "why": "Foil conducts well, so it is no help at all against "
                    "conduction."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e20",
        "band": "easier",
        "text": "What does a woolly hat do for your head?",
        "options": [
            {"text": "It adds warmth of its own to the top of your head",
             "correct": False,
             "why": "A hat has no energy supply and makes no warmth. It slows "
                    "what is already leaving."},
            {"text": "It makes your body produce more energy than usual",
             "correct": False,
             "why": "Your body runs at the same rate with or without a hat. "
                    "The hat changes the losses."},
            {"text": "It keeps the cold of the air out of your head",
             "correct": False,
             "why": "There is no cold to keep out. Only energy moves, and it "
                    "is moving outwards."},
            {"text": "It only slows the energy escaping from your own body",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e21",
        "band": "easier",
        "text": "Which fabric traps more air, a tightly woven one or a fluffy "
                "one?",
        "options": [
            {"text": "The tightly woven one, because tight weaves hold more "
                     "air",
             "correct": False,
             "why": "A tight weave squeezes the air out. That is why it "
                    "insulates worse."},
            {"text": "Neither, because a fabric cannot hold any air inside it",
             "correct": False,
             "why": "Fabrics hold a great deal of air, which is most of what "
                    "makes them warm."},
            {"text": "The tightly woven one, because it is thicker",
             "correct": False,
             "why": "Tight is not the same as thick, and a tight weave holds "
                    "less air whatever its thickness."},
            {"text": "The fluffy one, because its loose fibres hold pockets "
                     "of air between them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e22",
        "band": "easier",
        "text": "Why do birds fluff up their feathers in cold weather?",
        "options": [
            {"text": "To trap a thicker layer of air next to the skin",
             "correct": True},
            {"text": "To make themselves look larger so that predators leave "
                     "them alone in winter",
             "correct": False,
             "why": "Looking larger is a separate behaviour. Fluffing in the "
                    "cold is about trapped air."},
            {"text": "To let the wind pass through the feathers more easily "
                     "than it otherwise would",
             "correct": False,
             "why": "Letting wind through would carry energy away. The point "
                    "is to hold still air in."},
            {"text": "To produce extra warmth inside the feathers themselves",
             "correct": False,
             "why": "Feathers make no warmth. The bird's own body is the "
                    "source of all of it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e23",
        "band": "easier",
        "text": "What is cavity wall insulation?",
        "options": [
            {"text": "A layer of shiny foil fixed to the outside face of a "
                     "house wall",
             "correct": False,
             "why": "It goes inside the gap between the two walls, and it is "
                    "usually foam or wool rather than foil."},
            {"text": "A heater fitted inside the wall of a house to warm it "
                     "from within",
             "correct": False,
             "why": "It is not a heater and has no energy supply. It slows "
                    "energy leaving."},
            {"text": "Foam or wool filling the gap between two house walls",
             "correct": True},
            {"text": "A gap left completely empty between the two walls of a "
                     "house",
             "correct": False,
             "why": "An empty gap lets air circulate, which carries energy "
                    "across. Filling it stops that."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e24",
        "band": "easier",
        "text": "What is loft insulation for?",
        "options": [
            {"text": "To slow the energy escaping through the roof of a house",
             "correct": True},
            {"text": "To warm the loft so that the rooms underneath it become "
                     "warmer as well",
             "correct": False,
             "why": "An insulated loft is colder than before, because the "
                    "energy is kept below it."},
            {"text": "To stop rain getting into the loft space through the "
                     "tiles on the roof",
             "correct": False,
             "why": "Keeping rain out is the roof's job. Insulation is about "
                    "energy, not water."},
            {"text": "To make the house heavier so that it is more stable in "
                     "wind",
             "correct": False,
             "why": "Weight is irrelevant. It is fitted to reduce the energy "
                    "leaving through the roof."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e25",
        "band": "easier",
        "text": "Why does a cool box keep ice cream frozen on a warm day?",
        "options": [
            {"text": "Because the box makes cold and pours it into the ice "
                     "cream inside",
             "correct": False,
             "why": "Nothing makes cold. The box only slows energy coming in "
                    "from the warm air."},
            {"text": "Because the box slows the energy coming in from the "
                     "warm air outside",
             "correct": True},
            {"text": "Because the box is much colder than the ice cream that "
                     "has been put inside it",
             "correct": False,
             "why": "The box starts at room temperature, which is far warmer "
                    "than the ice cream."},
            {"text": "Because insulation works on cold things but not on hot "
                     "ones",
             "correct": False,
             "why": "It works on both. The same box carries hot food just as "
                    "well."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e26",
        "band": "easier",
        "text": "What is a cooling curve?",
        "options": [
            {"text": "A graph of temperature against time as something cools",
             "correct": True},
            {"text": "A graph of the wrapping used against the temperature",
             "correct": False,
             "why": "The wrapping is set at the start. A cooling curve "
                    "follows temperature as time passes."},
            {"text": "The shape a wrapped beaker makes",
             "correct": False,
             "why": "It is a graph, not a shape of apparatus."},
            {"text": "A graph of how much energy a beaker holds",
             "correct": False,
             "why": "Energy is not measured directly here. The trial reads "
                    "temperature against time."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e27",
        "band": "easier",
        "text": "Does insulation work on something colder than the room as "
                "well as on something hotter?",
        "options": [
            {"text": "No, because insulation is designed to hold warmth in "
                     "rather than to keep it out",
             "correct": False,
             "why": "It holds nothing in. It slows a flow, and a flow can run "
                    "either way."},
            {"text": "Yes — it always slows the flow whichever way it is going",
             "correct": True},
            {"text": "No, because energy only ever moves outwards from a "
                     "wrapped object",
             "correct": False,
             "why": "Energy moves from hotter to cooler, so it flows inwards "
                    "when the object is the cooler one."},
            {"text": "Yes, but only when the wrapping happens to be made of "
                     "shiny foil",
             "correct": False,
             "why": "Any insulator works both ways. The material does not "
                    "change the direction."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e28",
        "band": "easier",
        "text": "Which cup would keep a cold drink cold for longer?",
        "options": [
            {"text": "A thin metal cup", "correct": False,
             "why": "Metal conducts well, so energy would reach the drink "
                    "faster than through any of the others."},
            {"text": "A thin paper cup", "correct": False,
             "why": "Paper is thin and traps little air, so it is a much "
                    "poorer insulator than foam."},
            {"text": "A thick foam cup", "correct": True},
            {"text": "A glass tumbler", "correct": False,
             "why": "Glass conducts far better than foam and traps no air at "
                    "all inside its walls."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e29",
        "band": "easier",
        "text": "Why is double glazing better than a single pane of glass?",
        "options": [
            {"text": "Because the gap between the two panes slows the "
                     "transfer through the window",
             "correct": True},
            {"text": "Because two panes are thicker, and thick glass makes "
                     "warmth",
             "correct": False,
             "why": "Glass makes no warmth at any thickness. The gap is what "
                    "does the work."},
            {"text": "Because two panes reflect all the light back into the "
                     "room",
             "correct": False,
             "why": "You can see through a double-glazed window, so it is "
                    "certainly not reflecting everything."},
            {"text": "Because a second pane keeps the cold outside",
             "correct": False,
             "why": "There is no cold to keep out. The gap slows energy "
                    "leaving the room."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e30",
        "band": "easier",
        "text": "What happens to a household's heating bill when the house is "
                "better insulated?",
        "options": [
            {"text": "It rises, because the insulation has to be powered "
                     "throughout the winter months",
             "correct": False,
             "why": "Insulation uses no energy at all. It has nothing to "
                    "power."},
            {"text": "It stays exactly the same, because the house still has "
                     "to be heated to the same temperature",
             "correct": False,
             "why": "The same temperature now costs less, because less energy "
                    "escapes to be replaced."},
            {"text": "It falls, because less energy escapes and less has to "
                     "be supplied",
             "correct": True},
            {"text": "It falls to nothing, because no energy escapes from a "
                     "well-insulated house",
             "correct": False,
             "why": "Some always escapes. Insulation slows the loss rather "
                    "than ending it."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · standard ───────────────────────────────
    {
        "id": "p1-07-s07",
        "band": "standard",
        "text": "Why is a wall cavity filled with foam rather than left as an "
                "empty air gap?",
        "options": [
            {"text": "Because an empty gap lets the air circulate and carry "
                     "energy across it",
             "correct": True},
            {"text": "Because an empty gap would let the rain in through the "
                     "outer wall of the house",
             "correct": False,
             "why": "Keeping rain out is the wall's job. The foam is fitted "
                    "to stop air moving."},
            {"text": "Because foam conducts energy better than still air does "
                     "and spreads it out evenly",
             "correct": False,
             "why": "Foam conducts worse than that, and conducting better "
                    "would be the wrong thing to want."},
            {"text": "Because foam adds warmth of its own to the wall and "
                     "keeps the whole cavity heated",
             "correct": False,
             "why": "Foam has no energy supply and adds nothing. It slows "
                    "what is already leaving."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s08",
        "band": "standard",
        "text": "Why do several thin layers of clothing keep you warmer than "
                "one thick jumper of the same total weight?",
        "options": [
            {"text": "Because the layers are lighter and easier to move "
                     "around in on a cold day",
             "correct": False,
             "why": "Comfort is a real advantage but it is not why they are "
                    "warmer."},
            {"text": "Because more layers make more warmth of their own than a "
                     "single thick jumper does",
             "correct": False,
             "why": "No layer makes warmth. All of it comes from the body "
                    "inside them."},
            {"text": "Because thin fabrics are better insulators than thick "
                     "ones are, layer for layer",
             "correct": False,
             "why": "A thin fabric on its own insulates worse. The trapped "
                    "air between them is the reason."},
            {"text": "Because each gap between layers traps another pocket of "
                     "still air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s09",
        "band": "standard",
        "text": "A walker's jumper gets soaked and they feel much colder in "
                "it. Why does a wet jumper insulate so badly?",
        "options": [
            {"text": "Because water has filled the air pockets, and water "
                     "conducts far better than air",
             "correct": True},
            {"text": "Because water is colder than air and brings that cold "
                     "into the fibres with it",
             "correct": False,
             "why": "There is no cold to bring. Rain at air temperature still "
                    "ruins the insulation."},
            {"text": "Because wet wool cannot reflect the body's radiation "
                     "back",
             "correct": False,
             "why": "Wool was never working by reflection. It works by "
                    "trapping air, and the water has replaced it."},
            {"text": "Because wet fabric becomes heavier and presses down",
             "correct": False,
             "why": "Weight is not the mechanism. Water replacing air in the "
                    "gaps is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s10",
        "band": "standard",
        "text": "A sleeping bag squashed flat under a camper insulates much "
                "worse underneath than on top. Explain.",
        "options": [
            {"text": "Because the camper's weight squeezes the trapped air "
                     "out of the filling",
             "correct": True},
            {"text": "Because the ground is colder than the air, and that cold "
                     "moves upwards into the bag itself",
             "correct": False,
             "why": "Cold does not move anywhere. Energy leaves the camper, "
                    "and the flattened filling lets it go faster."},
            {"text": "Because the underside of a bag is made of a different "
                     "and thinner material",
             "correct": False,
             "why": "It is the same bag all round. Only the squashing "
                    "differs."},
            {"text": "Because a squashed bag conducts less than a fluffy one",
             "correct": False,
             "why": "A squashed bag conducts MORE, which is why it feels "
                    "colder underneath."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s11",
        "band": "standard",
        "text": "Emperor penguins huddle tightly together through the "
                "Antarctic winter. How does that reduce their losses?",
        "options": [
            {"text": "The huddle makes extra warmth that the outer birds pass "
                     "inwards to the middle",
             "correct": False,
             "why": "No warmth is made by huddling. Each bird's own body is "
                    "the only source."},
            {"text": "The huddle keeps the wind's cold out of the group "
                     "entirely rather than slowing it",
             "correct": False,
             "why": "There is no cold to keep out, and nothing is stopped "
                    "entirely — only slowed."},
            {"text": "Each bird has less surface exposed to the cold air, and "
                     "the trapped air between them is still",
             "correct": True},
            {"text": "The birds in the middle stop emitting infrared",
             "correct": False,
             "why": "Every bird emits all the time. What changes is what the "
                    "emission lands on."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s12",
        "band": "standard",
        "text": "A polar bear's coat is made of hollow hairs over a thick "
                "layer of fat. What does each part do?",
        "options": [
            {"text": "The hollow hairs make warmth and the fat stores it up",
             "correct": False,
             "why": "Neither makes warmth. The bear's own body supplies all "
                    "of it."},
            {"text": "The hollow hairs trap air and the fat is a thick layer "
                     "that conducts badly",
             "correct": True},
            {"text": "The hollow hairs keep the cold out and the fat keeps "
                     "any remaining cold from reaching the skin",
             "correct": False,
             "why": "Cold is not a substance that can be kept out. Both parts "
                    "slow energy leaving."},
            {"text": "Both parts reflect the Sun's radiation away in summer",
             "correct": False,
             "why": "A polar bear's problem is losing energy, not gaining it. "
                    "Both parts slow the loss."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s13",
        "band": "standard",
        "text": "A wetsuit lets a thin layer of water in and the diver still "
                "stays warmer. How does that work?",
        "options": [
            {"text": "The suit makes the water inside it warmer than the sea "
                     "outside before the diver has even got in",
             "correct": False,
             "why": "The suit warms nothing. The diver's own body warms that "
                    "thin layer."},
            {"text": "The water inside is held still, so the diver only has "
                     "to warm that layer once",
             "correct": True},
            {"text": "The water inside the suit conducts energy back into the "
                     "diver from the sea outside",
             "correct": False,
             "why": "The sea is colder than the diver, so energy flows "
                    "outwards, never in."},
            {"text": "The rubber stops the cold of the sea reaching the skin",
             "correct": False,
             "why": "There is no cold to stop. The rubber and the still water "
                    "slow the energy leaving."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s14",
        "band": "standard",
        "text": "A hot water tank is fitted with a thick jacket. What does "
                "that achieve, and what does it not?",
        "options": [
            {"text": "It makes the water hotter than the boiler alone could, "
                     "and saves a good deal on the fuel bill",
             "correct": False,
             "why": "A jacket cannot raise the temperature above what the "
                    "boiler delivers. It slows the loss."},
            {"text": "It stops the water cooling at all, so the boiler never "
                     "has to come on again",
             "correct": False,
             "why": "Nothing stops cooling completely. The boiler simply "
                    "fires less often."},
            {"text": "It slows the energy leaving the tank, so the boiler has "
                     "to reheat it less often",
             "correct": True},
            {"text": "It warms the cupboard the tank is standing in",
             "correct": False,
             "why": "A jacket keeps the cupboard cooler, because less energy "
                    "escapes into it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s15",
        "band": "standard",
        "text": "After twenty minutes four beakers read 38, 52, 61 and 70 °C. "
                "Which reading belongs to the best-wrapped beaker?",
        "options": [
            {"text": "38 °C, because the biggest change shows the wrapping "
                     "was doing the most work",
             "correct": False,
             "why": "The biggest fall means the fastest cooling, which is "
                    "what a bare beaker does."},
            {"text": "52 °C, because the middle readings are always the most "
                     "reliable ones to use",
             "correct": False,
             "why": "There is nothing reliable about a middle value here. The "
                    "highest reading is the best insulated."},
            {"text": "61 °C, because a well-wrapped beaker never stays above "
                     "two thirds of its start",
             "correct": False,
             "why": "No such rule exists. The best wrapping simply gives the "
                    "highest remaining temperature."},
            {"text": "70 °C, because the best wrapping leaves the water "
                     "hottest after the same time",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s16",
        "band": "standard",
        "text": "Why is a cooling curve steepest in the first few minutes of "
                "a trial?",
        "options": [
            {"text": "Because the thermometer takes several minutes to settle "
                     "down to a steady reading",
             "correct": False,
             "why": "A thermometer settles in seconds, and the shape is real "
                    "rather than an instrument fault."},
            {"text": "Because the water and the room differ most at the "
                     "start, so energy leaves fastest then",
             "correct": True},
            {"text": "Because the wrapping has not yet had a chance to warm "
                     "up and begin working properly",
             "correct": False,
             "why": "The wrapping works immediately. The steepness comes from "
                    "the temperature difference."},
            {"text": "Because the water holds the most energy at the start",
             "correct": False,
             "why": "It does hold most then, but the rate depends on the "
                    "difference rather than the amount held."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s17",
        "band": "standard",
        "text": "One reading in a set is far off the smooth curve the others "
                "make. What is the right thing to do?",
        "options": [
            {"text": "Rub it out and write in the value the curve would have "
                     "given at that time",
             "correct": False,
             "why": "Writing in a number you did not measure is inventing "
                    "data, whatever the curve suggests."},
            {"text": "Treat it as the true value and redraw the curve so that "
                     "it passes neatly through the point",
             "correct": False,
             "why": "One odd point should not overrule the whole set. It "
                    "needs checking first."},
            {"text": "Ignore it completely and never mention that it happened "
                     "at all in the write-up",
             "correct": False,
             "why": "An anomaly has to be reported, even when it is set aside "
                    "for the conclusion."},
            {"text": "Record it, check it, and repeat that reading if you can",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s18",
        "band": "standard",
        "text": "Why is a cooling trial repeated several times rather than "
                "run once?",
        "options": [
            {"text": "Because repeating shows how much the results scatter "
                     "and makes the mean more trustworthy",
             "correct": True},
            {"text": "Because the wrapping works a little better every time "
                     "it is used on a fresh beaker",
             "correct": False,
             "why": "A wrapping does not improve with use. Repeating is about "
                    "the reliability of the readings."},
            {"text": "Because one run cannot show whether water cools at all "
                     "over twenty-eight minutes",
             "correct": False,
             "why": "One run shows that clearly. What it cannot show is how "
                    "much the result varies."},
            {"text": "Because the room changes between one run and the next",
             "correct": False,
             "why": "The room is held as steady as possible, and repeating is "
                    "not a way of dealing with a drifting room."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s19",
        "band": "standard",
        "text": "The four cooling curves separate clearly. What conclusion do "
                "they properly support?",
        "options": [
            {"text": "That wool produces more warmth than foil does when it "
                     "is wrapped around a beaker",
             "correct": False,
             "why": "No wrapping produces warmth, and the curves say nothing "
                    "about anything being produced."},
            {"text": "That insulation adds nothing at all to a beaker of hot "
                     "water anywhere",
             "correct": False,
             "why": "That is true but it is not what the curves show. They "
                    "are equally consistent with the opposite."},
            {"text": "That a wrapped beaker will stay hot for as long as "
                     "somebody is prepared to leave it",
             "correct": False,
             "why": "Every curve heads for room temperature. None of them "
                    "levels off above it."},
            {"text": "That some wrappings slow the cooling more than others "
                     "do",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s20",
        "band": "standard",
        "text": "Why does a wrapped ice cube lasting longer rule out "
                "insulation being a source of warmth?",
        "options": [
            {"text": "Because a source of warmth would melt the wrapped cube "
                     "sooner, and it lasted longer",
             "correct": True},
            {"text": "Because ice is a much harder substance to keep warm "
                     "than hot water is to keep hot",
             "correct": False,
             "why": "Difficulty is not the point. The direction of the result "
                    "is what rules the claim out."},
            {"text": "Because wool cannot touch ice without melting it at the "
                     "point where the two meet",
             "correct": False,
             "why": "Wool at room temperature melts ice no faster than air "
                    "does. The result is the argument."},
            {"text": "Because the ice trial ran for a much longer time",
             "correct": False,
             "why": "Length of run is not what decides it. A short ice trial "
                    "would rule the claim out just as well."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s21",
        "band": "standard",
        "text": "A student writes that the wool “kept the heat in”. "
                "What is a better way to put it?",
        "options": [
            {"text": "The wool held on to the heat that was already inside "
                     "the beaker at the start",
             "correct": False,
             "why": "The wool holds nothing. It slows a flow rather than "
                    "gripping anything."},
            {"text": "The wool stopped the cold of the room getting into the "
                     "water inside the beaker at all",
             "correct": False,
             "why": "There is no cold to get in. Energy flows out, and the "
                    "wool slows that."},
            {"text": "The wool only slowed the rate at which energy left the "
                     "water",
             "correct": True},
            {"text": "The wool gave the water extra heat as it cooled down",
             "correct": False,
             "why": "It gave nothing. A wrapping has no energy supply of its "
                    "own."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s22",
        "band": "standard",
        "text": "A draught excluder at the bottom of a door saves energy. "
                "Which route is it working on?",
        "options": [
            {"text": "Conduction, because the door itself becomes a much "
                     "thicker barrier once it has been fitted",
             "correct": False,
             "why": "It sits at the gap rather than on the door, and the door "
                    "was never the leak."},
            {"text": "Radiation, because it stops infrared escaping straight "
                     "under the door and out",
             "correct": False,
             "why": "Very little radiation escapes through a narrow gap. "
                    "Moving air is what does."},
            {"text": "Convection, because it stops warm air flowing out "
                     "through the gap",
             "correct": True},
            {"text": "All three, because a gap is open to every route at once",
             "correct": False,
             "why": "The dominant loss through a draughty gap is the moving "
                    "air, which is convection."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s23",
        "band": "standard",
        "text": "Why does a foam cup keep a drink hot for longer than a paper "
                "one of the same thickness?",
        "options": [
            {"text": "Because foam is warmer than paper before the drink is "
                     "poured into either of them",
             "correct": False,
             "why": "Both start at room temperature. Neither is warmer than "
                    "the other to begin with."},
            {"text": "Because foam is full of tiny trapped air bubbles, and "
                     "air conducts badly",
             "correct": True},
            {"text": "Because foam reflects the drink's radiation back into "
                     "it in the way that shiny foil would",
             "correct": False,
             "why": "Foam is not shiny and reflects very little. Its trapped "
                    "air is what matters."},
            {"text": "Because paper soaks up the drink's energy and holds it",
             "correct": False,
             "why": "Paper holds very little energy, and holding is not the "
                    "same as passing on slowly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s24",
        "band": "standard",
        "text": "A freezer has unusually thick walls. What is the energy "
                "flowing through them doing?",
        "options": [
            {"text": "Flowing outwards from the freezer into the kitchen, "
                     "which is why the walls are thick",
             "correct": False,
             "why": "The inside is the colder side, so the flow runs the "
                    "other way."},
            {"text": "Flowing in both directions equally, so the thick walls "
                     "are there to balance the two",
             "correct": False,
             "why": "Energy flows one way, from the warmer kitchen to the "
                    "colder inside."},
            {"text": "Not flowing at all, because the walls are thick enough "
                     "to stop it completely",
             "correct": False,
             "why": "It is slowed, never stopped, which is why the motor has "
                    "to keep running."},
            {"text": "Flowing inwards from the warm kitchen, and the thick "
                     "walls slow that down",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s25",
        "band": "standard",
        "text": "Three layers of wool beat one layer clearly on the curves. "
                "What does that tell you about trapped air?",
        "options": [
            {"text": "That more trapped air means a slower transfer through "
                     "the wrapping",
             "correct": True},
            {"text": "That wool stops working altogether once a single layer "
                     "has been wrapped round the beaker",
             "correct": False,
             "why": "One layer works well. Three simply work better, which is "
                    "the point of the comparison."},
            {"text": "That the extra layers make warmth that the first layer "
                     "on its own could not",
             "correct": False,
             "why": "No layer makes warmth. All the energy came from the hot "
                    "water."},
            {"text": "That air is a better conductor than wool fibre is",
             "correct": False,
             "why": "Air conducts far worse than wool fibre, which is exactly "
                    "why trapping it helps."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s26",
        "band": "standard",
        "text": "Why does a cool box need a well-fitting lid as well as thick "
                "walls?",
        "options": [
            {"text": "Because a loose lid lets warm air move in and out, "
                     "which the walls cannot prevent",
             "correct": True},
            {"text": "Because a lid stops the cold inside the box escaping "
                     "upwards out of the top",
             "correct": False,
             "why": "There is no cold to escape. The lid closes a route "
                    "energy takes coming in."},
            {"text": "Because the lid is the part of the box that makes the "
                     "inside cold in the first place",
             "correct": False,
             "why": "No part of the box makes anything cold. The ice inside "
                    "does that."},
            {"text": "Because thick walls only work when a box is sealed shut",
             "correct": False,
             "why": "The walls work either way. The lid closes a separate "
                    "route of its own."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s27",
        "band": "standard",
        "text": "Two identical rooms are heated to 21 °C and the heating is "
                "switched off. One has insulated walls. Predict.",
        "options": [
            {"text": "Both cool at the same rate, because both rooms start at "
                     "the same temperature as each other",
             "correct": False,
             "why": "The starting temperature is the same, but the rate at "
                    "which energy leaves is not."},
            {"text": "The insulated room stays warmer for longer, though both "
                     "end at the outside temperature",
             "correct": True},
            {"text": "The insulated room stays at 21 °C indefinitely, because "
                     "its walls stop the transfer",
             "correct": False,
             "why": "Insulation slows a flow and never stops one. Both rooms "
                    "cool in the end."},
            {"text": "The insulated room cools faster, because its walls hold "
                     "less energy than bare ones do",
             "correct": False,
             "why": "Insulated walls slow the loss, so that room cools more "
                    "slowly rather than faster."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s28",
        "band": "standard",
        "text": "Why is insulating a loft usually a better first buy than "
                "insulating a ground floor?",
        "options": [
            {"text": "Because a loft is easier to reach, and nothing else "
                     "about the two is different at all",
             "correct": False,
             "why": "Access helps with the cost, but the size of the loss is "
                    "the real reason."},
            {"text": "Because a floor is already warm, so there is nothing "
                     "left for insulation to do down there",
             "correct": False,
             "why": "A floor loses energy too. It simply loses less than a "
                    "roof does."},
            {"text": "Because warm air rises, so more energy is leaving "
                     "through the roof than through the floor",
             "correct": True},
            {"text": "Because loft insulation is the only kind that works",
             "correct": False,
             "why": "Floor and wall insulation both work. The loft is chosen "
                    "because the loss there is biggest."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s29",
        "band": "standard",
        "text": "Why would the trial prove nothing without the unwrapped "
                "beaker?",
        "options": [
            {"text": "Because the thermometers could not be checked against "
                     "one another without a bare beaker there",
             "correct": False,
             "why": "Checking thermometers is a separate job. The bare beaker "
                    "is a comparison, not a calibration."},
            {"text": "Because a bare beaker cools at a steady rate that the "
                     "wrapped ones can be divided by",
             "correct": False,
             "why": "No beaker cools at a steady rate, and nothing is divided "
                    "by anything here."},
            {"text": "Because the room needs a beaker in it that is warming "
                     "the air up for all the others",
             "correct": False,
             "why": "The room is meant to stay steady, and no beaker is there "
                    "to warm it."},
            {"text": "Because there would be nothing to compare the wrapped "
                     "beakers against",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s30",
        "band": "standard",
        "text": "Halfway through the trial somebody opens a window and the "
                "room cools. What does that do to the results?",
        "options": [
            {"text": "Nothing at all, since every beaker is standing in the "
                     "same room as all the others",
             "correct": False,
             "why": "It affects them all, which is the trouble: the trial no "
                    "longer measures what it set out to."},
            {"text": "It makes every beaker cool faster, so the comparison "
                     "with the first half is spoiled",
             "correct": True},
            {"text": "It makes the wrapped beakers cool faster and leaves the "
                     "bare one exactly as it was",
             "correct": False,
             "why": "A bigger difference speeds every beaker up, and the bare "
                    "one most of all."},
            {"text": "It improves the trial by making the differences clearer",
             "correct": False,
             "why": "A control variable that changes mid-run spoils a trial "
                    "rather than sharpening it."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · harder ─────────────────────────────────
    {
        "id": "p1-07-h07",
        "band": "harder",
        "text": "Why does every cooling curve flatten out at room temperature "
                "rather than carrying on downwards?",
        "options": [
            {"text": "Because the water and the room are then at the same "
                     "temperature, so there is no net flow",
             "correct": True},
            {"text": "Because the insulation finally starts working properly "
                     "once the water inside has cooled a little",
             "correct": False,
             "why": "The wrapping works from the first second. What changes "
                    "is the temperature difference."},
            {"text": "Because the thermometer cannot read below the "
                     "temperature of the room around it",
             "correct": False,
             "why": "A thermometer reads well below room temperature — try it "
                    "in a fridge."},
            {"text": "Because the water has run out of energy by then",
             "correct": False,
             "why": "It still holds a great deal. It has simply stopped being "
                    "hotter than the room."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h08",
        "band": "harder",
        "text": "A student says the three-layer beaker staying hottest proves "
                "wool adds warmth. Why does it not?",
        "options": [
            {"text": "Because the beakers were not left running long enough "
                     "for any real difference between them to show",
             "correct": False,
             "why": "The difference is large and clear. The trouble is that "
                    "two explanations fit it equally."},
            {"text": "Because a curve that slows the loss and a wrapping that "
                     "adds warmth both fit those numbers",
             "correct": True},
            {"text": "Because the three-layer beaker did not in fact stay the "
                     "hottest of the four beakers",
             "correct": False,
             "why": "It did stay hottest. The argument is about what that "
                    "result can and cannot show."},
            {"text": "Because wool cannot be measured accurately",
             "correct": False,
             "why": "Nothing about measuring wool is at issue. The problem is "
                    "which explanation the data picks out."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h09",
        "band": "harder",
        "text": "You want a trial that tells a warmth-adding wrapping apart "
                "from a flow-slowing one. What must it do?",
        "options": [
            {"text": "Run the two wrappings against each other for far longer "
                     "than twenty-eight minutes",
             "correct": False,
             "why": "Longer runs give the same shape of result. The direction "
                    "of the flow has to change."},
            {"text": "Use more layers of wool, so that any warmth being added "
                     "would show up more clearly still",
             "correct": False,
             "why": "More layers make the two explanations agree more "
                    "closely, not less."},
            {"text": "Wrap something COLDER than the room, where the two "
                     "explanations predict opposite results",
             "correct": True},
            {"text": "Measure the wool's own temperature during the run",
             "correct": False,
             "why": "The wool warms on the way through in either account, so "
                    "that reading separates nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h10",
        "band": "harder",
        "text": "Why is the hot-water trial not decisive on its own, when it "
                "produces such clear separated curves?",
        "options": [
            {"text": "Because its readings are taken by hand and so are never "
                     "precise enough to decide anything",
             "correct": False,
             "why": "Precision is not the issue. Perfect readings would leave "
                    "the same two explanations standing."},
            {"text": "Because it only ever ran for twenty-eight minutes, "
                     "which is too short a time to conclude from",
             "correct": False,
             "why": "A longer run gives the same shape. Time is not what "
                    "separates the explanations."},
            {"text": "Because a wrapping that added warmth would produce "
                     "exactly the same curves",
             "correct": True},
            {"text": "Because hot water cools far too quickly for anybody to "
                     "measure it well in a classroom",
             "correct": False,
             "why": "It cools slowly enough to read easily. The problem is "
                    "what the numbers can rule out."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h11",
        "band": "harder",
        "text": "Could a perfect insulator ever make the water inside a "
                "beaker colder than the room around it?",
        "options": [
            {"text": "Yes, because a perfect insulator would keep drawing "
                     "energy out of whatever it wrapped",
             "correct": False,
             "why": "An insulator draws nothing. It only slows a flow that is "
                    "already happening."},
            {"text": "Yes, but only if the wrapping were shiny as well as "
                     "thick enough to work properly",
             "correct": False,
             "why": "Shine changes which route is slowed, not the direction "
                    "energy can flow."},
            {"text": "No, because energy never flows from a colder thing to a "
                     "warmer one on its own",
             "correct": True},
            {"text": "No, because a perfect insulator cannot be built at all",
             "correct": False,
             "why": "Even a perfect one could not do it, so the answer does "
                    "not depend on whether it exists."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h12",
        "band": "harder",
        "text": "Two identical lagged tanks hold water at 90 °C and 40 °C in "
                "the same room. Which loses energy faster, and why?",
        "options": [
            {"text": "The 90 °C tank, because the bigger difference from the "
                     "room drives a faster flow",
             "correct": True},
            {"text": "The 40 °C tank, because water that has already cooled "
                     "gives up the rest of its energy sooner",
             "correct": False,
             "why": "Cooling does not speed up as water gets cooler. It "
                    "slows, because the difference shrinks."},
            {"text": "Both at the same rate, since the lagging on the two "
                     "tanks is exactly the same thickness",
             "correct": False,
             "why": "Identical lagging does not give identical rates. The "
                    "temperature difference decides the rate."},
            {"text": "Neither, because lagging stops the loss on both tanks",
             "correct": False,
             "why": "Lagging slows a loss; it never stops one. Both tanks are "
                    "losing energy the whole time."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h13",
        "band": "harder",
        "text": "Why is a vacuum a better barrier against conduction and "
                "convection than any solid insulator can be?",
        "options": [
            {"text": "Because a vacuum is far colder than any solid material "
                     "that could be used instead of it",
             "correct": False,
             "why": "Temperature is not what makes a barrier. A vacuum works "
                    "because it is empty."},
            {"text": "Because a vacuum gap is thicker than any wrapping "
                     "anybody could put round a flask",
             "correct": False,
             "why": "A vacuum gap is usually very thin. Its emptiness rather "
                    "than its thickness is the point."},
            {"text": "Because a vacuum reflects energy back the way it came "
                     "instead of letting any across",
             "correct": False,
             "why": "A vacuum reflects nothing. Silvered surfaces do that, "
                    "and they are a separate feature."},
            {"text": "Because both of those routes need particles, and a "
                     "vacuum has none at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h14",
        "band": "harder",
        "text": "A student says doubling the thickness of an insulator must "
                "exactly double the time something stays hot. Evaluate.",
        "options": [
            {"text": "Correct, because twice the thickness means exactly "
                     "twice as long a journey for the energy",
             "correct": False,
             "why": "The journey is longer, but the loss also depends on the "
                    "shrinking temperature difference."},
            {"text": "Wrong, because thickness makes no difference at all to "
                     "how long something stays hot",
             "correct": False,
             "why": "Thickness makes a large difference. The claim is wrong "
                    "about the exactness, not the direction."},
            {"text": "Wrong — it slows the loss, but the falling temperature "
                     "difference also slows it, so it is not a neat doubling",
             "correct": True},
            {"text": "Correct, but only when the insulator is wool",
             "correct": False,
             "why": "No material gives a neat doubling, wool included."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h15",
        "band": "harder",
        "text": "Why does a very well insulated house still get cold "
                "overnight if the heating is switched off?",
        "options": [
            {"text": "Because insulation only works while a heating system is "
                     "running to supply it with energy",
             "correct": False,
             "why": "Insulation needs no supply. It works whether the heating "
                    "is on or off."},
            {"text": "Because the cold of the night is strong enough to get "
                     "through any thickness of insulation",
             "correct": False,
             "why": "There is no cold coming in. Energy is going out, just "
                    "more slowly."},
            {"text": "Because insulation only slows the loss without stopping "
                     "it, and the night is long",
             "correct": True},
            {"text": "Because a cold house conducts energy a great deal better "
                     "than a warm one does",
             "correct": False,
             "why": "The walls conduct at much the same rate. The loss slows "
                    "as the house cools, rather than speeding up."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h16",
        "band": "harder",
        "text": "A plumber lags the cold water pipes as well as the hot ones. "
                "What is the point of that?",
        "options": [
            {"text": "It makes the cold water colder, which is what people "
                     "want from a cold tap in summer",
             "correct": False,
             "why": "Lagging cannot lower a temperature. It only slows a "
                    "change."},
            {"text": "It slows energy reaching the cold pipes, so they are "
                     "slower to freeze and slower to warm",
             "correct": True},
            {"text": "It stops the cold in the pipes escaping into the rooms "
                     "of the house during the coldest winter months",
             "correct": False,
             "why": "Cold does not escape anywhere. Energy moves, and here it "
                    "would be moving into the pipe."},
            {"text": "It has no effect and is done out of habit",
             "correct": False,
             "why": "It has a real effect in both directions, which is why "
                    "plumbers do it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h17",
        "band": "harder",
        "text": "Why might a designer use both shiny foil AND thick wool "
                "around the same hot tank?",
        "options": [
            {"text": "Because two wrappings of any kind always work better "
                     "than one wrapping does on its own",
             "correct": False,
             "why": "Two of the SAME kind help less. These two are chosen "
                    "because they block different routes."},
            {"text": "Because the foil adds warmth and the wool keeps that "
                     "warmth from escaping again",
             "correct": False,
             "why": "Neither adds warmth. Both slow the energy already "
                    "leaving the tank."},
            {"text": "Because they block different routes — the foil works on "
                     "radiation and the wool on the other two",
             "correct": True},
            {"text": "Because foil conducts badly and wool conducts well",
             "correct": False,
             "why": "Exactly the wrong way round: foil is a metal and "
                    "conducts well, and wool conducts badly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h18",
        "band": "harder",
        "text": "A survival bag is a thin plastic sack with no warmth of its "
                "own. Why is it worth carrying on a hill walk?",
        "options": [
            {"text": "Because plastic is warmer than the air, so it raises "
                     "the temperature inside the bag at once",
             "correct": False,
             "why": "It comes out of a rucksack at air temperature and adds "
                    "nothing of its own."},
            {"text": "Because it slows the energy leaving the walker and "
                     "stops the wind carrying it away",
             "correct": True},
            {"text": "Because it keeps the cold of the hillside off the "
                     "walker until help arrives on the scene",
             "correct": False,
             "why": "There is no cold to keep off. The bag slows the energy "
                    "the walker is losing."},
            {"text": "Because a sealed bag makes the walker's own body work a "
                     "good deal harder than usual",
             "correct": False,
             "why": "The body runs at the same rate. What changes is how much "
                    "energy escapes."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h19",
        "band": "harder",
        "text": "Evaluate the statement: “a good insulator keeps the "
                "cold out.”",
        "options": [
            {"text": "Correct, and it is much the clearest way of describing "
                     "what an insulator actually does for a house",
             "correct": False,
             "why": "It is a common way of speaking and it describes the "
                    "physics wrongly."},
            {"text": "Correct, but only for a house rather than for a small "
                     "beaker standing on a laboratory bench",
             "correct": False,
             "why": "The same physics applies to both. Nothing about scale "
                    "makes the wording right."},
            {"text": "Wrong, because a good insulator lets the cold in faster",
             "correct": False,
             "why": "There is still no cold to let in. The wording is wrong "
                    "in both directions."},
            {"text": "Wrong — there is no cold to keep out, only energy "
                     "flowing, and the insulator slows that",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h20",
        "band": "harder",
        "text": "An igloo is built of snow and can be far warmer inside than "
                "the air outside. How is that possible?",
        "options": [
            {"text": "The snow makes warmth as it packs down under the weight "
                     "of the blocks above it",
             "correct": False,
             "why": "Packing snow makes no warmth. The people and lamps "
                    "inside are the only source."},
            {"text": "The snow melts slowly and the melting releases warmth "
                     "into the air inside the igloo itself",
             "correct": False,
             "why": "Melting takes energy in rather than giving it out, so it "
                    "would cool the igloo."},
            {"text": "Packed snow traps a great deal of air, so it slows the "
                     "loss from the people inside",
             "correct": True},
            {"text": "The dome shape reflects the cold of the sky away",
             "correct": False,
             "why": "There is no cold to reflect. The snow works by trapping "
                    "air and slowing the loss."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h21",
        "band": "harder",
        "text": "Two duvets weigh the same but one is far thicker. Why is the "
                "thicker one usually the warmer?",
        "options": [
            {"text": "Because a thicker duvet presses down harder and keeps "
                     "the sleeper's warmth against the skin",
             "correct": False,
             "why": "Pressing closer would help conduction away from the "
                    "sleeper. Weight is not the mechanism."},
            {"text": "Because the same filling spread thicker holds far more "
                     "still air between the fibres",
             "correct": True},
            {"text": "Because a thicker duvet contains a heavier filling than "
                     "the thin one does, weight for weight",
             "correct": False,
             "why": "The stem says they weigh the same, so neither holds more "
                    "filling than the other."},
            {"text": "Because thick fabric makes more warmth than thin fabric",
             "correct": False,
             "why": "No fabric makes warmth. The sleeper's own body is the "
                    "only source of it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h22",
        "band": "harder",
        "text": "Damp cavity wall insulation works far worse than dry. "
                "Explain, using what you know about trapped air.",
        "options": [
            {"text": "Damp foam becomes heavier, and heavy materials always "
                     "conduct energy more quickly than light ones",
             "correct": False,
             "why": "Weight does not decide conduction. Water replacing air "
                    "does."},
            {"text": "Damp foam is colder than dry foam, so more energy is "
                     "pulled through it from the warm room",
             "correct": False,
             "why": "Both sit at the same temperature in the wall. The "
                    "difference is what fills the spaces."},
            {"text": "Water has filled the spaces that held still air, and "
                     "water conducts far better than air",
             "correct": True},
            {"text": "Damp foam shrinks away from the wall and leaves a gap",
             "correct": False,
             "why": "A gap would insulate reasonably well on its own. The "
                    "water in the foam is the real problem."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h23",
        "band": "harder",
        "text": "Tank A has 50 mm of lagging and tank B has 100 mm. Both are "
                "filled at 80 °C. Predict the two curves.",
        "options": [
            {"text": "B falls more slowly than A, and both eventually reach "
                     "room temperature",
             "correct": True},
            {"text": "B falls more slowly than A, and B never reaches room "
                     "temperature at all, ever",
             "correct": False,
             "why": "Every tank reaches room temperature in the end. Lagging "
                    "only decides how long it takes."},
            {"text": "A and B fall at the same rate, because the lagging on "
                     "both of them is made of one material",
             "correct": False,
             "why": "Thickness changes the rate even for one material, which "
                    "is why B is slower."},
            {"text": "A falls more slowly, because thin lagging traps more air "
                     "than thick lagging does",
             "correct": False,
             "why": "Thicker lagging holds more trapped air, not less, so B "
                    "is the slower of the two."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h24",
        "band": "harder",
        "text": "The same trial is repeated in a much colder room. What "
                "happens to the shape of the curves?",
        "options": [
            {"text": "They stay exactly the same, because the water still "
                     "starts at the same temperature as before",
             "correct": False,
             "why": "The start is the same but the difference from the room "
                    "is larger, so the fall is steeper."},
            {"text": "They become flatter, because a cold room slows every "
                     "kind of energy transfer down",
             "correct": False,
             "why": "A colder room means a bigger difference, which speeds "
                    "the transfer up rather than slowing it."},
            {"text": "Only the bare beaker's curve changes, since the wrapped "
                     "ones are protected from the room",
             "correct": False,
             "why": "Every beaker is affected. The wrapped ones are slowed, "
                    "not sealed off."},
            {"text": "They all become steeper, and they level off at the new "
                     "lower room temperature",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h25",
        "band": "harder",
        "text": "Why is comparing the steepness of two curves often fairer "
                "than comparing their final temperatures?",
        "options": [
            {"text": "Because the final temperature is impossible to measure "
                     "accurately at the end of a long trial",
             "correct": False,
             "why": "The final reading is as easy as any other. The problem "
                    "is what it can tell you."},
            {"text": "Because the steepness shows the RATE of loss, while a "
                     "final value depends on how long you waited",
             "correct": True},
            {"text": "Because steepness can be read off a graph without any "
                     "measurements having been taken at all",
             "correct": False,
             "why": "Steepness comes from the measurements like everything "
                    "else on the graph."},
            {"text": "Because a final temperature is always the same anyway",
             "correct": False,
             "why": "It differs a great deal between wrappings partway "
                    "through, which is the whole point of the trial."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h26",
        "band": "harder",
        "text": "In one run the foil-wrapped beaker beats the single wool "
                "layer. What is the sensible conclusion?",
        "options": [
            {"text": "That foil must add warmth, since it beat a material "
                     "everybody expects to be better",
             "correct": False,
             "why": "No wrapping adds warmth, and a single result would never "
                    "show that in any case."},
            {"text": "That the trial must have gone wrong somewhere, because "
                     "wool is always the better insulator",
             "correct": False,
             "why": "Foil beating one thin layer of wool is a perfectly "
                    "believable result, not an error."},
            {"text": "That blocking radiation can matter as much as trapping "
                     "air, and the run is worth repeating",
             "correct": True},
            {"text": "That wool does not insulate at all",
             "correct": False,
             "why": "Wool clearly beat the bare beaker. Losing to foil once "
                    "does not make it useless."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h27",
        "band": "harder",
        "text": "Why can insulation reduce a heating bill a great deal but "
                "never reduce it to nothing?",
        "options": [
            {"text": "Because the boiler has to keep running whatever the "
                     "walls of the house are made of",
             "correct": False,
             "why": "The boiler runs because energy is still escaping. It is "
                    "the escape that sets the bill."},
            {"text": "Because insulation slows the loss but never stops it, "
                     "so some energy always has to be replaced",
             "correct": True},
            {"text": "Because the insulation itself uses up a small amount of "
                     "energy the whole time it is in place",
             "correct": False,
             "why": "Insulation uses none at all. It is not connected to "
                    "anything."},
            {"text": "Because a house has windows that cannot be insulated",
             "correct": False,
             "why": "Windows can be double glazed. Even a house with none "
                    "would still lose energy through its walls."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h28",
        "band": "harder",
        "text": "Loft insulation usually saves more per pound spent than "
                "triple glazing does. What explains that?",
        "options": [
            {"text": "Windows do not lose any energy at all, so improving "
                     "them can never save anything",
             "correct": False,
             "why": "Windows lose a great deal. They are simply a smaller "
                    "share of the total than the roof."},
            {"text": "Loft insulation is the only kind of insulation that "
                     "actually works in a real house",
             "correct": False,
             "why": "Glazing works too. The comparison is about how much "
                    "each saves for what it costs."},
            {"text": "Triple glazing makes a room colder by blocking the "
                     "sunlight that would have warmed it up",
             "correct": False,
             "why": "Glazing still lets sunlight through. That is not why the "
                    "loft comes first."},
            {"text": "More energy leaves through the roof, and rolls of "
                     "insulation cost far less than new windows",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h29",
        "band": "harder",
        "text": "Design a single trial that shows a cool box works in both "
                "directions. What would you do?",
        "options": [
            {"text": "Put hot food into one box and nothing at all into a "
                     "second box, and compare the two after an hour",
             "correct": False,
             "why": "An empty box gives nothing to compare against, and only "
                    "one direction has been tested."},
            {"text": "Put hot food in the box on a hot day and then again on a "
                     "cold day, and compare the two runs",
             "correct": False,
             "why": "Both runs test the outward direction. Nothing there "
                    "shows the box works inwards."},
            {"text": "Put hot food in the box and cold food in an identical "
                     "one, each beside an unwrapped sample",
             "correct": True},
            {"text": "Leave the box empty in a warm room and measure it",
             "correct": False,
             "why": "An empty box at room temperature has no flow to slow, so "
                    "nothing would be learnt."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h30",
        "band": "harder",
        "text": "A student wraps a beaker in three layers of wool but leaves "
                "the top open. Predict the result and explain it.",
        "options": [
            {"text": "It cools as slowly as a beaker with a lid, because the "
                     "wool handles every route on its own",
             "correct": False,
             "why": "Wool on the sides does nothing about the open top, which "
                    "is a route of its own."},
            {"text": "It cools faster than a bare beaker, because the wool "
                     "draws energy up and out of the open top",
             "correct": False,
             "why": "Wool draws nothing anywhere. The wrapped beaker still "
                    "beats the bare one."},
            {"text": "It cools at exactly the same rate as a bare beaker, "
                     "since an open top undoes any wrapping",
             "correct": False,
             "why": "The wool still slows the sides, so it beats the bare "
                    "beaker even with the top open."},
            {"text": "It beats the bare beaker but loses to the lidded one, "
                     "because warm air still escapes upwards",
             "correct": True},
        ],
        "figure": None,
    },
]
