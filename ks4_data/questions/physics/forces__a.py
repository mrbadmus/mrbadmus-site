"""Physics · Forces — part A: the vector foundations of the topic.

Six subtopics: scalar/vector quantities, contact and non-contact forces,
gravity, resultant forces (all BASE), then resolving forces and free body
diagrams (both HIGHER + TRIPLE ONLY).

The distractors are built almost entirely from the four declared common
mistakes for these pages: speed/velocity and distance/displacement treated as
synonyms; gravity mistaken for a contact force and normal contact force
conflated with weight; mass and weight swapped, with weight quoted in
kilograms or assumed to travel unchanged to the Moon; and "resultant force
zero" read as "stationary" rather than "constant velocity". The resolving and
free-body items add the sin/cos swap and the classic "a force the object
exerts belongs on its own free body diagram".

g is taken as 9.8 N/kg throughout (1.6 N/kg on the Moon), matching the lesson
pages. No question needs a figure: every arrangement of forces is described in
words and the student is asked for the result.
"""

TOPIC = "forces"
SUBJECT = "physics"

QUESTIONS = [
    # ── scalar-vector-quantities ────────────────────────────────────────
    {
        "id": "ks4-scalar-vector-quantities-e01",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of the following quantities is a vector?",
        "options": [
            "Temperature, measured in °C",
            "Energy, measured in J",
            "Acceleration, measured in m/s²",
            "Mass, measured in kg",
        ],
        "correct_index": 2,
        "why": "Acceleration has both a magnitude and a direction, so it is a "
               "vector; the other three have magnitude only.",
    },
    {
        "id": "ks4-scalar-vector-quantities-e02",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a scalar quantity.",
        "options": [
            "A quantity that has magnitude only",
            "A quantity that has both magnitude and direction",
            "A quantity that is always measured in newtons",
            "A quantity that can never have a negative value",
        ],
        "correct_index": 0,
        "why": "A scalar is fully described by its size alone — no direction "
               "is needed, which is what separates it from a vector.",
    },
    {
        "id": "ks4-scalar-vector-quantities-e03",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A vector quantity is represented by an arrow. State what "
                "the length of the arrow represents.",
        "options": [
            "The direction of the vector",
            "The magnitude of the vector",
            "The time for which the vector acts",
            "The unit in which the vector is measured",
        ],
        "correct_index": 1,
        "why": "Arrow length is drawn in proportion to magnitude; the way the "
               "arrow points carries the direction.",
    },
    {
        "id": "ks4-scalar-vector-quantities-e04",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of the following quantities is a scalar?",
        "options": [
            "Weight",
            "Displacement",
            "Momentum",
            "Mass",
        ],
        "correct_index": 3,
        "why": "Mass is an amount of matter with magnitude only; weight, "
               "displacement and momentum each need a direction as well.",
    },
    {
        "id": "ks4-scalar-vector-quantities-s01",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lift rises 24 m from the ground floor, then travels 9.0 m "
                "back down. State its total distance travelled and its "
                "displacement.",
        "options": [
            "Distance 33 m; displacement 15 m upwards",
            "Distance 15 m; displacement 33 m upwards",
            "Distance 33 m; displacement 33 m upwards",
            "Distance 15 m; displacement 15 m upwards",
        ],
        "correct_index": 0,
        "why": "Distance is the whole path length, 24 + 9.0 = 33 m, while "
               "displacement is the straight line from start to finish, "
               "24 − 9.0 = 15 m upwards.",
    },
    {
        "id": "ks4-scalar-vector-quantities-s02",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car enters a roundabout travelling north at a steady "
                "12 m/s and leaves it travelling south, still at 12 m/s. "
                "Which statement about the car is correct?",
        "options": [
            "Both its speed and its velocity have stayed the same",
            "Its speed has stayed the same but its velocity has changed",
            "Its velocity has stayed the same but its speed has changed",
            "Neither its speed nor its velocity has changed",
        ],
        "correct_index": 1,
        "why": "Speed is a scalar and is still 12 m/s, but velocity includes "
               "direction, and north has become south.",
    },
    {
        "id": "ks4-scalar-vector-quantities-s03",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two forces of 5 N each, acting on the same "
                "object, do not always produce a resultant of 10 N.",
        "options": [
            "Because forces always weaken each other when two act on one "
            "object",
            "Because force is a scalar quantity, and two equal scalars "
            "always cancel",
            "Because 5 N forces can only be added together when the object "
            "is stationary",
            "Because force is a vector, so the direction of each force must "
            "be taken into account",
        ],
        "correct_index": 3,
        "why": "Vectors add with direction: 5 N and 5 N the same way give "
               "10 N, but in opposite directions they give 0 N.",
    },
    {
        "id": "ks4-scalar-vector-quantities-s04",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two ropes are attached to the same point on a fixed post. "
                "One is pulled with a force of 60 N due north and the other "
                "with a force of 80 N due east. Calculate the magnitude of "
                "the resultant pull on the post.",
        "options": [
            "140 N",
            "20 N",
            "100 N",
            "70 N",
        ],
        "correct_index": 2,
        "why": "The forces are at right angles, so resultant² = 60² + 80² = "
               "10 000, giving a resultant of 100 N.",
    },
    {
        "id": "ks4-scalar-vector-quantities-h01",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drone flies 30 m due east, then 40 m due north, then 30 m "
                "due west, and stops. Determine the magnitude of its "
                "displacement from its starting point.",
        "options": [
            "100 m",
            "50 m",
            "40 m",
            "10 m",
        ],
        "correct_index": 2,
        "why": "The 30 m east and 30 m west cancel exactly, leaving only the "
               "40 m north as the straight line from start to finish.",
    },
    {
        "id": "ks4-scalar-vector-quantities-h02",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students walk from the school gate to the science "
                "block. One takes a direct route 90 m long; the other takes "
                "a route 150 m long. Compare the distance travelled and the "
                "displacement of the two students.",
        "options": [
            "Their distances differ but their displacements are identical",
            "Both their distances and their displacements are identical",
            "Their displacements differ but their distances are identical",
            "The student who walked further has the larger displacement",
        ],
        "correct_index": 0,
        "why": "Displacement depends only on the start and end points, which "
               "are the same for both; only the path length differs.",
    },
    {
        "id": "ks4-scalar-vector-quantities-h03",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Energy is a vector, because energy can "
                "be transferred in a particular direction.' Evaluate this "
                "statement.",
        "options": [
            "Correct — anything that can be transferred must have a "
            "direction as well",
            "Incorrect — energy is fully described by its magnitude alone, "
            "so it is scalar",
            "Correct — energy is a vector because joules can be counted in a "
            "direction",
            "Incorrect — energy is neither a scalar nor a vector but a "
            "separate kind",
        ],
        "correct_index": 1,
        "why": "A quantity is a vector only if a direction is part of the "
               "quantity itself; 500 J is a complete statement of energy.",
    },
    {
        "id": "ks4-scalar-vector-quantities-h04",
        "subtopic_slug": "scalar-vector-quantities",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three forces act at the same point on a block: 7 N to the "
                "east, 7 N to the west and 4 N to the north. Determine the "
                "resultant force on the block.",
        "options": [
            "18 N to the east",
            "10 N to the north",
            "0 N — the three forces balance",
            "4 N to the north",
        ],
        "correct_index": 3,
        "why": "The two 7 N forces are equal and opposite so they cancel, "
               "leaving the 4 N northward force as the resultant.",
    },

    # ── contact-noncontact-forces ───────────────────────────────────────
    {
        "id": "ks4-contact-noncontact-forces-e01",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a contact force.",
        "options": [
            "A force that acts only on stationary objects",
            "A force between two objects that are physically touching",
            "A force that acts at a distance through a field",
            "A force that always acts vertically downwards",
        ],
        "correct_index": 1,
        "why": "A contact force needs the two interacting objects to be "
               "touching — friction, tension and upthrust are examples.",
    },
    {
        "id": "ks4-contact-noncontact-forces-e02",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist freewheels along a level road and gradually slows "
                "down. Identify the contact force responsible.",
        "options": [
            "The weight of the cyclist, pulling downwards",
            "The gravitational field of the Earth, acting backwards",
            "The magnetic force between the wheels and the road",
            "Air resistance, which acts on every surface the air touches",
        ],
        "correct_index": 3,
        "why": "Air resistance is a contact force: the air particles have to "
               "touch the cyclist to push backwards on her.",
    },
    {
        "id": "ks4-contact-noncontact-forces-e03",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which non-contact force can only ever attract, and never "
                "repel?",
        "options": [
            "The magnetic force",
            "The electrostatic force",
            "The gravitational force",
            "The frictional force",
        ],
        "correct_index": 2,
        "why": "Gravity is always attractive between masses; magnetic and "
               "electrostatic forces can do either, and friction is a contact "
               "force.",
    },
    {
        "id": "ks4-contact-noncontact-forces-e04",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the upward force that a fluid exerts on an object "
                "placed in it.",
        "options": [
            "Upthrust",
            "Tension",
            "Compression",
            "Normal contact force",
        ],
        "correct_index": 0,
        "why": "Upthrust is the upward push a liquid or gas exerts on an "
               "object placed in it, and it is a contact force.",
    },
    {
        "id": "ks4-contact-noncontact-forces-s01",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A magnet held 2 cm above a bench lifts a steel paperclip up "
                "off the surface. Explain what this shows about the magnetic "
                "force.",
        "options": [
            "It is a contact force, because the paperclip ends up touching "
            "the magnet",
            "It is a non-contact force, because it acted across a gap before "
            "the objects touched",
            "It is a contact force, because the air carries the force between "
            "them",
            "It is not a force at all, because nothing was touching at the "
            "start",
        ],
        "correct_index": 1,
        "why": "The paperclip started to move while there was still a gap, so "
               "the force acted at a distance — it is non-contact.",
    },
    {
        "id": "ks4-contact-noncontact-forces-s02",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fridge magnet holds a note against a steel fridge door. "
                "Name the two forces holding the note in place and state the "
                "type of each.",
        "options": [
            "Magnetic (non-contact) pressing the note on, and friction "
            "(contact) stopping it sliding down",
            "Magnetic (contact) pressing the note on, and friction "
            "(non-contact) stopping it sliding down",
            "Weight (non-contact) pressing the note on, and tension (contact) "
            "stopping it sliding down",
            "Upthrust (contact) holding the note up, and air resistance "
            "(non-contact) stopping it sliding",
        ],
        "correct_index": 0,
        "why": "The magnet pulls across a gap, so it is non-contact, while "
               "friction needs the note and the door to touch.",
    },
    {
        "id": "ks4-contact-noncontact-forces-s03",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the three things a force can change about an object.",
        "options": [
            "Its mass, its speed and its temperature",
            "Its direction, its density and its energy",
            "Its speed, its direction and its shape",
            "Its speed, its mass and its shape",
        ],
        "correct_index": 2,
        "why": "A force can speed an object up or slow it down, turn it, or "
               "deform it; it cannot change how much matter the object "
               "contains.",
    },
    {
        "id": "ks4-contact-noncontact-forces-s04",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that the normal contact force on a laptop "
                "resting on a desk is the same force as the laptop's weight. "
                "Explain what is wrong with this statement.",
        "options": [
            "Nothing is wrong — normal contact force and weight are two "
            "names for one force",
            "They differ only in type: the normal contact force is "
            "non-contact and weight is contact",
            "They differ only in direction: the normal contact force acts "
            "downwards and weight upwards",
            "They are separate forces: the desk pushes back perpendicular to "
            "its surface, while weight is the Earth's pull",
        ],
        "correct_index": 3,
        "why": "They are equal in size here only because the laptop is at "
               "rest; they are separate forces with different causes.",
    },
    {
        "id": "ks4-contact-noncontact-forces-h01",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A charged plastic rod is held near a thin stream of running "
                "water and the stream bends towards the rod without touching "
                "it. Explain the force responsible.",
        "options": [
            "A contact force, because the rod is touching the air that "
            "surrounds the water",
            "A gravitational non-contact force, because the rod attracts the "
            "mass of the water",
            "An electrostatic non-contact force, because the charged rod "
            "attracts water across a gap",
            "A magnetic non-contact force, because water contains iron and "
            "so is magnetic",
        ],
        "correct_index": 2,
        "why": "The rod carries charge and acts on the water across empty "
               "space, which is the signature of an electrostatic "
               "non-contact force.",
    },
    {
        "id": "ks4-contact-noncontact-forces-h02",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One student says the Earth pulls a falling ball downwards. "
                "Another says the ball also pulls the Earth upwards. "
                "Evaluate the two claims.",
        "options": [
            "Only the Earth pulls, because the ball is far too small a mass "
            "to exert any force",
            "Both are right — the ball pulls the Earth equally and "
            "oppositely, but the Earth's mass makes its acceleration "
            "unnoticeable",
            "Only the ball pulls the Earth, because gravity always acts "
            "upwards out of the ground",
            "Neither is right, because gravity is a property of the ball "
            "alone, not an interaction",
        ],
        "correct_index": 1,
        "why": "Gravitational attraction acts between any two masses and the "
               "pair of forces is always equal and opposite.",
    },
    {
        "id": "ks4-contact-noncontact-forces-h03",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A window cleaner stands still on a level platform hanging "
                "from two ropes. Determine which combination of forces acts "
                "on him.",
        "options": [
            "Weight (non-contact, downwards) and the normal contact force "
            "from the platform (contact, upwards), equal in size",
            "Weight (contact, downwards) and tension (non-contact, upwards), "
            "equal in size",
            "Tension in the ropes only, because the ropes hold the whole "
            "arrangement up",
            "Weight (non-contact, downwards) and friction (contact, "
            "upwards), equal in size",
        ],
        "correct_index": 0,
        "why": "Only the platform touches him, so the upward force on him is "
               "the platform's normal contact force; the ropes act on the "
               "platform, not on the man.",
    },
    {
        "id": "ks4-contact-noncontact-forces-h04",
        "subtopic_slug": "contact-noncontact-forces",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the electrostatic force and the gravitational force "
                "in terms of whether each can attract, repel, or both.",
        "options": [
            "Both can only ever attract",
            "Both can attract or repel, depending on the objects",
            "The gravitational force can attract or repel; the electrostatic "
            "force can only attract",
            "The electrostatic force can attract or repel; the gravitational "
            "force can only attract",
        ],
        "correct_index": 3,
        "why": "Like charges repel and opposite charges attract, but masses "
               "only ever pull on one another.",
    },

    # ── gravity ─────────────────────────────────────────────────────────
    {
        "id": "ks4-gravity-e01",
        "subtopic_slug": "gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of gravitational field strength.",
        "options": [
            "N/kg",
            "N",
            "kg",
            "kg/N",
        ],
        "correct_index": 0,
        "why": "Gravitational field strength is the weight per unit of mass, "
               "so it is measured in newtons per kilogram.",
    },
    {
        "id": "ks4-gravity-e02",
        "subtopic_slug": "gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the weight of a 5.0 kg bag of potatoes on Earth. "
                "(g = 9.8 N/kg)",
        "options": [
            "0.51 N",
            "49 N",
            "5.0 N",
            "490 N",
        ],
        "correct_index": 1,
        "why": "W = m × g = 5.0 × 9.8 = 49 N — weight is a force, so the "
               "answer is in newtons.",
    },
    {
        "id": "ks4-gravity-e03",
        "subtopic_slug": "gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement about mass is correct?",
        "options": [
            "Mass is a vector quantity and is measured in newtons, like any "
            "force",
            "Mass becomes about six times smaller when an object is taken to "
            "the Moon",
            "Mass is a scalar measured in kilograms and has the same value "
            "everywhere",
            "Mass is the gravitational force on an object, so it varies with "
            "place",
        ],
        "correct_index": 2,
        "why": "Mass is the amount of matter in an object, so it does not "
               "change when the gravitational field around it changes.",
    },
    {
        "id": "ks4-gravity-e04",
        "subtopic_slug": "gravity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which instrument measures weight rather than mass.",
        "options": [
            "A top-pan balance reading in grams",
            "A measuring cylinder reading in cm³",
            "A beam balance that compares two masses",
            "A calibrated spring balance reading in newtons",
        ],
        "correct_index": 3,
        "why": "A newton meter stretches in proportion to the force pulling "
               "on it, so it reads weight in newtons directly.",
    },
    {
        "id": "ks4-gravity-s01",
        "subtopic_slug": "gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rock has a weight of 78.4 N on Earth. Calculate its mass. "
                "(g = 9.8 N/kg)",
        "options": [
            "768 kg",
            "78.4 kg",
            "0.13 kg",
            "8.0 kg",
        ],
        "correct_index": 3,
        "why": "Rearranging W = mg gives m = W ÷ g = 78.4 ÷ 9.8 = 8.0 kg.",
    },
    {
        "id": "ks4-gravity-s02",
        "subtopic_slug": "gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spacecraft component has a weight of 147 N on Earth, "
                "where g = 9.8 N/kg. Calculate its weight on the Moon, where "
                "g = 1.6 N/kg.",
        "options": [
            "235 N",
            "24 N",
            "91.9 N",
            "147 N",
        ],
        "correct_index": 1,
        "why": "Its mass is 147 ÷ 9.8 = 15 kg everywhere, so on the Moon "
               "W = 15 × 1.6 = 24 N.",
    },
    {
        "id": "ks4-gravity-s03",
        "subtopic_slug": "gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why weight is a vector quantity but mass is not.",
        "options": [
            "Weight always acts towards the centre of the Earth, so it has "
            "direction; mass has magnitude only",
            "Weight is numerically larger than mass, and only the larger of "
            "two quantities can be a vector",
            "Mass is a vector as well, because kilograms measure a quantity "
            "that has a direction",
            "It is the other way round: weight is the scalar of the pair and "
            "mass is the vector",
        ],
        "correct_index": 0,
        "why": "Weight is a gravitational force, and every force has a "
               "direction as well as a size.",
    },
    {
        "id": "ks4-gravity-s04",
        "subtopic_slug": "gravity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The gravitational field strength at the surface of Mars is "
                "3.7 N/kg. A crate has a mass of 40 kg. Determine how much "
                "less the crate weighs on Mars than on Earth. "
                "(g on Earth = 9.8 N/kg)",
        "options": [
            "148 N",
            "392 N",
            "244 N",
            "6.1 N",
        ],
        "correct_index": 2,
        "why": "On Earth W = 40 × 9.8 = 392 N and on Mars W = 40 × 3.7 = "
               "148 N, so the difference is 392 − 148 = 244 N.",
    },
    {
        "id": "ks4-gravity-h01",
        "subtopic_slug": "gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Astronauts on the International Space Station, about "
                "400 km above the Earth, appear to float. Explain why they "
                "are not truly weightless.",
        "options": [
            "The field strength is still about 8.7 N/kg, so they do have "
            "weight; they float only because they are in free fall",
            "Gravity does not reach that far from the Earth, so they have no "
            "weight at all and float freely",
            "Their mass has fallen to zero at that altitude, so their weight "
            "must be zero as well",
            "The station's orbital speed exactly cancels out the Earth's "
            "gravitational field at that height",
        ],
        "correct_index": 0,
        "why": "Gravitational field strength falls only slowly with height, "
               "so weight is still large — the floating comes from free "
               "fall, not from an absence of gravity.",
    },
    {
        "id": "ks4-gravity-h02",
        "subtopic_slug": "gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two blocks are carried from the Earth to the Moon. Block A "
                "has twice the mass of block B. Compare their masses and "
                "their weights on the Moon with the values on Earth.",
        "options": [
            "Both masses and both weights are unchanged, because neither "
            "depends on where the block is",
            "Both masses are unchanged, both weights fall to about a sixth, "
            "and A still weighs twice B",
            "Both masses fall to about a sixth while both weights are "
            "unchanged, so A still weighs twice B",
            "A's mass falls to about a sixth but B's does not, because A is "
            "the heavier of the two blocks",
        ],
        "correct_index": 1,
        "why": "Mass never changes with location, while weight is m × g and "
               "g on the Moon is about a sixth of Earth's, so the ratio "
               "between the two blocks survives.",
    },
    {
        "id": "ks4-gravity-h03",
        "subtopic_slug": "gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rover of mass 12 kg has a weight of 44.4 N on the surface "
                "of a planet. Determine the gravitational field strength at "
                "that surface.",
        "options": [
            "0.27 N/kg",
            "533 N/kg",
            "3.7 N/kg",
            "9.8 N/kg",
        ],
        "correct_index": 2,
        "why": "Rearranging W = mg gives g = W ÷ m = 44.4 ÷ 12 = 3.7 N/kg.",
    },
    {
        "id": "ks4-gravity-h04",
        "subtopic_slug": "gravity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crane holds a steel beam of mass 1200 kg stationary in "
                "mid-air. Calculate the minimum upward force the cable must "
                "provide. (g = 9.8 N/kg)",
        "options": [
            "1200 N",
            "122 N",
            "23 500 N",
            "11 800 N",
        ],
        "correct_index": 3,
        "why": "The cable must balance the beam's weight, W = 1200 × 9.8 = "
               "11 760 N, which is 11 800 N to 3 significant figures.",
    },

    # ── resultant-forces ────────────────────────────────────────────────
    {
        "id": "ks4-resultant-forces-e01",
        "subtopic_slug": "resultant-forces",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the resultant force on an object.",
        "options": [
            "The largest of the individual forces acting on the object",
            "The total of all the forces, added without regard to their "
            "directions",
            "The force the object exerts on its surroundings while the "
            "forces act",
            "The single force that has the same effect as all the forces "
            "together",
        ],
        "correct_index": 3,
        "why": "The resultant is one force that could replace all the others "
               "and leave the motion of the object unchanged.",
    },
    {
        "id": "ks4-resultant-forces-e02",
        "subtopic_slug": "resultant-forces",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two people push a shopping trolley in the same direction, "
                "one with a force of 30 N and the other with a force of "
                "45 N. Calculate the resultant force on the trolley.",
        "options": [
            "15 N",
            "1350 N",
            "75 N",
            "37.5 N",
        ],
        "correct_index": 2,
        "why": "Forces acting in the same direction simply add: 30 + 45 = "
               "75 N in that direction.",
    },
    {
        "id": "ks4-resultant-forces-e03",
        "subtopic_slug": "resultant-forces",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The resultant force on an object is zero. Describe the "
                "possible motion of the object.",
        "options": [
            "It must be stationary and cannot be moving at all",
            "It is either stationary or moving at a constant velocity",
            "It must be slowing down and will eventually stop",
            "It must be accelerating in the direction it is moving",
        ],
        "correct_index": 1,
        "why": "A zero resultant means no change of motion, so an object "
               "already moving keeps moving at the same speed in the same "
               "direction.",
    },
    {
        "id": "ks4-resultant-forces-e04",
        "subtopic_slug": "resultant-forces",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to an object when the forces acting on "
                "it are unbalanced.",
        "options": [
            "It accelerates in the direction of the resultant force",
            "It remains at rest whatever its previous motion",
            "It moves at a constant speed in a straight line",
            "Its mass increases",
        ],
        "correct_index": 0,
        "why": "An unbalanced set of forces leaves a resultant, and a "
               "resultant force changes the object's velocity.",
    },
    {
        "id": "ks4-resultant-forces-s01",
        "subtopic_slug": "resultant-forces",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lift has a weight of 6400 N and the cable holding it "
                "exerts an upward tension of 6400 N. Describe the motion of "
                "the lift.",
        "options": [
            "It is stationary, or moving at a constant velocity",
            "It is accelerating upwards",
            "It is accelerating downwards",
            "A lift cannot move at all while the forces on it are balanced",
        ],
        "correct_index": 0,
        "why": "The two forces are equal and opposite so the resultant is "
               "zero, which allows rest or steady motion but no acceleration.",
    },
    {
        "id": "ks4-resultant-forces-s02",
        "subtopic_slug": "resultant-forces",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A boat's engine provides a forward force of 2200 N while "
                "the water resistance on the hull is 1500 N. Determine the "
                "resultant force on the boat and its effect.",
        "options": [
            "3700 N forward — the boat accelerates forward",
            "700 N backward — the boat slows down",
            "700 N forward — the boat accelerates forward",
            "0 N — the boat travels at a constant speed",
        ],
        "correct_index": 2,
        "why": "The forces are in opposite directions, so 2200 − 1500 = "
               "700 N, acting in the direction of the larger force.",
    },
    {
        "id": "ks4-resultant-forces-s03",
        "subtopic_slug": "resultant-forces",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A parachutist has a weight of 750 N. At one moment during "
                "her fall the air resistance acting on her is 300 N. "
                "Calculate the resultant force on her and state its "
                "direction.",
        "options": [
            "1050 N downwards",
            "450 N downwards",
            "450 N upwards",
            "300 N upwards",
        ],
        "correct_index": 1,
        "why": "Weight acts down and air resistance up, so the resultant is "
               "750 − 300 = 450 N in the direction of the larger force, "
               "downwards.",
    },
    {
        "id": "ks4-resultant-forces-s04",
        "subtopic_slug": "resultant-forces",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A box on a smooth floor is pushed with a horizontal force "
                "of 7.0 N due east while a rope pulls it with a horizontal "
                "force of 24 N due north. Calculate the magnitude of the "
                "resultant force on the box.",
        "options": [
            "31 N",
            "17 N",
            "16 N",
            "25 N",
        ],
        "correct_index": 3,
        "why": "The forces are perpendicular, so resultant² = 7.0² + 24² = "
               "625, giving a resultant of 25 N.",
    },
    {
        "id": "ks4-resultant-forces-h01",
        "subtopic_slug": "resultant-forces",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist pedals with a driving force of 120 N and the "
                "total resistive force on her is also 120 N. A student "
                "concludes that the cyclist must be stationary. Explain what "
                "is wrong with this conclusion.",
        "options": [
            "A zero resultant means constant velocity, so she could equally "
            "be riding at a steady speed in a straight line",
            "Nothing is wrong, because a zero resultant force always means "
            "that the object must be stationary",
            "A zero resultant means the cyclist must be accelerating "
            "steadily rather than travelling at rest",
            "The two forces cannot both be 120 N, because a driving force is "
            "always larger than the resistance",
        ],
        "correct_index": 0,
        "why": "Balanced forces mean no change of velocity, and a velocity "
               "that does not change may be any steady value, including zero.",
    },
    {
        "id": "ks4-resultant-forces-h02",
        "subtopic_slug": "resultant-forces",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three horizontal forces act on a crate that starts at rest: "
                "90 N due east, 50 N due west and 40 N due west. Determine "
                "the resultant force and predict the crate's motion.",
        "options": [
            "180 N east — the crate accelerates east",
            "90 N east — only the largest force matters",
            "0 N — the crate remains at rest",
            "10 N west — the crate accelerates west",
        ],
        "correct_index": 2,
        "why": "The two westward forces total 90 N, which exactly cancels the "
               "90 N eastward force, so there is nothing left to change the "
               "crate's motion.",
    },
    {
        "id": "ks4-resultant-forces-h03",
        "subtopic_slug": "resultant-forces",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A skydiver of weight 700 N opens her parachute. Immediately "
                "afterwards the air resistance acting on her is 1600 N. "
                "Determine the resultant force on her and describe what "
                "happens to her speed.",
        "options": [
            "2300 N downwards — she speeds up",
            "900 N upwards — she slows down",
            "900 N downwards — she speeds up",
            "0 N — she continues to fall at a constant speed",
        ],
        "correct_index": 1,
        "why": "Air resistance now exceeds weight, so the resultant of "
               "1600 − 700 = 900 N acts upwards, opposite to her motion, and "
               "she decelerates.",
    },
    {
        "id": "ks4-resultant-forces-h04",
        "subtopic_slug": "resultant-forces",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A trolley is pulled at one point by a horizontal force of "
                "25 N due east and a horizontal force of 25 N due north. "
                "Determine the magnitude of the resultant and compare it "
                "with the sum of the two forces.",
        "options": [
            "50 N — equal to the sum, because two forces always add "
            "arithmetically",
            "0 N — the two forces are equal in size, so they cancel each "
            "other out",
            "25 N — the resultant of two equal forces is equal to one of "
            "them",
            "35 N — less than the 50 N sum, because the forces act at right "
            "angles",
        ],
        "correct_index": 3,
        "why": "Resultant² = 25² + 25² = 1250, giving 35 N; vectors at an "
               "angle never add to the full arithmetic total.",
    },

    # ── resolving-forces  (HIGHER · TRIPLE ONLY) ────────────────────────
    {
        "id": "ks4-resolving-forces-e01",
        "subtopic_slug": "resolving-forces",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A single force is replaced by two perpendicular components. "
                "State how the size of each component compares with the size "
                "of the original force.",
        "options": [
            "Each component is exactly half the size of the original force",
            "Each component is smaller than the original force",
            "Each component is larger than the original force",
            "Each component is the same size as the original force",
        ],
        "correct_index": 1,
        "why": "The original force is the hypotenuse of the right-angled "
               "triangle, and the hypotenuse is always the longest side.",
    },
    {
        "id": "ks4-resolving-forces-e02",
        "subtopic_slug": "resolving-forces",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A force of 20 N acts at 60° to the horizontal. Calculate "
                "its horizontal component. (cos 60° = 0.500)",
        "options": [
            "10.0 N",
            "17.3 N",
            "20.0 N",
            "0.33 N",
        ],
        "correct_index": 0,
        "why": "Fx = F cos θ = 20 × 0.500 = 10.0 N.",
    },
    {
        "id": "ks4-resolving-forces-e03",
        "subtopic_slug": "resolving-forces",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A single force has been resolved into a horizontal "
                "component of 12.0 N and a vertical component of 5.0 N. "
                "Calculate the magnitude of the original force.",
        "options": [
            "17.0 N",
            "7.0 N",
            "13.0 N",
            "60.0 N",
        ],
        "correct_index": 2,
        "why": "The components are perpendicular, so F² = 12.0² + 5.0² = 169 "
               "and F = 13.0 N.",
    },
    {
        "id": "ks4-resolving-forces-e04",
        "subtopic_slug": "resolving-forces",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by resolving a force.",
        "options": [
            "Adding two forces together to find a single resultant",
            "Measuring the size of a force with a newton meter",
            "Removing one of the forces acting on an object",
            "Splitting a single force into two perpendicular components",
        ],
        "correct_index": 3,
        "why": "Resolving is the reverse of finding a resultant: one force is "
               "replaced by two perpendicular forces with the same combined "
               "effect.",
    },
    {
        "id": "ks4-resolving-forces-s01",
        "subtopic_slug": "resolving-forces",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A sledge is pulled by a rope held at 30° to the horizontal "
                "with a force of 60 N. Calculate the horizontal component of "
                "the pull. (sin 30° = 0.500, cos 30° = 0.866)",
        "options": [
            "30.0 N",
            "52.0 N",
            "60.0 N",
            "69.3 N",
        ],
        "correct_index": 1,
        "why": "Fx = F cos θ = 60 × 0.866 = 52.0 N; using sine would give the "
               "vertical component instead.",
    },
    {
        "id": "ks4-resolving-forces-s02",
        "subtopic_slug": "resolving-forces",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A force of 45 N acts at 45° to the horizontal. Compare its "
                "horizontal and vertical components. "
                "(sin 45° = cos 45° = 0.707)",
        "options": [
            "The vertical component is the larger, at 63.6 N",
            "The horizontal component is the larger, at 45.0 N",
            "They are equal, at 22.5 N each",
            "They are equal, at 31.8 N each",
        ],
        "correct_index": 3,
        "why": "At 45° the sine and cosine are equal, so both components are "
               "45 × 0.707 = 31.8 N.",
    },
    {
        "id": "ks4-resolving-forces-s03",
        "subtopic_slug": "resolving-forces",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A force acting at 30° to the horizontal has a vertical "
                "component of 12 N. Determine the magnitude of the force. "
                "(sin 30° = 0.500, cos 30° = 0.866)",
        "options": [
            "24.0 N",
            "6.0 N",
            "13.9 N",
            "12.0 N",
        ],
        "correct_index": 0,
        "why": "Rearranging Fy = F sin θ gives F = 12 ÷ 0.500 = 24.0 N.",
    },
    {
        "id": "ks4-resolving-forces-s04",
        "subtopic_slug": "resolving-forces",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Two forces act at the same point on a bolt: 8.0 N due east "
                "and 15.0 N due north. Determine the magnitude of the "
                "resultant force.",
        "options": [
            "23.0 N",
            "7.0 N",
            "17.0 N",
            "11.5 N",
        ],
        "correct_index": 2,
        "why": "R = √(8.0² + 15.0²) = √289 = 17.0 N, since the two forces are "
               "already perpendicular components of the resultant.",
    },
    {
        "id": "ks4-resolving-forces-h01",
        "subtopic_slug": "resolving-forces",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A crate is pushed along a floor by a force of 200 N "
                "directed at 25° below the horizontal. Determine the "
                "component of that push acting vertically downwards. "
                "(sin 25° = 0.423, cos 25° = 0.906)",
        "options": [
            "181 N",
            "84.6 N",
            "200 N",
            "473 N",
        ],
        "correct_index": 1,
        "why": "The vertical component uses the sine of the angle to the "
               "horizontal: Fy = 200 × 0.423 = 84.6 N.",
    },
    {
        "id": "ks4-resolving-forces-h02",
        "subtopic_slug": "resolving-forces",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student resolves a 26 N force and states that its "
                "components are 24 N horizontally and 12 N vertically. "
                "Explain why these values must be wrong.",
        "options": [
            "They are not wrong, because the components add to 36 N, which "
            "is more than 26 N",
            "They are wrong because the vertical component must always be "
            "the larger of the two",
            "They are wrong because 24² + 12² = 720, which is not 26² = 676, "
            "as it must be",
            "They are wrong because a 26 N force cannot be resolved into "
            "whole-number components",
        ],
        "correct_index": 2,
        "why": "Perpendicular components must satisfy Fx² + Fy² = F², so "
               "Pythagoras is the check that catches a slip in the "
               "trigonometry.",
    },
    {
        "id": "ks4-resolving-forces-h03",
        "subtopic_slug": "resolving-forces",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A lamp of weight 40 N hangs at rest from two wires fixed to "
                "the ceiling, each wire making an angle of 60° to the "
                "vertical. Determine the tension in each wire. "
                "(sin 60° = 0.866, cos 60° = 0.500)",
        "options": [
            "20.0 N",
            "80.0 N",
            "34.6 N",
            "40.0 N",
        ],
        "correct_index": 3,
        "why": "The two vertical components must together balance the "
               "weight: 2 × T × cos 60° = 40, so T = 40 ÷ (2 × 0.500) = "
               "40.0 N.",
    },
    {
        "id": "ks4-resolving-forces-h04",
        "subtopic_slug": "resolving-forces",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A box of weight 150 N rests on a slope inclined at 20° to "
                "the horizontal. Determine the component of the box's weight "
                "acting down the slope. (sin 20° = 0.342, cos 20° = 0.940)",
        "options": [
            "51.3 N",
            "141 N",
            "150 N",
            "438 N",
        ],
        "correct_index": 0,
        "why": "The component of weight along a slope of angle θ is W sin θ = "
               "150 × 0.342 = 51.3 N; W cos θ is the component pressing into "
               "the slope.",
    },

    # ── free-body-diagrams  (HIGHER · TRIPLE ONLY) ──────────────────────
    {
        "id": "ks4-free-body-diagrams-e01",
        "subtopic_slug": "free-body-diagrams",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State which forces should be drawn on the free body diagram "
                "of an object.",
        "options": [
            "All the forces acting on that object",
            "All the forces that the object exerts on other objects",
            "Only the forces that are unbalanced",
            "Only the contact forces acting on the object",
        ],
        "correct_index": 0,
        "why": "A free body diagram isolates one object and shows every force "
               "the surroundings exert on it, balanced or not.",
    },
    {
        "id": "ks4-free-body-diagrams-e02",
        "subtopic_slug": "free-body-diagrams",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the direction in which the weight arrow is always "
                "drawn on a free body diagram.",
        "options": [
            "Perpendicular to the surface the object rests on",
            "Vertically downwards from the object's centre of mass",
            "Along the object's direction of motion",
            "Vertically upwards from the base of the object",
        ],
        "correct_index": 1,
        "why": "Weight is the Earth's pull on the object, so it always acts "
               "vertically downwards from the centre of mass, whatever the "
               "surface does.",
    },
    {
        "id": "ks4-free-body-diagrams-e03",
        "subtopic_slug": "free-body-diagrams",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what the length of each arrow on a free body diagram "
                "represents.",
        "options": [
            "The time for which the force acts",
            "The type of force",
            "The magnitude of the force",
            "The mass of the object",
        ],
        "correct_index": 2,
        "why": "Arrows are drawn to scale, so a force twice as large is drawn "
               "twice as long.",
    },
    {
        "id": "ks4-free-body-diagrams-e04",
        "subtopic_slug": "free-body-diagrams",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A ladder leans against a smooth vertical wall. State the "
                "direction of the force the wall exerts on the ladder.",
        "options": [
            "Vertically upwards, helping to support the ladder's weight",
            "Down along the ladder, in the direction the ladder points",
            "Vertically downwards, adding to the ladder's weight",
            "Horizontally, at right angles to the face of the wall",
        ],
        "correct_index": 3,
        "why": "A normal contact force is always perpendicular to the surface "
               "producing it, and this surface is vertical.",
    },
    {
        "id": "ks4-free-body-diagrams-s01",
        "subtopic_slug": "free-body-diagrams",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A crate is dragged at a constant velocity across a rough "
                "horizontal floor by a horizontal rope. Which statement "
                "about its free body diagram is correct?",
        "options": [
            "The rope tension is larger than the friction, because the crate "
            "is moving",
            "The rope tension equals the friction, and the weight equals the "
            "normal contact force",
            "Only the tension and the weight need to be shown on the diagram",
            "The friction is larger than the tension, because the floor is "
            "rough",
        ],
        "correct_index": 1,
        "why": "Constant velocity means the resultant is zero in both "
               "directions, so the horizontal pair balance and the vertical "
               "pair balance.",
    },
    {
        "id": "ks4-free-body-diagrams-s02",
        "subtopic_slug": "free-body-diagrams",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A helium balloon rises at a steady speed through still air. "
                "Determine which set of forces should appear on its free "
                "body diagram.",
        "options": [
            "Upthrust upwards, weight downwards and drag downwards, with the "
            "upthrust equal to the other two together",
            "Upthrust upwards and weight downwards only, with the upthrust "
            "larger, which is what makes it rise",
            "Weight downwards only, because a balloon rising through still "
            "air has no other forces on it",
            "Upthrust upwards, weight downwards and drag upwards, with all "
            "three of them equal in size",
        ],
        "correct_index": 0,
        "why": "Drag always opposes motion, so for a rising balloon it acts "
               "downwards, and steady speed means the upthrust balances "
               "weight and drag together.",
    },
    {
        "id": "ks4-free-body-diagrams-s03",
        "subtopic_slug": "free-body-diagrams",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A car of weight 12 000 N travels along a level road. Its "
                "engine provides a forward force of 3000 N and the total "
                "resistive force is 3000 N. Determine the resultant vertical "
                "force and the resultant horizontal force on the car.",
        "options": [
            "Vertical 12 000 N downwards; horizontal 0 N",
            "Vertical 0 N; horizontal 3000 N forwards",
            "Vertical 0 N; horizontal 0 N",
            "Vertical 12 000 N downwards; horizontal 6000 N forwards",
        ],
        "correct_index": 2,
        "why": "The road's normal contact force balances the weight and the "
               "resistive force balances the driving force, so both "
               "resultants are zero.",
    },
    {
        "id": "ks4-free-body-diagrams-s04",
        "subtopic_slug": "free-body-diagrams",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A box of mass 5.0 kg hangs at rest from a single vertical "
                "rope. Determine the tension in the rope. (g = 9.8 N/kg)",
        "options": [
            "5.0 N",
            "0.51 N",
            "98 N",
            "49 N",
        ],
        "correct_index": 3,
        "why": "At rest the tension must balance the weight, so T = W = "
               "5.0 × 9.8 = 49 N.",
    },
    {
        "id": "ks4-free-body-diagrams-h01",
        "subtopic_slug": "free-body-diagrams",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student draws a free body diagram of a car and includes "
                "an arrow labelled 'the force of the car on the road'. "
                "Explain what is wrong with this.",
        "options": [
            "Nothing is wrong, because the force of the car on the road also "
            "acts on the car itself",
            "That force acts on the road, not on the car, so it does not "
            "belong on this diagram",
            "The arrow is correct but should be drawn twice as long as the "
            "car's weight arrow",
            "The force of the car on the road is not a real force and so "
            "cannot be drawn",
        ],
        "correct_index": 1,
        "why": "A free body diagram shows only forces exerted ON the chosen "
               "object; the equal and opposite partner acts on the other "
               "object.",
    },
    {
        "id": "ks4-free-body-diagrams-h02",
        "subtopic_slug": "free-body-diagrams",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A ball is thrown vertically upwards and is momentarily at "
                "rest at the top of its flight. Air resistance is "
                "negligible. Determine which forces should appear on its "
                "free body diagram at that instant.",
        "options": [
            "Weight downwards only",
            "Weight downwards and an upward 'throwing force' of equal size",
            "No forces at all, because the ball is momentarily at rest",
            "An upward force larger than the weight, which is what made the "
            "ball rise",
        ],
        "correct_index": 0,
        "why": "The hand stopped acting on the ball the moment it was "
               "released, so gravity is the only force still acting on it.",
    },
    {
        "id": "ks4-free-body-diagrams-h03",
        "subtopic_slug": "free-body-diagrams",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A sledge of mass 25 kg is pulled along level ground at a "
                "constant velocity by a rope held at 40° to the horizontal "
                "with a tension of 90 N. Determine the normal contact force "
                "from the ground on the sledge. (g = 9.8 N/kg, "
                "sin 40° = 0.643, cos 40° = 0.766)",
        "options": [
            "245 N",
            "303 N",
            "187 N",
            "176 N",
        ],
        "correct_index": 2,
        "why": "The rope lifts with 90 × 0.643 = 57.9 N, so the ground only "
               "needs to supply 245 − 57.9 = 187 N to balance the weight.",
    },
    {
        "id": "ks4-free-body-diagrams-h04",
        "subtopic_slug": "free-body-diagrams",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A crate on a horizontal floor is in equilibrium under three "
                "horizontal forces: 30 N due east, 40 N due north and one "
                "unknown force. Determine the unknown force.",
        "options": [
            "70 N, opposite in direction to the resultant of the other two",
            "50 N, in the same direction as the resultant of the other two",
            "10 N, opposite in direction to the resultant of the other two",
            "50 N, exactly opposite in direction to the resultant of the "
            "other two",
        ],
        "correct_index": 3,
        "why": "The first two forces give a resultant of √(30² + 40²) = 50 N, "
               "so equilibrium needs a third force of 50 N pointing the "
               "opposite way.",
    },
]
