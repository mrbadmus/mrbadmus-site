"""P1 lesson 03 — Conservation of energy: twelve questions.

These probe the two things the lesson adds: that the totals before and after
are the same number, and that a quantity which is never consumed can never be
the REASON anything happened. The distractors are built from ENER-11 — energy
gets used up — and from the two habits `#s-count` and `#s-why` are aimed at:
reading "wasted" as "destroyed", and answering a how-or-why question with an
energy account that is true and explains nothing.

⚠️ Four of the twelve are arithmetic, because `KS3.P.CIS.01` asks for energy
"as a quantity that can be quantified and calculated" and a bank with no
number in it would not be testing the statement.

Answer positions are deliberately 2 zeros, 3 ones, 3 twos and 4 threes, which
brings the unit's running distribution back to level (MRB-278). No figures.
"""

UNIT = "P1"
LESSON = "conservation-of-energy"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-03-e01",
        "band": "easier",
        "text": "A machine is given 100 J and 40 J of that does the job it "
                "was built for. How much warmed the surroundings?",
        "options": [
            {"text": "140 J, because you add the two together",
             "correct": False,
             "why": "The two parts add up TO the whole, not on top of it. "
                    "Nothing more than 100 J went in."},
            {"text": "40 J, the same as the useful part",
             "correct": False,
             "why": "That is the part that did the job. The question asks "
                    "about the other part."},
            {"text": "It cannot be worked out without knowing the machine",
             "correct": False,
             "why": "Conservation does not care which machine it is. "
                    "Whatever went in has to come out somewhere."},
            {"text": "60 J",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e02",
        "band": "easier",
        "text": "What does the conservation of energy say?",
        "options": [
            {"text": "Energy should not be wasted, so machines must be "
                     "efficient",
             "correct": False,
             "why": "That is good advice about bills, not a law of physics. "
                    "The law is about a total, and it holds whether anyone "
                    "is careful or not."},
            {"text": "Some energy is always lost, so the total goes down",
             "correct": False,
             "why": "Nothing is ever lost. What people call losing is energy "
                    "ending up somewhere nobody wanted it."},
            {"text": "The total before a change equals the total after it",
             "correct": True},
            {"text": "Energy can be created but never destroyed",
             "correct": False,
             "why": "Neither. It cannot be created either, which is the half "
                    "that stops a perpetual motion machine."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e03",
        "band": "easier",
        "text": "A phone battery goes flat. Where has the energy gone?",
        "options": [
            {"text": "It has been used up and no longer exists",
             "correct": False,
             "why": "Nothing is ever used up in that sense. Weigh the room "
                    "before and after and the total has not moved."},
            {"text": "Into the phone, your hand, the air and the table, as "
                     "warmth",
             "correct": True},
            {"text": "It is still in the battery but too weak to reach the "
                     "circuit",
             "correct": False,
             "why": "The substances inside have genuinely changed into ones "
                    "that hold less. Nothing is stuck in there."},
            {"text": "It turned into the electricity that ran the phone, and "
                     "that is gone",
             "correct": False,
             "why": "An electric current is a pathway, not a destination. It "
                    "carried the energy somewhere, and the question is where."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-e04",
        "band": "easier",
        "text": "An LED lamp takes in 4000 J and gives out 1200 J as light. "
                "What warmed the room?",
        "options": [
            {"text": "5200 J, since both amounts have to go somewhere",
             "correct": False,
             "why": "Only 4000 J ever went in. Adding the light on top would "
                    "mean the lamp created some."},
            {"text": "1200 J, the same as the light",
             "correct": False,
             "why": "That is the useful part. It left as light and did not "
                    "warm anything on the way out."},
            {"text": "Nothing, because an LED is efficient",
             "correct": False,
             "why": "An LED is far better than a filament bulb and it is not "
                    "perfect. Feel one after an hour."},
            {"text": "2800 J",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-03-s01",
        "band": "standard",
        "text": "Why is a filament bulb's 95 J of warming called WASTED when "
                "a heater's is not?",
        "options": [
            {"text": "Because waste depends on what you were trying to do",
             "correct": True},
            {"text": "Because a heater is designed to work and a bulb is not",
             "correct": False,
             "why": "Both work exactly as their physics says they will. The "
                    "difference is in the person, not the device."},
            {"text": "Because the bulb's warming is spread more thinly than "
                     "the heater's",
             "correct": False,
             "why": "Both end up warming a room, and by the same route. The "
                    "spreading is the same."},
            {"text": "Because a heater's warming is a different kind of "
                     "energy",
             "correct": False,
             "why": "It is the same thermal store filling in the same way. "
                    "There is only one kind."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s02",
        "band": "standard",
        "text": "A ball is dropped from 1 m and bounces back to 0.6 m. What "
                "has happened to the missing amount?",
        "options": [
            {"text": "It was destroyed by the impact with the floor",
             "correct": False,
             "why": "Impacts destroy no energy. They squash things, and "
                    "squashing warms them."},
            {"text": "It is in the thermal stores of the ball, the floor and "
                     "the air",
             "correct": True},
            {"text": "It is still in the ball's gravitational store, out of "
                     "reach",
             "correct": False,
             "why": "The ball is only 0.6 m up, so its gravitational store is "
                    "genuinely smaller. That IS the missing amount, and the "
                    "question is where it went."},
            {"text": "It went into the ball's kinetic store, which is why it "
                     "moves",
             "correct": False,
             "why": "The ball's kinetic store is empty at the top of the "
                    "bounce, which is the moment being compared."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s03",
        "band": "standard",
        "text": "\"Why did the water in the kettle get hot?\" Which answer "
                "actually explains it?",
        "options": [
            {"text": "Because energy went from a chemical store into the "
                     "water's thermal store",
             "correct": False,
             "why": "True, and it would be equally true of a microwave, a "
                    "flame or a friction heater. It cannot tell them apart, "
                    "so it explains nothing about the kettle."},
            {"text": "Because the kettle was switched on and left for long "
                     "enough to boil",
             "correct": False,
             "why": "That is what someone DID, not what happened inside. It "
                    "restates the question."},
            {"text": "Because a current made the element's particles vibrate, "
                     "and they knocked the water's",
             "correct": True},
            {"text": "Because heat rose from the element and filled the water "
                     "above it",
             "correct": False,
             "why": "Heat is not a substance that can rise or fill anything. "
                    "Say what the particles did."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-s04",
        "band": "standard",
        "text": "Two kettles run for the same time, one holding 1 kg of water "
                "and one holding 2 kg. Which tool answers \"which ends up "
                "hotter?\"",
        "options": [
            {"text": "The mechanism, because the element works differently in "
                     "each",
             "correct": False,
             "why": "The element does exactly the same thing in both. A "
                    "mechanism that is identical cannot separate two cases."},
            {"text": "Neither, because the question cannot be answered "
                     "without measuring",
             "correct": False,
             "why": "It can be answered from first principles, and the "
                    "answer is that the 1 kg kettle wins."},
            {"text": "The mechanism, because heating always depends on how "
                     "the particles collide",
             "correct": False,
             "why": "The collisions are the same in both kettles. Something "
                    "else has to do the separating."},
            {"text": "The energy account, because the same joules are shared "
                     "among more water",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-03-h01",
        "band": "harder",
        "text": "If nothing is ever lost, why can you not run a room "
                "backwards and recharge a battery from the warmth in it?",
        "options": [
            {"text": "Because energy spread evenly has nowhere to flow to",
             "correct": True},
            {"text": "Because some of the energy really was destroyed on the "
                     "way",
             "correct": False,
             "why": "None of it was. Every joule that left the battery is "
                    "still in the room."},
            {"text": "Because the room's energy is a different kind from the "
                     "battery's",
             "correct": False,
             "why": "There is only one kind. What differs is how "
                    "concentrated it is."},
            {"text": "Because batteries can only be charged by an electric "
                     "current",
             "correct": False,
             "why": "That is how we do it, not why the reverse is "
                    "impossible. The reason is about spreading."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h02",
        "band": "harder",
        "text": "A student says a kettle is 90% efficient \"so 10% of the "
                "energy is lost\". Which correction is exact?",
        "options": [
            {"text": "It is 10% that never entered the kettle in the first "
                     "place",
             "correct": False,
             "why": "All of it entered. The question is where inside it "
                    "ended up."},
            {"text": "It is 10% that warmed the kettle body and the "
                     "surroundings instead of the water",
             "correct": True},
            {"text": "It is 10% that was turned into sound and light by the "
                     "element",
             "correct": False,
             "why": "A kettle makes a little noise and no light worth "
                    "counting. Almost all of the 10% is warmth."},
            {"text": "It is 10% that the kettle stored and gave back on the "
                     "next boil",
             "correct": False,
             "why": "A warm kettle does help slightly on the next boil, but "
                    "only if you boil it again within minutes. It is not "
                    "where the 10% goes."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h03",
        "band": "harder",
        "text": "A machine is claimed to give out 110 J for every 100 J put "
                "in. What is the strongest thing you can say?",
        "options": [
            {"text": "It is possible if the machine is very well designed",
             "correct": False,
             "why": "No design helps. The claim is not that it is difficult; "
                    "it is that it has never happened in any change ever "
                    "tested."},
            {"text": "It is possible if the extra comes from the "
                     "surroundings",
             "correct": False,
             "why": "A heat pump does move energy in from outside — and then "
                    "the account has to include the outside, and it balances "
                    "again."},
            {"text": "It is impossible, because 10 J would have to come from "
                     "nowhere",
             "correct": True},
            {"text": "It is impossible, because machines always waste some "
                     "energy",
             "correct": False,
             "why": "True but weaker. Even a perfect frictionless machine "
                    "could not do this, and that is the stronger reason."},
        ],
        "figure": None,
    },
    {
        "id": "p1-03-h04",
        "band": "harder",
        "text": "Which of these is a WHERE question, and so the kind an "
                "energy account answers rather than a mechanism?",
        "options": [
            {"text": "Why does a duvet keep you warm?",
             "correct": False,
             "why": "A why question. The answer is the still air trapped "
                    "between the fibres, which is a mechanism."},
            {"text": "Why does a rolling ball stop on grass but not on ice?",
             "correct": False,
             "why": "A why question. The answer is what the two surfaces are "
                    "doing to the ball, which is a mechanism."},
            {"text": "How does an electric current make a wire get hot?",
             "correct": False,
             "why": "A how question, and the answer is about what the "
                    "electrons and the metal ions are doing."},
            {"text": "What has the rolling ball's movement ended up as?",
             "correct": True},
        ],
        "figure": None,
    },
]
