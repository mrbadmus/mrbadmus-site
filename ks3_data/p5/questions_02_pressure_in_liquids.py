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
]
