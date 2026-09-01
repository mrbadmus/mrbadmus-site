"""P2 lesson 02 — Power ratings in watts: twelve questions (MRB-223).

Written against Design's DECODED page. The kettle/router figures, the six
sort cards and the crossover are all hers — except the appliance, which
was a phone charger and is a router since MRB-297 (P2-09). The numbers
are untouched; see the lesson module's docstring.

The discriminations, in the order the lesson builds them:

  · a watt IS a joule per second, so the unit states the definition;
  · a rating is a RATE and says nothing about a total (`ENER-21`) — the
    lesson's whole argument, and where the standard band sits;
  · low power is not no power, and time is what turns it into a bill
    (`ENER-22`);
  · what power IS good for — cables and safety — which is the half
    of the story a student who over-corrects will drop.

⚠️ POSITION IS AUTHORED. The correct option's index cycles 1, 2, 3, 0
through the twelve, giving exactly three of each.

⚠️ None of these restates Rung 1 ("one watt is equal to…") or Rung 2
(the 2000 W kettle against the 15 W router) — check 6 of
`verify_questions.py` forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P2"
LESSON = "power-ratings-in-watts"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p2-02-e01",
        "band": "easier",
        "text": "Which of these is a unit of POWER?",
        "options": [
            {"text": "The joule", "correct": False,
             "why": "A joule is an amount of energy. Power needs a “per "
                    "second” in it."},
            {"text": "The watt", "correct": True},
            {"text": "The kilowatt-hour", "correct": False,
             "why": "The “hour” means a time has already been "
                    "multiplied in, which makes it an amount of energy."},
            {"text": "The kilojoule", "correct": False,
             "why": "A thousand joules is still energy, not a rate."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e02",
        "band": "easier",
        "text": "A lamp is rated 60 W. How much energy does it transfer each "
                "second while it is on?",
        "options": [
            {"text": "60 joules every minute", "correct": False,
             "why": "A watt is per SECOND, not per minute. This answer is "
                    "sixty times too small."},
            {"text": "It depends how long it has been on", "correct": False,
             "why": "The rate does not change with time. That is exactly "
                    "what makes it a rating."},
            {"text": "60 joules", "correct": True},
            {"text": "60 joules in total, then nothing", "correct": False,
             "why": "It transfers 60 J every second it stays on, not 60 J "
                    "once."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e03",
        "band": "easier",
        "text": "Which sentence names an amount of ENERGY rather than a "
                "power?",
        "options": [
            {"text": "This shower is rated 8.5 kW", "correct": False,
             "why": "A rating is always a rate — how fast it transfers "
                    "while running."},
            {"text": "A sprinter peaks at about 1000 W", "correct": False,
             "why": "A peak figure in watts is still a rate, just the "
                    "highest one they can reach."},
            {"text": "The motor draws 400 W", "correct": False,
             "why": "Watts are joules per second, so this is a rate."},
            {"text": "The oven used 1.8 kWh last night", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e04",
        "band": "easier",
        "text": "Two heaters are rated 500 W and 2000 W. What can you say "
                "for certain?",
        "options": [
            {"text": "The 2000 W heater transfers energy four times as fast",
             "correct": True},
            {"text": "The 2000 W heater will cost four times as much to run",
             "correct": False,
             "why": "Only if both run for the same time, and nothing here "
                    "says they do."},
            {"text": "The 2000 W heater holds four times as much energy",
             "correct": False,
             "why": "A heater does not hold energy at all. It transfers it "
                    "while it runs."},
            {"text": "The 500 W heater is more efficient", "correct": False,
             "why": "A rating says nothing about efficiency — only how "
                    "fast the appliance draws energy."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p2-02-s01",
        "band": "standard",
        "text": "A 9 W router runs all day. A 900 W microwave runs for two "
                "minutes. Which transfers more energy in that day?",
        "options": [
            {"text": "The microwave, because 900 W is a hundred times more",
             "correct": False,
             "why": "900 × 120 s = 108 kJ. The router gets "
                    "9 × 86 400 s = 778 kJ. The rating is not the "
                    "whole calculation."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "The router, by about seven times", "correct": True},
            {"text": "They are equal", "correct": False,
             "why": "Work both products out — the router comes out about "
                    "seven times ahead."},
            {"text": "It cannot be decided without knowing the voltage",
             "correct": False,
             "why": "Power and time are all you need. The voltage is already "
                    "inside the power figure."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s02",
        "band": "standard",
        "text": "Why does a 2000 W kettle need thicker wiring than a 15 W "
                "router, even though the router uses more energy over a "
                "day?",
        "options": [
            {"text": "Because it will use more energy in total over its whole "
                     "lifetime than the router",
             "correct": False,
             "why": "Lifetime totals do not heat a cable. What heats it is "
                    "what flows through it at the moment it is running."},
            {"text": "Because thicker cable stores more of the energy on its "
                     "way through",
             "correct": False,
             "why": "Cable does not store energy on the way through. It "
                    "carries it."},
            {"text": "Because the cable has to survive the RATE, and the "
                     "kettle's rate is 130 times higher",
             "correct": True},
            {"text": "Because the kettle is switched on and off far more "
                     "often than a router is",
             "correct": False,
             "why": "Switching frequency is not what the cable rating is "
                    "about. It is about how much flows while it is on."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s03",
        "band": "standard",
        "text": "A set-top box draws 8 W on standby for 8760 hours a year. A "
                "kettle draws 2000 W for 30 hours a year. Which costs more "
                "over the year?",
        "options": [
            {"text": "The kettle, by a wide margin", "correct": False,
             "why": "2000 × 30 = 60 kWh, against the box's "
                    "8 × 8760 ÷ 1000 = 70 kWh. The box is ahead."},
            {"text": "They are about equal, at roughly 8 kWh each",
             "correct": False,
             "why": "Both figures are far larger than that — about 70 and "
                    "60 kilowatt-hours."},
            {"text": "The kettle, because standby is not really drawing "
                     "anything",
             "correct": False,
             "why": "Standby is a LOW power, not no power, and 8 W for a "
                    "whole year adds up."},
            {"text": "The set-top box", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s04",
        "band": "standard",
        "text": "Which piece of information would you still need before you "
                "could work out what an appliance costs to run?",
        "options": [
            {"text": "How long it runs for", "correct": True},
            {"text": "Its power rating", "correct": False,
             "why": "You would need this too, but the question asks what is "
                    "MISSING once you already know the rating."},
            {"text": "Its voltage", "correct": False,
             "why": "The voltage is already accounted for inside the power "
                    "figure."},
            {"text": "The mass of the appliance", "correct": False,
             "why": "Nothing in the calculation uses the mass of the "
                    "appliance."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p2-02-h01",
        "band": "harder",
        "text": "A shop assistant recommends a 1000 W kettle over a 2000 W "
                "one “to save electricity”. What is wrong with the "
                "advice?",
        "options": [
            {"text": "Nothing is wrong — half the power means half the "
                     "energy, so the bill for boiling halves as well",
             "correct": False,
             "why": "Only if the time stayed the same, and it does not. The "
                    "slower kettle runs about twice as long."},
            {"text": "The slower kettle takes about twice as long, so the "
                     "total is roughly the same or slightly worse",
             "correct": True},
            {"text": "A 1000 W kettle cannot bring a full jug to the boil, so "
                     "it never saves anything at all",
             "correct": False,
             "why": "It boils a full jug perfectly well. It simply takes "
                    "longer."},
            {"text": "The advice is right, but only for the small amounts of "
                     "water that most people actually boil",
             "correct": False,
             "why": "The amount of water does not change the argument: "
                    "halving the power roughly doubles the time either way."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h02",
        "band": "harder",
        "text": "Swapping a 2000 W kettle for a 1000 W one makes the total "
                "energy slightly WORSE, not just equal. Why?",
        "options": [
            {"text": "Lower-power elements are always less efficient, so more "
                     "energy is wasted",
             "correct": False,
             "why": "The element itself is close to fully efficient either "
                    "way — almost all the energy reaches the water."},
            {"text": "The slower kettle draws more current overall, so the "
                     "wires waste more",
             "correct": False,
             "why": "It draws LESS current. Current is not what makes the "
                    "difference here."},
            {"text": "It spends longer heating, so it has longer to lose "
                     "energy to the kitchen",
             "correct": True},
            {"text": "Water takes more energy to reach boiling point when it "
                     "is heated slowly",
             "correct": False,
             "why": "The energy needed to raise the water to 100 °C is the "
                    "same however fast you do it. The extra is loss, not "
                    "requirement."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h03",
        "band": "harder",
        "text": "When does swapping to a lower-wattage appliance GENUINELY "
                "save energy?",
        "options": [
            {"text": "Whenever the new appliance has a smaller number on it, "
                     "whatever job it happens to be doing",
             "correct": False,
             "why": "This is exactly the reasoning the lesson takes apart. A "
                    "smaller rate over a longer time can be the same or "
                    "worse."},
            {"text": "Whenever the appliance is used for less than an hour a "
                     "day, so the total stays small",
             "correct": False,
             "why": "How long it runs affects the total, but it does not make "
                    "a lower rating automatically a saving."},
            {"text": "Never — power and energy are unrelated, so the rating "
                     "cannot tell you anything at all",
             "correct": False,
             "why": "They are closely related: energy is power multiplied by "
                    "time. The point is that one alone is not enough."},
            {"text": "When it does the SAME job for fewer watts, like an LED "
                     "giving the same light as a filament bulb",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h04",
        "band": "harder",
        "text": "James Watt measured a strong pit horse and called it one "
                "horsepower, about 750 W. A person sustains roughly 100 W "
                "over a working day. What does that comparison actually "
                "tell you?",
        "options": [
            {"text": "A horse can transfer energy about seven times faster "
                     "than a person can sustain",
             "correct": True},
            {"text": "A horse holds about seven times as much energy in store "
                     "as a person does",
             "correct": False,
             "why": "Neither figure is an amount held. Both are rates — how "
                    "fast energy is transferred."},
            {"text": "A horse can do about seven times as much total work as "
                     "a person ever could",
             "correct": False,
             "why": "Total work depends on how long each keeps going, which "
                    "these figures do not say."},
            {"text": "A person is about seven times more efficient with "
                     "energy than a horse is",
             "correct": False,
             "why": "Efficiency is a different quantity again, and nothing "
                    "here measures it."},
        ],
        "figure": None,
    },
]
