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
]
