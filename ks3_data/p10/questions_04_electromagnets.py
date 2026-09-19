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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p10-04-e05",
        "band": "easier",
        "text": "What makes a magnetic field around a wire?",
        "options": [
            {"text": "A current flowing through it", "correct": True},
            {"text": "The wire being made of copper", "correct": False,
             "why": "Copper is not magnetic; the field appears only when a "
                    "current runs."},
            {"text": "The wire being coiled up", "correct": False,
             "why": "Coiling concentrates the field, but a current is what "
                    "creates it in the first place."},
            {"text": "The wire being connected to earth", "correct": False,
             "why": "Earthing is about charge escaping and makes no field of "
                    "its own."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e06",
        "band": "easier",
        "text": "Which of these makes an electromagnet stronger?",
        "options": [
            {"text": "Using fewer turns of wire", "correct": False,
             "why": "Fewer turns means fewer fields adding together, so it "
                    "gets weaker."},
            {"text": "Using a smaller current", "correct": False,
             "why": "A smaller current makes a weaker field, not a stronger "
                    "one."},
            {"text": "Putting a soft iron core down the middle",
             "correct": True},
            {"text": "Replacing the iron core with a plastic one",
             "correct": False,
             "why": "Plastic is not magnetic, so it multiplies nothing — it "
                    "is no better than empty space."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e07",
        "band": "easier",
        "text": "What happens to an electromagnet's magnetism when the "
                "current is switched off?",
        "options": [
            {"text": "It fades away over several minutes", "correct": False,
             "why": "With a soft iron core it stops at the same instant the "
                    "current does."},
            {"text": "It goes completely, at once", "correct": True},
            {"text": "It stays, because the core has been magnetised for "
                     "good",
             "correct": False,
             "why": "Soft iron is chosen precisely because it lets go the "
                    "moment the current stops."},
            {"text": "It reverses and becomes the other way round",
             "correct": False,
             "why": "Reversing needs the current to run the other way, not to "
                    "stop."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e08",
        "band": "easier",
        "text": "Reversing the current through an electromagnet…",
        "options": [
            {"text": "swaps its north and south ends", "correct": True},
            {"text": "makes it stronger", "correct": False,
             "why": "The size of the current sets the strength; its direction "
                    "sets which end is which."},
            {"text": "switches it off completely", "correct": False,
             "why": "A current is still flowing, so a field is still made."},
            {"text": "makes no difference at all", "correct": False,
             "why": "A compass held nearby swings right round, which shows it "
                    "makes a large difference."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e09",
        "band": "easier",
        "text": "Why is soft iron used for an electromagnet's core rather "
                "than hardened steel?",
        "options": [
            {"text": "Because soft iron is cheaper", "correct": False,
             "why": "Cost is not the reason; what matters is what happens "
                    "when the current stops."},
            {"text": "Because soft iron lets go of its magnetism at "
                     "switch-off",
             "correct": True},
            {"text": "Because hardened steel cannot be magnetised in the "
                     "first place",
             "correct": False,
             "why": "Steel is magnetic — too much so, since it keeps its "
                    "magnetism afterwards."},
            {"text": "Because soft iron carries the current better",
             "correct": False,
             "why": "The current runs in the coil, not through the core."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e10",
        "band": "easier",
        "text": "The field outside a coil carrying a current has the same "
                "shape as the field of…",
        "options": [
            {"text": "a single straight wire", "correct": False,
             "why": "A straight wire's field is a set of circles round it, "
                    "which is a different shape."},
            {"text": "a bar magnet", "correct": True},
            {"text": "the Earth's core", "correct": False,
             "why": "That is itself bar-magnet shaped, but the coil's field "
                    "is described directly by the bar magnet."},
            {"text": "no magnet at all — a coil's field has no shape",
             "correct": False,
             "why": "It has a clear shape, with a north end and a south end "
                    "like any magnet."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p10-04-s05",
        "band": "standard",
        "text": "An electromagnet holds six paper clips. The current is "
                "doubled and nothing else is changed. What happens?",
        "options": [
            {"text": "It holds fewer clips, because the coil warms up",
             "correct": False,
             "why": "It does warm, but a larger current makes a stronger "
                    "field and holds more."},
            {"text": "It holds about the same, because the number of turns "
                     "has not changed",
             "correct": False,
             "why": "Turns and current both matter, and the current has "
                    "changed."},
            {"text": "It holds more clips than before", "correct": True},
            {"text": "It lets all the clips go, because the field reverses",
             "correct": False,
             "why": "Reversing needs the current to change DIRECTION, not to "
                    "grow."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s06",
        "band": "standard",
        "text": "A coil with an iron core lifts a chain of clips. The core is "
                "pulled out while the current still flows. What happens?",
        "options": [
            {"text": "Nothing changes, because the coil makes the field",
             "correct": False,
             "why": "The coil does make it, and the core multiplies it many "
                    "times over."},
            {"text": "The field disappears completely", "correct": False,
             "why": "The coil alone still makes a field — just a much weaker "
                    "one."},
            {"text": "The field gets much weaker, and most of the clips fall",
             "correct": True},
            {"text": "The field reverses and the clips are pushed away",
             "correct": False,
             "why": "Nothing about removing the core changes which way the "
                    "current runs."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s07",
        "band": "standard",
        "text": "Why does a scrapyard crane use an electromagnet rather than "
                "a very strong permanent magnet?",
        "options": [
            {"text": "Because an electromagnet is stronger than any permanent "
                     "magnet can be",
             "correct": False,
             "why": "Strength is not the point; being able to let go is."},
            {"text": "Because it can be switched off to drop the load",
             "correct": True},
            {"text": "Because a permanent magnet would attract aluminium too",
             "correct": False,
             "why": "Neither attracts aluminium; both act only on magnetic "
                    "materials."},
            {"text": "Because an electromagnet works without any current",
             "correct": False,
             "why": "It works only WITH a current, which is exactly what lets "
                    "it be turned off."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s08",
        "band": "standard",
        "text": "Two coils are identical except that one is wound on a soft "
                "iron rod and the other on a wooden one. Which is stronger?",
        "options": [
            {"text": "The wooden one, because wood does not resist the field",
             "correct": False,
             "why": "Wood does nothing at all; it behaves like empty space."},
            {"text": "The same, because the coils are identical",
             "correct": False,
             "why": "The coils are, but the core is part of what makes the "
                    "magnet."},
            {"text": "The iron one, by a large margin", "correct": True},
            {"text": "The iron one, but only very slightly", "correct": False,
             "why": "A soft iron core multiplies the field many times over, "
                    "which is a very large difference."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s09",
        "band": "standard",
        "text": "Which change would NOT make an electromagnet stronger?",
        "options": [
            {"text": "Adding many more turns of wire to the coil", "correct": False,
             "why": "More turns means more fields adding together, so it gets "
                    "stronger."},
            {"text": "Increasing the current", "correct": False,
             "why": "A larger current makes a stronger field."},
            {"text": "Fitting a soft iron core", "correct": False,
             "why": "The core multiplies the field many times over."},
            {"text": "Painting the coil a different colour", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s10",
        "band": "standard",
        "text": "A compass is held near the end of a working electromagnet "
                "and settles pointing at it. The current is then reversed. "
                "What does the compass do?",
        "options": [
            {"text": "Turns right round to point the other way",
             "correct": True},
            {"text": "Stays exactly as it was", "correct": False,
             "why": "The ends have swapped, so the needle must swing round to "
                    "match."},
            {"text": "Spins continuously while the current flows",
             "correct": False,
             "why": "It settles again in the new direction, just as it did in "
                    "the old one."},
            {"text": "Stops responding, because the field has been cancelled",
             "correct": False,
             "why": "The field is as strong as before; only its direction has "
                    "changed."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p10-04-h05",
        "band": "harder",
        "text": "A student says adding turns helps because more wire carries "
                "more current. What is wrong?",
        "options": [
            {"text": "Nothing — more wire really does carry more current",
             "correct": False,
             "why": "Adding wire raises the resistance, so if anything the "
                    "current falls."},
            {"text": "More wire lowers the current slightly; the gain is the "
                     "extra turns",
             "correct": True},
            {"text": "Adding turns makes no difference to the strength at "
                     "all",
             "correct": False,
             "why": "It makes a large difference — the fields of the turns "
                    "add up."},
            {"text": "Adding turns weakens the magnet, so the student has it "
                     "backwards",
             "correct": False,
             "why": "It strengthens it; the student's ANSWER is right and "
                    "their reason is not."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h06",
        "band": "harder",
        "text": "An electromagnet is built with a hardened steel core by "
                "mistake. It lifts a load, and the current is switched off. "
                "What happens?",
        "options": [
            {"text": "The load drops at once, as it would with iron",
             "correct": False,
             "why": "Hardened steel keeps its magnetism, so it does not let "
                    "go cleanly."},
            {"text": "Some of the load stays stuck, because the steel keeps "
                     "its magnetism",
             "correct": True},
            {"text": "Nothing was lifted in the first place, since steel "
                     "cannot be a core",
             "correct": False,
             "why": "Steel is magnetic and works as a core; the problem comes "
                    "at switch-off."},
            {"text": "The load is pushed away as the field reverses",
             "correct": False,
             "why": "Switching off does not reverse anything; it simply stops "
                    "driving the field."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h07",
        "band": "harder",
        "text": "Electromagnet A has 40 turns and 2.0 A. Electromagnet B has "
                "80 turns and 1.0 A. Their cores are identical. What would "
                "you expect?",
        "options": [
            {"text": "A is much stronger, because its current is larger",
             "correct": False,
             "why": "B has twice the turns, which compensates for its smaller "
                    "current."},
            {"text": "B is much stronger, because it has more turns",
             "correct": False,
             "why": "A has twice the current, which compensates for its "
                    "smaller number of turns."},
            {"text": "They are close to each other in strength",
             "correct": True},
            {"text": "Neither works, because the currents differ",
             "correct": False,
             "why": "Both work perfectly well; the question is how their "
                    "strengths compare."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h08",
        "band": "harder",
        "text": "A fire door is held open by an electromagnet and closes when "
                "the alarm sounds. Why is that safer than a mechanical "
                "catch?",
        "options": [
            {"text": "Because an electromagnet is stronger than a catch",
             "correct": False,
             "why": "Strength is not the safety argument; what happens on a "
                    "power failure is."},
            {"text": "Because losing power releases the door rather than "
                     "jamming it",
             "correct": True},
            {"text": "Because a catch cannot hold a fire door open at all",
             "correct": False,
             "why": "A catch holds it perfectly well — until someone has to "
                    "release it."},
            {"text": "Because the magnet detects smoke directly",
             "correct": False,
             "why": "The alarm detects the smoke; the magnet only lets go "
                    "when its current stops."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h09",
        "band": "harder",
        "text": "In an electric bell the coil pulls an iron arm across, and "
                "moving the arm breaks the circuit. What happens next?",
        "options": [
            {"text": "The bell stops for good, because the circuit is broken",
             "correct": False,
             "why": "The arm springs back, which remakes the circuit, and the "
                    "cycle repeats."},
            {"text": "The arm springs back, the circuit remakes, and it all "
                     "repeats",
             "correct": True},
            {"text": "The arm stays across, because the iron keeps its "
                     "magnetism for good",
             "correct": False,
             "why": "The core is soft iron, chosen so it lets go the moment "
                    "the current stops."},
            {"text": "The current reverses and the arm is pushed the other "
                     "way",
             "correct": False,
             "why": "Breaking a circuit stops the current; it does not turn "
                    "it round."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h10",
        "band": "harder",
        "text": "Name one thing an electromagnet can do that no permanent "
                "magnet can.",
        "options": [
            {"text": "Attract iron and steel", "correct": False,
             "why": "Any magnet does that; it is not what separates the "
                    "two."},
            {"text": "Have a north end at one side and a south end at the "
                     "other", "correct": False,
             "why": "Both have two ends, and neither can have just one."},
            {"text": "Have its strength and poles changed by a switch",
             "correct": True},
            {"text": "Act across a gap without touching", "correct": False,
             "why": "Every magnet acts across a gap; that is what a field "
                    "means."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · easier ──────────────────────────────────
    {
        "id": "p10-04-e11",
        "band": "easier",
        "text": "A single straight wire is carrying a current, with no coil "
                "and no core. Is there a magnetic field around it?",
        "options": [
            {"text": "No — a field only appears once the wire is wound into "
                     "a coil", "correct": False,
             "why": "A straight wire has a field too; winding it into a coil "
                    "only changes its shape and adds the turns together, it "
                    "does not create it from nothing."},
            {"text": "Yes, but it is weak, and you need a sensitive compass "
                     "close against the wire to detect it", "correct": True},
            {"text": "No — a wire needs an iron core before any field can "
                     "form", "correct": False,
             "why": "Iron is not required at all. A current makes a field "
                    "in a coil or in a plain straight wire; the core only "
                    "responds to a field that is already there."},
            {"text": "Yes, and it is exactly as strong as the same wire "
                     "would be once wound into a coil, so winding it up "
                     "would achieve nothing at all", "correct": False,
             "why": "Winding the same wire into a coil makes many turns add "
                    "their fields together in the same place, which is a "
                    "real gain, not nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e12",
        "band": "easier",
        "text": "In an electromagnet, which part actually creates the "
                "magnetic field?",
        "options": [
            {"text": "The iron core, because it is the only magnetic "
                     "material present", "correct": False,
             "why": "Iron is not the only magnetic material present: soft "
                    "iron works because a coil's field magnetises it. Take "
                    "the core out and the coil alone still makes a field."},
            {"text": "The plastic former, once it has been wound with wire",
             "correct": False,
             "why": "Plastic is not magnetic and has no field of its own. "
                    "It only holds the wire in place."},
            {"text": "The current flowing through the coil", "correct": True},
            {"text": "The switch, once it has been closed", "correct": False,
             "why": "A switch only allows or stops the current. It does not "
                    "itself produce anything magnetic."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e13",
        "band": "easier",
        "text": "What does a relay use a small current for?",
        "options": [
            {"text": "To pull an iron arm across and close a much bigger "
                     "circuit", "correct": True},
            {"text": "To directly power a large motor or heater",
             "correct": False,
             "why": "The small circuit never carries the large device's own "
                    "current; it only operates a switch for it."},
            {"text": "To recharge the battery that runs the bigger circuit "
                     "between uses", "correct": False,
             "why": "A relay switches a circuit; it does not charge "
                    "anything."},
            {"text": "To measure how much current the bigger circuit needs",
             "correct": False,
             "why": "A relay is a switch operated by magnetism, not a "
                    "measuring instrument."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e14",
        "band": "easier",
        "text": "A car's ignition key turns a small circuit on, which then "
                "starts the much bigger starter motor circuit. What is "
                "doing that job?",
        "options": [
            {"text": "The starter motor's own magnets, switched on directly "
                     "by the key", "correct": False,
             "why": "The starter motor's magnets are permanent and are not "
                    "switched by the key at all; something else closes its "
                    "circuit."},
            {"text": "A solenoid making a permanent magnetic field that "
                     "never turns off, however the key happens to be "
                     "turned", "correct": False,
             "why": "The whole point is that the field is switched, on "
                    "demand from the key — not permanent."},
            {"text": "The car's battery, connected straight to the starter "
                     "motor", "correct": False,
             "why": "The battery supplies the current, but something has to "
                    "close that big circuit first, and a small key current "
                    "cannot do that directly."},
            {"text": "A relay: the key's small current pulls an iron arm "
                     "that closes the starter motor's circuit",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e15",
        "band": "easier",
        "text": "An electromagnetic door lock holds a fire door shut. The "
                "power to the building is cut. What happens to the door?",
        "options": [
            {"text": "It stays locked shut, because the iron core keeps "
                     "its magnetism for a good while afterwards",
             "correct": False,
             "why": "The core is soft iron chosen precisely because it does "
                    "not keep its magnetism once the current stops."},
            {"text": "It is released, because the field goes the instant "
                     "the current stops", "correct": True},
            {"text": "It locks even more tightly, because cutting the "
                     "power reverses the current through the coil",
             "correct": False,
             "why": "Cutting the power stops the current; it does not "
                    "reverse it."},
            {"text": "Nothing changes until someone switches the lock off "
                     "by hand", "correct": False,
             "why": "The lock needs no one present. Losing the current "
                    "alone is enough to release it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e16",
        "band": "easier",
        "text": "A loudspeaker cone is pushed in and out by…",
        "options": [
            {"text": "a coil carrying a current that keeps changing, "
                     "sitting in a permanent magnet's field", "correct": True},
            {"text": "a permanent magnet fixed inside the case that "
                     "physically vibrates back and forth", "correct": False,
             "why": "The magnet stays fixed in a loudspeaker. What moves is "
                    "the coil attached to the cone."},
            {"text": "an iron core being switched on and off by hand",
             "correct": False,
             "why": "Nothing is switched by hand; the current itself "
                    "changes thousands of times a second."},
            {"text": "the cone's own weight, swinging under gravity",
             "correct": False,
             "why": "Gravity plays no part. The cone only moves because of "
                    "the current in the coil."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e17",
        "band": "easier",
        "text": "To make a permanent magnet, a coil is wound around a bar "
                "of hardened steel, a current is run through it, and the "
                "current is switched off. What is the bar afterwards?",
        "options": [
            {"text": "Not magnetic at all, because switching off removes "
                     "any magnetism it might have had", "correct": False,
             "why": "That is true of soft iron, not of hardened steel. "
                    "Steel keeps what it is given."},
            {"text": "Magnetic, but only while another current is still "
                     "flowing somewhere nearby", "correct": False,
             "why": "Nothing else has to keep flowing. The steel keeps its "
                    "own magnetism once the coil is removed."},
            {"text": "A permanent magnet, because the steel keeps the "
                     "magnetism it was given", "correct": True},
            {"text": "The same as before, because steel cannot be "
                     "magnetised by a coil", "correct": False,
             "why": "Steel can certainly be magnetised by a coil — that is "
                    "exactly how this permanent magnet is made."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e18",
        "band": "easier",
        "text": "Why is hardened steel used to make a permanent magnet in "
                "this way, rather than soft iron?",
        "options": [
            {"text": "Steel is a better conductor of electricity than iron",
             "correct": False,
             "why": "How well a metal conducts current is not the reason; "
                    "what matters here is whether it keeps its magnetism."},
            {"text": "Steel keeps the magnetism it is given, instead of "
                     "losing it straightaway", "correct": True},
            {"text": "Steel is heavier, so the finished magnet is stronger",
             "correct": False,
             "why": "Weight has nothing to do with how strong the "
                    "magnetism is."},
            {"text": "Soft iron cannot be magnetised by a coil in the "
                     "first place, whatever current is used",
             "correct": False,
             "why": "Soft iron magnetises very easily — more easily than "
                    "steel. It just does not keep it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e19",
        "band": "easier",
        "text": "An MRI scanner's main magnet is a coil of superconducting "
                "wire. What is special about superconducting wire?",
        "options": [
            {"text": "It glows brightly so the scan can be seen",
             "correct": False,
             "why": "Nothing about the scan involves light from the wire "
                    "itself."},
            {"text": "It only works when the current keeps reversing "
                     "direction many times a second", "correct": False,
             "why": "The current in this coil runs steadily in one "
                    "direction; it is not switching back and forth."},
            {"text": "It is wound without any core at all", "correct": False,
             "why": "Whether it has a core is not what makes it "
                    "superconducting; having no resistance is."},
            {"text": "It has no resistance at all, so a current can flow "
                     "round it for years", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e20",
        "band": "easier",
        "text": "Why are steel objects, such as an oxygen cylinder, kept "
                "out of an MRI scanner room?",
        "options": [
            {"text": "The field is so strong it can pull a steel object in "
                     "violently enough to injure someone", "correct": True},
            {"text": "Steel would recharge the scanner's magnet "
                     "unexpectedly, adding to its own field", "correct": False,
             "why": "A steel object does not power the magnet in any way."},
            {"text": "Steel would switch the scanner's current off",
             "correct": False,
             "why": "Bringing steel near the magnet does not stop the "
                    "current flowing in it."},
            {"text": "The scanner would overheat if any metal were nearby",
             "correct": False,
             "why": "The danger is the pull of the field on the metal, not "
                    "heat."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e21",
        "band": "easier",
        "text": "What job does a plastic former do inside a coil?",
        "options": [
            {"text": "It multiplies the field, in the same way an iron "
                     "core does", "correct": False,
             "why": "Plastic is not magnetic, so it multiplies nothing at "
                    "all."},
            {"text": "It stores some of the magnetism after the current is "
                     "switched off, releasing it slowly", "correct": False,
             "why": "Nothing is stored in a plastic former; it is not "
                    "magnetic in any way."},
            {"text": "It gives the wire something to be wound around, with "
                     "no magnetic effect of its own", "correct": True},
            {"text": "It reverses the direction of the current passing "
                     "through the coil", "correct": False,
             "why": "The former does not touch the electrical circuit; the "
                    "current's direction is set at the supply."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e22",
        "band": "easier",
        "text": "A soft-iron-cored electromagnet is switched off. A minute "
                "later, is any of its magnetism left?",
        "options": [
            {"text": "Yes, a small amount fades away gradually",
             "correct": False,
             "why": "There is nothing gradual about it. The field is gone "
                    "the instant the current stops."},
            {"text": "Yes, all of it, because the core has been magnetised",
             "correct": False,
             "why": "Soft iron is chosen precisely because it does not "
                    "keep what it is given."},
            {"text": "It depends on how long the current was flowing "
                     "beforehand, the longer the more that stays",
             "correct": False,
             "why": "How long it was switched on makes no difference to "
                    "what happens the instant it is switched off."},
            {"text": "No, none at all — the field disappeared the moment "
                     "the current stopped", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e23",
        "band": "easier",
        "text": "Does a coil need a plastic former to make a magnetic "
                "field?",
        "options": [
            {"text": "No — the field comes from the current in the wire; "
                     "a former is just there to hold the wire in shape",
             "correct": True},
            {"text": "Yes — without a former, no current can flow through "
                     "the coil, since the wire needs support", "correct": False,
             "why": "The former plays no part in the electrical circuit at "
                    "all; the wire carries the current with or without "
                    "one."},
            {"text": "Yes — the former is what gets magnetised, not the "
                     "wire", "correct": False,
             "why": "A plastic former cannot be magnetised at all. It is "
                    "the current itself that creates the field."},
            {"text": "No — but the field is reversed without one fitted",
             "correct": False,
             "why": "Fitting or removing a former does not change which "
                    "way the current is flowing, so it does not reverse "
                    "anything."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e24",
        "band": "easier",
        "text": "Which of the four uses — the crane, the door lock, the "
                "relay, the loudspeaker — depends on the current reversing "
                "direction very rapidly, over and over?",
        "options": [
            {"text": "The crane", "correct": False,
             "why": "The crane only needs the current switched on to lift "
                    "and off to drop — it does not need reversing."},
            {"text": "The loudspeaker", "correct": True},
            {"text": "The door lock", "correct": False,
             "why": "The lock only needs the current on or off, holding "
                    "the door shut or releasing it."},
            {"text": "The relay", "correct": False,
             "why": "The relay only needs a current switched on to pull "
                    "the arm across; nothing about it needs reversing."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e25",
        "band": "easier",
        "text": "Which of the four uses — the crane, the door lock, the "
                "relay, the loudspeaker — depends on the electromagnet "
                "being able to let go of a heavy load on command?",
        "options": [
            {"text": "A relay", "correct": False,
             "why": "A relay's iron arm is light; its job is closing a "
                    "circuit, not letting go of a heavy load."},
            {"text": "A loudspeaker", "correct": False,
             "why": "A loudspeaker's coil is tiny and never lifts anything "
                    "at all."},
            {"text": "A scrapyard crane", "correct": True},
            {"text": "A fire-door lock", "correct": False,
             "why": "A door lock releases a door, which is much lighter "
                    "than the load a scrapyard crane lifts."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e26",
        "band": "easier",
        "text": "A motor's coil has 40 turns. It is compared with an "
                "otherwise identical coil that has only 4 turns, at the "
                "same current. Which coil gives the bigger turning effect?",
        "options": [
            {"text": "The 4-turn coil, because fewer turns means less "
                     "resistance and more push", "correct": False,
             "why": "Turns being fewer does lower resistance slightly, but "
                    "the far bigger effect is that ten times fewer turns "
                    "means ten times fewer pushes adding together."},
            {"text": "Neither — turning effect does not depend on the "
                     "number of turns", "correct": False,
             "why": "It does depend on turns: every turn carries the "
                    "current through the field and adds its own push."},
            {"text": "They are the same, since the current is identical in "
                     "both", "correct": False,
             "why": "The current being the same does not cancel out a "
                    "ten-times difference in the number of turns "
                    "contributing a push."},
            {"text": "The 40-turn coil, by a wide margin", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e27",
        "band": "easier",
        "text": "Ten turns of wire carry 1.0 A. A second, identical coil has "
                "twenty turns carrying the same 1.0 A. Which coil makes the "
                "stronger field?",
        "options": [
            {"text": "The twenty-turn coil", "correct": True},
            {"text": "The ten-turn coil", "correct": False,
             "why": "Fewer turns means fewer fields adding together in the "
                    "same place, so this coil is the weaker one."},
            {"text": "They are equally strong, since the current is the "
                     "same in both", "correct": False,
             "why": "The current being equal is only half the story; the "
                    "coil with more turns adds more fields together."},
            {"text": "It cannot be worked out without knowing the current "
                     "in amps first", "correct": False,
             "why": "The current is already given, and it is the same for "
                    "both — only the turns differ here."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e28",
        "band": "easier",
        "text": "Two identical coils carry 2.0 A each. One has 30 turns and "
                "the other has 60 turns. Which makes the weaker field?",
        "options": [
            {"text": "The 60-turn coil", "correct": False,
             "why": "More turns adds more fields together in the same "
                    "place, which makes a coil stronger, not weaker."},
            {"text": "The 30-turn coil", "correct": True},
            {"text": "Neither — the current decides the strength and it is "
                     "the same for both", "correct": False,
             "why": "The current being equal does not cancel out the "
                    "difference in turns."},
            {"text": "It is impossible to say without knowing the core "
                     "material", "correct": False,
             "why": "The core is the same for both here; only the number "
                    "of turns differs, and that is enough to compare "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e29",
        "band": "easier",
        "text": "One coil carries 1.0 A. An identical coil, with the same "
                "number of turns, carries 3.0 A instead. Which makes the "
                "weaker field?",
        "options": [
            {"text": "The 3.0 A coil", "correct": False,
             "why": "A bigger current through the same coil makes a "
                    "bigger field, not a smaller one."},
            {"text": "Neither — turns decide the strength, and they are "
                     "the same for both", "correct": False,
             "why": "Turns being equal does not cancel out the difference "
                    "in current."},
            {"text": "The 1.0 A coil", "correct": True},
            {"text": "It cannot be worked out from the currents alone",
             "correct": False,
             "why": "Turns and core are the same for both here; only the "
                    "current differs, which is enough to compare them."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-e30",
        "band": "easier",
        "text": "A coil's iron core is swapped for an identical piece of "
                "copper. Is copper a good choice as a core?",
        "options": [
            {"text": "No — the field would reverse direction with a copper "
                     "core, since copper conducts so well", "correct": False,
             "why": "Nothing about the core material can change which way "
                    "the current is flowing, so the direction would not "
                    "reverse."},
            {"text": "Yes — copper is an even better core than iron",
             "correct": False,
             "why": "Copper is not a magnetic material at all, so it "
                    "cannot be magnetised the way iron is."},
            {"text": "It makes no difference which metal is used as a "
                     "core", "correct": False,
             "why": "It makes a large difference: iron is magnetised by "
                    "the coil's field, and copper is not."},
            {"text": "No — copper is not magnetic, so it would do nothing "
                     "at all, just like a plastic former", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · standard ────────────────────────────────
    {
        "id": "p10-04-s11",
        "band": "standard",
        "text": "A coil with 20 turns carries 4.0 A. A second coil, with an "
                "identical core, has 80 turns and carries 1.0 A. How do their "
                "fields compare?",
        "options": [
            {"text": "They are close to each other in strength",
             "correct": True},
            {"text": "The 80-turn coil is far stronger, because turns "
                     "matter more than current", "correct": False,
             "why": "Neither one matters more than the other; the smaller "
                    "current here is balanced by the larger number of "
                    "turns."},
            {"text": "The 20-turn coil is far stronger, because current "
                     "matters more than turns", "correct": False,
             "why": "Neither one matters more than the other; the smaller "
                    "number of turns here is balanced by the larger "
                    "current."},
            {"text": "It cannot be compared without knowing the length of "
                     "each coil", "correct": False,
             "why": "Length is not one of the three things this lesson "
                    "says changes the field; turns, current and core are."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s12",
        "band": "standard",
        "text": "Two electromagnets share the same core. The first has 10 "
                "turns at 2.0 A; the second has 40 turns at that same "
                "2.0 A. Which one produces the stronger field?",
        "options": [
            {"text": "They are about the same, since the current has not "
                     "changed", "correct": False,
             "why": "The current being equal does not cancel out four "
                    "times as many turns adding their fields together."},
            {"text": "The 40-turn coil is much stronger", "correct": True},
            {"text": "The 10-turn coil is much stronger", "correct": False,
             "why": "Fewer turns means fewer fields adding together, which "
                    "makes the weaker coil, not the stronger one."},
            {"text": "The 40-turn coil is weaker, because more wire raises "
                     "the resistance", "correct": False,
             "why": "Resistance can lower the current slightly on the same "
                    "supply, but here both coils are simply given the same "
                    "2.0 A to carry."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s13",
        "band": "standard",
        "text": "An electromagnet carrying 1.0 A is set alongside an "
                "otherwise identical one carrying 4.0 A. Which of the two "
                "produces the stronger field?",
        "options": [
            {"text": "The 1.0 A coil is stronger, because a smaller "
                     "current is easier for the coil to carry",
             "correct": False,
             "why": "Ease of carrying the current is not what sets the "
                    "field's strength; the size of the current is."},
            {"text": "They are the same, since neither coil's turns have "
                     "changed", "correct": False,
             "why": "Turns being equal does not cancel out four times the "
                    "current flowing."},
            {"text": "The 4.0 A coil is much stronger", "correct": True},
            {"text": "It cannot be compared without knowing which coil has "
                     "the iron core", "correct": False,
             "why": "Both coils are identical apart from their current, so "
                    "the core is the same for both."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s14",
        "band": "standard",
        "text": "A student adds more turns to a coil, keeping the supply "
                "the same, and finds the electromagnet is stronger even "
                "though the current measured has gone down very slightly. "
                "How can both be true?",
        "options": [
            {"text": "The meter is faulty, since more wire should always "
                     "mean more current flowing through it", "correct": False,
             "why": "More wire is more resistance, so a slightly lower "
                    "current on the same supply is exactly what should be "
                    "expected."},
            {"text": "The extra turns store magnetism from before, on top "
                     "of the new field", "correct": False,
             "why": "Nothing is stored between turns; the field exists "
                    "only while the current flows."},
            {"text": "The current has not really changed; only the reading "
                     "looks different", "correct": False,
             "why": "The reading is real. Adding wire genuinely raises the "
                    "resistance a little."},
            {"text": "Each extra turn adds its own field in the same "
                     "place, which outweighs the small drop in current",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s15",
        "band": "standard",
        "text": "A student says the iron core is what makes an "
                "electromagnet magnetic, and the coil just holds it in "
                "place. What is the best response?",
        "options": [
            {"text": "The coil makes the field; the core is magnetised by "
                     "that field and adds its own", "correct": True},
            {"text": "That is correct — the coil is simply a support for "
                     "the core", "correct": False,
             "why": "The coil is not just a support; it is the coil's "
                    "current that creates the magnetic field in the first "
                    "place."},
            {"text": "Neither the coil nor the core makes the field; only "
                     "the switch itself creates it", "correct": False,
             "why": "A switch only allows or stops the current. It creates "
                    "no field of its own."},
            {"text": "The core and the coil each make an identical, "
                     "separate field", "correct": False,
             "why": "The core's field comes from being magnetised by the "
                    "coil; it does not appear on its own without the "
                    "coil's current."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s16",
        "band": "standard",
        "text": "A coil with an iron core is holding a chain of paper "
                "clips. Without changing the current or the turns, the "
                "iron core is replaced with an identical rod of hardened "
                "steel. Straight away, is there any difference?",
        "options": [
            {"text": "Yes — it lifts far more clips immediately, because "
                     "steel is simply a stronger, heavier metal",
             "correct": False,
             "why": "Being mechanically strong is a different property "
                    "from being easy to magnetise; steel is not obviously "
                    "a stronger core while the current is still flowing."},
            {"text": "Not obviously, while the current is still flowing — "
                     "the real difference shows up when it is switched "
                     "off", "correct": True},
            {"text": "Yes — the clips fall straight away, because steel is "
                     "not magnetic", "correct": False,
             "why": "Steel is magnetic; it can certainly be made into a "
                    "working electromagnet's core."},
            {"text": "Yes — the poles swap over immediately", "correct": False,
             "why": "Swapping the core does not change which way the "
                    "current is flowing, so the poles do not swap."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s17",
        "band": "standard",
        "text": "Why does a relay let a small current in one circuit "
                "control a much bigger current in another circuit?",
        "options": [
            {"text": "Because the relay's coil carries the big current "
                     "itself, just briefly", "correct": False,
             "why": "The coil only ever carries the small current; the big "
                    "circuit is a completely separate one that the arm "
                    "closes."},
            {"text": "Because the small current recharges a store of "
                     "energy that then powers the whole of the big "
                     "circuit", "correct": False,
             "why": "Nothing is stored. The relay is a switch, not an "
                    "energy store."},
            {"text": "Because the small current's magnetism pulls an arm "
                     "that physically closes the big circuit's own switch",
             "correct": True},
            {"text": "Because the small current heats a wire that then "
                     "melts a fuse in the big circuit", "correct": False,
             "why": "A relay works by magnetism pulling a mechanical arm, "
                    "not by heating anything."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s18",
        "band": "standard",
        "text": "A car's starter motor needs a very large current. Why is "
                "a relay used, rather than running that large current "
                "straight through the ignition key's switch?",
        "options": [
            {"text": "Because the key's switch could not be made from "
                     "metal", "correct": False,
             "why": "The switch could be made from metal perfectly well; "
                    "the issue is the size of current it would have to "
                    "carry."},
            {"text": "Because the starter motor itself needs a magnetic "
                     "field from the key circuit before its own separate "
                     "current can begin to flow", "correct": False,
             "why": "The starter motor does not need a field from the key; "
                    "it needs a large current, which the relay supplies "
                    "from a separate, heavier circuit."},
            {"text": "Because the ignition key circuit has no magnet in it "
                     "at all", "correct": False,
             "why": "The ignition key circuit is exactly what supplies the "
                    "small current that magnetises the relay's coil."},
            {"text": "Because a switch carrying that much current directly "
                     "would need to be far heavier and more expensive than "
                     "the small one at the key", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s19",
        "band": "standard",
        "text": "A loudspeaker's coil is driven by a current that keeps "
                "changing direction, thousands of times a second. What "
                "does the cone do as a result?",
        "options": [
            {"text": "Moves rapidly back and forth, pushing the air to "
                     "make sound", "correct": True},
            {"text": "Spins round continuously, getting faster as the "
                     "current increases", "correct": False,
             "why": "The cone is not free to spin; each change in current "
                    "pushes it one way and then the other, not round and "
                    "round."},
            {"text": "Stays still, because the pushes in each direction "
                     "cancel out", "correct": False,
             "why": "The pushes do not cancel; each reversal genuinely "
                    "drives the cone the other way, which is the "
                    "movement itself."},
            {"text": "Slowly rotates the permanent magnet inside the "
                     "speaker", "correct": False,
             "why": "The permanent magnet is fixed; it is the coil, "
                    "attached to the cone, that is pushed by the field."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s20",
        "band": "standard",
        "text": "To make a permanent magnet, why must the core be hardened "
                "steel rather than the soft iron used in an electromagnet's "
                "core?",
        "options": [
            {"text": "Soft iron would carry too little current for the "
                     "job", "correct": False,
             "why": "The core carries no current at all in either case; "
                    "the current runs through the coil around it."},
            {"text": "Soft iron loses its magnetism as soon as the coil's "
                     "current stops, which would leave nothing permanent "
                     "behind", "correct": True},
            {"text": "Soft iron cannot be placed inside a coil at all",
             "correct": False,
             "why": "Soft iron is exactly what usually goes inside a coil, "
                    "in an ordinary electromagnet."},
            {"text": "Hardened steel makes a far stronger field while the "
                     "current is flowing, stronger than soft iron ever "
                     "manages", "correct": False,
             "why": "While the current is flowing, soft iron and hardened "
                    "steel behave in a broadly similar way; the real "
                    "difference shows up once it is switched off."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s21",
        "band": "standard",
        "text": "An MRI scanner's superconducting coil carries a very "
                "large current with no supply connected, for years on end. "
                "What would happen if the wire had ordinary resistance "
                "instead?",
        "options": [
            {"text": "Nothing would change — resistance only matters for "
                     "very small currents, not large ones like this",
             "correct": False,
             "why": "Resistance matters whatever the size of the current; "
                    "a large current through a resistant wire loses energy "
                    "steadily."},
            {"text": "The field would immediately reverse direction",
             "correct": False,
             "why": "Resistance affects how long a current can keep "
                    "flowing on its own, not which way it points."},
            {"text": "The current would steadily lose energy and die "
                     "away, needing a constant supply to keep it going",
             "correct": True},
            {"text": "The coil would need an iron core to keep working",
             "correct": False,
             "why": "A core is unrelated to resistance; the coil already "
                    "works without a supply because it has none, not "
                    "because of any core."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s22",
        "band": "standard",
        "text": "Two identical scrapyard-crane electromagnets are "
                "compared. One is switched off gently, over several "
                "seconds using a dimmer switch; the other is switched off "
                "instantly. Does either one drop its load more slowly?",
        "options": [
            {"text": "No — the field stays at full strength until the "
                     "current reaches zero, so both drop their loads at "
                     "the very same moment", "correct": False,
             "why": "A soft iron core's field rises and falls in step "
                    "with the current in its coil. It does not hold full "
                    "strength and then vanish at the end."},
            {"text": "Yes — the instantly-switched one holds on longer, "
                     "because a sudden change leaves the core no time to "
                     "let go", "correct": False,
             "why": "Soft iron lets go as soon as its current does, so a "
                    "sudden switch-off releases the load at once rather "
                    "than delaying it."},
            {"text": "No — a crane magnet is either holding or released, "
                     "so switching it off slowly makes no difference",
             "correct": False,
             "why": "The core's magnetism is not all-or-nothing: it "
                    "follows the current, so a slow fall in current means "
                    "a slow fall in the field holding the load."},
            {"text": "Yes — the field falls as the current falls, so the "
                     "gently-switched one holds on until its current has "
                     "dropped far enough", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s23",
        "band": "standard",
        "text": "A student wants to build the strongest possible "
                "electromagnet from a fixed length of wire and a fixed "
                "current. Should they wind it into few, wide turns or "
                "many, narrow turns around the same core?",
        "options": [
            {"text": "Many, narrow turns — more turns in the same space "
                     "adds more fields together", "correct": True},
            {"text": "Few, wide turns — a wider loop makes a bigger field "
                     "on its own", "correct": False,
             "why": "The lesson's rule is about how many turns add "
                    "together in the same place, not about how wide any "
                    "one loop is."},
            {"text": "It makes no difference how the wire is wound, only "
                     "how much of it there is", "correct": False,
             "why": "How the wire is wound matters: more turns in the "
                    "same length of core means more fields stacking up."},
            {"text": "Few, wide turns — fewer turns means less resistance "
                     "and more current", "correct": False,
             "why": "A small change in current from fewer turns would not "
                    "outweigh losing most of the turns' fields."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s24",
        "band": "standard",
        "text": "A door lock's electromagnet is designed so a fire alarm "
                "cuts its current the instant it sounds. Why does the door "
                "open reliably even if the alarm's own wiring is damaged "
                "in the fire?",
        "options": [
            {"text": "Because the alarm sends a special signal that "
                     "unlocks the door directly", "correct": False,
             "why": "The door is not unlocked by a signal; it is unlocked "
                    "simply because current stops reaching the magnet."},
            {"text": "Because a broken wire also stops the current "
                     "reaching the lock, which releases it exactly as "
                     "cutting the power on purpose would", "correct": True},
            {"text": "Because fire cannot damage an electromagnet's coil",
             "correct": False,
             "why": "The coil can certainly be damaged by fire; what "
                    "matters is that damage of almost any kind removes "
                    "the current, which releases the door."},
            {"text": "Because the lock is fitted with its own separate "
                     "battery that never fails, whatever happens to the "
                     "mains supply or the wiring around it",
             "correct": False,
             "why": "The lock has no separate battery here; it depends "
                    "entirely on the current reaching it, which is "
                    "exactly the point."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s25",
        "band": "standard",
        "text": "A relay's iron arm is replaced with an identical arm made "
                "of copper. Does the relay still work?",
        "options": [
            {"text": "Yes — copper conducts electricity better than iron, "
                     "so it works even better", "correct": False,
             "why": "Conducting electricity is not the arm's job here; it "
                    "needs to be pulled by a magnetic field, and copper is "
                    "not attracted to one."},
            {"text": "Yes, but it needs a much bigger current in the small "
                     "circuit to work", "correct": False,
             "why": "No amount of extra current helps, because copper is "
                    "not a magnetic material and is never pulled by the "
                    "coil's field at all."},
            {"text": "No — copper is not magnetic, so the coil's field "
                     "cannot pull it across", "correct": True},
            {"text": "No — copper would carry the big circuit's current "
                     "straight through the small one", "correct": False,
             "why": "The arm does not carry the big circuit's current at "
                    "all; it only closes a switch for it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s26",
        "band": "standard",
        "text": "In an electric bell, would the bell still ring "
                "repeatedly if the iron arm were replaced with an "
                "identical plastic one?",
        "options": [
            {"text": "Yes — plastic conducts electricity well enough to "
                     "close the circuit", "correct": False,
             "why": "Whether it conducts is not the issue here; the arm "
                    "needs to be pulled by the coil's magnetic field, and "
                    "plastic is not affected by it."},
            {"text": "Yes — the coil would simply pull the plastic arm "
                     "just as it pulled the iron one before it was "
                     "replaced", "correct": False,
             "why": "A coil's field pulls magnetic materials. Plastic is "
                    "not magnetic, so nothing would pull it at all."},
            {"text": "It depends on how close the plastic arm is to the "
                     "coil", "correct": False,
             "why": "Distance makes no difference here, because plastic "
                    "is never attracted by a magnetic field in the first "
                    "place, near or far."},
            {"text": "No — plastic is not magnetic, so the coil could "
                     "never pull it across to break the circuit",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s27",
        "band": "standard",
        "text": "A soft-iron-cored electromagnet and an air-cored coil, "
                "both with the same turns and current, are switched off at "
                "the same instant. Which one still shows a field a moment "
                "later?",
        "options": [
            {"text": "Neither — both fields disappear the instant their "
                     "currents stop", "correct": True},
            {"text": "The iron-cored one, because the core keeps some "
                     "magnetism a moment longer than that", "correct": False,
             "why": "Soft iron is chosen precisely because it does not "
                    "keep any magnetism once the current stops."},
            {"text": "The air-cored one, because it never had much of a "
                     "field to lose", "correct": False,
             "why": "Having a smaller field to begin with does not mean "
                    "it lingers; it disappears just as instantly as the "
                    "stronger one."},
            {"text": "Both, briefly, because any coil takes a moment to "
                     "lose its field", "correct": False,
             "why": "There is no lingering field in either case; both go "
                    "to zero the instant the current does."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s28",
        "band": "standard",
        "text": "A coil's turns are halved and its current is doubled at "
                "the same time. How does the new field compare with the "
                "original?",
        "options": [
            {"text": "It is much weaker, because losing half the turns "
                     "matters more than doubling the current",
             "correct": False,
             "why": "Neither change matters more than the other; halving "
                    "one and doubling the other roughly cancels out."},
            {"text": "It is close to what it was before", "correct": True},
            {"text": "It is much stronger, because doubling the current "
                     "matters more than halving the turns", "correct": False,
             "why": "Neither change matters more than the other; halving "
                    "one and doubling the other roughly cancels out."},
            {"text": "It reverses direction, because one change is an "
                     "increase and the other a decrease", "correct": False,
             "why": "Direction depends on which way the current runs, not "
                    "on the size of the turns or the current."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s29",
        "band": "standard",
        "text": "An electromagnet is rebuilt so it has 60 turns instead of "
                "30, but its current is dropped from 4.0 A to 2.0 A. "
                "Compared with the original, is the new field stronger, "
                "weaker, or about the same?",
        "options": [
            {"text": "Stronger, because doubling the turns matters more "
                     "than halving the current", "correct": False,
             "why": "Neither change matters more than the other; doubling "
                    "one and halving the other roughly cancels out, "
                    "leaving the field close to where it started."},
            {"text": "Weaker, because halving the current matters more "
                     "than doubling the turns", "correct": False,
             "why": "Neither change matters more than the other; doubling "
                    "one and halving the other roughly cancels out, "
                    "leaving the field close to where it started."},
            {"text": "About the same as the original, since the two "
                     "changes roughly cancel each other out",
             "correct": True},
            {"text": "It cannot be worked out without knowing the core "
                     "material", "correct": False,
             "why": "The core has not changed here; only the turns and "
                    "the current have, and that is enough to compare "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-s30",
        "band": "standard",
        "text": "An electromagnet's turns are tripled, and its current is "
                "also tripled. How does the new field compare with the "
                "original?",
        "options": [
            {"text": "It stays the same, since both changes are identical "
                     "in size", "correct": False,
             "why": "Both increasing by the same amount does not cancel "
                    "out; each change on its own already makes the field "
                    "bigger."},
            {"text": "It triples, because only one of the two changes "
                     "actually counts", "correct": False,
             "why": "Both changes count. Turns and current both add to "
                    "the field, so both increases apply together."},
            {"text": "It doubles, because two changes together are capped "
                     "at doubling the effect, however large either change "
                     "is", "correct": False,
             "why": "There is no such cap; each change contributes its "
                    "own increase, and here both are tripled."},
            {"text": "It becomes very much stronger, since both changes "
                     "act together, each increasing the field",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · harder ──────────────────────────────────
    {
        "id": "p10-04-h11",
        "band": "harder",
        "text": "Electromagnet A has 15 turns and carries 4.0 A. "
                "Electromagnet B has 60 turns and carries 1.0 A. Both share "
                "an identical core. How do their fields compare?",
        "options": [
            {"text": "They are close to each other in strength",
             "correct": True},
            {"text": "B is four times stronger, because turns matter four "
                     "times as much as current", "correct": False,
             "why": "Neither one matters more than the other; B's smaller "
                    "current is balanced by four times as many turns."},
            {"text": "A is four times stronger, because current matters "
                     "four times as much as turns", "correct": False,
             "why": "Neither one matters more than the other; A's fewer "
                    "turns are balanced by four times the current."},
            {"text": "It cannot be compared without knowing the length of "
                     "each coil", "correct": False,
             "why": "Coil length is not one of the three things this "
                    "lesson says the field depends on."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h12",
        "band": "harder",
        "text": "A coil with 12 turns carries 5.0 A. It is rewound with 60 "
                "turns, and the current is reduced to 2.0 A on the same "
                "supply because the extra wire raises the resistance. Is "
                "the new coil stronger or weaker than the original?",
        "options": [
            {"text": "Weaker — the current has fallen to less than half "
                     "of what it was", "correct": False,
             "why": "The turns have increased by five times, which more "
                    "than makes up for the smaller current."},
            {"text": "Stronger — five times the turns outweighs the drop "
                     "in current", "correct": True},
            {"text": "About the same — the two changes roughly cancel "
                     "each other out", "correct": False,
             "why": "Five times the turns against less than half the "
                    "current does not roughly cancel; the turns' effect "
                    "wins by a wide margin."},
            {"text": "It cannot be worked out, because current and turns "
                     "cannot be compared with each other", "correct": False,
             "why": "They can be compared: each extra turn adds its own "
                    "field, and a smaller current gives each turn a "
                    "smaller push — both can be reasoned about together."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h13",
        "band": "harder",
        "text": "An electromagnet with a soft iron core lifts a load. A "
                "second, identical electromagnet is built with a core of "
                "hardened steel instead. Both are switched on, lift their "
                "loads, and are then switched off. Which one is harder to "
                "unload afterwards?",
        "options": [
            {"text": "The soft iron one, because iron is a stronger core "
                     "than steel while the current flows", "correct": False,
             "why": "While the current is flowing, soft iron and hardened "
                    "steel behave in a broadly similar way; the real "
                    "difference is what happens after switch-off."},
            {"text": "Neither — both release their loads identically, "
                     "since both are magnetic metals of a similar kind",
             "correct": False,
             "why": "Both being magnetic is not the whole story; steel "
                    "keeps the magnetism it is given, and soft iron does "
                    "not."},
            {"text": "The steel-cored one, because the steel keeps "
                     "magnetism the soft iron would have lost",
             "correct": True},
            {"text": "The soft iron one, because it takes longer to "
                     "switch off completely", "correct": False,
             "why": "Switching off is instantaneous in both cases; the "
                    "difference is what the core does with the magnetism "
                    "it was given, not how quickly the switch acts."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h14",
        "band": "harder",
        "text": "A relay's coil is rewound with far fewer turns, keeping "
                "the same current. The arm no longer moves across to close "
                "the big circuit. What is the most likely explanation?",
        "options": [
            {"text": "The big circuit's current has become too small to "
                     "detect, even though the small coil's own wiring is "
                     "unchanged", "correct": False,
             "why": "The relay's coil never carries the big circuit's "
                    "current at all; it is switched by the small circuit's "
                    "magnetism, which is what has weakened here."},
            {"text": "The iron arm has become demagnetised over time",
             "correct": False,
             "why": "The arm does not need to be permanently magnetised; "
                    "it only needs to be pulled by the coil's field each "
                    "time the coil is energised."},
            {"text": "The current in the small circuit has reversed "
                     "direction", "correct": False,
             "why": "Reversing the current would swap the coil's poles, "
                    "not stop it from making a field able to pull the arm "
                    "at all."},
            {"text": "Fewer turns has weakened the coil's field below the "
                     "strength needed to pull the arm across",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h15",
        "band": "harder",
        "text": "A student claims that reversing the current through an "
                "electromagnet's coil makes it stronger, because the field "
                "is now working in a fresh direction. What is wrong with "
                "this reasoning?",
        "options": [
            {"text": "Reversing the current changes which end is north "
                     "and which is south, but leaves the strength of the "
                     "field exactly as it was", "correct": True},
            {"text": "The reasoning is correct — reversing the current "
                     "does make it stronger", "correct": False,
             "why": "The strength is unchanged by reversing the current; "
                    "only the poles swap over."},
            {"text": "Reversing the current actually switches the field "
                     "off completely", "correct": False,
             "why": "A current is still flowing, in the other direction, "
                    "so a field of the same size is still being made."},
            {"text": "Reversing the current only affects a core made of "
                     "hardened steel, not soft iron, because only steel "
                     "keeps any magnetism at all", "correct": False,
             "why": "Reversing the current affects the poles of any "
                    "electromagnet's field, whatever the core is made "
                    "from."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h16",
        "band": "harder",
        "text": "An MRI scanner's coil carries an enormous, unchanging "
                "current for years with no power supply connected. A "
                "different, ordinary electromagnet is switched off the "
                "moment its supply is disconnected. What is the key "
                "difference between the two coils that explains this?",
        "options": [
            {"text": "The MRI coil is wound with far more turns than an "
                     "ordinary electromagnet, which is why its field can "
                     "persist for so long", "correct": False,
             "why": "The number of turns changes how strong a coil's "
                    "field is, not whether a current can keep flowing "
                    "with no supply at all."},
            {"text": "The MRI coil's wire has no electrical resistance, "
                     "so nothing drains the current away once it is set "
                     "flowing", "correct": True},
            {"text": "The MRI coil has no core at all, unlike an ordinary "
                     "electromagnet", "correct": False,
             "why": "Having no core changes how strong the field is, not "
                    "whether the current itself can persist without a "
                    "supply."},
            {"text": "The MRI coil's current is much smaller than an "
                     "ordinary electromagnet's", "correct": False,
             "why": "The current in an MRI's main coil is in fact very "
                    "large; its size is not what lets it persist without "
                    "a supply."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h17",
        "band": "harder",
        "text": "A permanent magnet is made by winding a coil around a bar "
                "of hardened steel, running a current, and switching off. "
                "A second attempt uses exactly the same coil and current, "
                "but around a bar of soft iron instead. What is the "
                "result?",
        "options": [
            {"text": "An identical permanent magnet, since both are made "
                     "of iron", "correct": False,
             "why": "Hardened steel and soft iron are both mostly iron, "
                    "but they behave very differently once the current "
                    "stops."},
            {"text": "A stronger permanent magnet, because soft iron "
                     "magnetises more easily and holds on to it just as "
                     "firmly", "correct": False,
             "why": "Soft iron magnetising more easily while the current "
                    "flows is exactly why it fails to STAY magnetised "
                    "afterwards."},
            {"text": "No permanent magnet at all — the soft iron loses "
                     "its magnetism as soon as the current stops",
             "correct": True},
            {"text": "A permanent magnet with reversed poles compared "
                     "with the steel one", "correct": False,
             "why": "Nothing about which metal is used changes which way "
                    "the current is flowing, so the poles would not "
                    "reverse."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h18",
        "band": "harder",
        "text": "A loudspeaker's coil is fed a current that changes "
                "direction only once a second, rather than thousands of "
                "times a second. What would a listener notice?",
        "options": [
            {"text": "Nothing different — the cone's motion does not "
                     "depend on how often the current changes, only on "
                     "how large it happens to be", "correct": False,
             "why": "The rate the current changes is exactly what sets "
                    "how fast the cone moves, which is what a listener "
                    "hears as pitch."},
            {"text": "The magnet inside would need to be switched, which "
                     "it cannot do", "correct": False,
             "why": "The magnet is permanent and fixed throughout; only "
                    "the coil's current changes direction."},
            {"text": "The cone would spin instead of moving back and "
                     "forth", "correct": False,
             "why": "The cone is not mounted to spin either way; the "
                    "current's direction sets which way it is pushed, "
                    "not whether it turns."},
            {"text": "The cone would move back and forth far more "
                     "slowly, which would sound as a very low, thumping "
                     "sound rather than a note", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h19",
        "band": "harder",
        "text": "A door lock's electromagnet is fitted with a soft iron "
                "core. A safety inspector suggests replacing it with "
                "hardened steel 'to make the lock stronger.' Why is this a "
                "bad idea?",
        "options": [
            {"text": "A steel core would keep some magnetism after the "
                     "power is cut, so the door might not release "
                     "reliably", "correct": True},
            {"text": "Steel cannot be magnetised strongly enough to hold "
                     "a door shut", "correct": False,
             "why": "Steel magnetises perfectly well; the problem is not "
                    "initial strength, it is what happens when the power "
                    "is cut."},
            {"text": "Steel would reverse the lock's poles every time the "
                     "door closes", "correct": False,
             "why": "Nothing about the core material reverses the "
                    "current's direction; the poles would not swap on "
                    "their own."},
            {"text": "Steel conducts electricity too well for a coil to "
                     "be safely wound around it without a serious risk of "
                     "a short circuit", "correct": False,
             "why": "The core does not carry the coil's current at all; "
                    "how well it conducts electricity is not relevant "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h20",
        "band": "harder",
        "text": "Two identical-looking electromagnets are being compared. "
                "One has 3 times the turns of the other, but only a third "
                "of the current. Which is stronger?",
        "options": [
            {"text": "The higher-turns one, because turns matter more "
                     "than current", "correct": False,
             "why": "Neither matters more; three times the turns and a "
                    "third of the current cancel out exactly."},
            {"text": "They are equally strong", "correct": True},
            {"text": "The higher-current one, because current matters "
                     "more than turns", "correct": False,
             "why": "Neither matters more; three times the turns and a "
                    "third of the current cancel out exactly."},
            {"text": "It cannot be worked out without knowing the core "
                     "material", "correct": False,
             "why": "The core is not said to differ here; turns and "
                    "current alone are enough to compare them, since one "
                    "exactly balances the other."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h21",
        "band": "harder",
        "text": "A soft-iron-cored electromagnet lifts eight paper clips "
                "at a certain current. The current is then reduced to a "
                "quarter of its original value, with everything else "
                "unchanged. What would you expect?",
        "options": [
            {"text": "It still lifts close to eight clips, because the "
                     "core does the real work", "correct": False,
             "why": "The core only multiplies whatever field the current "
                    "makes; cutting the current to a quarter cuts the "
                    "field it has to multiply."},
            {"text": "It lifts more clips, because a gentler current "
                     "strains the wire less", "correct": False,
             "why": "How gently the wire is treated has nothing to do "
                    "with how many clips a weaker field can hold; it "
                    "lifts fewer, not more."},
            {"text": "It lifts noticeably fewer clips, since a smaller "
                     "current makes a weaker field", "correct": True},
            {"text": "It lifts exactly two clips, since the field falls "
                     "by exactly the same fraction as the current",
             "correct": False,
             "why": "The number of clips held is not a simple fraction of "
                    "the current in this way; it falls, but not to a "
                    "value that can be read off directly like that."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h22",
        "band": "harder",
        "text": "A relay closes a big circuit whenever its small coil is "
                "energised. A student wires the small coil directly into "
                "the big circuit itself, hoping to simplify things, so "
                "one current does both jobs. Why is this a bad plan?",
        "options": [
            {"text": "The relay's arm cannot be pulled by a current at "
                     "all", "correct": False,
             "why": "The relay's arm is pulled by exactly the coil's "
                    "current; that is how a relay normally works."},
            {"text": "The big circuit's own current would be far too "
                     "small to close anything, since a relay is only ever "
                     "built to detect the smallest currents", "correct": False,
             "why": "It is not that the current is too small; the danger "
                    "is the opposite — the big circuit's current is far "
                    "too large for the small coil and switch to carry "
                    "safely."},
            {"text": "The coil would need to be made of hardened steel "
                     "instead of iron", "correct": False,
             "why": "The coil's own core material is not the issue here; "
                    "it is the size of current the small circuit's "
                    "wiring is built to carry."},
            {"text": "The small coil and its switch are built for a "
                     "small current, and the big circuit's current would "
                     "be far too large for them to carry safely",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h23",
        "band": "harder",
        "text": "An electromagnet is switched off, and a fellow student "
                "claims they can still feel a very faint pull on a paper "
                "clip nearby, a second later. What is the best "
                "explanation?",
        "options": [
            {"text": "They are mistaken — with a soft iron core the field "
                     "is gone the instant the current stops, so there is "
                     "nothing left to feel", "correct": True},
            {"text": "The pull is real, and it fades away gradually over "
                     "a few seconds", "correct": False,
             "why": "There is nothing gradual about a soft-iron-cored "
                    "electromagnet's field; it disappears at the same "
                    "instant the current does."},
            {"text": "The pull is real, because the paper clip itself has "
                     "become magnetised permanently by sitting close to "
                     "the coil", "correct": False,
             "why": "A single paper clip briefly held near a coil does "
                    "not become a permanent magnet from that alone, and "
                    "the coil's own field is what has gone in any case."},
            {"text": "The pull is real, because the switch itself has "
                     "stored some current", "correct": False,
             "why": "A switch stores no current at all; it only allows or "
                    "stops the flow."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h24",
        "band": "harder",
        "text": "A student wants an electromagnet that switches off "
                "completely but can also be made into a permanent magnet "
                "later, using the same coil, just by choosing what to put "
                "inside it at the time. What should they use as the core?",
        "options": [
            {"text": "Hardened steel every time, since it is more "
                     "magnetic than soft iron", "correct": False,
             "why": "Being 'more magnetic' is not quite it — the relevant "
                    "property is whether the core keeps the magnetism "
                    "once the current stops, which is what determines the "
                    "choice."},
            {"text": "Soft iron for everyday switching, swapped for "
                     "hardened steel on the occasion they want a lasting "
                     "magnet", "correct": True},
            {"text": "The same core material either way, since the coil "
                     "is what really matters and the core barely makes "
                     "any difference", "correct": False,
             "why": "The coil is not what really matters here; the whole "
                    "difference between switching off cleanly and keeping "
                    "magnetism for good comes down to the core material "
                    "chosen."},
            {"text": "Plastic, since it can be shaped to do either job",
             "correct": False,
             "why": "Plastic is not magnetic at all, so it could never "
                    "become a permanent magnet, however it is shaped."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h25",
        "band": "harder",
        "text": "A loudspeaker cone moves back and forth as the coil's "
                "current keeps reversing. What single change to the "
                "current would make the cone push out further each time, "
                "without changing how often it reverses?",
        "options": [
            {"text": "Making the current reverse even more often",
             "correct": False,
             "why": "Reversing more often changes the note's pitch; it "
                    "does not by itself make each push bigger."},
            {"text": "Making the current smaller", "correct": False,
             "why": "A smaller current gives a smaller push, moving the "
                    "cone less far, not more."},
            {"text": "Making the current larger", "correct": True},
            {"text": "Making the current reverse less predictably",
             "correct": False,
             "why": "Irregular reversing would distort the sound; it "
                    "does not, by itself, make each individual push "
                    "bigger."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h26",
        "band": "harder",
        "text": "Two identical fire doors are fitted with electromagnetic "
                "locks. Door A's lock uses a soft iron core; Door B's uses "
                "a hardened steel core by mistake. Both are working "
                "normally, holding their doors shut. The fire alarm cuts "
                "the power to both. Which door is more likely to fail to "
                "open?",
        "options": [
            {"text": "Door A, because soft iron reacts more slowly to "
                     "losing current", "correct": False,
             "why": "Soft iron reacts instantly, not slowly, when the "
                    "current stops — that is exactly the property that "
                    "makes it the right choice."},
            {"text": "Neither — both release identically, since both "
                     "cores are magnetic", "correct": False,
             "why": "Both being magnetic materials is not the deciding "
                    "factor; what matters is whether each one keeps the "
                    "magnetism it is given."},
            {"text": "Door A, because soft iron needs a reversed current "
                     "to release, not just a stopped one, at any point",
             "correct": False,
             "why": "Soft iron does not need a reversed current to "
                    "release; simply stopping the current is enough."},
            {"text": "Door B, because the hardened steel core may keep "
                     "some magnetism and hold the door partly shut",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h27",
        "band": "harder",
        "text": "A coil's current is switched on and off very rapidly, "
                "thousands of times a second, exactly as it would be in a "
                "loudspeaker — but this time the coil has a soft iron "
                "core, as in an electromagnet, rather than sitting rigidly "
                "in a fixed magnet's field. What would you expect to "
                "happen to the core's magnetism as the current switches?",
        "options": [
            {"text": "It would switch on and off in step with the "
                     "current, appearing and disappearing thousands of "
                     "times a second, since soft iron responds instantly",
             "correct": True},
            {"text": "It would build up steadily until the core became a "
                     "permanent magnet, holding its magnetism afterwards "
                     "regardless of how the current then switches",
             "correct": False,
             "why": "Soft iron does not accumulate magnetism over "
                    "repeated switching; it loses what it has the instant "
                    "each current pulse stops."},
            {"text": "It would stay constant, since soft iron cannot "
                     "respond that quickly", "correct": False,
             "why": "Soft iron responds as fast as the current changes; "
                    "there is nothing in the lesson suggesting any lag."},
            {"text": "It would reverse permanently after the first "
                     "switch-off", "correct": False,
             "why": "Switching the current off does not reverse anything; "
                    "it simply stops the field, and reversing needs the "
                    "current itself to run the other way."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h28",
        "band": "harder",
        "text": "A student says that because both the relay and the "
                "electric bell use an electromagnet to pull an iron arm, "
                "they must work in exactly the same way. What is the key "
                "difference between them?",
        "options": [
            {"text": "Only the bell uses a current at all; the relay "
                     "works by a permanent magnet that pulls its arm "
                     "across without needing a current of its own",
             "correct": False,
             "why": "Both devices are electromagnets, switched by a "
                    "current; neither uses a permanent magnet."},
            {"text": "The bell's own arm breaks the circuit that powers "
                     "it, so it repeats automatically; the relay's arm "
                     "closes a separate circuit and stays put",
             "correct": True},
            {"text": "Only the relay's arm is made of iron; the bell's "
                     "arm is made of steel", "correct": False,
             "why": "Both use an iron arm, pulled by a coil's field in "
                    "the same basic way; the difference is in what each "
                    "arm's movement does to the circuit."},
            {"text": "The bell needs a much bigger current than the relay "
                     "to work at all", "correct": False,
             "why": "The size of current needed is not the key difference "
                    "here; what differs is what happens once the arm has "
                    "moved."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h29",
        "band": "harder",
        "text": "An electromagnet with 25 turns and a current of 4.0 A is "
                "compared with one that has 100 turns and a current of "
                "1.0 A, both with identical iron cores. A third "
                "electromagnet has 50 turns and a current of 2.0 A. Which "
                "of the first two is this third one closest to in "
                "strength?",
        "options": [
            {"text": "Closer to the 25-turn one, because it has fewer "
                     "turns than the 100-turn one", "correct": False,
             "why": "Its field, from turns times current, sits between "
                    "the two — closeness in turns alone does not decide "
                    "closeness in field strength."},
            {"text": "Closer to the 100-turn one, because it has more "
                     "turns than the 25-turn one", "correct": False,
             "why": "Its field sits between the two — closeness in turns "
                    "alone does not decide closeness in field strength."},
            {"text": "About equally close to both, since all three give a "
                     "very similar field", "correct": True},
            {"text": "It cannot be compared, since three coils cannot be "
                     "ranked at once", "correct": False,
             "why": "Three coils can be compared the same way as two, by "
                    "reasoning about turns and current together."},
        ],
        "figure": None,
    },
    {
        "id": "p10-04-h30",
        "band": "harder",
        "text": "A single-coil electromagnet built for a school "
                "demonstration is later modified by a student, who "
                "reduces the number of turns to a quarter but keeps the "
                "current the same, hoping the coil will run cooler "
                "without becoming much weaker. Was the student right to "
                "expect only a small drop in strength?",
        "options": [
            {"text": "Yes — turns barely affect the strength compared "
                     "with the current", "correct": False,
             "why": "Turns affect the strength directly: each one adds "
                    "its own field, so removing three-quarters of them "
                    "removes most of that contribution."},
            {"text": "Yes — removing turns only affects how hot the coil "
                     "runs, not its field, which stays exactly as strong "
                     "however many turns are taken away", "correct": False,
             "why": "Removing turns changes both: fewer turns does run "
                    "cooler, but it also removes most of the fields that "
                    "were adding together."},
            {"text": "No — the coil would in fact become completely "
                     "non-magnetic", "correct": False,
             "why": "It would still make some field, from the turns and "
                    "current that remain; it would not vanish altogether."},
            {"text": "No — losing three-quarters of the turns would "
                     "weaken the field by roughly the same fraction, "
                     "which is a large drop, not a small one at all",
             "correct": True},
        ],
        "figure": None,
    },
]
