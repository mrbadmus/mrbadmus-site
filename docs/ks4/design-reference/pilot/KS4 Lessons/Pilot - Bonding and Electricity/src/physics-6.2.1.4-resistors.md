# Resistors  (Physics, AQA 6.2.1.4)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe I–V characteristics of resistors, lamps, diodes, thermistors and LDRs.

## theory
```json
[
  {
    "content": "OHMIC CONDUCTOR — constant resistance; I–V graph is a straight line through the origin.\n\nFILAMENT LAMP:\nAs current increases → lamp heats up → resistance INCREASES.\nI–V graph: curve that gets shallower at higher pd.\nNot ohmic — resistance changes with temperature.\n\nDIODE:\nAllows current in ONE DIRECTION only.\nVery high resistance in reverse.\nI–V graph: flat near zero in reverse; steep rise forward (above ~0.6 V threshold).\nUsed in rectifiers to convert AC to DC.\n\nLED (LIGHT-EMITTING DIODE):\nWorks like a diode but emits light when forward biased.\nVery efficient — widely used for lighting and indicators.",
    "heading": "Ohmic and Non-Ohmic Components"
  },
  {
    "content": "THERMISTOR (NTC — negative temperature coefficient):\nResistance DECREASES as temperature INCREASES.\nHotter → more charge carriers → lower resistance → more current.\n\nApplications: thermostats, temperature sensors, fire alarms, ovens.\n\nLDR (LIGHT-DEPENDENT RESISTOR):\nResistance DECREASES as light intensity INCREASES.\nBright light → more charge carriers available → lower resistance.\nIn darkness → very high resistance.\n\nApplications: automatic street lights (switch on when dark), security lights, camera exposure meters.\n\nEXAMPLE: Street light circuit — dark → LDR resistance high → voltage across LDR high → triggers switch → light activates.",
    "heading": "Thermistors and LDRs"
  },
  {
    "content": "REQUIRED PRACTICAL (RP16) — Investigate I–V characteristics of:\n1. A resistor at constant temperature (ohmic — straight line)\n2. A filament lamp (non-ohmic — curve, resistance rises)\n3. A diode (allows one direction — flat then steep)\n\nMETHOD:\nVariable resistor changes pd across component.\nAmmeter (series) and voltmeter (parallel) measure I and V.\nReverse connections to obtain negative values.\nPlot I–V graph for each.\n\nSAFETY: Keep current low to avoid overheating. Use a protective resistor in series with the diode.",
    "heading": "I–V Characteristics and Required Practical"
  }
]
```

## common_mistake

Thermistor resistance DECREASES with higher temperature (NTC). LDR resistance DECREASES with more light. Both are the OPPOSITE of what students often assume. A filament lamp is NOT ohmic — its resistance increases as it heats up.

## key_note

Ohmic resistor: constant R, straight I–V. Filament lamp: R increases with temperature, curved I–V. Diode: one direction only. Thermistor (NTC): R decreases with temperature. LDR: R decreases with light. RP16: investigate I–V graphs for resistor, lamp, diode.

## equations
```json
[
  "R = V ÷ I"
]
```

## rp

RP16 (Physics) — Construct circuits to investigate I–V characteristics of a filament lamp, diode and resistor. Plot graphs and interpret each.

## variables
```json
[
  [
    "R",
    "Resistance",
    "ohms",
    "Ω"
  ],
  [
    "I",
    "Current",
    "amperes",
    "A"
  ],
  [
    "V",
    "Potential difference",
    "volts",
    "V"
  ]
]
```

## matching
```json
{
  "instruction": "Match each component to how its resistance changes.",
  "pairs": [
    [
      "Ohmic resistor",
      "Resistance stays constant — straight I–V line through origin"
    ],
    [
      "Filament lamp",
      "Resistance increases as it heats up — curved I–V graph"
    ],
    [
      "Diode",
      "Very low resistance in forward direction only — blocks reverse current"
    ],
    [
      "Thermistor (NTC)",
      "Resistance decreases as temperature increases"
    ],
    [
      "LDR",
      "Resistance decreases as light intensity increases"
    ]
  ],
  "title": "Component Behaviour"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Resistance decreases, current increases — NTC thermistors have lower resistance at higher temperatures",
        true
      ],
      [
        "Resistance increases, current decreases — hotter means more resistance like a metal wire",
        false
      ],
      [
        "Resistance stays the same — thermistors are ohmic",
        false
      ],
      [
        "Current stays constant — current is set by the battery",
        false
      ]
    ],
    "q": "When temperature rises, what happens to a thermistor's resistance and the current through it?",
    "wrong_explanations": {
      "1": "Metal wires do increase resistance with temperature, but thermistors are NTC — opposite behaviour.",
      "2": "Thermistors are NOT ohmic — resistance changes significantly with temperature.",
      "3": "I = V/R — if R changes, I changes too (assuming constant pd)."
    }
  },
  {
    "opts": [
      [
        "Current increases — LDR resistance falls in light, total circuit resistance falls, current rises",
        true
      ],
      [
        "Current decreases — more light makes the LDR resist more",
        false
      ],
      [
        "Current stays the same — the fixed resistor controls the current",
        false
      ],
      [
        "Current becomes zero — LDR blocks current in light",
        false
      ]
    ],
    "q": "An LDR is in series with a fixed resistor and battery. A light is switched on. What happens to the current?",
    "wrong_explanations": {
      "1": "LDR resistance DECREASES in light. Lower total resistance → I = V/R gives higher current.",
      "2": "Fixed resistor limits the minimum resistance but total R still falls when LDR R falls.",
      "3": "LDRs are not diodes — they conduct in both directions, just with different resistance values."
    }
  }
]
```
