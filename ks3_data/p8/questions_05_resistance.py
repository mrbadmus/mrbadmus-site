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
]
