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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p8-01-e05",
        "band": "easier",
        "text": "When a current passes through a copper wire, what is "
                "actually moving?",
        "options": [
            {"text": "Free electrons that were already in the metal",
             "correct": True},
            {"text": "Electricity sent out from inside the cell",
             "correct": False,
             "why": "The cell pushes on charge that is already in the wire; it "
                    "sends nothing out of itself."},
            {"text": "The copper atoms, sliding along the wire",
             "correct": False,
             "why": "The atoms stay where they are, which is why the wire "
                    "keeps its shape and its mass."},
            {"text": "Heat, travelling from the cell to the lamp",
             "correct": False,
             "why": "Warming is a result of the current, not the thing that "
                    "flows round the loop."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-e06",
        "band": "easier",
        "text": "In a single loop containing a cell and a lamp, where is the "
                "current largest?",
        "options": [
            {"text": "In the wire going into the lamp", "correct": False,
             "why": "Nothing is used up in the lamp, so the same current "
                    "comes out as goes in."},
            {"text": "In the wire coming out of the lamp", "correct": False,
             "why": "The current is the same on both sides — neither wire "
                    "carries more."},
            {"text": "It is the same everywhere in the loop", "correct": True},
            {"text": "In the wire nearest the cell", "correct": False,
             "why": "Distance from the cell makes no difference; charge is "
                    "not handed out along the way."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-e07",
        "band": "easier",
        "text": "A wire is disconnected at one point in a single loop. What "
                "happens?",
        "options": [
            {"text": "Everything in the loop stops working", "correct": True},
            {"text": "Only the parts after the break stop working",
             "correct": False,
             "why": "A loop has no after: with the path broken anywhere, "
                    "nothing flows anywhere."},
            {"text": "Only the parts before the break stop working",
             "correct": False,
             "why": "Charge cannot flow into a dead end, so the whole loop "
                    "stops together."},
            {"text": "Everything keeps working but more dimly",
             "correct": False,
             "why": "A break is not a partial obstacle; there is no complete "
                    "path at all."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-e08",
        "band": "easier",
        "text": "Roughly how much current does a small torch bulb draw?",
        "options": [
            {"text": "A few thousandths of an amp", "correct": False,
             "why": "That is a hundred times too small — a few milliamps "
                    "would barely glow."},
            {"text": "A few hundred amps", "correct": False,
             "why": "That is enormous; a current like that melts wires and "
                    "welds metal."},
            {"text": "A few tenths of an amp", "correct": True},
            {"text": "A few thousand amps", "correct": False,
             "why": "That is more than a lightning strike delivers, and far "
                    "beyond any torch."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p8-01-s05",
        "band": "standard",
        "text": "A student claims the lamp uses up the current. Which "
                "measurement settles it?",
        "options": [
            {"text": "A voltmeter across the lamp, showing a reading",
             "correct": False,
             "why": "That measures energy given up per unit of charge, which "
                    "is a different quantity."},
            {"text": "Ammeters on both sides of the lamp, reading the same",
             "correct": True},
            {"text": "An ammeter beside the cell, reading more than zero",
             "correct": False,
             "why": "One reading cannot show whether anything was lost "
                    "further round the loop."},
            {"text": "Weighing the lamp before and after it is switched on",
             "correct": False,
             "why": "Charge has no measurable mass here, so a balance shows "
                    "nothing either way."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-s06",
        "band": "standard",
        "text": "Why must a circuit be a complete loop, rather than a wire "
                "that simply reaches the lamp?",
        "options": [
            {"text": "Because the lamp needs current arriving from both sides "
                     "at once",
             "correct": False,
             "why": "The current passes through in one direction; what it "
                    "needs is a path onwards."},
            {"text": "Because the second wire carries the electricity that "
                     "was not used",
             "correct": False,
             "why": "None of it is used up. Both wires carry exactly the same "
                    "current."},
            {"text": "Because the charge needs a complete path back, or "
                     "nothing flows at all",
             "correct": True},
            {"text": "Because two wires halve the current and keep the lamp "
                     "safe",
             "correct": False,
             "why": "Nothing is halved; both wires are part of the one loop "
                    "carrying one current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-s07",
        "band": "standard",
        "text": "A student writes that a cell holds a store of current and "
                "sends it out. Which correction is right?",
        "options": [
            {"text": "A cell holds a store of current but releases it slowly",
             "correct": False,
             "why": "It holds no current at any rate. Current is a flow, not "
                    "something that can be kept."},
            {"text": "A cell holds a chemical store and pushes on charge that "
                     "is already in the wire",
             "correct": True},
            {"text": "A cell holds a store of electrons and pumps them into "
                     "the circuit",
             "correct": False,
             "why": "The wire is already full of free electrons; the cell "
                    "adds none of its own."},
            {"text": "A cell holds a store of voltage and shares it out",
             "correct": False,
             "why": "Potential difference is not held either — it is the "
                    "energy given up between two points."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-s08",
        "band": "standard",
        "text": "A loop is complete except for a small gap of air. Why does "
                "no current flow, even though the cell still pushes?",
        "options": [
            {"text": "Because air is too light for the electrons to push "
                     "through",
             "correct": False,
             "why": "Weight is not the issue; what matters is whether there "
                    "are charges free to move."},
            {"text": "Because the cell only works when the loop is short",
             "correct": False,
             "why": "Loop length barely matters. The gap is what stops it."},
            {"text": "Because the push is used up crossing the gap",
             "correct": False,
             "why": "Nothing crosses the gap at all, so nothing can be used "
                    "up doing it."},
            {"text": "Because air has almost no free charges, so the loop is "
                     "not complete",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p8-01-h05",
        "band": "harder",
        "text": "An ammeter reads 0.30 A leaving a cell and 0.30 A returning "
                "to it. What does that show, and what IS used up?",
        "options": [
            {"text": "Charge is not used up anywhere in the loop; energy is",
             "correct": True},
            {"text": "Both charge and energy are conserved, so nothing is "
                     "used up anywhere",
             "correct": False,
             "why": "The cell's chemical store really does empty, so "
                    "something is being spent."},
            {"text": "Charge is used up, and the meters are not sensitive "
                     "enough to show it",
             "correct": False,
             "why": "The equality is exact, not a limit of the meters; charge "
                    "is genuinely conserved."},
            {"text": "Energy is not used up either, because it returns to the "
                     "cell",
             "correct": False,
             "why": "It leaves the lamp as light and warmth and never comes "
                    "back to the cell."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-h06",
        "band": "harder",
        "text": "Two identical cells are put in a holder facing in opposite "
                "directions, in one loop with a lamp. What happens?",
        "options": [
            {"text": "The lamp is twice as bright, because two cells are "
                     "present",
             "correct": False,
             "why": "Two cells add only when they push the same way round the "
                    "loop."},
            {"text": "The lamp is as bright as with one cell", "correct": False,
             "why": "One does not simply drop out; the second actively pushes "
                    "against the first."},
            {"text": "The lamp stays dark, because the two pushes cancel",
             "correct": True},
            {"text": "The lamp lights, but the current flows the other way "
                     "round",
             "correct": False,
             "why": "Neither push wins: they are equal and opposite, so there "
                    "is nothing left to drive a current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-h07",
        "band": "harder",
        "text": "A torch is rebuilt with the filament lamp connected the "
                "other way round. What happens when the switch is closed?",
        "options": [
            {"text": "It lights exactly as it did before the change",
             "correct": True},
            {"text": "It stays dark, because current can only pass one way "
                     "through a lamp",
             "correct": False,
             "why": "That is true of a diode, not of a filament lamp, which "
                    "simply heats a wire."},
            {"text": "It lights, but much more dimly than before",
             "correct": False,
             "why": "Nothing about the filament changes with direction, so "
                    "the brightness is the same."},
            {"text": "It lights and then fails, because the current runs "
                     "backwards through it",
             "correct": False,
             "why": "A filament is heated by the current whichever way it "
                    "passes, and takes no harm from it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-h08",
        "band": "harder",
        "text": "A closed loop of copper wire with no cell in it is still "
                "full of free electrons. Why is there no current?",
        "options": [
            {"text": "Because the electrons have all been used up by earlier "
                     "circuits",
             "correct": False,
             "why": "They are part of the metal itself and are never used "
                    "up."},
            {"text": "Because free electrons only appear once a cell is "
                     "connected",
             "correct": False,
             "why": "They are there in every piece of metal, connected or "
                    "not."},
            {"text": "Because a loop with no cell is not a complete circuit",
             "correct": False,
             "why": "The loop is complete; what it lacks is anything to push "
                    "the electrons one way."},
            {"text": "Because nothing pushes them the same way, so they move "
                     "randomly instead of drifting",
             "correct": True},
        ],
        "figure": None,
    },
]
