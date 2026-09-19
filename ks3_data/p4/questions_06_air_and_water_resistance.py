"""P4 lesson 06 — Air and water resistance: twelve questions (MRB-223).

Written against Design's page. The skydiver, the fall bench and the
four-stage strip are hers.

The discriminations, in the order the lesson builds them:

  · resistance acts against the motion and GROWS with speed
    (`FORCE-33`);
  · a bigger area facing the flow means more resistance;
  · terminal velocity is a BALANCE, not a limit (`FORCE-35`);
  · an upward resultant means slowing, not rising (`FORCE-34`) — the
    harder band sits here;
  · what decides which of two objects falls faster is the balance
    between weight and resistance, not the weight (`FORCE-32`).

⚠️ POSITION IS AUTHORED — index cycles 1, 3, 0, 2, giving three of each.

⚠️ Rung 1 (the 1 N hailstone) and Rung 2 (the lead and plastic balls) are
NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "air-and-water-resistance"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-06-e01",
        "band": "easier",
        "text": "Air resistance on a falling object acts…",
        "options": [
            {"text": "downwards, adding to the weight", "correct": False,
             "why": "It acts AGAINST the motion. A falling object is going "
                    "down, so the resistance pushes up."},
            {"text": "upwards, against the motion", "correct": True},
            {"text": "sideways", "correct": False,
             "why": "It acts along the line of travel, opposing it."},
            {"text": "only once the object is falling fast", "correct": False,
             "why": "It acts at any speed above zero. It is simply very "
                    "small at low speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e02",
        "band": "easier",
        "text": "What happens to air resistance as an object falls faster?",
        "options": [
            {"text": "It stays the same", "correct": False,
             "why": "Then a falling object would never stop speeding up, and "
                    "skydivers would not survive."},
            {"text": "It gets smaller", "correct": False,
             "why": "Faster means more air shoved aside every second, so it "
                    "gets bigger."},
            {"text": "It disappears", "correct": False,
             "why": "The opposite. It grows until it can match the weight."},
            {"text": "It gets bigger", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e03",
        "band": "easier",
        "text": "A skydiver has stopped getting any faster. What is the "
                "resultant force on them?",
        "options": [
            {"text": "0 N", "correct": True},
            {"text": "750 N downwards", "correct": False,
             "why": "That is their weight alone, which would mean the "
                    "resistance was zero and they were still speeding up."},
            {"text": "750 N upwards", "correct": False,
             "why": "That is the resistance alone. The weight is still "
                    "acting and cancels it."},
            {"text": "It cannot be worked out without the speed.",
             "correct": False,
             "why": "“Stopped getting faster” is enough: no change means "
                    "nothing left over."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e04",
        "band": "easier",
        "text": "Why is a parachute made large?",
        "options": [
            {"text": "To make the skydiver weigh less", "correct": False,
             "why": "The weight is unchanged. What changes is the force "
                    "resisting the fall."},
            {"text": "To catch the wind and lift the skydiver upwards, so "
                     "that the fall turns into a rise",
             "correct": False,
             "why": "Nobody goes up. The canopy slows the fall; it does not "
                    "reverse it."},
            {"text": "To present a much bigger area to the air, which gives "
                     "far more resistance", "correct": True},
            {"text": "To make the skydiver more streamlined",
             "correct": False,
             "why": "The opposite — a canopy is designed to be as UN"
                    "streamlined as possible."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-06-s01",
        "band": "standard",
        "text": "A skydiver steps out of the aircraft and is barely moving. "
                "What is the air resistance at that instant?",
        "options": [
            {"text": "The same as their weight", "correct": False,
             "why": "Then the fall would never begin. The resistance has to "
                    "grow first."},
            {"text": "Close to 0 N", "correct": True},
            {"text": "Bigger than their weight", "correct": False,
             "why": "That would push them back up before they had started to "
                    "fall."},
            {"text": "Exactly half their weight", "correct": False,
             "why": "There is no such rule, and at almost no speed almost no "
                    "air is being pushed aside."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s02",
        "band": "standard",
        "text": "A skydiver changes from spread-out to head-down. What "
                "happens to their terminal velocity?",
        "options": [
            {"text": "It falls, because a head-down skydiver weighs less "
                     "than a spread-out one",
             "correct": False,
             "why": "Their weight is exactly the same in either posture."},
            {"text": "It stays the same, because weight is what sets it and "
                     "that has not changed", "correct": False,
             "why": "The weight has not changed, but the AREA facing the "
                    "flow has, so the balance point moves."},
            {"text": "It cannot change without a parachute, because posture "
                     "does not set it",
             "correct": False,
             "why": "Posture alone changes it — from about 55 m/s to "
                    "about 80 m/s."},
            {"text": "It rises, because a smaller area means less resistance "
                     "at any given speed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s03",
        "band": "standard",
        "text": "A car with the accelerator flat to the floor stops speeding "
                "up at its top speed. Why?",
        "options": [
            {"text": "The engine has run out of force.", "correct": False,
             "why": "The engine is still working just as hard. What has "
                    "changed is what it is up against."},
            {"text": "The backwards forces have grown until they match the "
                     "forward force, so the resultant is 0 N.",
             "correct": True},
            {"text": "There is a legal limit built into the car.",
             "correct": False,
             "why": "Some cars have one, but the physics reason is about "
                    "forces, not about a limiter."},
            {"text": "The car has reached the fastest speed anything can "
                     "travel, which is fixed and the same for everything", "correct": False,
             "why": "It is this car's balance point, not a universal limit. "
                    "A more powerful car settles higher."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s04",
        "band": "standard",
        "text": "Why does a swimmer at 2 m/s feel more resistance than a "
                "runner at 4 m/s?",
        "options": [
            {"text": "Because swimming uses more muscles.", "correct": False,
             "why": "The question is about the force from the fluid, not "
                    "about effort."},
            {"text": "Because water is much denser than air — a cubic metre "
                     "of it has around eight hundred times the mass.",
             "correct": True},
            {"text": "Because water resistance does not depend on speed, so "
                     "it is the same however fast you go",
             "correct": False,
             "why": "It does, exactly as air resistance does. The difference "
                    "is what is being shoved aside."},
            {"text": "Because a swimmer is bigger than a runner.",
             "correct": False,
             "why": "They are the same person. Only the fluid has changed."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-06-h01",
        "band": "harder",
        "text": "The moment a parachute opens, the resultant force points "
                "UPWARDS. What is the skydiver doing?",
        "options": [
            {"text": "Rising, because the resultant is upwards.",
             "correct": False,
             "why": "An upward resultant means the DOWNWARD motion is "
                    "changing, which here means slowing. Nobody goes up."},
            {"text": "Falling, and slowing down hard.", "correct": True},
            {"text": "Hanging still in the air.", "correct": False,
             "why": "Still would need a resultant of 0 N. There is a large "
                    "one."},
            {"text": "Falling at exactly the same speed as before.",
             "correct": False,
             "why": "A resultant force always changes the motion. This one "
                    "changes it violently."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h02",
        "band": "harder",
        "text": "An astronaut on the Moon drops a hammer and a feather "
                "together and they land together. Why does the same test "
                "fail on Earth?",
        "options": [
            {"text": "Because the Moon's gravity is weaker.",
             "correct": False,
             "why": "Weaker gravity slows both equally. It is not what makes "
                    "the difference."},
            {"text": "Because the feather is lighter, and weight decides "
                     "how fast things fall, so a heavier thing always wins "
                     "whatever the air is doing to either of them", "correct": False,
             "why": "Then the Moon test would fail too. Weight on its own "
                    "does not decide it."},
            {"text": "Because on Earth the air resists both, and that "
                     "resistance is a large share of the feather's weight "
                     "and a tiny share of the hammer's.", "correct": True},
            {"text": "Because the Moon has no gravity at all.",
             "correct": False,
             "why": "It has about a sixth of Earth's. Without any, nothing "
                    "would have fallen."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h03",
        "band": "harder",
        "text": "Air resistance roughly QUADRUPLES when the speed doubles. "
                "Why?",
        "options": [
            {"text": "Because the object gets heavier as it speeds up, and "
                     "a heavier object needs more to hold it back",
             "correct": False,
             "why": "Its weight is unchanged. Only the resistance grows."},
            {"text": "Because you hit twice as much air per second, and hit "
                     "each bit of it twice as hard.", "correct": True},
            {"text": "Because air gets denser at higher speeds.",
             "correct": False,
             "why": "The air is the same. What changes is how much of it you "
                    "meet and how hard."},
            {"text": "Because the area facing the flow doubles.",
             "correct": False,
             "why": "The area is fixed by the shape. It is the speed that "
                    "has changed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h04",
        "band": "harder",
        "text": "Fish, dolphins, submarines and torpedoes all end up with a "
                "rounded nose and a tapering tail. What is the test of a "
                "good streamlined shape?",
        "options": [
            {"text": "How pointed the front is.", "correct": False,
             "why": "A very sharp nose is not the winner — the tail "
                    "matters more than the nose."},
            {"text": "How heavy the object is.", "correct": False,
             "why": "Weight is a separate question entirely. Streamlining is "
                    "about the shape."},
            {"text": "How smooth the surface feels.", "correct": False,
             "why": "Surface finish helps a little, but a blunt-tailed "
                    "smooth object still churns the water badly."},
            {"text": "How little wake it leaves behind.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-06-e05",
        "band": "easier",
        "text": "Which of these INCREASES the air resistance on a moving car?",
        "options": [
            {"text": "Fitting a large roof box", "correct": True},
            {"text": "Polishing the paintwork until it shines",
             "correct": False,
             "why": "A smoother surface slightly reduces resistance rather "
                    "than adding to it."},
            {"text": "Driving more slowly along the same road",
             "correct": False,
             "why": "Resistance grows with speed, so going slower makes it "
                    "smaller."},
            {"text": "Letting some air out of the tyres", "correct": False,
             "why": "That changes the friction at the road, not how much air "
                    "the car has to push aside."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e06",
        "band": "easier",
        "text": "What is terminal velocity?",
        "options": [
            {"text": "The fastest speed anything is allowed to fall at",
             "correct": False,
             "why": "It is not a rule or a limit. It is simply where the "
                    "forces happen to balance for that object."},
            {"text": "The speed at which a falling object hits the ground",
             "correct": False,
             "why": "It is reached well before landing, and an object can "
                    "land at other speeds entirely."},
            {"text": "The steady speed reached once resistance has grown to "
                     "match the weight",
             "correct": True},
            {"text": "The speed at which air resistance disappears",
             "correct": False,
             "why": "Air resistance is at its largest there — that is exactly "
                    "why the speed stops rising."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-06-s05",
        "band": "standard",
        "text": "A skydiver of weight 800 N is falling at terminal velocity. "
                "What is the air resistance on them?",
        "options": [
            {"text": "0 N, because the speed is steady", "correct": False,
             "why": "A steady speed means the RESULTANT is zero, which needs "
                    "the resistance to equal the weight."},
            {"text": "More than 800 N, or they would not have stopped "
                     "speeding up",
             "correct": False,
             "why": "More than 800 N would slow them down. Steady means "
                    "exactly equal."},
            {"text": "800 N, acting upwards on them", "correct": True},
            {"text": "It cannot be given without knowing the speed",
             "correct": False,
             "why": "Whatever the speed turns out to be, at terminal velocity "
                    "the resistance equals the weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s06",
        "band": "standard",
        "text": "A flat sheet of paper falls slowly, but the same sheet "
                "screwed into a tight ball falls quickly. Why?",
        "options": [
            {"text": "Because screwing it up makes it heavier",
             "correct": False,
             "why": "The paper is the same paper, so its weight has not "
                    "changed at all."},
            {"text": "Because the flat sheet has a much larger area facing "
                     "the air",
             "correct": True},
            {"text": "Because a ball is a more natural shape for falling",
             "correct": False,
             "why": "Shape matters only through the area meeting the air and "
                    "how smoothly it parts."},
            {"text": "Because gravity pulls harder on compact objects",
             "correct": False,
             "why": "Gravity depends on mass, which is unchanged by folding "
                    "the sheet up."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-06-h05",
        "band": "harder",
        "text": "Two skydivers have the same shape and posture, but one is "
                "heavier. Why does the heavier one reach a higher terminal "
                "velocity?",
        "options": [
            {"text": "Because gravity pulls heavier objects faster from the "
                     "start",
             "correct": False,
             "why": "Both start with the same acceleration; it is where the "
                    "balance point falls that differs."},
            {"text": "Because a heavier body pushes the air out of the way "
                     "rather than being slowed",
             "correct": False,
             "why": "Both push the air aside. The heavier one simply needs "
                    "more resistance before it balances."},
            {"text": "Because heavier objects have less air resistance at any "
                     "speed",
             "correct": False,
             "why": "Resistance depends on speed and area, not on weight, so "
                    "at a given speed it is the same."},
            {"text": "Because the resistance must grow larger to match the "
                     "bigger weight, and that needs more speed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h06",
        "band": "harder",
        "text": "Submarines and aircraft are both streamlined. Why does "
                "streamlining matter more in water than in air at the same "
                "speed?",
        "options": [
            {"text": "Because water is far denser, so far more of it must be "
                     "pushed aside",
             "correct": True},
            {"text": "Because water is colder than air, so it grips the hull "
                     "harder",
             "correct": False,
             "why": "Temperature is not what makes the resistance large; how "
                    "much material is in the way is."},
            {"text": "Because a submarine travels much faster than an "
                     "aircraft",
             "correct": False,
             "why": "It is much slower, and the question compares them at the "
                    "same speed anyway."},
            {"text": "Because water resistance does not grow with speed, so "
                     "shape is all that is left",
             "correct": False,
             "why": "Water resistance grows with speed exactly as air "
                    "resistance does."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · easier ────────────────────────────────
    {
        "id": "p4-06-e07",
        "band": "easier",
        "text": "A cyclist pedals forwards into a headwind. Which way does "
                "air resistance act on the cyclist?",
        "options": [
            {"text": "Backwards, always against the direction of "
                     "travel.", "correct": True},
            {"text": "Forwards, adding extra force to the pedalling "
                     "effort already being made.", "correct": False,
             "why": "Resistance always opposes the motion; it never adds "
                    "to it."},
            {"text": "Sideways, pushing the cyclist off course.",
             "correct": False,
             "why": "It acts along the line of travel, not across it."},
            {"text": "Downwards, adding directly onto the cyclist's own "
                     "body weight.", "correct": False,
             "why": "Resistance acts along the direction of travel, not "
                    "vertically."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e08",
        "band": "easier",
        "text": "An arrow flies through the air after leaving the bow. "
                "Which way does air resistance act on it?",
        "options": [
            {"text": "Forwards, helping it along.", "correct": False,
             "why": "Resistance opposes motion; it never helps an object "
                    "along."},
            {"text": "Backwards, always against the direction it is "
                     "flying.", "correct": True},
            {"text": "Downwards only, adding straight onto its own "
                     "weight as it falls.", "correct": False,
             "why": "Resistance acts along the direction of flight, not "
                    "straight down."},
            {"text": "It has no direction at all, since air is not a "
                     "solid object.", "correct": False,
             "why": "Air still exerts a real force with a direction, "
                    "opposing the arrow's motion."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e09",
        "band": "easier",
        "text": "A motorboat speeds across a lake. Which way does water "
                "resistance act on the hull?",
        "options": [
            {"text": "Forwards, pushing the boat steadily along through "
                     "the open water.", "correct": False,
             "why": "Resistance always opposes motion, never adds to it."},
            {"text": "Upwards, lifting the hull clean out of the "
                     "water's surface.", "correct": False,
             "why": "Resistance acts along the direction of travel, not "
                    "vertically."},
            {"text": "Backwards, always against the direction the boat "
                     "is moving.", "correct": True},
            {"text": "It depends on the colour of the hull.",
             "correct": False,
             "why": "Colour makes no difference to the direction of "
                    "resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e10",
        "band": "easier",
        "text": "A car speeds up from 30 mph to 70 mph on a motorway. What "
                "happens to the air resistance acting on it?",
        "options": [
            {"text": "It gets smaller.", "correct": False,
             "why": "Faster travel pushes more air aside every second, so "
                    "resistance grows, not shrinks."},
            {"text": "It stays exactly the same.", "correct": False,
             "why": "Resistance depends on speed, and the speed has "
                    "clearly changed."},
            {"text": "It disappears above a certain speed.", "correct": False,
             "why": "Resistance never disappears; it keeps growing as "
                    "speed rises."},
            {"text": "It gets bigger.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e11",
        "band": "easier",
        "text": "A runner speeds up during the final sprint of a race. "
                "What happens to the air resistance on them?",
        "options": [
            {"text": "It increases.", "correct": True},
            {"text": "It decreases.", "correct": False,
             "why": "Faster running pushes more air out of the way each "
                    "second, increasing resistance."},
            {"text": "It stays the same throughout the race.",
             "correct": False,
             "why": "Resistance changes with speed, and the runner's "
                    "speed is rising."},
            {"text": "It only matters once they cross the finish line.",
             "correct": False,
             "why": "Resistance acts throughout the run, at every speed, "
                    "not just at the end."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e12",
        "band": "easier",
        "text": "A cyclist freewheels down a hill, going faster and faster. "
                "What happens to the air resistance as they speed up?",
        "options": [
            {"text": "It grows smaller.", "correct": False,
             "why": "The faster the cyclist goes, the more air resistance "
                    "pushes back."},
            {"text": "It grows larger.", "correct": True},
            {"text": "It vanishes completely.", "correct": False,
             "why": "Resistance never vanishes while an object is moving "
                    "through air."},
            {"text": "It becomes a forward force instead.", "correct": False,
             "why": "Resistance always acts against the motion; it never "
                    "switches to push the same way."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e13",
        "band": "easier",
        "text": "A skydiver spreads their arms and legs out wide instead "
                "of staying streamlined. What happens to the air "
                "resistance on them?",
        "options": [
            {"text": "It decreases, since spreading out somehow makes "
                     "them noticeably lighter overall.", "correct": False,
             "why": "Spreading out does not change their weight at all; "
                    "it changes the area facing the air."},
            {"text": "It stays the same, since the skydiver's total body "
                     "size is unchanged.", "correct": False,
             "why": "The AREA facing the airflow has changed, even though "
                    "their overall size has not."},
            {"text": "It increases, because a bigger area facing the "
                     "airflow always means more resistance.",
             "correct": True},
            {"text": "It becomes zero, since arms and legs are thin.",
             "correct": False,
             "why": "A wider shape still meets plenty of air; resistance "
                    "does not vanish."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e14",
        "band": "easier",
        "text": "An umbrella is opened above someone's head in strong "
                "wind. What happens to the wind resistance on the "
                "umbrella compared with when it was closed?",
        "options": [
            {"text": "It increases a great deal, because far more area "
                     "now faces the wind.", "correct": True},
            {"text": "It decreases, since the fabric spreads the force "
                     "out.", "correct": False,
             "why": "Spreading the force out does not reduce the "
                    "resistance; the bigger area increases it."},
            {"text": "It stays the same as when closed.", "correct": False,
             "why": "A closed umbrella presents almost no area to the "
                    "wind; an open one presents a lot."},
            {"text": "It becomes negative, actively pulling the umbrella "
                     "towards the oncoming wind.", "correct": False,
             "why": "Resistance always opposes motion; it cannot pull "
                    "something along with the flow."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e15",
        "band": "easier",
        "text": "A cyclist sits upright instead of crouching low over the "
                "handlebars. What happens to the air resistance at the "
                "same speed?",
        "options": [
            {"text": "It decreases, since sitting up is more "
                     "comfortable.", "correct": False,
             "why": "Comfort has no bearing on resistance; the area "
                    "facing the air is what matters."},
            {"text": "It stays the same, since the cyclist's weight has "
                     "not changed.", "correct": False,
             "why": "Weight is unrelated here; it is the AREA facing the "
                    "air that has increased."},
            {"text": "It disappears, since the cyclist is not going any "
                     "faster.", "correct": False,
             "why": "Resistance does not disappear at any speed above "
                    "zero; the posture has simply made it bigger."},
            {"text": "It increases, because more of the body faces the "
                     "airflow.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e16",
        "band": "easier",
        "text": "A skydiver has been falling for a while and their speed "
                "has stopped changing. What must be true of the resultant "
                "force on them?",
        "options": [
            {"text": "It is 0 N.", "correct": True},
            {"text": "It is equal to their weight, downwards.",
             "correct": False,
             "why": "A downward resultant would still be speeding them "
                    "up; a steady speed needs 0 N."},
            {"text": "It is equal to their weight, upwards.",
             "correct": False,
             "why": "That would be slowing them down, not holding a "
                    "steady speed."},
            {"text": "It cannot be worked out without their exact speed.",
             "correct": False,
             "why": "A steady, unchanging speed on its own is enough to "
                    "say the resultant is 0 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e17",
        "band": "easier",
        "text": "A raindrop falls from a cloud and eventually stops "
                "getting any faster, continuing at a steady speed to the "
                "ground. What has happened to the resistance on it?",
        "options": [
            {"text": "It has grown considerably bigger than the "
                     "raindrop's own weight.", "correct": False,
             "why": "That would slow the raindrop down, not let it fall "
                    "at a steady speed."},
            {"text": "It has stayed exactly the same the whole way "
                     "throughout the entire fall.", "correct": False,
             "why": "Resistance grows with speed, and the raindrop was "
                    "speeding up before reaching this steady fall."},
            {"text": "It has grown until it exactly matches the "
                     "raindrop's weight.", "correct": True},
            {"text": "It has shrunk to zero.", "correct": False,
             "why": "Zero resistance would mean the raindrop kept "
                    "speeding up, which it has stopped doing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e18",
        "band": "easier",
        "text": "A table-tennis ball dropped from a height quickly reaches "
                "a slow, steady falling speed. What does this tell you "
                "about the forces on it at that point?",
        "options": [
            {"text": "They are unbalanced, with the ball's weight still "
                     "winning out overall.", "correct": False,
             "why": "Unbalanced forces would mean the speed was still "
                    "changing, and it has stopped changing."},
            {"text": "They are balanced — resistance now matches its "
                     "small weight.", "correct": True},
            {"text": "There are no forces acting on it at all.",
             "correct": False,
             "why": "Both weight and resistance are still acting; they "
                    "simply now cancel out."},
            {"text": "The ball has stopped being affected by gravity.",
             "correct": False,
             "why": "Gravity never switches off; its pull is simply "
                    "matched by the resistance now."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e19",
        "band": "easier",
        "text": "A parachutist rolls from a flat, spread-out position "
                "into a tight, head-first dive. What happens to their "
                "weight at that moment?",
        "options": [
            {"text": "Nothing — weight never depends on posture.",
             "correct": True},
            {"text": "It decreases, since a head-down shape is smaller.",
             "correct": False,
             "why": "Weight depends on mass, not on the shape or posture "
                    "of the body."},
            {"text": "It increases, since diving head-down feels "
                     "heavier.", "correct": False,
             "why": "Weight has not changed; it may simply feel "
                    "different, but the actual force has not altered."},
            {"text": "It becomes impossible to state without their exact "
                     "speed.", "correct": False,
             "why": "Weight does not depend on speed at all, only on "
                    "mass."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e20",
        "band": "easier",
        "text": "A parachute is opened during a skydive. What happens to "
                "the skydiver's weight the moment it opens?",
        "options": [
            {"text": "It suddenly decreases.", "correct": False,
             "why": "Opening a parachute changes the resistance acting on "
                    "the skydiver, not their weight."},
            {"text": "It suddenly increases by a surprisingly large "
                     "amount.", "correct": False,
             "why": "Nothing about a parachute opening adds mass to the "
                    "skydiver."},
            {"text": "It becomes completely zero for a brief moment in "
                     "time.", "correct": False,
             "why": "Weight never becomes zero during an ordinary "
                    "skydive; only the resistance changes suddenly."},
            {"text": "Nothing changes — weight never depends on the "
                     "resistance acting on an object.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e21",
        "band": "easier",
        "text": "Why are racing cars built low and smoothly curved rather "
                "than tall and boxy?",
        "options": [
            {"text": "To make them heavier, for better grip.", "correct": False,
             "why": "Shape does not add weight; a low, smooth shape is "
                    "about resistance, not mass."},
            {"text": "To make them louder for spectators.", "correct": False,
             "why": "Shape has nothing to do with sound; it is about how "
                    "easily air flows around the car."},
            {"text": "To reduce the air resistance acting on them at "
                     "speed.", "correct": True},
            {"text": "To increase the air resistance deliberately, for "
                     "more control.", "correct": False,
             "why": "Racing cars are shaped to REDUCE resistance, letting "
                    "them reach higher speeds."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e22",
        "band": "easier",
        "text": "Why do fish have smooth, tapered bodies rather than flat, "
                "blocky ones?",
        "options": [
            {"text": "To reduce the water resistance as they swim.",
             "correct": True},
            {"text": "To make themselves considerably heavier while "
                     "swimming in the water.", "correct": False,
             "why": "Body shape does not change how much a fish weighs; "
                    "it changes how easily water flows past it."},
            {"text": "To increase the resistance, helping them stop "
                     "quickly.", "correct": False,
             "why": "A streamlined shape reduces resistance, letting a "
                    "fish swim more efficiently, not stop faster."},
            {"text": "To make them more visible to predators.",
             "correct": False,
             "why": "Visibility is unrelated; the shape is about moving "
                    "efficiently through water."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e23",
        "band": "easier",
        "text": "A speed skater wears a tight, smooth suit instead of "
                "loose clothing. Why?",
        "options": [
            {"text": "To keep them warmer during the race.", "correct": False,
             "why": "Warmth is a side effect at most; the main purpose is "
                    "reducing resistance."},
            {"text": "To reduce the air resistance slowing them down.",
             "correct": True},
            {"text": "To increase their own body weight for much better "
                     "balance in the water.", "correct": False,
             "why": "A suit does not add meaningful weight; its purpose "
                    "is a smoother shape for the air."},
            {"text": "To increase the air resistance, for more control "
                     "while turning.", "correct": False,
             "why": "Skinsuits are designed to CUT resistance, not add to "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e24",
        "band": "easier",
        "text": "Why is a parachute designed to be as large as possible?",
        "options": [
            {"text": "To make the skydiver weigh less.", "correct": False,
             "why": "A parachute changes the resistance acting on the "
                    "skydiver, not their weight."},
            {"text": "To make the skydiver more streamlined.",
             "correct": False,
             "why": "The opposite is true — a parachute is deliberately "
                    "UNstreamlined, to maximise resistance."},
            {"text": "To create as much air resistance as possible, "
                     "slowing the fall.", "correct": True},
            {"text": "To reduce the air resistance so the fall speeds up "
                     "a great deal more.", "correct": False,
             "why": "A parachute is meant to slow the fall by increasing "
                    "resistance, not reduce it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e25",
        "band": "easier",
        "text": "A racing car opens a rear wing flap sharply under heavy "
                "braking. What is this flap doing?",
        "options": [
            {"text": "Reducing the air resistance so the car can brake "
                     "faster on its own.", "correct": False,
             "why": "The flap is designed to increase resistance, adding "
                    "to the braking effect."},
            {"text": "Increasing the air resistance to help slow the car "
                     "down.", "correct": True},
            {"text": "Increasing the car's weight for better grip.",
             "correct": False,
             "why": "The flap changes resistance, not the car's actual "
                    "weight."},
            {"text": "Making the car more streamlined for cornering.",
             "correct": False,
             "why": "Opening a flap under braking deliberately increases "
                    "resistance rather than reducing it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e26",
        "band": "easier",
        "text": "Why does a badminton shuttlecock slow down very quickly "
                "compared with a tennis ball hit at the same speed?",
        "options": [
            {"text": "It weighs more than a tennis ball.", "correct": False,
             "why": "A shuttlecock weighs far less than a tennis ball; "
                    "weight is not the reason."},
            {"text": "It is hit with less force to begin with.",
             "correct": False,
             "why": "The comparison is for the same starting speed; the "
                    "shape is what causes the rapid slowing."},
            {"text": "Air resistance does not act on such a very light "
                     "object at all.", "correct": False,
             "why": "Its light weight is exactly why the resistance, "
                    "though modest in force, slows it so quickly."},
            {"text": "Its open, feathered shape gives it far more air "
                     "resistance.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e27",
        "band": "easier",
        "text": "A swimmer and a cyclist travel at the same speed, one "
                "through water and one through air. Which one feels more "
                "resistance, and why?",
        "options": [
            {"text": "The swimmer, because water is far denser than "
                     "air.", "correct": True},
            {"text": "The cyclist, because air moves faster than water.",
             "correct": False,
             "why": "Air does not move faster than water on its own; the "
                    "difference is in how dense each fluid is."},
            {"text": "Neither — resistance is the same in any fluid at "
                     "the same speed.", "correct": False,
             "why": "Resistance depends on the fluid as well as the "
                    "speed, and water and air are very different fluids."},
            {"text": "The cyclist, because bicycles are less streamlined "
                     "than swimmers.", "correct": False,
             "why": "The comparison is about the FLUID's density, not "
                    "about how streamlined the traveller is."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e28",
        "band": "easier",
        "text": "Why does wading through a swimming pool feel so much "
                "harder than walking the same distance through air?",
        "options": [
            {"text": "Because water is colder than air.", "correct": False,
             "why": "Temperature is not what causes the extra resistance; "
                    "the density of the fluid is."},
            {"text": "Water is much denser than air, so it resists "
                     "movement far more strongly.", "correct": True},
            {"text": "Because swimming pools have no friction at all.",
             "correct": False,
             "why": "This is about resistance from the water itself, not "
                    "about friction with a pool floor."},
            {"text": "Because walking uses entirely different muscles "
                     "once you are fully underwater in the pool.",
             "correct": False,
             "why": "The muscles used do not change how much resistance "
                    "the water itself provides."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e29",
        "band": "easier",
        "text": "Do a feather and a hailstone falling through air reach "
                "the same terminal velocity?",
        "options": [
            {"text": "Yes, because terminal velocity is exactly the same "
                     "for every single falling object.", "correct": False,
             "why": "Terminal velocity depends on the object's own weight "
                    "and shape; it is not a single fixed value."},
            {"text": "Yes, because air resistance is the same for every object, so every fall settles at the one speed the air allows.", "correct": False,
             "why": "Resistance depends on an object's speed, area and "
                    "shape, which differ between a feather and a "
                    "hailstone."},
            {"text": "No — their different weights and shapes mean they "
                     "balance out at different speeds.", "correct": True},
            {"text": "No, but only because the hailstone is colder.",
             "correct": False,
             "why": "Temperature is not the reason; weight and shape are "
                    "what set the balance point."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e30",
        "band": "easier",
        "text": "A skydiver reaches one terminal velocity spread out, and "
                "a different, higher terminal velocity diving head-down. "
                "Why can there be more than one terminal velocity for the "
                "same person?",
        "options": [
            {"text": "Because terminal velocity is simply wherever "
                     "resistance happens to balance weight, and a smaller "
                     "area always needs more speed to do that.",
             "correct": True},
            {"text": "Because their weight changes between the two "
                     "postures.", "correct": False,
             "why": "Their weight is exactly the same in either posture; "
                    "only the area facing the air changes."},
            {"text": "Because terminal velocity is completely fixed for "
                     "any one person and can never actually change at "
                     "all, however they arrange their body.",
             "correct": False,
             "why": "It is not fixed — it depends on the shape presented "
                    "to the air, which the skydiver can change."},
            {"text": "Because gravity is stronger when diving head-down.",
             "correct": False,
             "why": "Gravity's pull does not depend on body posture at "
                    "all."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · standard ──────────────────────────────
    {
        "id": "p4-06-s07",
        "band": "standard",
        "text": "A skydiver weighing 700 N is falling and the air "
                "resistance on them is currently 500 N. What is the "
                "resultant force, and what is happening to their speed?",
        "options": [
            {"text": "200 N downwards; they are still speeding up.",
             "correct": True},
            {"text": "200 N upwards; they are slowing down quite "
                     "rapidly now.", "correct": False,
             "why": "Weight (700 N) is bigger than resistance (500 N), so "
                    "the resultant points down, not up."},
            {"text": "1200 N downwards; they are speeding up very fast.",
             "correct": False,
             "why": "The two forces subtract because they act in "
                    "opposite directions; they do not add together."},
            {"text": "0 N; their speed has stopped changing.",
             "correct": False,
             "why": "700 N and 500 N are not equal, so there is a "
                    "resultant force and the speed is still changing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s08",
        "band": "standard",
        "text": "A shuttlecock weighing 0.5 N experiences 0.5 N of air "
                "resistance while falling. What is happening to its "
                "speed?",
        "options": [
            {"text": "It has stopped changing — the shuttlecock is at its "
                     "terminal velocity.", "correct": True},
            {"text": "It is still increasing steadily, since the "
                     "shuttlecock is so very light.", "correct": False,
             "why": "Weight and resistance are exactly equal here, giving "
                    "a resultant of 0 N, whatever the shuttlecock's "
                    "weight."},
            {"text": "It is decreasing, since resistance is holding it "
                     "back.", "correct": False,
             "why": "Resistance exactly matches the weight; the "
                    "resultant is 0 N, not a slowing resultant."},
            {"text": "It cannot be worked out without knowing its speed.",
             "correct": False,
             "why": "Equal weight and resistance are enough on their own "
                    "to show the resultant is 0 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s09",
        "band": "standard",
        "text": "A hailstone weighing 2 N experiences 3 N of air "
                "resistance at a particular moment. What must be true?",
        "options": [
            {"text": "The hailstone is slowing down, because resistance "
                     "is now bigger than its weight.", "correct": True},
            {"text": "The hailstone is speeding up.", "correct": False,
             "why": "A resistance bigger than the weight gives an upward "
                    "resultant, which slows a falling object down."},
            {"text": "The hailstone has reached terminal velocity.",
             "correct": False,
             "why": "Terminal velocity needs the two forces to be EQUAL; "
                    "here they are not."},
            {"text": "The hailstone is falling at a completely steady "
                     "speed throughout its whole descent.", "correct": False,
             "why": "A steady speed needs a resultant of 0 N, and here "
                    "resistance exceeds the weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s10",
        "band": "standard",
        "text": "A skydiver weighing 800 N opens their parachute, and the "
                "resistance immediately jumps to 1000 N. What is the "
                "resultant force, and what happens to their fall?",
        "options": [
            {"text": "200 N downwards; the fall speeds up considerably "
                     "from here.", "correct": False,
             "why": "Resistance (1000 N) is now bigger than weight "
                    "(800 N), giving a resultant upwards, not downwards."},
            {"text": "200 N upwards; the fall slows down sharply.",
             "correct": True},
            {"text": "1800 N upwards; the skydiver rises into the air.",
             "correct": False,
             "why": "The forces subtract, not add, and an upward "
                    "resultant here means slowing the fall, not reversing "
                    "it into a rise."},
            {"text": "0 N; nothing about the fall changes.", "correct": False,
             "why": "800 N and 1000 N are not equal, so there genuinely "
                    "is a resultant force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s11",
        "band": "standard",
        "text": "A cyclist and their bicycle weigh 750 N together. At a "
                "certain speed, the total resistance (air and friction "
                "combined) is exactly 750 N. What does this tell you?",
        "options": [
            {"text": "The cyclist is still speeding up.", "correct": False,
             "why": "Equal forces give a resultant of 0 N, which means no "
                    "further change in speed."},
            {"text": "The cyclist must be freewheeling steadily downhill "
                     "the whole time without pedalling at all.",
             "correct": False,
             "why": "The cause of the motion is not stated; what the "
                    "equal forces show is simply that the speed is "
                    "steady."},
            {"text": "The cyclist is travelling at a steady speed — the "
                     "resultant is 0 N.", "correct": True},
            {"text": "The cyclist's weight has become equal to their "
                     "resistance permanently.", "correct": False,
             "why": "The 750 N figures are for a moment at this "
                    "particular speed, not a permanent equality."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s12",
        "band": "standard",
        "text": "A skydiver pulls their arms and legs in close to their "
                "body while falling. What happens to their terminal "
                "velocity?",
        "options": [
            {"text": "It decreases, because pulling in reduces their "
                     "weight.", "correct": False,
             "why": "Their weight is unchanged; only the area facing the "
                    "air has altered."},
            {"text": "It increases, because a smaller area means less "
                     "resistance at any given speed.", "correct": True},
            {"text": "It stays the same, since their weight decides "
                     "terminal velocity, not their shape.", "correct": False,
             "why": "Shape does change it, by changing how much "
                    "resistance is felt at a given speed."},
            {"text": "It becomes impossible to reach a steady speed at "
                     "all.", "correct": False,
             "why": "A steady speed is still reached; it is simply a "
                    "higher one than before."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s13",
        "band": "standard",
        "text": "A parachutist wearing a wingsuit spreads extra fabric "
                "between their arms and legs. Compared with normal "
                "free-fall clothing, what happens to their terminal "
                "velocity?",
        "options": [
            {"text": "It increases, because the wingsuit makes them "
                     "lighter.", "correct": False,
             "why": "A wingsuit does not reduce weight; it increases the "
                    "area facing the airflow."},
            {"text": "It decreases, because the extra fabric gives much "
                     "more resistance at a given speed.", "correct": True},
            {"text": "It stays the same, since a wingsuit does not affect "
                     "falling at all, whatever shape it is cut in.",
             "correct": False,
             "why": "A wingsuit dramatically increases the area facing "
                    "the air, which does affect the fall."},
            {"text": "It becomes zero, and the skydiver stops falling "
                     "completely.", "correct": False,
             "why": "The skydiver still falls, just far more slowly, "
                    "reaching a much lower steady speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s14",
        "band": "standard",
        "text": "A cyclist changes from riding upright to crouching low "
                "over the handlebars. What happens to their maximum "
                "achievable speed on a flat road?",
        "options": [
            {"text": "It decreases, because crouching makes pedalling "
                     "harder.", "correct": False,
             "why": "Crouching reduces resistance, which makes higher "
                    "speeds easier to sustain, not harder."},
            {"text": "It stays the same, since their weight has not "
                     "changed.", "correct": False,
             "why": "Weight is not what limits top speed here; the "
                    "resistance from their posture is."},
            {"text": "It increases, because less air resistance at a "
                     "given speed lets them go faster before it balances "
                     "their pedalling force.", "correct": True},
            {"text": "It becomes completely unlimited, since there is "
                     "supposedly no more resistance acting on them at "
                     "all.", "correct": False,
             "why": "Resistance is reduced, not removed; a limit still "
                    "exists, just a higher one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s15",
        "band": "standard",
        "text": "A delivery van fits a large roof box for extra storage. "
                "What effect does this have on its fuel economy at "
                "motorway speed, and why?",
        "options": [
            {"text": "It improves, because the roof box makes the van "
                     "lighter overall.", "correct": False,
             "why": "A roof box adds weight; it does not reduce it, and "
                    "the main effect here is on air resistance."},
            {"text": "It has no effect, since fuel economy only depends "
                     "on the engine.", "correct": False,
             "why": "Air resistance is a major factor in fuel use at "
                    "motorway speed, regardless of the engine."},
            {"text": "It improves, because the roof box somehow makes "
                     "the van considerably more streamlined overall.",
             "correct": False,
             "why": "A large roof box typically makes a vehicle LESS "
                    "streamlined, not more."},
            {"text": "It worsens, because the roof box increases the "
                     "area facing the air, increasing resistance.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s16",
        "band": "standard",
        "text": "A skydiver has just stepped out of the aircraft, barely "
                "moving. Which of these is closest to the resistance on "
                "them at that instant?",
        "options": [
            {"text": "Close to 0 N.", "correct": True},
            {"text": "Equal to their full weight.", "correct": False,
             "why": "That would mean they had already reached terminal "
                    "velocity, which takes time to build up to."},
            {"text": "Bigger than their weight.", "correct": False,
             "why": "That would push them back up towards the aircraft, "
                    "which does not happen."},
            {"text": "Exactly half their weight, always.", "correct": False,
             "why": "There is no such fixed rule; at almost no speed, "
                    "almost no resistance has built up yet."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s17",
        "band": "standard",
        "text": "A conker falls from a tall tree and stops speeding up well before it reaches the ground. Which of these is closest to the resistance on it at that point?",
        "options": [
            {"text": "Close to 0 N, since it is still moving.",
             "correct": False,
             "why": "0 N of resistance would mean the conker kept speeding up, which it has stopped doing."},
            {"text": "Equal to its own weight.", "correct": True},
            {"text": "Much bigger than its weight.", "correct": False,
             "why": "That would be slowing the conker down, not letting it fall at a steady speed."},
            {"text": "Impossible to estimate without its exact size.",
             "correct": False,
             "why": "A steady falling speed on its own is enough to say "
                    "resistance now matches the weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s18",
        "band": "standard",
        "text": "A sheet of paper is released from shoulder height and "
                "almost immediately falls at a slow, steady speed. What "
                "does 'almost immediately' suggest about this object?",
        "options": [
            {"text": "It never actually experiences any air resistance "
                     "at all during its whole fall.", "correct": False,
             "why": "It reaches a steady speed precisely BECAUSE "
                    "resistance is acting on it and quickly matches its "
                    "tiny weight."},
            {"text": "Its terminal velocity is very low, so resistance "
                     "catches up with its small weight extremely "
                     "quickly.", "correct": True},
            {"text": "Gravity does not act on light objects like paper.",
             "correct": False,
             "why": "Gravity acts on every mass; the paper's weight is "
                    "simply very small, so resistance catches up fast."},
            {"text": "The paper's weight keeps changing as it falls.",
             "correct": False,
             "why": "Its weight stays constant throughout; what changes "
                    "quickly is the resistance, until it matches that "
                    "weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s19",
        "band": "standard",
        "text": "A cricket ball and a beach ball are both dropped from "
                "the same height. The beach ball reaches a slow steady "
                "speed almost immediately, while the cricket ball keeps "
                "speeding up all the way down. Explain the difference.",
        "options": [
            {"text": "The beach ball is not affected by gravity at all.",
             "correct": False,
             "why": "Gravity affects both balls identically; the "
                    "difference lies in how quickly resistance can match "
                    "each one's weight."},
            {"text": "The cricket ball has noticeably more air "
                     "resistance acting on it throughout its whole fall "
                     "to the ground, compared with the beach ball.",
             "correct": False,
             "why": "At the same speed the cricket ball, being smaller, "
                    "likely has LESS resistance than the beach ball, not "
                    "more."},
            {"text": "The beach ball's low weight is quickly matched by "
                     "resistance, while the cricket ball's greater weight "
                     "needs much more speed before resistance can catch "
                     "up.", "correct": True},
            {"text": "The beach ball weighs more, so resistance affects "
                     "it sooner.", "correct": False,
             "why": "The beach ball weighs far less than the cricket "
                    "ball, which is exactly why resistance catches up "
                    "with it so quickly."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s20",
        "band": "standard",
        "text": "A saloon car and a boxy delivery van of similar weight "
                "travel at the same motorway speed. Which needs more "
                "engine force to maintain that speed, and why?",
        "options": [
            {"text": "The car, because it is lower to the ground.",
             "correct": False,
             "why": "Being lower is part of what REDUCES a car's "
                    "resistance; it does not increase the force needed."},
            {"text": "The van, because its blocky shape gives it more air "
                     "resistance at the same speed.", "correct": True},
            {"text": "Neither — the engine force needed depends only on "
                     "weight, never on shape at all.", "correct": False,
             "why": "Shape strongly affects the resistance that the "
                    "engine has to overcome at a given speed."},
            {"text": "The van, but only because it has a bigger engine.",
             "correct": False,
             "why": "Engine size is not the reason; the van's shape is "
                    "what creates more resistance to overcome."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s21",
        "band": "standard",
        "text": "A javelin is designed to be long, thin and pointed "
                "rather than short and blunt. How does this help it "
                "travel further?",
        "options": [
            {"text": "Its shape makes it heavier, so gravity affects it "
                     "less.", "correct": False,
             "why": "A pointed shape does not add weight; it changes how "
                    "easily air flows around the javelin."},
            {"text": "Its shape increases the resistance, giving it more "
                     "lift.", "correct": False,
             "why": "A streamlined shape REDUCES resistance; a javelin "
                    "gets no meaningful lift from its shape."},
            {"text": "Its shape lets air flow past more easily, reducing "
                     "the resistance slowing it down in flight.",
             "correct": True},
            {"text": "Its shape has no effect whatsoever on how it "
                     "travels through the air at any speed or distance.",
             "correct": False,
             "why": "Shape has a large effect on the resistance a "
                    "javelin experiences in flight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s22",
        "band": "standard",
        "text": "A submarine has a smooth, rounded hull rather than a "
                "flat-sided one. What advantage does this give it "
                "underwater?",
        "options": [
            {"text": "A flat-sided hull would actually give noticeably "
                     "less resistance than a rounded one.", "correct": False,
             "why": "A rounded, tapered shape lets water flow past more "
                    "smoothly, giving LESS resistance than a flat-sided "
                    "hull."},
            {"text": "Lower water resistance at a given speed, so less "
                     "power is needed to maintain that speed.",
             "correct": True},
            {"text": "The rounded hull makes the submarine lighter.",
             "correct": False,
             "why": "Hull shape does not change the submarine's weight; "
                    "it changes how the water resists its motion."},
            {"text": "The shape has no real effect underwater, only in "
                     "air.", "correct": False,
             "why": "Streamlining reduces resistance in water just as it "
                    "does in air — arguably even more, since water is "
                    "denser."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s23",
        "band": "standard",
        "text": "Two identical toy cars are raced down a slope, one "
                "fitted with a large flat spoiler facing forwards and one "
                "without. Which reaches the bottom first, and why?",
        "options": [
            {"text": "The one with the spoiler, because spoilers always "
                     "add speed.", "correct": False,
             "why": "A forward-facing flat spoiler adds resistance here, "
                    "which slows the car rather than speeding it up."},
            {"text": "They arrive together, since spoilers only affect "
                     "steering.", "correct": False,
             "why": "A large flat surface facing the airflow does add "
                    "meaningful resistance, not just affect steering."},
            {"text": "The one without the spoiler, because the spoiler "
                     "increases the area facing the air, increasing "
                     "resistance.", "correct": True},
            {"text": "The one with the spoiler, because it weighs "
                     "considerably more and therefore falls faster down "
                     "the slope.", "correct": False,
             "why": "Extra weight is not the deciding factor on a slope "
                    "where resistance differs; the added resistance is "
                    "what slows it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s24",
        "band": "standard",
        "text": "A rower pulls an oar through water and then, out of the "
                "water, swings it back through the air for the next "
                "stroke. In which part is the resistance on the oar "
                "bigger, and why?",
        "options": [
            {"text": "In the air, because the oar moves faster there.",
             "correct": False,
             "why": "Even accounting for speed, water's much greater "
                    "density gives it far more resistance at comparable "
                    "speeds."},
            {"text": "They are the same, since it is the same oar both "
                     "times.", "correct": False,
             "why": "The oar is the same, but the FLUID it is moving "
                    "through is very different, giving very different "
                    "resistance."},
            {"text": "In the water, because water is far denser than air "
                     "and resists motion more strongly.", "correct": True},
            {"text": "In the air, because air resistance always beats "
                     "water resistance at any given speed.", "correct": False,
             "why": "The opposite is generally true — water resistance is "
                    "much larger than air resistance at the same speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s25",
        "band": "standard",
        "text": "A kayak glides to a stop far more quickly on water than "
                "a bicycle coasting on a flat road takes to slow by the "
                "same amount. What is the main reason?",
        "options": [
            {"text": "The kayak is much heavier than the bicycle.",
             "correct": False,
             "why": "A loaded bicycle and rider often weigh as much as or "
                    "more than a kayak and paddler; weight is not the "
                    "deciding factor here."},
            {"text": "Kayaks have no friction or resistance with the "
                     "water acting on them at all, whatever the "
                     "conditions.", "correct": False,
             "why": "There is friction and resistance between the kayak "
                    "and the water — that is exactly why it slows so "
                    "quickly."},
            {"text": "Water gives far more resistance than air at a "
                     "similar speed, because it is so much denser.",
             "correct": True},
            {"text": "Bicycles experience no air resistance at all.",
             "correct": False,
             "why": "Bicycles do experience air resistance; it is simply "
                    "much smaller than the resistance water gives a "
                    "kayak."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s26",
        "band": "standard",
        "text": "Why do competitive swimmers shave their body hair and "
                "wear extremely smooth, tight swimsuits?",
        "options": [
            {"text": "To make themselves noticeably lighter while "
                     "moving through the water.", "correct": False,
             "why": "Shaving and tight suits do not meaningfully change "
                    "body weight; they change how smoothly water flows "
                    "past the skin."},
            {"text": "To reduce the water resistance acting on them as "
                     "they swim.", "correct": True},
            {"text": "To increase their resistance, giving them more to "
                     "push against.", "correct": False,
             "why": "Swimmers want LESS resistance, so they can hold a "
                    "faster pace for the same effort."},
            {"text": "To keep warm during a race.", "correct": False,
             "why": "These measures are about reducing resistance, not "
                    "about warmth."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s27",
        "band": "standard",
        "text": "A dragster fitted with a rear parachute deploys it "
                "immediately after crossing the finish line at very high "
                "speed. Why?",
        "options": [
            {"text": "The parachute makes the car lighter, helping it "
                     "stop.", "correct": False,
             "why": "A parachute changes the resistance acting on the "
                    "car, not its weight."},
            {"text": "The parachute reduces the resistance considerably, "
                     "letting the car glide smoothly to a gentle stop.",
             "correct": False,
             "why": "A parachute is deployed specifically to INCREASE "
                    "resistance and help brake the car."},
            {"text": "The parachute has no real effect on stopping "
                     "distance.", "correct": False,
             "why": "A dragster's parachute makes a very large, "
                    "deliberate difference to how quickly it slows down."},
            {"text": "The parachute creates a large increase in air "
                     "resistance, helping slow the car down quickly.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s28",
        "band": "standard",
        "text": "Some fighter aircraft deploy a small parachute (a drogue "
                "chute) immediately after landing. Explain why.",
        "options": [
            {"text": "It creates useful lift, helping the aircraft stay "
                     "airborne for quite a bit longer than expected.",
             "correct": False,
             "why": "The chute is deployed AFTER landing specifically to "
                    "slow the plane, not to keep it flying."},
            {"text": "It creates extra air resistance, helping the "
                     "aircraft slow down on the runway more quickly.",
             "correct": True},
            {"text": "It reduces the aircraft's weight for easier "
                     "braking.", "correct": False,
             "why": "The chute changes the resistance acting on the "
                    "plane; it does not reduce its weight."},
            {"text": "It has no aerodynamic effect at all.", "correct": False,
             "why": "A drogue chute has a large, deliberate aerodynamic "
                    "effect: increasing resistance sharply."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s29",
        "band": "standard",
        "text": "Why might a cyclist deliberately sit upright and open "
                "their jacket wide when freewheeling down a very steep "
                "hill?",
        "options": [
            {"text": "To make themselves noticeably heavier, so that "
                     "gravity pulls them down less strongly.",
             "correct": False,
             "why": "Weight is unaffected by posture or clothing; the "
                    "change here is to the resistance from the air."},
            {"text": "To become more streamlined for extra speed.",
             "correct": False,
             "why": "Sitting upright with an open jacket makes a cyclist "
                    "LESS streamlined, increasing resistance rather than "
                    "reducing it."},
            {"text": "To increase the air resistance, helping to control "
                     "their speed on the descent.", "correct": True},
            {"text": "To reduce the resistance so they can freewheel "
                     "further.", "correct": False,
             "why": "The described change increases resistance, which "
                    "would slow the descent, not extend the freewheel."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s30",
        "band": "standard",
        "text": "A large cargo plane extends spoilers on its wings just "
                "after landing. What effect is this intended to have?",
        "options": [
            {"text": "To reduce the plane's weight for a shorter landing "
                     "roll.", "correct": False,
             "why": "Spoilers change the resistance and lift acting on "
                    "the plane; they do not change its weight."},
            {"text": "To make the plane more streamlined for taxiing.",
             "correct": False,
             "why": "Extending spoilers deliberately makes the plane LESS "
                    "streamlined, to increase resistance."},
            {"text": "To create some extra lift, helping the plane climb "
                     "back up into the sky again if needed.",
             "correct": False,
             "why": "Spoilers reduce lift and add resistance after "
                    "landing — the opposite of helping the plane climb."},
            {"text": "To sharply increase air resistance, helping the "
                     "plane slow down on the runway.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · harder ────────────────────────────────
    {
        "id": "p4-06-h07",
        "band": "harder",
        "text": "A skydiver's fall can be divided into three stages: "
                "stepping out, speeding up, and falling at a steady "
                "speed. Describe how the resultant force changes across "
                "these three stages.",
        "options": [
            {"text": "It starts equal to the full weight, then shrinks "
                     "to 0 N as resistance grows to match it.",
             "correct": True},
            {"text": "It starts at 0 N and then slowly grows until it "
                     "exactly equals the full weight by the final stage.",
             "correct": False,
             "why": "At the very start almost no resistance has built up, "
                    "so the resultant is close to the FULL weight, not "
                    "zero."},
            {"text": "It stays equal to the weight throughout all three "
                     "stages of the entire jump, from start to finish.",
             "correct": False,
             "why": "As resistance grows with speed, the resultant "
                    "shrinks; it does not stay fixed at the full weight."},
            {"text": "It becomes negative once terminal velocity is "
                     "reached.", "correct": False,
             "why": "A resultant of 0 N is neither positive nor negative; "
                    "it simply means no further change in speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h08",
        "band": "harder",
        "text": "A cyclist accelerates from rest and eventually reaches a "
                "steady top speed on the flat. Describe how the resultant "
                "force changes.",
        "options": [
            {"text": "It stays constant throughout the whole ride, since "
                     "the cyclist pedals with an unchanging effort the "
                     "entire time.", "correct": False,
             "why": "Even with constant pedalling force, the resultant "
                    "shrinks as resistance grows with speed."},
            {"text": "It starts largest, near the full pedalling force, "
                     "then shrinks to 0 N as resistance catches up.",
             "correct": True},
            {"text": "It grows larger and larger without ever reaching "
                     "zero, no matter how fast the cyclist eventually "
                     "goes.", "correct": False,
             "why": "As speed rises resistance grows to match the "
                    "pedalling force, shrinking the resultant, not "
                    "growing it."},
            {"text": "It is zero from the very start, since the cyclist "
                     "begins at rest.", "correct": False,
             "why": "At rest, before resistance has built up, the "
                    "pedalling force is largely unopposed, giving a large "
                    "resultant."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h09",
        "band": "harder",
        "text": "A car accelerates hard from a standstill, then settles "
                "at a steady top speed with the accelerator held flat to "
                "the floor. Sketch, in words, how resistance compares "
                "with the driving force across this process.",
        "options": [
            {"text": "Resistance starts equal to the driving force and stays that way for the whole of the acceleration.", "correct": False,
             "why": "At low speed resistance is small; it only grows to "
                    "match the driving force once top speed is reached."},
            {"text": "Resistance is always bigger than the driving force "
                     "from the very start, which is why the car "
                     "eventually grinds to a complete stop.",
             "correct": False,
             "why": "The car reaches a steady TOP speed, not a stop; "
                    "resistance rises to MATCH the driving force, not "
                    "exceed it."},
            {"text": "Resistance starts low, grows with speed, and "
                     "reaches the driving force exactly at top speed.",
             "correct": True},
            {"text": "Resistance has nothing to do with why the car has a "
                     "top speed.", "correct": False,
             "why": "Resistance growing until it matches the driving "
                    "force is precisely why a top speed exists."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h10",
        "band": "harder",
        "text": "A stone is dropped down a very deep well. Assuming it "
                "never hits the water, describe what eventually happens "
                "to its motion.",
        "options": [
            {"text": "It speeds up forever and ever, since nothing in an "
                     "ordinary well could ever stop a falling object from "
                     "accelerating indefinitely.", "correct": False,
             "why": "Air resistance grows with speed and eventually "
                    "matches the weight, stopping any further increase in "
                    "speed."},
            {"text": "It falls at a constant speed from the very first "
                     "instant.", "correct": False,
             "why": "At the start there is almost no resistance, so the "
                    "stone speeds up considerably before reaching a "
                    "steady fall."},
            {"text": "Its weight decreases the longer it falls, slowing "
                     "it down, because objects are believed to lose a "
                     "little mass every time they speed up further.",
             "correct": False,
             "why": "Weight does not change during a fall; it is the "
                    "growing resistance that eventually balances it."},
            {"text": "It speeds up more and more slowly until "
                     "resistance matches its weight, then falls at a "
                     "steady terminal velocity.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h11",
        "band": "harder",
        "text": "A cyclist feels 20 N of air resistance at 5 m/s. Roughly "
                "how much resistance would you expect at 10 m/s, given "
                "that resistance roughly quadruples when speed doubles?",
        "options": [
            {"text": "About 40 N.", "correct": False,
             "why": "That only doubles the resistance, but doubling the "
                    "speed roughly QUADRUPLES it."},
            {"text": "About 20 N, unchanged.", "correct": False,
             "why": "Resistance depends strongly on speed; doubling the "
                    "speed should noticeably increase it."},
            {"text": "About 80 N.", "correct": True},
            {"text": "About 160 N.", "correct": False,
             "why": "That multiplies by eight rather than by the "
                    "fourfold increase expected from doubling the speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h12",
        "band": "harder",
        "text": "A car experiences 100 N of air resistance at 20 m/s. "
                "Roughly how much would you expect at 40 m/s?",
        "options": [
            {"text": "About 200 N.", "correct": False,
             "why": "That only doubles the resistance, but doubling the "
                    "speed roughly quadruples it."},
            {"text": "About 100 N, unchanged.", "correct": False,
             "why": "Resistance grows sharply with speed; doubling the "
                    "speed should have a large effect."},
            {"text": "About 800 N.", "correct": False,
             "why": "That is eight times the original, but the expected "
                    "scaling from doubling speed is four times, not "
                    "eight."},
            {"text": "About 400 N.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h13",
        "band": "harder",
        "text": "A skydiver feels 200 N of resistance at a certain speed. "
                "If their speed doubles, roughly what resistance would "
                "you expect, and does this match how a real skydiver's "
                "fall behaves?",
        "options": [
            {"text": "About 800 N; skydivers never actually reach double "
                     "their terminal speed, since the huge resistance "
                     "would slow them straight back down.",
             "correct": True},
            {"text": "About 400 N — and it is common for skydivers to "
                     "comfortably sustain twice their terminal falling "
                     "speed for quite some time during a long dive.",
             "correct": False,
             "why": "The quadrupling rule gives roughly 800 N, not "
                    "400 N, and real skydivers do not sustain double "
                    "their terminal speed for long, precisely because "
                    "resistance would then be far too large."},
            {"text": "About 200 N, unchanged — speed has no effect on "
                     "resistance.", "correct": False,
             "why": "Resistance depends strongly on speed; doubling it "
                    "should greatly increase the resistance felt."},
            {"text": "About 1600 N — and this would let the skydiver "
                     "keep accelerating forever.", "correct": False,
             "why": "1600 N overstates the quadrupling (which gives "
                    "about 800 N), and such a large resistance would "
                    "rapidly SLOW the skydiver, not let them keep "
                    "accelerating."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h14",
        "band": "harder",
        "text": "A speedboat feels 500 N of water resistance at 4 m/s. "
                "Roughly how much resistance would it feel at 8 m/s, and "
                "what does this suggest about doubling a boat's speed?",
        "options": [
            {"text": "About 1000 N, since doubling a boat's speed simply doubles both the resistance it has to meet and the engine power needed for it.", "correct": False,
             "why": "The expected scaling is a fourfold increase in "
                    "resistance, not a twofold one, when the speed "
                    "doubles."},
            {"text": "About 500 N, unchanged — resistance does not "
                     "depend at all on a boat's speed through the water, "
                     "whatever speed it happens to be travelling at.",
             "correct": False,
             "why": "Water resistance depends strongly on speed, exactly "
                    "as air resistance does."},
            {"text": "About 2000 N; doubling speed needs roughly four "
                     "times the resistance overcome, so boats need much "
                     "more power to go faster.", "correct": True},
            {"text": "About 4000 N — resistance rises with the cube of "
                     "the speed for boats.", "correct": False,
             "why": "The rule to use here is that resistance roughly quadruples when the speed doubles, rather than rising with the cube of the speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h15",
        "band": "harder",
        "text": "A student claims: 'Terminal velocity is a speed limit "
                "built into the air itself, and no object can ever go "
                "faster than it.' Correct this claim.",
        "options": [
            {"text": "The claim is correct — air itself enforces one "
                     "single, universal, unbreakable speed limit that "
                     "applies to every falling object without exception.",
             "correct": False,
             "why": "There is no single universal limit; each falling "
                    "object has its own terminal velocity, set by its own "
                    "weight and shape."},
            {"text": "It is not a universal limit — terminal velocity is "
                     "simply wherever an object's own resistance balances "
                     "its own weight, and it changes with shape.",
             "correct": True},
            {"text": "The claim is wrong, because falling objects never "
                     "reach a steady speed at all.", "correct": False,
             "why": "Falling objects genuinely do reach a steady terminal "
                    "velocity; the flaw is describing it as a fixed "
                    "universal limit."},
            {"text": "The claim is correct, but only for objects heavier "
                     "than about 1 kg.", "correct": False,
             "why": "The idea of a fixed, universal speed limit is wrong "
                    "regardless of an object's mass."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h16",
        "band": "harder",
        "text": "A student claims: 'Heavier objects always fall faster than lighter ones, in any situation.' Assess this claim.",
        "options": [
            {"text": "It is not reliably true — in a vacuum, objects of "
                     "any weight always fall together; real-world speed "
                     "depends on the balance of weight and resistance.",
             "correct": True},
            {"text": "The claim is completely correct in every "
                     "situation, with no exceptions.", "correct": False,
             "why": "In a vacuum, a heavy and a light object fall "
                    "together, showing the claim is not universally "
                    "true."},
            {"text": "The claim is wrong because lighter objects reach the ground first, since a light object is carried down by the column of air that moves with it as it drops.",
             "correct": False,
             "why": "That simply reverses the claim without justification; in air, heavier objects often do reach a higher terminal velocity, because resistance has to grow further before it matches a bigger weight."},
            {"text": "The claim is correct only when there is no air "
                     "present at all.", "correct": False,
             "why": "That is precisely the opposite of when it holds — "
                    "with no air (a vacuum), weight makes no difference "
                    "at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h17",
        "band": "harder",
        "text": "A student claims: 'Once a skydiver's parachute opens, "
                "the strong upward force means they are now moving "
                "upwards.' What is the flaw?",
        "options": [
            {"text": "There is no flaw; any upward force acting on a "
                     "falling object always and immediately means it has "
                     "started rising back up into the sky instead.",
             "correct": False,
             "why": "A resultant force changes existing motion; it does "
                    "not need to reverse it completely — here it slows a "
                    "fall rather than reversing it."},
            {"text": "An upward resultant slows the DOWNWARD motion — "
                     "the skydiver keeps falling the whole time, just "
                     "much more slowly than before.", "correct": True},
            {"text": "The flaw is that parachutes do not create any "
                     "upward force at all.", "correct": False,
             "why": "The parachute genuinely does create a large upward "
                    "force for a short time; the flaw is in what that "
                    "force is assumed to do to the motion."},
            {"text": "The flaw is that the skydiver's weight disappears "
                     "once the parachute opens.", "correct": False,
             "why": "Weight is unaffected by the parachute opening; only "
                    "the resistance changes suddenly."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h18",
        "band": "harder",
        "text": "A student claims: 'Air resistance is a fixed force on "
                "any object, the same at every speed.' Explain why this "
                "cannot be right, using the fall of a single skydiver as "
                "evidence.",
        "options": [
            {"text": "The same skydiver feels almost no resistance at "
                     "first but feels resistance equal to their full "
                     "weight at a steady fall — proof it changes with "
                     "speed.", "correct": True},
            {"text": "It is right, because the skydiver's own body weight stays the same from start to finish, and a force of a fixed size must be met by a resistance of a fixed size too.",
             "correct": False,
             "why": "Weight staying constant says nothing about "
                    "resistance; resistance clearly grows as the "
                    "skydiver's own fall speeds up."},
            {"text": "It is right, but only because the air gets thinner "
                     "as the skydiver falls.", "correct": False,
             "why": "The change described (near-zero resistance rising "
                    "to match the weight) happens over the course of a "
                    "normal fall, mainly because of the changing SPEED, "
                    "not altitude."},
            {"text": "It cannot be assessed without knowing the "
                     "skydiver's exact mass.", "correct": False,
             "why": "The skydiver's own fall already shows resistance "
                    "changing dramatically at different speeds, whatever "
                    "their exact mass is."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h19",
        "band": "harder",
        "text": "A tennis ball and a table-tennis ball of the same size are dropped from a tall tower. The tennis ball is still speeding up at 25 m/s when it lands; the table-tennis ball levels off at about 9 m/s. Explain why their steady speeds differ so much.",
        "options": [
            {"text": "The table-tennis ball levels off lower because a hollow ball is pulled on less strongly by gravity than a solid one.", "correct": False,
             "why": "Gravity pulls on whatever mass is there, and the two balls have very different weights; that difference in weight is the point, not a difference in how gravity acts."},
            {"text": "At any given speed both feel similar resistance, so the lighter ball's small weight is matched at a much lower speed than the heavier ball's.",
             "correct": True},
            {"text": "The table-tennis ball meets far more air resistance at every speed, because its thin shell catches the air as it falls.", "correct": False,
             "why": "The two balls are the same size, so at a given speed each pushes aside about the same amount of air; what differs between them is the weight that resistance has to match."},
            {"text": "Both balls have the same steady speed, and the difference must lie in how each one was released from the tower.", "correct": False,
             "why": "The two measured speeds are plainly different, and how a ball is released cannot change the speed at which resistance finally matches its weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h20",
        "band": "harder",
        "text": "A shot-put ball and a football of similar size are both "
                "thrown with the same force. Explain which travels "
                "further before landing, and why.",
        "options": [
            {"text": "The football, because heavier objects always and "
                     "without exception experience more air resistance "
                     "than lighter ones do.", "correct": False,
             "why": "At a similar size, the resistance on each is "
                    "roughly similar; it is the DIFFERENCE in weight that "
                    "matters, not a difference in resistance."},
            {"text": "They travel the same distance, since they were "
                     "thrown with the same force.", "correct": False,
             "why": "The same starting force does not cancel out how "
                    "differently resistance, relative to weight, affects "
                    "each object's path."},
            {"text": "The shot-put — at similar sizes the resistance is "
                     "similar, but it is a far smaller share of the "
                     "shot-put's much greater weight.", "correct": True},
            {"text": "The football, because its lighter weight lets it "
                     "fly further unaffected.", "correct": False,
             "why": "The football's LOW weight means resistance affects "
                    "its path MORE, not less, cutting its distance rather "
                    "than extending it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h21",
        "band": "harder",
        "text": "A canoe and a much larger cargo ship are compared as "
                "they both move through water at the same speed. Explain "
                "why the cargo ship needs proportionally less power per "
                "tonne of its own weight to keep moving, in terms of "
                "resistance.",
        "options": [
            {"text": "Because large ships experience no water resistance "
                     "at their size.", "correct": False,
             "why": "Large ships experience very real water resistance; "
                    "it is simply small relative to their enormous "
                    "weight, compared with a canoe."},
            {"text": "Because a cargo ship's engines are built far more powerful than a canoe's, and a bigger engine drives a hull through water using less power for each tonne it carries.", "correct": False,
             "why": "Powerful engines are a consequence of this "
                    "relationship, not the explanation for it — the "
                    "question asks about power NEEDED PER TONNE."},
            {"text": "As a ship's size grows its weight grows faster "
                     "than the extra resistance from its bigger surface, "
                     "so resistance is a smaller share of its weight.",
             "correct": True},
            {"text": "Because water resistance depends mainly on a vessel's colour and paintwork, and a freshly painted hull slips through the water rather more easily.", "correct": False,
             "why": "Colour and paintwork have negligible effect; the "
                    "relationship between size, weight and resistance is "
                    "what matters here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h22",
        "band": "harder",
        "text": "A sycamore seed spins gently to the ground while a "
                "similarly sized pebble falls quickly. Explain the "
                "difference in terms of the balance between weight and "
                "resistance.",
        "options": [
            {"text": "The seed experiences no air resistance because it "
                     "is so light.", "correct": False,
             "why": "The seed's light weight is exactly why resistance is "
                    "able to match it so easily and quickly, not a sign "
                    "that no resistance is acting."},
            {"text": "The pebble falls quickly because gravity pulls "
                     "noticeably harder on rougher, less smooth surfaces "
                     "than it does on smooth ones.", "correct": False,
             "why": "Gravity's pull depends on mass, not on surface "
                    "texture; the difference here is about weight and "
                    "shape, not roughness."},
            {"text": "They should fall at the same rate, since they are "
                     "similar sizes.", "correct": False,
             "why": "Being a similar SIZE does not mean similar WEIGHT, "
                    "and it is the weight that decides how quickly "
                    "resistance can catch up."},
            {"text": "The seed's tiny weight is quickly matched by "
                     "resistance on its wide shape, while the heavier "
                     "pebble needs far more speed first.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h23",
        "band": "harder",
        "text": "An engineer is designing a new delivery van and wants to "
                "improve its fuel economy at motorway speeds without "
                "changing its carrying capacity. Evaluate whether "
                "smoothing the front and roof of the van would help, and "
                "why.",
        "options": [
            {"text": "It would not help, since only the van's weight "
                     "affects its fuel economy.", "correct": False,
             "why": "Air resistance is a major factor in fuel use at "
                    "motorway speeds, independent of the van's weight."},
            {"text": "It would help — a smoother shape cuts the air "
                     "resistance the engine must overcome, without "
                     "shrinking the load space.", "correct": True},
            {"text": "It would help, but only by making the van lighter.",
             "correct": False,
             "why": "Smoothing the shape does not meaningfully change the "
                    "van's weight; it changes how much air resistance it "
                    "experiences."},
            {"text": "It would make things considerably worse, since "
                     "smoother shapes always increase resistance rather "
                     "than reduce it.", "correct": False,
             "why": "A smoother, more tapered shape typically REDUCES "
                    "resistance compared with a boxy one, at the same "
                    "frontal size."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h24",
        "band": "harder",
        "text": "A company wants to design a bicycle helmet that reduces "
                "wind resistance for time-trial cyclists. Evaluate two "
                "design ideas: (1) a smooth, elongated tail shape, and "
                "(2) lots of small vents and ridges across the surface.",
        "options": [
            {"text": "Idea (2) is better, since more surface detail breaks the air into smaller streams and lets it slide past the helmet more easily.", "correct": False,
             "why": "More surface detail, such as vents and ridges, tends "
                    "to disturb smooth airflow and can INCREASE "
                    "resistance rather than reduce it."},
            {"text": "Both ideas would have no effect, since helmets are "
                     "too small to matter.", "correct": False,
             "why": "Even a small object's shape affects the airflow "
                    "around a fast-moving cyclist's head, and helmet "
                    "design is taken seriously for exactly this reason."},
            {"text": "Idea (1) — a smooth tapered shape lets air flow "
                     "past cleanly, while vents and ridges disturb the "
                     "airflow and add resistance.", "correct": True},
            {"text": "Idea (1) is worse, because a longer, more elongated helmet weighs considerably more, and that extra weight pressing down on the rider costs time over a long trial.", "correct": False,
             "why": "The relevant effect here is on AIR RESISTANCE from "
                    "shape, not on weight, and a smooth tapered shape "
                    "reduces resistance."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h25",
        "band": "harder",
        "text": "A manufacturer proposes fitting small fins to the back "
                "of delivery lorries to reduce the turbulent air pocket "
                "that forms behind a boxy trailer. Evaluate whether this "
                "is likely to improve fuel economy.",
        "options": [
            {"text": "It cannot help at all, since fuel economy depends "
                     "only on the engine.", "correct": False,
             "why": "Air resistance, including turbulence behind the "
                    "vehicle, is a major factor in fuel use, independent "
                    "of the engine itself."},
            {"text": "It will make things worse, since any extra "
                     "fitting bolted onto a lorry always adds more "
                     "resistance than it could ever remove.",
             "correct": False,
             "why": "The fins are specifically shaped to smooth the "
                    "airflow and reduce the turbulent pocket, which can "
                    "reduce OVERALL resistance despite being an added "
                    "part."},
            {"text": "It is likely to help — smoothing the turbulent "
                     "pocket behind a boxy trailer can meaningfully cut "
                     "the lorry's overall resistance.", "correct": True},
            {"text": "It will only help if the lorry is painted a "
                     "lighter colour.", "correct": False,
             "why": "Paint colour has no bearing on air resistance; the "
                    "shape of the airflow behind the lorry is what "
                    "matters here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h26",
        "band": "harder",
        "text": "A shoe company markets running shoes with a smooth, "
                "tapered heel shape instead of a blocky one, claiming it "
                "'cuts through the air.' Evaluate this claim in terms of "
                "resistance, given how slowly a runner's feet move "
                "compared with their overall body.",
        "options": [
            {"text": "The claim is definitely true, since any smoother "
                     "shape always meaningfully reduces total "
                     "resistance.", "correct": False,
             "why": "A small part of the body moving through air, like a "
                    "shoe, contributes very little compared with the much "
                    "larger torso and limbs facing the airflow."},
            {"text": "Almost certainly overstated — the body's much "
                     "larger frontal area faces far more resistance than "
                     "a shoe ever could.", "correct": True},
            {"text": "The claim is false, because shoes experience "
                     "absolutely no air resistance whatsoever while "
                     "running.", "correct": False,
             "why": "Shoes do experience some resistance; the issue is "
                    "that it is a tiny fraction of the runner's TOTAL "
                    "resistance, not that it is exactly zero."},
            {"text": "The claim is true, because heavier shoes always "
                     "create more resistance.", "correct": False,
             "why": "Weight is not what determines resistance; shape and "
                    "area do, and the claim is about the shoe's SHAPE, "
                    "not its weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h27",
        "band": "harder",
        "text": "A skydiver's parachute opens and for about two seconds "
                "the resultant force on them points upwards, before "
                "settling back to 0 N. Describe what happens to their "
                "velocity during those two seconds, and afterwards.",
        "options": [
            {"text": "They rise upwards during the two seconds, then fall "
                     "back down afterwards.", "correct": False,
             "why": "An upward resultant on a falling object slows the "
                    "fall; it does not reverse it into an actual rise."},
            {"text": "Their weight becomes negative for those two "
                     "seconds.", "correct": False,
             "why": "Weight is unaffected by the parachute; only the "
                    "balance between weight and resistance changes."},
            {"text": "Their speed stays exactly the same throughout, since a parachute changes the area facing the air and it is the skydiver's weight that sets how fast they come down.", "correct": False,
             "why": "The whole point of the parachute is to change the "
                    "resistance sharply, which does change the skydiver's "
                    "speed a great deal."},
            {"text": "Their downward speed drops sharply as the upward "
                     "resultant slows the fall, then they always continue "
                     "moving down, never up, at a new steady speed.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h28",
        "band": "harder",
        "text": "An aircraft's engines suddenly cut out mid-flight, and "
                "for a moment the resultant force on it points downwards "
                "even though it briefly keeps climbing due to its "
                "existing upward motion. Explain how this is possible.",
        "options": [
            {"text": "It is not possible at all; a downward resultant "
                     "must make any aircraft descend immediately and "
                     "without any delay whatsoever.", "correct": False,
             "why": "A resultant force changes motion gradually, over "
                    "time; it does not switch the direction of travel the "
                    "instant it appears."},
            {"text": "A downward resultant slows the climb gradually and "
                     "eventually turns it into a descent — it never has "
                     "to reverse the motion instantly.", "correct": True},
            {"text": "The aircraft's weight has temporarily increased, "
                     "forcing it down.", "correct": False,
             "why": "Weight has not changed at all; what has changed is "
                    "the balance of forces now acting without engine "
                    "thrust."},
            {"text": "This shows the aircraft is not really affected by "
                     "gravity at all.", "correct": False,
             "why": "Gravity is exactly what is now unopposed by engine "
                    "thrust, which is why a downward resultant has "
                    "appeared."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h29",
        "band": "harder",
        "text": "A drag racing car deploys its rear parachute at very "
                "high speed. For a short time the resultant force points "
                "backwards very strongly, yet the car keeps travelling "
                "forwards the whole time. Explain how both of these can "
                "be true.",
        "options": [
            {"text": "It cannot possibly be true; a backward force "
                     "acting on a car must always mean the car itself is "
                     "moving backwards.", "correct": False,
             "why": "A resultant force changes existing motion gradually; "
                    "the car decelerates forward before it would ever "
                    "reverse, and in practice it stops well before that."},
            {"text": "The car speeds up because two forces are now acting "
                     "on it.", "correct": False,
             "why": "A resultant force in one direction changes the "
                    "motion in that direction; here it slows the car "
                    "rather than speeding it up."},
            {"text": "The parachute makes the car's weight point "
                     "backwards instead of down.", "correct": False,
             "why": "Weight always points downwards, from gravity; the "
                    "parachute affects the resistance, not the direction "
                    "of the car's weight."},
            {"text": "A backward resultant slows the car's forward "
                     "motion rapidly, but its speed never switches to "
                     "reverse instantly — it simply decelerates.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h30",
        "band": "harder",
        "text": "A cyclist coasting downhill at increasing speed suddenly "
                "opens a large golfing umbrella facing forwards. For a "
                "moment the resultant force points backwards strongly. "
                "Describe what happens next, and correct the idea that "
                "the cyclist would immediately start moving backwards.",
        "options": [
            {"text": "The cyclist immediately starts moving backwards the instant the resultant force begins pointing that way, because the direction of the resultant is the direction of travel.", "correct": False,
             "why": "A resultant force changes existing motion gradually; "
                    "the cyclist decelerates forwards rather than "
                    "instantly reversing."},
            {"text": "The cyclist's forward speed drops rapidly from the "
                     "backward resultant, but they keep moving forwards "
                     "the whole time, simply slowing down.",
             "correct": True},
            {"text": "Nothing changes, since opening an umbrella cannot create a real force, and only the brakes or the road could alter how fast the cyclist is going.", "correct": False,
             "why": "The umbrella dramatically increases the resistance "
                    "facing the cyclist, creating a very real backward "
                    "force."},
            {"text": "The cyclist's weight increases because of the extra "
                     "resistance.", "correct": False,
             "why": "Weight is unrelated to the umbrella; only the "
                    "resistance (and hence the resultant) has changed."},
        ],
        "figure": None,
    },
]
