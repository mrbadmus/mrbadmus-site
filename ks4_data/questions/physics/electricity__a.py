"""Physics · Electricity — part A: symbols, charge and current, Ohm's law,
resistors, series and parallel circuits, and dc vs ac.

The first six subtopics of AQA 8463 §6.2 (spec points 6.2.1.1 to 6.2.3.1).
Part B (`electricity__b.py`) carries the remaining six.

Every one of these subtopics is BASE — tier 'foundation', triple_only False —
so a Foundation Combined class sits all of them, and nothing here reaches for
Higher-only content.

Where the distractors come from. Each subtopic's declared common mistake is
worked hard: meters swapped round (ammeter in series, voltmeter in parallel);
minutes left unconverted in Q = I t; R written as V × I instead of V ÷ I;
thermistor and LDR resistance assumed to RISE rather than fall; parallel total
resistance assumed to be the sum rather than less than the smallest branch;
and 230 V read as the peak mains pd rather than the effective value. The
calculation distractors are the arithmetic each of those errors actually
produces, not noise.

The lesson pages' own "Test yourself" items are a different pool and none of
them is restated here — in particular the 180 C / 2 min current, the 6 Ω at
3 A pd, the constant series ammeter reading, the thermistor-warms and
LDR-lit behaviours, the 6 V parallel lamps, the household-wiring question,
the flat dc oscilloscope line and the 50 Hz / 230 V pairing are all avoided,
and their spec content is reached from a different direction instead.
"""

TOPIC = "electricity"
SUBJECT = "physics"

QUESTIONS = [
    # ── circuit-symbols ─────────────────────────────────────────────────
    {
        "id": "ks4-circuit-symbols-e01",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which component is drawn as a rectangle with an arrow "
                "through it?",
        "options": [
            "A fixed resistor, whose resistance cannot be changed",
            "A thermistor, whose resistance depends on temperature",
            "A variable resistor, whose resistance can be changed",
            "A fuse, which melts if the current becomes too large",
        ],
        "correct_index": 2,
        "why": "The arrow struck through the resistor rectangle is the "
               "standard way of showing that the resistance can be varied.",
    },
    {
        "id": "ks4-circuit-symbols-e02",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which description matches the standard symbol for an "
                "open switch?",
        "options": [
            "A break in the wire, with a short line hinged at one end "
            "and lifted clear of the contact",
            "A circle with the capital letter S inside it",
            "Two parallel lines of the same length with a gap between "
            "them",
            "A rectangle with a gap in the middle of it",
        ],
        "correct_index": 0,
        "why": "An open switch is drawn as a gap in the wire with the "
               "hinged lever raised; closing the switch lowers the "
               "lever and completes the circuit.",
    },
    {
        "id": "ks4-circuit-symbols-e03",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why circuit diagrams are drawn using standard "
                "symbols.",
        "options": [
            "Because the symbols show the true size, shape and colour of "
            "each component",
            "Because a circuit will only work if its diagram has been drawn "
            "correctly first",
            "Because standard symbols reduce the resistance of the wires in "
            "the circuit",
            "Because any engineer anywhere can then read and build the same "
            "circuit",
        ],
        "correct_index": 3,
        "why": "A circuit diagram is a schematic written in a shared visual "
               "language, so the same drawing can be built in any laboratory "
               "in the world.",
    },
    {
        "id": "ks4-circuit-symbols-e04",
        "subtopic_slug": "circuit-symbols",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the symbol for a battery differs from the "
                "symbol for a single cell.",
        "options": [
            "A battery is drawn as a circle with a sine wave inside it",
            "A battery is two or more cell symbols drawn in series",
            "A battery is drawn with two long lines and no short line",
            "A battery is a cell symbol with an arrow drawn through it",
        ],
        "correct_index": 1,
        "why": "A battery is simply several cells joined in series, so its "
               "symbol repeats the long-line, short-line cell symbol.",
    },
    {
        "id": "ks4-circuit-symbols-s01",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student connects an ammeter in parallel across a lamp "
                "instead of in series with it. Suggest what will happen.",
        "options": [
            "An ammeter has a very low resistance, so it short-circuits the "
            "lamp and a very large current flows",
            "The ammeter will display the potential difference across the "
            "lamp instead of the current through it",
            "The ammeter will read the current correctly, but the lamp will "
            "glow more brightly than before",
            "The ammeter will read zero, because no current can enter a "
            "meter that is connected sideways",
        ],
        "correct_index": 0,
        "why": "An ammeter is built with almost no resistance so that it does "
               "not alter the circuit; placed across a component it offers a "
               "nearly resistance-free path and the current becomes "
               "dangerously large.",
    },
    {
        "id": "ks4-circuit-symbols-s02",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An outdoor lamp must switch itself on when it gets dark. "
                "Which symbol should be drawn for the sensing component?",
        "options": [
            "A resistor rectangle with a diagonal line drawn through it",
            "A resistor rectangle with an arrow drawn through it",
            "A triangle pointing towards a straight line",
            "A resistor rectangle with two arrows pointing in towards it",
        ],
        "correct_index": 3,
        "why": "Arrows pointing in towards the resistor show light falling on "
               "it, which is the light-dependent resistor — the component "
               "whose resistance responds to brightness.",
    },
    {
        "id": "ks4-circuit-symbols-s03",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A circuit diagram shows a cell, a closed switch and two "
                "lamps all in one loop. Describe the change needed so that "
                "one lamp can be switched off while the other stays lit.",
        "options": [
            "Add a second cell in series with the first one",
            "Redraw the two lamps on separate branches, each with its own "
            "switch",
            "Move the switch so that it sits between the two lamps in the "
            "same loop",
            "Replace one of the lamps with a diode so that current reaches "
            "only the other",
        ],
        "correct_index": 1,
        "why": "Only components on separate parallel branches can be switched "
               "independently — in a single loop, opening any switch breaks "
               "the one path and stops everything.",
    },
    {
        "id": "ks4-circuit-symbols-s04",
        "subtopic_slug": "circuit-symbols",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement about drawing a circuit diagram is correct?",
        "options": [
            "The wires must be drawn to scale so their real lengths can be "
            "measured from the diagram",
            "Components should be placed on the corners so that the "
            "connecting wires stay straight",
            "It is a schematic, so positions on paper need not match the "
            "layout on the bench",
            "Curved wires should be used wherever two components are a long "
            "way apart",
        ],
        "correct_index": 2,
        "why": "A circuit diagram records how components are connected, not "
               "where they sit, so one neat ruled rectangle can represent "
               "any physical arrangement.",
    },
    {
        "id": "ks4-circuit-symbols-h01",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student builds a single loop containing a cell, a switch, "
                "a resistor and an LED. With the switch closed the LED does "
                "not light. When the two connections to the cell are swapped "
                "over, it lights. Explain what was wrong at first.",
        "options": [
            "The cell had gone flat, and reversing its connections recharged "
            "it enough to light the LED",
            "The resistor was limiting the current too severely until the "
            "cell was turned round",
            "The switch was still open, and swapping the cell connections "
            "closed it again",
            "The LED was connected the wrong way round, and a diode passes "
            "current one way only",
        ],
        "correct_index": 3,
        "why": "An LED is a diode: it conducts only when the current flows "
               "the way its triangle points, and blocks it almost completely "
               "in the other direction.",
    },
    {
        "id": "ks4-circuit-symbols-h02",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students draw the sensing part of a fire alarm. Student "
                "A draws a resistor rectangle with a diagonal line through "
                "it; student B draws a resistor rectangle with two arrows "
                "pointing in towards it. Evaluate which student is correct.",
        "options": [
            "Student B, because the arrows show heat being absorbed by the "
            "resistor",
            "Student A, because a diagonal line through the resistor is the "
            "thermistor symbol",
            "Both, because the two symbols are alternative ways of drawing "
            "one component",
            "Neither, because a fire alarm must use a variable resistor to "
            "set the alarm level",
        ],
        "correct_index": 1,
        "why": "A fire alarm senses temperature, and the thermistor — the "
               "resistor rectangle with a line struck through it — is the "
               "component whose resistance changes with temperature.",
    },
    {
        "id": "ks4-circuit-symbols-h03",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an ammeter is made with a very low resistance "
                "while a voltmeter is made with a very high resistance.",
        "options": [
            "Both meters are made with a very low resistance so that neither "
            "of them wastes energy as heat",
            "The ammeter sits in parallel with the component, so a low "
            "resistance lets more of the current pass into it",
            "In series a low resistance barely reduces the current; in "
            "parallel a high resistance draws almost none away",
            "The high resistance of the voltmeter is what creates the "
            "potential difference that the meter then displays",
        ],
        "correct_index": 2,
        "why": "A meter must not change what it is measuring: in series the "
               "ammeter must add almost no resistance, and in parallel the "
               "voltmeter must take almost no current.",
    },
    {
        "id": "ks4-circuit-symbols-h04",
        "subtopic_slug": "circuit-symbols",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A circuit has a battery, a switch, and two branches — one "
                "holding a lamp and one holding a motor. An ammeter must "
                "read the total current supplied by the battery. Determine "
                "where it should be drawn.",
        "options": [
            "In the main wire between the battery and the junction, so all "
            "the current passes through it",
            "In the lamp branch only, because the lamp draws the larger of "
            "the two branch currents",
            "Across the two terminals of the battery, connected in parallel "
            "with the supply itself",
            "In each of the two branches, with the two readings then "
            "subtracted from one another to give the total",
        ],
        "correct_index": 0,
        "why": "All the charge leaving the battery passes along the main wire "
               "before the branches divide it, so an ammeter there reads the "
               "total current.",
    },

    # ── electrical-charge-current ───────────────────────────────────────
    {
        "id": "ks4-electrical-charge-current-e01",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric motor in a toy carries a current of 1.5 A "
                "for 30 s. Calculate the charge that passes through the "
                "motor.",
        "options": [
            "20 C",
            "45 C",
            "1.5 C",
            "0.050 C",
        ],
        "correct_index": 1,
        "why": "Q = I × t = 1.5 × 30 = 45 C — charge flow is the "
               "current multiplied by the time in seconds.",
    },
    {
        "id": "ks4-electrical-charge-current-e02",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by an electric current.",
        "options": [
            "The energy transferred by each coulomb of charge that passes",
            "The opposition of a component to the flow of charge",
            "The number of electrons stored inside a battery",
            "The rate of flow of electric charge",
        ],
        "correct_index": 3,
        "why": "Current is charge per second: one ampere means one coulomb of "
               "charge passes a point every second.",
    },
    {
        "id": "ks4-electrical-charge-current-e03",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a copper wire, which particles carry the charge?",
        "options": [
            "Free electrons",
            "Positive metal ions moving towards the negative terminal",
            "Protons that leave the positive terminal of the cell",
            "Ions, as they do in a conducting solution",
        ],
        "correct_index": 0,
        "why": "A metal holds a sea of free electrons that drift through a "
               "fixed lattice of positive ions; it is only in solutions that "
               "ions carry the charge.",
    },
    {
        "id": "ks4-electrical-charge-current-e04",
        "subtopic_slug": "electrical-charge-current",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two conditions needed for a current to flow in a "
                "circuit.",
        "options": [
            "A complete circuit and at least one resistor to control the "
            "current",
            "A source of potential difference and an ammeter to register the "
            "flow",
            "A complete, unbroken circuit and a source of potential "
            "difference",
            "A closed circuit and an alternating rather than a direct supply",
        ],
        "correct_index": 2,
        "why": "Charge needs an unbroken conducting path to travel round and "
               "something to push it, so a closed loop and a source of "
               "potential difference are both required.",
    },
    {
        "id": "ks4-electrical-charge-current-s01",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A current of 0.40 A flows through an LED. Calculate the time "
                "taken for 12 C of charge to pass through it.",
        "options": ["4.8 s", "3.0 s", "48 s", "30 s"],
        "correct_index": 3,
        "why": "Rearranging Q = I × t gives t = Q ÷ I = 12 ÷ 0.40 = 30 s.",
    },
    {
        "id": "ks4-electrical-charge-current-s02",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A parallel circuit draws 1.2 A from the supply. One branch "
                "carries 0.50 A and a second carries 0.30 A. Calculate the "
                "current in the third branch.",
        "options": ["1.2 A", "0.80 A", "0.40 A", "2.0 A"],
        "correct_index": 2,
        "why": "The branch currents add to give the supply current, so the "
               "third branch carries 1.2 − 0.50 − 0.30 = 0.40 A.",
    },
    {
        "id": "ks4-electrical-charge-current-s03",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an ammeter reads the same current at every point "
                "in a series circuit.",
        "options": [
            "Charge is neither created nor used up, and there is only one "
            "path for it to take",
            "The components share the current out equally between them as it "
            "passes through",
            "Each component uses up some current, which the battery then "
            "immediately replaces",
            "The resistances happen to be equal, so the current has no "
            "reason to change value",
        ],
        "correct_index": 0,
        "why": "Charge cannot pile up or disappear in a single loop, so the "
               "same number of coulombs pass every point each second.",
    },
    {
        "id": "ks4-electrical-charge-current-s04",
        "subtopic_slug": "electrical-charge-current",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the current in the wires of a torch flows "
                "from the negative terminal of the cell round to the "
                "positive terminal. Determine whether this is correct.",
        "options": [
            "It is wrong: electrons in a metal drift from the positive "
            "terminal to the negative one",
            "The electrons do move that way, but conventional current is "
            "defined from positive to negative",
            "It is right, and conventional current is defined in exactly the "
            "same direction as this",
            "It is wrong: in a metal the charge is carried by positive ions "
            "leaving the positive terminal",
        ],
        "correct_index": 1,
        "why": "Conventional current was defined as positive-to-negative "
               "before the electron was discovered, so it runs opposite to "
               "the real electron flow in a metal.",
    },
    {
        "id": "ks4-electrical-charge-current-h01",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rechargeable cell is rated at 2000 mA h, meaning it can "
                "supply a current of 2000 mA for one hour. Calculate the "
                "total charge it can deliver.",
        "options": ["2000 C", "120 C", "7200 C", "7.2 C"],
        "correct_index": 2,
        "why": "2000 mA is 2.0 A and one hour is 3600 s, so Q = I × t = "
               "2.0 × 3600 = 7200 C.",
    },
    {
        "id": "ks4-electrical-charge-current-h02",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 3.0 Ω branch and a 6.0 Ω branch are connected in parallel "
                "across a 6.0 V supply. Determine the charge that leaves the "
                "battery in 20 s.",
        "options": ["60 C", "40 C", "20 C", "13 C"],
        "correct_index": 0,
        "why": "Each branch has the full 6.0 V across it, giving 2.0 A and "
               "1.0 A, so 3.0 A leaves the battery and Q = 3.0 × 20 = 60 C.",
    },
    {
        "id": "ks4-electrical-charge-current-h03",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical lamps are connected to the same cell, first "
                "in series and then in parallel. Compare the charge that "
                "flows through the cell in one minute in each case.",
        "options": [
            "The same charge flows, because the cell always supplies the "
            "same charge each minute",
            "More flows in the parallel circuit, because its lower total "
            "resistance gives a larger current",
            "More flows in the series circuit, because all of the charge "
            "must pass through both lamps",
            "Less flows in the parallel circuit, because the current is "
            "split between the two branches",
        ],
        "correct_index": 1,
        "why": "Two paths are easier for charge than one, so the total "
               "resistance falls, the current from the cell rises, and more "
               "coulombs pass in the minute.",
    },
    {
        "id": "ks4-electrical-charge-current-h04",
        "subtopic_slug": "electrical-charge-current",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ammeter in the main wire of a parallel circuit holding "
                "three identical lamps reads 0.60 A. One lamp is removed and "
                "its branch left open. Predict the new reading.",
        "options": [
            "0.60 A, because the current in the main wire is fixed by the "
            "battery",
            "0.90 A, because removing a branch raises the current in the "
            "ones that remain",
            "0.20 A, because the current now splits between the two lamps "
            "that are left",
            "0.40 A, because the two remaining branches each still carry "
            "0.20 A",
        ],
        "correct_index": 3,
        "why": "Each identical branch carries 0.20 A and each keeps the full "
               "supply pd, so removing one simply takes its 0.20 A out of "
               "the total.",
    },

    # ── current-resistance-pd ───────────────────────────────────────────
    {
        "id": "ks4-current-resistance-pd-e01",
        "subtopic_slug": "current-resistance-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 15 V supply drives a current of 5.0 A through a "
                "resistor. Calculate its resistance.",
        "options": [
            "75 Ω",
            "10 Ω",
            "0.33 Ω",
            "3.0 Ω",
        ],
        "correct_index": 3,
        "why": "Rearranging V = I × R gives R = V ÷ I = 15 ÷ 5.0 = 3.0 "
               "Ω — resistance is pd divided by current, never pd times "
               "current.",
    },
    {
        "id": "ks4-current-resistance-pd-e02",
        "subtopic_slug": "current-resistance-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by potential difference.",
        "options": [
            "The rate at which charge flows past a point in a circuit",
            "The energy transferred by each coulomb of charge that passes",
            "The opposition of a component to the flow of charge",
            "The total energy stored inside a battery before it is used",
        ],
        "correct_index": 1,
        "why": "One volt is one joule per coulomb, so potential difference "
               "measures the energy each coulomb gives up as it passes.",
    },
    {
        "id": "ks4-current-resistance-pd-e03",
        "subtopic_slug": "current-resistance-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement about an ohmic conductor kept at a constant "
                "temperature is correct?",
        "options": [
            "Its resistance increases as the current through it increases",
            "Its resistance decreases as the potential difference across it "
            "increases",
            "Its resistance stays the same whatever current flows through it",
            "Its resistance is zero until the potential difference reaches a "
            "threshold",
        ],
        "correct_index": 2,
        "why": "For an ohmic conductor the current is directly proportional "
               "to the pd, so V ÷ I gives the same resistance every time.",
    },
    {
        "id": "ks4-current-resistance-pd-e04",
        "subtopic_slug": "current-resistance-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two resistors are connected in series across a 9.0 V "
                "battery. The potential difference across the first is "
                "6.0 V. State the potential difference across the second.",
        "options": ["3.0 V", "9.0 V", "4.5 V", "15 V"],
        "correct_index": 0,
        "why": "In series the potential differences add up to the supply pd, "
               "so the second resistor takes 9.0 − 6.0 = 3.0 V.",
    },
    {
        "id": "ks4-current-resistance-pd-s01",
        "subtopic_slug": "current-resistance-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An 8.0 Ω resistor and a 4.0 Ω resistor are connected "
                "in series across a 24 V supply. Calculate the "
                "potential difference across the 8.0 Ω resistor.",
        "options": [
            "8.0 V",
            "16 V",
            "12 V",
            "24 V",
        ],
        "correct_index": 1,
        "why": "The total resistance is 12 Ω, so the current is 2.0 A, "
               "and V = I × R = 2.0 × 8.0 = 16 V across the 8.0 Ω "
               "resistor.",
    },
    {
        "id": "ks4-current-resistance-pd-s02",
        "subtopic_slug": "current-resistance-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student halves the resistance in a circuit and at the same "
                "time halves the supply potential difference. Predict the "
                "effect on the current.",
        "options": [
            "It is unchanged, because I = V ÷ R and both quantities have "
            "been halved",
            "It halves, because halving the supply potential difference "
            "halves the current",
            "It doubles, because halving the resistance always doubles the "
            "current",
            "It falls to a quarter, because both of the changes act to "
            "reduce the current",
        ],
        "correct_index": 0,
        "why": "Current depends on the ratio V ÷ R, and halving both leaves "
               "that ratio — and so the current — exactly as it was.",
    },
    {
        "id": "ks4-current-resistance-pd-s03",
        "subtopic_slug": "current-resistance-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A resistor obeys Ohm's law. At 4.0 V the current through it "
                "is 0.20 A. Determine the current when the potential "
                "difference is 10.0 V.",
        "options": ["0.80 A", "0.20 A", "0.50 A", "0.05 A"],
        "correct_index": 2,
        "why": "Its resistance is 4.0 ÷ 0.20 = 20 Ω and stays constant, so "
               "I = V ÷ R = 10.0 ÷ 20 = 0.50 A.",
    },
    {
        "id": "ks4-current-resistance-pd-s04",
        "subtopic_slug": "current-resistance-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures 4.5 V across a component and 0.30 A "
                "through it. Calculate its resistance.",
        "options": ["1.4 Ω", "4.8 Ω", "0.067 Ω", "15 Ω"],
        "correct_index": 3,
        "why": "R = V ÷ I = 4.5 ÷ 0.30 = 15 Ω.",
    },
    {
        "id": "ks4-current-resistance-pd-h01",
        "subtopic_slug": "current-resistance-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 12 V battery is connected in series with a fixed 8.0 Ω "
                "resistor and a variable resistor. The variable resistor is "
                "adjusted until the current is 0.50 A. Determine its "
                "resistance.",
        "options": ["16 Ω", "24 Ω", "8.0 Ω", "4.0 Ω"],
        "correct_index": 0,
        "why": "The total resistance must be 12 ÷ 0.50 = 24 Ω, and the fixed "
               "resistor provides 8.0 Ω of that, so the variable resistor is "
               "set to 16 Ω.",
    },
    {
        "id": "ks4-current-resistance-pd-h02",
        "subtopic_slug": "current-resistance-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'The voltmeter reads 9.0 V and the "
                "ammeter reads 1.5 A, so the resistance is 9.0 × 1.5 = "
                "13.5 Ω.' Identify the error and give the correct "
                "resistance.",
        "options": [
            "There is no error in the working; the resistance really is "
            "13.5 Ω",
            "They divided the wrong way round; the resistance is 1.5 ÷ 9.0 = "
            "0.17 Ω",
            "They multiplied instead of dividing; the resistance is 9.0 ÷ "
            "1.5 = 6.0 Ω",
            "They should have added the readings; the resistance is 9.0 + "
            "1.5 = 10.5 Ω",
        ],
        "correct_index": 2,
        "why": "Resistance is potential difference divided by current, "
               "R = V ÷ I, so 9.0 ÷ 1.5 = 6.0 Ω.",
    },
    {
        "id": "ks4-current-resistance-pd-h03",
        "subtopic_slug": "current-resistance-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 5.0 Ω resistor and a 15 Ω resistor are connected in "
                "series across a 12 V supply. Compare the potential "
                "difference across each.",
        "options": [
            "6.0 V across each, because a supply pd always divides equally "
            "between components",
            "9.0 V across the 5.0 Ω and 3.0 V across the 15 Ω, as the "
            "smaller resistance passes more energy",
            "12 V across each, because every component in one loop receives "
            "the full supply pd",
            "3.0 V across the 5.0 Ω and 9.0 V across the 15 Ω, as the same "
            "current flows through both",
        ],
        "correct_index": 3,
        "why": "The same 0.60 A flows through both, so V = I × R makes the "
               "larger resistance take the larger share of the 12 V.",
    },
    {
        "id": "ks4-current-resistance-pd-h04",
        "subtopic_slug": "current-resistance-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student finds the resistance of a coil of wire to be "
                "8.0 Ω using a 2.0 V supply, then repeats the measurement "
                "with a 6.0 V supply and obtains 9.5 Ω. Suggest why the two "
                "values differ.",
        "options": [
            "The voltmeter must have been misread, because a metal wire's "
            "resistance cannot change",
            "The larger pd drove a larger current, which heated the wire, "
            "and a hotter metal resists more",
            "The larger pd pushed the electrons through more easily, so the "
            "resistance should have fallen",
            "The 6.0 V supply was alternating rather than direct, so its "
            "resistance value means nothing",
        ],
        "correct_index": 1,
        "why": "A metal is ohmic only at constant temperature: a bigger "
               "current warms the wire, its ions vibrate more strongly, and "
               "the resistance rises.",
    },

    # ── resistors ───────────────────────────────────────────────────────
    {
        "id": "ks4-resistors-e01",
        "subtopic_slug": "resistors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which component allows current to flow in one direction "
                "only?",
        "options": [
            "A diode",
            "A thermistor",
            "A light-dependent resistor",
            "A variable resistor",
        ],
        "correct_index": 0,
        "why": "A diode has a very high resistance in the reverse direction, "
               "so current passes only the way its triangle points.",
    },
    {
        "id": "ks4-resistors-e02",
        "subtopic_slug": "resistors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the shape of the I–V graph for a resistor held at "
                "a constant temperature.",
        "options": [
            "A curve that becomes shallower as the potential difference "
            "increases",
            "A line that stays flat until about 0.6 V and then rises steeply",
            "A straight line passing through the origin",
            "A straight line that crosses the current axis above the origin",
        ],
        "correct_index": 2,
        "why": "Its resistance is constant, so current is directly "
               "proportional to potential difference and the graph is a "
               "straight line through the origin.",
    },
    {
        "id": "ks4-resistors-e03",
        "subtopic_slug": "resistors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the resistance of a filament lamp as "
                "the current through it increases.",
        "options": [
            "It decreases, because more charge carriers are freed",
            "It increases, because the filament gets hotter",
            "It stays constant, because a lamp is an ohmic conductor",
            "It falls to zero once the filament begins to glow",
        ],
        "correct_index": 1,
        "why": "A larger current heats the filament, its ions vibrate more "
               "and obstruct the electrons, so the resistance rises.",
    },
    {
        "id": "ks4-resistors-e04",
        "subtopic_slug": "resistors",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one everyday use of a thermistor.",
        "options": [
            "In an automatic street light that switches itself on when dusk "
            "falls",
            "In a rectifier that changes an alternating supply into a direct "
            "one",
            "In a fuse that melts whenever the current becomes too large to "
            "be safe",
            "In an oven thermostat that switches the heater off at the set "
            "temperature",
        ],
        "correct_index": 3,
        "why": "A thermistor's resistance changes with temperature, so it is "
               "the sensing component in thermostats, fire alarms and "
               "temperature probes.",
    },
    {
        "id": "ks4-resistors-s01",
        "subtopic_slug": "resistors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the I–V graph for a filament lamp curves "
                "instead of being a straight line.",
        "options": [
            "Some of the current is given out as light, so less of it "
            "reaches the ammeter",
            "The glass envelope stores charge, which holds the current down "
            "at high pd",
            "The filament heats up as the current rises, so its resistance "
            "increases",
            "The filament melts a little at high current, which lowers its "
            "resistance",
        ],
        "correct_index": 2,
        "why": "Rising temperature raises the filament's resistance, so each "
               "extra volt adds less current than the last and the line "
               "bends over.",
    },
    {
        "id": "ks4-resistors-s02",
        "subtopic_slug": "resistors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diode is connected in series with a resistor and a "
                "battery. The battery connections are then reversed. Predict "
                "the current.",
        "options": [
            "The same size as before, but flowing in the opposite direction",
            "Larger than before, because a diode's resistance falls when it "
            "is reversed",
            "Half of its previous value, because only half of each cycle can "
            "pass through",
            "Almost zero, because a diode has a very high resistance in "
            "reverse",
        ],
        "correct_index": 3,
        "why": "A diode conducts in one direction only; reversed, its "
               "resistance is so high that virtually no current flows.",
    },
    {
        "id": "ks4-resistors-s03",
        "subtopic_slug": "resistors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical to obtain an I–V characteristic, "
                "state the purpose of the variable resistor.",
        "options": [
            "To vary the potential difference across the component, giving "
            "a range of readings",
            "To hold the current constant while the potential difference "
            "across it is varied",
            "To measure the resistance of the component directly, in ohms, "
            "as it varies",
            "To stop the ammeter from ever displaying a negative current "
            "reading",
        ],
        "correct_index": 0,
        "why": "Adjusting the variable resistor changes the share of the "
               "supply pd reaching the component, giving the spread of I and "
               "V values a graph needs.",
    },
    {
        "id": "ks4-resistors-s04",
        "subtopic_slug": "resistors",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the resistance of an LED in the forward direction "
                "and in the reverse direction.",
        "options": [
            "High in the forward direction and low in the reverse direction",
            "Low in the forward direction above about 0.6 V, and very high "
            "in reverse",
            "The same in both directions, because an LED is an ohmic "
            "conductor",
            "Very high in both directions until the LED starts to emit light",
        ],
        "correct_index": 1,
        "why": "An LED is a diode: above its threshold pd it conducts easily "
               "one way, and blocks the current almost completely the other "
               "way.",
    },
    {
        "id": "ks4-resistors-h01",
        "subtopic_slug": "resistors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thermistor is connected in series with a fixed resistor "
                "across a battery. Explain what happens to the potential "
                "difference across the fixed resistor as the room warms up.",
        "options": [
            "It decreases, because the thermistor's resistance rises and "
            "takes a larger share of the supply pd",
            "It stays the same, because the supply potential difference is "
            "fixed by the battery",
            "It decreases, because a warmer circuit wastes more of the "
            "supplied energy as heat",
            "It increases, because the thermistor's resistance falls and "
            "takes a smaller share of the supply pd",
        ],
        "correct_index": 3,
        "why": "In series the larger resistance takes the larger share of the "
               "pd, and a warming thermistor's resistance falls, so the "
               "fixed resistor's share grows.",
    },
    {
        "id": "ks4-resistors-h02",
        "subtopic_slug": "resistors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student testing a filament lamp records 0.20 A at 1.0 V "
                "and 0.50 A at 6.0 V. Calculate the change in the lamp's "
                "resistance between the two readings.",
        "options": [
            "It falls by 7.0 Ω, from 12 Ω to 5.0 Ω",
            "It rises by 7.0 Ω, from 5.0 Ω to 12 Ω",
            "It is unchanged at 5.0 Ω, as resistance is a fixed property",
            "It rises by 0.30 Ω, from 0.20 Ω to 0.50 Ω",
        ],
        "correct_index": 1,
        "why": "R = V ÷ I gives 1.0 ÷ 0.20 = 5.0 Ω and 6.0 ÷ 0.50 = 12 Ω, a "
               "rise of 7.0 Ω as the filament heats up.",
    },
    {
        "id": "ks4-resistors-h03",
        "subtopic_slug": "resistors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical, explain why a protective "
                "resistor is placed in series with the diode.",
        "options": [
            "To prevent the diode from conducting at all when it is "
            "connected in reverse",
            "To straighten the diode's I–V graph into a line passing "
            "through the origin",
            "A conducting diode has a very low resistance, so the current "
            "would rise dangerously",
            "To hold the potential difference across the diode at exactly "
            "0.6 V at all times",
        ],
        "correct_index": 2,
        "why": "Above its threshold a diode has almost no resistance, so "
               "without a resistor to limit it the current would rise sharply "
               "enough to destroy the diode.",
    },
    {
        "id": "ks4-resistors-h04",
        "subtopic_slug": "resistors",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A street-light circuit has a light-dependent resistor in "
                "series with a 10 kΩ fixed resistor across a 9.0 V supply. "
                "At dusk the LDR's resistance is 20 kΩ. Calculate the "
                "potential difference across the fixed resistor.",
        "options": ["3.0 V", "6.0 V", "4.5 V", "9.0 V"],
        "correct_index": 0,
        "why": "The resistances add to 30 kΩ, so the current is 0.30 mA, and "
               "V = I × R = 0.30 mA × 10 kΩ = 3.0 V.",
    },

    # ── series-parallel-circuits ────────────────────────────────────────
    {
        "id": "ks4-series-parallel-circuits-e01",
        "subtopic_slug": "series-parallel-circuits",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three resistors of 2.0 Ω, 3.0 Ω and 5.0 Ω are connected in "
                "series. Calculate the total resistance.",
        "options": ["0.97 Ω", "2.0 Ω", "10 Ω", "3.3 Ω"],
        "correct_index": 2,
        "why": "Resistors in series add: 2.0 + 3.0 + 5.0 = 10 Ω, because the "
               "charge has to pass through all three in turn.",
    },
    {
        "id": "ks4-series-parallel-circuits-e02",
        "subtopic_slug": "series-parallel-circuits",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the other lamps in a series circuit "
                "when one lamp breaks.",
        "options": [
            "They stay lit and grow brighter, because there is now less "
            "resistance",
            "They stay lit at exactly the same brightness as they were "
            "before",
            "Only the lamps that come after the break stop working",
            "They all stop working, because the single loop is broken",
        ],
        "correct_index": 3,
        "why": "A series circuit has only one path, so a break anywhere in it "
               "stops the current everywhere.",
    },
    {
        "id": "ks4-series-parallel-circuits-e03",
        "subtopic_slug": "series-parallel-circuits",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement about the total resistance of a parallel "
                "combination is correct?",
        "options": [
            "It is equal to the sum of the individual branch resistances",
            "It is smaller than the resistance of any single branch",
            "It is equal to the resistance of the largest single branch",
            "It is the average of the individual branch resistances",
        ],
        "correct_index": 1,
        "why": "Each extra branch gives the charge another path, so the "
               "combination is easier to drive current through than any one "
               "branch on its own.",
    },
    {
        "id": "ks4-series-parallel-circuits-e04",
        "subtopic_slug": "series-parallel-circuits",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 3.0 Ω and a 9.0 Ω resistor are connected in series "
                "across an 18 V supply. Calculate the current.",
        "options": [
            "1.5 A",
            "6.0 A",
            "2.0 A",
            "0.67 A",
        ],
        "correct_index": 0,
        "why": "The resistances add to give 12 Ω, so I = V ÷ R = 18 ÷ "
               "12 = 1.5 A.",
    },
    {
        "id": "ks4-series-parallel-circuits-s01",
        "subtopic_slug": "series-parallel-circuits",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 12 Ω resistor and a 4.0 Ω resistor are connected in "
                "parallel across a 12 V supply. Calculate the total current "
                "drawn from the supply.",
        "options": ["0.75 A", "3.0 A", "1.0 A", "4.0 A"],
        "correct_index": 3,
        "why": "Each branch has the full 12 V across it, giving 1.0 A and "
               "3.0 A, and the branch currents add to 4.0 A.",
    },
    {
        "id": "ks4-series-parallel-circuits-s02",
        "subtopic_slug": "series-parallel-circuits",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A decorative string has 20 identical lamps in series across "
                "a 240 V supply. Calculate the potential difference across "
                "each lamp.",
        "options": ["12 V", "240 V", "120 V", "4800 V"],
        "correct_index": 0,
        "why": "In series the supply pd divides between the components, so "
               "each of the 20 identical lamps takes 240 ÷ 20 = 12 V.",
    },
    {
        "id": "ks4-series-parallel-circuits-s03",
        "subtopic_slug": "series-parallel-circuits",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why connecting a second identical lamp in parallel "
                "increases the current drawn from the battery.",
        "options": [
            "The two lamps share the supply pd, so each of them needs less "
            "resistance",
            "The second lamp's resistance adds to the first, and that raises "
            "the current",
            "The extra branch is another path, so the total resistance falls "
            "and the current rises",
            "The battery is made to work harder whenever more components are "
            "attached to it in any way",
        ],
        "correct_index": 2,
        "why": "Adding a parallel path lowers the total resistance, and a "
               "lower resistance across the same supply pd means a larger "
               "total current.",
    },
    {
        "id": "ks4-series-parallel-circuits-s04",
        "subtopic_slug": "series-parallel-circuits",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two resistors are in series across a 9.0 V battery. The "
                "potential difference across the 6.0 Ω resistor is 3.0 V. "
                "Determine the resistance of the other resistor.",
        "options": ["6.0 Ω", "12 Ω", "18 Ω", "3.0 Ω"],
        "correct_index": 1,
        "why": "The current is 3.0 ÷ 6.0 = 0.50 A and the other resistor has "
               "6.0 V across it, so R = 6.0 ÷ 0.50 = 12 Ω.",
    },
    {
        "id": "ks4-series-parallel-circuits-h01",
        "subtopic_slug": "series-parallel-circuits",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 6.0 Ω resistor and a 3.0 Ω resistor are connected in "
                "parallel across a 6.0 V supply. Determine the total "
                "resistance of the combination.",
        "options": ["9.0 Ω", "2.0 Ω", "4.5 Ω", "3.0 Ω"],
        "correct_index": 1,
        "why": "The branches carry 1.0 A and 2.0 A, so 3.0 A in all, and "
               "R = V ÷ I = 6.0 ÷ 3.0 = 2.0 Ω — less than either branch.",
    },
    {
        "id": "ks4-series-parallel-circuits-h02",
        "subtopic_slug": "series-parallel-circuits",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 3.0 Ω resistor is in series with a pair of 6.0 Ω "
                "resistors that are in parallel with each other, all across "
                "a 12 V supply. Calculate the current from the supply.",
        "options": ["0.80 A", "4.0 A", "2.0 A", "1.3 A"],
        "correct_index": 2,
        "why": "The parallel pair behaves as 3.0 Ω, which adds to the series "
               "3.0 Ω to give 6.0 Ω, so I = 12 ÷ 6.0 = 2.0 A.",
    },
    {
        "id": "ks4-series-parallel-circuits-h03",
        "subtopic_slug": "series-parallel-circuits",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what happens to a circuit's total resistance when a "
                "10 Ω resistor is added in series and when the same resistor "
                "is added in parallel.",
        "options": [
            "In series the total rises by 10 Ω; in parallel the total falls "
            "below its previous value",
            "In both cases the total rises, but the rise is greater when it "
            "is added in parallel",
            "In series the total falls because the charge travels further; "
            "in parallel the total rises",
            "In both cases the total is unchanged, because the supply "
            "potential difference is unchanged",
        ],
        "correct_index": 0,
        "why": "A series resistor lengthens the single path and adds its "
               "resistance, while a parallel resistor opens a second path and "
               "so always lowers the total.",
    },
    {
        "id": "ks4-series-parallel-circuits-h04",
        "subtopic_slug": "series-parallel-circuits",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car's headlamps and its radio are connected in parallel "
                "across a 12 V battery. The headlamps draw 8.0 A and the "
                "radio draws 0.50 A. Determine the radio's resistance and "
                "predict the effect of switching the headlamps off.",
        "options": [
            "12 Ω, and the radio's current falls once the headlamps stop "
            "sharing the supply",
            "1.4 Ω, found from 12 V divided by the total current of 8.5 A "
            "drawn from the battery",
            "24 Ω, and the radio's current rises because more current is "
            "then available to it",
            "24 Ω, and the radio is unaffected because it still has the full "
            "12 V across it",
        ],
        "correct_index": 3,
        "why": "Every parallel branch keeps the full 12 V, so R = 12 ÷ 0.50 = "
               "24 Ω, and switching off another branch changes neither the "
               "radio's pd nor its current.",
    },

    # ── direct-alternating-pd ───────────────────────────────────────────
    {
        "id": "ks4-direct-alternating-pd-e01",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by an alternating current.",
        "options": [
            "A current that flows one way but keeps changing in size",
            "A current that repeatedly reverses its direction of flow",
            "A current that flows only while a switch is held closed",
            "A current that alternates between two separate circuits",
        ],
        "correct_index": 1,
        "why": "In an alternating supply the potential difference reverses "
               "over and over, so the charge flows first one way and then the "
               "other.",
    },
    {
        "id": "ks4-direct-alternating-pd-e02",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which list correctly sorts these three supplies?",
        "options": [
            "A battery and a solar cell give dc; a power-station generator "
            "gives ac",
            "A battery and a power-station generator give dc; a solar cell "
            "gives ac",
            "A solar cell and a power-station generator give dc; a battery "
            "gives ac",
            "All three give ac, because every electrical supply alternates "
            "at 50 Hz",
        ],
        "correct_index": 0,
        "why": "Batteries and solar cells push charge one way only, while a "
               "rotating generator produces a potential difference that "
               "reverses on each half turn.",
    },
    {
        "id": "ks4-direct-alternating-pd-e03",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alternating supply has a period of 0.040 s. Calculate "
                "its frequency.",
        "options": ["40 Hz", "2.5 Hz", "0.040 Hz", "25 Hz"],
        "correct_index": 3,
        "why": "f = 1 ÷ T = 1 ÷ 0.040 = 25 Hz — twenty-five complete cycles "
               "happen every second.",
    },
    {
        "id": "ks4-direct-alternating-pd-e04",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what each axis of an oscilloscope screen shows.",
        "options": [
            "The vertical axis shows time and the horizontal axis shows "
            "potential difference",
            "The vertical axis shows current and the horizontal axis shows "
            "potential difference",
            "The vertical axis shows potential difference and the horizontal "
            "axis shows time",
            "Both axes show potential difference, one for each of the two "
            "input terminals",
        ],
        "correct_index": 2,
        "why": "An oscilloscope plots how the potential difference changes as "
               "time passes, so pd runs up the screen and time runs across "
               "it.",
    },
    {
        "id": "ks4-direct-alternating-pd-s01",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oscilloscope shows one complete cycle across 5.0 "
                "horizontal divisions, with the time base set to 2.0 ms "
                "per division. Calculate the frequency of the supply.",
        "options": [
            "100 Hz",
            "500 Hz",
            "10 Hz",
            "0.10 Hz",
        ],
        "correct_index": 0,
        "why": "One cycle takes 5.0 × 2.0 ms = 10 ms = 0.010 s, so f = "
               "1 ÷ T = 1 ÷ 0.010 = 100 Hz.",
    },
    {
        "id": "ks4-direct-alternating-pd-s02",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The UK mains supply is quoted as 230 V. Explain what this "
                "value describes.",
        "options": [
            "The peak potential difference, which the supply reaches twice "
            "in every single cycle",
            "An effective value; the potential difference varies and peaks "
            "near 325 V",
            "A constant potential difference that the supply holds steady at "
            "all times",
            "The potential difference measured across the earth wire of the "
            "mains cable",
        ],
        "correct_index": 1,
        "why": "An alternating pd is changing all the time, so it is quoted "
               "as the steady value that would transfer energy at the same "
               "rate — 230 V, with peaks near 325 V.",
    },
    {
        "id": "ks4-direct-alternating-pd-s03",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The frequency of an alternating supply is raised from 50 Hz "
                "to 100 Hz with the time base setting unchanged. Describe "
                "how the oscilloscope trace changes.",
        "options": [
            "The trace becomes twice as tall, because doubling the frequency "
            "doubles the pd",
            "The trace flattens to a horizontal line, because the changes "
            "are now too fast",
            "Half as many cycles fit on the screen, because a higher "
            "frequency means a longer period",
            "Twice as many cycles fit on the screen, because each cycle now "
            "takes half as long",
        ],
        "correct_index": 3,
        "why": "Period is 1 ÷ frequency, so doubling the frequency halves the "
               "time for one cycle and twice as many cycles fit into the same "
               "width of screen.",
    },
    {
        "id": "ks4-direct-alternating-pd-s04",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main advantage of using an alternating supply to "
                "carry electricity from a power station to homes.",
        "options": [
            "An alternating current can travel much further along a cable "
            "before it runs out",
            "An alternating current can flow even when the circuit is not a "
            "complete loop",
            "An alternating pd can be transformed to a very high value, "
            "cutting the wasted energy",
            "An alternating current can be switched off 50 times a second in "
            "order to save energy",
        ],
        "correct_index": 2,
        "why": "Only an alternating potential difference can be stepped up by "
               "a transformer, and a higher transmission pd means a smaller "
               "current and far less heating in the cables.",
    },
    {
        "id": "ks4-direct-alternating-pd-h01",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that the current in a mains cable changes "
                "direction 50 times each second. Determine whether this is "
                "correct.",
        "options": [
            "Yes, because a frequency of 50 Hz means exactly 50 reversals "
            "every second",
            "No, because a frequency of 50 Hz means the current reverses 25 "
            "times a second",
            "No, because there are 50 cycles a second and the current "
            "reverses twice per cycle",
            "No, because the current in a mains cable does not reverse "
            "direction at all",
        ],
        "correct_index": 2,
        "why": "One complete cycle takes the current one way and then back "
               "the other, so 50 cycles a second means 100 reversals a "
               "second.",
    },
    {
        "id": "ks4-direct-alternating-pd-h02",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Trace X shows 5 complete cycles across an oscilloscope "
                "screen. Trace Y shows 10 complete cycles across the same "
                "screen at the same time base setting. Compare the two "
                "supplies.",
        "options": [
            "Y has half the frequency and twice the period of X",
            "Y has twice the frequency and twice the period of X",
            "The frequencies are equal; only the peak potential differences "
            "differ",
            "Y has twice the frequency and half the period of X",
        ],
        "correct_index": 3,
        "why": "Fitting twice as many cycles into the same time means each "
               "cycle lasts half as long, and f = 1 ÷ T, so the frequency "
               "doubles.",
    },
    {
        "id": "ks4-direct-alternating-pd-h03",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alternating supply has a peak potential difference of "
                "325 V. Explain why UK mains is rated at 230 V rather than "
                "325 V.",
        "options": [
            "230 V is the effective value — the steady pd that would "
            "transfer energy at the same rate",
            "230 V is simply the peak value of 325 V rounded down to make "
            "the label safer",
            "230 V is the pd remaining once the earth wire has taken its "
            "share of the supply",
            "230 V is measured between live and neutral, while 325 V is "
            "measured from live to earth",
        ],
        "correct_index": 0,
        "why": "An alternating pd spends most of its cycle below the peak, so "
               "appliances are rated by the steady potential difference that "
               "would deliver the same power — about 230 V.",
    },
    {
        "id": "ks4-direct-alternating-pd-h04",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 12 V dc supply and an alternating supply with a peak "
                "potential difference of 12 V are each connected in turn to "
                "the same lamp. Predict which makes the lamp brighter.",
        "options": [
            "The alternating supply, because its reversing pd drives current "
            "in both directions",
            "The dc supply, because it holds 12 V at all times while the ac "
            "supply only peaks there",
            "Neither, because both supplies are labelled 12 V and so deliver "
            "the same power",
            "The alternating supply, because at 50 Hz it delivers 50 pulses "
            "of energy every second",
        ],
        "correct_index": 1,
        "why": "The alternating pd is below its peak for most of every cycle, "
               "so its effective value is under 12 V and it transfers less "
               "energy each second than a steady 12 V.",
    },
]
