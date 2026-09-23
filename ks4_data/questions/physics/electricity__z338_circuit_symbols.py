"""Physics · Electricity — the MRB-338 expansion of `circuit-symbols`.

One leaf only: AQA 8463 §6.2.1.1, drawing and interpreting circuit diagrams
with standard symbols. The original twelve rows already own the variable
resistor, the open switch, why standard symbols exist at all, the battery
against the single cell, the ammeter wired in parallel, the LDR for a light
sensor, the redraw onto separate branches, the schematic-not-to-scale rule,
the LED the wrong way round, thermistor against LDR, the two meters' internal
resistances, and the ammeter reading a total current.

⊕ MRB-352 run 2 (Mide's rulings): no circuit question may use a motor
symbol — the motor is not on the AQA 8463 §4.2.1.1 list — and no question
may ask a pupil to describe a symbol or a diagram in words. The ten rows
that used a motor (e06, s05, s06, s19, s23, s26, h08, h14, h21, h24) were
rebuilt on the same id, band and tier: six around a drawn figure, four with
the motor swapped for an AQA component. The notes below describe the file
as first authored.

This file takes what those leave, and the weight follows the CONTENT. The
`easier` eight are the symbols the baseline never names — the alternating
supply, the motor, the buzzer, the fuse, the plain rectangle of a fixed
resistor, the two outward arrows that make a diode an LED, the closed switch,
and the rule that components sit on the lines. The real demand in this
subtopic is not symbol recall at all: it is READING a circuit that is
described only in words — which components share a loop, how many paths the
current has, what one switch in one branch controls, what a meter in a branch
can and cannot read — and finding the fault in a diagram that has been drawn
wrongly. So `standard` and `harder` carry twenty-two rows each, and most of
them hand the pupil a circuit in prose and ask what it does.

Nothing here asks a pupil to look at a picture: every described circuit is
traced in words, from the cell's long line round to its short one. Meter
resistance, Ohm's law, the mains and the behaviour of an LED under reverse
bias all belong to other leaves and are absent.
"""

TOPIC = "electricity"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The symbols the frozen twelve never name: ac supply, (motor — e06
    # is now the ammeter, MRB-352), buzzer, fuse, the plain rectangle, the LED's outward arrows, the closed
    # switch, and where a component sits on the line.
    {
        "id": "ks4-circuit-symbols-e05",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a circle with a sine wave drawn inside it "
                "stands for.",
        "options": [
            "An alternating supply, such as a laboratory power pack",
            "A single cell, drawn this way when its voltage can be set",
            "A battery whose cells are stacked inside a circular case of "
            "their own",
            "A rechargeable cell, drawn this way while it is charging",
        ],
        "correct_index": 0,
        "why": "The sine wave inside the circle stands for a current that "
               "repeatedly changes direction, which is what an alternating "
               "supply provides.",
    },
    {
        "id": "ks4-circuit-symbols-e06",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-symbol-ammeter",
        "text": "The diagram shows a circuit symbol. Which component does it "
                "represent?",
        "options": [
            "A voltmeter, which measures the potential difference across a "
            "component",
            "A lamp, which gives out light when a current passes through it",
            "An ammeter, which measures the current through a component",
            "A fuse, which melts if the current becomes too large",
        ],
        "correct_index": 2,
        "why": "A circle with the letter A inside it is the ammeter symbol — the"
               " A is for amperes, the unit of current. A voltmeter is a circle "
               "with a V, and a lamp is a circle with a cross.",
    },
    {
        "id": "ks4-circuit-symbols-e07",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram shows a small rectangle inside a circle. Name "
                "that component.",
        "options": [
            "A fuse, whose rectangle is ringed to warn a reader that it can "
            "melt open",
            "A buzzer, which makes a sound when a current passes through it",
            "A battery, whose rectangle stands for the cells inside its case",
            "A switch, whose rectangle is the lever that meets the contact",
        ],
        "correct_index": 1,
        "why": "A buzzer is drawn as a circle with a rectangle inside it, "
               "and it sounds while a current passes through it.",
    },
    {
        "id": "ks4-circuit-symbols-e08",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "One symbol is a rectangle with a thin line running along "
                "its length. Which component is it?",
        "options": [
            "A cell, whose line through the box joins its positive end to "
            "its negative end",
            "A buzzer, whose line through the box stands for the sound made",
            "A closed switch, whose line is the lever resting on a contact",
            "A fuse, which breaks the circuit if the current becomes too "
            "large",
        ],
        "correct_index": 3,
        "why": "The line drawn through the resistor-shaped rectangle is the "
               "thin wire of a fuse, which melts and breaks the circuit when "
               "the current is too large.",
    },
    {
        "id": "ks4-circuit-symbols-e09",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a diagram, one of the rectangles carries no extra mark. "
                "State which component that is.",
        "options": [
            "A variable resistor, whose resistance the user sets by hand",
            "A fixed resistor, whose resistance stays at one value",
            "A thermistor, whose resistance falls as it becomes warmer",
            "An LDR, whose resistance falls when the light shining on its "
            "surface brightens",
        ],
        "correct_index": 1,
        "why": "The plain rectangle is the fixed resistor; every other "
               "member of that family adds a mark to show what changes its "
               "resistance.",
    },
    {
        "id": "ks4-circuit-symbols-e10",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diode symbol is drawn with two arrows pointing away from "
                "it. Which component does this show?",
        "options": [
            "A light-emitting diode, which gives out light as it conducts",
            "A diode that has been damaged and now conducts in both ways",
            "A diode fitted with a fuse to guard it from a large current",
            "A light-dependent resistor, which responds to the light on it",
        ],
        "correct_index": 0,
        "why": "Two arrows drawn pointing away from a diode show light "
               "leaving it, which makes the symbol a light-emitting diode.",
    },
    {
        "id": "ks4-circuit-symbols-e11",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "How is a closed switch shown on a circuit diagram?",
        "options": [
            "By a gap in the wire with the lever raised",
            "By a circle with the letter S drawn inside",
            "By a rectangle with a line along its length",
            "By the lever lowered onto its contact, so the wire is whole",
        ],
        "correct_index": 3,
        "why": "Closing a switch joins the wire again, so the symbol shows "
               "the lever lying on its contact with no gap left.",
    },
    {
        "id": "ks4-circuit-symbols-e12",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Where should components be placed when a circuit diagram "
                "is drawn?",
        "options": [
            "At the corners, where the two wires reaching a component are "
            "already joined",
            "Wherever they sit on the bench, so the drawing matches it",
            "On the straight lines, spaced out along the sides of the loop",
            "Outside the loop, with a short wire joining each one of them "
            "to it",
        ],
        "correct_index": 2,
        "why": "Components are drawn on the straight ruled lines so that the "
               "two wires reaching each one can be seen clearly.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Symbols put to work: finding the fault in a wrongly drawn diagram,
    # reading a circuit given only in words, and the drawing conventions
    # applied rather than recited.
    {
        "id": "ks4-circuit-symbols-s05",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-torch-ldr-for-bulb",
        "text": "A student draws the circuit for a torch, which holds a battery, "
                "a switch and a bulb. The drawing is shown. Explain the error.",
        "options": [
            "The battery should be drawn as a single cell, because a torch "
            "can only hold one cell",
            "The bulb has been drawn with the LDR symbol instead of the lamp "
            "symbol",
            "The parts should be drawn on separate branches, one branch for "
            "each part",
            "Nothing is wrong, as any symbol may stand for a part that gives "
            "out light",
        ],
        "correct_index": 1,
        "why": "The symbol where the bulb should be — a small rectangle inside a"
               " circle with two arrows pointing in — is a light-dependent "
               "resistor, which responds to light rather than giving it out. A "
               "torch bulb is a lamp, drawn as a circle with a cross. The "
               "battery, the switch and the single loop are right.",
    },
    {
        "id": "ks4-circuit-symbols-s06",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell, a switch and a lamp are joined in one loop. State where "
                "a voltmeter is connected to measure the potential difference "
                "across the lamp.",
        "options": [
            "In the loop between the switch and the lamp, like an ammeter",
            "Across the two terminals of the cell, where the supply is made",
            "In the loop on the far side of the lamp from the cell",
            "On a second pair of wires joined either side of the lamp",
        ],
        "correct_index": 3,
        "why": "A voltmeter is connected in parallel, bridging the component "
               "with its own pair of wires so that it spans the lamp only.",
    },
    {
        "id": "ks4-circuit-symbols-s07",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A voltmeter is wired into the loop itself, in line with a "
                "lamp, rather than bridging across the lamp. Predict what "
                "happens.",
        "options": [
            "Hardly any current flows, as the voltmeter resists it strongly",
            "The lamp lights as usual, as a voltmeter changes no circuit",
            "The voltmeter is short-circuited by the lamp and its reading "
            "runs off the scale",
            "The lamp glows brighter, as the voltmeter adds its own supply",
        ],
        "correct_index": 0,
        "why": "A voltmeter is built with a very high resistance, so placing "
               "it in the loop itself leaves almost no current for the lamp.",
    },
    {
        "id": "ks4-circuit-symbols-s08",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A supply is drawn as three long lines, each paired with a "
                "short line, joined end to end. State what it shows.",
        "options": [
            "Three separate circuits, each of them fed by a supply of its "
            "own",
            "One cell that has been drawn three times over by mistake",
            "Three cells joined in series, making a battery",
            "Three resistors joined one after another along the loop",
        ],
        "correct_index": 2,
        "why": "Each long-and-short pair of lines is one cell, so three "
               "pairs drawn end to end show three cells in series.",
    },
    {
        "id": "ks4-circuit-symbols-s09",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is joined to a switch, the switch to a buzzer, and "
                "the buzzer back to the cell. State how the three components "
                "are connected.",
        "options": [
            "In parallel, because each one has the cell across it",
            "In parallel, because the current divides between them",
            "In series, because there is one path for the current",
            "In series, because each one sits on a branch of its own",
        ],
        "correct_index": 2,
        "why": "One unbroken loop with no junctions is a series circuit: the "
               "same current passes through every component in turn.",
    },
    {
        "id": "ks4-circuit-symbols-s10",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the wires on a circuit diagram are drawn as "
                "straight ruled lines.",
        "options": [
            "Because a ruled line has a lower resistance than a curved one",
            "Because the connections are then clear to anyone reading it",
            "Because the ruled length of a line gives the length of wire",
            "Because a ruled line shows the current which path to take",
        ],
        "correct_index": 1,
        "why": "Straight ruled lines make it unambiguous which components "
               "are joined to which, which is the whole purpose of the "
               "diagram.",
    },
    {
        "id": "ks4-circuit-symbols-s11",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the order to work in when sketching a circuit "
                "diagram.",
        "options": [
            "Meters first, so that each one has room",
            "The lamps first, as they are being tested",
            "The wires first, then the corners",
            "Supply and switch first, then the components, then the meters",
        ],
        "correct_index": 3,
        "why": "Drawing the supply and switch first fixes the shape of the "
               "loop, so the components and then the meters can be fitted "
               "into it neatly.",
    },
    {
        "id": "ks4-circuit-symbols-s12",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram is to be read. Describe where to begin tracing "
                "the circuit, and why.",
        "options": [
            "At the switch, as the switch is the part that starts a circuit",
            "At the component being tested, working outwards to the supply",
            "At any corner, as the corners are where the branches divide",
            "At the long line of the cell, following the current round",
        ],
        "correct_index": 3,
        "why": "The long line of the cell is its positive terminal, so "
               "tracing from there follows the conventional current through "
               "each component in turn.",
    },
    {
        "id": "ks4-circuit-symbols-s13",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram carries a circle with the letter A inside it, "
                "labelled as the buzzer. Explain what is wrong.",
        "options": [
            "The label is right, but the circle belongs on its own branch",
            "The letter is right, but a buzzer is drawn as a rectangle",
            "That circle is an ammeter; a buzzer holds a rectangle inside",
            "The label is wrong: a circle holding the letter A is how an "
            "alternating supply is drawn",
        ],
        "correct_index": 2,
        "why": "A circle with A inside it is the ammeter, while the buzzer "
               "is the circle holding a small rectangle.",
    },
    {
        "id": "ks4-circuit-symbols-s14",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a diagram of a cell, a switch and a lamp, one wire stops "
                "short of the cell and does not reach it. A technician "
                "builds the circuit exactly as drawn. Predict what happens.",
        "options": [
            "Nothing happens, as a broken loop can never carry a current",
            "The lamp lights dimly, as the current crosses the small gap",
            "The lamp lights fully, as the missing piece is only on paper",
            "The lamp flickers, as current reaches it along the other wire "
            "and then falls away",
        ],
        "correct_index": 0,
        "why": "A current needs a complete loop, so a gap anywhere in a "
               "single-loop circuit stops the current everywhere in it.",
    },
    {
        "id": "ks4-circuit-symbols-s15",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram shows two rectangles: one is plain, and one has a "
                "line drawn along its length. State what each one is.",
        "options": [
            "The plain one is a fuse and the other a fixed resistor",
            "Both are resistors, the line marking the larger of the two",
            "The plain one is a switch and the other a variable resistor",
            "The plain one is a fixed resistor and the other a fuse",
        ],
        "correct_index": 3,
        "why": "The plain rectangle is the fixed resistor, and the line "
               "drawn through a rectangle is the fuse wire.",
    },
    {
        "id": "ks4-circuit-symbols-s16",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diode must let the current pass from the cell to a "
                "buzzer. Describe how its triangle should be drawn.",
        "options": [
            "Pointing back at the cell, so the current is pushed on",
            "Pointing towards the buzzer, as a diode passes current one "
            "way only",
            "Pointing upwards, as a diode symbol is drawn upright",
            "Either way round, as a diode blocks only large currents",
        ],
        "correct_index": 1,
        "why": "A diode passes current in the direction its triangle points, "
               "so the triangle must point the way the current is wanted.",
    },
    {
        "id": "ks4-circuit-symbols-s17",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp's brightness must be adjustable while the circuit "
                "runs, but the diagram shows a plain rectangle. Suggest the "
                "correction.",
        "options": [
            "Draw an arrow through the rectangle, making it a variable one",
            "Draw a diagonal line through it, making it a thermistor",
            "Draw two arrows pointing in at it, making it an LDR",
            "Draw a second plain rectangle beside it",
        ],
        "correct_index": 0,
        "why": "The arrow struck through the rectangle is the variable "
               "resistor, the component whose resistance a user can change "
               "while the circuit runs.",
    },
    {
        "id": "ks4-circuit-symbols-s18",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a diagram the cell is drawn with its long line on the "
                "left. State what this tells a student.",
        "options": [
            "That the cell is the largest component in this circuit",
            "That the diagram is meant to be read from the left to the right",
            "That the left-hand end is the positive terminal of the cell",
            "That the cell has been fitted the wrong way round in its holder",
        ],
        "correct_index": 2,
        "why": "In the cell symbol the long line is the positive terminal "
               "and the short line the negative one.",
    },
    {
        "id": "ks4-circuit-symbols-s19",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-symbol-panel-battery-ldr-switch-lamp",
        "text": "A circuit must contain a battery, a closed switch and a lamp. "
                "The diagram shows four circuit symbols. Which three are needed?",
        "options": [
            "P, Q and R",
            "Q, R and S",
            "P, Q and S",
            "P, R and S",
        ],
        "correct_index": 3,
        "why": "P is a battery (two cells joined by a dashed line), R is a "
               "closed switch (its lever joins both contacts) and S is a lamp (a"
               " circle with a cross). Q, with arrows pointing in, is a "
               "light-dependent resistor, which this circuit does not need.",
    },
    {
        "id": "ks4-circuit-symbols-s20",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is joined to a switch; the wire then divides, one "
                "branch holding a buzzer and the other a lamp, and the "
                "branches rejoin before the cell. State how many complete "
                "paths the current has.",
        "options": [
            "One, because the switch puts every part into a single loop",
            "Two, one through the buzzer and one through the lamp",
            "Three, counting the two branches and the main wire",
            "Four, counting each branch in both directions round",
        ],
        "correct_index": 1,
        "why": "Each branch gives the current one route from the cell and "
               "back, so a circuit that divides into two branches has two "
               "complete paths.",
    },
    {
        "id": "ks4-circuit-symbols-s21",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rectangle with a line running through it is drawn in the "
                "wire leaving the supply. Describe what this component does.",
        "options": [
            "It stores charge, letting it go when the current drops too low",
            "It holds the current steady at the value the supply gives",
            "It melts and breaks the circuit if the current becomes too big",
            "It lowers the current to a safe value each time that this is "
            "needed",
        ],
        "correct_index": 2,
        "why": "That symbol is a fuse: a thin wire that melts and opens the "
               "circuit once the current passing through it is too large.",
    },
    {
        "id": "ks4-circuit-symbols-s22",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram has a lamp drawn at the corner where two wires "
                "meet. Explain why this is poor practice.",
        "options": [
            "The lamp is dimmer at a corner, as the wire bends",
            "A corner carries twice the current, so the lamp may fail",
            "A lamp is drawn at a corner when a circuit branches",
            "The corner hides which wires join the lamp, so the loop is "
            "unclear",
        ],
        "correct_index": 3,
        "why": "A component drawn on a straight side shows its two "
               "connections plainly; one drawn into a corner leaves a reader "
               "guessing which wires reach it.",
    },
    {
        "id": "ks4-circuit-symbols-s23",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-ammeter-voltmeter-resistor",
        "text": "The diagram shows a circuit with two meters. What does each "
                "meter measure?",
        "options": [
            "The meter in the loop measures the potential difference across "
            "the cell; the other measures the current in the resistor",
            "The meter in the loop measures the current; the other measures "
            "the potential difference across the resistor",
            "Both meters measure the current, one before the resistor and one"
            " across it",
            "Both meters measure the potential difference, one across the "
            "cell and one across the resistor",
        ],
        "correct_index": 1,
        "why": "The circle with A is an ammeter, connected in series in the "
               "loop, so it measures the current. The circle with V is a "
               "voltmeter, connected in parallel across the resistor, so it "
               "measures the potential difference across the resistor.",
    },
    {
        "id": "ks4-circuit-symbols-s24",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A circuit must be drawn in its switched-off state. A pupil "
                "draws the lever resting on the contact. Explain the error.",
        "options": [
            "A lever drawn down means the circuit is off, so it is correct",
            "A switched-off circuit is shown by leaving the switch symbol "
            "out of the diagram",
            "A switched-off circuit is shown by a cross drawn over the switch",
            "The lever must be lifted clear, leaving a gap in the wire",
        ],
        "correct_index": 3,
        "why": "The lever resting on its contact is the closed switch, so a "
               "circuit meant to be off is drawn with the lever raised and "
               "the wire broken.",
    },
    {
        "id": "ks4-circuit-symbols-s25",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell feeds a switch; the wire then divides into two "
                "branches, each holding a lamp, before rejoining. Predict "
                "what the lamps do when the switch is opened.",
        "options": [
            "Both go out, as all the current must pass through that switch",
            "Both stay lit, as each branch still has a complete loop of "
            "its own",
            "One goes out and the other stays lit, sharing the current",
            "Both dim, as the switch halves the current in each branch",
        ],
        "correct_index": 0,
        "why": "The switch sits in the single wire that every branch is fed "
               "from, so opening it breaks the supply to both branches at "
               "once.",
    },
    {
        "id": "ks4-circuit-symbols-s26",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-symbol-panel-diode-ldr-led-lamp",
        "text": "A warning light is to be made with a light-emitting diode. The "
                "diagram shows four circuit symbols. Which one should be drawn?",
        "options": [
            "P",
            "Q",
            "R",
            "S",
        ],
        "correct_index": 2,
        "why": "R is the LED: a diode symbol with two arrows pointing outwards, "
               "for the light it gives out. P is a plain diode, which gives out "
               "no light. Q's arrows point inwards, making it a light-dependent "
               "resistor. S is a filament lamp.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Unfamiliar contexts: circuits given only in prose, diagrams with a
    # fault to find, claims to evaluate, and what a symbol error would
    # actually build.
    {
        "id": "ks4-circuit-symbols-h05",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A class is given a list naming a cell, a switch and two "
                "lamps, and asked why a circuit diagram is still needed. "
                "Evaluate the list.",
        "options": [
            "The list is enough, as a circuit works however its parts are "
            "joined",
            "The list is enough, as the symbol for each part is a standard "
            "one",
            "The list is not enough, as it does not show how the parts are "
            "joined",
            "The list is not enough, as it does not give the size of each "
            "part",
        ],
        "correct_index": 2,
        "why": "Two lamps in one loop and two lamps on separate branches "
               "need the same list of parts but behave differently, so only "
               "a diagram fixes the circuit.",
    },
    {
        "id": "ks4-circuit-symbols-h06",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram was meant to protect a circuit with a fuse, but a "
                "plain rectangle has been drawn instead. Predict what the "
                "built circuit does if the current becomes far too large.",
        "options": [
            "The rectangle melts first, as a resistor gives way before a fuse",
            "Nothing breaks the circuit, as a resistor does not melt open",
            "The current is cut off, as a resistor opens above its rating",
            "The supply shuts itself down, as the diagram shows no fuse",
        ],
        "correct_index": 1,
        "why": "A fixed resistor is built to carry current, not to fail, so "
               "a circuit drawn with one in place of a fuse has no "
               "protection at all.",
    },
    {
        "id": "ks4-circuit-symbols-h07",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram shows two circles: one lies in the loop itself, "
                "the other on a short pair of wires bridging a resistor. "
                "Determine which meter is which.",
        "options": [
            "The one in the loop is the ammeter; the bridging one is the "
            "voltmeter",
            "The one in the loop is the voltmeter; the bridging one is the "
            "ammeter",
            "Both are ammeters, as a meter is drawn inside the loop whose "
            "current it is reading",
            "Both are voltmeters, as each of them is reached by a pair of "
            "wires",
        ],
        "correct_index": 0,
        "why": "An ammeter is drawn in the loop so the whole current passes "
               "through it, while a voltmeter bridges the component it "
               "spans.",
    },
    {
        "id": "ks4-circuit-symbols-h08",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-two-lamp-branches-switch-y",
        "text": "The diagram shows a circuit. Determine what the switch controls.",
        "options": [
            "Both lamps, as one cell feeds them both",
            "Lamp X only, as a switch acts on the branch opposite it",
            "Lamp Y only, as it is the one lamp in the switch's branch",
            "Neither lamp, as a switch has an effect only in the main wire",
        ],
        "correct_index": 2,
        "why": "A switch breaks the path it is in, so a switch in one branch "
               "stops that branch alone and leaves the other branch complete. "
               "Opening it turns off lamp Y; lamp X stays lit.",
    },
    {
        "id": "ks4-circuit-symbols-h09",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil labels a supply as two cells but draws only one "
                "long line with one short line. Evaluate the diagram.",
        "options": [
            "It is correct, as the label tells the reader how many cells "
            "there are",
            "It is correct, as a single pair of lines stands for a supply "
            "of any size",
            "It is wrong: two cells are drawn as two long-and-short pairs "
            "in line",
            "It is wrong: two cells are drawn as two long lines with one "
            "short",
        ],
        "correct_index": 2,
        "why": "One long-and-short pair is one cell, so a battery of two "
               "cells is drawn as two such pairs joined end to end.",
    },
    {
        "id": "ks4-circuit-symbols-h10",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A circuit is to hold two cells, one switch, one lamp and "
                "one ammeter, all in a single loop. Determine how many "
                "symbols are drawn in total.",
        "options": [
            "Four symbols, as the two cells count as a single battery symbol",
            "Five symbols, one for each cell and one for each other part",
            "Six symbols, counting one more for the loop of wire that joins "
            "them all up",
            "Three symbols, as the meter is a label rather than a part",
        ],
        "correct_index": 1,
        "why": "Every cell is drawn as its own long-and-short pair, so two "
               "cells plus the switch, the lamp and the ammeter make five "
               "symbols.",
    },
    {
        "id": "ks4-circuit-symbols-h11",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A circuit divides into two branches, one with a lamp and "
                "one with a buzzer. A gap is left in the lamp branch only, "
                "and the circuit is built as drawn. Determine what works.",
        "options": [
            "Neither works, as a gap anywhere stops the whole circuit",
            "Both work, as the current reaches the lamp by the other branch",
            "Only the buzzer works: its own branch is still a whole path",
            "Only the lamp works, as the gap leaves more current for it",
        ],
        "correct_index": 2,
        "why": "Each branch is a separate path, so breaking one leaves the "
               "other joined to the supply and still carrying a current.",
    },
    {
        "id": "ks4-circuit-symbols-h12",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A model railway controller must let its user change the "
                "current to the track while the train runs. Compare a plain "
                "rectangle with a rectangle carrying an arrow.",
        "options": [
            "The plain one, as its value is picked before drawing",
            "The one with an arrow, as the arrow shows a resistance that is "
            "set by hand",
            "Either, as an arrow marks which way the current goes",
            "Neither, as track current is changed at the supply",
        ],
        "correct_index": 1,
        "why": "The arrow through the rectangle is the variable resistor, "
               "the only one of the two whose resistance can be altered "
               "while the circuit is working.",
    },
    {
        "id": "ks4-circuit-symbols-h13",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that the triangle in a diode symbol points "
                "the way the electrons move. Evaluate the claim.",
        "options": [
            "Correct, as each circuit symbol is drawn to follow the "
            "electrons",
            "Correct, as electrons and conventional current run the same way",
            "Wrong: the triangle points the way the conventional current "
            "flows",
            "Wrong: the triangle points to the end where the diode is joined",
        ],
        "correct_index": 2,
        "why": "Circuit symbols follow the conventional current, which runs "
               "from the positive terminal of the supply, and electrons in "
               "the wires travel the other way.",
    },
    {
        "id": "ks4-circuit-symbols-h14",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell feeds two parallel branches, one holding a resistor and "
                "one holding a lamp. An ammeter is to read the current in the "
                "resistor alone. Determine where it is placed.",
        "options": [
            "In the resistor branch, between the junction and the resistor",
            "In the main wire, where the whole of the current passes",
            "On a pair of wires bridging the resistor from side to side",
            "In the lamp branch, whose reading is taken away from the total",
        ],
        "correct_index": 0,
        "why": "An ammeter reads the current in the path it is placed in, so "
               "reading one branch means placing it inside that branch.",
    },
    {
        "id": "ks4-circuit-symbols-h15",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two lamps are wired from one cell. One lamp fails, and the "
                "other stays lit. Determine which diagram matches what "
                "happened.",
        "options": [
            "The two lamps drawn one after the other along a single loop of "
            "wire",
            "The two lamps drawn on separate branches from the same cell",
            "The two lamps drawn in one loop with a switch between the two",
            "The two lamps drawn in one loop with the cell between them",
        ],
        "correct_index": 1,
        "why": "A failed lamp breaks the path it sits in, so the second lamp "
               "can only stay lit if it has a complete path of its own.",
    },
    {
        "id": "ks4-circuit-symbols-h16",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil draws the ammeter and voltmeter first and then "
                "finds there is no room left for the lamp. Evaluate the "
                "method used.",
        "options": [
            "Sound, as the meters are the parts whose positions matter most",
            "Sound, as a meter takes more room on paper than a lamp does",
            "Poor: the supply and switch are drawn first to fix the loop",
            "Poor: the wires should have been ruled in before anything else",
        ],
        "correct_index": 2,
        "why": "Sketching the supply and the switch first sets out the shape "
               "and size of the loop, leaving room for the components and "
               "the meters that go into it.",
    },
    {
        "id": "ks4-circuit-symbols-h17",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell feeds two branches. One branch holds a lamp on its "
                "own; the other holds a lamp with a rectangle carrying an "
                "arrow beside it. Determine which lamp can be dimmed.",
        "options": [
            "Both lamps, as the two branches are fed by the same cell",
            "The lamp sharing its branch with the variable resistor",
            "The lamp on its own, which the resistor leaves more current for",
            "Neither lamp, as brightness is changed at the supply itself",
        ],
        "correct_index": 1,
        "why": "A variable resistor changes the current in the path it is "
               "drawn in, so it dims the lamp sharing its branch and leaves "
               "the other branch alone.",
    },
    {
        "id": "ks4-circuit-symbols-h18",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram shows a cell joined to a lamp by two ruled wires, "
                "and a pupil complains that the lamp cannot be turned off. "
                "Determine which symbol is missing.",
        "options": [
            "An ammeter, drawn in the loop to show when a current flows",
            "A fuse, drawn as a rectangle with a line running through it",
            "A second cell, drawn in series with the first one",
            "A switch, drawn as a gap in the wire with a hinged lever",
        ],
        "correct_index": 3,
        "why": "A switch is the component that opens and closes the loop, so "
               "a circuit drawn without one cannot be turned off.",
    },
    {
        "id": "ks4-circuit-symbols-h19",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A circuit is powered by three cells in a battery holder, "
                "but the diagram shows the supply as a circle with a sine "
                "wave. Suggest the correction.",
        "options": [
            "Add the letter D inside the circle to show direct current",
            "Replace it with three long-and-short pairs drawn end to end",
            "Replace it with a rectangle, as a holder is a fixed component",
            "Leave it, as any supply may be drawn as a circle with a wave",
        ],
        "correct_index": 1,
        "why": "The circle with a sine wave is an alternating supply, while "
               "cells give a direct current and are drawn as long-and-short "
               "pairs in series.",
    },
    {
        "id": "ks4-circuit-symbols-h20",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single loop is drawn holding a cell, a lamp and two "
                "switches. Determine what the lamp does when one switch is "
                "closed and the other is left open.",
        "options": [
            "It lights fully, as one closed switch completes the loop",
            "It lights dimly, as only half of the loop has been closed off "
            "by the open switch",
            "It stays off, as a loop with a switch open never carries a "
            "current",
            "It flashes, as the current passes the open switch in bursts",
        ],
        "correct_index": 2,
        "why": "In a single loop the current has one path, so every switch "
               "in that path has to be closed before the lamp can light.",
    },
    {
        "id": "ks4-circuit-symbols-h21",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two lamps, X and Y, are on separate parallel branches fed by one"
                " cell. Lamp X must be switchable on its own while lamp Y stays "
                "lit, and a second switch must turn both off. Determine where the"
                " two switches are placed.",
        "options": [
            "Both in the main wire, one on each side of the junction",
            "One in lamp X's branch and one in lamp Y's branch",
            "Both in lamp X's branch, one before the lamp and one after it",
            "One in lamp X's branch and one in the main wire from the cell",
        ],
        "correct_index": 3,
        "why": "A switch stops only the path it sits in, so the branch switch "
               "takes out lamp X alone and a switch in the main wire takes out "
               "every branch.",
    },
    {
        "id": "ks4-circuit-symbols-h22",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram is ruled neatly, but a lamp sits at a corner and "
                "one wire stops short of the cell. Evaluate the diagram.",
        "options": [
            "It is acceptable, as ruled lines are what a diagram is marked on",
            "It is acceptable, as a reader can see where the missing wire "
            "goes",
            "It is faulty: neat ruling does not mend an open loop or a "
            "corner",
            "It is faulty, as the lamp at the corner is its one mistake",
        ],
        "correct_index": 2,
        "why": "A diagram has to be both neat and right: the loop must close "
               "and each component must sit on a straight side where its two "
               "wires show.",
    },
    {
        "id": "ks4-circuit-symbols-h23",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One loop is drawn holding a cell, a circle with A, a "
                "rectangle with an arrow through it and a circle with a "
                "cross. Determine what this circuit is for.",
        "options": [
            "Measuring the current while the resistance in the loop is "
            "altered",
            "Measuring the potential difference across the lamp as it warms",
            "Comparing two lamps that are lit by one cell at the same time "
            "as each other",
            "Sounding an alarm when the current through the loop rises",
        ],
        "correct_index": 0,
        "why": "The circle with A reads the current, the arrow through the "
               "rectangle changes the resistance, and the circle with a "
               "cross is the lamp being studied.",
    },
    {
        "id": "ks4-circuit-symbols-h24",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-ammeter-in-lamp-branch",
        "text": "The diagram shows how a circuit is meant to be built, to measure"
                " the current in the lamp. A technician builds the ammeter into "
                "the other branch instead. Evaluate whether the reading is still "
                "the one wanted.",
        "options": [
            "Yes, as an ammeter reads the current of the circuit as a whole",
            "Yes, as the two branches are fed from one cell and must match",
            "No: it now reads the resistor's current, not the lamp's",
            "No: an ammeter placed on a branch cannot give any reading",
        ],
        "correct_index": 2,
        "why": "Parallel branches can carry different currents, so an ammeter "
               "reports whatever passes through the branch it has been built "
               "into — here the resistor's.",
    },
    {
        "id": "ks4-circuit-symbols-h25",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single loop holds a cell, a fuse, a switch and a lamp. "
                "Predict what the lamp does if the fuse melts.",
        "options": [
            "It goes out, as the melted fuse leaves a gap in the one loop",
            "It stays lit, as the fuse sits on a separate branch of its own",
            "It dims, as the melted fuse adds resistance to the loop",
            "It brightens, as the fuse no longer takes a share of the supply",
        ],
        "correct_index": 0,
        "why": "A fuse works by melting open, and in a single loop that gap "
               "stops the current through every component in the loop.",
    },
    {
        "id": "ks4-circuit-symbols-h26",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diagram shows only a cell and a lamp joined in a loop. "
                "Determine what must be added so the lamp can be dimmed and "
                "also switched off.",
        "options": [
            "A thermistor and a fuse, both drawn in the same loop",
            "A second cell and a diode, both drawn in the same loop",
            "A rectangle with two arrows pointing in, and a hinged lever",
            "A rectangle with an arrow through it, and a hinged lever",
        ],
        "correct_index": 3,
        "why": "The arrow through the rectangle is the variable resistor "
               "that dims the lamp, and the hinged lever is the switch that "
               "breaks the loop.",
    },
]
