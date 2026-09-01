"""P10 lesson 04 — Electromagnets: twelve questions (MRB-223).

Written against Design's page. The scrapyard crane, the four-control bench,
the four jobs and the four rungs are hers.

The discriminations, in the order the lesson builds them:

  · a CURRENT makes the field, and the coil is what stacks it up;
  · the core responds to the coil rather than the other way round (`MAG-13`),
    and a former that is not magnetic does nothing at all;
  · turns and current are two separate reasons, not one (`MAG-14`);
  · switching off removes the field completely — it does not fade (`MAG-15`)
    and it does not stay (`MAG-16`) — which is the harder band.

⚠️ NO VALUE IN TESLA APPEARS IN ANY QUESTION, and no force in newtons. Ruled
for the whole unit: the only numbers here are turn counts, currents in amps
and counts of paper clips.

⚠️ POSITION IS AUTHORED — 3,0,1,2 · 0,1,2,3 · 1,2,3,0, three of each.

⚠️ NO RUNG IS RESTATED. The ladder owns the which-change-will-not-help
question, the opened switch, the crane-versus-permanent-magnet explanation and
the fire door; nothing here reuses any of the four.
"""

UNIT = "P10"
LESSON = "electromagnets"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p10-04-e01",
        "band": "easier",
        "text": "What has to be happening for an electromagnet to be magnetic "
                "at all?",
        "options": [
            {"text": "The iron core has to have been magnetised beforehand",
             "correct": False,
             "why": "The coil magnetises the core, every time it is switched "
                    "on. Nothing has to be prepared first."},
            {"text": "The coil has to be moving through the air",
             "correct": False,
             "why": "It works perfectly well bolted to a wall. Nothing has to "
                    "move."},
            {"text": "The coil has to be near a permanent magnet",
             "correct": False,
             "why": "An electromagnet needs no other magnet anywhere near it. "
                    "It makes its own field."},
            {"text": "A current has to be flowing through the coil",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e02",
        "band": "easier",
        "text": "What is a solenoid?",
        "options": [
            {"text": "A coil of wire", "correct": True},
            {"text": "A bar of soft iron", "correct": False,
             "why": "The iron is the core. The solenoid is the wire wound "
                    "round it, and a solenoid works with no core at all."},
            {"text": "A switch that reverses a current", "correct": False,
             "why": "Reversing the current is done at the supply. A solenoid "
                    "is the coil itself."},
            {"text": "The magnetic field a current makes", "correct": False,
             "why": "The solenoid is the thing that makes the field, not the "
                    "field."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e03",
        "band": "easier",
        "text": "What shape is the magnetic field outside a solenoid?",
        "options": [
            {"text": "A set of rings wrapped round the outside of the coil",
             "correct": False,
             "why": "Rings are the shape round a single straight wire. Wind "
                    "it into a coil and the shape changes."},
            {"text": "The same shape as a bar magnet's field",
             "correct": True},
            {"text": "A ball, spreading out equally in every direction",
             "correct": False,
             "why": "A magnetic field never spreads out equally. It always "
                    "has a north end and a south end."},
            {"text": "There is no field outside a solenoid — it is all inside "
                     "the coil", "correct": False,
             "why": "There is field outside, and it is what lifts the paper "
                    "clips hanging off the end."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e04",
        "band": "easier",
        "text": "What does putting a soft iron core down the middle of a coil "
                "do?",
        "options": [
            {"text": "It stops the coil overheating", "correct": False,
             "why": "It does nothing about heat. What it changes is the "
                    "strength of the field."},
            {"text": "It stores the magnetism so the coil can be switched off",
             "correct": False,
             "why": "Nothing is stored. Soft iron loses its magnetism the "
                    "instant the current stops."},
            {"text": "It makes the field many times stronger", "correct": True},
            {"text": "It reverses the north and south ends of the coil",
             "correct": False,
             "why": "The ends are set by which way the current runs. A core "
                    "makes the field bigger, not different in direction."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p10-04-s01",
        "band": "standard",
        "text": "A coil is connected to a supply with nothing at all down the "
                "middle of it. Is there a magnetic field?",
        "options": [
            {"text": "Yes — a real one, and a compass at either end finds a "
                     "definite pole", "correct": True},
            {"text": "No — a coil with nothing down the middle is just a "
                     "length of wire",
             "correct": False,
             "why": "Wound into a coil it is a magnet whenever a current runs "
                    "through it. The core only multiplies what is already "
                    "there."},
            {"text": "No — the field cannot form without a piece of iron to "
                     "form it in",
             "correct": False,
             "why": "The current makes the field. Iron responds to it, which "
                    "is a different job."},
            {"text": "Only while the coil is being wound, and never once it "
                     "is finished", "correct": False,
             "why": "Winding it does nothing. Switching the current on is "
                    "what matters."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s02",
        "band": "standard",
        "text": "The number of turns on a coil is doubled and the current "
                "through it is kept the same. What happens to the field?",
        "options": [
            {"text": "It halves, because the current is shared between twice "
                     "as many turns", "correct": False,
             "why": "The same current runs through every turn, one after "
                    "another. Nothing is shared out."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "It roughly doubles, as each turn adds its own "
                     "field", "correct": True},
            {"text": "It stays the same, because the current has not changed",
             "correct": False,
             "why": "The current is only half the story. Each turn adds its "
                    "own field in the same place."},
            {"text": "It grows enormously, far more than doubling",
             "correct": False,
             "why": "That is what dropping an iron core in does. Doubling the "
                    "turns roughly doubles the field, no more."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s03",
        "band": "standard",
        "text": "The two leads of an electromagnet are swapped over at the "
                "supply, so the current runs the other way round the coil. "
                "What changes?",
        "options": [
            {"text": "Nothing at all — a magnet works the same either way",
             "correct": False,
             "why": "Something does change. Hold a compass at one end before "
                    "and after and it turns right round."},
            {"text": "The field becomes weaker, because the current is now "
                     "working against the coil", "correct": False,
             "why": "There is nothing for it to work against. The same "
                    "current in the other direction gives the same size of "
                    "field."},
            {"text": "The north and south ends swap over, and the strength "
                     "stays the same", "correct": True},
            {"text": "The coil stops being magnetic until the leads are put "
                     "back", "correct": False,
             "why": "A current in either direction makes a field. Only "
                    "stopping the current stops the magnetism."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s04",
        "band": "standard",
        "text": "A coil that was empty is rewound on a plastic former, with "
                "the same number of turns and the same current. What happens "
                "to the field?",
        "options": [
            {"text": "It gets much stronger, because the former holds the "
                     "turns closer together", "correct": False,
             "why": "Tidier winding does not change what the field is made "
                    "of. The plastic itself contributes nothing."},
            {"text": "It gets weaker, because the plastic gets in the way of "
                     "the field", "correct": False,
             "why": "Nothing gets in the way of a magnetic field. It passes "
                    "straight through plastic."},
            {"text": "It reverses, because the former is an insulator",
             "correct": False,
             "why": "Insulating the wire matters for the circuit and not for "
                    "the direction of the field."},
            {"text": "Nothing — plastic is not magnetic, so it does the same "
                     "as no core at all", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p10-04-h01",
        "band": "harder",
        "text": "A student winds twice as much wire onto a coil, leaving the "
                "supply alone. They measure the current and find it has gone "
                "slightly DOWN — yet the electromagnet is clearly stronger. "
                "Explain how both can be true.",
        "options": [
            {"text": "The meter must be wrong, because more wire always "
                     "carries more current, whatever it is wound onto",
             "correct": False,
             "why": "More wire is more resistance, so slightly less current "
                    "is exactly what you would expect."},
            {"text": "Each extra turn adds its own field in the same place, "
                     "and that outweighs the slightly smaller current",
             "correct": True},
            {"text": "The extra wire stores magnetism from earlier, so the "
                     "coil keeps some of what it had before",
             "correct": False,
             "why": "Nothing is stored anywhere. Switch off and the whole "
                    "field goes at once."},
            {"text": "The current is smaller but travels faster, so it does "
                     "the same job in less time than before", "correct": False,
             "why": "There is no speed here to trade against size. The field "
                    "depends on how much current, not on how quickly."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h02",
        "band": "harder",
        "text": "In an electric bell, the coil pulls an iron arm across — and "
                "moving the arm breaks the very circuit that made the coil "
                "magnetic. Why does the bell then ring over and over?",
        "options": [
            {"text": "The arm bounces off the bell and closes the circuit "
                     "again by chance", "correct": False,
             "why": "It is not chance. Breaking the circuit is what releases "
                    "the arm, every single time."},
            {"text": "The coil keeps enough magnetism to pull the arm a "
                     "second time before it fades", "correct": False,
             "why": "The field goes the instant the current stops. There is "
                    "nothing left over to pull with."},
            {"text": "The field goes, the arm springs back, that remakes the "
                     "circuit, and the whole thing repeats", "correct": True},
            {"text": "The current reverses each time the arm moves, so the "
                     "coil pushes and pulls alternately", "correct": False,
             "why": "Reversing the current would reverse the poles, and the "
                    "iron arm would still be attracted. What matters is that "
                    "the circuit is broken."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h03",
        "band": "harder",
        "text": "An electromagnet is built with a hardened steel core by "
                "mistake, instead of soft iron. It is switched on, lifts a "
                "load, and is then switched off. What is different?",
        "options": [
            {"text": "It never lifts the load at all, because steel cannot be "
                     "magnetised", "correct": False,
             "why": "Steel can certainly be magnetised — it is what permanent "
                    "magnets are made from. It is just harder to do and "
                    "harder to undo."},
            {"text": "It lifts more, because steel is stronger than iron",
             "correct": False,
             "why": "Being mechanically strong is a different property "
                    "entirely from being easy to magnetise."},
            {"text": "It works normally, because the core makes no difference "
                     "once the current is off", "correct": False,
             "why": "With soft iron that is right. With steel it is exactly "
                    "what goes wrong."},
            {"text": "Some magnetism stays in the core, so the load is not "
                     "cleanly released", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h04",
        "band": "harder",
        "text": "Two electromagnets have identical iron cores. One has 40 "
                "turns and carries 2.0 A; the other has 80 turns and carries "
                "1.0 A. How do their fields compare?",
        "options": [
            {"text": "They are about the same, because turns and current "
                     "count for the same amount", "correct": True},
            {"text": "The 80-turn one is stronger, because turns matter more "
                     "than current", "correct": False,
             "why": "Neither one matters more. Halving one while doubling the "
                    "other leaves the field where it was."},
            {"text": "The 40-turn one is stronger, because current matters "
                     "more than turns", "correct": False,
             "why": "Neither one matters more. Doubling the current does "
                    "exactly what doubling the turns does."},
            {"text": "It cannot be worked out without knowing how long each "
                     "coil is", "correct": False,
             "why": "The length of the coil is not one of the three things "
                    "the bench changes. Turns, current and core are."},
        ],
        "figure": None,
    },
]
