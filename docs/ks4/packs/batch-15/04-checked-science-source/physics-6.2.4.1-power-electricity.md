# Power  (Physics, AQA 6.2.4.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| power = rate of energy transfer; P = VI; P = I²R; I = P ÷ V (theory 1, 3; equations; variables; common_mistake; key_note; FIFA; q1) | base | 8464 6.2.4.1; 8463 4.2.4.1 |
| E = Pt, E = VQ (theory 2; equations; key_note) | base — taught in `energy-transfers-appliances` | 8464 6.2.4.2; 8463 4.2.4.2 |
| choosing a fuse rating (theory 3; key_note; matching; q2) | beyond spec — not on 8463/8464 (PE-F1); q2 not usable | — |

True page routes: CF CH TF TH (all base; no HT). Matches the site.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Calculate electrical power using P = VI and P = I²R, and select appropriate fuse ratings.

## theory
```json
[
  {
    "content": "ELECTRICAL POWER is the rate of energy transfer by an electrical component.\n\nP = V × I\nP = I² × R\n\nP = power (W)\nV = potential difference (V)\nI = current (A)\nR = resistance (Ω)\n\nUse P = VI when you know V and I.\nUse P = I²R when you know I and R.\n\nEXAMPLE:\nLamp: 12 V, 2 A.\nP = 12 × 2 = 24 W\nCheck: R = 12/2 = 6 Ω; P = 2² × 6 = 4 × 6 = 24 W ✓",
    "heading": "Electrical Power Equations"
  },
  {
    "content": "E = P × t (energy in J, time in seconds)\nE = V × Q (energy = pd × charge)\n\nEXAMPLE:\n60 W lamp for 5 minutes:\nE = 60 × 300 = 18,000 J\n\nCharge link:\n150 C through 12 V component:\nE = 12 × 150 = 1800 J",
    "heading": "Energy and Charge"
  },
  {
    "content": "Step 1: I = P ÷ V\nStep 2: Choose fuse rated JUST ABOVE operating current.\n\nCommon ratings: 1 A, 3 A, 5 A, 13 A.\n\nEXAMPLE 1 — 500 W TV at 230 V:\nI = 500 ÷ 230 ≈ 2.2 A → 3 A fuse.\n\nEXAMPLE 2 — 2300 W kettle at 230 V:\nI = 2300 ÷ 230 = 10 A → 13 A fuse.\n\nFuse too low → blows in normal use.\nFuse too high → won't blow in a fault → dangerous.",
    "heading": "Choosing the Correct Fuse"
  }
]
```

## common_mistake

In P = I²R, CURRENT is squared, not resistance. Students often write P = I × R² by mistake. To find I from power: use I = P ÷ V (not P = I²R unless R is known and V is not).

## key_note

P = VI. P = I²R. E = Pt. E = VQ. I = P/V for fuse selection — choose just above. UK mains = 230 V.

## equations
```json
[
  "P = V × I",
  "P = I² × R",
  "E = P × t",
  "E = V × Q"
]
```

## fifas
```json
[
  {
    "label": "Electrical Power",
    "question": "A lamp operates at 240 V and draws 0.25 A. Calculate its power.",
    "steps": [
      [
        "F",
        "P = V × I"
      ],
      [
        "I",
        "V = 240 V, I = 0.25 A"
      ],
      [
        "F",
        "P = 240 × 0.25"
      ],
      [
        "A",
        "P = 60 W"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "P",
    "Power",
    "watts",
    "W"
  ],
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
  ],
  [
    "E",
    "Energy",
    "joules",
    "J"
  ],
  [
    "Q",
    "Charge",
    "coulombs",
    "C"
  ]
]
```

## matching
```json
{
  "instruction": "Match each scenario to the correct answer.",
  "pairs": [
    [
      "24 W",
      "V = 12 V, I = 2 A — P = 12 × 2"
    ],
    [
      "100 W",
      "I = 10 A, R = 1 Ω — P = 10² × 1"
    ],
    [
      "3 A fuse",
      "690 W appliance on 230 V — I = 3 A"
    ],
    [
      "13 A fuse",
      "2300 W kettle on 230 V — I = 10 A"
    ]
  ],
  "title": "Power Calculations"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "72 W — P = I² × R = 9 × 8 = 72 W",
        true
      ],
      [
        "24 W — P = I × R = 3 × 8 (forgot to square I)",
        false
      ],
      [
        "576 W — P = I² × R² = 9 × 64 (squared both)",
        false
      ],
      [
        "2.67 W — P = R ÷ I",
        false
      ]
    ],
    "q": "A resistor (R = 8 Ω) carries 3 A. What is the power dissipated?",
    "wrong_explanations": {
      "1": "P = I × R gives volts (A × Ω = V) — not watts. Must square the current.",
      "2": "Only CURRENT is squared: P = I²R = 9 × 8 = 72 W.",
      "3": "R ÷ I gives Ω/A — not watts. P = I²R."
    }
  },
  {
    "opts": [
      [
        "13 A — I = 1380 ÷ 230 = 6 A; next rating above 6 A is 13 A",
        true
      ],
      [
        "3 A — safest choice for any appliance",
        false
      ],
      [
        "5 A — just below 6 A so it will work",
        false
      ],
      [
        "1 A — smallest fuse is always safest",
        false
      ]
    ],
    "q": "A 1380 W iron on 230 V mains. Which fuse?",
    "wrong_explanations": {
      "1": "A 3 A fuse would blow immediately — the iron draws ~6 A.",
      "2": "5 A is BELOW the 6 A operating current — it would blow under normal use.",
      "3": "1 A is far below operating current — would blow immediately."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A lamp operates at 240 V and draws 0.25 A. Calculate its power.

**Convert:** [NEW — examined ✓] Nothing to convert — V and I are both already given in SI units (volts, amps).

**F:** P = V × I

**I:** V = 240 V, I = 0.25 A

**F:** P = 240 × 0.25

**A:** P = 60 W
