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
            {"text": "An extra charge for using more units than your "
                     "allowance",
             "correct": False,
             "why": "It does not depend on how much you use at all — that is "
                    "the whole point of it."},
            {"text": "The cost of the first unit of electricity you use each "
                     "day",
             "correct": False,
             "why": "It is charged even on a day when no units are used."},
            {"text": "A one-off fee charged when you first join a supplier",
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
            {"text": "Because bills involve money as well as energy, and a "
                     "triangle has no place for money",
             "correct": False,
             "why": "Money is not what decides the shape. The arithmetic is."},
            {"text": "Because a triangle only works for three quantities, and "
                     "a bill has five appliances on it",
             "correct": False,
             "why": "Closer, but not the reason. Even a two-row bill would "
                    "need a beam, because a total of two rows is still a "
                    "sum."},
            {"text": "Because a triangle can only show a multiplication and "
                     "never a division of any kind",
             "correct": False,
             "why": "A triangle shows divisions perfectly well — that is most "
                    "of what it is for."},
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
            {"text": "Because the price per unit rises once you drop below a "
                     "certain amount",
             "correct": False,
             "why": "The unit price is the same however much you use. Nothing "
                    "on the bill works that way."},
            {"text": "Because the standing charge is a fixed portion that "
                     "does not move",
             "correct": True},
            {"text": "Because appliances draw more power when they are used "
                     "less often",
             "correct": False,
             "why": "An appliance draws its rated power whenever it runs, "
                    "regardless of how often that is."},
            {"text": "Because the meter cannot measure small amounts of "
                     "energy accurately",
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
            {"text": "Because charging in that way is simply more profitable "
                     "than putting it all into the unit price",
             "correct": False,
             "why": "It is a way of matching a cost to how that cost actually "
                    "arises, not a way of charging more."},
            {"text": "Because energy is more expensive to produce on days "
                     "when very little of it is used",
             "correct": False,
             "why": "Production cost does not rise on a quiet day."},
            {"text": "Because the cables, meters and repair crews cost the "
                     "same whether a house draws 400 units or none",
             "correct": True},
            {"text": "Because a fixed daily charge discourages people from "
                     "wasting energy around the house",
             "correct": False,
             "why": "It does the opposite if anything — it is the one part of "
                    "the bill that using less cannot reduce."},
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
            {"text": "The first, because a lower price for every unit is "
                     "always the better deal overall",
             "correct": False,
             "why": "For a low user the units are a small part of the bill, "
                    "so the daily charge dominates."},
            {"text": "The first, because 70p a day comes to only about £21 "
                     "over the course of a month",
             "correct": False,
             "why": "£21 against £12 is a £9 gap the cheaper units would have "
                    "to make up — and a low user does not buy enough units to "
                    "do it."},
            {"text": "It makes no difference, because the two bills always "
                     "come to the same total",
             "correct": False,
             "why": "They match only at one particular usage. Above and below "
                    "it, one is cheaper."},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p2-04-e05",
        "band": "easier",
        "text": "A 2 kW heater runs for 3 hours. How many units does it use?",
        "options": [
            {"text": "6 units", "correct": True},
            {"text": "1.5 units", "correct": False,
             "why": "That is 3 ÷ 2, the division upside down as well as the "
                    "wrong operation."},
            {"text": "5 units", "correct": False,
             "why": "That is 2 + 3, and a power cannot be added to a time."},
            {"text": "2 units, one for each kilowatt", "correct": False,
             "why": "The hours have to be counted in: a unit is a kilowatt "
                    "for an hour."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e06",
        "band": "easier",
        "text": "At 30p a unit, what do 12 units cost?",
        "options": [
            {"text": "£42", "correct": False,
             "why": "That adds 30 to 12 rather than multiplying, and then "
                    "reads pence as pounds."},
            {"text": "£3.60", "correct": True},
            {"text": "£0.40", "correct": False,
             "why": "That is 12 ÷ 30, dividing where the calculation "
                    "multiplies."},
            {"text": "£360", "correct": False,
             "why": "That is the answer in pence read as pounds — a hundred "
                    "times too much."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e07",
        "band": "easier",
        "text": "How many joules is one unit on a bill?",
        "options": [
            {"text": "1000 J", "correct": False,
             "why": "That is a kilojoule. A unit runs for a whole hour as "
                    "well."},
            {"text": "3600 J", "correct": False,
             "why": "That is one WATT for an hour; a kilowatt is a thousand "
                    "times more."},
            {"text": "3 600 000 J", "correct": True},
            {"text": "60 000 J", "correct": False,
             "why": "That uses 60 seconds instead of the 3600 in an hour."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e08",
        "band": "easier",
        "text": "A household uses no electricity at all for a whole month. "
                "What does it owe?",
        "options": [
            {"text": "Nothing at all", "correct": False,
             "why": "The standing charge is owed for being connected, "
                    "whatever is used."},
            {"text": "The standing charge for those days", "correct": True},
            {"text": "The price of one unit, as a minimum", "correct": False,
             "why": "No unit was used, so no unit is charged; the fixed daily "
                    "amount is what remains."},
            {"text": "Double the standing charge, as a penalty",
             "correct": False,
             "why": "Nothing doubles it. It is a fixed daily amount and "
                    "nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e09",
        "band": "easier",
        "text": "Which of these is a unit of ENERGY?",
        "options": [
            {"text": "The kilowatt", "correct": False,
             "why": "A kilowatt is a rate — a thousand joules every second."},
            {"text": "The kilowatt-hour", "correct": True},
            {"text": "The watt", "correct": False,
             "why": "A watt is one joule per second, which is a rate rather "
                    "than an amount."},
            {"text": "The pence per unit", "correct": False,
             "why": "That is a price, charged against an amount of energy."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e10",
        "band": "easier",
        "text": "A standing charge of 50p a day is billed over 30 days. How "
                "much is that?",
        "options": [
            {"text": "£1.50", "correct": False,
             "why": "That is 50 × 30 in pence read as though it were pounds "
                    "divided by ten."},
            {"text": "£15.00", "correct": True},
            {"text": "£80", "correct": False,
             "why": "That adds 50 to 30 instead of multiplying."},
            {"text": "£0.60", "correct": False,
             "why": "That is 30 ÷ 50, a division where a multiplication is "
                    "needed."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p2-04-s05",
        "band": "standard",
        "text": "A 3 kW immersion heater runs for 40 minutes a day. How many "
                "units a day is that?",
        "options": [
            {"text": "120 units", "correct": False,
             "why": "That is 3 × 40, with the minutes going in as though they "
                    "were hours."},
            {"text": "2 units", "correct": True},
            {"text": "0.075 units", "correct": False,
             "why": "That is 3 ÷ 40, dividing where the calculation "
                    "multiplies."},
            {"text": "1.33 units", "correct": False,
             "why": "That is 40 ÷ 30, which uses neither the rating nor the "
                    "right conversion."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s06",
        "band": "standard",
        "text": "A household uses 250 units in a month at 28p a unit. What is "
                "the energy part of the bill?",
        "options": [
            {"text": "£8.93", "correct": False,
             "why": "That is 250 ÷ 28, a division where the cost is units "
                    "MULTIPLIED by price."},
            {"text": "£70.00", "correct": True},
            {"text": "£2.78", "correct": False,
             "why": "That is 250 × 28 read with the decimal point two places "
                    "out."},
            {"text": "£7000", "correct": False,
             "why": "That is the answer in pence read as pounds — a hundred "
                    "times too much."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s07",
        "band": "standard",
        "text": "Which of these uses exactly two units of electricity?",
        "options": [
            {"text": "A 2 kW heater for 30 minutes", "correct": False,
             "why": "That is 2 × 0.5, which is one unit, not two."},
            {"text": "A 500 W lamp for 2 hours", "correct": False,
             "why": "0.5 kW for 2 hours is one unit; the watts have to become "
                    "kilowatts first."},
            {"text": "A 4 kW shower for 30 minutes", "correct": True},
            {"text": "A 100 W television for 2 hours", "correct": False,
             "why": "0.1 kW for 2 hours is 0.2 units — a tenth of what is "
                    "wanted."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s08",
        "band": "standard",
        "text": "A bill shows 300 units at 28p and a standing charge of 50p a "
                "day for 30 days. What is the total?",
        "options": [
            {"text": "£84.00, the units alone", "correct": False,
             "why": "That leaves the standing charge out, and it is owed "
                    "whatever the usage."},
            {"text": "£99.00, the units plus the standing charge",
             "correct": True},
            {"text": "£15.00, the standing charge alone", "correct": False,
             "why": "That leaves out the 300 units, which are the larger part "
                    "of the bill."},
            {"text": "£84.50, adding one day's standing charge",
             "correct": False,
             "why": "The standing charge runs for all 30 days, not for one."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s09",
        "band": "standard",
        "text": "Why does working out a bill need a sum of products rather "
                "than a single multiplication?",
        "options": [
            {"text": "Because each row is multiplied first, and the rows are "
                     "then added",
             "correct": True},
            {"text": "Because electricity and gas are charged at different "
                     "rates",
             "correct": False,
             "why": "That is one example of two rows, but the shape holds "
                    "even for one fuel with a standing charge."},
            {"text": "Because the price per unit changes every day",
             "correct": False,
             "why": "The price is normally fixed for the period; the two "
                    "different sorts of charge are what need adding."},
            {"text": "Because units and pounds cannot be multiplied together",
             "correct": False,
             "why": "They are multiplied together — that is exactly what each "
                    "row does."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s10",
        "band": "standard",
        "text": "A 9 W LED runs 6 hours a day for 30 days. Roughly how many "
                "units does it use in the month?",
        "options": [
            {"text": "About 1.6 units", "correct": True},
            {"text": "About 1620 units", "correct": False,
             "why": "That leaves the watts as watts; 9 W is 0.009 kW."},
            {"text": "About 54 units", "correct": False,
             "why": "That is 9 × 6, using watts and one day rather than "
                    "kilowatts and thirty."},
            {"text": "About 0.054 units", "correct": False,
             "why": "That is one day's worth, and the month has thirty of "
                    "them."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p2-04-h05",
        "band": "harder",
        "text": "A household on 28p a unit with a 50p daily standing charge "
                "uses 400 units in 30 days. What would halving the usage "
                "save?",
        "options": [
            {"text": "Half the whole bill, because usage is what a bill "
                     "charges for",
             "correct": False,
             "why": "The £15 standing charge does not move, so the saving is "
                    "less than half."},
            {"text": "£112.00, the whole of the energy charge",
             "correct": False,
             "why": "That is what stopping ALL use would save, not halving "
                    "it."},
            {"text": "£56.00, half the energy charge, with the £15 standing "
                     "charge unchanged",
             "correct": True},
            {"text": "£63.50, half of the whole bill", "correct": False,
             "why": "Halving the total would need the standing charge to halve "
                    "too, and it is fixed."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h06",
        "band": "harder",
        "text": "Supplier A charges 24p a unit with 70p a day; supplier B "
                "charges 29p a unit with 40p a day. Which suits a household "
                "using very little?",
        "options": [
            {"text": "A, because its unit price is lower", "correct": False,
             "why": "A low unit price helps a heavy user. A light user pays "
                    "mostly the daily charge."},
            {"text": "B, because its daily charge is lower", "correct": True},
            {"text": "A, because a lower unit price always wins",
             "correct": False,
             "why": "It only wins once enough units are bought to outweigh "
                    "the extra 30p a day."},
            {"text": "Neither — the two tariffs cost the same for everybody",
             "correct": False,
             "why": "They cross at one particular usage; above and below it "
                    "the winner changes."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h07",
        "band": "harder",
        "text": "Roughly how many units a day would the two tariffs in the "
                "last question cost the same?",
        "options": [
            {"text": "About 30 units a day", "correct": False,
             "why": "That is ten times too many; the difference in unit price "
                    "is 5p, not 1p."},
            {"text": "About 6 units a day", "correct": True},
            {"text": "About 0.6 units a day", "correct": False,
             "why": "That is ten times too few — 0.6 × 5p is only 3p, nowhere "
                    "near the 30p gap."},
            {"text": "They can never cost the same", "correct": False,
             "why": "The 30p daily gap and the 5p unit gap must cross, and "
                    "they do at 6 units."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h08",
        "band": "harder",
        "text": "A family is advised to switch off lights to save money. "
                "Their lighting is eight 9 W LEDs on 5 hours a day. What is "
                "the strongest response?",
        "options": [
            {"text": "It is good advice, because lights are on for longer "
                     "than anything else",
             "correct": False,
             "why": "Time alone is not the measure. At 0.36 kWh a day the "
                    "lighting is a very small share."},
            {"text": "It is poor advice, because switching a light off saves "
                     "no energy at all",
             "correct": False,
             "why": "It saves a real amount, just a small one — about 0.36 "
                    "units a day."},
            {"text": "It is poor advice here: the lighting is about 0.36 "
                     "units a day, far less than heating",
             "correct": True},
            {"text": "It cannot be judged without knowing the price per unit",
             "correct": False,
             "why": "The comparison is between appliances, and the same price "
                    "applies to all of them."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h09",
        "band": "harder",
        "text": "Why do suppliers charge a standing charge instead of putting "
                "everything into the unit price?",
        "options": [
            {"text": "Because the network costs the same whether anyone "
                     "uses electricity or not",
             "correct": True},
            {"text": "Because it makes the bill easier to work out",
             "correct": False,
             "why": "It makes it harder — the bill becomes a sum of two rows "
                    "instead of one product."},
            {"text": "Because the price of electricity changes during the "
                     "day",
             "correct": False,
             "why": "That is handled by different unit prices at different "
                    "times, not by a fixed daily charge."},
            {"text": "Because it stops households using too much "
                     "electricity",
             "correct": False,
             "why": "A charge that does not vary with usage cannot discourage "
                    "usage."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h10",
        "band": "harder",
        "text": "A student says a 3 kW heater used for 2 hours must cost more "
                "than a 100 W lamp used for 60 hours. Is that right?",
        "options": [
            {"text": "Yes — the heater's rating is thirty times larger",
             "correct": False,
             "why": "The rating is thirty times larger and the time thirty "
                    "times shorter, so they land in the same place."},
            {"text": "No — the lamp uses twice as many units", "correct": False,
             "why": "The lamp uses 6 units, the same as the heater, not twice "
                    "as many."},
            {"text": "No — both come to 6 units, so both cost the same",
             "correct": True},
            {"text": "It cannot be decided without the standing charge",
             "correct": False,
             "why": "The standing charge is owed either way, so it cannot "
                    "separate the two."},
        ],
        "figure": None,
    },
]
