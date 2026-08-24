"""P2 lesson 04 — Reading a fuel bill: twelve questions (MRB-223).

Written against Design's page. The 412 units, the 27p and 53p constants,
the four equal-area rectangles and the balance beam are hers.

The discriminations:

  · a unit IS a kilowatt-hour, and a kilowatt-hour is ENERGY (`ENER-25`);
  · one kilowatt-hour is one AREA, and four different shapes enclose it;
  · a bill is a SUM OF PRODUCTS — the arithmetic MRB-204 makes visible,
    and the reason the page carries a beam as well as a triangle;
  · the standing charge is owed whatever you do, so halving usage does not
    halve the bill (`ENER-26`) — the harder band turns on this.

⚠️ POSITION IS AUTHORED — index cycles 1, 2, 3, 0, giving three of each.

⚠️ Rung 1 ("one unit on an electricity bill is one…") and Rung 2 (the
2.2 kW oven for 45 min over 30 days) are NOT restated; check 6 of
`verify_questions.py` forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P2"
LESSON = "reading-a-fuel-bill"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p2-04-e01",
        "band": "easier",
        "text": "A kilowatt-hour is a unit of…",
        "options": [
            {"text": "power", "correct": False,
             "why": "The “hour” on the end means a time has already "
                    "been multiplied in, and a rate times a time is an "
                    "amount."},
            {"text": "energy", "correct": True},
            {"text": "time", "correct": False,
             "why": "It contains a time, but multiplied by a power — "
                    "which makes the result an amount of energy."},
            {"text": "cost", "correct": False,
             "why": "The cost is the units multiplied by a price. The unit "
                    "itself measures energy."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e02",
        "band": "easier",
        "text": "A 1 kW heater runs for one hour. How many units does it "
                "use?",
        "options": [
            {"text": "60", "correct": False,
             "why": "That is the number of minutes. A unit is a kilowatt for "
                    "an HOUR, so this is one of them."},
            {"text": "3 600 000", "correct": False,
             "why": "That is the number of JOULES in one unit — the same "
                    "energy, counted in a much smaller unit."},
            {"text": "1", "correct": True},
            {"text": "1000", "correct": False,
             "why": "That is the number of watts in a kilowatt, not the "
                    "number of units."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e03",
        "band": "easier",
        "text": "At 27p a unit, what does 20 units cost?",
        "options": [
            {"text": "£0.47", "correct": False,
             "why": "That is 27p + 20p. The units multiply by the price."},
            {"text": "£1.35", "correct": False,
             "why": "That is 27 ÷ 20. More units means more money, so "
                    "this must be a multiplication."},
            {"text": "£0.74", "correct": False,
             "why": "That is 20 ÷ 27, the division the wrong way round."},
            {"text": "£5.40", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e04",
        "band": "easier",
        "text": "What is a standing charge?",
        "options": [
            {"text": "A fixed daily amount for being connected, whatever you "
                     "use",
             "correct": True},
            {"text": "An extra charge for using more than your allowance",
             "correct": False,
             "why": "It does not depend on how much you use at all — "
                    "that is the whole point of it."},
            {"text": "The cost of the first unit each day", "correct": False,
             "why": "It is charged even on a day when no units are used."},
            {"text": "A one-off fee when you join a supplier",
             "correct": False,
             "why": "It appears on every bill, every day, not once."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p2-04-s01",
        "band": "standard",
        "text": "Which of these uses exactly one unit of electricity?",
        "options": [
            {"text": "A 100 W lamp for 1 hour", "correct": False,
             "why": "0.1 kW × 1 h = 0.1 units. It would need ten "
                    "hours."},
            {"text": "A 100 W lamp for 10 hours", "correct": True},
            {"text": "A 2 kW heater for 1 hour", "correct": False,
             "why": "2 kW × 1 h = 2 units. Half an hour would do it."},
            {"text": "A 1 kW heater for 10 minutes", "correct": False,
             "why": "1 kW × (1/6) h = 0.17 units. It would need a full "
                    "hour."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s02",
        "band": "standard",
        "text": "A 9 W LED runs for 111 hours and a 2 kW heater runs for 30 "
                "minutes. What is true of the two?",
        "options": [
            {"text": "The heater uses about two hundred times more",
             "correct": False,
             "why": "Both come to about one unit. The heater's higher rate "
                    "is cancelled by its much shorter time."},
            {"text": "The LED uses more, because it runs far longer",
             "correct": False,
             "why": "Longer, yes, but at a tiny rate. Both products land in "
                    "the same place."},
            {"text": "They use about the same energy — one unit each",
             "correct": True},
            {"text": "It cannot be compared without knowing the tariff",
             "correct": False,
             "why": "The tariff turns units into money. The units themselves "
                    "are fixed by power and time alone."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s03",
        "band": "standard",
        "text": "Why does a bill need a balance beam to describe it and not "
                "just a formula triangle?",
        "options": [
            {"text": "Because bills involve money as well as energy",
             "correct": False,
             "why": "Money is not what decides the shape. The arithmetic is."},
            {"text": "Because a triangle only works for three quantities and "
                     "a bill has five appliances",
             "correct": False,
             "why": "Closer, but not the reason. Even a two-row bill would "
                    "need a beam, because a total of two rows is still a "
                    "sum."},
            {"text": "Because a triangle cannot show a division",
             "correct": False,
             "why": "A triangle shows divisions perfectly well — that is "
                    "most of what it is for."},
            {"text": "Because each row is a product but the total is a SUM, "
                     "and a triangle cannot show adding up",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s04",
        "band": "standard",
        "text": "A household uses 300 units in a month at 27p each, with a "
                "53p daily standing charge over 30 days. What is the bill?",
        "options": [
            {"text": "About £96.90", "correct": True},
            {"text": "About £81.00", "correct": False,
             "why": "That is the units alone. The standing charge has not "
                    "been added."},
            {"text": "About £15.90", "correct": False,
             "why": "That is the standing charge alone, with no units."},
            {"text": "About £81.53", "correct": False,
             "why": "That adds ONE day of standing charge. It is charged for "
                    "all thirty."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p2-04-h01",
        "band": "harder",
        "text": "A family halves its electricity usage. Why does the bill "
                "fall by less than half?",
        "options": [
            {"text": "Because the price per unit rises when you use less",
             "correct": False,
             "why": "The unit price is the same however much you use. "
                    "Nothing on the bill works that way."},
            {"text": "Because the standing charge is a fixed portion that "
                     "does not move",
             "correct": True},
            {"text": "Because appliances draw more power when used less "
                     "often",
             "correct": False,
             "why": "An appliance draws its rated power whenever it runs, "
                    "regardless of how often that is."},
            {"text": "Because the meter cannot measure small amounts "
                     "accurately",
             "correct": False,
             "why": "Meters measure small amounts fine. The reason is on the "
                    "bill, in plain sight."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h02",
        "band": "harder",
        "text": "Why do suppliers charge a standing charge at all, rather "
                "than putting everything into the unit price?",
        "options": [
            {"text": "Because it is more profitable than charging per unit",
             "correct": False,
             "why": "It is a way of matching a cost to how that cost "
                    "actually arises, not a way of charging more."},
            {"text": "Because energy is more expensive to produce on days "
                     "when little is used",
             "correct": False,
             "why": "Production cost does not rise on a quiet day."},
            {"text": "Because the cables, meters and repair crews cost the "
                     "same whether a house draws 400 units or none",
             "correct": True},
            {"text": "Because it discourages people from wasting energy",
             "correct": False,
             "why": "It does the opposite if anything — it is the one "
                    "part of the bill that using less cannot reduce."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h03",
        "band": "harder",
        "text": "Two suppliers offer 24p a unit with 70p a day, and 29p a "
                "unit with 40p a day. For a household using very little "
                "electricity, which is likely better and why?",
        "options": [
            {"text": "The first, because a lower unit price is always better",
             "correct": False,
             "why": "For a low user the units are a small part of the bill, "
                    "so the daily charge dominates."},
            {"text": "The first, because 70p a day is only £21 a month",
             "correct": False,
             "why": "£21 against £12 is a £9 gap the cheaper units would "
                    "have to make up — and a low user does not buy "
                    "enough units to do it."},
            {"text": "It makes no difference; the totals always match",
             "correct": False,
             "why": "They match only at one particular usage. Above and "
                    "below it, one is cheaper."},
            {"text": "The second, because the lower daily charge saves more "
                     "than the higher unit price costs",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h04",
        "band": "harder",
        "text": "A student is told a household's five appliances each use "
                "between 20 and 60 units, and that the amount due is £127. "
                "Which shape describes the calculation as a whole?",
        "options": [
            {"text": "A sum of products, plus one fixed term",
             "correct": True},
            {"text": "A single product of power and time",
             "correct": False,
             "why": "That describes ONE ROW. There are five of them and a "
                    "standing charge."},
            {"text": "A product of five sums", "correct": False,
             "why": "The other way round. Each appliance is multiplied "
                    "first, and the results are then added."},
            {"text": "A sum of five equal terms", "correct": False,
             "why": "The rows are not equal — they run from 20 to 60 "
                    "units — and there is a sixth term that is not a "
                    "row at all."},
        ],
        "figure": None,
    },
]
