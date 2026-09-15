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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p5-02-e05",
        "band": "easier",
        "text": "The pressure at a point in a liquid depends on…",
        "options": [
            {"text": "the depth and which liquid it is", "correct": True},
            {"text": "how much liquid there is altogether", "correct": False,
             "why": "A thin tube and a wide tank at the same depth give the "
                    "same pressure."},
            {"text": "how wide the container is", "correct": False,
             "why": "Width changes how much liquid there is, and that is not "
                    "what sets the pressure."},
            {"text": "the shape of the container's base", "correct": False,
             "why": "The base's shape makes no difference; the depth above it "
                    "does."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e06",
        "band": "easier",
        "text": "At one depth in a liquid, the pressure acts…",
        "options": [            {"text": "downwards only", "correct": False,
             "why": "Water squirts sideways out of a hole in a can, so it "
                    "clearly pushes that way too."},
            {"text": "in whichever direction the liquid is flowing",
             "correct": False,
             "why": "Still water in a sealed tank presses in every direction "
                    "without flowing anywhere."},
            {"text": "sideways only", "correct": False,
             "why": "It pushes down on the base of a tank as well, so it is "
                    "not sideways only."},
            {"text": "equally in every direction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e07",
        "band": "easier",
        "text": "Why does the pressure in a liquid increase with depth?",
        "options": [
            {"text": "Because the liquid is squeezed tighter lower down",
             "correct": False,
             "why": "Water is very hard to squash, and its spacing barely "
                    "changes with depth."},
            {"text": "Because the liquid is heavier lower down",
             "correct": False,
             "why": "Every part of it weighs the same for its size; what "
                    "changes is how much is stacked above."},
            {"text": "Because more liquid is stacked above, adding its weight",
             "correct": True},
            {"text": "Because gravity is stronger further down",
             "correct": False,
             "why": "Gravity is effectively the same throughout a tank or "
                    "even an ocean."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e08",
        "band": "easier",
        "text": "A diver swims from 5 m down to 20 m down. The pressure on "
                "them…",
        "options": [
            {"text": "stays the same, because it is the same water",
             "correct": False,
             "why": "The depth is what decides it, and the depth has "
                    "quadrupled."},
            {"text": "falls, because there is more room lower down",
             "correct": False,
             "why": "There is more water above, not more room, so the "
                    "pressure rises."},
            {"text": "rises, because there is more water above",
             "correct": True},
            {"text": "rises only if the water is salty", "correct": False,
             "why": "Salt water raises it further, but the pressure rises "
                    "with depth in any liquid."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e09",
        "band": "easier",
        "text": "Does making a container wider change the pressure at its "
                "base?",
        "options": [
            {"text": "Yes, because a wider base holds more water",
             "correct": False,
             "why": "It does hold more, and the extra sits over extra base, "
                    "so the pressure is unchanged."},
            {"text": "Yes, because the weight is spread more thinly",
             "correct": False,
             "why": "Both the weight and the area grow together, leaving the "
                    "pressure where it was."},
            {"text": "No — only the depth and the liquid matter",
             "correct": True},
            {"text": "No, because pressure does not act on a base at all",
             "correct": False,
             "why": "It certainly acts there; it simply does not depend on "
                    "how wide the base is."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e10",
        "band": "easier",
        "text": "A reading that counts the liquid alone and leaves out the "
                "air pressing on the surface is called…",
        "options": [            {"text": "atmospheric pressure", "correct": False,
             "why": "That is the air's own push, which is exactly what this "
                    "reading leaves out."},
            {"text": "depth", "correct": False,
             "why": "Depth is a distance in metres; the reading is a pressure "
                    "in pascals."},
            {"text": "upthrust", "correct": False,
             "why": "Upthrust is an upward force in newtons, not a pressure "
                    "reading."},
            {"text": "gauge pressure", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e11",
        "band": "easier",
        "text": "Two holes are made in a full can, one near the top and one "
                "near the base. Which jet travels furthest?",
        "options": [
            {"text": "The one near the base", "correct": True},
            {"text": "The one near the top", "correct": False,
             "why": "There is less water above it, so it is pushed out at a "
                    "lower pressure."},
            {"text": "They travel the same distance", "correct": False,
             "why": "The pressures differ, because the depths differ."},
            {"text": "Neither — water only falls straight down from a hole",
             "correct": False,
             "why": "The liquid pushes sideways too, which is what drives the "
                    "jet outwards."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e12",
        "band": "easier",
        "text": "The water above a probe face of 0.04 m² weighs 1200 N. What "
                "is the pressure on the face?",
        "options": [            {"text": "48 Pa", "correct": False,
             "why": "That is 1200 × 0.04, a multiplication where the formula "
                    "divides."},
            {"text": "1200 Pa", "correct": False,
             "why": "That is the weight in newtons with the unit changed; the "
                    "area still has to be divided in."},
            {"text": "0.000033 Pa", "correct": False,
             "why": "That is 0.04 ÷ 1200, the ratio upside down."},
            {"text": "30 000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e13",
        "band": "easier",
        "text": "A manometer tells you a pressure from…",
        "options": [
            {"text": "the height of a column of liquid", "correct": True},
            {"text": "the weight of the whole instrument", "correct": False,
             "why": "Its own weight is irrelevant; the liquid column is what "
                    "is read."},
            {"text": "the temperature of the liquid inside it",
             "correct": False,
             "why": "Temperature is read on a thermometer and is a different "
                    "quantity altogether."},
            {"text": "the width of the tube it is made from", "correct": False,
             "why": "Width does not change the pressure a column gives, which "
                    "is why the instrument works at all."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p5-02-s05",
        "band": "standard",
        "text": "A hatch of area 0.05 m² has 2000 N of water standing above "
                "it. What is the pressure on it?",
        "options": [            {"text": "100 Pa", "correct": False,
             "why": "That is 2000 × 0.05, a multiplication where the formula "
                    "divides."},
            {"text": "2000 Pa", "correct": False,
             "why": "That is the weight with the unit swapped; the area has "
                    "to be divided in."},
            {"text": "0.000025 Pa", "correct": False,
             "why": "That is 0.05 ÷ 2000, the ratio the wrong way up."},
            {"text": "40 000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s06",
        "band": "standard",
        "text": "A pressure of 20 000 Pa acts on a hatch of 0.30 m². What "
                "force does the hatch take?",
        "options": [
            {"text": "6000 N", "correct": True},
            {"text": "66 700 N", "correct": False,
             "why": "That is 20 000 ÷ 0.30, dividing where the rearrangement "
                    "multiplies."},
            {"text": "20 000 N", "correct": False,
             "why": "That is the pressure read as a force; the area still has "
                    "to be multiplied in."},
            {"text": "0.000015 N", "correct": False,
             "why": "That is 0.30 ÷ 20 000, which is neither the formula nor "
                    "its rearrangement."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s07",
        "band": "standard",
        "text": "A probe at 4 m deep reads 40 000 Pa. What would it read at "
                "2 m in the same liquid?",
        "options": [
            {"text": "40 000 Pa, because it is the same liquid",
             "correct": False,
             "why": "The liquid is the same, but half the depth means half "
                    "the weight above."},
            {"text": "80 000 Pa", "correct": False,
             "why": "That doubles it; coming shallower reduces the pressure "
                    "rather than raising it."},
            {"text": "20 000 Pa", "correct": True},
            {"text": "10 000 Pa", "correct": False,
             "why": "That quarters it. Halving the depth halves the "
                    "pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s08",
        "band": "standard",
        "text": "Why must a submarine's hull be far stronger for 300 m than "
                "for 30 m?",
        "options": [            {"text": "Because the water is colder that far down",
             "correct": False,
             "why": "Temperature does change with depth, but it is the "
                    "pressure the hull has to resist."},
            {"text": "Because the ocean is wider at that depth",
             "correct": False,
             "why": "How wide the ocean is makes no difference; the depth "
                    "above the hull does."},
            {"text": "Because there is less oxygen dissolved that far down",
             "correct": False,
             "why": "Dissolved gas has nothing to do with the force on the "
                    "hull."},
            {"text": "Because the pressure there is about ten times as great",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s09",
        "band": "standard",
        "text": "Why is the thickness a dam needs decided by depth rather "
                "than by the size of the lake behind it?",
        "options": [            {"text": "Because a large lake spreads its weight over the whole "
                     "valley floor",
             "correct": False,
             "why": "True but beside the point: the pressure on the dam "
                    "depends on depth alone."},
            {"text": "Because the amount of water in a lake changes with the "
                     "weather",
             "correct": False,
             "why": "It does, but even a fixed volume would not set the "
                    "pressure — only the depth does."},
            {"text": "Because a small lake would freeze and a large one would "
                     "not",
             "correct": False,
             "why": "Freezing is a separate engineering worry and is not what "
                    "sets the thickness."},
            {"text": "Because the pressure on the dam depends on depth, not "
                     "on the amount",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s10",
        "band": "standard",
        "text": "Two tanks hold water to the same depth, but one holds ten "
                "times as much. Compare the pressures at their bases.",
        "options": [
            {"text": "The larger tank's base takes ten times the pressure",
             "correct": False,
             "why": "Ten times the water sits over ten times the base, "
                    "leaving the pressure unchanged."},
            {"text": "The smaller tank's base takes the greater pressure",
             "correct": False,
             "why": "Nothing concentrates the pressure in a narrow container; "
                    "the depths are equal, so the pressures are."},
            {"text": "They are equal at both bases", "correct": True},
            {"text": "It cannot be said without knowing the shapes",
             "correct": False,
             "why": "Shape does not enter into it. Equal depth in the same "
                    "liquid means equal pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s11",
        "band": "standard",
        "text": "Mercury is far denser than water. At the same depth in each, "
                "which gives the greater pressure?",
        "options": [            {"text": "Water, because it flows more easily", "correct": False,
             "why": "How easily a liquid flows does not set its pressure; how "
                    "much a given volume weighs does."},
            {"text": "It depends on how much of each liquid there is",
             "correct": False,
             "why": "Total amount never enters into it — only depth and the "
                    "liquid itself."},
            {"text": "They are the same, because the depth is the same",
             "correct": False,
             "why": "Depth is one of the two things that matter; which liquid "
                    "it is, is the other."},
            {"text": "Mercury, because it is denser", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s12",
        "band": "standard",
        "text": "Why is the pressure on the SIDE wall of a tank greatest near "
                "the bottom?",
        "options": [
            {"text": "Because the water gathers at the bottom of the tank and "
                     "presses there",
             "correct": False,
             "why": "The water fills the tank; what varies is how much of it "
                    "is above each point."},
            {"text": "Because the base supports the wall there",
             "correct": False,
             "why": "What supports the wall does not change what pushes on "
                    "it."},
            {"text": "Because the depth is greatest there, and pressure acts "
                     "sideways",
             "correct": True},
            {"text": "Because the water is moving fastest near the bottom",
             "correct": False,
             "why": "Still water in a sealed tank presses hardest at the "
                    "bottom without moving at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s13",
        "band": "standard",
        "text": "A student writes that water is packed tighter deep down, "
                "which is why the pressure is higher. What is right?",
        "options": [
            {"text": "The packing is right, but it is the temperature that "
                     "causes it to happen",
             "correct": False,
             "why": "Neither half holds: water barely compresses, whatever "
                    "the temperature."},
            {"text": "Water hardly squashes at all; more water above raises "
                     "the pressure",
             "correct": True},
            {"text": "Water really is packed tighter, by about a tenth at "
                     "50 m",
             "correct": False,
             "why": "The change even at great depth is far too small to "
                    "explain the pressure."},
            {"text": "The student is right, which is why deep water is "
                     "denser",
             "correct": False,
             "why": "Deep water is very nearly the same density as shallow "
                    "water."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p5-02-h05",
        "band": "harder",
        "text": "A tank is 3 m deep and the pressure at its base is "
                "30 000 Pa. What is the pressure 1 m above the base?",
        "options": [
            {"text": "10 000 Pa", "correct": False,
             "why": "That is the pressure 1 m BELOW the surface, not 1 m "
                    "above the base."},
            {"text": "20 000 Pa", "correct": True},
            {"text": "30 000 Pa", "correct": False,
             "why": "The pressure falls as you rise, so it cannot still be "
                    "the base value."},
            {"text": "29 999 Pa", "correct": False,
             "why": "A whole metre of water is a third of the tank, so the "
                    "change is large, not tiny."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h06",
        "band": "harder",
        "text": "A hatch measuring 0.60 m by 0.50 m sits where the pressure "
                "is 50 000 Pa. What force must it withstand?",
        "options": [
            {"text": "55 000 N", "correct": False,
             "why": "That adds the pressure to something; force is pressure "
                    "MULTIPLIED by area."},
            {"text": "1.1 m²", "correct": False,
             "why": "That adds the two side lengths, and the answer wanted is "
                    "a force in newtons."},
            {"text": "15 000 N", "correct": True},
            {"text": "166 667 N", "correct": False,
             "why": "That is 50 000 ÷ 0.30, dividing where the calculation "
                    "multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h07",
        "band": "harder",
        "text": "A thin pipe of water rising 10 m above a sealed barrel can "
                "burst it, though the pipe holds only a few litres. Why?",
        "options": [
            {"text": "Because the narrow pipe concentrates the water's weight "
                     "onto the barrel",
             "correct": False,
             "why": "Nothing is concentrated; a wide column 10 m tall gives "
                    "exactly the same pressure."},
            {"text": "Because the water in a thin pipe is denser",
             "correct": False,
             "why": "It is the same water at the same density, whatever the "
                    "pipe's width."},
            {"text": "Because the water falls a long way and gains speed",
             "correct": False,
             "why": "The water is standing still; the pressure is there "
                    "whether it flows or not."},
            {"text": "Because pressure is set by the height, not the amount "
                     "of water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h08",
        "band": "harder",
        "text": "A pressure probe at one depth is turned to face upwards, "
                "then sideways, then downwards. What happens to the reading?",
        "options": [
            {"text": "It is largest facing downwards, because pressure pushes "
                     "down",
             "correct": False,
             "why": "At one depth the liquid pushes equally in every "
                    "direction, so the facing does not matter."},
            {"text": "It stays the same in all three positions",
             "correct": True},
            {"text": "It is largest facing upwards, because the water above "
                     "presses on it",
             "correct": False,
             "why": "The water above sets the size of the pressure, but that "
                    "pressure then acts every way at once."},
            {"text": "It falls to zero when the probe faces sideways",
             "correct": False,
             "why": "A jet squirting sideways from a can shows there is "
                    "plenty of sideways push."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h09",
        "band": "harder",
        "text": "A lock gate holds 5 m of water on one side and 2 m on the "
                "other. Where is the net push on it greatest?",
        "options": [
            {"text": "At the top, where the gate is thinnest",
             "correct": False,
             "why": "How thick the gate is does not set the push on it; the "
                    "depths on either side do."},
            {"text": "Halfway up, where the two depths average out",
             "correct": False,
             "why": "There is no averaging: the difference in pressure grows "
                    "all the way down."},
            {"text": "Near the bottom, pushing towards the shallow side",
             "correct": True},
            {"text": "Near the bottom, pushing towards the deep side",
             "correct": False,
             "why": "The deeper water pushes harder, so the gate is driven "
                    "the other way."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h10",
        "band": "harder",
        "text": "Why does a pipe of water 10 m tall press on its base as hard "
                "as a swimming pool 10 m deep?",
        "options": [
            {"text": "Because the pipe holds so little water that it presses "
                     "harder for its size",
             "correct": False,
             "why": "Nothing presses harder for its size; the depth is what "
                    "sets the pressure."},
            {"text": "Because both are made of the same water",
             "correct": False,
             "why": "Same liquid is one of the two conditions; the equal "
                    "depth is the other, and both are needed."},
            {"text": "Because the pool spreads its weight over a base big "
                     "enough to cancel out",
             "correct": False,
             "why": "It does spread it, and that is why the total weight "
                    "never enters the calculation."},
            {"text": "Because pressure depends on depth and the liquid, and "
                     "nothing else",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h11",
        "band": "harder",
        "text": "A student predicts three jets from three holes down a can "
                "will look identical. What will they actually see?",
        "options": [
            {"text": "All three the same, because it is one can of water",
             "correct": False,
             "why": "One can, but three different depths, and depth is what "
                    "sets the pressure."},
            {"text": "The top jet furthest, because it has furthest to fall",
             "correct": False,
             "why": "Falling distance is not what drives the jet out; the "
                    "pressure at the hole is."},
            {"text": "The bottom jet furthest, because the pressure is "
                     "greatest there",
             "correct": True},
            {"text": "Only the bottom jet flowing, because the others are too "
                     "high",
             "correct": False,
             "why": "All three flow while there is water above them; they "
                    "simply flow at different rates."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h12",
        "band": "harder",
        "text": "Two identical fish swim at 5 m down — one in a lake, one in "
                "the sea. Which meets the greater pressure?",
        "options": [
            {"text": "The lake fish, because fresh water is thinner and "
                     "presses harder",
             "correct": False,
             "why": "Thinner means less weight for the same volume, so it "
                    "presses less."},
            {"text": "The sea fish, because salt water is denser",
             "correct": True},
            {"text": "They meet the same pressure, because the depth is the "
                     "same",
             "correct": False,
             "why": "Depth is only half the answer; which liquid it is "
                    "matters too."},
            {"text": "The sea fish, because the sea is much larger",
             "correct": False,
             "why": "Right answer, wrong reason: the total amount of water "
                    "never enters the calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h13",
        "band": "harder",
        "text": "Why is the water pressure at a tap on the ground floor "
                "higher than at one on the top floor of the same building?",
        "options": [
            {"text": "Because the pipe is wider lower down", "correct": False,
             "why": "Pipe width does not set the pressure; the height of "
                    "water above the tap does."},
            {"text": "Because water gathers at the bottom of the building "
                     "over time",
             "correct": False,
             "why": "The pipes are full at both taps; what differs is the "
                    "depth below the tank."},
            {"text": "Because the ground-floor tap is further below the tank",
             "correct": True},
            {"text": "Because gravity is stronger at ground level",
             "correct": False,
             "why": "The difference in gravity over a few floors is far too "
                    "small to notice."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p5-02-e14",
        "band": "easier",
        "text": "Which change would double the pressure at the bottom of a "
                "tank of water?",
        "options": [
            {"text": "Doubling the depth of the water", "correct": True},
            {"text": "Doubling the width of the tank", "correct": False,
             "why": "A wider tank puts the extra water over extra base, so "
                    "each square metre carries what it did before."},
            {"text": "Doubling the area of the tank's base", "correct": False,
             "why": "The base area cancels out: twice the area carries twice "
                    "the water, at the same pressure."},
            {"text": "Doubling the thickness of the tank's walls",
             "correct": False,
             "why": "Thicker walls change what the tank can survive, not what "
                    "the water pushes with."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e15",
        "band": "easier",
        "text": "Water is poured into a container made of a wide arm and a "
                "narrow arm joined at the base. Where does it settle?",
        "options": [
            {"text": "Higher in the narrow arm", "correct": False,
             "why": "A taller column in the narrow arm would press harder at "
                    "the join, and the water would flow back."},
            {"text": "Higher in the wide arm", "correct": False,
             "why": "The wide arm's extra weight sits over extra base, so it "
                    "presses no harder at the join."},
            {"text": "All of it in the wide arm", "correct": False,
             "why": "Water is not drawn towards the roomier side. It settles "
                    "where the pressures at the join match."},
            {"text": "At the same level in both arms", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e16",
        "band": "easier",
        "text": "Two points in one tank of water are the same distance below "
                "the surface, but at opposite ends. Compare the pressures.",
        "options": [
            {"text": "Greater at the end nearer the tank's wall",
             "correct": False,
             "why": "A wall neither adds to nor takes from the water above a "
                    "point."},
            {"text": "The two are equal", "correct": True},
            {"text": "Greater at the end with more water beside it",
             "correct": False,
             "why": "Water beside a point rests on its own patch of floor, "
                    "not on that point."},
            {"text": "It depends which end the tank was filled from",
             "correct": False,
             "why": "Once the water is still, how it got in leaves no trace "
                    "on the pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e17",
        "band": "easier",
        "text": "When a pressure in a liquid is worked out, the depth of a "
                "point means…",
        "options": [
            {"text": "how far above the base of the container it sits",
             "correct": False,
             "why": "Measured from the base, a deeper point would give a "
                    "smaller figure, and the pressure would come out "
                    "backwards."},
            {"text": "how wide the container is at that point", "correct": False,
             "why": "Width is a distance across, and it makes no difference "
                    "to the pressure."},
            {"text": "how far below the surface it sits", "correct": True},
            {"text": "how many litres of liquid the container holds",
             "correct": False,
             "why": "A volume is not a depth, and the total held is what the "
                    "pressure does not depend on."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p5-02-s14",
        "band": "standard",
        "text": "A probe is swapped for one with a much larger face and held "
                "at the same depth in the same tank. What does it read?",
        "options": [
            {"text": "More, because a bigger face has more water sitting on "
                     "it", "correct": False,
             "why": "It carries more water AND has more area for that water "
                    "to press on, so the two grow together."},
            {"text": "Less, because the weight above is shared over a bigger "
                     "face", "correct": False,
             "why": "The weight above grows with the face, so nothing is "
                    "shared more thinly than before."},
            {"text": "Less, because a large face is harder for water to push "
                     "on", "correct": False,
             "why": "Water pushes on every square metre of it just as hard as "
                    "on a small face."},
            {"text": "The same, because the extra weight is spread over the "
                     "extra area", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s15",
        "band": "standard",
        "text": "A diving bell has a window of 0.25 m². At the depth it is "
                "working, the water pressure is 80 000 Pa. What force is on "
                "the window?",
        "options": [
            {"text": "20 000 N", "correct": True},
            {"text": "320 000 N", "correct": False,
             "why": "That is 80 000 ÷ 0.25, dividing where the rearrangement "
                    "multiplies."},
            {"text": "80 000 N", "correct": False,
             "why": "That is the pressure read as a force, before the window "
                    "area has been multiplied in."},
            {"text": "0.0000031 N", "correct": False,
             "why": "That is 0.25 ÷ 80 000, which matches neither the formula "
                    "nor its rearrangement."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s16",
        "band": "standard",
        "text": "A pool is 1 m deep at the shallow end and 3 m deep at the "
                "other. How do the pressures on the floor compare?",
        "options": [
            {"text": "The same at both ends, because it is one pool of water",
             "correct": False,
             "why": "One pool, but two depths, and depth is what sets the "
                    "pressure."},
            {"text": "Twice as great at the deep end", "correct": False,
             "why": "The depth is three times as great, and the pressure "
                    "follows the depth."},
            {"text": "Three times as great at the deep end", "correct": True},
            {"text": "Nine times as great at the deep end", "correct": False,
             "why": "Nothing here is squared: three times the depth gives "
                    "three times the pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s17",
        "band": "standard",
        "text": "A probe 5 m down in an open tank reads 50 000 Pa of liquid "
                "pressure. What is the total pressure on its face?",
        "options": [
            {"text": "About 50 000 Pa", "correct": False,
             "why": "That is the probe's own reading. It measures the liquid "
                    "alone, and the air on the surface is pressing as well."},
            {"text": "About 150 000 Pa", "correct": True},
            {"text": "About 100 000 Pa", "correct": False,
             "why": "That treats the air as replacing the liquid reading. It "
                    "adds to it rather than standing in for it."},
            {"text": "About 25 000 Pa", "correct": False,
             "why": "Nothing is halved. The air's push is added to the "
                    "liquid's, not split with it."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p5-02-h14",
        "band": "harder",
        "text": "A pipe 20 m tall stands full of water above a valve of area "
                "0.02 m². Water gives 10 000 Pa for every metre of depth. "
                "What force is on the valve?",
        "options": [
            {"text": "200 000 N", "correct": False,
             "why": "200 000 is the pressure in pascals. It still has to be "
                    "multiplied by the valve's area."},
            {"text": "4000 N", "correct": True},
            {"text": "200 N", "correct": False,
             "why": "That uses one metre of water rather than the full 20 m "
                    "standing above the valve."},
            {"text": "10 000 000 N", "correct": False,
             "why": "That divides the pressure by the area, where the "
                    "rearrangement multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h15",
        "band": "harder",
        "text": "A U-shaped tube holds water in one arm and cooking oil in "
                "the other. The oil stands taller. Why?",
        "options": [
            {"text": "Oil is stickier, so it climbs further up the glass",
             "correct": False,
             "why": "Sticking to glass lifts a liquid a millimetre or two, "
                    "nowhere near the difference seen here."},
            {"text": "Oil floats, so it is pushed upwards out of the tube",
             "correct": False,
             "why": "The two are in separate arms and are not stacked, so "
                    "neither floats on the other."},
            {"text": "Oil weighs less for its size, so a taller column is "
                     "needed to press as hard", "correct": True},
            {"text": "Oil flows more slowly, so it has not finished settling "
                     "yet", "correct": False,
             "why": "The difference stays for as long as you watch, so it is "
                    "not a liquid still on the move."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h16",
        "band": "harder",
        "text": "A probe reads 30 000 Pa at 3 m down in water. Paraffin "
                "weighs 800 kg per cubic metre against water's 1000. At what "
                "depth in paraffin would it read the same?",
        "options": [
            {"text": "3.75 m", "correct": True},
            {"text": "2.4 m", "correct": False,
             "why": "That takes four fifths of the depth. A lighter liquid "
                    "needs a deeper column, not a shallower one."},
            {"text": "3 m", "correct": False,
             "why": "Equal depths in the two liquids give different "
                    "pressures, which is why the question can be asked."},
            {"text": "24 m", "correct": False,
             "why": "That multiplies the depth by eight, reading the 800 as a "
                    "factor rather than as a comparison with 1000."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h17",
        "band": "harder",
        "text": "A tank holds water 4 m deep. One hatch sits in the base and "
                "an identical one in the side wall, 1 m below the surface. "
                "Which takes the greater force?",
        "options": [
            {"text": "The side hatch, because a wall is pushed harder than a "
                     "floor", "correct": False,
             "why": "A liquid pushes as hard sideways as downwards at one "
                    "depth, so the wall gains nothing from being a wall."},
            {"text": "Neither, because the two hatches are the same size",
             "correct": False,
             "why": "Equal areas at unequal depths take unequal forces, "
                    "because the pressures differ."},
            {"text": "The side hatch, because the water above it has further "
                     "to fall", "correct": False,
             "why": "Nothing is falling. The pressure comes from the weight "
                    "of water standing above the point."},
            {"text": "The base hatch, because it is deeper and the pressure "
                     "there is greater", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · easier ─────────────────────────────
    {
        "id": "p5-02-e18",
        "band": "easier",
        "text": "Going down through water, roughly how much does the pressure "
                "rise for every metre?",
        "options": [
            {"text": "About 10 000 Pa", "correct": True},
            {"text": "About 10 Pa", "correct": False,
             "why": "10 Pa is the push of a layer a millimetre thick, not a "
                    "whole metre of water."},
            {"text": "About 1000 Pa", "correct": False,
             "why": "That is a tenth of the real figure, which would make a "
                    "10 m dive feel like 1 m."},
            {"text": "About 1 000 000 Pa", "correct": False,
             "why": "That much would be reached at about 100 m down, not "
                    "after one metre."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e19",
        "band": "easier",
        "text": "Water gives 10 000 Pa for each metre of depth. What is the "
                "pressure on a probe 6 m down?",
        "options": [
            {"text": "1667 Pa", "correct": False,
             "why": "That divides where the two figures should be "
                    "multiplied."},
            {"text": "60 000 Pa", "correct": True},
            {"text": "10 006 Pa", "correct": False,
             "why": "That adds the depth on, and a distance cannot be added "
                    "to a pressure."},
            {"text": "6 Pa", "correct": False,
             "why": "That is the depth in metres with a pressure unit written "
                    "after it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e20",
        "band": "easier",
        "text": "A tank is drained until the water standing in it is half as "
                "deep. The pressure on its base…",
        "options": [
            {"text": "stays the same", "correct": False,
             "why": "The tank is the same and the depth of water above the "
                    "base is not."},
            {"text": "doubles", "correct": False,
             "why": "The space left above the water presses with nothing; it "
                    "is the liquid above a point that counts."},
            {"text": "halves", "correct": True},
            {"text": "falls to a quarter", "correct": False,
             "why": "Nothing here is squared: half the depth gives half the "
                    "pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e21",
        "band": "easier",
        "text": "A builder fills a long clear hose with water and holds both "
                "ends up to mark two heights. Why does that work?",
        "options": [
            {"text": "Because water flows to whichever end is warmer",
             "correct": False,
             "why": "Temperature does not decide where water settles; the "
                    "pressures at the bottom do."},
            {"text": "Because a hose keeps water at whatever height it was "
                     "poured in at", "correct": False,
             "why": "Water moves freely inside the hose until the two columns "
                    "press equally."},
            {"text": "Because the water is pushed along by the builder's grip "
                     "on the ends", "correct": False,
             "why": "Nothing is being squeezed; the water settles on its own "
                    "once it is still."},
            {"text": "Because water settles at the same level at both open "
                     "ends", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e22",
        "band": "easier",
        "text": "Counting the liquid alone, what is the pressure right at the "
                "surface of a tank of water?",
        "options": [
            {"text": "Zero", "correct": True},
            {"text": "10 000 Pa", "correct": False,
             "why": "That is one metre's worth of water, and no water at all "
                    "stands above the surface."},
            {"text": "100 000 Pa", "correct": False,
             "why": "That is roughly the air's own push, which a reading of "
                    "the liquid alone leaves out."},
            {"text": "Half the base value", "correct": False,
             "why": "Half the base pressure is found halfway down, not at the "
                    "top."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e23",
        "band": "easier",
        "text": "One cubic metre of water has a mass of 1000 kg. Taking "
                "gravity as 10 N/kg, what does it weigh?",
        "options": [
            {"text": "100 N", "correct": False,
             "why": "That divides by 10 where the two figures should be "
                    "multiplied."},
            {"text": "10 000 N", "correct": True},
            {"text": "1000 N", "correct": False,
             "why": "That is the mass in kilograms with a newton written "
                    "after it; the 10 N/kg is still to be used."},
            {"text": "1010 N", "correct": False,
             "why": "That adds the two figures, and a mass cannot be added to "
                    "a gravity value."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e24",
        "band": "easier",
        "text": "Two hatches sit at the same depth in a tank, but one has "
                "twice the area of the other. Compare the forces on them.",
        "options": [
            {"text": "The same force on both", "correct": False,
             "why": "The pressure is the same, and the bigger hatch has twice "
                    "as many square metres for it to act on."},
            {"text": "The smaller hatch takes twice the force",
             "correct": False,
             "why": "Nothing concentrates onto a smaller hatch; each square "
                    "metre takes the same share."},
            {"text": "The bigger hatch takes twice the force", "correct": True},
            {"text": "The bigger hatch takes half the force", "correct": False,
             "why": "Spreading the same pressure over more area gives more "
                    "total force, not less."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e25",
        "band": "easier",
        "text": "Three metres down, a liquid gives 24 000 Pa. What does nine "
                "metres down give?",
        "options": [
            {"text": "8000 Pa", "correct": False,
             "why": "That divides by three, and going deeper raises the "
                    "pressure rather than lowering it."},
            {"text": "24 009 Pa", "correct": False,
             "why": "That adds the depth on, and metres cannot be added to "
                    "pascals."},
            {"text": "27 000 Pa", "correct": False,
             "why": "That adds another 3000 Pa, when each metre is worth "
                    "8000 Pa in this liquid."},
            {"text": "72 000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e26",
        "band": "easier",
        "text": "A diver's depth gauge works by measuring…",
        "options": [
            {"text": "the pressure of the water, which rises with depth",
             "correct": True},
            {"text": "how long the diver has been under the water",
             "correct": False,
             "why": "Time is on a separate dial and says nothing about how "
                    "far down the diver is."},
            {"text": "the temperature of the water, which falls with depth",
             "correct": False,
             "why": "Temperature does change, but far too unreliably to give "
                    "a depth."},
            {"text": "how much air is left in the diver's cylinder",
             "correct": False,
             "why": "That is a different gauge measuring a different thing."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e27",
        "band": "easier",
        "text": "Ten metres down in water, the pressure of the water alone is "
                "about…",
        "options": [
            {"text": "1000 Pa", "correct": False,
             "why": "1000 Pa is reached after about a tenth of a metre, not "
                    "after ten."},
            {"text": "10 000 Pa", "correct": False,
             "why": "10 000 Pa is one metre's worth, and there are ten metres "
                    "here."},
            {"text": "100 000 Pa", "correct": True},
            {"text": "10 Pa", "correct": False,
             "why": "That is the depth in metres with a pressure unit written "
                    "after it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e28",
        "band": "easier",
        "text": "A liquid presses on…",
        "options": [
            {"text": "the base of its container and nothing else",
             "correct": False,
             "why": "Water squirts out of a hole in the side of a can, so it "
                    "presses on the walls too."},
            {"text": "only the surfaces below it", "correct": False,
             "why": "It pushes up on anything held underneath it as well as "
                    "down."},
            {"text": "everything it touches", "correct": True},
            {"text": "whatever is moving through it", "correct": False,
             "why": "Still water in a sealed tank presses on the walls with "
                    "nothing moving at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e29",
        "band": "easier",
        "text": "A tower holds its water 30 m above the ground. Water gives "
                "10 000 Pa for each metre. What pressure does that give at "
                "ground level?",
        "options": [
            {"text": "3000 Pa", "correct": False,
             "why": "That divides by ten where the two figures should be "
                    "multiplied."},
            {"text": "10 030 Pa", "correct": False,
             "why": "That adds the height on, and metres cannot be added to "
                    "pascals."},
            {"text": "333 Pa", "correct": False,
             "why": "That is 10 000 ÷ 30, the division the wrong way round."},
            {"text": "300 000 Pa", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-e30",
        "band": "easier",
        "text": "The pressure at a point in a liquid comes from the weight of "
                "the liquid…",
        "options": [
            {"text": "above that point", "correct": True},
            {"text": "below that point", "correct": False,
             "why": "The liquid underneath is resting on the base, not on the "
                    "point in question."},
            {"text": "beside that point", "correct": False,
             "why": "Liquid off to the sides rests on its own patch of floor "
                    "rather than on this point."},
            {"text": "in the whole container", "correct": False,
             "why": "A wide tank holds far more liquid than a narrow tube and "
                    "gives the same pressure at the same depth."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · standard ───────────────────────────
    {
        "id": "p5-02-s18",
        "band": "standard",
        "text": "A probe reads 45 000 Pa in water, which gives 10 000 Pa for "
                "each metre. How deep is the probe?",
        "options": [
            {"text": "45 m", "correct": False,
             "why": "That reads the pascals as metres; each metre is worth "
                    "10 000 of them."},
            {"text": "4.5 m", "correct": True},
            {"text": "450 000 m", "correct": False,
             "why": "That multiplies the two, which points the wrong way: a "
                    "bigger per-metre figure means a shallower depth."},
            {"text": "0.22 m", "correct": False,
             "why": "That is 10 000 ÷ 45 000, the division the wrong way "
                    "round."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s19",
        "band": "standard",
        "text": "A probe with a face of 0.03 m² reads 25 000 Pa. What does the "
                "water standing above its face weigh?",
        "options": [
            {"text": "833 333 N", "correct": False,
             "why": "That is 25 000 ÷ 0.03, dividing where the rearrangement "
                    "multiplies."},
            {"text": "25 000 N", "correct": False,
             "why": "That is the pressure with the unit swapped, before the "
                    "face area is multiplied in."},
            {"text": "750 N", "correct": True},
            {"text": "0.0000012 N", "correct": False,
             "why": "That is 0.03 ÷ 25 000, which matches neither the "
                    "relationship nor its rearrangement."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s20",
        "band": "standard",
        "text": "At one depth the pressure is 30 000 Pa. Two hatches sit "
                "there, of 0.10 m² and 0.40 m². What forces do they take?",
        "options": [
            {"text": "300 N and 1200 N", "correct": False,
             "why": "Those are a hundred times too small; 30 000 × 0.10 is "
                    "3000, not 300."},
            {"text": "3000 N on each, because the pressure is the same",
             "correct": False,
             "why": "Equal pressure on unequal areas gives unequal forces."},
            {"text": "300 000 N and 75 000 N", "correct": False,
             "why": "Those come from dividing by the areas, where the "
                    "rearrangement multiplies."},
            {"text": "3000 N and 12 000 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s21",
        "band": "standard",
        "text": "A reservoir's surface stands 40 m above a village tap. Water "
                "gives 10 000 Pa per metre. What pressure reaches the tap?",
        "options": [
            {"text": "400 000 Pa", "correct": True},
            {"text": "40 000 Pa", "correct": False,
             "why": "That uses four metres rather than forty, losing a factor "
                    "of ten."},
            {"text": "250 Pa", "correct": False,
             "why": "That is 10 000 ÷ 40, the division the wrong way round."},
            {"text": "10 040 Pa", "correct": False,
             "why": "That adds the height on, and metres cannot be added to "
                    "pascals."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s22",
        "band": "standard",
        "text": "Why is a dam's sluice gate hardest to open when the reservoir "
                "behind it is full?",
        "options": [
            {"text": "Because a full reservoir holds far more water "
                     "altogether", "correct": False,
             "why": "The total held never enters into it; the depth above the "
                    "gate does."},
            {"text": "Because the water is deepest then, so the pressure and "
                     "the force on the gate are greatest", "correct": True},
            {"text": "Because the gate swells when it is wet for a long time",
             "correct": False,
             "why": "A steel gate does not swell, and the same gate opens "
                    "easily when the reservoir is low."},
            {"text": "Because a full reservoir is colder, and cold water "
                     "presses harder", "correct": False,
             "why": "Temperature is not what sets the pressure; the depth and "
                    "the liquid are."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s23",
        "band": "standard",
        "text": "Sea water gives about 10 250 Pa for each metre and fresh "
                "water 10 000. How much more pressure does a diver meet 20 m "
                "down in the sea?",
        "options": [
            {"text": "250 Pa more", "correct": False,
             "why": "250 Pa is the extra from one metre; twenty metres give "
                    "twenty times that."},
            {"text": "2500 Pa more", "correct": False,
             "why": "That uses ten metres rather than twenty."},
            {"text": "5000 Pa more", "correct": True},
            {"text": "No more, because the depth is the same in both",
             "correct": False,
             "why": "Depth is only half of it; which liquid it is matters "
                    "too, and sea water is heavier for its size."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s24",
        "band": "standard",
        "text": "A tank's base measures 2 m by 1.5 m and holds water 1 m deep, "
                "giving 10 000 Pa there. What force is on the base?",
        "options": [
            {"text": "3333 N", "correct": False,
             "why": "That divides the pressure by the area, where force = "
                    "pressure × area multiplies."},
            {"text": "10 000 N", "correct": False,
             "why": "That is the pressure with the unit swapped; the base "
                    "area still has to be multiplied in."},
            {"text": "35 000 N", "correct": False,
             "why": "That uses 3.5 m², which adds the two sides instead of "
                    "multiplying them."},
            {"text": "30 000 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s25",
        "band": "standard",
        "text": "A liquid 2 m deep gives 16 000 Pa at its base, where water "
                "would give 20 000 Pa. What does that say about the liquid?",
        "options": [
            {"text": "It weighs less than water for the same volume",
             "correct": True},
            {"text": "It weighs more than water for the same volume",
             "correct": False,
             "why": "A heavier liquid would press harder than water at that "
                    "depth, not less hard."},
            {"text": "There is less of it than there would be water",
             "correct": False,
             "why": "The amount held never sets the pressure, and both fill "
                    "the same depth."},
            {"text": "It is at a lower temperature than water would be",
             "correct": False,
             "why": "Temperature shifts a liquid's weight per cubic metre "
                    "very slightly, far too little to explain this gap."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s26",
        "band": "standard",
        "text": "A diver's ears hurt while they swim downwards but settle "
                "again while they swim along at one depth. Why?",
        "options": [
            {"text": "Because swimming along is gentler on the body than "
                     "swimming down", "correct": False,
             "why": "The effort involved is not what presses on an eardrum; "
                    "the water is."},
            {"text": "Because the pressure changes as the depth changes and "
                     "holds steady along one depth", "correct": True},
            {"text": "Because water presses downwards, so it only reaches the "
                     "ears on the way down", "correct": False,
             "why": "A liquid presses equally in every direction at any one "
                    "depth."},
            {"text": "Because the ears seal themselves once a diver stops "
                     "going deeper", "correct": False,
             "why": "Nothing seals. The push on the eardrum simply stops "
                    "changing."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s27",
        "band": "standard",
        "text": "A hatch 3 m below the surface takes a force of 6000 N. What "
                "force does an identical hatch 6 m down take?",
        "options": [
            {"text": "6000 N", "correct": False,
             "why": "The hatches are the same size at different depths, and "
                    "the deeper one meets a greater pressure."},
            {"text": "3000 N", "correct": False,
             "why": "Being further from the surface means more water above, "
                    "so the force rises rather than falling."},
            {"text": "12 000 N", "correct": True},
            {"text": "36 000 N", "correct": False,
             "why": "That multiplies by six. Doubling the depth doubles the "
                    "pressure, and so the force."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s28",
        "band": "standard",
        "text": "A bucket and a swimming pool are both filled to 0.5 m deep. "
                "Compare the FORCE the water puts on each base.",
        "options": [
            {"text": "The same on both", "correct": False,
             "why": "The pressures match; the pool's base has thousands of "
                    "times more square metres for that pressure to act on."},
            {"text": "Greater on the bucket, because its base is smaller",
             "correct": False,
             "why": "A smaller base takes the same pressure over less area, "
                    "so it takes less force."},
            {"text": "Far greater on the pool's base", "correct": True},
            {"text": "It cannot be compared, since one holds far more water "
                     "than the other", "correct": False,
             "why": "It can: the pressure is equal and the areas are known to "
                    "differ hugely, which settles the forces."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s29",
        "band": "standard",
        "text": "Oil gives 8000 Pa for each metre of depth. What pressure does "
                "it give 5 m down?",
        "options": [
            {"text": "40 000 Pa", "correct": True},
            {"text": "1600 Pa", "correct": False,
             "why": "That divides where the two figures should be "
                    "multiplied."},
            {"text": "8005 Pa", "correct": False,
             "why": "That adds the depth on, and metres cannot be added to "
                    "pascals."},
            {"text": "50 000 Pa", "correct": False,
             "why": "That uses water's 10 000 Pa per metre instead of the "
                    "8000 Pa the question gives for oil."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-s30",
        "band": "standard",
        "text": "A student says the force on a hatch depends only on how deep "
                "it is. What have they left out?",
        "options": [
            {"text": "How long it has been under", "correct": False,
             "why": "Time makes no difference; the force is the same after an "
                    "hour as after a second."},
            {"text": "The area of the hatch", "correct": True},
            {"text": "The tank's width", "correct": False,
             "why": "The tank's width never enters into it, for the pressure "
                    "or for the force."},
            {"text": "Which way up it faces", "correct": False,
             "why": "A liquid presses equally in every direction at one "
                    "depth, so the facing does not matter."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · harder ─────────────────────────────
    {
        "id": "p5-02-h18",
        "band": "harder",
        "text": "A tank holds 1 m of oil, giving 8000 Pa per metre, floating "
                "on 2 m of water, giving 10 000 Pa per metre. What is the "
                "pressure at the base?",
        "options": [
            {"text": "20 000 Pa", "correct": False,
             "why": "That counts the water alone. The oil is stacked above "
                    "it, so its weight presses on the base as well."},
            {"text": "18 000 Pa", "correct": False,
             "why": "That adds one metre of each. There are two metres of "
                    "water, which contribute 20 000 Pa."},
            {"text": "28 000 Pa", "correct": True},
            {"text": "8000 Pa", "correct": False,
             "why": "That counts the oil alone. Being on top means its weight "
                    "is added to the water's, not that it replaces it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h19",
        "band": "harder",
        "text": "A straight-sided tank has a base of 4 m² and the water gives "
                "15 000 Pa there. What does the water in the tank weigh?",
        "options": [
            {"text": "3750 N", "correct": False,
             "why": "That divides the pressure by the area, where force = "
                    "pressure × area multiplies."},
            {"text": "15 000 N", "correct": False,
             "why": "That is the pressure with the unit swapped, before the "
                    "base area is multiplied in."},
            {"text": "60 000 N", "correct": True},
            {"text": "It cannot be found without knowing how deep the water "
                     "is", "correct": False,
             "why": "The depth is already inside the 15 000 Pa; the base area "
                    "turns that into a force."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h20",
        "band": "harder",
        "text": "A diver is 20 m down in sea water, which gives 10 250 Pa per "
                "metre. Their mask window is 0.010 m². What force does the "
                "water put on it?",
        "options": [
            {"text": "205 000 N", "correct": False,
             "why": "205 000 is the pressure in pascals; the window's area "
                    "still has to be multiplied in."},
            {"text": "2050 N", "correct": True},
            {"text": "102 N", "correct": False,
             "why": "That uses one metre of depth rather than twenty."},
            {"text": "20 500 000 N", "correct": False,
             "why": "That divides by the area rather than multiplying by it, "
                    "which sends the answer the wrong way."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h21",
        "band": "harder",
        "text": "Water 6 m deep presses on one face of a canal gate and "
                "nothing presses on the other. Water gives 10 000 Pa per "
                "metre. What is the pressure difference at the gate's foot?",
        "options": [
            {"text": "10 000 Pa", "correct": False,
             "why": "That is what one metre gives. The foot of the gate is "
                    "six metres down, with six metres of water above it."},
            {"text": "60 000 Pa", "correct": True},
            {"text": "Nothing", "correct": False,
             "why": "Both faces of the gate are at that depth, and only one "
                    "of them has water standing above it."},
            {"text": "30 000 Pa", "correct": False,
             "why": "That averages over the gate's height. The foot itself is "
                    "at the full depth."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h22",
        "band": "harder",
        "text": "A probe reads 36 000 Pa at 4 m down in an unknown liquid. "
                "Taking gravity as 10 N/kg, what is the liquid's mass per "
                "cubic metre?",
        "options": [
            {"text": "1000 kg, the same as water", "correct": False,
             "why": "Water would give 40 000 Pa at 4 m, so this liquid is "
                    "lighter for its size."},
            {"text": "9000 kg", "correct": False,
             "why": "That reads the 9000 Pa each metre gives as a mass "
                    "directly, without dividing by the 10 N/kg."},
            {"text": "900 kg", "correct": True},
            {"text": "144 000 kg", "correct": False,
             "why": "That multiplies the reading by the depth, where the two "
                    "should be divided."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h23",
        "band": "harder",
        "text": "A funnel of water is wide at the top and narrow at the "
                "bottom. Why does the pressure at its tip match that at the "
                "base of a straight tube filled to the same height?",
        "options": [
            {"text": "Because the sloping sides carry part of the water's "
                     "weight down to the tip", "correct": False,
             "why": "The sides carry some weight, and that is why the tip "
                    "does not take the whole funnel's load."},
            {"text": "Because the funnel holds less water, and less water "
                     "presses less", "correct": False,
             "why": "It does hold less, and the amount held is not what sets "
                    "the pressure."},
            {"text": "Because the pressure at a point is set by the height of "
                     "liquid above it, not by the amount", "correct": True},
            {"text": "Because a narrow opening concentrates the push into a "
                     "smaller space", "correct": False,
             "why": "Nothing is concentrated by a narrowing; each square "
                    "metre carries the column directly above it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h24",
        "band": "harder",
        "text": "An aquarium window is 1 m tall, with its top 1 m below the "
                "surface and its bottom 2 m below. Water gives 10 000 Pa per "
                "metre. Compare the pressures at the two edges.",
        "options": [
            {"text": "Equal, because they are part of the same window",
             "correct": False,
             "why": "One edge is a metre deeper than the other, and depth is "
                    "what sets the pressure."},
            {"text": "The bottom edge takes 10 000 Pa more", "correct": True},
            {"text": "The top edge takes 10 000 Pa more, because the water "
                     "above it is nearer the air", "correct": False,
             "why": "The shallower edge has less water above it, so it takes "
                    "less pressure."},
            {"text": "The bottom edge takes 20 000 Pa more, because it is "
                     "twice as deep", "correct": False,
             "why": "Twice the depth gives twice the pressure, which here is "
                    "20 000 Pa against 10 000 Pa — a gap of 10 000 Pa."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h25",
        "band": "harder",
        "text": "A tap must be supplied at 250 000 Pa. Water gives 10 000 Pa "
                "for each metre of depth. How far above the tap must the "
                "water surface stand?",
        "options": [
            {"text": "25 m", "correct": True},
            {"text": "250 m", "correct": False,
             "why": "That treats each metre as worth 1000 Pa rather than "
                    "10 000 Pa."},
            {"text": "2.5 m", "correct": False,
             "why": "2.5 m of water gives 25 000 Pa, a tenth of what is "
                    "wanted."},
            {"text": "2 500 000 m", "correct": False,
             "why": "That multiplies the two figures, where finding a depth "
                    "from a pressure divides."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h26",
        "band": "harder",
        "text": "A sealed rigid box is fine on the deck of a boat but is "
                "crushed when it is lowered to 50 m. Why?",
        "options": [
            {"text": "Because the water is colder down there, and cold metal "
                     "gives way", "correct": False,
             "why": "A box in a freezer keeps its shape; it is the push from "
                    "the water that crushes this one."},
            {"text": "Because the box gets heavier the deeper it goes",
             "correct": False,
             "why": "Its weight is unchanged at any depth; the pressure "
                    "around it is not."},
            {"text": "Because the water outside now presses with about "
                     "500 000 Pa while the air sealed inside does not",
             "correct": True},
            {"text": "Because a sealed box has nothing inside it to hold its "
                     "walls apart", "correct": False,
             "why": "It has air inside, which is why it survives at the "
                    "surface at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h27",
        "band": "harder",
        "text": "A thin plastic bottle held open-end-up under water crumples "
                "from the bottom first. Why?",
        "options": [
            {"text": "Because the plastic is thinnest at the bottom of a "
                     "bottle", "correct": False,
             "why": "A bottle's base is usually its thickest part, so it "
                    "would give way last if thickness decided it."},
            {"text": "Because water reaches the bottom of the bottle before "
                     "the top", "correct": False,
             "why": "The bottle is already under; nothing is filling it in "
                    "order."},
            {"text": "Because the deepest part meets the greatest pressure",
             "correct": True},
            {"text": "Because the bottle's weight rests on its base",
             "correct": False,
             "why": "A plastic bottle's own weight is tiny beside the push "
                    "the water gives it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h28",
        "band": "harder",
        "text": "A U-tube of mercury has one arm open to the air and the "
                "other joined to a pump. The mercury stands 20 mm higher in "
                "the open arm. What does that show?",
        "options": [
            {"text": "The pump's pressure is greater than the air's",
             "correct": True},
            {"text": "The pump's pressure is lower than the air's",
             "correct": False,
             "why": "A weaker pump would let the air push the mercury back "
                    "towards it, raising the column on the pump's side."},
            {"text": "The two pressures are equal, since the mercury has "
                     "stopped moving", "correct": False,
             "why": "It stops moving when the pressures balance including the "
                    "extra column, which means they are not equal."},
            {"text": "The mercury in the open arm has become less dense",
             "correct": False,
             "why": "It is one body of mercury at one temperature, so both "
                    "arms hold the same stuff."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h29",
        "band": "harder",
        "text": "A pipe runs from a reservoir down a hill to a village 60 m "
                "below it. Water gives 10 000 Pa per metre. What is the "
                "pressure at the village, and would a longer, more winding "
                "pipe change it?",
        "options": [
            {"text": "600 000 Pa, and a longer pipe would raise it, since the "
                     "water travels further", "correct": False,
             "why": "Distance travelled adds nothing; only the height "
                    "difference counts."},
            {"text": "60 000 Pa, and the pipe's route makes no difference",
             "correct": False,
             "why": "The figure is a tenth of the right one: sixty metres at "
                    "10 000 Pa each is 600 000 Pa."},
            {"text": "600 000 Pa, and the pipe's route makes no difference",
             "correct": True},
            {"text": "It depends on the pipe's length, since a longer column "
                     "of water weighs more", "correct": False,
             "why": "What presses is the height of water above the tap, and a "
                    "winding pipe does not change that height."},
        ],
        "figure": None,
    },
    {
        "id": "p5-02-h30",
        "band": "harder",
        "text": "Why is it the distance BELOW the surface, rather than the "
                "height above the base, that decides the pressure at a point "
                "in a liquid?",
        "options": [
            {"text": "Because the base of a container is where the pressure "
                     "is worked out from", "correct": False,
             "why": "The base is simply the deepest point; nothing is "
                    "measured from it."},
            {"text": "Because liquids are measured downwards by convention, "
                     "whichever end you start at", "correct": False,
             "why": "This is not a matter of convention: measuring from the "
                    "base gives the wrong answer."},
            {"text": "Because a container's base moves when it is refilled",
             "correct": False,
             "why": "The base stays where it is; it is the surface that moves "
                    "when a tank is filled or drained."},
            {"text": "Because it is the liquid above a point that rests on "
                     "it, and the liquid below rests on the base instead",
             "correct": True},
        ],
        "figure": None,
    },
]
