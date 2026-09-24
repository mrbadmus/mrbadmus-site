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

⊕ MRB-352 run 2, batch 3 (the 174 flagged rows): 34 more rows that painted
a symbol or a circuit in words were rebuilt on the same id, band, tier and
bank_position — each now SHOWS its symbol or circuit as a figure and asks
about it. The alternating-supply circle and the buzzer are gone: neither is
on the AQA 8463 §4.2.1.1 list (p.24), and a "small rectangle inside a
circle" is AQA's LDR. Every symbol drawn or named here is on that list.

This file takes what the original twelve leave, and the weight follows the
CONTENT. The `easier` eight name single AQA symbols the baseline never asks
for — the voltmeter, the ammeter, the LDR, the fuse, the plain rectangle of a
fixed resistor, the LED, the closed switch — and the rule that components sit
on the lines. The real demand in this subtopic is not symbol recall at all:
it is READING a circuit — which components share a loop, how many paths the
current has, what one switch in one branch controls, what a meter in a branch
can and cannot read — and finding the fault in a diagram that has been drawn
wrongly. So `standard` and `harder` carry twenty-two rows each. Most show the
circuit; a few describe a physical set-up in words (a cell, a switch and a
lamp joined in one loop) and ask what it does, never what a drawing looks
like.

Meter resistance, Ohm's law, the mains and the behaviour of an LED under
reverse bias beyond "it does not conduct" belong to other leaves and are
absent.
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
        "figure": "ks4-fig-circuit-symbol-voltmeter",
        "text": "Name the component that the circuit symbol in the diagram "
                "represents.",
        "options": [
            "A voltmeter, which measures the potential difference across a "
            "component",
            "An ammeter, which measures the current through a component",
            "A lamp, which gives out light when a current passes through it",
            "A variable resistor, whose resistance can be changed",
        ],
        "correct_index": 0,
        "why": "A circle with the letter V inside it is the voltmeter symbol, "
               "and V stands for volts, the unit of potential difference. An "
               "ammeter is a circle with an A, and a lamp is a circle with a "
               "cross.",
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
        "figure": "ks4-fig-circuit-symbol-ldr",
        "text": "Look at the circuit symbol in the diagram. Which component "
                "is it?",
        "options": [
            "A thermistor, whose resistance changes with temperature",
            "A light-dependent resistor (LDR), whose resistance changes with "
            "light intensity",
            "A light-emitting diode (LED), which gives out light when a "
            "current passes through it",
            "A lamp, which gives out light when a current passes through it",
        ],
        "correct_index": 1,
        "why": "The small rectangle is a resistor, and the two arrows "
               "pointing IN towards it show light falling on it. This is the "
               "LDR, whose resistance decreases as light intensity increases. "
               "An LED's arrows point out, away from it. A thermistor has a "
               "diagonal line with a short tail and no arrows.",
    },
    {
        "id": "ks4-circuit-symbols-e08",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-symbol-fuse",
        "text": "Which component is shown by the circuit symbol in the "
                "diagram?",
        "options": [
            "A cell, which provides the potential difference in a circuit",
            "A resistor, whose resistance stays at one value",
            "A closed switch, which completes the circuit",
            "A fuse, which melts and breaks the circuit if the current "
            "becomes too large",
        ],
        "correct_index": 3,
        "why": "A rectangle with the wire running straight through it along "
               "its length is the fuse. The thin wire inside it melts and "
               "breaks the circuit if the current becomes too large. A plain "
               "rectangle with no line through it is a resistor.",
    },
    {
        "id": "ks4-circuit-symbols-e09",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-symbol-resistor",
        "text": "The diagram shows one circuit symbol. Identify the component "
                "it stands for.",
        "options": [
            "A variable resistor, whose resistance can be changed by hand",
            "A fixed resistor, whose resistance stays at one value",
            "A thermistor, whose resistance falls as it becomes warmer",
            "An LDR, whose resistance falls as the light on it gets brighter",
        ],
        "correct_index": 1,
        "why": "A plain rectangle with no other mark is the fixed resistor. A "
               "variable resistor adds a diagonal arrow through it, a "
               "thermistor adds a diagonal line with a short tail, and an LDR "
               "is drawn inside a circle with two arrows pointing in.",
    },
    {
        "id": "ks4-circuit-symbols-e10",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-symbol-led",
        "text": "Which component does the circuit symbol shown in the diagram "
                "stand for?",
        "options": [
            "A light-emitting diode, which gives out light as it conducts",
            "A diode that has been damaged and now conducts in both ways",
            "A diode fitted with a fuse to guard it from a large current",
            "A light-dependent resistor, which responds to the light on it",
        ],
        "correct_index": 0,
        "why": "The triangle and bar inside the circle are a diode. The two "
               "arrows pointing OUT show light leaving it, so this is a "
               "light-emitting diode. An LDR's arrows point in, towards a "
               "small rectangle.",
    },
    {
        "id": "ks4-circuit-symbols-e11",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-symbol-switch-closed",
        "text": "Identify the component drawn in the diagram.",
        "options": [
            "An open switch, which leaves a gap so there is no current",
            "A fuse, which melts if the current becomes too large",
            "A resistor, whose resistance stays at one value",
            "A closed switch, which completes the circuit so there can be a "
            "current",
        ],
        "correct_index": 3,
        "why": "The lever runs from one contact to the other and touches "
               "both, so there is no gap in the wire. This is a closed "
               "switch, and it completes the circuit. An open switch's lever "
               "is angled away from the second contact and leaves a gap.",
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
        "why": "The symbol drawn where the bulb should be is an LDR — its "
               "arrows point in, because it responds to light rather than "
               "giving it out. A torch bulb is a lamp. The battery, switch and "
               "single loop are right.",
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
        "figure": "ks4-fig-symbol-panel-cell-fuse-battery-resistor",
        "text": "A torch runs from two cells joined in series. The diagram "
                "shows four circuit symbols. Which one should be drawn for "
                "the torch's supply?",
        "options": [
            "P",
            "Q",
            "R",
            "S",
        ],
        "correct_index": 2,
        "why": "R is a battery: two cells joined by a dashed line, which is "
               "how two or more cells in series are drawn. P is a single "
               "cell, Q is a fuse and S is a resistor.",
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
        "figure": "ks4-fig-circuit-voltmeter-in-loop-lamp",
        "text": "A student draws this circuit to measure the current in the "
                "lamp. Explain the error.",
        "options": [
            "The meter should be drawn after the lamp, not before it",
            "The lamp should be drawn as a plain rectangle, because it has a "
            "resistance",
            "The meter is a voltmeter; current is measured with an ammeter, "
            "connected in series",
            "Nothing is wrong: a meter in the loop measures the current "
            "whatever letter it carries",
        ],
        "correct_index": 2,
        "why": "The circle with V is a voltmeter, which measures potential "
               "difference and is connected in parallel across a component. "
               "Current is measured with an ammeter (a circle with A) "
               "connected in series, in the same loop as the lamp. The order "
               "of components in a series loop does not matter.",
    },
    {
        "id": "ks4-circuit-symbols-s14",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-wire-short-of-cell",
        "text": "The diagram shows a circuit a student has drawn. A "
                "technician builds it exactly as drawn. Predict what happens.",
        "options": [
            "Nothing happens, as a broken loop can never carry a current",
            "The lamp lights dimly, as the current crosses the small gap",
            "The lamp lights fully, as the missing piece is only on paper",
            "The lamp flickers, as current reaches it along the other wire "
            "and then falls away",
        ],
        "correct_index": 0,
        "why": "A current needs a complete loop. The gap in the wire means "
               "the circuit is not closed, so there is no current anywhere in "
               "it and the lamp stays off.",
    },
    {
        "id": "ks4-circuit-symbols-s15",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-symbol-panel-resistor-fuse",
        "text": "The diagram shows two circuit symbols, P and Q. Name each "
                "component.",
        "options": [
            "P is a fuse and Q is a fixed resistor",
            "Both are resistors, and Q is the one with the larger resistance",
            "P is a switch and Q is a variable resistor",
            "P is a fixed resistor and Q is a fuse",
        ],
        "correct_index": 3,
        "why": "The plain rectangle, P, is a fixed resistor. The rectangle "
               "with the wire running through it along its length, Q, is a "
               "fuse.",
    },
    {
        "id": "ks4-circuit-symbols-s16",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-cell-diode-reversed-lamp",
        "text": "The diagram shows a circuit. The lamp does not light. "
                "Explain why.",
        "options": [
            "The lamp comes after the diode, so the current is used up before "
            "it reaches the lamp",
            "The diode is the wrong way round, so its resistance is very high "
            "and there is almost no current",
            "A diode only works with an alternating supply, so a cell cannot "
            "light the lamp",
            "The cell's potential difference is shared, so the lamp gets too "
            "little to light",
        ],
        "correct_index": 1,
        "why": "A diode lets current flow in one direction only, the way its "
               "triangle points, and has a very high resistance in the "
               "reverse direction. The current from the cell leaves its "
               "positive (+) terminal. Here the diode's triangle points back "
               "against that current, so almost no current flows round the "
               "loop.",
    },
    {
        "id": "ks4-circuit-symbols-s17",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-cell-resistor-lamp",
        "text": "The diagram shows a circuit for a lamp. The lamp's "
                "brightness must be adjustable while the circuit is working. "
                "Which change is needed?",
        "options": [
            "Replace the resistor with a variable resistor",
            "Replace the resistor with a thermistor",
            "Replace the resistor with an LDR",
            "Add a second resistor in series with the first",
        ],
        "correct_index": 0,
        "why": "A variable resistor's resistance can be changed by hand while "
               "the circuit is working. That changes the current, and so the "
               "lamp's brightness. A thermistor or an LDR changes only with "
               "temperature or light. A second fixed resistor would dim the "
               "lamp by one fixed amount.",
    },
    {
        "id": "ks4-circuit-symbols-s18",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-cell-led-resistor",
        "text": "In the circuit shown, the LED is lit. The cell is then "
                "turned round. Predict what happens to the LED.",
        "options": [
            "The LED stays lit, because a cell pushes current either way round",
            "The LED gets brighter, because the current now reaches it from "
            "the other side first",
            "The LED goes out, because the current would now have to pass "
            "through it the wrong way",
            "The LED flashes on and off, because the current keeps changing "
            "direction",
        ],
        "correct_index": 2,
        "why": "An LED is a diode: current flows through it in one direction "
               "only, and it has a very high resistance the other way. "
               "Turning the cell round reverses the direction of the current, "
               "so almost no current flows and the LED goes out.",
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
        "why": "P is a battery, R a closed switch and S a lamp. Q is an LDR, "
               "which this circuit does not need.",
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
        "figure": "ks4-fig-circuit-fuse-in-supply-wire",
        "text": "The diagram shows a circuit containing a cell, a lamp and "
                "one other component. What does that other component do?",
        "options": [
            "It stores charge, letting it go when the current drops too low",
            "It holds the current steady at the value the supply gives",
            "It melts and breaks the circuit if the current becomes too big",
            "It lowers the current to a safe value each time that this is "
            "needed",
        ],
        "correct_index": 2,
        "why": "The other component is a fuse, drawn as a rectangle with the "
               "wire running through it along its length. It is a thin wire "
               "that melts and opens the circuit once the current through it "
               "is too large.",
    },
    {
        "id": "ks4-circuit-symbols-s22",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-symbol-panel-ldr-resistor-varres-thermistor",
        "text": "A circuit needs a component that senses changes in "
                "temperature. The diagram shows four circuit symbols. Which "
                "one should be drawn?",
        "options": [
            "W",
            "X",
            "Y",
            "Z",
        ],
        "correct_index": 3,
        "why": "Z is a thermistor: a rectangle with a diagonal line that ends "
               "in a short horizontal tail. Its resistance decreases as its "
               "temperature increases, so it is used to sense temperature. W "
               "is an LDR, which senses light. X is a fixed resistor and Y a "
               "variable resistor.",
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
            "The meter in the main loop measures the potential difference "
            "across the cell; the other measures the current in the resistor",
            "The meter in the main loop measures the current; the other "
            "measures the potential difference across the resistor",
            "Both meters measure the current, one before the resistor and one"
            " across it",
            "Both meters measure the potential difference, one across the "
            "cell and one across the resistor",
        ],
        "correct_index": 1,
        "why": "The circle with A is an ammeter, connected in series in the "
               "main loop, so it measures the current. The circle with V is a "
               "voltmeter, connected in parallel across the resistor, so it "
               "measures the potential difference across the resistor.",
    },
    {
        "id": "ks4-circuit-symbols-s24",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-cell-closed-switch-lamp",
        "text": "A circuit diagram must show the lamp switched off. A pupil's "
                "drawing is shown. Explain the error.",
        "options": [
            "Nothing is wrong: a switch drawn like this is off",
            "A switched-off circuit is shown by leaving the switch out of the "
            "diagram",
            "The cell should be drawn the other way round to stop the current",
            "The switch is drawn closed; it must be drawn open, leaving a gap "
            "in the circuit",
        ],
        "correct_index": 3,
        "why": "The switch in the drawing has its lever touching both "
               "contacts. That is a closed switch, which completes the "
               "circuit, so the lamp would be lit. To show the lamp off, the "
               "switch must be drawn open, so there is a gap and no current.",
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
        "figure": "ks4-fig-circuit-cell-resistor-lamp",
        "text": "A circuit was meant to include a fuse to protect it. The "
                "diagram shows the circuit as it was drawn and then built. "
                "Predict what happens if the current becomes far too large.",
        "options": [
            "The resistor melts first, as a resistor gives way before a fuse "
            "would",
            "Nothing breaks the circuit, as a resistor is not designed to "
            "melt open",
            "The current is cut off, as a resistor opens the circuit above "
            "its rating",
            "The cell stops supplying current, as the diagram shows no fuse",
        ],
        "correct_index": 1,
        "why": "The component drawn is a plain rectangle, which is a "
               "resistor, not a fuse (a fuse has the wire drawn through it). "
               "A resistor is made to carry current, not to melt, so the "
               "circuit as built has no protection against a very large "
               "current.",
    },
    {
        "id": "ks4-circuit-symbols-h07",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-meters-swapped-lamp",
        "text": "A student draws this circuit to measure the current in the "
                "lamp and the potential difference across it. Evaluate the "
                "diagram.",
        "options": [
            "It is wrong: the meters are swapped — the ammeter belongs in "
            "series and the voltmeter across the lamp",
            "It is correct, as each meter is joined to the lamp and so reads "
            "the lamp's value",
            "Only the voltmeter is wrong, as an ammeter may be drawn either "
            "in series or in parallel",
            "Only the ammeter is wrong, as a voltmeter may be drawn either in "
            "series or in parallel",
        ],
        "correct_index": 0,
        "why": "An ammeter is connected in series, so the current passes "
               "through it. A voltmeter is connected in parallel, across the "
               "component. Here the voltmeter is in the loop and the ammeter "
               "bridges the lamp, so both are in the wrong place.",
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
        "figure": "ks4-fig-circuit-cell-closed-switch-lamp",
        "text": "A torch holds two cells joined in series, a switch and a "
                "bulb. A pupil draws its circuit as shown. Evaluate the "
                "diagram.",
        "options": [
            "It is correct, as one cell symbol stands for a supply of any size",
            "It is correct, as a circuit diagram does not need to show how "
            "many cells there are",
            "It is wrong: the supply is drawn as one cell, but two cells in "
            "series are drawn as a battery",
            "It is wrong: the switch must be drawn open, as a torch is "
            "normally off",
        ],
        "correct_index": 2,
        "why": "The supply drawn is a single cell, one long line and one "
               "short line. Two cells joined in series make a battery, drawn "
               "as two cells joined by a dashed line. The switch may be drawn "
               "open or closed; the diagram just shows one state.",
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
        "figure": "ks4-fig-circuit-two-lamp-branches-open-switch-x",
        "text": "The diagram shows a circuit. Determine which lamps are lit.",
        "options": [
            "Neither lamp, as an open switch anywhere stops the whole circuit",
            "Both lamps, as the current reaches lamp X by the other branch",
            "Only lamp Y: its own branch is still a complete path",
            "Only lamp X, as the open switch leaves more current for it",
        ],
        "correct_index": 2,
        "why": "Each branch is a separate path to the cell. The open switch "
               "breaks lamp X's branch only, so lamp Y's branch is still a "
               "complete path and Y stays lit.",
    },
    {
        "id": "ks4-circuit-symbols-h12",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-symbol-panel-resistor-varres",
        "text": "A model railway controller must let its user change the "
                "current to the track while the train runs. The diagram shows "
                "two circuit symbols, P and Q. Which one should be used?",
        "options": [
            "P, as its resistance is chosen before the circuit is built",
            "Q, as its resistance can be changed while the circuit is working",
            "Either, as both have a resistance that limits the current",
            "Neither, as the current to the track can only be changed at the "
            "supply",
        ],
        "correct_index": 1,
        "why": "Q is a variable resistor, a rectangle with a diagonal arrow "
               "through it. Its resistance can be changed while the circuit "
               "is working, which changes the current. P is a fixed resistor, "
               "whose resistance stays at one value.",
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
        "figure": "ks4-fig-circuit-cell-switch-two-lamps-loop",
        "text": "The diagram shows a circuit. One of the lamps fails and "
                "stops conducting. Determine what happens to the other lamp.",
        "options": [
            "It stays lit, as it still has the cell's potential difference "
            "across it",
            "It goes out, as the lamps are in series and the only path is now "
            "broken",
            "It gets brighter, as it now receives all of the current",
            "It stays lit but dimmer, as the current now reaches it along one "
            "wire only",
        ],
        "correct_index": 1,
        "why": "The lamps are in series: one loop, one path for the current. "
               "A failed lamp breaks that path, so the current everywhere in "
               "the loop falls to zero and the other lamp goes out.",
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
        "figure": "ks4-fig-circuit-lamp-x-branch-varres-lamp-y",
        "text": "The diagram shows a circuit. Determine which lamp can be "
                "dimmed.",
        "options": [
            "Both lamps, as both branches are fed by the same cell",
            "Lamp Y only, as the variable resistor is in the same branch as it",
            "Lamp X only, as the variable resistor leaves more current for it",
            "Neither lamp, as brightness can only be changed at the cell",
        ],
        "correct_index": 1,
        "why": "A variable resistor changes the current in the branch it is "
               "in. It shares a branch with lamp Y, so it can dim Y. Lamp X's "
               "branch has the cell's full potential difference across it "
               "whatever the variable resistor is set to, so X is unaffected.",
    },
    {
        "id": "ks4-circuit-symbols-h18",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-cell-lamp",
        "text": "The diagram shows a circuit. A pupil complains that the lamp "
                "cannot be turned off. Which component must be added?",
        "options": [
            "An ammeter, to show when there is a current",
            "A fuse, to break the circuit if the current is too large",
            "A second cell, in series with the first",
            "A switch, to open and close the circuit",
        ],
        "correct_index": 3,
        "why": "A switch is the component that opens and closes the circuit. "
               "Opening it leaves a gap, so there is no current and the lamp "
               "goes off. The circuit shown has only a cell and a lamp, so it "
               "cannot be turned off.",
    },
    {
        "id": "ks4-circuit-symbols-h19",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-cell-ammeter-thermistor",
        "text": "A pupil plans to measure how the current through a sensor "
                "changes as the light level changes. Their circuit diagram is "
                "shown. Suggest the correction.",
        "options": [
            "Replace the sensor drawn with a variable resistor, which the "
            "light level can set",
            "Replace the sensor drawn with an LDR, as the sensor drawn "
            "responds to temperature, not light",
            "Replace the ammeter with a voltmeter, as current cannot be "
            "measured in series",
            "Leave it as it is, as the sensor drawn is already the "
            "light-dependent one",
        ],
        "correct_index": 1,
        "why": "The sensor drawn is a thermistor: a rectangle with a diagonal "
               "line ending in a short tail. Its resistance changes with "
               "temperature. A sensor for light is an LDR, whose resistance "
               "decreases as light intensity increases. The ammeter is "
               "correctly placed in series.",
    },
    {
        "id": "ks4-circuit-symbols-h20",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-cell-two-switches-one-open-lamp",
        "text": "The diagram shows a circuit. Determine what the lamp does.",
        "options": [
            "It lights fully, as one closed switch completes the loop",
            "It lights dimly, as only one of the two switches is open",
            "It stays off, as the open switch leaves a gap in the only path",
            "It flashes, as the current passes the open switch in bursts",
        ],
        "correct_index": 2,
        "why": "In a single loop the current has only one path. One switch is "
               "open, which leaves a gap in that path, so there is no current "
               "and the lamp stays off. Every switch in the loop has to be "
               "closed before the lamp can light.",
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
        "figure": "ks4-fig-circuit-main-switch-two-lamp-branches",
        "text": "A pupil's circuit is meant to let lamp X be switched off "
                "while lamp Y stays lit. Their diagram is shown. Evaluate the "
                "diagram.",
        "options": [
            "It is acceptable, as the two lamps are on separate branches",
            "It is acceptable, as opening the switch turns lamp X off",
            "It is faulty: the switch is in the main wire, so it turns both "
            "lamps off together",
            "It is faulty, as lamps on separate branches cannot be switched "
            "at all",
        ],
        "correct_index": 2,
        "why": "The switch is in the main wire, which all of the current "
               "passes through, so opening it turns off both lamps at once. "
               "To switch lamp X off on its own, the switch must be in lamp "
               "X's branch.",
    },
    {
        "id": "ks4-circuit-symbols-h23",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-circuit-single-loop-four-components",
        "text": "The diagram shows a circuit. Determine what this circuit "
                "could be used for.",
        "options": [
            "Measuring the current while the resistance in the loop is altered",
            "Measuring the potential difference across the lamp as it warms",
            "Comparing the brightness of two lamps lit by the same cell",
            "Sounding an alarm when the current through the loop rises",
        ],
        "correct_index": 0,
        "why": "The ammeter (the circle with A) reads the current. The "
               "variable resistor (the rectangle with an arrow) changes the "
               "resistance in the loop. The lamp is the component being "
               "studied. There is no voltmeter, only one lamp and nothing "
               "that makes a sound.",
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
        "figure": "ks4-fig-circuit-cell-lamp",
        "text": "The diagram shows a circuit. Determine what must be added so "
                "that the lamp can be dimmed and also switched off.",
        "options": [
            "A thermistor and a fuse",
            "A second cell and a diode",
            "An LDR and a switch",
            "A variable resistor and a switch",
        ],
        "correct_index": 3,
        "why": "A variable resistor lets the user change the resistance, and "
               "so the current, which dims the lamp. A switch opens the "
               "circuit to turn the lamp off. A thermistor or an LDR changes "
               "only with temperature or light, not when the user chooses.",
    },
]
