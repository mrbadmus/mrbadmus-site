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
        "options": [
            {"text": "Yes, which is why it is measured in newtons",
             "correct": False,
             "why": "It is measured in pascals. Newtons measure the force "
                    "before it is divided by an area."},
            {"text": "Yes, but only when it acts downwards", "correct": False,
             "why": "Direction does not change what kind of quantity it is."},
            {"text": "No — it is an area divided by the force that acts on it",
             "correct": False,
             "why": "That is the ratio upside down, and it would be measured "
                    "in square metres per newton."},
            {"text": "No — it is a force divided by the area it acts on",
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

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p5-01-e14",
        "band": "easier",
        "text": "In pressure = force ÷ area, which force goes into the "
                "calculation?",
        "options": [
            {"text": "The largest force acting anywhere on the object",
             "correct": False,
             "why": "A force acting somewhere else does not press on this "
                    "surface, so it is not the one being shared out."},
            {"text": "The force needed to lift the object off the ground",
             "correct": False,
             "why": "That force would act upwards, away from the surface, and "
                    "it presses on nothing."},
            {"text": "The force acting at right angles to the surface",
             "correct": True},
            {"text": "The force of friction acting along the surface",
             "correct": False,
             "why": "Friction slides along a surface; pressure uses the force "
                    "pushing squarely into it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e15",
        "band": "easier",
        "text": "Two boxes stand on a floor on bases of exactly the same area, "
                "but one is heavier. Which puts the greater pressure on the "
                "floor?",
        "options": [
            {"text": "The heavier box, because a bigger force acts on the same "
                     "area", "correct": True},
            {"text": "The lighter box, because it rests more gently",
             "correct": False,
             "why": "Resting gently is not a measurement. A smaller force on "
                    "the same area gives a smaller pressure."},
            {"text": "Both the same, because the bases cover equal areas",
             "correct": False,
             "why": "Equal areas settle nothing on their own; the forces "
                    "pressing on them differ."},
            {"text": "Neither, until you know how tall each box is",
             "correct": False,
             "why": "Height does not appear in pressure = force ÷ area, so it "
                    "cannot change the answer."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e16",
        "band": "easier",
        "text": "An area of 0.05 m² written in square centimetres is…",
        "options": [
            {"text": "5 cm²", "correct": False,
             "why": "That moves the decimal point two places, as though a "
                    "metre held 100 centimetres of area."},
            {"text": "50 cm²", "correct": False,
             "why": "That multiplies by 1000, which is a volume step rather "
                    "than an area one."},
            {"text": "0.000005 cm²", "correct": False,
             "why": "That divides by 10 000. Square centimetres are the "
                    "smaller unit, so the number gets bigger."},
            {"text": "500 cm²", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e17",
        "band": "easier",
        "text": "Which of these is shaped to give the highest pressure it can "
                "on what it meets?",
        "options": [
            {"text": "A snowshoe", "correct": False,
             "why": "A snowshoe is built to spread a weight out over soft "
                    "snow, which lowers the pressure."},
            {"text": "The point of a nail", "correct": True},
            {"text": "A concrete footing", "correct": False,
             "why": "A footing hands the weight of a house to the ground over "
                    "enough square metres for the ground to take it."},
            {"text": "A broad tractor tyre", "correct": False,
             "why": "A broad tyre exists to keep the pressure low so the "
                    "tractor stays on top of soft soil."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p5-01-s14",
        "band": "standard",
        "text": "A tractor tyre presses on soil with 45 000 Pa through a "
                "contact patch of 0.08 m². What force is on that patch?",
        "options": [
            {"text": "562 500 N", "correct": False,
             "why": "That is 45 000 ÷ 0.08, dividing where the rearrangement "
                    "multiplies."},
            {"text": "45 000 N", "correct": False,
             "why": "That is the pressure with the unit swapped; the patch "
                    "area still has to be multiplied in."},
            {"text": "3600 N", "correct": True},
            {"text": "0.0000018 N", "correct": False,
             "why": "That is 0.08 ÷ 45 000, which is neither the formula nor "
                    "its rearrangement."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s15",
        "band": "standard",
        "text": "A crate of weight 600 N rests on four small feet, each "
                "covering 0.0050 m². What pressure is on the floor?",
        "options": [
            {"text": "30 000 Pa", "correct": True},
            {"text": "120 000 Pa", "correct": False,
             "why": "That uses one foot's area. All four feet are carrying "
                    "the crate, so their areas add up first."},
            {"text": "12 Pa", "correct": False,
             "why": "That multiplies the weight by the total area instead of "
                    "dividing by it."},
            {"text": "150 Pa", "correct": False,
             "why": "That shares the weight between the four feet and then "
                    "forgets to divide by an area at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s16",
        "band": "standard",
        "text": "A shelf is rated to take 8000 Pa. A tin weighing 24 N is "
                "stood on it on a base of 0.0020 m². Is the shelf safe?",
        "options": [
            {"text": "Yes — the tin puts 1200 Pa on it, well under the "
                     "rating", "correct": False,
             "why": "That divides by 0.020 rather than 0.0020, so a decimal "
                    "place has been lost."},
            {"text": "Yes — 24 N is a small weight, so any shelf will hold it",
             "correct": False,
             "why": "The rating is a pressure, and a small weight on a tiny "
                    "base can still break it."},
            {"text": "It cannot be decided from a weight and an area alone",
             "correct": False,
             "why": "Those two are exactly what the pressure is worked out "
                    "from, so it can be decided."},
            {"text": "No — the tin puts 12 000 Pa on it, over the rating",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s17",
        "band": "standard",
        "text": "A student works out a pressure and writes the answer as "
                "40 N/m². Is that an acceptable unit?",
        "options": [
            {"text": "No — a pressure has to be written in newtons, since a "
                     "push is a force", "correct": False,
             "why": "A pressure is never written in newtons. The area has "
                    "already been divided in."},
            {"text": "Yes — one pascal is one newton per square metre",
             "correct": True},
            {"text": "No — N/m² is the unit of an area, so the answer means "
                     "something else", "correct": False,
             "why": "Area is measured in square metres on their own. N/m² has "
                    "a force divided by that area."},
            {"text": "Yes, but the number has to be divided by 10 000 to turn "
                     "it into pascals", "correct": False,
             "why": "No conversion is needed, because the two units are the "
                    "same size as each other."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p5-01-h14",
        "band": "harder",
        "text": "A box puts 4000 Pa on the floor. It is repacked so that it "
                "weighs half as much and stands on a third of the area. What "
                "is the new pressure?",
        "options": [
            {"text": "2000 Pa", "correct": False,
             "why": "That halves for the lighter load and then ignores the "
                    "smaller area, which pushes the pressure back up."},
            {"text": "666 Pa", "correct": False,
             "why": "That divides by three for the area, when a smaller area "
                    "raises the pressure rather than lowering it."},
            {"text": "24 000 Pa", "correct": False,
             "why": "That trebles and doubles together, using the lighter "
                    "load as though it were heavier."},
            {"text": "6000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h15",
        "band": "harder",
        "text": "A skater of weight 600 N balances on one blade whose edge "
                "touches the ice over 0.0003 m². What is the pressure under "
                "the blade?",
        "options": [
            {"text": "2 000 000 Pa", "correct": True},
            {"text": "0.18 Pa", "correct": False,
             "why": "That multiplies the weight by the area, where the "
                    "formula divides."},
            {"text": "200 000 Pa", "correct": False,
             "why": "That divides by 0.003 rather than 0.0003, losing one "
                    "decimal place."},
            {"text": "600 Pa", "correct": False,
             "why": "That is the weight with the unit changed, before the "
                    "area has been divided in."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h16",
        "band": "harder",
        "text": "Two skaters stand on thin ice. One weighs 500 N on boots "
                "covering 0.040 m²; the other weighs 700 N on boots covering "
                "0.070 m². Who presses harder on the ice?",
        "options": [
            {"text": "The 700 N skater, because they are the heavier of the "
                     "two", "correct": False,
             "why": "Their boots cover proportionally more ice, so the extra "
                    "weight is more than shared out."},
            {"text": "Neither — equal weights on equal boots give equal "
                     "pressures", "correct": False,
             "why": "Nothing here is equal: the weights differ and so do the "
                    "boot areas."},
            {"text": "The 500 N skater, at 12 500 Pa against 10 000 Pa",
             "correct": True},
            {"text": "The 700 N skater, at 17 500 Pa against 12 500 Pa",
             "correct": False,
             "why": "17 500 comes from dividing 700 by 0.040, using the other "
                    "skater's boot area."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h17",
        "band": "harder",
        "text": "Asked for the pressure from a force of 30 N on 150 cm², a "
                "student writes 0.2 Pa. What went wrong, and what is the "
                "right answer?",
        "options": [
            {"text": "They divided by 150 rather than by 0.0150, and it comes "
                     "to 4500 Pa", "correct": False,
             "why": "The fault is named correctly and the arithmetic is not: "
                    "4500 is 30 × 150."},
            {"text": "They divided by 150 rather than by 0.0150, and it comes "
                     "to 2000 Pa", "correct": True},
            {"text": "They used the wrong formula, and it comes to 0.2 N",
             "correct": False,
             "why": "The formula was right. It was the area that went in "
                    "unconverted, and a pressure is not in newtons."},
            {"text": "They divided by 1.50 rather than by 0.0150, and it "
                     "comes to 20 Pa", "correct": False,
             "why": "150 cm² is 0.0150 m², so 1.50 is a hundred times too "
                    "large and 20 Pa follows from it."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · easier ─────────────────────────────
    {
        "id": "p5-01-e18",
        "band": "easier",
        "text": "A block has a mass of 5 kg. Taking gravity as 10 N/kg, what "
                "is its weight?",
        "options": [
            {"text": "50 N", "correct": True},
            {"text": "5 N", "correct": False,
             "why": "That is the mass with a newton written after it; the "
                    "10 N/kg still has to be used."},
            {"text": "0.5 N", "correct": False,
             "why": "That divides by 10 instead of multiplying by it."},
            {"text": "50 kg", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: a weight "
                    "is a force, so it is in newtons."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e19",
        "band": "easier",
        "text": "A box has a base measuring 0.5 m by 0.4 m. What is the area "
                "of that base?",
        "options": [
            {"text": "0.9 m²", "correct": False,
             "why": "That adds the two sides. An area comes from multiplying "
                    "them."},
            {"text": "0.20 m²", "correct": True},
            {"text": "1.8 m²", "correct": False,
             "why": "That adds all four sides, which gives the distance round "
                    "the edge rather than the area."},
            {"text": "1.25 m²", "correct": False,
             "why": "That divides one side by the other, which gives no area "
                    "at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e20",
        "band": "easier",
        "text": "Which change would raise the pressure a crate puts on the "
                "floor?",
        "options": [
            {"text": "Standing it on a wider pallet", "correct": False,
             "why": "A wider pallet spreads the same weight further, which "
                    "lowers the pressure."},
            {"text": "Sliding it along instead of leaving it still",
             "correct": False,
             "why": "Sliding adds a push along the floor, not into it, so the "
                    "pressure is unchanged."},
            {"text": "Standing it on a smaller face", "correct": True},
            {"text": "Painting it a darker colour", "correct": False,
             "why": "Colour changes neither the weight nor the area touching "
                    "the floor."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e21",
        "band": "easier",
        "text": "A push of 80 N is spread over 0.4 m². What pressure does it "
                "give?",
        "options": [
            {"text": "32 Pa", "correct": False,
             "why": "That multiplies the two, where sharing a force out over "
                    "an area divides."},
            {"text": "80.4 Pa", "correct": False,
             "why": "That adds them, and a force cannot be added to an area."},
            {"text": "0.005 Pa", "correct": False,
             "why": "That is 0.4 ÷ 80, the ratio upside down."},
            {"text": "200 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e22",
        "band": "easier",
        "text": "How many square millimetres are there in one square metre?",
        "options": [
            {"text": "1 000 000", "correct": True},
            {"text": "1000", "correct": False,
             "why": "1000 is how many millimetres make a metre. An area needs "
                    "that figure squared."},
            {"text": "10 000", "correct": False,
             "why": "10 000 is the number of square centimetres in a square "
                    "metre, not square millimetres."},
            {"text": "100 000", "correct": False,
             "why": "That is a factor of ten short: a metre holds 1000 "
                    "millimetres, and 1000 squared is a million."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e23",
        "band": "easier",
        "text": "A bed of nails has hundreds of points. Why does it not pierce "
                "someone lying on it?",
        "options": [
            {"text": "The points are blunted so that they cannot enter skin",
             "correct": False,
             "why": "The points are sharp. It is how many of them share the "
                    "weight that saves the person."},
            {"text": "The weight is shared between so many points that each "
                     "takes only a small force", "correct": True},
            {"text": "Lying down makes a person weigh less than standing does",
             "correct": False,
             "why": "Weight does not change with posture; the area in contact "
                    "does."},
            {"text": "The nails hold each other up, so none of them reaches "
                     "the skin", "correct": False,
             "why": "Every point touches. The saving is that each carries a "
                    "tiny share of the weight."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e24",
        "band": "easier",
        "text": "A pressure of 500 Pa means that each square metre of the "
                "surface carries…",
        "options": [
            {"text": "500 square metres", "correct": False,
             "why": "Square metres measure the area a force is spread over, "
                    "and the question asks what that area carries."},
            {"text": "500 kg", "correct": False,
             "why": "Kilograms measure mass, and the pascal is built from "
                    "newtons and square metres."},
            {"text": "500 N", "correct": True},
            {"text": "500 Pa", "correct": False,
             "why": "That is the pressure itself. What each square metre "
                    "carries is a force, in newtons."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e25",
        "band": "easier",
        "text": "The force pressing on a surface is doubled while the area "
                "stays the same. The pressure…",
        "options": [
            {"text": "halves", "correct": False,
             "why": "Halving would need the force to fall, or the area to "
                    "grow."},
            {"text": "stays the same", "correct": False,
             "why": "Both numbers matter, and one of them has changed."},
            {"text": "goes up four times", "correct": False,
             "why": "Nothing here is squared: twice the force on the same "
                    "area is twice the pressure."},
            {"text": "doubles", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e26",
        "band": "easier",
        "text": "A tall stack of boxes stands on a pallet. Which area is used "
                "to work out the pressure on the floor?",
        "options": [
            {"text": "The area actually touching the floor", "correct": True},
            {"text": "The area of the whole stack, from top to bottom",
             "correct": False,
             "why": "The sides of the stack touch nothing, so they carry no "
                    "share of the weight."},
            {"text": "The area of the largest box in the stack",
             "correct": False,
             "why": "Only the part in contact with the floor matters, "
                    "whichever box happens to be biggest."},
            {"text": "The area of the room the stack is standing in",
             "correct": False,
             "why": "The rest of the floor is carrying nothing from this "
                    "stack."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e27",
        "band": "easier",
        "text": "A second identical brick is stacked on top of the first, on "
                "the same base. What happens to the pressure on the floor?",
        "options": [
            {"text": "It halves, because the weight is now shared between two "
                     "bricks", "correct": False,
             "why": "Both bricks press down through the same base, so the "
                    "floor takes the whole of both weights."},
            {"text": "It doubles", "correct": True},
            {"text": "It stays the same, because the base has not changed",
             "correct": False,
             "why": "The base is unchanged and the force on it is not, so the "
                    "pressure rises."},
            {"text": "It goes up four times, because there are two bricks on "
                     "one base", "correct": False,
             "why": "Twice the weight on the same area is twice the pressure, "
                    "not four times."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e28",
        "band": "easier",
        "text": "A student says the pressure under a box depends only on how "
                "heavy the box is. What has been left out?",
        "options": [
            {"text": "How tall the box is", "correct": False,
             "why": "Height does not appear in the relationship, and a tall "
                    "box on a wide base presses gently."},
            {"text": "What the box is made of", "correct": False,
             "why": "The material matters only through the weight, which the "
                    "student has already counted."},
            {"text": "The area it is standing on", "correct": True},
            {"text": "How long the box has been standing there",
             "correct": False,
             "why": "Time does not enter into it: the pressure is the same "
                    "after an hour as after a second."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e29",
        "band": "easier",
        "text": "The same force is spread over twice as much area. What "
                "happens to the pressure?",
        "options": [
            {"text": "It doubles, because there is more surface for it to act "
                     "on", "correct": False,
             "why": "More area to share the force between means each square "
                    "metre carries less, not more."},
            {"text": "It stays the same, because the force has not changed",
             "correct": False,
             "why": "The force is only half the calculation; the area has "
                    "changed."},
            {"text": "It falls to a quarter, because the area has grown",
             "correct": False,
             "why": "Nothing here is squared: twice the area gives half the "
                    "pressure."},
            {"text": "It halves", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-e30",
        "band": "easier",
        "text": "Sand gives way when the pressure on it goes above 6000 Pa. A "
                "block standing on it makes 2000 Pa. What happens?",
        "options": [
            {"text": "The sand holds the block", "correct": True},
            {"text": "The block sinks in, because 2000 Pa is a large pressure",
             "correct": False,
             "why": "Whether it is large is beside the point: it is below the "
                    "figure at which this sand gives way."},
            {"text": "The sand gives way, because any pressure at all will "
                     "move sand", "correct": False,
             "why": "Sand carries plenty of pressure without moving, up to "
                    "the stated limit."},
            {"text": "It cannot be said without knowing the block's weight",
             "correct": False,
             "why": "The weight has already been used: the pressure it gives "
                    "is the figure quoted."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · standard ───────────────────────────
    {
        "id": "p5-01-s18",
        "band": "standard",
        "text": "A paint tin of mass 5 kg rests on a shelf through a base of "
                "0.0040 m². Gravity is 10 N/kg. Work out the pressure.",
        "options": [
            {"text": "1250 Pa", "correct": False,
             "why": "That divides the mass in kilograms by the area, without "
                    "turning it into a weight in newtons first."},
            {"text": "12 500 Pa", "correct": True},
            {"text": "0.2 Pa", "correct": False,
             "why": "That multiplies the weight by the area, where the "
                    "formula divides."},
            {"text": "50 Pa", "correct": False,
             "why": "That is the weight in newtons with the unit swapped; the "
                    "base area still has to be divided in."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s19",
        "band": "standard",
        "text": "A crate weighs 800 N and its base measures 0.50 m by 0.40 m. "
                "What pressure does it put on the floor?",
        "options": [
            {"text": "1778 Pa", "correct": False,
             "why": "That divides by 0.45, which is the average of the two "
                    "sides rather than the area."},
            {"text": "160 Pa", "correct": False,
             "why": "That divides by 5, using the sides as whole numbers and "
                    "ignoring the decimal point."},
            {"text": "4000 Pa", "correct": True},
            {"text": "889 Pa", "correct": False,
             "why": "That divides by 0.90, which is the two sides added "
                    "together rather than multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s20",
        "band": "standard",
        "text": "Ground can take 50 000 Pa before it gives way. A machine's "
                "feet cover 0.40 m² in total. How heavy can the machine be?",
        "options": [
            {"text": "125 000 N", "correct": False,
             "why": "That is 50 000 ÷ 0.40, dividing where the rearrangement "
                    "multiplies."},
            {"text": "50 000 N", "correct": False,
             "why": "That is the pressure limit with the unit swapped; the "
                    "foot area has to be multiplied in."},
            {"text": "0.000008 N", "correct": False,
             "why": "That is 0.40 ÷ 50 000, which matches neither the formula "
                    "nor its rearrangement."},
            {"text": "20 000 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s21",
        "band": "standard",
        "text": "A pressure of 1 N/cm² is the same as how many pascals?",
        "options": [
            {"text": "10 000 Pa", "correct": True},
            {"text": "1 Pa", "correct": False,
             "why": "A pascal needs the force spread over a square METRE, and "
                    "a square centimetre is far smaller."},
            {"text": "100 Pa", "correct": False,
             "why": "100 is the length conversion between centimetres and "
                    "metres; an area needs it squared."},
            {"text": "0.0001 Pa", "correct": False,
             "why": "That divides where the conversion multiplies: the same "
                    "force on a bigger area gives a bigger count per metre."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s22",
        "band": "standard",
        "text": "A load is doubled and, at the same time, the area it stands "
                "on is doubled. What happens to the pressure?",
        "options": [
            {"text": "It doubles", "correct": False,
             "why": "The extra load is carried by exactly as much extra area, "
                    "so nothing per square metre has changed."},
            {"text": "It stays the same", "correct": True},
            {"text": "It goes up four times", "correct": False,
             "why": "The two changes work against each other rather than "
                    "multiplying together."},
            {"text": "It halves", "correct": False,
             "why": "That counts the bigger area and forgets the heavier "
                    "load."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s23",
        "band": "standard",
        "text": "A wheelbarrow wheel carries 400 N on 0.0020 m². A plank under "
                "it spreads the same 400 N over 0.20 m². By what factor does "
                "the pressure fall?",
        "options": [
            {"text": "By 10 times", "correct": False,
             "why": "The area has grown a hundredfold, not tenfold, so the "
                    "pressure falls by the same hundred."},
            {"text": "It does not fall — the weight has not changed",
             "correct": False,
             "why": "The weight sets the force; the area sets how "
                    "concentrated it is, and the area has grown."},
            {"text": "By 100 times", "correct": True},
            {"text": "By 1000 times", "correct": False,
             "why": "0.20 divided by 0.0020 is 100, so the factor is a "
                    "hundred."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s24",
        "band": "standard",
        "text": "A drawing pin is pushed with 20 N and its point touches the "
                "wood over 0.000001 m². What pressure is under the point?",
        "options": [
            {"text": "20 000 Pa", "correct": False,
             "why": "That divides by 0.001 rather than by 0.000001, losing "
                    "three decimal places."},
            {"text": "0.00002 Pa", "correct": False,
             "why": "That multiplies the force by the area, where the formula "
                    "divides."},
            {"text": "20 Pa", "correct": False,
             "why": "That is the push in newtons with the unit changed, "
                    "before the area has been divided in."},
            {"text": "20 000 000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s25",
        "band": "standard",
        "text": "A force of 100 N on 0.5 m² gives 200 Pa. Which of these gives "
                "the same pressure?",
        "options": [
            {"text": "400 N on 2 m²", "correct": True},
            {"text": "200 N on 0.5 m²", "correct": False,
             "why": "Doubling the force on the same area gives 400 Pa, twice "
                    "as much."},
            {"text": "100 N on 1 m²", "correct": False,
             "why": "The same force on twice the area gives 100 Pa, half as "
                    "much."},
            {"text": "50 N on 0.5 m²", "correct": False,
             "why": "Halving the force on the same area gives 100 Pa."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s26",
        "band": "standard",
        "text": "A student reads that the pressure under a crate is 3000 Pa "
                "and says that means 3000 N is pushing down. What is right?",
        "options": [
            {"text": "3000 N is pushing down, since a pascal is a newton",
             "correct": False,
             "why": "A pascal is a newton on every square metre, which is not "
                    "the same as a newton."},
            {"text": "3000 N is carried by each square metre, so the whole "
                     "force depends on the area", "correct": True},
            {"text": "The student is right, as long as the crate is standing "
                     "on exactly two square metres", "correct": False,
             "why": "On two square metres the whole force would be 6000 N, so "
                    "the figures would not match."},
            {"text": "Nothing can be said about the force from a pressure on "
                     "its own", "correct": False,
             "why": "The pressure gives the force on every square metre, and "
                    "the area turns that into the whole force."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s27",
        "band": "standard",
        "text": "Two crates weigh 300 N each. One stands on 0.05 m² and the "
                "other on 0.15 m². What is the difference in the pressures?",
        "options": [
            {"text": "2000 Pa", "correct": False,
             "why": "That is the pressure under the crate on 0.15 m², not the "
                    "gap between the two."},
            {"text": "6000 Pa", "correct": False,
             "why": "That is the pressure under the crate on 0.05 m², not the "
                    "gap between the two."},
            {"text": "4000 Pa", "correct": True},
            {"text": "8000 Pa", "correct": False,
             "why": "That adds the two pressures together, where the question "
                    "asks for the difference."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s28",
        "band": "standard",
        "text": "A snowboard spreads a rider's weight of 700 N over 0.14 m² of "
                "snow. What pressure is that?",
        "options": [
            {"text": "98 Pa", "correct": False,
             "why": "That is 700 × 0.14, a multiplication where the formula "
                    "divides."},
            {"text": "0.0002 Pa", "correct": False,
             "why": "That is 0.14 ÷ 700, the ratio the wrong way up."},
            {"text": "700 Pa", "correct": False,
             "why": "That is the rider's weight with the unit swapped, before "
                    "the area has been divided in."},
            {"text": "5000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s29",
        "band": "standard",
        "text": "A machine puts 8000 Pa on ground that gives way above "
                "6000 Pa. Which change would let it stand?",
        "options": [
            {"text": "Fitting wider feet, so the same weight covers more area",
             "correct": True},
            {"text": "Fitting narrower feet, so the weight is carried more "
                     "firmly", "correct": False,
             "why": "Narrower feet concentrate the same weight and push the "
                    "pressure higher still."},
            {"text": "Parking it more gently, so it settles rather than drops",
             "correct": False,
             "why": "Once it is standing still, how it got there has no "
                    "effect on the pressure."},
            {"text": "Painting the feet, so they slide rather than dig",
             "correct": False,
             "why": "Sliding is about friction along the ground, not the push "
                    "into it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-s30",
        "band": "standard",
        "text": "A block is turned from its largest face onto its smallest. "
                "Which of these has NOT changed?",
        "options": [
            {"text": "The area touching the floor", "correct": False,
             "why": "That is exactly what turning it changes, and it is why "
                    "the pressure changes."},
            {"text": "Its weight", "correct": True},
            {"text": "The pressure under it", "correct": False,
             "why": "The same weight on a smaller area gives a higher "
                    "pressure."},
            {"text": "The force carried by each square metre of floor",
             "correct": False,
             "why": "That is another way of saying the pressure, and it has "
                    "gone up."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · harder ─────────────────────────────
    {
        "id": "p5-01-h18",
        "band": "harder",
        "text": "A block of mass 8 kg has a base 0.25 m by 0.16 m. Taking "
                "gravity as 10 N/kg, what pressure does it put on the floor?",
        "options": [
            {"text": "200 Pa", "correct": False,
             "why": "That divides the mass by the area, leaving out the step "
                    "that turns kilograms into newtons."},
            {"text": "3.2 Pa", "correct": False,
             "why": "That multiplies the weight by the area rather than "
                    "dividing by it."},
            {"text": "2000 Pa", "correct": True},
            {"text": "320 Pa", "correct": False,
             "why": "That divides by 0.25 alone, using one side of the base "
                    "instead of the area."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h19",
        "band": "harder",
        "text": "Three identical bricks are stacked on the base of the bottom "
                "one, giving 9000 Pa on the floor. What would one brick alone "
                "give on the same face?",
        "options": [
            {"text": "9000 Pa", "correct": False,
             "why": "The base is the same and the weight on it is a third of "
                    "what it was, so the pressure falls."},
            {"text": "27 000 Pa", "correct": False,
             "why": "That trebles instead of dividing by three; one brick is "
                    "the lightest case of the two."},
            {"text": "4500 Pa", "correct": False,
             "why": "One brick out of three is a third of the stack, not a "
                    "half."},
            {"text": "3000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h20",
        "band": "harder",
        "text": "Ground gives way above 30 000 Pa. A crate weighs 18 000 N and "
                "stands on four feet. What is the smallest area each foot can "
                "have?",
        "options": [
            {"text": "0.15 m²", "correct": True},
            {"text": "0.60 m²", "correct": False,
             "why": "0.60 m² is the total area all four feet need between "
                    "them, so each one needs a quarter of it."},
            {"text": "2.4 m²", "correct": False,
             "why": "That multiplies the total area by four instead of "
                    "dividing it, which points the wrong way."},
            {"text": "1.67 m²", "correct": False,
             "why": "That is 30 000 ÷ 18 000, the division the wrong way "
                    "round, and the four feet are not used at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h21",
        "band": "harder",
        "text": "Two solid blocks are cut from the same material and have the "
                "same base, but one is twice as tall. How do their pressures "
                "on the floor compare?",
        "options": [
            {"text": "The same, because the bases are the same",
             "correct": False,
             "why": "Equal bases carry unequal weights here, so the pressures "
                    "differ."},
            {"text": "The taller one gives twice the pressure", "correct": True},
            {"text": "The taller one gives half the pressure, because its "
                     "weight is spread further up", "correct": False,
             "why": "Height does not spread a weight out; all of it still "
                    "reaches the same base."},
            {"text": "The shorter one gives four times the pressure",
             "correct": False,
             "why": "The shorter block is the lighter of the two on an equal "
                    "base, so it gives the lower pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h22",
        "band": "harder",
        "text": "A lorry tyre's contact patch is 0.03 m² and the pressure "
                "under it is 200 000 Pa. How many such tyres would a 24 000 N "
                "lorry need?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "Each patch carries 6000 N, so two of them would leave "
                    "half the lorry unsupported."},
            {"text": "Six", "correct": False,
             "why": "Six would mean each tyre carrying 4000 N, which needs a "
                    "smaller patch or a lower pressure than the figures give."},
            {"text": "Four", "correct": True},
            {"text": "Eight", "correct": False,
             "why": "Eight would mean each tyre carrying 3000 N, half of what "
                    "200 000 Pa on 0.03 m² comes to."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h23",
        "band": "harder",
        "text": "Why is a pressure in pascals often a very large number even "
                "when the force causing it is small?",
        "options": [
            {"text": "Because pascals are a smaller unit than newtons, so "
                     "there are more of them", "correct": False,
             "why": "The two measure different quantities, so neither is a "
                    "smaller version of the other."},
            {"text": "Because a pressure counts the force twice, once for "
                     "each direction it acts in", "correct": False,
             "why": "The force is counted once. Nothing in the relationship "
                    "doubles it."},
            {"text": "Because a small force is spread over a tiny fraction of "
                     "a square metre, so each whole square metre would carry "
                     "a great deal", "correct": True},
            {"text": "Because pressures are always written in bigger units "
                     "than the forces that cause them", "correct": False,
             "why": "A large force on a large area gives a small pressure, so "
                    "the numbers can run either way."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h24",
        "band": "harder",
        "text": "A crate weighing 600 N has a base of 50 cm by 40 cm. A "
                "student works out 600 ÷ 2000 = 0.3. What is the pressure "
                "really?",
        "options": [
            {"text": "3000 Pa", "correct": True},
            {"text": "0.3 Pa", "correct": False,
             "why": "That keeps the student's working. 2000 is the base in "
                    "square centimetres, and a pascal needs square metres."},
            {"text": "30 Pa", "correct": False,
             "why": "That reads 2000 cm² as 20 m². Dividing by 10 000 makes "
                    "the number smaller, not larger."},
            {"text": "300 000 Pa", "correct": False,
             "why": "That divides by 10 000 twice over, giving 0.0020 m²; one "
                    "pass gives 0.20 m²."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h25",
        "band": "harder",
        "text": "A student claims that the number given for a pressure can "
                "never be bigger than the number given for the force causing "
                "it. Which case settles it?",
        "options": [
            {"text": "A force of 10 N acting on 5 m², which gives 2 Pa",
             "correct": False,
             "why": "Here the pressure is the smaller number, which is the "
                    "case the student already believes."},
            {"text": "A force of 10 N acting on 0.001 m², which gives "
                     "10 000 Pa", "correct": True},
            {"text": "A force of 10 N acting on 1 m², which gives 10 Pa",
             "correct": False,
             "why": "The two numbers match here, so this neither supports the "
                    "claim nor breaks it."},
            {"text": "A force of 10 N acting on 10 m², which gives 1 Pa",
             "correct": False,
             "why": "This is another case where the pressure comes out "
                    "smaller, so the claim survives it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h26",
        "band": "harder",
        "text": "A machine's tracks give 25 000 Pa. They are replaced by "
                "tracks half as wide and twice as long. What happens to the "
                "pressure?",
        "options": [
            {"text": "It doubles", "correct": False,
             "why": "The extra length is cancelled by the lost width, so the "
                    "area is where it started."},
            {"text": "It halves", "correct": False,
             "why": "That counts the narrower width and forgets the extra "
                    "length."},
            {"text": "It stays at 25 000 Pa", "correct": True},
            {"text": "It falls to a quarter", "correct": False,
             "why": "The two changes work against each other rather than "
                    "multiplying together."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h27",
        "band": "harder",
        "text": "A car weighing 15 000 N stands on four tyres of 0.02 m² each. "
                "A lorry weighing 108 000 N stands on twelve of 0.05 m² each. "
                "Which presses harder on the road?",
        "options": [
            {"text": "The lorry, because it is far heavier", "correct": False,
             "why": "Its twelve wide tyres give it 0.60 m² of road, which is "
                    "more than enough to take the extra weight."},
            {"text": "The lorry, because it has more tyres touching the road",
             "correct": False,
             "why": "More tyres lower the pressure rather than raising it, "
                    "which is why lorries have so many."},
            {"text": "Neither, because both are designed for the same roads",
             "correct": False,
             "why": "Being allowed on the same road does not make two "
                    "pressures equal, and these two are not."},
            {"text": "The car, at 187 500 Pa against 180 000 Pa",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h28",
        "band": "harder",
        "text": "A 2000 N crate sits on a pallet measuring 1.2 m², but only "
                "the pallet's feet touch the floor, over 0.05 m². What "
                "pressure reaches the floor?",
        "options": [
            {"text": "40 000 Pa", "correct": True},
            {"text": "1667 Pa", "correct": False,
             "why": "That uses the whole pallet. Its body is held clear of "
                    "the floor, so no weight passes through it."},
            {"text": "2400 Pa", "correct": False,
             "why": "That multiplies the pallet's area by the weight, where "
                    "the formula divides, and it uses the wrong area too."},
            {"text": "100 Pa", "correct": False,
             "why": "That shares the weight between the pallet and its feet. "
                    "All of it travels through whatever is touching."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h29",
        "band": "harder",
        "text": "A tracked machine sinks deeper into soft ground as it is "
                "loaded, although nothing about its tracks is altered. Why?",
        "options": [
            {"text": "The tracks spread out under a load, so less of them "
                     "touches", "correct": False,
             "why": "Tracks do not shrink under load, and the question says "
                    "they are unaltered."},
            {"text": "The weight rises while the track area stays the same, "
                     "so the pressure rises", "correct": True},
            {"text": "The load pushes the machine along, and moving machines "
                     "press harder", "correct": False,
             "why": "A load does not drive a machine forward, and standing "
                    "still gives the same pressure as moving."},
            {"text": "The ground gets softer as a machine stands on it for "
                     "longer", "correct": False,
             "why": "The question ties the sinking to the loading, and the "
                    "pressure is what the loading changes."},
        ],
        "figure": None,
    },
    {
        "id": "p5-01-h30",
        "band": "harder",
        "text": "A heavy crate is dragged across a floor instead of being left "
                "standing. Does that change the pressure it puts on the "
                "floor?",
        "options": [
            {"text": "Yes — dragging adds a force, so the pressure rises",
             "correct": False,
             "why": "The added force acts along the floor, and pressure uses "
                    "the force acting into it."},
            {"text": "Yes — a moving object presses more lightly, so the "
                     "pressure falls", "correct": False,
             "why": "Moving does not lift any weight off the floor."},
            {"text": "No — the force pressing into the floor and the area "
                     "touching it are both unchanged", "correct": True},
            {"text": "No — a pressure can only be worked out for something "
                     "standing still", "correct": False,
             "why": "The relationship holds whether the crate is moving or "
                    "not; nothing in it mentions motion."},
        ],
        "figure": None,
    },
]
