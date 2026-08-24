"""P4 lesson 04 — What forces do to motion: twelve questions (MRB-223).

Written against Design's page. The curling stone, the trolley and gates
and the four cards are hers.

The discriminations, in the order the lesson builds them:

  · moving needs NO force; changing motion does (`FORCE-24`);
  · a force against the motion is what slowing down IS;
  · a force ACROSS the motion bends the path and keeps the rest
    (`FORCE-25`) — the harder band sits here and on the orbit;
  · the force does not switch off when the object stops (`FORCE-26`);
  · a force is not a supply that drains (`FORCE-27`).

⚠️ POSITION IS AUTHORED — index cycles 0, 1, 2, 3, giving three of each.

⚠️ Rung 1 (the freewheeling cyclist) and Rung 2 (the ball at the top of a
throw) are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "what-forces-do-to-motion"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-04-e01",
        "band": "easier",
        "text": "A resultant force can do all of these EXCEPT one. Which?",
        "options": [
            {"text": "Keep something moving at a steady speed with no change "
                     "at all", "correct": True},
            {"text": "Speed something up", "correct": False,
             "why": "That is one of the three. A resultant in the direction "
                    "of travel makes it faster."},
            {"text": "Slow something down", "correct": False,
             "why": "That is one of the three. A resultant against the "
                    "motion makes it slower."},
            {"text": "Change the direction something is going",
             "correct": False,
             "why": "That is one of the three. A resultant across the motion "
                    "bends the path."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e02",
        "band": "easier",
        "text": "A trolley moving at 2 m/s has a resultant force of 0 N on "
                "it. One second later it is travelling at…",
        "options": [
            {"text": "0 m/s", "correct": False,
             "why": "Stopping is a change, and a change needs something left "
                    "over. Nothing is."},
            {"text": "2 m/s", "correct": True},
            {"text": "4 m/s", "correct": False,
             "why": "Speeding up is a change too. With 0 N left over nothing "
                    "about the motion changes."},
            {"text": "1 m/s", "correct": False,
             "why": "Slowing needs a resultant against the motion, and there "
                    "is none."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e03",
        "band": "easier",
        "text": "A curling stone slides across smooth ice with nothing "
                "touching it. Why does it keep going?",
        "options": [
            {"text": "The ice pushes it forwards.", "correct": False,
             "why": "The ice rubs backwards very slightly. Nothing pushes it "
                    "along."},
            {"text": "The push it was given is still inside it.",
             "correct": False,
             "why": "A force is not stuff and cannot be stored. The push "
                    "ended when the hand let go."},
            {"text": "Nothing is stopping it, and moving needs no force.",
             "correct": True},
            {"text": "It is heavy enough to keep itself moving.",
             "correct": False,
             "why": "Being heavy changes how much a force alters the motion, "
                    "not whether motion needs a force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-e04",
        "band": "easier",
        "text": "A car is speeding up. What must be true?",
        "options": [
            {"text": "The forces on it are balanced.", "correct": False,
             "why": "Balanced forces mean no change. Speeding up is a "
                    "change."},
            {"text": "Only the engine is acting on it.", "correct": False,
             "why": "Air resistance and friction are acting too. What "
                    "matters is what is LEFT OVER."},
            {"text": "There are no backwards forces at all.",
             "correct": False,
             "why": "There always are. The forward force is simply bigger "
                    "than they are."},
            {"text": "There is a resultant force forwards.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-04-s01",
        "band": "standard",
        "text": "A trolley travelling right has a resultant force pushing "
                "left for long enough. What happens?",
        "options": [
            {"text": "It slows, stops, and then starts moving left.",
             "correct": True},
            {"text": "It slows, stops, and stays stopped.", "correct": False,
             "why": "Nothing switches off when it reaches zero. The force is "
                    "still acting, so the motion keeps changing."},
            {"text": "It carries on right but more slowly for ever.",
             "correct": False,
             "why": "A steady backwards resultant keeps changing the motion "
                    "until it has reversed it."},
            {"text": "It immediately reverses direction.", "correct": False,
             "why": "A force changes motion gradually. It has to slow to a "
                    "stop before it can go the other way."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s02",
        "band": "standard",
        "text": "A trolley is travelling right when a resultant force acts "
                "SIDEWAYS on it. What happens to the motion it already had?",
        "options": [
            {"text": "It is cancelled — the trolley now goes sideways only.",
             "correct": False,
             "why": "Nothing cancels it. A resultant force adds a change; it "
                    "does not replace the motion."},
            {"text": "It is kept, and the path bends: the trolley goes right "
                     "AND sideways.", "correct": True},
            {"text": "It stops until the sideways force is removed.",
             "correct": False,
             "why": "The rightward motion continues throughout. The force is "
                    "not acting against it."},
            {"text": "It doubles, because two motions are now happening.",
             "correct": False,
             "why": "The rightward speed is unchanged. What is added is a "
                    "sideways change."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s03",
        "band": "standard",
        "text": "The same resultant force acts on the same trolley for three "
                "seconds instead of one. Compared with one second, the "
                "change in its motion is…",
        "options": [
            {"text": "the same, because the force is the same",
             "correct": False,
             "why": "How long a force acts matters. Three times as long "
                    "makes three times the change."},
            {"text": "a third as much, because it is spread over more time",
             "correct": False,
             "why": "It is not spread. The force keeps acting, so the change "
                    "keeps accumulating."},
            {"text": "three times as much", "correct": True},
            {"text": "nine times as much", "correct": False,
             "why": "Nothing here is squared. Three times as long gives "
                    "three times the change in speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-s04",
        "band": "standard",
        "text": "A box is pushed across a floor at a steady speed. Someone "
                "says “the push is winning, so the box moves.” What is wrong "
                "with that?",
        "options": [
            {"text": "The push is not really acting.", "correct": False,
             "why": "It is, and it is doing real work. The problem is what "
                    "the sentence claims it is FOR."},
            {"text": "Friction cannot act on a moving object.",
             "correct": False,
             "why": "Friction acts on the box the whole time it slides. That "
                    "is what the push is matching."},
            {"text": "Nothing is wrong — a push is what makes things move.",
             "correct": False,
             "why": "Moving needs no force. Only a CHANGE in motion does."},
            {"text": "At a steady speed nothing is winning: the push matches "
                     "the friction, and the box would keep going anyway.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-04-h01",
        "band": "harder",
        "text": "A satellite circles the Earth at a constant speed with its "
                "engines off. Is its motion changing?",
        "options": [
            {"text": "Yes — its direction is changing all the time, and "
                     "that is a change.", "correct": True},
            {"text": "No, because its speed is constant.", "correct": False,
             "why": "Motion is speed AND direction. Going round a circle "
                    "changes direction continuously."},
            {"text": "No, because there is no force on it in space.",
             "correct": False,
             "why": "The Earth's pull is acting the whole time. It is what "
                    "keeps the satellite in orbit."},
            {"text": "Yes, because it is slowly speeding up.",
             "correct": False,
             "why": "The speed is constant, as the question says. It is the "
                    "direction that changes."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h02",
        "band": "harder",
        "text": "Galileo rolled balls down one slope and up another, making "
                "the surfaces smoother each time. What did he conclude that "
                "he could never directly observe?",
        "options": [
            {"text": "That every ball eventually stops.", "correct": False,
             "why": "That is what he COULD see, and it is what everyone "
                    "before him concluded from it."},
            {"text": "That with the friction removed entirely, a ball would "
                     "never stop.", "correct": True},
            {"text": "That heavier balls roll further.", "correct": False,
             "why": "Not the point of the experiment, and not what he "
                    "concluded."},
            {"text": "That slopes make balls speed up.", "correct": False,
             "why": "True and directly observable. The powerful move was "
                    "imagining the limit he could not reach."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h03",
        "band": "harder",
        "text": "The same 1 N resultant acts on an empty trolley and on the "
                "same trolley loaded with bricks. What differs?",
        "options": [
            {"text": "The loaded one changes its motion less for the same "
                     "force.", "correct": True},
            {"text": "The loaded one changes its motion more, because there "
                     "is more of it.", "correct": False,
             "why": "It is the other way round. More mass means the same "
                    "force produces a smaller change."},
            {"text": "Nothing — the same force always gives the same "
                     "change.", "correct": False,
             "why": "Push a shopping trolley empty and full and the "
                    "difference is obvious."},
            {"text": "The resultant force on the loaded one is bigger.",
             "correct": False,
             "why": "The question fixes the resultant at 1 N for both. What "
                    "differs is what that 1 N achieves."},
        ],
        "figure": None,
    },
    {
        "id": "p4-04-h04",
        "band": "harder",
        "text": "Voyager 1 switched its engines off in 1980 and is still "
                "travelling at about 17 km/s. Which statement explains this "
                "best?",
        "options": [
            {"text": "Its engines are still producing a small push.",
             "correct": False,
             "why": "They are off. Nothing is pushing it along."},
            {"text": "It has stored the force from the engines and is "
                     "spending it slowly.", "correct": False,
             "why": "A force cannot be stored. What it has is speed, and "
                    "speed needs nothing to maintain it."},
            {"text": "Gravity from the Sun is pushing it outwards.",
             "correct": False,
             "why": "The Sun's gravity PULLS it back, very slightly. It is "
                    "not what keeps it going."},
            {"text": "There is almost nothing out there to slow it down, and "
                     "moving needs no force.", "correct": True},
        ],
        "figure": None,
    },
]
