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
        # ⊕ MRB-297 · 1 Sep 2026 — TWO DIFFERENT ROUTERS ON ONE LESSON. The
        # P2-09 rename put a router into the lesson's own hook at 15 W left
        # on for eight hours a night; this question already had one at 9 W
        # running all day. A student met the same appliance twice with two
        # ratings and two duties, on the same page, with nothing to say
        # which was theirs. The lesson's 15 W router is load-bearing — the
        # crossover, its `data-w` and three captions all derive from it, and
        # the whole point of the P2-09 rename was an appliance that really
        # does draw its rating all night — so the QUESTION moves instead.
        # A fish-tank pump genuinely runs the full 24 hours. The arithmetic
        # is unchanged and re-checked: 9 × 86 400 = 777.6 kJ against
        # 900 × 120 = 108 kJ, a ratio of 7.2, so "about seven times" holds.
        "text": "A 9 W fish-tank pump runs all day. A 900 W microwave runs "
                "for two minutes. Which transfers more energy in that day?",
        "options": [
            {"text": "The microwave, because 900 W is a hundred times more",
             "correct": False,
             "why": "900 × 120 s = 108 kJ. The pump gets "
                    "9 × 86 400 s = 778 kJ. The rating is not the "
                    "whole calculation."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "The pump, by about seven times", "correct": True},
            {"text": "They are equal", "correct": False,
             "why": "Work both products out — the pump comes out about "
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p2-02-e05",
        "band": "easier",
        "text": "One watt is one…",
        "options": [
            {"text": "joule for every second", "correct": True},
            {"text": "second for every joule", "correct": False,
             "why": "That is the definition upside down; the unit is joules "
                    "per second, not seconds per joule."},
            {"text": "joule altogether", "correct": False,
             "why": "A joule altogether is an amount of energy. A watt is a "
                    "rate, so a time has to be in it."},
            {"text": "kilojoule for every hour", "correct": False,
             "why": "That is a rate, but the wrong one — a watt is measured "
                    "in joules and seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e06",
        "band": "easier",
        "text": "A 1500 W hairdryer is switched on. How much energy does it "
                "transfer each second?",
        "options": [
            {"text": "1500 J", "correct": True},
            {"text": "1500 W", "correct": False,
             "why": "1500 W is the rate. The energy transferred in one second "
                    "is an amount, measured in joules."},
            {"text": "1.5 J", "correct": False,
             "why": "That is 1500 divided by 1000, as though the kilo were "
                    "being removed twice."},
            {"text": "It cannot be said without knowing how long it runs",
             "correct": False,
             "why": "The time is given: the question asks about one second, "
                    "and the rating answers it directly."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e07",
        "band": "easier",
        "text": "Which of these is a rate rather than a total?",
        "options": [            {"text": "3000 joules transferred by a lamp", "correct": False,
             "why": "Joules on their own are a total amount, with no time "
                    "attached."},
            {"text": "958 kilojoules in a bag of crisps", "correct": False,
             "why": "That is an amount held in a store, not how fast anything "
                    "is transferred."},
            {"text": "2.5 kilowatt-hours on a bill", "correct": False,
             "why": "A kilowatt-hour is an amount of energy, despite having "
                    "kilowatt in the name."},
            {"text": "A 60 watt rating on a lamp", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e08",
        "band": "easier",
        "text": "What does an appliance's power rating tell you?",
        "options": [
            {"text": "How much it will cost over a year", "correct": False,
             "why": "Cost needs the time it runs for as well; the rating "
                    "alone cannot give it."},
            {"text": "How much energy it holds inside it", "correct": False,
             "why": "Appliances hold nothing. They transfer energy that "
                    "arrives along the mains."},
            {"text": "How fast it transfers energy while it is running",
             "correct": True},
            {"text": "How long it can safely be left switched on",
             "correct": False,
             "why": "Safe running time is a separate matter and is not what "
                    "the watts measure."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e09",
        "band": "easier",
        "text": "An appliance is left on standby. What power does it draw?",
        "options": [
            {"text": "None at all — standby means off", "correct": False,
             "why": "Standby is a low power, and low is not zero. It runs for "
                    "thousands of hours a year."},
            {"text": "Its full rating, because it is still plugged in",
             "correct": False,
             "why": "It draws far less than its running rating; the point is "
                    "that it is not nothing."},
            {"text": "A small but real power, for as long as it is left",
             "correct": True},
            {"text": "A power that changes with the price of electricity",
             "correct": False,
             "why": "Price affects the bill, not how many joules a second the "
                    "appliance draws."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e10",
        "band": "easier",
        "text": "Which quantity is measured in watts?",
        "options": [            {"text": "Energy", "correct": False,
             "why": "Energy is measured in joules; watts always carry a time "
                    "in them."},
            {"text": "Time", "correct": False,
             "why": "Time is measured in seconds, and it is the thing a watt "
                    "divides by."},
            {"text": "Force", "correct": False,
             "why": "Force is measured in newtons, and nothing about it is a "
                    "rate of energy transfer."},
            {"text": "Power", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e11",
        "band": "easier",
        "text": "A 3 kW immersion heater is the same as a heater rated…",
        "options": [
            {"text": "0.003 W", "correct": False,
             "why": "That divides by 1000 instead of multiplying; a kilowatt "
                    "is larger than a watt, not smaller."},
            {"text": "3000 W", "correct": True},
            {"text": "300 W", "correct": False,
             "why": "That multiplies by 100. A kilo always means a thousand."},
            {"text": "3 W", "correct": False,
             "why": "That drops the kilo entirely, leaving a heater about as "
                    "powerful as a night light."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p2-02-s05",
        "band": "standard",
        "text": "A 1200 W toaster runs for 2 minutes and a 5 W phone charger "
                "runs for 10 hours. Which transfers more energy?",
        "options": [
            {"text": "The toaster, at 144 000 J against 180 000 J",
             "correct": False,
             "why": "The two totals are right but attached the wrong way "
                    "round: 144 000 J is the toaster's."},
            {"text": "The toaster, because 1200 W is far more than 5 W",
             "correct": False,
             "why": "A rating alone settles nothing. The charger runs for "
                    "three hundred times as long."},
            {"text": "The charger, at 180 000 J against 144 000 J",
             "correct": True},
            {"text": "They are the same, because a rating and a time always "
                     "balance",
             "correct": False,
             "why": "Nothing makes them balance; the two products have to be "
                    "worked out and compared."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s06",
        "band": "standard",
        "text": "Two lamps are rated 5 W and 60 W. Which statement is "
                "certain?",
        "options": [
            {"text": "The 60 W lamp will cost more to run over the course of "
                     "a whole year",
             "correct": False,
             "why": "Only if it is on for as long. A 5 W lamp left on always "
                    "can easily cost more."},
            {"text": "The 60 W lamp is brighter", "correct": False,
             "why": "Brightness depends on the technology too — a 5 W LED can "
                    "beat a 60 W filament lamp."},
            {"text": "The 60 W lamp transfers more energy each second it is "
                     "on",
             "correct": True},
            {"text": "The 60 W lamp holds more energy inside it",
             "correct": False,
             "why": "Neither lamp holds any; the energy arrives along the "
                    "mains while it is switched on."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s07",
        "band": "standard",
        "text": "A 2 W smart speaker is left on all year, about 8760 hours. "
                "Roughly how much energy is that?",
        "options": [
            {"text": "About 17.5 kWh", "correct": True},
            {"text": "About 17 500 kWh", "correct": False,
             "why": "That is a thousand times too big — the watts have to "
                    "become kilowatts before multiplying by hours."},
            {"text": "About 2 kWh, because it is only a 2 W device",
             "correct": False,
             "why": "That is one hour's worth in the wrong unit; the hours "
                    "have to be counted in."},
            {"text": "About 4380 kWh", "correct": False,
             "why": "That is 8760 ÷ 2, dividing where the calculation "
                    "multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s08",
        "band": "standard",
        "text": "Why does a 2000 W kettle need thicker cable than a 60 W "
                "lamp?",
        "options": [
            {"text": "Because the kettle uses more energy over a year",
             "correct": False,
             "why": "It may not — a lamp on all evening can beat it. Cable "
                    "thickness answers a different question."},
            {"text": "Because the kettle holds more energy inside it",
             "correct": False,
             "why": "Neither holds any. Both transfer energy arriving along "
                    "the mains."},
            {"text": "Because far more energy passes through the cable each "
                     "second",
             "correct": True},
            {"text": "Because the kettle is used in a hotter part of the "
                     "house than the lamp",
             "correct": False,
             "why": "Where it stands has nothing to do with how much the "
                    "cable has to carry each second."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s09",
        "band": "standard",
        "text": "Which piece of information alone is enough to say which of "
                "two appliances transferred more energy?",
        "options": [
            {"text": "The two power ratings", "correct": False,
             "why": "A rating is a rate. Without a time it cannot give a "
                    "total."},
            {"text": "The two power ratings and how long each ran",
             "correct": True},
            {"text": "The prices the two appliances were bought for",
             "correct": False,
             "why": "The purchase price says nothing about joules "
                    "transferred."},
            {"text": "How long each ran for", "correct": False,
             "why": "A time on its own cannot give an energy either; the rate "
                    "is needed as well."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s10",
        "band": "standard",
        "text": "A 900 W microwave runs for 5 minutes. What is the energy "
                "transferred?",
        "options": [
            {"text": "4500 J", "correct": False,
             "why": "That is 900 × 5, with the minutes put into the formula "
                    "as they stand."},
            {"text": "270 000 J", "correct": True},
            {"text": "180 J", "correct": False,
             "why": "That is 900 ÷ 5, a division where a multiplication is "
                    "needed."},
            {"text": "54 000 J", "correct": False,
             "why": "That is 900 × 60, using one minute instead of five."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s11",
        "band": "standard",
        "text": "A television draws 100 W when watched for 4 hours a day and "
                "1 W on standby for the other 20 hours. Which draws more "
                "energy in a day?",
        "options": [
            {"text": "Standby, because 20 hours is far longer than 4",
             "correct": False,
             "why": "Longer, but at a hundredth of the power: 20 Wh against "
                    "400 Wh."},
            {"text": "Watching it, at 400 Wh against 20 Wh", "correct": True},
            {"text": "They come out equal, which is why standby matters",
             "correct": False,
             "why": "Standby matters, but not because it equals viewing — "
                    "here it is twenty times smaller."},
            {"text": "Standby, at 2000 Wh against 400 Wh", "correct": False,
             "why": "That uses 100 W for the standby hours; on standby it "
                    "draws 1 W."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p2-02-h05",
        "band": "harder",
        "text": "A 3 kW heater and a 1 kW heater are used to warm the same "
                "room to the same temperature. Which uses more energy?",
        "options": [
            {"text": "The 3 kW heater, because its rating is three times as "
                     "big as the other one",
             "correct": False,
             "why": "It transfers three times as fast, so it reaches the "
                    "temperature in about a third of the time."},
            {"text": "The 1 kW heater, because it has to run for far longer",
             "correct": False,
             "why": "Longer at a third of the rate comes to roughly the same "
                    "total, not to more."},
            {"text": "Roughly the same, because the room needs a fixed amount "
                     "of energy",
             "correct": True},
            {"text": "Neither — a heater's energy depends only on its rating",
             "correct": False,
             "why": "Energy is always the rating multiplied by the time, so "
                    "the time can never drop out."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h06",
        "band": "harder",
        "text": "A 15 W router runs 8760 hours a year; a 2000 W kettle runs "
                "about 30 hours a year. Which transfers more, and by roughly "
                "how much?",
        "options": [
            {"text": "The router, about twice the kettle's total",
             "correct": True},
            {"text": "The kettle, because 2000 W dwarfs 15 W", "correct": False,
             "why": "The rating does dwarf it, but the router runs nearly "
                    "three hundred times as long."},
            {"text": "The router, about a hundred times the kettle's total",
             "correct": False,
             "why": "The gap is far smaller: 131 kWh against 60 kWh is about "
                    "two to one."},
            {"text": "They are almost equal, which is why standby is ignored",
             "correct": False,
             "why": "They are not equal, and the router's larger figure is "
                    "precisely why standby is not ignored."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h07",
        "band": "harder",
        "text": "A 2 kW fan heater and a 2 kW oil-filled radiator each run "
                "for one hour. Which transfers more energy?",
        "options": [
            {"text": "The fan heater, because it warms the room much faster",
             "correct": False,
             "why": "It spreads the warmth faster, but both draw 2000 J every "
                    "second, so both transfer 7.2 MJ."},
            {"text": "The radiator, because it stays warm after it is "
                     "switched off",
             "correct": False,
             "why": "Staying warm afterwards releases energy it already took "
                    "in; it does not draw any extra."},
            {"text": "Exactly the same, because both draw 2 kW for the same "
                     "hour",
             "correct": True},
            {"text": "It cannot be decided without knowing the size of the "
                     "room",
             "correct": False,
             "why": "The room decides how warm it gets, not how much energy "
                    "the heaters draw from the mains."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h08",
        "band": "harder",
        "text": "Why can swapping a 2000 W kettle for a 1000 W one make the "
                "total energy slightly WORSE?",
        "options": [
            {"text": "Because the slower kettle has longer to lose energy to "
                     "the kitchen while it boils",
             "correct": True},
            {"text": "Because a 1000 W element is less efficient at turning "
                     "electricity into warmth",
             "correct": False,
             "why": "Both elements put nearly all of it into the water; the "
                    "difference is the time spent losing some."},
            {"text": "Because the water needs more energy when it is heated "
                     "slowly",
             "correct": False,
             "why": "The water needs the same energy either way; the extra is "
                    "what escapes on the way."},
            {"text": "Because a lower rating draws a larger current",
             "correct": False,
             "why": "A lower rating draws a smaller current, and that is not "
                    "what changes the total."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h09",
        "band": "harder",
        "text": "A person can sustain about 100 W of useful output. Roughly "
                "how many people would it take to run one 2000 W kettle?",
        "options": [
            {"text": "About 2, because 2000 W is about twice 1000 W",
             "correct": False,
             "why": "That compares the kettle with 1000 W, not with one "
                    "person's 100 W."},
            {"text": "About 200", "correct": False,
             "why": "That divides by 10 W rather than by 100 W, giving ten "
                    "times too many."},
            {"text": "About 20", "correct": True},
            {"text": "About 2000, one for each watt", "correct": False,
             "why": "Each person supplies 100 W, so far fewer than one per "
                    "watt are needed."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h10",
        "band": "harder",
        "text": "An appliance is described as using 5 kW an hour. What is "
                "wrong with that description?",
        "options": [
            {"text": "Nothing — that is how power is always written",
             "correct": False,
             "why": "Power is written as a plain rating; the 'an hour' turns "
                    "it into something else entirely."},
            {"text": "A kilowatt is already a rate, so 'an hour' divides by "
                     "time twice",
             "correct": True},
            {"text": "It should say 5 kW a second, because power uses "
                     "seconds",
             "correct": False,
             "why": "The rating needs no time phrase at all; the watt already "
                    "carries the seconds."},
            {"text": "5 kW is far too large a figure for any appliance",
             "correct": False,
             "why": "An electric shower can be 8.5 kW, so the size is "
                    "perfectly ordinary."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h11",
        "band": "harder",
        "text": "Two students argue about a 9 W LED and a 60 W filament lamp "
                "that light a room equally well. Which conclusion is sound?",
        "options": [
            {"text": "The LED is the better buy only if it is cheaper to "
                     "purchase",
             "correct": False,
             "why": "Purchase price is a separate question; on energy the LED "
                    "wins by a factor of about seven."},
            {"text": "The two use the same energy, because they give the same "
                     "light",
             "correct": False,
             "why": "The same light for far fewer joules a second is exactly "
                    "what makes the LED different."},
            {"text": "The 60 W lamp is brighter, because a bigger rating "
                     "always means more light",
             "correct": False,
             "why": "The question says they light the room equally; most of "
                    "the filament's 60 W ends up as warmth."},
            {"text": "The LED does the same job for about a seventh of the "
                     "energy each second",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ──────────────────────────────────
    {
        "id": "p2-02-e12",
        "band": "easier",
        "text": "Which of these household appliances carries the highest "
                "power rating?",
        "options": [
            {"text": "An electric shower", "correct": True},
            {"text": "A bedside lamp", "correct": False,
             "why": "A lamp is tens of watts at most, which is thousands of "
                    "times below a shower."},
            {"text": "A home router", "correct": False,
             "why": "A router sits at about 15 W, the lowest rating of the "
                    "four."},
            {"text": "A phone charger", "correct": False,
             "why": "A charger is only a few watts, whatever it is charging."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e13",
        "band": "easier",
        "text": "A pump is rated 0.5 kW. What is that in watts?",
        "options": [
            {"text": "0.0005 W", "correct": False,
             "why": "That divides by a thousand, and a kilowatt is the larger "
                    "of the two units."},
            {"text": "500 W", "correct": True},
            {"text": "50 W", "correct": False,
             "why": "That multiplies by a hundred. A kilo always means a "
                    "thousand."},
            {"text": "5000 W", "correct": False,
             "why": "That is ten times too many; half a thousand is five "
                    "hundred."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e14",
        "band": "easier",
        "text": "In the word kilowatt, what does “kilo” stand for?",
        "options": [
            {"text": "A hundred", "correct": False,
             "why": "A hundred has no prefix of its own in everyday use, and "
                    "kilo is not it."},
            {"text": "A million", "correct": False,
             "why": "A million is mega, which is a thousand kilowatts."},
            {"text": "A thousand", "correct": True},
            {"text": "An hour's worth", "correct": False,
             "why": "No prefix carries a time in it; that is what the “hour” "
                    "in kilowatt-hour does."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e15",
        "band": "easier",
        "text": "A sprinter is said to peak at about 1000 W. What does peak "
                "mean here?",
        "options": [
            {"text": "The total energy they can transfer in a race",
             "correct": False,
             "why": "A total would be in joules. This figure is a rate, "
                    "measured in watts."},
            {"text": "The energy stored in their muscles before they start",
             "correct": False,
             "why": "Nothing here describes a store. Watts describe how fast "
                    "energy is being transferred."},
            {"text": "The rate they can keep up for a whole race",
             "correct": False,
             "why": "A peak can be held for only a few seconds; a sustained "
                    "figure is far lower."},
            {"text": "The fastest rate they can transfer energy at",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e16",
        "band": "easier",
        "text": "One horsepower stands for about how many watts?",
        "options": [
            {"text": "About 750 W", "correct": True},
            {"text": "About 75 W", "correct": False,
             "why": "That is ten times too small, and below what a person "
                    "sustains over a day."},
            {"text": "About 7500 W", "correct": False,
             "why": "That is ten times too large, and close to an electric "
                    "shower's rating."},
            {"text": "About 100 W", "correct": False,
             "why": "That is roughly a person's sustained output, not a "
                    "horse's."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e17",
        "band": "easier",
        "text": "About how much useful power can a person keep up across a "
                "working day?",
        "options": [
            {"text": "About 10 W", "correct": False,
             "why": "That is roughly a low-energy lamp, and far below what a "
                    "working body manages."},
            {"text": "About 100 W", "correct": True},
            {"text": "About 1000 W", "correct": False,
             "why": "That is a sprinter's peak, and it lasts a few seconds "
                    "rather than a day."},
            {"text": "About 2000 W", "correct": False,
             "why": "That is a kettle, which outruns a person by a factor of "
                    "about twenty."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e18",
        "band": "easier",
        "text": "Which of these figures would be quoted in kilowatts?",
        "options": [
            {"text": "The energy an oven used overnight", "correct": False,
             "why": "An amount of energy is quoted in kilowatt-hours or "
                    "joules, both of which carry a time."},
            {"text": "The time a lamp was left switched on", "correct": False,
             "why": "A time is quoted in hours, minutes or seconds."},
            {"text": "The rating of an electric shower", "correct": True},
            {"text": "The price charged for a unit of electricity",
             "correct": False,
             "why": "A price is quoted in pence, and it is charged against "
                    "energy rather than against a rate."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e19",
        "band": "easier",
        "text": "A washing machine is rated 2.1 kW. How many watts is that?",
        "options": [
            {"text": "21 W", "correct": False,
             "why": "That multiplies by ten. A kilowatt is a thousand watts, "
                    "not ten."},
            {"text": "210 W", "correct": False,
             "why": "That multiplies by a hundred, leaving the figure ten "
                    "times too small."},
            {"text": "0.0021 W", "correct": False,
             "why": "That divides by a thousand, which turns a large rating "
                    "into an impossibly tiny one."},
            {"text": "2100 W", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e20",
        "band": "easier",
        "text": "James Watt measured what a strong pit horse could lift and "
                "called it one horsepower. Why?",
        "options": [
            {"text": "So that buyers who knew horses could compare his "
                     "engines", "correct": True},
            {"text": "Because a horse was the only thing to test against",
             "correct": False,
             "why": "He could have used any number he liked. He chose the one "
                    "his customers already understood."},
            {"text": "Because the watt had not been invented and he needed "
                     "some unit of energy",
             "correct": False,
             "why": "Horsepower is a rate rather than an amount, and a unit "
                    "of energy would not have done the job."},
            {"text": "Because a horse and an engine transfer energy by "
                     "exactly the same process",
             "correct": False,
             "why": "A horse and a steam engine work in entirely different "
                    "ways; what is shared is the rate."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e21",
        "band": "easier",
        "text": "An LED lamp and a filament lamp light a room equally well. "
                "Which carries the lower rating?",
        "options": [
            {"text": "The filament lamp", "correct": False,
             "why": "Most of a filament's rating leaves as warmth, so it needs "
                    "far more watts for the same light."},
            {"text": "The LED lamp", "correct": True},
            {"text": "Both carry the same rating", "correct": False,
             "why": "Equal light does not mean equal rating; that is the whole "
                    "reason LEDs replaced filaments."},
            {"text": "It depends on the colour of the light", "correct": False,
             "why": "Colour does not set the rating, and the question has "
                    "already fixed the light as equal."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e22",
        "band": "easier",
        "text": "Two appliances run for exactly the same length of time. Which "
                "transfers more energy?",
        "options": [
            {"text": "The one that costs more to buy", "correct": False,
             "why": "Purchase price has nothing to do with how fast energy is "
                    "transferred."},
            {"text": "The heavier of the two appliances", "correct": False,
             "why": "Mass does not appear anywhere in the calculation."},
            {"text": "The one with the higher rating", "correct": True},
            {"text": "Neither — equal times always mean equal energy",
             "correct": False,
             "why": "Equal times settle half of it. The rate settles the "
                    "rest."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e23",
        "band": "easier",
        "text": "A cable has to be thick enough to survive what?",
        "options": [
            {"text": "The energy that passes through it each second",
             "correct": True},
            {"text": "The total energy that will pass through it over its "
                     "life",
             "correct": False,
             "why": "A lifetime total does not heat a cable. What heats it is "
                    "what flows while the appliance runs."},
            {"text": "The price of the electricity the appliance uses",
             "correct": False,
             "why": "Price is on a bill, and a cable is untouched by it."},
            {"text": "The number of times the appliance is switched on",
             "correct": False,
             "why": "Switching is a separate matter; the thickness answers the "
                    "rate."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e24",
        "band": "easier",
        "text": "Which of these would be a sensible power rating for a "
                "kettle?",
        "options": [
            {"text": "2 W", "correct": False,
             "why": "Two joules a second would take most of a day to warm a "
                    "mugful."},
            {"text": "20 W", "correct": False,
             "why": "That is about a low-energy lamp, and nowhere near enough "
                    "to boil water."},
            {"text": "200 000 W", "correct": False,
             "why": "That is larger than a whole street draws, and no domestic "
                    "cable could carry it."},
            {"text": "2000 W", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e25",
        "band": "easier",
        "text": "A set-top box draws 8 W while it sits on standby. How many "
                "joules is that in each second?",
        "options": [
            {"text": "8 J", "correct": True},
            {"text": "480 J", "correct": False,
             "why": "That is a minute's worth, found by multiplying by sixty."},
            {"text": "0 J", "correct": False,
             "why": "Standby is a low power, and low is not nothing at all."},
            {"text": "8000 J", "correct": False,
             "why": "That treats the watts as kilowatts, which is a thousand "
                    "times too many."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e26",
        "band": "easier",
        "text": "Put a 9 W LED, a 60 W lamp and a 2 kW heater in order, "
                "starting with the lowest rating.",
        "options": [
            {"text": "Heater, lamp, LED", "correct": False,
             "why": "That is the order reversed: the heater is the highest of "
                    "the three, not the lowest."},
            {"text": "LED, heater, lamp", "correct": False,
             "why": "The heater is 2000 W, which is far above the 60 W lamp."},
            {"text": "LED, lamp, heater", "correct": True},
            {"text": "Lamp, LED, heater", "correct": False,
             "why": "9 W is below 60 W, so the LED comes first."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e27",
        "band": "easier",
        "text": "Power is the rate of what?",
        "options": [
            {"text": "Energy transfer", "correct": True},
            {"text": "Temperature rise", "correct": False,
             "why": "A temperature rise is one effect of a transfer, not the "
                    "quantity being counted."},
            {"text": "Fuel burning", "correct": False,
             "why": "Fuel burning is one way energy is transferred; power "
                    "covers every way."},
            {"text": "Money spent", "correct": False,
             "why": "Money follows the energy used, and a rate of spending is "
                    "not measured in watts."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e28",
        "band": "easier",
        "text": "A shower is rated 8.5 kW. What does that tell you about how "
                "long anyone stands in it?",
        "options": [
            {"text": "That nobody stands in it for long",
             "correct": False,
             "why": "A high rating does not shorten a shower. People choose "
                    "how long they stand in one."},
            {"text": "Nothing at all", "correct": True},
            {"text": "About an hour",
             "correct": False,
             "why": "Nothing in a rating sets a running time, and no shower "
                    "has such a limit."},
            {"text": "That it uses 8.5 units an hour",
             "correct": False,
             "why": "That is true of the energy, and it is not what the "
                    "question asks, which is about the time."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e29",
        "band": "easier",
        "text": "Which of these appliances would need the thickest cable?",
        "options": [
            {"text": "A 15 W router", "correct": False,
             "why": "Fifteen joules a second is a trickle, and the thinnest "
                    "flex will carry it."},
            {"text": "A 60 W lamp", "correct": False,
             "why": "A lamp draws too little to trouble ordinary flex."},
            {"text": "An 8.5 kW shower", "correct": True},
            {"text": "A 9 W LED", "correct": False,
             "why": "Nine joules a second is the smallest figure here by a "
                    "long way."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-e30",
        "band": "easier",
        "text": "A router rated 15 W has been on since the evening. What is "
                "its power at three in the morning?",
        "options": [
            {"text": "15 W", "correct": True},
            {"text": "More than 15 W",
             "correct": False,
             "why": "The hours build up the energy, not the rate. A rating "
                    "does not climb."},
            {"text": "Less than 15 W",
             "correct": False,
             "why": "It draws the same each second all night; nothing settles "
                    "the rate downwards."},
            {"text": "None",
             "correct": False,
             "why": "An appliance holds no energy to finish. It keeps drawing "
                    "while it is on."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ────────────────────────────────
    {
        "id": "p2-02-s12",
        "band": "standard",
        "text": "A 2 kW heater and a 500 W heater are both run for exactly one "
                "hour. How do the two totals compare?",
        "options": [
            {"text": "They are equal, because both ran for the same hour",
             "correct": False,
             "why": "Equal times settle half the calculation; the rates are "
                    "what separate the totals."},
            {"text": "The 2 kW heater transfers four times as much",
             "correct": True},
            {"text": "The 2 kW heater transfers about 1500 J more",
             "correct": False,
             "why": "The gap is a factor rather than a small difference, and "
                    "an hour of it runs into millions of joules."},
            {"text": "The 500 W heater transfers more, because it runs more "
                     "steadily",
             "correct": False,
             "why": "Nothing about a lower rating makes it steadier, and a "
                    "quarter of the rate cannot beat the whole."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s13",
        "band": "standard",
        "text": "A shower is rated 8500 W and a lamp 60 W. Roughly how many "
                "times faster does the shower transfer energy?",
        "options": [
            {"text": "About 14 times", "correct": False,
             "why": "That divides by 600 rather than by 60, losing a factor "
                    "of ten."},
            {"text": "About 1400 times", "correct": False,
             "why": "That is ten times too many; 8500 ÷ 60 is nearer a "
                    "hundred and fifty."},
            {"text": "About 140 times", "correct": True},
            {"text": "About 8440 times", "correct": False,
             "why": "That subtracts the two ratings, and a comparison of this "
                    "sort is a division."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s14",
        "band": "standard",
        "text": "A hairdryer is rated 1500 W and a desk fan 40 W. Which "
                "statement is certain?",
        "options": [
            {"text": "The hairdryer will cost more over a year",
             "correct": False,
             "why": "Only if it runs for a comparable time, and a fan left on "
                    "all summer can easily win."},
            {"text": "The hairdryer transfers energy far faster while both "
                     "are running", "correct": True},
            {"text": "The hairdryer holds far more energy inside it",
             "correct": False,
             "why": "Neither holds any; both transfer energy arriving along "
                    "the mains."},
            {"text": "The fan is the more efficient of the two appliances",
             "correct": False,
             "why": "A rating says nothing about efficiency — only about how "
                    "fast energy is drawn."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s15",
        "band": "standard",
        "text": "Which decision can an appliance's rating settle on its own, "
                "with no other information?",
        "options": [
            {"text": "How much the appliance will add to a monthly bill",
             "correct": False,
             "why": "A bill needs the hours as well, and a rating carries "
                    "none."},
            {"text": "Whether the appliance is worth buying", "correct": False,
             "why": "That depends on what it does and how long it runs, "
                    "neither of which is in the rating."},
            {"text": "How thick the cable supplying it has to be",
             "correct": True},
            {"text": "How long the appliance will last before it fails",
             "correct": False,
             "why": "Lifetime is a matter of how it is built, and no rating "
                    "predicts it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s16",
        "band": "standard",
        "text": "A sprinter peaks near 1000 W but sustains about 100 W across "
                "a day. What does that gap show?",
        "options": [
            {"text": "That the peak figure was measured wrongly",
             "correct": False,
             "why": "Both figures are real; they describe two different "
                    "lengths of effort."},
            {"text": "That a high rate can be held only briefly",
             "correct": True},
            {"text": "That the body stores ten times more energy during a "
                     "sprint",
             "correct": False,
             "why": "Neither figure is an amount stored. Both are rates of "
                    "transfer."},
            {"text": "That sprinting is about ten times more efficient than "
                     "walking",
             "correct": False,
             "why": "Efficiency is a different quantity, and nothing here "
                    "measures it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s17",
        "band": "standard",
        "text": "One horsepower is about 750 W. What would a team of four "
                "horses stand for?",
        "options": [
            {"text": "About 188 W", "correct": False,
             "why": "That divides by four, which would make four horses weaker "
                    "than one."},
            {"text": "About 754 W", "correct": False,
             "why": "That adds four to the figure rather than multiplying by "
                    "it."},
            {"text": "About 750 W", "correct": False,
             "why": "That is one horse. Four of them transfer energy four "
                    "times as fast."},
            {"text": "About 3000 W", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s18",
        "band": "standard",
        "text": "Standby costs far more over a year than most people expect. "
                "What explains that?",
        "options": [
            {"text": "A standby circuit draws nearly as much as the appliance "
                     "running does",
             "correct": False,
             "why": "It draws a small fraction of the running figure. The "
                    "hours are what make it count."},
            {"text": "Electricity costs more when a device is idle",
             "correct": False,
             "why": "The price per unit is the same whatever the appliance is "
                    "doing."},
            {"text": "A small rate runs for thousands of hours a year",
             "correct": True},
            {"text": "Appliances draw a surge of power each time they are "
                     "woken from standby",
             "correct": False,
             "why": "Any waking surge lasts a moment; the yearly total comes "
                    "from the long idle hours."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s19",
        "band": "standard",
        "text": "A 2000 W kettle runs 3 minutes and a 1000 W toaster runs 6. "
                "What can be said without working anything out?",
        "options": [
            {"text": "The two totals are about the same, because one is twice "
                     "the rate and the other twice the time", "correct": True},
            {"text": "The kettle wins, because it carries twice the rating of "
                     "the toaster",
             "correct": False,
             "why": "Twice the rate for half the time comes to the same "
                    "total, not to a win."},
            {"text": "The toaster wins, because it runs for twice as long as "
                     "the kettle does",
             "correct": False,
             "why": "Twice the time at half the rate also comes to the same "
                    "total."},
            {"text": "Nothing can be said until both products have actually "
                     "been worked out",
             "correct": False,
             "why": "When one figure doubles and the other halves, the product "
                    "is unchanged, and that can be seen at once."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s20",
        "band": "standard",
        "text": "Which sentence uses the word power the way a scientist would?",
        "options": [
            {"text": "This battery holds a lot of power", "correct": False,
             "why": "A battery holds energy. Power would describe how fast it "
                    "gave that energy up."},
            {"text": "The shower is rated 8.5 kW", "correct": True},
            {"text": "We used a lot of power last month", "correct": False,
             "why": "What a bill counts is energy over a month, which is a "
                    "total rather than a rate."},
            {"text": "The oven used 1.8 kWh of power overnight",
             "correct": False,
             "why": "A kilowatt-hour is an amount of energy, so this sentence "
                    "names the wrong quantity."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s21",
        "band": "standard",
        "text": "How can two lamps with very different ratings give out the "
                "same amount of light?",
        "options": [
            {"text": "Because a rating counts the energy going in, not the "
                     "light coming out", "correct": True},
            {"text": "Because light is not a form of energy, so the rating "
                     "cannot describe it",
             "correct": False,
             "why": "Light certainly carries energy. The rating simply "
                    "measures what arrives rather than what leaves."},
            {"text": "Because the brighter lamp must have been running for "
                     "longer beforehand",
             "correct": False,
             "why": "Brightness does not build up over time; a lamp is as "
                    "bright in its first second as its last."},
            {"text": "Because a lamp's rating changes once it has warmed up "
                     "properly",
             "correct": False,
             "why": "The rating is fixed. What differs between the two lamps "
                    "is how much of it becomes light."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s22",
        "band": "standard",
        "text": "A 9 W LED replaces a 60 W filament lamp. By roughly what "
                "factor does the rate of transfer fall?",
        "options": [
            {"text": "About 51 times", "correct": False,
             "why": "That subtracts the two ratings, and a factor comes from "
                    "dividing them."},
            {"text": "About 7 times", "correct": True},
            {"text": "About 70 times", "correct": False,
             "why": "That is ten times too many; 60 ÷ 9 is under seven."},
            {"text": "It does not fall — both draw the same, since the light "
                     "is the same",
             "correct": False,
             "why": "The light is the same and the rate is not, which is "
                    "exactly what makes the LED worth fitting."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s23",
        "band": "standard",
        "text": "Why can a rating never tell you how long an appliance has "
                "been running?",
        "options": [
            {"text": "Because ratings are printed before the appliance is ever "
                     "used",
             "correct": False,
             "why": "When it was printed is beside the point; a meter reading "
                    "is printed before use too and still records hours."},
            {"text": "Because a rating describes each second rather than the "
                     "number of seconds", "correct": True},
            {"text": "Because a rating is a rough estimate rather than an "
                     "exact figure",
             "correct": False,
             "why": "Ratings are accurate. The problem is what they describe, "
                    "not how precisely."},
            {"text": "Because the rating falls slowly as an appliance gets "
                     "older",
             "correct": False,
             "why": "A rating does not drift with age, and even if it did it "
                    "would not record a running time."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s24",
        "band": "standard",
        "text": "A plate on an appliance reads “230 V · 10 A · 2300 W”. "
                "Which figure is the power?",
        "options": [
            {"text": "230 V", "correct": False,
             "why": "Volts measure the supply, and the voltage is already "
                    "accounted for inside the watts."},
            {"text": "10 A", "correct": False,
             "why": "Amps measure the current drawn, which is a different "
                    "quantity again."},
            {"text": "2300 W", "correct": True},
            {"text": "All three together give the power", "correct": False,
             "why": "Only one of them is measured in watts, and that one is "
                    "the power on its own."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s25",
        "band": "standard",
        "text": "One heater is marked 1 kW and another 1000 W. How do they "
                "compare?",
        "options": [
            {"text": "The 1000 W one is a thousand times the other",
             "correct": False,
             "why": "That treats the kilowatt as a watt, which loses the "
                    "thousand the prefix supplies."},
            {"text": "The 1 kW one is a thousand times the other",
             "correct": False,
             "why": "It is the same figure written two ways, so neither is "
                    "larger."},
            {"text": "The 1000 W one is slightly higher, because it is the "
                     "bigger number",
             "correct": False,
             "why": "The number is bigger because the unit is smaller. They "
                    "describe the same rate."},
            {"text": "They are the same rating, written two ways",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s26",
        "band": "standard",
        "text": "A 1000 W microwave and a 2000 W kettle are switched on "
                "together. Which draws more each second, and by how much?",
        "options": [
            {"text": "The kettle, by 1000 J every second", "correct": True},
            {"text": "The kettle, by 1000 J altogether", "correct": False,
             "why": "The gap is a rate, so it repeats every second rather "
                    "than happening once."},
            {"text": "The microwave, because it heats food from the inside",
             "correct": False,
             "why": "How an appliance works does not change its rating, and "
                    "the kettle's is the higher one."},
            {"text": "Neither — running together means they share the same "
                     "supply equally",
             "correct": False,
             "why": "Each draws its own rating from the supply; they do not "
                    "divide one between them."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s27",
        "band": "standard",
        "text": "A student says a 2 kW fan heater “holds 2 kW of energy”. "
                "What is the correction?",
        "options": [
            {"text": "It holds 2000 J, which it releases as soon as it is "
                     "switched on",
             "correct": False,
             "why": "It holds nothing at all; the energy arrives along the "
                    "mains while it runs."},
            {"text": "It transfers 2000 J every second, and holds nothing",
             "correct": True},
            {"text": "It holds 2 kW until it is unplugged, and then loses it",
             "correct": False,
             "why": "A kilowatt is a rate and cannot be held by anything, "
                    "plugged in or not."},
            {"text": "It holds 2 kWh, which is what the rating is short for",
             "correct": False,
             "why": "A kilowatt-hour is an amount of energy, and a rating is "
                    "not an abbreviation of one."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s28",
        "band": "standard",
        "text": "A small wind turbine is rated 6 kW. What does that tell you "
                "about the energy it produces in a year?",
        "options": [
            {"text": "That it produces 6 kWh in every year it is standing",
             "correct": False,
             "why": "That is a rate read as a yearly total, which loses the "
                    "hours entirely."},
            {"text": "That it produces more energy than a 3 kW turbine does, "
                     "whatever the weather",
             "correct": False,
             "why": "A larger turbine becalmed all year beats nothing; the "
                    "hours it turns decide the total."},
            {"text": "Nothing on its own — the hours it turns are needed too",
             "correct": True},
            {"text": "That it produces 6 kJ every second it is standing "
                     "outside",
             "correct": False,
             "why": "It transfers that only while it is turning, and a still "
                    "day gives nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s29",
        "band": "standard",
        "text": "One room is warmed by a single 2 kW heater and an identical "
                "room by two 1 kW heaters. Compare the rate of transfer.",
        "options": [
            {"text": "The single heater transfers twice as fast, because its "
                     "rating is the larger one",
             "correct": False,
             "why": "Two 1 kW heaters add to 2 kW, so there is nothing to "
                    "choose between the rooms."},
            {"text": "The pair transfers twice as fast, because there are two "
                     "of them working",
             "correct": False,
             "why": "Two halves make one whole; they match the single heater "
                    "rather than doubling it."},
            {"text": "The pair transfers energy more slowly",
             "correct": False,
             "why": "Each is half, and there are two, so together they equal "
                    "the single heater."},
            {"text": "The two rooms are warmed at the same rate",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-s30",
        "band": "standard",
        "text": "Why is a rating useful for choosing a cable but useless for "
                "predicting a bill?",
        "options": [
            {"text": "A cable is heated by what flows each second; a bill "
                     "counts the hours too", "correct": True},
            {"text": "A cable is sold by its rating, while electricity is sold "
                     "by the appliance",
             "correct": False,
             "why": "Electricity is sold by the unit of energy, not by the "
                    "appliance drawing it."},
            {"text": "A bill is worked out from the voltage, which a rating "
                     "does not include",
             "correct": False,
             "why": "The voltage is already inside the rating, and a bill is "
                    "worked out from energy."},
            {"text": "A cable can carry any rate, so the figure matters to "
                     "the bill alone",
             "correct": False,
             "why": "A cable very much has a limit, which is why the rating "
                    "is the figure that chooses one."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ──────────────────────────────────
    {
        "id": "p2-02-h12",
        "band": "harder",
        "text": "One horsepower is about 750 W. Roughly how many pit horses "
                "would match a 3 kW immersion heater?",
        "options": [
            {"text": "About 40", "correct": False,
             "why": "That uses 75 W for a horse instead of 750 W, giving ten "
                    "times too many."},
            {"text": "About 2250",
             "correct": False,
             "why": "That multiplies the two instead of dividing, which would "
                    "make a heater weaker than one horse."},
            {"text": "About 4", "correct": True},
            {"text": "About 30",
             "correct": False,
             "why": "A horse is about seven times a person, so far fewer "
                    "horses are needed than people."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h13",
        "band": "harder",
        "text": "Watt's horsepower was a generous figure, which made his "
                "engines sound modest. Why would a seller do that?",
        "options": [
            {"text": "So that an engine he sold as the match of six horses "
                     "would quietly outwork them",
             "correct": True},
            {"text": "Because a smaller figure let him charge a higher price "
                     "for the same engine",
             "correct": False,
             "why": "A modest claim does not raise a price; it makes the "
                    "engine look like better value once it is running."},
            {"text": "Because the unit had to be generous to be accepted as a "
                     "scientific one",
             "correct": False,
             "why": "Scientific units are not chosen for generosity, and "
                    "horsepower was never one."},
            {"text": "Because a strong horse could not be measured any more "
                     "precisely at the time",
             "correct": False,
             "why": "He chose a strong horse deliberately. The imprecision is "
                    "not what made the figure generous."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h14",
        "band": "harder",
        "text": "A 1.5 kW oil-filled radiator replaces a 3 kW fan heater in "
                "the same room. Predict what changes.",
        "options": [
            {"text": "The room reaches the same warmth in half the time, for "
                     "half the energy",
             "correct": False,
             "why": "Halving the rate makes the job take longer, not "
                    "shorter."},
            {"text": "The room takes about twice as long and needs a similar "
                     "total", "correct": True},
            {"text": "The room never reaches quite the same warmth as it "
                      "did before",
             "correct": False,
             "why": "A lower rating means slower, not incapable; the room "
                    "warms in the end."},
            {"text": "The room warms at the same rate, because the total "
                     "energy is the same",
             "correct": False,
             "why": "The totals end up similar, and the rate is halved, which "
                    "is why the time doubles."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h15",
        "band": "harder",
        "text": "Why is it wrong to say that a 2000 W kettle “uses 2000 W”?",
        "options": [
            {"text": "Because the figure applies only while the water is "
                     "actually boiling",
             "correct": False,
             "why": "It applies for the whole time the element is on, which is "
                    "the whole boil."},
            {"text": "Because a kettle draws less than its rating",
             "correct": False,
             "why": "Small differences are not the issue; the wording names "
                    "the wrong sort of quantity."},
            {"text": "Because “uses” names a total, and 2000 W is a rate",
             "correct": True},
            {"text": "Because a kettle is rated in kilowatts and cannot be "
                     "described in watts",
             "correct": False,
             "why": "2000 W and 2 kW are the same rating, so either unit is "
                    "correct."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h16",
        "band": "harder",
        "text": "A fuse trips when a kettle, an oven and a shower are all "
                "switched on together. Which quantity explains that?",
        "options": [
            {"text": "The total energy the three will transfer before they "
                     "finish",
             "correct": False,
             "why": "A fuse cannot know a future total. It responds to what is "
                    "passing through it now."},
            {"text": "The total power being drawn at that moment",
             "correct": True},
            {"text": "The number of appliances plugged in",
             "correct": False,
             "why": "Twenty LED lamps trip nothing. It is the ratings that "
                    "add up, not the count."},
            {"text": "The cost of the electricity the three appliances are "
                     "using",
             "correct": False,
             "why": "Cost is worked out after the event and has no effect on "
                    "a fuse."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h17",
        "band": "harder",
        "text": "Dryer A is rated 2.5 kW and takes an hour; dryer B is 1.5 kW "
                "and takes two hours. Which transfers more?",
        "options": [
            {"text": "A, by 1.0 kWh",
             "correct": False,
             "why": "A gives 2.5 kWh. B runs at a lower rate for twice as "
                    "long and reaches 3.0 kWh."},
            {"text": "B, by 0.5 kWh", "correct": True},
            {"text": "They are equal",
             "correct": False,
             "why": "They would trade off exactly if the rating had halved; "
                    "1.5 is more than half of 2.5."},
            {"text": "B, by 1.0 kWh",
             "correct": False,
             "why": "The extra hour is worth 1.5 kWh, but A's higher rate over "
                    "its own hour claws most of it back."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h18",
        "band": "harder",
        "text": "Why does a power rating say nothing about how efficient an "
                "appliance is?",
        "options": [
            {"text": "Because efficiency is measured in watts as well, so the "
                     "two cancel out",
             "correct": False,
             "why": "Efficiency is a comparison between two energies and "
                    "carries no unit at all."},
            {"text": "Because ratings are measured when an appliance is new "
                     "and efficiency falls later",
             "correct": False,
             "why": "Even a brand-new appliance's rating says nothing about "
                    "what comes out of it."},
            {"text": "Because efficiency depends on the price of electricity "
                     "and a rating does not",
             "correct": False,
             "why": "Price has no part in efficiency; both are about energy."},
            {"text": "Because a rating counts what goes in, and efficiency "
                     "compares that with what comes out usefully",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h19",
        "band": "harder",
        "text": "An electric shower carries the highest rating in a house. Why "
                "is that not a reason to avoid using one?",
        "options": [
            {"text": "Because a shower's rating is measured differently "
                      "from other appliances",
             "correct": False,
             "why": "Every rating means the same thing: joules each second "
                    "while running."},
            {"text": "Because the mains supplies a shower separately, so it "
                     "does not reach the bill",
             "correct": False,
             "why": "A separate circuit is a safety measure. Every unit it "
                    "draws is still metered."},
            {"text": "Because it runs for only a few minutes, and the total "
                     "is what costs", "correct": True},
            {"text": "Because heating water is cheaper per joule than any "
                     "other use of electricity",
             "correct": False,
             "why": "Every joule costs the same whatever it does. The "
                    "difference here is the running time."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h20",
        "band": "harder",
        "text": "An extension lead is marked “max 3 kW”. What does plugging in "
                "a 2 kW heater and a 2.2 kW kettle together risk?",
        "options": [
            {"text": "Nothing, because neither appliance on its own is above "
                     "3 kW",
             "correct": False,
             "why": "The lead carries both at once, so what matters is the "
                    "4.2 kW passing through it together."},
            {"text": "Nothing, because a lead's marking describes a whole "
                     "day's use rather than a moment",
             "correct": False,
             "why": "A marking in kilowatts is a rate, so it describes the "
                    "moment and not the day."},
            {"text": "4.2 kW passes through a lead built for 3 kW, and it "
                     "overheats", "correct": True},
            {"text": "The two appliances share the 3 kW between them and both "
                     "run slowly",
             "correct": False,
             "why": "Appliances do not share a limit politely; each draws its "
                    "own rating and the lead carries the sum."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h21",
        "band": "harder",
        "text": "A student says a router must be more powerful than a kettle, "
                "because it uses more energy in a day. Correct them.",
        "options": [
            {"text": "The router transfers more in a day at a far lower rate, "
                     "because it runs far longer", "correct": True},
            {"text": "The router is indeed the more powerful, since power is "
                     "what a day's energy measures",
             "correct": False,
             "why": "A day's energy is a total. Power is the rate, and the "
                    "kettle's is over a hundred times higher."},
            {"text": "The kettle uses more in a day as well, so the student "
                     "has the arithmetic wrong",
             "correct": False,
             "why": "The router really does win on the day's energy; it is the "
                    "conclusion about power that fails."},
            {"text": "Neither is more powerful, because power cannot be "
                     "compared between different appliances",
             "correct": False,
             "why": "Ratings compare perfectly well: 2000 W against 15 W is a "
                    "plain comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h22",
        "band": "harder",
        "text": "A 100 W lamp and a 100 W speaker each run for an hour. What "
                "is the same, and what is not?",
        "options": [
            {"text": "Both the energy and what it becomes are the same, "
                     "because the ratings match",
             "correct": False,
             "why": "The energy matches; what it becomes is light in one case "
                    "and sound and warmth in the other."},
            {"text": "The energy transferred is the same; what it becomes is "
                     "not", "correct": True},
            {"text": "The speaker transfers less, because sound carries less "
                     "energy than light",
             "correct": False,
             "why": "Both draw 100 J each second from the mains, whatever "
                    "leaves them afterwards."},
            {"text": "The lamp transfers more, because light travels further "
                     "than sound",
             "correct": False,
             "why": "How far something travels is not how much energy went "
                    "into it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h23",
        "band": "harder",
        "text": "A petrol mower is rated 3 kW and an electric one 1.8 kW. What "
                "else is needed to say which uses more energy per lawn?",
        "options": [
            {"text": "The price of petrol against the price of a unit of "
                     "electricity",
             "correct": False,
             "why": "That would settle the cost. The question asks about "
                    "energy."},
            {"text": "The mass of each mower when it is full", "correct": False,
             "why": "Mass appears nowhere in a calculation of energy "
                    "transferred."},
            {"text": "How long each one takes to cut the lawn", "correct": True},
            {"text": "The width of the blade each mower turns", "correct": False,
             "why": "The blade changes how long the job takes, so it is the "
                    "time that is actually wanted."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h24",
        "band": "harder",
        "text": "Why is the watt defined as a joule per second rather than a "
                "joule per hour?",
        "options": [
            {"text": "Because an hour is too long for any appliance to run "
                     "steadily",
             "correct": False,
             "why": "Plenty of appliances run for hours; length of time is not "
                    "the reason."},
            {"text": "Because a joule is too small to be counted over a whole "
                     "hour",
             "correct": False,
             "why": "Joules are counted in millions on a bill, so counting "
                    "them over an hour is no trouble."},
            {"text": "Because energy is only transferred in whole seconds",
             "correct": False,
             "why": "Transfer is continuous; nothing about it comes in second-"
                    "sized parcels."},
            {"text": "Because the second is the standard unit of time in "
                     "science", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h25",
        "band": "harder",
        "text": "A person sustains about 100 W. How long would they need to "
                "work to match a 2000 W kettle running for 3 minutes?",
        "options": [
            {"text": "About 3 minutes",
             "correct": False,
             "why": "At a twentieth of the rate, the same job takes twenty "
                    "times as long."},
            {"text": "About 20 minutes",
             "correct": False,
             "why": "Twenty times the rate over three minutes needs sixty "
                    "minutes, not twenty."},
            {"text": "About an hour", "correct": True},
            {"text": "About a day",
             "correct": False,
             "why": "A person certainly can match it, given the time: three "
                    "minutes of kettle is an hour of work."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h26",
        "band": "harder",
        "text": "A box says “60 W equivalent · 9 W actual”. What do the two "
                "figures mean?",
        "options": [
            {"text": "The lamp draws 60 W at first and settles to 9 W once it "
                     "is warm",
             "correct": False,
             "why": "It draws 9 W from the moment it is switched on; nothing "
                    "settles."},
            {"text": "It gives the light a 60 W filament gave, while drawing "
                     "9 W", "correct": True},
            {"text": "It draws 60 W, and just 9 W of that is paid for on the "
                     "bill",
             "correct": False,
             "why": "Every joule drawn is metered. There is no untaxed part of "
                    "a rating."},
            {"text": "It can be run at either rating, depending on the switch "
                     "used",
             "correct": False,
             "why": "There is one rating here. The other figure describes the "
                    "lamp it replaces."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h27",
        "band": "harder",
        "text": "A generator is rated 5 kW. Can it run a 2 kW oven, a 2.2 kW "
                "kettle and eight 9 W lamps at the same time?",
        "options": [
            {"text": "No — three appliances at once always need more than a "
                     "generator's rating",
             "correct": False,
             "why": "The number of appliances decides nothing; the ratings "
                    "have to be added and compared."},
            {"text": "No — the lamps alone add more than 5 kW",
             "correct": False,
             "why": "Eight 9 W lamps are 72 W, which is 0.072 kW — a thousand "
                    "times smaller than that."},
            {"text": "Yes — the three together draw about 4.3 kW",
             "correct": True},
            {"text": "Yes — a generator can supply any load, just more slowly "
                     "when it is busy",
             "correct": False,
             "why": "A generator has a real ceiling, and going over it cuts "
                    "out rather than slowing down."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h28",
        "band": "harder",
        "text": "Two identical fan heaters are run for 20 minutes and for 40 "
                "minutes. Compare their ratings and their energy.",
        "options": [
            {"text": "The same rating, and the same energy, since the "
                     "appliances are identical",
             "correct": False,
             "why": "Identical appliances share a rating, and the one running "
                    "twice as long transfers twice as much."},
            {"text": "Twice the rating for the second, and twice the energy",
             "correct": False,
             "why": "The rating is a property of the heater and does not "
                    "change with how long it is left on."},
            {"text": "The same rating, and twice the energy for the second",
             "correct": True},
            {"text": "Half the rating for the second, so the energy comes out "
                     "the same",
             "correct": False,
             "why": "Nothing halves the rating. Both draw the same each "
                    "second."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h29",
        "band": "harder",
        "text": "An advert claims a 500 W appliance is “four times cheaper to "
                "run” than a 2000 W one. What would have to be true?",
        "options": [
            {"text": "That the 500 W one is four times as efficient",
             "correct": False,
             "why": "Efficiency is not what the claim rests on; a rating "
                    "counts what goes in."},
            {"text": "That both are run for exactly the same length of time",
             "correct": True},
            {"text": "That electricity is charged at four different prices "
                     "through the day",
             "correct": False,
             "why": "One price applies to both appliances, so pricing cannot "
                    "produce the factor."},
            {"text": "That the 2000 W one is run for a quarter as long as the "
                     "500 W one",
             "correct": False,
             "why": "That would make their totals equal, so neither would be "
                    "cheaper at all."},
        ],
        "figure": None,
    },
    {
        "id": "p2-02-h30",
        "band": "harder",
        "text": "Which question can a power rating never answer on its own?",
        "options": [
            {"text": "How much energy the appliance will transfer altogether",
             "correct": True},
            {"text": "How many joules the appliance draws in a single "
                      "second",
             "correct": False,
             "why": "That is exactly what a rating states, because a watt is a "
                    "joule each second."},
            {"text": "Whether the appliance needs a thicker cable than another "
                     "one does",
             "correct": False,
             "why": "Cable thickness answers the rate, which is the one thing "
                    "a rating gives."},
            {"text": "Which of two appliances transfers energy faster while "
                     "both are running",
             "correct": False,
             "why": "Comparing two ratings settles that without any further "
                    "information."},
        ],
        "figure": None,
    },
]
