"""P4 lesson 05 — Friction: twelve questions (MRB-223).

Written against Design's page. The stuck crate, the drag bench and the
four rules are hers.

The discriminations, in the order the lesson builds them:

  · friction acts AGAINST the sliding, never with it;
  · it is a property of the PAIR of surfaces, not of one of them;
  · it grows with how hard they are pressed together;
  · it is largest just before sliding starts (`FORCE-28`);
  · it exists before anything moves (`FORCE-30`) — the harder band sits
    here and on smooth-is-not-slippery (`FORCE-29`).

⚠️ POSITION IS AUTHORED — index cycles 2, 1, 3, 0, giving three of each.

⚠️ Rung 1 (the 40 N sledge on snow) and Rung 2 (the toolbox on a sloping
roof) are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "friction"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-05-e01",
        "band": "easier",
        "text": "Friction always acts…",
        "options": [
            {"text": "downwards", "correct": False,
             "why": "That is weight. Friction acts along the surfaces, "
                    "whichever way they are facing."},
            {"text": "in the direction of movement", "correct": False,
             "why": "The opposite. Friction acts against the sliding "
                    "between the surfaces."},
            {"text": "against the sliding", "correct": True},
            {"text": "away from the heavier object", "correct": False,
             "why": "Mass does not set the direction. The sliding does."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e02",
        "band": "easier",
        "text": "Rubbing your hands together makes them warm. What does this "
                "show about friction?",
        "options": [
            {"text": "That friction only happens between skin and skin",
             "correct": False,
             "why": "It happens between any two surfaces sliding across each "
                    "other."},
            {"text": "That friction turns movement into heat",
             "correct": True},
            {"text": "That friction creates energy", "correct": False,
             "why": "Nothing creates energy. The movement is turned into "
                    "heat, which is a transfer rather than a creation."},
            {"text": "That friction disappears once things are warm",
             "correct": False,
             "why": "Keep rubbing and they keep getting warmer. The friction "
                    "is still there."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e03",
        "band": "easier",
        "text": "The same block is dragged over carpet and then over "
                "polished wood. What happens to the reading on the spring "
                "balance?",
        "options": [
            {"text": "It goes up on the wood", "correct": False,
             "why": "Polished wood grips less than carpet, so it takes a "
                    "smaller pull."},
            {"text": "It goes down on the wood", "correct": True},
            {"text": "It stays the same — the block has not changed",
             "correct": False,
             "why": "Friction is a property of the PAIR of surfaces. Change "
                    "one and the reading changes."},
            {"text": "It drops to zero on the wood", "correct": False,
             "why": "It still takes a real pull to keep the block sliding. "
                    "No surface has zero friction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e04",
        "band": "easier",
        "text": "Where is friction WANTED?",
        "options": [
            {"text": "In a bicycle chain", "correct": False,
             "why": "There it wastes energy as heat, which is why chains are "
                    "oiled."},
            {"text": "In a hip joint", "correct": False,
             "why": "A joint is lubricated precisely to keep friction as low "
                    "as possible."},
            {"text": "In a drawer that sticks and will not slide open", "correct": False,
             "why": "That is friction being a nuisance. Nobody wants a "
                    "drawer that will not open."},
            {"text": "Between a brake block and a wheel rim", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-05-s01",
        "band": "standard",
        "text": "A crate needs a 90 N push to break away and a 75 N push to "
                "keep sliding. Why is the first number bigger?",
        "options": [
            {"text": "Because the crate is heavier before it moves.",
             "correct": False,
             "why": "Nothing about the crate changed. Its weight is the same "
                    "throughout."},
            {"text": "Because left at rest the two surfaces settle into one "
                     "another, and sliding never lets them settle again.",
             "correct": True},
            {"text": "Because your push gets stronger once it is moving, "
                     "and a moving push is worth more than a still one",
             "correct": False,
             "why": "It gets weaker — you need less. The change is in the "
                    "friction, not in you."},
            {"text": "Because friction only appears once something moves.",
             "correct": False,
             "why": "It is at its LARGEST just before movement. That is the "
                    "90 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s02",
        "band": "standard",
        "text": "A 4 kg block on a surface needs 14 N to keep it sliding. "
                "What happens when the same block is loaded to 8 kg on the "
                "SAME surface?",
        "options": [
            {"text": "It still needs about 14 N.", "correct": False,
             "why": "Friction grows with how hard the surfaces are pressed "
                    "together, and the load has doubled."},
            {"text": "It needs about 28 N.", "correct": True},
            {"text": "It needs about 7 N.", "correct": False,
             "why": "That is half. Doubling the load makes the friction "
                    "bigger, not smaller."},
            {"text": "It cannot be worked out without knowing the surface "
                     "again.", "correct": False,
             "why": "The surface is the same, so the grip is the same. Only "
                    "the load has changed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s03",
        "band": "standard",
        "text": "A book rests on a desk lid that is slowly being tilted. For "
                "the first few degrees it does not slide. What is holding "
                "it?",
        "options": [
            {"text": "Nothing — gravity is not pulling it down the slope "
                     "yet.", "correct": False,
             "why": "Gravity pulls it down the slope from the very first "
                    "degree of tilt. Something is matching that pull."},
            {"text": "The weight of the book itself.", "correct": False,
             "why": "The weight is what is trying to move it. Something else "
                    "is resisting."},
            {"text": "Air resistance on the book.", "correct": False,
             "why": "It is not moving, so there is no air being pushed out "
                    "of the way."},
            {"text": "Friction, acting UP the slope.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s04",
        "band": "standard",
        "text": "Two sheets of glass are very smooth, yet they are hard to "
                "slide apart. What does this show?",
        "options": [
            {"text": "That glass is a special case and the rules do not "
                     "apply.", "correct": False,
             "why": "The rules apply. What the case shows is that one of the "
                    "everyday assumptions is wrong."},
            {"text": "That smooth is not the same as slippery.",
             "correct": True},
            {"text": "That glass has no friction, so the sheets are stuck "
                     "for another reason.", "correct": False,
             "why": "Friction is exactly what is holding them. Under a "
                    "microscope no surface is flat."},
            {"text": "That friction only exists on rough surfaces.",
             "correct": False,
             "why": "The two sheets disprove that on the spot."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-05-h01",
        "band": "harder",
        "text": "Why does friction depend on how hard two surfaces are "
                "pressed together, rather than on how big the block looks?",
        "options": [
            {"text": "Because a bigger block traps more air underneath it, "
                     "and that cushion of air is what has to be dragged "
                     "along.",
             "correct": False,
             "why": "There is no cushion of air to drag. The gripping is "
                    "done by the peaks that touch."},
            {"text": "Because a bigger block is always heavier, and the "
                     "sheer size of a block is what sets how much friction "
                     "it feels.",
             "correct": False,
             "why": "Not necessarily — and even at the same weight, "
                    "spreading the block over a wider area does not change "
                    "the friction."},
            {"text": "Because only the highest peaks are actually touching, "
                     "and pressing harder flattens them so more come into "
                     "contact.", "correct": True},
            {"text": "Because a bigger block has more surface to heat up, "
                     "and it is the heating that decides how much friction "
                     "there is",
             "correct": False,
             "why": "Heating is a consequence of friction, not what sets its "
                    "size."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h02",
        "band": "harder",
        "text": "In curling, sweeping melts a very thin film of water in "
                "front of the stone. Why does the stone then travel "
                "further?",
        "options": [
            {"text": "The water pushes the stone forwards, adding to "
                     "whatever the throw gave it, which is why a thrown "
                     "stone speeds up under water", "correct": False,
             "why": "Nothing pushes it forwards. The stone was already "
                    "moving and needs no push."},
            {"text": "The water keeps the surfaces apart, so the backwards "
                     "friction is smaller and the stone slows more "
                     "gradually.", "correct": True},
            {"text": "The water makes the stone lighter.", "correct": False,
             "why": "Its weight is unchanged. What changes is the force "
                    "resisting the slide."},
            {"text": "Sweeping adds energy to the stone.", "correct": False,
             "why": "The sweepers never touch the stone. They change the ice "
                    "in front of it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h03",
        "band": "harder",
        "text": "A cyclist oils the chain and fits new brake blocks the same "
                "afternoon. Which sentence describes both jobs correctly?",
        "options": [
            {"text": "Both jobs reduce friction, because friction is always "
                     "wasteful.", "correct": False,
             "why": "New brake blocks INCREASE the friction at the rim. "
                    "Without it the brakes do nothing."},
            {"text": "Both jobs increase friction, to give better control.",
             "correct": False,
             "why": "Oiling the chain reduces it, which is the whole point "
                    "of oil."},
            {"text": "Friction is wanted or unwanted depending on the job, "
                     "and each part is being tuned for its own.",
             "correct": True},
            {"text": "Neither job is about friction — oil and rubber do "
                     "different things, and only one of them touches the "
                     "surface", "correct": False,
             "why": "Both are about friction, in opposite directions."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h04",
        "band": "harder",
        "text": "A student says “polished wood has no friction, so a block "
                "on it would never stop.” Which reply is best?",
        "options": [
            {"text": "The bench shows it still takes 8 N to keep the block "
                     "sliding on polished wood, so friction is real there.",
             "correct": True},
            {"text": "They are right, and that is why polished floors are "
                     "dangerous: a smooth surface has nothing left to grip "
                     "with", "correct": False,
             "why": "Polished floors are slippery, not frictionless. A "
                    "block on one does stop."},
            {"text": "They are wrong, because friction only acts on rough "
                     "surfaces.", "correct": False,
             "why": "The verdict is right and the reason is wrong — two "
                    "sheets of glass are smooth and grip strongly."},
            {"text": "They are wrong, because air resistance would stop it "
                     "anyway.", "correct": False,
             "why": "Air resistance is real but tiny at a block's speed. The "
                    "point is that the wood itself resists."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-05-e05",
        "band": "easier",
        "text": "Which of these REDUCES friction?",
        "options": [
            {"text": "Fitting rubber grips to a handle", "correct": False,
             "why": "Rubber is chosen to increase grip, which means more "
                    "friction, not less."},
            {"text": "Oiling the moving parts of a machine", "correct": True},
            {"text": "Roughening a surface with sandpaper", "correct": False,
             "why": "A rougher surface gives more friction, which is why "
                    "sandpaper works at all."},
            {"text": "Pressing two surfaces together more firmly",
             "correct": False,
             "why": "Pressing harder increases friction — that is one of the "
                    "two things its size depends on."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e06",
        "band": "easier",
        "text": "When two surfaces rub together, where does the energy end "
                "up?",
        "options": [
            {"text": "In the thermal stores of the two surfaces",
             "correct": True},
            {"text": "It is destroyed by the rubbing", "correct": False,
             "why": "Nothing destroys energy. Rubbing moves it into thermal "
                    "stores."},
            {"text": "In the elastic store of the moving object",
             "correct": False,
             "why": "Nothing is stretched or squashed by sliding, so no "
                    "elastic store fills."},
            {"text": "Back in the chemical store it came from",
             "correct": False,
             "why": "Energy does not return the way it came; the warmed "
                    "surfaces are where it goes."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-05-s05",
        "band": "standard",
        "text": "A box is pushed with 50 N and does not move at all. What is "
                "the friction on it?",
        "options": [
            {"text": "0 N, because friction only exists once something slides",
             "correct": False,
             "why": "Friction acts before sliding starts — it is exactly what "
                    "is stopping the box moving."},
            {"text": "50 N, acting backwards against the push",
             "correct": True},
            {"text": "As much as the surfaces can possibly manage",
             "correct": False,
             "why": "It matches the push up to a limit; here it matches "
                    "exactly 50 N and no more."},
            {"text": "100 N, because it must beat the push", "correct": False,
             "why": "More than the push would drive the box backwards, and it "
                    "is not moving at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s06",
        "band": "standard",
        "text": "Why does a rubber tyre grip a road better than a smooth "
                "plastic wheel of the same size?",
        "options": [
            {"text": "Because rubber is heavier, so it presses down harder",
             "correct": False,
             "why": "The car's weight sets how hard it presses, not what the "
                    "wheel is made of."},
            {"text": "Because plastic has no friction at all",
             "correct": False,
             "why": "Every real surface has some. Plastic on tarmac simply "
                    "has much less than rubber does."},
            {"text": "Because friction depends on the surfaces, and rubber "
                     "on tarmac gives more",
             "correct": True},
            {"text": "Because rubber is softer, so it slides more easily",
             "correct": False,
             "why": "Sliding more easily would be LESS grip, which is the "
                    "opposite of what a tyre is for."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-05-h05",
        "band": "harder",
        "text": "A crate needs 90 N to break away and 75 N to keep sliding. "
                "What happens if the 90 N push is held on once it is moving?",
        "options": [
            {"text": "It slides at a steady speed, because 90 N was the "
                     "amount needed",
             "correct": False,
             "why": "Once moving, friction drops to 75 N, so 90 N leaves "
                    "15 N over."},
            {"text": "It stops again, because the push is now too big",
             "correct": False,
             "why": "A push larger than friction never stops anything; it "
                    "speeds it up."},
            {"text": "It speeds up, because there is a 15 N resultant force",
             "correct": True},
            {"text": "Nothing changes, because friction always matches the "
                     "push exactly",
             "correct": False,
             "why": "Friction matches the push only up to the point of "
                    "sliding; after that it settles at 75 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h06",
        "band": "harder",
        "text": "Running spikes and ice skates both work by changing "
                "friction. Which description is right?",
        "options": [
            {"text": "Spikes increase friction for grip; skates reduce it so "
                     "the blade slides",
             "correct": True},
            {"text": "Both increase friction, one on a track and one on ice",
             "correct": False,
             "why": "A skater who could not slide would go nowhere; the blade "
                    "is designed for very little friction."},
            {"text": "Both reduce friction so that the athlete moves more "
                     "freely",
             "correct": False,
             "why": "A sprinter with no grip could not push off at all — "
                    "spikes are there to increase it."},
            {"text": "Spikes reduce friction for speed; skates increase it "
                     "for control",
             "correct": False,
             "why": "The two are the wrong way round: spikes bite in, and a "
                    "blade glides."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · easier ────────────────────────────────
    {
        "id": "p4-05-e07",
        "band": "easier",
        "text": "A hand rubs firmly across a tabletop. In which direction "
                "does the friction on the hand act?",
        "options": [
            {"text": "Against the direction the hand is sliding.",
             "correct": True},
            {"text": "In the same direction as the hand is sliding, adding "
                     "to the push.", "correct": False,
             "why": "Friction always opposes the sliding between the two "
                    "surfaces; it never adds to it."},
            {"text": "Sideways, at right angles to the sliding.",
             "correct": False,
             "why": "Friction acts along the line of the sliding, not "
                    "across it."},
            {"text": "Downwards, because that is the direction of weight.",
             "correct": False,
             "why": "Weight is a separate force acting on the hand; "
                    "friction acts along the surfaces in contact."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e08",
        "band": "easier",
        "text": "A shoe pushes backwards against the ground as someone "
                "walks. Which way does friction from the ground act on the "
                "shoe?",
        "options": [
            {"text": "Backwards, the same way the shoe pushed.",
             "correct": False,
             "why": "Friction on the SHOE acts opposite to what the SHOE "
                    "does to the ground, which makes it forwards here."},
            {"text": "Forwards, which is what actually propels the walker "
                     "along.", "correct": True},
            {"text": "Downwards, matching the walker's weight.",
             "correct": False,
             "why": "Friction acts along the surfaces in contact, "
                    "horizontally here, not vertically."},
            {"text": "There is no friction while walking, since the foot "
                     "keeps lifting off.", "correct": False,
             "why": "Each footfall presses and slides slightly against the "
                    "ground, and friction acts throughout that contact."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e09",
        "band": "easier",
        "text": "A block is dragged to the left across a bench. Which way "
                "does friction act on the block?",
        "options": [
            {"text": "To the left, along with the drag.", "correct": False,
             "why": "Friction opposes sliding; it does not act with it."},
            {"text": "Upwards, lifting the block slightly off the "
                     "surface as though the drag itself were somehow "
                     "pulling it up and away.", "correct": False,
             "why": "Friction acts along the surfaces in contact, not "
                    "perpendicular to them."},
            {"text": "To the right, against the direction of the drag.",
             "correct": True},
            {"text": "It depends on how heavy the block is, since "
                     "heavier objects always drag along in the direction "
                     "of the pull.", "correct": False,
             "why": "Weight changes the SIZE of the friction, not which "
                    "way it points."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e10",
        "band": "easier",
        "text": "A trainer sole is tested first on tarmac and then on wet "
                "tiles, with nothing else changed. Why does the grip "
                "differ?",
        "options": [
            {"text": "Because the trainer itself somehow changes its own "
                     "grip between the two different tests, even though "
                     "nothing about it was altered.", "correct": False,
             "why": "The same trainer is used both times; nothing about it "
                    "changes."},
            {"text": "Because grip is supposedly a completely fixed "
                     "property that belongs entirely to the shoe alone, "
                     "whatever floor it happens to be tested on.",
             "correct": False,
             "why": "If it were fixed to the shoe alone, it would not "
                    "differ between the two floors."},
            {"text": "Because tarmac and tiles weigh different amounts.",
             "correct": False,
             "why": "The weight of the floor has nothing to do with the "
                    "friction between it and the shoe."},
            {"text": "Because friction depends on BOTH surfaces, and the "
                     "tiles are a different partner from the tarmac.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e11",
        "band": "easier",
        "text": "The same rope is tested against a smooth pole and then "
                "against a rough pole. What does the different amount of "
                "grip show?",
        "options": [
            {"text": "That friction is a property of the pair of surfaces, "
                     "not of the rope alone.", "correct": True},
            {"text": "That the rope itself must be changing its own grip "
                     "between the two different tests, even though it is "
                     "exactly the same rope both times.", "correct": False,
             "why": "The rope is unchanged; what differs is the surface it "
                    "is touching."},
            {"text": "That thicker ropes generally grip more.", "correct": False,
             "why": "Thickness has not changed between the two tests; only "
                    "the pole's surface has."},
            {"text": "That friction is decided entirely and exclusively "
                     "by the pole on its own, with the rope itself never "
                     "making any difference to it at all.", "correct": False,
             "why": "Both surfaces matter; changing the rope as well would "
                    "also change the grip."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e12",
        "band": "easier",
        "text": "A sledge slides easily on packed snow but drags heavily on "
                "bare gravel. What does this tell you about friction?",
        "options": [
            {"text": "It depends only and entirely on how heavy the "
                     "sledge happens to be, regardless of whatever surface "
                     "it is being dragged across.", "correct": False,
             "why": "The sledge's weight has not changed between the two "
                    "surfaces; the ground has."},
            {"text": "It depends on which two surfaces are sliding against "
                     "each other.", "correct": True},
            {"text": "It is the same on every surface, and the difference "
                     "between them is simply imagined by whoever is "
                     "dragging it.", "correct": False,
             "why": "The dragging is real and measurable, showing the "
                    "surfaces genuinely differ."},
            {"text": "It depends on the colour of the ground.",
             "correct": False,
             "why": "Colour makes no difference to grip; texture and "
                    "material do."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e13",
        "band": "easier",
        "text": "A rucksack is loaded with more books, pressing down harder "
                "on the ground as someone drags it. What happens to the "
                "friction?",
        "options": [
            {"text": "It gets smaller.", "correct": False,
             "why": "Pressing the surfaces together harder increases "
                    "friction, not decreases it."},
            {"text": "It stays exactly the same.", "correct": False,
             "why": "The load pressing the surfaces together has changed, "
                    "and friction responds to that."},
            {"text": "It gets bigger.", "correct": True},
            {"text": "It disappears once the rucksack is full.",
             "correct": False,
             "why": "A heavier rucksack has MORE friction to overcome, not "
                    "none at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e14",
        "band": "easier",
        "text": "Two identical boxes are pushed across the same floor, one "
                "empty and one full of tins. Which box needs more force to "
                "keep sliding?",
        "options": [
            {"text": "The empty one.", "correct": False,
             "why": "Less weight presses the surfaces together less "
                    "firmly, giving LESS friction to overcome."},
            {"text": "Both need exactly the same force.", "correct": False,
             "why": "Their weights differ, and friction grows with how "
                    "hard the surfaces are pressed together."},
            {"text": "Neither needs any force once already moving.",
             "correct": False,
             "why": "Keeping something sliding at a steady speed still "
                    "needs a force to match the friction."},
            {"text": "The full one.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e15",
        "band": "easier",
        "text": "A drawing pin is pressed harder into a corkboard. What "
                "happens to the friction between the pin and the board?",
        "options": [
            {"text": "It increases, because the surfaces are pressed "
                     "together more firmly.", "correct": True},
            {"text": "It decreases, because pressing harder squashes the "
                     "fibres flat, leaving less surface for anything to "
                     "grip onto.", "correct": False,
             "why": "Squashing the fibres does not remove them; pressing "
                    "harder increases the grip, not reduces it."},
            {"text": "It stays the same, since the pin itself has not been changed in any way.", "correct": False,
             "why": "The pin is unchanged, but how hard it presses against "
                    "the board has changed, and that is what friction "
                    "responds to."},
            {"text": "It becomes impossible to predict.", "correct": False,
             "why": "More pressing force reliably means more friction "
                    "between two given surfaces."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e16",
        "band": "easier",
        "text": "A crate needs a firm shove to get it moving, but only a "
                "gentle push once it is sliding. What does this show?",
        "options": [
            {"text": "The crate becomes lighter once it starts moving.",
             "correct": False,
             "why": "Its weight has not changed at all; only the friction "
                    "resisting it has."},
            {"text": "Friction is bigger just before sliding starts than "
                     "once it is under way.", "correct": True},
            {"text": "The floor becomes noticeably smoother once the crate has started sliding across it.", "correct": False,
             "why": "The floor's surface has not changed; the FRICTION has "
                    "simply dropped once sliding begins."},
            {"text": "The person pushing simply gets tired and starts "
                     "pushing less hard on purpose once the crate is "
                     "already moving.", "correct": False,
             "why": "The change is in the friction itself, not in how the "
                    "person happens to feel."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e17",
        "band": "easier",
        "text": "A heavy wardrobe is much harder to start moving across a "
                "carpet than to keep moving. What is this an example of?",
        "options": [
            {"text": "The wardrobe losing mass as it slides.",
             "correct": False,
             "why": "Its mass stays the same throughout; only the friction "
                    "changes."},
            {"text": "The carpet somehow becoming more slippery the very "
                     "moment contact with the wardrobe begins.",
             "correct": False,
             "why": "The carpet's surface does not change; the drop is in "
                    "the friction between it and the wardrobe."},
            {"text": "Friction being largest just before the surfaces "
                     "start to slide.", "correct": True},
            {"text": "The push needed depending mainly on the colour the wardrobe is painted.", "correct": False,
             "why": "Colour has no bearing on friction at all; the "
                    "surfaces and the load do."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e18",
        "band": "easier",
        "text": "A student notices a filing cabinet needs a hard shove to "
                "start sliding but glides easily once moving. Which "
                "statement explains this correctly?",
        "options": [
            {"text": "The cabinet somehow gets noticeably lighter the "
                     "very instant it starts moving across the floor.",
             "correct": False,
             "why": "Its weight is unchanged throughout; the difference is "
                    "in the friction."},
            {"text": "The floor changes texture once the cabinet is sliding, because the first movement polishes a smooth track under it.", "correct": False,
             "why": "The floor stays exactly the same surface the whole "
                    "time."},
            {"text": "Friction only begins once an object starts to "
                     "slide.", "correct": False,
             "why": "It is present even before sliding, which is why the "
                    "first shove is the hardest part."},
            {"text": "Friction drops once the cabinet is sliding, from its "
                     "largest value just before it moved.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e19",
        "band": "easier",
        "text": "Two polished metal plates, cleaned and pressed flat "
                "together, are surprisingly hard to slide apart. What does "
                "this show?",
        "options": [
            {"text": "That a very smooth surface can still have strong "
                     "friction.", "correct": True},
            {"text": "That metal has no friction at all normally.",
             "correct": False,
             "why": "Metal plates in everyday use clearly do have "
                    "friction, which is exactly why they resist sliding "
                    "here."},
            {"text": "That polishing removes all friction between two "
                     "surfaces.", "correct": False,
             "why": "Polishing has made them SMOOTHER, yet they grip "
                    "strongly — the opposite of removing friction."},
            {"text": "That the plates must be magnetic rather than "
                     "gripping by friction.", "correct": False,
             "why": "Nothing here suggests magnetism; ordinary surface "
                    "contact is enough to explain the strong grip."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e20",
        "band": "easier",
        "text": "Ice looks perfectly smooth, yet a shoe still grips it a "
                "little rather than sliding with zero resistance. What "
                "does this tell you?",
        "options": [
            {"text": "That ice has no friction at all.", "correct": False,
             "why": "Some grip remains, which means the friction is small "
                    "but not zero."},
            {"text": "That even a very smooth-looking surface still has "
                     "some friction.", "correct": True},
            {"text": "That the shoe is providing all of the grip on its "
                     "own.", "correct": False,
             "why": "Grip depends on BOTH the shoe and the ice, not on the "
                    "shoe alone."},
            {"text": "That friction cannot possibly exist on any surface "
                     "that looks smooth to the eye.", "correct": False,
             "why": "This example is exactly the opposite: a smooth-"
                    "looking surface still grips a little."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e21",
        "band": "easier",
        "text": "A heavy box is pushed but does not move at all. Is "
                "friction acting on it?",
        "options": [
            {"text": "No, because nothing is sliding yet.", "correct": False,
             "why": "Friction can act on objects that are not sliding, "
                    "matching the push exactly."},
            {"text": "No, friction only appears once motion begins.",
             "correct": False,
             "why": "It is present from the very first push, which is why "
                    "the box does not move."},
            {"text": "Yes, matching the push exactly and keeping the box "
                     "still.", "correct": True},
            {"text": "Yes, but only after several seconds of continuous "
                     "pushing.", "correct": False,
             "why": "It acts immediately the push begins, not after a "
                    "delay."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e22",
        "band": "easier",
        "text": "A parked car is nudged gently but does not move. What is "
                "providing the resistance that keeps it still?",
        "options": [
            {"text": "Nothing — the car is simply too heavy to feel a "
                     "gentle nudge.", "correct": False,
             "why": "Something is resisting the nudge, or any push however "
                    "small would move the car."},
            {"text": "The brakes alone, regardless of friction with the "
                     "road.", "correct": False,
             "why": "Even with the brakes off, friction between the tyres "
                    "and the road would resist a gentle nudge."},
            {"text": "The car's own weight pressing down on the road.",
             "correct": False,
             "why": "Weight presses down vertically; the resistance to a "
                    "sideways nudge is a horizontal friction force."},
            {"text": "Friction between the tyres and the road, matching "
                     "the push.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e23",
        "band": "easier",
        "text": "A sheet of paper is placed under a heavy book and given a "
                "gentle tug. It does not move at first. What is resisting "
                "the tug?",
        "options": [
            {"text": "Friction between the paper and the surface below the "
                     "book, matching the tug.", "correct": True},
            {"text": "The book's weight pulling the paper back.",
             "correct": False,
             "why": "Weight acts downwards, not sideways against the tug; "
                    "friction is what resists sideways sliding."},
            {"text": "Static electricity between the paper and the book.",
             "correct": False,
             "why": "Nothing here suggests electricity; ordinary surface "
                    "contact and friction explain it."},
            {"text": "The paper being glued to the surface.", "correct": False,
             "why": "The paper is not glued — it is simply held by "
                    "friction, matching a gentle tug up to a limit."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e24",
        "band": "easier",
        "text": "A cyclist's brake blocks get noticeably warm after a long, "
                "fast descent. Where has this warmth come from?",
        "options": [
            {"text": "It leaks out of the wheel's tyre.", "correct": False,
             "why": "Tyres do not supply heat; the warmth comes from the "
                    "braking surfaces themselves."},
            {"text": "Friction between the blocks and the rim has "
                     "transferred energy into their thermal stores.",
             "correct": True},
            {"text": "The brake blocks create new energy as they rub.",
             "correct": False,
             "why": "Nothing creates energy; rubbing transfers it into "
                    "thermal stores rather than making it from nothing."},
            {"text": "The air rushing past has warmed them up.",
             "correct": False,
             "why": "Air moving past a fast-moving object tends to cool it "
                    "down, not warm it up."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e25",
        "band": "easier",
        "text": "Two wooden blocks are rubbed together vigorously for a "
                "minute. What happens to their temperature, and why?",
        "options": [
            {"text": "It falls, because rubbing removes energy from them.",
             "correct": False,
             "why": "Rubbing does not remove energy from the blocks; it "
                    "adds to their thermal stores."},
            {"text": "It stays exactly the same, since wood does not "
                     "conduct heat well.", "correct": False,
             "why": "Even a poor conductor still warms up locally where "
                    "the friction is acting."},
            {"text": "It rises, because friction has transferred energy "
                     "from the movement into their thermal stores.",
             "correct": True},
            {"text": "It rises, because the wood chemically reacts as it "
                     "rubs.", "correct": False,
             "why": "Nothing chemical is happening; this is a physical "
                    "transfer of energy through friction, not a "
                    "reaction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e26",
        "band": "easier",
        "text": "Which of these is an example of friction being UNWANTED?",
        "options": [
            {"text": "A climber's hand gripping a rock hold.", "correct": False,
             "why": "That grip is exactly what friction is wanted for."},
            {"text": "A nail staying firmly in a piece of wood.",
             "correct": False,
             "why": "Friction is what keeps the nail in place, which is "
                    "wanted here."},
            {"text": "Chalk gripping a blackboard.", "correct": False,
             "why": "The grip between chalk and board is friction doing "
                    "its wanted job."},
            {"text": "Resistance between the moving parts inside a car engine.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e27",
        "band": "easier",
        "text": "Which situation shows friction being WANTED?",
        "options": [
            {"text": "A rock climber's shoes gripping a foothold.",
             "correct": True},
            {"text": "A conveyor-belt roller resisting the belt's motion.",
             "correct": False,
             "why": "Resistance in a roller is friction wasting energy, "
                    "which engineers try to reduce."},
            {"text": "A ship's hull dragging through water.", "correct": False,
             "why": "Drag through water wastes energy pushing the ship "
                    "along; it is not wanted there."},
            {"text": "A skater's blade catching on rough ice.",
             "correct": False,
             "why": "Catching on rough ice disrupts the glide a skater "
                    "wants; it is unwanted there."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e28",
        "band": "easier",
        "text": "In which of these is friction something engineers try "
                "hard to REDUCE?",
        "options": [
            {"text": "Between a car's tyres and the road.", "correct": False,
             "why": "Tyre grip is exactly the friction engineers want to "
                    "keep high, for safe braking and cornering."},
            {"text": "Between a rotating shaft and its bearing.",
             "correct": True},
            {"text": "Between a climbing rope and a belay device.",
             "correct": False,
             "why": "Friction there is used deliberately to control the "
                    "rope's speed."},
            {"text": "Between a shoe sole and a gym floor.", "correct": False,
             "why": "Grip between shoe and floor is wanted, to stop a "
                    "player slipping."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e29",
        "band": "easier",
        "text": "Which of these would REDUCE the friction between two metal "
                "surfaces?",
        "options": [
            {"text": "Pressing them together more firmly.", "correct": False,
             "why": "Pressing harder increases friction rather than "
                    "reducing it."},
            {"text": "Roughening both surfaces with a file.", "correct": False,
             "why": "A rougher surface grips more, which increases "
                    "friction."},
            {"text": "Adding a thin film of oil between them.",
             "correct": True},
            {"text": "Warming the surfaces with a heater.", "correct": False,
             "why": "Warming the metal does not itself change how the "
                    "surfaces grip each other."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-e30",
        "band": "easier",
        "text": "A workshop technician wants two metal plates to grip "
                "each other more firmly than before. Which action would "
                "achieve that?",
        "options": [
            {"text": "Coating them both in a layer of oil.", "correct": False,
             "why": "A layer of oil keeps the surfaces apart, which "
                    "reduces friction, not increases it."},
            {"text": "Polishing both surfaces until they shine.",
             "correct": False,
             "why": "Polishing tends to reduce friction slightly rather "
                    "than add to it."},
            {"text": "Cooling the surfaces down.", "correct": False,
             "why": "Temperature on its own does not change how firmly two "
                    "surfaces grip each other."},
            {"text": "Roughening both surfaces with sandpaper.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · standard ──────────────────────────────
    {
        "id": "p4-05-s07",
        "band": "standard",
        "text": "A 6 kg crate needs 18 N to keep sliding across a floor. If "
                "the load is increased to 12 kg on the SAME floor, roughly "
                "what force is needed to keep it sliding?",
        "options": [
            {"text": "About 36 N.", "correct": True},
            {"text": "About 18 N, unchanged.", "correct": False,
             "why": "Friction grows with how hard the surfaces are pressed "
                    "together, and the load has doubled."},
            {"text": "About 9 N.", "correct": False,
             "why": "That halves the force, but doubling the load makes "
                    "friction bigger, not smaller."},
            {"text": "It cannot be estimated without knowing the floor's "
                     "colour.", "correct": False,
             "why": "Colour is irrelevant; what matters is the surfaces "
                    "and how hard they are pressed together, which scale "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s08",
        "band": "standard",
        "text": "A 3 kg box needs 9 N to slide steadily on a bench. The "
                "same box is then loaded to 9 kg on the same bench. About "
                "how much force is now needed?",
        "options": [
            {"text": "About 9 N, since the bench has not changed.",
             "correct": False,
             "why": "The bench is the same, but the load pressing onto it "
                    "has trebled, and friction grows with that."},
            {"text": "About 27 N.", "correct": True},
            {"text": "About 3 N.", "correct": False,
             "why": "That is a reduction, but trebling the load increases "
                    "the friction, not decreases it."},
            {"text": "About 18 N.", "correct": False,
             "why": "That only doubles the original force, but the load "
                    "has trebled, not doubled."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s09",
        "band": "standard",
        "text": "A sledge needs 20 N to keep sliding when loaded to 5 kg. "
                "If the load is halved to 2.5 kg on the same snow, roughly "
                "what force is now needed?",
        "options": [
            {"text": "Still about 20 N.", "correct": False,
             "why": "Halving how hard the surfaces press together roughly "
                    "halves the friction as well."},
            {"text": "About 40 N.", "correct": False,
             "why": "That doubles the force, but the load has been "
                    "HALVED, not doubled."},
            {"text": "About 10 N.", "correct": True},
            {"text": "It cannot be estimated without a formula.",
             "correct": False,
             "why": "The same simple scaling used to double it can be used "
                    "to halve it — no formula beyond that is needed here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s10",
        "band": "standard",
        "text": "A 4 kg suitcase needs 12 N to slide across a floor. An "
                "identical, empty suitcase weighing 1 kg is tested on the "
                "same floor. About what force does it need?",
        "options": [
            {"text": "About 12 N, the same as before.", "correct": False,
             "why": "A much lighter case presses the floor far less "
                    "firmly, so it needs much less force."},
            {"text": "About 48 N.", "correct": False,
             "why": "That is far more than needed; a lighter case needs "
                    "LESS force, not more."},
            {"text": "About 6 N.", "correct": False,
             "why": "That only halves the value, but the mass has dropped "
                    "to a quarter, not a half."},
            {"text": "About 3 N.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s11",
        "band": "standard",
        "text": "A 90 N push is needed to start a crate sliding, and 75 N "
                "to keep it sliding. Explain why the two figures differ.",
        "options": [
            {"text": "Friction is largest just before sliding starts and "
                     "settles lower once the surfaces are moving.",
             "correct": True},
            {"text": "The crate becomes lighter once it starts sliding.",
             "correct": False,
             "why": "Its weight is unchanged throughout; only the friction "
                    "resisting it has changed."},
            {"text": "The push naturally gets easier and easier to give "
                     "the longer and longer someone keeps on pushing it.",
             "correct": False,
             "why": "The change is in the friction acting on the crate, "
                    "not in how tiring the push feels."},
            {"text": "The floor becomes smoother the moment the crate "
                     "starts moving.", "correct": False,
             "why": "The floor's surface has not changed at all; the drop "
                    "is in the friction, not the floor."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s12",
        "band": "standard",
        "text": "A box needs a 40 N push to start moving and 32 N to keep "
                "moving. If an identical box is loaded so it needs 80 N to "
                "start, about how much would you expect to keep it "
                "moving?",
        "options": [
            {"text": "About 32 N, the same as before.", "correct": False,
             "why": "The heavier box has more friction throughout, at both "
                    "the start and while sliding."},
            {"text": "About 64 N.", "correct": True},
            {"text": "About 40 N.", "correct": False,
             "why": "That is only the START figure from the lighter box; "
                    "the heavier box's sliding figure should scale up "
                    "too."},
            {"text": "About 80 N, the same as its start figure.",
             "correct": False,
             "why": "The sliding figure is always somewhat lower than the "
                    "start figure, in the same ratio as before."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s13",
        "band": "standard",
        "text": "A 2 kg block needs 6 N to keep sliding on a bench. A 2 kg "
                "block of a DIFFERENT material needs 15 N to keep sliding "
                "on the same bench. What does this show?",
        "options": [
            {"text": "That the second block must actually be heavier.",
             "correct": False,
             "why": "Both blocks are stated to have the same mass; what "
                    "differs is the material, not the weight."},
            {"text": "That the bench itself must somehow have changed "
                     "physically between the two separate tests.",
             "correct": False,
             "why": "The bench is the same throughout; the material of "
                    "the block sliding on it has changed."},
            {"text": "That friction depends on which materials are in "
                     "contact, not on the mass alone.", "correct": True},
            {"text": "That friction is completely unrelated to whichever "
                     "surfaces happen to be in contact with one another.",
             "correct": False,
             "why": "The surfaces are exactly what has changed here, and "
                    "the friction changed with them."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s14",
        "band": "standard",
        "text": "A rubber-soled shoe and a leather-soled shoe of the same "
                "weight are tested on the same tiled floor. The rubber "
                "sole grips far more strongly. What does this demonstrate?",
        "options": [
            {"text": "That rubber soles always weigh noticeably more than "
                     "leather ones of the very same size.", "correct": False,
             "why": "The shoes are stated to weigh the same; only the sole "
                    "material differs."},
            {"text": "That tiled floors, whatever the covering, "
                     "genuinely have no friction acting on them at all.",
             "correct": False,
             "why": "Both soles show measurable grip on the tiles, so the "
                    "floor clearly has friction."},
            {"text": "That the leather sole must be damaged.", "correct": False,
             "why": "Nothing suggests damage; leather genuinely grips less "
                    "strongly than rubber on tile."},
            {"text": "That friction depends on the pair of materials in "
                     "contact, not on weight alone.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s15",
        "band": "standard",
        "text": "A conveyor-belt roller runs in a well-oiled bearing. What "
                "has the oil done to the friction there, and why does it "
                "matter?",
        "options": [
            {"text": "It has reduced the friction, so less energy is "
                     "wasted heating the bearing.", "correct": True},
            {"text": "It has increased the friction quite a bit, to help "
                     "the roller grip more firmly onto the belt.",
             "correct": False,
             "why": "Oil is used specifically to reduce friction inside "
                    "the bearing, not to grip anything."},
            {"text": "It has removed the friction completely, since a film of oil holds the two metal surfaces apart so that neither one touches.",
             "correct": False,
             "why": "Oil reduces friction a great deal; it does not remove "
                    "it entirely."},
            {"text": "It has no effect on the friction at all.",
             "correct": False,
             "why": "Oil keeps the moving surfaces apart, which measurably "
                    "reduces the friction between them."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s16",
        "band": "standard",
        "text": "Sandpaper is glued to the tread of a climbing shoe to help "
                "on smooth rock. What is this doing to the friction, and "
                "why?",
        "options": [
            {"text": "Decreasing it, by smoothing the sole's surface.",
             "correct": False,
             "why": "Sandpaper roughens the surface; it does not smooth "
                    "it."},
            {"text": "Increasing it, by roughening the surface that meets "
                     "the rock.", "correct": True},
            {"text": "Having no effect, since rock is rock whatever the "
                     "sole is made of.", "correct": False,
             "why": "The sole's texture is exactly what changes how it "
                    "grips the same rock."},
            {"text": "Removing the friction so the shoe can glide more "
                     "easily.", "correct": False,
             "why": "Glide is the opposite of what a climbing shoe needs; "
                    "the sandpaper is there to grip, not glide."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s17",
        "band": "standard",
        "text": "A hovercraft rides on a cushion of air rather than "
                "wheels. What has this done to the friction with the "
                "ground, and why does it help?",
        "options": [
            {"text": "It has increased the friction, giving the craft more grip, because the cushion presses down on the ground harder than wheels would.", "correct": False,
             "why": "The whole point of the air cushion is to keep the "
                    "craft OFF the ground, cutting the friction almost to "
                    "nothing."},
            {"text": "It has had no real effect at all, since the craft "
                     "must still be touching the ground somewhere "
                     "underneath.", "correct": False,
             "why": "The air cushion is specifically there to keep the "
                    "craft from touching the ground at all."},
            {"text": "It has almost eliminated the friction, letting the "
                     "craft move with very little resistance.",
             "correct": True},
            {"text": "It has doubled the friction compared with wheels.",
             "correct": False,
             "why": "The air cushion reduces contact with the ground; it "
                    "does not add extra grip."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s18",
        "band": "standard",
        "text": "A climbing rope is passed through a metal belay device "
                "that grips it tightly when pulled. What role is friction "
                "playing here?",
        "options": [
            {"text": "None — the device works by magnetism, not friction.",
             "correct": False,
             "why": "There is no magnet involved; the device works "
                    "entirely by gripping the rope through friction."},
            {"text": "It is trying hard to reduce the friction on the "
                     "rope so that it can run through freely and "
                     "quickly.", "correct": False,
             "why": "The device is designed to INCREASE friction on the "
                    "rope when needed, not reduce it."},
            {"text": "It is relevant when the rope happens to be wet, since a dry rope passes through the metal without rubbing on it at all.", "correct": False,
             "why": "The friction in a belay device matters whether the "
                    "rope is wet or dry; it is not conditional on that."},
            {"text": "It is providing the controlled resistance that lets "
                     "a climber be safely lowered or held.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s19",
        "band": "standard",
        "text": "A cyclist's brake pads get warm on a long downhill run. "
                "Describe the energy change taking place at the pads.",
        "options": [
            {"text": "Kinetic energy of the bicycle is being transferred "
                     "into the thermal stores of the pads and rim, through "
                     "friction.", "correct": True},
            {"text": "Chemical energy stored in the pads is being released as heat, which is why brake material has to be renewed once it has been used up.", "correct": False,
             "why": "Brake pads do not store chemical energy for this "
                    "purpose; the warmth comes from friction converting "
                    "motion into heat."},
            {"text": "Electrical energy is building up in the pads as "
                     "they rub.", "correct": False,
             "why": "No electrical process is involved; this is a "
                    "straightforward mechanical transfer through "
                    "friction."},
            {"text": "The pads are simply absorbing warmth that has "
                     "drifted across from the surrounding air as the "
                     "bicycle speeds downhill.", "correct": False,
             "why": "The pads are the SOURCE of the warmth here, produced "
                    "by friction, not something absorbing it from the "
                    "air."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s20",
        "band": "standard",
        "text": "A blacksmith rubs two pieces of metal together vigorously "
                "and they become noticeably hot. Explain where this "
                "thermal energy has come from.",
        "options": [
            {"text": "It was already stored inside the metal and is "
                     "simply released by rubbing.", "correct": False,
             "why": "The metal did not contain that energy beforehand; the "
                    "rubbing is what transfers it in."},
            {"text": "The kinetic energy of the rubbing motion is "
                     "transferred into thermal energy by friction.",
             "correct": True},
            {"text": "The metal reacts chemically when rubbed, releasing "
                     "heat.", "correct": False,
             "why": "No chemical reaction takes place; this is a purely "
                    "physical transfer of energy through friction."},
            {"text": "Friction destroys some energy, and the missing "
                     "amount appears as heat.", "correct": False,
             "why": "No energy is destroyed; it is transferred into "
                    "thermal stores rather than lost."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s21",
        "band": "standard",
        "text": "A go-kart track deliberately uses a rough, high-grip "
                "surface rather than smooth tarmac. Explain the "
                "reasoning.",
        "options": [
            {"text": "Rough surfaces make karts lighter, so they go "
                     "faster.", "correct": False,
             "why": "Surface roughness does not change a kart's weight; it "
                    "changes the friction available."},
            {"text": "A rough surface reduces the friction so karts slide "
                     "more easily round bends.", "correct": False,
             "why": "The opposite is true — a rougher surface gives MORE "
                    "friction, helping karts grip round bends."},
            {"text": "More friction between the tyres and the track gives "
                     "better grip for accelerating and cornering.",
             "correct": True},
            {"text": "Rough surfaces are cheaper to build than smooth "
                     "ones.", "correct": False,
             "why": "Cost is not the physics reason; the reasoning here "
                    "concerns grip and friction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s22",
        "band": "standard",
        "text": "A skater's blade is kept smooth and sharp rather than "
                "rough. Explain why, in terms of friction.",
        "options": [
            {"text": "A rough blade would make the skater heavier.",
             "correct": False,
             "why": "Roughness does not add weight; it changes how much "
                    "the blade grips the ice."},
            {"text": "A rough blade would help the skater glide faster.",
             "correct": False,
             "why": "The opposite is true — roughening the blade would "
                    "increase friction and slow the glide, not help it."},
            {"text": "Friction between the blade and the ice does not "
                     "depend on the blade's own surface at all.",
             "correct": False,
             "why": "It very much does — a rough blade would grip more, "
                    "exactly what a smooth blade avoids."},
            {"text": "A smooth blade keeps the friction with the ice low, "
                     "allowing a fast, controlled glide.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s23",
        "band": "standard",
        "text": "A 5 kg block needs 15 N to keep sliding on a bench. It is "
                "then swapped for an 8 kg block of the SAME material on "
                "the same bench. Roughly what force will the heavier "
                "block need?",
        "options": [
            {"text": "About 24 N.", "correct": True},
            {"text": "About 15 N, unchanged.", "correct": False,
             "why": "The heavier block presses the bench more firmly, so "
                    "the friction on it should be bigger."},
            {"text": "About 12 N.", "correct": False,
             "why": "That is a decrease, but a heavier block gives MORE "
                    "friction, not less."},
            {"text": "It cannot be estimated at all without a formula.",
             "correct": False,
             "why": "The friction scales with how hard the surfaces are pressed together, so an estimate can be made from the two masses alone."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s24",
        "band": "standard",
        "text": "A 3 kg tin needs 9 N to slide steadily. Loaded to 6 kg on "
                "the same surface, about what force would you expect it to "
                "need?",
        "options": [
            {"text": "About 4.5 N.", "correct": False,
             "why": "That is a decrease, but doubling the load increases "
                    "the friction, not decreases it."},
            {"text": "About 18 N.", "correct": True},
            {"text": "About 9 N, unchanged.", "correct": False,
             "why": "The load pressing onto the surface has doubled, and "
                    "friction responds to that."},
            {"text": "About 36 N.", "correct": False,
             "why": "That scales up by four times, but the load has only "
                    "doubled."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s25",
        "band": "standard",
        "text": "A wooden crate needing 40 N to start sliding is emptied "
                "until it weighs half as much. Roughly what force would "
                "you now expect to start it sliding?",
        "options": [
            {"text": "Still about 40 N.", "correct": False,
             "why": "Less weight presses the crate onto the floor less "
                    "firmly, so less force should be needed."},
            {"text": "About 80 N.", "correct": False,
             "why": "That is an increase, but a lighter crate should need "
                    "LESS force to start sliding, not more."},
            {"text": "About 20 N.", "correct": True},
            {"text": "It cannot be estimated without knowing the crate's "
                     "colour.", "correct": False,
             "why": "Colour makes no difference to friction; the change "
                    "here is simply in the load."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s26",
        "band": "standard",
        "text": "A 10 kg case needs 25 N to slide steadily. An identical "
                "case loaded to 4 kg is tested on the same floor. Roughly "
                "what force is now needed?",
        "options": [
            {"text": "About 25 N, unchanged.", "correct": False,
             "why": "The lighter case presses the floor less firmly, so "
                    "the friction, and the force needed, should be "
                    "smaller."},
            {"text": "About 62.5 N.", "correct": False,
             "why": "That is an increase, but a lighter case should need "
                    "less force, not more."},
            {"text": "About 100 N.", "correct": False,
             "why": "That scales the wrong way — a lighter load reduces "
                    "the force needed rather than increasing it."},
            {"text": "About 10 N.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s27",
        "band": "standard",
        "text": "Explain why a heavier lorry generally needs a more "
                "powerful braking system than a light car.",
        "options": [
            {"text": "A heavier vehicle presses down harder on its brakes "
                     "and tyres, and needs a bigger friction force to "
                     "bring it to a stop in the same distance.",
             "correct": True},
            {"text": "Heavier vehicles are simply built with bigger brakes "
                     "for appearance.", "correct": False,
             "why": "The size of the brakes reflects the physics need for "
                    "more friction force, not appearance."},
            {"text": "Braking has nothing to do with friction, only with "
                     "the engine.", "correct": False,
             "why": "Braking relies entirely on friction, at the brakes "
                    "and at the tyres, not on the engine at all."},
            {"text": "A heavier vehicle actually needs LESS friction to "
                     "stop, since momentum helps it slow down.",
             "correct": False,
             "why": "Momentum makes a heavier vehicle harder to stop, not "
                    "easier, so more friction force is needed, not less."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s28",
        "band": "standard",
        "text": "A student oils a squeaky door hinge and the squeaking "
                "stops. Explain what has happened in terms of friction.",
        "options": [
            {"text": "The oil has increased the friction, silencing the "
                     "metal parts.", "correct": False,
             "why": "Oil reduces friction between the moving metal parts; "
                    "it does not increase it."},
            {"text": "The oil has reduced the friction between the metal "
                     "parts, which is what was causing the squeak.",
             "correct": True},
            {"text": "The oil has changed the hinge's mass, stopping the "
                     "vibration.", "correct": False,
             "why": "Oil is far too light to meaningfully change the "
                    "hinge's mass; it works by reducing friction."},
            {"text": "The squeak stopped because the door itself became "
                     "lighter.", "correct": False,
             "why": "The door's weight is unaffected by oiling the hinge; "
                    "the friction between the moving parts is what "
                    "changed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s29",
        "band": "standard",
        "text": "A cook rubs their oily hands together and the usual "
                "warming effect from rubbing barely happens. Explain why.",
        "options": [
            {"text": "Oily skin generates less heat energy overall.",
             "correct": False,
             "why": "The issue is not less energy overall, but that "
                    "friction — which converts the energy to heat — has "
                    "been reduced."},
            {"text": "The oil makes the hands heavier, reducing the "
                     "rubbing speed.", "correct": False,
             "why": "Oil does not meaningfully add weight; it works by "
                    "keeping the skin surfaces apart."},
            {"text": "The oil has reduced the friction between the hands, "
                     "so less energy is converted to heat.", "correct": True},
            {"text": "Oil absorbs the heat before it can be felt.",
             "correct": False,
             "why": "The heat is not being absorbed elsewhere; less of it "
                    "is being produced in the first place, because "
                    "friction is lower."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-s30",
        "band": "standard",
        "text": "A drawer sticks badly and a small amount of candle wax is "
                "rubbed along its runners. Explain why this helps.",
        "options": [
            {"text": "The wax makes the drawer lighter, so it slides more "
                     "easily.", "correct": False,
             "why": "Wax does not meaningfully change the drawer's weight; "
                    "it changes the friction on the runners."},
            {"text": "The wax roughens the runners, giving them more grip "
                     "to push against.", "correct": False,
             "why": "Wax is a lubricant — it smooths the sliding contact "
                    "and reduces friction rather than roughening it."},
            {"text": "The wax has no real effect; the improvement is "
                     "imagined.", "correct": False,
             "why": "The reduced friction from the wax coating is a real, "
                    "physical effect, not an imagined one."},
            {"text": "The wax reduces the friction between the runners and "
                     "the drawer, letting it slide more easily.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · harder ────────────────────────────────
    {
        "id": "p4-05-h07",
        "band": "harder",
        "text": "Two blocks of the same material and weight are pressed "
                "together, one with double the contact area of the other "
                "(same load, same material, spread over a bigger "
                "surface). Which has more friction resisting sliding?",
        "options": [
            {"text": "Neither — friction depends on the load and the "
                     "materials, not on the visible contact area.",
             "correct": True},
            {"text": "The one with more contact area, since a bigger "
                     "patch of visible surface touching should always "
                     "mean noticeably more grip overall.", "correct": False,
             "why": "Spreading the same load over a bigger visible area "
                    "does not increase friction; only the true "
                    "(microscopic) contact points matter, and pressing "
                    "harder is what changes those."},
            {"text": "The one with less contact area, since it presses harder on every square centimetre of the surface.", "correct": False,
             "why": "The friction between two given surfaces under the "
                    "same total load is essentially the same, regardless "
                    "of the visible area it is spread over."},
            {"text": "It cannot be determined without knowing the exact "
                     "shape of each block.", "correct": False,
             "why": "Shape is not the deciding factor here — visible area "
                    "does not change the true friction for the same load "
                    "and materials."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h08",
        "band": "harder",
        "text": "Pressing two rough surfaces together harder is found to "
                "increase the number of points that are genuinely in "
                "contact, even though the surfaces themselves have not "
                "changed. Explain why this happens.",
        "options": [
            {"text": "Because pressing harder heats the two surfaces up "
                     "quite noticeably, melting them together very "
                     "slightly at every point of contact.", "correct": False,
             "why": "No melting is involved at ordinary pressing forces; "
                    "the extra contact comes from flattening existing "
                    "peaks, not from heat."},
            {"text": "Because only the highest peaks touch at first, and "
                     "pressing harder flattens more of them into contact.",
             "correct": True},
            {"text": "Because the surfaces chemically bond more strongly under pressure, forming new joins between the two metals.", "correct": False,
             "why": "No new chemical bonding occurs; more of the already-"
                    "present peaks are simply brought into contact."},
            {"text": "Because harder pressing makes the surfaces smoother "
                     "overall.", "correct": False,
             "why": "The surfaces are not becoming smoother; more of "
                    "their existing peaks are being brought into contact."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h09",
        "band": "harder",
        "text": "A student says: 'A bigger block always has more friction "
                "than a smaller one, because it touches more of the "
                "surface.' Using the idea of microscopic peaks, explain "
                "the flaw.",
        "options": [
            {"text": "There is no flaw whatsoever here — bigger blocks of "
                     "the same material and shape genuinely always have "
                     "more total friction than smaller ones, without "
                     "exception.", "correct": False,
             "why": "Two blocks of the same weight but different sizes "
                    "give roughly the same friction; size on its own is "
                    "not the deciding factor."},
            {"text": "The flaw is that friction does not exist between "
                     "large surfaces at all.", "correct": False,
             "why": "Friction certainly exists between large surfaces; the "
                    "flaw is in assuming visible size alone increases it."},
            {"text": "Only the true contact points set the friction, and a "
                     "bigger block spreads the same load over more peaks "
                     "rather than adding extra grip.", "correct": True},
            {"text": "The flaw is supposedly that bigger blocks are "
                     "always proportionally heavier than smaller ones, "
                     "and that this extra weight is what cancels the "
                     "larger area out completely.", "correct": False,
             "why": "Two blocks of the SAME weight but different visible "
                    "sizes are being compared; weight is not what is "
                    "varying here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h10",
        "band": "harder",
        "text": "Explain, using the idea of microscopic peaks, why a block "
                "cut in half (same material, same total weight split "
                "between the two halves) does not give twice the total "
                "friction of the whole block.",
        "options": [
            {"text": "It does give exactly twice the total friction, "
                     "since there are now two separate blocks instead of "
                     "the original single one.", "correct": False,
             "why": "Splitting the load between two smaller blocks does "
                    "not increase the total force pressing peaks "
                    "together; the total load is unchanged."},
            {"text": "Cutting the block clean in half somehow removes its "
                     "friction entirely, leaving neither half with any "
                     "grip on the surface at all.", "correct": False,
             "why": "Both halves would still have real friction with the "
                    "surface; cutting does not remove it."},
            {"text": "The two halves become smoother when separated.",
             "correct": False,
             "why": "Cutting a block does not smooth its surface; the "
                    "peaks and valleys remain much as before."},
            {"text": "The true contact area, set by the load pressing the "
                     "peaks together, has not doubled just because the "
                     "block was cut.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h11",
        "band": "harder",
        "text": "A crate needs 90 N to start sliding and settles at 75 N "
                "once moving. If a student keeps the push at exactly 90 N "
                "once the crate is already sliding, what happens?",
        "options": [
            {"text": "The crate speeds up, since 90 N is now more than "
                     "the 75 N of friction resisting it.", "correct": True},
            {"text": "The crate slides along at a perfectly steady speed, "
                     "since a push of 90 N exactly matches what is now "
                     "needed.", "correct": False,
             "why": "Once sliding, only 75 N is needed to match the "
                    "friction; 90 N leaves 15 N over."},
            {"text": "The crate slows down and stops.", "correct": False,
             "why": "A push bigger than the resisting friction speeds an "
                    "object up; it does not slow it down."},
            {"text": "Nothing changes, because friction always rises to match whatever push is applied to it.", "correct": False,
             "why": "Friction only matches the push up to the point of "
                    "sliding; once sliding it settles at its own lower "
                    "value."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h12",
        "band": "harder",
        "text": "A box needs 50 N to start sliding and 40 N to keep "
                "sliding. A push of exactly 40 N is applied from the very "
                "start, before the box has moved at all. What happens?",
        "options": [
            {"text": "The box slides immediately from the very first "
                     "instant, since 40 N is already enough to keep it "
                     "moving steadily.", "correct": False,
             "why": "Before sliding starts, static friction can match a "
                    "push up to 50 N; a 40 N push is simply matched and "
                    "the box stays still."},
            {"text": "The box does not move, because static friction can "
                     "match a push all the way up to 50 N.", "correct": True},
            {"text": "The box slides briefly, then stops again.",
             "correct": False,
             "why": "Nothing here is enough to start the box moving in the "
                    "first place, so it never begins to slide."},
            {"text": "It cannot be worked out without knowing the mass of the box and the material it is made from.", "correct": False,
             "why": "The two given figures — 50 N to start, 40 N to keep "
                    "sliding — are enough on their own to answer this."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h13",
        "band": "harder",
        "text": "A sledge needs 60 N to break away and 45 N to keep "
                "sliding on packed snow. A rope pulls with a steadily "
                "increasing force, starting from 0 N. At what point does "
                "the sledge actually start to move, and what happens the "
                "instant after?",
        "options": [
            {"text": "It starts moving as soon as the pull passes 45 N, and then slides steadily at whatever speed that particular pull happens to give it.", "correct": False,
             "why": "Below 60 N the sledge has not broken away yet — "
                    "static friction can still match the pull, right up "
                    "to that point."},
            {"text": "It never starts moving at all until the pull "
                     "reaches some entirely separate fixed maximum that "
                     "has no relation whatsoever to either of these two "
                     "figures.", "correct": False,
             "why": "The 60 N breakaway figure is precisely the point at "
                    "which it starts moving — no other figure is relevant."},
            {"text": "It starts moving once the pull exceeds 60 N, and "
                     "then accelerates because 60 N is now bigger than the "
                     "45 N of sliding friction.", "correct": True},
            {"text": "It starts moving at 60 N and immediately settles to "
                     "a steady speed.", "correct": False,
             "why": "The pull (60 N) is bigger than the new, lower sliding "
                    "friction (45 N), so there is a resultant force and "
                    "the sledge speeds up rather than holding steady."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h14",
        "band": "harder",
        "text": "A crate breaks away at 100 N and slides steadily at 80 N. "
                "The pulling force is held constant at exactly 80 N "
                "throughout, from before it starts moving. Describe what "
                "happens.",
        "options": [
            {"text": "The crate slides along at a perfectly steady speed "
                     "throughout the whole time, since 80 N matches the "
                     "sliding friction figure exactly.", "correct": False,
             "why": "That sliding figure only applies once the crate is "
                    "ALREADY moving; it never gets that far here."},
            {"text": "The crate accelerates the whole time, since a resultant force is being applied to it from the very start.", "correct": False,
             "why": "The crate never starts moving in the first place; "
                    "nothing here overcomes the 100 N breakaway "
                    "threshold."},
            {"text": "The crate moves briefly and then stops again.",
             "correct": False,
             "why": "It never starts moving at all — the applied force "
                    "never exceeds the breakaway threshold."},
            {"text": "The crate never starts moving at all, because 80 N "
                     "never reaches the 100 N needed to break it away.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h15",
        "band": "harder",
        "text": "A student claims: 'Because sliding friction is lower than "
                "static friction, an object under a steady force will keep "
                "speeding up forever once it starts moving.' What is the "
                "flaw?",
        "options": [
            {"text": "Once moving, sliding friction still resists the "
                     "motion — the object only keeps speeding up if the "
                     "applied force stays bigger than that (now lower) "
                     "friction, not forever automatically.", "correct": True},
            {"text": "There is no flaw — this is exactly what happens to "
                     "every sliding object.", "correct": False,
             "why": "An object reaches a steady speed once the applied "
                    "force no longer exceeds the sliding friction; it does "
                    "not speed up forever."},
            {"text": "The flaw is supposedly that sliding friction must "
                     "actually be higher than static friction rather than "
                     "lower, which would mean the whole premise of the "
                     "question has been stated completely backwards from "
                     "the very start.", "correct": False,
             "why": "Sliding friction genuinely is lower than static "
                    "friction here; the flaw lies elsewhere in the "
                    "reasoning."},
            {"text": "The flaw is that friction has nothing to do with how "
                     "fast something moves.", "correct": False,
             "why": "Friction is central to this scenario — it is exactly "
                    "what limits how the speed changes."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h16",
        "band": "harder",
        "text": "Explain why a heavy metal safe is far harder to start "
                "sliding across a floor than to keep sliding once it is "
                "moving, using the ideas of both static and kinetic "
                "friction.",
        "options": [
            {"text": "Because the safe becomes magnetic to the floor while it is standing still, and that magnetism has to be broken before it will shift at all.", "correct": False,
             "why": "No magnetism is involved; this is a friction effect, "
                    "present in ordinary materials."},
            {"text": "Because static friction, which resists the very "
                     "first movement, is bigger than the sliding friction "
                     "that takes over once it is moving.", "correct": True},
            {"text": "Because the safe is heavier before it moves and "
                     "lighter afterwards.", "correct": False,
             "why": "Its weight never changes; only the friction resisting "
                    "it changes between the two states."},
            {"text": "Because the floor beneath it somehow becomes "
                     "freshly polished the very instant the safe first "
                     "starts to slide across it, leaving it permanently "
                     "smoother than it was before.", "correct": False,
             "why": "The floor's surface does not change during the "
                    "slide; it is the friction, not the floor, that "
                    "drops."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h17",
        "band": "harder",
        "text": "A crate has a breakaway force of 120 N and a sliding force of 96 N. A rope is pulled with a force that rises steadily from 0 N to 150 N over ten seconds. Describe, in words, what the crate does.",
        "options": [
            {"text": "It stays still the whole ten seconds, since the "
                     "rope never reaches a genuinely large force.",
             "correct": False,
             "why": "The pull does exceed 120 N well before the ten "
                    "seconds are up, at which point the crate does start "
                    "to move."},
            {"text": "It slides steadily from the very start, since some "
                     "pull is always present.", "correct": False,
             "why": "Below 120 N the crate has not broken away — static "
                    "friction matches the pull exactly, and nothing moves "
                    "yet."},
            {"text": "It stays still while the pull is below 120 N, then "
                     "breaks away and accelerates once the pull exceeds "
                     "that, because it is now above the 96 N sliding "
                     "friction.", "correct": True},
            {"text": "It breaks away at exactly 96 N, the sliding figure, "
                     "rather than at 120 N.", "correct": False,
             "why": "96 N is the friction once ALREADY sliding; the crate "
                    "does not break away until the pull passes the higher "
                    "120 N figure."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h18",
        "band": "harder",
        "text": "A box needs 70 N to break away and settles at 55 N once "
                "sliding. If someone keeps the pull at a constant 60 N "
                "throughout, from the very start, describe what happens.",
        "options": [
            {"text": "The box slides at a steady speed, matching the 60 N "
                     "pull exactly.", "correct": False,
             "why": "60 N is not enough to break the box away from rest in "
                    "the first place; static friction can match it up to "
                    "70 N."},
            {"text": "The box slides immediately and speeds up, since 60 N "
                     "is more than the sliding friction of 55 N.",
             "correct": False,
             "why": "The box never gets to the sliding stage — a 60 N pull "
                    "is matched entirely by static friction, which can go "
                    "as high as 70 N."},
            {"text": "It cannot be determined without knowing the box's "
                     "exact mass.", "correct": False,
             "why": "The two given figures — the 70 N breakaway and 55 N "
                    "sliding forces — are enough on their own to answer "
                    "this."},
            {"text": "The box never moves at all, because 60 N never "
                     "exceeds the 70 N needed to break it away.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h19",
        "band": "harder",
        "text": "A block needs 40 N to keep sliding at a given load. The "
                "load is doubled AND the surface is changed to one that "
                "grips half as strongly per newton of load, compared with "
                "the original surface. What happens to the sliding force "
                "needed?",
        "options": [
            {"text": "It stays roughly the same, because doubling the "
                     "load and halving the surface's grip cancel each "
                     "other out.", "correct": True},
            {"text": "It roughly doubles, to about 80 N.", "correct": False,
             "why": "That ignores the surface change entirely — the new "
                    "surface grips only half as strongly per newton of "
                    "load."},
            {"text": "It roughly halves, to about 20 N.", "correct": False,
             "why": "That ignores the doubled load, which on its own "
                    "would double the force needed."},
            {"text": "It becomes four times as big, at about 160 N, since doubling the load and changing the surface each multiply the force that is needed.",
             "correct": False,
             "why": "That combines the two effects as though they "
                    "multiplied together in the same direction, when one "
                    "increases the force needed and the other decreases "
                    "it by the same factor."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h20",
        "band": "harder",
        "text": "A wheelie bin needs 30 N to keep sliding on tarmac. It "
                "is then filled until its load is three times as much, "
                "and wheeled instead onto a path where the surface grips "
                "twice as strongly for every newton pressing down. "
                "Roughly how much force does it now take to keep it "
                "sliding?",
        "options": [
            {"text": "About 90 N.", "correct": False,
             "why": "That only accounts for the trebled load, ignoring "
                    "that the new surface also doubles the grip on top of "
                    "that."},
            {"text": "About 180 N.", "correct": True},
            {"text": "About 60 N.", "correct": False,
             "why": "That only accounts for the doubled grip, ignoring "
                    "that the load has also trebled."},
            {"text": "About 30 N, unchanged.", "correct": False,
             "why": "Both changes push the required force up; trebling "
                    "the load and doubling the grip do not cancel out "
                    "here — they combine."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h21",
        "band": "harder",
        "text": "A packing case needs 24 N to slide steadily on a "
                "workshop floor. Someone empties it until the load "
                "pressing down is half what it was, and slides it "
                "instead across a floor whose surface grips three times "
                "as strongly per newton of load. About how much force is "
                "needed now?",
        "options": [
            {"text": "About 12 N.", "correct": False,
             "why": "That only accounts for the halved load, ignoring "
                    "that the new surface also grips three times as "
                    "strongly."},
            {"text": "About 72 N.", "correct": False,
             "why": "That trebles the original figure without also "
                    "applying the halving of the load."},
            {"text": "About 36 N.", "correct": True},
            {"text": "About 24 N, unchanged.", "correct": False,
             "why": "The two changes do not cancel here; halving the load "
                    "and trebling the grip together give a net increase, "
                    "not no change."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h22",
        "band": "harder",
        "text": "A shipping crate needs 50 N to keep sliding on its "
                "usual pallet track. The crate is loaded until it presses "
                "down twice as hard, and moved onto a different track "
                "whose surface grips only a quarter as strongly for "
                "every newton of load. Roughly what force is needed to "
                "keep it sliding now?",
        "options": [
            {"text": "About 100 N.", "correct": False,
             "why": "That only accounts for the doubled load, ignoring "
                    "that the new surface grips far less strongly per "
                    "newton."},
            {"text": "About 12.5 N.", "correct": False,
             "why": "That only accounts for the quartered grip, ignoring "
                    "that the load has also doubled, which pushes the "
                    "other way."},
            {"text": "About 50 N, unchanged.", "correct": False,
             "why": "The two changes do not fully cancel — doubling the "
                    "load and quartering the grip combine to give a net "
                    "decrease."},
            {"text": "About 25 N.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h23",
        "band": "harder",
        "text": "A student argues: 'Friction always wastes energy, so engineers should try to remove it everywhere in a machine.' Evaluate this claim, using examples from a car.",
        "options": [
            {"text": "The claim is wrong — friction is essential in "
                     "places like brakes, tyres and clutches, and only "
                     "unwanted in others like bearings and chains.",
             "correct": True},
            {"text": "The claim is correct, since every use of friction in "
                     "a machine wastes some energy as heat.", "correct": False,
             "why": "Wasting energy as heat is only true of friction "
                    "acting where it is NOT wanted; in brakes or tyres it "
                    "provides essential grip and control."},
            {"text": "The claim is correct only for very fast machines.",
             "correct": False,
             "why": "Speed is not what decides whether friction is "
                    "wanted; the job the friction is doing is what "
                    "matters, at any speed."},
            {"text": "The claim is wrong, because friction never wastes "
                     "any energy at all.", "correct": False,
             "why": "Friction genuinely does waste energy as heat where it "
                    "is unwanted, such as in an unlubricated bearing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h24",
        "band": "harder",
        "text": "A student argues: 'A smoother surface always has less friction than a rougher one.' Two clean, flat sheets of glass pressed together are surprisingly hard to slide apart. Evaluate the claim.",
        "options": [
            {"text": "The claim is completely correct, and the two glass sheets stick only because a film of water has gathered between them.", "correct": False,
             "why": "Dry, clean glass sheets grip just as strongly, so water is not the explanation: two very smooth surfaces can have a great deal of friction."},
            {"text": "The claim is not reliably true — two very smooth, "
                     "clean surfaces like glass can grip strongly because "
                     "so many of their peaks come into full contact.",
             "correct": True},
            {"text": "The claim is correct, but only for metals rather "
                     "than glass.", "correct": False,
             "why": "The glass sheets are themselves the counterexample, and the same effect is found with polished metal, so the material is not what decides it."},
            {"text": "The claim is wrong because rougher surfaces always "
                     "have less friction than smooth ones.", "correct": False,
             "why": "That reverses the usual pattern without evidence; the point of the glass sheets is that smoothness alone does not decide it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h25",
        "band": "harder",
        "text": "A student argues: 'Since oil reduces friction, adding "
                "more and more oil to a bearing will keep reducing the "
                "friction indefinitely.' Assess this claim.",
        "options": [
            {"text": "The claim is correct, and friction eventually "
                     "reaches exactly zero with enough oil.", "correct": False,
             "why": "Real friction never reaches exactly zero; a thin, "
                    "well-placed film does most of the work, and excess "
                    "oil adds little further benefit."},
            {"text": "The claim is wrong, because oil actually increases "
                     "friction in a bearing.", "correct": False,
             "why": "Oil does reduce friction in a bearing; the flaw is in "
                    "assuming ever more of it keeps helping without "
                    "limit."},
            {"text": "The claim overstates it — once the surfaces are "
                     "adequately separated, more oil brings little further "
                     "reduction.", "correct": True},
            {"text": "The claim is wrong, because friction depends only on "
                     "the load, not on any lubricant.", "correct": False,
             "why": "A lubricant genuinely changes the friction between "
                    "two surfaces; the load is not the only factor."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h26",
        "band": "harder",
        "text": "A student argues: 'Rubbing your hands together always warms them by the same amount, however hard you press.' Assess this claim.",
        "options": [
            {"text": "The claim is correct, since friction always "
                     "converts the same fraction of movement into heat.",
             "correct": False,
             "why": "Pressing harder increases the friction and the "
                    "energy converted to heat, so the warming is not "
                    "fixed regardless of pressure."},
            {"text": "The claim is correct, but only on cold days.",
             "correct": False,
             "why": "Temperature outside is not what the claim is about; "
                    "the flaw concerns how pressing harder changes the "
                    "friction and the heating."},
            {"text": "The claim is wrong, because rubbing hands together "
                     "does not use friction at all.", "correct": False,
             "why": "Rubbing hands together is a direct example of "
                    "friction converting movement into heat."},
            {"text": "The claim is wrong — pressing harder increases the "
                     "friction, so more energy is converted to heat and "
                     "the warming is greater.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h27",
        "band": "harder",
        "text": "A sprinter's foot pushes backwards against the starting "
                "blocks. A student claims this has nothing to do with "
                "friction, since the sprinter is not sliding across the "
                "ground at all. Assess this claim.",
        "options": [
            {"text": "The claim is wrong — friction, matching the push up "
                     "to its limit, is exactly what stops the foot sliding "
                     "backwards, which is what lets the push actually "
                     "drive the sprinter forwards.", "correct": True},
            {"text": "The claim is correct, because friction matters once sliding has started, and a foot pressed into a starting block is held by the shape of the block rather than by anything between the two surfaces.", "correct": False,
             "why": "Friction can act — and matters just as much — before "
                    "any sliding happens, which is exactly the case here."},
            {"text": "The claim is correct, because the starting blocks "
                     "remove the need for any friction.", "correct": False,
             "why": "The blocks give the foot something firm to push "
                    "against, but friction between foot and block is "
                    "still what stops the foot slipping."},
            {"text": "The claim is wrong, but only because the sprinter is "
                     "moving very fast.", "correct": False,
             "why": "Speed is not the reason; the reason is that friction "
                    "resists the foot's push whether the sprinter ends up "
                    "fast or slow."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h28",
        "band": "harder",
        "text": "A rock climber pushes down and back on a foothold to move "
                "upward. A student says the climber moves because the "
                "FOOTHOLD pushes the climber, which has nothing to do with "
                "friction. What is missing from this?",
        "options": [
            {"text": "Nothing is missing — friction genuinely plays no "
                     "part in this.", "correct": False,
             "why": "Friction between the boot and the foothold is "
                    "exactly what stops the boot slipping as the climber "
                    "pushes, which is essential here."},
            {"text": "Friction between the boot and the foothold is what "
                     "stops the boot slipping, allowing the push to be "
                     "effective at all.", "correct": True},
            {"text": "The climber's weight is what pushes them upward, not "
                     "the foothold.", "correct": False,
             "why": "Weight pulls the climber DOWN; it is the push against "
                    "the foothold, made effective by friction, that helps "
                    "them move up."},
            {"text": "The claim is right, because friction only matters "
                     "for objects that are already sliding.", "correct": False,
             "why": "Friction matters here precisely because the boot is "
                    "NOT sliding — it is what stops it from doing so."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h29",
        "band": "harder",
        "text": "A car's driven wheel spins against wet, icy tarmac and "
                "simply spins in place without the car moving. Explain, in "
                "terms of friction, why the car fails to move.",
        "options": [
            {"text": "The wheel is producing too much friction against the ice, and that excess grip locks the tyre to the surface so the car cannot be driven forwards.", "correct": False,
             "why": "The problem here is TOO LITTLE friction, not too "
                    "much — that is exactly why the wheel spins "
                    "uselessly."},
            {"text": "The car's weight has decreased on ice, so it cannot "
                     "move.", "correct": False,
             "why": "The car's weight is unchanged; what has changed is "
                    "how much friction the tyre can get from the icy "
                    "surface."},
            {"text": "The tyre cannot get enough friction from the icy "
                     "surface to stop itself slipping, so the wheel spins "
                     "without gripping.", "correct": True},
            {"text": "The engine is not providing enough force to turn the "
                     "wheel.", "correct": False,
             "why": "The wheel IS turning — spinning freely — which shows "
                    "the engine is providing plenty of force; the missing "
                    "ingredient is grip."},
        ],
        "figure": None,
    },
    {
        "id": "p4-05-h30",
        "band": "harder",
        "text": "A cyclist stands on the pedals and pushes down hard to "
                "accelerate away from a junction. Explain the role "
                "friction plays between the tyre and the road in this "
                "moment.",
        "options": [
            {"text": "None, because the wheel simply rolls forward under its own weight once the pedal is pushed, and the road plays no part beyond holding the bicycle up.", "correct": False,
             "why": "Rolling forward from a standing start needs the tyre "
                    "to grip the road; without friction the wheel would "
                    "simply spin."},
            {"text": "Friction only matters once the bicycle is already "
                     "moving at speed.", "correct": False,
             "why": "Friction between tyre and road matters from the very "
                    "first push, which is when grip is needed most."},
            {"text": "The chain provides all the force needed; the road "
                     "surface is irrelevant.", "correct": False,
             "why": "However hard the chain drives the wheel, without "
                    "friction at the tyre the wheel would just spin in "
                    "place."},
            {"text": "Friction between the tyre and the road is what stops "
                     "the tyre slipping, converting the pedalling force "
                     "into forward motion.", "correct": True},
        ],
        "figure": None,
    },
]
