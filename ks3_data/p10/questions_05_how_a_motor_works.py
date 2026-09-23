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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "It roughly doubles, because the push follows the "
                     "current", "correct": True},
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
        "text": "Look at the two force arrows in the diagram. Why must they "
                "always be the same length as each other, whatever the "
                "current is set to?",
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
        "figure": "p10-motor-arrows-marked",
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
            {"text": "It stays the same, because neither the current nor "
                     "the magnets have been changed at all",
             "correct": False,
             "why": "The same current now passes through the field twenty "
                    "times over instead of once, and each pass gets its own "
                    "push."},
            {"text": "It falls to a twentieth, because the current has to be "
                     "shared out between the twenty turns", "correct": False,
             "why": "Nothing is shared. The current runs through every turn "
                    "in succession."},
            {"text": "It reverses, because half of the twenty turns must end "
                     "up running the other way round", "correct": False,
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p10-05-e05",
        "band": "easier",
        "text": "A wire carrying a current in a magnetic field is pushed…",
        "options": [
            {"text": "along its own length", "correct": False,
             "why": "The push is at right angles to the wire, not along it."},
            {"text": "sideways, at right angles to both",
             "correct": True},
            {"text": "towards the nearest pole", "correct": False,
             "why": "It is not attracted to a pole; the push is across both "
                    "the current and the field."},
            {"text": "nowhere — a wire is not magnetic", "correct": False,
             "why": "The current makes a field of its own, and that is what "
                    "the magnet's field acts on."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e06",
        "band": "easier",
        "text": "Reversing the current through a motor's coil, with the "
                "magnets left alone, does what?",
        "options": [
            {"text": "Reverses the direction it turns", "correct": True},
            {"text": "Makes it turn faster the same way", "correct": False,
             "why": "Speed depends on how big the current is, not on which "
                    "way it runs."},
            {"text": "Stops it turning altogether", "correct": False,
             "why": "A current is still flowing, so a push is still made — "
                    "just the other way."},
            {"text": "Makes no difference at all", "correct": False,
             "why": "The direction of the push depends on the current's "
                    "direction, so it changes."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e07",
        "band": "easier",
        "text": "In a motor, the two sides of the coil are pushed…",
        "options": [
            {"text": "the same way, so the coil slides sideways",
             "correct": False,
             "why": "The current runs opposite ways along the two sides, so "
                    "the pushes are opposite too."},
            {"text": "opposite ways, so the coil turns", "correct": True},
            {"text": "towards each other, so the coil is squashed",
             "correct": False,
             "why": "The pushes are opposite in the sense that turns the "
                    "coil, not that crushes it."},
            {"text": "not at all, until the split ring acts", "correct": False,
             "why": "The pushes are there from the first instant; the split "
                    "ring only keeps them useful."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e08",
        "band": "easier",
        "text": "What does a split-ring commutator do?",
        "options": [
            {"text": "It makes the coil turn in the first place",
             "correct": False,
             "why": "The forces on the two sides do the turning; the split "
                    "ring only keeps them going the same way round."},
            {"text": "It reverses the current every half turn",
             "correct": True},
            {"text": "It supplies the current to the magnets", "correct": False,
             "why": "The magnets are permanent and need no current at all."},
            {"text": "It stops the coil turning too fast", "correct": False,
             "why": "It does not limit the speed; it keeps the turning effect "
                    "pointing the same way."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e09",
        "band": "easier",
        "text": "A motor's magnets are turned round so the poles swap, and "
                "nothing else is changed. What happens?",
        "options": [
            {"text": "It turns the other way", "correct": True},
            {"text": "It turns faster the same way", "correct": False,
             "why": "Swapping the poles changes the direction of the push, "
                    "not its size."},
            {"text": "It stops", "correct": False,
             "why": "The field is as strong as before, so the coil is still "
                    "pushed — just the other way."},
            {"text": "It carries on exactly as before", "correct": False,
             "why": "The push depends on the field's direction, and that has "
                    "been reversed."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e10",
        "band": "easier",
        "text": "What has to flow through a motor's coil for it to turn?",
        "options": [
            {"text": "A magnetic field", "correct": False,
             "why": "A field surrounds the coil; it is not something that "
                    "flows through the wire."},
            {"text": "An electric current", "correct": True},
            {"text": "Air, through the gaps in the windings", "correct": False,
             "why": "A motor works in a vacuum; nothing needs to pass through "
                    "it."},
            {"text": "Heat from the magnets", "correct": False,
             "why": "The magnets supply a field, not warmth, and warmth would "
                    "turn nothing."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p10-05-s05",
        "band": "standard",
        "text": "Both the current AND the magnets in a motor are reversed. "
                "What happens?",
        "options": [
            {"text": "It turns the other way", "correct": False,
             "why": "One reversal would do that; two of them put it back "
                    "where it started."},
            {"text": "It carries on turning the same way as before",
             "correct": True},
            {"text": "It stops, because the two reversals fight each other",
             "correct": False,
             "why": "Nothing fights: reversing twice returns the push to its "
                    "original direction."},
            {"text": "It turns twice as fast", "correct": False,
             "why": "Neither change alters the size of the current or the "
                    "field, so the speed is unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s06",
        "band": "standard",
        "text": "A motor is built with two plain rings instead of a split "
                "ring. What happens when it is switched on?",
        "options": [
            {"text": "It runs normally, since the rings still carry the "
                     "current",
             "correct": False,
             "why": "They do carry it, but they never reverse it, so the "
                    "turning effect fights itself after half a turn."},
            {"text": "It swings round and then rocks back and forth instead "
                     "of turning",
             "correct": True},
            {"text": "It turns steadily but the other way round",
             "correct": False,
             "why": "The direction of the first push is unchanged; what fails "
                    "is keeping it going."},
            {"text": "Nothing happens at all", "correct": False,
             "why": "The first half turn happens perfectly well; it is what "
                    "comes after that fails."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s07",
        "band": "standard",
        "text": "The current through a working motor is doubled and nothing "
                "else changes. What happens to the turning effect?",
        "options": [
            {"text": "It halves", "correct": False,
             "why": "A larger current makes a larger push, not a smaller "
                    "one."},
            {"text": "It gets bigger", "correct": True},
            {"text": "It stays the same, because the magnets have not "
                     "changed",
             "correct": False,
             "why": "The push depends on the current as well as the field, "
                    "and the current has doubled."},
            {"text": "It reverses", "correct": False,
             "why": "Reversing needs the current's DIRECTION to change, not "
                    "its size."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s08",
        "band": "standard",
        "text": "A motor's coil is rewound with twenty turns instead of one, "
                "with the same current and magnets. What happens?",
        "options": [
            {"text": "Nothing changes, because the current is the same",
             "correct": False,
             "why": "Each turn is pushed, so twenty turns give about twenty "
                    "times the turning effect."},
            {"text": "The turning effect is much greater", "correct": True},
            {"text": "It turns the other way", "correct": False,
             "why": "Adding turns does not reverse anything; the direction is "
                    "set by the current and the field."},
            {"text": "It stops, because the extra wire blocks the current",
             "correct": False,
             "why": "The current still flows; more wire raises the resistance "
                    "a little, and no more."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s09",
        "band": "standard",
        "text": "A motor's copper coil is replaced with an identical "
                "aluminium one. Does it still turn?",
        "options": [
            {"text": "No, because aluminium is not magnetic", "correct": False,
             "why": "The wire does not need to be magnetic; it needs to carry "
                    "a current."},
            {"text": "Yes, because what matters is that a current flows",
             "correct": True},
            {"text": "No, because aluminium cannot carry a current",
             "correct": False,
             "why": "Aluminium conducts well and is used for power cables."},
            {"text": "Yes, but it turns the other way", "correct": False,
             "why": "Changing the metal does not change which way the current "
                    "runs."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s10",
        "band": "standard",
        "text": "A current-carrying wire lies exactly along the field "
                "direction between two poles. What force acts on it?",
        "options": [
            {"text": "The largest force possible", "correct": False,
             "why": "The push is largest when the wire is at right angles to "
                    "the field, not along it."},
            {"text": "A force along the wire, pushing it out", "correct": False,
             "why": "The push is never along the wire; it is at right angles "
                    "to it."},
            {"text": "None at all", "correct": True},
            {"text": "A force towards the north pole", "correct": False,
             "why": "The wire is not attracted to a pole; the push depends on "
                    "how the current crosses the field."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p10-05-h05",
        "band": "harder",
        "text": "A single-coil motor is held with its coil exactly upright "
                "and released with the current on. What happens?",
        "options": [
            {"text": "It accelerates away at once, just as it would from any "
                     "other position",
             "correct": False,
             "why": "In that one position the two pushes act straight along "
                    "the coil and give no turning effect."},
            {"text": "It may not start, because there is no turning effect "
                     "there",
             "correct": True},
            {"text": "It turns the other way from usual", "correct": False,
             "why": "Nothing has reversed; the difficulty is that nothing "
                    "turns it at all."},
            {"text": "It burns out immediately", "correct": False,
             "why": "It draws its usual current; standing still is not the "
                    "same as a fault."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h06",
        "band": "harder",
        "text": "Why does a motor need the current reversed every half turn?",
        "options": [
            {"text": "Because the current would otherwise run out",
             "correct": False,
             "why": "The supply keeps delivering it; nothing runs out."},
            {"text": "Because after half a turn the sides have swapped over",
             "correct": True},
            {"text": "Because the magnets swap poles as the coil turns",
             "correct": False,
             "why": "The magnets are fixed and never change; it is the coil "
                    "that moves."},
            {"text": "Because the coil would otherwise overheat",
             "correct": False,
             "why": "Heating depends on the current's size, not on its "
                    "direction."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h07",
        "band": "harder",
        "text": "A cordless drill has a forward and reverse switch, and its "
                "magnets cannot be moved. What must the switch do?",
        "options": [
            {"text": "Swap the magnets over inside the casing",
             "correct": False,
             "why": "The question says they cannot be moved, and no switch "
                    "could turn a fixed magnet round."},
            {"text": "Reverse the current fed into the motor", "correct": True},
            {"text": "Slow the motor until it turns the other way",
             "correct": False,
             "why": "Slowing never reverses a direction; it only reduces the "
                    "speed."},
            {"text": "Disconnect the split ring", "correct": False,
             "why": "Without the split ring the motor would rock rather than "
                    "run backwards."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h08",
        "band": "harder",
        "text": "In a loudspeaker a coil sits in a magnet's field and the "
                "current through it changes direction thousands of times a "
                "second. What does the coil do?",
        "options": [
            {"text": "Spins round faster and faster", "correct": False,
             "why": "It is not free to spin; each reversal pushes it back the "
                    "other way."},
            {"text": "Moves back and forth, pushing the air", "correct": True},
            {"text": "Stays still, because the reversals cancel out",
             "correct": False,
             "why": "They do not cancel — each one drives it the other way, "
                    "which is the movement."},
            {"text": "Heats up until the cone melts", "correct": False,
             "why": "It warms a little, but the useful effect is the "
                    "movement it makes."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h09",
        "band": "harder",
        "text": "A student says the coil is pulled round because the magnets "
                "attract it. What is right?",
        "options": [
            {"text": "They are right — the coil is iron and is attracted",
             "correct": False,
             "why": "The coil is usually copper, which is not magnetic at "
                    "all."},
            {"text": "A current in a field feels a force, pushing the coil "
                     "sideways",
             "correct": True},
            {"text": "The coil is repelled by both magnets equally",
             "correct": False,
             "why": "Neither attraction nor repulsion of the metal is "
                    "involved; the current is what matters."},
            {"text": "The magnets attract it only while the split ring keeps "
                     "the circuit closed",
             "correct": False,
             "why": "The split ring switches the current; it does not turn an "
                    "attraction on and off."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h10",
        "band": "harder",
        "text": "On a motor diagram the two force arrows are drawn the same "
                "length as each other whatever the current is. Why?",
        "options": [
            {"text": "Because the arrows are decorative and their length "
                     "means nothing",
             "correct": False,
             "why": "Arrow length is meaningful; the point is that these two "
                    "forces really are equal."},
            {"text": "Because the same current runs through both sides in the "
                     "same field",
             "correct": True},
            {"text": "Because one side is always stronger and the diagram "
                     "simplifies it",
             "correct": False,
             "why": "Neither side is stronger; the equality is real rather "
                    "than a simplification."},
            {"text": "Because the split ring makes them equal", "correct": False,
             "why": "The split ring reverses the current; it does not balance "
                    "two forces."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · easier ──────────────────────────────────
    {
        "id": "p10-05-e11",
        "band": "easier",
        "text": "What provides the magnetic field that a motor's coil sits "
                "inside?",
        "options": [
            {"text": "Two permanent magnets, fixed either side of the "
                     "coil", "correct": True},
            {"text": "The coil's own current, doubling back on itself",
             "correct": False,
             "why": "The coil's current is what gets pushed by the field; "
                    "the field itself comes from the magnets either side "
                    "of it."},
            {"text": "The split-ring commutator", "correct": False,
             "why": "The commutator switches the current's direction; it "
                    "makes no magnetic field of its own."},
            {"text": "The brushes, once they touch the split ring",
             "correct": False,
             "why": "Brushes are just fixed electrical contacts; they "
                    "produce no field."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e12",
        "band": "easier",
        "text": "What is the job of the brushes in a motor?",
        "options": [
            {"text": "To hold the two magnets in place", "correct": False,
             "why": "The magnets are fixed to the case directly; the "
                    "brushes touch the spinning part, not the magnets."},
            {"text": "To let a current reach a part of the machine that is "
                     "spinning", "correct": True},
            {"text": "To reverse the current every half turn as the coil keeps on going round and round", "correct": False,
             "why": "That is the split ring's job. The brushes are the "
                    "fixed contacts that press against it."},
            {"text": "To slow the coil down once the current is switched off, the way a brake on a wheel would", "correct": False,
             "why": "Nothing here brakes the coil; the brushes are simply "
                    "an electrical connection."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e13",
        "band": "easier",
        "text": "What does the split-ring commutator do, exactly, every "
                "half turn?",
        "options": [
            {"text": "It disconnects the coil completely for an instant, losing contact with it entirely",
             "correct": False,
             "why": "The connection is not broken; the current is "
                    "switched to run the other way round the coil."},
            {"text": "It swaps which magnet the field comes from",
             "correct": False,
             "why": "The magnets are fixed and never swapped; what "
                    "changes is the direction of the current in the "
                    "coil."},
            {"text": "It reverses the direction of the current through "
                     "the coil", "correct": True},
            {"text": "It doubles the current flowing through the coil on every single pass",
             "correct": False,
             "why": "Nothing about the size of the current changes at "
                    "the commutator; only its direction."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e14",
        "band": "easier",
        "text": "Run a working electric motor backwards by hand — turn its "
                "axle yourself instead of feeding it a current. What "
                "happens?",
        "options": [
            {"text": "Nothing at all; a motor only ever works one way round and cannot be reversed by hand", "correct": False,
             "why": "Turning the coil through the field pushes charge "
                    "along the wire, exactly as feeding it a current "
                    "pushes the coil round."},
            {"text": "The magnets swap poles automatically", "correct": False,
             "why": "The magnets are fixed permanently and do not "
                    "respond to the axle being turned."},
            {"text": "The split ring stops working", "correct": False,
             "why": "The split ring keeps doing its job of switching the "
                    "connection every half turn, whichever way the "
                    "machine is being driven."},
            {"text": "A voltage appears across its two ends — it is now "
                     "acting as a generator", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e15",
        "band": "easier",
        "text": "A single-coil motor's turning effect falls to nothing "
                "twice during every full turn, when the coil is upright. "
                "What do real motors do to avoid running unevenly because "
                "of this?",
        "options": [
            {"text": "Use several coils, set at different angles, so one "
                     "is always well placed", "correct": True},
            {"text": "Use a much bigger single coil instead of one small one, to make its swing more powerful", "correct": False,
             "why": "A bigger single coil still has the same upright "
                    "position where its turning effect falls to nothing; "
                    "size does not fix the problem."},
            {"text": "Remove the split ring and rely on the magnets alone to keep it turning smoothly", "correct": False,
             "why": "Removing the split ring makes a single coil stop "
                    "after half a turn; it does not solve the upright "
                    "problem at all."},
            {"text": "Spin the magnets instead of the coil", "correct": False,
             "why": "It is the coil that turns in a normal motor; "
                    "spinning the magnets instead is not how the fix "
                    "works."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e16",
        "band": "easier",
        "text": "A real motor with several coils has a commutator with "
                "more than one segment. Why?",
        "options": [
            {"text": "So each coil can be switched off in turn to save "
                     "power", "correct": False,
             "why": "The coils are not switched off in turn to save "
                    "power; every segment exists to reverse each coil's "
                    "own current at the right moment."},
            {"text": "Each coil needs its own connection reversed at its "
                     "own moment, as it passes through the upright "
                     "position", "correct": True},
            {"text": "So the motor can run at more than one speed",
             "correct": False,
             "why": "Speed is set by the current, not by how many "
                    "commutator segments there are."},
            {"text": "So the magnets can be reversed independently of each other, switching their poles apart at different times", "correct": False,
             "why": "The magnets are fixed and are not switched by the "
                    "commutator at all; only the coils' currents are."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e17",
        "band": "easier",
        "text": "At 0.5 A, the turning effect on the bench reads 13, and "
                "friction at the axle is worth about 15. What happens?",
        "options": [
            {"text": "The motor turns very slowly, creeping round bit by bit", "correct": False,
             "why": "A turning effect smaller than the friction is not "
                    "enough to move it at all, however slowly."},
            {"text": "The motor turns at normal speed after a short "
                     "delay", "correct": False,
             "why": "There is no delay effect here; if the turning "
                    "effect cannot beat the friction, it simply never "
                    "starts."},
            {"text": "The motor does not start at all", "correct": True},
            {"text": "The motor turns backwards", "correct": False,
             "why": "Nothing here reverses the current or the field; not "
                    "starting is not the same as running the wrong way."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e18",
        "band": "easier",
        "text": "At 2.0 A, the turning effect on the bench reads 50, well "
                "above the friction of about 15. What happens?",
        "options": [
            {"text": "The motor does not start", "correct": False,
             "why": "A turning effect well above the friction is exactly "
                    "what is needed to start turning."},
            {"text": "The motor turns for a moment and then stops",
             "correct": False,
             "why": "Nothing here causes it to stop after starting; with "
                    "the split ring fitted the current keeps reversing "
                    "and the motor keeps going."},
            {"text": "The motor spins the magnets around the coil",
             "correct": False,
             "why": "It is the coil that turns; the magnets are fixed to "
                    "the case."},
            {"text": "The motor starts and keeps turning", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e19",
        "band": "easier",
        "text": "Comparing the bench's own figures, why does the motor "
                "start at 1.0 A but not at 0.5 A?",
        "options": [
            {"text": "Because at 1.0 A the turning effect (25) beats "
                     "the friction (about 15), but at 0.5 A it (13) "
                     "does not", "correct": True},
            {"text": "Because 1.0 A is an even number and 0.5 A is not",
             "correct": False,
             "why": "Whether a number is even has nothing to do with a "
                    "real motor starting; what matters is the turning "
                    "effect against the friction."},
            {"text": "Because the split ring only works above 1.0 A",
             "correct": False,
             "why": "The split ring works at any current; the reason "
                    "for not starting at 0.5 A is that the turning "
                    "effect there is too small, not a threshold on the "
                    "split ring."},
            {"text": "Because the magnets are only switched on above 1.0 A, staying off below that current entirely, whatever the split ring is doing", "correct": False,
             "why": "The magnets are permanent and are not switched on "
                    "or off by the current at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e20",
        "band": "easier",
        "text": "In a motor, the current runs one way along one side of "
                "the coil and the other way along the other side. Why "
                "does this matter?",
        "options": [
            {"text": "It means only one side of the coil is ever pushed, while the other side stays completely still",
             "correct": False,
             "why": "Both sides carry a current and both are pushed; the "
                    "currents simply run in opposite directions along "
                    "them."},
            {"text": "It means the two sides are pushed in opposite "
                     "directions, which is what turns the coil",
             "correct": True},
            {"text": "It means the coil heats up twice as fast",
             "correct": False,
             "why": "Heating depends on the size of the current, not on "
                    "which way it happens to be running along each "
                    "side."},
            {"text": "It means the split ring is not needed", "correct": False,
             "why": "The split ring is still needed, to keep reversing "
                    "the current every half turn as the coil turns."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e21",
        "band": "easier",
        "text": "A motor's magnets are swapped for a stronger pair, with "
                "the current left exactly the same. What would you "
                "expect?",
        "options": [
            {"text": "No change, because the coil decides the strength "
                     "on its own", "correct": False,
             "why": "The field the coil sits in is part of what sets the "
                    "push; a stronger field gives a bigger push."},
            {"text": "The motor turns the opposite way", "correct": False,
             "why": "Direction depends on which pole is on which side, "
                    "not on how strong the magnets are."},
            {"text": "The turning effect increases", "correct": True},
            {"text": "The motor stops completely", "correct": False,
             "why": "A stronger field gives a bigger push, not none at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e22",
        "band": "easier",
        "text": "A current-carrying wire is turned so it lies exactly at "
                "right angles to the magnetic field, rather than at any "
                "other angle. What happens to the push on it?",
        "options": [
            {"text": "It disappears completely", "correct": False,
             "why": "A wire at right angles to the field gets the "
                    "largest push, not none at all; the push vanishes "
                    "only when the wire lies along the field."},
            {"text": "It becomes weaker than at any other angle",
             "correct": False,
             "why": "Right angles is the strongest angle for the push, "
                    "not the weakest."},
            {"text": "It stays exactly the same as at any other angle",
             "correct": False,
             "why": "The angle between the wire and the field changes "
                    "the size of the push; right angles gives the "
                    "biggest push there is."},
            {"text": "It becomes as large as it can possibly be, for "
                     "that current and field", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e23",
        "band": "easier",
        "text": "A motor's split ring is present, but the brushes fail to "
                "touch it because they have worn away. What happens when "
                "the switch is closed?",
        "options": [
            {"text": "Nothing — no current can reach the spinning coil, "
                     "so it does not turn", "correct": True},
            {"text": "The coil turns normally, since the split ring "
                     "itself still switches correctly", "correct": False,
             "why": "Switching correctly is useless if no current can "
                    "get to the coil through the brushes in the first "
                    "place."},
            {"text": "The magnets take over and turn the coil instead",
             "correct": False,
             "why": "The magnets never turn the coil on their own; they "
                    "only provide the field a current in the coil is "
                    "pushed against."},
            {"text": "The coil turns, but only in one direction, without ever reversing at all", "correct": False,
             "why": "It does not turn in any direction at all if no "
                    "current reaches it; nothing is pushing it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e24",
        "band": "easier",
        "text": "A wire lies exactly along the direction of the magnetic "
                "field, rather than across it. What force acts on it "
                "while a current flows?",
        "options": [
            {"text": "The strongest push possible, since it is lined up "
                     "with the field", "correct": False,
             "why": "Lining up with the field gives the weakest push of "
                    "all, not the strongest — none at all, in fact."},
            {"text": "No force at all", "correct": True},
            {"text": "A force that pulls it towards the nearest pole",
             "correct": False,
             "why": "There is no attraction here between the wire and "
                    "the magnet's poles."},
            {"text": "A force along the wire's own length", "correct": False,
             "why": "Even where a push does occur, it is always across "
                    "the wire, never along it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e25",
        "band": "easier",
        "text": "A working motor is running clockwise. Its current is "
                "reversed, but its magnets are left alone. Which way does "
                "it now turn?",
        "options": [
            {"text": "Clockwise still, at the same speed", "correct": False,
             "why": "Reversing the current on its own reverses the "
                    "direction of the push, not leaves it unchanged."},
            {"text": "It stops completely", "correct": False,
             "why": "A current is still flowing, in the opposite "
                    "direction, so a push is still made — just the "
                    "other way."},
            {"text": "Anticlockwise", "correct": True},
            {"text": "Clockwise, but more slowly", "correct": False,
             "why": "The size of the push has not changed, only its "
                    "direction, since only the current was reversed."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e26",
        "band": "easier",
        "text": "A motor's split ring wears down and starts making poor "
                "contact with the brushes at random moments. What is "
                "the most likely symptom?",
        "options": [
            {"text": "The magnets weaken over time", "correct": False,
             "why": "Wear on the split ring has no effect on the "
                    "magnets, which are fixed and unaffected by "
                    "anything happening at the axle."},
            {"text": "The current reverses permanently", "correct": False,
             "why": "Poor contact interrupts the current now and then; "
                    "it does not permanently reverse anything."},
            {"text": "The coil runs at exactly double its normal speed, however poor the contact becomes",
             "correct": False,
             "why": "Poor contact can only interrupt or weaken the "
                    "push; it cannot double it."},
            {"text": "The coil turns unevenly, sometimes losing its "
                     "push mid-turn", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e27",
        "band": "easier",
        "text": "In an ordinary motor, is it the coil or the magnets that "
                "spin round?",
        "options": [
            {"text": "The coil", "correct": True},
            {"text": "The magnets", "correct": False,
             "why": "The magnets are fixed to the case; it is the coil, "
                    "on its axle, that turns."},
            {"text": "Both of them, together", "correct": False,
             "why": "The magnets stay fixed throughout; only the coil is "
                    "mounted to turn."},
            {"text": "Neither — only the split ring turns", "correct": False,
             "why": "The split ring is fixed to the same axle as the "
                    "coil and turns with it, but it is the coil's "
                    "turning that is the point of a motor."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e28",
        "band": "easier",
        "text": "Two identical single-coil motors are set running. One is "
                "stopped by hand with its coil flat (the strongest "
                "position); the other is stopped with its coil upright. "
                "Both are released at the same moment, with the same "
                "current still flowing. Which one starts turning again "
                "immediately?",
        "options": [
            {"text": "The upright one, since it has further to go",
             "correct": False,
             "why": "Having further to travel is not what matters; in "
                    "the upright position there is no turning effect at "
                    "all to start it moving."},
            {"text": "The flat one, since that is where the turning "
                     "effect is largest", "correct": True},
            {"text": "Both, equally, since the current is exactly the same in each one", "correct": False,
             "why": "The current being the same does not mean the "
                    "turning effect is the same; position matters too, "
                    "and upright gives none at all."},
            {"text": "Neither — releasing a stopped motor never restarts it, whatever position it was stopped in", "correct": False,
             "why": "A motor can restart perfectly well from a position "
                    "where there is a genuine turning effect, such as "
                    "the flat position."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e29",
        "band": "easier",
        "text": "A relay-like device pulls its arm using a coil's "
                "magnetic field, just as a motor's coil is pushed by the "
                "magnets around it. What is the key difference in what "
                "moves?",
        "options": [
            {"text": "In a relay, the coil turns; in a motor, the arm "
                     "turns", "correct": False,
             "why": "It is the other way round in terms of the moving "
                    "part carrying current: in a motor the "
                    "current-carrying coil is what moves, not a "
                    "separate arm."},
            {"text": "Neither device has anything that moves at all",
             "correct": False,
             "why": "Both devices have a moving part — the relay's arm "
                    "and the motor's coil."},
            {"text": "In a relay, an iron arm is pulled straight across; "
                     "in a motor, the coil itself turns continuously",
             "correct": True},
            {"text": "In a motor, the magnets move; in a relay, the coil moves, each one doing completely the other's usual job", "correct": False,
             "why": "In a motor the magnets are fixed and the coil "
                    "turns; the comparison the other way round is not "
                    "correct either."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-e30",
        "band": "easier",
        "text": "A motor's split ring is coated by accident with an "
                "insulating layer, so no current can reach the coil "
                "through it at all. What happens when the switch is "
                "closed?",
        "options": [
            {"text": "The motor runs exactly as normal", "correct": False,
             "why": "With no current able to reach the coil, there is no "
                    "push on it at all, so it cannot run normally."},
            {"text": "The motor runs, but only in one direction with no half-turn reversal, never swapping over at all", "correct": False,
             "why": "There is no current reaching the coil in the first "
                    "place, so there is nothing to reverse and nothing "
                    "to make it turn at all."},
            {"text": "The magnets spin instead of the coil", "correct": False,
             "why": "The magnets are fixed to the case regardless of "
                    "what happens at the split ring; they never spin."},
            {"text": "Nothing happens — no current reaches the coil, so "
                     "there is no push and no turning at all",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · standard ────────────────────────────────
    {
        "id": "p10-05-s11",
        "band": "standard",
        "text": "A single-coil motor is compared with an identical one, "
                "except the second is deliberately started from a "
                "position half way between flat and upright. Which one "
                "is more likely to start moving strongly straight away?",
        "options": [
            {"text": "The one started away from upright, since it "
                     "already has a genuine turning effect there",
             "correct": True},
            {"text": "The one started upright, since it has the furthest to accelerate through, covering the most ground overall", "correct": False,
             "why": "The upright position starts with no turning "
                    "effect at all; having further to go does not help "
                    "if nothing is pushing it round yet."},
            {"text": "Neither — both start identically regardless of "
                     "position", "correct": False,
             "why": "Position matters: the turning effect is not the "
                    "same in every position, it is smallest exactly "
                    "upright and larger elsewhere."},
            {"text": "It depends only on the current, not on position",
             "correct": False,
             "why": "Current sets how big the turning effect could be; "
                    "position decides whether that effect is close to "
                    "zero or not, which matters just as much here."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s12",
        "band": "standard",
        "text": "A student says a motor's turning effect is the same in "
                "every position as the coil spins round. Are they right?",
        "options": [
            {"text": "Yes — the pushes on the coil never change as it turns, "
                     "and neither does the distance from the axle that they act "
                     "at", "correct": False,
             "why": "The pushes are always there, but the amount of "
                    "TURNING they produce changes with position, largest "
                    "when flat and none at all when upright."},
            {"text": "No — it is largest when the coil is flat and falls "
                     "to nothing when it is upright", "correct": True},
            {"text": "Yes — that is exactly why real motors only need one coil, and never more than a single one", "correct": False,
             "why": "Real motors use several coils precisely because a "
                    "single coil's turning effect is not the same all "
                    "the way round."},
            {"text": "No — it is largest when the coil is upright",
             "correct": False,
             "why": "Upright is the position with no turning effect at "
                    "all; flat is where it is largest."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s13",
        "band": "standard",
        "text": "At 1.0 A the turning effect reads 25 and the friction is "
                "about 15; at 0.5 A it reads 13. Roughly what is the "
                "smallest current at which this motor would just about "
                "start?",
        "options": [
            {"text": "About 0.1 A, since any current at all gives some turning effect, however tiny that effect might be", "correct": False,
             "why": "Some turning effect is not the same as enough "
                    "turning effect; 0.5 A already gives 13, still below "
                    "the friction of 15."},
            {"text": "About 4.0 A, since only the very largest current "
                     "works", "correct": False,
             "why": "4.0 A works, but so does a current well below "
                    "that — 1.0 A already gives 25, comfortably above "
                    "the 15 needed."},
            {"text": "Somewhere between 0.5 A and 1.0 A, since 13 is "
                     "just below the friction and 25 is comfortably "
                     "above it", "correct": True},
            {"text": "Exactly 0.5 A, since that is the value given on "
                     "the bench", "correct": False,
             "why": "0.5 A is given as a value where it does NOT start, "
                    "since 13 is below the friction of 15."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s14",
        "band": "standard",
        "text": "A motor's magnets and its current are both reversed at "
                "the same time. A student expects it to spin twice as "
                "fast in the opposite direction. What is wrong?",
        "options": [
            {"text": "Reversing the current alone would already make it spin at the same speed, exactly as before but backwards",
             "correct": False,
             "why": "That much is correct on its own, but the question "
                    "is about what happens when BOTH are reversed "
                    "together, which this option does not address."},
            {"text": "Two reversals make it stop completely, not spin "
                     "faster", "correct": False,
             "why": "Two reversals cancel out and leave it turning "
                    "exactly as it did before — not stopped, and not "
                    "faster."},
            {"text": "Reversing the magnets makes the motor run at half "
                     "speed", "correct": False,
             "why": "Reversing the magnets on its own reverses the "
                    "direction, not the speed; speed is set by the "
                    "current."},
            {"text": "Reversing both changes cancel out, so the motor "
                     "turns exactly as it did before — not faster, and "
                     "not reversed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s15",
        "band": "standard",
        "text": "A student knows which way the current flows in a "
                "motor's coil, but does not know how the magnets are "
                "arranged around it. Can they predict which way the "
                "coil will turn?",
        "options": [
            {"text": "No — the direction depends on both the current's "
                     "direction and the field's direction, so knowing "
                     "only one is not enough", "correct": True},
            {"text": "Yes — the current's direction on its own always "
                     "decides which way it turns", "correct": False,
             "why": "The current is only half the story; the field's "
                    "direction also decides which way the push acts."},
            {"text": "Yes — a motor always turns clockwise regardless of "
                     "how the magnets are arranged", "correct": False,
             "why": "There is no fixed default direction; it depends on "
                    "both the current and the field together."},
            {"text": "No — the direction cannot be predicted from "
                     "either quantity, however much is known",
             "correct": False,
             "why": "Direction can be predicted, but only once both the "
                    "current's direction and the field's direction are "
                    "known together."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s16",
        "band": "standard",
        "text": "A motor's axle bearings are lubricated, cutting the "
                "friction at the axle roughly in half. With the current "
                "unchanged, what happens to the lowest current at which "
                "the motor will just start turning?",
        "options": [
            {"text": "It rises, since less friction needs a bigger push "
                     "to overcome it", "correct": False,
             "why": "Less friction needs a smaller push to overcome, "
                    "not a bigger one, so the required current falls "
                    "rather than rises."},
            {"text": "It falls, since a smaller turning effect is now "
                     "enough to beat the reduced friction", "correct": True},
            {"text": "It stays the same, since friction does not affect when a motor starts turning at all", "correct": False,
             "why": "Friction is exactly what must be beaten before any "
                    "motor starts turning; less friction lowers the "
                    "current needed."},
            {"text": "It cannot be worked out, since friction and "
                     "current cannot be compared with each other",
             "correct": False,
             "why": "They can be compared directly, on the bench's own "
                    "scale, where a numerical turning effect is set "
                    "against a numerical friction value."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s17",
        "band": "standard",
        "text": "A motor's coil has its wire doubled in thickness, "
                "keeping the same number of turns and the same current. "
                "What happens to the turning effect?",
        "options": [
            {"text": "It doubles, since a thicker wire carries a "
                     "stronger push", "correct": False,
             "why": "Wire thickness is not stated in the lesson as "
                    "something the turning effect depends on; current "
                    "and turns are."},
            {"text": "It halves, since a thicker wire resists the "
                     "current more", "correct": False,
             "why": "A thicker wire in fact has less resistance, not "
                    "more, but in any case resistance is not what this "
                    "question is testing — the current here is "
                    "unchanged."},
            {"text": "It stays about the same, since neither the "
                     "current nor the number of turns has changed",
             "correct": True},
            {"text": "It reverses, since a thicker wire changes which way the current flows through the whole circuit", "correct": False,
             "why": "Wire thickness has no bearing on the direction a "
                    "current runs; that is set by the supply "
                    "connections."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s18",
        "band": "standard",
        "text": "A generator is a motor run in reverse: the coil is "
                "turned by hand or by an engine, rather than by a "
                "current. Why does turning the coil produce a voltage?",
        "options": [
            {"text": "The magnets are spun by the turning coil, which "
                     "creates the voltage", "correct": False,
             "why": "The magnets stay fixed; it is the coil that is "
                    "physically turned through their field."},
            {"text": "The split ring reverses direction fast enough to generate its own current without any coil at all", "correct": False,
             "why": "The split ring only switches connections; it does "
                    "not create a current on its own."},
            {"text": "Friction at the axle converts the turning into "
                     "electrical energy", "correct": False,
             "why": "Friction wastes energy as heat; it plays no part "
                    "in producing the voltage."},
            {"text": "Moving a wire through a magnetic field pushes the "
                     "charge inside it along, which is a voltage",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s19",
        "band": "standard",
        "text": "A single-coil motor is compared with an otherwise "
                "identical motor that has three coils set at different "
                "angles. Both use the same current. What is the main "
                "advantage of the three-coil version?",
        "options": [
            {"text": "It can start from any position, since at least one "
                     "coil always has a useful turning effect",
             "correct": True},
            {"text": "It produces a stronger magnetic field from its magnets, which is what the extra coils are really for", "correct": False,
             "why": "The magnets are unchanged; the difference is "
                    "entirely in the coil arrangement, not the field "
                    "they sit in."},
            {"text": "It needs a smaller current to run at the same "
                     "speed", "correct": False,
             "why": "Adding coils changes how evenly the turning effect "
                    "is produced, not how much current is needed for a "
                    "given speed."},
            {"text": "It no longer needs a split ring at all", "correct": False,
             "why": "A commutator is still needed — now with a segment "
                    "for each coil, rather than none at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s20",
        "band": "standard",
        "text": "At 4.0 A a motor's turning effect reads 100, and the "
                "friction at its axle is worth about 15. How much "
                "turning effect is left over to drive a load?",
        "options": [
            {"text": "About 115, since the friction adds to the push the "
                     "motor is making", "correct": False,
             "why": "Friction acts against the turning, so it comes off "
                    "the turning effect rather than adding to it."},
            {"text": "About 85, since the friction is taken away from "
                     "the turning effect", "correct": True},
            {"text": "About 100, since friction acts on the axle rather "
                     "than on the coil", "correct": False,
             "why": "Wherever it acts, the friction has to be overcome "
                    "by the coil's turning effect, so it still comes off "
                    "the 100."},
            {"text": "About 15, since the friction sets the size of what "
                     "is left over", "correct": False,
             "why": "The 15 is the friction itself, not what is left "
                    "after it. Taking 15 from 100 leaves 85."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s21",
        "band": "standard",
        "text": "A student wants to make a bigger turning effect without "
                "changing the current or the magnets. What could they "
                "change instead?",
        "options": [
            {"text": "The colour of the coil's insulation", "correct": False,
             "why": "Colour has no bearing on the size of any push; it "
                    "is not one of the things this lesson says the "
                    "turning effect depends on."},
            {"text": "The material the axle is made from", "correct": False,
             "why": "The axle material affects friction, not the "
                    "turning effect itself."},
            {"text": "The number of turns on the coil", "correct": True},
            {"text": "The thickness of the brushes", "correct": False,
             "why": "The brushes are an electrical connection to the "
                    "spinning part; their thickness does not change how "
                    "big the push on the coil is."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s22",
        "band": "standard",
        "text": "A motor is running normally. The magnets are then "
                "swapped for a pair with the same strength but "
                "positioned the other way round — north where south was, "
                "and south where north was. What happens?",
        "options": [
            {"text": "The turning effect gets bigger, since the magnets "
                     "have been repositioned", "correct": False,
             "why": "Repositioning which pole faces which side changes "
                    "the DIRECTION of the push, not how big it is."},
            {"text": "The motor stops, since the field now opposes "
                     "itself", "correct": False,
             "why": "The field does not oppose itself; it simply points "
                    "the other way, giving a push in the opposite "
                    "direction."},
            {"text": "Nothing changes, since the magnets are equally "
                     "strong either way round", "correct": False,
             "why": "Which pole faces which side sets the direction of "
                    "the push; swapping them over does change "
                    "something, even though the strength is unchanged."},
            {"text": "The motor turns the opposite way, at the same "
                     "speed as before", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s23",
        "band": "standard",
        "text": "In a motor, why must the current run in opposite "
                "directions along the two sides of the coil, rather than "
                "the same direction along both?",
        "options": [
            {"text": "So the two sides are pushed in opposite "
                     "directions, which is what creates a turning "
                     "effect rather than a sideways one", "correct": True},
            {"text": "So the coil carries twice as much current overall, flowing twice as fast around the whole of the loop from end to end and back again", "correct": False,
             "why": "The total current is set by the supply and the "
                    "coil's resistance, not by which way it happens to "
                    "be running on each side."},
            {"text": "So the split ring can tell the two sides apart",
             "correct": False,
             "why": "The split ring reverses the current at the right "
                    "moment regardless of this; it does not need the "
                    "two sides to differ to do its job."},
            {"text": "So the coil does not overheat as quickly",
             "correct": False,
             "why": "Heating depends on how much current flows and for "
                    "how long, not on which direction it runs along "
                    "each side."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s24",
        "band": "standard",
        "text": "A real motor has several coils rather than one, each "
                "with its own segment on the commutator. If one "
                "segment's connection to its brush is broken, what would "
                "you expect?",
        "options": [
            {"text": "The whole motor stops working completely, with every one of its coils losing power all at once",
             "correct": False,
             "why": "The other coils and their segments are unaffected; "
                    "a single broken connection removes one coil's "
                    "contribution, not all of them."},
            {"text": "That one coil no longer contributes a push, but "
                     "the motor still turns using the others",
             "correct": True},
            {"text": "All the coils lose their current at once, since every "
                     "segment of a commutator feeds the whole set of coils "
                     "together",
             "correct": False,
             "why": "Each coil has its own separate segment and "
                    "connection; one failing does not disconnect the "
                    "others."},
            {"text": "The magnets stop providing a field", "correct": False,
             "why": "The magnets are unaffected by anything happening "
                    "at the commutator; they are permanent and fixed."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s25",
        "band": "standard",
        "text": "A motor's coil is rewound with the same number of turns "
                "but thinner wire, keeping the current exactly the same "
                "on the same supply. What happens to the turning "
                "effect?",
        "options": [
            {"text": "It falls, because thinner wire cannot carry "
                     "current as well", "correct": False,
             "why": "The current is stated to be exactly the same here, "
                    "so however well the wire carries it, the push it "
                    "experiences is unchanged."},
            {"text": "It reverses, because thinner wire changes the current's direction through the whole of the coil", "correct": False,
             "why": "Wire thickness has no bearing on which way a "
                    "current runs; only the supply connections decide "
                    "that."},
            {"text": "It stays about the same, since the turning effect "
                     "depends on the current and the turns, and neither "
                     "has changed", "correct": True},
            {"text": "It grows, because thinner wire sits closer to the "
                     "magnets", "correct": False,
             "why": "How close the wire sits to the magnets is not "
                    "something this lesson's rule depends on; current "
                    "and turns are."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s26",
        "band": "standard",
        "text": "A generator is built exactly like a motor, with a coil, "
                "a split ring and brushes, but is turned by an engine "
                "instead of being fed a current. What job does the "
                "split ring do here?",
        "options": [
            {"text": "It supplies the mechanical turning force from the "
                     "engine", "correct": False,
             "why": "The engine supplies the turning force directly to "
                    "the axle; the split ring is an electrical part, "
                    "not a mechanical one."},
            {"text": "It creates the magnetic field the coil moves "
                     "through", "correct": False,
             "why": "The magnets create that field, exactly as in a "
                    "motor; the split ring plays no part in making the "
                    "field."},
            {"text": "It slows the coil down so a steady voltage can be measured, the same way brakes work on a bicycle wheel", "correct": False,
             "why": "The split ring does not brake anything; its job "
                    "concerns the direction of the current at each "
                    "brush, not the speed."},
            {"text": "It still switches the connection every half turn, "
                     "so the voltage produced always pushes current the "
                     "same way out of the two brushes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s27",
        "band": "standard",
        "text": "A motor's coil sits exactly upright and is given a "
                "small nudge by hand while the current is still on. "
                "What happens next?",
        "options": [
            {"text": "The turning effect returns almost immediately as "
                     "the coil moves away from that one exact position",
             "correct": True},
            {"text": "Nothing — once stopped upright, a motor can never restart again, however long it is left sitting there", "correct": False,
             "why": "It only fails to start FROM that exact position; "
                    "nudging it away from upright puts it somewhere the "
                    "turning effect is not zero."},
            {"text": "It reverses direction because it was nudged",
             "correct": False,
             "why": "A small nudge does not reverse the current or the "
                    "field; it only moves the coil to a position where a "
                    "turning effect exists again."},
            {"text": "It spins the magnets instead of the coil",
             "correct": False,
             "why": "The magnets remain fixed to the case whatever "
                    "happens to the coil."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s28",
        "band": "standard",
        "text": "Two identical motors are compared. Motor A runs on "
                "2.0 A; Motor B, otherwise identical, runs on 4.0 A. How "
                "does Motor B's turning effect compare with Motor A's?",
        "options": [
            {"text": "About the same, since the magnets are identical in "
                     "both", "correct": False,
             "why": "The magnets being the same does not cancel out a "
                    "doubled current; a bigger current gives a bigger "
                    "push."},
            {"text": "Roughly twice as large, since the turning effect "
                     "rises with current", "correct": True},
            {"text": "About four times as large, since current appears "
                     "squared in the relationship", "correct": False,
             "why": "Nothing here squares the current; the turning "
                    "effect rises roughly in proportion to it, not to "
                    "its square."},
            {"text": "Smaller, since a bigger current makes the coil "
                     "run hotter and weaker", "correct": False,
             "why": "Heating is a real practical issue, but it does not "
                    "turn a bigger current into a smaller push in this "
                    "comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s29",
        "band": "standard",
        "text": "A student increases both the current AND the number of "
                "turns on a motor's coil, each by the same factor. What "
                "happens to the turning effect?",
        "options": [
            {"text": "It changes by that one factor only, since one of the two changes is wasted completely", "correct": False,
             "why": "Neither change is wasted; both the current and the "
                    "turns each add to the turning effect."},
            {"text": "It stays the same, since increasing two things "
                     "together always cancels out", "correct": False,
             "why": "Increasing two things that both help does not "
                    "cancel out; it makes the effect considerably "
                    "bigger, not unchanged."},
            {"text": "It increases by much more than either change on "
                     "its own, since both contribute together",
             "correct": True},
            {"text": "It reverses, since two increases together flip "
                     "the direction", "correct": False,
             "why": "The size of the current and the number of turns "
                    "have no bearing on which way the coil is pushed."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-s30",
        "band": "standard",
        "text": "In a loudspeaker, unlike in a motor, the coil is not "
                "mounted on an axle to turn. What effect does reversing "
                "the current have on the coil, given that it cannot "
                "rotate?",
        "options": [
            {"text": "None at all, since a coil that cannot turn cannot "
                     "be pushed", "correct": False,
             "why": "A push does not require the ability to rotate; the "
                    "coil can still be pushed bodily, just not turned "
                    "round."},
            {"text": "It rotates the coil slightly before it jams",
             "correct": False,
             "why": "The coil is not mounted to rotate at all here, so "
                    "nothing turns even slightly."},
            {"text": "It reverses which pole the coil becomes, exactly the way a bar magnet's own ends would swap over", "correct": False,
             "why": "The coil is not acting as a fixed magnet here; "
                    "what reverses is the direction of the push it "
                    "feels from the field."},
            {"text": "It reverses the direction of the push on the "
                     "coil, moving it the other way instead of turning "
                     "it", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · harder ──────────────────────────────────
    {
        "id": "p10-05-h11",
        "band": "harder",
        "text": "A single-coil motor stalls exactly upright with the "
                "current still on. A second, identical motor never "
                "stalls, because it has three coils at different angles. "
                "Explain why the second one keeps going where the first "
                "one stops.",
        "options": [
            {"text": "While one coil sits upright with no turning "
                     "effect, the other two coils are at other angles "
                     "and still have a genuine turning effect between "
                     "them", "correct": True},
            {"text": "The three-coil motor's magnets are stronger",
             "correct": False,
             "why": "The magnets are described as unchanged here; the "
                    "difference is entirely in how the coils are "
                    "arranged."},
            {"text": "The three-coil motor has no upright position at "
                     "all", "correct": False,
             "why": "Each individual coil still passes through an "
                    "upright-equivalent position at some point; the fix "
                    "is that the others are not there at the same "
                    "moment."},
            {"text": "The three-coil motor's split ring never needs to reverse anything, since a coil that never sits upright needs no switching at all, however it is angled", "correct": False,
             "why": "A multi-coil motor's commutator still reverses "
                    "each coil's current at the right moment; it has "
                    "more segments, not none at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h12",
        "band": "harder",
        "text": "At 0.5 A the turning effect reads 13 against a friction "
                "of about 15. A student proposes tripling the current to "
                "1.5 A, expecting the turning effect to roughly triple "
                "as well. Given that 1.0 A reads 25 and 2.0 A reads 50, "
                "is the student's expectation reasonable?",
        "options": [
            {"text": "No — turning effect does not depend on current in "
                     "any simple way", "correct": False,
             "why": "The pattern given (0.5→13, 1.0→25, 2.0→50, 4.0→100) "
                    "is close to proportional; doubling the current is "
                    "close to doubling the reading each time."},
            {"text": "Roughly, yes — the readings given roughly double "
                     "each time the current doubles, so 1.5 A landing "
                     "somewhere around 35–40 fits that pattern",
             "correct": True},
            {"text": "No — the turning effect would fall, since higher "
                     "currents overheat the coil", "correct": False,
             "why": "Overheating is a real practical concern but is not "
                    "what the bench's own readings show; here, a bigger "
                    "current reads a bigger turning effect each time."},
            {"text": "Yes, exactly — the readings show turning effect is always exactly three times the current in amps, however large or small that current happens to be",
             "correct": False,
             "why": "The readings do not fit a fixed 'times three' "
                    "rule; 1.0 A reads 25, not 3, so the relationship is "
                    "proportional to current but with a different "
                    "scale."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h13",
        "band": "harder",
        "text": "A motor is fitted with a split ring but a fault means "
                "the current briefly stops reaching the coil for an "
                "instant at every reversal, rather than switching "
                "smoothly. What is the most likely result, compared "
                "with a fault-free motor?",
        "options": [
            {"text": "It runs completely smoothly, since a momentary gap makes no difference to how the coil feels the push", "correct": False,
             "why": "A gap at every single reversal, many times a "
                    "second, would be expected to make the motor's "
                    "turning noticeably less smooth, not identical to a "
                    "fault-free one."},
            {"text": "It reverses direction completely", "correct": False,
             "why": "A brief gap in current does not reverse anything; "
                    "the current still switches the same way each time, "
                    "just with an interruption."},
            {"text": "It runs, but less smoothly, with a small check in "
                     "its turning at every reversal", "correct": True},
            {"text": "It stops permanently the first time the fault "
                     "occurs", "correct": False,
             "why": "A brief gap at one reversal does not stop the coil "
                    "for good; the coil keeps moving on its own momentum "
                    "and the current resumes on the next contact."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h14",
        "band": "harder",
        "text": "A generator's coil is turned steadily by hand. A "
                "student expects a steady, unchanging voltage to appear "
                "at the two brushes, just as a battery gives a steady "
                "voltage. Why might they be wrong?",
        "options": [
            {"text": "Turning a coil by hand can never produce any "
                     "voltage at all", "correct": False,
             "why": "Turning a coil through a magnetic field does "
                    "produce a voltage; that is exactly the generator "
                    "effect."},
            {"text": "The magnets would need to be turned as well as "
                     "the coil", "correct": False,
             "why": "The magnets stay fixed; only the coil needs to "
                    "move through their field to produce a voltage."},
            {"text": "The brushes only work when a current is fed in, not when one is generated by the coil's own motion through the field", "correct": False,
             "why": "The brushes are simply fixed electrical contacts; "
                    "they work the same way whether current is being "
                    "fed in or drawn out."},
            {"text": "The push on the charge in the coil changes as the "
                     "coil's position changes, so the voltage rises and "
                     "falls rather than staying constant", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h15",
        "band": "harder",
        "text": "A cordless drill's forward/reverse switch is examined, "
                "and it is found that reversing it swaps only two of the "
                "four wires between the battery and the motor. Why is "
                "that enough to reverse the motor's direction?",
        "options": [
            {"text": "Swapping which two wires connect to which battery "
                     "terminal reverses the direction the current flows "
                     "through the coil, which is all that is needed",
             "correct": True},
            {"text": "It physically turns the magnets round inside the case, using a small motor built into the switch itself", "correct": False,
             "why": "The switch has no mechanical connection to the "
                    "magnets; only the current path is being changed."},
            {"text": "It disconnects the split ring temporarily",
             "correct": False,
             "why": "The split ring stays connected and keeps doing its "
                    "usual job of reversing each half turn; the switch "
                    "changes the overall current direction, on top of "
                    "that."},
            {"text": "It doubles the current flowing into the motor",
             "correct": False,
             "why": "Nothing about the size of the current changes when "
                    "the switch is thrown; only its overall direction "
                    "through the coil does."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h16",
        "band": "harder",
        "text": "A motor is running normally. A fault causes the "
                "magnets' field to become half as strong, with "
                "everything else unchanged. What is the effect on the "
                "turning effect, and does the motor still work at all?",
        "options": [
            {"text": "The turning effect doubles, and the motor speeds "
                     "up", "correct": False,
             "why": "A weaker field gives a smaller push, not a bigger "
                    "one."},
            {"text": "The turning effect roughly halves; it may still "
                     "work, but more slowly or not at all if the "
                     "smaller turning effect now falls below the "
                     "friction", "correct": True},
            {"text": "The turning effect is unaffected, since it only depends on the current flowing through the coil, whatever the magnets happen to be doing at the time", "correct": False,
             "why": "The field is one of the two things the push "
                    "depends on; halving it halves the push, current "
                    "unchanged or not."},
            {"text": "The motor reverses direction", "correct": False,
             "why": "A weaker field changes the size of the push, not "
                    "which way it points; direction needs the field's "
                    "or the current's direction to change, not just its "
                    "strength."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h17",
        "band": "harder",
        "text": "A three-coil motor is compared with a single-coil motor "
                "of the same current and magnets. The single-coil motor "
                "gives a turning effect that varies from 0 to 100 as it "
                "spins; the three-coil motor gives a combined turning "
                "effect that never falls much below about 87. Why is "
                "the three-coil motor's minimum so much higher?",
        "options": [
            {"text": "Its magnets are three times as strong",
             "correct": False,
             "why": "The magnets are described as the same; the "
                    "difference comes entirely from having three coils "
                    "at different angles instead of one."},
            {"text": "Its current is three times as large", "correct": False,
             "why": "The current is stated to be the same; what differs "
                    "is how many coils are sharing the work of turning "
                    "it."},
            {"text": "Whenever one coil is near its weakest position, "
                     "the other two are near stronger positions of "
                     "their own, so their combined effect never falls "
                     "as low as a single coil's does", "correct": True},
            {"text": "It has no upright-equivalent position at all, for any of its three coils, however the whole arrangement is angled", "correct": False,
             "why": "Each individual coil still passes through its own "
                    "weakest position at some point; what changes is "
                    "that the others are not there at the same moment."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h18",
        "band": "harder",
        "text": "A motor's coil and its magnets are BOTH reversed, and "
                "at the same time its current is also doubled. Compared "
                "with the original, unreversed, un-doubled motor, what "
                "happens?",
        "options": [
            {"text": "It turns the opposite way, at the same speed",
             "correct": False,
             "why": "Reversing both the current's direction and the "
                    "magnets cancels out as far as direction goes; "
                    "direction is unchanged here, only the size of the "
                    "current has altered."},
            {"text": "It stops completely, since three changes together are too many for the coil to keep responding to", "correct": False,
             "why": "There is no limit here on the number of changes; "
                    "each one can be reasoned through on its own and "
                    "combined."},
            {"text": "It turns the opposite way, twice as fast",
             "correct": False,
             "why": "The two reversals cancel each other out for "
                    "direction, leaving the direction the same as the "
                    "original — only the speed has changed here, from "
                    "the doubled current."},
            {"text": "It turns the same way as the original, but with "
                     "roughly twice the turning effect, because the two "
                     "reversals cancel and the doubled current adds its "
                     "own increase", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h19",
        "band": "harder",
        "text": "A motor is deliberately built with its coil wound the "
                "opposite way round compared with a standard design, so "
                "the current runs the reverse way along each side "
                "compared with normal — but the magnets and the "
                "external current direction are both left exactly as in "
                "the standard design. What would you expect?",
        "options": [
            {"text": "It turns the opposite way to the standard motor, "
                     "since reversing which way the coil is wound is "
                     "equivalent to reversing the current's effective "
                     "direction through it", "correct": True},
            {"text": "It turns exactly like the standard motor, since the external current direction has not changed anywhere along the supply wires",
             "correct": False,
             "why": "The winding direction changes which way the "
                    "current effectively runs relative to the magnets, "
                    "even with the external supply connections "
                    "unchanged."},
            {"text": "It does not turn at all, since a reverse-wound "
                     "coil cannot carry a current", "correct": False,
             "why": "A reverse-wound coil carries current perfectly "
                    "well; what changes is the direction of the push it "
                    "experiences, not whether current flows."},
            {"text": "It turns twice as fast, since reversing the "
                     "winding is like doubling the current",
             "correct": False,
             "why": "Reversing the winding changes the direction of the "
                    "effective push, not its size; speed is set by the "
                    "current, which is unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h20",
        "band": "harder",
        "text": "A student argues that because reversing the current "
                "reverses a motor's direction, and reversing the "
                "magnets also reverses it, doing BOTH must reverse it "
                "'twice as hard' — running it backwards at higher "
                "torque. What is the flaw in this argument?",
        "options": [
            {"text": "Reversing the current and reversing the magnets "
                     "are actually the same action, so nothing changes "
                     "at all", "correct": False,
             "why": "They are two genuinely different actions — one "
                    "changes the current's direction, the other the "
                    "field's — that happen to combine to leave the "
                    "direction as it was."},
            {"text": "Each reversal flips the direction once; two flips "
                     "return the direction to where it started, rather "
                     "than compounding into something 'more reversed'",
             "correct": True},
            {"text": "Torque cannot be affected by direction, only by "
                     "current size, so the whole question is "
                     "meaningless", "correct": False,
             "why": "The question is really about direction, not the "
                    "size of the turning effect, and direction genuinely "
                    "is affected by these reversals — just not in the "
                    "way the student thinks."},
            {"text": "The magnets cannot actually be reversed once fitted, so the second half of the claim is impossible in practice, regardless of how the argument about current is framed", "correct": False,
             "why": "The magnets can be turned round physically; the "
                    "flaw in the reasoning is about how the two "
                    "reversals combine, not about whether the magnets "
                    "can be moved at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h21",
        "band": "harder",
        "text": "A bicycle dynamo lights a lamp more brightly the faster "
                "the wheel is turned. Using the idea that a generator's "
                "voltage comes from moving a wire through a field, "
                "explain why speed matters.",
        "options": [
            {"text": "A faster wheel makes the magnets inside the "
                     "dynamo stronger", "correct": False,
             "why": "The magnets are permanent and their strength does "
                    "not change with how fast they are turned past the "
                    "coil."},
            {"text": "A faster wheel means more current is fed into the "
                     "dynamo from the bicycle's battery", "correct": False,
             "why": "A dynamo has no battery feeding it; it generates "
                    "its own voltage from the turning, and a bicycle "
                    "has no battery supplying it either."},
            {"text": "Turning the coil through the field faster pushes "
                     "the charge along more strongly each moment, "
                     "giving a bigger voltage", "correct": True},
            {"text": "A faster wheel reverses the dynamo's split ring more often, which is read as extra voltage by whatever is measuring it at the lamp",
             "correct": False,
             "why": "More frequent reversal changes how quickly the "
                    "voltage's direction alternates, not directly how "
                    "large it is at any instant."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h22",
        "band": "harder",
        "text": "A three-coil motor's commutator has one of its three "
                "segments wired to the wrong brush by mistake, so that "
                "one coil's current is never reversed at the right "
                "moment, though the other two coils work correctly. "
                "What would you expect to observe?",
        "options": [
            {"text": "The whole motor fails to turn at all", "correct": False,
             "why": "The other two coils are unaffected and continue to "
                    "provide a correct turning effect between them; the "
                    "fault affects only the one segment's coil."},
            {"text": "The motor runs faster than normal, since one coil is contributing extra force on top of what the other two already provide", "correct": False,
             "why": "A coil whose current is not reversed at the right "
                    "moment ends up fighting the rotation for part of "
                    "each turn, rather than adding a helpful extra "
                    "push."},
            {"text": "The magnets lose their field entirely", "correct": False,
             "why": "The magnets are unaffected by anything happening "
                    "at the commutator; only the current in the coils "
                    "is switched there."},
            {"text": "The motor still turns, driven mainly by the other "
                     "two coils, but runs a little less smoothly "
                     "because the faulty coil sometimes works against "
                     "the turning", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h23",
        "band": "harder",
        "text": "A motor is running with a current of 2.0 A, giving a "
                "turning effect of 50 against a friction of about 15. "
                "The current is then reduced in steps: 1.5 A, 1.0 A, "
                "0.5 A. At roughly which of these currents would the "
                "motor be expected to stop turning?",
        "options": [
            {"text": "Around 0.5 A, since the readings given show the "
                     "turning effect there (about 13) already falls "
                     "below the friction of 15", "correct": True},
            {"text": "Around 1.5 A, since that is roughly halfway between the given values of 1.0 A and 2.0 A shown on the bench's own scale", "correct": False,
             "why": "Halfway between 1.0 A (25) and 2.0 A (50) still "
                    "gives a turning effect comfortably above the "
                    "friction of 15."},
            {"text": "It never stops, however low the current goes",
             "correct": False,
             "why": "Given readings show the turning effect falling "
                    "well below the friction of about 15 once the "
                    "current is small enough, at which point it "
                    "stops."},
            {"text": "Around 1.0 A, since that is the middle value in "
                     "the list", "correct": False,
             "why": "1.0 A gives a turning effect of about 25, still "
                    "comfortably above the friction of 15."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h24",
        "band": "harder",
        "text": "A student claims that a motor and a generator are "
                "'completely different machines' because one uses "
                "electricity to move and the other makes electricity "
                "from movement. Evaluate this claim using what the "
                "lesson says about running a motor backwards.",
        "options": [
            {"text": "The claim is correct, since the two machines have entirely different parts inside them, built from scratch for their own separate jobs", "correct": False,
             "why": "The lesson describes a generator as the same "
                    "machine — coil, magnets, split ring and brushes — "
                    "simply driven the other way round."},
            {"text": "The claim is largely wrong: the lesson describes "
                     "a generator as the same machine as a motor, run "
                     "the other way round, using the same coil, "
                     "magnets, split ring and brushes", "correct": True},
            {"text": "The claim is correct, since a generator needs no "
                     "magnets at all", "correct": False,
             "why": "A generator needs the same magnets as a motor; the "
                    "field they provide is exactly what the moving coil "
                    "needs to be pushed against, or to push charge "
                    "along."},
            {"text": "The claim is correct, since a motor cannot be "
                     "turned by hand", "correct": False,
             "why": "The lesson states directly that turning the coil "
                    "by hand makes a voltage appear, which is exactly "
                    "turning a motor by hand and getting the generator "
                    "effect."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h25",
        "band": "harder",
        "text": "A single-coil motor and a three-coil motor are both "
                "compared at the same current and the same magnets. A "
                "student says the three-coil motor must be exactly "
                "three times as powerful at every instant. Is this "
                "exactly right?",
        "options": [
            {"text": "Yes, since three coils always triple whatever a single coil manages at every angle, with no exceptions anywhere around the turn", "correct": False,
             "why": "Because each coil is at a different angle at any "
                    "instant, they do not all give the same turning "
                    "effect as each other at the same moment, so a "
                    "simple triple does not hold exactly at every "
                    "angle."},
            {"text": "No, because the three-coil version has no split "
                     "ring at all", "correct": False,
             "why": "The three-coil version still has a commutator, "
                    "with one segment for each coil, not none at all."},
            {"text": "Not exactly — at any instant the three coils are "
                     "at different angles and so contribute different "
                     "amounts, though their combined effect stays high "
                     "because at least one is always well placed",
             "correct": True},
            {"text": "No, because only one of the three coils is ever "
                     "connected to the current at once", "correct": False,
             "why": "All three coils can be connected through their own "
                    "commutator segments; the arrangement is what keeps "
                    "the overall turning effect from falling to zero, "
                    "not disconnecting two of them."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h26",
        "band": "harder",
        "text": "A motor's coil and a generator's coil both sit between "
                "two fixed magnets and both have a split ring and "
                "brushes. Explain, using the current and the field, why "
                "one experiences a force that turns it and the other "
                "produces a voltage instead.",
        "options": [
            {"text": "A motor's coil is made of a different metal from "
                     "a generator's coil", "correct": False,
             "why": "The same kind of coil — usually copper — can do "
                    "either job; the difference is not the material."},
            {"text": "A generator's magnets are electromagnets, while a "
                     "motor's are permanent", "correct": False,
             "why": "Both typically use permanent magnets to provide "
                    "the fixed field; that is not what separates the "
                    "two effects."},
            {"text": "A generator has no current in its coil at all, so nothing can be compared between the two machines in the way the question asks", "correct": False,
             "why": "A generator's coil does carry a current, once it "
                    "starts turning and producing a voltage; the "
                    "comparison is still meaningful."},
            {"text": "In a motor a current is fed in and the field "
                     "pushes the coil round; in a generator the coil is "
                     "turned and that motion through the field pushes "
                     "charge along it instead, which is read as a "
                     "voltage", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h27",
        "band": "harder",
        "text": "A motor's split ring is redesigned with the current "
                "reversed at a slightly wrong moment — a little before "
                "the coil actually reaches the upright position, rather "
                "than exactly at it. What effect would this have?",
        "options": [
            {"text": "The coil would be pushed backwards briefly just "
                     "before each reversal, giving a less smooth "
                     "turning effect than a perfectly timed switch",
             "correct": True},
            {"text": "The motor would run exactly as smoothly as before, since timing the switch makes no real difference to how the pushes add up around the whole turn", "correct": False,
             "why": "Timing the reversal to the exact upright position "
                    "is what keeps the pushes always working with the "
                    "rotation; switching early briefly works against "
                    "it instead."},
            {"text": "The motor would spin twice as fast", "correct": False,
             "why": "Mistiming the switch does not add extra current or "
                    "turns; if anything it makes the motion less "
                    "smooth, not faster."},
            {"text": "The motor would stop completely at the first "
                     "mistimed switch", "correct": False,
             "why": "A slightly early switch briefly works against the "
                    "rotation rather than stopping it outright; the "
                    "coil's own motion carries it past that point."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h28",
        "band": "harder",
        "text": "A motor is run at a fixed current, and its magnets are "
                "then replaced with a pair only two-thirds as strong. "
                "Using the idea that both current and field set the "
                "size of the push, predict roughly what happens to the "
                "turning effect, and whether the motor still runs.",
        "options": [
            {"text": "The turning effect stays the same, since only the "
                     "current sets its size", "correct": False,
             "why": "The field is the other half of what sets the "
                    "push's size; weakening it should weaken the "
                    "turning effect too."},
            {"text": "The turning effect falls to roughly two-thirds of "
                     "what it was; the motor may still run, but could "
                     "stall if that smaller effect no longer beats the "
                     "friction", "correct": True},
            {"text": "The turning effect reverses direction", "correct": False,
             "why": "Weakening the magnets changes the size of the "
                    "push, not which way it points; direction needs a "
                    "directional change, not just a weaker field."},
            {"text": "The turning effect increases, since a weaker field lets the current act more freely, without anything holding it back at all",
             "correct": False,
             "why": "A weaker field gives a smaller push on the "
                    "current, not a bigger one."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h29",
        "band": "harder",
        "text": "A student wants to build the fastest possible small "
                "motor using one fixed size of coil and one fixed pair "
                "of magnets, and can only choose the current. Using the "
                "bench's own figures (0.5 A → 13, 1.0 A → 25, 2.0 A → "
                "50, 4.0 A → 100, friction ≈ 15), which current gives "
                "the largest USABLE turning effect once friction is "
                "accounted for?",
        "options": [
            {"text": "0.5 A, since it is the gentlest setting and "
                     "causes the least wear", "correct": False,
             "why": "At 0.5 A the turning effect of 13 does not even "
                    "beat the friction of about 15, so the motor would "
                    "not turn at all."},
            {"text": "1.0 A, since that is enough to beat the friction with the smallest current that will get the motor moving at all", "correct": False,
             "why": "1.0 A does beat the friction, but 4.0 A gives a "
                    "far larger usable turning effect once the fixed "
                    "friction is subtracted."},
            {"text": "4.0 A, since it gives by far the largest turning "
                     "effect, and friction is a fixed amount subtracted "
                     "from whichever current is chosen", "correct": True},
            {"text": "It cannot be decided, since friction is not a "
                     "fixed value", "correct": False,
             "why": "Friction at the axle is described as one fixed "
                    "amount here, about 15, whatever the current; it is "
                    "the turning effect that changes with current."},
        ],
        "figure": None,
    },
    {
        "id": "p10-05-h30",
        "band": "harder",
        "text": "A generator and a motor share an identical coil, "
                "identical magnets, an identical split ring and "
                "identical brushes. A student says that means the two "
                "machines must always produce or need exactly the same "
                "voltage or current when compared at the same speed or "
                "current respectively. Evaluate this claim.",
        "options": [
            {"text": "The claim is correct, since sharing every part guarantees identical numbers in both directions, with nothing left to differ",
             "correct": False,
             "why": "Sharing the same parts explains why the same "
                    "machine can do either job, but it does not by "
                    "itself guarantee that a given speed as a generator "
                    "produces a voltage numerically equal to whatever "
                    "current would be needed to spin it that fast as a "
                    "motor."},
            {"text": "The claim is wrong, because a generator cannot "
                     "use the same magnets as a motor", "correct": False,
             "why": "The lesson describes exactly the same magnets "
                    "doing both jobs; that is not the flaw in the "
                    "claim."},
            {"text": "The claim is wrong, because a generator has no "
                     "split ring", "correct": False,
             "why": "A generator keeps the same split ring, still "
                    "switching the connection every half turn so that "
                    "the voltage always pushes current out the same way "
                    "at the brushes."},
            {"text": "The claim goes further than the lesson supports: "
                     "sharing every part explains why one machine can "
                     "do either job, but no comparison of the actual "
                     "sizes involved is given here", "correct": True},
        ],
        "figure": None,
    },
]
