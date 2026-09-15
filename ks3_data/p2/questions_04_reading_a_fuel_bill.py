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
            {"text": "It is poor advice, because switching a light off never "
                     "saves any energy at all",
             "correct": False,
             "why": "It saves a real amount, just a small one — about 0.36 "
                    "units a day."},
            {"text": "Poor advice here: the lighting is only about 0.36 units "
                     "a day",
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
            {"text": "Because the network costs the same however much is used",
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
            {"text": "Because it stops households from using too much "
                     "electricity at once",
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

    # ── MRB-338 night 3 top-up · easier ──────────────────────────────────
    {
        "id": "p2-04-e11",
        "band": "easier",
        "text": "A meter read 41 250 at the start of a month and 41 662 at "
                "the end. How many units were used?",
        "options": [
            {"text": "412", "correct": True},
            {"text": "41 662", "correct": False,
             "why": "That is the closing reading, which counts everything "
                    "since the meter was fitted."},
            {"text": "82 912", "correct": False,
             "why": "That adds the two readings, and the month's use is the "
                    "difference between them."},
            {"text": "41 250", "correct": False,
             "why": "That is the opening reading, which was already on the "
                    "meter before the month began."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e12",
        "band": "easier",
        "text": "The energy charge on a bill is the units used multiplied by "
                "what?",
        "options": [
            {"text": "The number of days in the billing period",
             "correct": False,
             "why": "Days multiply the standing charge, which is a separate "
                    "line altogether."},
            {"text": "The price per unit", "correct": True},
            {"text": "The power rating of the largest appliance",
             "correct": False,
             "why": "No rating appears on a bill; the meter has already turned "
                    "everything into units."},
            {"text": "The standing charge for the month", "correct": False,
             "why": "The standing charge is added at the end rather than "
                    "multiplied by anything."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e13",
        "band": "easier",
        "text": "A 1.5 kW towel rail is left on from six until eight in the "
                "evening. How many units appear on the bill?",
        "options": [
            {"text": "0.75 units", "correct": False,
             "why": "That is 1.5 ÷ 2, a division where the two figures "
                    "multiply."},
            {"text": "3.5 units", "correct": False,
             "why": "That adds the hours to the kilowatts, which cannot be "
                    "done."},
            {"text": "3 units", "correct": True},
            {"text": "1.5 units", "correct": False,
             "why": "That is one hour's worth, and the rail was on for two."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e14",
        "band": "easier",
        "text": "A bill lists units used, price per unit, standing charge and "
                "days. Which two multiply together?",
        "options": [
            {"text": "Units used and the number of days", "correct": False,
             "why": "Multiplying those gives nothing on the bill; the days "
                    "belong with the standing charge."},
            {"text": "The standing charge and the price per unit",
             "correct": False,
             "why": "Those two never meet; one is charged per day and the "
                    "other per unit."},
            {"text": "The price per unit and the number of days",
             "correct": False,
             "why": "The price is charged against units, and days are charged "
                    "the standing rate."},
            {"text": "Units used and the price per unit", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e15",
        "band": "easier",
        "text": "Domestic gas and electricity carry VAT at what rate?",
        "options": [
            {"text": "20 per cent", "correct": False,
             "why": "That is the standard rate, and domestic energy is charged "
                    "at a lower one."},
            {"text": "5 per cent", "correct": True},
            {"text": "No VAT at all", "correct": False,
             "why": "There is VAT on a domestic bill; it is simply charged at "
                    "a reduced rate."},
            {"text": "27 per cent", "correct": False,
             "why": "27 is the price of a unit in pence, not a rate of tax."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e16",
        "band": "easier",
        "text": "What does a gas meter actually count?",
        "options": [
            {"text": "The volume of gas that has gone past, in cubic metres",
             "correct": True},
            {"text": "The energy the gas carries, in kilowatt-hours",
             "correct": False,
             "why": "The energy is worked out from the volume afterwards; the "
                    "meter cannot measure it."},
            {"text": "The mass of gas burnt, in kilograms", "correct": False,
             "why": "Nothing on a gas meter weighs anything."},
            {"text": "The money owed, in pounds and pence", "correct": False,
             "why": "The price is applied later, once the volume has become "
                    "kilowatt-hours."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e17",
        "band": "easier",
        "text": "One kilowatt-hour is 3.6 MJ. How many megajoules is 4 kWh?",
        "options": [
            {"text": "0.9 MJ", "correct": False,
             "why": "That divides by four, which would make more units into "
                    "less energy."},
            {"text": "7.6 MJ", "correct": False,
             "why": "That adds four to the conversion figure rather than "
                    "multiplying by it."},
            {"text": "14.4 MJ", "correct": True},
            {"text": "3.6 MJ", "correct": False,
             "why": "That is a single unit, and the question asks about "
                    "four."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e18",
        "band": "easier",
        "text": "A bill covers 28 days with a standing charge of 53p a day. "
                "What does that come to?",
        "options": [
            {"text": "£14.84", "correct": True},
            {"text": "£0.81", "correct": False,
             "why": "That adds the pence to the days instead of multiplying "
                    "them."},
            {"text": "£53.00", "correct": False,
             "why": "That charges 53p once and then reads it as pounds."},
            {"text": "£1.89", "correct": False,
             "why": "That is 53 ÷ 28, a division where the calculation "
                    "multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e19",
        "band": "easier",
        "text": "How many units does a 100 W lamp use in 20 hours?",
        "options": [
            {"text": "2000 units", "correct": False,
             "why": "That leaves the rating in watts; 100 W is 0.1 kW."},
            {"text": "20 units", "correct": False,
             "why": "That charges a whole kilowatt for every hour, and the "
                    "lamp draws a tenth of one."},
            {"text": "0.2 units", "correct": False,
             "why": "That is one tenth of the right answer, from using 2 hours "
                    "rather than 20."},
            {"text": "2 units", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e20",
        "band": "easier",
        "text": "A price per unit is quoted in what?",
        "options": [
            {"text": "Pence for each kilowatt-hour", "correct": True},
            {"text": "Pence for each kilowatt", "correct": False,
             "why": "A kilowatt is a rate, and nobody is charged for a rate — "
                    "only for the energy it delivers."},
            {"text": "Pounds for each day connected", "correct": False,
             "why": "That describes the standing charge, which is a different "
                    "line on the bill."},
            {"text": "Pence for each joule", "correct": False,
             "why": "A joule is far too small to price; a unit is 3 600 000 of "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e21",
        "band": "easier",
        "text": "A household uses 500 units at 25p each. What is the energy "
                "charge?",
        "options": [
            {"text": "£525", "correct": False,
             "why": "That adds the pence to the units and then reads the "
                    "result as pounds."},
            {"text": "£125", "correct": True},
            {"text": "£20", "correct": False,
             "why": "That is 500 ÷ 25, a division where the cost is a "
                    "product."},
            {"text": "£12 500", "correct": False,
             "why": "That is the answer in pence read as pounds — a hundred "
                    "times too much."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e22",
        "band": "easier",
        "text": "Which of these appears on a gas bill but never on an "
                "electricity one?",
        "options": [
            {"text": "A standing charge", "correct": False,
             "why": "Both fuels carry one; it pays for the connection either "
                    "way."},
            {"text": "A price per kilowatt-hour", "correct": False,
             "why": "Both are priced per kilowatt-hour once the energy is "
                    "known."},
            {"text": "A calorific value", "correct": True},
            {"text": "A meter reading", "correct": False,
             "why": "Both fuels are metered, and both bills print the "
                    "readings."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e23",
        "band": "easier",
        "text": "An electricity meter shows 08234 in its window. What does "
                "that number count?",
        "options": [
            {"text": "The pounds owed since the last bill", "correct": False,
             "why": "A meter counts energy. The money is worked out from it "
                    "afterwards."},
            {"text": "The power being drawn at that moment", "correct": False,
             "why": "A rate would rise and fall all day; this figure only "
                    "climbs."},
            {"text": "The days since the meter was installed", "correct": False,
             "why": "Days are counted on the bill for the standing charge, not "
                    "by the meter."},
            {"text": "The units used since the meter was fitted",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e24",
        "band": "easier",
        "text": "Two homes are on the same tariff. One uses 200 units and the "
                "other 400. Which pays more for energy?",
        "options": [
            {"text": "The 400-unit home", "correct": True},
            {"text": "The 200-unit home, because a smaller user pays a higher "
                     "rate",
             "correct": False,
             "why": "The rate is the same on one tariff, however much is "
                    "used."},
            {"text": "Both the same, because the tariff is the same",
             "correct": False,
             "why": "The tariff fixes the price of each unit, and one home "
                    "bought twice as many."},
            {"text": "It cannot be said without knowing the standing charge",
             "correct": False,
             "why": "The standing charge is the same for both, so it cannot "
                    "change which pays more."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e25",
        "band": "easier",
        "text": "A unit costs 27p. What is that in pounds?",
        "options": [
            {"text": "£27.00", "correct": False,
             "why": "That reads pence as pounds, making a unit a hundred times "
                    "too expensive."},
            {"text": "£2.70", "correct": False,
             "why": "That divides by ten; there are a hundred pence in a "
                    "pound."},
            {"text": "£0.27", "correct": True},
            {"text": "£0.027", "correct": False,
             "why": "That divides by a thousand, which is one step too far."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e26",
        "band": "easier",
        "text": "A 2 kW kettle is used for a total of 15 minutes in a week. "
                "How many units is that?",
        "options": [
            {"text": "30 units", "correct": False,
             "why": "That is 2 × 15, with the minutes standing in for hours."},
            {"text": "2 units", "correct": False,
             "why": "That charges a full hour, and the kettle ran for a "
                    "quarter of one."},
            {"text": "0.5 units", "correct": True},
            {"text": "0.13 units", "correct": False,
             "why": "That is 2 ÷ 15, a division where the calculation "
                    "multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e27",
        "band": "easier",
        "text": "A month's energy charge is £27.00 at 27p a unit. How many "
                "units were used?",
        "options": [
            {"text": "100 units", "correct": True},
            {"text": "729 units", "correct": False,
             "why": "That multiplies the two, and the units come from dividing "
                    "the charge by the price."},
            {"text": "27 units", "correct": False,
             "why": "That reads the pounds as units, which would make every "
                    "unit cost a pound."},
            {"text": "0.01 units", "correct": False,
             "why": "That is 0.27 ÷ 27, the division the wrong way up."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e28",
        "band": "easier",
        "text": "A gas bill converts the cubic metres on the meter into what, "
                "before charging for them?",
        "options": [
            {"text": "Litres", "correct": False,
             "why": "That is still a volume, and a bill charges for energy."},
            {"text": "Kilowatt-hours", "correct": True},
            {"text": "Kilowatts", "correct": False,
             "why": "A kilowatt is a rate, and a bill charges for an amount."},
            {"text": "Degrees Celsius", "correct": False,
             "why": "Temperature plays no part in what a bill charges for."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e29",
        "band": "easier",
        "text": "At 53p a day, roughly how many days of standing charge come "
                "to about £16?",
        "options": [
            {"text": "About 3", "correct": False,
             "why": "Three days come to about £1.60, which is a tenth of the "
                    "figure."},
            {"text": "About 300", "correct": False,
             "why": "Three hundred days would come to about £159, ten times "
                    "too much."},
            {"text": "About 30", "correct": True},
            {"text": "About 16", "correct": False,
             "why": "That reads the pounds as days; each day costs about half "
                    "a pound."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-e30",
        "band": "easier",
        "text": "Why is a meter reading taken at the start and the end of a "
                "billing period?",
        "options": [
            {"text": "So the units used in between can be found by "
                     "subtracting", "correct": True},
            {"text": "So the meter can be reset to zero for the new period",
             "correct": False,
             "why": "A meter is never reset; it simply keeps counting "
                    "upwards."},
            {"text": "So the standing charge can be worked out from the "
                     "readings",
             "correct": False,
             "why": "The standing charge comes from the number of days, which "
                    "the meter knows nothing about."},
            {"text": "So the price per unit can be set for that household",
             "correct": False,
             "why": "The price comes from the tariff and is the same whatever "
                    "the meter says."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ────────────────────────────────
    {
        "id": "p2-04-s11",
        "band": "standard",
        "text": "A meter goes from 12 480 to 12 815 over a month, at 26p a "
                "unit. What is the energy charge?",
        "options": [
            {"text": "£3332.30", "correct": False,
             "why": "That charges for the whole closing reading rather than "
                    "the month's use."},
            {"text": "£87.10", "correct": True},
            {"text": "£335.00", "correct": False,
             "why": "That is the number of units read as pounds, with the "
                    "price never applied."},
            {"text": "£12.88", "correct": False,
             "why": "That is 335 ÷ 26, a division where the cost is units "
                    "multiplied by price."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s12",
        "band": "standard",
        "text": "A 3 kW shower is used for 20 minutes a day across a 30-day "
                "month. How many units?",
        "options": [
            {"text": "1800 units", "correct": False,
             "why": "That is 3 × 20 × 30, with the minutes treated as "
                    "hours."},
            {"text": "90 units", "correct": False,
             "why": "That charges a full hour a day rather than a third of "
                    "one."},
            {"text": "30 units", "correct": True},
            {"text": "1 unit", "correct": False,
             "why": "That is one day's worth, and the month holds thirty of "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s13",
        "band": "standard",
        "text": "One month's electricity comes to 200 units priced 25p, and the "
                "connection is charged 45p on each of 30 days. What is owed "
                "altogether?",
        "options": [
            {"text": "£50.00", "correct": False,
             "why": "That is the units alone, with the standing charge left "
                    "out."},
            {"text": "£13.50", "correct": False,
             "why": "That is the standing charge alone, with the 200 units "
                    "left out."},
            {"text": "£63.50", "correct": True},
            {"text": "£50.45", "correct": False,
             "why": "That adds one day of standing charge where thirty are "
                    "owed."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s14",
        "band": "standard",
        "text": "A 90 W fridge motor runs about 5 hours a day. How many units "
                "does it use in 30 days?",
        "options": [
            {"text": "13 500 units", "correct": False,
             "why": "That leaves the rating in watts, which is a thousand "
                    "times too large."},
            {"text": "13.5 units", "correct": True},
            {"text": "0.45 units", "correct": False,
             "why": "That is one day's worth, and the month holds thirty of "
                    "them."},
            {"text": "2700 units", "correct": False,
             "why": "That is 90 × 30, using watts and leaving the hours out "
                    "altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s15",
        "band": "standard",
        "text": "A gas meter's 100 m³ works out as about 1122 kWh. At 7p a "
                "kWh, what is the gas charge?",
        "options": [
            {"text": "£7854", "correct": False,
             "why": "That is the answer in pence read as pounds — a hundred "
                    "times too much."},
            {"text": "£7.00", "correct": False,
             "why": "That charges for one kilowatt-hour rather than for "
                    "eleven hundred of them."},
            {"text": "£160.29", "correct": False,
             "why": "That is 1122 ÷ 7, a division where the cost is a "
                    "product."},
            {"text": "£78.54", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s16",
        "band": "standard",
        "text": "Why does a gas bill print a calorific value?",
        "options": [
            {"text": "Because the energy in each cubic metre depends on where "
                     "the gas came from", "correct": True},
            {"text": "Because the price of gas changes with the weather",
             "correct": False,
             "why": "The price comes from the tariff, and the calorific value "
                    "is about the gas itself."},
            {"text": "Because a meter measures energy and the value gives a "
                     "volume",
             "correct": False,
             "why": "It runs the other way: the meter measures volume and the "
                    "value turns it into energy."},
            {"text": "Because VAT on gas is worked out from the calorific "
                     "value",
             "correct": False,
             "why": "VAT is a percentage of the money charged and has nothing "
                    "to do with the gas's energy."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s17",
        "band": "standard",
        "text": "A bill comes to £120, of which £16 is standing charge. How "
                "much of it could using less electricity reduce?",
        "options": [
            {"text": "£120",
             "correct": False,
             "why": "The standing charge is owed whatever is used, so £16 of "
                    "it will not move."},
            {"text": "£16",
             "correct": False,
             "why": "The standing charge is the one part a household cannot "
                    "control at all."},
            {"text": "£104", "correct": True},
            {"text": "£60",
             "correct": False,
             "why": "Nothing splits a bill in half; the figures are given and "
                    "the fixed part is £16."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s18",
        "band": "standard",
        "text": "A 2.5 kW tumble dryer is run three times a week for 90 "
                "minutes. How many units in four weeks?",
        "options": [
            {"text": "2700 units", "correct": False,
             "why": "That uses 90 as though it were hours rather than "
                    "minutes."},
            {"text": "11.25 units", "correct": False,
             "why": "That is one week's worth, and the question asks about "
                    "four."},
            {"text": "3.75 units", "correct": False,
             "why": "That is a single run, with neither the three runs nor the "
                    "four weeks counted."},
            {"text": "45 units", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s19",
        "band": "standard",
        "text": "A domestic bill is £80 before VAT, which is charged at 5 per "
                "cent. What is the total?",
        "options": [
            {"text": "£84", "correct": True},
            {"text": "£96", "correct": False,
             "why": "That applies 20 per cent, which is the standard rate "
                    "rather than the domestic one."},
            {"text": "£85", "correct": False,
             "why": "That adds £5 rather than 5 per cent of £80, which is "
                    "£4."},
            {"text": "£76", "correct": False,
             "why": "That takes the VAT off instead of adding it on."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s20",
        "band": "standard",
        "text": "A household's monthly use falls from 400 units to 300. At 27p "
                "a unit, what is saved?",
        "options": [
            {"text": "£81", "correct": False,
             "why": "That is what the remaining 300 units cost, not what was "
                    "saved."},
            {"text": "£108", "correct": False,
             "why": "That is what all 400 units cost before the change."},
            {"text": "£27", "correct": True},
            {"text": "£100", "correct": False,
             "why": "That is the number of units saved, with the price never "
                    "applied to it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s21",
        "band": "standard",
        "text": "One unit is 3.6 MJ. How many units are there in 18 MJ?",
        "options": [
            {"text": "64.8 units", "correct": False,
             "why": "That multiplies the two, and the count comes from "
                    "dividing."},
            {"text": "0.2 units", "correct": False,
             "why": "That is 3.6 ÷ 18, the division the wrong way up."},
            {"text": "5 units", "correct": True},
            {"text": "21.6 units", "correct": False,
             "why": "That adds the two figures, which cannot be done to a "
                    "quantity and a conversion."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s22",
        "band": "standard",
        "text": "Two meter readings taken 90 days apart differ by 1080 units. "
                "What is the average daily use?",
        "options": [
            {"text": "12 units a day", "correct": True},
            {"text": "97 200 units a day", "correct": False,
             "why": "That multiplies the two, and an average comes from "
                    "dividing."},
            {"text": "1080 units a day", "correct": False,
             "why": "That is the whole period's use charged to a single day."},
            {"text": "0.08 units a day", "correct": False,
             "why": "That is 90 ÷ 1080, the division upside down."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s23",
        "band": "standard",
        "text": "A supplier raises the unit price from 25p to 30p. A home "
                "using 350 units a month pays how much more?",
        "options": [
            {"text": "£105.00", "correct": False,
             "why": "That is the new monthly charge in full, not the increase "
                    "in it."},
            {"text": "£5.00", "correct": False,
             "why": "That is the rise in pence read as pounds, with the 350 "
                    "units never counted."},
            {"text": "£87.50", "correct": False,
             "why": "That is the old monthly charge, which is what the rise "
                    "is measured against."},
            {"text": "£17.50", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s24",
        "band": "standard",
        "text": "A 9 W LED and a 60 W lamp each run 5 hours a day for 30 days. "
                "What is the difference in units?",
        "options": [
            {"text": "51 units", "correct": False,
             "why": "That is the gap in watts, with neither the hours nor the "
                    "conversion to kilowatts applied."},
            {"text": "7.65 units", "correct": True},
            {"text": "9 units", "correct": False,
             "why": "That is the lamp's own total; the question asks for the "
                    "gap between the two."},
            {"text": "0.255 units", "correct": False,
             "why": "That is one day's difference, and the month holds thirty "
                    "of them."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s25",
        "band": "standard",
        "text": "Why can a household's bill be much higher in January than in "
                "July with the same appliances?",
        "options": [
            {"text": "Because appliances draw more power when the weather "
                     "outside is colder",
             "correct": False,
             "why": "A rating does not change with the season; it is the "
                    "running hours that do."},
            {"text": "Because the standing charge is higher through the "
                     "winter months",
             "correct": False,
             "why": "The standing charge is a fixed daily amount and does not "
                    "move with the season."},
            {"text": "Because heating and lighting run for far longer",
             "correct": True},
            {"text": "Because a meter counts faster when the house is warm "
                     "inside",
             "correct": False,
             "why": "A meter counts energy, and nothing about the room "
                    "changes how it counts."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s26",
        "band": "standard",
        "text": "A prepayment meter holds £5 of credit at 28p a unit. Ignoring "
                "the standing charge, how many units is that?",
        "options": [
            {"text": "About 140 units", "correct": False,
             "why": "That multiplies the two, and the count comes from "
                    "dividing the credit by the price."},
            {"text": "About 18 units", "correct": True},
            {"text": "About 5 units", "correct": False,
             "why": "That reads the pounds as units, which would price a unit "
                    "at a pound."},
            {"text": "About 0.06 units", "correct": False,
             "why": "That is 0.28 ÷ 5, the division the wrong way round."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s27",
        "band": "standard",
        "text": "Which adds more to a bill each day: a 2 kW kettle used 10 "
                "minutes, or a 60 W lamp on for 10 hours?",
        "options": [
            {"text": "The kettle, because its rating is over thirty times "
                     "higher",
             "correct": False,
             "why": "The kettle gives 0.33 units and the lamp 0.6, so the "
                    "rating does not settle it."},
            {"text": "They are equal, because ten minutes and ten hours "
                     "balance the ratings",
             "correct": False,
             "why": "The lamp runs sixty times as long at a thirty-third of "
                    "the rate, so it comes out ahead."},
            {"text": "The lamp, at 0.6 units against 0.33", "correct": True},
            {"text": "The lamp, at 6 units against 0.33", "correct": False,
             "why": "6 units would need the lamp to be rated 600 W; at 60 W "
                    "it uses 0.6."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s28",
        "band": "standard",
        "text": "A bill covers 62 days and the standing charge is 53p a day. "
                "How much of the bill is fixed?",
        "options": [
            {"text": "£32.86", "correct": True},
            {"text": "£1.17", "correct": False,
             "why": "That is 62 ÷ 53, a division where the calculation "
                    "multiplies."},
            {"text": "£53.00", "correct": False,
             "why": "That charges 53p once and reads it as pounds."},
            {"text": "£62.53", "correct": False,
             "why": "That adds the pence to the days rather than multiplying "
                    "them together."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s29",
        "band": "standard",
        "text": "Which two figures does a fair comparison of two suppliers "
                "need?",
        "options": [
            {"text": "The price per unit and the daily standing charge",
             "correct": True},
            {"text": "The price per unit and the number of appliances in the "
                     "house",
             "correct": False,
             "why": "How many appliances there are does not appear on a bill; "
                    "the meter has already counted their energy."},
            {"text": "The standing charge and the reading on the meter",
             "correct": False,
             "why": "The reading is the household's own use, which is the same "
                    "whichever supplier bills for it."},
            {"text": "The price per unit and the VAT rate charged",
             "correct": False,
             "why": "VAT is the same 5 per cent on every domestic bill, so it "
                    "cannot separate two suppliers."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-s30",
        "band": "standard",
        "text": "A 7 kW car charger is used for 3 hours a night on 20 nights, "
                "at 27p a unit. What does that cost?",
        "options": [
            {"text": "£5.67", "correct": False,
             "why": "That charges for one night of three hours and leaves the "
                    "other nineteen out."},
            {"text": "£420.00", "correct": False,
             "why": "That is the number of units read as pounds, with the "
                    "price never applied."},
            {"text": "£113.40", "correct": True},
            {"text": "£37.80", "correct": False,
             "why": "That uses one hour a night rather than three."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ──────────────────────────────────
    {
        "id": "p2-04-h11",
        "band": "harder",
        "text": "A meter goes from 04 812 to 05 006 in 31 days. At 27p a unit "
                "and 53p a day, what is the total bill?",
        "options": [
            {"text": "£52.38",
             "correct": False,
             "why": "That is the energy charge on its own; 31 days of standing "
                    "charge are still owed."},
            {"text": "£68.81", "correct": True},
            {"text": "£16.43",
             "correct": False,
             "why": "That leaves out the 194 units, which are the larger part "
                    "of the bill."},
            {"text": "£1352.15",
             "correct": False,
             "why": "The closing reading counts every unit since the meter was "
                    "fitted, not this month's."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h12",
        "band": "harder",
        "text": "A gas bill converts with kWh = m³ × 1.02264 × 39.5 ÷ 3.6. "
                "Roughly what does 120 m³ come to?",
        "options": [
            {"text": "About 135 kWh", "correct": False,
             "why": "That is ten times too small; the conversion multiplies a "
                    "cubic metre up to about eleven kilowatt-hours."},
            {"text": "About 4850 kWh", "correct": False,
             "why": "That stops at the megajoules and never divides by 3.6."},
            {"text": "About 1350 kWh", "correct": True},
            {"text": "About 120 kWh", "correct": False,
             "why": "That treats one cubic metre as one kilowatt-hour, which "
                    "is why the conversion exists."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h13",
        "band": "harder",
        "text": "A gas bill's calorific value falls from 39.5 to 38.0. What "
                "happens to the kWh billed for the same volume?",
        "options": [
            {"text": "It rises by about 4 per cent, because a lower value "
                     "means more gas is needed",
             "correct": False,
             "why": "The volume is fixed by the meter, so a lower value can "
                    "only reduce the energy it stands for."},
            {"text": "It falls by about 4 per cent", "correct": True},
            {"text": "It does not change",
             "correct": False,
             "why": "The reading is a volume, and the energy it converts to "
                    "depends on this very figure."},
            {"text": "It falls by about 40 per cent, because the value dropped "
                     "by 1.5",
             "correct": False,
             "why": "1.5 out of 39.5 is under four per cent, not forty."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h14",
        "band": "harder",
        "text": "A home using 400 units a month at 27p, with 53p a day over 30 "
                "days, halves its usage as the standing charge rises to 73p. "
                "Does the bill fall?",
        "options": [
            {"text": "No — it rises",
             "correct": False,
             "why": "The standing charge rises by £6 while the units fall by "
                    "£54, so the saving is far from cancelled."},
            {"text": "No — halving usage cannot beat a rise in a fixed "
                     "charge",
             "correct": False,
             "why": "A fixed charge is the smaller part of this bill, so "
                    "halving the larger part wins comfortably."},
            {"text": "Yes — by about £48", "correct": True},
            {"text": "Yes — by about £62, which is half of the original bill",
             "correct": False,
             "why": "Half the bill would need the standing charge to halve "
                    "too, and it has risen instead."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h15",
        "band": "harder",
        "text": "Gas costs 7p a kWh and electricity 27p a kWh. For the same "
                "warmth, which is cheaper and by roughly what factor?",
        "options": [
            {"text": "Gas, by about four times", "correct": True},
            {"text": "Gas, by about twenty times", "correct": False,
             "why": "That is the gap in pence rather than the factor; 27 "
                    "divided by 7 is under four."},
            {"text": "Electricity, because it is measured in the same unit and "
                     "therefore costs the same",
             "correct": False,
             "why": "Sharing a unit is what makes the two comparable, and the "
                    "comparison favours gas."},
            {"text": "Neither — the two cannot be compared, because gas is "
                     "metered by volume",
             "correct": False,
             "why": "The volume is converted to kilowatt-hours on the bill, "
                    "which is exactly what allows the comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h16",
        "band": "harder",
        "text": "A display shows 0.42 kW being drawn right now. At 27p a unit, "
                "what would an hour at that rate add?",
        "options": [
            {"text": "About 27p",
             "correct": False,
             "why": "27p buys a whole unit, and an hour at 0.42 kW is well "
                    "under half of one."},
            {"text": "About £1.13",
             "correct": False,
             "why": "That is a hundred times too much, from reading pence as "
                    "pounds."},
            {"text": "About 64p",
             "correct": False,
             "why": "Dividing gives nothing meaningful here; the cost is units "
                    "multiplied by price."},
            {"text": "About 11p", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h17",
        "band": "harder",
        "text": "Which saves more a month: cutting an 8.5 kW shower from 20 to "
                "10 minutes a day, or switching off eight 9 W lamps that ran 5 "
                "hours a day?",
        "options": [
            {"text": "The lamps, because eight of them run far longer than "
                     "one shower",
             "correct": False,
             "why": "Eight lamps come to 72 W, which is a hundredth of the "
                    "shower's rating."},
            {"text": "The shower, by about four times", "correct": True},
            {"text": "They save about the same, at roughly 40 units each",
             "correct": False,
             "why": "The lamps save about 11 units and the shower about "
                    "42."},
            {"text": "The shower, by about a hundred times, which is the gap "
                     "in their ratings",
             "correct": False,
             "why": "The ratings do differ by about a hundred, and the lamps "
                    "run for thirty times as long, which closes most of it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h18",
        "band": "harder",
        "text": "A bill shows an energy charge of £30.24 at 28p a unit. What "
                "would 30 days at 53p a day bring the total to?",
        "options": [
            {"text": "£46.14", "correct": True},
            {"text": "£30.77", "correct": False,
             "why": "That adds one day of standing charge where thirty are "
                    "owed."},
            {"text": "£15.90", "correct": False,
             "why": "That is the standing charge on its own, with the energy "
                    "charge dropped."},
            {"text": "£108.00", "correct": False,
             "why": "That is the number of units read as pounds rather than "
                    "priced at 28p."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h19",
        "band": "harder",
        "text": "VAT on domestic energy is 5 per cent. A gas account of £200 "
                "has yet to have it added. What will the customer pay?",
        "options": [
            {"text": "£205", "correct": False,
             "why": "That adds £5 rather than 5 per cent of £200, which is "
                    "£10."},
            {"text": "£240", "correct": False,
             "why": "That applies the 20 per cent standard rate instead of the "
                    "domestic one."},
            {"text": "£210", "correct": True},
            {"text": "£190", "correct": False,
             "why": "That takes the tax off the bill instead of adding it "
                    "on."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h20",
        "band": "harder",
        "text": "A home uses 380 units in November and 610 in January on the "
                "same 26p tariff. How much more is the energy charge, and does "
                "the standing charge explain any of it?",
        "options": [
            {"text": "£59.80 more, and the standing charge explains none of "
                     "it", "correct": True},
            {"text": "£59.80 more, and the standing charge explains most of "
                     "it",
             "correct": False,
             "why": "The standing charge is the same daily amount in both "
                    "months, so it cannot produce a difference."},
            {"text": "£230 more, which is the difference in units",
             "correct": False,
             "why": "230 is the number of extra units; the price has still to "
                    "be applied to it."},
            {"text": "£158.60 more, which is January's whole charge",
             "correct": False,
             "why": "That is January's charge in full rather than the "
                    "increase over November."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h21",
        "band": "harder",
        "text": "Four different appliances each use exactly one unit. What "
                "must be true of all four?",
        "options": [
            {"text": "They all draw the same power while they are running",
             "correct": False,
             "why": "A 1 kW heater and a 9 W lamp can both reach a unit; the "
                    "rate need not match."},
            {"text": "They all ran for the same length of time",
             "correct": False,
             "why": "One can take an hour and another nearly five days, and "
                    "both reach a unit."},
            {"text": "Each one's power multiplied by its time comes to the "
                     "same", "correct": True},
            {"text": "They all cost different amounts, because their ratings "
                     "differ",
             "correct": False,
             "why": "One unit is one unit, so all four cost the same on a "
                    "given tariff."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h22",
        "band": "harder",
        "text": "A meter is misread as 05 006 when it truly reads 05 060. At "
                "27p a unit, how wrong is the bill?",
        "options": [
            {"text": "£14.58 too little", "correct": True},
            {"text": "£14.58 too much", "correct": False,
             "why": "The misreading is the lower figure, so the bill charges "
                    "for fewer units than were used."},
            {"text": "£54.00 too little", "correct": False,
             "why": "54 is the number of missed units; the price has still to "
                    "be applied."},
            {"text": "£1351.62 too little", "correct": False,
             "why": "That prices a whole meter reading rather than the "
                    "difference between two."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h23",
        "band": "harder",
        "text": "Two households pay identical totals, but one used 500 units "
                "and the other 200. What must differ?",
        "options": [
            {"text": "The meters, one of which must be counting wrongly",
             "correct": False,
             "why": "Two correct meters can easily give these readings; the "
                    "bills match because the tariffs differ."},
            {"text": "Nothing — a bill does not depend on how much is used",
             "correct": False,
             "why": "The energy charge depends on it entirely; that is what a "
                    "unit price is for."},
            {"text": "The number of days each bill covers",
             "correct": False,
             "why": "Days would change the standing charge a little, nowhere "
                    "near enough to cover 300 units."},
            {"text": "Their tariffs — a different unit price or standing "
                     "charge", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h24",
        "band": "harder",
        "text": "A 3 kW immersion heater is on a timer for 90 minutes a day. "
                "At 27p a unit, what does a 30-day month cost?",
        "options": [
            {"text": "£36.45", "correct": True},
            {"text": "£2187.00", "correct": False,
             "why": "That uses 90 as hours rather than minutes, so it charges "
                    "for sixty times too long."},
            {"text": "£1.22", "correct": False,
             "why": "That is one day's cost, and the month holds thirty of "
                    "them."},
            {"text": "£24.30", "correct": False,
             "why": "That uses one hour a day rather than an hour and a "
                    "half."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h25",
        "band": "harder",
        "text": "Gas is billed in kilowatt-hours and so is electricity. Why "
                "does that matter to a household?",
        "options": [
            {"text": "Because it means the two fuels are taxed at the same "
                     "rate as each other",
             "correct": False,
             "why": "Both are taxed at 5 per cent, but that follows from the "
                    "rules rather than from the unit."},
            {"text": "Because the two halves of the bill can be compared "
                     "directly", "correct": True},
            {"text": "Because a single meter can then record both fuels at "
                     "once",
             "correct": False,
             "why": "Each fuel keeps its own meter, and one of them counts "
                    "volume rather than energy."},
            {"text": "Because it means a kilowatt-hour of gas costs the same "
                     "as one of electricity",
             "correct": False,
             "why": "The prices differ by about four times, which is exactly "
                    "what the shared unit reveals."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h26",
        "band": "harder",
        "text": "One tariff is 30p a unit with no standing charge; another is "
                "24p with 55p a day. Which suits a heavy user, and from about "
                "what daily use?",
        "options": [
            {"text": "The first, because paying nothing each day is always "
                     "the better deal",
             "correct": False,
             "why": "It is better for a light user; the 6p saved on every unit "
                    "overtakes 55p once enough units are bought."},
            {"text": "The second, from about 9 units a day", "correct": True},
            {"text": "The second, from about 2 units a day", "correct": False,
             "why": "Two units save only 12p a day, which does not cover the "
                    "55p standing charge."},
            {"text": "The first, because the second costs 55p even on a day "
                     "with no usage",
             "correct": False,
             "why": "That is true and does not settle it: a heavy user buys "
                    "enough units to more than repay the 55p."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h27",
        "band": "harder",
        "text": "At 53p a day, how much more standing charge does a 31-day "
                "month carry than a 28-day one?",
        "options": [
            {"text": "£16.43", "correct": False,
             "why": "That is the whole 31 days rather than the three extra "
                    "ones."},
            {"text": "£1.59", "correct": True},
            {"text": "53p, because only the extra days matter",
             "correct": False,
             "why": "There are three extra days, so it is three times 53p."},
            {"text": "£3.00", "correct": False,
             "why": "That charges a pound a day, where the rate is 53p."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h28",
        "band": "harder",
        "text": "A year's bill covers 3200 units priced at 27p, plus 365 days "
                "of standing charge at 53p. Work out the total.",
        "options": [
            {"text": "£864.00", "correct": False,
             "why": "That is the energy charge alone, with a year of standing "
                    "charge left out."},
            {"text": "£193.45", "correct": False,
             "why": "That is the standing charge alone, with the 3200 units "
                    "left out."},
            {"text": "£1057.45", "correct": True},
            {"text": "£3200.53", "correct": False,
             "why": "That reads the units as pounds and adds a single day's "
                    "standing charge."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h29",
        "band": "harder",
        "text": "A supplier offers 5 per cent off units only. On a bill of "
                "£108 of units and £15.90 of standing charge, what is saved?",
        "options": [
            {"text": "£6.20",
             "correct": False,
             "why": "The offer names the units only, so the standing charge is "
                    "not part of the discount."},
            {"text": "£5.40", "correct": True},
            {"text": "£0.80",
             "correct": False,
             "why": "It is the units that are discounted, and they are the "
                    "larger figure by far."},
            {"text": "£54.00",
             "correct": False,
             "why": "A twentieth of £108 is £5.40; £54 would be half of it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-04-h30",
        "band": "harder",
        "text": "Two households on one tariff own the same appliances yet get "
                "very different bills. What explains it?",
        "options": [
            {"text": "One meter must be faulty, because identical appliances "
                     "give identical bills",
             "correct": False,
             "why": "Owning an appliance is not using it; the meters can both "
                    "be perfectly accurate."},
            {"text": "One household must be charged a higher price for each "
                     "unit it uses",
             "correct": False,
             "why": "They are on one tariff, so the price per unit is the "
                    "same for both."},
            {"text": "One household runs its appliances for far longer",
             "correct": True},
            {"text": "One household must have a larger standing charge on its "
                     "account",
             "correct": False,
             "why": "The standing charge comes with the tariff, and they "
                    "share one."},
        ],
        "figure": None,
    },
]
