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

    # ── MRB-338 night-3 top-up · easier ────────────────────────────────────
    {
        "id": "p8-07-e08",
        "band": "easier",
        "text": "Why does an ammeter need almost no resistance of its own?",
        "options": [
            {"text": "So that putting it in the loop barely changes the "
                     "current it measures.", "correct": True},
            {"text": "So that it can be swapped for a voltmeter without rewiring anything", "correct": False,
             "why": "Swapping components always needs rewiring; an "
                    "ammeter's low resistance is about not disturbing the "
                    "current, not about being interchangeable."},
            {"text": "So that it never gets warm while it is working",
             "correct": False,
             "why": "Every real ammeter warms slightly under load; its "
                    "resistance is about accuracy, not staying cool."},
            {"text": "So that it can be read without a scale marked on it",
             "correct": False,
             "why": "Every ammeter still needs a scale to be read; low "
                    "resistance has nothing to do with the scale."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e09",
        "band": "easier",
        "text": "Why does a voltmeter need an enormous resistance of its "
                "own?",
        "options": [
            {"text": "So that it can measure current as well as voltage",
             "correct": False,
             "why": "A voltmeter measures p.d. only; a large resistance does "
                    "not give it a second job."},
            {"text": "So that connecting it across a component draws almost "
                     "no current away.", "correct": True},
            {"text": "So that it survives being connected the wrong way "
                     "round without any damage", "correct": False,
             "why": "Reversed connection is a separate issue from the "
                    "meter's own resistance."},
            {"text": "So that it can be left connected permanently without a "
                     "battery connected anywhere in the room", "correct": False,
             "why": "A voltmeter needs no battery of its own either way; "
                    "resistance is not about power."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e10",
        "band": "easier",
        "text": "A student says an ammeter and a voltmeter could simply swap "
                "roles if you also swapped where they sit in the circuit. "
                "What is wrong with that idea?",
        "options": [
            {"text": "Nothing is wrong — meters are identical inside and "
                     "can swap jobs on any circuit you can build in the "
                     "lab, provided each one is moved into the other's place "
                     "at the same time", "correct": False,
             "why": "Their internal resistances are built deliberately "
                    "different, for opposite jobs."},
            {"text": "It would work, but only for a lamp, never for a "
                     "resistor", "correct": False,
             "why": "The mismatch in resistance causes a problem whatever "
                    "the component is."},
            {"text": "Each meter's own resistance is built for the job it "
                     "does; the wrong resistance in the wrong place changes "
                     "the circuit itself.", "correct": True},
            {"text": "It would work only if the battery were reversed too",
             "correct": False,
             "why": "Reversing the battery does not fix a meter's own "
                    "resistance being wrong for its new job."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e11",
        "band": "easier",
        "text": "Before closing the switch on a newly built circuit, what "
                "should you do?",
        "options": [
            {"text": "Check that the battery is fully charged only",
             "correct": False,
             "why": "A flat battery is one possible fault among many; "
                    "checking connections catches far more."},
            {"text": "Turn the room lights off so you can see better",
             "correct": False,
             "why": "Lighting has nothing to do with checking a circuit's "
                    "connections."},
            {"text": "Write down the expected reading before building "
                     "anything", "correct": False,
             "why": "A predicted reading is useful later, but it does not "
                    "replace checking the wiring."},
            {"text": "Check every connection by eye and by hand.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e12",
        "band": "easier",
        "text": "A pair builds a circuit, closes the switch, and the lamp is "
                "dark with both meters at zero. What is the most likely "
                "cause?",
        "options": [
            {"text": "A loose connection somewhere in the loop.",
             "correct": True},
            {"text": "The lamp is rated for a higher voltage than the "
                     "battery gives", "correct": False,
             "why": "That gives a dim lamp with real readings on both "
                    "meters, not zero on both."},
            {"text": "The ammeter has been swapped for a second voltmeter by "
                     "mistake", "correct": False,
             "why": "That would give an unusual reading, not zero on both "
                    "meters."},
            {"text": "The switch has been closed twice in a row",
             "correct": False,
             "why": "Closing a switch twice does nothing different from "
                    "closing it once."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e13",
        "band": "easier",
        "text": "Why should a circuit be built with the switch open rather "
                "than closed?",
        "options": [
            {"text": "So that the battery lasts longer overall",
             "correct": False,
             "why": "A switch left open briefly makes almost no difference "
                    "to how long a battery lasts."},
            {"text": "So that no current flows while you are still checking "
                     "the connections.", "correct": True},
            {"text": "So that the meters can be fitted more easily onto "
                     "the bench before any wires reach them",
             "correct": False,
             "why": "Fitting a meter does not depend on whether the switch "
                    "is open or closed."},
            {"text": "So that the wires do not tangle while you work on "
                     "the bench in front of you",
             "correct": False,
             "why": "Tangling is a practical nuisance, not the reason for "
                    "the rule."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e14",
        "band": "easier",
        "text": "A group takes a reading, then repeats the same setting a "
                "second time before moving on. Why?",
        "options": [
            {"text": "Because a single reading is against the rules of any "
                     "school practical", "correct": False,
             "why": "A single reading is not forbidden; repeating is about "
                    "catching a mistake, not following a rule for its own "
                    "sake."},
            {"text": "Because the meters need to warm up on the first "
                     "attempt and read low until they have", "correct": False,
             "why": "School meters read correctly straight away; warming up "
                    "is not the reason."},
            {"text": "To check the two readings agree, before trusting "
                     "either of them.", "correct": True},
            {"text": "Because the first reading is always the least "
                     "accurate one", "correct": False,
             "why": "Neither reading is assumed less accurate; repeating "
                    "checks for agreement, not for a known bias."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e15",
        "band": "easier",
        "text": "One of five readings at the same setting is very different "
                "from the other four. What should be done with it?",
        "options": [
            {"text": "Leave it out of the table completely, without "
                     "comment", "correct": False,
             "why": "Removing a result silently, without checking it, hides "
                    "a possible real fault."},
            {"text": "Change the other four readings to match it",
             "correct": False,
             "why": "Changing agreed results to match one outlier throws "
                    "away good data."},
            {"text": "Report it as the true reading, since it was the "
                     "one measured last", "correct": False,
             "why": "Being measured last does not make a value more "
                    "trustworthy."},
            {"text": "Take that setting again before deciding what to do "
                     "with the odd value.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e16",
        "band": "easier",
        "text": "What is the purpose of the switch in a circuit being "
                "investigated?",
        "options": [
            {"text": "To start and stop the current without disconnecting "
                     "any wires at all.", "correct": True},
            {"text": "To change how bright the lamp glows", "correct": False,
             "why": "Brightness is controlled by the supply or the "
                    "component, not by the switch."},
            {"text": "To measure the current passing through the loop every time",
             "correct": False,
             "why": "Measuring current is the ammeter's job, not the "
                    "switch's."},
            {"text": "To protect the battery from ever going flat",
             "correct": False,
             "why": "A switch does not stop a battery running down while "
                    "current flows."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e17",
        "band": "easier",
        "text": "A circuit diagram shows an ammeter symbol and a voltmeter "
                "symbol. How can you tell them apart before reading any "
                "labels?",
        "options": [
            {"text": "By the colour used to draw the two symbols",
             "correct": False,
             "why": "Circuit symbols are not colour-coded to tell meters "
                    "apart."},
            {"text": "By whether the circle is drawn in the main loop or "
                     "connected across a component.", "correct": True},
            {"text": "By counting how many wires leave the circle",
             "correct": False,
             "why": "Both symbols connect with two wires; the difference is "
                    "where those wires go, not how many there are."},
            {"text": "By the size of the circle drawn for each meter on the printed circuit diagram",
             "correct": False,
             "why": "Symbol size carries no meaning in a circuit diagram."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e18",
        "band": "easier",
        "text": "A group wants to measure the p.d. across a lamp. Where "
                "should the voltmeter go?",
        "options": [
            {"text": "In the loop, immediately before the lamp",
             "correct": False,
             "why": "That places it in series, which is where an ammeter "
                    "belongs, not a voltmeter."},
            {"text": "Anywhere in the circuit, since a voltmeter reads the "
                     "same value everywhere", "correct": False,
             "why": "A voltmeter reads different values depending on what "
                    "it is connected across."},
            {"text": "Across the lamp, with one lead on each side of it.",
             "correct": True},
            {"text": "Directly across the battery only, never across a "
                     "component", "correct": False,
             "why": "A voltmeter can be placed across any component, "
                    "including the lamp itself."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e19",
        "band": "easier",
        "text": "A group wants to measure the current through a lamp. Where "
                "should the ammeter go?",
        "options": [
            {"text": "Across the lamp, with one lead on each side of it",
             "correct": False,
             "why": "That places it in parallel, which shorts the lamp out "
                    "instead of measuring its current."},
            {"text": "Connected only to the positive terminal of the "
                     "battery", "correct": False,
             "why": "An ammeter needs to be part of the complete loop, not "
                    "attached to one terminal alone."},
            {"text": "Wherever there is space on the board for it",
             "correct": False,
             "why": "Its position in the LOOP matters; convenience of space "
                    "is not the deciding factor."},
            {"text": "In the loop, in series with the lamp.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e20",
        "band": "easier",
        "text": "What happens to a lamp if the ammeter meant to be in series "
                "with it is instead connected across it?",
        "options": [
            {"text": "The lamp goes dark, because the ammeter offers a "
                     "route with almost no resistance.", "correct": True},
            {"text": "The lamp gets brighter, because the ammeter adds "
                     "extra push", "correct": False,
             "why": "A meter adds no extra push of its own; it simply gives "
                    "the current an easier route past the lamp."},
            {"text": "Nothing changes, because meters do not affect a "
                     "circuit", "correct": False,
             "why": "A meter in the wrong place changes the circuit itself, "
                    "not just the reading."},
            {"text": "The lamp flickers, because the current now "
                     "arrives in pulses set by the meter", "correct": False,
             "why": "Nothing about this fault makes the current pulse; it "
                    "is steady, just diverted."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e21",
        "band": "easier",
        "text": "A voltmeter is supposed to sit across the lamp but is "
                "wired into the main loop by mistake instead. What is the "
                "result?",
        "options": [
            {"text": "The lamp gets brighter, because the voltmeter "
                     "adds extra push on top of the battery's", "correct": False,
             "why": "A meter adds no push of its own; here it blocks the "
                    "current rather than boosting it."},
            {"text": "The lamp goes dark, because the voltmeter's huge "
                     "resistance blocks almost all the current.",
             "correct": True},
            {"text": "Nothing changes, because a voltmeter never affects a "
                     "circuit", "correct": False,
             "why": "A voltmeter in the wrong place changes the circuit "
                    "dramatically, by blocking almost all the current."},
            {"text": "The lamp glows dimly but steadily at half power",
             "correct": False,
             "why": "So little current gets through that the lamp stays "
                    "dark, not dimly lit."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e22",
        "band": "easier",
        "text": "Both meters have been checked and are in their correct "
                "places — ammeter in the loop, voltmeter across the lamp. "
                "Which reading would then make you suspect a broken "
                "filament inside the lamp?",
        "options": [
            {"text": "Zero on both meters, with the switch closed",
             "correct": False,
             "why": "That points at a broken loop somewhere, not "
                    "specifically at the lamp's own filament."},
            {"text": "A steady reading on both meters, exactly as expected for a circuit built exactly to the diagram",
             "correct": False,
             "why": "A steady, expected reading is a sign nothing is wrong "
                    "at all."},
            {"text": "A reading that slowly falls over several minutes of testing every time it is tried",
             "correct": False,
             "why": "A slowly falling reading points at the cells running "
                    "down, not at a broken filament."},
            {"text": "Zero on the ammeter and the full battery p.d. on the "
                     "voltmeter across the lamp.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e23",
        "band": "easier",
        "text": "Why is it good practice to draw the circuit diagram before "
                "building the circuit?",
        "options": [
            {"text": "So the meters read more accurately once built",
             "correct": False,
             "why": "A diagram does not change how accurately a meter "
                    "reads; it guides where things are connected."},
            {"text": "So the battery lasts longer during the practical "
                     "than it otherwise would, because a drawn circuit is "
                     "connected up in fewer separate attempts",
             "correct": False,
             "why": "Drawing a diagram first has no effect on how long a "
                    "battery lasts."},
            {"text": "So the circuit uses fewer wires overall",
             "correct": False,
             "why": "The number of wires needed depends on the circuit "
                    "itself, not on whether a diagram was drawn first."},
            {"text": "So you know where every component and meter should go "
                     "before you start connecting wires.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e24",
        "band": "easier",
        "text": "A pair swaps the lamp for a buzzer partway through an "
                "investigation, without changing anything else. What has "
                "gone wrong with their method?",
        "options": [
            {"text": "They have changed a variable they were supposed to "
                     "keep the same.", "correct": True},
            {"text": "Nothing — a buzzer and a lamp behave identically in a circuit", "correct": False,
             "why": "A buzzer and a lamp are different components; swapping "
                    "one for the other changes the very thing being "
                    "investigated."},
            {"text": "The switch must now be replaced as well",
             "correct": False,
             "why": "The switch is unaffected by which component sits "
                    "elsewhere in the loop."},
            {"text": "The meters must now be recalibrated from scratch",
             "correct": False,
             "why": "The meters do not need recalibrating just because a "
                    "different component is in the circuit."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e25",
        "band": "easier",
        "text": "What should stay fixed while an investigation changes the "
                "number of cells in a circuit?",
        "options": [
            {"text": "The reading on the ammeter, from start to finish "
                     "of the investigation",
             "correct": False,
             "why": "The ammeter reading is exactly what is being measured; "
                    "it is not something to fix in advance."},
            {"text": "The lamp, the leads and the connections used "
                     "throughout.", "correct": True},
            {"text": "The position of the switch on the bench",
             "correct": False,
             "why": "Where the switch physically sits on the bench makes no "
                    "difference to the results."},
            {"text": "The colour of the wires chosen for each separate "
                     "connection round the loop",
             "correct": False,
             "why": "Wire colour has no effect on a circuit's electrical "
                    "behaviour."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e26",
        "band": "easier",
        "text": "Two ammeters are placed at different points in the SAME "
                "single loop. What should you expect?",
        "options": [
            {"text": "The one nearer the battery reads higher",
             "correct": False,
             "why": "One loop carries one current at every point; nearness "
                    "to the battery makes no difference."},
            {"text": "The one nearer the lamp reads lower, since the lamp "
                     "uses some of it up", "correct": False,
             "why": "Current is not used up passing through a component; "
                    "the same current leaves as entered."},
            {"text": "Both give the same reading, since one loop always "
                     "carries one current everywhere.", "correct": True},
            {"text": "They cannot both be trusted, since two ammeters in "
                     "one loop is not allowed, and each would only show "
                     "its own share of the current", "correct": False,
             "why": "Two ammeters in one loop is a perfectly normal way to "
                    "double-check a reading."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e27",
        "band": "easier",
        "text": "An analogue meter's needle swings hard BACKWARDS, below "
                "zero and against the stop, the moment the circuit is "
                "switched on. What is the likely cause?",
        "options": [
            {"text": "The battery is far too weak to drive the circuit",
             "correct": False,
             "why": "A weak battery gives a small or zero reading, not a "
                    "needle slammed against the stop."},
            {"text": "The lamp has blown inside its glass", "correct": False,
             "why": "A blown lamp gives zero current, not a needle driven "
                    "hard against the stop."},
            {"text": "The meter has been left on the wrong scale",
             "correct": False,
             "why": "A wrong scale usually gives an off-scale HIGH reading "
                    "in the correct direction, not the needle driven "
                    "backwards."},
            {"text": "The meter's leads are connected the wrong way round.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e28",
        "band": "easier",
        "text": "Why is it worth recording which piece of apparatus was "
                "used, not just the readings it gave?",
        "options": [
            {"text": "Because a piece of apparatus can disturb a circuit "
                     "slightly, and that is worth knowing alongside the "
                     "reading.", "correct": True},
            {"text": "Because apparatus is graded and only the best equipment counts towards a group's final mark for the practical", "correct": False,
             "why": "There is no grading of apparatus; the point is "
                    "recording what might have disturbed the reading."},
            {"text": "Because it tells you which student did the measuring",
             "correct": False,
             "why": "Recording apparatus is about the equipment's effect on "
                    "the circuit, not about who used it."},
            {"text": "Because it lets you skip repeating the reading later",
             "correct": False,
             "why": "Recording the apparatus used does not replace "
                    "repeating a doubtful reading."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e29",
        "band": "easier",
        "text": "A group builds a circuit exactly to the diagram, but "
                "forgets to close the switch before reading the meters. "
                "What will they see?",
        "options": [
            {"text": "A normal reading on both meters, as if the switch "
                     "made no difference", "correct": False,
             "why": "An open switch stops the current everywhere in the "
                    "loop; the readings will not be normal."},
            {"text": "Zero on both meters and a dark lamp.", "correct": True},
            {"text": "A full reading on the ammeter but nothing on the "
                     "voltmeter", "correct": False,
             "why": "With the loop broken by the open switch, no current "
                    "reaches the ammeter at all."},
            {"text": "A half reading on both meters", "correct": False,
             "why": "An open switch stops the current completely "
                    "everywhere in the loop; there is no half-way reading."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-e30",
        "band": "easier",
        "text": "What is the very first thing to check if a circuit that "
                "worked yesterday gives no reading today?",
        "options": [
            {"text": "Whether the diagram has changed overnight",
             "correct": False,
             "why": "A diagram does not change on its own; checking the "
                    "physical connections finds far more faults."},
            {"text": "Every connection and terminal round the loop.",
             "correct": True},
            {"text": "Whether a different model of battery is now "
                     "required",
             "correct": False,
             "why": "A working circuit does not suddenly need a different "
                    "kind of battery."},
            {"text": "Whether the meters have been replaced with different "
                     "brands", "correct": False,
             "why": "Different meter brands would not stop a previously "
                    "working circuit reading at all."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · standard ───────────────────────────────────
    {
        "id": "p8-07-s08",
        "band": "standard",
        "text": "A voltmeter is connected across a lamp and reads 3.0 V. "
                "The same lamp is then also given an ammeter in series, "
                "reading 0.20 A. Does adding the ammeter change the "
                "voltmeter's reading noticeably?",
        "options": [
            {"text": "No — the ammeter's resistance is so low that it "
                     "barely changes the current, so the p.d. across the "
                     "lamp barely changes either.", "correct": True},
            {"text": "Yes — adding any meter changes every other "
                     "reading in the circuit substantially, however small "
                     "that meter's own resistance is", "correct": False,
             "why": "An ammeter's very low resistance is chosen "
                    "specifically so its effect on the rest of the circuit "
                    "is negligible."},
            {"text": "No — because meters never draw any current or affect "
                     "a circuit at all", "correct": False,
             "why": "Every real meter disturbs a circuit slightly; the "
                    "ammeter's effect here is small, not zero."},
            {"text": "Yes — the ammeter reading always changes to match the "
                     "voltmeter's", "correct": False,
             "why": "The two meters measure different quantities; neither "
                    "reading is adjusted to match the other."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s09",
        "band": "standard",
        "text": "A group wires the ammeter in series correctly, but on the "
                "wrong side of the switch, between the switch and the "
                "negative terminal instead of between the switch and the "
                "lamp. Does this change the ammeter's reading?",
        "options": [
            {"text": "Yes — a reading taken nearer the negative terminal is "
                     "always smaller than one taken nearer the positive "
                     "terminal", "correct": False,
             "why": "One loop carries one current at every point in it; "
                    "nearness to a terminal makes no difference."},
            {"text": "No — the ammeter is still in the one loop, so it "
                     "always reads the same current wherever in that loop "
                     "it sits.", "correct": True},
            {"text": "Yes — the reading now includes the switch's own "
                     "current as well", "correct": False,
             "why": "A switch does not add or carry a separate current of "
                    "its own; it simply opens or closes the one loop."},
            {"text": "No — but only because the switch happens to be "
                     "closed at the time; with it open the two positions "
                     "would read differently", "correct": False,
             "why": "Whether the switch is open or closed decides whether "
                    "current flows AT ALL; position within the loop is the "
                    "separate point being tested here."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s10",
        "band": "standard",
        "text": "A lamp is dark, the ammeter reads 0.00 A, and the "
                "voltmeter across the lamp also reads 0.00 V. What does "
                "this pair of readings suggest?",
        "options": [
            {"text": "The voltmeter has been wired into the loop by mistake instead of across properly", "correct": False,
             "why": "That fault gives a FULL voltmeter reading, not zero, "
                    "because the meter itself would be holding the p.d."},
            {"text": "The ammeter has been wired across the lamp by "
                     "mistake", "correct": False,
             "why": "That fault sends the ammeter off the scale with a "
                    "large reading, not zero."},
            {"text": "A break somewhere in the loop, since nothing is "
                     "reaching the lamp at all.", "correct": True},
            {"text": "The lamp is working normally at a brightness too low "
                     "for either meter to register", "correct": False,
             "why": "Zero on both meters means no current at all is "
                    "reaching the lamp, not a dim but working one."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s11",
        "band": "standard",
        "text": "A pair wires a circuit and get a dim, working lamp with "
                "sensible readings on both meters. A second, identical pair "
                "builds from the same diagram and gets a bright lamp with "
                "noticeably higher readings on both meters. What is the "
                "most likely explanation?",
        "options": [
            {"text": "The two lamps must be rated for different voltages",
             "correct": False,
             "why": "A rating difference would be an odd coincidence for "
                    "two lamps from the same box; a connection fault is far "
                    "more likely and testable."},
            {"text": "One group's meters must be reading in different "
                     "units, even though both sets came from the same "
                     "cupboard, since two meters only agree once someone "
                     "has matched their ranges by hand", "correct": False,
             "why": "School meters read in the same units regardless of "
                    "which set is used; a units mismatch is not a real "
                    "possibility here."},
            {"text": "The two circuits cannot really be compared at all",
             "correct": False,
             "why": "Identical diagrams and apparatus CAN be compared "
                    "directly; a difference like this is exactly the kind a "
                    "fault-check should explain."},
            {"text": "One of the two circuits has an extra connection "
                     "resistance, such as a loose or dirty clip, lowering "
                     "its readings.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s12",
        "band": "standard",
        "text": "An investigation into current against the number of cells "
                "gets a table of results that rises smoothly, then "
                "suddenly drops on the last-but-one row before rising "
                "again on the last. What is the sensible next step?",
        "options": [
            {"text": "Repeat the last-but-one setting to see whether the "
                     "drop happens again.", "correct": True},
            {"text": "Delete the whole table and start again from scratch",
             "correct": False,
             "why": "One odd row does not make the rest of the table "
                    "untrustworthy; only the doubtful setting needs "
                    "repeating."},
            {"text": "Draw the graph as a smooth curve straight through "
                     "all the points anyway", "correct": False,
             "why": "Smoothing over an unexplained drop hides it rather "
                    "than checking whether it is real."},
            {"text": "Report the drop as a genuine effect of adding more "
                     "cells, which begin to work against each other", "correct": False,
             "why": "A single unexplained drop should be checked by "
                    "repeating it, not reported as a real trend straight "
                    "away."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s13",
        "band": "standard",
        "text": "Why is it better to build a circuit by following a "
                "diagram exactly, rather than by memory or by guessing "
                "where things go?",
        "options": [
            {"text": "Because a diagram is required paperwork for every practical that a teacher has to sign off", "correct": False,
             "why": "The reason given here is about avoiding a wiring "
                    "fault, not about paperwork."},
            {"text": "Because a small mistake in a meter's position changes "
                     "the whole circuit, not just the reading.",
             "correct": True},
            {"text": "Because guessing takes longer than following a "
                     "diagram", "correct": False,
             "why": "Speed is not the reason; getting the wiring right the "
                    "first time is."},
            {"text": "Because a diagram tells you which battery brand to "
                     "use", "correct": False,
             "why": "A circuit diagram shows connections, not brand of "
                    "equipment."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s14",
        "band": "standard",
        "text": "A voltmeter is connected across the WHOLE circuit (across "
                "the battery terminals) rather than across one component. "
                "What does it then read?",
        "options": [
            {"text": "Zero, since a voltmeter must be across a single "
                     "component to read anything", "correct": False,
             "why": "A voltmeter can be placed across any two points, "
                    "including the battery itself, and will read the p.d. "
                    "between them."},
            {"text": "The current flowing round the loop", "correct": False,
             "why": "A voltmeter always reads a potential difference, "
                    "never a current."},
            {"text": "The resistance of the whole circuit directly every time it is read",
             "correct": False,
             "why": "A voltmeter reads a p.d., not a resistance; resistance "
                    "has to be calculated from a p.d. and a current "
                    "together."},
            {"text": "The battery's own p.d., shared out among whatever is "
                     "in the loop.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s15",
        "band": "standard",
        "text": "A multimeter is switched to its ohms setting and connected "
                "across a lamp that is still wired into a working, "
                "switched-on circuit. Why is the reading meaningless?",
        "options": [
            {"text": "Because a multimeter cannot measure a lamp's "
                     "resistance under any circumstances, however it is "
                     "connected, because a filament only has a resistance "
                     "while a current is running through it", "correct": False,
             "why": "It can measure a lamp's resistance perfectly well once "
                    "the lamp is disconnected from everything else."},
            {"text": "Because the ohms setting supplies its own small "
                     "current, and the circuit's own current interferes "
                     "with that measurement.", "correct": True},
            {"text": "Because the lamp's filament is too hot for the meter "
                     "to read safely", "correct": False,
             "why": "Heat is not the reason the ohms setting fails here; "
                    "the circuit's own live current is."},
            {"text": "Because the ohms setting only works on resistors, "
                     "never on lamps", "correct": False,
             "why": "The ohms setting works on any component; the problem "
                    "here is testing it while still connected to a live "
                    "circuit."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s16",
        "band": "standard",
        "text": "A group reads the ammeter and voltmeter one after the "
                "other rather than at the same moment, for a lamp that is "
                "still warming up. Why might this be a problem?",
        "options": [
            {"text": "Because reading two meters in sequence is against "
                     "the rules of any practical, however carefully it is "
                     "done, since every reading in a table has to be taken "
                     "by the same person to count", "correct": False,
             "why": "There is no such rule; the concern here is "
                    "specifically the lamp's resistance changing while it "
                    "warms."},
            {"text": "Because a meter's battery runs down faster if read "
                     "second", "correct": False,
             "why": "School meters read directly from the circuit; reading "
                    "order does not run down anything."},
            {"text": "Because the lamp's resistance is changing as it "
                     "heats, so the two readings may no longer belong to "
                     "the same instant.", "correct": True},
            {"text": "Because only the ammeter's reading is ever needed "
                     "anyway", "correct": False,
             "why": "Both readings are needed together to find a "
                    "resistance; the voltmeter's reading matters just as "
                    "much."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s17",
        "band": "standard",
        "text": "Explain why building a circuit with the switch closed the "
                "whole time makes faults harder to find, not easier.",
        "options": [
            {"text": "Because a closed switch makes every meter read zero "
                     "automatically", "correct": False,
             "why": "A closed switch is what LETS current flow; it does "
                    "not force every reading to zero."},
            {"text": "Because a closed switch uses more current than an "
                     "open one, whatever else is wired into the loop, so "
                     "the cells go flat before the fault can be found", "correct": False,
             "why": "How much current flows depends on the whole circuit, "
                    "not simply on the switch being closed."},
            {"text": "Because faults can only be seen while the switch is "
                     "open", "correct": False,
             "why": "Many faults are only revealed once the switch IS "
                    "closed and current flows; the danger is not checking "
                    "connections first."},
            {"text": "Because a bad connection may spark or a component may "
                     "be damaged before you have finished checking "
                     "anything.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s18",
        "band": "standard",
        "text": "A student claims that adding a second, identical ammeter "
                "in series with the first will make the reading more "
                "accurate. Are they right?",
        "options": [
            {"text": "No — both ammeters read the true current just as "
                     "accurately as one alone did; a second one adds "
                     "nothing useful.", "correct": True},
            {"text": "Yes — two ammeters together always give a more "
                     "precise combined value", "correct": False,
             "why": "Both ammeters are simply reading the same one current "
                    "in the same loop; there is no combining to be done."},
            {"text": "Yes — the second ammeter corrects for any error the "
                     "first one makes", "correct": False,
             "why": "One ammeter does not correct another; if anything, "
                    "two low-resistance meters in series disturb the "
                    "current very slightly more than one."},
            {"text": "No — in fact a second ammeter cancels out the first one's reading entirely leaving nothing at all for either", "correct": False,
             "why": "Two ammeters in the same loop read the same current "
                    "together; neither cancels the other."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s19",
        "band": "standard",
        "text": "A circuit's ammeter reads exactly 0.00 A while the "
                "voltmeter across the whole battery reads the battery's "
                "full rated p.d. What does this combination suggest?",
        "options": [
            {"text": "A dead battery that needs replacing", "correct": False,
             "why": "A dead battery would give a LOW voltmeter reading "
                    "across it, not its full rated value."},
            {"text": "A lamp that is far too bright for the supply it "
                     "has been connected to",
             "correct": False,
             "why": "An over-bright lamp would still draw some current, "
                    "giving a reading above zero, not exactly zero."},
            {"text": "A break somewhere in the loop other than right at the "
                     "battery terminals.", "correct": True},
            {"text": "Nothing unusual — this is exactly what a working "
                     "circuit looks like", "correct": False,
             "why": "A working circuit drives a real current, which the "
                    "ammeter would show as more than zero."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s20",
        "band": "standard",
        "text": "Why does a school circuits practical usually ask you to "
                "record BOTH the ammeter and the voltmeter reading, rather "
                "than just one?",
        "options": [
            {"text": "Because one of the two meters is often unreliable on "
                     "its own", "correct": False,
             "why": "Both meters are equally reliable individually; the "
                    "reason for taking both is the calculation, not "
                    "distrust of either."},
            {"text": "Because together they let you calculate the "
                     "resistance, which neither reading alone can give "
                     "you.", "correct": True},
            {"text": "Because the teacher needs both numbers to mark the "
                     "practical", "correct": False,
             "why": "Marking is not the scientific reason for taking both "
                    "readings."},
            {"text": "Because a single meter cannot be used on its own "
                     "in a school lab under any circumstances", "correct": False,
             "why": "There is no such rule; either meter can be used alone "
                    "if only that one quantity is wanted."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s21",
        "band": "standard",
        "text": "A group's results table has a column for 'apparatus used' "
                "alongside their readings, even though every group used "
                "identical kit from the same cupboard. Why bother?",
        "options": [
            {"text": "Because different kit is always the reason two "
                     "groups disagree about any reading taken anywhere in "
                     "the practical, so once it is written down nothing "
                     "else needs checking", "correct": False,
             "why": "It is only ONE possible reason among several, not "
                    "always the cause of a difference."},
            {"text": "Because the school needs to track which kit is used "
                     "the most", "correct": False,
             "why": "That is an equipment-management reason, not a "
                    "scientific one for the practical."},
            {"text": "Because even identical-looking kit can differ "
                     "slightly, and noting it helps explain any small "
                     "differences between groups later.", "correct": True},
            {"text": "Because it replaces the need to repeat any readings",
             "correct": False,
             "why": "Recording the apparatus used does not replace "
                    "repeating a doubtful reading."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s22",
        "band": "standard",
        "text": "An ammeter reading suddenly jumps to a much higher value "
                "the instant a second lamp is added in parallel with the "
                "first, on the same battery. Is this expected?",
        "options": [
            {"text": "No — adding a component should never change any "
                     "other reading in the circuit, wherever that new "
                     "component goes", "correct": False,
             "why": "Adding a parallel branch genuinely changes the total "
                    "current the battery supplies; that is expected here, "
                    "not a fault."},
            {"text": "Yes — a parallel branch gives the current a second "
                     "path, so the battery now drives more current "
                     "overall.", "correct": True},
            {"text": "No — the reading must have jumped because the first "
                     "ammeter has failed for good, since one loop can only "
                     "ever carry one current", "correct": False,
             "why": "A sudden rise exactly when a parallel branch is added "
                    "has a straightforward explanation without assuming a "
                    "fault."},
            {"text": "Yes — but only because the second lamp is a "
                     "different colour", "correct": False,
             "why": "A lamp's colour has no bearing on the current it "
                    "draws."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s23",
        "band": "standard",
        "text": "A group wants to know whether swapping the type of "
                "connecting wire (banana leads vs crocodile clips) changes "
                "their readings. What should they do to test this fairly?",
        "options": [
            {"text": "Change the wire type and the battery together, to "
                     "see the biggest possible effect on the ammeter and voltmeter readings at once", "correct": False,
             "why": "Changing two things at once means you cannot tell "
                    "which one caused any difference seen."},
            {"text": "Ask a different group to test it instead, using their "
                     "own circuit", "correct": False,
             "why": "A different circuit built by a different group is not "
                    "a fair, controlled comparison."},
            {"text": "Keep everything else in the circuit the same, and "
                     "change only the type of connecting wire between "
                     "repeats.", "correct": True},
            {"text": "Assume the wire type never matters and skip the test",
             "correct": False,
             "why": "Assuming the answer defeats the purpose of testing it "
                    "fairly in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s24",
        "band": "standard",
        "text": "A pair records their ammeter reading in amps and their "
                "voltmeter reading in millivolts by mistake. What is wrong "
                "with dividing one by the other straight away?",
        "options": [
            {"text": "Nothing is wrong — resistance can be found from any "
                     "pair of units, without converting either of them "
                     "first", "correct": False,
             "why": "Mismatched unit prefixes throw the answer out by "
                    "whatever factor separates them; converting first is "
                    "essential."},
            {"text": "The units do not match, so the division gives a "
                     "resistance a thousand times too big until they are "
                     "converted.", "correct": True},
            {"text": "The division is impossible until both readings "
                     "are given to exactly the same number of decimal "
                     "places",
             "correct": False,
             "why": "Decimal places do not need to match; the UNITS do."},
            {"text": "The reading is fine, but the answer must be reported "
                     "in millivolts too", "correct": False,
             "why": "Reporting the WRONG unit does not fix a calculation "
                    "that used mismatched units in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s25",
        "band": "standard",
        "text": "Explain why a circuit that worked perfectly on the bench "
                "yesterday might give no reading today, even though "
                "nothing was changed on purpose.",
        "options": [
            {"text": "Circuits are not expected to keep working from one "
                     "day to the next once they have been switched off "
                     "and packed away", "correct": False,
             "why": "A properly built circuit is expected to keep working; "
                    "something specific has usually gone wrong, worth "
                    "finding."},
            {"text": "The wires must have swapped their own polarity "
                     "overnight", "correct": False,
             "why": "Wires do not spontaneously reverse polarity; a loose "
                    "connection or a flat cell is a far more likely cause."},
            {"text": "A connection may have loosened slightly overnight, or "
                     "a cell may have run down; both are common, ordinary "
                     "causes.", "correct": True},
            {"text": "The meters must be recalibrated every single day "
                     "before use", "correct": False,
             "why": "School meters do not need daily recalibration; a "
                    "wiring or battery fault is the more likely "
                    "explanation."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s26",
        "band": "standard",
        "text": "A group's voltmeter reads a steady 6.0 V across a lamp no "
                "matter which of several different lamps they clip in. "
                "What does this suggest about their circuit?",
        "options": [
            {"text": "Every lamp they own happens to need exactly 6.0 V",
             "correct": False,
             "why": "Different lamps needing exactly the same p.d. by "
                    "coincidence, every time, is far less likely than a "
                    "wiring fault."},
            {"text": "The battery is unusually good at keeping a constant "
                     "voltage, whichever component happens to be drawing "
                     "current from it", "correct": False,
             "why": "A steady 6.0 V regardless of the LAMP points at where "
                    "the voltmeter sits, not at the battery's quality."},
            {"text": "The ammeter must be broken, since it is not "
                     "mentioned", "correct": False,
             "why": "Nothing about the ammeter is implied by this "
                    "voltmeter behaviour alone."},
            {"text": "The voltmeter is very likely wired into the loop, "
                     "holding almost the whole battery p.d. regardless of "
                     "the lamp.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s27",
        "band": "standard",
        "text": "Why does swapping the order of two resistors in a single "
                "series loop leave both meters' readings unchanged?",
        "options": [
            {"text": "Because resistors do not actually affect a circuit's "
                     "readings at all", "correct": False,
             "why": "Resistors genuinely limit the current; the point here "
                    "is that ORDER does not matter, not that resistors have "
                    "no effect."},
            {"text": "Because one loop always carries one current "
                     "everywhere, and each resistor keeps its own share of "
                     "the p.d. wherever it sits.", "correct": True},
            {"text": "Because the ammeter only reads the current near the "
                     "battery, not near the resistors further round the "
                     "same loop, so moving them changes nothing it is able "
                     "to see", "correct": False,
             "why": "An ammeter anywhere in the loop reads the one shared "
                    "current, not just a value 'near the battery'."},
            {"text": "Because swapping order also swaps which terminal the "
                     "battery uses", "correct": False,
             "why": "The battery's own terminals are unaffected by how "
                    "components are ordered elsewhere in the loop."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s28",
        "band": "standard",
        "text": "A group's circuit gives a reading, but they realise "
                "afterwards that one crocodile clip was biting the plastic "
                "insulation rather than the bare wire underneath. What "
                "does this explain?",
        "options": [
            {"text": "Why the current was slightly larger than expected "
                     "once the fault had been found and fixed at the clip",
             "correct": False,
             "why": "A clip biting insulation instead of metal gives LESS "
                    "current, not more — often none at all."},
            {"text": "Why the voltmeter read a negative value",
             "correct": False,
             "why": "A negative reading points at reversed leads, not at a "
                    "clip biting insulation."},
            {"text": "Why the circuit may have behaved as if it were "
                     "broken, even though every wire was technically "
                     "present.", "correct": True},
            {"text": "Why the lamp glowed brighter than usual",
             "correct": False,
             "why": "A poor connection like this dims or kills a reading; "
                    "it does not brighten anything."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s29",
        "band": "standard",
        "text": "A teacher asks a group to identify the independent, "
                "dependent and control variables in their investigation of "
                "current against number of cells. Match them correctly.",
        "options": [
            {"text": "Independent: the current. Dependent: number of "
                     "cells. Control: the switch position and the room's "
                     "temperature throughout", "correct": False,
             "why": "The number of cells is what the group deliberately "
                    "CHANGES, which makes it the independent variable, not "
                    "the dependent one."},
            {"text": "Independent: the lamp. Dependent: the leads. "
                     "Control: the current", "correct": False,
             "why": "The current is what is MEASURED here, which makes it "
                    "the dependent variable, not something kept constant."},
            {"text": "Independent: the connections. Dependent: the switch. "
                     "Control: the number of cells throughout", "correct": False,
             "why": "The number of cells is the thing being deliberately "
                    "changed, so it cannot also be the control."},
            {"text": "Independent: number of cells. Dependent: the "
                     "current. Control: the same lamp, leads and "
                     "connections.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-s30",
        "band": "standard",
        "text": "Why is 'the lamp got brighter' not, on its own, good "
                "enough data to report from this investigation?",
        "options": [
            {"text": "Because it gives no number, so nobody can check it, "
                     "compare it, or plot it against anything.",
             "correct": True},
            {"text": "Because brightness can never be linked to current in "
                     "any circuit however carefully an observer looks at it", "correct": False,
             "why": "Brightness and current are closely linked; the "
                    "objection here is that 'brighter' alone gives no "
                    "measurable number."},
            {"text": "Because only a voltmeter reading counts as real "
                     "data", "correct": False,
             "why": "An ammeter reading is equally real data; the issue is "
                    "the lack of any NUMBER at all, not which meter it came "
                    "from."},
            {"text": "Because brightness always depends on the room's own "
                     "lighting on any given day of the school week",
             "correct": False,
             "why": "Room lighting might affect how brightness LOOKS to an "
                    "observer, but that is not the reason a numberless "
                    "description is poor data here."},
        ],
        "figure": None,
    },

    # ── MRB-338 night-3 top-up · harder ─────────────────────────────────────
    {
        "id": "p8-07-h08",
        "band": "harder",
        "text": "A circuit is built correctly, but the leads used are old "
                "and slightly corroded at their tips, adding a small extra "
                "resistance at each connection. What effect would this "
                "have on the ammeter and voltmeter readings, compared with "
                "fresh leads?",
        "options": [
            {"text": "Both readings would be slightly lower than with "
                     "fresh leads, since the extra resistance reduces the "
                     "current a little.", "correct": True},
            {"text": "The ammeter reading would rise, since corrosion "
                     "increases the current flowing through every part of "
                     "the loop, while the voltmeter would fall by the same "
                     "amount to match it", "correct": False,
             "why": "Corrosion adds resistance, which REDUCES the current "
                    "in the loop, not increases it."},
            {"text": "Only the voltmeter reading would change, never the "
                     "ammeter's", "correct": False,
             "why": "Extra resistance anywhere in the loop changes the ONE "
                    "shared current, so both readings are affected "
                    "together."},
            {"text": "Neither reading would change, since corrosion only "
                     "affects appearance", "correct": False,
             "why": "Corroded contacts genuinely add resistance to the "
                    "path the current takes, not just to how the leads "
                    "look."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h09",
        "band": "harder",
        "text": "Two identical circuits are built side by side. One uses "
                "thick leads, the other uses very thin leads of the same "
                "length. Both give slightly different ammeter readings. "
                "Explain why, referring to resistance.",
        "options": [
            {"text": "The thin leads add a little more resistance to their "
                     "loop than the thick leads do, lowering that circuit's "
                     "current slightly.", "correct": True},
            {"text": "Lead thickness has no effect on current at all, so "
                     "the readings must have some cause unconnected to "
                     "either set of leads",
             "correct": False,
             "why": "Thinner wire genuinely resists more than thicker wire "
                    "of the same length and metal, which is exactly the "
                    "cause here."},
            {"text": "The thick leads must be carrying a completely "
                     "different current from the thin ones", "correct": False,
             "why": "Both circuits carry one current each, decided by "
                    "their own total resistance; the difference is small, "
                    "from the leads themselves, not two unrelated "
                    "currents."},
            {"text": "Only the voltmeter reading could possibly be "
                     "affected by the leads", "correct": False,
             "why": "The leads' resistance is part of the loop, so it "
                    "affects the shared current the ammeter reads too."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h10",
        "band": "harder",
        "text": "A student argues that since a voltmeter's resistance is "
                "'almost infinite', connecting one across a lamp should "
                "stop the lamp working, the same way a break in the loop "
                "would. What is wrong with this argument?",
        "options": [
            {"text": "Nothing is wrong — a voltmeter across a lamp really "
                     "does behave exactly like a break anywhere else in that same single loop every time", "correct": False,
             "why": "A parallel branch, however high its resistance, "
                    "leaves the original loop through the lamp completely "
                    "intact."},
            {"text": "A voltmeter connected ACROSS a component adds a "
                     "parallel path, not a break in the main loop, so the "
                     "lamp's own path is untouched.", "correct": True},
            {"text": "The argument is right for a lamp, but wrong for a "
                     "resistor", "correct": False,
             "why": "The reasoning fails for the same reason whatever the "
                    "component is: a parallel branch is not a break in the "
                    "original loop."},
            {"text": "The argument is only wrong if the voltmeter's "
                     "resistance is below a certain value, above which a "
                     "parallel branch does behave like a break", "correct": False,
             "why": "It is wrong regardless of how high the voltmeter's "
                    "resistance is, because of WHERE it is connected, not "
                    "how big its resistance is."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h11",
        "band": "harder",
        "text": "A group wires the voltmeter in series by mistake and "
                "reports the reading as the lamp's own p.d. anyway, since "
                "'a voltmeter measures p.d.'. Evaluate this reasoning.",
        "options": [
            {"text": "The reading is a genuine p.d., but it is almost "
                     "entirely across the voltmeter itself, not across the "
                     "lamp.", "correct": True},
            {"text": "The reasoning is entirely correct, since a "
                     "voltmeter reads the p.d. of whatever component it "
                     "sits nearest in the loop",
             "correct": False,
             "why": "A voltmeter reads the p.d. across ITSELF, between its "
                    "own two leads — not the p.d. of a component it merely "
                    "sits close to in the loop."},
            {"text": "The reading is meaningless and cannot be a real p.d. "
                     "at all", "correct": False,
             "why": "It IS a real, genuine p.d. — just one across the "
                    "wrong thing, the voltmeter's own huge resistance "
                    "rather than the lamp."},
            {"text": "The reasoning is correct only if the lamp happens to "
                     "be bright enough for its own p.d. to reach the "
                     "voltmeter down the loop", "correct": False,
             "why": "The lamp's brightness has no bearing on which "
                    "component the voltmeter's reading actually belongs "
                    "to."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h12",
        "band": "harder",
        "text": "A circuit gives 0.40 A and 3.0 V across a lamp on Monday, "
                "then 0.30 A and 3.0 V across the SAME lamp on Tuesday, "
                "with nothing deliberately changed. Suggest a genuine "
                "cause, and rule out one that sounds plausible but isn't.",
        "options": [
            {"text": "A genuine cause is the lamp's rating changing "
                     "overnight; ruled out is the cells running down, "
                     "since cells never weaken with use", "correct": False,
             "why": "It is exactly the other way round: a lamp's rating is "
                    "fixed, while cells genuinely do weaken as they are "
                    "used."},
            {"text": "A genuine cause is the cells running down a little "
                     "between days; ruled out is the lamp needing a "
                     "different voltage on different days, since its "
                     "rating does not change.", "correct": True},
            {"text": "A genuine cause is the room getting colder; ruled "
                     "out is any change in the cells", "correct": False,
             "why": "Ordinary room-temperature changes do not "
                    "meaningfully alter a simple circuit's readings; a "
                    "weakening cell is the standard, real explanation."},
            {"text": "A genuine cause is the meters swapping their own "
                     "scales automatically; ruled out is the cells",
             "correct": False,
             "why": "Meters do not change scale on their own overnight; a "
                    "weakening cell remains the sensible explanation here."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h13",
        "band": "harder",
        "text": "A multimeter's ohms setting gives a sensible reading for a "
                "disconnected resistor, but gives a wildly wrong number "
                "for the same resistor while it is still wired into a "
                "live, switched-on circuit. Explain both results using how "
                "the ohms setting works.",
        "options": [
            {"text": "The setting supplies and measures its own small "
                     "current; disconnected, that is the only current "
                     "present, but live, the circuit's own current "
                     "interferes with the measurement.", "correct": True},
            {"text": "The setting only works on resistors below a certain "
                     "value, and this one happens to be too large once "
                     "connected into a circuit that is still switched on, "
                     "so the meter gives up and repeats whatever the last "
                     "resistor it measured showed", "correct": False,
             "why": "The resistor's own value has not changed at all; what "
                    "has changed is whether the CIRCUIT's own current is "
                    "also flowing."},
            {"text": "The meter is faulty and needs replacing, since it "
                     "gives two different readings for one resistor",
             "correct": False,
             "why": "The meter is working correctly in both cases; the two "
                    "very different readings come from a real difference "
                    "in what current is present, not a fault."},
            {"text": "The disconnected reading is the false one, and the "
                     "live reading is the resistor's true value",
             "correct": False,
             "why": "It is the other way round: the disconnected reading "
                    "is the trustworthy one, and the live reading is "
                    "corrupted by the circuit's own current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h14",
        "band": "harder",
        "text": "A group is asked to find out whether the ORDER of two "
                "different lamps in a series loop affects how bright each "
                "one glows. Design the fairest way to test this.",
        "options": [
            {"text": "Build two separate circuits, one for each lamp "
                     "order, using a different battery for each so that "
                     "every order gets a fresh supply, which takes the "
                     "battery out of the comparison altogether",
             "correct": False,
             "why": "Using different batteries introduces a second "
                    "variable, so any difference could come from the "
                    "battery rather than the order."},
            {"text": "Build the circuit once, note each lamp's brightness "
                     "and its meter readings, then swap only their "
                     "positions and repeat, keeping everything else the "
                     "same.", "correct": True},
            {"text": "Ask two different groups to test one order each, "
                     "then compare their results", "correct": False,
             "why": "Different groups' circuits and apparatus are not a "
                    "controlled, fair comparison of order alone."},
            {"text": "Swap the order and also swap the meters to new ones "
                     "at the same time", "correct": False,
             "why": "Changing the meters as well as the order means any "
                    "difference could come from either change."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h15",
        "band": "harder",
        "text": "Explain why 'the reading changed' is not, by itself, "
                "evidence that the thing you changed on purpose caused it.",
        "options": [
            {"text": "Because readings never change for any real reason in "
                     "a school circuit once it has been built and left "
                     "switched on", "correct": False,
             "why": "Readings do change for real reasons; the point is "
                    "making sure the CHANGE you meant to test is the one "
                    "responsible."},
            {"text": "Because meters are not sensitive enough to detect a "
                     "genuine change", "correct": False,
             "why": "School meters are perfectly capable of detecting a "
                    "genuine change; the concern is about the CAUSE, not "
                    "the meter's sensitivity."},
            {"text": "Because only a graph, never a single reading, can "
                     "show a real change", "correct": False,
             "why": "A single before-and-after reading can show a real "
                    "change; the issue is ruling out OTHER causes, not the "
                    "number of readings taken."},
            {"text": "Because something else may also have changed at the "
                     "same time, such as a connection loosening or a cell "
                     "weakening.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h16",
        "band": "harder",
        "text": "A group claims their investigation is fair because they "
                "'kept everything the same except the thing we were "
                "testing'. What is missing from their reasoning, even if "
                "this is true?",
        "options": [
            {"text": "Nothing is missing — that description alone "
                     "guarantees a fair test every single time", "correct": False,
             "why": "A fair CONTROL of variables is one requirement; "
                    "repeating readings to catch odd values is a separate, "
                    "additional check."},
            {"text": "They also needed to change two things at once, to "
                     "see a bigger effect on the readings than changing only one thing would give", "correct": False,
             "why": "Changing two things at once would break the very "
                    "fairness they are claiming to have."},
            {"text": "Whether they REPEATED each reading to rule out a "
                     "one-off fault or a misread scale.", "correct": True},
            {"text": "They needed a different battery for every single "
                     "reading", "correct": False,
             "why": "Changing the battery between readings would itself be "
                    "an uncontrolled variable, not a fix."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h17",
        "band": "harder",
        "text": "A circuit's ammeter and voltmeter both read exactly zero, "
                "but a THIRD meter clipped across the switch itself reads "
                "the full battery p.d. What does this combination pin "
                "down?",
        "options": [
            {"text": "The break must be at the lamp, since the lamp is "
                     "always the first thing to suspect when a circuit "
                     "stops reading, whatever the other meters happen to "
                     "be showing at the time", "correct": False,
             "why": "The switch reading the full p.d. specifically points "
                    "AT the switch, not at the lamp."},
            {"text": "There is no break anywhere, since a p.d. is being "
                     "read somewhere in the circuit", "correct": False,
             "why": "A p.d. appearing across the switch with zero current "
                    "everywhere else is exactly the signature of a break "
                    "at that switch."},
            {"text": "The break in the loop is at the switch itself, since "
                     "the whole battery's push is stuck there with nowhere "
                     "else to go.", "correct": True},
            {"text": "The battery itself must be flat, since the ammeter "
                     "reads zero", "correct": False,
             "why": "A flat battery would give a low reading everywhere, "
                    "not the full rated p.d. concentrated across the "
                    "switch."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h18",
        "band": "harder",
        "text": "Why might a real, working circuit still show a TINY "
                "difference between two ammeters placed at different "
                "points in the same simple loop, even though the theory "
                "says they should read identically?",
        "options": [
            {"text": "Because the current really is used up a little "
                     "between the two points as it travels further from "
                     "the battery", "correct": False,
             "why": "Current is not used up moving round a loop; the "
                    "theoretical prediction of one equal current is "
                    "exactly right."},
            {"text": "Because the two ammeters must be measuring two "
                     "different circuits", "correct": False,
             "why": "Both ammeters are stated to be in the SAME simple "
                    "loop; there is only one circuit here."},
            {"text": "Ordinary meter tolerance and reading precision, not "
                     "a real difference in the current itself, which "
                     "genuinely is the same everywhere in one loop.",
             "correct": True},
            {"text": "Because whichever ammeter is read second always "
                     "reads lower", "correct": False,
             "why": "There is no rule that a second reading is always "
                    "lower; any tiny mismatch comes from ordinary meter "
                    "tolerance, not reading order."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h19",
        "band": "harder",
        "text": "A group wants to investigate how current depends on the "
                "NUMBER OF LAMPS wired in series, but their supply is a "
                "fixed battery that cannot be changed. Explain the "
                "practical limit they will run into as they add more "
                "lamps, and why it happens.",
        "options": [
            {"text": "The current will rise steadily as more lamps are "
                     "added, without any limit", "correct": False,
             "why": "Adding more lamps in SERIES adds more resistance, "
                    "which lowers the current, not raises it."},
            {"text": "The current will stay exactly the same, however many "
                     "lamps are added", "correct": False,
             "why": "Each extra lamp in series adds its own resistance to "
                    "the loop, so the current does change as more are "
                    "added."},
            {"text": "The lamps will get progressively brighter as more "
                     "are added, with no limit on the current however "
                     "many are wired in, because every extra lamp brings "
                     "its own share of push into the loop", "correct": False,
             "why": "More lamps in series means less current reaching "
                    "each one, so they dim rather than brighten."},
            {"text": "The current will keep falling as more lamps add more "
                     "resistance to the loop, eventually becoming too "
                     "small to see clearly or to light any lamp at all.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h20",
        "band": "harder",
        "text": "A student says a circuit diagram and the physical circuit "
                "built from it are 'basically decoration for the same "
                "thing', with no real difference worth discussing. "
                "Evaluate this.",
        "options": [
            {"text": "They are simply identical in every respect, so the "
                     "student is completely right about there being nothing further worth discussing between the two of them", "correct": False,
             "why": "The physical build can develop a real fault the "
                    "diagram never shows, such as a loose connection — a "
                    "genuine difference worth discussing."},
            {"text": "They represent the same circuit, but only the "
                     "physical build can develop real faults like a loose "
                     "clip, which the diagram can never show.",
             "correct": True},
            {"text": "The diagram is always more accurate than the "
                     "physical circuit", "correct": False,
             "why": "The diagram shows the INTENDED circuit; the physical "
                    "build shows what was actually achieved, faults "
                    "included — neither is simply 'more accurate' than the "
                    "other."},
            {"text": "There is no relationship between the two at all",
             "correct": False,
             "why": "The physical circuit is meant to be a faithful build "
                    "of the diagram; they are closely related, just not "
                    "identical once real-world faults are possible."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h21",
        "band": "harder",
        "text": "Why does an experienced technician often check a suspect "
                "circuit by testing each SECTION of the loop in turn (say, "
                "the switch, then the lamp holder, then each clip), rather "
                "than testing the whole loop at once?",
        "options": [
            {"text": "Because a whole-loop test always gives a false "
                     "reading", "correct": False,
             "why": "A whole-loop test genuinely shows whether current "
                    "flows at all; it simply does not say WHERE a break "
                    "is, which is the reason for the section-by-section "
                    "method."},
            {"text": "Because each section of a loop carries a different "
                     "current", "correct": False,
             "why": "One loop carries one current throughout; sectioning "
                    "it is about LOCATING a fault, not about different "
                    "currents in different parts."},
            {"text": "Because testing section by section narrows down "
                     "exactly where a fault is, rather than only "
                     "confirming that a fault exists somewhere.",
             "correct": True},
            {"text": "Because meters can only be trusted on short "
                     "sections of wire, never on a whole loop tested end "
                     "to end at once, where the separate faults average "
                     "themselves out into one reading", "correct": False,
             "why": "Meters work identically on a short section or a whole "
                    "loop; the reason for sectioning is fault-finding, not "
                    "meter trust."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h22",
        "band": "harder",
        "text": "A circuit investigation's results table has a 'repeat 2' "
                "column that exactly matches 'repeat 1' for every single "
                "row, to the last decimal place. Should this level of "
                "agreement raise any concern?",
        "options": [
            {"text": "No — perfect agreement is exactly what every good "
                     "experiment should produce", "correct": False,
             "why": "Some tiny natural variation between genuine repeats "
                    "is normal; suspiciously perfect agreement is worth "
                    "checking, not simply celebrating."},
            {"text": "Yes — it proves the readings must have been copied "
                     "without actually being taken by whichever pair produced that suspiciously tidy table of results in the first place", "correct": False,
             "why": "It is a reason to double-check, not proof on its own; "
                    "very stable apparatus can occasionally give this by "
                    "chance."},
            {"text": "No — meters are built to give identical repeats, so "
                     "this is guaranteed", "correct": False,
             "why": "Meters are not guaranteed to repeat perfectly; "
                    "ordinary reading variation is expected, which is "
                    "exactly why the perfect match is worth a second look."},
            {"text": "Possibly — real repeated readings usually show at "
                     "least tiny natural variation, so perfect agreement "
                     "every time is worth double-checking rather than "
                     "simply accepting.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h23",
        "band": "harder",
        "text": "A group finds that swapping which of two identical "
                "ammeters they use makes a small but consistent difference "
                "to their readings — one ammeter always reads a little "
                "higher than the other on the same circuit. What does "
                "this suggest, and how could they check it?",
        "options": [
            {"text": "It suggests the circuit itself is unstable, and "
                     "the ammeters are blameless however consistently the "
                     "same offset keeps appearing", "correct": False,
             "why": "A CONSISTENT difference tied to WHICH ammeter is used "
                    "points at the meters themselves, not at an unstable "
                    "circuit."},
            {"text": "It cannot be checked, since two ammeters can never "
                     "be compared directly", "correct": False,
             "why": "Two ammeters can be compared directly, exactly as "
                    "suggested, by testing both on the same unchanging "
                    "circuit."},
            {"text": "It suggests one of the two ammeters is measuring "
                     "voltage by mistake", "correct": False,
             "why": "Both are stated to be ammeters giving current "
                    "readings; a small consistent offset points at meter "
                    "tolerance, not at measuring the wrong quantity."},
            {"text": "The two ammeters may not be perfectly identical in "
                     "practice; testing both on a single, unchanging "
                     "circuit one after another would show whether the "
                     "difference is genuine and consistent.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h24",
        "band": "harder",
        "text": "Why is it poor practice to change a circuit's wiring "
                "WHILE the switch is still closed, even for what seems "
                "like a tiny adjustment?",
        "options": [
            {"text": "Because it is against the school's timetable for the "
                     "lesson", "correct": False,
             "why": "The reason given here is about safety and equipment, "
                    "not about timetabling."},
            {"text": "Because the diagram becomes invalid the moment "
                     "the switch is closed and has to be redrawn before "
                     "anyone can trust it again, and it is the out-of-date "
                     "diagram that damages the components", "correct": False,
             "why": "A diagram does not become invalid based on the "
                    "switch; the concern is a genuinely damaging brief "
                    "fault while current flows."},
            {"text": "Because a brief wrong connection while current is "
                     "flowing can send a large current somewhere it should "
                     "not go, damaging a meter or a component.",
             "correct": True},
            {"text": "Because the battery immediately goes flat if touched "
                     "while closed", "correct": False,
             "why": "A battery does not go flat instantly from a brief "
                    "touch; the real risk is a damaging surge through a "
                    "meter or component."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h25",
        "band": "harder",
        "text": "A circuit built for an investigation happens to include a "
                "longer-than-necessary loop of spare wire, coiled up out "
                "of the way. Does this coil affect the results, and "
                "should it be removed?",
        "options": [
            {"text": "It has absolutely no effect whatsoever, so there is "
                     "never any reason to remove it, however long the "
                     "spare loop happens to be, since a loop's resistance "
                     "comes only from the components fitted into it", "correct": False,
             "why": "Any extra length of wire adds a little resistance, "
                    "even if it is normally too small to matter — 'no "
                    "effect whatsoever' overstates it."},
            {"text": "It adds a very small amount of extra resistance from "
                     "the extra wire length, which is usually negligible "
                     "but is best removed for a cleaner, fairer test.",
             "correct": True},
            {"text": "It will make the circuit dangerously overheat, and "
                     "must be removed immediately", "correct": False,
             "why": "A modest coil of ordinary wire in a low-voltage "
                    "school circuit is not a serious heating hazard; the "
                    "concern is tidiness and a slightly cleaner result, not "
                    "danger."},
            {"text": "It changes which component the ammeter is "
                     "measuring", "correct": False,
             "why": "A coiled length of connecting wire does not change "
                    "what the ammeter is measuring; it can only add a "
                    "small resistance to the loop."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h26",
        "band": "harder",
        "text": "Two students disagree: one says a voltmeter reading of "
                "exactly the battery's rated p.d., taken across a single "
                "lamp in a simple loop, proves the circuit is working "
                "correctly. The other says it might not. Who is right, "
                "and why?",
        "options": [
            {"text": "The first student — that exact reading can only "
                     "ever mean a correctly working circuit, and no fault "
                     "could produce that same number", "correct": False,
             "why": "The very same reading also appears in a specific "
                    "fault (the voltmeter wired into the loop), so it "
                    "cannot PROVE the circuit is correct on its own."},
            {"text": "Neither — the reading given is actually impossible "
                     "for any circuit to produce", "correct": False,
             "why": "That reading is entirely possible, and even common, "
                    "in more than one situation — both the working circuit "
                    "and one particular fault."},
            {"text": "The second student — that exact reading is also what "
                     "you would see if the voltmeter were wrongly wired "
                     "into the loop instead of across the lamp.",
             "correct": True},
            {"text": "The first student, but only if the lamp is new",
             "correct": False,
             "why": "The lamp's age has no bearing on which of the two "
                    "explanations for that reading is correct."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h27",
        "band": "harder",
        "text": "Explain why a fault-finding guide tells you to check the "
                "SIMPLEST, most common causes (a loose clip, an open "
                "switch) before the rarer ones (a broken meter, a "
                "manufacturing fault in the lamp).",
        "options": [
            {"text": "Because rare faults are impossible in a school "
                     "circuit and never need checking by anyone, however "
                     "carefully they look, so a fault-finding guide lists "
                     "only the faults that can actually happen", "correct": False,
             "why": "Rare faults are not impossible, just uncommon; the "
                    "guide's ORDER is about likelihood, not about ruling "
                    "rare faults out entirely."},
            {"text": "Because simple faults are the only ones a school "
                     "meter can detect", "correct": False,
             "why": "A school meter can reveal evidence of any of these "
                    "faults; the ordering is about which cause is MOST "
                    "LIKELY, not about detection limits."},
            {"text": "Because checking rare faults first would damage the "
                     "equipment", "correct": False,
             "why": "Checking for a rare fault does not itself damage "
                    "anything; the ordering is purely about efficiency, "
                    "checking likely causes first."},
            {"text": "Because the simple, common faults account for most "
                     "real breakdowns, so checking them first always finds "
                     "the problem faster on average.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h28",
        "band": "harder",
        "text": "A group's circuit works fine when tested on the bench at "
                "school, but a very similar circuit built by the same "
                "group at home, with a different (but similar) battery, "
                "behaves noticeably differently. Name one variable that "
                "has genuinely changed, and one thing that has probably "
                "stayed the same.",
        "options": [
            {"text": "Changed: the laws of physics between school and "
                     "home. Stayed the same: the battery and its exact "
                     "condition", "correct": False,
             "why": "Physics does not change between locations; the "
                    "battery is exactly the part that HAS changed here."},
            {"text": "Changed: nothing at all, since it is the same group. "
                     "Stayed the same: everything", "correct": False,
             "why": "A different battery, by the question's own "
                    "description, is a real change — not nothing."},
            {"text": "Changed: the components' identities. Stayed the "
                     "same: the battery", "correct": False,
             "why": "The question states a DIFFERENT battery was used at "
                    "home; the components are described as similar, i.e. "
                    "unchanged in identity."},
            {"text": "Changed: the exact battery and its condition. Stayed "
                     "the same: the basic circuit design and the "
                     "components' identities.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h29",
        "band": "harder",
        "text": "A group proposes testing whether current depends on lamp "
                "brightness by simply looking at different lamps and "
                "guessing which is brighter, rather than measuring "
                "anything. Critique this method.",
        "options": [
            {"text": "Brightness judged by eye is not a reliable number; "
                     "two different people might disagree, and it cannot "
                     "be compared precisely between lamps or repeated "
                     "exactly.", "correct": True},
            {"text": "The method is perfectly fine, since brightness and "
                     "current are the same thing to anyone looking at two "
                     "lamps side by side, and the eye compares two "
                     "brightnesses more finely than any meter can", "correct": False,
             "why": "Brightness and current are related but are not the "
                    "same quantity, and 'looking at brightness' gives no "
                    "actual number to compare."},
            {"text": "The only problem is that it takes too long to look "
                     "at each lamp", "correct": False,
             "why": "Time is not the real problem; the lack of an "
                    "objective, repeatable NUMBER is."},
            {"text": "The method is fine as long as the same person looks "
                     "at every lamp", "correct": False,
             "why": "Even one consistent observer is still judging "
                    "brightness by eye, with no real number attached, "
                    "rather than measuring it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-07-h30",
        "band": "harder",
        "text": "Summarise, for a younger student, why 'build with the "
                "switch open, check every connection, then close the "
                "switch and read' is a better instruction than 'build the "
                "circuit and see what happens'.",
        "options": [
            {"text": "The first method is simply the traditional way and "
                     "carries no real advantage over building the circuit "
                     "and seeing what happens", "correct": False,
             "why": "There is a real, practical advantage: catching "
                    "mistakes before current flows, which the second "
                    "method risks missing entirely."},
            {"text": "The first method catches wiring mistakes before any "
                     "current flows, avoiding damaged meters or components "
                     "and making faults far easier to trace.",
             "correct": True},
            {"text": "The second method is actually safer, since it finds "
                     "faults immediately", "correct": False,
             "why": "The second method risks running current through a "
                    "wrongly-wired circuit BEFORE any fault is caught, "
                    "which is the more dangerous order."},
            {"text": "Both methods are identical once the switch is "
                     "eventually closed", "correct": False,
             "why": "The difference is in WHEN faults are caught — before "
                    "current flows, or only after — which is not erased by "
                    "the switch eventually closing in both cases."},
        ],
        "figure": None,
    },
]
