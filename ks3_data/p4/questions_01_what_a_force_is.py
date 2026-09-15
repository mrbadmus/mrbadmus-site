"""P4 lesson 01 — What a force is: twelve questions (MRB-223).

Written against Design's page. The wall and the skateboard, the five
interaction cases and the three questions are hers.

The discriminations, in the order the lesson builds them:

  · a force takes TWO objects, and naming one is half an answer;
  · a force is not stuff and does not run out (`FORCE-12`);
  · a surface pushing back is doing something, even though it is not
    alive (`FORCE-13`);
  · some forces act across a gap (`FORCE-14`) — the harder band sits
    here and on the pair-on-different-objects idea;
  · movement, speed and energy are not forces (`FORCE-15`).

⚠️ POSITION IS AUTHORED — index cycles 2, 3, 0, 1, giving three of each.

⚠️ Rung 1 (the header) and Rung 2 (the magnet and the paperclip) are NOT
restated; check 6 of `verify_questions.py` forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P4"
LESSON = "what-a-force-is"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-01-e01",
        "band": "easier",
        "text": "A force is…",
        "options": [
            {"text": "something an object stores inside it and spends as it "
                     "moves", "correct": False,
             "why": "A force is not stuff and cannot be stored. It exists "
                    "only while two objects are interacting."},
            {"text": "how fast an object is travelling", "correct": False,
             "why": "That is speed. A force is what one object does to "
                    "another, not how quickly it moves."},
            {"text": "a push or a pull on one object, caused by a second "
                     "object", "correct": True},
            {"text": "the movement an object makes", "correct": False,
             "why": "Movement is a result, not the force. The force has to "
                    "be named at both ends."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e02",
        "band": "easier",
        "text": "Forces are measured in…",
        "options": [
            {"text": "kilograms", "correct": False,
             "why": "Kilograms measure mass. A force is measured in newtons, "
                    "and the two are different quantities."},
            {"text": "metres per second", "correct": False,
             "why": "That is a speed. Nothing in it is a force."},
            {"text": "joules", "correct": False,
             "why": "Joules measure energy. A force can be there with no "
                    "energy going anywhere at all — a table holding a book."},
            {"text": "newtons", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e03",
        "band": "easier",
        "text": "Which of these is a complete description of a force?",
        "options": [
            {"text": "The rope pulls the sledge with 200 N.", "correct": True},
            {"text": "There is a force of 200 N on the sledge.",
             "correct": False,
             "why": "That names one object. The second one — whatever is "
                    "doing the pulling — is missing."},
            {"text": "The sledge is moving with 200 N.", "correct": False,
             "why": "Moving is not a force, and a moving object does not "
                    "carry newtons around inside it."},
            {"text": "There is 200 N of force.", "correct": False,
             "why": "Neither object is named, so nothing has been described "
                    "— only a number given."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e04",
        "band": "easier",
        "text": "About how big is the force of an apple resting on your "
                "hand?",
        "options": [
            {"text": "1 000 N", "correct": False,
             "why": "That is roughly the weight of a small motorbike. An "
                    "apple is about a thousand times less."},
            {"text": "1 N", "correct": True},
            {"text": "100 N", "correct": False,
             "why": "That is about the weight of a ten-year-old child, not "
                    "of an apple."},
            {"text": "0 N", "correct": False,
             "why": "You can feel it, so something is pressing down. A force "
                    "of 0 N would feel like nothing at all."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-01-s01",
        "band": "standard",
        "text": "A swimmer pushes water backwards with their hand and moves "
                "forwards. What pushes the swimmer forwards?",
        "options": [
            {"text": "Their own muscles", "correct": False,
             "why": "Muscles are part of the swimmer, and a force needs a "
                    "SECOND object. The muscles move the arm; the water "
                    "moves the swimmer."},
            {"text": "The lane rope", "correct": False,
             "why": "It is not touched. The forward push comes from the "
                    "thing the hand is pressing on."},
            {"text": "Their own speed", "correct": False,
             "why": "Speed is not an object, so nothing can be on the other "
                    "end of it."},
            {"text": "The water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s02",
        "band": "standard",
        "text": "A book lies still on a table. Which statement is right?",
        "options": [
            {"text": "There are no forces on the book, because nothing is "
                     "happening.", "correct": False,
             "why": "Take the table away and the book falls, which is not "
                    "what happens to an object with no forces on it."},
            {"text": "The table pushes up on the book with the same force "
                     "the book presses down with.", "correct": True},
            {"text": "The table cannot push, because it is not alive.",
             "correct": False,
             "why": "A force needs no effort and no intention. Every surface "
                    "presses back on whatever presses into it."},
            {"text": "Only the book's weight acts, and the table simply gets "
                     "in the way.", "correct": False,
             "why": "Getting in the way IS pushing back. The surface is "
                    "squashed very slightly and pushes."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s03",
        "band": "standard",
        "text": "A tow bar pulls a caravan forwards with about 2 000 N. What "
                "does the caravan do to the tow bar?",
        "options": [
            {"text": "Nothing — the tow bar is the one doing the pulling.",
             "correct": False,
             "why": "Forces come in pairs. If the bar pulls the caravan, the "
                    "caravan pulls the bar."},
            {"text": "It pushes the tow bar forwards with about 2 000 N.",
             "correct": False,
             "why": "The size is right and the direction is wrong. The pair "
                    "acts in OPPOSITE directions."},
            {"text": "It pulls back along the bar with about 2 000 N.",
             "correct": True},
            {"text": "It pulls back, but with much less force, because it is "
                     "being dragged.", "correct": False,
             "why": "The two forces in a pair are the same size, whichever "
                    "object is winning."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s04",
        "band": "standard",
        "text": "A footballer kicks a ball. The boot and the ball are in "
                "contact for about a hundredth of a second. What is the "
                "force on the ball once the boot has left it?",
        "options": [
            {"text": "The boot's push, still acting until the ball slows "
                     "down.", "correct": False,
             "why": "The boot's push stops existing the moment they "
                    "separate. Nothing was handed over."},
            {"text": "The force the ball was given, gradually running out.",
             "correct": False,
             "why": "A force is not a supply. The ball keeps its speed, not "
                    "a force."},
            {"text": "No force from the boot at all — only the air and the "
                     "Earth act on it.", "correct": True},
            {"text": "The force is in the ball's movement, so it acts on "
                     "nothing and needs no second object", "correct": False,
             "why": "Movement is not a force. Every force on the ball has a "
                    "second object at the other end of it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-01-h01",
        "band": "harder",
        "text": "The Earth pulls the Moon with about 200 billion billion N. "
                "How hard does the Moon pull the Earth?",
        "options": [
            {"text": "With the same force, about 200 billion billion N.",
             "correct": True},
            {"text": "Much less, because the Moon is much smaller.",
             "correct": False,
             "why": "Size does not split the pair. The two forces in an "
                    "interaction are always the same size."},
            {"text": "Not at all — only the bigger object pulls.",
             "correct": False,
             "why": "Then the force would have only one object, which is not "
                    "possible. Tides are the Moon's pull, arriving."},
            {"text": "It depends on which one is moving.", "correct": False,
             "why": "The pair is the same size whether either is moving or "
                    "not. Motion is not part of the description."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h02",
        "band": "harder",
        "text": "If the two forces in every pair are equal and opposite, why "
                "does anything ever move?",
        "options": [
            {"text": "Because one of the pair is always slightly bigger.",
             "correct": False,
             "why": "They are exactly equal. Nothing about the pair is "
                    "uneven."},
            {"text": "Because the two forces act on DIFFERENT objects, and "
                     "only forces on the same object can cancel.",
             "correct": True},
            {"text": "Because the pair only exists while the objects are "
                     "touching.", "correct": False,
             "why": "The pair exists across a gap too — the Earth and the "
                    "Moon — and things still move."},
            {"text": "Because one of the forces is used up in moving the "
                     "object, leaving the other to act alone", "correct": False,
             "why": "Nothing is used up. Both forces act for exactly as long "
                    "as the interaction lasts."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h03",
        "band": "harder",
        "text": "A magnet lifts a paperclip across a two-centimetre gap. The "
                "air is then pumped out of the gap. What happens to the "
                "pull?",
        "options": [
            {"text": "It stops, because there is nothing left to carry it.",
             "correct": False,
             "why": "The gap does not need filling. This is the whole point "
                    "of a non-contact force."},
            {"text": "It gets weaker, because the air was helping.",
             "correct": False,
             "why": "The air was doing nothing for the magnetism. Removing "
                    "it changes nothing about the pull."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "It is exactly the same. Magnetism crosses a "
                     "vacuum.", "correct": True},
            {"text": "It gets stronger, because nothing is in the way any "
                     "more.", "correct": False,
             "why": "The air was never in the way. The pull is unchanged in "
                    "both directions."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h04",
        "band": "harder",
        "text": "A rocket in deep space fires its engine and speeds up, with "
                "nothing around it. Which pair of objects is the force "
                "between?",
        "options": [
            {"text": "The rocket and the empty space it is pushing against.",
             "correct": False,
             "why": "Space is not an object and cannot be one end of a "
                    "force. Something with mass has to be thrown."},
            {"text": "The rocket and the distant planet it set out from.",
             "correct": False,
             "why": "That pull is real but it acts towards the planet, and "
                    "it is not what the engine is doing."},
            {"text": "The rocket and the fuel tank bolted inside it.",
             "correct": False,
             "why": "The tank is part of the rocket. A force needs a second "
                    "object, not another part of the first one."},
            {"text": "The rocket and the exhaust gas it throws backwards.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-01-e05",
        "band": "easier",
        "text": "Which of these is a CONTACT force?",
        "options": [            {"text": "A charged balloon lifting hair from a head",
             "correct": False,
             "why": "The electrostatic force works across a gap too, so it is "
                    "non-contact."},
            {"text": "Gravity pulling a dropped ball down", "correct": False,
             "why": "Gravity acts across a gap with nothing in between, so it "
                    "is a non-contact force."},
            {"text": "A magnet attracting a pin from 2 cm away",
             "correct": False,
             "why": "Magnetism reaches across the gap without touching, which "
                    "makes it non-contact."},
            {"text": "Friction between a shoe and the floor", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e06",
        "band": "easier",
        "text": "Which statement about the two forces in a pair is right?",
        "options": [            {"text": "They are the same size and both act on the same object",
             "correct": False,
             "why": "If both acted on one object nothing could ever move; the "
                    "two act on the two different objects."},
            {"text": "They are the same size and act in the same direction on "
                     "one object",
             "correct": False,
             "why": "Two forces in the same direction on one object would add "
                    "up, and a pair never does."},
            {"text": "The bigger object always pushes with the larger force",
             "correct": False,
             "why": "Size makes no difference: the Moon pulls the Earth as "
                    "hard as the Earth pulls the Moon."},
            {"text": "They are the same size, act in opposite directions, and "
                     "act on two different objects",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-01-s05",
        "band": "standard",
        "text": "A gymnast presses down on a beam with 500 N. What does the "
                "beam do?",
        "options": [            {"text": "It pushes down on the gymnast with 500 N",
             "correct": False,
             "why": "The pair acts in opposite directions, so the beam's "
                    "force on the gymnast is upwards."},
            {"text": "It pushes up on the gymnast with rather less than "
                     "500 N",
             "correct": False,
             "why": "The pair is always equal. Less would leave a resultant "
                    "and the gymnast would sink."},
            {"text": "Nothing — a beam is not able to push", "correct": False,
             "why": "It is squashed very slightly and pushes back, exactly as "
                    "a stiff spring does."},
            {"text": "It pushes up on the gymnast with 500 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s06",
        "band": "standard",
        "text": "A student says a rolling ball has force inside it that runs "
                "out. What is wrong with that?",
        "options": [            {"text": "Force is stored in the ball but it leaks out through "
                     "the floor",
             "correct": False,
             "why": "Nothing stores force at all, so there is nothing to "
                    "leak."},
            {"text": "The force is there, but it is far too small to measure "
                     "in newtons",
             "correct": False,
             "why": "Size is not the issue. There is no force being carried "
                    "along, at any size."},
            {"text": "Nothing is wrong — that is why a ball eventually stops "
                     "rolling",
             "correct": False,
             "why": "It stops because friction acts ON it, not because "
                    "something inside it has run out."},
            {"text": "A force only exists while two objects interact, so "
                     "nothing carries a supply of it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-01-h05",
        "band": "harder",
        "text": "A horse pulls a cart, and the cart pulls back on the horse "
                "just as hard. Why does the pair move at all?",
        "options": [            {"text": "Because the horse's pull is really slightly bigger than "
                     "the cart's",
             "correct": False,
             "why": "The two are exactly equal. The movement is explained "
                    "elsewhere."},
            {"text": "Because a pair of equal forces cancels and leaves the "
                     "horse free",
             "correct": False,
             "why": "They cannot cancel: cancelling needs two forces on the "
                    "SAME object, and these act on two."},
            {"text": "Because the cart's pull only starts once the cart is "
                     "moving",
             "correct": False,
             "why": "It is there from the first instant; both appear and "
                    "disappear together."},
            {"text": "Because the two forces act on different objects, and "
                     "the ground pushes the horse forwards",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h06",
        "band": "harder",
        "text": "A student insists a table is not doing anything to the book "
                "resting on it. What single test would settle it?",
        "options": [            {"text": "Weigh the book and check it against the table's mass",
             "correct": False,
             "why": "The table's mass has nothing to do with the force it "
                    "pushes back with."},
            {"text": "Take the table away and see whether the book falls",
             "correct": False,
             "why": "It shows something WAS holding it, but not that the "
                    "table itself pushes — the foam does."},
            {"text": "Slide the book along and see whether it slows down",
             "correct": False,
             "why": "That tests friction along the surface, not the upward "
                    "push holding the book up."},
            {"text": "Stand the book on a thin sheet of foam and watch it "
                     "squash",
             "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-01-e07",
        "band": "easier",
        "text": "A force is a push or a pull. How many objects does it take "
                "for one to exist?",
        "options": [
            {"text": "Two: one being pushed or pulled, and one doing it",
             "correct": True},
            {"text": "One, because a moving object carries its own force",
             "correct": False,
             "why": "Nothing carries a force around inside it. A force needs a "
                    "second object at the other end of it."},
            {"text": "One, as long as that object is touching something else",
             "correct": False,
             "why": "The something else IS the second object, so the count is "
                    "two rather than one."},
            {"text": "Three, once the movement is counted as well",
             "correct": False,
             "why": "Movement is not an object and cannot be one end of a "
                    "force. Two objects is the whole list."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e08",
        "band": "easier",
        "text": "Which force can act between two objects that are not "
                "touching?",
        "options": [
            {"text": "Friction between a shoe and a wet floor",
             "correct": False,
             "why": "Friction stops the instant the shoe leaves the floor, so "
                    "it needs contact."},
            {"text": "The pull of a magnet on a steel pin across a gap",
             "correct": True},
            {"text": "The push of a table top on a book resting on it",
             "correct": False,
             "why": "Lift the book off and the push is gone, so the table has "
                    "to be touching it."},
            {"text": "Air resistance on a cyclist going quickly downhill",
             "correct": False,
             "why": "The air has to be touching the cyclist to push on them, "
                    "so it is a contact force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e09",
        "band": "easier",
        "text": "A boot kicks a football. Which object is the kick acting on?",
        "options": [
            {"text": "The pitch it travels over", "correct": False,
             "why": "The pitch is not being kicked. The force acts on whatever "
                    "the boot is pressing into."},
            {"text": "The speed the kick produces", "correct": False,
             "why": "Speed is not an object, so no force can act on it."},
            {"text": "The ball", "correct": True},
            {"text": "The boot doing the kicking", "correct": False,
             "why": "The boot feels the other half of the pair. The kick "
                    "itself is the force on the ball."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e10",
        "band": "easier",
        "text": "A dog pulls hard on its lead. Which two objects is that pull "
                "between?",
        "options": [
            {"text": "The dog and the lead", "correct": True},
            {"text": "The lead and the pavement", "correct": False,
             "why": "The lead is not being dragged along the ground, and the "
                    "pavement is not holding it."},
            {"text": "The dog and its own collar", "correct": False,
             "why": "Both of those are parts of the same dog, and a force "
                    "needs a genuinely second object."},
            {"text": "The dog and the ground", "correct": False,
             "why": "That is a different force. The pull in question is the "
                    "one along the lead."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e11",
        "band": "easier",
        "text": "A car travelling at 15 m/s has friction and air resistance "
                "acting on it. Which of these is NOT a force?",
        "options": [
            {"text": "Its speed of 15 m/s", "correct": True},
            {"text": "The friction on its tyres", "correct": False,
             "why": "Friction is one object pushing another, so it is a force "
                    "and is measured in newtons."},
            {"text": "The air resistance on it", "correct": False,
             "why": "The air pushes back on the car, which makes it a force "
                    "like any other."},
            {"text": "The push of the road on its tyres", "correct": False,
             "why": "The road presses back on whatever presses into it, and "
                    "that push is a force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e12",
        "band": "easier",
        "text": "Which of these is a pull rather than a push?",
        "options": [
            {"text": "A boot sending a football up the pitch",
             "correct": False,
             "why": "The boot presses into the ball, which makes it a push."},
            {"text": "A tow bar dragging a caravan forwards", "correct": True},
            {"text": "A table holding a book above the floor",
             "correct": False,
             "why": "The table presses upwards on the book, so it is a push."},
            {"text": "A hand pressing flat against a wall",
             "correct": False,
             "why": "Pressing into something is pushing it, not pulling it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e13",
        "band": "easier",
        "text": "About how big is the force between a boot and a ball while "
                "the ball is being kicked?",
        "options": [
            {"text": "About 3 N, like three apples", "correct": False,
             "why": "Three apples resting on a hand would not send a ball "
                    "anywhere."},
            {"text": "About 30 000 N, like a lorry", "correct": False,
             "why": "That is roughly the weight of a lorry, and no boot "
                    "supplies anything like it."},
            {"text": "About 300 N", "correct": True},
            {"text": "About 0.3 N, like a biscuit", "correct": False,
             "why": "That is less than the weight of an apple, so the ball "
                    "would barely stir."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e14",
        "band": "easier",
        "text": "About how hard does a tow bar pull a caravan along a "
                "motorway?",
        "options": [
            {"text": "About 20 N", "correct": False,
             "why": "That is about the pull of a full shopping bag, nowhere "
                    "near enough to tow a caravan."},
            {"text": "About 2 000 N", "correct": True},
            {"text": "About 2 N", "correct": False,
             "why": "That is roughly the pull of a small fridge magnet, which "
                    "would move nothing at all."},
            {"text": "About 200 000 N", "correct": False,
             "why": "That is a hundred times too big, and no tow bar is built "
                    "to take it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e15",
        "band": "easier",
        "text": "A contact force acts...",
        "options": [
            {"text": "at any distance, as long as one object is moving",
             "correct": False,
             "why": "Acting at a distance is what makes a force NON-contact. "
                    "Movement makes no difference."},
            {"text": "only while the two objects are touching",
             "correct": True},
            {"text": "only when one of the two objects is alive",
             "correct": False,
             "why": "A force needs no living thing. A table and a book manage "
                    "one between them."},
            {"text": "for as long as the object keeps moving afterwards",
             "correct": False,
             "why": "The push ends when the contact ends. What carries on is "
                    "the object's speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e16",
        "band": "easier",
        "text": "A balloon rubbed on a jumper lifts hair from a head without "
                "touching it. This force is...",
        "options": [
            {"text": "a contact force", "correct": False,
             "why": "Movement does not decide it. Whether the objects touch "
                    "is what decides it, and here they do not."},
            {"text": "a non-contact force", "correct": True},
            {"text": "static, not a force", "correct": False,
             "why": "Static electricity is a force between charged objects, "
                    "and it is measured in newtons."},
            {"text": "a force that needs air in the gap", "correct": False,
             "why": "Take the air away and the pull is unchanged, so the air "
                    "is not what makes it work."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e17",
        "band": "easier",
        "text": "A hand presses flat against a wall with 200 N. How hard does "
                "the wall press back on the hand?",
        "options": [
            {"text": "0 N, because a wall is not able to push",
             "correct": False,
             "why": "Every surface presses back on whatever presses into it, "
                    "alive or not."},
            {"text": "200 N, in the opposite direction", "correct": True},
            {"text": "400 N, which is twice as hard", "correct": False,
             "why": "Nothing doubles. The two forces in a pair are the same "
                    "size as each other."},
            {"text": "Less than 200 N, since the wall does not move",
             "correct": False,
             "why": "Moving has nothing to do with it. A wall bolted to a "
                    "building still pushes back with the full amount."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e18",
        "band": "easier",
        "text": "Forces come in pairs. The two forces in a pair point...",
        "options": [
            {"text": "in the same direction", "correct": False,
             "why": "Pointing the same way would make them add up, and a pair "
                    "never does that."},
            {"text": "in whichever direction the object happens to move",
             "correct": False,
             "why": "Movement does not set the directions. One points each "
                    "way, whatever is moving."},
            {"text": "in opposite directions", "correct": True},
            {"text": "in no fixed direction", "correct": False,
             "why": "Every force has a direction, and the two in a pair have "
                    "opposite ones."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e19",
        "band": "easier",
        "text": "A shelf snaps when too many books are stacked on it. What was "
                "the shelf doing before it snapped?",
        "options": [
            {"text": "Pushing up on the books", "correct": True},
            {"text": "Pulling the books downwards", "correct": False,
             "why": "The shelf pushes the books UP. What pulls them down is "
                    "the Earth."},
            {"text": "Storing up the load until it could hold no more",
             "correct": False,
             "why": "Nothing is stored. The shelf pushes up the whole time, "
                    "and then stops being able to."},
            {"text": "Doing nothing", "correct": False,
             "why": "A force needs no effort and no intention. Being not alive "
                    "stops nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e20",
        "band": "easier",
        "text": "The wind fills a sail and drives a boat along. Which two "
                "objects is that push between?",
        "options": [
            {"text": "The air and the sail", "correct": True},
            {"text": "The boat and the sea", "correct": False,
             "why": "The water does push on the hull, but that is a different "
                    "force from the one filling the sail."},
            {"text": "The boat and its own speed", "correct": False,
             "why": "Speed is not an object, so it cannot be one end of a "
                    "force."},
            {"text": "The wind and the mast it blows past",
             "correct": False,
             "why": "The mast holds the sail up; it is the sail that the air "
                    "presses on."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e21",
        "band": "easier",
        "text": "A student writes '5 N of push'. What would turn that into a "
                "full description of a force?",
        "options": [
            {"text": "Saying how long the push lasted for",
             "correct": False,
             "why": "Time is not part of describing a force. The missing part "
                    "is the two objects."},
            {"text": "Naming the two objects the push acts between",
             "correct": True},
            {"text": "Saying how fast the object then moved",
             "correct": False,
             "why": "A speed is a different quantity and describes no force at "
                    "all."},
            {"text": "Converting the 5 N into kilograms",
             "correct": False,
             "why": "Kilograms measure mass. A force is already in the right "
                    "unit when it is in newtons."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e22",
        "band": "easier",
        "text": "Gravity, magnetism and the force between charged objects are "
                "grouped together because...",
        "options": [
            {"text": "they are all pulls and never pushes",
             "correct": False,
             "why": "Two magnets the wrong way round push each other apart, so "
                    "pulls are not the rule."},
            {"text": "they are all far weaker than contact forces",
             "correct": False,
             "why": "The Earth's pull on the Moon is about 200 billion billion "
                    "N, which is not weak."},
            {"text": "none of them needs the two objects to touch",
             "correct": True},
            {"text": "they are all measured in something other than newtons",
             "correct": False,
             "why": "Every force is measured in newtons, whether it needs "
                    "contact or not."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e23",
        "band": "easier",
        "text": "A force is never something one object has on its own. Which "
                "of these IS a property of one object on its own?",
        "options": [
            {"text": "The friction between it and the floor",
             "correct": False,
             "why": "Friction needs the floor as well, so it belongs to the "
                    "pair and not to the object."},
            {"text": "Its speed, in metres per second", "correct": True},
            {"text": "The pull a nearby magnet has on it",
             "correct": False,
             "why": "That pull needs the magnet too. Take the magnet away and "
                    "there is nothing left."},
            {"text": "The push it gets from a hand", "correct": False,
             "why": "A push needs the hand at the other end, so it is not the "
                    "object's own property."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e24",
        "band": "easier",
        "text": "A skater on a skateboard pushes a wall and rolls backwards. "
                "Which object pushed the skater?",
        "options": [
            {"text": "The skater's own arms", "correct": False,
             "why": "Arms are part of the skater, and a force needs a second "
                    "object."},
            {"text": "The wall the skater pushed on", "correct": True},
            {"text": "The push the skater stored up first",
             "correct": False,
             "why": "A push cannot be stored. It exists only while the hands "
                    "are on the wall."},
            {"text": "The skateboard's wheels rolling on the floor",
             "correct": False,
             "why": "The wheels let the skater roll; they did not supply the "
                    "backwards push."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e25",
        "band": "easier",
        "text": "A crane lifts a girder on a steel cable. Is the cable's pull "
                "a contact force?",
        "options": [
            {"text": "Yes, because the cable and the girder are touching",
             "correct": True},
            {"text": "No, the crane driver is not touching it",
             "correct": False,
             "why": "The driver is not one of the two objects. The cable and "
                    "the girder are, and they touch."},
            {"text": "No, lifting is always done by gravity",
             "correct": False,
             "why": "Gravity pulls the girder DOWN. The upward pull comes from "
                    "the cable."},
            {"text": "Yes, but only while the girder is on its way up and not "
                     "once it is hanging still", "correct": False,
             "why": "The pull is there while the girder hangs still as well, "
                    "and it is still a contact force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e26",
        "band": "easier",
        "text": "About how big is the pull between a small magnet and a "
                "paperclip it lifts off a desk?",
        "options": [
            {"text": "About 200 N, like an adult's weight", "correct": False,
             "why": "That is about the weight of a grown adult, and no small "
                    "magnet pulls that hard."},
            {"text": "About 2 000 N, like a tow bar", "correct": False,
             "why": "That is the sort of pull a tow bar gives a caravan, not a "
                    "magnet and a paperclip."},
            {"text": "About 2 N", "correct": True},
            {"text": "About 0.002 N, like a pinch of salt", "correct": False,
             "why": "That would be far too weak to lift a paperclip off the "
                    "desk at all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e27",
        "band": "easier",
        "text": "The push a swimmer gives the water is written as 'about "
                "150 N' rather than '150 N'. Why?",
        "options": [
            {"text": "Because nobody has ever measured a swimmer's push",
             "correct": False,
             "why": "Swimmers have been measured many times. The hedge is "
                    "about the value varying, not about ignorance."},
            {"text": "Because a typical value depends on how hard the push is",
             "correct": True},
            {"text": "Because forces cannot be measured accurately in newtons",
             "correct": False,
             "why": "They can be measured very accurately. The newton is a "
                    "perfectly precise unit."},
            {"text": "Because a push in water is too quick to read on a meter",
             "correct": False,
             "why": "Instruments read far quicker events than a swimming "
                    "stroke. Speed of measurement is not the issue."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e28",
        "band": "easier",
        "text": "Which statement about forces and living things is right?",
        "options": [
            {"text": "A force needs a living thing to start it",
             "correct": False,
             "why": "The Earth pulls the Moon and neither is alive, so life is "
                    "not needed."},
            {"text": "Only living things can push", "correct": False,
             "why": "A table pushes up on a book all day and is not alive."},
            {"text": "A force between two objects stops if neither is alive",
             "correct": False,
             "why": "Nothing stops. A magnet and a paperclip keep pulling with "
                    "no living thing involved."},
            {"text": "A force needs no living thing at either end",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e29",
        "band": "easier",
        "text": "A parachute is pulled downwards as it falls. Which object "
                "is at the other end of that pull?",
        "options": [
            {"text": "The air", "correct": False,
             "why": "The air pushes UP on a falling parachute. It is not what "
                    "pulls it down."},
            {"text": "Its own weight", "correct": False,
             "why": "Weight is the force itself, not an object that could be "
                    "at one end of it."},
            {"text": "The Earth", "correct": True},
            {"text": "The ground below", "correct": False,
             "why": "The ground has not been reached yet, and the pull is "
                    "acting the whole way down."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e30",
        "band": "easier",
        "text": "Two objects are pulled together by gravity. Which of them "
                "feels a pull?",
        "options": [
            {"text": "Only the smaller one", "correct": False,
             "why": "Both feel the pull. Which one moves more is a separate "
                    "question altogether."},
            {"text": "Only the heavier one", "correct": False,
             "why": "Gravity is not owned by one object; it acts between the "
                    "two of them."},
            {"text": "Neither, until they are close enough to touch",
             "correct": False,
             "why": "Gravity is a non-contact force and acts across 384 000 km "
                    "between the Earth and the Moon."},
            {"text": "Both of them, with the same size force",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-01-s07",
        "band": "standard",
        "text": "The Moon is held in orbit by a pull from the Earth across "
                "384 000 km of empty space. What does this show about forces?",
        "options": [
            {"text": "That gravity is the one force able to act over a "
                     "distance", "correct": False,
             "why": "Magnetism and the force between charges also cross a gap, "
                    "so gravity is not alone."},
            {"text": "That a force can act with nothing in between the two "
                     "objects", "correct": True},
            {"text": "That the Earth must be touching the Moon through "
                     "something", "correct": False,
             "why": "There is nothing in the gap to touch through, and the "
                    "pull is there anyway."},
            {"text": "That a force grows stronger the further apart the "
                     "objects are", "correct": False,
             "why": "Nothing in this lesson says that, and a magnet's pull "
                    "plainly weakens as you pull it away."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s08",
        "band": "standard",
        "text": "A student says a wall cannot have pushed a skater because a "
                "wall is not alive. What is the best correction?",
        "options": [
            {"text": "A wall can push, but only because the building behind "
                     "it is held up by people", "correct": False,
             "why": "No person is involved. A wall in an empty building "
                    "pushes back exactly the same."},
            {"text": "The skater was pushed by their own arms, so the wall did "
                     "nothing at all", "correct": False,
             "why": "Arms are part of the skater, and a force needs a second "
                    "object to act from."},
            {"text": "A force needs no effort: every surface presses back on "
                     "whatever presses into it", "correct": True},
            {"text": "Walls push only when they are damaged slightly, and an "
                     "undamaged wall does nothing", "correct": False,
             "why": "Every wall is squashed a little, far too little to see, "
                    "and it pushes back whether it is damaged or not."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s09",
        "band": "standard",
        "text": "A fridge magnet is pulled onto a fridge door with 3 N. What "
                "does the magnet do to the door?",
        "options": [
            {"text": "It pulls the door towards the magnet with 3 N",
             "correct": True},
            {"text": "It pushes the door away from the magnet with 3 N",
             "correct": False,
             "why": "The pair points towards each other here, because the door "
                    "is being attracted rather than repelled."},
            {"text": "It does nothing, because the door is the heavier of the "
                     "two objects", "correct": False,
             "why": "Weight decides nothing. Both objects in a pair feel the "
                    "same size force."},
            {"text": "It pulls the door with rather less than 3 N, because it "
                     "is the smaller object", "correct": False,
             "why": "Size does not split the pair. Both forces are 3 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s10",
        "band": "standard",
        "text": "A climber hangs still from a rope. Name the force holding "
                "them up, and say whether it is a contact force.",
        "options": [
            {"text": "The rope pulls the climber up, and it is a contact "
                     "force", "correct": True},
            {"text": "The climber's own grip holds them up, and grip is not a "
                     "force", "correct": False,
             "why": "The grip is how the climber holds the rope; the upward "
                    "pull still comes from the rope, and it is a force."},
            {"text": "The rope pulls the climber up, and it is a non-contact "
                     "force", "correct": False,
             "why": "The rope and the climber are touching, so the pull is a "
                    "contact force."},
            {"text": "Gravity pushes the climber up, and it is a non-contact "
                     "force", "correct": False,
             "why": "Gravity pulls DOWN on the climber. The upward force comes "
                    "from the rope."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s11",
        "band": "standard",
        "text": "A charged balloon lifts strands of hair without touching "
                "them. Which statement is right?",
        "options": [
            {"text": "The force acts across the gap, so it is non-contact",
             "correct": True},
            {"text": "The hair must touch the balloon for it to work",
             "correct": False,
             "why": "The hair rises before it reaches the balloon, so the "
                    "force is already acting across the gap."},
            {"text": "The air between them carries the pull across",
             "correct": False,
             "why": "Take the air away and the pull is unchanged, so the air "
                    "is not carrying it."},
            {"text": "There is no force at all, because nothing is touching "
                     "the hair", "correct": False,
             "why": "The hair moves, so something is acting on it. Not "
                    "touching does not mean no force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s12",
        "band": "standard",
        "text": "A student describes a kick as 'a contact force of 300 N'. "
                "Which of the three questions is left unanswered?",
        "options": [
            {"text": "Which two objects the force is between",
             "correct": True},
            {"text": "Whether the force was measured", "correct": False,
             "why": "That is not one of the three questions. The three are the "
                    "objects, the size and whether they touch."},
            {"text": "Which direction the ball ends up going",
             "correct": False,
             "why": "Where the ball goes is not part of describing the force "
                    "between the boot and the ball."},
            {"text": "How big the force is, in newtons", "correct": False,
             "why": "That one is answered: the size given is 300 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s13",
        "band": "standard",
        "text": "Two ice skaters push each other apart. Which statement "
                "describes the forces correctly?",
        "options": [
            {"text": "The heavier skater pushes harder, which is why the "
                     "lighter one travels further", "correct": False,
             "why": "The two pushes are the same size. What differs is the "
                    "effect, not the force."},
            {"text": "Only the skater who started the push exerts a force on "
                     "the other one", "correct": False,
             "why": "A push cannot exist at one end only. Both skaters push "
                    "and both are pushed."},
            {"text": "Each skater pushes the other with the same size force, "
                     "in opposite directions", "correct": True},
            {"text": "Both pushes act on the lighter skater, which is what "
                     "sends it away faster", "correct": False,
             "why": "One force acts on each skater. A pair never acts on one "
                    "object."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s14",
        "band": "standard",
        "text": "The Earth pulls a parachutist downwards with 700 N. What "
                "does the parachutist do to the Earth?",
        "options": [
            {"text": "Pulls the Earth upwards with 700 N", "correct": True},
            {"text": "Pulls the Earth upwards, but far more weakly",
             "correct": False,
             "why": "The pair is equal however unequal the two objects are."},
            {"text": "Nothing — the Earth is too big", "correct": False,
             "why": "Size does not stop a force. The Moon pulls the Earth "
                    "hard enough to raise the tides."},
            {"text": "Pushes the Earth downwards with 700 N",
             "correct": False,
             "why": "The pair is a pull at both ends, and the two point "
                    "opposite ways."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s15",
        "band": "standard",
        "text": "In a tug of war, which sentence describes one team's force "
                "on the rope completely?",
        "options": [
            {"text": "There is a pull of 400 N somewhere on the rope",
             "correct": False,
             "why": "Neither object is named and 'somewhere' says nothing "
                    "about where it acts."},
            {"text": "The rope is being pulled and is moving slowly left",
             "correct": False,
             "why": "That describes the movement and gives no size and no "
                    "second object."},
            {"text": "A force of 400 N exists in the tug of war rope",
             "correct": False,
             "why": "A force is not something the rope contains. It acts "
                    "between the rope and something else."},
            {"text": "The red team's hands pull the rope with 400 N",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s16",
        "band": "standard",
        "text": "Which force acting on a moving cyclist is a contact force?",
        "options": [
            {"text": "Gravity pulling the cyclist downwards",
             "correct": False,
             "why": "Gravity reaches across a gap with nothing in between, so "
                    "it is non-contact."},
            {"text": "Air resistance pushing back on the cyclist",
             "correct": True},
            {"text": "The magnetic pull between the frame and a signpost",
             "correct": False,
             "why": "Magnetism acts across a gap, which makes it a non-contact "
                    "force."},
            {"text": "The static charge built up on the cyclist's waterproof "
                     "jacket", "correct": False,
             "why": "The force between charged objects crosses a gap too, so "
                    "it is non-contact."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s17",
        "band": "standard",
        "text": "Why is speed not a force?",
        "options": [
            {"text": "Because speed is measured in newtons, not in metres per "
                     "second", "correct": False,
             "why": "Speed is in metres per second and forces are in newtons, "
                    "which is the wrong way round here."},
            {"text": "Because speed belongs to one object on its own, and a "
                     "force needs two", "correct": True},
            {"text": "Because speed exists only while something is pushing",
             "correct": False,
             "why": "A ball keeps its speed long after the push has stopped, "
                    "which is the whole difference."},
            {"text": "Because speed is a push, while every force is a pull "
                     "instead", "correct": False,
             "why": "Forces are pushes as well as pulls, and speed is neither "
                    "of them."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s18",
        "band": "standard",
        "text": "Why can a force not be measured in kilograms?",
        "options": [
            {"text": "Because kilograms suit objects that are not moving",
             "correct": False,
             "why": "A moving object has the same mass in kilograms as a still "
                    "one."},
            {"text": "Because kilograms measure how much space an object takes "
                     "up", "correct": False,
             "why": "Space taken up is volume. Kilograms measure mass."},
            {"text": "Because kilograms measure mass, a different quantity "
                     "from a push or a pull", "correct": True},
            {"text": "Because a force is measured in joules, and newton is just "
                     "a shorter way of writing a joule", "correct": False,
             "why": "Joules measure energy, and newton is not short for "
                    "anything. Forces are in newtons."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s19",
        "band": "standard",
        "text": "Why does naming only one object leave a force half "
                "described?",
        "options": [
            {"text": "Because the second object is where the force is stored "
                     "until it is needed", "correct": False,
             "why": "Nothing stores a force. The second object is what causes "
                    "it, not a container for it."},
            {"text": "Because a force cannot be measured until both objects "
                     "have been weighed", "correct": False,
             "why": "A newtonmeter reads the force without weighing anything."},
            {"text": "Because the first object named is always the one that "
                     "feels nothing", "correct": False,
             "why": "Both objects feel the force, whichever order they are "
                    "named in."},
            {"text": "Because the force is an interaction, and the second "
                     "object is what causes it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s20",
        "band": "standard",
        "text": "A hammer drives a nail into a plank. Which two objects does "
                "the force that moves the nail act between?",
        "options": [
            {"text": "The hammer and the nail", "correct": True},
            {"text": "The nail and the plank it enters", "correct": False,
             "why": "The plank pushes BACK on the nail. It is not what drives "
                    "the nail in."},
            {"text": "The hammer and the swinging arm", "correct": False,
             "why": "That pair moves the hammer. The force on the nail comes "
                    "from the hammer head."},
            {"text": "The nail and the hammer's speed",
             "correct": False,
             "why": "Speed is not an object and cannot be one end of a "
                    "force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s21",
        "band": "standard",
        "text": "A student says 'the ball keeps the force the bat gave it'. "
                "Which correction is right?",
        "options": [
            {"text": "The ball keeps the force but shares it with the air it "
                     "moves through", "correct": False,
             "why": "There is no force to share. The air acts on the ball as a "
                    "second object of its own."},
            {"text": "The ball keeps its speed; the bat's push stopped when "
                     "they separated", "correct": True},
            {"text": "The ball keeps the force until it lands, and then hands "
                     "it over to the ground", "correct": False,
             "why": "Nothing is handed over at either end. A force is not an "
                    "object's property."},
            {"text": "The ball keeps the force only if the bat stays in "
                     "contact long enough", "correct": False,
             "why": "However long the contact lasts, the push ends when the "
                    "contact does."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s22",
        "band": "standard",
        "text": "A seat belt pulls a passenger back into the seat. Which "
                "statement about that force is complete?",
        "options": [
            {"text": "There is a backwards force of about 400 N in the car",
             "correct": False,
             "why": "Neither object is named, so nothing has been described "
                    "beyond a number."},
            {"text": "The passenger's own weight pulls them back with 400 N",
             "correct": False,
             "why": "Weight pulls downwards, not backwards, and the belt is "
                    "what holds the passenger."},
            {"text": "The seat belt pulls the passenger backwards with about "
                     "400 N", "correct": True},
            {"text": "About 400 N of force is produced by the sudden stop",
             "correct": False,
             "why": "A stop is an event, not an object. The belt is the second "
                    "object here."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s23",
        "band": "standard",
        "text": "Two magnets repel each other across a gap of one centimetre. "
                "Which statement is right?",
        "options": [
            {"text": "The stronger magnet pushes, and the weaker one is simply "
                     "moved", "correct": False,
             "why": "Both push, and the two pushes are the same size whatever "
                    "the magnets are like."},
            {"text": "The push happens only once the gap is closed to nothing",
             "correct": False,
             "why": "The push is plainly there across the gap, which is why "
                    "the magnets will not meet."},
            {"text": "Neither magnet pushes, because they are not in contact "
                     "with one another", "correct": False,
             "why": "Magnetism is a non-contact force and does not need the "
                    "two to touch."},
            {"text": "Each magnet pushes the other away with the same size "
                     "force", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s24",
        "band": "standard",
        "text": "A shopping trolley is pushed with 60 N. Which statement "
                "describes that force completely?",
        "options": [
            {"text": "A push of 60 N is happening in the supermarket aisle",
             "correct": False,
             "why": "No objects are named, so the force has not been described "
                    "at all."},
            {"text": "The trolley is moving forwards because of 60 N of speed",
             "correct": False,
             "why": "Speed is not measured in newtons and is not a force."},
            {"text": "The trolley carries 60 N of force with it as it rolls",
             "correct": False,
             "why": "Nothing carries a force. It exists only while the hands "
                    "are pushing."},
            {"text": "The shopper's hands push the trolley forwards with 60 N",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s25",
        "band": "standard",
        "text": "A kite is held on a string in a strong wind. Which two "
                "objects is the pull in the string between?",
        "options": [
            {"text": "The kite and the wind past it", "correct": False,
             "why": "The air pushes the kite, but the pull being asked about "
                    "is the one along the string."},
            {"text": "The string and the air around it", "correct": False,
             "why": "The air does act on the string a little, but that is not "
                    "the pull holding the kite."},
            {"text": "The string and the kite", "correct": True},
            {"text": "The kite and the height it has reached", "correct": False,
             "why": "A height is a distance, not an object, so it cannot be "
                    "one end of a force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s26",
        "band": "standard",
        "text": "Air resistance and friction are both contact forces. What do "
                "they have in common?",
        "options": [
            {"text": "Both act at any distance, in the way that gravity does",
             "correct": False,
             "why": "Acting at a distance is what makes a force non-contact, "
                    "and these two are not."},
            {"text": "Both act only while the object is touching something",
             "correct": True},
            {"text": "Both are pulls rather than pushes, in each case",
             "correct": False,
             "why": "Both push against the object's motion rather than pulling "
                    "it."},
            {"text": "Both are measured in kilograms rather than in newtons",
             "correct": False,
             "why": "Every force is measured in newtons, these two included."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s27",
        "band": "standard",
        "text": "A tennis ball bounces off a wall. Which statement about the "
                "forces is right?",
        "options": [
            {"text": "The wall gives the ball a new force, which the ball then "
                     "carries away with it", "correct": False,
             "why": "Nothing is given or carried. The wall's push exists only "
                    "during the bounce."},
            {"text": "Only the wall exerts a force, because only the ball "
                     "changes direction", "correct": False,
             "why": "The ball pushes the wall just as hard; the wall is simply "
                    "bolted to a building."},
            {"text": "The ball's force bounces back off the wall and returns "
                     "into the ball", "correct": False,
             "why": "A force is not a thing that can travel or bounce. It is "
                    "an interaction between two objects."},
            {"text": "The ball pushes the wall and the wall pushes the ball, "
                     "just as hard", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s28",
        "band": "standard",
        "text": "A book is placed on a thin foam pad and the pad visibly "
                "squashes. What does that show?",
        "options": [
            {"text": "The book presses down on the pad and the pad presses "
                     "back up on the book", "correct": True},
            {"text": "The book is heavier than the pad can hold, so it will "
                     "go through", "correct": False,
             "why": "A squash that stops is a pad that is holding. Going "
                    "through would mean it had run out."},
            {"text": "Foam is the one material that pushes back",
             "correct": False,
             "why": "Every surface does the same thing. Foam simply squashes "
                    "far enough to see."},
            {"text": "The pad is storing the book's load until it is lifted "
                     "off", "correct": False,
             "why": "Nothing is stored. The pad pushes up the whole time the "
                    "book is there."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s29",
        "band": "standard",
        "text": "Why is 'there is a force of 8 N on the box' not a full "
                "description of a force?",
        "options": [
            {"text": "It gives a size but leaves out how long the force lasts "
                     "for", "correct": False,
             "why": "How long it lasts is not part of describing a force. The "
                    "missing part is the second object."},
            {"text": "It uses newtons, and a force ought to be given in "
                     "kilograms instead", "correct": False,
             "why": "Newtons are exactly right. Kilograms measure mass."},
            {"text": "It names one object only, and a force needs both of them "
                     "named", "correct": True},
            {"text": "It does not say how fast the box was travelling at the "
                     "time", "correct": False,
             "why": "A speed describes the box, not the force acting on it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s30",
        "band": "standard",
        "text": "A compass needle swings round to point north even though "
                "nothing touches it. Which statement is right?",
        "options": [
            {"text": "The air in the room pushes it round",
             "correct": False,
             "why": "Put the compass in a sealed jar with the air pumped out "
                    "and it still points north."},
            {"text": "The needle has a force stored inside it",
             "correct": False,
             "why": "Nothing stores a force. A second object is acting on the "
                    "needle."},
            {"text": "Nothing acts on it; needles settle facing north on "
                     "their own", "correct": False,
             "why": "Something has to turn it, and a turn with no force is not "
                    "possible."},
            {"text": "A non-contact force is acting on the needle",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-01-h07",
        "band": "harder",
        "text": "A diver stands still on a springboard. Which pair of forces "
                "is a genuine interaction pair?",
        "options": [
            {"text": "The diver's push down on the board and the board's push "
                     "up on the diver", "correct": True},
            {"text": "The diver's weight and the board's push up on the diver",
             "correct": False,
             "why": "Both of those act on the diver, and a pair acts on two "
                    "different objects."},
            {"text": "The diver's weight and the diver's push down on the "
                     "board", "correct": False,
             "why": "These are two different forces with two different "
                    "partners; they are not a pair with each other."},
            {"text": "The board's push up on the diver and the board's own "
                     "weight", "correct": False,
             "why": "The board's weight is between the board and the Earth, so "
                    "it does not pair with the push on the diver."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h08",
        "band": "harder",
        "text": "The Moon pulls the Earth as hard as the Earth pulls the "
                "Moon. What everyday evidence shows that pull arriving?",
        "options": [
            {"text": "The phases of the Moon through the month",
             "correct": False,
             "why": "The phases are about which side is lit by the Sun and "
                    "have nothing to do with a pull."},
            {"text": "The rise and fall of the tides", "correct": True},
            {"text": "The Moon always showing us the same face",
             "correct": False,
             "why": "That is an effect of the Earth's pull on the Moon, which "
                    "is the other half of the pair."},
            {"text": "The Moon staying in orbit rather than flying off",
             "correct": False,
             "why": "That shows the Earth pulling the Moon, not the Moon "
                    "pulling the Earth."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h09",
        "band": "harder",
        "text": "One newton is the force that changes the speed of one "
                "kilogram by one metre per second, every second. What does "
                "that definition say about contact?",
        "options": [
            {"text": "It shows a force must involve contact, because a change "
                     "of speed needs a push", "correct": False,
             "why": "A pull across a gap changes speed perfectly well, as a "
                    "falling ball shows."},
            {"text": "It shows a force can only act on objects of exactly one "
                     "kilogram", "correct": False,
             "why": "The kilogram in the definition sets the size of the unit, "
                    "not a limit on what forces act on."},
            {"text": "Nothing in it mentions touching, so a force need not "
                     "involve contact", "correct": True},
            {"text": "It shows a force lasts for exactly one second and then "
                     "stops acting", "correct": False,
             "why": "The second in the definition describes the rate of "
                    "change, not how long a force lasts."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h10",
        "band": "harder",
        "text": "One student says 'the boot pushes the ball with 300 N'. "
                "Another adds 'and the ball pushes the boot with 300 N'. Who "
                "is right?",
        "options": [
            {"text": "Both, as the two halves of one interaction",
             "correct": True},
            {"text": "Only the second student", "correct": False,
             "why": "Which object moves is a separate question from which "
                    "objects exert forces."},
            {"text": "Neither, because the two forces must be different sizes "
                     "from one another", "correct": False,
             "why": "The two forces in a pair are always the same size, "
                    "however different the objects are."},
            {"text": "Only the first student", "correct": False,
             "why": "Doing the kicking does not make it the only one pushing. "
                    "Both halves exist together."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h11",
        "band": "harder",
        "text": "A magnet holds a steel pin in mid-air below it. A student "
                "says the air must be carrying the pull. How would you test "
                "that claim?",
        "options": [
            {"text": "Weigh the pin before and after", "correct": False,
             "why": "The pin's mass does not change, so the reading would say "
                    "nothing about the air."},
            {"text": "Warm the air in the gap and see whether the pin drops",
             "correct": False,
             "why": "That changes the air but not whether it is doing the "
                    "carrying, so it settles nothing."},
            {"text": "Move the magnet sideways and see whether the pin follows "
                     "it along", "correct": False,
             "why": "It would follow with or without air, so the result "
                    "separates nothing."},
            {"text": "Pump the air out and see whether the pull changes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h12",
        "band": "harder",
        "text": "A magnet in a clamp pulls a paperclip with 2 N. The magnet "
                "cannot move. Does the paperclip still pull on the magnet?",
        "options": [
            {"text": "No, the clamp takes the pull instead", "correct": False,
             "why": "The clamp holds the magnet still by adding a force of its "
                    "own; it does not remove the paperclip's pull."},
            {"text": "Only if the clamp is removed", "correct": False,
             "why": "Being free to move is not what makes a force exist. The "
                    "pull is there either way."},
            {"text": "Yes, with 2 N, whether or not the magnet can move",
             "correct": True},
            {"text": "No, because only an object that is free to move can pull "
                     "on anything", "correct": False,
             "why": "A wall moves nowhere and still pushes. Movement is not "
                    "what makes a force real."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h13",
        "band": "harder",
        "text": "A student claims a table pushes up only because a book is "
                "heavy enough to make it. Why is that wrong?",
        "options": [
            {"text": "Every surface presses back on whatever presses into it, "
                     "however light", "correct": True},
            {"text": "A table pushes back only while the book is put down",
             "correct": False,
             "why": "It pushes for as long as the book is there, not just "
                    "while it is being put down."},
            {"text": "A table pushes back with a fixed amount, set by how thick "
                     "the wood is", "correct": False,
             "why": "A fixed push would fling a light object off. It matches "
                    "whatever is resting on it."},
            {"text": "Only a table can push back; a cushion cannot",
             "correct": False,
             "why": "Every surface does it, which is why a cushion squashes "
                    "under something light."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h14",
        "band": "harder",
        "text": "A satellite circles the Earth 400 km up, where there is "
                "almost no air. Which force keeps it curving round?",
        "options": [
            {"text": "Air resistance from the thin air up there",
             "correct": False,
             "why": "There is almost no air at that height, and air resistance "
                    "would slow it rather than curve it."},
            {"text": "The Earth's gravity, acting across the gap",
             "correct": True},
            {"text": "The satellite's own speed", "correct": False,
             "why": "Speed is not a force, and on its own it would send the "
                    "satellite off in a straight line."},
            {"text": "The push of sunlight, which is what holds it on its "
                     "path", "correct": False,
             "why": "Sunlight does push a little, but nowhere near hard enough "
                    "to hold a satellite in orbit."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h15",
        "band": "harder",
        "text": "A student says 'the ball has 300 N in it as it flies through "
                "the air'. Write the correction that keeps everything true.",
        "options": [
            {"text": "The ball has 300 N until it lands, when the ground takes "
                     "it back again", "correct": False,
             "why": "There is nothing to take back. The push ended when the "
                    "boot left the ball."},
            {"text": "The ball has 300 N, spread thinly over the whole of its "
                     "flight through the air", "correct": False,
             "why": "A force is not a quantity that can be spread out or used "
                    "up over a journey."},
            {"text": "The ball has speed; the 300 N existed only while the "
                     "boot was touching it", "correct": True},
            {"text": "The ball has 300 N while it rises and none of it at all "
                     "once it starts to fall", "correct": False,
             "why": "It has none of it at any point in the flight, rising or "
                    "falling."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h16",
        "band": "harder",
        "text": "A magnet is brought near a steel nail and both are free to "
                "move. What happens, and why?",
        "options": [
            {"text": "They move together, each pulling the other with the same "
                     "force", "correct": True},
            {"text": "Only the magnet moves, because the nail is not a magnet "
                     "itself", "correct": False,
             "why": "The nail is pulled just as hard as the magnet is, so it "
                    "moves too."},
            {"text": "Neither moves until they touch, since non-contact forces "
                     "are far weaker", "correct": False,
             "why": "The pull acts across the gap, which is exactly why they "
                    "come together in the first place."},
            {"text": "Only the nail moves, because the magnet is the one doing "
                     "the pulling", "correct": False,
             "why": "Both are pulled with the same force, so both move towards "
                    "each other."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h17",
        "band": "harder",
        "text": "A crane holds a 5 000 N girder still on a cable. A student "
                "says the cable pulls and the girder does nothing. What is "
                "wrong with that?",
        "options": [
            {"text": "The girder pulls down on the cable with 5 000 N at the "
                     "same time", "correct": True},
            {"text": "The girder pushes up on the cable with 5 000 N at the "
                     "same time", "correct": False,
             "why": "The size is right and the direction is not: the girder "
                    "pulls the cable down, along its line."},
            {"text": "Nothing is wrong, because only the cable is exerting a "
                     "force here", "correct": False,
             "why": "A pull cannot exist at one end. If the cable pulls the "
                    "girder, the girder pulls the cable."},
            {"text": "The girder pulls down, but with less force than the "
                     "cable is pulling up", "correct": False,
             "why": "The two halves of a pair are equal, whichever object is "
                    "heavier."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h18",
        "band": "harder",
        "text": "Why is it wrong to say a force lives in an object's movement "
                "rather than in either object?",
        "options": [
            {"text": "Movement is not an object, so it can never be one end of "
                     "a force", "correct": True},
            {"text": "Movement is a force, but it is measured in metres per "
                     "second", "correct": False,
             "why": "Movement is not a force, and forces are measured in "
                    "newtons."},
            {"text": "Movement can be one end of a force, but only for an "
                     "object that is moving", "correct": False,
             "why": "Movement can never be one end of a force, moving object "
                    "or not."},
            {"text": "Movement is an object, but it is far too small to be "
                     "measured", "correct": False,
             "why": "Movement is not an object at all, and size has nothing "
                    "to do with it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h19",
        "band": "harder",
        "text": "An astronaut on a spacewalk throws a spanner away from the "
                "spacecraft. What happens to the astronaut, and why?",
        "options": [
            {"text": "Nothing happens, because there is nothing in space to "
                     "push against", "correct": False,
             "why": "The spanner is the second object, and space being empty "
                    "makes no difference."},
            {"text": "They drift the other way, because the spanner pushes "
                     "back just as hard", "correct": True},
            {"text": "They drift the same way as the spanner, since the throw "
                     "pushed them both along", "correct": False,
             "why": "The two halves of a pair point in opposite directions, so "
                    "the astronaut goes the other way."},
            {"text": "They stay exactly still, because the spanner is much "
                     "lighter than they are", "correct": False,
             "why": "The forces are equal, so the astronaut moves too, whatever "
                    "the spanner weighs."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h20",
        "band": "harder",
        "text": "A student measures a magnet's pull on a paperclip as 2 N and "
                "the paperclip's pull on the magnet as 2 N, and says one "
                "reading must be a mistake. Why is the student wrong?",
        "options": [
            {"text": "Both readings are wrong, because the pull has to be "
                     "shared between the two", "correct": False,
             "why": "Nothing is shared. Each object feels the full 2 N."},
            {"text": "One is right and the other is measuring the weight of "
                     "the paperclip", "correct": False,
             "why": "The paperclip's weight is a pull from the Earth and is a "
                    "different force altogether."},
            {"text": "The paperclip's pull should be smaller, as it is the "
                     "lighter of the two", "correct": False,
             "why": "Weight does not split a pair. Both forces are the same "
                    "size."},
            {"text": "Both readings are right: a pair is always the same size "
                     "at both ends", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h21",
        "band": "harder",
        "text": "A helicopter hovers by driving air downwards. Which object "
                "pushes the helicopter upwards?",
        "options": [
            {"text": "The air, which is pushed down and pushes back up",
             "correct": True},
            {"text": "The helicopter's rotors, which lift the body of it",
             "correct": False,
             "why": "The rotors are part of the helicopter, and a force needs "
                    "a second object."},
            {"text": "The ground below, which the downwash eventually reaches",
             "correct": False,
             "why": "A helicopter hovers just as well far above the ground, "
                    "where no downwash arrives."},
            {"text": "The engine, which supplies the lift straight to the "
                     "body", "correct": False,
             "why": "The engine is part of the helicopter too, and it turns "
                    "the rotors rather than lifting anything."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h22",
        "band": "harder",
        "text": "A student argues that gravity cannot be a force because a "
                "force needs two objects and nothing is touching. Where is "
                "the flaw?",
        "options": [
            {"text": "Gravity works through the air in between",
             "correct": False,
             "why": "It works with no air at all, which is how the Moon is "
                    "held in orbit."},
            {"text": "Gravity is a property of one object",
             "correct": False,
             "why": "It acts between two objects, which is exactly what makes "
                    "it a force."},
            {"text": "A force needs two objects, not two touching objects",
             "correct": True},
            {"text": "The two objects for gravity are the Earth and the air "
                     "above it", "correct": False,
             "why": "The two objects are the Earth and whatever is being "
                    "pulled, air or no air."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h23",
        "band": "harder",
        "text": "Why would it be wrong to say 'the kick gave the ball 300 N "
                "to use up'?",
        "options": [
            {"text": "The kick gave it 300 N, but the ball uses it up more "
                     "slowly than that", "correct": False,
             "why": "Nothing was given, so there is nothing to use up at any "
                    "rate."},
            {"text": "The kick gave it 300 N, and the air gradually takes that "
                     "force back", "correct": False,
             "why": "The air acts on the ball as a second object; it is not "
                    "reclaiming anything."},
            {"text": "The kick gave it 300 N, which stays stored until the "
                     "ball hits the ground", "correct": False,
             "why": "A force cannot be stored in an object at all, for any "
                    "length of time."},
            {"text": "A force is not a supply: it exists only during the "
                     "interaction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h24",
        "band": "harder",
        "text": "A lorry and a car collide head on. Which statement about the "
                "forces during the collision is right?",
        "options": [
            {"text": "The lorry pushes harder, because it is much the heavier "
                     "of the two", "correct": False,
             "why": "The two pushes are equal. What differs is the effect on "
                    "each vehicle, not the force."},
            {"text": "The car pushes harder, because it is the one that ends "
                     "up wrecked", "correct": False,
             "why": "Damage measures the effect, not the size of the force. "
                    "Both feel the same."},
            {"text": "Each always pushes the other with the same size force, in "
                     "opposite directions", "correct": True},
            {"text": "Only the lorry exerts a force, because it is the one "
                     "with more mass", "correct": False,
             "why": "A push cannot exist at one end only, whichever vehicle "
                    "has more mass."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h25",
        "band": "harder",
        "text": "A student writes 'gravity acts on the apple'. What has to be "
                "added before the force is fully described?",
        "options": [
            {"text": "The speed the apple reaches, and how long it takes to "
                     "fall", "correct": False,
             "why": "Both of those describe the apple's motion rather than the "
                    "force acting on it."},
            {"text": "The mass of the apple in kilograms, and nothing else",
             "correct": False,
             "why": "Mass is a property of the apple. The second object and "
                    "the size in newtons are what is missing."},
            {"text": "Whether the apple was moving before the pull started to "
                     "act on it", "correct": False,
             "why": "The pull is there whether the apple moves or not, so this "
                    "adds nothing."},
            {"text": "The second object, the Earth, and the size of the pull "
                     "in newtons", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h26",
        "band": "harder",
        "text": "The pull between the Earth and the Moon is about 200 billion "
                "billion N; between a magnet and a paperclip it is about 2 N. "
                "What do the two have in common?",
        "options": [
            {"text": "Both are far too weak to move the larger of the two "
                     "objects", "correct": False,
             "why": "Both do move both objects: the Moon's pull raises the "
                    "tides on the Earth."},
            {"text": "Both act only because something fills the space in "
                     "between them", "correct": False,
             "why": "Both work across a vacuum, so nothing has to fill the "
                    "gap."},
            {"text": "Both are pushes, since a non-contact force cannot be a "
                     "pull", "correct": False,
             "why": "Both are pulls, and non-contact forces can be either."},
            {"text": "Both act across a gap, and both are the same size at "
                     "each end", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h27",
        "band": "harder",
        "text": "A cyclist pushes the pedals and the bicycle moves forwards. "
                "A student says no second object is involved. What is wrong "
                "with that?",
        "options": [
            {"text": "The pedals are the second object, and they push the "
                     "cyclist along the road", "correct": False,
             "why": "The pedals are part of the bicycle the cyclist is sitting "
                    "on, so they cannot drive the pair forwards."},
            {"text": "The cyclist's legs are the second object, so the claim "
                     "is right after all", "correct": False,
             "why": "Legs are part of the cyclist, and a force needs a "
                    "genuinely separate object."},
            {"text": "The air is the second object, and it pushes the bicycle "
                     "forwards from behind", "correct": False,
             "why": "The air pushes BACK on a moving cyclist rather than "
                    "driving them along."},
            {"text": "The road pushes the tyres forwards; without it the "
                     "wheels would only spin", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h28",
        "band": "harder",
        "text": "Why does a force stop existing the instant two objects "
                "separate, while the object's speed does not?",
        "options": [
            {"text": "The force leaks away into the air as soon as the contact "
                     "is broken", "correct": False,
             "why": "There is nothing to leak. The force was an interaction, "
                    "not a substance."},
            {"text": "The force turns into speed, which is why the object "
                     "keeps on travelling", "correct": False,
             "why": "A force does not turn into anything. The object already "
                    "had its speed."},
            {"text": "Speed belongs to the object; the force belonged to the "
                     "interaction", "correct": True},
            {"text": "The force is still there but is much too small to be "
                     "measured now", "correct": False,
             "why": "It is not small; it is gone. Nothing is pushing once the "
                    "objects part."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h29",
        "band": "harder",
        "text": "A book is pushed along a desk and stops when the pushing "
                "stops. A student concludes the push was used up. Give the "
                "correction.",
        "options": [
            {"text": "The push was used up, and that is exactly why the book "
                     "comes to a stop", "correct": False,
             "why": "A push cannot be used up, because it was never stored in "
                    "the book to begin with."},
            {"text": "The push turned into friction", "correct": False,
             "why": "Friction is a separate force from a separate object, the "
                    "desk, and nothing turns into it."},
            {"text": "The push stays in the book until the desk takes it back",
             "correct": False,
             "why": "Nothing stays in the book. The hand's push ended when the "
                    "hand did."},
            {"text": "Friction from the desk acts on the book and slows it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h30",
        "band": "harder",
        "text": "An anchor chain holds a boat against a current. Which "
                "statement names both forces in the interaction between the "
                "chain and the boat?",
        "options": [
            {"text": "The chain pulls the boat back and the current pushes the "
                     "boat forward", "correct": False,
             "why": "Those are two forces on the boat from two different "
                    "objects, not a pair between chain and boat."},
            {"text": "The chain pulls the boat back and the boat pulls the "
                     "chain forward", "correct": True},
            {"text": "The chain pulls the boat back and the water pulls the "
                     "chain forward", "correct": False,
             "why": "The water is a third object, so this is not the pair "
                    "between the chain and the boat."},
            {"text": "The chain holds the boat still and the boat exerts "
                     "nothing on the chain", "correct": False,
             "why": "A pull cannot act at one end only: the boat pulls the "
                    "chain just as hard."},
        ],
        "figure": None,
    },
]
