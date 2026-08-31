"""P5 lesson 02 — Pressure in liquids: twelve questions (MRB-223).

Written against Design's page. The three holes in the can, the probe in
the tank and the stack of layers are hers.

The discriminations, in the order the lesson builds them:

  · depth is what decides it, not how much liquid there is (`PRESS-05`);
  · nothing about the water changes with depth (`PRESS-06`);
  · a liquid presses equally in EVERY direction (`PRESS-07`);
  · the width of the container is irrelevant (`PRESS-08`) — the harder
    band sits here and on the dam.

⚠️ POSITION IS AUTHORED — index cycles 3, 2, 1, 0, giving three of each.

⚠️ Rung 1 (0.05 m² face, 1500 N above) and Rung 2 (the pool and the pipe)
are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P5"
LESSON = "pressure-in-liquids"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p5-02-e01",
        "band": "easier",
        "text": "As you go deeper in a liquid, the pressure…",
        "options": [
            {"text": "stays the same", "correct": False,
             "why": "Then the three holes in the can would give identical "
                    "jets, and they do not."},
            {"text": "falls", "correct": False,
             "why": "The opposite. There is more liquid stacked above you, "
                    "so more weight is pressing."},
            {"text": "falls at first and then rises", "correct": False,
             "why": "It rises steadily the whole way down. Nothing turns "
                    "round partway."},
            {"text": "rises", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e02",
        "band": "easier",
        "text": "Why does water come out SIDEWAYS through a hole in the side "
                "of a can?",
        "options": [
            {"text": "Because the air pressing on the surface above drives "
                     "the water out of the hole",
             "correct": False,
             "why": "Air pressure acts on the surface, but the sideways jet "
                    "happens with an open can either way."},
            {"text": "Because the hole is lower than the surface, so the "
                     "water is aimed sideways out of it",
             "correct": False,
             "why": "Depth sets how FAST it comes out, not why it comes out "
                    "sideways rather than running down inside."},
            {"text": "Because a liquid presses equally in every direction, "
                     "including sideways on the wall", "correct": True},
            {"text": "Because the can squeezes the water and forces some "
                     "of it out through the hole", "correct": False,
             "why": "The can is rigid and is doing nothing. The push comes "
                    "from the water itself."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e03",
        "band": "easier",
        "text": "A probe 3 m down reads a certain pressure. It is raised to "
                "1.5 m. What does it read now?",
        "options": [
            {"text": "Twice as much", "correct": False,
             "why": "Half the depth means half the liquid above, so half the "
                    "pressure — not twice."},
            {"text": "The same", "correct": False,
             "why": "The depth has changed, and depth is the only thing "
                    "besides the liquid that sets the reading."},
            {"text": "Four times less", "correct": False,
             "why": "Nothing here is squared. Half the depth, half the "
                    "pressure."},
            {"text": "Half as much", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e04",
        "band": "easier",
        "text": "The pressure at a depth is worked out as…",
        "options": [
            {"text": "the weight of the liquid above ÷ the area it presses "
                     "on", "correct": True},
            {"text": "the weight of all the liquid in the tank ÷ the area of "
                     "the tank floor", "correct": False,
             "why": "Only the liquid ABOVE your patch is resting on it. The "
                    "rest is resting on its own."},
            {"text": "the depth × the area", "correct": False,
             "why": "That has no force in it at all, and multiplying a depth "
                    "by an area gives a volume."},
            {"text": "the area ÷ the weight of the liquid above",
             "correct": False,
             "why": "That is the division upside down. Pressure asks how "
                    "much force each square metre carries."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p5-02-s01",
        "band": "standard",
        "text": "A hatch has 900 N of water above it and an area of 0.03 m². "
                "What is the pressure on it?",
        "options": [
            {"text": "27 Pa", "correct": False,
             "why": "That is 900 × 0.03. To find a pressure the weight is "
                    "shared out over the area, so you divide."},
            {"text": "0.000033 Pa", "correct": False,
             "why": "That is 0.03 ÷ 900 — the division the wrong way "
                    "round."},
            {"text": "30 000 Pa", "correct": True},
            {"text": "30 000 N", "correct": False,
             "why": "The arithmetic is right and the unit is wrong. Newtons "
                    "divided by square metres gives pascals."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s02",
        "band": "standard",
        "text": "A narrow tube of water 3 m tall stands next to a wide tank "
                "of water 3 m deep. Where is the pressure greater at the "
                "bottom?",
        "options": [
            {"text": "The tank, because it holds far more water.",
             "correct": False,
             "why": "The extra water is sitting on its own patch of floor, "
                    "not on yours. Above any one square metre there is 3 m "
                    "in both."},
            {"text": "The tube, because the water is squeezed into a narrow "
                     "space.", "correct": False,
             "why": "Nothing is being squeezed. Each square metre of the "
                    "tube's base carries the column directly above it."},
            {"text": "The same in both.", "correct": True},
            {"text": "It depends which liquid is in each.", "correct": False,
             "why": "True in general — but the question says water in both, "
                    "so the only remaining variable is the depth, and it "
                    "matches."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s03",
        "band": "standard",
        "text": "The same probe is lowered to 2 m in water and then to 2 m "
                "in paraffin, which is lighter for its size. What happens to "
                "the reading?",
        "options": [
            {"text": "It goes up, because paraffin flows more easily.",
             "correct": False,
             "why": "How easily a liquid flows is not what sets the "
                    "pressure. The weight of the column above is."},
            {"text": "It stays the same, because the depth is the same and "
                     "nothing else in the tank has changed",
             "correct": False,
             "why": "Depth is one of two things that matter. The other is "
                    "the liquid, and it has changed."},
            {"text": "It goes down, because a column of paraffin weighs less "
                     "than the same column of water.", "correct": True},
            {"text": "It drops to zero, because paraffin floats.",
             "correct": False,
             "why": "There is a full 2 m of paraffin above the probe and it "
                    "has real weight. The reading falls; it does not "
                    "vanish."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s04",
        "band": "standard",
        "text": "Why is a water tower built tall rather than wide?",
        "options": [
            {"text": "So it can hold more water.", "correct": False,
             "why": "A wide tank holds more for the same height, and gives "
                    "no more pressure at the tap."},
            {"text": "Because the pressure at the taps comes from the HEIGHT "
                     "of the water above them, not from how many litres it "
                     "holds.", "correct": True},
            {"text": "So the water stays colder at the top, where the wall "
                     "is thinnest and the pressure is least, and cold water "
                     "presses less",
             "correct": False,
             "why": "Temperature is a separate matter and is not why the "
                    "shape is chosen."},
            {"text": "So the weight is spread over less ground.",
             "correct": False,
             "why": "A tall tower puts MORE pressure on its footings, not "
                    "less. The height is for the supply, not the base."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p5-02-h01",
        "band": "harder",
        "text": "Why is a concrete dam thin at the top and thick at the "
                "base?",
        "options": [
            {"text": "Because the water at the base is heavier.",
             "correct": False,
             "why": "A litre from the base weighs what a litre from the top "
                    "weighs. What differs is how much is stacked above."},
            {"text": "Because the base has to carry the weight of the wall "
                     "above it, and the water is not the reason.",
             "correct": False,
             "why": "That is a real load too, but the shape follows the "
                    "water pressure, which grows with depth."},
            {"text": "Because the water presses sideways on the wall harder "
                     "the deeper it is.", "correct": True},
            {"text": "Because the base is under more of the reservoir's "
                     "surface area.", "correct": False,
             "why": "The surface area of the reservoir does not enter it. "
                    "Only the depth at each point does."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h02",
        "band": "harder",
        "text": "A probe at the surface of the tank reads 0 Pa. Does that "
                "mean nothing is pressing on it?",
        "options": [
            {"text": "Yes — 0 Pa means no push at all.", "correct": False,
             "why": "The probe reports the LIQUID only. It is reading zero "
                    "liquid above it, not zero pressure."},
            {"text": "Yes, because there is no water above it.",
             "correct": False,
             "why": "The first half is right and the conclusion is not. The "
                    "atmosphere is still pressing on the surface."},
            {"text": "No — the atmosphere is pressing on the surface too, "
                     "and adds about 100 000 Pa everywhere in the tank.",
             "correct": True},
            {"text": "No, because a probe can never read a true zero "
                     "however carefully it is made or wherever it is placed",
             "correct": False,
             "why": "It can, and it is reading one honestly — for the "
                    "quantity it measures."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h03",
        "band": "harder",
        "text": "Deep-sea vehicles use a SPHERE for the crew rather than a "
                "box. Why?",
        "options": [
            {"text": "A sphere holds more for its size.", "correct": False,
             "why": "It does, but that is not what keeps the crew alive at "
                    "depth."},
            {"text": "A sphere is easier to make out of thick metal than "
                     "any other shape is, so deep-sea vessels are built "
                     "that way",
             "correct": False,
             "why": "It is considerably harder. The shape is chosen despite "
                    "that."},
            {"text": "A sphere sinks more slowly.", "correct": False,
             "why": "Sinking is decided by weight against upthrust, not by "
                    "whether the hull is round."},
            {"text": "A sphere has no flat side for the water to work on, so "
                     "the push is carried evenly all the way round.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h04",
        "band": "harder",
        "text": "Blood pressure is quoted in millimetres of mercury. What "
                "does that tell you about how it is measured?",
        "options": [
            {"text": "That mercury is injected into the patient.",
             "correct": False,
             "why": "It certainly is not. The mercury is in the instrument."},
            {"text": "That a pressure can be reported as the HEIGHT of a "
                     "liquid column it would hold up.", "correct": True},
            {"text": "That blood is measured by weighing it.",
             "correct": False,
             "why": "Nothing is weighed. A height is read off a scale."},
            {"text": "That blood pressure is not a real pressure, only a "
                     "number doctors have agreed on",
             "correct": False,
             "why": "It is, and it could be quoted in pascals. The mercury "
                    "unit survives because the instrument did."},
        ],
        "figure": None,
    },
]
