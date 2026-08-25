"""P8 lesson 01 — Current and circuits: twelve questions (MRB-223).

Written against Design's page. The torch with the snipped strip, the loop
with three meter sockets and the eight-symbol key are hers.

The discriminations, in the order the lesson builds them:

  · a current is a FLOW OF CHARGE, and the charge was already there
    (`CIRC-04`);
  · the loop has to be COMPLETE, and a gap anywhere stops it everywhere
    (`CIRC-03`);
  · nothing is USED UP — what the bulb takes is energy (`CIRC-01`) — the
    harder band sits here;
  · the delay a student expects does not exist, because nothing has to
    make the journey (`CIRC-02`).

⚠️ POSITION IS AUTHORED AND MEASURED —
2,0,3,1 · 1,3,0,2 · 0,2,1,2;
the twelve fall 3/3/4/2 across the four indices.

⚠️ The ladder's own two marked rungs are NOT restated: neither the two
ammeters either side of a bulb reading 0.24 A, nor the long cable and the
delay a student predicts.
"""

UNIT = "P8"
LESSON = "current-and-circuits"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p8-01-e01",
        "band": "easier",
        "text": "An electric current is…",
        "options": [
            {"text": "a flow of heat through a wire", "correct": False,
             "why": "A wire does get warm, but that is a consequence of the "
                    "current rather than the current itself."},
            {"text": "a flow of light along the inside of the wire",
             "correct": False,
             "why": "Light comes out of the bulb, not along the wire. The "
                    "wire is solid metal."},
            {"text": "a flow of charge", "correct": True},
            {"text": "a store of electricity kept inside the cell",
             "correct": False,
             "why": "A cell stores energy, not current. Current is something "
                    "that happens in the wire when the cell pushes."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-e02",
        "band": "easier",
        "text": "Current is measured in…",
        "options": [
            {"text": "amperes", "correct": True},
            {"text": "volts", "correct": False,
             "why": "Volts measure potential difference — how hard the "
                    "charge was pushed, not how much is flowing."},
            {"text": "ohms", "correct": False,
             "why": "Ohms measure resistance — how hard a component makes it "
                    "for charge to get through."},
            {"text": "joules", "correct": False,
             "why": "Joules measure energy. A current carries energy but is "
                    "not measured in it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-e03",
        "band": "easier",
        "text": "Where does an ammeter go in a circuit?",
        "options": [
            {"text": "Across a component, with a lead on each side",
             "correct": False,
             "why": "That is where a voltmeter goes. An ammeter across a "
                    "component bypasses it."},
            {"text": "Anywhere at all — it reads the current wherever you "
                     "hold it", "correct": False,
             "why": "It has to be wired into the circuit. A meter not "
                    "connected to anything reads nothing."},
            {"text": "Beside the cell, connected to one terminal only",
             "correct": False,
             "why": "A meter with one lead connected is not in a loop, so no "
                    "charge passes through it."},
            {"text": "In the loop, so the current runs through it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-e04",
        "band": "easier",
        "text": "In the circuit symbols, a circle with a cross inside it "
                "means…",
        "options": [
            {"text": "a switch", "correct": False,
             "why": "A switch is drawn as two contacts with a lever lifted "
                    "away from one of them."},
            {"text": "a lamp", "correct": True},
            {"text": "an ammeter", "correct": False,
             "why": "An ammeter is a circle with the letter A inside it."},
            {"text": "a resistor", "correct": False,
             "why": "A resistor is a plain rectangle drawn in the wire."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p8-01-s01",
        "band": "standard",
        "text": "A switch is opened in a loop that holds a cell and two "
                "lamps. What happens?",
        "options": [
            {"text": "The lamp nearer the cell stays lit and the far one "
                     "goes out", "correct": False,
             "why": "There is no nearer and further in a loop. Both lamps go "
                    "out at the same instant."},
            {"text": "Both lamps go out, because the loop is no longer "
                     "complete", "correct": True},
            {"text": "Both lamps dim but stay lit, because the switch only "
                     "narrows the path", "correct": False,
             "why": "An open switch is a gap, not a narrowing. Nothing flows "
                    "at all."},
            {"text": "Nothing changes until the charge already in the wire "
                     "has been used up", "correct": False,
             "why": "The charge is not used up, and nothing is waiting to "
                    "run out. The flow stops the instant the ring breaks."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-s02",
        "band": "standard",
        "text": "Three cells are put in the holder instead of one. The "
                "ammeter reading…",
        "options": [
            {"text": "stays the same, because the loop has not changed",
             "correct": False,
             "why": "More cells give a bigger push, so more charge goes past "
                    "each second."},
            {"text": "falls, because there is more for the charge to get "
                     "through", "correct": False,
             "why": "Cells push; they do not obstruct. Adding them makes the "
                    "current larger."},
            {"text": "drops to zero, because the cells cancel each other out",
             "correct": False,
             "why": "Cells in a holder are lined up the same way and add "
                    "their pushes together."},
            {"text": "rises, because a bigger push moves the charge faster "
                     "everywhere at once", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-s03",
        "band": "standard",
        "text": "An ammeter is moved from in front of a bulb to right beside "
                "the cells. The reading…",
        "options": [
            {"text": "is the same in both places", "correct": True},
            {"text": "is largest right beside the cells, because that is "
                     "where the charge starts", "correct": False,
             "why": "The charge does not start there. It is already spread "
                    "round the whole loop, and one loop carries one current."},
            {"text": "is largest in front of the bulb, because the bulb has "
                     "not taken its share yet", "correct": False,
             "why": "The bulb takes energy, not charge. The same amount of "
                    "charge goes past every point."},
            {"text": "cannot be compared, because the two positions are "
                     "measuring different things", "correct": False,
             "why": "Both positions measure the current in the same single "
                    "loop, which is one quantity."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-s04",
        "band": "standard",
        "text": "Why does a metal conduct while a piece of plastic of the "
                "same shape does not?",
        "options": [
            {"text": "The metal is heavier, and heavier materials carry "
                     "charge better", "correct": False,
             "why": "Mass has nothing to do with it. Aluminium is light and "
                    "conducts very well."},
            {"text": "The metal is smoother inside, so the charge slides "
                     "through it", "correct": False,
             "why": "There is no sliding surface inside a solid. What "
                    "matters is whether any charges are free to move."},
            {"text": "The metal has electrons that are free to move; the "
                     "plastic has none", "correct": True},
            {"text": "The metal makes new electrons when the cell is "
                     "connected", "correct": False,
             "why": "No electrons are made or destroyed. The metal's own "
                    "electrons are simply pushed along."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p8-01-h01",
        "band": "harder",
        "text": "A student says the electrons rush from the cell to the bulb "
                "at nearly the speed of light. What is wrong with that?",
        "options": [
            {"text": "The electrons drift very slowly; it is the PUSH that "
                     "travels through them at close to the speed of light",
             "correct": True},
            {"text": "Nothing is wrong — that is exactly what happens",
             "correct": False,
             "why": "The lamp does light instantly, but not because "
                    "electrons made the journey. They drift under a "
                    "millimetre a second."},
            {"text": "The electrons travel the other way, from the bulb to "
                     "the cell", "correct": False,
             "why": "Electrons in a metal do drift from − to +, which is the "
                    "opposite of the conventional arrow, but they still "
                    "drift very slowly."},
            {"text": "Electrons cannot move through a solid metal at all, "
                     "so what travels is a wave of energy passed from one "
                     "fixed electron to the next", "correct": False,
             "why": "They can move, and they do — slowly. A metal's loose "
                    "electrons drifting is exactly what makes it a "
                    "conductor."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-h02",
        "band": "harder",
        "text": "A loop contains a cell and a buzzer. A student claims the "
                "wire returning to the cell carries \"used electricity\" "
                "that is thrown away. What should you tell them?",
        "options": [
            {"text": "The return wire carries less charge, but that is "
                     "normal and is not thrown away", "correct": False,
             "why": "It does not carry less. The two sides of the buzzer "
                    "carry identical currents."},
            {"text": "They are right, which is why the return wire is "
                     "usually thinner", "correct": False,
             "why": "Both wires carry the same current, so both are the same "
                    "thickness. Nothing is discarded."},
            {"text": "All the charge comes back; what the buzzer took was "
                     "energy, not charge", "correct": True},
            {"text": "The charge comes back but with less energy, so the "
                     "return wire is at a lower current", "correct": False,
             "why": "The first half is right and the second does not follow. "
                    "Less energy per charge does not mean less charge per "
                    "second."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-h03",
        "band": "harder",
        "text": "A torch works. Reverse the cell in the holder and press the "
                "switch. What happens?",
        "options": [
            {"text": "Nothing at all — a cell only pushes one way and a "
                     "reversed cell pushes nothing", "correct": False,
             "why": "A reversed cell pushes just as hard; it simply pushes "
                    "the other way round the loop."},
            {"text": "The bulb still lights, because a filament does not "
                     "care which way the charge goes through it",
             "correct": True},
            {"text": "The bulb lights twice as brightly, because the cell is "
                     "now pushing with the current instead of against it",
             "correct": False,
             "why": "There is no with or against. One cell gives one push, "
                    "whichever way round it sits."},
            {"text": "The bulb is damaged, because current through a "
                     "filament must always go the same way", "correct": False,
             "why": "A filament is just a thin wire. It heats up whichever "
                    "direction the charge drifts."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-h04",
        "band": "harder",
        "text": "Two identical torches are switched on. One has a cable a "
                "metre long between the cell and the bulb; the other has a "
                "cable a hundred metres long. Ignoring the resistance of the "
                "cable, what is the difference in how quickly each lights?",
        "options": [
            {"text": "The short one lights a hundred times sooner, because "
                     "the charge has a hundred times less far to go",
             "correct": False,
             "why": "No charge has to make the journey. The wire is already "
                    "full before the switch closes."},
            {"text": "The long one never lights, because the charge runs out "
                     "on the way", "correct": False,
             "why": "Charge does not run out. It is pushed round a ring, and "
                    "the ring is complete in both torches."},
            {"text": "The long one lights a little later, but far too little "
                     "to notice", "correct": True},
            {"text": "The long one lights first, because a longer wire holds "
                     "more electrons to start with", "correct": False,
             "why": "It does hold more electrons, and that changes nothing: "
                    "what matters is when the push arrives at the bulb."},
        ],
        "figure": None,
    },
]
