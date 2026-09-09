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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-04-e05",
        "band": "easier",
        "text": "What does the word pressure mean?",
        "options": [
            {"text": "How much a gas weighs in its container.",
             "correct": False,
             "why": "Weight is a different quantity. Pressure is about how "
                    "hard the pushing is on each bit of surface."},
            {"text": "How fast the particles of a gas are moving about.",
             "correct": False,
             "why": "Speed is part of what causes pressure, but it is not "
                    "what pressure means."},
            {"text": "How much space a gas takes up.",
             "correct": False,
             "why": "That is volume. A gas can be at high or low pressure in "
                    "the same volume."},
            {"text": "How hard a force pushes on each bit of a surface.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e06",
        "band": "easier",
        "text": "The bench counts collisions. What is a collision?",
        "options": [
            {"text": "When a moving particle hits something and bounces off.",
             "correct": True},
            {"text": "A particle being destroyed as it reaches the wall.",
             "correct": False,
             "why": "Nothing is destroyed. The particle bounces and carries "
                    "on."},
            {"text": "A particle sticking to the wall and staying there.",
             "correct": False,
             "why": "If particles stuck, the count would fall to nothing "
                    "within seconds. They bounce off."},
            {"text": "Two particles joining together to make a bigger one.",
             "correct": False,
             "why": "Particles do not join or grow in this unit. A collision "
                    "is a hit followed by a bounce."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e07",
        "band": "easier",
        "text": "The bench lets you change three things about the gas. Which "
                "of these is NOT one of them?",
        "options": [
            {"text": "The temperature",
             "correct": False,
             "why": "This is one of the three, and it is the control that "
                    "changes how fast the particles move."},
            {"text": "The size of the particles",
             "correct": True},
            {"text": "The size of the container",
             "correct": False,
             "why": "This is one of the three. Shrink the box and each "
                    "particle reaches a wall sooner."},
            {"text": "The number of particles",
             "correct": False,
             "why": "This is one of the three. Take particles out and fewer "
                    "arrive at the wall each second."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e08",
        "band": "easier",
        "text": "Half the particles are removed from a sealed container, and "
                "the temperature and the container stay exactly the same. What "
                "happens to the pressure?",
        "options": [
            {"text": "It stays the same, because each particle now has more "
                     "room to build up speed.",
             "correct": False,
             "why": "Temperature sets the speed, and it has not changed. Each "
                    "remaining particle behaves exactly as before — there are "
                    "simply fewer of them."},
            {"text": "It rises, because the particles have further to travel "
                     "and hit harder.",
             "correct": False,
             "why": "A longer trip means a particle reaches the wall LESS "
                    "often, and it hits no harder. Fewer arrivals means less "
                    "pressure."},
            {"text": "It falls to about half.",
             "correct": True},
            {"text": "It falls to nothing, because half the gas has gone.",
             "correct": False,
             "why": "Half the particles are still there, still moving, still "
                    "hitting the wall. Half the gas gives about half the "
                    "pressure, not none."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e09",
        "band": "easier",
        "text": "A gas is heated. What happens to its particles?",
        "options": [
            {"text": "They swell up and fill more of the container.",
             "correct": False,
             "why": "Particles never change size. The reference particle on "
                    "the bench is drawn to prove it."},
            {"text": "There are more of them, because heat makes new ones.",
             "correct": False,
             "why": "Heating creates nothing. The same particles are there "
                    "before and after."},
            {"text": "They move apart until they are touching the walls.",
             "correct": False,
             "why": "In a sealed container the gas already fills it. What "
                    "heating changes is speed, not spacing."},
            {"text": "They move faster.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c1-04-s05",
        "band": "standard",
        "text": "The bench reads 14 wall hits per second. The container is "
                "made half its size and nothing else is touched. What should "
                "the count settle at?",
        "options": [
            {"text": "About 7 per second, because there is half as much "
                     "space.",
             "correct": False,
             "why": "Less space means each particle gets back to a wall "
                    "sooner, so the count goes UP rather than down."},
            {"text": "About 14 per second, because no particles were added "
                     "and none were removed.",
             "correct": False,
             "why": "The number of particles is only one of the three "
                    "controls. Moving the walls closer changes the count "
                    "without changing the number."},
            {"text": "About 196 per second, because the count is squared.",
             "correct": False,
             "why": "Nothing here is squared. Halving the space roughly "
                    "doubles how often each particle arrives."},
            {"text": "About 28 per second, because each particle reaches a "
                     "wall twice as often.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s06",
        "band": "standard",
        "text": "A rubber suction cup pressed onto a wall holds a shelf up. "
                "What is holding it there?",
        "options": [
            {"text": "Air particles outside hitting it, with almost none "
                     "behind it to push back.",
             "correct": True},
            {"text": "The rubber sucking the air out and pulling itself hard "
                     "against the wall.",
             "correct": False,
             "why": "Nothing sucks. Squeezing the cup pushes air out; what "
                    "holds it is the air outside pushing in."},
            {"text": "The stickiness of the rubber against the smooth "
                     "surface.",
             "correct": False,
             "why": "A dry suction cup is not sticky, and it falls off the "
                    "moment air gets behind it."},
            {"text": "The vacuum behind the cup pulling on it.",
             "correct": False,
             "why": "A vacuum is nothing, and nothing cannot pull. The push "
                    "comes from the side where the particles are."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s07",
        "band": "standard",
        "text": "The air above you pushes down with about the weight of a "
                "tonne on your shoulders. Why can you not feel it?",
        "options": [
            {"text": "Because your skin is far too thick to notice a push as "
                     "gentle as that.",
             "correct": False,
             "why": "A tonne is not gentle. It is unnoticed because it is "
                    "balanced, not because it is small."},
            {"text": "Because the same pressure pushes out from inside you, "
                     "and the two balance.",
             "correct": True},
            {"text": "Because air is far too light to push on anything.",
             "correct": False,
             "why": "Air is made of particles and they hit you constantly. "
                    "Their combined push is enormous."},
            {"text": "Because you only feel a push when something is moving.",
             "correct": False,
             "why": "A book resting on your hand is not moving and you feel "
                    "it. What matters here is that the push is matched from "
                    "the other side."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s08",
        "band": "standard",
        "text": "A balloon left on a car's back seat on a hot day bursts, "
                "although nobody has touched it. Using the collision count, "
                "why?",
        "options": [
            {"text": "The rubber was weakened by the sun, so the pressure it "
                     "already held was enough to burst it.",
             "correct": False,
             "why": "Warm rubber actually stretches more easily rather than "
                    "less. The change that matters is inside the balloon."},
            {"text": "More air got in through the neck as the balloon warmed "
                     "up.",
             "correct": False,
             "why": "The balloon is tied. No particles were added, and none "
                    "need to be."},
            {"text": "The particles inside sped up, hitting the rubber more "
                     "often and harder, until it gave way.",
             "correct": True},
            {"text": "The particles inside got bigger and needed more room.",
             "correct": False,
             "why": "Particles never change size. Heating changes how fast "
                    "they move and nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s09",
        "band": "standard",
        "text": "A student says the pressure inside a sealed can comes from "
                "the weight of the gas pressing down. Which observation deals "
                "with that best?",
        "options": [
            {"text": "Gas has almost no weight, so it could not press "
                     "anywhere.",
             "correct": False,
             "why": "Gas does have mass and does have weight. The point is "
                    "that weight acts downwards and pressure acts in every "
                    "direction."},
            {"text": "The can weighs the same whether the pressure is high or "
                     "low.",
             "correct": False,
             "why": "Pumping more gas in does make the can heavier. What "
                    "rules weight out is the direction the pressure acts."},
            {"text": "The pressure changes when the can is heated, and "
                     "heating does not change the weight.",
             "correct": False,
             "why": "True, and it does count for something — but the "
                    "sharpest evidence is that the push is just as strong "
                    "upwards on the lid."},
            {"text": "The pressure pushes on the top and sides of the can as "
                     "hard as on the bottom.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-04-h05",
        "band": "harder",
        "text": "Two sealed boxes are the same size and hold the same number "
                "of particles. Box A is at 20 °C and box B at 80 °C. How do "
                "their wall hits compare?",
        "options": [
            {"text": "B's particles arrive more often, but each hit is just "
                     "as gentle as A's.",
             "correct": False,
             "why": "Half the story. Faster particles arrive more often AND "
                    "carry more punch when they get there."},
            {"text": "B's hits are harder, but they arrive no more often than "
                     "A's.",
             "correct": False,
             "why": "The other half. A faster particle crosses the box in "
                    "less time, so it also arrives more often."},
            {"text": "The counts are the same, because the boxes hold the same "
                     "number of particles.",
             "correct": False,
             "why": "The number is only one control of three. Temperature is "
                    "another, and it has been changed."},
            {"text": "B's particles arrive more often and each hit is harder, "
                     "so B's pressure is higher.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h06",
        "band": "harder",
        "text": "A gas sits at 100 kPa in a 2-litre sealed box. It is pushed "
                "into a 1-litre box at the same temperature, with no particles "
                "lost. What is the best estimate of the new pressure?",
        "options": [
            {"text": "200 kPa",
             "correct": True},
            {"text": "50 kPa",
             "correct": False,
             "why": "That is dividing where you should multiply. Half the "
                    "space means each particle reaches a wall more often, not "
                    "less."},
            {"text": "100 kPa",
             "correct": False,
             "why": "Nothing would have changed only if the box had stayed "
                    "the same size. Moving the walls in raises the hit count "
                    "on its own."},
            {"text": "400 kPa",
             "correct": False,
             "why": "That is doubling twice. The volume was halved once, so "
                    "the pressure roughly doubles once."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h07",
        "band": "harder",
        "text": "An aerosol can that no longer sprays is thrown onto a "
                "bonfire and bursts. Put the reason in the right order.",
        "options": [
            {"text": "The metal weakens in the heat, so the pressure inside "
                     "no longer has to rise for the can to fail.",
             "correct": False,
             "why": "The metal does soften, but the can bursts outwards, "
                    "which needs a rising pressure inside to do the "
                    "bursting."},
            {"text": "The gas inside is heated, so the particles move faster, "
                     "so they hit the walls more often and harder, so the "
                     "pressure rises until the can gives way.",
             "correct": True},
            {"text": "The gas inside is heated, so the particles swell up, so "
                     "they press harder against the walls of the can, so the "
                     "pressure rises and the can gives way.",
             "correct": False,
             "why": "The last step is right and the middle one is not. "
                    "Particles never swell — they simply move faster."},
            {"text": "The fire forces extra air in through the nozzle, so "
                     "there are more particles, so the pressure rises.",
             "correct": False,
             "why": "Nothing gets in through a closed valve, and the "
                    "pressure inside is already higher than outside. No "
                    "particles are added."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h08",
        "band": "harder",
        "text": "A sealed syringe is pushed in, released, and springs back "
                "out; then it is pulled out, released, and springs back in. "
                "Which explanation covers both?",
        "options": [
            {"text": "The gas inside pulls the plunger back when stretched "
                     "and pushes it back when squashed.",
             "correct": False,
             "why": "A gas never pulls. When you pull the plunger out, what "
                    "moves it back is the air OUTSIDE pushing in."},
            {"text": "The rubber seal returns to its resting shape both "
                     "times.",
             "correct": False,
             "why": "The seal only slides. Do the same with a well-oiled "
                    "metal plunger and it still springs back both ways."},
            {"text": "The plunger always returns to the point where the "
                     "pressure inside and outside are equal.",
             "correct": True},
            {"text": "Gravity returns the plunger to its resting position "
                     "each time.",
             "correct": False,
             "why": "It happens whichever way up the syringe is held, so "
                    "gravity cannot be what does it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h09",
        "band": "harder",
        "text": "A student argues: “Squeeze the gas and there are more "
                "particle-to-particle bumps, so those bumps must add to the "
                "pressure after all.” The first half is true. Why does the "
                "conclusion still fail?",
        "options": [
            {"text": "Because the bumps are too gentle to be worth counting.",
             "correct": False,
             "why": "They are no gentler than wall hits. Where they happen is "
                    "what rules them out, not how hard they are."},
            {"text": "Because there are not really any more of those bumps "
                     "when the gas is squeezed into less space.",
             "correct": False,
             "why": "There genuinely are more — the student has that right. "
                    "The error is in what follows from it."},
            {"text": "Because the bumps cancel each other out, leaving no net "
                     "push.",
             "correct": False,
             "why": "It is not a cancelling argument. The wall simply never "
                    "feels them at all."},
            {"text": "Because the bumps happen away from the wall, and "
                     "pressure is only what arrives at the wall.",
             "correct": True},
        ],
        "figure": None,
    },
    # ── easier · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c1-04-e10",
        "band": "easier",
        "text": "The pressure of a gas is measured in kilopascals. Which "
                "of these is the short way of writing that unit?",
        "options": [
            {"text": "kJ",
             "correct": False,
             "why": "kJ is kilojoules, the unit of energy. Pressure is not "
                    "an energy."},
            {"text": "kPa",
             "correct": True},
            {"text": "kg",
             "correct": False,
             "why": "kg is kilograms, the unit of mass. A gas has a mass, "
                    "but that is a different quantity."},
            {"text": "kW",
             "correct": False,
             "why": "kW is kilowatts, the unit of power. Nothing on a "
                    "pressure gauge is measured in watts."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e11",
        "band": "easier",
        "text": "The air around you at sea level pushes on every surface "
                "it touches. About what is that pressure?",
        "options": [
            {"text": "About 1 kPa, which is only a very gentle push.",
             "correct": False,
             "why": "That is about a hundredth of the real figure. "
                    "Atmospheric pressure amounts to something like a "
                    "tonne pressing on your shoulders."},
            {"text": "About 10 kPa, which is a tenth of what the bench "
                     "rests at.",
             "correct": False,
             "why": "That is about a tenth of the real figure. The air "
                    "around you pushes far harder than that."},
            {"text": "About 100 kPa, which is what the bench rests at.",
             "correct": True},
            {"text": "About 100 000 kPa, which is an enormous push.",
             "correct": False,
             "why": "That is the figure written in pascals rather than "
                    "kilopascals. A kilopascal is a thousand pascals, so "
                    "the number is a thousand times too big."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e12",
        "band": "easier",
        "text": "Which piece of equipment would you use to measure the "
                "pressure of the air inside a bicycle tyre?",
        "options": [
            {"text": "A pressure gauge",
             "correct": True},
            {"text": "A thermometer",
             "correct": False,
             "why": "A thermometer measures temperature. Temperature is "
                    "one of the things that sets a pressure, but it is not "
                    "the pressure."},
            {"text": "A measuring cylinder",
             "correct": False,
             "why": "A measuring cylinder measures the volume of a liquid. "
                    "It says nothing about how hard a gas pushes."},
            {"text": "A top-pan balance",
             "correct": False,
             "why": "A balance measures mass. A tyre has a mass whether it "
                    "is pumped up or flat."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e13",
        "band": "easier",
        "text": "The air in a room pushes on the outside of a closed "
                "window. What is that push?",
        "options": [
            {"text": "The weight of the air in the room resting against "
                     "the glass.",
             "correct": False,
             "why": "Weight acts downwards only, yet the air pushes on an "
                    "upright window just as hard as on a flat one."},
            {"text": "The air particles pushing against one another and "
                     "squeezing the glass.",
             "correct": False,
             "why": "Those bumps happen away from the glass, and the glass "
                    "never feels them. Only arrivals at the glass count."},
            {"text": "The wind outside pressing on the far side of the "
                     "glass.",
             "correct": False,
             "why": "The push is there on a perfectly still day. It comes "
                    "from the particles' own motion, not from moving air."},
            {"text": "The huge number of air particles colliding with the "
                     "glass.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e14",
        "band": "easier",
        "text": "More air is pumped into a rigid metal cylinder, and the "
                "temperature does not change. State what happens to the "
                "pressure inside.",
        "options": [
            {"text": "It stays the same, because a rigid cylinder cannot "
                     "change its size.",
             "correct": False,
             "why": "A rigid cylinder fixes the volume, not the pressure. "
                    "The extra particles still arrive at the walls."},
            {"text": "It falls, because the crowded particles slow one "
                     "another down.",
             "correct": False,
             "why": "Crowding changes no particle's speed. Only "
                    "temperature does that, and it has not been changed."},
            {"text": "It rises, because more particles arrive at the walls "
                     "each second.",
             "correct": True},
            {"text": "It rises and then falls back again, because the gas "
                     "settles into the corners.",
             "correct": False,
             "why": "A gas never settles anywhere. Its particles keep "
                    "moving in every direction and keep arriving at the "
                    "walls."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e15",
        "band": "easier",
        "text": "A sealed rigid can of gas is left alone in a room at a "
                "steady temperature for an hour. State what happens to the "
                "pressure inside it.",
        "options": [
            {"text": "It stays the same, because nothing about the gas has "
                     "changed.",
             "correct": True},
            {"text": "It falls, because the particles slowly run out of "
                     "energy.",
             "correct": False,
             "why": "Gas particles do not run down. Nothing has taken "
                    "energy from them, so they keep arriving at the walls "
                    "at the same rate."},
            {"text": "It falls, because the particles settle towards the "
                     "bottom.",
             "correct": False,
             "why": "Particles do not settle while the substance is a gas. "
                    "They travel in straight lines in every direction."},
            {"text": "It rises, because the particles gradually gather at "
                     "the walls.",
             "correct": False,
             "why": "There is nothing to gather them. They spread through "
                    "the whole can and reach the walls at a steady rate."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e16",
        "band": "easier",
        "text": "What is atmospheric pressure?",
        "options": [
            {"text": "The pressure inside a sealed container of gas before "
                     "it is heated.",
             "correct": False,
             "why": "That is the pressure of a gas someone has trapped. "
                    "Atmospheric pressure is the push of the air outside, "
                    "on everything."},
            {"text": "The pressure of the wind on a day when the weather "
                     "is stormy.",
             "correct": False,
             "why": "It is there on a perfectly still day too. The wind is "
                    "moving air; the pressure is the collisions of air "
                    "particles."},
            {"text": "The extra pressure a pump has to add before a tyre "
                     "will hold you up.",
             "correct": False,
             "why": "That is what a pump adds on top. Atmospheric pressure "
                    "is there whether anything has been pumped or not."},
            {"text": "The push of the air of the atmosphere on everything "
                     "at the surface.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e17",
        "band": "easier",
        "text": "A sealed gas is moved into a container three times the "
                "size, at the same temperature. State what happens to its "
                "pressure.",
        "options": [
            {"text": "It rises, because each particle has further to "
                     "travel and builds up more speed.",
             "correct": False,
             "why": "A longer journey means a particle reaches a wall less "
                    "often, not more, and its speed is set by the "
                    "temperature alone."},
            {"text": "It falls, because each particle now takes longer to "
                     "reach a wall.",
             "correct": True},
            {"text": "It stays the same, because no particles have been "
                     "added or taken away.",
             "correct": False,
             "why": "The number of particles is only one of the things a "
                    "pressure depends on, and the space they are in has "
                    "trebled."},
            {"text": "It falls to nothing, because the gas spreads until "
                     "it is too thin to push.",
             "correct": False,
             "why": "However much room a gas is given, its particles still "
                    "reach the walls and still push. The pressure falls; "
                    "it does not vanish."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e18",
        "band": "easier",
        "text": "A gas is described as being at low pressure. State what "
                "that tells you about the collisions on the inside of its "
                "container.",
        "options": [
            {"text": "Particles arrive less often, or hit less hard, or "
                     "both.",
             "correct": True},
            {"text": "The particles have become smaller, so each does "
                     "less.",
             "correct": False,
             "why": "Particles never change size, at any pressure. What "
                    "changes is how often and how hard they arrive."},
            {"text": "The particles have stopped, so almost none reach a "
                     "wall.",
             "correct": False,
             "why": "Gas particles never stop moving. Low pressure means "
                    "fewer or gentler arrivals, not none at all."},
            {"text": "The particles are spread out evenly instead of "
                     "packed at the walls.",
             "correct": False,
             "why": "Gas particles are spread through the container at "
                    "every pressure. They are never packed against the "
                    "walls."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e19",
        "band": "easier",
        "text": "The air inside a car tyre is at 220 kPa. The air around "
                "the tyre is at 100 kPa. Calculate the difference between "
                "the pressure inside the tyre and the pressure outside it.",
        "options": [
            {"text": "320 kPa",
             "correct": False,
             "why": "That adds the two pressures. A difference is found by "
                    "subtracting one from the other."},
            {"text": "220 kPa",
             "correct": False,
             "why": "That is the inside reading on its own. The question "
                    "asks by how much it beats the outside."},
            {"text": "2.2 kPa",
             "correct": False,
             "why": "That divides one pressure by the other. A difference "
                    "in kilopascals comes from a subtraction."},
            {"text": "120 kPa",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e20",
        "band": "easier",
        "text": "In this lesson, what is meant by a vacuum?",
        "options": [
            {"text": "A space that pulls particles into itself.",
             "correct": False,
             "why": "Nothing sucks. A vacuum has nothing inside it to do "
                    "any pulling."},
            {"text": "A space with no particles in it at all.",
             "correct": True},
            {"text": "A space filled with a very cold, still gas.",
             "correct": False,
             "why": "A vacuum has no gas in it at all, however cold that "
                    "gas might be."},
            {"text": "A space where the particles have stopped.",
             "correct": False,
             "why": "Gas particles never stop. A vacuum is a space with no "
                    "particles in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e21",
        "band": "easier",
        "text": "Can a vacuum suck air into itself?",
        "options": [
            {"text": "Yes, but only when the vacuum is a large one.",
             "correct": False,
             "why": "Size makes no difference. There is nothing inside a "
                    "vacuum to do any pulling, however big it is."},
            {"text": "Yes, because empty space always pulls matter in.",
             "correct": False,
             "why": "Empty space contains nothing, and nothing cannot "
                    "pull. Movement into a vacuum is a push from outside."},
            {"text": "No — air is pushed in from the side that has "
                     "particles.",
             "correct": True},
            {"text": "Yes, and that is how a vacuum cleaner lifts dust.",
             "correct": False,
             "why": "A cleaner lowers the pressure inside its pipe so that "
                    "the outside air is pushed in. Nothing is pulled."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e22",
        "band": "easier",
        "text": "A blown-up balloon is tied shut. What holds its rubber "
                "skin out?",
        "options": [
            {"text": "The stretched rubber holding itself out in the new "
                     "shape it was blown into.",
             "correct": False,
             "why": "Let the air out and the rubber goes limp at once, so "
                    "the rubber is not what holds the shape."},
            {"text": "The air particles inside pushing against one another "
                     "all through the middle of the balloon.",
             "correct": False,
             "why": "Those bumps happen in the middle of the balloon, away "
                    "from the rubber, so the rubber never feels them."},
            {"text": "The air outside gripping the balloon and holding it "
                     "up on every side at once.",
             "correct": False,
             "why": "The air outside pushes inwards, which is the "
                    "opposite. What holds the skin out is the air inside."},
            {"text": "Air particles inside colliding with the rubber, over "
                     "and over.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e23",
        "band": "easier",
        "text": "A sealed rigid can holds gas. Which of these changes "
                "would leave the pressure inside it exactly as it was?",
        "options": [
            {"text": "Warming the can in bright sunshine",
             "correct": False,
             "why": "Warming speeds the particles up, so they arrive more "
                    "often and hit harder. The pressure rises."},
            {"text": "Turning the can upside down on the bench",
             "correct": True},
            {"text": "Letting some of the gas out through a valve",
             "correct": False,
             "why": "Fewer particles means fewer arrivals at the walls "
                    "each second, so the pressure falls."},
            {"text": "Pumping more gas into the can",
             "correct": False,
             "why": "More particles means more arrivals at the walls each "
                    "second, so the pressure rises."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e24",
        "band": "easier",
        "text": "Press the button on a full aerosol can and the contents "
                "rush out. State why they come out rather than staying in.",
        "options": [
            {"text": "The air in the room pulls the contents out through "
                     "the open nozzle.",
             "correct": False,
             "why": "Nothing pulls. The contents are pushed out from the "
                    "side where the particles are arriving more often."},
            {"text": "Your finger squeezes the can, and that forces the "
                     "contents out of it.",
             "correct": False,
             "why": "A finger on a button opens a valve. It does not "
                    "squeeze a steel can in the slightest."},
            {"text": "The pressure inside the can is higher than the "
                     "pressure outside it.",
             "correct": True},
            {"text": "The gas inside the can is trying to escape into a "
                     "bigger space.",
             "correct": False,
             "why": "A gas has no aim and tries nothing. The contents "
                    "leave because the push from inside beats the push "
                    "from outside."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e25",
        "band": "easier",
        "text": "A rigid gas cylinder holds gas at 200 kPa. Half of the "
                "gas is let out, and the temperature does not change. "
                "State the new pressure.",
        "options": [
            {"text": "100 kPa",
             "correct": True},
            {"text": "200 kPa",
             "correct": False,
             "why": "Half the particles have gone, so only about half as "
                    "many arrive at the walls each second."},
            {"text": "400 kPa",
             "correct": False,
             "why": "That is a doubling, and letting gas out of a cylinder "
                    "lowers the pressure rather than raising it."},
            {"text": "0 kPa",
             "correct": False,
             "why": "Half the gas is still inside, still moving and still "
                    "hitting the walls. Half the gas gives about half the "
                    "pressure."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e26",
        "band": "easier",
        "text": "A fizzy drink bottle is made of thick plastic with a "
                "screw cap, while a milk bottle can be thin. State why the "
                "fizzy drink bottle has to be so much stronger.",
        "options": [
            {"text": "The liquid inside is much heavier than milk is.",
             "correct": False,
             "why": "The two liquids weigh about the same. What the bottle "
                    "has to hold in is the gas above the drink."},
            {"text": "The gas inside it is at a much higher pressure than "
                     "the air outside.",
             "correct": True},
            {"text": "The gas inside is trying to escape and pulls on the "
                     "plastic.",
             "correct": False,
             "why": "A gas never pulls on anything. It pushes, by "
                    "colliding with the walls, and here it collides very "
                    "often."},
            {"text": "The bubbles in the drink are sharp and would cut "
                     "thin plastic.",
             "correct": False,
             "why": "Bubbles cut nothing. The bottle is thick because the "
                    "gas inside pushes far harder than the air outside "
                    "pushes back."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e27",
        "band": "easier",
        "text": "A sealed rigid can of gas is heated strongly. State what "
                "happens to the number of particles inside it.",
        "options": [
            {"text": "It rises, because heating a gas makes more "
                     "particles.",
             "correct": False,
             "why": "Heating creates nothing. Exactly the same particles "
                    "are inside before and after."},
            {"text": "It falls, because some particles are burned up by "
                     "the heat.",
             "correct": False,
             "why": "Nothing is burned or destroyed inside a sealed can. "
                    "Every particle is still in there."},
            {"text": "It stays exactly the same, because heating adds no "
                     "particles.",
             "correct": True},
            {"text": "It rises, because each particle splits in two when "
                     "hot enough.",
             "correct": False,
             "why": "Particles do not split in this unit. Heating changes "
                    "only how fast they move."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e28",
        "band": "easier",
        "text": "You drink through a straw. What pushes the drink up the "
                "straw and into your mouth?",
        "options": [
            {"text": "The air pushing down on the surface of the drink in "
                     "the glass.",
             "correct": True},
            {"text": "Your mouth pulling the drink upwards through the "
                     "straw.",
             "correct": False,
             "why": "Your mouth lowers the pressure inside the straw. "
                    "Nothing is pulled — the air outside does the pushing."},
            {"text": "The empty space in the straw drawing the liquid up "
                     "into it.",
             "correct": False,
             "why": "An empty space contains nothing, and nothing cannot "
                    "draw anything anywhere."},
            {"text": "The drink flowing uphill because a straw holds no "
                     "air.",
             "correct": False,
             "why": "The straw is full of air before you start. What "
                    "matters is the air outside pushing down on the drink."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e29",
        "band": "easier",
        "text": "A gas is described as having been compressed. What has "
                "been done to it?",
        "options": [
            {"text": "It has been cooled until it turned into a liquid.",
             "correct": False,
             "why": "That is condensing. Compressing is about the space "
                    "the gas is given, not the state it is in."},
            {"text": "It has had extra particles pumped into it.",
             "correct": False,
             "why": "That raises the pressure too, but compressing means "
                    "squeezing the same gas into less room."},
            {"text": "It has been squashed until each one of its particles "
                     "is smaller.",
             "correct": False,
             "why": "Particles never change size. What gets smaller is the "
                    "space between them."},
            {"text": "It has been pushed into a smaller space.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e30",
        "band": "easier",
        "text": "In this lesson a container is often described as sealed. "
                "What does sealed mean?",
        "options": [
            {"text": "It cannot be squashed or changed in size.",
             "correct": False,
             "why": "That is what rigid means. A sealed container can "
                    "still be flexible, like a tied balloon."},
            {"text": "There is nothing at all inside it.",
             "correct": False,
             "why": "A sealed container is usually full of gas. Sealed "
                    "says only that nothing can get in or out."},
            {"text": "No particles can get in or out of it.",
             "correct": True},
            {"text": "It is airtight only while it stays cold.",
             "correct": False,
             "why": "Sealing has nothing to do with temperature. Nothing "
                    "gets in or out however hot or cold it is."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e31",
        "band": "easier",
        "text": "Put these three in order of gas pressure, starting with "
                "the lowest.",
        "options": [
            {"text": "Inside a vacuum, then the air in a room, then the "
                     "air in a pumped-up football.",
             "correct": True},
            {"text": "The air in a pumped-up football, then the air in a "
                     "room, then inside a vacuum.",
             "correct": False,
             "why": "That is exactly the wrong way round. A vacuum has no "
                    "particles at all, so nothing hits any surface."},
            {"text": "The air in a room, then inside a vacuum, then the "
                     "air in a pumped-up football.",
             "correct": False,
             "why": "A vacuum has nothing inside it to hit a surface, so "
                    "it cannot come above ordinary room air."},
            {"text": "Inside a vacuum, then the air in a pumped-up "
                     "football, then the air in a room.",
             "correct": False,
             "why": "Pumping a football raises its pressure well above the "
                    "room's, so it belongs last rather than in the middle."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-e32",
        "band": "easier",
        "text": "A syringe holds 60 cm³ of air and its nozzle is blocked. "
                "The plunger is pushed in until the air occupies 30 cm³, "
                "at the same temperature. State what has happened to the "
                "pressure of the trapped air.",
        "options": [
            {"text": "It has roughly halved, because the air has half the "
                     "room.",
             "correct": False,
             "why": "Less room means each particle reaches a wall sooner, "
                    "so the pressure goes up rather than down."},
            {"text": "It has stayed the same, since no air was added or "
                     "let out.",
             "correct": False,
             "why": "The number of particles is only one of the things "
                    "pressure depends on, and the space has been halved."},
            {"text": "It has risen four times over, because both halves "
                     "now push.",
             "correct": False,
             "why": "Halving the space roughly doubles the arrivals at the "
                    "walls. Doubling once gives twice, not four times."},
            {"text": "It has roughly doubled, because each particle "
                     "arrives twice as often.",
             "correct": True},
        ],
        "figure": None,
    },
    # ── standard · MRB-338 expansion ──────────────────────────────────
    {
        "id": "c1-04-s10",
        "band": "standard",
        "text": "A sealed rigid tin of air is taken from a warm kitchen "
                "and left in a freezer. After an hour its sides have bowed "
                "inwards. Explain why.",
        "options": [
            {"text": "The cold air inside has shrunk away from the sides "
                     "of the tin, leaving an empty gap behind it that the "
                     "thin metal has then folded into.",
             "correct": False,
             "why": "A gas always fills its container. It never shrinks "
                    "away from the walls and leaves a gap behind."},
            {"text": "The air inside has cooled, so its particles hit the "
                     "tin less often and less hard, while the room air "
                     "outside has not changed.",
             "correct": True},
            {"text": "The cold has made a vacuum inside the tin, and that "
                     "vacuum has pulled the sides in.",
             "correct": False,
             "why": "The particles are all still in there, so there is no "
                    "vacuum — and a vacuum could not pull on anything even "
                    "if there were."},
            {"text": "A coat of frost has formed on the outside of the tin "
                     "and squeezed its sides in.",
             "correct": False,
             "why": "A thin coat of frost pushes on nothing. What pushes "
                    "the sides in is the room air, now winning against the "
                    "cooled air within."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s11",
        "band": "standard",
        "text": "A marshmallow is put under a glass jar and the air is "
                "pumped out of the jar. The marshmallow swells up. Explain "
                "why.",
        "options": [
            {"text": "The gas in the marshmallow's bubbles still hits "
                     "their walls, and almost nothing is left outside to "
                     "push back.",
             "correct": True},
            {"text": "The pump has taken hold of the marshmallow and "
                     "pulled it outwards from every side at once until it "
                     "had swelled right up.",
             "correct": False,
             "why": "A pump takes particles away; it does not pull on "
                    "anything. Nothing sucks."},
            {"text": "The marshmallow's own gas has been heated by the "
                     "working of the pump, and a hot gas always takes up "
                     "more room than a cold one.",
             "correct": False,
             "why": "Nothing has heated the marshmallow. What has changed "
                    "is the pushing from outside, which has almost gone."},
            {"text": "The bubbles inside the marshmallow have made new gas "
                     "to fill the emptied jar.",
             "correct": False,
             "why": "No gas is made. The gas already in the bubbles is "
                    "simply no longer being pushed back by anything."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s12",
        "band": "standard",
        "text": "A glass is filled to the brim with water, a stiff card is "
                "held over the top, and the glass is turned upside down. "
                "The card stays put and the water stays in. Explain what "
                "holds the card up.",
        "options": [
            {"text": "The weight of the water presses the card against the "
                     "rim and seals it there.",
             "correct": False,
             "why": "The water's weight pushes the card downwards, away "
                    "from the glass. That would drop it, not hold it."},
            {"text": "A vacuum inside the glass holds the card up by "
                     "pulling on it.",
             "correct": False,
             "why": "The glass is full of water, so there is no vacuum — "
                    "and a vacuum has nothing in it to pull with anyway."},
            {"text": "Air trapped at the top of the glass presses down and "
                     "stops the water falling.",
             "correct": False,
             "why": "Pressing down would push the water and the card "
                    "straight out. The card is held by a push from below."},
            {"text": "The air below pushes up on the card harder than the "
                     "water above pushes down.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s13",
        "band": "standard",
        "text": "Your ears pop as an aircraft climbs. Explain what is "
                "happening, in terms of pressure.",
        "options": [
            {"text": "The air pressure outside your eardrum rises steadily "
                     "as the plane climbs, and it presses the eardrum "
                     "inwards until it finally clicks.",
             "correct": False,
             "why": "Atmospheric pressure falls as you go up, not rises, "
                    "so the push from outside gets weaker rather than "
                    "stronger."},
            {"text": "The air pressure outside your eardrum falls, so the "
                     "air trapped behind it pushes the eardrum outwards "
                     "until some escapes.",
             "correct": True},
            {"text": "The air trapped behind your eardrum is heated by the "
                     "engines and takes up more room.",
             "correct": False,
             "why": "The engines do not heat your head, and ears pop on "
                    "the way down too, when the pressure outside is "
                    "rising."},
            {"text": "The speed of the aircraft pulls the air out of your "
                     "ears as it flies.",
             "correct": False,
             "why": "Nothing pulls air anywhere. It is the difference "
                    "between the two pressures that moves the eardrum."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s14",
        "band": "standard",
        "text": "A jar of jam is filled hot and sealed at once. When it is "
                "cold the lid is very hard to lift, and it pops loudly "
                "when it finally gives. Explain what is holding the lid "
                "down.",
        "options": [
            {"text": "The hot jam swelled up as it was poured in, and it "
                     "pressed the lid tightly against the rim from the "
                     "inside, where it has held it ever since.",
             "correct": False,
             "why": "A push from inside would lift the lid off, not hold "
                    "it down. The lid is being pushed the other way."},
            {"text": "The metal lid shrank onto the glass rim as it cooled "
                     "and has been wedged tightly in place ever since, "
                     "which is why it takes such a twist.",
             "correct": False,
             "why": "The pop as it opens is air rushing in, which tells "
                    "you the two pressures were different — not that the "
                    "lid was stuck fast."},
            {"text": "The gas left in the jar cooled and hits the lid less "
                     "often, so the room air outside now pushes it down "
                     "harder than the gas pushes it up.",
             "correct": True},
            {"text": "The jam has set into a glue between the rim and the "
                     "lid, and it holds the two of them together until the "
                     "seal finally breaks with a pop.",
             "correct": False,
             "why": "The lid is just as hard to lift on a jar whose jam "
                    "never reached it. What holds it is the air outside."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s15",
        "band": "standard",
        "text": "Two identical rigid cylinders hold the same gas at the "
                "same temperature. Cylinder A is at 100 kPa and cylinder B "
                "is at 400 kPa. Compare the number of particles in the two "
                "cylinders.",
        "options": [
            {"text": "B holds about twice as many particles as A does.",
             "correct": False,
             "why": "400 kPa is four times 100 kPa, not twice, and the "
                    "pressure rises in step with the number of particles "
                    "here."},
            {"text": "Both hold the same number, and B's particles simply "
                     "move faster.",
             "correct": False,
             "why": "The two are at the same temperature, so their "
                    "particles move at the same average speed. Only the "
                    "number can differ."},
            {"text": "A holds four times as many, because low pressure "
                     "leaves more room.",
             "correct": False,
             "why": "More particles in the same space means more arrivals "
                    "at the walls and a higher pressure, not a lower one."},
            {"text": "B holds about four times as many particles as A "
                     "does.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s16",
        "band": "standard",
        "text": "A fixed amount of gas is squeezed into a quarter of the "
                "space it started in, at the same temperature. Explain, in "
                "terms of collisions, why its pressure rises.",
        "options": [
            {"text": "The particles are squashed smaller, so more of them "
                     "fit against the wall.",
             "correct": False,
             "why": "Particles never change size. What has shrunk is the "
                    "space between them, not the particles themselves."},
            {"text": "Each particle has a shorter journey between the "
                     "walls, so it arrives about four times as often.",
             "correct": True},
            {"text": "The particles are forced to move faster because they "
                     "have less room to travel in.",
             "correct": False,
             "why": "Only temperature changes a particle's speed, and the "
                    "temperature has been kept the same throughout."},
            {"text": "The particles bump into each other far more, and "
                     "those bumps press on the walls.",
             "correct": False,
             "why": "Particle-to-particle bumps happen away from the wall, "
                    "so the wall never feels a single one of them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s17",
        "band": "standard",
        "text": "A diver releases a bubble of air at the bottom of a deep "
                "lake, and the bubble grows steadily larger as it rises. "
                "Explain why.",
        "options": [
            {"text": "The bubble collects more and more air out of the "
                     "water around it as it travels upwards, which is what "
                     "makes it grow on the way up.",
             "correct": False,
             "why": "No air joins it. The same particles simply spread "
                    "into more room as the push from outside weakens."},
            {"text": "The air particles inside the bubble swell as the "
                     "water gets shallower.",
             "correct": False,
             "why": "Particles never change size, at any depth. The bubble "
                    "grows because the push from outside falls."},
            {"text": "The water pressing on the bubble weakens as it "
                     "rises, so the air inside pushes the bubble out "
                     "further before the two balance.",
             "correct": True},
            {"text": "The bubble is pulled outwards by the open air "
                     "waiting above the surface.",
             "correct": False,
             "why": "Nothing pulls a bubble. It is pushed outwards from "
                    "within by its own particles hitting its walls."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s18",
        "band": "standard",
        "text": "A plastic bottle is emptied and screwed shut at the top "
                "of a mountain, then carried down to sea level. By the "
                "time it arrives it has crumpled. Explain why.",
        "options": [
            {"text": "Atmospheric pressure is greater at sea level, so the "
                     "air outside now hits the bottle more often than the "
                     "mountain air sealed inside it.",
             "correct": True},
            {"text": "The air sealed inside the bottle cooled on the long "
                     "drive down the mountain, and as it cooled it took up "
                     "far less room than it had done at the top.",
             "correct": False,
             "why": "The air is warmer at sea level, not colder. What has "
                    "changed is the pressure of the air outside the "
                    "bottle."},
            {"text": "The thicker air at sea level has been forced in "
                     "through the walls of the bottle and has crushed it "
                     "from the inside outwards as it collected.",
             "correct": False,
             "why": "The bottle is sealed, so no air got in. The crushing "
                    "is done entirely from the outside."},
            {"text": "The empty bottle holds a vacuum, and a vacuum pulls "
                     "harder the lower it goes.",
             "correct": False,
             "why": "The bottle is full of mountain air, and a vacuum "
                    "could not pull on anything in any case."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s19",
        "band": "standard",
        "text": "A class investigates how the pressure of a fixed amount "
                "of gas depends on the volume it is given. Which variable "
                "must they keep the same for the investigation to be fair?",
        "options": [
            {"text": "The pressure of the gas, because it must be the same "
                     "in every reading.",
             "correct": False,
             "why": "Pressure is what they are measuring. Holding it fixed "
                    "would leave nothing at all to find out."},
            {"text": "The temperature of the gas, because heating would "
                     "raise the pressure on its own.",
             "correct": True},
            {"text": "The volume of the gas, because a fair test must "
                     "change nothing at all.",
             "correct": False,
             "why": "Volume is the variable they are deliberately "
                    "changing. A fair test changes one thing and holds the "
                    "rest."},
            {"text": "The shape of the container, because pressure depends "
                     "on which face is largest.",
             "correct": False,
             "why": "Pressure does not depend on the shape of a container. "
                    "It acts on every face of it alike."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s20",
        "band": "standard",
        "text": "A student says the air in an open classroom has no "
                "pressure, because nothing is squeezing it. Explain why "
                "the student is wrong.",
        "options": [
            {"text": "The air is squeezed by the walls of the room, and "
                     "that gives it its pressure.",
             "correct": False,
             "why": "Pressure needs nothing to do the squeezing. It is "
                    "there in open air just as much as in a sealed can."},
            {"text": "The air does have a pressure, but only down near the "
                     "floor, where the weight of all the air above it "
                     "collects.",
             "correct": False,
             "why": "Air pushes on a ceiling as hard as on a floor, "
                    "because its particles arrive from every direction."},
            {"text": "Air particles are colliding with every surface in "
                     "the room all the time, and that is what pressure is.",
             "correct": True},
            {"text": "The student is right about the room, and wrong only "
                     "about sealed containers.",
             "correct": False,
             "why": "The air in a room is at about 100 kPa — the very "
                    "pressure the sealed containers in this lesson start "
                    "at."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s21",
        "band": "standard",
        "text": "A class squeezes a sealed syringe of air and reads its "
                "pressure at each volume. Every reading comes out lower "
                "than expected. Suggest the most likely reason.",
        "options": [
            {"text": "Air has been leaking slowly past the plunger, so "
                     "fewer particles are trapped than they think.",
             "correct": True},
            {"text": "They pushed the plunger in far too quickly for the "
                     "pressure inside the syringe to have had time to "
                     "build up to its full value.",
             "correct": False,
             "why": "Pressure does not need time to build. It is there as "
                    "soon as the particles are in the smaller space."},
            {"text": "The syringe was held upright rather than lying flat, "
                     "so the particles all fell towards the nozzle end of "
                     "it.",
             "correct": False,
             "why": "The way a syringe is held makes no difference. The "
                    "particles arrive on every face of it alike."},
            {"text": "They recorded each volume in cm³ rather than in "
                     "litres, which makes every pressure they worked out "
                     "come out too small.",
             "correct": False,
             "why": "Writing a volume in different units does not change "
                    "the pressure the gauge is showing."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s22",
        "band": "standard",
        "text": "A sealed gas can be changed in two ways: the number of "
                "particles can be doubled, or the container can be made "
                "half its size. Compare the effect of each on the "
                "pressure, at the same temperature.",
        "options": [
            {"text": "Both roughly double the pressure, because both "
                     "roughly double the arrivals at the walls.",
             "correct": True},
            {"text": "Doubling the particles doubles it, but halving the "
                     "container changes nothing.",
             "correct": False,
             "why": "Halving the space halves each particle's journey to a "
                    "wall, so it arrives about twice as often."},
            {"text": "Halving the container doubles it, but doubling the "
                     "particles changes nothing.",
             "correct": False,
             "why": "Twice as many particles means twice as many arrivals "
                    "each second, so that route doubles the pressure too."},
            {"text": "Doubling the particles doubles it, and halving the "
                     "container quadruples it.",
             "correct": False,
             "why": "Halving the volume roughly doubles the arrival rate "
                    "at the walls. It does not quadruple it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s23",
        "band": "standard",
        "text": "A rigid container of gas is at 100 kPa. Enough gas is "
                "pumped in to make three times as many particles as "
                "before, at the same temperature. Calculate the new "
                "pressure.",
        "options": [
            {"text": "103 kPa",
             "correct": False,
             "why": "That adds three to the pressure. The particles have "
                    "been multiplied by three, so the pressure is too."},
            {"text": "33 kPa",
             "correct": False,
             "why": "That divides by three. More particles in the same "
                    "container means a higher pressure, not a lower one."},
            {"text": "300 kPa",
             "correct": True},
            {"text": "200 kPa",
             "correct": False,
             "why": "That is a doubling. The number of particles has been "
                    "tripled, so the arrivals at the walls treble as well."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s24",
        "band": "standard",
        "text": "A blown-up balloon is put in a fridge and is noticeably "
                "smaller an hour later, with nothing let out of it. "
                "Explain why.",
        "options": [
            {"text": "Its particles have slowed, so they hit the rubber "
                     "less often and less hard, and the air outside pushes "
                     "the balloon in until the two balance.",
             "correct": True},
            {"text": "The cold has made the balloon's rubber shrink, and "
                     "the shrinking rubber has squeezed the air inside "
                     "into a much smaller space than it filled before.",
             "correct": False,
             "why": "The rubber follows the air, not the other way round. "
                    "It is the slower particles inside that stop holding "
                    "the skin out."},
            {"text": "The particles inside have shrunk in the cold, so "
                     "they take up less room.",
             "correct": False,
             "why": "Particles never change size, when they are heated or "
                    "when they are cooled."},
            {"text": "The cold has pulled the balloon inwards from every "
                     "side at once.",
             "correct": False,
             "why": "Cold cannot pull on anything. The balloon is pushed "
                    "in by the air outside, once the inside stops pushing "
                    "back so hard."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s25",
        "band": "standard",
        "text": "A football left overnight in a cold shed is soft in the "
                "morning. A student says air must have leaked out of it. "
                "Suggest one observation that would test whether that is "
                "what happened.",
        "options": [
            {"text": "Press it hard and listen for air hissing out of it "
                     "somewhere.",
             "correct": False,
             "why": "A ball with no leak makes no sound either, so hearing "
                    "nothing would tell you nothing at all."},
            {"text": "Pump the ball up again and see whether it holds its "
                     "pressure right the way through the day.",
             "correct": False,
             "why": "Pumping changes the ball, so whatever happens "
                    "afterwards cannot tell you what happened overnight."},
            {"text": "Measure how cold the shed became during the night.",
             "correct": False,
             "why": "The temperature does not separate the two "
                    "explanations. The ball would be soft either way."},
            {"text": "Bring it into a warm room and see whether it firms "
                     "up again without being pumped.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s26",
        "band": "standard",
        "text": "A sealed syringe holds 30 cm³ of air at 100 kPa. The "
                "plunger is pulled out until the air occupies 60 cm³, at "
                "the same temperature. Calculate the new pressure of the "
                "trapped air.",
        "options": [
            {"text": "200 kPa",
             "correct": False,
             "why": "That is what happens when air is squeezed into half "
                    "the space. Here it has been given twice the room."},
            {"text": "50 kPa",
             "correct": True},
            {"text": "100 kPa",
             "correct": False,
             "why": "The same particles now have twice the room, so each "
                    "one reaches a wall about half as often as before."},
            {"text": "130 kPa",
             "correct": False,
             "why": "That adds the two numbers together. The volume has "
                    "doubled, so the pressure falls to about half."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s27",
        "band": "standard",
        "text": "A vacuum cleaner picks dust up off the floor. Describe "
                "what actually moves the dust into the machine.",
        "options": [
            {"text": "The cleaner makes a vacuum inside its pipe, and a "
                     "vacuum pulls in anything that comes near enough to "
                     "the open end of it.",
             "correct": False,
             "why": "A vacuum contains nothing, and nothing can pull. The "
                    "movement is always a push from the side with the "
                    "particles."},
            {"text": "The cleaner's brushes throw the dust upwards and the "
                     "bag catches it.",
             "correct": False,
             "why": "A cleaner still picks dust up with the brushes off, "
                    "and off a smooth floor that the brushes cannot even "
                    "touch."},
            {"text": "The cleaner lowers the pressure inside its pipe, so "
                     "the air outside is pushed in and carries the dust "
                     "with it.",
             "correct": True},
            {"text": "The dust is drawn towards the empty space inside the "
                     "pipe, because matter will always move to fill an "
                     "empty gap wherever it finds one.",
             "correct": False,
             "why": "Matter does not seek out gaps. It is pushed into them "
                    "by the particles behind it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s28",
        "band": "standard",
        "text": "Explain, in terms of particles, why atmospheric pressure "
                "is lower at the top of a mountain than at sea level.",
        "options": [
            {"text": "There is less air above, so each cubic metre up "
                     "there holds fewer particles and fewer of them reach "
                     "any surface each second.",
             "correct": True},
            {"text": "The air at the top of a mountain is far colder than "
                     "the air at sea level, and a cold gas has no pressure "
                     "of its own to speak of.",
             "correct": False,
             "why": "Cold air still has plenty of pressure. The reason the "
                    "summit reading is low is that less air lies above it."},
            {"text": "The air at the summit is much further from the "
                     "ground, so gravity is far too weak up there to press "
                     "it down onto the rocks below.",
             "correct": False,
             "why": "Gravity still acts at the summit. What has changed is "
                    "how much air is stacked above you."},
            {"text": "The wind is always stronger on a summit than it is "
                     "down in a valley, and fast-moving air presses far "
                     "less hard on the rocks it passes.",
             "correct": False,
             "why": "Pressure does not depend on the wind. It falls with "
                    "height because there is less air above."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s29",
        "band": "standard",
        "text": "A student says that a gas at high pressure must be hot. "
                "Evaluate that claim.",
        "options": [
            {"text": "It is right, because only heating a gas can make its "
                     "particles hit the walls hard enough to give a high "
                     "pressure.",
             "correct": False,
             "why": "Hitting harder is one route to a high pressure. "
                    "Arriving more often is another, and squeezing or "
                    "adding gas does that."},
            {"text": "It is right, because pressure and temperature are "
                     "really two different names for one and the same "
                     "quantity.",
             "correct": False,
             "why": "They are different quantities. A gas can be cold at a "
                    "high pressure, or warm at a low one."},
            {"text": "It is wrong, because the pressure of a gas does not "
                     "depend on its temperature in any way at all.",
             "correct": False,
             "why": "Temperature is genuinely one of the three things that "
                    "set a pressure. It is simply not the only one."},
            {"text": "It is wrong: a cold gas squeezed small, or holding "
                     "many particles, is also at high pressure.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s30",
        "band": "standard",
        "text": "A single gas particle hits a wall and bounces away, "
                "giving it the tiniest of taps. Explain why the wall feels "
                "a steady push rather than a string of separate taps.",
        "options": [
            {"text": "The particles line up and hit the wall together, so "
                     "their taps arrive as one.",
             "correct": False,
             "why": "Particles move at random and arrive independently of "
                    "each other. Nothing lines them up."},
            {"text": "So many particles arrive every second that the taps "
                     "blur into one constant push.",
             "correct": True},
            {"text": "Each particle stays pressed against the wall after "
                     "arriving, holding it steady.",
             "correct": False,
             "why": "A particle bounces straight off again. The push is "
                    "steady because the arrivals never stop coming."},
            {"text": "The wall stores each tap and releases it slowly, "
                     "which smooths them out.",
             "correct": False,
             "why": "A wall stores nothing at all. The steadiness comes "
                    "from the sheer number of arrivals each second."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s31",
        "band": "standard",
        "text": "A sealed tin of gas at 100 kPa is sitting in a room where "
                "the air is also at 100 kPa. Explain why the tin neither "
                "bulges nor caves in.",
        "options": [
            {"text": "The tin is made of thick metal, and it is far too "
                     "strong for the gas inside it to move its walls in "
                     "either direction.",
             "correct": False,
             "why": "A tin no stronger than this one bulges the moment it "
                    "is heated, so its strength is not what is keeping it "
                    "flat."},
            {"text": "The gas inside has settled down and stopped pushing "
                     "on the walls, now that it has been sitting still on "
                     "the shelf for a while.",
             "correct": False,
             "why": "Gas particles never settle or stop. They are still "
                    "arriving at the tin, and so are the ones outside."},
            {"text": "Particles hit the tin about as often from the inside "
                     "as from the outside, so there is no net push either "
                     "way.",
             "correct": True},
            {"text": "There is no gas pressing on the outside of the tin, "
                     "so the only pressure acting anywhere on it is the "
                     "one inside it.",
             "correct": False,
             "why": "The room is full of air, and that air pushes on the "
                    "outside of the tin just as hard as the gas pushes "
                    "out."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-s32",
        "band": "standard",
        "text": "A 1-litre rigid flask holds gas at 300 kPa. All of that "
                "gas is moved into an empty 3-litre rigid flask at the "
                "same temperature. Calculate the pressure in the larger "
                "flask.",
        "options": [
            {"text": "900 kPa",
             "correct": False,
             "why": "That multiplies where you should divide. Three times "
                    "the room means each particle reaches a wall a third "
                    "as often."},
            {"text": "100 kPa",
             "correct": True},
            {"text": "300 kPa",
             "correct": False,
             "why": "The number of particles is unchanged, but the space "
                    "they are in is not. Three times the room lowers the "
                    "pressure."},
            {"text": "150 kPa",
             "correct": False,
             "why": "That halves the pressure. The gas has been given "
                    "three times the room, not twice."},
        ],
        "figure": None,
    },
    # ── harder · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c1-04-h10",
        "band": "harder",
        "text": "A 4-litre cylinder holds gas at 100 kPa. The gas is "
                "compressed into 1 litre at the same temperature, and then "
                "half of it is let out. Calculate the final pressure.",
        "options": [
            {"text": "400 kPa",
             "correct": False,
             "why": "That is the pressure after the squeeze alone. Half "
                    "the gas was then released, which halves it again."},
            {"text": "50 kPa",
             "correct": False,
             "why": "That treats both steps as reductions. Squeezing gas "
                    "into a quarter of the space raises its pressure four "
                    "times over."},
            {"text": "200 kPa",
             "correct": True},
            {"text": "800 kPa",
             "correct": False,
             "why": "That doubles the pressure at the second step. Letting "
                    "half the gas out halves it instead."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h11",
        "band": "harder",
        "text": "A class measures the pressure of a fixed amount of gas at "
                "five different volumes, all at the same temperature, and "
                "plots pressure against volume. Describe the graph they "
                "should get.",
        "options": [
            {"text": "A curve falling from left to right, with pressure "
                     "times volume coming to about the same number at "
                     "every point.",
             "correct": True},
            {"text": "A straight line sloping down, because equal steps in "
                     "volume give equal falls in pressure.",
             "correct": False,
             "why": "Halving the volume doubles the pressure, and halving "
                    "it again doubles it once more, so the fall is not in "
                    "equal steps."},
            {"text": "A straight line sloping up, because a larger "
                     "container holds a larger pressure.",
             "correct": False,
             "why": "A larger container gives each particle a longer "
                    "journey to a wall, so the pressure falls as the "
                    "volume rises."},
            {"text": "A flat line, because the number of particles has not "
                     "been changed at all.",
             "correct": False,
             "why": "The number of particles is only one of the things a "
                    "pressure depends on, and the volume is being changed "
                    "deliberately."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h12",
        "band": "harder",
        "text": "A sealed syringe holds 40 cm³ of air at the surface of a "
                "lake, where the pressure is 100 kPa. It is taken down to "
                "10 m, where the total pressure is about 200 kPa. Predict "
                "the volume of the trapped air at that depth.",
        "options": [
            {"text": "80 cm³",
             "correct": False,
             "why": "That doubles the volume when the pressure has "
                    "doubled. A greater pressure squeezes the gas into "
                    "less room, not more."},
            {"text": "20 cm³",
             "correct": True},
            {"text": "40 cm³",
             "correct": False,
             "why": "The pressure outside has doubled, and the plunger "
                    "moves in until the pressure inside matches it."},
            {"text": "10 cm³",
             "correct": False,
             "why": "That divides the volume by four. The pressure has "
                    "doubled once, so the volume halves once."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h13",
        "band": "harder",
        "text": "Design an investigation to show that heating a gas raises "
                "its pressure. Which plan does the job?",
        "options": [
            {"text": "Warm an open flask of air on a tripod and record the "
                     "pressure of the room at several temperatures.",
             "correct": False,
             "why": "An open flask lets particles leave, and the room's "
                    "pressure is not the flask's pressure in any case."},
            {"text": "Seal a fixed amount of gas in a rigid flask fitted "
                     "with a pressure gauge, warm it in a water bath, and "
                     "record the pressure at several temperatures.",
             "correct": True},
            {"text": "Seal a fixed amount of gas in a balloon, warm it in "
                     "a water bath, and record how much larger the balloon "
                     "grows at each temperature it reaches.",
             "correct": False,
             "why": "A balloon can change size, so the volume changes too "
                    "and you cannot tell which change moved the reading."},
            {"text": "Heat sealed flasks of four different gases to one "
                     "temperature and compare their pressure readings.",
             "correct": False,
             "why": "That compares one gas with another rather than one "
                    "temperature with another, so it shows nothing about "
                    "heating."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h14",
        "band": "harder",
        "text": "A sealed rigid flask of gas is placed on a balance and "
                "its mass recorded. It is then heated until its pressure "
                "has doubled, and weighed again on the same balance. "
                "Predict the two readings.",
        "options": [
            {"text": "The two readings are the same, because heating adds "
                     "no particles and none can leave.",
             "correct": True},
            {"text": "The second reading is higher, because the gas now "
                     "pushes down harder on the balance.",
             "correct": False,
             "why": "The gas pushes on every face of the flask, not only "
                    "on its base, and a pressure is not a weight."},
            {"text": "The second reading is higher, because heat has been "
                     "added and heat has a mass of its own.",
             "correct": False,
             "why": "Energy is not a substance that can be weighed. "
                    "Nothing has been put into the sealed flask."},
            {"text": "The second reading is lower, because faster "
                     "particles spend less time touching the walls.",
             "correct": False,
             "why": "The balance reads the mass of the flask and "
                    "everything inside it, and every particle is still in "
                    "there."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h15",
        "band": "harder",
        "text": "A gas is sealed at 100 kPa. Its container is then made "
                "half its size, and the gas is heated as well. A student "
                "says the pressure must now be exactly 200 kPa. Evaluate "
                "that.",
        "options": [
            {"text": "It is right, because halving the space doubles the "
                     "pressure and heating does not change it.",
             "correct": False,
             "why": "Heating a gas held at a fixed size raises its "
                    "pressure on its own, so here the two effects add "
                    "together."},
            {"text": "It is too high: the heating spreads the particles "
                     "out again and cancels part of the squeeze.",
             "correct": False,
             "why": "The container fixes the space, so the particles "
                    "cannot spread out and nothing is cancelled."},
            {"text": "It cannot be worked out at all, because heating a "
                     "gas lowers its pressure.",
             "correct": False,
             "why": "Heating raises the pressure of a gas held at a fixed "
                    "size. Both changes here push the pressure the same "
                    "way."},
            {"text": "It is too low: halving the space alone gives about "
                     "200 kPa, and the heating pushes it higher still.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h16",
        "band": "harder",
        "text": "A weather station at one place reads 98 kPa one day and "
                "103 kPa the next. Suggest what is different about the air "
                "above the station on the second day.",
        "options": [
            {"text": "The air above the station is moving far faster, and "
                     "fast-moving air presses harder.",
             "correct": False,
             "why": "Pressure comes from the particles' own constant "
                    "motion in all directions, not from the wind."},
            {"text": "The station has been moved lower down, where more "
                     "air lies above it.",
             "correct": False,
             "why": "Both readings are taken at the same place. What "
                    "differs from day to day is the air above it."},
            {"text": "There is more air above the station, so more "
                     "particles reach each surface every second.",
             "correct": True},
            {"text": "The particles in the air have grown larger, so each "
                     "one of them hits harder.",
             "correct": False,
             "why": "Particles never change size, in any weather. Only "
                    "their number and their speed can change."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h17",
        "band": "harder",
        "text": "Two identical metal cans of air are heated to the same "
                "temperature. One is sealed; the other has a small hole in "
                "its lid. Compare the pressure inside the two cans.",
        "options": [
            {"text": "The sealed can's pressure rises, while the holed can "
                     "stays near the room's pressure because particles can "
                     "leave.",
             "correct": True},
            {"text": "Both rise by exactly the same amount, because the "
                     "two cans hold the same air and are given the same "
                     "heat for the same time.",
             "correct": False,
             "why": "The holed can cannot keep its particles in. They "
                    "leave through the hole instead of crowding the walls."},
            {"text": "The holed can rises further, because the hole lets "
                     "extra air in as it heats.",
             "correct": False,
             "why": "Particles leave through the hole while the can is "
                    "hot, so the inside stays level with the room."},
            {"text": "Neither changes, because heating alters only how "
                     "fast the particles are moving.",
             "correct": False,
             "why": "Faster particles reach the walls more often and hit "
                    "harder, and that is exactly what lifts the sealed "
                    "can's pressure."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h18",
        "band": "harder",
        "text": "Half the particles are taken out of a sealed container "
                "and its pressure halves. A student says this proves "
                "pressure depends on how crowded the particles are rather "
                "than on how often they hit the walls. Explain why this "
                "result cannot decide between the two ideas, and say what "
                "would.",
        "options": [
            {"text": "The result does decide it, because taking half the "
                     "particles out changes how crowded they are and "
                     "changes nothing else.",
             "correct": False,
             "why": "Taking particles out changes the arrivals at the wall "
                    "as well, so the two ideas cannot be told apart by it."},
            {"text": "Neither idea can ever be tested, because nobody can "
                     "watch a single particle arrive at a wall and count "
                     "it as it lands.",
             "correct": False,
             "why": "You do not need to see one. Any test the two ideas "
                    "answer differently will settle it."},
            {"text": "Make the container smaller instead, because that "
                     "changes how crowded the particles are without "
                     "changing the hits at the wall at all.",
             "correct": False,
             "why": "Making it smaller raises the arrivals at the wall as "
                    "well as the crowding, so it separates nothing either."},
            {"text": "Both ideas predict a halving here, so heat the gas "
                     "instead: the crowding is unchanged and the pressure "
                     "still rises.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h19",
        "band": "harder",
        "text": "The collision counter turns wall hits into a pressure at "
                "7 kPa for every hit per second. A setting is found where "
                "it reads 30 hits per second. Calculate the pressure, and "
                "compare it with the 100 kPa of ordinary room air.",
        "options": [
            {"text": "210 kPa, which is about twenty times the pressure of "
                     "room air.",
             "correct": False,
             "why": "The arithmetic is right, but 210 kPa is a little over "
                    "twice 100 kPa, nowhere near twenty times it."},
            {"text": "210 kPa, which is about twice the pressure of room "
                     "air.",
             "correct": True},
            {"text": "37 kPa, which is well below the pressure of ordinary "
                     "room air.",
             "correct": False,
             "why": "That adds the 7 to the count. Each hit per second is "
                    "worth 7 kPa, so the count is multiplied by 7."},
            {"text": "4.3 kPa, which is a tiny fraction of the pressure of "
                     "room air.",
             "correct": False,
             "why": "That divides 30 by 7. Every hit per second is worth "
                    "another 7 kPa, so the two are multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h20",
        "band": "harder",
        "text": "Two identical sealed rigid flasks hold the same gas at "
                "the same temperature. Flask A contains 1 g of the gas and "
                "reads 50 kPa. Flask B contains 3 g of it. Calculate the "
                "pressure in flask B.",
        "options": [
            {"text": "50 kPa",
             "correct": False,
             "why": "The flasks are the same size and the same "
                    "temperature, so three times the gas gives three times "
                    "the arrivals at the walls."},
            {"text": "53 kPa",
             "correct": False,
             "why": "That adds the 3 g to the pressure. A mass in grams "
                    "and a pressure in kilopascals cannot be added "
                    "together."},
            {"text": "150 kPa",
             "correct": True},
            {"text": "16.7 kPa",
             "correct": False,
             "why": "That divides by three. More gas in a flask of the "
                    "same size means a higher pressure, not a lower one."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h21",
        "band": "harder",
        "text": "A student argues: air has no weight, so atmospheric "
                "pressure must be caused by the wind. Evaluate the "
                "argument.",
        "options": [
            {"text": "The first half is right and the second wrong: air "
                     "has no weight, but the pressure comes from "
                     "collisions.",
             "correct": False,
             "why": "Air does have mass and weight, which is why the whole "
                    "depth of it above you presses so hard on you."},
            {"text": "The argument is sound, because a barometer reading "
                     "changes when the wind gets up.",
             "correct": False,
             "why": "Readings do change with the weather, but the pressure "
                    "is still about 100 kPa on a completely still day."},
            {"text": "The first half is wrong and the second right: air "
                     "has weight, and the wind is what presses on us.",
             "correct": False,
             "why": "The 100 kPa is there in still air, produced by the "
                    "particles' own motion, with no wind involved at all."},
            {"text": "Both halves fail: air does have weight, and the "
                     "pressure is there on a completely still day.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h22",
        "band": "harder",
        "text": "A sealed bag of nuts bought at an airport is noticeably "
                "puffed up when the aircraft reaches cruising height, even "
                "though the cabin is pressurised and nobody has opened the "
                "bag. Suggest why.",
        "options": [
            {"text": "The bag has been warmed by the cabin's heating all "
                     "through the climb, and a warm gas takes up more room "
                     "than a cold one does.",
             "correct": False,
             "why": "The cabin is no warmer than the terminal was, and the "
                    "bag puffs up on a cold flight just the same."},
            {"text": "The cabin is held at a lower pressure than the "
                     "ground, so the outside now pushes on the bag less "
                     "than the sealed air pushes out.",
             "correct": True},
            {"text": "The speed of the aircraft pulls the sides of the bag "
                     "outwards as it flies.",
             "correct": False,
             "why": "Nothing pulls on the bag. Its shape is decided by the "
                    "collisions arriving on each side of the plastic."},
            {"text": "Air has been forced into the bag through the plastic "
                     "by the cabin's pumps.",
             "correct": False,
             "why": "The bag is sealed and no air enters it. The same "
                    "particles simply have more room once the outside "
                    "pushes back less."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h23",
        "band": "harder",
        "text": "A sealed rigid can of gas and a tied balloon are both "
                "moved into a hot room. Compare what happens to the "
                "pressure inside each of them.",
        "options": [
            {"text": "Both pressures rise by the same amount, because both "
                     "hold gas and both are heated alike.",
             "correct": False,
             "why": "The balloon grows instead, giving its particles a "
                    "longer journey to the rubber, so its pressure stays "
                    "close to the room's."},
            {"text": "The balloon's pressure rises sharply while the can's "
                     "holds still, because rubber traps heat better than "
                     "metal does.",
             "correct": False,
             "why": "The can cannot change size, so its faster particles "
                    "have nowhere to go but into more collisions with the "
                    "walls."},
            {"text": "The can's pressure rises sharply while the balloon's "
                     "barely changes, because the balloon can grow and the "
                     "can cannot.",
             "correct": True},
            {"text": "Neither pressure changes, because no particles have "
                     "been added to either of them.",
             "correct": False,
             "why": "Heating raises a pressure without adding a single "
                    "particle: the particles already there arrive more "
                    "often and hit harder."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h24",
        "band": "harder",
        "text": "A student writes: space is a vacuum, so it sucks an "
                "astronaut's body outwards, and the suit is there to "
                "resist that pull. Evaluate the student's account.",
        "options": [
            {"text": "It is entirely right, because a vacuum does pull on "
                     "anything at its edge.",
             "correct": False,
             "why": "A vacuum has nothing inside it to do any pulling. "
                    "Only the side that has particles can push."},
            {"text": "The suit is not needed at all, because a body is "
                     "sealed and holds itself together.",
             "correct": False,
             "why": "A suit is very much needed. It supplies the outside "
                    "push that the missing air used to provide."},
            {"text": "Space is not really a vacuum, so there is nothing "
                     "there for the suit to resist.",
             "correct": False,
             "why": "Space is very close to a true vacuum. The error is in "
                    "the pulling, not in how empty it is."},
            {"text": "Nothing pulls: the astronaut's own body pushes "
                     "outwards, with nothing outside to push back.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h25",
        "band": "harder",
        "text": "Two identical rigid tanks are joined by a closed tap. "
                "Tank A holds gas at 200 kPa; every particle has been "
                "pumped out of tank B. The tap is opened. Predict the "
                "pressure afterwards, at the same temperature.",
        "options": [
            {"text": "About 200 kPa in both, because no particles have "
                     "been lost.",
             "correct": False,
             "why": "The particles are all still there, but they now have "
                    "twice the room, so each reaches a wall about half as "
                    "often."},
            {"text": "About 100 kPa in both, because the same particles "
                     "now have twice the room.",
             "correct": True},
            {"text": "200 kPa in A and nothing in B, because a gas will "
                     "not move into empty space by itself.",
             "correct": False,
             "why": "Gas particles are already travelling in every "
                    "direction, so they cross into B the moment the tap "
                    "opens."},
            {"text": "About 400 kPa in both, because the vacuum in B draws "
                     "the gas across hard.",
             "correct": False,
             "why": "A vacuum draws nothing. The gas spreads because its "
                    "particles were already moving, and spreading lowers "
                    "the pressure."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h26",
        "band": "harder",
        "text": "Explain why the air inside a blown-up balloon must be at "
                "a slightly greater pressure than the air outside it.",
        "options": [
            {"text": "The two must be exactly equal, or the balloon would "
                     "not stay the same size.",
             "correct": False,
             "why": "The stretched rubber pushes inwards as well, so the "
                    "inside has to beat the outside by just enough to "
                    "balance it."},
            {"text": "The air inside the balloon is warmer than the room, "
                     "because it came straight out of somebody's lungs "
                     "when it was blown up.",
             "correct": False,
             "why": "A balloon blown up hours ago has long since cooled to "
                    "room temperature, and it is still tight."},
            {"text": "The stretched rubber pushes inwards too, so the air "
                     "inside must push harder to hold the skin where it "
                     "is.",
             "correct": True},
            {"text": "There are far more particles inside the balloon than "
                     "there are outside it.",
             "correct": False,
             "why": "A room holds vastly more air than a balloon does. "
                    "What matters is how often particles arrive on each "
                    "side of the rubber."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h27",
        "band": "harder",
        "text": "A student says a sealed can at 200 kPa must hold twice as "
                "much gas as a sealed can at 100 kPa. Evaluate that claim.",
        "options": [
            {"text": "It holds only if the two cans are the same size and "
                     "at the same temperature; otherwise the pressure "
                     "alone cannot tell you.",
             "correct": True},
            {"text": "It always holds, because the pressure of a gas is a "
                     "straight count of the particles in it and of nothing "
                     "else at all.",
             "correct": False,
             "why": "Temperature and the size of the can both change a "
                    "pressure without changing the number of particles at "
                    "all."},
            {"text": "It never holds, because the pressure of a gas and "
                     "the amount of gas in a container have nothing at all "
                     "to do with each other.",
             "correct": False,
             "why": "They are connected. Add particles to a fixed "
                    "container at a fixed temperature and the pressure "
                    "rises in step."},
            {"text": "It holds only when the two cans contain different "
                     "gases from each other.",
             "correct": False,
             "why": "Which gas it is does not come into it. What matters "
                    "is the size of the can and the temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h28",
        "band": "harder",
        "text": "A sealed gas is squeezed into a smaller container and "
                "cooled at the same time. Predict what happens to its "
                "pressure.",
        "options": [
            {"text": "It must rise, because squeezing a gas into less "
                     "space always outweighs whatever cooling it at the "
                     "same time can do.",
             "correct": False,
             "why": "Neither change automatically outweighs the other. A "
                    "small squeeze with a large drop in temperature lowers "
                    "the pressure."},
            {"text": "It cannot be decided without knowing the size of "
                     "each change, because squeezing raises the pressure "
                     "and cooling lowers it.",
             "correct": True},
            {"text": "It must fall, because cooling takes energy out of "
                     "the gas, and the energy of the particles is what a "
                     "pressure really is.",
             "correct": False,
             "why": "Pressure is not energy. It is how often and how hard "
                    "particles arrive at a wall, and squeezing raises the "
                    "arrival rate."},
            {"text": "It stays exactly the same, because a squeeze and a "
                     "cooling of any size at all always cancel each other "
                     "out exactly.",
             "correct": False,
             "why": "Nothing makes the two match. The result depends "
                    "entirely on how big each of the changes is."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h29",
        "band": "harder",
        "text": "A student measures atmospheric pressure at the foot of a "
                "hill and again 100 m higher, and finds it has fallen by "
                "about 1 kPa. Estimate the fall over a climb of 500 m, and "
                "state the assumption behind the estimate.",
        "options": [
            {"text": "About 5 kPa, assuming the temperature falls by the "
                     "same amount every 100 m.",
             "correct": False,
             "why": "The estimate rests on the rate at which the air thins "
                    "with height, not on anything the temperature does."},
            {"text": "About 5 kPa, assuming the air keeps thinning at the "
                     "same rate all the way up.",
             "correct": True},
            {"text": "About 1 kPa, assuming the fall is the same however "
                     "far you climb.",
             "correct": False,
             "why": "The fall of 1 kPa is per 100 m, so climbing five "
                    "times as far gives about five times the fall."},
            {"text": "About 500 kPa, assuming every metre climbed costs 1 "
                     "kPa of pressure.",
             "correct": False,
             "why": "It is 1 kPa per 100 m, not per metre. 500 kPa is five "
                    "times the whole atmosphere."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h30",
        "band": "harder",
        "text": "A sealed rigid can of gas is at 100 kPa. A student wants "
                "to double its pressure and suggests three ways: heat it, "
                "pump more gas in, or squeeze it into half the space. "
                "Explain which one cannot be done to this can.",
        "options": [
            {"text": "Heating it, because heating a sealed can changes "
                     "only the speed of the particles inside.",
             "correct": False,
             "why": "Changing their speed is exactly what raises a "
                    "pressure: faster particles arrive more often and hit "
                    "harder."},
            {"text": "Pumping gas in, because a sealed can is already full "
                     "and cannot take more.",
             "correct": False,
             "why": "A gas is mostly empty space, so far more particles "
                    "can always be forced into the same can."},
            {"text": "Squeezing it, because the can is rigid and its "
                     "volume cannot be changed.",
             "correct": True},
            {"text": "None of them, because a rigid can will still squeeze "
                     "if you push hard enough.",
             "correct": False,
             "why": "Rigid means the volume does not change, however hard "
                    "it is pushed. That is what rules the third method "
                    "out."},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h31",
        "band": "harder",
        "text": "A gas cylinder's gauge reads 0 kPa and the cylinder is "
                "described as empty. Explain what that reading actually "
                "tells you.",
        "options": [
            {"text": "Every last particle has been driven out of the "
                     "cylinder through its valve, so there is now a vacuum "
                     "inside it.",
             "correct": False,
             "why": "Gas stops flowing out once the inside matches the "
                    "outside, and that leaves a cylinder still full of "
                    "gas."},
            {"text": "The gas inside has cooled right down until its "
                     "particles have stopped moving about altogether in "
                     "there.",
             "correct": False,
             "why": "Gas particles never stop. A zero reading is about the "
                    "difference between inside and outside, not about "
                    "motion."},
            {"text": "The gauge must be broken, because a sealed cylinder "
                     "with gas in it can never read a pressure of zero.",
             "correct": False,
             "why": "A working gauge reads zero whenever the inside and "
                    "the outside pressures match, which is perfectly "
                    "ordinary."},
            {"text": "The gas inside is now at about the pressure of the "
                     "air outside, so there is still plenty of gas in it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-04-h32",
        "band": "harder",
        "text": "The air in a room is at about 100 kPa, and so is the air "
                "inside your lungs. Explain what has to happen for air to "
                "move into your lungs when you breathe in.",
        "options": [
            {"text": "Your lungs take hold of the air and pull it in, in "
                     "just the same way that a straw pulls a drink up into "
                     "your mouth.",
             "correct": False,
             "why": "Neither a lung nor a straw pulls. Both work by "
                    "lowering the pressure inside so that the outside air "
                    "is pushed in."},
            {"text": "Your body warms the air in the room until it is "
                     "light enough to float up on its own and into your "
                     "open mouth.",
             "correct": False,
             "why": "Air is not made to float into anyone. Breathing works "
                    "by making the pressure in the chest lower than the "
                    "pressure outside."},
            {"text": "Your chest gets bigger, which lowers the pressure in "
                     "your lungs below the room's, so the outside air is "
                     "pushed in.",
             "correct": True},
            {"text": "The pressure of the room rises briefly and forces "
                     "air into everyone in it.",
             "correct": False,
             "why": "The room's pressure does not change when you breathe. "
                    "What changes is the pressure inside your own chest."},
        ],
        "figure": None,
    },
]
