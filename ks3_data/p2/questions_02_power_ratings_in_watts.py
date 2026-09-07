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
        "options": [
            {"text": "3000 joules transferred by a lamp", "correct": False,
             "why": "Joules on their own are a total amount, with no time "
                    "attached."},
            {"text": "A 60 watt rating on a lamp", "correct": True},
            {"text": "2.5 kilowatt-hours on a bill", "correct": False,
             "why": "A kilowatt-hour is an amount of energy, despite having "
                    "kilowatt in the name."},
            {"text": "958 kilojoules in a bag of crisps", "correct": False,
             "why": "That is an amount held in a store, not how fast anything "
                    "is transferred."},
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
        "options": [
            {"text": "Energy", "correct": False,
             "why": "Energy is measured in joules; watts always carry a time "
                    "in them."},
            {"text": "Power", "correct": True},
            {"text": "Force", "correct": False,
             "why": "Force is measured in newtons, and nothing about it is a "
                    "rate of energy transfer."},
            {"text": "Time", "correct": False,
             "why": "Time is measured in seconds, and it is the thing a watt "
                    "divides by."},
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
            {"text": "The 60 W lamp will cost more over a year",
             "correct": False,
             "why": "Only if it is on for as long. A 5 W lamp left on always "
                    "can easily cost more."},
            {"text": "The 60 W lamp is brighter", "correct": False,
             "why": "Brightness depends on the technology too — a 5 W LED can "
                    "beat a 60 W filament lamp."},
            {"text": "The 60 W lamp transfers more energy each second while "
                     "it is on",
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
            {"text": "Because the kettle transfers energy far faster, so more "
                     "passes through the cable each second",
             "correct": True},
            {"text": "Because the kettle is used at a hotter part of the "
                     "house",
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
                     "big",
             "correct": False,
             "why": "It transfers three times as fast, so it reaches the "
                    "temperature in about a third of the time."},
            {"text": "The 1 kW heater, because it has to run for far longer",
             "correct": False,
             "why": "Longer at a third of the rate comes to roughly the same "
                    "total, not to more."},
            {"text": "Roughly the same, because the room needs a fixed amount "
                     "of energy either way",
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
]
