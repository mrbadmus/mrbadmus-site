# Electrical Charge and Current  (Physics, AQA 6.2.1.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Closed circuit + source of pd needed for charge to flow (theory 1) | base | 8464 6.2.1.2 / 8463 4.2.1.2 |
| Current = rate of flow of charge; A; 1 A = 1 C/s (theory 1; key_note) | base | 6.2.1.2 / 4.2.1.2 |
| Q = I t; rearrangements; min → s (theory 2; equations; variables; FIFA; common_mistake; q1) | base | 6.2.1.2 / 4.2.1.2 |
| Same current at any point in a single closed loop (theory 3; common_mistake; q2) | base | 6.2.1.2 / 4.2.1.2 |
| Current splits in parallel; I_total = sum (theory 3; key_note) | base | 8464 6.2.2 / 8463 4.2.2 |
| Free electrons carry the charge in metals (theory 1; key_note) | base (supporting) | 8464 5.2.2.8 / 8462 4.2.2.8 (delocalised electrons, chemistry) |
| Ions in electrolytes; conventional current vs electron flow; 1 C ≈ 6.24 × 10¹⁸ electrons (theory 1–2; key_note) | off-spec | — |
| `rp` "RP15 (Physics) — … ammeters at different positions…" | none — not an AQA required practical | 8464 RP15 / 8463 RP3 is resistance (6.2.1.3 / 4.2.1.3) |
| `higher` | none | — |

True page routes: CF CH TF TH (all base). Site currently ships: CF CH TF TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe electric current as flow of charge and calculate charge, current and time.

## theory
```json
[
  {
    "content": "ELECTRIC CURRENT is a flow of electrical charge.\n\nFor current to flow, two conditions must be met:\n1. There must be a CLOSED CIRCUIT — a complete, unbroken conducting path.\n2. There must be a SOURCE OF POTENTIAL DIFFERENCE (a battery or power supply) to drive the charge.\n\nCurrent is measured in AMPERES (A).\n1 ampere = 1 coulomb of charge passing a point per second.\n\nIn metal conductors, the charge carriers are FREE ELECTRONS.\nIn solutions (electrolytes), the charge carriers are IONS.\n\nCONVENTIONAL CURRENT flows from + to − around the external circuit.\nELECTRON FLOW is actually from − to + (electrons repelled from the negative terminal).\nConventional current direction was defined before electrons were discovered.",
    "heading": "Electric Current — Flow of Charge"
  },
  {
    "content": "Q = I × t\n\nQ = charge flow (coulombs, C)\nI = current (amperes, A)\nt = time (seconds, s)\n\nRearranging:\nI = Q ÷ t\nt = Q ÷ I\n\nEXAMPLE 1:\nA current of 2 A flows for 30 s:\nQ = 2 × 30 = 60 C\n\nEXAMPLE 2:\n120 C flows in 4 minutes:\nt = 4 × 60 = 240 s\nI = 120 ÷ 240 = 0.5 A\n\nOne coulomb ≈ 6.24 × 10¹⁸ electrons.",
    "heading": "Charge, Current and Time"
  },
  {
    "content": "SERIES circuit:\nCurrent is the SAME everywhere — only one path for charge.\nI₁ = I₂ = I₃\n\nPARALLEL circuit:\nCurrent SPLITS at junctions — more paths available.\nI_total = I₁ + I₂ + I₃\nBranches with lower resistance carry more current.\n\nMEASURING CURRENT:\nUse an AMMETER connected in SERIES.\nAmmeters have very LOW resistance — do not significantly affect the circuit.",
    "heading": "Current in Series and Parallel Circuits"
  }
]
```

## common_mistake

Time must be in SECONDS when using Q = It. If given minutes, multiply by 60 first. In a series circuit, current is the SAME at every point — it does not get 'used up' passing through components.

## key_note

Current = rate of flow of charge. Q = It. Unit: ampere (A). Series: same current everywhere. Parallel: current splits — I_total = sum of branches. Charge carriers in metals = electrons. Conventional current: + to −. Electron flow: − to +.

## equations
```json
[
  "Q = I × t"
]
```

## fifas
```json
[
  {
    "label": "Charge Calculation",
    "question": "A current of 0.4 A flows through a lamp for 5 minutes. Calculate the charge that flows.",
    "steps": [
      [
        "F",
        "Q = I × t"
      ],
      [
        "I",
        "I = 0.4 A, t = 5 × 60 = 300 s"
      ],
      [
        "F",
        "Q = 0.4 × 300"
      ],
      [
        "A",
        "Q = 120 C"
      ]
    ]
  }
]
```

## rp

RP15 (Physics) — Set up series and parallel circuits; measure current with ammeters at different positions to verify series current is constant and parallel currents sum to total.

## variables
```json
[
  [
    "Q",
    "Charge",
    "coulombs",
    "C"
  ],
  [
    "I",
    "Current",
    "amperes",
    "A"
  ],
  [
    "t",
    "Time",
    "seconds",
    "s"
  ]
]
```

## matching
```json
{
  "instruction": "Match each scenario to the correct value.",
  "pairs": [
    [
      "60 C",
      "Current = 3 A, time = 20 s — Q = 3 × 20"
    ],
    [
      "0.5 A",
      "Charge = 90 C, time = 3 minutes — I = 90 ÷ 180"
    ],
    [
      "Same everywhere",
      "Current at each point in a series circuit"
    ],
    [
      "Splits at junctions",
      "Current behaviour in a parallel circuit"
    ]
  ],
  "title": "Charge and Current"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "1.5 A — I = Q ÷ t = 180 ÷ 120 = 1.5 A (t = 2 × 60 = 120 s)",
        true
      ],
      [
        "90 A — I = 180 ÷ 2 (used minutes not seconds)",
        false
      ],
      [
        "360 A — I = 180 × 2 (multiplied instead of divided)",
        false
      ],
      [
        "0.013 A — I = 180 ÷ 14400 (used hours)",
        false
      ]
    ],
    "q": "A charge of 180 C flows through a resistor in 2 minutes. What is the current?",
    "wrong_explanations": {
      "1": "2 minutes = 120 seconds. I = 180 ÷ 2 = 90 A — used minutes, not seconds.",
      "2": "I = Q ÷ t, not Q × t. Must divide.",
      "3": "2 minutes = 120 s (not 14400). I = 180 ÷ 120 = 1.5 A."
    }
  },
  {
    "opts": [
      [
        "0.3 A — current is identical at every point in a series circuit",
        true
      ],
      [
        "Less than 0.3 A — the first lamp has used some of the current",
        false
      ],
      [
        "More than 0.3 A — the second lamp draws extra current",
        false
      ],
      [
        "Depends on the resistance of each lamp",
        false
      ]
    ],
    "q": "In a series circuit, an ammeter before the first lamp reads 0.3 A. What does an ammeter between the two lamps read?",
    "wrong_explanations": {
      "1": "Current is NOT 'used up' — energy is transferred but the charges continue flowing. Current is identical throughout a series circuit.",
      "2": "Current cannot increase through a series circuit without a junction.",
      "3": "In a series circuit, current is always the same at all points regardless of individual resistances."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A current of 0.4 A flows through a lamp for 5 minutes. Calculate the charge that flows.

**Convert:** [NEW — examined ✓] minutes → seconds: t = 5 min = 5 × 60 = 300 s (I is already in A, needs no conversion).

**F:** Q = I × t

**I:** I = 0.4 A, t = 5 × 60 = 300 s

**F:** Q = 0.4 × 300

**A:** Q = 120 C
