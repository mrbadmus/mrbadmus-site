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
            {"text": "To make the force pushing it bigger", "correct": False,
             "why": "The force is whatever your thumb supplies. Sharpening "
                    "changes no force anywhere."},
            {"text": "To make the metal harder", "correct": False,
             "why": "Hardness matters for a pin that has to survive, but it "
                    "is not why the point goes in."},
            {"text": "To concentrate the same force onto a tiny area, giving "
                     "a very high pressure", "correct": True},
            {"text": "To make the pin lighter", "correct": False,
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
            {"text": "They concentrate the weight into a smaller area, so it "
                     "presses through the soft layer.", "correct": False,
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
            {"text": "The pressure in the big cylinder is much higher.",
             "correct": False,
             "why": "The pressure is the SAME in both. What differs is the "
                    "area it acts on."},
            {"text": "There is no catch — force really is created.",
             "correct": False,
             "why": "Force can be multiplied; nothing is created. The energy "
                    "transferred is the same either way."},
            {"text": "The small piston has to move much further than the big "
                     "one, so the energy transferred is the same.",
             "correct": True},
            {"text": "The jack only works while the oil is warm.",
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
            {"text": "Nothing — a press on the ground is a force.",
             "correct": False,
             "why": "The press IS a force, but the quantity they were asked "
                    "for is how that force is spread out."},
            {"text": "The number is wrong; the unit is fine.",
             "correct": False,
             "why": "The arithmetic may be perfect. What is wrong is that a "
                    "pressure cannot be reported in newtons."},
            {"text": "They should divide by the area again to fix the unit.",
             "correct": False,
             "why": "The area has already been divided in. Dividing twice "
                    "would give a number that means nothing at all."},
            {"text": "Force ÷ area gives newtons per square metre, so the "
                     "unit should be Pa.", "correct": True},
        ],
        "figure": None,
    },
]
