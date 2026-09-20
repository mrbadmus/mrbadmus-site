"""Physics · Electricity — the MRB-338 expansion of `electrical-charge-current`.

The weight falls on Q = I × t and its two rearrangements, because that is what
this spec point asks a pupil to DO, and the errors it punishes are almost all
errors of time: minutes, hours and milliseconds left unconverted. Around that
calculating core sit the ideas the arithmetic rests on — one ampere is one
coulomb per second, charge carriers are free electrons in a metal and ions in a
solution, charge is conserved so it is never used up and never piles up at a
junction, and a break anywhere in a loop stops the current everywhere in it.
Proportional reasoning ("predict", "compare") carries the points that would
otherwise only ever be met as another substitution.
"""

TOPIC = "electricity"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-electrical-charge-current-e05",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wire carries a steady current of 3.0 A. State the charge "
                "that passes a point in the wire each second.",
        "options": [
            "3.0 C",
            "180 C",
            "0.33 C",
            "1.0 C",
        ],
        "correct_index": 0,
        "why": "One ampere means one coulomb passes a point every second, so a "
               "current of 3.0 A carries 3.0 C past that point each second.",
    },
    {
        "id": "ks4-electrical-charge-current-e06",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which particles carry the charge when a current passes "
                "through a copper sulfate solution.",
        "options": [
            "Free electrons, which leave the metal electrodes and cross the "
            "liquid",
            "Ions, which are free to move through the solution",
            "Protons released from the positive electrode",
            "Neutral atoms drifting towards the negative electrode",
        ],
        "correct_index": 1,
        "why": "In a solution the charge carriers are ions, which are free to "
               "move through the liquid; free electrons carry the charge in a "
               "metal.",
    },
    {
        "id": "ks4-electrical-charge-current-e07",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp carries a current of 0.25 A for 40 s. Calculate the "
                "charge that flows through the lamp.",
        "options": [
            "160 C",
            "0.0063 C",
            "10 C",
            "600 C",
        ],
        "correct_index": 2,
        "why": "Q = I × t = 0.25 × 40 = 10 C, with the time already in "
               "seconds.",
    },
    {
        "id": "ks4-electrical-charge-current-e08",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hairdryer carries a current of 5.0 A. Calculate the charge "
                "that passes through it in 2.0 minutes.",
        "options": [
            "10 C",
            "24 C",
            "36000 C",
            "600 C",
        ],
        "correct_index": 3,
        "why": "2.0 minutes is 120 s, so Q = I × t = 5.0 × 120 = 600 C.",
    },
    {
        "id": "ks4-electrical-charge-current-e09",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of the quantity found when a current in "
                "amperes is multiplied by a time in seconds.",
        "options": [
            "The coulomb",
            "The ampere",
            "The volt",
            "The watt",
        ],
        "correct_index": 0,
        "why": "Q = I × t, so an ampere multiplied by a second gives a "
               "coulomb, the unit of charge.",
    },
    {
        "id": "ks4-electrical-charge-current-e10",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how an ammeter must be connected in order to measure "
                "the current in a lamp.",
        "options": [
            "In parallel with the lamp, in the same way that a voltmeter is "
            "connected across it",
            "In series with the lamp, so that the same charge passes through "
            "both",
            "In parallel with the cell, so that it registers the whole supply "
            "current",
            "In series with a second ammeter, so that the two readings can be "
            "added",
        ],
        "correct_index": 1,
        "why": "An ammeter goes in series, so that all the charge passing "
               "through the lamp also passes through the meter.",
    },
    {
        "id": "ks4-electrical-charge-current-e11",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single loop contains a cell and two lamps. One lamp is "
                "unscrewed from its holder. State the current in the wire on "
                "the far side of the loop.",
        "options": [
            "Unchanged, because the second lamp is still working normally",
            "Half its earlier value, since one lamp has gone",
            "Zero, because the loop is no longer a complete path",
            "Larger, because the total resistance has fallen",
        ],
        "correct_index": 2,
        "why": "Breaking the loop leaves no complete conducting path, so the "
               "current falls to zero right round the circuit, not only at "
               "the gap.",
    },
    {
        "id": "ks4-electrical-charge-current-e12",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to the charge that passes through a "
                "component in a fixed time if the current is doubled.",
        "options": [
            "It halves, because a larger current empties the cell faster",
            "It is four times larger, because both quantities increase",
            "It stays the same, because the time has not been changed",
            "It doubles, because charge is current multiplied by time",
        ],
        "correct_index": 3,
        "why": "Q = I × t, so with the time fixed, doubling the current "
               "doubles the charge that passes.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-electrical-charge-current-s05",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A torch bulb allows 54 C of charge to pass in 3.0 minutes. "
                "Calculate the current in the bulb.",
        "options": [
            "0.30 A",
            "18 A",
            "162 A",
            "0.015 A",
        ],
        "correct_index": 0,
        "why": "3.0 minutes is 180 s, so I = Q ÷ t = 54 ÷ 180 = 0.30 A.",
    },
    {
        "id": "ks4-electrical-charge-current-s06",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A battery delivers 96 C of charge at a steady current of "
                "0.80 A. Determine the time for which it supplies the charge.",
        "options": [
            "77 s",
            "120 s",
            "1.2 s",
            "0.0083 s",
        ],
        "correct_index": 1,
        "why": "Rearranging gives t = Q ÷ I = 96 ÷ 0.80 = 120 s.",
    },
    {
        "id": "ks4-electrical-charge-current-s07",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A small motor in a model draws 250 mA for 1.0 minute. "
                "Calculate the charge that passes through the motor.",
        "options": [
            "250 C",
            "15000 C",
            "15 C",
            "4.2 C",
        ],
        "correct_index": 2,
        "why": "250 mA is 0.25 A and 1.0 minute is 60 s, so Q = 0.25 × 60 = "
               "15 C.",
    },
    {
        "id": "ks4-electrical-charge-current-s08",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kettle carries a current of 9.0 A and a lamp carries a "
                "current of 0.45 A. Both are switched on for the same length "
                "of time. Compare the charge that passes through each.",
        "options": [
            "The same charge passes through both, since both run for the same "
            "time",
            "Twenty times as much passes through the lamp as through the "
            "kettle",
            "About four times as much passes through the kettle as the lamp",
            "Twenty times as much passes through the kettle as the lamp",
        ],
        "correct_index": 3,
        "why": "Q = I × t, so for equal times the charges are in the ratio of "
               "the currents: 9.0 ÷ 0.45 = 20.",
    },
    {
        "id": "ks4-electrical-charge-current-s09",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that the lamp nearest the positive terminal "
                "of a cell in a series circuit glows more brightly because it "
                "receives the charge first. Explain why the student is wrong.",
        "options": [
            "Charge is not used up, so the same current passes through both "
            "lamps",
            "The first lamp does draw a little more current, but the "
            "difference is too small to see",
            "The current is shared out equally, so each lamp receives exactly "
            "half of it",
            "Charge leaves both terminals at once, so the two flows meet "
            "inside the lamps",
        ],
        "correct_index": 0,
        "why": "Charge is conserved in a single loop, so the same number of "
               "coulombs pass through each lamp every second and neither is "
               "reached first.",
    },
    {
        "id": "ks4-electrical-charge-current-s10",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a parallel circuit, 0.80 A arrives at a junction where "
                "the wire divides into two branches. One branch carries "
                "0.45 A. Determine the current in the other branch.",
        "options": [
            "1.25 A",
            "0.35 A",
            "0.80 A",
            "0.45 A",
        ],
        "correct_index": 1,
        "why": "The branch currents add to the current arriving at the "
               "junction, so the other branch carries 0.80 − 0.45 = 0.35 A.",
    },
    {
        "id": "ks4-electrical-charge-current-s11",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a practical, a student joins two lamps in a single loop "
                "with a cell and places an ammeter at four different points "
                "in turn. State what the four readings should show.",
        "options": [
            "The readings should fall steadily as the meter is moved round "
            "the loop",
            "The readings should be largest right beside the cell and "
            "smallest beyond the lamps",
            "All four readings should be the same, to within the precision "
            "of the meter",
            "The four readings should add up to the current measured beside "
            "the cell",
        ],
        "correct_index": 2,
        "why": "There is one path only, so the same charge passes every point "
               "each second and all four readings agree within the "
               "uncertainty of the meter.",
    },
    {
        "id": "ks4-electrical-charge-current-s12",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student connects an ammeter across a lamp instead of in "
                "series with it. Explain the effect this has on the circuit.",
        "options": [
            "The ammeter reads the lamp current correctly, but as a negative "
            "value",
            "The ammeter reads zero, since charge cannot enter a meter joined "
            "this way",
            "The ammeter reads half the current, as the charge divides "
            "between paths",
            "The meter has a very low resistance, so the charge bypasses the "
            "lamp through it",
        ],
        "correct_index": 3,
        "why": "An ammeter is built with a very low resistance, so joined "
               "across the lamp it offers an easy path that misses the lamp "
               "and the lamp goes out.",
    },
    {
        "id": "ks4-electrical-charge-current-s13",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why conventional current is taken to run from the "
                "positive terminal to the negative terminal, even though "
                "electrons in a metal travel the other way.",
        "options": [
            "The direction was agreed before electrons were discovered and "
            "has been kept",
            "Positive charges also travel through the metal with the "
            "electrons",
            "Current has no direction of its own, so either arrow will do",
            "Electrons move positive to negative in the cell, so the arrows "
            "agree",
        ],
        "correct_index": 0,
        "why": "Conventional current was defined as a flow from positive to "
               "negative long before the electron was discovered, and the "
               "convention has been kept ever since.",
    },
    {
        "id": "ks4-electrical-charge-current-s14",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of charge, why the currents in the "
                "branches of a parallel circuit add up to the current in the "
                "main wire.",
        "options": [
            "The cell sends a separate supply of charge into each branch at "
            "once",
            "Every coulomb arriving each second must leave along one branch "
            "or the other",
            "Charge is shared out equally at the junction, so each branch "
            "takes the same number of coulombs",
            "Each branch stores a little of the charge, and the rest returns "
            "to the cell",
        ],
        "correct_index": 1,
        "why": "Charge is conserved, so the coulombs reaching a junction each "
               "second must equal the coulombs leaving it along the branches "
               "each second.",
    },
    {
        "id": "ks4-electrical-charge-current-s15",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A camera flash passes a current of 4.0 A for 20 ms. "
                "Calculate the charge that flows during the flash.",
        "options": [
            "80 C",
            "0.20 C",
            "0.080 C",
            "5.0 C",
        ],
        "correct_index": 2,
        "why": "20 ms is 0.020 s, so Q = I × t = 4.0 × 0.020 = 0.080 C.",
    },
    {
        "id": "ks4-electrical-charge-current-s16",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student divides a charge in coulombs by a current in "
                "amperes and writes the answer in coulombs per ampere. State "
                "the usual name for this unit.",
        "options": [
            "The joule",
            "The volt",
            "The watt",
            "The second",
        ],
        "correct_index": 3,
        "why": "Rearranging Q = I × t gives t = Q ÷ I, so coulombs divided by "
               "amperes is a time in seconds.",
    },
    {
        "id": "ks4-electrical-charge-current-s17",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two separate single-loop circuits each run for 2.0 minutes. "
                "The first carries 0.80 A and the second carries 0.55 A. "
                "Calculate the difference between the charges that flow.",
        "options": [
            "30 C",
            "0.50 C",
            "162 C",
            "0.25 C",
        ],
        "correct_index": 0,
        "why": "In 120 s the circuits pass 0.80 × 120 = 96 C and 0.55 × 120 = "
               "66 C, a difference of 30 C.",
    },
    {
        "id": "ks4-electrical-charge-current-s18",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A phone charger supplies a steady current of 1.5 A for half "
                "an hour. Calculate the charge delivered.",
        "options": [
            "45 C",
            "2700 C",
            "0.75 C",
            "5400 C",
        ],
        "correct_index": 1,
        "why": "Half an hour is 1800 s, so Q = I × t = 1.5 × 1800 = 2700 C.",
    },
    {
        "id": "ks4-electrical-charge-current-s19",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electrolysis cell passes a current of 0.50 A. Determine "
                "the time, in minutes, for 300 C of charge to pass through "
                "it.",
        "options": [
            "600 minutes",
            "150 minutes",
            "10 minutes",
            "2.5 minutes",
        ],
        "correct_index": 2,
        "why": "t = Q ÷ I = 300 ÷ 0.50 = 600 s, and 600 ÷ 60 = 10 minutes.",
    },
    {
        "id": "ks4-electrical-charge-current-s20",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical lamps are connected in parallel across a cell "
                "and each carries 0.65 A. Calculate the charge that leaves "
                "the cell in 1.0 minute.",
        "options": [
            "39 C",
            "1.3 C",
            "4680 C",
            "78 C",
        ],
        "correct_index": 3,
        "why": "The branch currents add, so 1.3 A leaves the cell and Q = "
               "1.3 × 60 = 78 C.",
    },
    {
        "id": "ks4-electrical-charge-current-s21",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The time for which a steady current flows is tripled. "
                "Predict the effect on the charge that passes.",
        "options": [
            "The charge is three times as large, because charge is current "
            "times time",
            "The charge is unchanged, because the current has stayed at "
            "exactly the same value",
            "The charge is one third as large, as it is spread over a longer "
            "time",
            "The charge is nine times as large, because the current rises "
            "with time",
        ],
        "correct_index": 0,
        "why": "Q = I × t, so at a steady current tripling the time triples "
               "the charge that passes.",
    },
    {
        "id": "ks4-electrical-charge-current-s22",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fuse in one wire of a single-loop circuit melts while the "
                "lamp is lit. Explain what happens to the current in the rest "
                "of the loop.",
        "options": [
            "It carries on until the charge already in the wires is used up",
            "It falls to zero at once, because charge can no longer travel "
            "round the loop",
            "It falls to zero beyond the melted fuse, and is unchanged before "
            "it",
            "It rises sharply, because a melted fuse no longer resists the "
            "charge",
        ],
        "correct_index": 1,
        "why": "A melted fuse leaves a gap in the only path, so no charge can "
               "circulate and the current is zero everywhere in the loop.",
    },
    {
        "id": "ks4-electrical-charge-current-s23",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In 25 s, 9.0 C of charge passes through a red lamp. In 1.0 "
                "minute, 15 C passes through a green lamp. Determine which "
                "lamp carries the larger current.",
        "options": [
            "The green lamp, whose current works out at 0.60 A",
            "They carry equal currents, because both rates are the same",
            "The red lamp, at 0.36 A against the green lamp's 0.25 A",
            "The green lamp, because a larger charge passed through it",
        ],
        "correct_index": 2,
        "why": "I = Q ÷ t gives 9.0 ÷ 25 = 0.36 A for the red lamp and 15 ÷ "
               "60 = 0.25 A for the green one.",
    },
    {
        "id": "ks4-electrical-charge-current-s24",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell drives 1.5 C of charge round a circuit every 2.0 s. "
                "State the current in the circuit.",
        "options": [
            "1.3 A",
            "1.5 A",
            "0.75 C",
            "0.75 A",
        ],
        "correct_index": 3,
        "why": "A current of one ampere is one coulomb each second, so 1.5 C "
               "every 2.0 s is 1.5 ÷ 2.0 = 0.75 A.",
    },
    {
        "id": "ks4-electrical-charge-current-s25",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the way charge moves through a copper wire with the "
                "way it moves through a salt solution.",
        "options": [
            "Electrons drift through the wire, while ions move through the "
            "solution",
            "Ions drift through the wire, while electrons move through the "
            "solution",
            "Electrons carry the charge in both, but more slowly in the "
            "solution",
            "Protons carry it in the wire, and electrons carry it in the "
            "solution",
        ],
        "correct_index": 0,
        "why": "A metal conducts by the drift of free electrons through its "
               "lattice, while a solution conducts by the movement of "
               "positive and negative ions.",
    },
    {
        "id": "ks4-electrical-charge-current-s26",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates the charge through a heater by "
                "multiplying 3.0 A by 4.0 minutes and writes down 12 C. "
                "Explain the error.",
        "options": [
            "The current should have been divided by the time, not multiplied "
            "by it",
            "The time was not converted into seconds before the "
            "multiplication",
            "The current must be changed into milliamperes before it is used",
            "The charge should be added to the current rather than multiplied "
            "by it",
        ],
        "correct_index": 1,
        "why": "Q = I × t needs the time in seconds: 4.0 minutes is 240 s, so "
               "the charge is 3.0 × 240 = 720 C.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-electrical-charge-current-h05",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One coulomb of charge is carried by about 6.25 × 10¹⁸ "
                "electrons. A current of 0.50 A flows along a wire for 8.0 s. "
                "Estimate the number of electrons that pass a point in the "
                "wire.",
        "options": [
            "6.3 × 10¹⁸",
            "1.6 × 10¹⁸",
            "2.5 × 10¹⁹",
            "2.5 × 10²⁰",
        ],
        "correct_index": 2,
        "why": "Q = I × t = 0.50 × 8.0 = 4.0 C, and 4.0 × 6.25 × 10¹⁸ is "
               "2.5 × 10¹⁹ electrons.",
    },
    {
        "id": "ks4-electrical-charge-current-h06",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pump draws 2.4 A for 45 s and then 0.80 A for a further "
                "2.0 minutes. Calculate the total charge that passes through "
                "the pump.",
        "options": [
            "110 C",
            "528 C",
            "156 C",
            "204 C",
        ],
        "correct_index": 3,
        "why": "The two stages give 2.4 × 45 = 108 C and 0.80 × 120 = 96 C, "
               "and 108 + 96 = 204 C.",
    },
    {
        "id": "ks4-electrical-charge-current-h07",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sensor draws a steady current of 15 mA. Determine the "
                "time, in hours, for 108 C of charge to pass through it.",
        "options": [
            "2.0 hours",
            "7.2 hours",
            "120 hours",
            "7200 hours",
        ],
        "correct_index": 0,
        "why": "15 mA is 0.015 A, so t = Q ÷ I = 108 ÷ 0.015 = 7200 s, and "
               "7200 ÷ 3600 = 2.0 hours.",
    },
    {
        "id": "ks4-electrical-charge-current-h08",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A parallel circuit has three branches carrying 0.10 A, "
                "0.25 A and 0.45 A. Calculate the charge that passes through "
                "the cell in 50 s.",
        "options": [
            "22.5 C",
            "40 C",
            "0.80 C",
            "5.0 C",
        ],
        "correct_index": 1,
        "why": "The branch currents add to give 0.80 A from the cell, so Q = "
               "0.80 × 50 = 40 C.",
    },
    {
        "id": "ks4-electrical-charge-current-h09",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that because the same current flows into and "
                "out of a lamp, the lamp cannot be transferring any energy. "
                "Evaluate this statement.",
        "options": [
            "The student is right, because a lamp can transfer energy only if "
            "it uses up charge",
            "The student is wrong, because the current leaving a lit lamp is "
            "smaller than the current going in",
            "The charge is unchanged, but each coulomb leaves with less "
            "energy, so energy is transferred",
            "The student is right for a lamp in a single loop, but wrong for "
            "one in a parallel branch",
        ],
        "correct_index": 2,
        "why": "Charge is conserved, so the current is the same on both sides "
               "of the lamp; what falls is the energy carried by each "
               "coulomb.",
    },
    {
        "id": "ks4-electrical-charge-current-h10",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a required practical a student records 0.42 A, 0.41 A and "
                "0.42 A at three points in a single-loop circuit. Explain "
                "what the small differences show.",
        "options": [
            "They show the current falling slightly as each component in turn "
            "uses up some charge",
            "They show the ammeter was connected the wrong way round at one "
            "of the three points",
            "They show that a little of the charge leaks away into the wires "
            "that join the components together",
            "They are measurement uncertainty; the current is the same at "
            "every point in the loop",
        ],
        "correct_index": 3,
        "why": "One path means one current, so readings differing by 0.01 A "
               "differ only by the uncertainty of the meter.",
    },
    {
        "id": "ks4-electrical-charge-current-h11",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A toaster carries 4.0 A for 3.0 minutes and a phone charger "
                "carries 1.2 A for 15 minutes. Determine which passes the "
                "greater charge, and by how much.",
        "options": [
            "The charger, by 360 C",
            "The toaster, by 360 C",
            "The charger, by 6.0 C",
            "The charger, by 1800 C",
        ],
        "correct_index": 0,
        "why": "The toaster passes 4.0 × 180 = 720 C and the charger 1.2 × "
               "900 = 1080 C, so the charger passes 360 C more.",
    },
    {
        "id": "ks4-electrical-charge-current-h12",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A second identical lamp is added in parallel to a circuit "
                "that already contains one lamp and a cell. Predict the "
                "effect on the charge leaving the cell each second.",
        "options": [
            "It is unchanged, because the cell can supply only a fixed charge "
            "each second",
            "It doubles, because the second path draws the same current as "
            "the first one",
            "It halves, because the charge leaving the cell is now shared out "
            "between the two lamps",
            "It falls a little, because the extra lamp adds resistance to the "
            "circuit",
        ],
        "correct_index": 1,
        "why": "Each branch has the full supply potential difference across "
               "it, so the new lamp draws the same current as the original "
               "and twice the charge leaves the cell each second.",
    },
    {
        "id": "ks4-electrical-charge-current-h13",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same charge passes along two wires. It takes 25 s in the "
                "first wire and 5.0 s in the second. Compare the currents in "
                "the two wires.",
        "options": [
            "The second wire carries one fifth of the current of the first",
            "Both wires carry the same current, because the charge is equal",
            "The second wire carries five times the current of the first",
            "The second wire carries twenty times the current of the first",
        ],
        "correct_index": 2,
        "why": "I = Q ÷ t, so for the same charge a fifth of the time means "
               "five times the current.",
    },
    {
        "id": "ks4-electrical-charge-current-h14",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A welding machine passes 1800 C of charge in 1.5 minutes. "
                "Calculate the current.",
        "options": [
            "1200 A",
            "0.050 A",
            "2.0 A",
            "20 A",
        ],
        "correct_index": 3,
        "why": "1.5 minutes is 90 s, so I = Q ÷ t = 1800 ÷ 90 = 20 A.",
    },
    {
        "id": "ks4-electrical-charge-current-h15",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power bank stores 36000 C of charge. Compare how long it "
                "can supply 0.50 A with how long it can supply 2.0 A.",
        "options": [
            "20 hours at 0.50 A and 5.0 hours at 2.0 A",
            "5.0 hours at 0.50 A and 20 hours at 2.0 A",
            "20 hours at 0.50 A and 10 hours at 2.0 A",
            "The same time in both cases, since the stored charge is fixed",
        ],
        "correct_index": 0,
        "why": "t = Q ÷ I gives 36000 ÷ 0.50 = 72000 s, which is 20 hours, "
               "and 36000 ÷ 2.0 = 18000 s, which is 5.0 hours.",
    },
    {
        "id": "ks4-electrical-charge-current-h16",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a conducting solution, positive ions move one way and "
                "negative ions move the other. Explain how both movements "
                "contribute to the current.",
        "options": [
            "Only the positive ions count, since conventional current runs "
            "positive to negative",
            "Both movements carry charge past a point each second, so their "
            "contributions add together",
            "The two movements cancel out, so a solution carries less current "
            "than a metal wire",
            "Only the negative ions count, as they are the carriers of charge "
            "in a metal wire",
        ],
        "correct_index": 1,
        "why": "Positive charge moving one way and negative charge moving the "
               "other both move charge past a point in the same sense, so the "
               "two contributions add.",
    },
    {
        "id": "ks4-electrical-charge-current-h17",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp passes 66 C of charge in 2.0 minutes. Determine the "
                "charge it would pass in 5.0 minutes at the same current.",
        "options": [
            "330 C",
            "132 C",
            "165 C",
            "26 C",
        ],
        "correct_index": 2,
        "why": "I = 66 ÷ 120 = 0.55 A, so over 300 s the charge is 0.55 × 300 "
               "= 165 C.",
    },
    {
        "id": "ks4-electrical-charge-current-h18",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp lights the instant a switch is closed, even though "
                "the electrons in the wires drift very slowly. Explain why "
                "the lamp does not have to wait.",
        "options": [
            "The electrons from the cell travel at the speed of light to "
            "reach the lamp",
            "The cell fires a burst of new electrons into the wires, and they "
            "arrive there almost at once",
            "A current needs no moving charges, only the potential difference "
            "of the cell",
            "Charges are already present all round the circuit and all start "
            "to move together",
        ],
        "correct_index": 3,
        "why": "The wires already contain free electrons everywhere, so when "
               "the loop is completed they all begin to drift at once and "
               "charge passes through the lamp immediately.",
    },
    {
        "id": "ks4-electrical-charge-current-h19",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures 0.24 A in one branch of a parallel "
                "circuit, 0.18 A in the other and 0.38 A in the main wire. "
                "Suggest the most likely reason the readings do not agree.",
        "options": [
            "One of the readings is inaccurate, since the branch currents "
            "must add to the main current",
            "Some of the charge is used up inside the branches before it "
            "returns to the cell",
            "The main wire carries the least current, since its resistance "
            "is the lowest",
            "The branch currents should be multiplied rather than added to "
            "give the total",
        ],
        "correct_index": 0,
        "why": "Charge is conserved at a junction, so the branches should sum "
               "to 0.24 + 0.18 = 0.42 A in the main wire, and a reading of "
               "0.38 A points to a measurement error.",
    },
    {
        "id": "ks4-electrical-charge-current-h20",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A resistor passes 4.5 C of charge every 15 s. Calculate the "
                "total charge that passes through it in 4.0 minutes.",
        "options": [
            "18 C",
            "72 C",
            "1080 C",
            "4.5 C",
        ],
        "correct_index": 1,
        "why": "The current is 4.5 ÷ 15 = 0.30 A, so over 240 s the charge is "
               "0.30 × 240 = 72 C.",
    },
    {
        "id": "ks4-electrical-charge-current-h21",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two lamps joined one after another to a cell carry 0.24 A. "
                "With only one of the lamps connected to the same cell the "
                "current is 0.48 A. Compare the charge passing through the "
                "cell in 1.0 minute in the two cases.",
        "options": [
            "14.4 C with one lamp against 28.8 C with two",
            "14.4 C in both cases, because the cell is the same",
            "28.8 C with one lamp against 14.4 C with two",
            "28.8 C with one lamp against 7.2 C with two",
        ],
        "correct_index": 2,
        "why": "Q = I × t gives 0.48 × 60 = 28.8 C with the single lamp and "
               "0.24 × 60 = 14.4 C with the two lamps.",
    },
    {
        "id": "ks4-electrical-charge-current-h22",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A defibrillator delivers 0.15 C of charge in 2.0 ms. "
                "Calculate the current during the pulse.",
        "options": [
            "0.075 A",
            "7.5 A",
            "750 A",
            "75 A",
        ],
        "correct_index": 3,
        "why": "2.0 ms is 0.0020 s, so I = Q ÷ t = 0.15 ÷ 0.0020 = 75 A.",
    },
    {
        "id": "ks4-electrical-charge-current-h23",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A parallel circuit has two branches. The branch of smaller "
                "resistance carries 0.70 A and the other carries 0.25 A. "
                "Determine the reading of an ammeter placed in the wire "
                "returning to the cell.",
        "options": [
            "0.95 A",
            "0.70 A",
            "0.45 A",
            "0.35 A",
        ],
        "correct_index": 0,
        "why": "Every coulomb that leaves the cell returns to it, so the "
               "return wire carries the whole 0.70 + 0.25 = 0.95 A.",
    },
    {
        "id": "ks4-electrical-charge-current-h24",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is marked 1200 mA h, meaning it can supply 1200 mA "
                "for one hour. Determine the steady current it could supply "
                "for a full 6.0 hours.",
        "options": [
            "7.2 A",
            "0.20 A",
            "200 A",
            "0.020 A",
        ],
        "correct_index": 1,
        "why": "1200 mA is 1.2 A for one hour, so spread over 6.0 hours the "
               "steady current is 1.2 ÷ 6.0 = 0.20 A.",
    },
    {
        "id": "ks4-electrical-charge-current-h25",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the charge that passes through an electric fan "
                "drawing 0.36 A during a quarter of an hour.",
        "options": [
            "5.4 C",
            "1296 C",
            "324 C",
            "2500 C",
        ],
        "correct_index": 2,
        "why": "A quarter of an hour is 900 s, so Q = I × t = 0.36 × 900 = "
               "324 C.",
    },
    {
        "id": "ks4-electrical-charge-current-h26",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine passes 0.90 C of charge every second while it is "
                "running. Determine the current it draws and the total charge "
                "that passes during a 25-minute cycle.",
        "options": [
            "22.5 C at 0.90 A",
            "1350 C at 1.5 A",
            "54 C at 0.90 A",
            "1350 C at 0.90 A",
        ],
        "correct_index": 3,
        "why": "0.90 C each second is a current of 0.90 A, and over 25 × 60 = "
               "1500 s the charge is 0.90 × 1500 = 1350 C.",
    },
]
