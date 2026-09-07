"""P8 lesson 07 — Building and measuring a circuit: twelve questions
(MRB-223).

Written against Design's page. The two pairs with the same diagram, the
bench you wire wrong on purpose and the six-row fault table are hers.

The discriminations, in the order the lesson builds them:

  · a meter's OWN RESISTANCE is what decides where it goes;
  · a zero reading is usually a true reading of a broken loop
    (`CIRC-25`);
  · a meter in the wrong place builds a different circuit and then reads
    it correctly (`CIRC-28`) — the harder band sits here;
  · a value that refuses to sit with the rest is repeated, never smoothed
    over.

⚠️ POSITION IS AUTHORED AND MEASURED —
3,2,1,0 · 0,1,2,3 · 1,0,3,1;
the twelve fall 3/4/2/3 across the four indices.

⚠️ Neither ladder rung is restated: not the 0.00 A with 3.00 V symptom,
and not the student who wires the voltmeter into the loop and reads it as
success. This lesson has no worked examples, so no worked figure can be
restated either.
"""

UNIT = "P8"
LESSON = "building-and-measuring-a-circuit"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p8-07-e01",
        "band": "easier",
        "text": "An ammeter is built to have…",
        "options": [
            {"text": "an enormous resistance, so it draws almost nothing",
             "correct": False,
             "why": "That is a voltmeter. An ammeter with a large resistance "
                    "would strangle the loop it was meant to measure."},
            {"text": "exactly the same resistance as the component it "
                     "measures", "correct": False,
             "why": "It would then take half the p.d. and halve the current "
                    "— it would change the thing it is reading."},
            {"text": "a resistance that can be adjusted to suit the circuit",
             "correct": False,
             "why": "Nothing about a meter's own resistance is set by the "
                    "user. It is as small as the maker can make it."},
            {"text": "almost no resistance, so it barely changes the current "
                     "it is measuring", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e02",
        "band": "easier",
        "text": "Both meters read zero and the lamp is dark. What is the "
                "first thing to check?",
        "options": [
            {"text": "Whether the ammeter is faulty", "correct": False,
             "why": "It is far more likely that the loop is broken, and "
                    "swapping the meter hides the real fault from the next "
                    "pair."},
            {"text": "Whether the lamp is the right rating", "correct": False,
             "why": "A wrong rating gives a dim or a blown lamp, not zero on "
                    "both meters."},
            {"text": "Every clip and terminal round the loop", "correct": True},
            {"text": "Whether the voltmeter is on the right scale",
             "correct": False,
             "why": "A wrong scale gives a hard-to-read number, not zero on "
                    "both."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e03",
        "band": "easier",
        "text": "Building a circuit is easier if you…",
        "options": [
            {"text": "close the switch first, so you can see what is "
                     "happening as you connect it", "correct": False,
             "why": "That is how a short circuit is discovered the "
                    "expensive way. Build with the switch open."},
            {"text": "put the loop together with the switch open, check "
                     "every connection, then close it", "correct": True},
            {"text": "connect the meters first and add the components round "
                     "them", "correct": False,
             "why": "Order of assembly is not the point. What matters is "
                    "that the switch is open while you work."},
            {"text": "leave one connection loose so you can break the "
                     "circuit quickly", "correct": False,
             "why": "A loose connection is the commonest fault in the whole "
                    "practical. That is what the switch is for."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e04",
        "band": "easier",
        "text": "One reading in a set of six refuses to sit with the rest. "
                "What do you do?",
        "options": [
            {"text": "Take that setting again before writing it down",
             "correct": True},
            {"text": "Cross it out and move the line on the graph to suit "
                     "the others", "correct": False,
             "why": "That is smoothing over a result, which is a fault in "
                    "the method rather than a fix for one."},
            {"text": "Average it with the reading either side of it",
             "correct": False,
             "why": "Averaging hides the disagreement rather than finding "
                    "out where it came from."},
            {"text": "Keep it and note that the circuit was faulty",
             "correct": False,
             "why": "You do not know that yet. Repeating the setting is what "
                    "tells you whether it was the circuit or the reading."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p8-07-s01",
        "band": "standard",
        "text": "Why can a voltmeter hang across a component without "
                "changing what it reads?",
        "options": [
            {"text": "Because its enormous resistance means it draws almost "
                     "no current away", "correct": True},
            {"text": "Because it is connected in parallel, and parallel "
                     "branches never affect each other", "correct": False,
             "why": "A parallel branch does change the total the supply has "
                    "to give. What makes the effect negligible is the "
                    "meter's own resistance."},
            {"text": "Because it measures a difference rather than a flow, "
                     "so nothing has to pass through it", "correct": False,
             "why": "Something does pass through it — a very small current. "
                    "That is why the resistance has to be large."},
            {"text": "Because it has no resistance, so it adds nothing to "
                     "the circuit", "correct": False,
             "why": "That describes an ammeter, and a voltmeter with no "
                    "resistance would short out whatever it was across."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s02",
        "band": "standard",
        "text": "A lamp goes out and the ammeter slams off the scale. What "
                "has most likely been done?",
        "options": [
            {"text": "The switch has been left open", "correct": False,
             "why": "An open switch gives zero on both meters, not an "
                    "off-the-scale ammeter."},
            {"text": "The ammeter has been connected across the lamp",
             "correct": True},
            {"text": "The voltmeter has been connected in the loop",
             "correct": False,
             "why": "That gives the opposite symptom: almost no current and "
                    "a full voltmeter reading."},
            {"text": "The cells have been put in the wrong way round",
             "correct": False,
             "why": "Reversed cells still drive the lamp; on a digital meter "
                    "you would just get a minus sign."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s03",
        "band": "standard",
        "text": "In a single loop, does it matter whether the ammeter goes "
                "before the lamp or after it?",
        "options": [
            {"text": "Yes — before the lamp reads the full current and after "
                     "it reads what is left", "correct": False,
             "why": "Nothing is left behind. One loop carries one current at "
                    "every point."},
            {"text": "Yes — the reading is more accurate nearer the battery",
             "correct": False,
             "why": "Accuracy does not depend on position. The same charge "
                    "passes every point each second."},
            {"text": "No — one loop carries one current, so both positions "
                     "read the same", "correct": True},
            {"text": "No — but only if the lamp is working; a broken "
                     "filament changes it", "correct": False,
             "why": "A broken filament stops the current everywhere, so both "
                    "positions still agree — at zero."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s04",
        "band": "standard",
        "text": "A student plans to investigate how the current through a "
                "lamp depends on the number of cells. What must they keep "
                "the same?",
        "options": [
            {"text": "The number of cells, so that the comparison is fair",
             "correct": False,
             "why": "The number of cells is the thing being CHANGED. That is "
                    "the point of the investigation."},
            {"text": "The reading on the ammeter, so the lamp is not "
                     "damaged", "correct": False,
             "why": "The ammeter reading is what is being MEASURED. Fixing "
                    "it would leave nothing to find out."},
            {"text": "The room temperature only, since nothing else can "
                     "affect an electrical reading", "correct": False,
             "why": "Plenty else can — the lamp, the leads, the tightness of "
                    "the clips. Temperature is not the main one here."},
            {"text": "The same lamp, the same leads and the same "
                     "connections", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p8-07-h01",
        "band": "harder",
        "text": "Why is a meter in the wrong place said to give you a "
                "different CIRCUIT rather than a wrong reading?",
        "options": [
            {"text": "Because the meter's scale is calibrated for one "
                     "position only", "correct": False,
             "why": "A meter reads the same scale wherever it is. What "
                    "changes is the circuit round it."},
            {"text": "Because the meter's own resistance becomes part of the "
                     "loop, and the loop is then a different one",
             "correct": True},
            {"text": "Because the leads are the wrong length for the other "
                     "position", "correct": False,
             "why": "Lead length changes nothing that matters in a school "
                    "circuit."},
            {"text": "Because a meter can only measure the quantity its "
                     "position allows, so the other reading is meaningless",
             "correct": False,
             "why": "The reading is not meaningless — it is a true reading "
                    "of what the circuit has become, which is what makes it "
                    "misleading."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h02",
        "band": "harder",
        "text": "A pair reports 0.00 A on the ammeter and 0.00 V on the "
                "voltmeter, with a dark lamp. Both meters were fine an hour "
                "ago. What does the pair of readings point at?",
        "options": [
            {"text": "A break somewhere in the loop", "correct": True},
            {"text": "The voltmeter wired into the loop", "correct": False,
             "why": "That gives a FULL voltmeter reading, because the "
                    "meter itself is holding the p.d."},
            {"text": "The ammeter wired across the lamp", "correct": False,
             "why": "That gives an off-the-scale ammeter, not zero."},
            {"text": "A flat battery", "correct": False,
             "why": "A flat battery gives small readings rather than zero on "
                    "both, and the voltmeter across a flat battery still "
                    "reads something."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h03",
        "band": "harder",
        "text": "Neither meter is quite innocent. What does that mean for a "
                "careful experimenter?",
        "options": [
            {"text": "That both meters should be removed before the final "
                     "reading is taken", "correct": False,
             "why": "You would then have nothing to read. The point is to "
                    "know the size of the disturbance, not to avoid it."},
            {"text": "That the readings should be corrected by hand "
                     "afterwards", "correct": False,
             "why": "In a school circuit the effect is far too small to be "
                    "worth correcting. Reporting the apparatus is what is "
                    "asked for."},
            {"text": "That a meter's reading is never worth quoting to more "
                     "than one figure, because the meter's own resistance "
                     "makes everything after that a guess", "correct": False,
             "why": "The precision of a reading is a separate question from "
                    "the meter's own resistance."},
            {"text": "That the meters do disturb the circuit slightly, so "
                     "what they were is reported alongside what they read",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h04",
        "band": "harder",
        "text": "A multimeter has an ohms setting that seems to do the "
                "resistance calculation for you. Why does it only work on a "
                "component that has been disconnected?",
        "options": [
            {"text": "Because a connected component is at the battery's p.d. "
                     "and the meter cannot measure above its own range",
             "correct": False,
             "why": "The range is not the problem. The problem is that the "
                    "meter's own current is no longer the only one."},
            {"text": "Because it supplies its own small current and divides "
                     "by it, and any other current in the circuit spoils "
                     "that", "correct": True},
            {"text": "Because the ohms setting has an enormous resistance "
                     "and would strangle the loop", "correct": False,
             "why": "That describes the volts setting. The ohms setting has "
                    "to pass a current of its own."},
            {"text": "Because resistance can only be defined for a component "
                     "that is not carrying a current", "correct": False,
             "why": "Resistance is defined exactly when a current IS "
                    "flowing: it is the p.d. divided by that current."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p8-07-e05",
        "band": "easier",
        "text": "A voltmeter is built to have…",
        "options": [
            {"text": "an enormous resistance, so almost no current passes "
                     "through it",
             "correct": True},
            {"text": "almost no resistance, so it does not slow the current",
             "correct": False,
             "why": "That is an ammeter, which has to sit in the loop without "
                    "changing it."},
            {"text": "exactly the same resistance as the component it "
                     "measures",
             "correct": False,
             "why": "Matching the component would halve the current through "
                    "it and change what it reads."},
            {"text": "no resistance at all, so it reads instantly",
             "correct": False,
             "why": "No resistance across a component would short it out "
                    "completely."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e06",
        "band": "easier",
        "text": "While a circuit is being built, the switch should be…",
        "options": [
            {"text": "closed, so faults show up straight away",
             "correct": False,
             "why": "A fault found by running current through it can damage a "
                    "meter or a cell."},
            {"text": "removed from the circuit until it is finished",
             "correct": False,
             "why": "The switch is part of the loop and should be wired in "
                    "from the start — just left open."},
            {"text": "open, so nothing flows until the loop has been checked",
             "correct": True},
            {"text": "replaced with a plain wire while the meters are fitted",
             "correct": False,
             "why": "That makes it impossible to stop the current while you "
                    "check anything."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e07",
        "band": "easier",
        "text": "An ammeter is connected ACROSS a lamp instead of in the "
                "loop. What happens?",
        "options": [
            {"text": "It reads the lamp's current correctly anyway",
             "correct": False,
             "why": "It is no longer carrying the lamp's current, so what it "
                    "reads is something else entirely."},
            {"text": "It reads zero, because no current reaches it",
             "correct": False,
             "why": "A great deal reaches it — its resistance is almost "
                    "nothing, so it takes the lot."},
            {"text": "It short-circuits the lamp, so the lamp goes dark",
             "correct": True},
            {"text": "Nothing changes, because meters do not affect a "
                     "circuit",
             "correct": False,
             "why": "A meter in the wrong place changes the circuit itself, "
                    "not just the reading."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p8-07-s05",
        "band": "standard",
        "text": "Why does putting a voltmeter IN the loop stop almost all the "
                "current?",
        "options": [
            {"text": "Because its resistance is enormous, so very little gets "
                     "through",
             "correct": True},
            {"text": "Because it only allows current to pass in one "
                     "direction",
             "correct": False,
             "why": "That is a diode. A voltmeter blocks by resistance, not "
                    "by direction."},
            {"text": "Because it measures p.d. and therefore cannot carry "
                     "current",
             "correct": False,
             "why": "It carries a tiny current; being a voltmeter does not "
                    "forbid it, its resistance limits it."},
            {"text": "Because it has no resistance, so it shorts the loop out",
             "correct": False,
             "why": "That is the ammeter's problem when it is misplaced; a "
                    "voltmeter has the opposite fault."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s06",
        "band": "standard",
        "text": "A group takes one reading at each setting and no more. Why "
                "is that not enough?",
        "options": [
            {"text": "Because a single reading is always wrong",
             "correct": False,
             "why": "A single reading is often perfectly good; the problem is "
                    "that you cannot tell which ones are."},
            {"text": "Because a value that does not fit cannot be spotted "
                     "without repeats",
             "correct": True},
            {"text": "Because meters need to warm up before they read "
                     "correctly",
             "correct": False,
             "why": "School meters read immediately; repeating is about "
                    "spotting odd values."},
            {"text": "Because the average of one reading cannot be "
                     "calculated",
             "correct": False,
             "why": "The point is not the arithmetic; it is having something "
                    "to compare each value with."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s07",
        "band": "standard",
        "text": "A set of readings runs 0.20, 0.21, 0.20, 0.35 and 0.21 A. "
                "What should be done about the 0.35 A?",
        "options": [
            {"text": "Cross it out, because it is obviously wrong",
             "correct": False,
             "why": "It may be telling you something. Crossing it out decides "
                    "that before you have checked."},
            {"text": "Include it in the mean, because all readings count",
             "correct": False,
             "why": "Averaging it in hides it, and a value that far out "
                    "usually has a cause worth finding."},
            {"text": "Take that setting again before writing anything down",
             "correct": True},
            {"text": "Move the point onto the line when the graph is drawn",
             "correct": False,
             "why": "Smoothing a point onto a line is changing the data, "
                    "which is never allowed."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p8-07-h05",
        "band": "harder",
        "text": "An ammeter reads a negative value. What has happened, and "
                "does it matter?",
        "options": [
            {"text": "The current is genuinely flowing backwards through the "
                     "battery",
             "correct": False,
             "why": "The battery drives it one way; the meter is simply "
                    "connected against that direction."},
            {"text": "The meter is broken and should be replaced",
             "correct": False,
             "why": "It is working perfectly — a negative sign is exactly how "
                    "it reports reversed leads."},
            {"text": "The leads are the wrong way round; the size is right, "
                     "but reconnect them",
             "correct": True},
            {"text": "Nothing has happened; a negative current is an ordinary "
                     "reading to record",
             "correct": False,
             "why": "The size is usable, but leaving it reversed invites a "
                    "sign error later in the table."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h06",
        "band": "harder",
        "text": "A group swaps the order of the lamp and the buzzer round a "
                "single loop and expects the readings to change. What "
                "actually happens?",
        "options": [
            {"text": "Both readings change, because the first component gets "
                     "the current first",
             "correct": False,
             "why": "There is no first in a loop; the same current passes "
                    "through every part of it."},
            {"text": "The ammeter changes but the voltmeter does not",
             "correct": False,
             "why": "Neither changes: the same current and the same shares of "
                    "p.d. are unaffected by order."},
            {"text": "Nothing changes at all in either reading", "correct": True},
            {"text": "The readings swap over between the two components",
             "correct": False,
             "why": "Each component keeps its own share of the p.d. wherever "
                    "it sits in the loop."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h07",
        "band": "harder",
        "text": "In an investigation of current against the number of cells, "
                "why must the same lamp be used throughout?",
        "options": [
            {"text": "Because a second lamp would not fit the same holder",
             "correct": False,
             "why": "Fitting is a practical detail, not the reason the result "
                    "would be spoilt."},
            {"text": "Because a different lamp would change the current for a "
                     "reason other than the cells",
             "correct": True},
            {"text": "Because lamps wear out and give lower readings each "
                     "time",
             "correct": False,
             "why": "A lamp does not fade measurably over one lesson; the "
                    "issue is comparing like with like."},
            {"text": "Because only one lamp can be connected to a battery at "
                     "a time",
             "correct": False,
             "why": "Several can be, in series or parallel — but then the "
                    "circuit itself has changed."},
        ],
        "figure": None,
    },
]
