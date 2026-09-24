"""P8 lesson 04 — Potential difference: twelve questions (MRB-223).

Written against Design's page. The number stamped on a bulb, the loop with
four voltmeter positions, the ratings table, the part–whole bar and both
worked examples are hers.

The discriminations, in the order the lesson builds them:

  · a p.d. is a DIFFERENCE, so a voltmeter goes across and never in the
    loop (`CIRC-14`);
  · nothing flows except charge — voltage is not used up (`CIRC-13`);
  · in series the push is SHARED and the shares add back to the battery,
    so a full-battery reading across one component is not a fault
    (`CIRC-15`) — the harder band sits here;
  · a rating says what a component WANTS; a battery's says what it gives.

⚠️ POSITION IS AUTHORED AND MEASURED —
0,2,2,3 · 3,1,2,0 · 1,2,0,1;
the twelve fall 3/3/4/2 across the four indices.

⚠️ Neither ladder rung is restated (the three components on 6.0 V reading
1.5 V and 3.0 V, the single lamp reading the battery's own 3.0 V), and
neither are the figures in the worked examples (4.5 V with 1.8 V, 12 V
with 4500 mV) or in the two attempts (the live bench, and 6.0 V with
1500 mV).
"""

UNIT = "P8"
LESSON = "potential-difference"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p8-04-e01",
        "band": "easier",
        "text": "Potential difference is measured in…",
        "options": [
            {"text": "volts", "correct": True},
            {"text": "amperes", "correct": False,
             "why": "Amps measure current — how much charge goes past each "
                    "second."},
            {"text": "ohms", "correct": False,
             "why": "Ohms measure resistance, which is the p.d. divided by "
                    "the current rather than the p.d. itself."},
            {"text": "watts", "correct": False,
             "why": "Watts measure power — how fast energy is transferred, "
                    "not how much each charge carries."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-e02",
        "band": "easier",
        "text": "A voltmeter is connected…",
        "options": [
            {"text": "in the loop, so the current runs through it",
             "correct": False,
             "why": "That is where an ammeter goes. A voltmeter in the loop "
                    "almost stops the current."},
            {"text": "to one side of a component only", "correct": False,
             "why": "A difference needs two points. One lead measures "
                    "nothing."},
            {"text": "across a component, with a lead on each side",
             "correct": True},
            {"text": "directly to the battery's positive terminal and "
                     "nothing else", "correct": False,
             "why": "Again, one point is not a difference. Across the "
                    "battery means a lead on each of its two terminals."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-e03",
        "band": "easier",
        "text": "A bulb is marked 2.5 V. What does that number tell you?",
        "options": [
            {"text": "How much electricity the bulb uses up while it is on",
             "correct": False,
             "why": "Nothing is used up, and a rating is not a measure of "
                    "consumption. It is the p.d. the bulb was designed for."},
            {"text": "The current that will flow through it", "correct": False,
             "why": "That would be quoted in amps. A number in volts is a "
                    "p.d."},
            {"text": "The p.d. the maker designed it to run at",
             "correct": True},
            {"text": "How bright it will be, on a scale of ten",
             "correct": False,
             "why": "Brightness has no unit of volts, and a rating is a "
                    "specification rather than a score."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-e04",
        "band": "easier",
        "text": "Four 1.5 V cells are put in a holder in series. The battery "
                "supplies…",
        "options": [
            {"text": "1.5 V, because the cells are identical",
             "correct": False,
             "why": "Identical cells in series add their pushes. One cell's "
                    "value is what each contributes, not the total."},
            {"text": "0.375 V, because the push is shared between them",
             "correct": False,
             "why": "That divides instead of adding. Sharing happens across "
                    "the components, not across the cells driving them."},
            {"text": "3.0 V, because only the two end cells count",
             "correct": False,
             "why": "All four are in the path and all four push. There is no "
                    "reason for the middle two to be idle."},
            {"text": "6.0 V", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p8-04-s01",
        "band": "standard",
        "text": "A 9.0 V battery drives two components in series. A "
                "voltmeter across the first reads 3.5 V. What does it read "
                "across the second?",
        "options": [
            {"text": "12.5 V", "correct": False,
             "why": "That adds the share to the whole. The whole is already "
                    "given; the other share is what is left of it."},
            {"text": "4.5 V", "correct": False,
             "why": "That halves the battery. The shares are not equal here "
                    "— one is measured at 3.5 V."},
            {"text": "9.0 V", "correct": False,
             "why": "That is the rule for parallel branches. In series the "
                    "p.d. is shared out."},
            {"text": "5.5 V", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-s02",
        "band": "standard",
        "text": "Two components sit in series. One resists twice as much as "
                "the other. How is the battery's p.d. shared?",
        "options": [
            {"text": "Equally, because the same current goes through both",
             "correct": False,
             "why": "The current is the same, and that is exactly why the "
                    "shares differ: the same current through more resistance "
                    "gives up more energy."},
            {"text": "Two thirds to the one that resists more",
             "correct": True},
            {"text": "Two thirds to the one that resists less, because "
                     "charge goes through it more easily", "correct": False,
             "why": "It is the other way round. The bigger share goes to "
                    "whatever is harder to get through."},
            {"text": "It depends which one comes first in the loop",
             "correct": False,
             "why": "Position round a single loop decides nothing. Swap them "
                    "over and both readings are unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-s03",
        "band": "standard",
        "text": "A voltmeter is connected across a plain piece of wire in a "
                "working circuit. What does it read, and why?",
        "options": [
            {"text": "The battery's full p.d., because a wire carries the "
                     "whole current", "correct": False,
             "why": "Carrying the current is not the same as having a p.d. "
                    "across you. A wire gives up almost no energy."},
            {"text": "Half the battery's p.d., because the wire is half the "
                     "loop", "correct": False,
             "why": "Length of wire is not how a share is decided. "
                    "Resistance is, and a plain wire has almost none."},
            {"text": "Almost 0 V, because there is almost nothing for the "
                     "charge to give up energy to", "correct": True},
            {"text": "It cannot be read, because a voltmeter needs a "
                     "component between its leads", "correct": False,
             "why": "It reads perfectly well. What it reads is a very small "
                    "difference, which is the useful answer."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-s04",
        "band": "standard",
        "text": "Two lamps sit in parallel across a 6 V battery. What is the "
                "p.d. across each one?",
        "options": [
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "6 V across each, as each branch is straight "
                     "across the battery", "correct": True},
            {"text": "3 V across each, because the battery shares its push "
                     "between them", "correct": False,
             "why": "Sharing is the SERIES rule. Each parallel branch is "
                    "connected straight across the battery."},
            {"text": "12 V across each, because the two branches add",
             "correct": False,
             "why": "Currents add in parallel; potential differences do not. "
                    "Nothing in the circuit is larger than the battery."},
            {"text": "6 V across the first and 3 V across the second",
             "correct": False,
             "why": "There is no first and second in parallel. Both branches "
                    "sit across the same two points."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p8-04-h01",
        "band": "harder",
        "text": "A student says the voltage is used up as it goes round the "
                "loop, in the same way that the current is. What is wrong "
                "with the sentence?",
        "options": [
            {"text": "Only the second half — the current IS used up, "
                     "because each component in the loop takes a share of "
                     "it",
             "correct": False,
             "why": "The current is not used up either: an ammeter reads the "
                    "same before a lamp and after it. Both halves of the "
                    "sentence are wrong, for different reasons."},
            {"text": "Both halves. Nothing flows except charge, and the "
                     "charge all comes back; what is handed over is energy",
             "correct": True},
            {"text": "Nothing — it is a fair way to describe what happens "
                     "all the way round the loop",
             "correct": False,
             "why": "It puts two different quantities in one wrong picture. "
                    "A p.d. is a difference between two places and does not "
                    "travel at all."},
            {"text": "Only the first half — the voltage IS used up, because "
                     "each component in the loop takes a share of it",
             "correct": False,
             "why": "The shares do add to the battery's value, which is why "
                    "it sounds right. But a difference between two points is "
                    "not a substance being spent."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-h02",
        "band": "harder",
        "text": "A 12 V lamp is run on a 6 V battery. What happens, and why?",
        "options": [
            {"text": "It flares once and the filament breaks, because the "
                     "battery cannot supply what it asks for", "correct": False,
             "why": "That is what happens the other way round — a 6 V lamp "
                    "on a 12 V supply."},
            {"text": "It works exactly as normal, because the rating is only "
                     "a guide", "correct": False,
             "why": "The rating is the p.d. it needs to reach its designed "
                    "brightness. At half of it, the filament never gets hot "
                    "enough."},
            {"text": "It glows dimly or not at all, because it has only half "
                     "the p.d. it was designed for", "correct": True},
            {"text": "It draws twice the current, because the battery is "
                     "half the size", "correct": False,
             "why": "Less push through the same resistance gives LESS "
                    "current, not more."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-h03",
        "band": "harder",
        "text": "A voltmeter across a lamp reads 3.0 V. The same voltmeter "
                "across the battery driving it also reads 3.0 V. What can "
                "you conclude?",
        "options": [
            {"text": "The lamp is the only component in the loop, so it "
                     "takes the whole share", "correct": True},
            {"text": "The meter is faulty, because a component can never "
                     "have the battery's full p.d. across it",
             "correct": False,
             "why": "It can, and it does whenever it is alone in the loop. "
                    "There is nothing else to share with."},
            {"text": "The lamp has failed, because a broken filament reads "
                     "the full p.d.", "correct": False,
             "why": "A broken filament WOULD read the full p.d. — and so "
                    "does a working lamp on its own, so the reading alone "
                    "cannot tell you. Look at whether it is lit."},
            {"text": "The battery is flat, because a flat battery reads the "
                     "same everywhere", "correct": False,
             "why": "A flat battery reads LESS than its rating under load. "
                    "Reading its full value is the healthy case."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-h04",
        "band": "harder",
        "text": "Two resistors in series across a 9 V supply, and you take a "
                "connection from the point between them. Why is that useful?",
        "options": [
            {"text": "It doubles the supply, because two resistors give two "
                     "shares", "correct": False,
             "why": "The two shares ADD to 9 V. Nothing in the circuit is "
                    "bigger than the supply."},
            {"text": "It gives you a fraction of the 9 V, decided by how the "
                     "two resistances compare", "correct": True},
            {"text": "It gives you the current in the loop, which you can "
                     "read as a voltage", "correct": False,
             "why": "A connection taken to a point gives a p.d., not a "
                    "current. The two are different quantities with "
                    "different units."},
            {"text": "It isolates the second resistor so it can be removed "
                     "safely", "correct": False,
             "why": "Nothing is isolated. Both resistors stay in the same "
                    "single loop."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p8-04-e05",
        "band": "easier",
        "text": "Potential difference tells you…",
        "options": [
            {"text": "how much charge passes a point each second",
             "correct": False,
             "why": "That is current, measured in amps on an ammeter."},
            {"text": "how much energy each unit of charge gives up between "
                     "two points",
             "correct": True},
            {"text": "how hard a component makes it for charge to get "
                     "through",
             "correct": False,
             "why": "That is resistance, measured in ohms and found from a "
                    "ratio."},
            {"text": "how much charge a battery is holding", "correct": False,
             "why": "A battery holds a chemical store, and its rating says "
                    "how hard it pushes, not how much it holds."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-e06",
        "band": "easier",
        "text": "Two 1.5 V cells are put in series in a holder. What does the "
                "battery supply?",
        "options": [
            {"text": "1.5 V, because both cells are the same", "correct": False,
             "why": "In series the pushes add, so two cells give more than "
                    "one."},
            {"text": "3.0 V", "correct": True},
            {"text": "0.75 V, shared between the two", "correct": False,
             "why": "Cells in series add rather than share; sharing is what "
                    "components do."},
            {"text": "2.25 V", "correct": False,
             "why": "That multiplies 1.5 by 1.5. The two ratings are simply "
                    "added."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-e07",
        "band": "easier",
        "text": "Three lamps are wired in parallel across a 6.0 V battery. "
                "What is the p.d. across each lamp?",
        "options": [
            {"text": "2.0 V, a third each", "correct": False,
             "why": "Sharing is what happens in series. Parallel branches "
                    "each get the whole of it."},
            {"text": "18 V, three times the battery", "correct": False,
             "why": "Nothing multiplies the battery's push; branches cannot "
                    "get more than it supplies."},
            {"text": "6.0 V across each one", "correct": True},
            {"text": "3.0 V, half each", "correct": False,
             "why": "Halving would be sharing between two in series, and "
                    "these are three in parallel."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p8-04-s05",
        "band": "standard",
        "text": "Three components sit in series on a 6.0 V battery. "
                "Voltmeters across two of them read 1.5 V and 2.0 V. What "
                "does the third read?",
        "options": [
            {"text": "3.5 V, the two readings added", "correct": False,
             "why": "The three shares add to the battery's 6.0 V, so the "
                    "third is what is left over."},
            {"text": "2.5 V, the share that is left", "correct": True},
            {"text": "6.0 V, because the battery drives it", "correct": False,
             "why": "That is the whole push, and two components have already "
                    "taken shares of it."},
            {"text": "2.0 V, the same as the second", "correct": False,
             "why": "Shares are only equal when the components resist "
                    "equally, and these do not."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-s06",
        "band": "standard",
        "text": "Why is a voltmeter connected across a component rather than "
                "in the loop?",
        "options": [
            {"text": "Because it needs the current to pass through it to "
                     "work",
             "correct": False,
             "why": "That is an ammeter. A voltmeter is built to take almost "
                    "no current at all."},
            {"text": "Because a p.d. is a difference between two points, "
                     "needing a lead at each",
             "correct": True},
            {"text": "Because it would be damaged by the full current of the "
                     "loop",
             "correct": False,
             "why": "It would not be damaged — it would simply stop the "
                    "current, because its resistance is enormous."},
            {"text": "Because it can then measure the current as well",
             "correct": False,
             "why": "It measures p.d. only; the current needs a separate "
                    "instrument."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-s07",
        "band": "standard",
        "text": "A 12 V battery drives two identical lamps in series. What is "
                "the p.d. across each lamp?",
        "options": [
            {"text": "12 V across each", "correct": False,
             "why": "That would need 24 V altogether, and the battery "
                    "supplies 12 V."},
            {"text": "24 V across each", "correct": False,
             "why": "Nothing in a circuit multiplies the battery's push."},
            {"text": "6 V across each", "correct": True},
            {"text": "0 V across each, because they cancel", "correct": False,
             "why": "Components do not cancel; they share the push out "
                    "between them."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p8-04-h05",
        "band": "harder",
        "text": "A 9.0 V battery drives a lamp and a resistor in series. The "
                "lamp takes 6.0 V. How do their resistances compare?",
        "options": [
            {"text": "The lamp resists twice as much as the resistor",
             "correct": True},
            {"text": "The resistor resists twice as much as the lamp",
             "correct": False,
             "why": "The larger share of the p.d. goes to whatever resists "
                    "more, and the lamp took 6.0 V of the 9.0 V."},
            {"text": "They resist equally, because the current through them "
                     "is the same",
             "correct": False,
             "why": "The current is the same, which is exactly why the "
                    "p.d. shares reveal the resistances."},
            {"text": "Their resistances cannot be compared without an "
                     "ammeter reading",
             "correct": False,
             "why": "The same current passes through both, so the ratio of "
                    "the p.d.s is the ratio of the resistances."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-h06",
        "band": "harder",
        "text": "A student writes that the p.d. is used up as the charge goes "
                "round the loop. Which rewrite is right?",
        "options": [
            {"text": "The p.d. is used up, but only at the last component in "
                     "the loop",
             "correct": False,
             "why": "Every component takes a share; nothing waits until the "
                    "end."},
            {"text": "The charge gives up energy at each component, and the "
                     "shares add to the battery's p.d.",
             "correct": True},
            {"text": "The charge is used up at each component, which is why "
                     "the p.d. falls",
             "correct": False,
             "why": "Charge is conserved all the way round; it is energy that "
                    "is given up."},
            {"text": "The p.d. is the same across every component, so nothing "
                     "is shared",
             "correct": False,
             "why": "That is true of parallel branches only. Round a series "
                    "loop the shares differ."},
        ],
        "figure": None,
    },
    {
        "id": "p8-04-h07",
        "band": "harder",
        "text": "Two lamps sit in parallel across a 6 V battery. A third lamp "
                "is added in series ahead of the pair. What happens to the "
                "p.d. across the pair?",
        "options": [
            {"text": "It stays at 6 V, because parallel branches always get "
                     "the whole supply",
             "correct": False,
             "why": "They get the whole of what reaches them, and the new "
                    "lamp now takes a share first."},
            {"text": "It rises above 6 V, because there are more lamps",
             "correct": False,
             "why": "No arrangement of components can give more than the "
                    "battery supplies."},
            {"text": "It falls below 6 V, because the new lamp takes a share",
             "correct": True},
            {"text": "It halves to 3 V, because there are now two stages",
             "correct": False,
             "why": "The share depends on how much each part resists, and "
                    "there is no reason for an even split."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────

    {"id": "p8-04-e08", "band": "easier",
     "text": "2500 mV, written in volts, is…",
     "options": [
         {"text": "2.500 V", "correct": True},
         {"text": "25.00 V", "correct": False,
          "why": "That divides by 100, but a millivolt is a thousandth "
                 "of a volt, not a hundredth."},
         {"text": "250.0 V", "correct": False,
          "why": "That divides by 10, far too small a conversion for "
                 "millivolts to volts."},
         {"text": "2500 V", "correct": False,
          "why": "That drops the prefix without converting; the number "
                 "has to get smaller when millivolts become volts."},
     ], "figure": None},
    {"id": "p8-04-e09", "band": "easier",
     "text": "Roughly what p.d. does a single AA or AAA cell supply?",
     "options": [
         {"text": "About 150 V", "correct": False,
          "why": "That is far closer to a mains-level voltage than a "
                 "single small cell."},
         {"text": "About 1.5 V", "correct": True},
         {"text": "About 0.15 V", "correct": False,
          "why": "That is ten times too small — a torch bulb would "
                 "barely glow on such a tiny push."},
         {"text": "About 15 V", "correct": False,
          "why": "That is ten times too large for a single small cell."},
     ], "figure": None},
    {"id": "p8-04-e10", "band": "easier",
     "text": "Roughly what p.d. does a UK mains wall socket supply?",
     "options": [
         {"text": "About 2.3 V", "correct": False,
          "why": "That is barely more than a single AA cell, nowhere "
                 "near mains level."},
         {"text": "About 2300 V", "correct": False,
          "why": "That is ten times too large — closer to some overhead "
                 "power lines than an ordinary wall socket."},
         {"text": "About 230 V", "correct": True},
         {"text": "About 23 V", "correct": False,
          "why": "That is ten times too small for a UK mains socket."},
     ], "figure": None},
    {"id": "p8-04-e11", "band": "easier",
     "text": "A car battery is usually rated at…",
     "options": [
         {"text": "About 120 V", "correct": False,
          "why": "That is ten times too large for an ordinary car "
                 "battery."},
         {"text": "About 230 V", "correct": False,
          "why": "That is mains level, not the rating of a car battery."},
         {"text": "About 1.5 V", "correct": False,
          "why": "That is the rating of a single small cell, far too "
                 "little to run a car's starter motor."},
         {"text": "About 12 V", "correct": True},
     ], "figure": None},
    {"id": "p8-04-e12", "band": "easier",
     "text": "A voltmeter is designed so that connecting it across a "
             "component…",
     "options": [
         {"text": "takes almost no current for itself, so it barely "
                  "disturbs the circuit", "correct": True},
         {"text": "adds its own extra push to the circuit",
          "correct": False,
          "why": "A voltmeter measures a difference; it does not add "
                 "any push of its own to the circuit."},
         {"text": "doubles the size of the current passing through that "
                  "component", "correct": False,
          "why": "Connecting a voltmeter across a component does not "
                 "change the current through it, doubled or "
                 "otherwise."},
         {"text": "stops almost all the current in the loop, which is "
                  "why it must go in series instead", "correct": False,
          "why": "A voltmeter goes ACROSS a component, in parallel with "
                 "it, not in series with the loop."},
     ], "figure": None},
    {"id": "p8-04-e13", "band": "easier",
     "text": "A p.d. of 0.6 V, written in millivolts, is…",
     "options": [
         {"text": "0.0006 mV", "correct": False,
          "why": "That divides by a thousand. Going from volts to "
                 "millivolts makes the number larger, because a "
                 "millivolt is the smaller unit of the two."},
         {"text": "600 mV", "correct": True},
         {"text": "6 mV", "correct": False,
          "why": "That multiplies by ten, nowhere near enough: there "
                 "are a thousand millivolts in every volt."},
         {"text": "60 mV", "correct": False,
          "why": "That multiplies by a hundred, which is ten times too "
                 "few; a volt holds a thousand millivolts."},
     ], "figure": None},
    {"id": "p8-04-e14", "band": "easier",
     "text": "A single volt means that every coulomb of charge passing "
             "between two points gives up…",
     "options": [
         {"text": "one ohm of resistance", "correct": False,
          "why": "The ohm measures resistance, not the energy carried "
                 "by each coulomb of charge."},
         {"text": "one newton of force", "correct": False,
          "why": "The newton measures force, which is not the quantity "
                 "a volt is defined from."},
         {"text": "one joule of energy", "correct": True},
         {"text": "one ampere of current", "correct": False,
          "why": "The ampere measures current, a separate quantity from "
                 "the energy each coulomb gives up."},
     ], "figure": None},
    {"id": "p8-04-e15", "band": "easier",
     "text": "What word names the p.d. a component was designed to run "
             "at?",
     "options": [
         {"text": "Its resistance", "correct": False,
          "why": "Resistance is a separate quantity, measured in ohms, "
                 "not the p.d. a component was designed for."},
         {"text": "Its current", "correct": False,
          "why": "Current is measured in amps and is not the name for "
                 "the p.d. a component is designed to run at."},
         {"text": "Its charge", "correct": False,
          "why": "Charge is measured in coulombs and is a different "
                 "quantity from a component's designed p.d."},
         {"text": "Its rating", "correct": True},
     ], "figure": None},
    {"id": "p8-04-e16", "band": "easier",
     "text": "500 mV, written in volts, is…",
     "options": [
         {"text": "0.500 V", "correct": True},
         {"text": "5.00 V", "correct": False,
          "why": "That divides by 100 rather than 1000, giving ten "
                 "times too large a value."},
         {"text": "50.0 V", "correct": False,
          "why": "That divides by 10, far too small a conversion for "
                 "millivolts to volts."},
         {"text": "500 V", "correct": False,
          "why": "That leaves the number unchanged; converting from "
                 "millivolts must make it smaller."},
     ], "figure": None},
    {"id": "p8-04-e17", "band": "easier",
     "text": "A voltmeter is connected the wrong way round, so that just "
             "one of its two leads touches the circuit. What "
             "does it read?",
     "options": [
         {"text": "The full battery p.d., since one lead is enough for a "
                  "meter to sense the push behind it", "correct": False,
          "why": "A p.d. is a difference between two points; with just "
                 "one lead touching anything, there is no second point "
                 "to compare it with."},
         {"text": "Nothing meaningful — a p.d. needs a lead on each of "
                  "two points to compare", "correct": True},
         {"text": "Exactly half the battery's p.d.", "correct": False,
          "why": "There is no reason for a one-lead connection to give "
                 "half of anything; it simply cannot form a genuine "
                 "difference to measure."},
         {"text": "The current flowing past that one single point in the "
                  "working loop", "correct": False,
          "why": "A voltmeter measures p.d., not current, and a single "
                 "lead cannot give a meaningful reading of either."},
     ], "figure": None},
    {"id": "p8-04-e18", "band": "easier",
     "text": "A 3.0 V battery and a 12.0 V battery are compared. Which "
             "one gives each coulomb of charge more energy, and by "
             "roughly how many times?",
     "options": [
         {"text": "The 12.0 V battery, about 9 times as much energy per "
                  "coulomb", "correct": False,
          "why": "That subtracts 3.0 from 12.0. To find how many TIMES "
                 "bigger one value is than another you divide, which "
                 "gives four."},
         {"text": "The 12.0 V battery, about 4 times as much energy per "
                  "coulomb", "correct": True},
         {"text": "The 3.0 V battery, because a smaller rating means "
                  "each coulomb is packed with more energy",
          "correct": False,
          "why": "A larger p.d. means MORE energy per coulomb, not "
                 "less — that is exactly what the volt measures."},
         {"text": "Neither — both give each coulomb the same energy, "
                  "because both are made of the same kind of cells",
          "correct": False,
          "why": "The chemistry decides one cell's push, but the "
                 "battery's rating is what each coulomb is given, and "
                 "these two ratings differ."},
     ], "figure": None},
    {"id": "p8-04-e19", "band": "easier",
     "text": "Roughly what p.d. does a USB phone charger supply at its "
             "socket?",
     "options": [
         {"text": "About 0.5 V", "correct": False,
          "why": "That is less than a single AA cell gives, far too "
                 "little to charge a phone at any useful rate."},
         {"text": "About 50 V", "correct": False,
          "why": "That is ten times too large for a USB socket, and "
                 "well above anything considered safe to handle on a "
                 "bare connector."},
         {"text": "About 5 V", "correct": True},
         {"text": "About 500 V", "correct": False,
          "why": "That is closer to industrial machinery than to a "
                 "charging lead; no small consumer socket supplies "
                 "hundreds of volts."},
     ], "figure": None},
    {"id": "p8-04-e20", "band": "easier",
     "text": "Two identical resistors sit in series on a battery. Must "
             "the p.d. across each one be the same?",
     "options": [
         {"text": "Yes — identical resistors always take identical "
                  "shares of the battery's p.d.", "correct": True},
         {"text": "No — the one nearer the battery takes the "
                  "bigger share", "correct": False,
          "why": "Position in a single loop makes no difference to the "
                 "share a component takes; only its own resistance "
                 "compared with the others does."},
         {"text": "No — the shares are random and cannot be predicted",
          "correct": False,
          "why": "The shares are not random; equal resistances in "
                 "series always take equal shares of the p.d."},
         {"text": "It depends on which terminal of the battery is drawn "
                  "on the left", "correct": False,
          "why": "Left or right on the page makes no difference to how "
                 "the p.d. is shared between identical resistors."},
     ], "figure": None},
    {"id": "p8-04-e21", "band": "easier",
     "text": "A single cell rated 1.5 V is put in a torch the wrong way "
             "round. Does the p.d. it supplies change size?",
     "options": [
         {"text": "Yes — a reversed cell supplies half its rated value",
          "correct": False,
          "why": "There is no halving from reversing a cell; its rated "
                 "p.d. is unchanged, just the direction of the push "
                 "flips."},
         {"text": "No — it still supplies 1.5 V", "correct": True},
         {"text": "Yes — a reversed cell supplies 0 V", "correct": False,
          "why": "A reversed cell pushes just as hard as before; just "
                 "the direction changes, not the size of the p.d."},
         {"text": "Yes — a reversed cell supplies double its rated "
                  "value", "correct": False,
          "why": "Reversing a cell does not change how hard it pushes; "
                 "the p.d. stays at its rated 1.5 V either way."},
     ], "figure": None},
    {"id": "p8-04-e22", "band": "easier",
     "text": "750 mV, written in volts, is…",
     "options": [
         {"text": "75.0 V", "correct": False,
          "why": "That divides by 10, far too small a conversion for "
                 "millivolts to volts."},
         {"text": "750 V", "correct": False,
          "why": "That leaves the number unchanged; converting from "
                 "millivolts to volts must make it smaller."},
         {"text": "0.750 V", "correct": True},
         {"text": "7.50 V", "correct": False,
          "why": "That divides by 100 rather than 1000, giving ten "
                 "times too large a value."},
     ], "figure": None},
    {"id": "p8-04-e23", "band": "easier",
     "text": "A battery's rating tells you what it supplies. A "
             "component's rating tells you…",
     "options": [
         {"text": "how much current it will draw, in any circuit "
                  "it is put into", "correct": False,
          "why": "The current a component draws depends on the whole "
                 "circuit, not on its rating alone; the rating names its "
                 "designed p.d."},
         {"text": "how much energy it stores permanently",
          "correct": False,
          "why": "A rated component, like a lamp or a resistor, does "
                 "not store energy permanently; a rating names the p.d. "
                 "it is designed to run at."},
         {"text": "what it supplies as well, in exactly the same sense",
          "correct": False,
          "why": "A component does not supply a p.d. of its own; its rating "
                 "instead names the p.d. it is designed to receive."},
         {"text": "what p.d. it is designed to run at", "correct": True},
     ], "figure": None},
    {"id": "p8-04-e24", "band": "easier",
     "text": "A p.d. of zero volts is measured across a length of wire. "
             "Is any current flowing through it?",
     "options": [
         {"text": "Not necessarily — a very low-resistance wire can "
                  "carry real current", "correct": True},
         {"text": "No — a reading of zero volts means the current is zero too",
          "correct": False,
          "why": "A p.d. near zero across a low-resistance wire is "
                 "entirely normal even while a real current flows "
                 "through it."},
         {"text": "Yes — a reading of exactly zero can only come from a "
                  "current that is flowing", "correct": False,
          "why": "A reading of exactly zero says nothing certain about "
                 "current on its own; it mainly reflects how little the "
                 "wire resists the flow."},
         {"text": "It depends on which way round the voltmeter is "
                  "connected", "correct": False,
          "why": "Reversing the voltmeter's leads just flips the sign "
                 "of a reading; it does not decide whether current is "
                 "flowing through the wire."},
     ], "figure": None},
    {"id": "p8-04-e25", "band": "easier",
     "text": "Which of these p.d.s would normally be quoted in millivolts "
             "rather than in volts?",
     "options": [
         {"text": "The p.d. across the terminals of a car battery",
          "correct": False,
          "why": "A car battery's p.d. runs to double figures in volts, "
                 "so quoting it in millivolts would mean writing tens of "
                 "thousands of them."},
         {"text": "The faint signal picked up from a beating heart by a "
                  "hospital monitor", "correct": True},
         {"text": "The p.d. at a UK wall socket", "correct": False,
          "why": "A wall socket's p.d. runs to hundreds of volts, which "
                 "would be hundreds of thousands of millivolts — a "
                 "clumsy way to write it."},
         {"text": "The p.d. across a single AA cell", "correct": False,
          "why": "A single cell's p.d. is a little over one volt, which "
                 "is already a convenient size; there is no reason to "
                 "quote it as a thousand-odd millivolts."},
     ], "figure": None},
    {"id": "p8-04-e26", "band": "easier",
     "text": "A student says a voltmeter and an ammeter are basically "
             "the same instrument, just with different dials. Is that a "
             "fair description?",
     "options": [
         {"text": "Yes — both take almost no current for themselves",
          "correct": False,
          "why": "An ammeter is built to take current freely, almost "
                 "like a plain wire; a voltmeter is built to take "
                 "almost none."},
         {"text": "Yes, since both give their reading in the same "
                  "unit", "correct": False,
          "why": "They give readings in different units — amps for an "
                 "ammeter, volts for a voltmeter — because they measure "
                 "different quantities."},
         {"text": "No — they measure different quantities",
          "correct": True},
         {"text": "Yes — both are wired into the loop in exactly the "
                  "same way", "correct": False,
          "why": "Just an ammeter is wired into the loop; a voltmeter "
                 "goes across a component instead, in parallel with it."},
     ], "figure": None},
    {"id": "p8-04-e27", "band": "easier",
     "text": "A lamp is rated 6 V. Connected to a 6 V battery on its "
             "own, what should a voltmeter across it read?",
     "options": [
         {"text": "3 V, since a single component takes half the "
                  "battery's p.d.", "correct": False,
          "why": "There is no such halving rule; a single component "
                 "alone in the loop takes the WHOLE of the battery's "
                 "p.d."},
         {"text": "0 V, since the lamp uses up the p.d. before the "
                  "voltmeter can measure it", "correct": False,
          "why": "A voltmeter measures the p.d. across the lamp "
                 "directly; nothing is used up before it can be read."},
         {"text": "12 V, since the lamp doubles the p.d. it receives",
          "correct": False,
          "why": "A lamp does not amplify or double a p.d.; with just "
                 "one component in the loop, it simply takes the "
                 "battery's own value."},
         {"text": "6 V", "correct": True},
     ], "figure": None},
    {"id": "p8-04-e28", "band": "easier",
     "text": "Two shares in a series loop are written down as 1.5 V and "
             "1500 mV. A student says one of them must have been copied "
             "down wrongly, because they look nothing like each other. "
             "What is right?",
     "options": [
         {"text": "The two shares are exactly the same size, because "
                  "1500 mV is 1.5 V", "correct": True},
         {"text": "The student is right, because 1500 mV is a thousand "
                  "times bigger than 1.5 V", "correct": False,
          "why": "The prefix is already doing that work: 1500 millivolts "
                 "IS 1.5 volts, so the two figures are equal rather than "
                 "a thousand apart."},
         {"text": "The student is right, because a p.d. in a series loop "
                  "can never be written in millivolts", "correct": False,
          "why": "Any p.d. may be written in millivolts if the size "
                 "suits; the unit chosen says nothing about where in a "
                 "circuit the reading was taken."},
         {"text": "The 1500 mV share is the larger of the two, because "
                  "1500 is the bigger number written down", "correct": False,
          "why": "Bare numbers in different units cannot be compared; "
                 "once 1500 mV is converted it comes to 1.5 V, exactly "
                 "the same as the other share."},
     ], "figure": None},
    {"id": "p8-04-e29", "band": "easier",
     "text": "A student says: \"A bigger battery always means a bigger "
             "p.d.\" Is size a reliable way to judge a battery's p.d.?",
     "options": [
         {"text": "It is reliable for single-cell batteries and no "
                  "cell inside them", "correct": False,
          "why": "Even among single-cell batteries, physical size does "
                 "not reliably predict the p.d.; the rating depends on "
                 "the cell chemistry, not the casing size."},
         {"text": "No — a battery's p.d. comes from its cells and their "
                  "arrangement, not from its physical size",
          "correct": True},
         {"text": "Yes — bigger batteries are built with more "
                  "cells inside them", "correct": False,
          "why": "Physical size does not reliably tell you how many "
                 "cells are inside or how they are arranged; two "
                 "different-sized batteries can supply the same p.d."},
         {"text": "Yes, because a bigger battery has a thicker "
                  "casing built to handle a bigger push", "correct": False,
          "why": "Casing thickness is not linked to p.d. in this way; "
                 "size alone tells you nothing reliable about a "
                 "battery's rating."},
     ], "figure": None},
    {"id": "p8-04-e30", "band": "easier",
     "text": "Two lamps sit on separate branches, each connected straight "
             "across the same 6 V battery. What p.d. does a voltmeter "
             "read across EACH lamp?",
     "options": [
         {"text": "6 V across one and 0 V across the other",
          "correct": False,
          "why": "Both branches sit identically across the same two "
                 "points of the battery, so both read the same p.d."},
         {"text": "12 V across each, since two branches double the "
                  "battery's p.d.", "correct": False,
          "why": "Nothing in the circuit can exceed the battery's own "
                 "p.d.; adding a branch does not multiply it."},
         {"text": "6 V across each", "correct": True},
         {"text": "3 V across each, since the battery shares its p.d. "
                  "between the two branches", "correct": False,
          "why": "Sharing is the series rule. Each parallel branch is "
                 "connected straight across the battery and gets the "
                 "whole of its p.d."},
     ], "figure": None},
    # ── MRB-338 night 3 top-up · standard ─────────────────────────────

    {"id": "p8-04-s08", "band": "standard",
     "text": "A 9.0 V battery drives three components in series. Two "
             "voltmeter readings across two of them are 2.0 V and "
             "3.5 V. What is the reading across the third?",
     "options": [
         {"text": "3.5 V", "correct": True},
         {"text": "14.5 V, all three given numbers added together",
          "correct": False,
          "why": "The battery's own 9.0 V is the total to reach, not "
                 "another value to add to the two known shares."},
         {"text": "5.5 V, the two known shares added", "correct": False,
          "why": "That gives the combined size of the two KNOWN shares, "
                 "not what remains for the third."},
         {"text": "3.0 V, sharing the battery equally between three "
                  "components", "correct": False,
          "why": "Equal sharing does not apply once two shares are "
                 "already measured unequally; the third is simply what "
                 "remains of the total."},
     ], "figure": None},
    {"id": "p8-04-s09", "band": "standard",
     "text": "A 6.0 V battery drives a lamp and a resistor in series. A "
             "voltmeter across the lamp reads 2500 mV. What does it read "
             "across the resistor, in volts?",
     "options": [
         {"text": "5.75 V, treating 2500 mV as 0.25 V before subtracting",
          "correct": False,
          "why": "2500 mV converts to 2.5 V, not 0.25 V — a factor of "
                 "ten is lost before the subtraction even begins."},
         {"text": "3.5 V", "correct": True},
         {"text": "8.5 V, adding the lamp's share to the battery's p.d. "
                  "instead of taking it away", "correct": False,
          "why": "The two shares have to ADD to the battery's 6.0 V, so "
                 "the resistor's share is found by taking the lamp's "
                 "2.5 V away from 6.0 V, not by adding it on."},
         {"text": "3.0 V, halving the battery's p.d. between the two "
                  "components", "correct": False,
          "why": "Halving assumes equal shares, but the lamp's share is "
                 "already known to be 2.5 V, not half of 6.0 V."},
     ], "figure": None},
    {"id": "p8-04-s10", "band": "standard",
     "text": "A lamp branch and a resistor branch each sit on their own "
             "path across the same battery. The resistor is then "
             "swapped for one with much higher resistance. What happens "
             "to the p.d. across the LAMP?",
     "options": [
         {"text": "It rises, since the higher-resistance branch pushes the "
                  "p.d. it cannot use across onto the lamp's branch "
                  "instead of keeping it", "correct": False,
          "why": "A branch does not push extra p.d. onto its "
                 "neighbour; each parallel branch simply has the whole "
                 "battery p.d. across it, unaffected by the others."},
         {"text": "It becomes impossible to predict without knowing "
                  "the exact new resistance value", "correct": False,
          "why": "No resistance value is needed — a parallel branch's "
                 "p.d. is fixed by the battery alone, whatever sits in "
                 "the other branch."},
         {"text": "Nothing changes — a parallel branch always has the "
                  "whole battery p.d. across it, whichever way the "
                  "other branch is changed", "correct": True},
         {"text": "It falls, since the higher-resistance branch now "
                  "takes a bigger share of the battery's p.d., leaving "
                  "less of it for the lamp's branch to work with",
          "correct": False,
          "why": "Sharing a p.d. is the SERIES rule. Each parallel "
                 "branch has the whole of the battery's p.d. across it, "
                 "whatever is in the other branch."},
     ], "figure": None},
    {"id": "p8-04-s11", "band": "standard",
     "text": "A device needs 4.5 V to run. Its holder takes identical "
             "1.5 V cells, wired in series. How many cells does it need?",
     "options": [
         {"text": "Two, because two cells in series give more than twice "
                  "one cell's push", "correct": False,
          "why": "Two cells in series give 3.0 V and no more: each cell "
                 "adds its own 1.5 V to the total and nothing beyond "
                 "that."},
         {"text": "Three, because three lots of 1.5 V add to 4.5 V",
          "correct": True},
         {"text": "Four, because one cell's push is lost to the holder's "
                  "metal contacts", "correct": False,
          "why": "A holder's contacts take a share far too small to "
                 "measure, so no spare cell is needed: three cells at "
                 "1.5 V add to exactly 4.5 V."},
         {"text": "It cannot be worked out without knowing what kind of "
                  "device it is", "correct": False,
          "why": "The count follows from the arithmetic alone — 4.5 V "
                 "divided by 1.5 V per cell — whatever the device turns "
                 "out to be."},
     ], "figure": None},
    {"id": "p8-04-s12", "band": "standard",
     "text": "A 3 V battery drives two identical lamps in series. Their "
             "combined voltmeter reading — across both lamps together "
             "— is measured. What should it read, and why?",
     "options": [
         {"text": "3 V, since the two individual shares must add back "
                  "to the battery's own p.d.", "correct": True},
         {"text": "1.5 V, half the battery's p.d., since two lamps are "
                  "sharing it", "correct": False,
          "why": "Reading across BOTH lamps together captures the "
                 "whole shared p.d., which adds back to the full 3 V, "
                 "not half of it."},
         {"text": "6 V, since reading across two lamps doubles the value "
                  "a single one would show", "correct": False,
          "why": "Nothing in the loop can exceed the battery's own "
                 "p.d.; reading across both lamps together simply "
                 "recovers the full 3 V."},
         {"text": "0 V, since the two lamps' shares cancel each other "
                  "out", "correct": False,
          "why": "The two shares add together rather than cancelling; "
                 "together they recover the full battery p.d."},
     ], "figure": None},
    {"id": "p8-04-s13", "band": "standard",
     "text": "Explain why a component's rating and a battery's rating, "
             "though both measured in volts, mean different things.",
     "options": [
         {"text": "A component's rating applies only once it starts to "
                  "fail", "correct": False,
          "why": "A rating describes the component's normal, intended "
                 "operating p.d., not a value that matters only once it "
                 "is failing."},
         {"text": "A component's rating names the p.d. it receives; a "
                  "battery's names what it supplies", "correct": True},
         {"text": "A component's rating names its resistance in "
                  "disguise, while a battery's rating names its p.d.",
          "correct": False,
          "why": "A component's rating is a p.d. value in its own right, not a "
                 "disguised resistance; resistance is measured "
                 "separately, in ohms."},
         {"text": "Both ratings mean exactly the same thing; the wording "
                  "used is all that differs between them", "correct": False,
          "why": "The two ratings describe opposite roles — one names "
                 "what is supplied, the other names what is expected to "
                 "be received."},
     ], "figure": None},
    {"id": "p8-04-s14", "band": "standard",
     "text": "A voltmeter is mistakenly wired into the main loop instead "
             "of across a component. What happens to the circuit?",
     "options": [
         {"text": "The circuit short-circuits, since a voltmeter has "
                  "almost no resistance", "correct": False,
          "why": "A voltmeter has almost no resistance is backwards — "
                 "it is built with very HIGH resistance so it barely "
                 "disturbs a circuit it is placed across."},
         {"text": "The voltmeter is destroyed instantly, but the rest "
                  "of the circuit keeps running normally", "correct": False,
          "why": "The voltmeter is not destroyed; its very high "
                 "resistance simply chokes off the current in the loop "
                 "it is now part of."},
         {"text": "The current in the loop almost stops, since a "
                  "voltmeter is built to take almost no current",
          "correct": True},
         {"text": "Nothing changes, since a voltmeter behaves the same "
                  "wherever it is connected", "correct": False,
          "why": "Where a voltmeter is connected matters a great deal — "
                 "wired into the loop, its huge resistance almost stops "
                 "the current."},
     ], "figure": None},
    {"id": "p8-04-s15", "band": "standard",
     "text": "A voltmeter is left connected across a torch's battery. "
             "Over an evening of use the battery runs flat and the bulb "
             "stops lighting. What happens to the voltmeter's reading "
             "over that time?",
     "options": [
         {"text": "It stays fixed at the battery's printed rating the "
                  "whole time, since a rating never changes",
          "correct": False,
          "why": "A rating names the DESIGNED p.d.; the actual reading "
                 "falls well below it as the battery's chemical store "
                 "runs down."},
         {"text": "It falls, well below the battery's rated value, as "
                  "the chemical store that drives the push runs down",
          "correct": True},
         {"text": "It rises, since a flat battery has to push harder to "
                  "keep any current flowing", "correct": False,
          "why": "A flat battery pushes less hard, not harder; that is "
                 "exactly why the bulb dims and finally goes out."},
         {"text": "It reads zero the instant the bulb goes out, with no "
                  "gradual change beforehand", "correct": False,
          "why": "The reading falls gradually as the battery weakens "
                 "over the evening, rather than staying at its rated "
                 "value and then dropping suddenly to zero."},
     ], "figure": None},
    {"id": "p8-04-s16", "band": "standard",
     "text": "A student says: \"A bigger p.d. across a lamp always means "
             "more current is flowing through it.\" Is that a safe rule "
             "to rely on?",
     "options": [
         {"text": "Yes, for one FIXED lamp, since a bigger push through "
                  "the same resistance drives more current",
          "correct": True},
         {"text": "No — p.d. and current are completely unrelated "
                  "quantities in any circuit", "correct": False,
          "why": "They are closely related for a single, fixed "
                 "component — a bigger p.d. across it does drive more "
                 "current through it."},
         {"text": "No — a bigger p.d. means LESS current is "
                  "flowing", "correct": False,
          "why": "That is backwards; for a fixed component, a bigger "
                 "p.d. across it drives a bigger current through it, "
                 "not a smaller one."},
         {"text": "Yes, but only for components with no resistance of "
                  "their own", "correct": False,
          "why": "The relationship holds for an ordinary resistive "
                 "component too, which is the more common case; it is "
                 "not limited to resistance-free ones."},
     ], "figure": None},
    {"id": "p8-04-s17", "band": "standard",
     "text": "A torch bulb rated 2.5 V is compared with one rated 6 V. "
             "Which bulb is designed to run on the bigger push, and does "
             "that alone tell you which one is brighter?",
     "options": [
         {"text": "Neither rating tells you anything about the push "
                  "each bulb is designed for", "correct": False,
          "why": "A rating is precisely the designed p.d.; here it "
                 "shows the 6 V bulb is designed for the bigger push of "
                 "the two."},
         {"text": "The 6 V bulb, but that alone does not settle which "
                  "one turns out to be the brighter of the two",
          "correct": True},
         {"text": "The 6 V bulb is designed for the bigger push, and "
                  "this alone guarantees it is the brighter bulb of the two",
          "correct": False,
          "why": "A rating names the DESIGNED push, not a guarantee "
                 "about brightness on its own — how each bulb is "
                 "run also matters."},
         {"text": "The 2.5 V bulb is designed for the bigger push, "
                  "since smaller numbers mean a bulb works harder",
          "correct": False,
          "why": "A smaller rating means a smaller designed push, not a "
                 "harder-working bulb; the 6 V bulb is the one designed "
                 "for the bigger push."},
     ], "figure": None},
    {"id": "p8-04-s18", "band": "standard",
     "text": "A 4.5 V battery drives a lamp and a buzzer in series. The "
             "lamp's share is measured at 2700 mV. What is the buzzer's "
             "share, in volts?",
     "options": [
         {"text": "7.2 V, adding the lamp's 2.7 V share to the battery's "
                  "4.5 V instead of taking it away", "correct": False,
          "why": "The two shares must add to the battery's 4.5 V, so the "
                 "buzzer's share is what is left once the lamp's 2.7 V "
                 "is taken away, not what you get by adding it on."},
         {"text": "4.23 V, subtracting 0.27 from 4.5", "correct": False,
          "why": "That misreads 2700 mV as 0.27 V; it converts "
                 "to 2.7 V, ten times larger."},
         {"text": "1.8 V", "correct": True},
         {"text": "2.25 V, splitting the battery's p.d. equally between "
                  "the lamp and the buzzer", "correct": False,
          "why": "An equal split would need the two components to resist "
                 "the same, and they clearly do not: the lamp's share is "
                 "already measured at 2.7 V, well over half of 4.5 V."},
     ], "figure": None},
    {"id": "p8-04-s19", "band": "standard",
     "text": "A parallel pair of lamps reads 6 V across each branch. A "
             "student says raising the battery to 12 V would make each "
             "lamp read 6 V still, \"since parallel branches always read "
             "the same as before\". Assess this.",
     "options": [
         {"text": "Right — a parallel branch's reading does not depend on "
                  "the battery's own p.d.", "correct": False,
          "why": "A parallel branch's reading depends directly on the "
                 "battery's p.d., since it is connected straight across "
                 "it."},
         {"text": "Right, but only because there are exactly two "
                  "branches in this example", "correct": False,
          "why": "The number of branches makes no difference; every "
                 "parallel branch tracks the battery's own p.d. "
                 "directly."},
         {"text": "Wrong — raising the battery would instead make each "
                  "branch read half of the new value", "correct": False,
          "why": "Halving is the series rule; a parallel branch simply "
                 "reads the same value the battery itself now supplies."},
         {"text": "Wrong — each branch is straight across the battery, "
                  "so its p.d. rises too", "correct": True},
     ], "figure": None},
    {"id": "p8-04-s20", "band": "standard",
     "text": "Two identical resistors are in series across a 9 V supply. "
             "A wire is taken from the point between them. What fraction "
             "of the 9 V would you expect to read between that point and "
             "one end?",
     "options": [
         {"text": "About half, since the two identical resistors share "
                  "the p.d. equally", "correct": True},
         {"text": "All of it, since a tap point reads the full "
                  "supply value", "correct": False,
          "why": "A tap point between two components reads just that "
                 "component's own share, not the whole supply."},
         {"text": "None of it, since a tap point between two "
                  "components reads zero of its own", "correct": False,
          "why": "A tap point reads that component's genuine share of "
                 "the p.d., which is not zero unless that component has "
                 "no resistance."},
         {"text": "It cannot be estimated without knowing the exact "
                  "resistance values in ohms", "correct": False,
          "why": "Knowing the two resistors are IDENTICAL is already "
                 "enough to know they take equal shares, without "
                 "needing the exact ohm value."},
     ], "figure": None},
    {"id": "p8-04-s21", "band": "standard",
     "text": "A voltmeter reads 4.5 V across a resistor in a series "
             "loop. That resistor is then replaced with an IDENTICAL "
             "one, of the same value, and nothing else in the loop "
             "changes. Does the voltmeter's reading change?",
     "options": [
         {"text": "No — an identical replacement always takes exactly "
                  "the same share as before", "correct": True},
         {"text": "Yes — a fresh, unused component always starts by "
                  "taking a larger share until it settles in",
          "correct": False,
          "why": "A resistor does not need to \"settle in\"; an "
                 "identical replacement takes exactly the same share "
                 "from the very first instant."},
         {"text": "Yes — replacing any component always resets the "
                  "sharing in the whole loop", "correct": False,
          "why": "The share depends on the resistances involved, not on "
                 "whether a part has been physically swapped; an "
                 "identical part gives an identical share."},
         {"text": "It cannot be judged without knowing the exact "
                  "battery voltage", "correct": False,
          "why": "The battery's value is not needed to answer this — "
                 "since the resistor is unchanged in value, its share of "
                 "whatever the battery supplies stays the same."},
     ], "figure": None},
    {"id": "p8-04-s22", "band": "standard",
     "text": "A junction-style claim: \"A voltmeter reading tells you "
             "how much energy has ARRIVED at a point.\" Correct this "
             "statement.",
     "options": [
         {"text": "It should instead say the reading measures current "
                  "arriving at a point", "correct": False,
          "why": "Current, not p.d., is what could be described as "
                 "arriving at a point; but a voltmeter measures p.d., a "
                 "difference between two points."},
         {"text": "It should instead say the reading measures charge "
                  "arriving at a point", "correct": False,
          "why": "Charge is what an ammeter's reading relates to over "
                 "time, not what a voltmeter measures; a voltmeter "
                 "reads a difference, not an arrival."},
         {"text": "A voltmeter reading is a DIFFERENCE between two "
                  "points, not an amount arriving at just one point",
          "correct": True},
         {"text": "The statement is completely correct as it stands",
          "correct": False,
          "why": "A p.d. makes sense only as a comparison between two "
                 "points; it is not a quantity that arrives at a single "
                 "point on its own."},
     ], "figure": None},
    {"id": "p8-04-s23", "band": "standard",
     "text": "A 9 V battery drives a lamp and a resistor in series. The "
             "lamp's share is exactly THREE times the resistor's share. "
             "What is each share?",
     "options": [
         {"text": "4.5 V and 4.5 V, splitting the battery equally",
          "correct": False,
          "why": "Equal splitting applies only to equal shares; here "
                 "the lamp's share is stated to be three times the "
                 "resistor's, not equal to it."},
         {"text": "3 V and 6 V, matching the ratio the wrong way round",
          "correct": False,
          "why": "That gives the resistor the bigger share, but the "
                 "lamp's share is the one stated to be three times "
                 "larger."},
         {"text": "9 V and 3 V, treating the resistor's share as a "
                  "third of the BATTERY rather than of the lamp's "
                  "share", "correct": False,
          "why": "The ratio is between the lamp's and the resistor's "
                 "own shares, and those two shares must add to 9 V, not "
                 "come to 12 V between them."},
         {"text": "6.75 V and 2.25 V", "correct": True},
     ], "figure": None},
    {"id": "p8-04-s24", "band": "standard",
     "text": "A series loop has a battery, a lamp and a buzzer. The "
             "buzzer is removed and replaced with a plain wire link, "
             "leaving the loop complete. What happens to the p.d. "
             "across the lamp?",
     "options": [
         {"text": "It rises to almost the full battery p.d., since the "
                  "wire link now takes almost none of it",
          "correct": True},
         {"text": "It falls, since removing a component always lowers "
                  "what the remaining one can receive", "correct": False,
          "why": "Removing a component that took a real share, and "
                 "replacing it with one that takes almost none, leaves "
                 "MORE of the battery's p.d. for the lamp, not less."},
         {"text": "It stays exactly the same as before the swap",
          "correct": False,
          "why": "The lamp's share must still add with the wire link's "
                 "share to reach the battery's p.d.; since the wire "
                 "link's share falls close to zero, the lamp's share "
                 "must rise to make up for it."},
         {"text": "It cannot be judged without knowing the buzzer's "
                  "original resistance", "correct": False,
          "why": "This course's convention already treats a plain wire "
                 "link as having no resistance, which is enough on its "
                 "own to predict the outcome here."},
     ], "figure": None},
    {"id": "p8-04-s25", "band": "standard",
     "text": "A student wants to know a lamp's rated p.d. without a "
             "data sheet. They read the number printed on its base as "
             "\"3.7 V\". Is reading the printed number a reliable way to "
             "find the rating?",
     "options": [
         {"text": "It depends on whether the lamp is for a torch or a "
                  "car", "correct": False,
          "why": "The kind of device does not change whether a printed "
                 "rating can be trusted; either way it is the p.d. the "
                 "maker designed it for."},
         {"text": "Yes — a rating is normally printed directly on the "
                  "component for exactly this purpose", "correct": True},
         {"text": "No — the printed number is the CURRENT the lamp draws, "
                  "not the p.d. it is rated for", "correct": False,
          "why": "Manufacturers commonly print the rated p.d. on a "
                 "component; it is not a current value."},
         {"text": "No — a lamp's true rating can be found only by "
                  "connecting it to different batteries and testing",
          "correct": False,
          "why": "Testing is one way to check a rating, but reading a "
                 "clearly printed value is a perfectly reliable "
                 "shortcut when it is available."},
     ], "figure": None},
    {"id": "p8-04-s26", "band": "standard",
     "text": "Two batteries, one rated 3.0 V and one rated 4.5 V, are "
             "each connected to an IDENTICAL single lamp in turn. "
             "Compare the p.d. across the lamp in each case.",
     "options": [
         {"text": "The larger battery gives a SMALLER reading, since "
                  "extra p.d. is used up faster by the lamp",
          "correct": False,
          "why": "Nothing is used up by the lamp; a lone component "
                 "simply reads whatever p.d. its battery supplies."},
         {"text": "It cannot be predicted without knowing the lamp's "
                  "own rating", "correct": False,
          "why": "The lamp's rating is not needed to predict this — a "
                 "lone component reads exactly its battery's own "
                 "p.d., whatever its rating happens to be."},
         {"text": "3.0 V with the first battery, 4.5 V with the "
                  "second one", "correct": True},
         {"text": "The p.d. is the same both times, since the lamp "
                  "itself has not changed", "correct": False,
          "why": "A lone component's reading tracks the battery it is "
                 "connected to, not just its own fixed properties."},
     ], "figure": None},
    {"id": "p8-04-s27", "band": "standard",
     "text": "A 6 V supply drives two components in series. A "
             "voltmeter is moved from across the first component, to "
             "across the second, to across BOTH together. State what it "
             "reads in each of the three positions if the first takes "
             "2 V.",
     "options": [
         {"text": "2 V, then 2 V, then 4 V, since both individual "
                  "components should read the same", "correct": False,
          "why": "There is no reason for the two components to share "
                 "equally here; only the fact that they add to 6 V "
                 "together is guaranteed."},
         {"text": "2 V, then 6 V, then 8 V, adding each new reading to "
                  "the one before", "correct": False,
          "why": "The three readings are not simply added to one "
                 "another; the second component's own share is 6 minus "
                 "2, and both together recover the full 6 V."},
         {"text": "2 V, then 4 V, then 12 V, since reading across both "
                  "doubles the sum of the parts", "correct": False,
          "why": "Reading across both components together cannot "
                 "exceed the battery's own p.d.; it simply recovers the "
                 "full 6 V, not double the parts' sum."},
         {"text": "2 V, then 4 V, then 6 V", "correct": True},
     ], "figure": None},
    {"id": "p8-04-s28", "band": "standard",
     "text": "A car's dashboard shows \"12.6 V\" from its own battery "
             "sensor. Is this reading, on its own, a p.d. measurement "
             "in the same sense as a voltmeter across a school circuit "
             "component?",
     "options": [
         {"text": "Yes — it is a difference between the battery's two "
                  "terminals, shown digitally", "correct": True},
         {"text": "No — a dashboard sensor measures current, not p.d., "
                  "despite being labelled in volts", "correct": False,
          "why": "A reading labelled in volts is a p.d. "
                 "measurement; current would be labelled in amps "
                 "instead."},
         {"text": "No — car batteries do not have a genuine p.d. "
                  "across their terminals the way school cells do",
          "correct": False,
          "why": "A car battery's terminals do have a genuine p.d. "
                 "across them, exactly like a school cell's, just at a "
                 "higher rated value."},
         {"text": "It depends on whether the car's engine is currently "
                  "running", "correct": False,
          "why": "Whether the engine is running can change the exact "
                 "reading a little, but it does not change what kind of "
                 "quantity — a p.d. — the sensor is reporting."},
     ], "figure": None},
    {"id": "p8-04-s29", "band": "standard",
     "text": "A 4.5 V battery drives a lamp and a resistor in series. "
             "The lamp takes the SMALLER share of the two. Which "
             "component resists the current more?",
     "options": [
         {"text": "The resistor", "correct": True},
         {"text": "The lamp, since it took the smaller share and so "
                  "must be working harder", "correct": False,
          "why": "Working harder is not shown by a smaller share; the "
                 "bigger share of the p.d. goes to whichever component "
                 "resists more, not less."},
         {"text": "Neither — the share a component takes has nothing "
                  "to do with its resistance", "correct": False,
          "why": "The share a component takes is decided directly by "
                 "its resistance compared with the other one; the "
                 "bigger resistance takes the bigger share."},
         {"text": "It cannot be told without knowing the exact current "
                  "flowing in the loop", "correct": False,
          "why": "The current is the same through both components in "
                 "series, so it does not distinguish them; the SHARES "
                 "already reveal which one resists more."},
     ], "figure": None},
    {"id": "p8-04-s30", "band": "standard",
     "text": "Explain why a voltmeter needs a lead on each side of a "
             "component, while an ammeter's two leads are simply the "
             "wire coming in and going out.",
     "options": [
         {"text": "A voltmeter needs two leads because it is less "
                  "sensitive than an ammeter", "correct": False,
          "why": "Sensitivity is not the reason; it is about what "
                 "quantity is being measured — a difference between two "
                 "points, rather than a flow through one."},
         {"text": "An ammeter's two leads are also measuring a "
                  "difference, just like a voltmeter's", "correct": False,
          "why": "An ammeter measures the single current flowing "
                 "through the loop at that point, not a difference "
                 "between two separate points."},
         {"text": "A voltmeter measures a difference between two "
                  "points; an ammeter measures a single flow",
          "correct": True},
         {"text": "Both instruments need two leads for exactly the "
                  "same reason — to complete the loop through "
                  "themselves", "correct": False,
          "why": "An ammeter's two leads complete the loop through "
                 "itself; a voltmeter's two leads instead sit across a "
                 "component without joining the loop through itself."},
     ], "figure": None},
    # ── MRB-338 night 3 top-up · harder ───────────────────────────────

    {"id": "p8-04-h08", "band": "harder",
     "text": "A 9.0 V battery drives a lamp and a resistor in series. "
             "The resistor is then swapped for one letting the SAME "
             "current through at HALF the p.d. across it as before. "
             "What happens to the lamp's own p.d., given the current "
             "through the whole loop stays the same?",
     "options": [
         {"text": "It rises, since the lamp's share must make up "
                  "whatever the resistor's smaller share leaves",
          "correct": True},
         {"text": "It stays exactly the same, since the lamp itself has "
                  "not been touched", "correct": False,
          "why": "The two shares must always add to 9.0 V; if the "
                 "resistor's share halves, the lamp's own "
                 "share must rise to make up the difference."},
         {"text": "It falls, since a smaller resistor share always "
                  "drags the lamp's share down with it", "correct": False,
          "why": "The two shares move in OPPOSITE directions, since "
                 "together they must always add to the fixed 9.0 V "
                 "total."},
         {"text": "It becomes impossible to predict without knowing "
                  "the exact resistance values in ohms", "correct": False,
          "why": "The resistor's new share is already given indirectly "
                 "(half its old value), which is enough to find the "
                 "lamp's new share by subtraction from 9.0 V."},
     ], "figure": None},
    {"id": "p8-04-h09", "band": "harder",
     "text": "A designer needs FOUR identical warning lamps that must "
             "each run at their full rated 3 V, from a single 12 V "
             "supply, using no extra components beyond the lamps "
             "themselves. Is this achievable, and how?",
     "options": [
         {"text": "No — a single supply can drive no more than ONE lamp "
                  "at its exact rated p.d.", "correct": False,
          "why": "Multiple identical lamps in series can each land "
                 "exactly on their rating simultaneously, provided the "
                 "supply is an exact multiple of that rating."},
         {"text": "Yes — wire all four in series; four identical 3 V "
                  "lamps share the 12 V supply exactly, 3 V each",
          "correct": True},
         {"text": "Yes — wire all four in parallel; parallel branches "
                  "automatically share a bigger supply down to each "
                  "lamp's rating", "correct": False,
          "why": "Parallel branches do not share the supply down at "
                 "all — each would receive the full 12 V, well above "
                 "each lamp's 3 V rating."},
         {"text": "No — achieving exactly 3 V per lamp from a 12 V "
                  "supply needs an extra resistor somewhere",
          "correct": False,
          "why": "Four identical 3 V lamps in series divide a 12 V "
                 "supply exactly evenly on their own, with no extra "
                 "component needed."},
     ], "figure": None},
    {"id": "p8-04-h10", "band": "harder",
     "text": "A parallel pair of lamps and a series pair of identical "
             "lamps are both connected to their own 6 V battery. State, "
             "for EACH pair, what happens to the p.d. across a lamp if "
             "one lamp is removed from that pair.",
     "options": [
         {"text": "Both pairs behave the same way: removing a lamp "
                  "breaks the whole arrangement in either case",
          "correct": False,
          "why": "Removing a lamp from a PARALLEL pair leaves the "
                 "surviving branch completely intact and working; only "
                 "removing one from a SERIES pair changes what remains "
                 "in this particular way."},
         {"text": "Parallel: the survivor's p.d. rises to 12 V. "
                  "Series: the survivor's p.d. stays at half of 6 V",
          "correct": False,
          "why": "Nothing in either circuit can exceed the battery's "
                 "own 6 V, and the series survivor — now alone in the "
                 "loop — takes the WHOLE 6 V, not half of it."},
         {"text": "Parallel: the survivor stays at 6 V. Series: the "
                  "lone survivor rises to the full 6 V too",
          "correct": True},
         {"text": "Both pairs behave the same way: removing a lamp "
                  "makes the survivor's p.d. rise to the full 6 V",
          "correct": False,
          "why": "A parallel branch already reads the full 6 V before "
                 "any removal, so there is no rise left for it to "
                 "make — only the series survivor's p.d. "
                 "rises."},
     ], "figure": None},
    {"id": "p8-04-h11", "band": "harder",
     "text": "A student claims: \"Since current is the same everywhere "
             "in a series loop, p.d. must be the same everywhere too, "
             "by the same logic.\" Explain precisely why this reasoning "
             "fails.",
     "options": [
         {"text": "The reasoning is sound; p.d. is "
                  "the same everywhere in a series loop, just like "
                  "current", "correct": False,
          "why": "P.d. varies component to component in series — that "
                 "is precisely the sharing rule this lesson is built "
                 "around; only current stays uniform."},
         {"text": "Current is not the same everywhere in a "
                  "series loop either, so the comparison is meaningless "
                  "from the start", "correct": False,
          "why": "Current IS the same everywhere in a single "
                 "series loop; the flaw lies in extending that same "
                 "logic to a fundamentally different kind of quantity."},
         {"text": "P.d. and current are the same quantity "
                  "measured in different units, so the same rule should "
                  "apply to both", "correct": False,
          "why": "P.d. and current are different physical "
                 "quantities — one energy per charge, the other charge "
                 "per second — not the same thing in different units."},
         {"text": "Current is one flowing quantity; p.d. is a "
                  "difference BETWEEN two points, which naturally "
                  "varies with which points you pick", "correct": True},
     ], "figure": None},
    {"id": "p8-04-h12", "band": "harder",
     "text": "A 6.0 V battery drives two lamps in series, sharing "
             "2.0 V and 4.0 V. The battery is then swapped for a 12.0 V "
             "one, with nothing else in the circuit changed. Predict "
             "the NEW shares, using the fact that shares in series stay "
             "in the same ratio when the components themselves have not "
             "changed.",
     "options": [
         {"text": "4.0 V and 8.0 V", "correct": True},
         {"text": "8.0 V and 10.0 V, adding 6.0 V onto each old share",
          "correct": False,
          "why": "The shares must stay in the SAME RATIO as before "
                 "(1:2), and simply adding 6.0 V to each breaks that "
                 "ratio rather than preserving it."},
         {"text": "2.0 V and 4.0 V, unchanged, since the lamps "
                  "themselves have not been swapped", "correct": False,
          "why": "The lamps' resistances are unchanged, but the "
                 "battery driving them has doubled, so both shares "
                 "double too, to keep the same ratio at the new total."},
         {"text": "6.0 V and 6.0 V, splitting the new battery equally "
                  "between the two lamps", "correct": False,
          "why": "The two lamps are not stated to be identical — their "
                 "original 2.0 V and 4.0 V shares show they are not — "
                 "so an equal split is not right at the new voltage "
                 "either."},
     ], "figure": None},
    {"id": "p8-04-h13", "band": "harder",
     "text": "Assess this claim: \"A voltmeter with even LOWER "
             "resistance than usual would be a better voltmeter, since "
             "lower resistance always means a better meter.\"",
     "options": [
         {"text": "The claim cannot be assessed without knowing the "
                  "voltmeter's exact original resistance",
          "correct": False,
          "why": "No specific value is needed — for a voltmeter, "
                 "LOWERING its resistance from any starting point makes "
                 "it a worse meter, not a better one."},
         {"text": "False for a voltmeter — it needs the HIGHEST "
                  "resistance practical, so it barely disturbs the "
                  "circuit", "correct": True},
         {"text": "True — a voltmeter, like any meter, works "
                  "better with lower resistance", "correct": False,
          "why": "A voltmeter is a special case: unlike an ammeter, "
                 "lowering its resistance would make it disturb the "
                 "circuit MORE, not less."},
         {"text": "True, but only once the voltmeter's resistance is "
                  "lower than the component it is measuring",
          "correct": False,
          "why": "Even then, a voltmeter's job is to draw almost no "
                 "current of its own — a lower resistance than the "
                 "component would draw a significant, disturbing "
                 "current."},
     ], "figure": None},
    {"id": "p8-04-h14", "band": "harder",
     "text": "A parallel pair of lamps, each rated 6 V, is driven by a "
             "6 V battery. A THIRD identical lamp is then added in "
             "SERIES, between the battery and the junction feeding the "
             "pair. Explain what happens to the ORIGINAL two lamps, in "
             "terms of both their p.d. and their rating.",
     "options": [
         {"text": "The p.d. across the pair rises above 6 V, since "
                  "adding any lamp anywhere increases the total p.d. "
                  "available", "correct": False,
          "why": "A lamp does not add p.d. of its own; adding one ahead "
                 "of the junction can only take a share, lowering what "
                 "reaches the pair, not raising it."},
         {"text": "The pair is completely unaffected, since the new "
                  "lamp is in series and the pair is in parallel — "
                  "different arrangements do not interact",
          "correct": False,
          "why": "A series component placed AHEAD of a parallel "
                 "junction absolutely does affect what reaches that "
                 "junction, despite the pair itself being wired in "
                 "parallel."},
         {"text": "The p.d. across the pair falls below 6 V, so both "
                  "original lamps now run below their 6 V rating and "
                  "glow more dimly than before", "correct": True},
         {"text": "The p.d. across the pair stays at 6 V, since "
                  "parallel branches keep the full battery p.d. "
                  "regardless of anything added ahead of them",
          "correct": False,
          "why": "Parallel branches keep the full p.d. of whatever "
                 "REACHES them; the new lamp ahead of the junction now "
                 "takes a share first, lowering what reaches the pair."},
     ], "figure": None},
    {"id": "p8-04-h15", "band": "harder",
     "text": "A battery is described just as having \"some p.d.\", with "
             "no number given. A single lamp is connected to it alone, "
             "and a voltmeter across the lamp reads a real, non-zero "
             "value. What single further fact would let you state the "
             "battery's own p.d. exactly, without moving the voltmeter?",
     "options": [
         {"text": "You would need to know the lamp's exact resistance "
                  "in ohms before the battery's p.d. could be stated",
          "correct": False,
          "why": "No resistance value is needed here — a lone "
                 "component's reading already equals the whole battery "
                 "p.d., regardless of its resistance."},
         {"text": "You would need a second voltmeter reading taken "
                  "directly across the battery's own terminals",
          "correct": False,
          "why": "That reading would simply repeat the same value the "
                 "lamp's voltmeter already shows, since the lamp alone "
                 "takes the whole battery p.d."},
         {"text": "You would need to know the current flowing through "
                  "the loop as well", "correct": False,
          "why": "The current is not needed to state the battery's "
                 "p.d. here; the lamp's own reading, with just it in "
                 "the loop, already gives that value directly."},
         {"text": "None is needed — with just the lamp in the loop, "
                  "the voltmeter's own reading already IS the battery's "
                  "p.d.", "correct": True},
     ], "figure": None},
    {"id": "p8-04-h16", "band": "harder",
     "text": "Two separate series loops each have a 9 V battery and two "
             "components. Loop A's shares are 3 V and 6 V. Loop B's "
             "shares are 4.5 V and 4.5 V. What single fact about Loop "
             "B's two components can you state with confidence that "
             "you cannot state about Loop A's?",
     "options": [
         {"text": "Loop B's two components resist the current equally; "
                  "Loop A's do not", "correct": True},
         {"text": "Loop B's battery is somehow stronger than Loop A's, "
                  "despite both being rated 9 V", "correct": False,
          "why": "Both batteries supply the same 9 V; the difference "
                 "between the loops is how that 9 V happens to be "
                 "shared, not the strength of either battery."},
         {"text": "Loop B carries more current than Loop A, since its "
                  "shares are more evenly split", "correct": False,
          "why": "An even split says nothing about the SIZE of the "
                 "current in that loop; it just tells you the two "
                 "components resist equally, relative to each other."},
         {"text": "Loop B's components must both be lamps, while Loop "
                  "A's must both be resistors", "correct": False,
          "why": "The kind of component cannot be read off from how "
                 "evenly the shares split; only their resistances "
                 "relative to each other can be compared this way."},
     ], "figure": None},
    {"id": "p8-04-h17", "band": "harder",
     "text": "Explain why the sharing rule for p.d. in series (shares "
             "add to the battery's value) and the addition rule for "
             "current at a junction (branches add to the main current) "
             "are, in a sense, MIRROR IMAGES of each other rather than "
             "the same rule twice.",
     "options": [
         {"text": "The junction rule is simply the series rule applied "
                  "to a different shape of circuit, with no real "
                  "conceptual difference between them", "correct": False,
          "why": "The conceptual difference is real: one rule "
                 "describes ONE current giving up its p.d. in stages; "
                 "the other describes SEVERAL currents combining into "
                 "one."},
         {"text": "In series, one current gives up its p.d. in "
                  "pieces; at a junction, several currents combine "
                  "into one — opposite in each case", "correct": True},
         {"text": "They are no different from one another — both rules "
                  "simply say that parts add up to a whole, so they are "
                  "the very same rule applied twice", "correct": False,
          "why": "Both involve addition, but WHAT is added differs "
                 "fundamentally — one shares out a single p.d. along a "
                 "path, the other combines several separate currents "
                 "into one."},
         {"text": "The series rule governs p.d. and the junction rule "
                  "governs current, so the two of them cannot "
                  "be compared to each other in any way", "correct": False,
          "why": "They CAN be meaningfully compared — the comparison "
                 "reveals a genuine structural mirroring, even though "
                 "they govern different quantities."},
     ], "figure": None},
    {"id": "p8-04-h18", "band": "harder",
     "text": "A 9 V battery drives a lamp in series with a plain wire "
             "link, in a single loop. The wire link is then replaced "
             "with an identical lamp. Track what happens to the FIRST "
             "lamp's own p.d. across this change, and explain why.",
     "options": [
         {"text": "It rises from a smaller value to 9 V, since adding "
                  "a matching lamp increases every other "
                  "component's own share", "correct": False,
          "why": "Adding a genuine second component to share with can "
                 "only lower an existing component's share, not raise "
                 "it, since together they must still add to just 9 V."},
         {"text": "It cannot be tracked without knowing the exact "
                  "resistance of the wire link before it was replaced",
          "correct": False,
          "why": "This course's convention already treats a plain "
                 "wire link as having no resistance, which is enough to "
                 "know the first lamp started at essentially the full "
                 "9 V."},
         {"text": "It falls from 9 V to 4.5 V, since the wire link took "
                  "almost no share of its own, but the new lamp takes an "
                  "equal share alongside it", "correct": True},
         {"text": "It stays at 9 V throughout, since the first lamp's "
                  "own resistance has not changed at any point",
          "correct": False,
          "why": "The first lamp's OWN resistance staying fixed does "
                 "not fix its SHARE — that depends on what else is in "
                 "the loop taking a share alongside it."},
     ], "figure": None},
    {"id": "p8-04-h19", "band": "harder",
     "text": "A technician wants to check whether a series loop's THREE "
             "components divide a 12 V supply correctly, using "
             "the fewest possible voltmeter readings. What is the "
             "minimum number of readings needed, and why?",
     "options": [
         {"text": "Three — every component's share must be measured "
                  "directly, since none can ever be inferred from the "
                  "others", "correct": False,
          "why": "The third share can be found by subtracting "
                 "the other two from the known 12 V total, so a direct "
                 "third reading is not strictly necessary."},
         {"text": "One — reading across any single component "
                  "automatically reveals the other two as well",
          "correct": False,
          "why": "A single reading just gives you that one component's "
                 "own share; it says nothing on its own about how the "
                 "remaining 12 V minus that share then splits between "
                 "the other two."},
         {"text": "None — the three shares can be predicted from "
                  "the supply voltage alone, without any voltmeter "
                  "readings taken", "correct": False,
          "why": "The supply voltage alone fixes just the TOTAL of the "
                 "three shares; how it splits between the "
                 "three components still needs measuring."},
         {"text": "Two — read across any two of the three components "
                  "directly, then find the third by subtracting both "
                  "from 12 V", "correct": True},
     ], "figure": None},
    {"id": "p8-04-h20", "band": "harder",
     "text": "A single 1.5 V cell is compared with four of the same "
             "cells in series (6.0 V), each driving an otherwise "
             "identical single lamp. Explain why the SAME lamp being "
             "used both times does not mean the p.d. across it is the "
             "same both times.",
     "options": [
         {"text": "A lone component's p.d. tracks whatever battery it "
                  "is connected to, not a fixed property of its own",
          "correct": True},
         {"text": "The lamp's resistance must secretly change between "
                  "the two tests, which is what changes its p.d.",
          "correct": False,
          "why": "The lamp's own resistance need not change; "
                 "what changes is simply the battery's own p.d. that it "
                 "is connected to."},
         {"text": "It is the same both times, since using the "
                  "identical lamp guarantees an identical reading",
          "correct": False,
          "why": "The readings differ — a lone component's "
                 "p.d. equals whatever its battery supplies, and the "
                 "two batteries here supply different values."},
         {"text": "The difference appears because the four-cell "
                  "battery is wired in parallel rather than in series",
          "correct": False,
          "why": "The four cells are stated to be in series, which is "
                 "exactly why their p.d.s add to 6.0 V rather than "
                 "staying at 1.5 V."},
     ], "figure": None},
    {"id": "p8-04-h21", "band": "harder",
     "text": "A single loop has a battery, a lamp and a switch. When the "
             "switch is OPEN, a voltmeter connected across the OPEN "
             "switch itself reads the full battery p.d.; the voltmeter "
             "across the lamp reads 0 V. Explain both readings.",
     "options": [
         {"text": "The switch's reading is a measurement error, since an "
                  "open switch cannot have any p.d. across its own gap",
          "correct": False,
          "why": "It is not an error — an open gap in an otherwise "
                 "resistance-free loop is exactly where the whole "
                 "battery p.d. does appear."},
         {"text": "With no current flowing, the lamp gives up no p.d. "
                  "at all; the switch's gap takes the whole battery "
                  "p.d.",
          "correct": True},
         {"text": "Both readings must be wrong, since a battery's p.d. "
                  "can never appear anywhere but across a working component, "
                  "not across an open switch", "correct": False,
          "why": "An open switch can carry the whole battery "
                 "p.d. across its gap — that gap is the one place any "
                 "real resistance now exists in the loop."},
         {"text": "The lamp reads 0 V because it is broken, unrelated "
                  "to the switch being open", "correct": False,
          "why": "Nothing here suggests the lamp is broken; with no "
                 "current flowing, ANY working component gives "
                 "up zero p.d., open switch or not."},
     ], "figure": None},
    {"id": "p8-04-h22", "band": "harder",
     "text": "Compare what happens to (a) the CURRENT and (b) the P.D. "
             "across each lamp, when two identical lamps are rewired "
             "from series to parallel on the same battery.",
     "options": [
         {"text": "Neither the current nor the p.d. changes for an "
                  "individual lamp, since rewiring changes the TOTAL "
                  "current from the battery and nothing else", "correct": False,
          "why": "An individual lamp's own p.d. and current both "
                 "change here — from a shared series value to the full "
                 "battery value in parallel."},
         {"text": "The current through each lamp rises, but the p.d. "
                  "across each stays the same, since p.d. depends only "
                  "on the lamp's own fixed resistance", "correct": False,
          "why": "A lamp's p.d. is not fixed by its own resistance "
                 "alone; it depends on how the whole circuit is wired, "
                 "and it rises when moving to parallel here."},
         {"text": "Both RISE, since in parallel each lamp gets the "
                  "full battery p.d. instead of a shared share",
          "correct": True},
         {"text": "The current through each lamp falls, while the p.d. "
                  "across each rises, since the two quantities always "
                  "move in opposite directions", "correct": False,
          "why": "They do not always move oppositely — here, moving to "
                 "parallel raises the p.d. across each lamp, which in "
                 "turn raises the current through each one too."},
     ], "figure": None},
    {"id": "p8-04-h23", "band": "harder",
     "text": "A 6.0 V battery, a lamp and a buzzer are wired in series. "
             "A student proposes adding a SECOND, identical 6.0 V "
             "battery in series with the first, facing the SAME way, to "
             "\"give the components more to share\". Predict the new "
             "p.d. shares, given the lamp originally took 2.0 V and the "
             "buzzer 4.0 V, and the two components' resistances stay "
             "fixed relative to each other.",
     "options": [
         {"text": "2.0 V and 4.0 V, unchanged, since neither component "
                  "was itself replaced", "correct": False,
          "why": "The two shares must add to the NEW total of 12.0 V, "
                 "not stay fixed at the old 6.0 V total, even though "
                 "the components themselves are unchanged."},
         {"text": "6.0 V and 6.0 V, splitting the new total equally "
                  "regardless of the original ratio", "correct": False,
          "why": "The original 2.0 V and 4.0 V shares already show the "
                 "two components do not resist equally, so an equal "
                 "split at the new total is not right either."},
         {"text": "12.0 V and 12.0 V, since both components now "
                  "individually receive the doubled battery's full "
                  "value", "correct": False,
          "why": "The two components still SHARE whatever the battery "
                 "supplies between them; neither can individually reach "
                 "the full new total on its own."},
         {"text": "4.0 V and 8.0 V, keeping the same 1:2 ratio at the "
                  "new 12.0 V total", "correct": True},
     ], "figure": None},
    {"id": "p8-04-h24", "band": "harder",
     "text": "Explain why it makes sense that a voltmeter's own "
             "reading changes very little when it is connected across "
             "an already-working circuit, while an ammeter's own "
             "insertion could, in principle, change the reading a "
             "great deal if it were poorly designed.",
     "options": [
         {"text": "A voltmeter's huge resistance means almost no "
                  "current flows through it; an ammeter must carry the "
                  "full current itself", "correct": True},
         {"text": "A voltmeter is simply a more modern, more accurate "
                  "design than an ammeter, which is why it disturbs "
                  "circuits less", "correct": False,
          "why": "The difference is not about which instrument is more "
                 "modern; it comes from where and how each is "
                 "connected, and what resistance each is built with."},
         {"text": "An ammeter disturbs a circuit more than a "
                  "voltmeter simply because it displays a bigger number "
                  "on its scale", "correct": False,
          "why": "The size of the number displayed has nothing to do "
                 "with how much either instrument disturbs the "
                 "circuit; that depends on the instrument's own "
                 "resistance and how it is wired in."},
         {"text": "Both instruments disturb a circuit by exactly the "
                  "same small amount, so the comparison in the question "
                  "does not hold up", "correct": False,
          "why": "The two instruments do differ here — a "
                 "voltmeter's very high resistance protects the "
                 "circuit, while a poorly designed ammeter's own "
                 "resistance would directly limit the very current it "
                 "is trying to measure."},
     ], "figure": None},
    {"id": "p8-04-h25", "band": "harder",
     "text": "A 9 V battery drives three components in series: a lamp, "
             "a buzzer and a resistor. The resistor is removed and "
             "replaced with a plain wire link. Track what happens to "
             "the COMBINED p.d. across the lamp and buzzer together, "
             "and explain why.",
     "options": [
         {"text": "It cannot be predicted without knowing the exact "
                  "resistance of the wire link that replaced the "
                  "resistor", "correct": False,
          "why": "This course's convention already treats a plain wire "
                 "link as having no resistance, which is enough on its "
                 "own to predict the outcome here."},
         {"text": "It rises to the full 9 V, since the wire link now "
                  "takes essentially none of the p.d.", "correct": True},
         {"text": "It falls, since removing a component lowers "
                  "what remains for the others to share", "correct": False,
          "why": "Removing a component that took a real share, and "
                 "replacing it with one that takes almost none, leaves "
                 "MORE for the others to share, not less."},
         {"text": "It stays exactly the same, since the resistor itself "
                  "was the one thing changed", "correct": False,
          "why": "The three shares must always add to the battery's "
                 "9 V; if the resistor's own share falls close to zero, "
                 "the combined share of the other two must rise to "
                 "make up for it."},
     ], "figure": None},
    {"id": "p8-04-h26", "band": "harder",
     "text": "Summarise, in ONE general statement, what a component's "
             "rating, a battery's rating, and the reading a voltmeter "
             "gives across any single component in a loop, all have in "
             "common.",
     "options": [
         {"text": "They have nothing in common beyond "
                  "happening to share the same unit by convention",
          "correct": False,
          "why": "Sharing the same unit here is not a coincidence — "
                 "all three describe the very same underlying "
                 "quantity, p.d., just in three different roles."},
         {"text": "They are comparable only once every component in "
                  "the loop is running at its own rated value "
                  "simultaneously", "correct": False,
          "why": "The comparison holds generally, not just in that "
                 "special case — all three are p.d. values whether or "
                 "not any component happens to be at its rating."},
         {"text": "All three are p.d. values, though what each "
                  "describes — a target, a supply, a share — differs",
          "correct": True},
         {"text": "All three are current values, despite "
                  "being conventionally written and labelled in volts",
          "correct": False,
          "why": "None of the three is a current value; all three "
                 "describe p.d. — energy per unit charge — which is "
                 "exactly why all three share the same unit."},
     ], "figure": None},
    {"id": "p8-04-h27", "band": "harder",
     "text": "A 6 V battery drives two lamps in series, taking 2 V and "
             "4 V. A wire is connected in parallel across BOTH lamps "
             "together, from one end of the pair to the other. Predict "
             "the new voltmeter reading across the WIRE itself, and "
             "explain what has happened to each lamp.",
     "options": [
         {"text": "6 V across the wire, since it is connected directly "
                  "across the battery's own full p.d.", "correct": False,
          "why": "The wire itself, having almost no resistance, gives "
                 "up almost no p.d. — it cannot read anywhere near the "
                 "battery's own 6 V."},
         {"text": "2 V across the wire, matching the first lamp's own "
                  "old share", "correct": False,
          "why": "The wire is connected across BOTH lamps together, "
                 "not just the first one, and its own reading reflects "
                 "its own near-zero resistance, not either lamp's old "
                 "share."},
         {"text": "The two lamps stay exactly as bright as before, "
                  "since the wire is simply an extra addition alongside "
                  "them", "correct": False,
          "why": "The wire offers a far easier path than either lamp, "
                 "so almost all the current now bypasses them entirely "
                 "— both lamps go dark rather than staying lit."},
         {"text": "Close to 0 V across the wire; both lamps go dark, "
                  "each reading close to 0 V too", "correct": True},
     ], "figure": None},
    {
        "id": "p8-04-h28",
        "band": "harder",
        "text": "In this circuit, ammeters A1 and A2 give the same reading, "
                "but voltmeters V1 and V2 give different readings. Has the "
                "student who set it up made a mistake?",
        "options": [
            {"text": "No: the current is the same all round the loop, but "
                     "the p.d. shares can differ",
             "correct": True},
            {"text": "Yes: if the two currents are equal, the two p.d.s must "
                     "be equal too",
             "correct": False,
             "why": "Current is the same everywhere in one loop, but p.d. "
                    "depends on which component the voltmeter is across. "
                    "Different components can take different shares."},
            {"text": "Yes: A2 should read less than A1, because the lamp "
                     "uses up some of the current",
             "correct": False,
             "why": "Current is not used up. What the lamp takes is energy, "
                    "so A1 and A2 must read the same."},
            {"text": "Yes: the voltmeters should always read the same as "
                     "each other in a single loop",
             "correct": False,
             "why": "In a single loop the cell's p.d. is shared between the "
                    "components. V1 and V2 only match if the lamp and the "
                    "resistor take equal shares."},
        ],
        "figure": "p8-series-meters-lamp-resistor",
    },
    {"id": "p8-04-h29", "band": "harder",
     "text": "A 9 V battery drives two lamps in series. The FIRST lamp "
             "is swapped for one with much LOWER resistance, while the "
             "current through the loop stays observably almost "
             "unchanged (the second lamp dominates the loop's total "
             "resistance). Predict what happens to each lamp's p.d. "
             "share.",
     "options": [
         {"text": "The first lamp's share rises, since lower resistance "
                  "means a bigger share of the p.d.",
          "correct": False,
          "why": "Lower resistance means a SMALLER share for the same "
                 "current passing through it, the opposite of what this "
                 "option claims."},
         {"text": "The first lamp's share falls close to 0 V; the "
                  "second lamp's share rises to take up almost the "
                  "whole 9 V", "correct": True},
         {"text": "Both shares fall together, since lowering any "
                  "resistance in the loop lowers every share in "
                  "it", "correct": False,
          "why": "The two shares must still add to 9 V; if one falls "
                 "close to zero, the other must rise to make up the "
                 "difference, not fall alongside it."},
         {"text": "Both shares stay exactly as they were, since the "
                  "current through the loop is stated to be almost "
                  "unchanged", "correct": False,
          "why": "Even with the current nearly unchanged, a much lower "
                 "resistance in the first lamp means it now gives up "
                 "far less p.d. for that same current, so its share "
                 "does fall."},
     ], "figure": None},
    {"id": "p8-04-h30", "band": "harder",
     "text": "Explain why measuring \"the p.d. of a battery\" makes "
             "sense as a single number, while asking \"the p.d. of a "
             "whole series circuit\" is ambiguous unless you specify "
             "which two points you mean.",
     "options": [
         {"text": "A battery's p.d. is fixed by law and cannot vary, "
                  "unlike a circuit's, which is why the battery alone "
                  "gives one clean number", "correct": False,
          "why": "It is not about the battery's p.d. being fixed by "
                 "law; it is simply that a battery has just one pair of "
                 "terminals to measure between, unlike a multi-component "
                 "circuit."},
         {"text": "Both questions are equally ambiguous; a battery's "
                  "p.d. also depends on which two points you choose",
          "correct": False,
          "why": "A battery offers just ONE meaningful pair of points — "
                 "its two terminals — so there is nothing left to "
                 "specify, unlike a circuit with several components."},
         {"text": "A battery has only two terminals to compare; a "
                  "circuit offers many different pairs of points",
          "correct": True},
         {"text": "A whole circuit has no p.d. of its own, so "
                  "the question is meaningless rather than merely "
                  "ambiguous", "correct": False,
          "why": "A circuit does have p.d.s to measure — between any "
                 "pair of points in it — which is exactly why the "
                 "question needs those two points specified, rather "
                 "than being meaningless."},
     ], "figure": None},
]
