"""P10 lesson 05 — How a motor works: twelve questions (MRB-223).

Written against Design's page. The swapped leads, the four-control bench, the
four parts and the four rungs are hers.

The discriminations, in the order the lesson builds them:

  · a current-carrying wire in a field is PUSHED SIDEWAYS, at right angles to
    both — it is not attracted (`MAG-17`);
  · the direction depends on two things, so reversing one reverses it and
    reversing both does not (`MAG-19`, `MAG-20`);
  · two opposite pushes either side of an axle make a turning effect;
  · the split ring does not start it, it keeps it going (`MAG-18`) — the
    harder band sits on the consequences of that.

⚠️ NO FORCE IN NEWTONS OR NEWTON METRES APPEARS IN ANY QUESTION, and no
tesla. Ruled for the whole unit: the only numbers here are currents in amps
and relative figures on a declared scale.

⚠️ POSITION IS AUTHORED — 0,1,2,3 · 1,2,3,0 · 2,3,0,1, three of each.

⚠️ NO RUNG IS RESTATED. The ladder owns the turned-round magnets, the plain
rings, the explanation of why a coil turns rather than slides, and the
cordless drill; nothing here reuses any of the four, and nothing restates the
commit gate's both-reversed case either.
"""

UNIT = "P10"
LESSON = "how-a-motor-works"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p10-05-e01",
        "band": "easier",
        "text": "A straight wire carrying a current is held between the poles "
                "of a magnet. What happens to the wire?",
        "options": [
            {"text": "It is pushed sideways", "correct": True},
            {"text": "It is pulled towards the nearer pole", "correct": False,
             "why": "Copper is not a magnetic material, so neither pole "
                    "attracts it. The push is at right angles to the field."},
            {"text": "It heats up but does not move", "correct": False,
             "why": "It does warm slightly, as any wire carrying a current "
                    "does — and it also jumps, which is the new effect here."},
            {"text": "It is pushed along its own length, in the direction of "
                     "the current", "correct": False,
             "why": "The push is at right angles to the current as well as to "
                    "the field, so it is never along the wire."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e02",
        "band": "easier",
        "text": "Which two things decide which way a current-carrying wire is "
                "pushed?",
        "options": [
            {"text": "The size of the current and the length of the wire",
             "correct": False,
             "why": "Those change how BIG the push is. They do not change "
                    "which way it goes."},
            {"text": "The direction of the current and the direction of the "
                     "field", "correct": True},
            {"text": "The strength of the magnet and the thickness of the "
                     "wire", "correct": False,
             "why": "Both change the size again. Direction is set by two "
                    "directions."},
            {"text": "Which way up the magnet is standing and how warm the "
                     "wire is", "correct": False,
             "why": "Temperature has nothing to do with it, and what matters "
                    "about the magnet is which way its field runs, not which "
                    "way up it sits."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e03",
        "band": "easier",
        "text": "In a motor, how are the two sides of the coil pushed?",
        "options": [
            {"text": "Both upwards, so the whole coil lifts", "correct": False,
             "why": "If both went the same way the coil would move sideways "
                    "rather than turn."},
            {"text": "Both towards the axle, so the coil is squashed",
             "correct": False,
             "why": "Nothing squashes it. The two pushes are parallel to each "
                    "other and opposite in direction."},
            {"text": "In opposite directions, one up and one down",
             "correct": True},
            {"text": "First one and then the other, half a turn apart",
             "correct": False,
             "why": "Both are pushed at the same moment. What happens half a "
                    "turn later is that the sides have swapped places."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e04",
        "band": "easier",
        "text": "What are the brushes in a motor for?",
        "options": [
            {"text": "Keeping the coil clean so it does not stick",
             "correct": False,
             "why": "They are called brushes because of their shape, not "
                    "because they sweep anything."},
            {"text": "Slowing the coil down when the current is switched off",
             "correct": False,
             "why": "Nothing is braking. They are there to make an electrical "
                    "connection."},
            {"text": "Holding the magnets in place either side of the coil",
             "correct": False,
             "why": "The magnets are fixed to the case. The brushes touch the "
                    "spinning part."},
            {"text": "Letting current reach a part of the machine that is "
                     "spinning", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p10-05-s01",
        "band": "standard",
        "text": "The current through a working motor is doubled and nothing "
                "else is changed. What happens to the turning effect?",
        "options": [
            {"text": "It stays the same, because the magnets have not changed",
             "correct": False,
             "why": "The magnets are only half of it. The push also depends "
                    "on how much current is flowing."},
            {"text": "It roughly doubles", "correct": True},
            {"text": "It reverses, because doubling passes through the point "
                     "where it cancels", "correct": False,
             "why": "There is no such point. Direction is set by the two "
                    "directions and does not care about size."},
            {"text": "It falls, because a bigger current heats the coil and "
                     "weakens it", "correct": False,
             "why": "A hot coil is a real problem for a real motor, but it "
                    "does not turn a bigger push into a smaller one."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s02",
        "band": "standard",
        "text": "A motor is running. The current is switched off, and the "
                "coil is left hanging between the two magnets. What do the "
                "magnets do to it now?",
        "options": [
            {"text": "They pull it round to line up with the field",
             "correct": False,
             "why": "That is what would happen to an iron bar. A copper coil "
                    "with no current in it is not magnetic at all."},
            {"text": "They pull it towards whichever pole it is nearest",
             "correct": False,
             "why": "Copper is not attracted to a magnet, however close it "
                    "gets."},
            {"text": "Nothing at all — copper is not a magnetic material",
             "correct": True},
            {"text": "They push it away, because the coil is still charged",
             "correct": False,
             "why": "There is no charge left sitting on the coil, and being "
                    "charged is not what made it move in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s03",
        "band": "standard",
        "text": "A motor's copper coil is replaced with an identical one made "
                "of aluminium wire. Does it still turn?",
        "options": [
            {"text": "No, because aluminium is not attracted to a magnet",
             "correct": False,
             "why": "Copper is not attracted either. Attraction was never "
                    "what made it turn."},
            {"text": "No, because aluminium cannot carry a current",
             "correct": False,
             "why": "Aluminium is a good conductor — overhead power lines are "
                    "made of it."},
            {"text": "Only if the magnets are made stronger, because aluminium "
                     "takes a smaller push than copper", "correct": False,
             "why": "Nothing needs making up for. The same current in the "
                    "same field gives the same push."},
            {"text": "Yes — the push acts on the current in the wire, "
                     "whatever metal the wire is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s04",
        "band": "standard",
        "text": "As a motor's coil turns, its turning effect is largest when "
                "the coil is…",
        "options": [
            {"text": "flat, with its two sides furthest from lining up with "
                     "the field", "correct": True},
            {"text": "upright, with its two sides one above the other",
             "correct": False,
             "why": "Upright is the worst position of all: there the two "
                    "pushes are pulling the coil apart rather than round."},
            {"text": "half way between the two, at forty-five degrees",
             "correct": False,
             "why": "Half way gives a middling turning effect. The largest is "
                    "at one end of the swing, not in the middle."},
            {"text": "in any position — the turning effect is the same all "
                     "the way round", "correct": False,
             "why": "It changes right through the turn, which is why a real "
                    "motor uses several coils rather than one."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p10-05-h01",
        "band": "harder",
        "text": "A single-coil motor is stopped by hand with its coil exactly "
                "upright, and let go with the current still switched on. It "
                "does not start. Why not?",
        "options": [
            {"text": "The split ring has been left half way between its two "
                     "contacts, so no current flows", "correct": False,
             "why": "Even with current flowing it would not start from here. "
                    "The problem is where the pushes are pointing."},
            {"text": "The coil is now lined up with the field, so the magnets "
                     "hold it there", "correct": False,
             "why": "The magnets do nothing to a copper coil. It is the "
                    "pushes on the current that matter."},
            {"text": "The two pushes are now pulling the coil apart rather "
                     "than turning it", "correct": True},
            {"text": "The current reverses at exactly that point, so the two "
                     "pushes cancel", "correct": False,
             "why": "The current does reverse near there, and both pushes "
                    "reverse together — which is what keeps a running motor "
                    "going rather than cancelling anything."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h02",
        "band": "harder",
        "text": "On a motor diagram the two force arrows are always drawn the "
                "same length as each other, whatever the current is set to. "
                "Why must that be right?",
        "options": [
            {"text": "The two sides are the same distance from the axle, so "
                     "the pushes must match", "correct": False,
             "why": "Distance from the axle decides how much TURNING each "
                    "push gives, not how big the push is."},
            {"text": "One arrow is the reaction to the other, so it copies "
                     "whatever the first one does", "correct": False,
             "why": "These two pushes both act on the coil, from the field. "
                    "They are not a pair acting on each other."},
            {"text": "Arrows on a diagram are drawn to a fixed length by "
                     "convention", "correct": False,
             "why": "They are drawn to scale here — they get longer as the "
                    "current goes up. What stays equal is the two of them."},
            {"text": "The same current runs through both sides, and both "
                     "sides are in the same field", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h03",
        "band": "harder",
        "text": "A motor's coil is rewound with twenty turns instead of one, "
                "with the same current and the same magnets. What happens to "
                "the turning effect?",
        "options": [
            {"text": "It becomes about twenty times larger, because each turn "
                     "carries the current through the field", "correct": True},
            {"text": "It stays the same, because the current has not changed",
             "correct": False,
             "why": "The same current now passes through the field twenty "
                    "times over instead of once, and each pass gets its own "
                    "push."},
            {"text": "It falls to a twentieth, because the current is shared "
                     "between the turns", "correct": False,
             "why": "Nothing is shared. The current runs through every turn "
                    "in succession."},
            {"text": "It reverses, because half of the twenty turns run the "
                     "other way", "correct": False,
             "why": "Every turn is wound the same way round, so all twenty "
                    "pushes act in the same direction."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h04",
        "band": "harder",
        "text": "In a loudspeaker a coil sits in a permanent magnet's field, "
                "and the current through it changes direction thousands of "
                "times a second. The cone moves in and out rather than round. "
                "Why?",
        "options": [
            {"text": "The current changes direction too fast for the coil to "
                     "get all the way round before it is reversed",
             "correct": False,
             "why": "Speed is not the reason. Even a slow, steady current "
                    "would not turn this coil — it is not mounted to turn."},
            {"text": "The coil is not on an axle, so a push moves it bodily, "
                     "and reversing the current reverses the push",
             "correct": True},
            {"text": "A loudspeaker has no magnets, so there is nothing to "
                     "turn against", "correct": False,
             "why": "It has a permanent magnet — a strong one, and that is "
                    "what the coil sits in."},
            {"text": "The cone stops the coil turning, so the push has to go "
                     "somewhere else", "correct": False,
             "why": "The cone is what the coil moves. Nothing is being held "
                    "back and redirected."},
        ],
        "figure": None,
    },
]
