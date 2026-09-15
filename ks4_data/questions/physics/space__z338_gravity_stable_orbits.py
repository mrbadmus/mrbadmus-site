"""Physics · Space — `gravity-stable-orbits`, the MRB-338 expansion.

Higher tier, Triple only. The leaf arrived with twelve rows: the direction of
the centripetal force, the changing velocity, the low-orbit speed, the
definition of escape velocity, the straight line a satellite would fly if
gravity vanished, the single geostationary altitude, two 2πr calculations,
the counter-intuitive catch-up burn, the work-done argument and the black
hole. What it did not carry is the rest of the HT spec point itself — that a
stable orbit has exactly ONE speed for each radius, and therefore what
happens when the speed is changed either way — nor anything about the
atmosphere that makes low orbits decay, nor free fall, nor how the field of a
different body changes the numbers.

The split is 14 / 14 / 14 because all three bands started at four and the
material divides cleanly: recall of the radius–speed–period relations and the
maintenance facts at `easier`; the two directions of a speed change, free
fall, decay rates and the Moon's weaker field at `standard`; and at `harder`
the rearranged calculations, the mass-independence of orbital speed, and four
claims to evaluate (the "no force acts" claim, the hovering geostationary
satellite, the Moon falling towards us, and a star orbiting something
invisible).

⚠️ Written deliberately AROUND the lesson page's two printed tasks — what
eventually becomes of a low satellite slowed by drag, and why a geostationary
satellite appears stationary. The decay material here asks for the CAUSE
(e13), the MAINTENANCE (e14), the RATE (s14), the floor on altitude (s18) and
the effect on the period (h17); none of them asks for the outcome the page
prints with its answer.
"""

TOPIC = "space"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-gravity-stable-orbits-e05",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what happens to the gravitational force between two "
                "masses as the distance between them increases.",
        "options": [
            "It stays the same",
            "It increases",
            "It becomes a repulsive force instead of an attractive one",
            "It decreases",
        ],
        "correct_index": 3,
        "why": "Gravitational attraction falls off as separation grows, which "
               "is why a satellite in a high orbit is held less strongly than "
               "one in a low orbit.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e06",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the strength of the Earth's gravitational field at the "
                "altitude of a geostationary orbit, compared with its strength "
                "at the surface.",
        "options": [
            "Weaker, but never zero",
            "Exactly zero",
            "Stronger than at the surface",
            "Exactly the same",
        ],
        "correct_index": 0,
        "why": "The field weakens with height but never switches off; at "
               "36 000 km it is still strong enough to hold a satellite in "
               "orbit.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e07",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the force that provides the centripetal force for a "
                "satellite in orbit around the Earth.",
        "options": [
            "The push of the solar wind",
            "The thrust of its own engines",
            "The gravitational attraction of the Earth",
            "Air resistance acting on its solar panels",
        ],
        "correct_index": 2,
        "why": "For any orbit it is gravity that supplies the centre-seeking "
               "force; nothing else is acting on a satellite in a vacuum.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e08",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the direction in which a satellite in a circular orbit "
                "is accelerating.",
        "options": [
            "Along its path, in the direction it is travelling",
            "Towards the centre of its orbit",
            "Away from the centre of its orbit",
            "It is not accelerating, because its speed stays constant",
        ],
        "correct_index": 1,
        "why": "Acceleration is in the same direction as the resultant force, "
               "and for an orbit that force is gravity, pointing at the centre.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e09",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite's speed is increased while it is at a given "
                "orbital radius. State where it ends up.",
        "options": [
            "In a smaller orbit, closer to the Earth than before",
            "In the same orbit, travelling round it more quickly than before",
            "On a straight path away from the Earth, leaving orbit altogether",
            "In a larger orbit",
        ],
        "correct_index": 3,
        "why": "Too fast for the gravity available at that radius, the "
               "satellite moves outwards to a larger orbit where the stable "
               "speed is lower.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e10",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by the orbital period of a satellite.",
        "options": [
            "The length of time the satellite is expected to keep working for",
            "The time it takes to complete one orbit",
            "The distance it travels in one orbit",
            "The number of orbits it completes in a single day",
        ],
        "correct_index": 1,
        "why": "The period is a time: one full trip around the orbit, 90 "
               "minutes in a low orbit and 24 hours for a geostationary one.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e11",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what happens to the speed needed for a stable circular "
                "orbit as the radius of that orbit gets larger.",
        "options": [
            "The speed needed gets larger",
            "The speed needed stays the same",
            "The speed needed gets smaller",
            "No stable speed exists that far out",
        ],
        "correct_index": 2,
        "why": "Gravity is weaker further out, so less speed is needed to "
               "balance it: 7700 m/s in a low orbit against 3000 m/s at "
               "geostationary height.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e12",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by a centripetal force.",
        "options": [
            "A force that pushes an object outwards as it turns a corner",
            "The resultant force that always acts towards the centre of the "
            "circle",
            "A force that acts along the direction an object is travelling in",
            "A force that only ever acts between two objects in contact",
        ],
        "correct_index": 1,
        "why": "Centripetal means centre-seeking: it is the name for whatever "
               "resultant force holds a body on a circular path, which for an "
               "orbit is gravity.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e13",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what causes the orbit of a satellite a few hundred "
                "kilometres up to change over a period of years.",
        "options": [
            "The pull of the Moon",
            "The thin air still present at that height",
            "The pressure of sunlight",
            "The Earth's magnetic field",
        ],
        "correct_index": 1,
        "why": "There is still a trace of atmosphere in low orbit, and the drag "
               "it causes gradually slows the satellite.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e14",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what a satellite in a low orbit must do if it is to stay "
                "in that orbit for many years.",
        "options": [
            "Keep its solar panels edge-on to the direction of travel",
            "Spin about its own axis",
            "Nothing, because a low orbit keeps its size",
            "Fire its engines from time to time",
        ],
        "correct_index": 3,
        "why": "Drag keeps taking speed away, so the satellite needs "
               "occasional burns to put that speed back and hold its altitude.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e15",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what happens to a satellite's orbital period when it is "
                "moved to an orbit of larger radius.",
        "options": [
            "The period gets shorter",
            "The period is unchanged, because every satellite of the Earth has "
            "the same period",
            "The period gets longer",
            "The period becomes zero, because the satellite then stays above "
            "one point on the ground",
        ],
        "correct_index": 2,
        "why": "A larger orbit is a longer path travelled at a lower speed, so "
               "the time for one orbit rises on both counts.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e16",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State what is meant by a stable orbit.",
        "options": [
            "An orbit in which the forces on the satellite are balanced, so "
            "there is no resultant force",
            "An orbit in which gravity supplies exactly the centripetal force "
            "needed at that radius and speed",
            "An orbit in which the satellite's engines run continuously to hold "
            "it at a fixed height",
            "An orbit in which the satellite is far enough out for gravity to "
            "have no effect on it",
        ],
        "correct_index": 1,
        "why": "Stability is a match: the gravitational pull available at that "
               "radius is exactly the centre-seeking force the speed requires.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e17",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State how the escape velocity of a planet depends on its mass.",
        "options": [
            "A more massive planet has a lower escape velocity",
            "Escape velocity is the same for every planet, since it is a "
            "property of space and not of the planet",
            "Escape velocity depends on how fast the planet spins rather than "
            "on how much mass it contains",
            "A more massive planet has a higher escape velocity",
        ],
        "correct_index": 3,
        "why": "More mass means a stronger gravitational field, so a greater "
               "speed is needed to get clear of it.",
    },
    {
        "id": "ks4-gravity-stable-orbits-e18",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State which quantity is greater for a satellite in a low orbit "
                "than for one in a geostationary orbit.",
        "options": [
            "The period of its orbit",
            "Its distance from the centre of the Earth",
            "Its orbital speed",
            "The time it takes for a radio signal from it to reach the ground",
        ],
        "correct_index": 2,
        "why": "The low satellite is the faster one — about 7700 m/s against "
               "3000 m/s — while its period, its radius and its signal delay "
               "are all smaller.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-gravity-stable-orbits-s05",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite in a circular orbit is slowed slightly by a "
                "backward burn of its engines. Predict what happens to its "
                "orbit.",
        "options": [
            "It rises to an orbit of larger radius, because slowing down means "
            "gravity has less work to do on it",
            "It stays in the same orbit, because gravity restores the lost "
            "speed",
            "It drops vertically to the ground",
            "It falls to an orbit of smaller radius",
        ],
        "correct_index": 3,
        "why": "At the lower speed gravity is more than the centripetal force "
               "required, so the excess pull draws the satellite into a smaller "
               "orbit.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s06",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why the one stable speed for a small orbit is greater "
                "than the one stable speed for a large orbit.",
        "options": [
            "The satellite is closer to the air, which pushes it along faster",
            "A small orbit is a shorter path, so it is travelled more quickly",
            "The Earth spins beneath the satellite, and its rotation drags "
            "nearby satellites along",
            "Gravity is stronger closer in, so a greater speed is needed to "
            "balance it",
        ],
        "correct_index": 3,
        "why": "The stable speed is whatever makes the required centripetal "
               "force equal to the gravitational pull available, and that pull "
               "is larger at a smaller radius.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s07",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite goes once round a circular orbit of radius "
                "1.0 × 10⁷ m in 10 000 s. Taking the circumference as 2πr, "
                "calculate its orbital speed.",
        "options": [
            "1000 m/s",
            "3140 m/s",
            "6280 m/s",
            "12 600 m/s",
        ],
        "correct_index": 2,
        "why": "2π × 1.0 × 10⁷ = 6.28 × 10⁷ m, and 6.28 × 10⁷ ÷ 10 000 = "
               "6280 m/s.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s08",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why an astronaut inside a space station appears to "
                "float, even though the Earth's gravitational field there is "
                "almost as strong as it is at the ground.",
        "options": [
            "The astronaut and the station are falling together, so the "
            "astronaut does not press on the floor",
            "The station spins, and spinning cancels out the pull of gravity "
            "on anything inside it",
            "The air inside the station is pressurised, and that pressure holds "
            "the astronaut up against gravity",
            "The astronaut's weight is carried by the station's walls, leaving "
            "the astronaut with no weight of their own",
        ],
        "correct_index": 0,
        "why": "Both are in free fall around the Earth with the same "
               "acceleration, so there is no contact force between astronaut "
               "and floor — the sensation people call weightlessness.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s09",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite in low orbit is given a large increase in speed by "
                "its engines. Describe the orbit it settles into and the speed "
                "it travels at there.",
        "options": [
            "A larger orbit, travelling more slowly than it did before",
            "A larger orbit, travelling faster than it did before",
            "A smaller orbit, travelling faster than it did before",
            "The same orbit as before, but now travelling at two different "
            "speeds on opposite sides of the Earth",
        ],
        "correct_index": 0,
        "why": "The burn lifts it outwards, and the stable speed in the larger "
               "orbit is lower than the speed it started with — the result "
               "that surprises everybody.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s10",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A weather satellite maintains a circular orbit of radius "
                "2.0 × 10⁷ m at a constant speed of 4000 m/s. Using 2πr for "
                "the orbit's circumference, find how long it takes to "
                "complete one full orbit.",
        "options": [
            "5000 s",
            "31 400 s",
            "15 700 s",
            "80 000 s",
        ],
        "correct_index": 1,
        "why": "2π × 2.0 × 10⁷ = 1.26 × 10⁸ m, and 1.26 × 10⁸ ÷ 4000 = "
               "31 400 s.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s11",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a geostationary satellite keeps its altitude for "
                "decades while a satellite a few hundred kilometres up does "
                "not.",
        "options": [
            "A geostationary satellite runs its engines continuously, and a low "
            "satellite has no engines of its own",
            "Gravity does not reach as far as 36 000 km, so nothing can pull "
            "it down",
            "A geostationary satellite is heavier, and a heavier satellite is "
            "harder to slow",
            "There is no appreciable atmosphere at 36 000 km, so nothing slows "
            "the geostationary satellite",
        ],
        "correct_index": 3,
        "why": "Orbital decay is caused by drag from the residual atmosphere, "
               "and at geostationary height there is effectively none.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s12",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "The escape velocity of the Moon is 2.4 km/s and that of the "
                "Earth is 11.2 km/s. Explain what this comparison tells you "
                "about the two bodies.",
        "options": [
            "The Moon's gravitational field is much weaker than the Earth's, "
            "because the Moon has far less mass",
            "The Moon is moving away from the Earth, so less speed is needed to "
            "leave it behind",
            "The Moon has no atmosphere, so there is nothing to slow a "
            "spacecraft down as it leaves",
            "The Moon is closer to the Sun, whose gravity helps a spacecraft "
            "away once it has left the surface",
        ],
        "correct_index": 0,
        "why": "Escape velocity measures how firmly a body holds on to things "
               "at its surface, and the Moon's much smaller mass makes a much "
               "weaker field.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s13",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "The radius of a satellite's circular orbit is doubled. "
                "Describe what happens to its orbital speed and to its period.",
        "options": [
            "The speed rises and the period gets shorter",
            "The speed falls and the period gets shorter as well",
            "The speed and the period are both unchanged, because the satellite "
            "still orbits the same planet",
            "The speed falls and the period gets longer",
        ],
        "correct_index": 3,
        "why": "Gravity is weaker at the larger radius so the stable speed "
               "drops, and the path round is longer as well — both make the "
               "period longer.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s14",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why the orbit of a satellite at 300 km changes more "
                "quickly than the orbit of one at 1500 km.",
        "options": [
            "The Earth's field is weaker at 300 km, so the orbit is held less "
            "firmly",
            "There is more air left at 300 km, so the drag on the satellite "
            "there is greater",
            "The satellite at 300 km travels more slowly and is pulled down "
            "sooner",
            "The satellite at 300 km is nearer the equator, where the Earth "
            "bulges outwards towards it",
        ],
        "correct_index": 1,
        "why": "The atmosphere thins out with height, so a lower satellite "
               "meets more gas each second and loses speed faster.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s15",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A geostationary satellite has an orbital radius of "
                "4.2 × 10⁷ m and a period of 86 400 s. Taking the "
                "circumference as 2πr, determine its orbital speed.",
        "options": [
            "490 m/s",
            "1500 m/s",
            "3100 m/s",
            "7700 m/s",
        ],
        "correct_index": 2,
        "why": "2π × 4.2 × 10⁷ = 2.64 × 10⁸ m, and 2.64 × 10⁸ ÷ 86 400 = about "
               "3100 m/s.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s16",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare what the orbital speed of a spacecraft does with what "
                "its escape velocity does.",
        "options": [
            "Orbital speed keeps it circling the Earth; escape velocity is the "
            "greater speed that takes it out of the field",
            "Orbital speed is the speed it reaches on re-entry; escape velocity "
            "is the speed it left the launch pad at",
            "Orbital speed is measured relative to the ground; escape velocity "
            "is the same speed measured relative to the Sun",
            "Orbital speed is the fastest it may travel in orbit; escape "
            "velocity is the slowest it may travel there",
        ],
        "correct_index": 0,
        "why": "One holds a craft on a curved path around the Earth; the other "
               "is the minimum speed for leaving the Earth's gravitational "
               "field behind.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s17",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A probe is launched away from the Earth at 15 km/s, which is "
                "above the Earth's escape velocity. Predict what happens to it.",
        "options": [
            "It leaves the Earth's gravitational field and never comes back",
            "It rises, stops, and is pulled back down to the ground",
            "It settles into a circular orbit at the height where it slows "
            "enough",
            "It burns up, because nothing can travel faster than the escape "
            "velocity of the planet it leaves",
        ],
        "correct_index": 0,
        "why": "Above escape velocity the probe has more than enough speed to "
               "get clear of the field, so gravity slows it without ever "
               "stopping it.",
    },
    {
        "id": "ks4-gravity-stable-orbits-s18",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a satellite cannot be left in orbit at an altitude "
                "of 50 km, even if it is given exactly the right speed for that "
                "radius.",
        "options": [
            "The air at 50 km is thick enough to slow it very quickly, so the "
            "orbit collapses almost at once",
            "Gravity is too strong at 50 km for any orbit to exist, whatever "
            "speed the satellite is given",
            "There is no speed that gives a stable orbit at such a small "
            "radius, so the satellite must fall",
            "At 50 km the satellite would be inside the Earth's magnetic field, "
            "which would pull it off course",
        ],
        "correct_index": 0,
        "why": "Orbit needs a near-vacuum: at 50 km the atmosphere still has "
               "enough density to strip the satellite's speed away in minutes.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-gravity-stable-orbits-h05",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A moon orbits its planet once every 1.2 × 10⁵ s, moving at "
                "a constant 2000 m/s along its circular path. Given that the "
                "orbit's circumference equals 2πr, work out the orbit's "
                "radius.",
        "options": [
            "2.4 × 10⁸ m",
            "3.8 × 10⁷ m",
            "7.6 × 10⁷ m",
            "6.0 × 10¹ m",
        ],
        "correct_index": 1,
        "why": "The path length is 2000 × 1.2 × 10⁵ = 2.4 × 10⁸ m, and dividing "
               "that circumference by 2π gives r = 3.8 × 10⁷ m.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h06",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Two satellites are in circular orbits of the same radius, but "
                "one has twice the mass of the other. Compare the orbital "
                "speeds they need.",
        "options": [
            "The heavier one needs the greater speed",
            "The lighter one needs the greater speed",
            "They need the same speed",
            "The heavier one cannot orbit at that radius",
        ],
        "correct_index": 2,
        "why": "A greater mass needs a proportionally greater centripetal force "
               "and receives a proportionally greater gravitational pull, so "
               "the stable speed at a given radius is the same for both.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h07",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student writes: 'A satellite going round a circular orbit at "
                "a steady speed has no resultant force acting on it.' Evaluate "
                "this statement.",
        "options": [
            "Correct, because a steady speed means the forces on the satellite "
            "must be balanced",
            "Correct, because gravity is cancelled out by the satellite's "
            "forward motion through space",
            "Wrong — there is always a resultant force towards the centre, and "
            "that is what turns the satellite",
            "Wrong — the resultant force acts along the direction of travel, "
            "which is what keeps the satellite moving",
        ],
        "correct_index": 2,
        "why": "The direction of motion is changing, so the satellite is "
               "accelerating and there must be a resultant force; it is "
               "gravity, and it points at the centre.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h08",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A spacecraft in a circular orbit 100 km above the Moon needs a "
                "speed of about 1600 m/s. Explain why a spacecraft 100 km above "
                "the Earth would need a far greater speed.",
        "options": [
            "The Earth's mass is far greater, so its gravitational field at "
            "that height is much stronger",
            "The Earth turns on its axis and the Moon does not",
            "The Earth's atmosphere at that height pushes a spacecraft "
            "backwards",
            "The Earth is further from the Sun, whose gravity would otherwise "
            "help to hold the spacecraft in its orbit",
        ],
        "correct_index": 0,
        "why": "The stable speed matches the gravitational pull available, and "
               "the Earth is about eighty times the Moon's mass, so its field "
               "demands a much higher speed.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h09",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite is placed in a circular orbit above the equator "
                "with a period of 24 hours, but travelling in the opposite "
                "direction to the Earth's rotation. Deduce what would be seen "
                "from the ground.",
        "options": [
            "It would appear fixed above one point, because its period is "
            "24 hours",
            "It would cross the sky about twice a day, because its motion and "
            "the Earth's rotation add together",
            "It would appear to drift slowly westwards, taking about a month "
            "to work its way round the sky",
            "It would leave orbit within a day, because a satellite cannot "
            "orbit against the Earth's spin",
        ],
        "correct_index": 1,
        "why": "Relative to the ground the satellite's angular motion and the "
               "Earth's rotation add rather than cancel, so it works its way "
               "round the sky roughly twice in each 24 hours.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h10",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite completes 5 orbits of radius 8.0 × 10⁶ m in "
                "3.6 × 10⁴ s. Taking the circumference of one orbit as 2πr, "
                "determine its orbital speed.",
        "options": [
            "1400 m/s",
            "7000 m/s",
            "1110 m/s",
            "35 000 m/s",
        ],
        "correct_index": 1,
        "why": "One orbit is 2π × 8.0 × 10⁶ = 5.03 × 10⁷ m, so five are "
               "2.51 × 10⁸ m, and 2.51 × 10⁸ ÷ 3.6 × 10⁴ = about 7000 m/s — "
               "which is the one stable speed an orbit of that radius has.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h11",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Evaluate this statement: 'The Moon is falling towards the "
                "Earth.'",
        "options": [
            "It is true — the Moon accelerates towards the Earth continuously, "
            "but its sideways motion keeps it in orbit",
            "It is false, because the Moon is in orbit and an orbiting body is "
            "not falling",
            "It is false, because the Earth's gravity is too weak at that "
            "distance to pull on the Moon",
            "It is true, and the Moon will reach the Earth's surface once its "
            "orbit has finished decaying",
        ],
        "correct_index": 0,
        "why": "Gravity accelerates the Moon towards the Earth the whole time; "
               "because it is also travelling sideways, the fall curves into an "
               "orbit rather than closing the distance.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h12",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Astronomers watch a star moving round a very small orbit at an "
                "enormous speed, with nothing visible at the centre of that "
                "orbit. Suggest what lies at the centre, and why.",
        "options": [
            "Nothing, because a star can orbit an empty point in space if it "
            "is spinning quickly enough",
            "A cloud of cold gas, because gas is invisible and spreads its mass "
            "over a large volume of space",
            "Another star exactly like the first one, because two stars of "
            "equal mass orbit an empty centre",
            "A very dense object such as a black hole, because a small fast "
            "orbit needs a very strong field",
        ],
        "correct_index": 3,
        "why": "A small radius combined with a high speed requires a very large "
               "centripetal force, so the unseen mass must be both great and "
               "extremely compact.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h13",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Suggest why a probe that is to leave the Solar System "
                "altogether must reach a speed greater than the Earth's escape "
                "velocity.",
        "options": [
            "It has to travel faster than the Earth does in its own orbit",
            "It has to escape the Sun's gravitational field as well as the "
            "Earth's",
            "It has to carry fuel enough to run its engines the whole way out",
            "It has to reach the speed of light",
        ],
        "correct_index": 1,
        "why": "Escaping the Earth only frees the probe into orbit around the "
               "Sun; leaving the Solar System means climbing out of the Sun's "
               "much deeper field too.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h14",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A satellite's circular orbit has a circumference of "
                "1.67 × 10⁸ m and the satellite travels at 3900 m/s. Determine "
                "its orbital period in hours.",
        "options": [
            "1.2 hours",
            "6.0 hours",
            "12 hours",
            "24 hours",
        ],
        "correct_index": 2,
        "why": "1.67 × 10⁸ ÷ 3900 = 4.28 × 10⁴ s, and 4.28 × 10⁴ ÷ 3600 is "
               "about 12 hours — the orbit a navigation satellite uses.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h15",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "An astronaut releases a spanner while working outside a space "
                "station in orbit. Predict what the spanner does, and explain "
                "why.",
        "options": [
            "It falls straight down to the Earth as soon as it is let go",
            "It flies off into space, with nothing left to hold it",
            "It stops moving and is left behind, because the station carries on "
            "and the spanner does not",
            "It stays alongside the station, because it already has the "
            "station's orbital speed",
        ],
        "correct_index": 3,
        "why": "The spanner is in the same orbit at the same speed, so it "
               "carries on round with the station — it is in free fall exactly "
               "as the station is.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h16",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A geostationary satellite is found to be drifting slowly away "
                "from the longitude it should sit above. Suggest what a "
                "controller must do, and why that works.",
        "options": [
            "Fire the thrusters briefly to adjust its speed, which changes its "
            "radius and so its period",
            "Fire the thrusters continuously so that the satellite is pushed "
            "back to the longitude it should be above",
            "Turn the satellite to face a different direction, which alters the "
            "pull of gravity on it",
            "Wait, because the Earth's rotation will carry the satellite back "
            "to the right longitude within a day",
        ],
        "correct_index": 0,
        "why": "Drift means the period is no longer exactly 24 hours; a small "
               "speed change moves the satellite to the radius whose period "
               "matches the Earth's rotation again.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h17",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Deduce what happens to the orbital period of a space station "
                "as drag slowly reduces the radius of its orbit.",
        "options": [
            "The period gets longer, because the station has lost speed to the "
            "drag acting on it",
            "The period is unchanged, because the period of an orbit depends "
            "only on the mass of the Earth",
            "The period gets longer at first and then shorter, because the "
            "drag force reverses as the station drops",
            "The period gets shorter, because the path is shorter and the "
            "stable speed there is higher",
        ],
        "correct_index": 3,
        "why": "A smaller orbit has both a shorter circumference and a higher "
               "stable speed, so the time for one orbit falls.",
    },
    {
        "id": "ks4-gravity-stable-orbits-h18",
        "subtopic_slug": "gravity-stable-orbits",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Measurements show that the radius of the Moon's orbit is "
                "increasing by about 4 cm each year. Deduce what is happening "
                "to its orbital speed and to its period.",
        "options": [
            "The speed is rising very slowly and the period is getting shorter",
            "The speed is falling very slowly while the period stays exactly "
            "the same as it was",
            "The speed is falling very slowly and the period is getting longer",
            "The speed and the period are both rising, because a larger orbit "
            "means both a longer path and a faster journey",
        ],
        "correct_index": 2,
        "why": "A larger radius means weaker gravity and so a lower stable "
               "speed, and the path round is longer as well, so each orbit "
               "takes a little more time.",
    },
]
