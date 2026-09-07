"""Physics · Forces — motion graphs, acceleration, Newton's laws, stopping
distance, circular motion and momentum (part C of three).

Six subtopics of `forces`: distance-time-graphs, acceleration, newtons-laws,
stopping-distance-braking, motion-in-a-circle, momentum.

The distractors are built from the misconceptions the brief declares and the
lesson prose implies. The recurring ones are: reading a distance-time graph as
though it were a velocity-time graph (gradient taken for acceleration, area
treated as meaningful); the mirror error on a velocity-time graph (gradient
taken for distance); thinking distance and braking distance swapped, with the
v-vs-v-squared dependence attached to the wrong one; Newton's third-law pairs
given as two forces on the SAME object; circular motion read as equilibrium,
or as needing an outward force; and momentum arithmetic done on magnitudes
with the direction signs dropped.

⚠️ `distance-time-graphs` is byte-identical to a KS3 lesson slug, which is
part of why this pool has its own table. These twelve are pitched at KS4:
gradient computed as a speed with unit conversion, average speed across a
whole journey including a stationary section, distance vs displacement, and
the area-under-the-graph error — never "which line is steeper".

Two deliberate exclusions, both to keep BASE questions free of higher-tier
content (authoring standard §8). `distance-time-graphs` carries no tangent
construction and `acceleration` carries no v² = u² + 2as and no trapezium
area: the brief files all three under HIGHER-TIER extension prose, and this
subtopic's derived flag is `tier='foundation'`, so a Foundation Combined class
sits these.

No question here needs a figure. Every graph is described in words.
"""

TOPIC = "forces"
SUBJECT = "physics"

QUESTIONS = [
    # ── distance-time-graphs ─────────────────────────────── BASE ───────
    {
        "id": "ks4-distance-time-graphs-e01",
        "subtopic_slug": "distance-time-graphs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A distance–time graph for a cyclist is a straight line from "
                "the origin passing through the point (8.0 s, 40 m). "
                "Calculate the speed of the cyclist.",
        "options": [
            "0.20 m/s",
            "320 m/s",
            "5.0 m/s",
            "48 m/s",
        ],
        "correct_index": 2,
        "why": "The gradient of a distance–time graph is the speed, so speed "
               "= 40 m ÷ 8.0 s = 5.0 m/s.",
    },
    {
        "id": "ks4-distance-time-graphs-e02",
        "subtopic_slug": "distance-time-graphs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which quantity is given by the gradient of a "
                "distance–time graph.",
        "options": [
            "The speed of the object",
            "The acceleration of the object",
            "The distance travelled by the object",
            "The time taken by the object",
        ],
        "correct_index": 0,
        "why": "Gradient is change in distance ÷ change in time, which is the "
               "definition of speed.",
    },
    {
        "id": "ks4-distance-time-graphs-e03",
        "subtopic_slug": "distance-time-graphs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The distance–time graph of a runner is a straight line "
                "sloping downwards from 200 m at 40 s to 0 m at 90 s. "
                "Describe her motion during this part of the journey.",
        "options": [
            "Speeding up as she moves further from her starting point",
            "Slowing down steadily until she stops at 90 s",
            "Stationary for the whole of the 50 s",
            "Returning towards her starting point at a steady 4.0 m/s",
        ],
        "correct_index": 3,
        "why": "A straight negative gradient means the distance from the "
               "start is falling steadily: 200 m ÷ 50 s = 4.0 m/s back "
               "towards the start.",
    },
    {
        "id": "ks4-distance-time-graphs-e04",
        "subtopic_slug": "distance-time-graphs",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bus's distance–time graph is a straight line from "
                "(5.0 s, 20 m) to (15 s, 90 m). Calculate the speed of the "
                "bus over this section.",
        "options": [
            "4.0 m/s",
            "7.0 m/s",
            "6.0 m/s",
            "5.5 m/s",
        ],
        "correct_index": 1,
        "why": "Speed is the gradient, and a gradient uses the CHANGES: "
               "(90 − 20) m ÷ (15 − 5.0) s = 70 ÷ 10 = 7.0 m/s.",
    },
    {
        "id": "ks4-distance-time-graphs-s01",
        "subtopic_slug": "distance-time-graphs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A delivery van's distance–time graph is a straight line "
                "from (0 s, 0 m) to (20 s, 300 m), then horizontal from "
                "(20 s, 300 m) to (50 s, 300 m). Calculate the average "
                "speed of the van over the whole 50 s.",
        "options": [
            "6.0 m/s",
            "15 m/s",
            "10 m/s",
            "7.5 m/s",
        ],
        "correct_index": 0,
        "why": "Average speed uses the whole journey: 300 m ÷ 50 s = 6.0 m/s, "
               "and the 30 s spent stationary still counts as part of the "
               "time.",
    },
    {
        "id": "ks4-distance-time-graphs-s02",
        "subtopic_slug": "distance-time-graphs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lorry's distance–time graph is a straight line passing "
                "through (2.0 min, 1.2 km) and (6.0 min, 4.8 km). Calculate "
                "the speed of the lorry in m/s.",
        "options": [
            "0.90 m/s",
            "900 m/s",
            "20 m/s",
            "15 m/s",
        ],
        "correct_index": 3,
        "why": "Speed is the gradient, in consistent units: Δd = 3600 m and "
               "Δt = 240 s, so speed = 3600 ÷ 240 = 15 m/s.",
    },
    {
        "id": "ks4-distance-time-graphs-s03",
        "subtopic_slug": "distance-time-graphs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two cyclists set off together from the same point. On a "
                "distance–time graph both lines are straight and start at "
                "the origin: cyclist P reaches 90 m at 6.0 s and cyclist Q "
                "reaches 90 m at 15 s. Compare their speeds.",
        "options": [
            "Q is faster, because its line covers a longer time interval",
            "P is faster: 15 m/s compared with 6.0 m/s for Q",
            "They have the same speed, because both lines are straight",
            "Q is faster: 0.17 m/s compared with 0.067 m/s for P",
        ],
        "correct_index": 1,
        "why": "Gradient is speed: P covers 90 m in 6.0 s (15 m/s) while Q "
               "takes 15 s (6.0 m/s), so the steeper line, P, is faster.",
    },
    {
        "id": "ks4-distance-time-graphs-s04",
        "subtopic_slug": "distance-time-graphs",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'The area under a distance–time graph "
                "gives the distance travelled.' Explain what is wrong with "
                "this statement.",
        "options": [
            "Nothing is wrong — the area gives the distance on any motion graph",
            "The area gives the acceleration of the object instead",
            "Distance is read off the vertical axis; the area means "
            "nothing here",
            "The area gives the average speed of the object instead",
        ],
        "correct_index": 2,
        "why": "Distance is already the vertical axis of a distance–time "
               "graph, so it is read off directly; it is the area under a "
               "velocity–time graph that gives distance.",
    },
    {
        "id": "ks4-distance-time-graphs-h01",
        "subtopic_slug": "distance-time-graphs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car's distance–time graph is a straight line from the "
                "origin to (12 s, 180 m), then a straight line of smaller "
                "gradient from (12 s, 180 m) to (30 s, 234 m). Determine "
                "the average speed for the whole journey and how the speed "
                "changes.",
        "options": [
            "9.0 m/s average; the car speeds up after 12 s",
            "7.8 m/s average; the car speeds up after 12 s",
            "18 m/s average; the car slows down after 12 s",
            "7.8 m/s average; the car slows down after 12 s",
        ],
        "correct_index": 3,
        "why": "Average speed is total distance ÷ total time = 234 m ÷ 30 s "
               "= 7.8 m/s, and the second gradient (3.0 m/s) is smaller than "
               "the first (15 m/s), so the car slows.",
    },
    {
        "id": "ks4-distance-time-graphs-h02",
        "subtopic_slug": "distance-time-graphs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A runner's distance–time graph rises steeply from the "
                "origin and then curves, becoming gradually less steep, "
                "until it is horizontal at 400 m after 80 s. Determine her "
                "average speed and compare it with her speed at 70 s.",
        "options": [
            "5.0 m/s; at 70 s the gradient is steeper, so she is faster there",
            "5.0 m/s; at 70 s the gradient is shallower, so she is slower "
            "there",
            "0.20 m/s; the flattening curve shows her speed falling to zero",
            "5.0 m/s; her speed is identical at every point of the run",
        ],
        "correct_index": 1,
        "why": "Average speed is 400 m ÷ 80 s = 5.0 m/s, and by 70 s the "
               "curve has flattened, so the gradient there — her speed — is "
               "below that average.",
    },
    {
        "id": "ks4-distance-time-graphs-h03",
        "subtopic_slug": "distance-time-graphs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A commuter walks 600 m to a station in 500 s, waits 200 s, "
                "then walks the same 600 m home in 400 s. Determine her "
                "average speed for the whole trip and her displacement at "
                "the end of it.",
        "options": [
            "1.09 m/s and a displacement of 1200 m",
            "1.20 m/s and a displacement of 0 m",
            "1.09 m/s and a displacement of 0 m",
            "0.55 m/s and a displacement of 600 m",
        ],
        "correct_index": 2,
        "why": "Average speed uses the whole 1200 m and the whole 1100 s "
               "including the wait, giving 1.09 m/s, and finishing where she "
               "started makes the displacement zero.",
    },
    {
        "id": "ks4-distance-time-graphs-h04",
        "subtopic_slug": "distance-time-graphs",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A distance–time graph is plotted with distance in "
                "kilometres and time in hours. The line is straight and "
                "passes through (0.50 h, 30 km) and (2.5 h, 150 km). "
                "Determine the speed in m/s.",
        "options": [
            "16.7 m/s",
            "60.0 m/s",
            "1.00 m/s",
            "216 m/s",
        ],
        "correct_index": 0,
        "why": "The gradient is 120 km ÷ 2.0 h = 60 km/h, and 60 × 1000 ÷ "
               "3600 = 16.7 m/s.",
    },

    # ── acceleration ─────────────────────────────────────── BASE ───────
    {
        "id": "ks4-acceleration-e01",
        "subtopic_slug": "acceleration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of these correctly defines acceleration.",
        "options": [
            "The distance travelled each second, measured in m/s",
            "The change in velocity each second, measured in m/s²",
            "The total change in velocity, measured in m/s",
            "The force needed to change velocity, measured in N",
        ],
        "correct_index": 1,
        "why": "Acceleration is the rate of change of velocity — how much "
               "the velocity changes each second — so its unit is m/s².",
    },
    {
        "id": "ks4-acceleration-e02",
        "subtopic_slug": "acceleration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A motorcycle speeds up from rest to 18 m/s in 6.0 s. "
                "Calculate its acceleration.",
        "options": [
            "108 m/s²",
            "0.33 m/s²",
            "12 m/s²",
            "3.0 m/s²",
        ],
        "correct_index": 3,
        "why": "a = (v − u) ÷ t = (18 − 0) ÷ 6.0 = 3.0 m/s².",
    },
    {
        "id": "ks4-acceleration-e03",
        "subtopic_slug": "acceleration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a horizontal (flat) line on a velocity–time "
                "graph shows.",
        "options": [
            "The object is moving at constant velocity",
            "The object is stationary",
            "The object is accelerating at a steady rate",
            "The object is decelerating steadily",
        ],
        "correct_index": 0,
        "why": "On a velocity–time graph the height is the velocity, so a "
               "flat line means the velocity is not changing — zero "
               "acceleration, not zero speed.",
    },
    {
        "id": "ks4-acceleration-e04",
        "subtopic_slug": "acceleration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A van's velocity rises from 14 m/s to 32 m/s in 4.0 s. "
                "Calculate its acceleration.",
        "options": [
            "8.0 m/s²",
            "3.5 m/s²",
            "4.5 m/s²",
            "72 m/s²",
        ],
        "correct_index": 2,
        "why": "a = (v − u) ÷ t = (32 − 14) ÷ 4.0 = 4.5 m/s² — it is the "
               "CHANGE in velocity that is divided by the time.",
    },
    {
        "id": "ks4-acceleration-s01",
        "subtopic_slug": "acceleration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist accelerates uniformly at 1.5 m/s² for 8.0 s from "
                "an initial velocity of 4.0 m/s. Calculate her final "
                "velocity.",
        "options": [
            "12 m/s",
            "48 m/s",
            "16 m/s",
            "5.5 m/s",
        ],
        "correct_index": 2,
        "why": "Rearranging a = (v − u) ÷ t gives v = u + at = 4.0 + 1.5 × "
               "8.0 = 16 m/s.",
    },
    {
        "id": "ks4-acceleration-s02",
        "subtopic_slug": "acceleration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car's velocity–time graph is a straight line from the "
                "origin up to (10 s, 24 m/s), then horizontal until 30 s. "
                "Calculate the distance travelled during the first 10 s.",
        "options": [
            "120 m",
            "240 m",
            "2.4 m",
            "34 m",
        ],
        "correct_index": 0,
        "why": "Distance is the area under the graph, and the sloping "
               "section is a triangle: ½ × 10 s × 24 m/s = 120 m.",
    },
    {
        "id": "ks4-acceleration-s03",
        "subtopic_slug": "acceleration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lift starts from rest, accelerates uniformly to 2.4 m/s "
                "in 4.0 s, travels at 2.4 m/s for 6.0 s, then slows "
                "uniformly to rest in 3.0 s. Calculate the magnitude of its "
                "deceleration in the final stage.",
        "options": [
            "0.60 m/s²",
            "7.2 m/s²",
            "0.18 m/s²",
            "0.80 m/s²",
        ],
        "correct_index": 3,
        "why": "Only the final stage matters: the velocity falls by 2.4 m/s "
               "in 3.0 s, so a = 2.4 ÷ 3.0 = 0.80 m/s².",
    },
    {
        "id": "ks4-acceleration-s04",
        "subtopic_slug": "acceleration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ball is dropped from rest and falls freely. Taking the "
                "acceleration due to gravity as 9.8 m/s², calculate its "
                "velocity after 2.5 s.",
        "options": [
            "3.9 m/s",
            "24.5 m/s",
            "12.3 m/s",
            "9.8 m/s",
        ],
        "correct_index": 1,
        "why": "In free fall the acceleration is 9.8 m/s², so v = u + at = "
               "0 + 9.8 × 2.5 = 24.5 m/s.",
    },
    {
        "id": "ks4-acceleration-h01",
        "subtopic_slug": "acceleration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A train travelling at 45 m/s brakes uniformly and comes to "
                "rest in 30 s. Determine the magnitude of its deceleration "
                "and the distance it travels while braking.",
        "options": [
            "1.5 m/s² and 675 m",
            "1.5 m/s² and 1350 m",
            "0.67 m/s² and 675 m",
            "0.67 m/s² and 1350 m",
        ],
        "correct_index": 0,
        "why": "a = (0 − 45) ÷ 30 = −1.5 m/s², and the distance is the "
               "triangular area under the velocity–time graph, ½ × 30 s × "
               "45 m/s = 675 m.",
    },
    {
        "id": "ks4-acceleration-h02",
        "subtopic_slug": "acceleration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two cars accelerate uniformly from rest. Car A reaches "
                "20 m/s in 5.0 s and car B reaches 30 m/s in 10 s. Compare "
                "their accelerations.",
        "options": [
            "Car B, because it reaches the greater final velocity",
            "They are equal, because both cars start from rest",
            "Car A: 4.0 m/s² compared with 3.0 m/s² for car B",
            "Car B: 3.0 m/s² compared with 2.0 m/s² for car A",
        ],
        "correct_index": 2,
        "why": "a = (v − u) ÷ t, so car A gives 20 ÷ 5.0 = 4.0 m/s² and car "
               "B gives 30 ÷ 10 = 3.0 m/s² — a bigger final velocity does "
               "not mean a bigger acceleration.",
    },
    {
        "id": "ks4-acceleration-h03",
        "subtopic_slug": "acceleration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A skydiver's velocity–time graph rises steeply from the "
                "origin, then curves so that its gradient falls to zero at "
                "a velocity of 55 m/s after 14 s. Determine what is "
                "happening to her acceleration and her velocity at 14 s.",
        "options": [
            "Her acceleration is constant and her velocity is still rising",
            "Her acceleration is zero and her velocity is a steady 55 m/s",
            "Her acceleration is increasing and her velocity is 55 m/s",
            "Her acceleration is negative, so she is slowing down at 14 s",
        ],
        "correct_index": 1,
        "why": "The gradient of a velocity–time graph is the acceleration, "
               "so a gradient that has fallen to zero means no acceleration "
               "— she continues at a steady 55 m/s.",
    },
    {
        "id": "ks4-acceleration-h04",
        "subtopic_slug": "acceleration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist accelerates uniformly from rest at 1.2 m/s² for "
                "10 s, then travels at a constant velocity for a further "
                "25 s. Determine the total distance travelled.",
        "options": [
            "300 m",
            "420 m",
            "210 m",
            "360 m",
        ],
        "correct_index": 3,
        "why": "The velocity after 10 s is 1.2 × 10 = 12 m/s, so the "
               "distance is the triangle ½ × 10 × 12 = 60 m plus the "
               "rectangle 12 × 25 = 300 m, giving 360 m.",
    },

    # ── newtons-laws ─────────────────────────────────────── BASE ───────
    {
        "id": "ks4-newtons-laws-e01",
        "subtopic_slug": "newtons-laws",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State Newton's First Law of motion.",
        "options": [
            "An object accelerates in proportion to the resultant force on it",
            "Every force is matched by an equal and opposite force on the "
            "same object",
            "A moving object slows down by itself unless a force keeps "
            "pushing it",
            "An object keeps its velocity unless a resultant force acts on it",
        ],
        "correct_index": 3,
        "why": "With no resultant force there is no change in motion, so the "
               "object stays at rest or carries on at the same constant "
               "velocity.",
    },
    {
        "id": "ks4-newtons-laws-e02",
        "subtopic_slug": "newtons-laws",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 60 kg go-kart experiences a resultant force of 150 N. "
                "Calculate its acceleration.",
        "options": [
            "9000 m/s²",
            "2.5 m/s²",
            "0.40 m/s²",
            "90 m/s²",
        ],
        "correct_index": 1,
        "why": "F = ma rearranges to a = F ÷ m = 150 ÷ 60 = 2.5 m/s².",
    },
    {
        "id": "ks4-newtons-laws-e03",
        "subtopic_slug": "newtons-laws",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A puck slides across a smooth, level ice rink at a steady "
                "6.0 m/s. State the resultant force acting on the puck.",
        "options": [
            "6.0 N, acting in the direction of motion",
            "Equal to the puck's weight, acting vertically downwards",
            "Zero — no resultant force is needed to keep it moving",
            "A small forward force, which is what keeps the puck going",
        ],
        "correct_index": 2,
        "why": "Newton's First Law: a steady velocity needs no resultant "
               "force at all — a force is needed to CHANGE motion, not to "
               "continue it.",
    },
    {
        "id": "ks4-newtons-laws-e04",
        "subtopic_slug": "newtons-laws",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these is a Newton's Third Law pair of "
                "forces.",
        "options": [
            "A boot pushes a football forwards; the football pushes the "
            "boot backwards",
            "The weight of a book on a table; the table pushing up on the "
            "book",
            "The driving force of a car; the air resistance acting on the car",
            "The weight of a falling ball; the air resistance on that ball",
        ],
        "correct_index": 0,
        "why": "Third Law pairs are the same type of force, equal and "
               "opposite, and act on two different objects — here, the boot "
               "and the ball.",
    },
    {
        "id": "ks4-newtons-laws-s01",
        "subtopic_slug": "newtons-laws",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1200 kg van is acted on by a driving force of 4000 N and "
                "by total resistive forces of 1600 N. Calculate its "
                "acceleration.",
        "options": [
            "3.33 m/s²",
            "2.00 m/s²",
            "1.33 m/s²",
            "4.67 m/s²",
        ],
        "correct_index": 1,
        "why": "Only the resultant force accelerates the van: 4000 − 1600 = "
               "2400 N, so a = 2400 ÷ 1200 = 2.00 m/s².",
    },
    {
        "id": "ks4-newtons-laws-s02",
        "subtopic_slug": "newtons-laws",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a passenger standing on a bus lurches forwards "
                "when the bus brakes sharply.",
        "options": [
            "A forward force acts on her as soon as the brakes are applied",
            "Her weight increases while the bus is slowing down",
            "She keeps her velocity, as no resultant force acts on her",
            "She is pushed forward by the reaction to the braking force",
        ],
        "correct_index": 2,
        "why": "Newton's First Law: with no resultant force on her, the "
               "passenger carries on at the bus's original velocity while "
               "the bus slows beneath her.",
    },
    {
        "id": "ks4-newtons-laws-s03",
        "subtopic_slug": "newtons-laws",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rocket engine pushes exhaust gas downwards with a force "
                "of 8.0 × 10⁵ N. State the size and direction of the force "
                "the gas exerts on the rocket.",
        "options": [
            "8.0 × 10⁵ N upwards",
            "8.0 × 10⁵ N downwards",
            "Less than 8.0 × 10⁵ N upwards, as the gas has a smaller mass",
            "Zero, because the two forces cancel each other out",
        ],
        "correct_index": 0,
        "why": "Newton's Third Law: the pair is equal in size and opposite "
               "in direction, and because the two forces act on different "
               "objects they cannot cancel.",
    },
    {
        "id": "ks4-newtons-laws-s04",
        "subtopic_slug": "newtons-laws",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 150 g ball is struck by a bat and accelerates at "
                "320 m/s². Calculate the resultant force on the ball.",
        "options": [
            "48 000 N",
            "2130 N",
            "0.47 N",
            "48 N",
        ],
        "correct_index": 3,
        "why": "F = ma, and the mass must be in kilograms: 0.150 kg × "
               "320 m/s² = 48 N.",
    },
    {
        "id": "ks4-newtons-laws-h01",
        "subtopic_slug": "newtons-laws",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'When a horse pulls a cart, the cart pulls "
                "back on the horse with an equal force, so the cart can "
                "never move.' Explain the error in this reasoning.",
        "options": [
            "The horse's pull is larger, which is why the cart accelerates",
            "Newton's Third Law does not apply when one object is much "
            "heavier",
            "The two forces act on different objects, so they cannot cancel",
            "The forces do cancel, and only friction pushes the cart forwards",
        ],
        "correct_index": 2,
        "why": "A Third Law pair acts on two different objects, so it never "
               "cancels — what accelerates the cart is the resultant of the "
               "forces acting on the cart alone.",
    },
    {
        "id": "ks4-newtons-laws-h02",
        "subtopic_slug": "newtons-laws",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A parachutist of mass 75 kg has a weight of 735 N and, at "
                "one moment during her fall, experiences 435 N of air "
                "resistance. Determine her acceleration at that moment.",
        "options": [
            "4.0 m/s² downwards",
            "9.8 m/s² downwards",
            "15.6 m/s² downwards",
            "5.8 m/s² upwards",
        ],
        "correct_index": 0,
        "why": "The resultant force is 735 − 435 = 300 N downwards, so a = "
               "300 ÷ 75 = 4.0 m/s² downwards.",
    },
    {
        "id": "ks4-newtons-laws-h03",
        "subtopic_slug": "newtons-laws",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two trolleys are pushed along a bench. Trolley P has a mass "
                "of 2.0 kg and a resultant force of 6.0 N on it; trolley Q "
                "has a mass of 3.5 kg and a resultant force of 9.0 N on it. "
                "Compare their accelerations.",
        "options": [
            "Q accelerates faster, because a larger force always gives a "
            "larger acceleration",
            "They accelerate equally, because force and mass both increase",
            "Q accelerates faster: 4.5 m/s² compared with 3.0 m/s² for P",
            "P accelerates faster: 3.0 m/s² compared with 2.6 m/s² for Q",
        ],
        "correct_index": 3,
        "why": "a = F ÷ m, so P gives 6.0 ÷ 2.0 = 3.0 m/s² and Q gives 9.0 ÷ "
               "3.5 = 2.6 m/s² — Q's extra mass more than cancels its extra "
               "force.",
    },
    {
        "id": "ks4-newtons-laws-h04",
        "subtopic_slug": "newtons-laws",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lift of mass 800 kg is pulled upwards by a cable. The "
                "tension in the cable is 8600 N and the weight of the lift "
                "is 7840 N. Determine the acceleration of the lift.",
        "options": [
            "10.8 m/s² upwards",
            "0.95 m/s² upwards",
            "0.95 m/s² downwards",
            "20.6 m/s² upwards",
        ],
        "correct_index": 1,
        "why": "The resultant force is 8600 − 7840 = 760 N upwards, so a = "
               "760 ÷ 800 = 0.95 m/s² upwards.",
    },

    # ── stopping-distance-braking ────────────────────────── BASE ───────
    {
        "id": "ks4-stopping-distance-braking-e01",
        "subtopic_slug": "stopping-distance-braking",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define the thinking distance of a vehicle.",
        "options": [
            "The distance travelled while the driver reacts, before braking",
            "The distance travelled after the brakes are applied until it "
            "stops",
            "The total distance travelled from seeing a hazard to stopping",
            "The gap a driver leaves between their car and the one in front",
        ],
        "correct_index": 0,
        "why": "Thinking distance = speed × reaction time — the ground "
               "covered in the moment before the driver touches the brakes.",
    },
    {
        "id": "ks4-stopping-distance-braking-e02",
        "subtopic_slug": "stopping-distance-braking",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A driver with a reaction time of 0.70 s is travelling at "
                "30 m/s. Calculate the thinking distance.",
        "options": [
            "43 m",
            "30.7 m",
            "21 m",
            "0.023 m",
        ],
        "correct_index": 2,
        "why": "Thinking distance = speed × reaction time = 30 m/s × 0.70 s "
               "= 21 m.",
    },
    {
        "id": "ks4-stopping-distance-braking-e03",
        "subtopic_slug": "stopping-distance-braking",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the factor that increases the braking distance but "
                "not the thinking distance.",
        "options": [
            "The driver having taken drugs before setting off",
            "Worn brake pads that grip the discs poorly",
            "The driver being distracted by a mobile phone",
            "The driver having drunk alcohol before setting off",
        ],
        "correct_index": 1,
        "why": "Worn brakes reduce the braking force, which lengthens the "
               "distance travelled after the brakes are applied; the other "
               "three lengthen the driver's reaction time instead.",
    },
    {
        "id": "ks4-stopping-distance-braking-e04",
        "subtopic_slug": "stopping-distance-braking",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car's stopping distance is 36 m and its braking distance "
                "is 24 m. Calculate the thinking distance.",
        "options": [
            "60 m",
            "24 m",
            "36 m",
            "12 m",
        ],
        "correct_index": 3,
        "why": "Stopping distance = thinking distance + braking distance, so "
               "the thinking distance is 36 − 24 = 12 m.",
    },
    {
        "id": "ks4-stopping-distance-braking-s01",
        "subtopic_slug": "stopping-distance-braking",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a car's braking distance is longer on a wet "
                "road than on a dry one.",
        "options": [
            "Water increases the car's mass, so more energy must be removed",
            "Water increases the driver's reaction time on a wet road",
            "Water reduces the car's weight, so the brakes have less to hold on to",
            "Water reduces the friction at the tyres, so braking force is less",
        ],
        "correct_index": 3,
        "why": "A smaller frictional force at the tyres means the car's "
               "kinetic energy is removed over a longer distance.",
    },
    {
        "id": "ks4-stopping-distance-braking-s02",
        "subtopic_slug": "stopping-distance-braking",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car travelling at 15 m/s has a braking distance of 18 m. "
                "Estimate its braking distance at 45 m/s on the same road "
                "with the same braking force.",
        "options": [
            "54 m",
            "162 m",
            "72 m",
            "36 m",
        ],
        "correct_index": 1,
        "why": "Braking distance is proportional to v², and the speed has "
               "tripled, so the braking distance becomes 3² × 18 = 162 m.",
    },
    {
        "id": "ks4-stopping-distance-braking-s03",
        "subtopic_slug": "stopping-distance-braking",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car travels at 24 m/s. The driver's reaction time is "
                "0.50 s and the braking distance is 45 m. Calculate the "
                "stopping distance.",
        "options": [
            "45 m",
            "69 m",
            "57 m",
            "12 m",
        ],
        "correct_index": 2,
        "why": "Thinking distance = 24 × 0.50 = 12 m, and stopping distance "
               "= 12 + 45 = 57 m.",
    },
    {
        "id": "ks4-stopping-distance-braking-s04",
        "subtopic_slug": "stopping-distance-braking",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a fully loaded lorry has a longer stopping "
                "distance than the same lorry when empty, at the same speed.",
        "options": [
            "It has more kinetic energy to remove, so the braking force acts "
            "over a longer distance",
            "Its greater mass lengthens the driver's reaction time, so the "
            "thinking distance grows",
            "Its greater mass raises the friction, so the brakes overheat "
            "and fail",
            "Its greater weight presses the tyres down harder, lengthening "
            "the thinking distance",
        ],
        "correct_index": 0,
        "why": "Braking distance depends on how much kinetic energy the "
               "brakes must remove, and more mass at the same speed means "
               "more energy to remove.",
    },
    {
        "id": "ks4-stopping-distance-braking-h01",
        "subtopic_slug": "stopping-distance-braking",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "At 13 m/s a car has a thinking distance of 9.0 m and a "
                "braking distance of 14 m. Estimate its total stopping "
                "distance at 26 m/s for the same driver, car and road.",
        "options": [
            "46 m",
            "74 m",
            "92 m",
            "23 m",
        ],
        "correct_index": 1,
        "why": "Thinking distance is proportional to speed, so it doubles to "
               "18 m, while braking distance is proportional to v², so it "
               "quadruples to 56 m — a total of 74 m.",
    },
    {
        "id": "ks4-stopping-distance-braking-h02",
        "subtopic_slug": "stopping-distance-braking",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Fitting tyres with deeper tread will "
                "shorten a car's thinking distance.' Evaluate this "
                "statement.",
        "options": [
            "Correct — better grip lets the driver react and stop sooner",
            "Correct — deeper tread shortens the thinking and braking "
            "distances",
            "Incorrect — tyre tread has no effect on the stopping distance",
            "Incorrect — tread changes grip, so it shortens the braking "
            "distance",
        ],
        "correct_index": 3,
        "why": "Thinking distance depends only on speed and the driver's "
               "reaction time; tread changes the friction available once the "
               "brakes are applied.",
    },
    {
        "id": "ks4-stopping-distance-braking-h03",
        "subtopic_slug": "stopping-distance-braking",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Car X travels at 20 m/s with a driver whose reaction time "
                "is 0.90 s. Car Y travels at 25 m/s with a driver whose "
                "reaction time is 0.50 s. Determine which driver has the "
                "longer thinking distance.",
        "options": [
            "Car X: 18 m compared with 12.5 m for car Y",
            "Car Y: 22.5 m compared with 18 m for car X",
            "Car Y, because thinking distance is decided by speed alone",
            "They are equal, because thinking distance depends only on "
            "reaction time",
        ],
        "correct_index": 0,
        "why": "Thinking distance = speed × reaction time, so 20 × 0.90 = "
               "18 m beats 25 × 0.50 = 12.5 m — the longer reaction time "
               "outweighs the lower speed.",
    },
    {
        "id": "ks4-stopping-distance-braking-h04",
        "subtopic_slug": "stopping-distance-braking",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "At 20 m/s a car's stopping distance is 60 m, of which 18 m "
                "is thinking distance. Determine its stopping distance at "
                "10 m/s for the same car, driver and road.",
        "options": [
            "30 m",
            "15 m",
            "19.5 m",
            "25.5 m",
        ],
        "correct_index": 2,
        "why": "Halving the speed halves the thinking distance to 9.0 m but "
               "quarters the braking distance from 42 m to 10.5 m, giving "
               "19.5 m in total.",
    },

    # ── motion-in-a-circle ───────────────── TRIPLE ONLY, HIGHER ───────
    {
        "id": "ks4-motion-in-a-circle-e01",
        "subtopic_slug": "motion-in-a-circle",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "An object moves in a circle at a constant speed. State "
                "which quantity is changing continuously.",
        "options": [
            "The speed of the object",
            "The direction of the velocity",
            "The mass of the object",
            "The magnitude of the centripetal force",
        ],
        "correct_index": 1,
        "why": "Velocity is a vector, and in a circle its direction changes "
               "at every instant even though its magnitude stays the same.",
    },
    {
        "id": "ks4-motion-in-a-circle-e02",
        "subtopic_slug": "motion-in-a-circle",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the direction of the acceleration of an object moving "
                "in a circle at constant speed.",
        "options": [
            "Along the tangent, in the direction of motion",
            "Outwards, away from the centre of the circle",
            "Vertically downwards, in the direction of gravity",
            "Towards the centre of the circle",
        ],
        "correct_index": 3,
        "why": "Centripetal means centre-seeking: the resultant force, and "
               "therefore the acceleration, points at the centre of the "
               "circle.",
    },
    {
        "id": "ks4-motion-in-a-circle-e03",
        "subtopic_slug": "motion-in-a-circle",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A fairground 'rotor' spins fast enough to hold its riders "
                "pressed against the inside of its cylindrical wall. State "
                "what provides the centripetal force on a rider.",
        "options": [
            "The rider's weight, acting downwards",
            "Friction between the rider's back and the wall",
            "The normal contact force of the wall, pushing inwards",
            "An outward force produced by the spinning of the ride",
        ],
        "correct_index": 2,
        "why": "The wall pushes inwards at right angles to its surface, and "
               "that inward push is what curves the rider's path; friction "
               "acts upwards, holding the rider up.",
    },
    {
        "id": "ks4-motion-in-a-circle-e04",
        "subtopic_slug": "motion-in-a-circle",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by a centripetal force.",
        "options": [
            "The resultant force on the object, directed towards the centre "
            "of the circle",
            "An extra force that appears only while an object moves in a "
            "circle",
            "The outward force the object exerts on whatever holds it in its "
            "circle",
            "The force acting along the tangent, which keeps the object "
            "moving",
        ],
        "correct_index": 0,
        "why": "Centripetal force is not a new kind of force — it is the name "
               "for whichever resultant force happens to point at the centre.",
    },
    {
        "id": "ks4-motion-in-a-circle-s01",
        "subtopic_slug": "motion-in-a-circle",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why an object moving in a circle at constant speed "
                "is not in equilibrium.",
        "options": [
            "Its velocity changes direction, so it accelerates and a "
            "resultant force must act",
            "Its speed changes continuously, so a resultant force must act "
            "on it",
            "It is in equilibrium, because the centripetal and centrifugal "
            "forces balance",
            "Gravity acts on it, and gravity can never be balanced in a "
            "circle",
        ],
        "correct_index": 0,
        "why": "Equilibrium means zero resultant force, but a velocity that "
               "changes direction is an acceleration, and acceleration "
               "requires a resultant force.",
    },
    {
        "id": "ks4-motion-in-a-circle-s02",
        "subtopic_slug": "motion-in-a-circle",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A ball is whirled in a horizontal circle on the end of a "
                "string, and the string snaps. Predict the path the ball "
                "takes immediately afterwards.",
        "options": [
            "It moves directly outwards, along the line of the radius",
            "It continues in a circle of a larger radius",
            "It moves in a straight line along the tangent to the circle",
            "It drops vertically from the point where the string snapped",
        ],
        "correct_index": 2,
        "why": "With the centripetal force gone there is no resultant force, "
               "so Newton's First Law keeps it going in the direction it was "
               "already travelling — along the tangent.",
    },
    {
        "id": "ks4-motion-in-a-circle-s03",
        "subtopic_slug": "motion-in-a-circle",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A cyclist rides at a steady 8.0 m/s around a circular "
                "track. Describe her acceleration.",
        "options": [
            "Zero, because her speed is constant",
            "8.0 m/s², directed along her direction of travel",
            "Directed outwards, away from the centre of the track",
            "Non-zero and directed towards the centre of the track",
        ],
        "correct_index": 3,
        "why": "Constant speed is not constant velocity: her direction "
               "changes, so there is a centripetal acceleration pointing at "
               "the centre.",
    },
    {
        "id": "ks4-motion-in-a-circle-s04",
        "subtopic_slug": "motion-in-a-circle",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Describe how the centripetal force is provided for a "
                "roller-coaster car at the lowest point of a vertical loop.",
        "options": [
            "By the weight of the car alone, which acts towards the centre",
            "By the normal contact force of the track, which exceeds the "
            "weight",
            "By friction between the wheels and the track, acting inwards",
            "By a centrifugal force that pushes the car towards the centre",
        ],
        "correct_index": 1,
        "why": "At the bottom of the loop the centre lies directly above, so "
               "the upward contact force must be larger than the downward "
               "weight to give a net inward force.",
    },
    {
        "id": "ks4-motion-in-a-circle-h01",
        "subtopic_slug": "motion-in-a-circle",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student says: 'When a car turns a corner, a centrifugal "
                "force pushes the passengers outwards.' Evaluate this "
                "statement.",
        "options": [
            "Correct — the outward force is the Third Law pair of the "
            "centripetal force",
            "Correct — the outward force grows as the car takes the corner "
            "faster",
            "Incorrect — no force of any kind acts on the passengers as the "
            "car turns",
            "Incorrect — the passengers tend to continue straight on while "
            "the car turns",
        ],
        "correct_index": 3,
        "why": "There is no outward force: the passengers obey Newton's "
               "First Law and keep going straight, so the side of the car "
               "has to push them inwards.",
    },
    {
        "id": "ks4-motion-in-a-circle-h02",
        "subtopic_slug": "motion-in-a-circle",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Two satellites are in stable circular orbits around the "
                "Earth. Satellite A's orbit has a smaller radius than "
                "satellite B's. Compare their orbital speeds.",
        "options": [
            "B is faster, because a larger orbit means a longer path to cover",
            "A is faster: a tighter orbit needs, and gets, a bigger inward "
            "force",
            "They travel at the same speed, because gravity acts equally on "
            "both",
            "A is slower, because gravity is stronger nearby and holds it "
            "back",
        ],
        "correct_index": 1,
        "why": "Closer to the Earth gravity is stronger, so it can supply "
               "the larger centripetal force a faster, tighter orbit needs — "
               "low satellites orbit faster.",
    },
    {
        "id": "ks4-motion-in-a-circle-h03",
        "subtopic_slug": "motion-in-a-circle",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A planet moves around the Sun in a circular orbit at "
                "constant speed. Explain why the Sun's gravitational pull "
                "does no work on the planet.",
        "options": [
            "The gravitational force is at 90° to the motion at every instant",
            "The gravitational force is effectively zero at that distance",
            "The planet's velocity is zero in the direction of the force",
            "The work done moving inwards cancels the work done moving "
            "outwards",
        ],
        "correct_index": 0,
        "why": "Work needs a force component along the direction of motion, "
               "and in a circle the pull is radial while the velocity is "
               "tangential, so there is none.",
    },
    {
        "id": "ks4-motion-in-a-circle-h04",
        "subtopic_slug": "motion-in-a-circle",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A fairground ride carries a car around a horizontal circle "
                "at constant speed. Compare the car's velocity and "
                "acceleration at two points half a revolution apart.",
        "options": [
            "Both the velocity and the acceleration are the same at the two "
            "points",
            "The velocity is the same but the acceleration is reversed",
            "Both the velocity and the acceleration are reversed in direction",
            "The velocity is reversed but the acceleration is the same",
        ],
        "correct_index": 2,
        "why": "Half a revolution later the car is travelling the opposite "
               "way, so its velocity is reversed, and the centre now lies on "
               "the opposite side, so the centripetal acceleration is "
               "reversed too.",
    },

    # ── momentum ─────────────────────────────────── HIGHER TIER ───────
    {
        "id": "ks4-momentum-e01",
        "subtopic_slug": "momentum",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Momentum is calculated using p = mv. State the unit of "
                "momentum.",
        "options": [
            "N",
            "kg m/s²",
            "kg m/s",
            "m/s",
        ],
        "correct_index": 2,
        "why": "Momentum is mass × velocity, so its unit is kilogram × metre "
               "per second — kg m/s.",
    },
    {
        "id": "ks4-momentum-e02",
        "subtopic_slug": "momentum",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A 1500 kg car travels along a straight road at 12 m/s. "
                "Calculate its momentum.",
        "options": [
            "18 000 kg m/s",
            "125 kg m/s",
            "1512 kg m/s",
            "9000 kg m/s",
        ],
        "correct_index": 0,
        "why": "p = mv = 1500 kg × 12 m/s = 18 000 kg m/s.",
    },
    {
        "id": "ks4-momentum-e03",
        "subtopic_slug": "momentum",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State why momentum is described as a vector quantity.",
        "options": [
            "Because its value is always positive",
            "Because it has a direction as well as a size",
            "Because it is measured in kg m/s",
            "Because it is conserved in every collision and explosion",
        ],
        "correct_index": 1,
        "why": "Momentum takes the direction of the velocity, so a full "
               "answer needs both a size and a direction.",
    },
    {
        "id": "ks4-momentum-e04",
        "subtopic_slug": "momentum",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Complete the statement: in a closed system, the total "
                "momentum before an event is …",
        "options": [
            "always zero",
            "greater than the total momentum after the event",
            "equal to the total kinetic energy after the event",
            "equal to the total momentum after the event",
        ],
        "correct_index": 3,
        "why": "With no external forces acting, momentum is conserved: the "
               "total before an event equals the total after it.",
    },
    {
        "id": "ks4-momentum-s01",
        "subtopic_slug": "momentum",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A 60 g tennis ball leaves a racket at 45 m/s. Calculate its "
                "momentum.",
        "options": [
            "750 kg m/s",
            "2.7 kg m/s",
            "2700 kg m/s",
            "1.4 kg m/s",
        ],
        "correct_index": 1,
        "why": "p = mv, with the mass in kilograms: 0.060 kg × 45 m/s = "
               "2.7 kg m/s.",
    },
    {
        "id": "ks4-momentum-s02",
        "subtopic_slug": "momentum",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A 2.0 kg trolley moving at 3.0 m/s to the right approaches "
                "a 1.0 kg trolley moving at 4.0 m/s to the left. Taking "
                "rightwards as positive, calculate the total momentum before "
                "they meet.",
        "options": [
            "10 kg m/s to the right",
            "2.0 kg m/s to the left",
            "0 kg m/s, because they move in opposite directions",
            "2.0 kg m/s to the right",
        ],
        "correct_index": 3,
        "why": "Momentum is a vector, so the leftward momentum is negative: "
               "(+6.0) + (−4.0) = +2.0 kg m/s, that is 2.0 kg m/s to the "
               "right.",
    },
    {
        "id": "ks4-momentum-s03",
        "subtopic_slug": "momentum",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A 0.045 kg golf ball leaves a club at 70 m/s. A 7.3 kg "
                "bowling ball rolls along a lane at 4.0 m/s. Determine which "
                "has the greater momentum.",
        "options": [
            "The bowling ball: 29 kg m/s against 3.2 kg m/s for the golf ball",
            "The golf ball: 3.2 kg m/s against 1.8 kg m/s for the bowling ball",
            "They are equal, because momentum depends on speed alone",
            "The golf ball, because the greater velocity always wins",
        ],
        "correct_index": 0,
        "why": "p = mv, so the bowling ball has 7.3 × 4.0 = 29 kg m/s against "
               "the golf ball's 0.045 × 70 = 3.2 kg m/s — mass matters as "
               "much as speed.",
    },
    {
        "id": "ks4-momentum-s04",
        "subtopic_slug": "momentum",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A 0.50 kg ball travelling at 8.0 m/s hits a wall "
                "perpendicularly and rebounds at 6.0 m/s. Calculate the "
                "magnitude of its change in momentum.",
        "options": [
            "1.0 kg m/s",
            "3.0 kg m/s",
            "7.0 kg m/s",
            "4.0 kg m/s",
        ],
        "correct_index": 2,
        "why": "The ball reverses direction, so Δp = (−3.0) − (+4.0) = "
               "−7.0 kg m/s, a magnitude of 7.0 kg m/s.",
    },
    {
        "id": "ks4-momentum-h01",
        "subtopic_slug": "momentum",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A 1400 kg car moving east at 18 m/s runs into the back of a "
                "600 kg car moving east at 6.0 m/s, and the two lock "
                "together. Determine their common velocity.",
        "options": [
            "14.4 m/s east",
            "24.0 m/s east",
            "12.0 m/s east",
            "9.0 m/s east",
        ],
        "correct_index": 0,
        "why": "Total momentum before is (1400 × 18) + (600 × 6.0) = "
               "28 800 kg m/s, and afterwards 28 800 = 2000 × v, so v = "
               "14.4 m/s east.",
    },
    {
        "id": "ks4-momentum-h02",
        "subtopic_slug": "momentum",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A stationary 3.0 kg firework shell explodes into two "
                "pieces. A 0.50 kg piece flies forwards at 90 m/s. "
                "Determine the velocity of the other piece.",
        "options": [
            "18 m/s forwards",
            "90 m/s backwards",
            "18 m/s backwards",
            "15 m/s backwards",
        ],
        "correct_index": 2,
        "why": "The total momentum starts at zero, so the pieces must carry "
               "equal and opposite momenta: 0.50 × 90 = 45 kg m/s forwards, "
               "so 2.5 kg × v = 45 kg m/s backwards, giving 18 m/s.",
    },
    {
        "id": "ks4-momentum-h03",
        "subtopic_slug": "momentum",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A 0.15 kg cricket ball travelling at 30 m/s is caught. By "
                "letting his hands move back, the fielder stops the ball in "
                "0.50 s instead of 0.10 s. Determine the reduction in the "
                "average force on his hands.",
        "options": [
            "4.5 N",
            "54 N",
            "5.0 N",
            "36 N",
        ],
        "correct_index": 3,
        "why": "The change in momentum is fixed at 0.15 × 30 = 4.5 kg m/s, "
               "so F = Δp ÷ t falls from 45 N to 9.0 N — a reduction of "
               "36 N.",
    },
    {
        "id": "ks4-momentum-h04",
        "subtopic_slug": "momentum",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student claims that a 500 kg cannon recoils at the same "
                "speed as the 5.0 kg ball it fires, because momentum is "
                "conserved. Explain the error in this claim.",
        "options": [
            "There is no error — conservation of momentum makes the speeds "
            "equal",
            "Momentum, not speed, is shared equally, so the cannon recoils "
            "far slower",
            "Momentum is not conserved in an explosion, so nothing can be "
            "predicted",
            "The cannon recoils faster, because the ball loses momentum to "
            "the air",
        ],
        "correct_index": 1,
        "why": "The two momenta are equal and opposite, so 500 × v = 5.0 × "
               "u — a hundred times the mass means one hundredth of the "
               "speed.",
    },
]
