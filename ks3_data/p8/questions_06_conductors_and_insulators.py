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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "rises to ten times, because resistance grows with "
                     "length", "correct": True},
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
        "text": "Look at the scale along the bottom of the chart. Why is it "
                "drawn like this?",
        "options": [
            {"text": "Because an evenly spaced scale that reached the "
                     "plastic ruler would squash every conductor to zero",
             "correct": True},
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
        "figure": "p8-resistance-chart-recap",
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
            {"text": "Wet wood becomes a metal itself, so it conducts about "
                     "as well as the aluminium one does", "correct": False,
             "why": "It becomes no such thing. Its resistance falls a long "
                    "way and it is still wood."},
            {"text": "Water is a conductor and wood is an insulator, so a "
                     "wet ladder is really two ladders side by side",
             "correct": False,
             "why": "Pure water conducts poorly. What matters is the "
                    "dissolved ions the water brings with it."},
            {"text": "Dry wood resists millions of ohms; water carries "
                     "dissolved ions, so wetting it drops the resistance "
                     "enormously", "correct": True},
            {"text": "Aluminium resists more than either dry wood or wet "
                     "wood, which is why the metal ladder is the dangerous "
                     "one", "correct": False,
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p8-06-e05",
        "band": "easier",
        "text": "In a metal, the charges that are free to move are…",
        "options": [
            {"text": "loose electrons", "correct": True},
            {"text": "dissolved ions", "correct": False,
             "why": "Ions carry the charge in salt water, not in a solid "
                    "metal."},
            {"text": "the metal's whole atoms", "correct": False,
             "why": "The atoms stay in place; only the loose electrons "
                    "travel."},
            {"text": "protons from the nuclei", "correct": False,
             "why": "Protons are locked inside nuclei and never move through "
                    "a wire."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e06",
        "band": "easier",
        "text": "An insulator is a material with…",
        "options": [
            {"text": "almost no free charges, and a very high resistance",
             "correct": True},
            {"text": "no charged particles in it at all", "correct": False,
             "why": "It is full of charged particles; they are simply not "
                    "free to move."},
            {"text": "a resistance of exactly zero", "correct": False,
             "why": "That describes a perfect conductor, which is the "
                    "opposite end of the range."},
            {"text": "free charges that move only very slowly",
             "correct": False,
             "why": "Even in a conductor the drift is slow. What an insulator "
                    "lacks is charges that are free at all."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e07",
        "band": "easier",
        "text": "Which of these conducts best?",
        "options": [
            {"text": "Tap water", "correct": False,
             "why": "Tap water passes a small current, far less than any "
                    "metal."},
            {"text": "Graphite", "correct": False,
             "why": "Graphite conducts, unusually for a non-metal, but "
                    "nowhere near as well as copper."},
            {"text": "Dry wood", "correct": False,
             "why": "Dry wood sits near the insulating end of the range."},
            {"text": "Copper", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p8-06-s05",
        "band": "standard",
        "text": "A specimen clipped across a 6.0 V supply passes 0.020 A. "
                "What is its resistance?",
        "options": [
            {"text": "300 Ω", "correct": True},
            {"text": "0.12 Ω", "correct": False,
             "why": "That is 6.0 × 0.020. Resistance is the p.d. divided by "
                    "the current."},
            {"text": "0.0033 Ω", "correct": False,
             "why": "That is 0.020 ÷ 6.0, the ratio upside down."},
            {"text": "6.02 Ω", "correct": False,
             "why": "That adds the readings, and volts cannot be added to "
                    "amps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s06",
        "band": "standard",
        "text": "Graphite is unusual among non-metals. Why?",
        "options": [
            {"text": "Because it is the only non-metal that is shiny",
             "correct": False,
             "why": "Appearance is not the test; being able to pass a current "
                    "is."},
            {"text": "Because it dissolves to give ions that carry charge",
             "correct": False,
             "why": "It does not dissolve. Its own electrons do the "
                    "carrying."},
            {"text": "Because some of its electrons are free to move, so it "
                     "conducts",
             "correct": True},
            {"text": "Because it has no resistance at all", "correct": False,
             "why": "It has a real resistance, well above copper's — it is "
                    "simply far below plastic's."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s07",
        "band": "standard",
        "text": "Why does damp wood conduct far better than dry wood?",
        "options": [
            {"text": "Because water makes the wood softer, so charge passes "
                     "more easily",
             "correct": False,
             "why": "Softness has nothing to do with it; what matters is "
                    "having charges free to move."},
            {"text": "Because the water carries dissolved ions that are free "
                     "to move",
             "correct": True},
            {"text": "Because wet wood is a metal once the water is in it",
             "correct": False,
             "why": "It is not a metal at all, and it has no loose electrons "
                    "of its own."},
            {"text": "Because water has no resistance", "correct": False,
             "why": "Even salt water has a substantial resistance; it is "
                    "simply far lower than dry wood's."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p8-06-h05",
        "band": "harder",
        "text": "A student says a short enough piece of an insulator would "
                "conduct properly. What is wrong with that?",
        "options": [
            {"text": "Nothing — halving the length halves the resistance, so "
                     "it must work eventually",
             "correct": False,
             "why": "Halving from millions of millions of ohms still leaves "
                    "millions of millions of ohms."},
            {"text": "Length has no effect on resistance at all",
             "correct": False,
             "why": "It does have an effect, and that is exactly why the "
                    "argument is tempting."},
            {"text": "Shortening lowers the resistance a little, but it "
                     "starts far too high to matter",
             "correct": True},
            {"text": "A short piece would have a HIGHER resistance, not a "
                     "lower one",
             "correct": False,
             "why": "Shorter really is lower; the argument fails on the size "
                    "of the starting figure, not the direction."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h06",
        "band": "harder",
        "text": "Why are conductors and insulators better drawn as one "
                "continuous range than as two separate boxes?",
        "options": [
            {"text": "Because the measured resistances fill every value in "
                     "between",
             "correct": True},
            {"text": "Because no material has ever had its resistance "
                     "measured accurately",
             "correct": False,
             "why": "They are measured routinely, and it is those "
                    "measurements that fill the range."},
            {"text": "Because a material can be either one depending on the "
                     "day",
             "correct": False,
             "why": "A dry specimen keeps its value; it is the spread ACROSS "
                    "materials that is continuous."},
            {"text": "Because every insulator becomes a conductor if enough "
                     "voltage is applied",
             "correct": False,
             "why": "That can happen at extremes, but it is not why the chart "
                    "is drawn as a range."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h07",
        "band": "harder",
        "text": "Silicon's resistance can be controlled on purpose. What is a "
                "material like that called, and where does it sit?",
        "options": [
            {"text": "A superconductor, at the very bottom of the range",
             "correct": False,
             "why": "A superconductor has no resistance at all, and its value "
                    "is not adjustable."},
            {"text": "A semiconductor, in the middle of the range",
             "correct": True},
            {"text": "An insulator, at the very top of the range",
             "correct": False,
             "why": "An insulator's resistance is fixed and enormous; "
                    "silicon's is neither."},
            {"text": "A conductor, at the very bottom of the range",
             "correct": False,
             "why": "Silicon conducts far less well than copper, so it does "
                    "not sit at that end."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · easier ────────────────────────────────────
    {
        "id": "p8-06-e08",
        "band": "easier",
        "text": "A specimen is tested and the meters show 6.0 V and 0.60 A. "
                "What is its resistance, and what does that make it?",
        "options": [
            {"text": "10 Ω — a conductor", "correct": True},
            {"text": "10 Ω — an insulator", "correct": False,
             "why": "Ten ohms passes plenty of current — nothing like an "
                    "insulator's range."},
            {"text": "0.10 Ω — a conductor", "correct": False,
             "why": "That divides the current by the p.d., the ratio the "
                    "wrong way up."},
            {"text": "6.6 Ω — a conductor", "correct": False,
             "why": "That adds the two readings, and volts cannot be added "
                    "to amps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e09",
        "band": "easier",
        "text": "Clip a specimen into the 6.0 V gap and the ammeter settles "
                "on 6.0 mA. Work out its resistance and say what that makes "
                "it.",
        "options": [
            {"text": "1000 Ω — a poor conductor", "correct": True},
            {"text": "1000 Ω — an insulator", "correct": False,
             "why": "A thousand ohms still passes a small but real current — "
                    "well short of the millions needed for an insulator."},
            {"text": "0.0010 Ω — a conductor", "correct": False,
             "why": "That divides the current by the p.d., the ratio the "
                    "wrong way up."},
            {"text": "1006 Ω — a poor conductor", "correct": False,
             "why": "That tacks the milliamp reading onto the end of the "
                    "resistance; milliamps and ohms cannot be added."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e10",
        "band": "easier",
        "text": "With the supply fixed at 6.0 V, a specimen draws a current "
                "of 120 mA. Find its resistance and classify it.",
        "options": [
            {"text": "50 Ω — a poor conductor", "correct": False,
             "why": "Fifty ohms is comfortably inside the good-conductor "
                    "range on this bench, nothing like a poor conductor's "
                    "higher range."},
            {"text": "0.020 Ω — a conductor", "correct": False,
             "why": "That divides the current by the p.d., the ratio "
                    "upside down."},
            {"text": "50 Ω — a conductor", "correct": True},
            {"text": "6.12 Ω — a conductor", "correct": False,
             "why": "That adds the p.d. and the current together, and "
                    "volts cannot be added to amps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e11",
        "band": "easier",
        "text": "6.0 V is placed across a specimen and the meter shows "
                "3.0 mA. What resistance and classification follow from "
                "that?",
        "options": [
            {"text": "2000 Ω — an insulator", "correct": False,
             "why": "Two thousand ohms still passes a small real current, "
                    "far short of an insulator's range."},
            {"text": "0.00050 Ω — a poor conductor", "correct": False,
             "why": "That divides the current by the p.d., the wrong way "
                    "up."},
            {"text": "2000 Ω — a poor conductor", "correct": True},
            {"text": "2003 Ω — a poor conductor", "correct": False,
             "why": "That tacks the milliamp reading onto the end of the "
                    "resistance, which cannot be done."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e12",
        "band": "easier",
        "text": "An insulator's own current, at an ordinary voltage, is best "
                "described as…",
        "options": [
            {"text": "exactly zero", "correct": False,
             "why": "Nothing has exactly zero current across it; an "
                    "insulator's current is real, just far too small for a "
                    "school meter to show."},
            {"text": "extremely small, but not exactly zero", "correct": True},
            {"text": "large enough to feel as a shock through dry skin", "correct": False,
             "why": "That describes a conductor's current, not an "
                    "insulator's."},
            {"text": "impossible to ever measure with any instrument",
             "correct": False,
             "why": "A sensitive enough lab instrument can measure it; a "
                    "school ammeter simply cannot."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e13",
        "band": "easier",
        "text": "Between \"good conductor\" and \"insulator\" there is…",
        "options": [
            {"text": "no sharp boundary — materials fill in the whole range",
             "correct": True},
            {"text": "a fixed value of exactly 1000 ohms printed on every "
                     "resistance chart",
             "correct": False,
             "why": "There is no such fixed marker; the boundary drawn on "
                    "the chart is only a convenience."},
            {"text": "nothing at all — every material is one or the other",
             "correct": False,
             "why": "Graphite, salt water, tap water and damp wood all sit "
                    "in between."},
            {"text": "a boundary that depends on the colour of the material "
                     "being tested",
             "correct": False,
             "why": "Colour plays no part in resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e14",
        "band": "easier",
        "text": "Silicon is best described as a…",
        "options": [
            {"text": "conductor, at the very bottom of the range for a metal",
             "correct": False,
             "why": "Pure silicon conducts far worse than a metal; it does "
                    "not sit at that end."},
            {"text": "insulator, at the very top of the range and beyond "
                     "a plastic ruler's", "correct": False,
             "why": "Silicon's resistance is nowhere near as high as a true "
                    "insulator's, and it can be changed on purpose."},
            {"text": "semiconductor, in the middle of the resistance range",
             "correct": True},
            {"text": "superconductor, with no resistance at all",
             "correct": False,
             "why": "Silicon has a real, substantial resistance; a "
                    "superconductor has none."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e15",
        "band": "easier",
        "text": "A superconductor is a material whose resistance…",
        "options": [
            {"text": "becomes exactly zero below a very low temperature",
             "correct": True},
            {"text": "is always very high, whatever the temperature",
             "correct": False,
             "why": "That describes an insulator, the opposite behaviour."},
            {"text": "rises without limit as it cools", "correct": False,
             "why": "A superconductor's resistance falls as it cools, then "
                    "drops to zero — it does not rise."},
            {"text": "is the same as any ordinary metal's", "correct": False,
             "why": "An ordinary metal never reaches exactly zero "
                    "resistance, however cold it gets."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e16",
        "band": "easier",
        "text": "At a high enough voltage, even a good insulator can…",
        "options": [
            {"text": "become a perfect conductor permanently", "correct": False,
             "why": "The insulator does not change what it is made of; the "
                    "effect stops once the voltage is removed."},
            {"text": "allow a spark to jump across it", "correct": True},
            {"text": "catch fire immediately, every time", "correct": False,
             "why": "A spark can jump without the material catching fire at "
                    "all."},
            {"text": "turn into a different material entirely",
             "correct": False,
             "why": "Its identity does not change; only whether a current "
                    "can briefly cross it does."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e17",
        "band": "easier",
        "text": "An extension lead's cable is copper inside and plastic "
                "outside, for the same reason as a lamp flex. What is that "
                "reason?",
        "options": [
            {"text": "Plastic is cheaper to manufacture than copper",
             "correct": False,
             "why": "Copper is the expensive part; cost is not the reason "
                    "for the choice."},
            {"text": "Copper has free charges and a very low resistance; "
                     "plastic has none and a very high one.", "correct": True},
            {"text": "Copper conducts heat better, which keeps the cable "
                     "cool during long periods of heavy use", "correct": False,
             "why": "The design is about electrical resistance, not heat "
                    "conduction."},
            {"text": "Plastic simply looks neater than bare copper wire",
             "correct": False,
             "why": "Appearance is not the reason; the enormous difference "
                    "in resistance is."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e18",
        "band": "easier",
        "text": "Water on the outside of an appliance is dangerous mainly "
                "because…",
        "options": [
            {"text": "water makes the plastic casing melt", "correct": False,
             "why": "Water does not melt plastic casing."},
            {"text": "water attracts electricity towards it from a distance, "
                     "across the gap between a hand and the casing",
             "correct": False,
             "why": "Current does not reach across empty space towards "
                    "water; it needs an actual conducting path."},
            {"text": "water always destroys the appliance's circuits "
                     "instantly on the very first contact", "correct": False,
             "why": "The danger described here is to a person, from current "
                    "finding a new path — not guaranteed damage to the "
                    "circuit."},
            {"text": "water carries dissolved ions and conducts far better "
                     "than dry skin or dry plastic", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e19",
        "band": "easier",
        "text": "A copper wire and a silver wire are both excellent "
                "conductors. What do they have in common?",
        "options": [
            {"text": "Both have no resistance at all", "correct": False,
             "why": "Even the best ordinary conductors have a small but "
                    "real resistance; only a superconductor has none."},
            {"text": "Both have huge numbers of loose electrons free to "
                     "move.", "correct": True},
            {"text": "Both are the only two materials that conduct anywhere",
             "correct": False,
             "why": "Many materials conduct to some degree, including "
                    "graphite and salt water."},
            {"text": "Neither has any electrons at all", "correct": False,
             "why": "Every atom has electrons; what makes a good conductor "
                    "is having plenty of them free to drift."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e20",
        "band": "easier",
        "text": "Which pair best represents the two ENDS of the "
                "conductor-insulator range studied on this page?",
        "options": [
            {"text": "Salt water and tap water", "correct": False,
             "why": "Both sit in the middle of the range, nowhere near "
                    "either end."},
            {"text": "Graphite and dry wood", "correct": False,
             "why": "Both are somewhere in the middle — graphite is a poor "
                    "conductor and dry wood a fairly ordinary insulator, "
                    "neither the extreme."},
            {"text": "Nichrome and salt water", "correct": False,
             "why": "Both are somewhere in the middle of the range."},
            {"text": "Copper and a plastic ruler", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e21",
        "band": "easier",
        "text": "A doped semiconductor's resistance, compared with pure "
                "silicon's, is…",
        "options": [
            {"text": "much higher — doping adds resistance", "correct": False,
             "why": "Doping is normally used to LOWER silicon's resistance "
                    "by adding charge carriers, not to raise it."},
            {"text": "infinite — doping turns silicon into an insulator",
             "correct": False,
             "why": "Doping moves silicon's resistance DOWN towards a "
                    "conductor's, not up towards an insulator's."},
            {"text": "exactly the same — doping does nothing to resistance",
             "correct": False,
             "why": "Doping is specifically what changes silicon's "
                    "resistance so much."},
            {"text": "much lower — doping adds charge carriers.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e22",
        "band": "easier",
        "text": "For an ORDINARY metal (not a superconductor), cooling it "
                "down generally makes its resistance…",
        "options": [
            {"text": "rise", "correct": False,
             "why": "Cooling a metal calms the vibrating lattice, which "
                    "means fewer collisions, not more."},
            {"text": "fall.", "correct": True},
            {"text": "stay exactly the same", "correct": False,
             "why": "A metal's resistance does change with temperature, as "
                    "the filament lamp fact already shows for heating."},
            {"text": "become infinite", "correct": False,
             "why": "That would describe becoming a perfect insulator, the "
                    "opposite of what cooling an ordinary metal does."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e23",
        "band": "easier",
        "text": "Why is the plastic sheath on a cable an important safety "
                "feature, rather than just tidy packaging?",
        "options": [
            {"text": "It stops the copper from rusting", "correct": False,
             "why": "Rust protection is not the electrical safety reason "
                    "the sheath is there for."},
            {"text": "It keeps the cable a fixed length", "correct": False,
             "why": "A sheath does not control the cable's length."},
            {"text": "It stops your hand completing a path to the live "
                     "copper inside, since plastic has almost no free "
                     "charges.", "correct": True},
            {"text": "It makes the cable lighter to carry around a large workshop all day and easier to coil up for storage", "correct": False,
             "why": "Weight is not the safety reason for the sheath."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e24",
        "band": "easier",
        "text": "A material that lets through only a current far too small "
                "to matter is called…",
        "options": [
            {"text": "a conductor", "correct": False,
             "why": "A conductor is defined by passing a USEFUL current, the "
                    "opposite case."},
            {"text": "a semiconductor", "correct": False,
             "why": "A semiconductor sits in the middle of the range and can "
                    "be made to conduct usefully."},
            {"text": "an insulator", "correct": True},
            {"text": "a superconductor", "correct": False,
             "why": "A superconductor sits at the opposite end, with zero "
                    "resistance and a huge current if allowed."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e25",
        "band": "easier",
        "text": "Copper conducts far better than salt water mainly because…",
        "options": [
            {"text": "copper's charges move through a shorter path",
             "correct": False,
             "why": "Path length is not what is being compared here; the "
                    "specimens can be the same length."},
            {"text": "copper has vastly more charges free to move.",
             "correct": True},
            {"text": "salt water's ions are heavier and slower for that "
                     "reason alone", "correct": False,
             "why": "The main difference taught here is how MANY charges are "
                    "free, not how heavy they are."},
            {"text": "copper is a liquid at room temperature, which helps",
             "correct": False,
             "why": "Copper is a solid at room temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e26",
        "band": "easier",
        "text": "Why can't an ordinary straight ruler-style scale show both "
                "copper's and plastic's resistance on one chart?",
        "options": [
            {"text": "Because resistance cannot be written as a single "
                     "number", "correct": False,
             "why": "Every specimen's resistance is a single number in "
                    "ohms; the difficulty is only the size of the range."},
            {"text": "Because a straight scale shows whole numbers, not "
                     "decimals",
             "correct": False,
             "why": "A straight scale can show decimals perfectly well; the "
                    "problem is the size of the range, not decimals."},
            {"text": "Because copper and plastic use different units of "
                     "resistance that cannot be drawn on one axis", "correct": False,
             "why": "Both are measured in ohms."},
            {"text": "The numbers differ by more than fourteen zeros, so a "
                     "straight scale would always put every conductor at "
                     "the same point near zero.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e27",
        "band": "easier",
        "text": "A bare copper wire is connected straight across a supply "
                "with nothing else in the loop. What is this called?",
        "options": [
            {"text": "A broken circuit", "correct": False,
             "why": "A broken circuit has no complete path at all; this one "
                    "has too GOOD a path."},
            {"text": "A series circuit", "correct": False,
             "why": "Series describes how components are arranged, not this "
                    "particular fault."},
            {"text": "A short circuit.", "correct": True},
            {"text": "An insulated circuit", "correct": False,
             "why": "Bare copper is the opposite of insulated."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e28",
        "band": "easier",
        "text": "A transistor is built from semiconductor material because "
                "its resistance can be…",
        "options": [
            {"text": "reduced to exactly zero, like a superconductor's",
             "correct": False,
             "why": "A transistor's resistance is not reduced to zero; it is "
                    "controlled between values."},
            {"text": "raised to infinity permanently", "correct": False,
             "why": "A permanently infinite resistance would make the "
                    "transistor useless as a switch."},
            {"text": "controlled on purpose, unlike a fixed conductor or "
                     "insulator, whose resistance can never be tuned that "
                     "way.", "correct": True},
            {"text": "changed by heating it in an oven", "correct": False,
             "why": "The control used in real devices comes from doping and "
                    "an applied voltage, not from baking it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e29",
        "band": "easier",
        "text": "Dry wood and wet wood are best described as…",
        "options": [
            {"text": "exactly the same electrically, since it is the same "
                     "wood", "correct": False,
             "why": "The moisture genuinely changes the resistance by a "
                    "large factor."},
            {"text": "always safe to touch near electricity, wet or dry",
             "correct": False,
             "why": "Wet wood conducts far better than dry wood and is not "
                    "treated as safe."},
            {"text": "so good an insulator, wet or dry, that neither is ever "
                     "a risk to anyone", "correct": False,
             "why": "Wet wood's resistance is far lower than dry wood's, "
                    "which is exactly why it is treated as a risk."},
            {"text": "wood that conducts very differently depending on how "
                     "much water it holds.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-e30",
        "band": "easier",
        "text": "Which everyday object relies on being a GOOD conductor to "
                "work safely?",
        "options": [
            {"text": "A plug's metal pins.", "correct": True},
            {"text": "A plug's plastic casing", "correct": False,
             "why": "The casing needs to be a good INSULATOR, the opposite "
                    "property."},
            {"text": "A lamp's glass bulb", "correct": False,
             "why": "The glass is not part of the conducting path at all."},
            {"text": "A cable's outer sheath", "correct": False,
             "why": "The sheath needs a very high resistance, not a low "
                    "one."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · standard ───────────────────────────────────
    {
        "id": "p8-06-s08",
        "band": "standard",
        "text": "Twelve milliamps is what the ammeter shows for a specimen "
                "held at the fixed 6.0 V. Calculate its resistance and "
                "classify it.",
        "options": [
            {"text": "500 Ω — a poor conductor", "correct": True},
            {"text": "500 Ω — an insulator", "correct": False,
             "why": "Five hundred ohms is well inside the poor-conductor "
                    "range on this bench, nowhere near an insulator's."},
            {"text": "0.50 Ω — a conductor", "correct": False,
             "why": "That treats 12 mA as 12 A, without converting to "
                    "amps."},
            {"text": "0.0020 Ω — a poor conductor", "correct": False,
             "why": "That divides the current by the p.d. — the ratio "
                    "upside down."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s09",
        "band": "standard",
        "text": "Holding the supply at 6.0 V, a technician records a "
                "current of 4.0 mA for one specimen. What resistance and "
                "classification does that give?",
        "options": [
            {"text": "1500 Ω — an insulator", "correct": False,
             "why": "1500 Ω still passes a real, if modest, current — far "
                    "short of an insulator's range."},
            {"text": "1.5 Ω — a conductor", "correct": False,
             "why": "That treats 4.0 mA as 4.0 A, without converting."},
            {"text": "1500 Ω — a poor conductor", "correct": True},
            {"text": "0.00067 Ω — a poor conductor", "correct": False,
             "why": "That divides the current by the p.d., the wrong way "
                    "up."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s10",
        "band": "standard",
        "text": "A specimen barely registers on the meter: 0.020 mA at "
                "6.0 V. Work out its resistance and how it should be "
                "classed.",
        "options": [
            {"text": "300 Ω — a conductor", "correct": False,
             "why": "That treats 0.020 as amps rather than converting "
                    "milliamps to amps first."},
            {"text": "300,000 Ω — a poor conductor", "correct": False,
             "why": "Three hundred thousand ohms is above this bench's "
                    "poor-conductor ceiling of 100,000 Ω — that makes it an "
                    "insulator, not a poor conductor."},
            {"text": "30,000 Ω — an insulator reading", "correct": False,
             "why": "That is ten times too small; the true resistance is "
                    "300,000 Ω."},
            {"text": "300,000 Ω — an insulator", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s11",
        "band": "standard",
        "text": "Dry wood measures about 5 million ohms and tap water about "
                "40 thousand ohms for the same size sample. What does "
                "comparing these two numbers show?",
        "options": [
            {"text": "That the \"insulator\" judgement is about degree, not "
                     "a fixed switch — tap water conducts far better than "
                     "dry wood without being called a conductor.",
             "correct": True},
            {"text": "That tap water must be a mistake, since water should "
                     "always insulate", "correct": False,
             "why": "Plenty of water conducts well; only very pure water "
                    "insulates well."},
            {"text": "That dry wood is actually the better conductor of the "
                     "two", "correct": False,
             "why": "Dry wood's resistance is over a hundred times bigger "
                    "than tap water's, so tap water conducts far better."},
            {"text": "That both numbers must be measurement errors, since "
                     "neither is zero or infinite and real specimens rarely are exactly one or the other in a school experiment.", "correct": False,
             "why": "Neither is expected to be exactly zero or infinite in "
                    "this model; both are ordinary real readings."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s12",
        "band": "standard",
        "text": "An immersion heater has a metal heating element inside a "
                "sealed metal case, with an insulating layer between them. "
                "Why is that insulating layer necessary?",
        "options": [
            {"text": "To stop the live element's current reaching the case, "
                     "which a person might touch.", "correct": True},
            {"text": "To help the element heat up faster", "correct": False,
             "why": "The insulating layer plays no part in how fast the "
                    "element heats the water; it is there for safety."},
            {"text": "To make the case waterproof", "correct": False,
             "why": "Waterproofing is a sealing job, a different function "
                    "from electrically insulating the case from the "
                    "element."},
            {"text": "To reduce the resistance of the heating element so it heats the water faster",
             "correct": False,
             "why": "The insulating layer sits between the element and the "
                    "case; it does not touch or change the element's own "
                    "resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s13",
        "band": "standard",
        "text": "The resistance chart uses a scale where equal steps mean "
                "×1000, not +1000. Why does that suit this data better than "
                "an equal-steps-of-one scale?",
        "options": [
            {"text": "Because ohms can only be measured in multiples of a "
                     "thousand on any instrument ever built in any school or university laboratory anywhere in the world.", "correct": False,
             "why": "Resistance can be any value in ohms; the multiples "
                    "belong to the CHART's scale, not to the unit itself."},
            {"text": "Because the seven materials span from hundredths of "
                     "an ohm to trillions of ohms, and a ×1000 scale can "
                     "show huge ratios in a small space.", "correct": True},
            {"text": "Because it makes all seven bars come out the same "
                     "length", "correct": False,
             "why": "The bars are deliberately different lengths; that "
                    "difference is the whole point of the chart."},
            {"text": "Because scientists prefer round numbers to decimals",
             "correct": False,
             "why": "Preference is not the reason; the reason is fitting an "
                    "enormous range onto one readable axis."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s14",
        "band": "standard",
        "text": "Adding a tiny number of doping atoms can change silicon's "
                "resistance by a factor of a million. What does that suggest "
                "about a semiconductor's resistance, compared with a plain "
                "conductor's?",
        "options": [
            {"text": "A semiconductor's resistance can be engineered, while "
                     "a conductor's is fixed by the metal itself.",
             "correct": True},
            {"text": "A semiconductor always has a lower resistance than any "
                     "conductor once it has been doped at all", "correct": False,
             "why": "Undoped or lightly doped silicon is usually a far "
                    "worse conductor than a metal."},
            {"text": "Doping turns silicon permanently into a metal",
             "correct": False,
             "why": "Doped silicon is still silicon; it behaves more like a "
                    "conductor without becoming one."},
            {"text": "A semiconductor's resistance cannot be measured at "
                     "all", "correct": False,
             "why": "It can be measured exactly like any other resistance, "
                    "with a p.d. and a current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s15",
        "band": "standard",
        "text": "A loop of superconducting wire is set carrying a current, "
                "then left alone with no battery connected, still cooled "
                "below its critical temperature. What happens to the "
                "current?",
        "options": [
            {"text": "It stops almost immediately, like current in any "
                     "ordinary wire", "correct": False,
             "why": "That is what happens in an ORDINARY wire, which has "
                    "resistance; a superconductor has none."},
            {"text": "It keeps flowing, because there is no resistance to "
                     "lose energy to.", "correct": True},
            {"text": "It grows larger and larger without limit",
             "correct": False,
             "why": "Nothing is adding extra energy to the loop, so the "
                    "current has no reason to grow."},
            {"text": "It reverses direction on its own", "correct": False,
             "why": "Nothing in the loop gives the current a reason to "
                    "reverse."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s16",
        "band": "standard",
        "text": "The ammeter reads 75 mA when a specimen sits in the 6.0 V "
                "test gap. What resistance and classification does that "
                "give?",
        "options": [
            {"text": "80 Ω — a poor conductor", "correct": False,
             "why": "Eighty ohms sits comfortably below this bench's "
                    "hundred-ohm good-conductor ceiling."},
            {"text": "0.013 Ω — a conductor", "correct": False,
             "why": "That divides the current by the p.d., the ratio "
                    "upside down."},
            {"text": "80 Ω — a conductor", "correct": True},
            {"text": "6.075 Ω — a conductor", "correct": False,
             "why": "That adds the p.d. and the current together."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s17",
        "band": "standard",
        "text": "The test bench's ammeter is specified to read anything "
                "from hundreds of amps down to millionths of a millionth "
                "of an amp. Why does a specimen bench need a meter with "
                "such an enormous span?",
        "options": [
            {"text": "Because the specimens themselves span that range — "
                     "the same 6.0 V drives amps through copper and a "
                     "sliver of a millionth of an amp through a plastic "
                     "ruler.", "correct": True},
            {"text": "Because a meter with a narrow span would give the "
                     "wrong value rather than no value at all",
             "correct": False,
             "why": "A current outside a meter's span reads as zero or off "
                    "the scale; it does not quietly return a wrong number."},
            {"text": "Because one specimen's own current swings across that "
                     "whole range while it is being measured",
             "correct": False,
             "why": "A steady specimen on a fixed supply holds a steady "
                    "current; the huge range is between specimens, not "
                    "within one."},
            {"text": "Because the same instrument has to read potential "
                     "difference as well as current", "correct": False,
             "why": "The bench's supply is fixed at 6.0 V and stated, so "
                    "nothing here asks the ammeter to measure a p.d."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s18",
        "band": "standard",
        "text": "Salt water measures about 400 Ω and tap water about "
                "40,000 Ω, both for the same length. Roughly how many times "
                "more does tap water resist?",
        "options": [
            {"text": "About 10 times more", "correct": False,
             "why": "That underestimates the gap; 40,000 divided by 400 is "
                    "a hundred, not ten."},
            {"text": "About 1000 times more", "correct": False,
             "why": "That overestimates the gap by a factor of ten."},
            {"text": "About 100 times more.", "correct": True},
            {"text": "They are roughly the same, since both are water",
             "correct": False,
             "why": "The two numbers differ by a factor of a hundred; they "
                    "are not close."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s19",
        "band": "standard",
        "text": "A plug's metal pins must conduct well, and the plastic body "
                "around them must not conduct at all. Which combination of "
                "resistances would be a design FAILURE?",
        "options": [
            {"text": "Low-resistance pins are fine, but a plastic body of "
                     "only a few hundred ohms would be dangerous.",
             "correct": True},
            {"text": "High-resistance pins and a very high-resistance body "
                     "— both fine, since a pin's resistance never matters "
                     "once it is pushed into a socket", "correct": False,
             "why": "High-resistance pins would not carry the current "
                    "properly at all; that is a failure of the pins, not a "
                    "safe design."},
            {"text": "Low-resistance pins and a body of millions of "
                     "millions of ohms — a design failure that no manufacturer would risk", "correct": False,
             "why": "That is exactly the safe design being described, not a "
                    "failure."},
            {"text": "Any combination is safe, since plastic never conducts "
                     "at all", "correct": False,
             "why": "Plastic still passes a tiny current; a poor-quality "
                    "plastic body with only a few hundred ohms would be a "
                    "real hazard."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s20",
        "band": "standard",
        "text": "Graphite and silicon are both non-metals, yet a "
                "manufacturer would choose silicon, not graphite, when they "
                "want to tune a component's resistance. Why?",
        "options": [
            {"text": "Graphite and silicon behave identically, since both "
                     "are made of a single element with nothing to tell them apart once you leave them both at room temperature", "correct": False,
             "why": "Their resistances are worlds apart, and only one of "
                    "them responds usefully to doping."},
            {"text": "Silicon conducts better than graphite in every single "
                     "case", "correct": False,
             "why": "Undoped silicon is usually a far worse conductor than "
                    "graphite; the difference is what CAN be done to it."},
            {"text": "Graphite has a fixed, fairly low resistance from its "
                     "own carbon structure; silicon's resistance is "
                     "deliberately altered by doping to whatever value is "
                     "wanted.", "correct": True},
            {"text": "Graphite is a semiconductor too, just like silicon",
             "correct": False,
             "why": "Graphite is classed here as a poor conductor, not a "
                    "semiconductor."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s21",
        "band": "standard",
        "text": "MRI scanners use superconducting coils cooled by liquid "
                "helium rather than ordinary copper coils. What is the main "
                "electrical advantage?",
        "options": [
            {"text": "Superconducting wire is cheaper than copper",
             "correct": False,
             "why": "A superconducting setup, with its cooling system, is "
                    "far more expensive than copper wire."},
            {"text": "A superconducting coil carries current with no "
                     "resistance, so no energy at all is wasted heating it "
                     "up.", "correct": True},
            {"text": "Superconducting coils need no electricity supply at "
                     "all", "correct": False,
             "why": "A current still has to be started in the coil; the "
                    "advantage is that it then keeps flowing without loss."},
            {"text": "Copper coils cannot carry a current large enough for "
                     "an MRI scanner, however thick the wire is made", "correct": False,
             "why": "Copper could carry the current; the problem is how much "
                    "energy it would waste as heat doing so."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s22",
        "band": "standard",
        "text": "A frayed extension lead has some of its copper showing "
                "through a split in the plastic sheath. Why is that "
                "dangerous even before anyone touches it?",
        "options": [
            {"text": "Nothing is dangerous until the copper is actually "
                     "touched by bare skin or by any other conductor nearby that happens to brush against it.", "correct": False,
             "why": "The exposed copper is already a live risk to anything "
                    "conducting that comes near it, not only bare skin."},
            {"text": "The plastic split just looks untidy, with no "
                     "electrical risk", "correct": False,
             "why": "The plastic sheath is the only thing keeping the "
                    "copper's current away from anything that touches it."},
            {"text": "The exposed copper can pass current into anything "
                     "that touches it, since only the missing plastic was "
                     "stopping that.", "correct": True},
            {"text": "The cable will stop working immediately, which is the "
                     "only issue", "correct": False,
             "why": "The bigger issue is the safety risk of exposed live "
                    "copper, not whether the cable still works."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s23",
        "band": "standard",
        "text": "A moisture-sensing circuit tests a soil sample at 6.0 V and "
                "reads 0.0050 A. What resistance does it detect, and how "
                "would you classify the soil at that reading?",
        "options": [
            {"text": "1200 Ω — an insulator", "correct": False,
             "why": "1200 Ω still passes a small real current — far short "
                    "of an insulator's range."},
            {"text": "0.00083 Ω — a poor conductor", "correct": False,
             "why": "That divides the current by the p.d., the wrong way "
                    "up."},
            {"text": "1.2 Ω — a conductor", "correct": False,
             "why": "That treats 0.0050 as amps directly without converting "
                    "properly, and drops a factor of a thousand."},
            {"text": "1200 Ω — a poor conductor", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s24",
        "band": "standard",
        "text": "Copper, silicon and a plastic ruler are given, and you are "
                "told one of the three can have its resistance deliberately "
                "tuned by the manufacturer. Which one, and why?",
        "options": [
            {"text": "Copper, because any metal's resistance can be tuned "
                     "by alloying it with anything", "correct": False,
             "why": "Alloying changes a metal's resistance a little; it is "
                    "not the deliberate, large-scale tuning meant here."},
            {"text": "Silicon, because doping lets its resistance be "
                     "engineered to a chosen value.", "correct": True},
            {"text": "The plastic ruler, because an insulator's resistance "
                     "can be set to any value the manufacturer chooses", "correct": False,
             "why": "That describes choosing a different insulator, not "
                    "tuning one specimen's resistance on purpose."},
            {"text": "None of the three — resistance is fixed by nature for "
                     "every material", "correct": False,
             "why": "Doping is exactly a deliberate, engineered change to "
                    "silicon's resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s25",
        "band": "standard",
        "text": "Why are the pins of a plug always made from a metal, never "
                "from a graphite-like material, even though graphite does "
                "conduct?",
        "options": [
            {"text": "Graphite is too heavy to use in a small plug",
             "correct": False,
             "why": "Weight is not the reason; resistance is."},
            {"text": "Graphite cannot be shaped into pins", "correct": False,
             "why": "Shape is not the obstacle; graphite could be shaped, "
                    "but its resistance would be far too high for the job."},
            {"text": "Graphite resists far more than a metal, and a plug's "
                     "pins need the lowest possible resistance to carry "
                     "mains current safely.", "correct": True},
            {"text": "There is no real difference, and either would work "
                     "equally well in a plug carrying mains current into any ordinary household appliance.", "correct": False,
             "why": "Graphite resists many times more than a metal like "
                    "brass, which matters a great deal for a plug's pins."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s26",
        "band": "standard",
        "text": "Dry wood and a plastic ruler are both classed as "
                "insulators, but their resistances differ by hundreds of "
                "times. What does that tell you about the word "
                "\"insulator\"?",
        "options": [
            {"text": "It means one of the two must actually be a conductor",
             "correct": False,
             "why": "Both genuinely sit at the insulating end of the range; "
                    "neither is a conductor."},
            {"text": "It means wood is secretly a better insulator than "
                     "plastic", "correct": False,
             "why": "Plastic's resistance is the far bigger of the two, so "
                    "plastic is the better insulator here, not wood."},
            {"text": "It means the measurements must be wrong, since "
                     "insulators should all agree to a single shared "
                     "resistance value", "correct": False,
             "why": "Real insulators are not expected to share one exact "
                    "value; \"insulator\" covers a wide range."},
            {"text": "It is a broad practical category, not a single exact "
                     "value — many different resistances all count as \"too "
                     "high to matter\".", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s27",
        "band": "standard",
        "text": "A specimen on the 6.0 V bench gives an ammeter reading "
                "of 0.80 mA. What resistance and classification follow?",
        "options": [
            {"text": "7500 Ω — an insulator", "correct": False,
             "why": "7500 Ω still passes a small real current, well short "
                    "of an insulator's range."},
            {"text": "7.5 Ω — a conductor", "correct": False,
             "why": "That treats 0.80 as amps directly, without converting "
                    "the milliamps to amps first."},
            {"text": "0.00013 Ω — a poor conductor", "correct": False,
             "why": "That divides the current by the p.d., the ratio "
                    "upside down."},
            {"text": "7500 Ω — a poor conductor", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s28",
        "band": "standard",
        "text": "A 10 cm strip of graphite measures 30 Ω on the 6.0 V "
                "bench, which classes it as a good conductor. If a 100 cm "
                "strip of the same graphite were tested instead, would its "
                "classification change?",
        "options": [
            {"text": "Yes — it would become an insulator, since a tenfold "
                     "rise is enough to cross into the insulator range",
             "correct": False,
             "why": "A tenfold rise takes 30 Ω to 300 Ω, nowhere near the "
                    "100,000 Ω needed to reach the insulator range."},
            {"text": "Yes — ten times the length gives about 300 Ω, which "
                     "is past the bench's 100 Ω good-conductor ceiling.",
             "correct": True},
            {"text": "No — length changes a specimen's resistance but never "
                     "which band it falls in", "correct": False,
             "why": "The band is decided by the resistance itself, so a "
                    "change big enough to cross 100 Ω changes the band "
                    "with it."},
            {"text": "No — length never changes a specimen's resistance at "
                     "all", "correct": False,
             "why": "Length does change resistance — that is exactly why "
                    "the 100 cm piece measures more."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s29",
        "band": "standard",
        "text": "More salt is dissolved into a beaker of salt water that is "
                "already conducting well. What happens to its resistance?",
        "options": [
            {"text": "It rises, because the water becomes more crowded and "
                     "harder to move through as more particles are packed in", "correct": False,
             "why": "More dissolved ions give the charge MORE carriers, not "
                    "fewer, so the resistance falls rather than rises."},
            {"text": "It becomes infinite once the salt cannot dissolve any "
                     "further, because the undissolved grains block the "
                     "ions already there", "correct": False,
             "why": "Nothing here drives the resistance towards infinite; "
                    "more dissolved salt only lowers it further."},
            {"text": "It stays exactly the same, since it was already "
                     "conducting", "correct": False,
             "why": "Adding more ions genuinely changes how many charge "
                    "carriers are available."},
            {"text": "It falls further, because there are now even more "
                     "dissolved ions free to carry the charge.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-s30",
        "band": "standard",
        "text": "A safety guide says never to touch a light switch with wet "
                "hands. Using resistance, explain why wet skin makes this "
                "more dangerous.",
        "options": [
            {"text": "Wet skin generates its own extra voltage",
             "correct": False,
             "why": "Wet skin does not generate any voltage of its own; the "
                    "danger comes from a change in resistance, not a new "
                    "source."},
            {"text": "Wet skin's extra moisture and dissolved salts lower "
                     "the skin's resistance, letting far more current "
                     "through a person for the same voltage.", "correct": True},
            {"text": "Water attracts the electric current towards it from a "
                     "distance", "correct": False,
             "why": "Current needs an actual conducting path; it is not "
                    "pulled through empty air."},
            {"text": "Wet skin has no effect at all on the current — the "
                     "danger is only from the switch getting wet, never "
                     "from the person holding it",
             "correct": False,
             "why": "The skin's own resistance is exactly what changes and "
                    "is exactly why the danger rises."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · harder ─────────────────────────────────────
    {
        "id": "p8-06-h08",
        "band": "harder",
        "text": "A specimen on the 6.0 V bench takes fifteen minutes to "
                "settle to a steady reading of 24 mA. What is its "
                "steady-state resistance, and how should it be classified?",
        "options": [
            {"text": "250 Ω — a poor conductor", "correct": True},
            {"text": "250 Ω — a conductor", "correct": False,
             "why": "250 Ω is above this bench's hundred-ohm good-conductor "
                    "ceiling, which makes it a poor conductor, not a "
                    "conductor."},
            {"text": "0.0040 Ω — a poor conductor", "correct": False,
             "why": "That divides the current by the p.d., the ratio "
                    "upside down."},
            {"text": "6.024 Ω — a poor conductor", "correct": False,
             "why": "That adds the p.d. and the current together rather "
                    "than dividing them."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h09",
        "band": "harder",
        "text": "On the resistance chart, copper's bar looks only slightly "
                "shorter than nichrome's, even though nichrome resists "
                "about twenty times more. Why doesn't the bar length show "
                "that clearly?",
        "options": [
            {"text": "Because the axis is logarithmic — equal DISTANCES "
                     "represent equal RATIOS, not equal differences, so a "
                     "modest ratio like twenty makes only a small visual "
                     "gap.", "correct": True},
            {"text": "Because the chart-maker measured the two specimens "
                     "incorrectly", "correct": False,
             "why": "No measuring error is implied; the twenty-times figure "
                    "is the true ratio."},
            {"text": "Because copper and nichrome are actually very close "
                     "in resistance really once you allow for the scale used to draw the whole chart from end to end", "correct": False,
             "why": "Twenty times apart is a genuine, large difference, not "
                    "a close one."},
            {"text": "Because the chart rounds all small resistances to the "
                     "same value", "correct": False,
             "why": "No such rounding is applied; every specimen keeps its "
                    "own true value."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h10",
        "band": "harder",
        "text": "A pure silicon crystal is a poor conductor. Adding "
                "phosphorus atoms turns it into a much better one. Explain, "
                "in terms of charge carriers, why this works.",
        "options": [
            {"text": "The phosphorus atoms contribute spare electrons that "
                     "are free to move, giving the silicon far more charge "
                     "carriers than it had alone.", "correct": True},
            {"text": "Phosphorus atoms physically punch holes through the "
                     "silicon for the current to flow through on its way "
                     "across the crystal",
             "correct": False,
             "why": "Nothing is physically punched; the change is about "
                    "electrons being made available, not tunnels being "
                    "drilled."},
            {"text": "Phosphorus makes the silicon crystal melt slightly, "
                     "which lets charge move", "correct": False,
             "why": "The crystal stays solid; the effect is electronic, not "
                    "a change of state."},
            {"text": "Phosphorus is itself a perfect conductor, so it "
                     "carries all the current on its own", "correct": False,
             "why": "It is the doped SILICON as a whole that conducts "
                    "better, not phosphorus acting as a separate wire."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h11",
        "band": "harder",
        "text": "A superconducting wire suddenly warms above its critical "
                "temperature while still carrying a large current. What "
                "happens?",
        "options": [
            {"text": "Nothing changes, since the current was already "
                     "flowing and will keep flowing forever regardless of "
                     "temperature once it has been started", "correct": False,
             "why": "The zero-resistance property only holds below the "
                    "critical temperature; above it, the wire behaves like "
                    "an ordinary conductor again."},
            {"text": "It regains an ordinary resistance, and that "
                     "resistance always has a large current to dissipate "
                     "as heat, which can be dangerous.", "correct": True},
            {"text": "The wire becomes a perfect insulator instead",
             "correct": False,
             "why": "Losing superconductivity means gaining an ordinary, "
                    "modest resistance, not becoming an insulator."},
            {"text": "The current reverses direction to protect the wire",
             "correct": False,
             "why": "Nothing in the physics makes the current reverse to "
                    "protect anything."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h12",
        "band": "harder",
        "text": "A manufacturer advertises a cable sheath as a \"perfect "
                "insulator\". Is that claim exactly true?",
        "options": [
            {"text": "Yes — plastic has exactly zero free charges, so "
                     "exactly zero current can ever pass through it",
             "correct": False,
             "why": "At an ordinary voltage that is true almost to the "
                    "point of being unmeasurable, but \"exactly zero\" is "
                    "stronger than the physics allows."},
            {"text": "No — because the sheath conducts about as well as the "
                     "copper it covers", "correct": False,
             "why": "The sheath resists enormously more than the copper "
                    "core; the two are nothing alike."},
            {"text": "No — every real insulator still passes some current, "
                     "however tiny; \"perfect\" is a convenient "
                     "exaggeration, not a literal one.", "correct": True},
            {"text": "Yes — because the word \"perfect\" has a precise "
                     "scientific meaning of zero current under all "
                     "conditions, which manufacturers are required to meet",
             "correct": False,
             "why": "\"Perfect\" here is marketing language, not a defined "
                    "physics term with that exact meaning."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h13",
        "band": "harder",
        "text": "A 10 cm strip of a material measures 40 Ω. What length of "
                "the SAME material would be needed to reach 1000 Ω, and "
                "would that piece still classify as a conductor or a poor "
                "conductor?",
        "options": [
            {"text": "25 cm, and it would stay a conductor", "correct": False,
             "why": "That treats the required increase as ×2.5 rather than "
                    "×25; 1000 Ω is twenty-five times 40 Ω, not two and a "
                    "half."},
            {"text": "2.5 cm, and it would become an insulator",
             "correct": False,
             "why": "A SHORTER piece resists less, not more; reaching a "
                    "bigger resistance needs a LONGER piece."},
            {"text": "250 cm, and it would still count as a conductor, "
                     "since the material itself has not changed",
             "correct": False,
             "why": "A resistance of 1000 Ω is above this bench's 100 Ω "
                    "good-conductor ceiling, so it counts as a poor "
                    "conductor now, not a conductor."},
            {"text": "250 cm, and it would now be a poor conductor rather "
                     "than a conductor.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h14",
        "band": "harder",
        "text": "Why do bathroom safety rules ban ordinary plug sockets from "
                "being fitted within reach of a bath, even though the flex "
                "and casing are insulated?",
        "options": [
            {"text": "Because water always short-circuits any plug it "
                     "touches instantly", "correct": False,
             "why": "That overstates the mechanism; the real risk is "
                    "moisture lowering resistance along new paths, not a "
                    "guaranteed instant short."},
            {"text": "Because bathrooms are too small to fit a socket "
                     "safely", "correct": False,
             "why": "Room size is not the electrical reason for the rule."},
            {"text": "Because a bathroom is full of water and steam, which "
                     "can lower the resistance of surfaces and skin enough "
                     "for a dangerous current to find a path that dry "
                     "insulation would normally prevent.", "correct": True},
            {"text": "Because insulation stops working completely once it "
                     "is warm and humid and no longer resists any current at all however well it was made in the first place, whatever the manufacturer originally claimed about it", "correct": False,
             "why": "The insulation itself does not simply stop working; "
                    "the danger is the extra conducting paths moisture "
                    "creates elsewhere."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h15",
        "band": "harder",
        "text": "A 5 cm strip of material A measures 2,000,000 Ω; a 20 cm "
                "strip of material B (same cross-section) measures "
                "3,000,000 Ω. Scaled to the SAME length, which material "
                "actually resists more per centimetre?",
        "options": [
            {"text": "Material A — once scaled to the same length, it "
                     "resists more per centimetre (400,000 Ω/cm against "
                     "material B's 150,000 Ω/cm).", "correct": True},
            {"text": "Material B, because its raw reading of 3,000,000 Ω is "
                     "the bigger number, whatever length each strip "
                     "happened to be cut to", "correct": False,
             "why": "B's reading covers a length four times longer than A's, "
                    "so the raw numbers are not a fair comparison."},
            {"text": "They are equal once you account for length",
             "correct": False,
             "why": "400,000 Ω per centimetre and 150,000 Ω per centimetre "
                    "are not equal."},
            {"text": "It cannot be worked out without knowing the "
                     "material's thickness", "correct": False,
             "why": "The specimens are stated to share the same "
                    "cross-section, so the per-centimetre comparison can be "
                    "made directly from the given readings and lengths."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h16",
        "band": "harder",
        "text": "A bare wire of NICHROME (not copper) is clipped straight "
                "across the same 6.0 V supply. Nichrome measures 1.1 Ω for "
                "10 cm. Should the ammeter reading be treated as "
                "\"supply-limited\" the way copper's is?",
        "options": [
            {"text": "No — 1.1 Ω is enough real resistance to give a "
                     "genuine, honest current of about 5.5 A; only copper's "
                     "near-zero resistance makes its current meaningless to "
                     "print.", "correct": True},
            {"text": "Yes — any bare wire across a supply is automatically "
                     "a short circuit, whatever its resistance and "
                     "whatever current it happens to draw once it is "
                     "clipped straight across the terminals",
             "correct": False,
             "why": "That over-generalises copper's specific case; "
                    "nichrome's resistance is high enough to give a genuine, "
                    "printable reading here."},
            {"text": "No — because nichrome cannot be short-circuited, ever",
             "correct": False,
             "why": "Nichrome COULD be short-circuited in principle; here it "
                    "simply resists enough not to need that treatment."},
            {"text": "Yes — because 5.5 A is too large a number for a "
                     "school ammeter to be trusted", "correct": False,
             "why": "The issue with copper was the READING's validity given "
                    "the supply's own resistance, not the size of the "
                    "number on its own."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h17",
        "band": "harder",
        "text": "As dry wood absorbs a little moisture from humid air, does "
                "it ever cross from \"insulator\" into \"poor conductor\" "
                "on this bench's scale?",
        "options": [
            {"text": "It could — its resistance can fall enough with added "
                     "moisture to cross the 100,000 Ω line into the "
                     "poor-conductor range.", "correct": True},
            {"text": "No — once something is classed an insulator it can "
                     "never become anything else under any circumstance whatsoever no matter what happens to it afterwards", "correct": False,
             "why": "The whole range is continuous, and damp wood is "
                    "already known to conduct far better than dry wood."},
            {"text": "Yes — but only if the wood is completely submerged in "
                     "water", "correct": False,
             "why": "Even damp, unsubmerged wood is already known to "
                    "conduct far better than dry wood."},
            {"text": "No — dry wood's resistance never changes for any "
                     "reason", "correct": False,
             "why": "Moisture is exactly the kind of change that shifts a "
                    "specimen's resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h18",
        "band": "harder",
        "text": "A technician wants to test whether a suspect cable's "
                "copper core is still intact after a fire, without cutting "
                "it open. Explain how measuring its resistance from end to "
                "end could tell them, referring to what an undamaged length "
                "of copper should measure.",
        "options": [
            {"text": "Any reading at all proves the copper is undamaged, "
                     "since even a broken wire has a resistance of exactly "
                     "the same size as an intact one of the same length no matter how badly the fire damaged the cable", "correct": False,
             "why": "A full break gives an effectively enormous reading, "
                    "wildly different from an intact core's fraction of an "
                    "ohm."},
            {"text": "An intact core of that length should measure only a "
                     "fraction of an ohm, like any short piece of copper; a "
                     "much higher reading would mean the copper has been "
                     "damaged or broken somewhere along its length.",
             "correct": True},
            {"text": "Resistance cannot tell you anything about internal "
                     "damage, only a visual inspection can", "correct": False,
             "why": "Resistance is exactly the tool being described here — "
                    "it can reveal damage a visual check would miss."},
            {"text": "A HIGHER reading than normal would mean the copper is "
                     "undamaged, since heat improves a metal's "
                     "conductivity", "correct": False,
             "why": "Fire damage typically raises a metal's resistance "
                    "rather than improving its conductivity."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h19",
        "band": "harder",
        "text": "A silicon sample and a piece of graphite happen to measure "
                "the same resistance today. Does that mean they belong in "
                "the same category permanently?",
        "options": [
            {"text": "Yes — equal resistance always means the same "
                     "classification, permanently", "correct": False,
             "why": "One of the two can be re-engineered to a very "
                    "different resistance; equal resistance today says "
                    "nothing about tomorrow."},
            {"text": "No — because graphite and silicon can never have the "
                     "same resistance, even briefly", "correct": False,
             "why": "The question's own premise is that they DO happen to "
                    "match today."},
            {"text": "No — the graphite's resistance is essentially fixed "
                     "by its own structure, while the silicon's could be "
                     "changed hugely by doping it further, so the "
                     "coincidence is temporary and about resistance, not "
                     "about category.", "correct": True},
            {"text": "Yes — because only conductors and insulators exist, "
                     "so anything with the same number must be the same "
                     "kind of material, whatever it is made from and however that resistance was arrived at in each case", "correct": False,
             "why": "Semiconductors are a genuine third category on this "
                    "page, distinct from both."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h20",
        "band": "harder",
        "text": "Dry skin might resist around 100,000 Ω; the same skin, "
                "wet, might resist closer to 1,000 Ω. Using I = V ÷ R, "
                "explain in words (no need to calculate) why the wet case "
                "is far more dangerous at the same voltage.",
        "options": [
            {"text": "The wet case is dangerous because water itself "
                     "carries an electric charge that attacks the body directly, the moment skin gets wet anywhere near a switch",
             "correct": False,
             "why": "Water is not itself charged; the danger comes from the "
                    "drop in skin resistance, not from a charge in the "
                    "water."},
            {"text": "The wet case is dangerous only because it feels "
                     "colder, distracting the person", "correct": False,
             "why": "Temperature sensation plays no part in the electrical "
                    "danger being described here."},
            {"text": "The far lower resistance means far more current "
                     "passes through the body for exactly the same push, "
                     "and it is the current through the body that causes "
                     "harm.", "correct": True},
            {"text": "Both cases are equally dangerous, since the voltage "
                     "has not changed", "correct": False,
             "why": "The voltage is the same, but the current is not — a "
                    "hundred-fold drop in resistance means a hundred-fold "
                    "rise in current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h21",
        "band": "harder",
        "text": "Two materials' bars on the log chart look almost the same "
                "length, yet a caption says one resists \"about four "
                "hundred times as much\" as the other. How can bars that "
                "look similar represent such different numbers?",
        "options": [
            {"text": "The caption must be a printing mistake, since "
                     "equal-length bars mean equal resistance on any "
                     "chart, whatever scale it is drawn to",
             "correct": False,
             "why": "On a logarithmic axis, similar bar lengths do NOT mean "
                    "similar resistances; the caption's number is the true "
                    "one."},
            {"text": "The bars are only similar in COLOUR, not in length, "
                     "once you look closely", "correct": False,
             "why": "That sidesteps the actual explanation, which is about "
                    "how the logarithmic scale itself compresses large "
                    "ratios."},
            {"text": "Because equal-looking gaps near the high end of a "
                     "logarithmic axis correspond to far bigger real "
                     "differences than the same gap near the low end.",
             "correct": True},
            {"text": "Resistance charts always exaggerate small differences "
                     "on purpose", "correct": False,
             "why": "A logarithmic scale compresses huge ranges onto one "
                    "axis; it does not exaggerate small differences."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h22",
        "band": "harder",
        "text": "A moisture alarm on the 6.0 V bench fires only once the "
                "specimen across it passes at least 1.0 mA. What is the "
                "largest resistance that will still set the alarm off, and "
                "which band does that limit sit in?",
        "options": [
            {"text": "6.0 Ω, which sits in the good-conductor band",
             "correct": False,
             "why": "That divides 6.0 V by 1.0 as though the trigger "
                    "current were a whole amp; 1.0 mA is a thousandth of "
                    "that."},
            {"text": "0.00017 Ω, which sits in the good-conductor band",
             "correct": False,
             "why": "That divides the current by the p.d. — the ratio the "
                    "wrong way up."},
            {"text": "6000 Ω, which sits in the poor-conductor band",
             "correct": True},
            {"text": "6,000,000 Ω, which sits in the insulator band",
             "correct": False,
             "why": "That multiplies by a thousand instead of dividing by "
                    "it when converting the milliamps."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h23",
        "band": "harder",
        "text": "A fuse is a short, deliberately thin piece of wire inside a "
                "plug. Explain, using resistance and current, why it melts "
                "and breaks the circuit only when the current gets "
                "dangerously large.",
        "options": [
            {"text": "The fuse melts because it is an insulator that "
                     "cannot handle any current", "correct": False,
             "why": "A fuse element is a CONDUCTOR that carries ordinary "
                    "currents perfectly well; it is not an insulator."},
            {"text": "The thin wire's own resistance means large currents "
                     "transfer a lot of energy to heat inside it; past a "
                     "certain current that heat is enough to melt the wire "
                     "and break the loop.", "correct": True},
            {"text": "The fuse works by sensing the voltage directly and "
                     "switching off electronically", "correct": False,
             "why": "That describes a different kind of protection device; "
                    "a simple fuse works by melting from heat, not by "
                    "sensing voltage."},
            {"text": "The fuse melts at the same current every appliance "
                     "uses, which is why one fuse rating fits all "
                     "appliances from a kettle to a phone charger", "correct": False,
             "why": "Different fuses have different ratings for different "
                    "appliances; there is no single rating that fits all."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h24",
        "band": "harder",
        "text": "A metal's resistance rises when it is heated. Silicon (a "
                "semiconductor) behaves the opposite way: warming it frees "
                "up more charge carriers, lowering its resistance. Why "
                "might engineers need to bear this contrast in mind when "
                "designing circuits that get warm?",
        "options": [
            {"text": "They don't need to — heat affects every material in a "
                     "circuit identically", "correct": False,
             "why": "The question's own premise is that metals and silicon "
                    "respond to heat in opposite directions."},
            {"text": "The contrast only matters in space, where there is no "
                     "air to carry heat away and every circuit runs perfectly cool however much current is flowing through either kind of component in the whole circuit, "
                     "however hot it gets.", "correct": False,
             "why": "The contrast is about how each material's own "
                    "resistance responds to temperature, wherever the "
                    "circuit happens to be."},
            {"text": "Silicon actually behaves exactly like a metal once it "
                     "is warm enough", "correct": False,
             "why": "The contrast is stated to hold as it warms; silicon "
                    "does not switch to behaving like a metal."},
            {"text": "A metal component's resistance climbing with heat and "
                     "a silicon component's resistance falling with heat "
                     "can have opposite, and sometimes compounding, effects "
                     "on the currents in the same warm circuit.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h25",
        "band": "harder",
        "text": "Rank copper, nichrome, salt water and a plastic ruler from "
                "the one you would MOST want as a plug's pin material to "
                "the one you would LEAST want, and justify the order using "
                "resistance.",
        "options": [
            {"text": "Plastic first, because pins should protect the user "
                     "from any current at all", "correct": False,
             "why": "A pin's whole job is to CARRY current into the "
                    "appliance; plastic's huge resistance would make it "
                    "useless as a pin."},
            {"text": "All four would work equally well, since a pin's shape "
                     "matters more than its material in any plug ever manufactured anywhere in the world, whatever the current it has to carry", "correct": False,
             "why": "The material's resistance is exactly what decides "
                    "whether a pin can do its job."},
            {"text": "Salt water first, since it is a liquid and easiest to "
                     "shape into a pin", "correct": False,
             "why": "Ease of shaping is not the deciding factor, and salt "
                    "water resists far more than either metal."},
            {"text": "Copper first (lowest resistance, best conductor), "
                     "then nichrome, then salt water, then plastic last (far "
                     "too high a resistance to carry any useful current).",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h26",
        "band": "harder",
        "text": "A specimen is to be classed as a \"poor conductor\" (any "
                "reading from 100 Ω up to 100,000 Ω) on the 6.0 V bench. "
                "Between which two ammeter readings must its current fall?",
        "options": [
            {"text": "Between 60 mA and 6.0 A", "correct": False,
             "why": "That range does not correspond to the stated "
                    "resistance window at all."},
            {"text": "Above 60 mA only, with no lower limit", "correct": False,
             "why": "That misses the upper-resistance boundary; the "
                    "poor-conductor band has a lower current limit too, at "
                    "0.060 mA."},
            {"text": "Between 6.0 mA and 600 mA overall", "correct": False,
             "why": "That range is a hundred times too big at both ends."},
            {"text": "Between 0.060 mA and 60 mA.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h27",
        "band": "harder",
        "text": "A 40 cm strip of graphite measures 120 Ω, just inside the "
                "poor-conductor range. Suggest ONE change to the specimen "
                "that would move it back into the good-conductor range, and "
                "explain why it would work.",
        "options": [
            {"text": "Use a longer piece, since more graphite means more "
                     "current can get through, which lowers its "
                     "resistance further every time", "correct": False,
             "why": "A longer piece raises the resistance further, moving "
                    "it deeper into the poor-conductor range, not out of "
                    "it."},
            {"text": "Use a shorter piece — cutting it back down towards "
                     "10 cm would lower its resistance below 100 Ω again, "
                     "since a shorter path always resists less.",
             "correct": True},
            {"text": "Test it at a higher voltage, since more volts always "
                     "lowers resistance", "correct": False,
             "why": "Graphite's resistance does not fall with voltage the "
                    "way a lamp's does; that fact belongs to a different "
                    "kind of component."},
            {"text": "Nothing can move it, since a poor conductor can never "
                     "become a good one", "correct": False,
             "why": "The range is continuous, and a shorter piece of the "
                    "same material genuinely resists less."},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h28",
        "band": "harder",
        "text": "A specimen's resistance is measured as 98 Ω, 101 Ω and "
                "99 Ω on three repeats — scattered either side of the "
                "100 Ω good/poor boundary. What is the sensible conclusion "
                "about its classification?",
        "options": [
            {"text": "It must be classified twice, once as each category",
             "correct": False,
             "why": "A specimen is one material with one true resistance "
                    "near 100 Ω, not two different materials."},
            {"text": "It should always be rounded up to the poor-conductor "
                     "side to be safe whenever a reading is anywhere near "
                     "the line, however small the scatter turns out to "
                     "be", "correct": False,
             "why": "There is no such rounding rule; the sensible reading "
                    "is that the scatter does not change the classification "
                    "either way."},
            {"text": "The three readings prove the meter is broken",
             "correct": False,
             "why": "A percent or two of scatter around one true value is "
                    "ordinary experimental spread, not a fault."},
            {"text": "It sits right at the boundary, and small experimental "
                     "scatter around 100 Ω does not change what kind of "
                     "material it clearly is — the classification is not "
                     "sensitive to a percent or two either way.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h29",
        "band": "harder",
        "text": "Specimen X is 5 cm and measures 50 Ω. Specimen Y is 20 cm "
                "of the SAME material and measures 200 Ω. Are X and Y made "
                "of two different materials, or could they be the same "
                "one?",
        "options": [
            {"text": "They must be different materials, since their raw "
                     "resistances (50 Ω and 200 Ω) are not equal",
             "correct": False,
             "why": "The two specimens are different LENGTHS, so their raw "
                    "resistances are not expected to match even for the "
                    "same material."},
            {"text": "It cannot be decided without knowing the specimens' "
                     "colour", "correct": False,
             "why": "Colour has no bearing on resistance; the lengths and "
                    "readings already given are enough to compare the two "
                    "per centimetre."},
            {"text": "They must be different materials, since resistance "
                     "should stay the same regardless of length however long or short each piece "
                     "happens to be.",
             "correct": False,
             "why": "Resistance does not stay fixed as length changes; a "
                    "longer specimen of the SAME material resists more."},
            {"text": "They could well be the same material — Y's "
                     "resistance is exactly four times X's, matching Y "
                     "being exactly four times as long.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-06-h30",
        "band": "harder",
        "text": "Summarise, using resistance, why a single wire can be "
                "safely handled at one end while carrying a dangerous "
                "current, provided its plastic sheath is intact.",
        "options": [
            {"text": "The copper core has almost no current in it near the "
                     "ends of the wire, only in the middle", "correct": False,
             "why": "A single wire carries the same current at every point "
                    "along its length, not more in the middle."},
            {"text": "The sheath's enormous resistance means almost no "
                     "current can escape sideways into a hand touching it, "
                     "even though the copper core inside is carrying "
                     "plenty of current along its length.", "correct": True},
            {"text": "Handling the wire is safe because plastic conducts "
                     "just as well as copper, so touching it is no "
                     "different from touching the core itself, wherever you happen to touch it along its whole length.", "correct": False,
             "why": "Plastic resists enormously more than copper; that "
                    "difference is exactly why handling it is safe."},
            {"text": "The current only becomes dangerous once the wire is "
                     "cut, never while it is intact", "correct": False,
             "why": "That does not explain the mechanism asked for — it is "
                    "the sheath's resistance keeping the current away from "
                    "a hand, not the wire being uncut."},
        ],
        "figure": None,
    },
]
