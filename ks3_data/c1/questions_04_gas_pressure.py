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
]
