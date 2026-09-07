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
]
