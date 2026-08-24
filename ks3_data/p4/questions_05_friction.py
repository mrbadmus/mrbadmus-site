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
             "why": "The opposite. Friction never pushes something along."},
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
            {"text": "In a drawer that sticks", "correct": False,
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
            {"text": "Because your push gets stronger once it is moving.",
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
            {"text": "Because a bigger block has more air underneath it.",
             "correct": False,
             "why": "Air is not what is doing the gripping. The peaks are."},
            {"text": "Because a bigger block is always heavier.",
             "correct": False,
             "why": "Not necessarily — and even at the same weight, "
                    "spreading the block over a wider area does not change "
                    "the friction."},
            {"text": "Because only the highest peaks are actually touching, "
                     "and pressing harder flattens them so more come into "
                     "contact.", "correct": True},
            {"text": "Because a bigger block has more surface to heat up.",
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
            {"text": "The water pushes the stone forwards.", "correct": False,
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
                     "different things.", "correct": False,
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
                     "dangerous.", "correct": False,
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
]
