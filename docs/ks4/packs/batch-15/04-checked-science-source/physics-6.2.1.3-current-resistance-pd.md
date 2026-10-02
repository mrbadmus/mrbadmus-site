# Current, Resistance and Potential Difference  (Physics, AQA 6.2.1.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| V = IR, rearrangements; greater R → smaller I (theory 1, equations, variables, common_mistake, key_note, FIFA) | base | 8464 6.2.1.3; 8463 4.2.1.3 |
| pd = energy per unit charge (theory 1) | base | 8464 6.2.4.2; 8463 4.2.4.2 |
| Ohmic conductor, I–V graph, measuring R (theory 2; q2) | base — pilot `resistors` owns it; recap only | 8464 6.2.1.4; 8463 4.2.1.4 |
| Series/parallel pd (theory 3) | base — pilot `series-parallel-circuits` owns it; recap only | 8464 6.2.2; 8463 4.2.2 |
| q1 | base — option 4 WRONG, do not use as written (CRP-F1) | 6.2.1.3 |
| `rp` | WRONG as written (CRP-F2) — true RP: Combined RP15 / Physics RP3, factors affecting resistance (wire length; resistors in series and parallel) | 8464 RP15; 8463 RP3 |

True page routes: CF CH TF TH (all base; no HT, no physics-only content). Matches the site.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Apply Ohm's Law (V = IR) to calculate current, resistance and potential difference.

## theory
```json
[
  {
    "content": "POTENTIAL DIFFERENCE (pd) — also called voltage — is the energy transferred per unit charge.\nUnit: VOLT (V). 1 V = 1 joule per coulomb.\n\nRESISTANCE is the opposition to the flow of current.\nUnit: OHM (Ω).\n\nOHM'S LAW:\nV = I × R\n\nV = potential difference (V)\nI = current (A)\nR = resistance (Ω)\n\nRearranging:\nI = V ÷ R\nR = V ÷ I\n\nHigher resistance → lower current for a given pd.\nHigher pd → higher current for a given resistance.",
    "heading": "Potential Difference and Resistance"
  },
  {
    "content": "An OHMIC CONDUCTOR (e.g. a resistor at constant temperature):\nCurrent is DIRECTLY PROPORTIONAL to pd.\nResistance stays CONSTANT as current changes.\n\nOn an I–V graph:\nStraight line through the origin.\nSteeper gradient = lower resistance (more current per volt).\n\nMEASURING RESISTANCE:\nAmmeter in series + voltmeter in parallel.\nR = V ÷ I\n\nEXAMPLE:\n6 V across a resistor, 2 A through it:\nR = 6 ÷ 2 = 3 Ω",
    "heading": "Ohmic Conductors and I–V Graphs"
  },
  {
    "content": "SERIES — pd SPLITS between components:\nV_total = V₁ + V₂ + V₃\nHigher resistance → larger share of pd.\n\nPARALLEL — pd is the SAME across all branches:\nV₁ = V₂ = V₃ = V_supply\n\nEXAMPLE — series circuit:\nBattery = 12 V. R₁ = 4 Ω, R₂ = 8 Ω.\nTotal R = 12 Ω. I = 12 ÷ 12 = 1 A.\nV₁ = 1 × 4 = 4 V. V₂ = 1 × 8 = 8 V. Check: 4 + 8 = 12 V ✓",
    "heading": "Potential Difference in Circuits"
  }
]
```

## common_mistake

R = V ÷ I, NOT V × I. Use the triangle: cover the unknown — the remaining two show the operation. 'Voltage' is acceptable in everyday speech but the precise term is POTENTIAL DIFFERENCE.

## key_note

V = IR. I = V/R. R = V/I. Ohmic: I ∝ V, straight I–V line. Series: pd splits (sum = total). Parallel: same pd across each branch. Ammeter in series; voltmeter in parallel.

## equations
```json
[
  "V = I × R"
]
```

## fifas
```json
[
  {
    "label": "Resistance Calculation",
    "question": "A component has 12 V across it and 0.4 A through it. Calculate its resistance.",
    "steps": [
      [
        "F",
        "R = V ÷ I"
      ],
      [
        "I",
        "V = 12 V, I = 0.4 A"
      ],
      [
        "F",
        "R = 12 ÷ 0.4"
      ],
      [
        "A",
        "R = 30 Ω"
      ]
    ]
  }
]
```

## rp

RP15 (Physics) — Measure V and I for different components; calculate resistance using R = V/I.

## variables
```json
[
  [
    "V",
    "Potential difference",
    "volts",
    "V"
  ],
  [
    "I",
    "Current",
    "amperes",
    "A"
  ],
  [
    "R",
    "Resistance",
    "ohms",
    "Ω"
  ]
]
```

## matching
```json
{
  "instruction": "Match each circuit scenario to the correct calculated value.",
  "pairs": [
    [
      "R = 6 Ω",
      "V = 12 V, I = 2 A — R = 12 ÷ 2"
    ],
    [
      "I = 0.5 A",
      "V = 3 V, R = 6 Ω — I = 3 ÷ 6"
    ],
    [
      "V = 9 V",
      "I = 3 A, R = 3 Ω — V = 3 × 3"
    ],
    [
      "I doubles",
      "Pd doubles for an ohmic conductor — current proportional to pd"
    ]
  ],
  "title": "V = IR Calculations"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "18 V — V = I × R = 3 × 6 = 18 V",
        true
      ],
      [
        "2 V — V = R ÷ I = 6 ÷ 3 = 2 V",
        false
      ],
      [
        "0.5 V — V = I ÷ R = 3 ÷ 6",
        false
      ],
      [
        "9 V — V = (I + R) / 2",
        false
      ]
    ],
    "q": "A 6 Ω resistor has 3 A through it. What is the potential difference?",
    "wrong_explanations": {
      "1": "R ÷ I gives Ω/A — not volts. V = I × R = 3 × 6 = 18 V.",
      "2": "I ÷ R gives A/Ω — not volts. The equation is V = I × R.",
      "3": "There is no averaging formula in Ohm's Law."
    }
  },
  {
    "opts": [
      [
        "Lower resistance — more current per volt (I = V/R, larger I means smaller R)",
        true
      ],
      [
        "Higher resistance — steeper means more opposition",
        false
      ],
      [
        "Higher pd — the axes are swapped",
        false
      ],
      [
        "Non-ohmic behaviour — only curved graphs are ohmic",
        false
      ]
    ],
    "q": "On an I–V graph for an ohmic conductor, what does a steeper gradient indicate?",
    "wrong_explanations": {
      "1": "Steeper I–V gradient means MORE current for same pd → LOWER resistance. High resistance = shallower gradient.",
      "2": "On a standard I–V graph (I on y-axis, V on x-axis), steeper = more current per volt = lower R.",
      "3": "Ohmic conductors produce straight-line I–V graphs — steepness indicates the R value."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A component has 12 V across it and 0.4 A through it. Calculate its resistance.

**Convert:** [NEW — examined ✓] Nothing to convert — V and I are both already given in SI units (volts, amps).

**F:** R = V ÷ I

**I:** V = 12 V, I = 0.4 A

**F:** R = 12 ÷ 0.4

**A:** R = 30 Ω

## Spec core missing from the frozen data (written from the spec, examiner)

The frozen `rp` line names the wrong practical. The practical sited at this spec point, verbatim:

> "Required practical activity 15: use circuit diagrams to set up and check appropriate circuits to investigate the factors affecting the resistance of electrical circuits. This should include:
> • the length of a wire at constant temperature
> • combinations of resistors in series and parallel.
> AT skills covered by this practical activity: physics AT 1, 6 and 7." — AQA 8464 6.2.1.3 (Combined RP15)

> "Required practical activity 3: Use circuit diagrams to set up and check appropriate circuits to investigate the factors affecting the resistance of electrical circuits. This should include:
> • the length of a wire at constant temperature
> • combinations of resistors in series and parallel." — AQA 8463 4.2.1.3 (Physics RP3), same practical.

Apparatus and techniques (8463 §8.2.3): "AT 1 – use appropriate apparatus to measure and record length accurately. AT 6 – use appropriate apparatus to measure current, potential difference and resistance. AT 7 – use circuit diagrams to construct and check series and parallel circuits."

Also verbatim from 6.2.1.3 / 4.2.1.3: "Questions will be set using the term potential difference. Students will gain credit for the correct use of either potential difference or voltage."
