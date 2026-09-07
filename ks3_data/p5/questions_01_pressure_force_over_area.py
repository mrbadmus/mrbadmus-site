"""P5 lesson 01 — Pressure = force ÷ area: twelve questions (MRB-223).

Written against Design's page. The drawing pin, the block on sand and both
worked examples are hers.

The discriminations, in the order the lesson builds them:

  · sharpening changes the AREA, not the force (`PRESS-01`);
  · pressure is not a force and is not in newtons (`PRESS-03`);
  · the unit needs SQUARE METRES, and there are 10 000 cm² in one;
  · more contact area LOWERS the pressure (`PRESS-04`);
  · pressure acts at right angles to whatever surface it meets, whichever
    way that faces (`PRESS-02`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — index cycles 1, 3, 0, 2, giving three of each.

⚠️ Rung 1 (600 N on 0.30 m²) and Rung 2 (the boots and the heels) are NOT
restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P5"
LESSON = "pressure-force-over-area"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p5-01-e01",
        "band": "easier",
        "text": "Pressure is measured in…",
        "options": [
            {"text": "newtons", "correct": False,
             "why": "Newtons measure force. Pressure is a force shared out "
                    "over an area, which is a different quantity."},
            {"text": "pascals", "correct": True},
            {"text": "square metres", "correct": False,
             "why": "That is the area on the bottom of the division, not the "
                    "answer."},
            {"text": "kilograms", "correct": False,
             "why": "Kilograms measure mass. Nothing in pressure is a mass."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e02",
        "band": "easier",
        "text": "One pascal is…",
        "options": [
            {"text": "one newton", "correct": False,
             "why": "A newton on its own is a force. A pascal says how that "
                    "force is spread out."},
            {"text": "one newton multiplied by one square metre",
             "correct": False,
             "why": "Multiplying gives a force back from a known pressure. "
                    "The pascal is the other way round."},
            {"text": "one square metre for every newton", "correct": False,
             "why": "That is the division upside down — area over force "
                    "rather than force over area."},
            {"text": "one newton spread over one square metre",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e03",
        "band": "easier",
        "text": "A force of 60 N acts on an area of 0.20 m². What is the "
                "pressure?",
        "options": [
            {"text": "300 Pa", "correct": True},
            {"text": "12 Pa", "correct": False,
             "why": "That is 60 × 0.20. To find the pressure the force is "
                    "shared out over the area, so you divide."},
            {"text": "0.0033 Pa", "correct": False,
             "why": "That is 0.20 ÷ 60 — the division the wrong way round."},
            {"text": "300 N", "correct": False,
             "why": "The arithmetic is right and the unit is wrong. Force "
                    "divided by area gives pascals."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e04",
        "band": "easier",
        "text": "Why is a drawing pin given a sharp point?",
        "options": [
            {"text": "To make the force pushing it bigger than it would be "
                     "with a blunt point", "correct": False,
             "why": "The force is whatever your thumb supplies. Sharpening "
                    "changes no force anywhere."},
            {"text": "To make the metal harder, so that the pin is stiff "
                     "enough to enter wood", "correct": False,
             "why": "Hardness matters for a pin that has to survive, but it "
                    "is not why the point goes in."},
            {"text": "To concentrate the same force onto a tiny area, giving "
                     "a very high pressure", "correct": True},
            {"text": "To make the pin lighter, so that less weight has to "
                     "be forced into the wood", "correct": False,
             "why": "Its weight is nowhere near enough to matter. What goes "
                    "in is the pressure under the point."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p5-01-s01",
        "band": "standard",
        "text": "A box presses down with 200 N on a base of 400 cm². What is "
                "the pressure?",
        "options": [
            {"text": "0.5 Pa", "correct": False,
             "why": "That divides by the CENTIMETRES squared. A pascal needs "
                    "square metres, and there are 10 000 cm² in one."},
            {"text": "80 000 Pa", "correct": False,
             "why": "That multiplies. Pressure shares the force out over the "
                    "area, so it divides."},
            {"text": "5000 Pa", "correct": True},
            {"text": "2 Pa", "correct": False,
             "why": "That divides 400 by 200 — the wrong way round, and in "
                    "the wrong unit."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s02",
        "band": "standard",
        "text": "A block stands on its largest face and then on its smallest. "
                "The weight has not changed. What happens to the pressure "
                "under it?",
        "options": [
            {"text": "It stays the same, because the weight has not changed.",
             "correct": False,
             "why": "The weight sets the force. The AREA sets how "
                    "concentrated it is, and that has changed."},
            {"text": "It goes down, because a smaller face means less of the "
                     "force reaches the ground.", "correct": False,
             "why": "All of the force still reaches the ground. It is now "
                    "carried by fewer square metres, so each one carries "
                    "more."},
            {"text": "It goes up, because standing something on its end "
                     "makes it heavier.", "correct": False,
             "why": "The verdict is right and the reason is wrong. Turning a "
                    "block over changes nothing about its weight."},
            {"text": "It goes up, because the same force now acts on a "
                     "smaller area.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s03",
        "band": "standard",
        "text": "The ground under a machine must take no more than 40 000 Pa. "
                "The machine weighs 20 000 N. What is the smallest area its "
                "feet can cover?",
        "options": [
            {"text": "0.5 m²", "correct": True},
            {"text": "2 m²", "correct": False,
             "why": "That is 40 000 ÷ 20 000 — the division the wrong way "
                    "round. Cover A on the triangle: F sits over P."},
            {"text": "800 000 000 m²", "correct": False,
             "why": "That multiplies the two. To find an area from a force "
                    "and a pressure you divide."},
            {"text": "20 000 m²", "correct": False,
             "why": "That is the weight with a square metre written after "
                    "it. The pressure limit still has to be divided in."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s04",
        "band": "standard",
        "text": "Why do tank tracks and snowshoes work?",
        "options": [
            {"text": "They make the thing standing on them lighter.",
             "correct": False,
             "why": "The weight is unchanged. What changes is how it is "
                    "shared out."},
            {"text": "They spread the same weight over a much larger area, "
                     "so the pressure on the soft ground is much lower.",
             "correct": True},
            {"text": "They concentrate the weight into a smaller area, so "
                     "it presses through the soft layer instead of resting "
                     "on it", "correct": False,
             "why": "That is what a stiletto heel does, and it is exactly "
                    "how to sink. Tracks do the opposite."},
            {"text": "They reduce the friction, so nothing digs in.",
             "correct": False,
             "why": "Friction is a separate force. What keeps them on top is "
                    "the pressure being low enough for the ground to take."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p5-01-h01",
        "band": "harder",
        "text": "A drawing pin is pushed sideways into a noticeboard. Which "
                "way does the pressure under its point act?",
        "options": [
            {"text": "Sideways, at right angles to the board.",
             "correct": True},
            {"text": "Downwards, because pressure always acts downwards.",
             "correct": False,
             "why": "Downwards is only where the everyday examples happen to "
                    "point. The rule is at right angles to the SURFACE."},
            {"text": "In every direction at once, because it is a pressure.",
             "correct": False,
             "why": "A fluid presses in every direction. A solid point on a "
                    "solid board presses at right angles to the board."},
            {"text": "It has no direction — a pressure is just a number.",
             "correct": False,
             "why": "It acts on a surface and it has a direction relative to "
                    "that surface, which is why the phrase 'at right angles' "
                    "is in the definition."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h02",
        "band": "harder",
        "text": "Two people press on a board with a force meter behind each: "
                "one with a sharp pin, one with a blunt one. Both push until "
                "the pin stops going in. What do the meters read?",
        "options": [
            {"text": "The sharp pin's meter reads more, because it pushes "
                     "harder.", "correct": False,
             "why": "Sharpening changes no force. It changes the area that "
                    "force has to act through."},
            {"text": "The blunt pin's meter reads more, because you have to "
                     "lean on it.", "correct": False,
             "why": "True in practice for getting it IN — but the question "
                    "fixes both at the point where the pin stops, and the "
                    "reading is the force you supplied."},
            {"text": "The same reading, because the force is whatever the "
                     "hand supplies.", "correct": True},
            {"text": "Neither reads anything, because a meter cannot measure "
                     "a pressure.", "correct": False,
             "why": "It is not being asked to. It measures the force, which "
                    "is exactly what the comparison needs."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h03",
        "band": "harder",
        "text": "A hydraulic jack lets a small force on a small piston hold "
                "up a car on a big one. What is the catch?",
        "options": [
            {"text": "The pressure in the big cylinder is much higher, "
                     "which is where all of the extra force comes from",
             "correct": False,
             "why": "The pressure is the SAME in both. What differs is the "
                    "area it acts on."},
            {"text": "There is no catch — a jack really does make force "
                     "out of nothing, and nothing is paid for it.",
             "correct": False,
             "why": "Force can be multiplied; nothing is created. The energy "
                    "transferred is the same either way."},
            {"text": "The small piston has to move much further than the big "
                     "one, so the energy transferred is the same.",
             "correct": True},
            {"text": "The jack only works while the oil is warm, because "
                     "cold oil is too stiff to pass the push on.",
             "correct": False,
             "why": "Temperature is not the trade. The trade is distance "
                    "against force."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h04",
        "band": "harder",
        "text": "A student writes “pressure = 3000 N” for a block on sand. "
                "What has gone wrong, and what would fix it?",
        "options": [
            {"text": "Nothing has gone wrong — a press on the ground is a "
                     "force in newtons.",
             "correct": False,
             "why": "The press IS a force, but the quantity they were asked "
                    "for is how that force is spread out."},
            {"text": "The number is wrong and the unit is fine, so only "
                     "the arithmetic needs redoing.",
             "correct": False,
             "why": "The arithmetic may be perfect. What is wrong is that a "
                    "pressure cannot be reported in newtons."},
            {"text": "They should divide by the area a second time, and "
                     "that would fix the unit.",
             "correct": False,
             "why": "The area has already been divided in. Dividing twice "
                    "would give a number that means nothing at all."},
            {"text": "Force ÷ area gives newtons per square metre, so the "
                     "unit should be Pa.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p5-01-e05",
        "band": "easier",
        "text": "A force of 200 N acts on an area of 4 m². What is the "
                "pressure?",
        "options": [
            {"text": "50 Pa", "correct": True},
            {"text": "800 Pa", "correct": False,
             "why": "That is 200 × 4. Pressure is the force DIVIDED by the "
                    "area."},
            {"text": "0.02 Pa", "correct": False,
             "why": "That is 4 ÷ 200, the division upside down."},
            {"text": "204 Pa", "correct": False,
             "why": "That adds the two, and a force cannot be added to an "
                    "area."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e06",
        "band": "easier",
        "text": "In which direction does pressure act on a surface?",
        "options": [            {"text": "Downwards only", "correct": False,
             "why": "A wall and a ceiling both have pressure on them, so it "
                    "is not only downwards."},
            {"text": "Along the surface, like friction", "correct": False,
             "why": "Friction acts along a surface; pressure acts squarely "
                    "into it."},
            {"text": "In the direction the object is moving", "correct": False,
             "why": "A stationary block still presses on the floor, so motion "
                    "is not what sets the direction."},
            {"text": "At right angles to whatever surface it meets",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e07",
        "band": "easier",
        "text": "Is pressure a force?",
        "options": [            {"text": "Yes, which is why it is measured in newtons",
             "correct": False,
             "why": "It is measured in pascals. Newtons measure the force "
                    "before it is divided by an area."},
            {"text": "Yes, but only when it acts downwards", "correct": False,
             "why": "Direction does not change what kind of quantity it is."},
            {"text": "No — it is an area divided by the force on it",
             "correct": False,
             "why": "That is the ratio upside down, and it would be measured "
                    "in square metres per newton."},
            {"text": "No — it is a force divided by the area it is spread "
                     "over",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e08",
        "band": "easier",
        "text": "How many square centimetres are there in one square metre?",
        "options": [            {"text": "100", "correct": False,
             "why": "100 is how many centimetres are in a metre. An area "
                    "needs that figure squared."},
            {"text": "1000", "correct": False,
             "why": "That is the number in a litre-to-millilitre step, and "
                    "not an area conversion at all."},
            {"text": "1 000 000", "correct": False,
             "why": "That is the number of cubic centimetres in a cubic "
                    "metre, which is a volume."},
            {"text": "10 000", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e09",
        "band": "easier",
        "text": "The same push is applied through a sharp point and through a "
                "blunt one. Which gives the higher pressure?",
        "options": [
            {"text": "The sharp point, because the force is on a smaller "
                     "area",
             "correct": True},
            {"text": "The sharp point, because it pushes harder",
             "correct": False,
             "why": "The push is the same for both — the point does not add "
                    "any force of its own."},
            {"text": "The blunt one, because more of it is touching",
             "correct": False,
             "why": "More area spreads the same force out, which LOWERS the "
                    "pressure."},
            {"text": "Neither — the same force always gives the same "
                     "pressure",
             "correct": False,
             "why": "Only if the area matches too, and that is exactly what "
                    "differs here."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e10",
        "band": "easier",
        "text": "One pascal is the same as…",
        "options": [
            {"text": "1 N/m²", "correct": True},
            {"text": "1 m²/N", "correct": False,
             "why": "That is the ratio upside down — area divided by force, "
                    "not force divided by area."},
            {"text": "1 N", "correct": False,
             "why": "A newton on its own is a force. A pascal always has an "
                    "area underneath it."},
            {"text": "1 N/m", "correct": False,
             "why": "The area is in SQUARE metres, so the unit needs the "
                    "square."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e11",
        "band": "easier",
        "text": "A force of 500 N acts on an area of 0.25 m². What is the "
                "pressure?",
        "options": [            {"text": "125 Pa", "correct": False,
             "why": "That is 500 × 0.25, a multiplication where the formula "
                    "divides."},
            {"text": "500.25 Pa", "correct": False,
             "why": "That adds the force to the area, which cannot be done."},
            {"text": "0.0005 Pa", "correct": False,
             "why": "That is 0.25 ÷ 500, the ratio the wrong way up."},
            {"text": "2000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e12",
        "band": "easier",
        "text": "To reduce the pressure a load puts on soft ground, you "
                "should…",
        "options": [
            {"text": "spread it over a larger area", "correct": True},
            {"text": "spread it over a smaller area", "correct": False,
             "why": "A smaller area concentrates the same weight, which "
                    "raises the pressure."},
            {"text": "make the load lighter and the area smaller too",
             "correct": False,
             "why": "The lighter load helps, but shrinking the area works "
                    "against it."},
            {"text": "turn the load so it presses sideways", "correct": False,
             "why": "It still presses into whatever surface it meets, and the "
                    "area is what decides the pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e13",
        "band": "easier",
        "text": "Which quantity is measured in pascals?",
        "options": [            {"text": "Force", "correct": False,
             "why": "Force is measured in newtons; a pascal already has an "
                    "area divided into it."},
            {"text": "Area", "correct": False,
             "why": "Area is measured in square metres."},
            {"text": "Weight", "correct": False,
             "why": "Weight is a force, so it is in newtons too."},
            {"text": "Pressure", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p5-01-s05",
        "band": "standard",
        "text": "A block of weight 240 N stands on a base of 0.60 m². What "
                "pressure does it put on the floor?",
        "options": [            {"text": "144 Pa", "correct": False,
             "why": "That is 240 × 0.60, a multiplication where the formula "
                    "divides."},
            {"text": "240 Pa", "correct": False,
             "why": "That is the weight in newtons with the unit swapped; the "
                    "area still has to be divided in."},
            {"text": "0.0025 Pa", "correct": False,
             "why": "That is 0.60 ÷ 240, the ratio upside down."},
            {"text": "400 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s06",
        "band": "standard",
        "text": "A crate puts 500 Pa on a floor through a base of 0.40 m². "
                "What is its weight?",
        "options": [            {"text": "1250 N", "correct": False,
             "why": "That is 500 ÷ 0.40, dividing where the rearrangement "
                    "multiplies."},
            {"text": "0.0008 N", "correct": False,
             "why": "That is 0.40 ÷ 500, which is neither the formula nor its "
                    "rearrangement."},
            {"text": "500 N", "correct": False,
             "why": "That is the pressure in pascals read as a force; the "
                    "area has to be multiplied back in."},
            {"text": "200 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s07",
        "band": "standard",
        "text": "A force of 900 N produces a pressure of 300 Pa. What area is "
                "it spread over?",
        "options": [
            {"text": "270 000 m²", "correct": False,
             "why": "That is 900 × 300. To find the area you divide the force "
                    "by the pressure."},
            {"text": "0.33 m²", "correct": False,
             "why": "That is 300 ÷ 900, the division the wrong way round."},
            {"text": "600 m²", "correct": False,
             "why": "That subtracts, and a force cannot be taken away from a "
                    "pressure."},
            {"text": "3 m²", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s08",
        "band": "standard",
        "text": "A box presses down with 150 N on a base of 300 cm². What is "
                "the pressure in pascals?",
        "options": [            {"text": "0.5 Pa", "correct": False,
             "why": "That is 150 ÷ 300, using square centimetres as though "
                    "they were square metres."},
            {"text": "50 Pa", "correct": False,
             "why": "That divides by 3 m², treating 300 cm² as 3 m² instead "
                    "of 0.03 m²."},
            {"text": "45 000 Pa", "correct": False,
             "why": "That is 150 × 300, a multiplication where the formula "
                    "divides."},
            {"text": "5000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s09",
        "band": "standard",
        "text": "Why do heavy lorries have many wheels rather than four large "
                "ones?",
        "options": [
            {"text": "To spread the weight over more area and lower the "
                     "pressure",
             "correct": True},
            {"text": "To reduce the weight the lorry puts on the road",
             "correct": False,
             "why": "The weight is unchanged; only how widely it is spread "
                    "changes."},
            {"text": "To increase the pressure so the tyres grip better",
             "correct": False,
             "why": "High pressure is what damages a road surface, and it is "
                    "what the design avoids."},
            {"text": "To make the lorry accelerate more quickly",
             "correct": False,
             "why": "Acceleration is a separate matter and is not what more "
                    "wheels are for."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s10",
        "band": "standard",
        "text": "A brick can stand on a face of 0.020 m² or on an end of "
                "0.005 m². How do the two pressures compare?",
        "options": [
            {"text": "The end gives four times the pressure of the face",
             "correct": True},
            {"text": "The face gives four times the pressure of the end",
             "correct": False,
             "why": "The larger area spreads the same weight further, so it "
                    "gives the LOWER pressure."},
            {"text": "They are the same, because the brick's weight has not "
                     "changed",
             "correct": False,
             "why": "The weight is the same, which is exactly why the "
                    "different areas give different pressures."},
            {"text": "The end gives 0.015 Pa more than the face",
             "correct": False,
             "why": "0.015 is the difference in the two areas, not a "
                    "pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s11",
        "band": "standard",
        "text": "A knife is sharpened, and the same force is used on it. What "
                "happens to the pressure under the blade?",
        "options": [            {"text": "It falls, because a sharp blade needs less force",
             "correct": False,
             "why": "The force is stated as unchanged; what has changed is "
                    "the area."},
            {"text": "It stays the same, because the force is the same",
             "correct": False,
             "why": "Pressure needs both numbers, and the area has been made "
                    "much smaller."},
            {"text": "It cannot be said without knowing the blade's mass",
             "correct": False,
             "why": "The blade's mass does not appear in pressure = force ÷ "
                    "area."},
            {"text": "It rises, because the same force acts on a smaller "
                     "area",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s12",
        "band": "standard",
        "text": "When is it wrong to say a heavier person always presses "
                "harder on a floor?",
        "options": [            {"text": "Never — a heavier person always gives the higher "
                     "pressure",
             "correct": False,
             "why": "A lighter person in narrow heels can beat a heavier one "
                    "in flat boots by a long way."},
            {"text": "Only on a soft floor, where the area changes",
             "correct": False,
             "why": "The comparison depends on area on any floor, hard or "
                    "soft."},
            {"text": "Only when one of them is standing on one foot",
             "correct": False,
             "why": "That is one example of different areas, not the general "
                    "condition."},
            {"text": "Whenever the two are standing on different areas",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s13",
        "band": "standard",
        "text": "A camel's foot spreads to about twice the area of a horse's "
                "for a similar weight. What does that do?",
        "options": [
            {"text": "It halves the pressure on the sand", "correct": True},
            {"text": "It doubles the pressure on the sand", "correct": False,
             "why": "Doubling the area with the same weight halves the "
                    "pressure rather than doubling it."},
            {"text": "It halves the weight the camel puts on the sand",
             "correct": False,
             "why": "The weight is unchanged; only how widely it is spread "
                    "has changed."},
            {"text": "It makes no difference, because the weight is the same",
             "correct": False,
             "why": "The same weight over twice the area is exactly half the "
                    "pressure."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p5-01-h05",
        "band": "harder",
        "text": "A machine weighs 15 000 N and must not press on the ground "
                "with more than 25 000 Pa. What is its smallest usable track "
                "area?",
        "options": [
            {"text": "0.6 m²", "correct": True},
            {"text": "1.67 m²", "correct": False,
             "why": "That is 25 000 ÷ 15 000, the division the wrong way "
                    "round."},
            {"text": "375 000 000 m²", "correct": False,
             "why": "That multiplies the two, which gives a number with no "
                    "physical meaning here."},
            {"text": "10 000 m²", "correct": False,
             "why": "That subtracts the two figures, and a force cannot be "
                    "taken from a pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h06",
        "band": "harder",
        "text": "A stiletto heel of area 0.0001 m² carries 300 N. What is the "
                "pressure under it?",
        "options": [            {"text": "0.03 Pa", "correct": False,
             "why": "That is 300 × 0.0001, a multiplication where the formula "
                    "divides."},
            {"text": "30 000 Pa", "correct": False,
             "why": "That divides by 0.01 rather than 0.0001 — two decimal "
                    "places have been lost."},
            {"text": "300 Pa", "correct": False,
             "why": "That is the force with the unit swapped; the area still "
                    "has to be divided in."},
            {"text": "3 000 000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h07",
        "band": "harder",
        "text": "An elephant's foot carries 20 000 N over 0.1 m². How does "
                "that pressure compare with the 3 000 000 Pa under a stiletto "
                "heel?",
        "options": [            {"text": "The elephant's is higher, because it is far heavier",
             "correct": False,
             "why": "Weight alone does not settle it: the foot spreads that "
                    "weight over a thousand times more area."},
            {"text": "They are about the same, at 200 000 Pa each",
             "correct": False,
             "why": "The elephant gives 200 000 Pa and the heel gives fifteen "
                    "times that."},
            {"text": "The heel's is a hundred times higher, at 30 000 Pa for "
                     "the elephant",
             "correct": False,
             "why": "20 000 ÷ 0.1 is 200 000 Pa, not 30 000 Pa."},
            {"text": "The heel's is fifteen times higher, at 200 000 Pa for "
                     "the elephant",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h08",
        "band": "harder",
        "text": "A student converts 400 cm² into 4 m² before working out a "
                "pressure. What is wrong?",
        "options": [            {"text": "Nothing — there are 100 cm² in a square metre",
             "correct": False,
             "why": "100 is the LENGTH conversion. An area needs it squared, "
                    "giving 10 000."},
            {"text": "The conversion is right but the pressure should then be "
                     "in newtons",
             "correct": False,
             "why": "The conversion is wrong, and a pressure is never in "
                    "newtons."},
            {"text": "There are 1000 cm² in a square metre, so it is 0.4 m²",
             "correct": False,
             "why": "1000 is the millilitres-in-a-litre step, and it is not "
                    "an area conversion."},
            {"text": "There are 10 000 cm² in a square metre, so it is "
                     "0.04 m²",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h09",
        "band": "harder",
        "text": "A rescuer lies a ladder flat on thin ice and crawls along it "
                "rather than walking. Why?",
        "options": [
            {"text": "Because the ladder is lighter than the rescuer",
             "correct": False,
             "why": "The ladder adds weight. What it changes is how widely "
                    "the weight is spread."},
            {"text": "Because crawling makes the rescuer weigh less",
             "correct": False,
             "why": "Weight does not change with posture; the contact area "
                    "does."},
            {"text": "Because the ladder makes the ice stronger where it lies",
             "correct": False,
             "why": "The ice is unchanged. It is the pressure on it that has "
                    "been reduced."},
            {"text": "Because the weight is spread over a far larger area",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h10",
        "band": "harder",
        "text": "Why is pressure not simply another way of saying how hard "
                "you push?",
        "options": [
            {"text": "Because the same push gives different pressures on "
                     "different areas",
             "correct": True},
            {"text": "Because pressure is always larger than the force that "
                     "causes it",
             "correct": False,
             "why": "It can be smaller: 200 N over 4 m² gives only 50 Pa."},
            {"text": "Because a push is a force and pressure acts without any "
                     "force at all",
             "correct": False,
             "why": "There is always a force; pressure is that force divided "
                    "by an area."},
            {"text": "Because pressure only exists in liquids and gases",
             "correct": False,
             "why": "A block on a bench puts a pressure on it, and nothing "
                    "there is a liquid."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h11",
        "band": "harder",
        "text": "A jack pushes 20 N onto a small piston of 0.001 m². The "
                "large piston has an area of 0.05 m². What force can it hold "
                "up?",
        "options": [
            {"text": "20 N, the same as the force put in", "correct": False,
             "why": "The pressure is the same throughout, but the larger "
                    "piston has fifty times the area for it to act on."},
            {"text": "0.4 N", "correct": False,
             "why": "That divides where the second step multiplies; a jack "
                    "multiplies the force rather than shrinking it."},
            {"text": "1000 N", "correct": True},
            {"text": "20 000 N", "correct": False,
             "why": "20 000 Pa is the pressure. It still has to be multiplied "
                    "by the 0.05 m² piston area."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h12",
        "band": "harder",
        "text": "A drawing pin's head has a hundred times the area of its "
                "point. How do the two pressures compare?",
        "options": [
            {"text": "The point's pressure is a hundred times the head's",
             "correct": True},
            {"text": "The head's pressure is a hundred times the point's",
             "correct": False,
             "why": "The larger area spreads the same force further, so the "
                    "head gives the smaller pressure."},
            {"text": "They are equal, because the same force passes through "
                     "both",
             "correct": False,
             "why": "The force IS the same, which is why the areas decide the "
                    "answer."},
            {"text": "The point's is a hundred times smaller, which is why it "
                     "does not hurt",
             "correct": False,
             "why": "It is a hundred times LARGER, which is why the point "
                    "goes into the board and the head does not into a thumb."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h13",
        "band": "harder",
        "text": "A 60 kg student stands on one foot of area 0.015 m². What "
                "pressure is on the floor, taking gravity as 10 N/kg?",
        "options": [            {"text": "4000 Pa", "correct": False,
             "why": "That divides the 60 kg mass by the area without turning "
                    "it into a weight in newtons first."},
            {"text": "0.9 Pa", "correct": False,
             "why": "That multiplies the mass by the area, which uses neither "
                    "the weight nor the division."},
            {"text": "9 Pa", "correct": False,
             "why": "That is 600 × 0.015, a multiplication where the formula "
                    "divides."},
            {"text": "40 000 Pa", "correct": True},
        ],
        "figure": None,
    },
]
