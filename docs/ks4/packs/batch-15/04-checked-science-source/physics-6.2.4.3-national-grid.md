# The National Grid  (Physics, AQA 6.2.4.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Grid = cables + transformers; station → step-up → cables → step-down → homes 230 V (theory 1; key_note) | base | 8464 6.2.4.3 / 8463 4.2.4.3 |
| Why high p.d. is efficient: same P → lower I → less I²R loss (theory 2; common_mistake; key_note; q1) | base | 8464 6.2.4.3, 6.2.4.1 / 8463 4.2.4.3, 4.2.4.1 |
| Loss example I = P/V then P = I²R (theory 2) — a chained calculation; 1000 V line flagged NATIONAL-GRID-F3 | base | 8464 6.2.4.1 |
| P_lost = I²R (equations[1]) | base | 8464 6.2.4.1 / 8463 4.2.4.1 |
| Step-up lowers current, step-down raises it (theory 3) | base (qualitative, from P = VI) | 8464 6.2.4.3 |
| VpIp = VsIs (missing — see section below) | higher | 8464 6.2.4.3 (HT only); 8463 4.7.3.4 (HT only) |
| Transformers need ac (theory 3; common_mistake; key_note) | triple-higher | 8463 4.7.3.4 (physics only) (HT only) |
| Turns: Vp/Vs = np/ns; more/fewer secondary turns (theory 3; key_note; equations[0]; variables np, ns) | triple-higher | 8463 4.7.3.4 (physics only) (HT only) |
| FIFA (turns ratio, 230 kV → 11.5 kV) | triple-higher | 8463 4.7.3.4 |
| q2 (turns ratio) | triple-higher | 8463 4.7.3.4 |

True page routes: CF CH TF TH — base page; a Higher layer (VpIp = VsIs) on CH TH; a Triple Higher layer (turns ratio, ac only, the FIFA, q2) on TH only. Site currently ships: CF CH TF TH with the turns ratio on every route — flagged (NATIONAL-GRID-F1).

## Spec core missing from the frozen data (written from the spec, examiner)

8464 6.2.4.3 (HT only): "Higher tier only: Students should be able to select and use the equation: potential difference across primary coil x current in primary coil = potential difference across secondary coil x current in secondary coil as given on the equation sheet."

8463 4.7.3.4 (physics only) (HT only): "If transformers were 100% efficient, the electrical power output would equal the electrical power input. Vs × Is = Vp × Ip, where Vs × Is is the power output (secondary coil) and Vp × Ip is the power input (primary coil)." Students should be able to "calculate the current drawn from the input supply to provide a particular power output" and "apply the equation linking the p.d.s and number of turns in the two coils of a transformer to the currents and the power transfer involved, and relate these to the advantages of power transmission at high potential differences."

VpIp = VsIs is printed on both June 2026 sheets (8464 and 8463), marked HT → "On the sheet".

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain how the National Grid transmits electricity efficiently and the role of transformers.

## theory
```json
[
  {
    "content": "The NATIONAL GRID is the network of cables and transformers transmitting electrical energy from power stations to consumers.\n\nPath:\nPOWER STATIONS → STEP-UP TRANSFORMERS → HIGH-VOLTAGE CABLES → STEP-DOWN TRANSFORMERS → HOMES (230 V)\n\nTransmission uses very high voltages (132 kV to 400 kV).\nBefore homes receive it, voltage is stepped down to 230 V by local substations.",
    "heading": "What Is the National Grid?"
  },
  {
    "content": "P = IV. For a given power:\nHigh voltage → LOW current (for the same power)\nLow current → less I²R heating in cables → less energy wasted.\n\nCurrent is SQUARED in power loss (P = I²R) — halving current reduces cable losses by ¾.\n\nEXAMPLE:\nTransmit 1 MW through cables (R = 10 Ω):\nAt 1000 V: I = 1000 A → P_lost = 1000² × 10 = 10 MW (more than transmitted!)\nAt 100,000 V: I = 10 A → P_lost = 10² × 10 = 1000 W (tiny fraction)\n\nHigh voltage = far more efficient.",
    "heading": "Why Transmit at High Voltage?"
  },
  {
    "content": "TRANSFORMERS change voltage of AC only (not DC).\n\nSTEP-UP: increases voltage (decreases current) — at power stations.\nSTEP-DOWN: decreases voltage (increases current) — at local substations.\n\nTransformer equation:\nVp ÷ Vs = np ÷ ns\n\nVp = primary voltage; Vs = secondary voltage\nnp = primary turns; ns = secondary turns\n\nEXAMPLE:\n500 primary turns, 50 secondary turns, Vp = 10,000 V:\nVs = 10,000 × (50 ÷ 500) = 1000 V (step-down)",
    "heading": "Transformers"
  }
]
```

## common_mistake

Transformers only work with AC — DC produces no output. High voltage reduces CURRENT (not power) — cable losses are proportional to I² so even a small current reduction gives large savings.

## key_note

Power stations → step-up → high-voltage cables → step-down → homes (230 V). High V = low I = low I²R losses. Step-up: more secondary turns. Step-down: fewer secondary turns. Transformers: AC only. Vp/Vs = np/ns.

## equations
```json
[
  "Vp ÷ Vs = np ÷ ns",
  "P_lost in cables = I² × R"
]
```

## fifas
```json
[
  {
    "label": "Transformer Calculation",
    "question": "A step-down transformer: 2000 primary turns, 100 secondary turns, primary voltage 230,000 V. Find secondary voltage.",
    "steps": [
      [
        "F",
        "Vs = Vp × (ns ÷ np)"
      ],
      [
        "I",
        "Vp = 230,000 V; np = 2000; ns = 100"
      ],
      [
        "F",
        "Vs = 230,000 × (100 ÷ 2000) = 230,000 × 0.05"
      ],
      [
        "A",
        "Vs = 11,500 V"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "Vp",
    "Primary voltage",
    "volts",
    "V"
  ],
  [
    "Vs",
    "Secondary voltage",
    "volts",
    "V"
  ],
  [
    "np",
    "Primary turns",
    "",
    ""
  ],
  [
    "ns",
    "Secondary turns",
    "",
    ""
  ],
  [
    "I",
    "Current",
    "amperes",
    "A"
  ],
  [
    "P",
    "Power",
    "watts",
    "W"
  ]
]
```

## matching
```json
{
  "instruction": "Match each component to its role.",
  "pairs": [
    [
      "Step-up transformer",
      "At power stations — increases voltage to ~400 kV for efficient transmission"
    ],
    [
      "Transmission cables",
      "Carry high-voltage AC across the country on pylons or underground"
    ],
    [
      "Step-down transformer",
      "At substations — reduces voltage to 230 V for homes"
    ],
    [
      "High-voltage transmission",
      "Reduces current → reduces I²R losses — more efficient"
    ]
  ],
  "title": "National Grid Components"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "High voltage means lower current for the same power — lower current means far less I²R heating in cables",
        true
      ],
      [
        "High voltage means higher current — more charge carriers reduce resistance",
        false
      ],
      [
        "Cables are designed only for high voltage — they cannot carry low voltage",
        false
      ],
      [
        "High voltage prevents cable corrosion in rain",
        false
      ]
    ],
    "q": "Why is electricity transmitted at high voltage across the National Grid?",
    "wrong_explanations": {
      "1": "P = IV — for same power, high V means LOW current. Lower current → I²R losses much smaller.",
      "2": "Cable design is for mechanical and safety reasons — efficiency is determined by current levels.",
      "3": "Voltage has no effect on corrosion — cables are protected by materials regardless of voltage."
    }
  },
  {
    "opts": [
      [
        "1000 V — Vs = 20,000 × (200 ÷ 4000) = 20,000 × 0.05 = 1000 V",
        true
      ],
      [
        "400,000 V — Vs = 20,000 × (4000 ÷ 200) (inverted ratio)",
        false
      ],
      [
        "100 V — incorrect ratio calculation",
        false
      ],
      [
        "20,000 V — voltage unchanged through transformer",
        false
      ]
    ],
    "q": "A transformer has 4000 primary turns, 200 secondary turns, primary voltage 20,000 V. What is the secondary voltage?",
    "wrong_explanations": {
      "1": "Using np/ns inverts the ratio: Vs = Vp × (ns/np) = 20,000 × (200/4000) = 1000 V — not ×20.",
      "2": "Check: ns/np = 200/4000 = 0.05. Vs = 20,000 × 0.05 = 1000 V, not 100 V.",
      "3": "Transformers CHANGE the voltage — that is their purpose. Vs = Vp × (ns/np)."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A step-down transformer: 2000 primary turns, 100 secondary turns, primary voltage 230,000 V. Find secondary voltage.

**Convert:** [NEW — examined ✓] Nothing to convert — turns (ns, np) are a dimensionless ratio and Vp is already given in volts (SI).

**F:** Vs = Vp × (ns ÷ np)

**I:** Vp = 230,000 V; np = 2000; ns = 100

**F:** Vs = 230,000 × (100 ÷ 2000) = 230,000 × 0.05

**A:** Vs = 11,500 V
