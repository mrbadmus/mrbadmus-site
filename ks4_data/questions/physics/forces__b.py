"""Physics · Forces — work, elasticity, moments, fluid pressure, upthrust, speed.

Part B of the `forces` topic: six subtopics × twelve questions. The distractors
are built from the six misconceptions the briefs declare — work confused with
weight or with power, "extension" read as the spring's total length, moment
distance measured along the lever rather than perpendicular to the force,
P = F × A instead of F ÷ A, upthrust believed to depend on the object's own
mass, and speed treated as interchangeable with velocity. Calculation
distractors are the arithmetic each of those errors actually produces
(unconverted centimetres, an omitted g, an inverted ratio), never noise.

Nothing here restates a lesson page's "Test yourself" question: where a stem
covers the same spec content it reverses the direction of reasoning (find the
force from the moment rather than the moment from the force; find the density
from the submerged fraction rather than the fraction from the densities) or
moves to an unfamiliar context.
"""

TOPIC = "forces"
SUBJECT = "physics"

QUESTIONS = [
    # ── work-done-energy-transfer ───────────────────────────────────────
    {
        "id": "ks4-work-done-energy-transfer-e01",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which combination of units is equivalent to one joule?",
        "options": [
            "One newton per metre (1 N/m)",
            "One newton per second (1 N/s)",
            "One newton-metre (1 N·m)",
            "One newton per kilogram (1 N/kg)",
        ],
        "correct_index": 2,
        "why": "Work done is force multiplied by distance, so one joule is one "
               "newton acting through one metre.",
    },
    {
        "id": "ks4-work-done-energy-transfer-e02",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the symbol W represents in the equation W = Fs.",
        "options": [
            "The work done, measured in joules (J)",
            "The weight of the object, measured in newtons (N)",
            "The power developed, measured in watts (W)",
            "The applied force, measured in newtons (N)",
        ],
        "correct_index": 0,
        "why": "In this equation W is the work done — the energy transferred, "
               "in joules — not the weight, which would be a force in newtons.",
    },
    {
        "id": "ks4-work-done-energy-transfer-e03",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener pushes a wheelbarrow 14 m along a path with a "
                "steady horizontal force of 85 N. Calculate the work done by "
                "the gardener.",
        "options": [
            "6.07 J",
            "0.165 J",
            "99 J",
            "1190 J",
        ],
        "correct_index": 3,
        "why": "W = F × s = 85 N × 14 m = 1190 J.",
    },
    {
        "id": "ks4-work-done-energy-transfer-e04",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student pushes on a parked lorry with a force of 400 N "
                "for 20 s. The lorry does not move. State the work done on "
                "the lorry by the student.",
        "options": [
            "8000 J",
            "0 J",
            "400 J",
            "20 J",
        ],
        "correct_index": 1,
        "why": "W = Fs, and s is zero because the lorry does not move, so no "
               "energy is transferred however hard the student pushes.",
    },
    {
        "id": "ks4-work-done-energy-transfer-s01",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sledge is dragged 25 m along level ground and 4500 J of "
                "work is done against friction. Calculate the size of the "
                "friction force.",
        "options": [
            "112 500 N",
            "180 N",
            "4525 N",
            "0.0056 N",
        ],
        "correct_index": 1,
        "why": "Rearranging W = F × s gives F = W ÷ s = 4500 J ÷ 25 m = 180 N.",
    },
    {
        "id": "ks4-work-done-energy-transfer-s02",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist pushes against air resistance with a constant force "
                "of 120 N while travelling at a steady 8.0 m/s. Calculate the "
                "power developed.",
        "options": [
            "15 W",
            "128 W",
            "9600 W",
            "960 W",
        ],
        "correct_index": 3,
        "why": "For steady motion P = W ÷ t = F × v, so P = 120 N × 8.0 m/s = "
               "960 W.",
    },
    {
        "id": "ks4-work-done-energy-transfer-s03",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 3.0 kg book is lifted at a steady speed onto a shelf 1.5 m "
                "above the bench. Calculate the work done against gravity. "
                "(g = 9.8 N/kg)",
        "options": [
            "44.1 J",
            "4.50 J",
            "29.4 J",
            "441 J",
        ],
        "correct_index": 0,
        "why": "The lifting force equals the weight, mg = 3.0 × 9.8 = 29.4 N, "
               "so W = 29.4 N × 1.5 m = 44.1 J.",
    },
    {
        "id": "ks4-work-done-energy-transfer-s04",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A box is pushed across a rough floor at a constant speed. "
                "Describe what happens to the energy transferred by the "
                "pushing force.",
        "options": [
            "It is stored as gravitational potential energy, because the box "
            "has been moved",
            "It is stored in the kinetic energy store of the box, which is why "
            "the box keeps moving",
            "It is transferred to thermal energy stores of the box and floor "
            "by friction doing work",
            "It is destroyed by friction, so there is less energy afterwards "
            "than before",
        ],
        "correct_index": 2,
        "why": "At constant speed the kinetic store is unchanged, so all the "
               "work done by the push ends up heating the box and the floor.",
    },
    {
        "id": "ks4-work-done-energy-transfer-h01",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 60 kg climber ascends a vertical rock face of height 12 m "
                "in 90 s. Determine the useful output power of the climber. "
                "(g = 9.8 N/kg)",
        "options": [
            "8.00 W",
            "7056 W",
            "784 W",
            "78.4 W",
        ],
        "correct_index": 3,
        "why": "Work done against gravity = mgh = 60 × 9.8 × 12 = 7056 J, and "
               "power = 7056 J ÷ 90 s = 78.4 W.",
    },
    {
        "id": "ks4-work-done-energy-transfer-h02",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A trolley is pushed 5.0 m along a bench by a horizontal force "
                "of 12 N. Friction opposes the motion with a steady force of "
                "4.0 N. Calculate the increase in the trolley's kinetic energy "
                "store.",
        "options": [
            "60 J",
            "40 J",
            "20 J",
            "80 J",
        ],
        "correct_index": 1,
        "why": "Only the resultant force speeds the trolley up: (12 − 4) N × "
               "5.0 m = 40 J, with the other 20 J becoming thermal energy.",
    },
    {
        "id": "ks4-work-done-energy-transfer-h03",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: \"I carried a heavy suitcase up two flights of "
                "stairs and then along a 20 m level corridor, so I did work on "
                "it the whole way.\" Evaluate this statement.",
        "options": [
            "The student is right — the suitcase moved 20 m and also gained "
            "height, so work was done throughout",
            "The student is wrong — no work is done on a carried object at any "
            "point, because it is not being pushed",
            "The student is only partly right — work is done lifting the case "
            "up the stairs, but none along the level corridor",
            "The student is wrong — work is done along the corridor but not on "
            "the stairs, because the stairs are a slope",
        ],
        "correct_index": 2,
        "why": "The carrying force is vertical, so it does work while the case "
               "rises but none while the case moves horizontally.",
    },
    {
        "id": "ks4-work-done-energy-transfer-h04",
        "subtopic_slug": "work-done-energy-transfer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1200 kg car travelling at 20 m/s is brought to rest by its "
                "brakes in a distance of 40 m. Determine the average braking "
                "force.",
        "options": [
            "6000 N",
            "12 000 N",
            "300 N",
            "600 N",
        ],
        "correct_index": 0,
        "why": "The braking force does work equal to the kinetic energy, "
               "½mv² = 240 000 J, so F = 240 000 J ÷ 40 m = 6000 N.",
    },

    # ── forces-elasticity ───────────────────────────────────────────────
    {
        "id": "ks4-forces-elasticity-e01",
        "subtopic_slug": "forces-elasticity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of the spring constant, k.",
        "options": [
            "Newtons (N)",
            "Newtons per metre (N/m)",
            "Joules per metre (J/m)",
            "Newton-metres (N·m)",
        ],
        "correct_index": 1,
        "why": "k = F ÷ e, a force in newtons divided by an extension in "
               "metres, so the unit is N/m.",
    },
    {
        "id": "ks4-forces-elasticity-e02",
        "subtopic_slug": "forces-elasticity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring of spring constant 30 N/m is stretched, within its "
                "elastic limit, by an extension of 25 cm. Calculate the force "
                "applied.",
        "options": [
            "750 N",
            "120 N",
            "0.0083 N",
            "7.5 N",
        ],
        "correct_index": 3,
        "why": "F = k × e, and the extension must be in metres: 30 N/m × "
               "0.25 m = 7.5 N.",
    },
    {
        "id": "ks4-forces-elasticity-e03",
        "subtopic_slug": "forces-elasticity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement describes elastic deformation?",
        "options": [
            "The object returns to its original shape and length once the "
            "force is removed",
            "The object stays permanently longer after the force has been "
            "removed",
            "The object breaks apart at the moment the applied force is "
            "removed",
            "The object carries on stretching at a steady rate after the force "
            "is removed",
        ],
        "correct_index": 0,
        "why": "Elastic deformation is reversible — the object returns to its "
               "original shape, whereas inelastic deformation is permanent.",
    },
    {
        "id": "ks4-forces-elasticity-e04",
        "subtopic_slug": "forces-elasticity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring is stretched within its elastic limit. Predict what "
                "happens to the extension if the applied force is doubled.",
        "options": [
            "It stays the same, because the spring constant does not change",
            "It becomes four times as large, because extension depends on the "
            "force squared",
            "It doubles, because extension is directly proportional to the "
            "force",
            "It halves, because a larger force makes the spring behave more "
            "stiffly",
        ],
        "correct_index": 2,
        "why": "Within the elastic limit Hooke's law makes extension directly "
               "proportional to force, so doubling F doubles e.",
    },
    {
        "id": "ks4-forces-elasticity-s01",
        "subtopic_slug": "forces-elasticity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring of natural length 12 cm has a spring constant of "
                "40 N/m. Calculate its total length when a force of 2.0 N is "
                "applied, within the elastic limit.",
        "options": [
            "5.0 cm",
            "7.0 cm",
            "17 cm",
            "12.5 cm",
        ],
        "correct_index": 2,
        "why": "The extension is e = F ÷ k = 2.0 ÷ 40 = 0.05 m = 5 cm, which "
               "adds to the 12 cm natural length to give 17 cm.",
    },
    {
        "id": "ks4-forces-elasticity-s02",
        "subtopic_slug": "forces-elasticity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical on springs, a student plots force "
                "on the vertical axis against extension on the horizontal "
                "axis. State what the gradient of the straight section "
                "represents.",
        "options": [
            "The spring constant, in N/m",
            "The elastic potential energy stored, in J",
            "The extension at the elastic limit, in m",
            "The weight of each mass added, in N",
        ],
        "correct_index": 0,
        "why": "The gradient is force divided by extension, and F ÷ e is the "
               "spring constant k.",
    },
    {
        "id": "ks4-forces-elasticity-s03",
        "subtopic_slug": "forces-elasticity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring obeys Hooke's law up to an extension of 0.10 m. A "
                "student stretches it to an extension of 0.18 m and then "
                "removes the force. Predict what the student observes.",
        "options": [
            "The spring returns exactly to its original length, because "
            "springs are elastic materials",
            "The spring is left permanently longer, because it was taken "
            "past its elastic limit",
            "The spring returns to its original length but its spring constant "
            "has doubled",
            "The spring snaps back and settles shorter than its original "
            "natural length",
        ],
        "correct_index": 1,
        "why": "Beyond the elastic limit the deformation is inelastic, so the "
               "spring no longer returns to its original length.",
    },
    {
        "id": "ks4-forces-elasticity-s04",
        "subtopic_slug": "forces-elasticity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Springs P and Q are stretched by the same force. P extends by "
                "4.0 cm and Q extends by 10.0 cm. Compare the spring constants "
                "of P and Q.",
        "options": [
            "They have the same spring constant, because the same force was "
            "applied to both springs",
            "Q has the larger spring constant, because it extends further for "
            "the same applied force",
            "The spring constants cannot be compared, because k depends on "
            "each spring's natural length",
            "P has the larger spring constant, because it needs a larger force "
            "for each metre of extension",
        ],
        "correct_index": 3,
        "why": "k = F ÷ e, so for the same force the spring with the smaller "
               "extension is the stiffer one.",
    },
    {
        "id": "ks4-forces-elasticity-h01",
        "subtopic_slug": "forces-elasticity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring of spring constant 250 N/m is extended by 0.20 m, "
                "within its elastic limit. Calculate the elastic potential "
                "energy stored.",
        "options": [
            "5.00 J",
            "10.0 J",
            "25.0 J",
            "50.0 J",
        ],
        "correct_index": 0,
        "why": "Ee = ½ke² = 0.5 × 250 × 0.20² = 5.00 J — the extension must be "
               "squared.",
    },
    {
        "id": "ks4-forces-elasticity-h02",
        "subtopic_slug": "forces-elasticity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student stretches a spring with forces of 1.0 N, 2.0 N and "
                "3.0 N, recording extensions of 2.0 cm, 4.0 cm and 7.0 cm. "
                "Suggest what the third reading shows.",
        "options": [
            "The spring constant has increased between the second and third "
            "readings",
            "A measurement error must have been made, because extension is "
            "always proportional to force",
            "The spring has passed its elastic limit, so extension is no "
            "longer proportional to force",
            "The spring has reached its greatest possible extension and simply "
            "cannot be stretched any further",
        ],
        "correct_index": 2,
        "why": "The first two readings give 2.0 cm per newton but the third "
               "adds 3.0 cm, so proportionality has broken down.",
    },
    {
        "id": "ks4-forces-elasticity-h03",
        "subtopic_slug": "forces-elasticity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 250 g mass is hung from a spring, which extends by 5.0 cm. "
                "Determine the spring constant. (g = 9.8 N/kg)",
        "options": [
            "0.49 N/m",
            "49 000 N/m",
            "0.020 N/m",
            "49 N/m",
        ],
        "correct_index": 3,
        "why": "The stretching force is the weight, 0.250 kg × 9.8 N/kg = "
               "2.45 N, so k = F ÷ e = 2.45 ÷ 0.050 = 49 N/m.",
    },
    {
        "id": "ks4-forces-elasticity-h04",
        "subtopic_slug": "forces-elasticity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical springs, each of spring constant 60 N/m, are "
                "joined end to end to make one longer spring. A force of 3.0 N "
                "is applied to the combination. Determine the total extension.",
        "options": [
            "0.025 m",
            "0.10 m",
            "0.050 m",
            "0.20 m",
        ],
        "correct_index": 1,
        "why": "The same 3.0 N pulls on each spring, so each extends 3.0 ÷ 60 "
               "= 0.05 m and the two extensions add to 0.10 m.",
    },

    # ── moments-levers-gears ────────────────────────────────────────────
    {
        "id": "ks4-moments-levers-gears-e01",
        "subtopic_slug": "moments-levers-gears",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the unit of a moment.",
        "options": [
            "Newtons (N)",
            "Joules (J)",
            "Metres per newton (m/N)",
            "Newton-metres (N·m)",
        ],
        "correct_index": 3,
        "why": "A moment is a force multiplied by a perpendicular distance, so "
               "its unit is the newton multiplied by the metre.",
    },
    {
        "id": "ks4-moments-levers-gears-e02",
        "subtopic_slug": "moments-levers-gears",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A door handle is fitted at the edge of the door, as far as "
                "possible from the hinges. Explain why.",
        "options": [
            "The door is lighter at its edge, so a smaller force is needed to "
            "move it",
            "The distance from the pivot is largest there, so the same force "
            "gives a larger moment",
            "The hinges are weakest at the edge, so the door turns more easily "
            "from that side",
            "A handle near the hinge would give a moment larger than the door "
            "could withstand",
        ],
        "correct_index": 1,
        "why": "Moment = force × distance from the pivot, so a handle far from "
               "the hinges gives the biggest turning effect for the force you "
               "can apply.",
    },
    {
        "id": "ks4-moments-levers-gears-e03",
        "subtopic_slug": "moments-levers-gears",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which distance must be used when calculating a moment.",
        "options": [
            "The total length of the lever, measured from one end to the "
            "other end",
            "The distance from the point of the force to the far end of the "
            "lever",
            "The perpendicular distance from the force's line of action to "
            "the pivot",
            "The distance moved by the end of the lever as it turns about the "
            "pivot",
        ],
        "correct_index": 2,
        "why": "The moment uses the perpendicular distance between the pivot "
               "and the line along which the force acts, not the length of the "
               "lever.",
    },
    {
        "id": "ks4-moments-levers-gears-e04",
        "subtopic_slug": "moments-levers-gears",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A spanner turns a nut with a moment of 9.0 N·m. The force is "
                "applied at a perpendicular distance of 0.30 m from the nut. "
                "Calculate the size of the force.",
        "options": [
            "30 N",
            "2.7 N",
            "0.033 N",
            "9.3 N",
        ],
        "correct_index": 0,
        "why": "Rearranging M = F × d gives F = M ÷ d = 9.0 ÷ 0.30 = 30 N.",
    },
    {
        "id": "ks4-moments-levers-gears-s01",
        "subtopic_slug": "moments-levers-gears",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A uniform plank balances on a pivot at its centre. A child "
                "of weight 240 N sits 1.2 m to the left of the pivot, and a "
                "second child sitting 0.80 m to the right holds it level. "
                "Calculate the weight of the second child.",
        "options": [
            "360 N",
            "160 N",
            "240 N",
            "288 N",
        ],
        "correct_index": 0,
        "why": "For balance the moments are equal: 240 × 1.2 = 288 N·m, so "
               "W = 288 ÷ 0.80 = 360 N.",
    },
    {
        "id": "ks4-moments-levers-gears-s02",
        "subtopic_slug": "moments-levers-gears",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wheelbarrow is a lever with the load sitting between the "
                "wheel, which acts as the pivot, and the handles. Explain why "
                "a small force at the handles can lift a much heavier load.",
        "options": [
            "The handles are further from the load, so the weight of the load "
            "is reduced",
            "The wheel supports most of the load's weight, so the load itself "
            "becomes lighter",
            "The handles are further from the pivot than the load, so a "
            "smaller force there gives an equal moment",
            "The wheelbarrow multiplies the energy supplied to it, so much "
            "less work is needed to lift the load",
        ],
        "correct_index": 2,
        "why": "The lifting force acts at a greater distance from the pivot "
               "than the load does, so a smaller force produces the same "
               "moment — the lever multiplies force, not energy.",
    },
    {
        "id": "ks4-moments-levers-gears-s03",
        "subtopic_slug": "moments-levers-gears",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A driving gear with 12 teeth turns at 300 revolutions per "
                "minute and meshes with a driven gear with 36 teeth. "
                "Calculate the rate at which the driven gear turns.",
        "options": [
            "900 revolutions per minute",
            "300 revolutions per minute",
            "3600 revolutions per minute",
            "100 revolutions per minute",
        ],
        "correct_index": 3,
        "why": "Meshed teeth pass at the same rate, so the gear with three "
               "times as many teeth turns three times more slowly: "
               "300 ÷ 3 = 100 revolutions per minute.",
    },
    {
        "id": "ks4-moments-levers-gears-s04",
        "subtopic_slug": "moments-levers-gears",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A uniform beam is pivoted at its centre. A downward force of "
                "20 N acts 0.60 m to the left of the pivot and a downward "
                "force of 15 N acts 0.40 m to the right of it. Determine "
                "whether the beam is in equilibrium.",
        "options": [
            "It is in equilibrium, because the total downward force of 35 N "
            "acts through the central pivot",
            "It is not in equilibrium — the anticlockwise moment of 12 N·m "
            "beats the clockwise moment of 6 N·m",
            "It is not in equilibrium — the clockwise moment is the larger of "
            "the two, so the right-hand side of the beam falls",
            "It is in equilibrium, because the larger force acts at the larger "
            "distance from the pivot",
        ],
        "correct_index": 1,
        "why": "The moments are 20 × 0.60 = 12 N·m one way and 15 × 0.40 = "
               "6 N·m the other, and unequal moments mean the beam turns.",
    },
    {
        "id": "ks4-moments-levers-gears-h01",
        "subtopic_slug": "moments-levers-gears",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A crowbar 1.2 m long is used to lift a rock. The pivot is "
                "placed 0.20 m from the rock end, and a downward force of "
                "150 N is applied at the far end. Determine the greatest "
                "weight of rock that can be lifted.",
        "options": [
            "150 N",
            "750 N",
            "30 N",
            "180 N",
        ],
        "correct_index": 1,
        "why": "The moments balance about the pivot: 150 N × 1.0 m = W × "
               "0.20 m, so W = 150 ÷ 0.20 = 750 N.",
    },
    {
        "id": "ks4-moments-levers-gears-h02",
        "subtopic_slug": "moments-levers-gears",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student states: \"a heavier person always tips a seesaw "
                "down on their own side.\" Evaluate this statement.",
        "options": [
            "Correct — the larger weight always gives the larger moment, "
            "whatever the seating positions",
            "Correct, unless the heavier person sits exactly on the pivot, "
            "when neither side moves",
            "Incorrect — the heavier person tips down only if they sit further "
            "from the pivot than the lighter one",
            "Incorrect — the lighter person can balance the heavier one by "
            "sitting further from the pivot",
        ],
        "correct_index": 3,
        "why": "A moment is force × distance from the pivot, so a smaller "
               "weight at a greater distance can produce an equal moment.",
    },
    {
        "id": "ks4-moments-levers-gears-h03",
        "subtopic_slug": "moments-levers-gears",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A gearbox uses a small driving gear meshed with a large "
                "driven gear. A student claims the gearbox \"creates extra "
                "energy, because the output force is bigger\". Evaluate this "
                "claim.",
        "options": [
            "The claim is wrong — the output force is larger but acts through "
            "a smaller rotation, so the work done is unchanged",
            "The claim is correct — the gearbox multiplies the force, and so "
            "it multiplies the energy transferred as well",
            "The claim is wrong — gears reduce both the force and the energy, "
            "because of friction between the meshed teeth",
            "The claim is correct — extra energy is created whenever the gear "
            "ratio is greater than one",
        ],
        "correct_index": 0,
        "why": "Gears trade force against rotation, not energy: a bigger "
               "output force turns through a smaller angle, so the work done "
               "stays the same.",
    },
    {
        "id": "ks4-moments-levers-gears-h04",
        "subtopic_slug": "moments-levers-gears",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A uniform metre rule of weight 2.0 N is pivoted at the 30 cm "
                "mark. Its weight acts at the 50 cm mark. Calculate the "
                "downward force that must be applied at the 10 cm mark to hold "
                "the rule horizontal.",
        "options": [
            "0.40 N",
            "4.0 N",
            "2.0 N",
            "1.0 N",
        ],
        "correct_index": 2,
        "why": "The rule's weight acts 0.20 m from the pivot, giving 2.0 × "
               "0.20 = 0.40 N·m, and the applied force is also 0.20 m from the "
               "pivot, so it must be 2.0 N.",
    },

    # ── pressure-in-a-fluid ─────────────────────────────────────────────
    {
        "id": "ks4-pressure-in-a-fluid-e01",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the unit of pressure and what it is equivalent to.",
        "options": [
            "The pascal (Pa), which is one newton per square metre",
            "The pascal (Pa), which is one newton per metre",
            "The newton (N), which is one pascal per square metre",
            "The pascal (Pa), which is one square metre per newton",
        ],
        "correct_index": 0,
        "why": "Pressure is force divided by area, so 1 Pa is 1 N spread over "
               "1 m².",
    },
    {
        "id": "ks4-pressure-in-a-fluid-e02",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A force of 600 N is spread evenly over an area of 0.30 m². "
                "Calculate the pressure.",
        "options": [
            "180 Pa",
            "0.00050 Pa",
            "2000 Pa",
            "600.3 Pa",
        ],
        "correct_index": 2,
        "why": "P = F ÷ A = 600 N ÷ 0.30 m² = 2000 Pa — force is divided by "
               "area, not multiplied by it.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-e03",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the direction in which the pressure in a fluid acts at "
                "any given point.",
        "options": [
            "Downwards only, because the weight of the fluid above presses "
            "down",
            "In all directions equally at that point",
            "Sideways only, against the walls of the container",
            "Upwards only, because pressure is what produces upthrust",
        ],
        "correct_index": 1,
        "why": "The particles of a fluid move in all directions and collide "
               "with every surface, so the pressure at a point acts equally in "
               "every direction.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-e04",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how atmospheric pressure changes as altitude "
                "increases, and explain why.",
        "options": [
            "It increases, because the air is colder higher up",
            "It stays the same, because the atmosphere is the same everywhere",
            "It increases, because there is more room for the air to spread "
            "out",
            "It decreases, because there is less air above pressing down",
        ],
        "correct_index": 3,
        "why": "Atmospheric pressure comes from the weight of the column of "
               "air above you, and higher up there is less air above.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-s01",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the pressure caused by the liquid at a depth of "
                "4.0 m in a tank of brine of density 1250 kg/m³. "
                "(g = 9.8 N/kg)",
        "options": [
            "39 Pa",
            "510 Pa",
            "5000 Pa",
            "49 000 Pa",
        ],
        "correct_index": 3,
        "why": "P = hρg = 4.0 m × 1250 kg/m³ × 9.8 N/kg = 49 000 Pa.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-s02",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hydraulic press pushes on the fluid with a force of 4500 N "
                "through a piston of area 0.015 m². Calculate the pressure "
                "produced in the fluid.",
        "options": [
            "67.5 Pa",
            "300 000 Pa",
            "30 000 Pa",
            "4500 Pa",
        ],
        "correct_index": 1,
        "why": "P = F ÷ A = 4500 N ÷ 0.015 m² = 300 000 Pa.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-s03",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a drinking straw allows a drink to rise up the "
                "tube.",
        "options": [
            "Reducing the pressure inside the straw lets atmospheric "
            "pressure push the drink up",
            "The suction force created by the lungs pulls the drink upwards "
            "through the straw",
            "The straw contains a vacuum, and a vacuum attracts the liquid "
            "towards it",
            "The drink is squeezed upwards because the atmospheric pressure "
            "inside the straw increases",
        ],
        "correct_index": 0,
        "why": "You cannot pull a liquid — lowering the pressure inside the "
               "straw lets the atmosphere pressing on the drink's surface push "
               "it up.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-s04",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the wall of a reservoir dam is built much thicker "
                "at its base than at the top.",
        "options": [
            "The base carries the whole weight of the wall above it, which the "
            "top does not",
            "Water is denser near the bottom of the reservoir, so it presses "
            "harder there",
            "Water pressure increases with depth, so the force on the wall is "
            "greatest near the base",
            "The pressure at the base acts downwards, so the wall must be wide "
            "enough to resist it",
        ],
        "correct_index": 2,
        "why": "P = hρg, so the water pushes hardest where it is deepest and "
               "the wall must be strongest there.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-h01",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Determine the total pressure acting on a diver at a depth of "
                "20 m in seawater. (density of seawater = 1025 kg/m³, "
                "g = 9.8 N/kg, atmospheric pressure = 100 kPa)",
        "options": [
            "201 kPa",
            "100 kPa",
            "301 kPa",
            "101 kPa",
        ],
        "correct_index": 2,
        "why": "P = hρg gives 20 × 1025 × 9.8 = 201 kPa from the water, and "
               "the atmosphere above the sea adds a further 100 kPa.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-h02",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A rectangular block of weight 45 N rests on a table on a face "
                "measuring 0.30 m by 0.50 m. It is then stood on a face "
                "measuring 0.30 m by 0.10 m. Determine how the pressure on the "
                "table changes.",
        "options": [
            "It rises from 300 Pa to 1500 Pa, because the same weight acts on "
            "one fifth of the area",
            "It falls from 1500 Pa to 300 Pa, because the smaller face spreads "
            "the weight further",
            "It stays at 300 Pa, because the weight of the block has not "
            "changed",
            "It falls from 6.8 Pa to 1.4 Pa, because pressure is weight "
            "multiplied by area",
        ],
        "correct_index": 0,
        "why": "P = F ÷ A, and the area falls from 0.15 m² to 0.030 m², so the "
               "pressure rises fivefold.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-h03",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A U-shaped tube contains water. Oil, which is less dense than "
                "water and does not mix with it, is poured into one arm. "
                "Predict what is seen once the liquids settle.",
        "options": [
            "The oil sinks below the water in that arm, because it was "
            "poured in from above the surface",
            "Both arms settle at exactly the same height, because the "
            "pressure in a fluid is the same everywhere at every level",
            "The water rises in the oil arm until the two liquid surfaces are "
            "level with each other",
            "The oil column stands taller, because a less dense liquid needs "
            "more depth for equal pressure",
        ],
        "correct_index": 3,
        "why": "At the level where the liquids meet the pressures must match, "
               "and since P = hρg a smaller density needs a greater height.",
    },
    {
        "id": "ks4-pressure-in-a-fluid-h04",
        "subtopic_slug": "pressure-in-a-fluid",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A submarine hull can withstand a maximum additional pressure "
                "of 4.0 × 10⁶ Pa from the water around it. Determine the "
                "greatest depth at which it can operate in seawater. (density "
                "of seawater = 1025 kg/m³, g = 9.8 N/kg)",
        "options": [
            "3900 m",
            "398 m",
            "408 000 m",
            "41 m",
        ],
        "correct_index": 1,
        "why": "Rearranging P = hρg gives h = P ÷ (ρg) = 4.0 × 10⁶ ÷ (1025 × "
               "9.8) = 398 m.",
    },

    # ── upthrust-floating ───────────────────────────────────────────────
    {
        "id": "ks4-upthrust-floating-e01",
        "subtopic_slug": "upthrust-floating",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State Archimedes' principle.",
        "options": [
            "The upthrust on an object is equal to the weight of the object "
            "itself",
            "The upthrust on an object is equal to the volume of fluid that it "
            "displaces",
            "The upthrust on an object is equal to the weight of the fluid "
            "that it displaces",
            "The upthrust on an object is equal to the difference between its "
            "mass and the fluid's mass",
        ],
        "correct_index": 2,
        "why": "The upthrust is set by the fluid pushed aside, not by the "
               "object — it equals the weight of the displaced fluid.",
    },
    {
        "id": "ks4-upthrust-floating-e02",
        "subtopic_slug": "upthrust-floating",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain what causes the upthrust on a fully submerged object.",
        "options": [
            "The object's own weight pushing the fluid out of the way beneath "
            "it",
            "Friction between the object's surface and the fluid flowing past "
            "it",
            "The fluid particles above the object moving out of its path as it "
            "sinks",
            "The fluid pressure on its bottom being greater than that on "
            "its top",
        ],
        "correct_index": 3,
        "why": "Pressure increases with depth, so the upward push on the lower "
               "surface exceeds the downward push on the upper surface, and "
               "the difference is the upthrust.",
    },
    {
        "id": "ks4-upthrust-floating-e03",
        "subtopic_slug": "upthrust-floating",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A solid lump sinks when it is dropped into water but floats "
                "when it is dropped into mercury. State what this shows about "
                "the density of the lump.",
        "options": [
            "It is greater than the density of water but less than that of "
            "mercury",
            "It is less than the density of water but greater than that of "
            "mercury",
            "It is greater than the density of both water and mercury",
            "It is less than the density of both water and mercury",
        ],
        "correct_index": 0,
        "why": "An object sinks in a fluid less dense than itself and floats "
               "in one more dense, so the lump sits between the two.",
    },
    {
        "id": "ks4-upthrust-floating-e04",
        "subtopic_slug": "upthrust-floating",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Calculate the upthrust on an object that displaces 0.030 m³ "
                "of seawater. (density of seawater = 1030 kg/m³, g = 10 N/kg)",
        "options": [
            "30.9 N",
            "309 N",
            "1040 N",
            "3.09 N",
        ],
        "correct_index": 1,
        "why": "Upthrust = ρVg = 1030 kg/m³ × 0.030 m³ × 10 N/kg = 309 N.",
    },
    {
        "id": "ks4-upthrust-floating-s01",
        "subtopic_slug": "upthrust-floating",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A block of volume 0.020 m³ is held fully submerged in oil of "
                "density 900 kg/m³. Calculate the upthrust on the block. "
                "(g = 10 N/kg)",
        "options": [
            "18 N",
            "180 N",
            "910 N",
            "0.18 N",
        ],
        "correct_index": 1,
        "why": "Upthrust = ρVg = 900 × 0.020 × 10 = 180 N, using the density "
               "of the fluid rather than that of the block.",
    },
    {
        "id": "ks4-upthrust-floating-s02",
        "subtopic_slug": "upthrust-floating",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A steel block of weight 80 N hangs from a newtonmeter and is "
                "lowered until fully underwater, where it displaces water "
                "weighing 12 N. Determine the newtonmeter reading.",
        "options": [
            "68 N",
            "92 N",
            "80 N",
            "12 N",
        ],
        "correct_index": 0,
        "why": "The upthrust equals the 12 N weight of displaced water and "
               "acts upwards, so the apparent weight is 80 − 12 = 68 N.",
    },
    {
        "id": "ks4-upthrust-floating-s03",
        "subtopic_slug": "upthrust-floating",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A wooden cube of side 0.20 m and density 750 kg/m³ floats in "
                "water. Calculate the volume of water it displaces. (density "
                "of water = 1000 kg/m³, g = 10 N/kg)",
        "options": [
            "0.0080 m³",
            "0.0020 m³",
            "0.0060 m³",
            "0.0107 m³",
        ],
        "correct_index": 2,
        "why": "A floating object displaces its own weight of fluid: the cube "
               "weighs 750 × 0.0080 × 10 = 60 N, so V = 60 ÷ (1000 × 10) = "
               "0.0060 m³.",
    },
    {
        "id": "ks4-upthrust-floating-s04",
        "subtopic_slug": "upthrust-floating",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A student says the upthrust on a submerged brick depends on "
                "the brick's mass. Explain why the student is wrong.",
        "options": [
            "It is wrong — upthrust depends on the brick's weight in air "
            "rather than on its mass",
            "It is wrong — upthrust depends only on how far below the surface "
            "the brick is held",
            "It is wrong — upthrust depends on the brick's total surface area "
            "rather than on its mass",
            "It is wrong — upthrust depends on the weight of the fluid the "
            "brick displaces, not on the brick",
        ],
        "correct_index": 3,
        "why": "Upthrust = ρ_fluid × V × g, so two bricks of the same size but "
               "different masses feel exactly the same upthrust.",
    },
    {
        "id": "ks4-upthrust-floating-h01",
        "subtopic_slug": "upthrust-floating",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A diver weighs 700 N in air. When fully submerged in water, a "
                "balance reads their apparent weight as 60 N. Determine the "
                "volume of water displaced. (density of water = 1000 kg/m³, "
                "g = 10 N/kg)",
        "options": [
            "0.070 m³",
            "0.0060 m³",
            "0.076 m³",
            "0.064 m³",
        ],
        "correct_index": 3,
        "why": "The upthrust is the loss in apparent weight, 700 − 60 = 640 N, "
               "so V = U ÷ (ρg) = 640 ÷ 10 000 = 0.064 m³.",
    },
    {
        "id": "ks4-upthrust-floating-h02",
        "subtopic_slug": "upthrust-floating",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A submarine floating at neutral buoyancy lets seawater into "
                "its ballast tanks. Explain the effect on the submarine.",
        "options": [
            "Its volume increases, so the upthrust increases and the submarine "
            "rises",
            "Its upthrust decreases because the water inside presses "
            "downwards, so it sinks",
            "Its weight increases while its volume and upthrust are unchanged, "
            "so it sinks",
            "Its density falls because water has been added, so it rises to "
            "the surface",
        ],
        "correct_index": 2,
        "why": "Flooding the tanks adds mass without changing the hull's "
               "external volume, so the weight now exceeds the unchanged "
               "upthrust.",
    },
    {
        "id": "ks4-upthrust-floating-h03",
        "subtopic_slug": "upthrust-floating",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "An aluminium block and a lead block have the same volume. "
                "Both are held fully submerged in water on strings. Compare "
                "the upthrust acting on each block.",
        "options": [
            "The upthrust on the lead is larger, because lead is denser and so "
            "displaces more water",
            "The upthrust is the same on both, because they displace the same "
            "volume of water",
            "The upthrust on the aluminium is larger, because it is the block "
            "closer to floating",
            "The upthrust on the lead is larger, because a heavier object "
            "pushes harder into the fluid",
        ],
        "correct_index": 1,
        "why": "Upthrust = ρ_fluid × V × g, and the submerged volumes are "
               "equal, so the upthrusts are identical — only the weights "
               "differ.",
    },
    {
        "id": "ks4-upthrust-floating-h04",
        "subtopic_slug": "upthrust-floating",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A block floats in water with four fifths of its volume below "
                "the surface. Determine the density of the block. (density of "
                "water = 1000 kg/m³)",
        "options": [
            "800 kg/m³",
            "1250 kg/m³",
            "200 kg/m³",
            "1000 kg/m³",
        ],
        "correct_index": 0,
        "why": "For a floating object the submerged fraction equals the ratio "
               "of the densities, so ρ = 0.80 × 1000 = 800 kg/m³.",
    },

    # ── distance-speed-velocity ─────────────────────────────────────────
    {
        "id": "ks4-distance-speed-velocity-e01",
        "subtopic_slug": "distance-speed-velocity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the displacement of an object.",
        "options": [
            "The total length of the path travelled from the start of the "
            "journey to the finish",
            "The straight-line distance from start to finish, together with "
            "its direction",
            "The rate at which an object changes its position as time passes",
            "The distance an object travels during each second of its journey",
        ],
        "correct_index": 1,
        "why": "Displacement is a vector — how far, and in what direction, the "
               "finish is from the start, whatever route was taken.",
    },
    {
        "id": "ks4-distance-speed-velocity-e02",
        "subtopic_slug": "distance-speed-velocity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A runner covers 240 m in 40 s. Calculate the average speed.",
        "options": [
            "6.0 m/s",
            "0.17 m/s",
            "9600 m/s",
            "60 m/s",
        ],
        "correct_index": 0,
        "why": "v = d ÷ t = 240 m ÷ 40 s = 6.0 m/s.",
    },
    {
        "id": "ks4-distance-speed-velocity-e03",
        "subtopic_slug": "distance-speed-velocity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the typical speed at which an adult walks.",
        "options": [
            "0.15 m/s",
            "15 m/s",
            "6.0 m/s",
            "1.5 m/s",
        ],
        "correct_index": 3,
        "why": "A person walks at roughly 1.5 m/s — about one and a half "
               "metres in every second.",
    },
    {
        "id": "ks4-distance-speed-velocity-e04",
        "subtopic_slug": "distance-speed-velocity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car travels at a steady 25 m/s for 8.0 s. Calculate the "
                "distance travelled.",
        "options": [
            "3.1 m",
            "33 m",
            "200 m",
            "0.32 m",
        ],
        "correct_index": 2,
        "why": "Rearranging v = d ÷ t gives d = v × t = 25 m/s × 8.0 s = "
               "200 m.",
    },
    {
        "id": "ks4-distance-speed-velocity-s01",
        "subtopic_slug": "distance-speed-velocity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dog runs 45 m east along a straight path, then turns and "
                "runs 20 m back west. Calculate the total distance travelled "
                "and the magnitude of the displacement.",
        "options": [
            "Distance = 25 m, displacement = 65 m",
            "Distance = 65 m, displacement = 65 m",
            "Distance = 65 m, displacement = 25 m",
            "Distance = 45 m, displacement = 20 m",
        ],
        "correct_index": 2,
        "why": "Distance adds both legs of the run, 45 + 20 = 65 m, while "
               "displacement is how far the dog ends up from the start, "
               "45 − 20 = 25 m.",
    },
    {
        "id": "ks4-distance-speed-velocity-s02",
        "subtopic_slug": "distance-speed-velocity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A train travels 4.5 km in 3.0 minutes. Calculate its average "
                "speed in m/s.",
        "options": [
            "1.5 m/s",
            "1500 m/s",
            "0.025 m/s",
            "25 m/s",
        ],
        "correct_index": 3,
        "why": "4.5 km is 4500 m and 3.0 minutes is 180 s, so v = 4500 ÷ 180 = "
               "25 m/s.",
    },
    {
        "id": "ks4-distance-speed-velocity-s03",
        "subtopic_slug": "distance-speed-velocity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car travels at a steady 30 m/s. Convert this speed into "
                "kilometres per hour.",
        "options": [
            "8.3 km/h",
            "108 km/h",
            "30 km/h",
            "1800 km/h",
        ],
        "correct_index": 1,
        "why": "One metre per second is 3.6 km/h, so 30 × 3.6 = 108 km/h.",
    },
    {
        "id": "ks4-distance-speed-velocity-s04",
        "subtopic_slug": "distance-speed-velocity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hiker walks for 20 minutes at a steady 1.2 m/s, then rests "
                "for 10 minutes. Calculate the average speed over the whole "
                "30 minutes.",
        "options": [
            "0.80 m/s",
            "1.2 m/s",
            "0.60 m/s",
            "48 m/s",
        ],
        "correct_index": 0,
        "why": "The hiker covers 1.2 × 1200 = 1440 m, and average speed uses "
               "the whole 1800 s: 1440 ÷ 1800 = 0.80 m/s.",
    },
    {
        "id": "ks4-distance-speed-velocity-h01",
        "subtopic_slug": "distance-speed-velocity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sprinter covers the first 40 m of a 100 m race in 4.0 s and "
                "the remaining 60 m in 8.0 s. Determine the average speed over "
                "the whole race.",
        "options": [
            "8.3 m/s",
            "8.8 m/s",
            "10.0 m/s",
            "7.5 m/s",
        ],
        "correct_index": 0,
        "why": "Average speed is total distance ÷ total time, 100 m ÷ 12 s = "
               "8.3 m/s — two speeds lasting different times cannot simply be "
               "averaged.",
    },
    {
        "id": "ks4-distance-speed-velocity-h02",
        "subtopic_slug": "distance-speed-velocity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A train travelling north at 30 m/s slows to a stop and later "
                "travels south at 30 m/s. A student says the train's velocity "
                "has not changed, because its speed is still 30 m/s. Evaluate "
                "this statement.",
        "options": [
            "The student is right — speed and velocity are the same whenever "
            "the size of the motion is unchanged",
            "The student is wrong — velocity includes direction, so it has "
            "changed from 30 m/s north to 30 m/s south",
            "The student is wrong — the velocity has doubled to 60 m/s, "
            "because the train has reversed its motion",
            "The student is right — only a change in speed can change a "
            "velocity, and the speed is unchanged",
        ],
        "correct_index": 1,
        "why": "Velocity is a vector, so reversing direction changes it even "
               "though the speed stays at 30 m/s.",
    },
    {
        "id": "ks4-distance-speed-velocity-h03",
        "subtopic_slug": "distance-speed-velocity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A delivery van drives 12 km at an average speed of 15 m/s, "
                "then a further 8.0 km at an average speed of 20 m/s. "
                "Determine the total time for the journey.",
        "options": [
            "1140 s",
            "400 s",
            "1200 s",
            "800 s",
        ],
        "correct_index": 2,
        "why": "Each leg's time is distance ÷ speed: 12 000 ÷ 15 = 800 s and "
               "8000 ÷ 20 = 400 s, giving 1200 s altogether.",
    },
    {
        "id": "ks4-distance-speed-velocity-h04",
        "subtopic_slug": "distance-speed-velocity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cross-country runner completes a 5.0 km course in 25 "
                "minutes and finishes 1.2 km due east of the start. Determine "
                "the average speed and the magnitude of the average velocity.",
        "options": [
            "Speed = 0.80 m/s, velocity = 3.3 m/s",
            "Speed = 3.3 m/s, velocity = 3.3 m/s",
            "Speed = 3.3 m/s, velocity = 0 m/s",
            "Speed = 3.3 m/s, velocity = 0.80 m/s",
        ],
        "correct_index": 3,
        "why": "Average speed uses the 5000 m of path travelled (5000 ÷ 1500 = "
               "3.3 m/s) while average velocity uses the 1200 m displacement "
               "(1200 ÷ 1500 = 0.80 m/s).",
    },
]
