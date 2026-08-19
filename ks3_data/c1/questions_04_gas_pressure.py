"""C1 lesson 04 — Gas pressure: twelve questions (MRB-269).

These probe the single claim the lesson is built on — pressure is a count of
collisions with the wall, and nothing else. The distractors come from the two
declared misconceptions: PART-08 (gas pressure is the particles pushing against
each other), which the bench's grey rings exist to confront, and PART-09
(heating makes the particles swell up), which the lesson calls the right answer
for the wrong reason. Three more are lifted from the lesson's own corrections:
that an "empty" can is full of gas, that pumping a tyre adds particles rather
than squashing the air, and the stretch layer's flat statement that nothing
sucks — things get pushed, from the side where there are more particles. The
`standard` band works the bench a student has actually used, including reading a
pressure off its stated 7 kPa-per-hit calibration. The `harder` band compares
two boxes quantitatively (where "the particles get in each other's way" is
PART-08 dressed as arithmetic), takes the idea to a crisp packet on a mountain
and a vacuum-packed brick of coffee, and hands back a swelling explanation that
reaches the right answer so the error has to be found inside it.
"""

UNIT = "C1"
LESSON = "gas-pressure"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c1-04-e01",
        "band": "easier",
        "text": "The bench can mark particle-to-particle bumps in the middle "
                "of the box with grey rings. There are plenty of them, and the "
                "wall-hit count ignores every single one. Why?",
        "options": [
            {"text": "Grey bumps are too gentle to be worth counting, so the "
                     "bench leaves them out of the total.",
             "correct": False,
             "why": "The bench is not filtering out weak collisions. It counts "
                    "collisions with the wall, and those bumps happen nowhere "
                    "near a wall."},
            {"text": "Pressure is only ever what arrives at the wall, and "
                     "those bumps never touch it.",
             "correct": True},
            {"text": "They do add to the pressure, but the bench cannot draw "
                     "them and count them at the same time.",
             "correct": False,
             "why": "Nothing is being hidden from you. Particles bumping each "
                    "other in the middle of the box do nothing to the "
                    "container, because the wall never feels them."},
            {"text": "Particles only bump into each other when the gas is "
                     "hot, so most settings have none of them.",
             "correct": False,
             "why": "Turn the rings on with the gas set to Cold and they are "
                    "still there. Temperature changes how fast particles "
                    "move, not whether they meet."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e02",
        "band": "easier",
        "text": "Shake an aerosol can that has stopped spraying and it sounds "
                "empty; press the nozzle and nothing comes out. What is "
                "actually inside it?",
        "options": [
            {"text": "Gas — it was in there the whole time, and a sealed can "
                     "cannot have nothing in it.",
             "correct": True},
            {"text": "Nothing at all, which is why a can like this is safe to "
                     "throw on a bonfire.",
             "correct": False,
             "why": "An “empty” can is full of gas, and heating that "
                    "gas is exactly what bursts it. The warning printed on "
                    "the can is not decoration."},
            {"text": "A vacuum, because the propellant carried every last "
                     "particle out with it.",
             "correct": False,
             "why": "The spray stops when the pressure inside has dropped to "
                    "match the air outside, not when the can runs out of "
                    "particles. There are still plenty in there."},
            {"text": "Only paint and metal, because a gas has to come from a "
                     "liquid boiling inside.",
             "correct": False,
             "why": "Gas does not need a liquid to come from. What is left in "
                    "the can is gas, and it hits the walls exactly as any "
                    "other gas would."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e03",
        "band": "easier",
        "text": "The bench draws one reference particle at the bottom left, "
                "and it stays exactly the same size whether you set the gas to "
                "Cold, Warm or Hot. What is it there to prove?",
        "options": [
            {"text": "That the bench draws every particle at one size, simply "
                     "to keep the picture tidy.",
             "correct": False,
             "why": "It is not a drawing convenience. It is showing you a "
                    "fact: the size of a particle does not depend on the "
                    "temperature."},
            {"text": "That particles are far too small for any change in "
                     "their size to be visible.",
             "correct": False,
             "why": "The point is not that the change is too small to see. "
                    "There is no change at all — heating alters speed and "
                    "nothing else."},
            {"text": "That the particles nearest the wall are the same size "
                     "as the ones in the middle.",
             "correct": False,
             "why": "That was never in doubt. The reference particle is held "
                    "against the temperature setting, because temperature is "
                    "what the swelling idea claims changes it."},
            {"text": "That heating changes how fast the particles move and "
                     "never how big they are.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e04",
        "band": "easier",
        "text": "A sealed glass jar of gas is left in a freezer overnight. "
                "What happens to the collisions on the inside of the jar?",
        "options": [
            {"text": "More each second, because cold particles sink and crowd "
                     "the bottom of the jar.",
             "correct": False,
             "why": "Cooling does not gather the particles anywhere. It slows "
                    "them down, so they reach the walls less often than "
                    "before."},
            {"text": "The same number each second, but every one of them is "
                     "softer than before.",
             "correct": False,
             "why": "Cooling changes both things at once. Slower particles "
                    "arrive less often as well as hitting more gently, so the "
                    "count falls too."},
            {"text": "Fewer each second and each one softer, so the pressure "
                     "inside the jar falls.",
             "correct": True},
            {"text": "Fewer each second but harder, because shrunken "
                     "particles can build up more speed.",
             "correct": False,
             "why": "Particles do not shrink when cooled, any more than they "
                    "swell when heated. Slower particles hit more gently, not "
                    "harder."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c1-04-s01",
        "band": "standard",
        "text": "The bench turns the wall-hit count into a pressure at 7 kPa "
                "for every hit per second, so the resting setting's 14 hits a "
                "second reads about 100 kPa — the pressure of the air in the "
                "room. You change one control and the count settles at 20 hits "
                "a second. What does the pressure read?",
        "options": [
            {"text": "About 107 kPa: each hit above the resting count adds "
                     "another 7 kPa on top of the room's 100.",
             "correct": False,
             "why": "The 100 kPa is not a starting offset to add to. It is "
                    "what 14 hits a second already works out to, so 20 hits "
                    "means 20 × 7."},
            {"text": "About 100 kPa still, because the air in the room "
                     "outside the box has not changed at all.",
             "correct": False,
             "why": "The bar reads the pressure inside the box, which is the "
                    "collisions on its own walls. The air outside plays no "
                    "part in that number."},
            {"text": "About 140 kPa, because the reading is the hit count "
                     "multiplied by 7 at every setting.",
             "correct": True},
            {"text": "Somewhere between 100 and 140 kPa, because pressure "
                     "rises more slowly once the count is high.",
             "correct": False,
             "why": "There is no flattening off. Pressure is exactly "
                    "proportional to the hit rate, so double the hits is "
                    "double the pressure at every setting."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s02",
        "band": "standard",
        "text": "On the bench you press “Show particle-to-particle "
                "bumps” and grey rings appear all over the middle of the "
                "box. What happens to the wall-hit count on screen?",
        "options": [
            {"text": "Nothing changes — those bumps were happening already, "
                     "and the button only draws them.",
             "correct": True},
            {"text": "It rises, because those collisions are now being "
                     "included in the total on screen.",
             "correct": False,
             "why": "They are never included, drawn or not. The count is "
                    "collisions with the wall, and a bump in the middle of "
                    "the box is not one of those."},
            {"text": "It falls, because particles that bump each other are "
                     "turned away before they reach a wall.",
             "correct": False,
             "why": "A bump sends a particle off in a new direction, but it "
                    "does not take it out of the box. Arrivals at the wall "
                    "carry on at the same rate."},
            {"text": "It rises and then settles, because drawing all those "
                     "rings slows the gas down a little.",
             "correct": False,
             "why": "The button changes what you can see, not how the gas "
                    "behaves. How fast the particles move is set by the "
                    "temperature control alone."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s03",
        "band": "standard",
        "text": "If heating a gas really did make its particles swell up, "
                "there is one thing a hot gas would do that it does not "
                "actually do. What is it?",
        "options": [
            {"text": "It would cool back down quickly, because bigger "
                     "particles lose their heat faster.",
             "correct": False,
             "why": "The swelling idea says nothing about cooling. The test "
                    "that separates the two explanations is about how much "
                    "room the particles take up."},
            {"text": "It would push harder on the top of its container than "
                     "it does on the sides of it.",
             "correct": False,
             "why": "Pressure acts on every wall alike, whatever the "
                    "temperature. Swollen particles would have no reason to "
                    "pick one direction."},
            {"text": "It would weigh more than the same gas when cold, "
                     "because every particle is bigger.",
             "correct": False,
             "why": "Heating adds no matter. The number of particles is the "
                    "same and so is the mass, so weighing it settles "
                    "nothing."},
            {"text": "It would be harder to squash than a cold gas, because "
                     "its particles fill more of the room.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s04",
        "band": "standard",
        "text": "A student pumping up a bicycle tyre says, “I am "
                "squashing the air smaller and smaller in there.” What is "
                "actually happening as the tyre goes hard?",
        "options": [
            {"text": "The particles are being pressed down into a smaller "
                     "size, which is how they all fit in.",
             "correct": False,
             "why": "A particle never changes size. What changes is how many "
                    "of them are inside and how often they reach the wall."},
            {"text": "More particles are being forced into the same space, so "
                     "more of them reach the wall each second.",
             "correct": True},
            {"text": "The new air is being pushed into the gaps between the "
                     "particles that are already in there.",
             "correct": False,
             "why": "Those gaps are empty space, not a store you can fill. "
                    "The air is the particles — you are simply adding more of "
                    "them."},
            {"text": "The particles are pushed together until they touch, and "
                     "that is what holds the tyre out.",
             "correct": False,
             "why": "Even in a rock-hard tyre the particles are far apart and "
                    "still flying about. The tyre is held out by their "
                    "collisions, not by particles touching."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c1-04-h01",
        "band": "harder",
        "text": "Two sealed boxes are exactly the same size and both sit at "
                "room temperature. Box A holds 24 particles; box B holds 48. "
                "Which comparison is right?",
        "options": [
            {"text": "The two pressures are equal, because both boxes are at "
                     "the same temperature as each other.",
             "correct": False,
             "why": "Temperature fixes how fast the particles travel, not how "
                    "many of them arrive. Twice as many particles means twice "
                    "as many arrivals each second."},
            {"text": "B's particles are moving faster, because a crowded box "
                     "makes them speed up.",
             "correct": False,
             "why": "Crowding changes no particle's speed — only temperature "
                    "does that. B has more arrivals per second, each one "
                    "hitting just as hard as A's."},
            {"text": "B's pressure is a little higher but nothing like "
                     "double, as its particles get in each other's way.",
             "correct": False,
             "why": "Particle-to-particle bumps are exactly the collisions "
                    "the wall never feels, so they cannot hold the pressure "
                    "back. B reads about double."},
            {"text": "B's wall-hit count is about double A's, so B's pressure "
                     "is about double as well.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h02",
        "band": "harder",
        "text": "A sealed bag of crisps is driven up a mountain. Nobody opens "
                "it and nothing heats it, yet by the top it is puffed tight "
                "enough to look ready to split. What has changed?",
        "options": [
            {"text": "The air inside has warmed in the sun, and warm air "
                     "takes up more room than cold air.",
             "correct": False,
             "why": "Nothing heated it — the air on a mountain is colder, and "
                    "cooling would slacken the bag rather than tighten it. "
                    "The change is outside the bag."},
            {"text": "Up there the outside air is thinner, so fewer particles "
                     "hit the bag from outside than from within.",
             "correct": True},
            {"text": "The particles inside have swollen in the thinner air, "
                     "and that is what stretches the bag out.",
             "correct": False,
             "why": "Particles never swell — not when heated, and not with "
                    "height either. The bag stretches because the outside is "
                    "pushing back less than before."},
            {"text": "The thin air at the summit sucks the bag outwards from "
                     "every side until it is tight.",
             "correct": False,
             "why": "Nothing sucks, ever. The bag is pushed out by the "
                    "collisions inside it, and it bulges because there is "
                    "less pushing in from outside."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h03",
        "band": "harder",
        "text": "A student writes: “Heat a sealed can and the particles "
                "gain energy and spread out to fill more of the can, so they "
                "are packed tighter against the walls and the pressure "
                "rises.” The final claim is right. Which part is wrong?",
        "options": [
            {"text": "That the pressure rises. Heating a sealed can that "
                     "cannot change size leaves the pressure alone.",
             "correct": False,
             "why": "The pressure genuinely does rise. Getting the right "
                    "answer is what makes this explanation so hard to shift — "
                    "the reasoning is the faulty part."},
            {"text": "That the particles gain energy. Heating a gas gives the "
                     "particles nothing they did not have.",
             "correct": False,
             "why": "Heating really does give the particles more energy, and "
                    "you see it as speed. The error arrives in what the "
                    "student says happens next."},
            {"text": "That they spread out and pack tighter. They already "
                     "fill the can, and only their speed changes.",
             "correct": True},
            {"text": "That the can is sealed. This can only work if extra gas "
                     "is able to get in while it heats.",
             "correct": False,
             "why": "Sealed is the whole point. No particles are added, so "
                    "the extra pressure has to come from the ones already in "
                    "there moving faster."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h04",
        "band": "harder",
        "text": "A vacuum-packed brick of coffee is rock hard, even though the "
                "grounds inside it are loose powder. Snip off one corner and "
                "it goes soft straight away. Why?",
        "options": [
            {"text": "Air particles are pushed in through the hole until both "
                     "faces of the plastic are hit equally often.",
             "correct": True},
            {"text": "The hole lets the coffee's own pressure escape, and "
                     "that pressure was holding the brick hard.",
             "correct": False,
             "why": "There was almost no gas inside to escape — the air was "
                    "drawn out at the factory. The hardness came from air "
                    "outside pushing in."},
            {"text": "The vacuum inside sucks air in through the hole until "
                     "the packet is full again.",
             "correct": False,
             "why": "A vacuum cannot pull on anything, because there is "
                    "nothing in it to do the pulling. Outside air is pushed "
                    "in by its own collisions."},
            {"text": "The plastic relaxes once it is cut, and stretched "
                     "plastic was what kept the brick stiff.",
             "correct": False,
             "why": "The plastic is limp on its own once the packet is open. "
                    "What made the brick rigid was outside air colliding with "
                    "it and almost nothing colliding back."},
        ],
        "figure": None,
    },
]
