# Standard Circuit Diagram Symbols  (Physics, AQA 6.2.1.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Standard symbols; draw and interpret circuit diagrams (theory 1–3; key_note) | base | 8464 6.2.1.1 / 8463 4.2.1.1 |
| The AQA symbol list: switch (open, closed), cell, battery, diode, resistor, variable resistor, LED, lamp, fuse, voltmeter, ammeter, thermistor, LDR (theory 2) | base | 6.2.1.1 / 4.2.1.1 (spec figure) |
| Ammeter in series, voltmeter in parallel (theory 2–3; common_mistake; q1, q2) | base | 8464 6.2.1.3–6.2.1.4 / 8463 4.2.1.3–4.2.1.4 (RP context) |
| pd shared in series (q2 wx2, wx3) | base | 8464 6.2.2 / 8463 4.2.2 |
| `rp` "RP15 (Physics) … RP16" | none at this spec point — RPs belong to 6.2.1.3 (RP15/RP3) and 6.2.1.4 (RP16/RP4) | 8464 6.2.1.3–6.2.1.4 / 8463 4.2.1.3–4.2.1.4 |
| `higher` | none | — |

True page routes: CF CH TF TH (all base). Site currently ships: CF CH TF TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Draw and interpret circuit diagrams using standard symbols.

## theory
```json
[
  {
    "content": "Circuit diagrams use STANDARD SYMBOLS so that any engineer or scientist worldwide can read and build the same circuit — regardless of language.\n\nA circuit diagram shows how components are connected using straight lines (wires) and standardised symbols. It is a schematic, not a picture of the physical layout.\n\nRules for drawing circuit diagrams:\nUse a RULER — all lines must be straight.\nComponents are placed on the lines, not at corners.\nCircuit should be drawn as a CLOSED LOOP.\nWires are shown as straight horizontal and vertical lines.",
    "heading": "Why Standard Symbols?"
  },
  {
    "content": "You must be able to draw and recognise all of these — the AQA list:\n\nPOWER SUPPLIES:\nCell — one long line (positive) + one short line (negative)\nBattery — two cells joined by a dashed line (two or more cells in series)\n\nCONTROL:\nSwitch (open) — a lever angled away from its second contact\nSwitch (closed) — the lever touching both contacts\n\nOUTPUT COMPONENTS:\nLamp — circle with a cross inside\nLED — diode symbol with two arrows pointing out\n\nMEASUREMENT:\nAmmeter — circle with A (connected in SERIES)\nVoltmeter — circle with V (connected in PARALLEL)\n\nRESISTANCE:\nResistor — rectangle\nVariable resistor — rectangle with a diagonal arrow through it\nThermistor — rectangle with a diagonal line through it, ending in a short horizontal tail\nLDR (light-dependent resistor) — small rectangle inside a circle, with two arrows pointing in\n\nOTHER:\nDiode — triangle pointing to a bar (current flows in the direction of the triangle)\nFuse — rectangle with a line running through it along its length",
    "heading": "Essential Component Symbols"
  },
  {
    "content": "To INTERPRET a circuit diagram:\n1. Trace the path from the positive terminal of the battery.\n2. Identify all components along each branch.\n3. Note which components are in series (same path) and which are in parallel (different branches).\n\nTo DRAW a circuit diagram:\n1. Sketch the battery and switch first.\n2. Add components in the correct positions.\n3. Connect everything with straight ruled lines.\n4. Add meters: ammeter in series with the component; voltmeter in parallel across it.\n\nCOMMON EXAM TASK:\nGiven a description of a circuit, draw it accurately with all components in the correct positions and symbols drawn correctly.",
    "heading": "Reading and Drawing Circuit Diagrams"
  }
]
```

## common_mistake

Ammeters are connected IN SERIES — they must be in the same loop as the component. Voltmeters are connected IN PARALLEL — they bridge across the component. Swapping these will give wrong readings (and could damage the meter). Always draw with a ruler — freehand diagrams lose marks.

## key_note

Standard symbols allow universal reading of circuits. The AQA symbols: switch (open and closed), cell, battery, diode, resistor, variable resistor, LED, lamp, fuse, voltmeter, ammeter, thermistor, LDR. Ammeter in series. Voltmeter in parallel.

## rp

RP15 (Physics) — Use circuit diagrams to set up and investigate circuits. RP16 — Construct circuits to investigate I–V characteristics.

## matching
```json
{
  "instruction": "Match each component to what it does or how it is connected.",
  "pairs": [
    [
      "Ammeter",
      "Connected in series — measures current"
    ],
    [
      "Voltmeter",
      "Connected in parallel — measures potential difference"
    ],
    [
      "LDR",
      "Resistance decreases as light intensity increases"
    ],
    [
      "Thermistor",
      "Resistance decreases as temperature increases"
    ],
    [
      "Diode",
      "Lets current flow in one direction only"
    ]
  ],
  "title": "Component to Job"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "In series with the lamp — in the same loop, so the same current flows through both",
        true
      ],
      [
        "In parallel with the lamp — connected across it to measure the potential difference",
        false
      ],
      [
        "Anywhere in the circuit — ammeters measure the total current of the whole circuit",
        false
      ],
      [
        "Between the two terminals of the battery — to measure the source current",
        false
      ]
    ],
    "q": "How should an ammeter be connected to measure the current through a lamp?",
    "wrong_explanations": {
      "1": "In parallel is how you connect a VOLTMETER, not an ammeter. An ammeter in parallel would short-circuit the component.",
      "2": "An ammeter must be in series specifically with the component being measured — position matters in branched circuits.",
      "3": "Placing an ammeter directly across the battery terminals would short-circuit the battery — dangerous and incorrect."
    }
  },
  {
    "opts": [
      [
        "In parallel with the lamp — one lead connected on each side of the lamp only",
        true
      ],
      [
        "In series with the lamp — in the same loop as the lamp and the resistor",
        false
      ],
      [
        "Across the cell — the potential difference of the cell is all across the lamp",
        false
      ],
      [
        "Anywhere in the circuit — the potential difference is the same everywhere in series",
        false
      ]
    ],
    "q": "A lamp and a resistor are connected in series with a cell. How should a voltmeter be connected to measure the potential difference across the lamp?",
    "wrong_explanations": {
      "1": "Series is how you connect an AMMETER. A voltmeter has a very high resistance, so in series it would stop almost all of the current.",
      "2": "Across the cell, the voltmeter reads the pd of the cell. In series that pd is shared between the lamp and the resistor, so the lamp has only part of it.",
      "3": "In a series circuit the potential difference is SHARED between the components, not the same everywhere. Connect the voltmeter across the lamp itself."
    }
  }
]
```
