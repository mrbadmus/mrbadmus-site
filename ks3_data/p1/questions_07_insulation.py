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
            {"text": "It melts faster, because the coat is warm and passes "
                     "that warmth in",
             "correct": False,
             "why": "The coat has no warmth of its own. This is the ice "
                    "trial in a different hat."},
            {"text": "It melts at the same rate, because coats only work on "
                     "living things",
             "correct": False,
             "why": "Nothing about insulation requires a body. It slows a "
                    "flow either way."},
            {"text": "It melts more quickly at first and then much more "
                     "slowly afterwards",
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
]
