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
        "options": [            {"text": "In the wire going into the lamp", "correct": False,
             "why": "Nothing is used up in the lamp, so the same current "
                    "comes out as goes in."},
            {"text": "In the wire coming out of the lamp", "correct": False,
             "why": "The current is the same on both sides — neither wire "
                    "carries more."},
            {"text": "In the wire nearest the cell", "correct": False,
             "why": "Distance from the cell makes no difference; charge is "
                    "not handed out along the way."},
            {"text": "It is the same everywhere in the loop", "correct": True},
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
        "options": [            {"text": "A few thousandths of an amp", "correct": False,
             "why": "That is a hundred times too small — a few milliamps "
                    "would barely glow."},
            {"text": "A few hundred amps", "correct": False,
             "why": "That is enormous; a current like that melts wires and "
                    "welds metal."},
            {"text": "A few thousand amps", "correct": False,
             "why": "That is more than a lightning strike delivers, and far "
                    "beyond any torch."},
            {"text": "A few tenths of an amp", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p8-01-s05",
        "band": "standard",
        "text": "A student claims the lamp uses up the current. Which "
                "measurement settles it?",
        "options": [            {"text": "A voltmeter across the lamp, showing a reading",
             "correct": False,
             "why": "That measures energy given up per unit of charge, which "
                    "is a different quantity."},
            {"text": "Weighing the lamp before and after it is switched on",
             "correct": False,
             "why": "Charge has no measurable mass here, so a balance shows "
                    "nothing either way."},
            {"text": "An ammeter beside the cell, reading more than zero",
             "correct": False,
             "why": "One reading cannot show whether anything was lost "
                    "further round the loop."},
            {"text": "Ammeters on both sides of the lamp, reading the same",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-s06",
        "band": "standard",
        "text": "Why must a circuit be a complete loop, rather than a wire "
                "that simply reaches the lamp?",
        "options": [            {"text": "Because the lamp needs current arriving from both sides "
                     "at once",
             "correct": False,
             "why": "The current passes through in one direction; what it "
                    "needs is a path onwards."},
            {"text": "Because the second wire carries the electricity that "
                     "was not used",
             "correct": False,
             "why": "None of it is used up. Both wires carry exactly the same "
                    "current."},
            {"text": "Because two wires halve the current and keep the lamp "
                     "safe",
             "correct": False,
             "why": "Nothing is halved; both wires are part of the one loop "
                    "carrying one current."},
            {"text": "Because the charge needs a complete path back, or "
                     "nothing flows at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-01-s07",
        "band": "standard",
        "text": "A student writes that a cell holds a store of current and "
                "sends it out. Which correction is right?",
        "options": [            {"text": "A cell holds a store of current but releases it slowly",
             "correct": False,
             "why": "It holds no current at any rate. Current is a flow, not "
                    "something that can be kept."},
            {"text": "A cell holds a store of voltage and shares it out",
             "correct": False,
             "why": "Potential difference is not held either — it is the "
                    "energy given up between two points."},
            {"text": "A cell holds a store of electrons and pumps them into "
                     "the circuit",
             "correct": False,
             "why": "The wire is already full of free electrons; the cell "
                    "adds none of its own."},
            {"text": "A cell holds a chemical store and pushes on charge that "
                     "is already in the wire",
             "correct": True},
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
        "options": [            {"text": "The lamp is twice as bright, because two cells are "
                     "present",
             "correct": False,
             "why": "Two cells add only when they push the same way round the "
                    "loop."},
            {"text": "The lamp is as bright as with one cell", "correct": False,
             "why": "One does not simply drop out; the second actively pushes "
                    "against the first."},
            {"text": "The lamp lights, but the current flows the other way "
                     "round",
             "correct": False,
             "why": "Neither push wins: they are equal and opposite, so there "
                    "is nothing left to drive a current."},
            {"text": "The lamp stays dark, because the two pushes cancel",
             "correct": True},
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

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────
    {"id": "p8-01-e09", "band": "easier",
     "text": "In the circuit symbols, two long-and-short line pairs drawn one "
             "after the other represent…",
     "options": [
         {"text": "a switch", "correct": False,
          "why": "A switch is two contacts with a lever, not a pair of "
                 "lines."},
         {"text": "a resistor", "correct": False,
          "why": "A resistor is drawn as a plain rectangle in the wire."},
         {"text": "a battery", "correct": True},
         {"text": "a lamp", "correct": False,
          "why": "A lamp is a circle with a cross through it, not a set of "
                 "parallel lines."},
     ], "figure": None},
    {"id": "p8-01-e10", "band": "easier",
     "text": "One long line and one short line, side by side, is the symbol "
             "for…",
     "options": [
         {"text": "an ammeter", "correct": False,
          "why": "An ammeter is a circle with the letter A inside it, not a "
                 "pair of lines."},
         {"text": "a variable resistor", "correct": False,
          "why": "A variable resistor is a rectangle with a diagonal arrow "
                 "drawn across it."},
         {"text": "a cell", "correct": True},
         {"text": "a battery", "correct": False,
          "why": "A battery needs two or more of these pairs in a row; one "
                 "pair on its own is a single cell."},
     ], "figure": None},
    {"id": "p8-01-e11", "band": "easier",
     "text": "A switch that is open is drawn as…",
     "options": [
         {"text": "a circle with a cross inside it", "correct": False,
          "why": "That symbol is a lamp, not a switch."},
         {"text": "a plain rectangle sitting in the wire, drawn with a "
                  "gap along one edge", "correct": False,
          "why": "A plain rectangle is a resistor. A switch has moving "
                 "contacts, not a fixed shape."},
         {"text": "a circle with the capital letter A drawn inside it",
          "correct": False,
          "why": "That is the ammeter symbol. A switch has no letter inside "
                 "it at all."},
         {"text": "two contacts with a lever lifted away from one of them",
          "correct": True},
     ], "figure": None},
    {"id": "p8-01-e12", "band": "easier",
     "text": "A plain rectangle drawn in the wire, with nothing else added to "
             "it, is the symbol for…",
     "options": [
         {"text": "a fixed resistor", "correct": True},
         {"text": "a variable resistor", "correct": False,
          "why": "A variable resistor is the same rectangle with a diagonal "
                 "arrow added across it."},
         {"text": "a switch", "correct": False,
          "why": "A switch has two contacts and a lever, never a plain "
                 "rectangle."},
         {"text": "a battery", "correct": False,
          "why": "A battery is drawn as long and short lines, not a "
                 "rectangle."},
     ], "figure": None},
    {"id": "p8-01-e13", "band": "easier",
     "text": "What turns a plain resistor's symbol into a variable "
             "resistor's symbol?",
     "options": [
         {"text": "A second, smaller rectangle drawn inside the first",
          "correct": False,
          "why": "Nothing is nested inside it. The extra mark is a line "
                 "crossing the rectangle, not a second shape."},
         {"text": "A diagonal arrow drawn across the rectangle",
          "correct": True},
         {"text": "A dashed outline instead of a solid one", "correct": False,
          "why": "The outline stays solid. What changes is a line added "
                 "across it."},
         {"text": "A letter written above the rectangle", "correct": False,
          "why": "Meters carry letters inside a circle; a variable resistor "
                 "carries an arrow, not a letter."},
     ], "figure": None},
    {"id": "p8-01-e14", "band": "easier",
     "text": "A circle with the letter V inside it, rather than the letter "
             "A, is the symbol for…",
     "options": [
         {"text": "a voltmeter", "correct": True},
         {"text": "an ammeter", "correct": False,
          "why": "An ammeter carries the letter A inside its circle, not V."},
         {"text": "a cell", "correct": False,
          "why": "A cell is drawn as a long line and a short line, with no "
                 "circle at all."},
         {"text": "a variable resistor", "correct": False,
          "why": "A variable resistor is a rectangle with an arrow, not a "
                 "lettered circle."},
     ], "figure": None},
    {"id": "p8-01-e15", "band": "easier",
     "text": "In an equation, current is usually represented by the letter…",
     "options": [
         {"text": "C", "correct": False,
          "why": "C is not used for current; it more often stands for a "
                 "capacitance or a coulomb of charge."},
         {"text": "A", "correct": False,
          "why": "A is the unit symbol for the ampere, not the letter used "
                 "for the quantity itself."},
         {"text": "I", "correct": True},
         {"text": "Q", "correct": False,
          "why": "Q is the letter used for charge, which is a different "
                 "quantity from current."},
     ], "figure": None},
    {"id": "p8-01-e16", "band": "easier",
     "text": "A switch in a single loop is left open. What does an ammeter "
             "anywhere in that loop read?",
     "options": [
         {"text": "A small but non-zero current", "correct": False,
          "why": "An open switch is a complete gap, not a narrow path. "
                 "Nothing flows at all."},
         {"text": "Whatever it read the last time the switch was closed",
          "correct": False,
          "why": "A meter reads what is happening now. With the loop open "
                 "there is nothing to read."},
         {"text": "It depends how long ago the switch was closed",
          "correct": False,
          "why": "Time since the switch was last closed makes no "
                 "difference; an open loop reads zero straight away."},
         {"text": "0.00 A — nothing is flowing", "correct": True},
     ], "figure": None},
    {"id": "p8-01-e17", "band": "easier",
     "text": "Before a torch is ever switched on, are there already free "
             "electrons spread through its wires?",
     "options": [
         {"text": "No — the cell sends electrons into the wire once the "
                  "switch closes", "correct": False,
          "why": "A cell adds none of its own. The metal's own electrons "
                 "were already there before anything was switched on."},
         {"text": "No — electrons only appear once a current starts flowing",
          "correct": False,
          "why": "The electrons exist in the metal whether or not a current "
                 "is flowing. Flowing is something they start doing, not "
                 "something that creates them."},
         {"text": "Only in the part of the wire nearest the cell",
          "correct": False,
          "why": "They fill every part of the metal equally, not just the "
                 "section closest to the cell."},
         {"text": "Yes — the wire is already full of them, waiting to be "
                  "pushed", "correct": True},
     ], "figure": None},
    {"id": "p8-01-e18", "band": "easier",
     "text": "A circuit with a gap in it, so that no current can flow, is "
             "called…",
     "options": [
         {"text": "a short circuit", "correct": False,
          "why": "A short circuit is an unwanted low-resistance path, not a "
                 "gap. It usually carries a very large current, not none at "
                 "all."},
         {"text": "an open circuit", "correct": True},
         {"text": "a series circuit", "correct": False,
          "why": "Series describes how components are arranged, not "
                 "whether the loop is complete."},
         {"text": "a live circuit", "correct": False,
          "why": "\"Live\" describes a circuit connected to a supply, which "
                 "is the opposite state from having a gap that stops the "
                 "flow."},
     ], "figure": None},
    {"id": "p8-01-e19", "band": "easier",
     "text": "The coulomb is the unit of…",
     "options": [
         {"text": "current", "correct": False,
          "why": "Current is measured in amperes. A coulomb measures the "
                 "charge that current carries."},
         {"text": "energy", "correct": False,
          "why": "Energy is measured in joules, a different quantity from "
                 "the amount of charge that has flowed."},
         {"text": "charge", "correct": True},
         {"text": "resistance", "correct": False,
          "why": "Resistance is measured in ohms and describes how hard a "
                 "component makes it for charge to get through."},
     ], "figure": None},
    {"id": "p8-01-e20", "band": "easier",
     "text": "Roughly how many electrons make up a single coulomb of "
             "charge?",
     "options": [
         {"text": "About six thousand", "correct": False,
          "why": "That is far too small a number — a single electron's "
                 "charge is tiny, so it takes an enormous number of them to "
                 "add up to one coulomb."},
         {"text": "About six million", "correct": False,
          "why": "Still nowhere near enough. The true figure is millions of "
                 "millions of millions."},
         {"text": "About six million million million", "correct": True},
         {"text": "Exactly one, by definition", "correct": False,
          "why": "A coulomb is not the charge on one electron; it is a "
                 "far larger, everyday-sized unit built from a vast number "
                 "of them."},
     ], "figure": None},
    {"id": "p8-01-e21", "band": "easier",
     "text": "The ampere, the unit of current, is named after…",
     "options": [
         {"text": "André-Marie Ampère", "correct": True},
         {"text": "Alessandro Volta", "correct": False,
          "why": "Volta gives his name to the volt, the unit of potential "
                 "difference, not the amp."},
         {"text": "Georg Ohm", "correct": False,
          "why": "Ohm gives his name to the ohm, the unit of resistance."},
         {"text": "Michael Faraday", "correct": False,
          "why": "Faraday's name is attached to the farad, a unit used for "
                 "capacitance, not current."},
     ], "figure": None},
    {"id": "p8-01-e22", "band": "easier",
     "text": "Roughly what current does a phone charger supply while "
             "charging?",
     "options": [
         {"text": "About 1 A", "correct": True},
         {"text": "About 0.001 A", "correct": False,
          "why": "That is a thousand times too small — a charger that weak "
                 "would take days to charge a phone."},
         {"text": "About 100 A", "correct": False,
          "why": "That is enormous for a small plug — a current that size "
                 "would need a cable far thicker than a charging lead."},
         {"text": "About 1000 A", "correct": False,
          "why": "That is close to the current a factory furnace might use, "
                 "nowhere near a phone charger."},
     ], "figure": None},
    {"id": "p8-01-e23", "band": "easier",
     "text": "Roughly what current does a mains kettle draw while it is "
             "boiling?",
     "options": [
         {"text": "About 0.01 A", "correct": False,
          "why": "That is far too small to heat a kettle full of water in "
                 "any reasonable time."},
         {"text": "About 10 A", "correct": True},
         {"text": "About 1000 A", "correct": False,
          "why": "A current that size would need mains cabling much "
                 "thicker than a kettle's flex, and would trip a house's "
                 "supply instantly."},
         {"text": "About 0.5 A", "correct": False,
          "why": "That is closer to a small charger. A kettle's heating "
                 "element needs far more current to boil water quickly."},
     ], "figure": None},
    {"id": "p8-01-e24", "band": "easier",
     "text": "Roughly what current does a small indicator LED draw?",
     "options": [
         {"text": "About 2 A", "correct": False,
          "why": "That is a hundred times too large for a small indicator "
                 "light, which barely warms up in use."},
         {"text": "About 20 A", "correct": False,
          "why": "A current that size is closer to a kettle or a heater, "
                 "not a tiny LED."},
         {"text": "About 0.00002 A", "correct": False,
          "why": "That is far too small — a current that tiny would give "
                 "no visible light at all."},
         {"text": "About 0.02 A", "correct": True},
     ], "figure": None},
    {"id": "p8-01-e25", "band": "easier",
     "text": "Roughly what current does a car's headlamp draw?",
     "options": [
         {"text": "About 0.05 A", "correct": False,
          "why": "That is close to a small LED, far too little to light a "
                 "headlamp brightly."},
         {"text": "About 500 A", "correct": False,
          "why": "That is close to what a car's starter motor briefly "
                 "draws, not an ordinary headlamp."},
         {"text": "About 50 A", "correct": False,
          "why": "That is ten times too large for a headlamp bulb, which "
                 "runs steadily for hours on a car's battery."},
         {"text": "About 5 A", "correct": True},
     ], "figure": None},
    {"id": "p8-01-e26", "band": "easier",
     "text": "A piece of copper wire sits on a bench, not connected to "
             "anything. Are its free electrons moving?",
     "options": [
         {"text": "No — they only move once a cell is connected",
          "correct": False,
          "why": "They are free to move whether or not a cell is connected; "
                 "what a cell adds is a push in one direction."},
         {"text": "Yes, but randomly, with no overall drift in one "
                  "direction", "correct": True},
         {"text": "Yes, and they are already drifting steadily towards one "
                  "end", "correct": False,
          "why": "A steady drift in one direction needs something pushing "
                 "them that way. With nothing connected, there is no such "
                 "push."},
         {"text": "No — the electrons stay fixed in place until a current "
                  "starts", "correct": False,
          "why": "They are not fixed; the electrons that make a metal "
                 "conduct are free to move even before a current is "
                 "flowing."},
     ], "figure": None},
    {"id": "p8-01-e27", "band": "easier",
     "text": "What two things does a piece of wire need for a current to "
             "flow through it?",
     "options": [
         {"text": "A push from a source such as a cell, and a complete "
                  "path back to it", "correct": True},
         {"text": "A push from a source such as a cell, and enough time for "
                  "the electricity to travel along the wire", "correct": False,
          "why": "No travel time is needed — the wire is already full of "
                 "electrons before the push arrives."},
         {"text": "A complete path, and a store of extra electrons loaded "
                  "into the wire beforehand", "correct": False,
          "why": "No extra electrons need loading in. The ones already in "
                 "the metal are enough; what is missing without a source is "
                 "the push."},
         {"text": "A push from a source such as a cell, and a component "
                  "such as a bulb to use the current up", "correct": False,
          "why": "A bulb is not needed for current to flow, and nothing "
                 "uses the current up in any case — a plain wire loop "
                 "carries a current too."},
     ], "figure": None},
    {"id": "p8-01-e28", "band": "easier",
     "text": "By long-standing convention, which way is current drawn "
             "flowing in a circuit diagram, and is that the way the "
             "electrons actually move?",
     "options": [
         {"text": "From + to −, and the electrons drift the same way",
          "correct": False,
          "why": "The direction is right and the second half is not: the "
                 "electrons actually drift the other way round."},
         {"text": "From + to −, and the electrons drift the opposite way",
          "correct": True},
         {"text": "From − to +, and the electrons drift the same way",
          "correct": False,
          "why": "Conventional current is drawn from + to −, not the other "
                 "way round."},
         {"text": "From − to +, and the electrons drift the opposite way",
          "correct": False,
          "why": "The conventional direction itself is the wrong way round "
                 "here; it runs from + to −."},
     ], "figure": None},
    {"id": "p8-01-e29", "band": "easier",
     "text": "Roughly what current can a large lightning strike carry, for "
             "the brief instant it lasts?",
     "options": [
         {"text": "About 30 A", "correct": False,
          "why": "That is only about a hundred times a torch bulb's "
                 "current — far too small for a lightning strike."},
         {"text": "About 300 A", "correct": False,
          "why": "Still far too small. A lightning strike briefly carries a "
                 "current a hundred times larger than this."},
         {"text": "About 30 000 A", "correct": True},
         {"text": "About 3 A", "correct": False,
          "why": "That is barely more than a torch bulb draws, nowhere near "
                 "the huge current in a lightning strike."},
     ], "figure": None},
    {"id": "p8-01-e30", "band": "easier",
     "text": "Why is a circuit diagram drawn using agreed symbols joined by "
             "straight lines, rather than a picture of the real "
             "apparatus?",
     "options": [
         {"text": "So that it takes up less space on the page than a "
                  "drawing of the apparatus would", "correct": False,
          "why": "Saving space is not the reason; a hand-drawn sketch of "
                 "the apparatus could be made small too."},
         {"text": "So that the diagram shows exactly how large each "
                  "component is in real life", "correct": False,
          "why": "Symbols do not show real size at all — a huge resistor "
                 "and a tiny one are drawn with the same rectangle."},
         {"text": "So that anyone, anywhere, can build the exact same "
                  "circuit from the same diagram", "correct": True},
         {"text": "So that only trained engineers are able to read it",
          "correct": False,
          "why": "The opposite is true: agreed symbols make a diagram "
                 "readable by anyone who has learned the small, fixed set of "
                 "them."},
     ], "figure": None},

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────
    {"id": "p8-01-s09", "band": "standard",
     "text": "A torch runs on two cells facing the same way, giving an "
             "ammeter reading of a certain size. A third cell is added the "
             "wrong way round. What happens to the reading?",
     "options": [
         {"text": "It falls to what a single forward cell alone would give",
          "correct": True},
         {"text": "It falls to zero, because the reversed cell cancels the "
                  "whole push", "correct": False,
          "why": "One reversed cell cancels one forward cell and no more; "
                 "the remaining forward cell still drives the loop."},
         {"text": "It stays the same, because three cells still outnumber "
                  "the reversed one", "correct": False,
          "why": "The reversed cell does not get outvoted. It cancels an "
                 "equal forward push, leaving only the net difference."},
         {"text": "It rises, because there are now more cells in the "
                  "holder overall", "correct": False,
          "why": "Adding a cell the wrong way round works against the "
                 "others rather than adding to them."},
     ], "figure": None},
    {"id": "p8-01-s10", "band": "standard",
     "text": "A buzzer, not a bulb, sits in a single loop with a cell. Two "
             "ammeters either side of the buzzer are compared. What do you "
             "expect, and why?",
     "options": [
         {"text": "A smaller reading after the buzzer, because sound takes "
                  "some of the current", "correct": False,
          "why": "Sound is carried away as a form of energy, not as "
                 "charge. The current is unchanged by it."},
         {"text": "A smaller reading after the buzzer while it is sounding, "
                  "but not the rest of the time", "correct": False,
          "why": "The two readings match whether or not the buzzer happens "
                 "to be sounding at that instant; charge is still not "
                 "used up."},
         {"text": "A larger reading after the buzzer, because the buzzer "
                  "adds energy to the charge passing through", "correct": False,
          "why": "A buzzer takes energy from the charge rather than "
                 "adding any, and either way the current itself would be "
                 "unaffected."},
         {"text": "Equal readings, because charge is not used up by the "
                  "buzzer any more than it is by a bulb", "correct": True},
     ], "figure": None},
    {"id": "p8-01-s11", "band": "standard",
     "text": "A torch's bulb gradually dims over an evening of use until it "
             "goes out. Has the current been \"used up\" over that time?",
     "options": [
         {"text": "Yes — a fixed amount of current was stored in the cells "
                  "at the start and it has run out", "correct": False,
          "why": "Current is not a store to run down. What is stored is "
                 "chemical energy in the cells."},
         {"text": "No — the cells' chemical store is running down, which "
                  "makes the push weaker and the ammeter reading fall",
          "correct": True},
         {"text": "Yes, but just the current in the return wire — the "
                  "current going into the bulb is unaffected", "correct": False,
          "why": "The current is the same on both sides of the bulb at "
                 "every instant; it is not selectively used up on one "
                 "side."},
         {"text": "No — the bulb itself wears out and starts resisting "
                  "the current less, which is unrelated to the cells",
          "correct": False,
          "why": "It is the cells weakening, not the bulb, that causes the "
                 "dimming here — a torch dims as its batteries run down "
                 "even with a perfectly healthy bulb."},
     ], "figure": None},
    {"id": "p8-01-s12", "band": "standard",
     "text": "Two ammeters sit at different points of a single loop "
             "containing one resistor and one cell. One reads 0.18 A. What "
             "must the other read?",
     "options": [
         {"text": "More than 0.18 A, if it is placed nearer the cell",
          "correct": False,
          "why": "Position round the loop makes no difference to a single "
                 "current; nearer the cell is not a bigger reading."},
         {"text": "Less than 0.18 A, because the resistor has taken a "
                  "share of it by the time it gets there", "correct": False,
          "why": "A resistor does not remove any charge from the flow — "
                 "it only makes the flow harder to push, which is why the "
                 "meters still agree."},
         {"text": "0.18 A, because a single loop carries one current at "
                  "every point", "correct": True},
         {"text": "It cannot be worked out without knowing exactly where "
                  "in the loop the resistor sits", "correct": False,
          "why": "The position of the resistor changes nothing about the "
                 "one current shared by the whole loop."},
     ], "figure": None},
    {"id": "p8-01-s13", "band": "standard",
     "text": "In a description of a circuit, conventional current is said to "
             "flow clockwise round the single loop. Which way are the free "
             "electrons in the wire actually drifting?",
     "options": [
         {"text": "Clockwise, the same way as the conventional current",
          "correct": False,
          "why": "Electrons drift the opposite way to the conventional "
                 "arrow, by the long-standing convention for which "
                 "direction current is drawn."},
         {"text": "In both directions at once, cancelling out to leave no "
                  "overall drift at all", "correct": False,
          "why": "There is a single overall drift direction once the loop "
                 "is closed; nothing cancels it out."},
         {"text": "Anticlockwise, the opposite way to the conventional "
                  "current", "correct": True},
         {"text": "It depends on which terminal of the cell is drawn on "
                  "the left", "correct": False,
          "why": "Left or right on the page changes nothing about the "
                 "physical relationship between the two directions."},
     ], "figure": None},
    {"id": "p8-01-s14", "band": "standard",
     "text": "How do you tell an ammeter symbol and a voltmeter symbol apart "
             "on a circuit diagram, given that both are circles?",
     "options": [
         {"text": "By counting how many wires connect to it — an ammeter "
                  "has two and a voltmeter has four", "correct": False,
          "why": "Both meters connect with exactly two leads. What "
                 "differs is where those leads are wired, not how many "
                 "there are."},
         {"text": "By the size of the circle — a voltmeter's is drawn "
                  "larger", "correct": False,
          "why": "Both circles are drawn the same size. The difference is "
                 "the letter inside, not the size of the shape."},
         {"text": "By the letter written inside the circle — A for an "
                  "ammeter, V for a voltmeter", "correct": True},
         {"text": "There is no reliable way to tell; you have to know "
                  "which measurement the diagram is about", "correct": False,
          "why": "The letter inside the circle identifies the meter "
                 "unambiguously, without needing any other information."},
     ], "figure": None},
    {"id": "p8-01-s15", "band": "standard",
     "text": "Which of these ordinarily draws the smallest current: a "
             "small indicator LED, a mains kettle, or a car headlamp?",
     "options": [
         {"text": "The mains kettle", "correct": False,
          "why": "The kettle's current is the largest of the three named "
                 "here, not the smallest."},
         {"text": "The car headlamp", "correct": False,
          "why": "The headlamp draws more than the indicator LED, though "
                 "less than the kettle."},
         {"text": "The indicator LED", "correct": True},
         {"text": "They are all roughly the same size", "correct": False,
          "why": "The three values span from hundredths of an amp to "
                 "double figures — nowhere near the same size."},
     ], "figure": None},
    {"id": "p8-01-s16", "band": "standard",
     "text": "An ammeter is designed to have almost no resistance of its "
             "own. Why does that matter for the reading it gives?",
     "options": [
         {"text": "So that it can be connected across a component, like a "
                  "voltmeter, without disturbing the circuit", "correct": False,
          "why": "An ammeter still has to be wired into the loop, not "
                 "across a component — that is the voltmeter's job."},
         {"text": "So that inserting it into the loop does not itself "
                  "reduce the very current it is trying to measure",
          "correct": True},
         {"text": "So that it can survive being connected the wrong way "
                  "round without being damaged", "correct": False,
          "why": "Having almost no resistance is unrelated to which way "
                 "round it is connected; it is about not obstructing the "
                 "flow."},
         {"text": "So that it warms up quickly, which is what is supposed "
                  "to make its needle settle on a reading faster",
          "correct": False,
          "why": "Warming up is not how a meter gives its reading, and "
                 "low resistance actually keeps a meter cooler, not "
                 "warmer."},
     ], "figure": None},
    {"id": "p8-01-s17", "band": "standard",
     "text": "A motor is connected into a single loop instead of a bulb. Two "
             "ammeters, one either side of the motor, are compared while it "
             "runs. What do you expect?",
     "options": [
         {"text": "A smaller reading after the motor, because some of the "
                  "current is converted into the motor's motion",
          "correct": False,
          "why": "Current is not converted into motion. What the motor "
                 "converts is the energy the charge is carrying."},
         {"text": "A smaller reading after the motor while it is working "
                  "hard, but not otherwise", "correct": False,
          "why": "The two readings stay equal at every instant, loaded or "
                 "not, because charge is conserved round the loop either "
                 "way."},
         {"text": "It depends on how fast the motor is spinning and how "
                  "much mechanical load it is carrying at that particular "
                  "moment", "correct": False,
          "why": "Speed can change how much current the motor draws "
                 "overall, but the two meters either side of it still "
                 "agree with each other."},
         {"text": "Equal readings, because the motor takes energy from the "
                  "charge rather than using the charge itself up",
          "correct": True},
     ], "figure": None},
    {"id": "p8-01-s18", "band": "standard",
     "text": "A student says a variable resistor's symbol is just \"a "
             "resistor with an arrow for decoration\". What is the arrow "
             "actually showing?",
     "options": [
         {"text": "That the value of the resistance can be changed",
          "correct": True},
         {"text": "The direction conventional current flows through it",
          "correct": False,
          "why": "Direction is not shown by a variable resistor's arrow; "
                 "an arrow with that meaning is not part of this symbol."},
         {"text": "That the component works in one direction and stops "
                  "current in the other", "correct": False,
          "why": "A resistor, fixed or variable, works the same whichever "
                 "way round it is connected."},
         {"text": "That it can be swapped out for a different component "
                  "entirely", "correct": False,
          "why": "The symbol shows one adjustable component, not an "
                 "invitation to swap it for something else."},
     ], "figure": None},
    {"id": "p8-01-s19", "band": "standard",
     "text": "A single loop holds a cell and a heater element. Doubling the "
             "time the switch stays closed does what to the current an "
             "ammeter reads at any one instant?",
     "options": [
         {"text": "Roughly doubles it, because twice the time means twice "
                  "the total amount of charge that has gone all the way "
                  "round the loop", "correct": False,
          "why": "A reading at one instant is not affected by how long the "
                 "switch has already been closed."},
         {"text": "Halves it, because the charge already used cannot be "
                  "used a second time, so half of it has gone by "
                  "then", "correct": False,
          "why": "No charge is used up by the heater in the first place, "
                 "so there is nothing being depleted over time."},
         {"text": "It falls steadily to zero as the loop \"empties\" of "
                  "charge", "correct": False,
          "why": "A loop does not empty of charge — the same electrons "
                 "keep drifting round it for as long as the switch stays "
                 "closed."},
         {"text": "Nothing — the reading at any instant depends on the "
                  "loop, not on how long it has already been running",
          "correct": True},
     ], "figure": None},
    {"id": "p8-01-s20", "band": "standard",
     "text": "Roughly how many times bigger is the current in a mains "
             "kettle (about 10 A) than in a small indicator LED (about "
             "0.02 A)?",
     "options": [
         {"text": "About 5 times", "correct": False,
          "why": "That divides 10 by 2 rather than by 0.02, giving far too "
                 "small a ratio."},
         {"text": "About 50 times bigger", "correct": False,
          "why": "That treats the LED's current as 0.2 A rather than "
                 "0.02 A, which is ten times too large."},
         {"text": "About 500 times", "correct": True},
         {"text": "About 5000 times", "correct": False,
          "why": "That overshoots — dividing 10 A by 0.02 A gives hundreds, "
                 "not thousands, of times bigger."},
     ], "figure": None},
    {"id": "p8-01-s21", "band": "standard",
     "text": "A student claims that because a cell is drawn with a long "
             "line and a short line, the long line carries \"more "
             "electricity\". What is wrong with that idea?",
     "options": [
         {"text": "The lines should be reversed — the short line is the "
                  "positive terminal instead", "correct": False,
          "why": "By convention the long line is positive; the student's "
                 "error is not about which line is which."},
         {"text": "Nothing is wrong — the long line really carries a "
                  "larger current than the short one", "correct": False,
          "why": "Both terminals of a cell are part of the same single "
                 "loop once connected, and carry the same current."},
         {"text": "The long line marks the positive terminal; it is not a "
                  "sign that more charge collects there", "correct": True},
         {"text": "The idea is right for a single cell but wrong once "
                  "several cells are joined together into a battery",
          "correct": False,
          "why": "The lines mark terminals in exactly the same way in "
                 "both symbols; neither one marks a store of extra "
                 "charge."},
     ], "figure": None},
    {"id": "p8-01-s22", "band": "standard",
     "text": "A single loop is rewired so the switch, which used to sit next "
             "to the cell, now sits right next to the bulb instead. What "
             "changes about how the circuit behaves?",
     "options": [
         {"text": "Nothing at all — a switch works the same wherever it "
                  "sits in a single loop", "correct": True},
         {"text": "The bulb now lights up a fraction of a second sooner "
                  "when the switch closes", "correct": False,
          "why": "There is no travel delay to shorten in the first place; "
                 "the wire is already full of charge wherever the switch "
                 "sits."},
         {"text": "The bulb becomes dimmer, because the switch is now "
                  "closer to it and blocks more of the current",
          "correct": False,
          "why": "A closed switch offers almost no resistance wherever it "
                 "sits; it does not block current partially."},
         {"text": "Opening the switch now stops the bulb but leaves the "
                  "rest of the loop working", "correct": False,
          "why": "A single loop has no \"rest of the loop\" separate from "
                 "the bulb; opening the switch anywhere in it stops the "
                 "whole thing."},
     ], "figure": None},
    {"id": "p8-01-s23", "band": "standard",
     "text": "A student says a coulomb must be a very small amount of "
             "charge, \"because you never hear it mentioned\". What is a "
             "better way to judge its size?",
     "options": [
         {"text": "Compare it with the ampere — since a coulomb is smaller "
                  "than an amp, and an amp is itself a modest everyday "
                  "number, it must be tiny", "correct": False,
          "why": "An amp and a coulomb measure different quantities "
                 "entirely, so one cannot simply be compared as smaller "
                 "than the other."},
         {"text": "Trust the student's reasoning — a unit that is rarely "
                  "said out loud in everyday speech is usually a "
                  "small one", "correct": False,
          "why": "How often a unit is mentioned in everyday speech says "
                 "nothing about its actual size."},
         {"text": "Compare it with a single electron's charge, which is "
                  "similar in size", "correct": False,
          "why": "A coulomb is nothing like the charge on a single "
                 "electron — it takes millions of millions of millions of "
                 "them to make one."},
         {"text": "Compare it with how many electrons make it up — about "
                  "six million million million, which is an enormous "
                  "number", "correct": True},
     ], "figure": None},
    {"id": "p8-01-s24", "band": "standard",
     "text": "A wire loop with a cell and a lamp is compared with an "
             "identical loop where the lamp has been replaced by a plain "
             "length of wire. In which loop does the ammeter read more, "
             "and why?",
     "options": [
         {"text": "The lamp loop, because a lamp helps push the charge "
                  "along", "correct": False,
          "why": "A lamp does not add any push of its own; only the cell "
                 "pushes the charge."},
         {"text": "The plain-wire loop, because the wire resists the "
                  "current far less than the lamp does", "correct": True},
         {"text": "They read the same, because both loops are complete "
                  "and carry a current", "correct": False,
          "why": "Being complete is not the only thing that matters — how "
                 "hard the loop is to push charge through decides the "
                 "size of the current, and a lamp resists far more than "
                 "plain wire."},
         {"text": "The lamp loop, because the wire loop has nothing to "
                  "measure the current against", "correct": False,
          "why": "An ammeter measures a current on its own; it does not "
                 "need another component to compare it against."},
     ], "figure": None},
    {"id": "p8-01-s25", "band": "standard",
     "text": "A cell is connected the wrong way round in a torch that "
             "normally works. A student predicts the bulb will not light "
             "at all. Is that right?",
     "options": [
         {"text": "Yes — a reversed cell pushes charge the wrong way and "
                  "the filament cannot conduct in that direction",
          "correct": False,
          "why": "A filament is not a one-way component; it conducts and "
                 "heats up whichever direction the current is pushed "
                 "through it."},
         {"text": "Yes, because a reversed cell delivers no push in either "
                  "direction", "correct": False,
          "why": "A reversed cell pushes just as hard as before, only in "
                 "the opposite direction round the loop."},
         {"text": "No, but the bulb will be noticeably dimmer than before",
          "correct": False,
          "why": "Reversing the cell changes the direction of the current, "
                 "not its size, so the bulb is exactly as bright as "
                 "before."},
         {"text": "No — the bulb lights exactly as before, because a "
                  "filament heats up whichever way the charge drifts "
                  "through it", "correct": True},
     ], "figure": None},
    {"id": "p8-01-s26", "band": "standard",
     "text": "Explain why a circuit diagram never needs to show how far "
             "apart the real components actually sit on the bench.",
     "options": [
         {"text": "Because the diagram is just a rough, quick sketch that "
                  "nobody expects to be geometrically accurate anyway",
          "correct": False,
          "why": "A circuit diagram is precise about connections; it is "
                 "just not concerned with physical distance."},
         {"text": "Because it is a map of connections, and the current's "
                  "behaviour does not depend on how far apart things sit",
          "correct": True},
         {"text": "Because real components are usually placed close "
                  "together anyway", "correct": False,
          "why": "Real components can be metres apart on a real bench; "
                 "the diagram simply does not need to show that."},
         {"text": "Because distance would make the diagram too large to "
                  "fit on a page", "correct": False,
          "why": "Page size is not the reason symbols and connections are "
                 "used instead of a scale drawing."},
     ], "figure": None},
    {"id": "p8-01-s27", "band": "standard",
     "text": "A single loop's switch is opened and closed rapidly, many "
             "times a second. Between two adjacent closures, does any "
             "charge remain \"left over\" in the wire from the closure "
             "before?",
     "options": [
         {"text": "Yes, a small amount builds up in the wire each time the "
                  "switch closes and is used up before the next closure",
          "correct": False,
          "why": "Nothing builds up in the wire. Opening the switch stops "
                 "the drift completely rather than leaving any charge "
                 "behind."},
         {"text": "No — the wire is always full of the same free "
                  "electrons; opening the switch just stops them drifting",
          "correct": True},
         {"text": "Yes, which is why very fast switching eventually stops "
                  "the bulb lighting altogether", "correct": False,
          "why": "Fast switching does not deplete anything in the wire; "
                 "each closure simply restarts the same drift."},
         {"text": "It depends on how long the switch stays closed each "
                  "time", "correct": False,
          "why": "The electrons are always present in the wire regardless "
                 "of timing; nothing is left over or used up between "
                 "closures."},
     ], "figure": None},
    {"id": "p8-01-s28", "band": "standard",
     "text": "A single loop contains a cell and a resistor only — no lamp "
             "at all. Does a current still flow, and is anything visibly "
             "different about the circuit?",
     "options": [
         {"text": "Yes, a current flows, but there is nothing to see — "
                  "current does not require a lamp to exist", "correct": True},
         {"text": "No current flows, because a complete circuit needs a "
                  "component that uses the electricity to show it is "
                  "working", "correct": False,
          "why": "A complete loop is all that is needed for a current; a "
                 "visible component like a lamp is not a requirement."},
         {"text": "Current flows if the resistor happens to glow slightly, "
                  "but not otherwise", "correct": False,
          "why": "Whether the resistor glows depends on how much it "
                 "warms up, not on whether current is flowing at all."},
         {"text": "No current flows, because a resistor's whole purpose "
                  "by design is to block current completely", "correct": False,
          "why": "A resistor makes it harder for current to flow, not "
                 "impossible — some current still gets through."},
     ], "figure": None},
    {"id": "p8-01-s29", "band": "standard",
     "text": "Why is it fair to say a cell \"pushes\" charge rather than "
             "\"pumps out\" charge?",
     "options": [
         {"text": "Because pushing and pumping mean exactly the same "
                  "thing, so either word would do", "correct": False,
          "why": "The two words suggest different pictures, and only one "
                 "of them — pushing charge that is already present — "
                 "matches what actually happens."},
         {"text": "Because a cell pushes charge in one direction while a "
                  "pump could work in either direction", "correct": False,
          "why": "Direction is not the distinction being drawn here; it "
                 "is about where the charge comes from in the first "
                 "place."},
         {"text": "Because \"pumping\" is usually a word for water rather "
                  "than for electricity", "correct": False,
          "why": "The word itself is used loosely in everyday speech; the "
                 "real issue is that it wrongly suggests the cell supplies "
                 "the charge."},
         {"text": "Because pushing implies the charge is already there, "
                  "while pumping implies the cell is the source of it",
          "correct": True},
     ], "figure": None},
    {"id": "p8-01-s30", "band": "standard",
     "text": "A student sketches a battery symbol using three pairs of long "
             "and short lines instead of two. What has changed about what "
             "the symbol represents?",
     "options": [
         {"text": "It now represents three cells joined together rather "
                  "than two", "correct": True},
         {"text": "Nothing — a battery symbol means exactly two cells, "
                  "whatever the number of pairs drawn", "correct": False,
          "why": "The number of long-short pairs is exactly how many "
                 "cells the symbol shows; it is not fixed at two."},
         {"text": "It now represents a single, more powerful cell",
          "correct": False,
          "why": "Each pair still represents one ordinary cell; adding "
                 "pairs means more cells, not one stronger one."},
         {"text": "It becomes invalid, because a battery symbol may use "
                  "two pairs and no more", "correct": False,
          "why": "A battery can be drawn with any number of cell pairs "
                 "from two upwards; three is a perfectly valid battery."},
     ], "figure": None},

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────
    {"id": "p8-01-h09", "band": "harder",
     "text": "A student writes: \"Current takes time to reach the bulb, and "
             "by the time it arrives some of it has been used up making "
             "the bulb glow, so the returning current is smaller.\" How "
             "many separate errors does that sentence contain?",
     "options": [
         {"text": "One — the delay claim is wrong, but the size claim is "
                  "right, since a lit bulb really does take a share of "
                  "the current", "correct": False,
          "why": "A bulb takes a share of the energy, not of the current "
                 "itself; the return current is exactly the same size."},
         {"text": "One — the size claim is wrong, but the delay is real "
                  "enough to be worth mentioning", "correct": False,
          "why": "The wire is already full of charge, so there is no "
                 "meaningful delay to mention at all."},
         {"text": "Two — there is no meaningful delay, and the current is "
                  "not smaller on the way back", "correct": True},
         {"text": "None — both parts describe roughly what a working torch "
                  "does", "correct": False,
          "why": "Both halves describe common but false beliefs about "
                 "circuits, not what actually happens."},
     ], "figure": None},
    {"id": "p8-01-h10", "band": "harder",
     "text": "Torch A has two cells facing the same way. Torch B, "
             "otherwise identical, has four cells all facing the same way. "
             "Compare both the ammeter reading and the brightness of the "
             "two torches.",
     "options": [
         {"text": "Both readings and both brightnesses are the same, "
                  "because both torches are complete loops", "correct": False,
          "why": "Being complete only means a current flows at all; it "
                 "does not mean the size of the push is the same in both."},
         {"text": "Torch B has a larger reading and is brighter, because "
                  "four cells push harder than two", "correct": True},
         {"text": "Torch B has the same reading but is brighter, because "
                  "extra cells change how the bulb looks without "
                  "changing the ammeter", "correct": False,
          "why": "Brightness and current are not independent here — a "
                 "bulb is brighter precisely because more current is "
                 "passing through it."},
         {"text": "Torch A has a larger reading, because fewer cells make "
                  "it easier for the charge to get all the way round",
          "correct": False,
          "why": "Cells do not make the loop easier to get round; they "
                 "push harder. More of them means a bigger current, not a "
                 "smaller one."},
     ], "figure": None},
    {"id": "p8-01-h11", "band": "harder",
     "text": "Holder A has two cells, both facing forwards. Holder B has "
             "four cells, two forwards and two backwards. Both drive an "
             "identical bulb. Compare the two bulbs.",
     "options": [
         {"text": "Holder A's bulb is lit normally; holder B's bulb is "
                  "completely dark", "correct": True},
         {"text": "Holder A's bulb is lit normally; holder B's bulb is "
                  "twice as bright, since it has twice as many cells",
          "correct": False,
          "why": "The two reversed cells cancel the two forward cells "
                 "exactly, leaving nothing to drive a current at all."},
         {"text": "Both bulbs are lit exactly the same, because both "
                  "holders contain some forward-facing cells",
          "correct": False,
          "why": "Some forward-facing cells is not enough on its own — in "
                 "holder B they are exactly cancelled by the reversed "
                 "ones."},
         {"text": "Holder B's bulb is lit normally; holder A's bulb is "
                  "dim, since it has fewer cells overall", "correct": False,
          "why": "Holder A's two forward cells are not cancelled by "
                 "anything, so its bulb runs exactly as it would on any "
                 "ordinary two-cell torch."},
     ], "figure": None},
    {"id": "p8-01-h12", "band": "harder",
     "text": "A car's starter motor briefly draws around 200 A. Someone "
             "suggests using a thin phone-charger cable for the connection "
             "instead of the proper thick cable, arguing \"it's only for a "
             "moment, so a thin cable should just about cope.\" What is "
             "wrong with that argument?",
     "options": [
         {"text": "Nothing — a thin cable can carry any size of current "
                  "perfectly safely, for as long as the moment asking for "
                  "it stays brief enough", "correct": False,
          "why": "A cable has to cope with whatever current is asked of "
                 "it at that instant; briefness does not reduce the size "
                 "of the current flowing through it."},
         {"text": "A cable has to carry whatever current flows at that "
                  "instant, and a thin one overheats immediately, "
                  "however brief that moment is",
          "correct": True},
         {"text": "The current builds up gradually over the whole moment "
                  "the motor runs, so a thin cable only really struggles "
                  "right at the very end of it, not from the start",
          "correct": False,
          "why": "Current does not build up gradually in this sense; the "
                 "large current is present essentially from the instant "
                 "the motor starts turning."},
         {"text": "A thin cable is fine as long as it is disconnected "
                  "again before the charge inside it runs out",
          "correct": False,
          "why": "Charge is not a store that runs out; the danger is the "
                 "size of the current a thin cable is being asked to "
                 "carry, at every instant it is connected."},
     ], "figure": None},
    {"id": "p8-01-h13", "band": "harder",
     "text": "A working single loop has a lit bulb in it. Which one of "
             "these would NOT, on its own, count as evidence that a "
             "current is flowing?",
     "options": [
         {"text": "The cell in the holder feels slightly heavier than an "
                  "identical, unused one", "correct": True},
         {"text": "An ammeter placed anywhere round the loop shows a "
                  "reading above zero", "correct": False,
          "why": "That is direct evidence of a current — it is exactly "
                 "what an ammeter is built to detect."},
         {"text": "The bulb is visibly lit", "correct": False,
          "why": "A lit bulb is being given energy by the charge passing "
                 "through it, which only happens while a current flows."},
         {"text": "The connecting wires feel slightly warm to the touch",
          "correct": False,
          "why": "Warming is a sign that energy is being transferred in "
                 "the wires, which happens because a current is flowing "
                 "through them."},
     ], "figure": None},
    {"id": "p8-01-h14", "band": "harder",
     "text": "A metal rod is heated red hot but has no cell or complete "
             "loop connected to it, so no current flows. What is happening "
             "to its free electrons, and does the heat on its own create a "
             "current?",
     "options": [
         {"text": "They move faster, but with no overall drift there is "
                  "still no current", "correct": True},
         {"text": "They move faster and all drift the same way at once, "
                  "so heat alone does create a small current",
          "correct": False,
          "why": "Faster random motion has no preferred direction on its "
                 "own; something has to push the electrons the same way "
                 "for a current to exist."},
         {"text": "They stop moving almost entirely, because heat locks "
                  "them in place within the hot metal", "correct": False,
          "why": "Heat has the opposite effect — it agitates the free "
                 "electrons more, not less."},
         {"text": "They leave the rod entirely as heat radiates away, "
                  "which is itself a small current", "correct": False,
          "why": "The electrons stay inside the metal. What leaves as "
                 "heat is energy, not the electrons themselves, and "
                 "neither of those is a current in this rod."},
     ], "figure": None},
    {"id": "p8-01-h15", "band": "harder",
     "text": "In loop 1, conventional current is described as flowing "
             "clockwise. In a completely separate loop 2, it flows "
             "anticlockwise. In which loop, if either, do the free "
             "electrons drift clockwise?",
     "options": [
         {"text": "Loop 1, because electrons drift the same way as "
                  "conventional current is drawn", "correct": False,
          "why": "Electrons drift the opposite way to conventional "
                 "current, not the same way."},
         {"text": "Neither loop, because the electrons do not drift in a "
                  "fixed direction round either of them", "correct": False,
          "why": "Once a loop is closed and driven by a cell, the "
                 "electrons do have one overall drift direction — just the "
                 "opposite one to the conventional arrow."},
         {"text": "Loop 2, because its electrons drift opposite to its "
                  "own anticlockwise conventional current", "correct": True},
         {"text": "Both loops, because clockwise and anticlockwise "
                  "current would produce electrons drifting clockwise in "
                  "both cases",
          "correct": False,
          "why": "The electron direction depends on the conventional "
                 "direction in that particular loop; it cannot be the same "
                 "fixed direction in both."},
     ], "figure": None},
    {"id": "p8-01-h16", "band": "harder",
     "text": "A wall socket's cable is rated to carry up to about 13 A. "
             "Assess whether it is safe to run, one at a time: a kettle "
             "drawing about 10 A, and a heater drawing about 15 A.",
     "options": [
         {"text": "Both are safe, since 13 A is just a rough guide rather "
                  "than a real limit", "correct": False,
          "why": "A cable's rating is a real limit on how much current it "
                 "can carry without overheating, not a loose guideline."},
         {"text": "The kettle is safe, drawing less than the 13 A rating; "
                  "the heater is not, drawing more than it", "correct": True},
         {"text": "Neither is safe, because both currents are close "
                  "enough to the cable's 13 A rating to count as risky",
          "correct": False,
          "why": "10 A leaves a clear margin below the 13 A rating; only "
                 "the 15 A heater actually exceeds it."},
         {"text": "The heater is safe because it draws 15 A for a brief "
                  "moment while warming up, then settles lower",
          "correct": False,
          "why": "A cable has to cope with whatever current is flowing "
                 "at every instant, so a current above the rating is "
                 "unsafe whenever it occurs."},
     ], "figure": None},
    {"id": "p8-01-h17", "band": "harder",
     "text": "A student claims that a strong enough cell, or simply "
             "waiting long enough, would eventually push some current "
             "through a perfect insulator. Assess this claim.",
     "options": [
         {"text": "Both parts are wrong — a perfect insulator has "
                  "essentially no free charges to push, whatever the push "
                  "or however long you wait", "correct": True},
         {"text": "Both parts are right — enough push, or enough waiting, "
                  "would eventually free some of the insulator's own "
                  "charges to move through it", "correct": False,
          "why": "An insulator's charges are not freed by pushing harder "
                 "or waiting; they remain bound to their atoms either "
                 "way."},
         {"text": "The push part is right, but waiting longer would make "
                  "no difference on its own", "correct": False,
          "why": "Neither a stronger push nor more time creates the free "
                 "charges an insulator lacks."},
         {"text": "The waiting part is right, because charges slowly "
                  "build up at the surface of an insulator until "
                  "enough of them are free to move across it",
          "correct": False,
          "why": "Nothing accumulates inside an insulator over time; it "
                 "simply has almost no charges free to move, then or "
                 "later."},
     ], "figure": None},
    {"id": "p8-01-h18", "band": "harder",
     "text": "A single loop's cell is taken out and put back the other way "
             "round. Which of these changes: the direction conventional "
             "current is drawn flowing, the direction the electrons "
             "actually drift, both, or neither?",
     "options": [
         {"text": "The conventional current direction changes, while the "
                  "electrons keep drifting the same physical way as "
                  "before", "correct": False,
          "why": "The two directions are tied together by definition — "
                 "reversing one always reverses the other."},
         {"text": "The electron drift direction changes, while the "
                  "conventional current is drawn the same way on a "
                  "diagram regardless", "correct": False,
          "why": "The conventional direction is defined from + to − of "
                 "the cell, so reversing the cell reverses it too."},
         {"text": "Neither changes, because reversing a cell affects how "
                  "bright the bulb is, not any direction round the loop",
          "correct": False,
          "why": "Reversing a cell does not change the brightness at all, "
                 "and it does reverse both directions round the loop."},
         {"text": "Both change together, because the electron direction "
                  "is always defined as the opposite of the conventional "
                  "one", "correct": True},
     ], "figure": None},
    {"id": "p8-01-h19", "band": "harder",
     "text": "A student compares a circuit to a conveyor belt carrying "
             "parcels round a factory floor in a loop. In what way is the "
             "comparison a good one, and in what way could it mislead?",
     "options": [
         {"text": "Good: the belt is not used up going round, only what "
                  "it delivers changes. Misleading: a belt switches on "
                  "gradually, unlike a current", "correct": True},
         {"text": "Good: the parcels represent the current itself "
                  "arriving fresh from the motor each and every time it "
                  "sets off round the loop, which is a fair comparison "
                  "overall. Misleading: nothing else about the comparison "
                  "holds up well at all", "correct": False,
          "why": "The parcels are not a good stand-in for the current "
                 "arriving fresh — nothing arrives fresh; the loop is "
                 "already full before it starts, just like the wire."},
         {"text": "Good: both the belt and a wire eventually wear out and "
                  "need replacing after enough years of continuous, heavy "
                  "everyday use. Misleading: everything else about the "
                  "comparison is otherwise perfectly accurate throughout",
          "correct": False,
          "why": "Wearing out was never the point of the comparison, and "
                 "the comparison does have a real weakness worth naming."},
         {"text": "Good: a belt can be reversed just as easily as a "
                  "current, with no other differences worth mentioning",
          "correct": False,
          "why": "Reversibility is not the useful part of the comparison, "
                 "and the belt-versus-wire comparison does break down "
                 "elsewhere."},
     ], "figure": None},
    {"id": "p8-01-h20", "band": "harder",
     "text": "A lit bulb's switch is opened, then closed again a few "
             "seconds later. Are the electrons that resume drifting the "
             "same ones that were drifting before, or a fresh batch drawn "
             "in from the cell?",
     "options": [
         {"text": "A fresh batch, drawn in from the cell's chemical store "
                  "the moment the switch closes again", "correct": False,
          "why": "A cell supplies energy, not a fresh set of electrons; "
                 "the wire's own electrons were never used up or "
                 "replaced."},
         {"text": "A mixture — some of the original electrons and some "
                  "new ones supplied by the cell to make up for the ones "
                  "used while the switch was open", "correct": False,
          "why": "No electrons are used up while the switch is open — "
                 "they simply stop drifting, so there is nothing to make "
                 "up for."},
         {"text": "It cannot be known without knowing how long the switch "
                  "stayed open", "correct": False,
          "why": "The wire's electrons are never replaced or lost, "
                 "however long the switch stays open."},
         {"text": "The same ones — nothing arrives from the cell or leaves "
                  "the wire; the same free electrons simply stop and then "
                  "start drifting again", "correct": True},
     ], "figure": None},
    {"id": "p8-01-h21", "band": "harder",
     "text": "A single loop's cells are doubled in number AND its lamp is "
             "swapped for one that lets current through far less easily, "
             "both at the same time. A student says \"the two changes "
             "cancel out, so the current stays the same.\" Assess this.",
     "options": [
         {"text": "The student is right, because doubling and halving "
                  "effects in any circuit cancel out exactly, whatever the "
                  "particular components happen to be", "correct": False,
          "why": "There is no reason the two effects would land on "
                 "exactly opposite amounts; doubling one factor and "
                 "restricting another does not guarantee an exact "
                 "cancellation."},
         {"text": "Not necessarily — the two changes pull in opposite "
                  "directions, but nothing says they are matched closely "
                  "enough to cancel exactly", "correct": True},
         {"text": "The student is wrong, because more cells cannot "
                  "compensate for a harder lamp in a case like this",
          "correct": False,
          "why": "More cells absolutely can partly or fully compensate "
                 "for a harder lamp; the issue is only that an exact "
                 "cancellation cannot be assumed."},
         {"text": "The current must fall, because a change that makes "
                  "current harder to push always tends to win over a "
                  "change that merely pushes harder", "correct": False,
          "why": "Neither kind of change automatically wins; the outcome "
                 "depends on how large each change actually is."},
     ], "figure": None},
    {"id": "p8-01-h22", "band": "harder",
     "text": "A loop is made from just a cell and a length of wire — no "
             "lamp, resistor or any other component. Compare the current "
             "in this loop with one that includes a lamp, and explain why "
             "this wire-only loop is a bad idea in practice even though it "
             "still works.",
     "options": [
         {"text": "The current is far smaller, because a lamp normally "
                  "helps to draw considerably more charge around the "
                  "entire loop than plain wire alone would manage",
          "correct": False,
          "why": "A lamp does not help drive the current — it resists it. "
                 "Removing it makes the current larger, not smaller."},
         {"text": "The current is exactly the same, because both loops "
                  "are equally complete", "correct": False,
          "why": "Being complete only decides whether current flows at "
                 "all; how much flows depends on how hard the loop "
                 "resists it, which is very different in each case."},
         {"text": "No current flows, because a loop needs at least one "
                  "component besides the cell before it counts as a "
                  "complete circuit at all", "correct": False,
          "why": "A complete loop needs a full conducting path, not a "
                 "particular kind of component in it; a plain wire loop "
                 "with a cell is complete and does carry a current."},
         {"text": "The current is far larger, because almost nothing in "
                  "the loop resists it, which can overheat the wire and "
                  "drain the cell very quickly", "correct": True},
     ], "figure": None},
    {"id": "p8-01-h23", "band": "harder",
     "text": "A student wants to test whether the current is the same on "
             "both sides of a bulb. They take a reading in front of the "
             "bulb with one ammeter, then move that same ammeter behind "
             "the bulb and take a second reading a minute later — after "
             "briefly touching a different, weaker cell to the circuit in "
             "between the two readings \"to reset it\". Why does this not "
             "properly test the claim?",
     "options": [
         {"text": "Because using a single ammeter for both readings makes "
                  "the comparison meaningless, however the rest of the "
                  "test is run", "correct": False,
          "why": "One ammeter moved between two points is a perfectly "
                 "valid way to compare them, provided nothing else about "
                 "the circuit changes in between."},
         {"text": "Because the circuit itself changed between the two "
                  "readings, so any difference found no longer isolates "
                  "the comparison being tested", "correct": True},
         {"text": "Because a minute is not long enough for a current to "
                  "settle to a steady value before the second reading is "
                  "taken", "correct": False,
          "why": "A current in a simple loop settles essentially "
                 "instantly; the timing between the two readings is not "
                 "the problem here."},
         {"text": "Because an ammeter placed behind a bulb reads "
                  "differently from one placed in front of it in this "
                  "case, regardless of how the test is run",
          "correct": False,
          "why": "In a single loop the two positions read the same "
                 "current when nothing else changes — that is exactly "
                 "what this test failed to keep fixed."},
     ], "figure": None},
    {"id": "p8-01-h24", "band": "harder",
     "text": "A wiring diagram draws a switch right next to the cell and a "
             "lamp on the far side of the page. Could the lamp actually "
             "be physically closer to the cell than the switch is, on the "
             "real bench?",
     "options": [
         {"text": "No — the diagram is drawn to the same relative scale as "
                  "the real components", "correct": False,
          "why": "Circuit diagrams are not drawn to scale at all; "
                 "distance on the page carries no information about real "
                 "position."},
         {"text": "Yes, but if the connecting wires in the diagram happen "
                  "to be drawn unusually long", "correct": False,
          "why": "The length of a wire as drawn on the diagram is not "
                 "linked to its real length either, so this is not a "
                 "condition that needs to be met."},
         {"text": "Yes — position on the diagram carries no information "
                  "at all about real distance on the bench",
          "correct": True},
         {"text": "No — a diagram places components in the same "
                  "left-to-right order they will be built in, as a rule",
          "correct": False,
          "why": "There is no such rule; components can be drawn in any "
                 "order on the page regardless of how they end up "
                 "arranged on the bench."},
     ], "figure": None},
    {"id": "p8-01-h25", "band": "harder",
     "text": "A coulomb is an enormous number of electrons. Explain why "
             "touching "
             "both terminals of a healthy AA battery with dry fingers is "
             "still completely safe, despite that huge number.",
     "options": [
         {"text": "Because a single AA battery is not able to move even "
                  "one full coulomb of charge in a whole lifetime",
          "correct": False,
          "why": "An AA battery can move far more than a coulomb over "
                 "time; the reason touching it is safe is the tiny "
                 "current through skin, not a shortage of available "
                 "charge."},
         {"text": "Because the huge number applies mainly to current "
                  "flowing through metal wires, not through skin",
          "correct": False,
          "why": "A coulomb is the same enormous number of electrons "
                 "wherever charge is measured; what changes through skin "
                 "is how much current gets through, not the size of a "
                 "coulomb."},
         {"text": "Because your body conducts electricity much better when "
                  "wet, so dry skin normally lets no current through "
                  "it, whatever the number of electrons in a coulomb "
                  "happens to be", "correct": False,
          "why": "Dry skin still lets a very small current through — "
                 "which is exactly why the touch is harmless rather than "
                 "undetectable."},
         {"text": "Because dry skin resists the current so much that only "
                  "a tiny current — nowhere near enough to notice — "
                  "actually flows through you, whatever the size of a "
                  "coulomb", "correct": True},
     ], "figure": None},
    {"id": "p8-01-h26", "band": "harder",
     "text": "A bulb's filament breaks somewhere along its middle while a "
             "torch is switched on. Describe what happens to the current "
             "everywhere in the loop, and explain why a broken filament "
             "is, electrically, really no different from an open switch.",
     "options": [
         {"text": "The current stops on the far side of the break, while "
                  "the near side keeps flowing as before", "correct": False,
          "why": "There is no near side and far side in a single loop — "
                 "a gap anywhere stops the current at every point in it, "
                 "instantly."},
         {"text": "The current keeps flowing at a reduced level, because "
                  "the broken filament still offers a narrow path across "
                  "the gap", "correct": False,
          "why": "A genuine break leaves no path across the gap at all; "
                 "it is not a narrowing, so nothing continues to flow."},
         {"text": "The current stops permanently even once the filament "
                  "is repaired, unlike an open switch which can be closed "
                  "again", "correct": False,
          "why": "There is nothing special about a broken filament that "
                 "prevents current flowing again once the path is "
                 "properly restored; the comparison with a switch holds "
                 "both ways."},
         {"text": "The current stops everywhere at once — the break is "
                  "just a gap in the one path", "correct": True},
     ], "figure": None},
    {"id": "p8-01-h27", "band": "harder",
     "text": "A component's symbol is a plain rectangle with a diagonal "
             "arrow drawn across it. A student says the arrow must mean "
             "current can only pass through it in one direction, like a "
             "one-way valve. Assess this.",
     "options": [
         {"text": "The student is right, and the arrow shows the one "
                  "particular direction current is drawn flowing through "
                  "the component in a diagram", "correct": False,
          "why": "The arrow is not a direction-of-current marker at all; "
                 "it represents an adjustable value, and the component "
                 "works the same whichever way round it sits."},
         {"text": "The student is right for a variable resistor, though "
                  "not for a fixed one", "correct": False,
          "why": "Neither a fixed nor a variable resistor is a one-way "
                 "component; both conduct equally in either direction."},
         {"text": "It cannot be judged without knowing which way round "
                  "the component is wired into the loop", "correct": False,
          "why": "Which way round it is wired makes no difference — a "
                 "resistor, fixed or variable, is not directional at all."},
         {"text": "The student is wrong — the arrow shows that the "
                  "resistance can be adjusted, not that the component "
                  "only works one way round", "correct": True},
     ], "figure": None},
    {"id": "p8-01-h28", "band": "harder",
     "text": "A single loop is switched on and every ammeter placed round "
             "it reads 0.00 A, even though the switch itself is closed. "
             "What must be true?",
     "options": [
         {"text": "The cell must have been connected backwards, since a "
                  "reversed cell gives a reading of exactly zero in every "
                  "case", "correct": False,
          "why": "A reversed cell still pushes just as hard, only the "
                 "other way round the loop, so it would still give a "
                 "non-zero reading."},
         {"text": "There must be a break somewhere else in the loop — a "
                  "blown component, a disconnected wire, or some other "
                  "gap besides the switch", "correct": True},
         {"text": "Nothing unusual — a closed switch on its own is enough "
                  "to guarantee a non-zero reading every time",
          "correct": False,
          "why": "A closed switch only closes one gap. Any other break "
                 "left open elsewhere in the loop still stops the current "
                 "completely."},
         {"text": "The ammeters themselves must all be faulty, since a "
                  "properly complete loop should not read exactly zero",
          "correct": False,
          "why": "A genuinely complete loop reads whatever current is "
                 "flowing, which can be a very small but real value — a "
                 "true zero points to a break, not faulty meters."},
     ], "figure": None},
    {"id": "p8-01-h29", "band": "harder",
     "text": "An ammeter reading 0.24 A in a single loop is unplugged and "
             "replaced with a different ammeter of the same, well-made "
             "design, in exactly the same position. What does the new "
             "meter read?",
     "options": [
         {"text": "Slightly more than 0.24 A, because the new meter has "
                  "not yet warmed up to match the circuit",
          "correct": False,
          "why": "A meter's own temperature does not change the current "
                 "flowing through the loop; the reading reflects the loop, "
                 "not the meter's warmth."},
         {"text": "0.24 A, because a well-made ammeter does not disturb "
                  "the current it is placed into", "correct": True},
         {"text": "Slightly less than 0.24 A, because inserting any "
                  "ammeter adds a small amount of resistance to the loop",
          "correct": False,
          "why": "A well-made ammeter is designed to have almost no "
                 "resistance of its own, so swapping one in for another "
                 "makes no meaningful difference to the current."},
         {"text": "It cannot be predicted without knowing the exact make "
                  "of the new ammeter", "correct": False,
          "why": "Any two well-made ammeters are designed to behave the "
                 "same way — almost no resistance — so the make does not "
                 "matter here."},
     ], "figure": None},
    {"id": "p8-01-h30", "band": "harder",
     "text": "In a single loop, an ammeter beside the cell reads 0.40 A "
             "and a second ammeter next to the bulb reads 0.38 A — a tiny "
             "difference blamed on a small manufacturing fault in one of "
             "the meters. What does this discrepancy tell you about "
             "whether charge is used up in the bulb?",
     "options": [
         {"text": "It confirms charge is used up, since the reading after "
                  "the bulb is the smaller of the two, which is exactly "
                  "what you would expect once some charge has been spent "
                  "on lighting it", "correct": False,
          "why": "A gap this small between two separate meter units is "
                 "far more likely to be ordinary measurement error than "
                 "genuine evidence that charge has been consumed."},
         {"text": "Nothing reliable — two genuinely ideal meters in one "
                  "loop must read identically, so a small gap like this "
                  "points to meter error rather than charge being used up",
          "correct": True},
         {"text": "It shows charge is used up, but by a very small amount "
                  "each time round the loop", "correct": False,
          "why": "Charge is not used up at all in a bulb; a tiny "
                 "difference between two real meters does not establish a "
                 "small ongoing loss."},
         {"text": "It shows the bulb must be positioned closer to the "
                  "second ammeter than to the first one, so less of the "
                  "charge has had the time it needs to reach the "
                  "second meter", "correct": False,
          "why": "Position in the loop does not affect how much current "
                 "a meter reads; the discrepancy is about the meters, not "
                 "distances between components."},
     ], "figure": None},
]
