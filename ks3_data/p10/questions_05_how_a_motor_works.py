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
]
