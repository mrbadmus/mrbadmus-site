"""P8 lesson 05 — Resistance: twelve questions (MRB-223).

Written against Design's page. The spliced metre of nichrome, the
component under test, the four-times-over results table, the triangle and
both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · resistance is a RATIO and is never read off a component directly;
  · the division goes volts over amps, and the unit that leaves is the
    ohm (`CIRC-19`);
  · a resistor's ratio does not move and a filament lamp's does
    (`CIRC-18`) — the harder band sits here;
  · what makes a wire resist is its thinness and its length, not a push
    back against the current (`CIRC-17`).

⚠️ **NOTHING HERE CLAIMS THE LAMP'S RISE IS EVEN.** Mide's ruling of
21 Aug 2026: the linear model stays, and the page may say the resistance
RISES and may not say how steadily. Every question below names the two
ends and no rate.

⚠️ POSITION IS AUTHORED AND MEASURED —
2,3,0,1 · 1,0,3,2 · 0,2,2,0;
the twelve fall 4/2/4/2 across the four indices.

⚠️ Neither ladder rung is restated (4.5 V with 0.90 A, the lamp at 6.4 Ω
and 16.0 Ω), and neither are the figures in the worked examples (6.0 V
with 0.40 A, 3.0 V with 250 mA) or in the two attempts (the live bench,
and 4.5 V with 150 mA).
"""

UNIT = "P8"
LESSON = "resistance"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p8-05-e01",
        "band": "easier",
        "text": "Resistance is measured in…",
        "options": [
            {"text": "volts", "correct": False,
             "why": "Volts measure the p.d. across a component — one of the "
                    "two readings you divide."},
            {"text": "amperes", "correct": False,
             "why": "Amps measure the current through it — the other of the "
                    "two readings you divide."},
            {"text": "ohms", "correct": True},
            {"text": "newtons", "correct": False,
             "why": "Newtons measure force, and resistance is not a force at "
                    "all — it is a ratio."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e02",
        "band": "easier",
        "text": "To find a component's resistance you…",
        "options": [
            {"text": "read it off the component with an ohm-meter held "
                     "against it", "correct": False,
             "why": "There is no instrument that reads resistance off a "
                    "component the way a ruler reads a length."},
            {"text": "measure the current and multiply it by the p.d.",
             "correct": False,
             "why": "Multiplying gives the power in watts. Cover R on the "
                    "triangle and V sits over I."},
            {"text": "measure the p.d. and subtract the current",
             "correct": False,
             "why": "You cannot subtract amps from volts. Two different "
                    "quantities are divided, not taken away."},
            {"text": "measure the p.d. across it and the current through it, "
                     "and divide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e03",
        "band": "easier",
        "text": "One ohm is…",
        "options": [
            {"text": "one volt for each amp", "correct": True},
            {"text": "one amp for each volt", "correct": False,
             "why": "That is the ratio upside down, and it is the "
                    "commonest slip. Volts go on top."},
            {"text": "one volt taken away from one amp", "correct": False,
             "why": "Volts and amps are different quantities and cannot be "
                    "subtracted from each other."},
            {"text": "one joule for each coulomb", "correct": False,
             "why": "That is the definition of a VOLT, not of an ohm."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e04",
        "band": "easier",
        "text": "A voltmeter reads 2.0 V across a component and the ammeter "
                "reads 0.50 A. Its resistance is…",
        "options": [
            {"text": "1.0 Ω", "correct": False,
             "why": "That multiplies the two readings. Multiplying gives "
                    "watts."},
            {"text": "4.0 Ω", "correct": True},
            {"text": "0.25 Ω", "correct": False,
             "why": "That divides the current by the p.d. — the ratio the "
                    "wrong way up."},
            {"text": "2.5 Ω", "correct": False,
             "why": "That adds the two readings. Two different quantities "
                    "cannot be added."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p8-05-s01",
        "band": "standard",
        "text": "A 20 Ω resistor is tested at 2 V, then at 8 V. What happens "
                "to the resistance you calculate?",
        "options": [
            {"text": "It rises, because a bigger p.d. means more resistance",
             "correct": False,
             "why": "A bigger p.d. gives a bigger current too, and the "
                    "division comes back to the same answer."},
            {"text": "It stays at 20 Ω, because both readings grow together",
             "correct": True},
            {"text": "It falls to a quarter, because the current has "
                     "quadrupled", "correct": False,
             "why": "The current has quadrupled and so has the p.d. Both "
                    "sides of the division moved."},
            {"text": "It cannot be worked out at the second setting, because "
                     "the first answer is the resistor's real value",
             "correct": False,
             "why": "Every setting gives an answer, and for a resistor every "
                    "one gives the same answer."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s02",
        "band": "standard",
        "text": "Two wires are made of the same metal and are the same "
                "length. Wire A is thinner than wire B. Which resists more, "
                "and why?",
        "options": [
            {"text": "Wire A, because there are fewer routes through it for "
                     "the drifting electrons", "correct": True},
            {"text": "Wire B, because a thicker wire has more metal to get "
                     "through", "correct": False,
             "why": "More metal in the WIDTH is more room, not more "
                    "obstacle. More metal along the LENGTH would resist "
                    "more."},
            {"text": "Neither — thickness has no effect, only the metal "
                     "matters", "correct": False,
             "why": "The metal decides the resistance per unit of shape, and "
                    "the shape then decides the rest."},
            {"text": "Wire A, because a thin wire is longer than a thick one "
                     "for the same mass", "correct": False,
             "why": "The verdict is right and the reason is not: the two are "
                    "stated to be the same length. It is the width that "
                    "differs."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s03",
        "band": "standard",
        "text": "A filament lamp is tested at 3 V and then at 9 V. What "
                "happens to the resistance you calculate?",
        "options": [
            {"text": "It stays the same, because R = V ÷ I always gives one "
                     "answer for one component", "correct": False,
             "why": "R = V ÷ I always applies; what is not always true is "
                    "that the answer stays put. A lamp is the standard "
                    "counter-example."},
            # ⊕ MRB-297 · 1 Sep 2026 — the third option was widened so the
            # correct answer stops being resolvable as the second-longest.
            {"text": "It falls, because more p.d. drives more current, so "
                     "V ÷ I drops", "correct": False,
             "why": "More current would lower the ratio if the p.d. had not "
                    "risen too. It has, and by more — so V ÷ I goes up, not "
                    "down."},
            {"text": "It cannot be calculated for a lamp at all",
             "correct": False,
             "why": "It can, at every setting. Each answer is the lamp's "
                    "real resistance at that temperature."},
            {"text": "It rises, because the filament is hotter and hot metal "
                     "resists more", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s04",
        "band": "standard",
        "text": "A voltmeter reads 7.5 V and the ammeter reads 300 mA. The "
                "resistance is…",
        "options": [
            {"text": "0.025 Ω", "correct": False,
             "why": "That divides the current by the p.d. and forgets the "
                    "conversion. Two mistakes in one line."},
            {"text": "2250 Ω", "correct": False,
             "why": "That multiplies the two readings without converting. "
                    "Cover R on the triangle: V sits over I."},
            {"text": "25 Ω", "correct": True},
            {"text": "0.025 Ω — and the unit should be amps", "correct": False,
             "why": "Volts divided by amps leaves ohms, never amps, and the "
                    "division is the wrong way up as well."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p8-05-h01",
        "band": "harder",
        "text": "Why is Ohm's law stated as a special case rather than as an "
                "always-true rule?",
        "options": [
            {"text": "Because R = V ÷ I is a definition and always applies, "
                     "while the claim that R stays the same is extra and "
                     "some components refuse it", "correct": True},
            {"text": "Because Ohm's measurements were not accurate enough to "
                     "be a law", "correct": False,
             "why": "His measurements were fine, and his reputation caught "
                    "up with them. What limits the law is the physics of the "
                    "components, not his apparatus."},
            {"text": "Because it only works for metals, and a rule that "
                     "holds for one kind of material and not for the rest is "
                     "always stated as a special case rather than as a law",
             "correct": False,
             "why": "It works for a metal AT CONSTANT TEMPERATURE — the "
                    "qualifier is doing the work, and a metal filament that "
                    "heats up breaks it."},
            {"text": "Because resistance is measured in ohms rather than in "
                     "an SI base unit", "correct": False,
             "why": "The unit is not the issue. A thermistor and a diode "
                    "both refuse the law in ohms."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h02",
        "band": "harder",
        "text": "A kettle element and a lighting flex are made of similar "
                "metal and carry similar currents. Why must one resist much "
                "more than the other?",
        "options": [
            {"text": "The flex must resist more, so that the current it lets "
                     "through to the kettle is limited to a safe amount",
             "correct": False,
             "why": "That is the wrong way round. A cable that resisted "
                    "would waste energy heating itself, which is the danger."},
            {"text": "Neither has to — the resistance is decided only by "
                     "the metal, and the two of them are made of the same "
                     "metal",
             "correct": False,
             "why": "The metal sets the resistance per unit of shape. The "
                    "shape — long and thin against short and thick — is what "
                    "the manufacturer chooses."},
            {"text": "The element must resist more, because energy has to be "
                     "transferred to heat in it and almost none in the "
                     "cable", "correct": True},
            {"text": "The element must resist less, so that it can draw a "
                     "big enough current to get properly hot",
             "correct": False,
             "why": "A very low resistance draws a huge current and is a "
                    "short circuit. What makes an element hot is the energy "
                    "given up in it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h03",
        "band": "harder",
        "text": "A thermistor's resistance drops sharply as it warms. How "
                "does an oven use that to know its own temperature?",
        "options": [
            {"text": "The thermistor generates a voltage that rises with "
                     "temperature", "correct": False,
             "why": "It generates nothing. It is a resistance, and something "
                    "else has to drive a current through it."},
            {"text": "The oven measures how much heat the thermistor "
                     "absorbs", "correct": False,
             "why": "Nothing measures absorbed heat directly. The circuit "
                    "measures an electrical quantity."},
            {"text": "The circuit measures a resistance and reads the "
                     "temperature off it", "correct": True},
            {"text": "The thermistor melts at a set temperature and breaks "
                     "the circuit", "correct": False,
             "why": "That describes a fuse, and a fuse can only be used "
                    "once. A thermistor changes smoothly and reversibly."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h04",
        "band": "harder",
        "text": "Two students measure the same nichrome wire. One gets 8.0 Ω "
                "and the other 8.4 Ω. Which is the better first response?",
        "options": [
            {"text": "Take both readings again on the same setting, and "
                     "check the clips have not moved", "correct": True},
            {"text": "Average the two and record 8.2 Ω", "correct": False,
             "why": "Averaging hides the disagreement instead of finding "
                    "out where it came from. Repeat first."},
            {"text": "Keep the first and discard the second, because the "
                     "first was taken on a cooler wire", "correct": False,
             "why": "Nothing says which was taken first, and choosing by "
                    "preference is not a measurement decision."},
            {"text": "Conclude that nichrome does not obey R = V ÷ I",
             "correct": False,
             "why": "R = V ÷ I is a definition and cannot be disobeyed. A "
                    "5% spread between two students is ordinary "
                    "experimental scatter."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p8-05-e05",
        "band": "easier",
        "text": "Which two measurements does R = V ÷ I need?",
        "options": [
            {"text": "The p.d. across the component and the current through "
                     "it",
             "correct": True},
            {"text": "The p.d. across the battery and the current through the "
                     "battery",
             "correct": False,
             "why": "Those give the whole circuit's resistance, not the one "
                    "component's."},
            {"text": "The current through the component and the time it runs "
                     "for",
             "correct": False,
             "why": "Time appears nowhere in the definition of resistance."},
            {"text": "The p.d. across the component and its temperature",
             "correct": False,
             "why": "Temperature changes the answer for a filament, but it is "
                    "not one of the two measurements."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e06",
        "band": "easier",
        "text": "A component has 6.0 V across it and 2.0 A through it. What "
                "is its resistance?",
        "options": [
            {"text": "12 Ω", "correct": False,
             "why": "That is 6.0 × 2.0. Resistance is the p.d. DIVIDED by "
                    "the current."},
            {"text": "0.33 Ω", "correct": False,
             "why": "That is 2.0 ÷ 6.0, the ratio upside down."},
            {"text": "3.0 Ω", "correct": True},
            {"text": "8.0 Ω", "correct": False,
             "why": "That adds the two readings, and volts cannot be added to "
                    "amps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e07",
        "band": "easier",
        "text": "Why can a resistance not be read straight off a single "
                "meter?",
        "options": [
            {"text": "Because resistance changes too quickly to be read",
             "correct": False,
             "why": "A plain resistor holds steady; the reason is what "
                    "resistance IS."},
            {"text": "Because it is a ratio, so it takes two measurements and "
                     "a division",
             "correct": True},
            {"text": "Because ohms are too small a unit to display",
             "correct": False,
             "why": "Ohms display perfectly well; the difficulty is that two "
                    "readings are needed."},
            {"text": "Because a meter would change the resistance it was "
                     "measuring",
             "correct": False,
             "why": "Meters are built not to disturb the circuit; the point "
                    "is that resistance is defined as a ratio."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p8-05-s05",
        "band": "standard",
        "text": "A voltmeter reads 4.0 V across a component and the ammeter "
                "reads 0.25 A. What is its resistance?",
        "options": [
            {"text": "1.0 Ω", "correct": False,
             "why": "That is 4.0 × 0.25. The definition divides rather than "
                    "multiplies."},
            {"text": "0.0625 Ω", "correct": False,
             "why": "That is 0.25 ÷ 4.0, the ratio the wrong way up."},
            {"text": "16 Ω", "correct": True},
            {"text": "4.25 Ω", "correct": False,
             "why": "That adds the readings, and a p.d. cannot be added to a "
                    "current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s06",
        "band": "standard",
        "text": "A 12 Ω resistor carries 0.50 A. What is the p.d. across it?",
        "options": [
            {"text": "24 V", "correct": False,
             "why": "That is 12 ÷ 0.50. To find a p.d. you multiply the "
                    "resistance by the current."},
            {"text": "6.0 V", "correct": True},
            {"text": "12.5 V", "correct": False,
             "why": "That adds the two, and ohms cannot be added to amps."},
            {"text": "0.042 V", "correct": False,
             "why": "That is 0.50 ÷ 12, a division where a multiplication is "
                    "needed."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s07",
        "band": "standard",
        "text": "Two wires are the same metal and the same thickness, but one "
                "is twice as long. Which resists more?",
        "options": [
            {"text": "The shorter one, because the charge is more crowded",
             "correct": False,
             "why": "Crowding is not the issue; a longer path is harder to "
                    "get through, not an easier one."},
            {"text": "Neither — resistance depends only on the metal",
             "correct": False,
             "why": "The metal matters, and so do the length and the "
                    "thickness of the piece."},
            {"text": "The longer one, roughly twice as much", "correct": True},
            {"text": "The longer one, but only by a tiny amount",
             "correct": False,
             "why": "Doubling the length roughly doubles the resistance — "
                    "that is not a tiny change."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p8-05-h05",
        "band": "harder",
        "text": "A filament lamp gives 5 Ω when tested at 1 V and 20 Ω at "
                "12 V. Which statement is right?",
        "options": [
            {"text": "One reading must be a mistake, since a component has "
                     "one resistance",
             "correct": False,
             "why": "A filament genuinely has no single value; both readings "
                    "can be right."},
            {"text": "Both are right: the filament's resistance climbs as it "
                     "heats",
             "correct": True},
            {"text": "Both are right, but only because the ammeter drifts at "
                     "higher currents",
             "correct": False,
             "why": "The meters are steady. It is the filament itself that "
                    "changes."},
            {"text": "The 5 Ω figure is the true value and 20 Ω is the "
                     "distorted one",
             "correct": False,
             "why": "Neither is more true; each describes the lamp at the "
                    "temperature it was at."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h06",
        "band": "harder",
        "text": "A wire has 6.0 V across it and 400 mA through it. What is "
                "its resistance?",
        "options": [
            {"text": "0.015 Ω", "correct": False,
             "why": "That is 6.0 ÷ 400, using milliamps as if they were "
                    "amps."},
            {"text": "2400 Ω", "correct": False,
             "why": "That is 6.0 × 400, multiplying instead of dividing and "
                    "leaving the milliamps unconverted."},
            {"text": "15 Ω", "correct": True},
            {"text": "0.067 Ω", "correct": False,
             "why": "That is 0.400 ÷ 6.0, the ratio upside down."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h07",
        "band": "harder",
        "text": "A 3 Ω and a 6 Ω resistor sit in series on a 9 V battery. "
                "Which takes the larger share of the p.d., and how much?",
        "options": [
            {"text": "The 3 Ω one, with 6 V", "correct": False,
             "why": "The larger share goes to whatever resists more, and 6 Ω "
                    "is the larger of the two."},
            {"text": "They share it equally, 4.5 V each", "correct": False,
             "why": "Equal shares would need equal resistances, and these "
                    "differ by a factor of two."},
            {"text": "The 6 Ω one, with 6 V", "correct": True},
            {"text": "The 6 Ω one, with 9 V", "correct": False,
             "why": "That leaves nothing for the 3 Ω resistor, which must "
                    "take 3 V of the total."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · easier ────────────────────────────────────
    {
        "id": "p8-05-e08",
        "band": "easier",
        "text": "A component under test shows 5.0 V on the voltmeter and "
                "2.0 A on the ammeter. What does R = V ÷ I give for its "
                "resistance?",
        "options": [
            {"text": "10 Ω", "correct": False,
             "why": "That multiplies the two readings. R = V ÷ I means "
                    "dividing, not multiplying."},
            {"text": "0.40 Ω", "correct": False,
             "why": "That divides the current by the p.d. — the ratio is the "
                    "wrong way up."},
            {"text": "2.5 Ω", "correct": True},
            {"text": "7.0 Ω", "correct": False,
             "why": "That adds the two readings, and volts cannot be added to "
                    "amps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e09",
        "band": "easier",
        "text": "Testing a resistor gives readings of 9.0 V and 3.0 A on the "
                "two meters. What resistance does the division give?",
        "options": [
            {"text": "3.0 Ω", "correct": True},
            {"text": "27 Ω", "correct": False,
             "why": "That is 9.0 × 3.0. Resistance divides the p.d. by the "
                    "current; it does not multiply them."},
            {"text": "0.33 Ω", "correct": False,
             "why": "That is 3.0 ÷ 9.0, the ratio upside down."},
            {"text": "12 Ω", "correct": False,
             "why": "That adds the two readings, and a p.d. cannot be added "
                    "to a current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e10",
        "band": "easier",
        "text": "A lamp on test reads 4.0 V and 0.80 A. Its resistance works "
                "out at…",
        "options": [
            {"text": "3.2 Ω", "correct": False,
             "why": "That is 4.0 × 0.80. Dividing, not multiplying, gives the "
                    "resistance."},
            {"text": "5.0 Ω", "correct": True},
            {"text": "0.20 Ω", "correct": False,
             "why": "That divides the current by the p.d., which is the "
                    "ratio the wrong way up."},
            {"text": "4.8 Ω", "correct": False,
             "why": "That adds the readings, and volts cannot be added to "
                    "amps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e11",
        "band": "easier",
        "text": "Two meters on a component read 20 V and 4.0 A. Dividing the "
                "p.d. by the current gives…",
        "options": [
            {"text": "80 Ω", "correct": False,
             "why": "That multiplies the two readings instead of dividing "
                    "them."},
            {"text": "0.20 Ω", "correct": False,
             "why": "That divides the current by the p.d. — upside down."},
            {"text": "24 Ω", "correct": False,
             "why": "That adds the two readings, which cannot be done across "
                    "different quantities."},
            {"text": "5.0 Ω", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e12",
        "band": "easier",
        "text": "A component reads 14 V and 7.0 A on the two meters. What is "
                "its resistance?",
        "options": [
            {"text": "2.0 Ω", "correct": True},
            {"text": "98 Ω", "correct": False,
             "why": "That is 14 × 7.0. Resistance is the p.d. divided by the "
                    "current."},
            {"text": "0.50 Ω", "correct": False,
             "why": "That is 7.0 ÷ 14, the ratio upside down."},
            {"text": "21 Ω", "correct": False,
             "why": "That adds the two readings together."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e13",
        "band": "easier",
        "text": "A component of resistance 5 Ω has a current of 3.0 A flowing "
                "through it. What potential difference is needed to drive "
                "that current?",
        "options": [
            {"text": "0.60 V", "correct": False,
             "why": "That is 3.0 ÷ 5, which finds a current, not a p.d."},
            {"text": "15 V", "correct": True},
            {"text": "8.0 V", "correct": False,
             "why": "That adds the resistance and the current, which cannot "
                    "be added together."},
            {"text": "15 Ω", "correct": False,
             "why": "The number is right and the unit is wrong. Current "
                    "times resistance leaves volts, not ohms."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e14",
        "band": "easier",
        "text": "A component of resistance 20 Ω has a current of 0.25 A "
                "flowing through it. Calculate the potential difference "
                "across it.",
        "options": [
            {"text": "80 V", "correct": False,
             "why": "That is 20 ÷ 0.25, which is not how V = I × R works."},
            {"text": "5.0 V", "correct": True},
            {"text": "20.25 V", "correct": False,
             "why": "That adds the resistance and the current, which are "
                    "different quantities."},
            {"text": "5.0 A", "correct": False,
             "why": "The number is right and the unit is wrong: current "
                    "times resistance leaves volts."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e15",
        "band": "easier",
        "text": "A heater element of resistance 15 Ω carries a current of "
                "4.0 A. Find the potential difference needed to drive that "
                "current.",
        "options": [
            {"text": "60 V", "correct": True},
            {"text": "3.75 V", "correct": False,
             "why": "That is 15 ÷ 4.0, which is a resistance-style division, "
                    "not V = I × R."},
            {"text": "19 V", "correct": False,
             "why": "That adds the resistance and the current together."},
            {"text": "60 Ω", "correct": False,
             "why": "Current multiplied by resistance leaves volts, never "
                    "ohms."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e16",
        "band": "easier",
        "text": "A 10 Ω resistor is connected across a 5.0 V supply. What "
                "current flows through it?",
        "options": [
            {"text": "50 A", "correct": False,
             "why": "That multiplies the two figures. Current is found by "
                    "dividing the p.d. by the resistance."},
            {"text": "0.50 A", "correct": True},
            {"text": "2.0 A", "correct": False,
             "why": "That divides the resistance by the p.d. — the ratio the "
                    "wrong way up."},
            {"text": "15 A", "correct": False,
             "why": "That adds the two figures, and volts cannot be added to "
                    "ohms."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e17",
        "band": "easier",
        "text": "A component of resistance 8.0 Ω is placed across a 2.0 V "
                "supply. What current flows through it?",
        "options": [
            {"text": "16 A", "correct": False,
             "why": "That multiplies the resistance by the p.d., rather than "
                    "dividing."},
            {"text": "4.0 A", "correct": False,
             "why": "That divides the resistance by the p.d. — upside down."},
            {"text": "0.25 A", "correct": True},
            {"text": "10 A", "correct": False,
             "why": "That adds the two figures together."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e18",
        "band": "easier",
        "text": "A 25 Ω resistor sits across a 5.0 V cell. Calculate the "
                "current it carries.",
        "options": [
            {"text": "0.20 A", "correct": True},
            {"text": "125 A", "correct": False,
             "why": "That is 25 × 5.0, multiplying rather than dividing."},
            {"text": "5.0 A", "correct": False,
             "why": "That divides the resistance by the p.d., the ratio "
                    "upside down."},
            {"text": "30 A", "correct": False,
             "why": "That adds the resistance and the p.d. together."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e19",
        "band": "easier",
        "text": "A wire is replaced with one of the same metal and thickness, "
                "but four times as long. Its resistance…",
        "options": [
            {"text": "falls to a quarter, because the charge has further to "
                     "spread out", "correct": False,
             "why": "Spreading is not the effect. A longer path is harder to "
                    "get through, which raises resistance rather than "
                    "lowering it."},
            {"text": "stays the same, because it is still the same metal",
             "correct": False,
             "why": "The metal fixes the resistance per unit of shape; four "
                    "times the length is four times the total."},
            {"text": "falls slightly, because a longer wire cools the "
                     "current down", "correct": False,
             "why": "A wire does not cool a current. Length affects "
                    "resistance directly, and it raises it."},
            {"text": "rises to four times as much", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e20",
        "band": "easier",
        "text": "Two wires of the same metal and the same length differ only "
                "in thickness. The thinner one…",
        "options": [
            {"text": "resists less, because it is lighter", "correct": False,
             "why": "Weight plays no part. A thinner wire gives the drifting "
                    "charges fewer routes through, which resists more, not "
                    "less."},
            {"text": "resists the same, because thickness makes no "
                     "difference", "correct": False,
             "why": "Thickness does matter — fewer routes through a thin "
                    "wire means more resistance."},
            {"text": "resists more", "correct": True},
            {"text": "resists more only if it is also longer", "correct": False,
             "why": "Thickness alone changes the resistance here; the two "
                    "wires are stated to be the same length."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e21",
        "band": "easier",
        "text": "Two wires have the same length and the same thickness but "
                "are made of different metals. What decides which resists "
                "more?",
        "options": [
            {"text": "Nothing — identical shapes always give identical "
                     "resistance", "correct": False,
             "why": "Different metals give different resistances even in "
                    "identical shapes; copper and nichrome are nowhere near "
                    "equal."},
            {"text": "Whichever wire is connected nearer the battery",
             "correct": False,
             "why": "Position in the circuit does not change a wire's own "
                    "resistance."},
            {"text": "The colour of the wire's coating", "correct": False,
             "why": "A coating is not part of the conducting metal and plays "
                    "no part in its resistance."},
            {"text": "The metal itself", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e22",
        "band": "easier",
        "text": "As a metal wire gets hotter, its resistance generally…",
        "options": [
            {"text": "falls, because heat frees up more electrons to carry "
                     "the charge", "correct": False,
             "why": "Heating a metal does not create more free electrons; it "
                    "makes the existing ones collide more, which raises "
                    "resistance."},
            {"text": "stays exactly the same, whatever the temperature",
             "correct": False,
             "why": "A metal's resistance does change with temperature — "
                    "that is why a filament glows differently hot and cold."},
            {"text": "rises", "correct": True},
            {"text": "falls, because hot metal expands and gives charge more "
                     "room", "correct": False,
             "why": "Expansion is not the mechanism. More vigorous atoms "
                    "cause more collisions, raising resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e23",
        "band": "easier",
        "text": "Which of these keeps the same resistance no matter what p.d. "
                "is put across it?",
        "options": [
            {"text": "A filament lamp", "correct": False,
             "why": "A lamp's filament heats up and its resistance climbs as "
                    "the p.d. rises."},
            {"text": "A plain resistor", "correct": True},
            {"text": "Both, equally", "correct": False,
             "why": "Only the resistor holds its value; the lamp's "
                    "resistance changes with temperature."},
            {"text": "Neither — every component's resistance changes with "
                     "the p.d.", "correct": False,
             "why": "A plain resistor is built to hold one value across a "
                    "wide range of settings."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e24",
        "band": "easier",
        "text": "A filament lamp is tested cold and then again once it is "
                "glowing brightly. What is true of its resistance?",
        "options": [
            {"text": "It is always higher once the lamp is glowing",
             "correct": True},
            {"text": "It is lower once the lamp is glowing", "correct": False,
             "why": "A hotter filament resists more, not less, so the value "
                    "rises rather than falls."},
            {"text": "It cannot change, because R = V ÷ I always gives the "
                     "same number for one component", "correct": False,
             "why": "R = V ÷ I is a definition that always applies; it does "
                    "not promise the answer stays fixed, and a lamp is the "
                    "standard case where it does not."},
            {"text": "It is exactly the same both times", "correct": False,
             "why": "The filament's temperature has changed, and its "
                    "resistance changes with it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e25",
        "band": "easier",
        "text": "A thermistor is a component whose resistance…",
        "options": [
            {"text": "stays fixed, whatever its temperature", "correct": False,
             "why": "A fixed resistance describes a plain resistor. A "
                    "thermistor's whole purpose is that its resistance "
                    "changes."},
            {"text": "rises sharply as it gets warmer", "correct": False,
             "why": "A typical thermistor works the other way round: warming "
                    "it lowers its resistance."},
            {"text": "only changes when light shines on it", "correct": False,
             "why": "Light is what changes a light-dependent resistor. A "
                    "thermistor responds to temperature."},
            {"text": "falls sharply as it gets warmer", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e26",
        "band": "easier",
        "text": "A light-dependent resistor (LDR) is a component whose "
                "resistance…",
        "options": [
            {"text": "rises as more light reaches it", "correct": False,
             "why": "An LDR works the other way: more light gives it a lower "
                    "resistance, which is what lets more current through in "
                    "bright conditions."},
            {"text": "is fixed, and only its brightness changes",
             "correct": False,
             "why": "An LDR does not glow — it is a sensor. What changes is "
                    "its resistance, not its own brightness."},
            {"text": "falls as more light reaches it", "correct": True},
            {"text": "changes only with temperature, not with light",
             "correct": False,
             "why": "Temperature affects a thermistor. Light is what an LDR "
                    "responds to."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e27",
        "band": "easier",
        "text": "A component has a resistance of 1 Ω. How much current does "
                "1 V across it drive?",
        "options": [
            {"text": "1 mA", "correct": False,
             "why": "One ohm is defined as one volt for each whole amp, not "
                    "each milliamp."},
            {"text": "1 A", "correct": True},
            {"text": "10 A", "correct": False,
             "why": "One ohm gives exactly one amp for one volt, not ten "
                    "times that."},
            {"text": "0.1 A", "correct": False,
             "why": "That is a tenth of an amp; one ohm gives a full amp for "
                    "each volt."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e28",
        "band": "easier",
        "text": "A component is described as having a \"low resistance\". In "
                "terms of push and flow, what does that mean?",
        "options": [
            {"text": "A small potential difference is enough to drive a "
                     "large current through it", "correct": True},
            {"text": "A large potential difference is needed to drive even a "
                     "small current through it", "correct": False,
             "why": "That describes a HIGH resistance, not a low one — "
                    "expensive in push for not much flow."},
            {"text": "It needs no potential difference at all to carry a "
                     "current", "correct": False,
             "why": "Every real component still needs some p.d. to drive a "
                    "current; a low resistance just needs less of it."},
            {"text": "It can only carry current in short bursts",
             "correct": False,
             "why": "Resistance says nothing about how long a current can "
                    "run for, only how much push is needed for a given "
                    "flow."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e29",
        "band": "easier",
        "text": "R = V ÷ I is best described as…",
        "options": [
            {"text": "an estimate that only works roughly", "correct": False,
             "why": "The division is exact, not an estimate; every "
                    "component gives a true answer to it."},
            {"text": "a rule that applies only to resistors", "correct": False,
             "why": "The division works for a lamp, a thermistor or anything "
                    "else — it is what changes about the ANSWER that differs "
                    "between them."},
            {"text": "a definition, true for every component", "correct": True},
            {"text": "a law that only some components choose to obey",
             "correct": False,
             "why": "As a DEFINITION it always applies. What is not "
                    "guaranteed is that the ANSWER stays fixed as the "
                    "settings change."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-e30",
        "band": "easier",
        "text": "A wire carrying a current that is too big for its resistance "
                "to cope with safely will mostly…",
        "options": [
            {"text": "cool down", "correct": False,
             "why": "Energy is transferred to heat wherever there is "
                    "resistance and a current; more current means more "
                    "heating, not less."},
            {"text": "lose its resistance completely", "correct": False,
             "why": "Heating changes a metal's resistance a little; it does "
                    "not remove it."},
            {"text": "stop carrying any current at all", "correct": False,
             "why": "The current keeps flowing — the danger is the heat it "
                    "produces in doing so, not that it stops."},
            {"text": "always heat up", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · standard ───────────────────────────────────
    {
        "id": "p8-05-s08",
        "band": "standard",
        "text": "A component is tested and the meters show 9.0 V and 450 mA. "
                "What is its resistance?",
        "options": [
            {"text": "20 Ω", "correct": True},
            {"text": "4050 Ω", "correct": False,
             "why": "That treats 450 as amps and multiplies instead of "
                    "dividing."},
            {"text": "0.050 Ω", "correct": False,
             "why": "That divides the current by the p.d. — the ratio "
                    "upside down."},
            {"text": "0.020 Ω", "correct": False,
             "why": "That divides 9.0 by 450 without converting the "
                    "milliamps to amps first."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s09",
        "band": "standard",
        "text": "Meters on a heating coil read 6.0 V and 250 mA. Calculate "
                "its resistance.",
        "options": [
            {"text": "1500 Ω", "correct": False,
             "why": "That treats 250 as amps and multiplies rather than "
                    "divides."},
            {"text": "24 Ω", "correct": True},
            {"text": "0.042 Ω", "correct": False,
             "why": "That divides the current by the p.d., upside down."},
            {"text": "0.024 Ω", "correct": False,
             "why": "That uses 250 as if it were already in amps, without "
                    "converting."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s10",
        "band": "standard",
        "text": "A component under test shows 12 V and 600 mA on the meters. "
                "What resistance does that give?",
        "options": [
            {"text": "7200 Ω", "correct": False,
             "why": "That multiplies 12 by 600 instead of converting and "
                    "dividing."},
            {"text": "0.050 Ω", "correct": False,
             "why": "That is the current divided by the p.d., the wrong way "
                    "up."},
            {"text": "20 Ω", "correct": True},
            {"text": "0.020 Ω", "correct": False,
             "why": "That divides 12 by 600 directly, without converting the "
                    "milliamps to amps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s11",
        "band": "standard",
        "text": "A 40 Ω resistor carries a current of 150 mA. What potential "
                "difference is across it?",
        "options": [
            {"text": "6000 V", "correct": False,
             "why": "That treats 150 as amps and multiplies without "
                    "converting."},
            {"text": "0.0038 V", "correct": False,
             "why": "That divides the current by the resistance instead of "
                    "multiplying."},
            {"text": "6.0 Ω", "correct": False,
             "why": "The number is right and the unit is wrong; current "
                    "times resistance leaves volts."},
            {"text": "6.0 V", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s12",
        "band": "standard",
        "text": "A 15 Ω resistor sits across a 6.0 V supply. What current "
                "flows, given in milliamps?",
        "options": [
            {"text": "400 mA", "correct": True},
            {"text": "0.4 mA", "correct": False,
             "why": "That is the correct current in amps, left unconverted "
                    "to milliamps."},
            {"text": "40 mA", "correct": False,
             "why": "That misplaces the decimal point; 0.4 A is 400 mA, not "
                    "40."},
            {"text": "90 mA", "correct": False,
             "why": "That comes from multiplying rather than dividing the "
                    "two figures."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s13",
        "band": "standard",
        "text": "A 25 Ω resistor is placed across a 2.5 V cell. What current "
                "flows, in milliamps?",
        "options": [
            {"text": "10 mA", "correct": False,
             "why": "That misplaces the decimal point; the true current is "
                    "ten times bigger."},
            {"text": "100 mA", "correct": True},
            {"text": "62.5 mA", "correct": False,
             "why": "That is 25 × 2.5, multiplying rather than dividing."},
            {"text": "0.1 mA", "correct": False,
             "why": "That is the correct current in amps, left unconverted "
                    "to milliamps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s14",
        "band": "standard",
        "text": "A component reads 3.0 V and 1.5 A on the two meters at one "
                "setting, then 6.0 V and 3.0 A at a second setting. What can "
                "you say about it?",
        "options": [
            {"text": "It is a filament lamp, because turning the supply up "
                     "increased both readings", "correct": False,
             "why": "Both readings rising together is exactly what a "
                    "CONSTANT ratio looks like; a lamp's ratio would change, "
                    "not just its readings."},
            {"text": "It cannot be identified from two readings alone",
             "correct": False,
             "why": "Two matching ratios from two very different settings is "
                    "real evidence of a constant resistance."},
            {"text": "It is a resistor: the ratio V ÷ I is 2.0 Ω both "
                     "times.", "correct": True},
            {"text": "It must be an insulator, because the readings are "
                     "small", "correct": False,
             "why": "Small readings here still give a sensible few-ohm "
                    "resistance — nothing like an insulator's range."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s15",
        "band": "standard",
        "text": "A filament lamp reads 2.0 V and 0.40 A at one setting, then "
                "8.0 V and 0.80 A at a higher setting. What has happened to "
                "its resistance?",
        "options": [
            {"text": "It has stayed at 5.0 Ω, because a lamp is still "
                     "governed by R = V ÷ I", "correct": False,
             "why": "R = V ÷ I always applies, but the ANSWER need not stay "
                    "fixed — and here it clearly has not."},
            {"text": "It has fallen, because the current only doubled while "
                     "the p.d. quadrupled", "correct": False,
             "why": "A bigger fraction on top (V) than on the bottom (I) "
                    "means the ratio has gone UP, not down."},
            {"text": "It cannot be found without knowing the length of the "
                     "filament", "correct": False,
             "why": "The two readings are enough on their own; R = V ÷ I "
                    "needs nothing else."},
            {"text": "It has risen, from 5.0 Ω to 10 Ω.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s16",
        "band": "standard",
        "text": "A technician needs a wire that carries a large current "
                "without heating up much. Should they choose a long thin "
                "wire or a short thick wire of the same metal, and why?",
        "options": [
            {"text": "A short thick wire, because both properties lower the "
                     "resistance and a lower resistance wastes less energy "
                     "as heat.", "correct": True},
            {"text": "A long thin wire, because length and thinness make it "
                     "carry more current more easily", "correct": False,
             "why": "Both length and thinness RAISE resistance; a wire like "
                    "that would waste more energy as heat, not less."},
            {"text": "Either — the metal is what decides the resistance, not "
                     "the shape", "correct": False,
             "why": "The metal sets the resistance per unit of shape, but "
                    "the shape itself is what a technician can still "
                    "choose."},
            {"text": "A long thin wire, because a bigger resistance is "
                     "needed to control a large current safely, and a "
                     "thinner wire is far easier to route around equipment",
             "correct": False,
             "why": "A bigger resistance means MORE heating for the same "
                    "current, which is the opposite of what is wanted here."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s17",
        "band": "standard",
        "text": "A fridge's thermostat uses a thermistor to control the "
                "temperature inside. As the fridge warms up slightly, what "
                "happens to the thermistor's resistance, and how does the "
                "circuit use that?",
        "options": [
            {"text": "Its resistance rises, and the circuit reads that as a "
                     "fall in temperature", "correct": False,
             "why": "A typical thermistor's resistance FALLS as it warms, "
                    "not rises — the direction is reversed here."},
            {"text": "Its resistance falls, and the circuit always reads "
                     "the smaller resistance as a rise in temperature.",
             "correct": True},
            {"text": "Its resistance stays the same; only the current "
                     "changes", "correct": False,
             "why": "A thermistor's whole purpose is that its resistance "
                    "itself changes with temperature."},
            {"text": "It produces its own small voltage that the circuit "
                     "reads directly", "correct": False,
             "why": "A thermistor does not generate a voltage; something "
                    "else in the circuit has to drive a current through it "
                    "for its resistance to be measured."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s18",
        "band": "standard",
        "text": "A torch bulb is tested and its two meters read 7.0 V and "
                "1.4 A. What is the resistance of the bulb at that setting?",
        "options": [
            {"text": "9.8 Ω", "correct": False,
             "why": "That is 7.0 × 1.4, multiplying instead of dividing."},
            {"text": "0.20 Ω", "correct": False,
             "why": "That is 1.4 ÷ 7.0, the ratio upside down."},
            {"text": "5.0 Ω", "correct": True},
            {"text": "8.4 Ω", "correct": False,
             "why": "That adds the two readings, and volts cannot be added "
                    "to amps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s19",
        "band": "standard",
        "text": "A 5 Ω and a 15 Ω resistor are connected in series across a "
                "20 V battery. What potential difference is across the 15 Ω "
                "resistor?",
        "options": [
            {"text": "5 V", "correct": False,
             "why": "That is the smaller resistor's share; the larger "
                    "resistance always takes the larger share of the p.d."},
            {"text": "10 V", "correct": False,
             "why": "Equal shares would need equal resistances, and 15 Ω is "
                    "three times the 5 Ω one."},
            {"text": "20 V", "correct": False,
             "why": "That leaves nothing for the 5 Ω resistor, which must "
                    "take some of the total."},
            {"text": "15 V", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s20",
        "band": "standard",
        "text": "Heating elements are usually made from nichrome rather than "
                "copper, even though copper is the better conductor. Why?",
        "options": [
            {"text": "Nichrome's higher resistance means more energy is "
                     "transferred to heat in it for a similar current.",
             "correct": True},
            {"text": "Copper cannot be shaped into a coil", "correct": False,
             "why": "Copper is shaped into coils and springs all the time; "
                    "shape is not the obstacle."},
            {"text": "Nichrome is cheaper to manufacture than copper",
             "correct": False,
             "why": "Cost is not the reason given here; the choice is about "
                    "resistance and the heat it produces."},
            {"text": "Copper melts at a lower temperature than nichrome, so "
                     "it cannot be used at all", "correct": False,
             "why": "Melting point plays a part in some designs, but the "
                    "reason given here is about resistance and heating, not "
                    "melting."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s21",
        "band": "standard",
        "text": "A student records that a certain component's current "
                "DOUBLES every time the p.d. across it doubles, right across "
                "the range they test. What does that tell you about its "
                "resistance?",
        "options": [
            {"text": "Its resistance doubles every time the p.d. doubles",
             "correct": False,
             "why": "If resistance also doubled, the current would stay the "
                    "same rather than doubling with the p.d."},
            {"text": "Its resistance stays constant across that range.",
             "correct": True},
            {"text": "Its resistance halves every time the p.d. doubles",
             "correct": False,
             "why": "A halving resistance would make the current rise "
                    "faster than doubling; here it rises exactly in step, "
                    "which means the ratio has not moved."},
            {"text": "Nothing can be said about resistance from current and "
                     "p.d. alone", "correct": False,
             "why": "Current and p.d. are exactly the two quantities the "
                    "resistance is defined from."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s22",
        "band": "standard",
        "text": "A component of resistance 60 Ω is connected to a 9.0 V "
                "battery. Is the resulting current large enough to be "
                "measured on a normal school ammeter?",
        "options": [
            {"text": "No — the current is a few millionths of an amp, far "
                     "too small to read", "correct": False,
             "why": "150 mA is a sizeable, easily-read current; that "
                    "description fits an insulator's current, not this "
                    "component's."},
            {"text": "Yes — but only 15 mA, near the bottom of what a meter "
                     "can show", "correct": False,
             "why": "The correct current is ten times that: 150 mA, "
                    "comfortably inside a normal ammeter's range."},
            {"text": "Yes — 150 mA, well within a normal ammeter's range.",
             "correct": True},
            {"text": "No — a school ammeter cannot handle any current at all "
                     "above a few milliamps", "correct": False,
             "why": "School ammeters commonly read up to several amps; "
                    "150 mA is a modest current, not an overload."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s23",
        "band": "standard",
        "text": "A 4 Ω and a 6 Ω resistor are connected in series. What "
                "single resistor could replace the pair, without changing "
                "the current the battery drives?",
        "options": [
            {"text": "2 Ω", "correct": False,
             "why": "That is the difference between them, not their "
                    "combined effect in series."},
            {"text": "24 Ω", "correct": False,
             "why": "That multiplies the two values; resistors in series add "
                    "rather than multiply."},
            {"text": "5 Ω", "correct": False,
             "why": "That is their average, but resistors in series add "
                    "fully; they do not average."},
            {"text": "10 Ω", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s24",
        "band": "standard",
        "text": "A packet of resistors is printed \"100 Ω ± 5%\". A student "
                "measures one and gets 96 Ω. Does this mean the resistor "
                "breaks Ohm's law?",
        "options": [
            {"text": "No — the printed value always carries a manufacturing "
                     "tolerance, and 96 Ω is within 5% of 100 Ω.",
             "correct": True},
            {"text": "Yes — a true resistor must measure exactly the "
                     "printed value every time", "correct": False,
             "why": "Manufacturing gives every resistor a small, stated "
                    "tolerance; small differences from the printed value are "
                    "expected and normal."},
            {"text": "Yes — because Ohm's law says resistance must never "
                     "vary at all", "correct": False,
             "why": "Ohm's law concerns the ratio staying fixed as the p.d. "
                    "changes on ONE resistor, not that every resistor of a "
                    "type is identical to the ohm."},
            {"text": "No — because resistors never actually have the "
                     "resistance printed on them in the first place, only an "
                     "approximate colour code", "correct": False,
             "why": "The printed value is the resistor's intended "
                    "resistance; a real one sits close to it, within its "
                    "stated tolerance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s25",
        "band": "standard",
        "text": "A component's resistance drops from 20 Ω to 2 Ω because of "
                "a fault, while the supply stays the same. What happens to "
                "the current it draws?",
        "options": [
            {"text": "It falls to a tenth of what it was", "correct": False,
             "why": "A SMALLER resistance lets MORE current through for the "
                    "same p.d., not less."},
            {"text": "It rises to ten times what it was.", "correct": True},
            {"text": "It stays the same, because the supply has not "
                     "changed", "correct": False,
             "why": "The current depends on both the supply and the "
                    "resistance; with the resistance ten times smaller, the "
                    "current is ten times bigger."},
            {"text": "It becomes impossible to calculate without knowing the "
                     "new p.d.", "correct": False,
             "why": "The p.d. is stated to be unchanged, which is enough "
                    "information."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s26",
        "band": "standard",
        "text": "Two lamps are connected one at a time across the same "
                "battery. Lamp A has a lower resistance than Lamp B. Which "
                "draws the bigger current, and why?",
        "options": [
            {"text": "Lamp B, because a higher resistance pulls in more "
                     "current to compensate", "correct": False,
             "why": "A resistance does not \"pull in\" current; a higher "
                    "resistance restricts the current more, giving a SMALLER "
                    "one."},
            {"text": "Neither — both draw the same current from an "
                     "identical battery", "correct": False,
             "why": "The two lamps have different resistances, so the same "
                    "p.d. drives different currents through each."},
            {"text": "Lamp A, because a lower resistance lets more current "
                     "through for the same p.d.", "correct": True},
            {"text": "It depends on which lamp is connected first",
             "correct": False,
             "why": "Order does not matter here — each lamp is on the "
                    "battery on its own, and its own resistance decides its "
                    "own current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s27",
        "band": "standard",
        "text": "A component reads 0.60 V and 0.030 A on a low-voltage test "
                "rig. What is its resistance?",
        "options": [
            {"text": "0.018 Ω", "correct": False,
             "why": "That is 0.60 × 0.030, multiplying rather than "
                    "dividing."},
            {"text": "0.050 Ω", "correct": False,
             "why": "That is 0.030 ÷ 0.60, the ratio upside down."},
            {"text": "0.63 Ω", "correct": False,
             "why": "That adds the two readings, and volts cannot be added "
                    "to amps."},
            {"text": "20 Ω", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s28",
        "band": "standard",
        "text": "A 10 Ω resistor and a 40 Ω resistor are each tested at "
                "2.0 V and again at 8.0 V. What is true of the two ratios "
                "found for the 40 Ω resistor?",
        "options": [
            {"text": "Both readings give 40 Ω, because a resistor's ratio "
                     "does not change with the supply.", "correct": True},
            {"text": "The ratio is 40 Ω at 2.0 V and higher at 8.0 V, "
                     "because more p.d. means more resistance",
             "correct": False,
             "why": "A plain resistor's ratio does not climb with p.d. — "
                    "that behaviour belongs to a filament lamp, not a "
                    "resistor."},
            {"text": "The ratio falls at the higher p.d., because the "
                     "current has grown faster than the p.d.", "correct": False,
             "why": "For a resistor the current grows in exact step with the "
                    "p.d., so the ratio does not fall."},
            {"text": "The two readings cannot be compared, because they were "
                     "taken at different settings", "correct": False,
             "why": "Comparing the ratio at different settings is exactly "
                    "how you show a resistor's value is fixed."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s29",
        "band": "standard",
        "text": "A component draws a very large current from a given "
                "supply. What can you conclude about its resistance?",
        "options": [
            {"text": "It must be high, since more resistance is needed to "
                     "handle a big current safely", "correct": False,
             "why": "A HIGH resistance would restrict the current, giving a "
                    "SMALLER one for the same p.d., not a bigger one."},
            {"text": "It must be low, since a small resistance lets a large "
                     "current through for a given p.d.", "correct": True},
            {"text": "Nothing — current and resistance are unrelated",
             "correct": False,
             "why": "Current, p.d. and resistance are linked exactly by "
                    "R = V ÷ I; they are not unrelated."},
            {"text": "It depends only on the current, not on the p.d. used",
             "correct": False,
             "why": "The current by itself is not enough — a bigger current "
                    "only shows a lower resistance once you also know it was "
                    "on the SAME p.d."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-s30",
        "band": "standard",
        "text": "A 50 Ω resistor is connected across a 1.0 V cell. What "
                "current flows?",
        "options": [
            {"text": "0.02 mA", "correct": False,
             "why": "That is the correct current in amps, mislabelled as "
                    "milliamps rather than converted."},
            {"text": "2.0 mA", "correct": False,
             "why": "That misplaces the decimal point by a factor of ten."},
            {"text": "20 mA", "correct": True},
            {"text": "50 mA", "correct": False,
             "why": "That copies the resistance value rather than "
                    "calculating I = V ÷ R."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · harder ─────────────────────────────────────
    {
        "id": "p8-05-h08",
        "band": "harder",
        "text": "A wire's resistance is quoted as 15 Ω per metre. What "
                "current flows through a 40 cm length of it when 3.0 V is "
                "placed across that length?",
        "options": [
            {"text": "0.50 A", "correct": True},
            {"text": "0.20 A", "correct": False,
             "why": "That uses the resistance of a full metre, forgetting "
                    "the wire here is only 40 cm long."},
            {"text": "2.0 A", "correct": False,
             "why": "That correctly scales the resistance to 6 Ω for 40 cm, "
                    "but then divides the resistance by the p.d. instead of "
                    "the other way round."},
            {"text": "7.5 A", "correct": False,
             "why": "That scales the p.d. itself by the length fraction "
                    "instead of first finding the wire's actual resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h09",
        "band": "harder",
        "text": "A 6.0 Ω lamp and a 30 Ω resistor are connected one at a time "
                "to the same 12 V battery. How many times bigger is the "
                "current through the lamp than through the resistor?",
        "options": [
            {"text": "5 times bigger", "correct": True},
            {"text": "0.2 times as big", "correct": False,
             "why": "That compares the resistor's current to the lamp's, "
                    "the wrong way round."},
            {"text": "1.6 times bigger", "correct": False,
             "why": "That finds the DIFFERENCE between the two currents "
                    "(2.0 − 0.4 A) rather than how many times bigger one is "
                    "than the other."},
            {"text": "It cannot be compared without knowing the battery's "
                     "power rating", "correct": False,
             "why": "Current, p.d. and resistance are already enough to find "
                    "both currents directly; no extra rating is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h10",
        "band": "harder",
        "text": "A 9.0 V battery drives two resistors in series. The p.d. "
                "across the first is 6.0 V. If the first resistor is 12 Ω, "
                "what is the second?",
        "options": [
            {"text": "4.0 Ω", "correct": False,
             "why": "That uses the total 9.0 V to find the current instead "
                    "of the first resistor's own 6.0 V share."},
            {"text": "18 Ω", "correct": False,
             "why": "That uses the whole 9.0 V instead of the 3.0 V left "
                    "over for the second resistor."},
            {"text": "6.0 Ω", "correct": True},
            {"text": "12 Ω", "correct": False,
             "why": "That assumes the two resistors must be equal, but "
                    "nothing says so — the different p.d. shares rule that "
                    "out."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h11",
        "band": "harder",
        "text": "A street light's control circuit switches the light on once "
                "an LDR's resistance rises above a set value. Explain what "
                "triggers the light switching on.",
        "options": [
            {"text": "Rising light levels at dawn, because an LDR's "
                     "resistance rises as more light reaches it",
             "correct": False,
             "why": "An LDR's resistance FALLS as light increases; the "
                    "switching condition needs the resistance to RISE, which "
                    "happens as light falls, not rises."},
            {"text": "A rise in temperature as the day warms up",
             "correct": False,
             "why": "An LDR responds to light, not to temperature; that "
                    "description fits a thermistor instead."},
            {"text": "The LDR wearing out over time and permanently gaining "
                     "resistance", "correct": False,
             "why": "The LDR's resistance changes reversibly with light "
                    "every day; it is not a one-way wear effect."},
            {"text": "Falling light levels at dusk, because an LDR's "
                     "resistance rises as the light on it falls.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h12",
        "band": "harder",
        "text": "A resistor measures 2% away from its printed value; a lamp "
                "gives two very different resistances hot and cold. Are "
                "these two kinds of \"disagreement\" the same kind of thing?",
        "options": [
            {"text": "No — the resistor's small gap is manufacturing "
                     "tolerance around one true value, while the lamp's two "
                     "readings are both genuinely correct at their own "
                     "temperatures.", "correct": True},
            {"text": "Yes — both simply show that R = V ÷ I is not "
                     "reliable", "correct": False,
             "why": "R = V ÷ I is a definition and is reliable in both "
                    "cases; what differs is whether the TRUE value itself "
                    "has moved."},
            {"text": "Yes — both are measurement error that repeating the "
                     "test would remove", "correct": False,
             "why": "Repeating the lamp's test at the SAME p.d. would give "
                    "the same answer again; its two readings come from two "
                    "different temperatures, not from error."},
            {"text": "No — the resistor's value has genuinely changed, "
                     "while the lamp's has not, because a manufacturing "
                     "tolerance describes a fault made in production rather "
                     "than a real physical change happening afterwards",
             "correct": False,
             "why": "It is the other way round: the lamp's resistance "
                    "genuinely changes with temperature, while the resistor "
                    "is intended to hold one value within a small "
                    "tolerance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h13",
        "band": "harder",
        "text": "A component of resistance 300 Ω is designed to carry no "
                "more than 20 mA safely. What is the highest potential "
                "difference it should be run at?",
        "options": [
            {"text": "6000 V", "correct": False,
             "why": "That treats 20 mA as 20 A and multiplies without "
                    "converting."},
            {"text": "6.0 V", "correct": True},
            {"text": "0.067 V", "correct": False,
             "why": "That divides the milliamp figure by the resistance "
                    "instead of multiplying, and never converts to amps."},
            {"text": "320 V", "correct": False,
             "why": "That adds the resistance and the current together, "
                    "treating 20 as if it were in ohms too."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h14",
        "band": "harder",
        "text": "Long-distance power cables are made as thick as is "
                "practical, from a highly conducting metal. Why does keeping "
                "their resistance low matter over hundreds of kilometres?",
        "options": [
            {"text": "Because energy is wasted as heat in any resistance the "
                     "current passes through, and a very long cable already "
                     "has a lot of length to contribute.", "correct": True},
            {"text": "Because a high-resistance cable would carry no "
                     "current over such a distance", "correct": False,
             "why": "Some current would still flow; the concern is how much "
                    "energy is wasted as heat along the way, not that the "
                    "current would stop."},
            {"text": "Because thick cables are cheaper to manufacture than "
                     "thin ones", "correct": False,
             "why": "Thick cables use more metal and cost more; the choice "
                    "is driven by resistance and energy loss, not cost of "
                    "manufacture."},
            {"text": "Because resistance only matters for short wires in "
                     "circuits, not for long cables, since any long cable is "
                     "assumed to have next to no resistance by comparison "
                     "with its own length", "correct": False,
             "why": "The opposite is true: resistance's effect on wasted "
                    "heat grows directly with how long the wire is."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h15",
        "band": "harder",
        "text": "Three identical 4 Ω resistors are connected in series "
                "across a 24 V battery. What is the potential difference "
                "across each one?",
        "options": [
            {"text": "24 V", "correct": False,
             "why": "Only ONE component gets the whole p.d.; in series with "
                    "two others it shares a third of it."},
            {"text": "6.0 V", "correct": False,
             "why": "That is 24 ÷ 4, as if there were four equal shares "
                    "rather than three."},
            {"text": "4.0 V", "correct": False,
             "why": "That is 24 ÷ 6, as if there were six equal shares "
                    "rather than three."},
            {"text": "8.0 V", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h16",
        "band": "harder",
        "text": "An 8 Ω heating coil and a 12 Ω heating coil are wired one "
                "after the other across a 40 V bench supply. What current "
                "does the supply drive through them?",
        "options": [
            {"text": "5.0 A", "correct": False,
             "why": "That ignores the 12 Ω coil entirely; wired one after "
                    "the other, the two resistances add before you divide."},
            {"text": "2.0 A", "correct": True},
            {"text": "3.3 A", "correct": False,
             "why": "That ignores the 8 Ω coil; both resistances must be "
                    "added together first."},
            {"text": "0.50 A", "correct": False,
             "why": "That divides the resistance by the p.d. instead of the "
                    "p.d. by the resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h17",
        "band": "harder",
        "text": "A student measures a 100 Ω resistor five times at the same "
                "setting and gets 100, 99, 101, 100 and 137 Ω. What is the "
                "most sensible conclusion?",
        "options": [
            {"text": "The resistor's true value is 107.4 Ω, the mean of all "
                     "five readings", "correct": False,
             "why": "Averaging a clear outlier into the mean drags the "
                    "result away from the resistor's true, steady value "
                    "rather than towards it."},
            {"text": "The 137 Ω reading is likely a measurement slip and "
                     "should be taken again, not averaged in.",
             "correct": True},
            {"text": "The resistor does not obey R = V ÷ I, since its "
                     "readings vary", "correct": False,
             "why": "R = V ÷ I is a definition and every one of the five "
                    "readings is a value of it; small scatter around one "
                    "true value is ordinary experimental spread."},
            {"text": "The resistor's resistance is genuinely changing "
                     "between readings, like a filament lamp's",
             "correct": False,
             "why": "Four of the five readings agree closely, which is the "
                    "signature of one steady value and a single odd reading "
                    "— not a genuinely shifting resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h18",
        "band": "harder",
        "text": "A manufacturer doubles a wire's cross-sectional area "
                "(keeping the same metal and length) to reduce its "
                "resistance for a new product. Roughly what happens to the "
                "resistance?",
        "options": [
            {"text": "It stays the same, because only the metal and length "
                     "were changed", "correct": False,
             "why": "Cross-sectional area was changed too, and that does "
                    "affect resistance even though the metal and length did "
                    "not move."},
            {"text": "It rises, because there is more material for the "
                     "charge to pass through", "correct": False,
             "why": "More routes side by side make it EASIER to get "
                    "through, not harder — resistance falls with a bigger "
                    "cross-section."},
            {"text": "It falls, because a bigger cross-section gives the "
                     "charge more routes through.", "correct": True},
            {"text": "It doubles, because the wire now uses twice as much "
                     "metal", "correct": False,
             "why": "Using more metal in the WIDTH gives more room, which "
                    "lowers resistance; it does not raise or double it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h19",
        "band": "harder",
        "text": "A resistor is rated to keep a steady resistance \"at room "
                "temperature\". An engineer places it inside a hot engine "
                "bay instead. What should they expect?",
        "options": [
            {"text": "Nothing different — a resistor's value can never "
                     "change under any conditions, because R = V ÷ I is a "
                     "fixed definition that never varies", "correct": False,
             "why": "The steady-value claim comes with a temperature "
                    "condition; take it outside that condition and the "
                    "guarantee no longer applies."},
            {"text": "The resistor will stop obeying R = V ÷ I altogether",
             "correct": False,
             "why": "R = V ÷ I always applies, wherever the resistor sits; "
                    "what may change is the NUMBER the division gives, not "
                    "whether the definition works."},
            {"text": "The resistance will only change if the current is "
                     "also changed", "correct": False,
             "why": "Temperature alone can shift a resistor's value; the "
                    "current does not have to change for that to happen."},
            {"text": "The resistance may drift from its rated value, because "
                     "the \"constant resistance\" claim assumes room "
                     "temperature.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h20",
        "band": "harder",
        "text": "A component tested at 5.0 V draws 1.25 A. A safety rule for "
                "this circuit requires any component used to have a "
                "resistance of at least 3.0 Ω. Does this component meet the "
                "rule?",
        "options": [
            {"text": "Yes — its resistance is 4.0 Ω, which is above the "
                     "3.0 Ω limit.", "correct": True},
            {"text": "No — its resistance is 4.0 Ω, which is below the "
                     "3.0 Ω limit", "correct": False,
             "why": "4.0 Ω is ABOVE 3.0 Ω, not below it — the limit is met, "
                    "not missed."},
            {"text": "No — its resistance is 0.25 Ω, well below the limit",
             "correct": False,
             "why": "That divides the current by the p.d., the ratio the "
                    "wrong way up; the true resistance is 4.0 Ω."},
            {"text": "Yes — its resistance is 6.25 Ω, comfortably above the "
                     "limit", "correct": False,
             "why": "That multiplies the two readings instead of dividing "
                    "them; the true resistance is 4.0 Ω, still above the "
                    "limit but not that number."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h21",
        "band": "harder",
        "text": "Two identical 20 Ω resistors are connected in parallel "
                "across a 10 V battery. Is the resistance of the "
                "COMBINATION bigger, smaller, or the same as one resistor "
                "alone?",
        "options": [
            {"text": "Bigger — combining two resistors must add up their "
                     "resistances", "correct": False,
             "why": "Adding resistances is what happens in SERIES; in "
                    "parallel, extra paths make the combination easier to "
                    "get through, not harder."},
            {"text": "The same — parallel connections do not change the "
                     "total resistance, because adding a branch only gives "
                     "the current somewhere extra to go", "correct": False,
             "why": "Adding a second path genuinely gives the charge more "
                    "ways through, which lowers the combined resistance."},
            {"text": "Smaller — a parallel combination of resistors always "
                     "has a lower resistance than the smallest one on its "
                     "own.", "correct": True},
            {"text": "It depends on which resistor the current reaches "
                     "first", "correct": False,
             "why": "In parallel both resistors are reached by the current "
                    "at the same time via separate branches; order is not a "
                    "factor."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h22",
        "band": "harder",
        "text": "A battery is sometimes described as having its own small "
                "\"internal resistance\". What would that mean for a circuit "
                "connected to it?",
        "options": [
            {"text": "It means the battery's own casing conducts "
                     "electricity", "correct": False,
             "why": "The casing is not what is meant; internal resistance "
                    "describes something inside the cell's own chemistry and "
                    "structure, on the path the current already takes."},
            {"text": "Some of the battery's own p.d. is used up driving "
                     "current through the battery itself, so less is left "
                     "for the rest of the circuit.", "correct": True},
            {"text": "It means the battery can only be used with resistors "
                     "below a certain value", "correct": False,
             "why": "A battery can drive many different components; its "
                    "internal resistance is a property of the battery "
                    "itself, not a restriction on what may be connected."},
            {"text": "It means the battery stores less energy than a "
                     "battery with no internal resistance, because some of "
                     "that stored energy is used up inside the cell itself "
                     "before it ever reaches the circuit", "correct": False,
             "why": "Internal resistance affects how much of the p.d. "
                    "reaches the rest of the circuit, not directly how much "
                    "energy the battery stores."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h23",
        "band": "harder",
        "text": "Three components have resistances of 2 Ω, 200 Ω and "
                "2 000 000 Ω. Put them in order from the one that needs the "
                "smallest push for a useful current to the one that needs a "
                "push too large to ever safely arrange.",
        "options": [
            {"text": "2 000 000 Ω, then 200 Ω, then 2 Ω", "correct": False,
             "why": "That is the order reversed — the biggest resistance "
                    "needs the biggest push, not the smallest."},
            {"text": "200 Ω, then 2 Ω, then 2 000 000 Ω", "correct": False,
             "why": "2 Ω is the lowest resistance of the three and needs the "
                    "smallest push; it belongs first, not second."},
            {"text": "2 Ω, then 200 Ω, then 2 000 000 Ω.", "correct": True},
            {"text": "All three need the same push, since resistance does "
                     "not affect how big a p.d. is needed", "correct": False,
             "why": "Resistance is exactly what decides how big a push is "
                    "needed for a useful current; a bigger resistance "
                    "charges more volts for the same amp."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h24",
        "band": "harder",
        "text": "A filament lamp is tested at five p.d.s and gives "
                "resistances of 3, 7, 10, 12 and 13 Ω as the p.d. rises each "
                "time by the same amount. What does the size of each rise in "
                "resistance tell you?",
        "options": [
            {"text": "The lamp has stopped heating up after the third "
                     "reading", "correct": False,
             "why": "The resistance keeps climbing all the way to the fifth "
                    "reading, from 12 to 13 Ω — it has not stopped."},
            {"text": "The resistance is rising in exactly equal steps, so "
                     "the climb is perfectly even", "correct": False,
             "why": "The steps are 4, 3, 2 and 1 Ω — not equal — so the "
                    "climb is uneven, even though it is still an overall "
                    "rise."},
            {"text": "The resistance is still climbing overall, but each "
                     "equal step in p.d. adds a smaller amount of resistance "
                     "than the step before it.", "correct": True},
            {"text": "The lamp must be faulty, because a resistance should "
                     "either stay constant or rise by a fixed amount every "
                     "time", "correct": False,
             "why": "A filament lamp's resistance is not required to rise by "
                    "a fixed amount at all; only a plain resistor is "
                    "expected to hold one value."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h25",
        "band": "harder",
        "text": "An open break in a wire is sometimes described as having "
                "\"infinite\" resistance. In what sense is that description "
                "exact, and in what sense is it just a convenient label?",
        "options": [
            {"text": "It is exactly true: a gap of air has a genuinely "
                     "infinite resistance, full stop, because nothing can "
                     "ever conduct even the tiniest current across empty "
                     "space at any voltage whatsoever", "correct": False,
             "why": "Even a small air gap will pass a current at a high "
                    "enough p.d. — a spark can jump it — so its resistance, "
                    "while huge, is not truly infinite."},
            {"text": "It is a convenient label: no real gap has an infinite "
                     "resistance, but the current across it is so far below "
                     "anything measurable that treating it as infinite makes "
                     "no practical difference.", "correct": True},
            {"text": "It is neither true nor useful, and should never be "
                     "used", "correct": False,
             "why": "Treating the gap as if its resistance were infinite is "
                    "a fair simplification for ordinary circuit work, even "
                    "though it is not literally exact."},
            {"text": "It is exact because R = V ÷ I cannot be calculated "
                     "when the current is zero", "correct": False,
             "why": "The division breaks down at exactly zero current on "
                    "paper, but the physical gap still has some enormous, "
                    "non-infinite resistance underneath that."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h26",
        "band": "harder",
        "text": "A 3 Ω resistor and an unknown resistor are in series across "
                "a 15 V battery, and the current is measured as 1.5 A. What "
                "is the unknown resistor's value?",
        "options": [
            {"text": "10 Ω", "correct": False,
             "why": "That is the TOTAL resistance of the pair; the unknown "
                    "resistor is the total minus the 3 Ω already accounted "
                    "for."},
            {"text": "13 Ω", "correct": False,
             "why": "That adds the 3 Ω back on rather than taking it away "
                    "from the total."},
            {"text": "3.0 Ω", "correct": False,
             "why": "Nothing says the two resistors are equal; the total "
                    "resistance found from the current fixes the unknown one "
                    "uniquely."},
            {"text": "7.0 Ω", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h27",
        "band": "harder",
        "text": "Why is it meaningless to ask for the resistance of a "
                "component when no current is flowing through it at all?",
        "options": [
            {"text": "Because a component only has a resistance while it is "
                     "glowing or working", "correct": False,
             "why": "A component keeps its resistance whether or not current "
                    "happens to be flowing at that instant; the issue here "
                    "is purely the division by zero."},
            {"text": "Because the p.d. must also be zero if the current is "
                     "zero, so there is nothing to measure", "correct": False,
             "why": "A p.d. can exist across an open gap even with no "
                    "current flowing — that is exactly why an open switch "
                    "reads the full battery p.d. across it."},
            {"text": "Because resistance can only be found from a graph, "
                     "never from a single reading", "correct": False,
             "why": "A single V and I reading is exactly how resistance is "
                    "normally found; the problem here is specifically that I "
                    "is zero."},
            {"text": "Because R = V ÷ I involves dividing by the current, "
                     "and dividing by zero never has an answer.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h28",
        "band": "harder",
        "text": "Resistors of 2 Ω, 3 Ω and 5 Ω are connected in series across "
                "a 20 V supply. What current flows?",
        "options": [
            {"text": "10 A", "correct": False,
             "why": "That uses only the 2 Ω resistor; in series the three "
                    "resistances must be added together first."},
            {"text": "2.0 A", "correct": True},
            {"text": "4.0 A", "correct": False,
             "why": "That uses only the largest resistor; all three must be "
                    "added before dividing."},
            {"text": "0.50 A", "correct": False,
             "why": "That divides the total resistance by the p.d. instead "
                    "of the p.d. by the total resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h29",
        "band": "harder",
        "text": "A student argues: \"A 10 Ω resistor at 2 V gives 0.2 A, so "
                "R = V ÷ I = 10 Ω. At 20 V it must still give 0.2 A, "
                "otherwise the formula would be wrong.\" What is wrong with "
                "this argument?",
        "options": [
            {"text": "The formula stays right regardless; it is the CURRENT "
                     "that must scale up with the p.d. so that the ratio "
                     "comes back to 10 Ω, not stay fixed itself.",
             "correct": True},
            {"text": "Nothing is wrong — a resistor really does give the "
                     "same current at any p.d.", "correct": False,
             "why": "The CURRENT does change with the p.d.; what stays "
                    "fixed for a resistor is the RATIO of the two, not "
                    "either reading on its own."},
            {"text": "The formula only applies at low voltages, so it "
                     "breaks down at 20 V", "correct": False,
             "why": "R = V ÷ I is a definition with no voltage limit built "
                    "into it; a plain resistor keeps the same ratio across a "
                    "wide range."},
            {"text": "The student is right that the current stays the same, "
                     "but wrong about which formula to use, since R = V ÷ I "
                     "was never the correct way to check whether a current "
                     "has changed", "correct": False,
             "why": "For a plain resistor the current at 20 V is ten times "
                    "the current at 2 V — 2.0 A, not 0.2 A — so the current "
                    "itself has not stayed the same."},
        ],
        "figure": None,
    },
    {
        "id": "p8-05-h30",
        "band": "harder",
        "text": "A student tests a component seven times as the p.d. rises "
                "steadily from 1 V to 7 V, and finds the resistance "
                "calculated is 10 Ω every single time. A second component "
                "gives seven different resistances over the same range. What "
                "can be concluded about the two components?",
        "options": [
            {"text": "The first component is broken, since a real component "
                     "should show some variation", "correct": False,
             "why": "A steady, unchanging ratio across many readings is "
                    "exactly the signature of a good resistor, not a fault."},
            {"text": "The second component is broken, since its resistance "
                     "should not change", "correct": False,
             "why": "Only a resistor's value is expected to stay fixed; many "
                    "real components, like a lamp, genuinely change "
                    "resistance as conditions change."},
            {"text": "The first behaves like a plain resistor; the second "
                     "behaves like a filament lamp or another component "
                     "whose resistance depends on its state.",
             "correct": True},
            {"text": "Both components must be identical, since R = V ÷ I is "
                     "calculated in exactly the same way for each of them, "
                     "whatever the numbers happen to come out as",
             "correct": False,
             "why": "Using the same formula on both does not make their "
                    "behaviour identical; one gives a fixed answer and the "
                    "other does not."},
        ],
        "figure": None,
    },
]
