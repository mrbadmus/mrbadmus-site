"""P8 lesson 06 — Conductors and insulators: twelve questions (MRB-223).

Written against Design's page. The cable with copper inside and plastic
outside, the test gap, the fourteen-decade chart and both worked examples
are hers.

The discriminations, in the order the lesson builds them:

  · a conductor has charges FREE TO MOVE, and which charges they are
    differs between a metal and salt water;
  · the difference comes out as a resistance, and the range is
    continuous (`CIRC-22`);
  · an insulator passes a current too small to matter, not none
    (`CIRC-21`) — the harder band sits here;
  · a longer specimen resists more, so length is part of the answer
    (`CIRC-24`).

⚠️ **NOTHING HERE PRINTS A CURRENT FOR BARE COPPER ACROSS THE SUPPLY.**
Mide's ruling of 21 Aug 2026: 6.0 V ÷ 0.05 Ω is a division result and not
a reading, because the supply's own internal resistance is what limits the
current there. The one question that touches the state says so.

⚠️ POSITION IS AUTHORED AND MEASURED —
1,0,2,3 · 3,2,0,1 · 0,1,2,2;
the twelve fall 3/3/4/2 across the four indices.

⚠️ Neither ladder rung is restated (6.0 V with 0.15 A, the plastic ruler
reading zero), and neither are the figures in the worked examples (10 cm
of pencil lead at 0.20 A, 12 cm of graphite at 30 mA) or in the two
attempts (the live bench, and 15 cm of nichrome at 24 mA).
"""

UNIT = "P8"
LESSON = "conductors-and-insulators"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p8-06-e01",
        "band": "easier",
        "text": "A conductor is a material that…",
        "options": [
            {"text": "gets hot when electricity passes through it",
             "correct": False,
             "why": "Some conductors do, and so does a poor conductor like "
                    "pencil lead. Heating is a consequence, not the "
                    "definition."},
            {"text": "has charges free to move", "correct": True},
            {"text": "is always a metal", "correct": False,
             "why": "Salt water conducts and is not a metal, and graphite "
                    "conducts and is not a metal either."},
            {"text": "makes its own electricity", "correct": False,
             "why": "Nothing makes charge. A conductor lets the charge it "
                    "already has be pushed along."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e02",
        "band": "easier",
        "text": "In salt water, the charges that move are…",
        "options": [
            {"text": "dissolved ions", "correct": True},
            {"text": "loose electrons, as in a metal", "correct": False,
             "why": "Water has no pool of loose electrons. What carries the "
                    "charge is whole charged particles in solution."},
            {"text": "the water molecules themselves", "correct": False,
             "why": "A water molecule is neutral overall. Pure water is a "
                    "very poor conductor for exactly that reason."},
            {"text": "bubbles of gas", "correct": False,
             "why": "Bubbles may appear at the electrodes, and they are a "
                    "result of the current rather than the thing carrying "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e03",
        "band": "easier",
        "text": "Which of these has the highest resistance?",
        "options": [
            {"text": "A copper wire", "correct": False,
             "why": "Copper is the lowest on the chart — a few hundredths of "
                    "an ohm for a short piece."},
            {"text": "A piece of pencil lead", "correct": False,
             "why": "Graphite conducts poorly but it conducts: about 30 Ω "
                    "for 10 cm, which will light a lamp."},
            {"text": "A plastic ruler", "correct": True},
            {"text": "Salt water", "correct": False,
             "why": "Salt water is in the middle of the range, hundreds of "
                    "ohms rather than millions of millions."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e04",
        "band": "easier",
        "text": "A 10 cm specimen is replaced by a 100 cm piece of the same "
                "material. Its resistance…",
        "options": [
            {"text": "stays the same, because it is the same material",
             "correct": False,
             "why": "The material sets the resistance per unit of length. "
                    "Ten times the length is ten times the total."},
            {"text": "falls to a tenth, because there is more of it to carry "
                     "the charge", "correct": False,
             "why": "More LENGTH is more to get through. More WIDTH would be "
                    "more room."},
            {"text": "falls to zero, because a long enough piece of anything "
                     "conducts", "correct": False,
             "why": "Length makes a specimen worse, never better, and "
                    "nothing reaches zero resistance at room temperature."},
            {"text": "rises to ten times", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p8-06-s01",
        "band": "standard",
        "text": "Why is a lamp flex made of copper inside and plastic "
                "outside?",
        "options": [
            {"text": "Because copper is cheaper than plastic in the "
                     "quantities used", "correct": False,
             "why": "Copper is the expensive part. The choice is about "
                    "resistance, not price."},
            {"text": "Because plastic is stronger and copper is more "
                     "flexible", "correct": False,
             "why": "Both are true and neither is the reason. The reason is "
                    "the enormous difference in resistance."},
            {"text": "Because plastic melts before copper does, so the "
                     "sheath gives way first and warns you that the cable is "
                     "overloaded", "correct": False,
             "why": "It does melt first, and that is a consequence of a "
                    "fault rather than the reason for the design."},
            {"text": "Because copper has free electrons and plastic has "
                     "almost none, so the sideways route resists enormously "
                     "more", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s02",
        "band": "standard",
        "text": "A specimen on the 6.0 V test gap gives an ammeter reading "
                "of 0.30 A. What is its resistance, and what does that make "
                "it?",
        "options": [
            {"text": "1.8 Ω — a conductor", "correct": False,
             "why": "That multiplies the two readings. Resistance is volts "
                    "divided by amps."},
            {"text": "20 Ω — an insulator", "correct": False,
             "why": "The resistance is right and the classification is not. "
                    "Twenty ohms passes enough current to light a lamp."},
            {"text": "20 Ω — a conductor", "correct": True},
            {"text": "0.05 Ω — a conductor", "correct": False,
             "why": "That divides the current by the p.d. The volts go on "
                    "top."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s03",
        "band": "standard",
        "text": "Why does the chart of resistances use an axis where every "
                "mark is a thousand times the one before?",
        "options": [
            {"text": "Because a ruler scale that showed the plastic would "
                     "put every conductor at zero", "correct": True},
            {"text": "Because resistance is always measured in thousands",
             "correct": False,
             "why": "It is measured in ohms, and the values run from "
                    "hundredths to millions of millions of them."},
            {"text": "Because the chart is easier to draw that way",
             "correct": False,
             "why": "It is harder to draw and harder to read. It is used "
                    "because nothing else can show both ends at once."},
            {"text": "Because the boundary between conductors and insulators "
                     "falls at a round number of thousands", "correct": False,
             "why": "There is no boundary. The line on the chart is a "
                    "convenience and says so."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s04",
        "band": "standard",
        "text": "Tap water and salt water are both clipped into the gap in "
                "turn. Which passes more current, and why?",
        "options": [
            {"text": "Tap water, because it is purer and purer materials "
                     "conduct better", "correct": False,
             "why": "It is the other way round. What carries the charge here "
                    "is the dissolved ions, so more dissolved salt is more "
                    "carriers."},
            {"text": "Salt water, because it has far more dissolved ions "
                     "free to move", "correct": True},
            {"text": "They pass the same, because both are water",
             "correct": False,
             "why": "About a hundred times apart, in fact. Electrically they "
                    "are quite different materials."},
            {"text": "Salt water, because salt is a metal and metals "
                     "conduct", "correct": False,
             "why": "The verdict is right and the reason is not. Table salt "
                    "is not a metal, and dry salt does not conduct — the "
                    "ions have to be free to move."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p8-06-h01",
        "band": "harder",
        "text": "A student clips a plastic ruler across a supply and the "
                "ammeter stays on zero. Which statement is exactly right?",
        "options": [
            {"text": "A current does flow, far too small for the meter to "
                     "resolve, so the reading is the meter's limit rather "
                     "than the physics", "correct": True},
            {"text": "No current flows at all, because plastic has an "
                     "infinite resistance", "correct": False,
             "why": "Nothing has an infinite resistance. The reading is "
                    "zero because the meter cannot resolve a current that "
                    "small."},
            {"text": "The resistance cannot be found, because you cannot "
                     "divide by zero", "correct": False,
             "why": "The current is not really zero. With a sensitive enough "
                    "instrument there is a reading, and a division."},
            {"text": "A current flows into the plastic and is stored there "
                     "rather than passing through, which is why the meter on "
                     "the far side has nothing to read", "correct": False,
             "why": "Nothing is stored in a specimen. Whatever crosses it "
                    "goes on round the loop."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h02",
        "band": "harder",
        "text": "A bare copper wire is clipped straight across the supply. "
                "The bench reports the resistance and refuses to print a "
                "current. Why?",
        "options": [
            {"text": "Because copper has no resistance at all, so the "
                     "division is impossible", "correct": False,
             "why": "It has a small resistance, and the bench prints it. The "
                    "problem is with the CURRENT, not the division."},
            {"text": "Because a bare wire across a supply is a short "
                     "circuit, and what flows then is set by the supply "
                     "rather than by the wire", "correct": True},
            {"text": "Because copper is the reference and a reference is "
                     "never measured", "correct": False,
             "why": "It is the reference, and that is why its resistance IS "
                    "shown. What cannot be shown honestly is a current."},
            {"text": "Because the ammeter would be destroyed by a current "
                     "that large, and a bench that cannot show a reading "
                     "safely is written to show none at all", "correct": False,
             "why": "A real meter might well be, and this bench is a model. "
                    "The reason is that no figure it printed would be a "
                    "measurement."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h03",
        "band": "harder",
        "text": "A wooden ladder is said to be safer than an aluminium one "
                "near overhead cables, yet a WET wooden ladder is not safe "
                "at all. Which explanation fits both?",
        "options": [
            {"text": "Wet wood becomes a metal, so it conducts like the "
                     "aluminium one", "correct": False,
             "why": "It becomes no such thing. Its resistance falls a long "
                    "way and it is still wood."},
            {"text": "Water is a conductor and wood is an insulator, so the "
                     "wet ladder is really two ladders", "correct": False,
             "why": "Pure water conducts poorly. What matters is the "
                    "dissolved ions the water brings with it."},
            {"text": "Dry wood resists millions of ohms; water carries "
                     "dissolved ions, so wetting it drops the resistance "
                     "enormously", "correct": True},
            {"text": "Aluminium resists more than wet wood, which is why the "
                     "metal ladder is the dangerous one", "correct": False,
             "why": "Aluminium resists far LESS than either. It is the "
                    "dangerous one because it conducts freely."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h04",
        "band": "harder",
        "text": "Why is \"insulator\" described on this page as a practical "
                "judgement rather than a kind of material?",
        "options": [
            {"text": "Because the word is old and physicists no longer use "
                     "it", "correct": False,
             "why": "It is used constantly, and usefully. What it means is a "
                    "judgement about how much current."},
            {"text": "Because a material can be swapped between the two "
                     "groups by changing its shape", "correct": False,
             "why": "Shape changes the resistance of a SAMPLE, and a plastic "
                    "ruler cut short is still an insulator. The point is "
                    "about the range being continuous."},
            {"text": "Because every material passes some current, and the "
                     "range from copper to plastic is filled in with no "
                     "break in it", "correct": True},
            {"text": "Because insulators become conductors when they are "
                     "heated, so the two groups are really one group looked "
                     "at at different temperatures", "correct": False,
             "why": "Some do change with temperature, and that is a "
                    "different point. The judgement is about how much "
                    "current is too small to matter."},
        ],
        "figure": None,
    },
]
