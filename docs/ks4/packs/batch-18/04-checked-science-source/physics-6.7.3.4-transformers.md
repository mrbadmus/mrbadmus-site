# Transformers  (Physics, AQA 6.7.3.4 (HT only, physics only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
True spec reference: **8463 4.7.3.4 Transformers (HT only)**, under 4.7.3 "(physics only) (HT only)"; Vp Ip = Vs Is is also **8464 6.2.4.3 (Higher tier only)**; the National Grid points are 8464 6.2.4.3 / 8463 4.2.4.3 (base). The `spec` field "6.7.3.4" is the site's internal number.

| point | layer | spec ref |
|---|---|---|
| Construction: primary, secondary, iron core ("easily magnetised") (theory 1) | triple-higher | 8463 4.7.3.4 |
| ac in primary induces pd in secondary; dc gives nothing (theory 1; common_mistake; q1) | triple-higher | 8463 4.7.3.4 |
| Vp/Vs = np/ns; step-up / step-down by turns (theory 2; equations; FIFA; key_note) | triple-higher | 8463 4.7.3.4 |
| Vp Ip = Vs Is; voltage up → current down (theory 2; equations; common_mistake) | higher | 8464 6.2.4.3 (HT); 8463 4.7.3.4 |
| Step-up for transmission, step-down for homes; high pd → low current → less I²R loss (theory 3; common_mistake; q2) | base | 8464 6.2.4.3, 6.2.4.1 |
| Eddy currents, laminations, flux leakage (theory 3) | excluded by the spec — F2 | 8463 4.7.3.4 |
| quiz q1 | triple-higher — usable | 8463 4.7.3.4 |
| quiz q2 | base — usable | 8464 6.2.4.3 |
| FIFA | triple-higher — usable | 8463 4.7.3.4 |

True page routes: TH. Site currently ships: TH — matches. (Vp Ip = Vs Is reaches Combined Higher on `national-grid`, not here — TRANSFORMERS-F6.)

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how transformers work and use the transformer equation to solve problems.

## theory
```json
[
  {
    "content": "A TRANSFORMER changes the voltage of an alternating current supply.\n\nCONSTRUCTION:\nTwo coils of wire wound onto an IRON CORE:\nPRIMARY COIL: connected to the input AC supply (Vₚ).\nSECONDARY COIL: provides the output voltage (Vₛ).\nSOFT IRON CORE: channels magnetic flux between the coils efficiently.\n\nOPERATION (mutual induction):\n1. AC in primary coil → ALTERNATING MAGNETIC FIELD in the iron core.\n2. Alternating magnetic flux threads through the secondary coil.\n3. Changing flux induces an EMF in the secondary coil (Faraday's Law).\n4. Output voltage depends on the ratio of turns.\n\nCRITICAL: Transformers only work with AC — DC produces a CONSTANT magnetic flux, which does not change and therefore induces no emf.",
    "heading": "How Transformers Work"
  },
  {
    "content": "TURNS RATIO EQUATION:\nVₛ/Vₚ = Nₛ/Nₚ\n\nWhere:\nVₛ = secondary (output) voltage (V)\nVₚ = primary (input) voltage (V)\nNₛ = number of turns on secondary coil\nNₚ = number of turns on primary coil\n\nSTEP-UP TRANSFORMER: Nₛ > Nₚ → Vₛ > Vₚ (increases voltage).\nSTEP-DOWN TRANSFORMER: Nₛ < Nₚ → Vₛ < Vₚ (decreases voltage).\n\nPOWER CONSERVATION (for ideal transformer):\nPower in = Power out\nVₚ × Iₚ = Vₛ × Iₛ\n\nTherefore: Vₚ/Vₛ = Iₛ/Iₚ\nStep-up voltage → step-down current (and vice versa).\n\nEXAMPLE:\nPrimary: 230 V, 100 turns. Secondary: what voltage if 500 turns?\nVₛ = Vₚ × (Nₛ/Nₚ) = 230 × (500/100) = 1150 V.",
    "heading": "Transformer Equations"
  },
  {
    "content": "NATIONAL GRID uses transformers to transmit electricity efficiently.\n\nPOWER STATION → STEP-UP TRANSFORMER → HIGH VOLTAGE TRANSMISSION → STEP-DOWN TRANSFORMER → CONSUMERS\n\nTypically: 25 kV (power station) → 400 kV (transmission) → 33 kV (industrial) → 11 kV → 230 V (homes).\n\nWHY HIGH VOLTAGE FOR TRANSMISSION:\nP = V × I. To transmit a given power P at high voltage → LOW current needed.\nP_lost = I² × R (power lost in cable resistance).\nLow current → much less power wasted in transmission cables.\n\nEXAMPLE:\nTransmit 100 MW at 1000 V vs 1,000,000 V:\nAt 1000 V: I = 100,000 A → P_loss = 100,000² × R (enormous).\nAt 1,000,000 V: I = 100 A → P_loss = 100² × R (10,000 times less).\n\nENERGY LOSSES IN REAL TRANSFORMERS:\nEddy currents in the iron core — reduced by using laminated core.\nResistance heating in coil wires — use thick copper wire.\nMagnetic flux leakage — tight winding, soft iron core.\nReal transformers: ~95–99% efficient.",
    "heading": "Transformers in the National Grid"
  }
]
```

## higher

HT only — use the turns ratio equation to calculate transformer voltages and turns. Apply power conservation to find current in transformer circuits. Explain why the National Grid uses high voltage transmission and calculate power losses at different voltages.

## common_mistake

Transformers only work with AC — not DC. DC produces constant flux → no change → no induced emf. Step-up transformer increases VOLTAGE but DECREASES current (power is conserved). National Grid uses high voltage to REDUCE current → reduces I²R power losses in transmission cables.

## key_note

Transformer: AC in primary → alternating flux in iron core → emf induced in secondary. Turns ratio: Vs/Vp = Ns/Np. Step-up: Ns > Np. Power conservation: Vp×Ip = Vs×Is. National Grid: step-up to ~400 kV for transmission (low current → less I²R loss), step-down for consumers. AC only — DC gives constant flux, no induction.

## equations
```json
[
  "Vₛ/Vₚ = Nₛ/Nₚ  (turns ratio equation)",
  "Vₚ × Iₚ = Vₛ × Iₛ  (power conservation in ideal transformer)"
]
```

## fifas
```json
[
  {
    "label": "Transformer Voltage",
    "question": "A transformer has 200 primary turns and 800 secondary turns. Input voltage = 230 V. Find the output voltage.",
    "steps": [
      [
        "F",
        "Vs/Vp = Ns/Np"
      ],
      [
        "I",
        "Vp = 230 V, Np = 200, Ns = 800"
      ],
      [
        "F",
        "Vs = Vp × (Ns/Np) = 230 × (800/200) = 230 × 4"
      ],
      [
        "A",
        "Vs = 920 V (step-up transformer)"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "Vₚ",
    "Primary voltage",
    "volts",
    "V"
  ],
  [
    "Vₛ",
    "Secondary voltage",
    "volts",
    "V"
  ],
  [
    "Nₚ",
    "Number of primary turns",
    "",
    ""
  ],
  [
    "Nₛ",
    "Number of secondary turns",
    "",
    ""
  ]
]
```

## matching
```json
{
  "instruction": "Match each transformer scenario to the correct calculation.",
  "pairs": [
    [
      "Step-up transformer",
      "Ns > Np → output voltage greater than input voltage"
    ],
    [
      "Step-down transformer",
      "Ns < Np → output voltage less than input voltage"
    ],
    [
      "National Grid transmission",
      "Step-up to ~400 kV → low current → low I²R losses in cables"
    ],
    [
      "Power conservation",
      "Vp × Ip = Vs × Is — higher voltage means lower current"
    ]
  ],
  "title": "Transformer Equations"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "DC produces a constant magnetic flux — no change in flux means no induced emf in the secondary coil (Faraday's law requires changing flux)",
        true
      ],
      [
        "DC is too powerful for the iron core — it would overheat and be destroyed",
        false
      ],
      [
        "DC cannot flow through coils of wire — coils require AC to function",
        false
      ],
      [
        "DC has a frequency of zero — transformers are calibrated for 50 Hz only",
        false
      ]
    ],
    "q": "Why can't transformers work with direct current (DC)?",
    "wrong_explanations": {
      "1": "DC can flow through transformer coils and would create a magnetic field — but a CONSTANT field causes no induction.",
      "2": "DC flows through coils perfectly well — it's the absence of CHANGE that prevents transformer action.",
      "3": "Technically DC frequency = 0 Hz, and transformers are designed for 50 Hz — but the fundamental reason is CONSTANT FLUX, not calibration."
    }
  },
  {
    "opts": [
      [
        "High voltage means low current for the same power — less power wasted as heat in cables since P_loss = I²R",
        true
      ],
      [
        "High voltage makes electricity travel faster through the cables",
        false
      ],
      [
        "High voltage prevents energy loss by radiation — lower voltage radiates more energy",
        false
      ],
      [
        "Transformers only work at high voltages — required for transformer compatibility",
        false
      ]
    ],
    "q": "Why does the National Grid transmit electricity at very high voltages?",
    "wrong_explanations": {
      "1": "Electrical signals travel at nearly the speed of light regardless of voltage — voltage doesn't affect transmission speed.",
      "2": "While there is some electromagnetic radiation from power lines, this is not the reason for high voltage — P_loss = I²R is the key formula.",
      "3": "Transformers work at any voltage — the reason for high voltage is specifically to reduce current and therefore reduce I²R heating losses."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A transformer has 200 primary turns and 800 secondary turns. Input voltage = 230 V. Find the output voltage.

**Convert:** [NEW — examiner-corrected] Nothing to convert — the numbers of turns have no unit, and the input potential difference is already in volts, so the answer comes out in volts.

**F:** Vs/Vp = Ns/Np

**I:** Vp = 230 V, Np = 200, Ns = 800

**F:** Vs = Vp × (Ns/Np) = 230 × (800/200) = 230 × 4

**A:** Vs = 920 V (step-up transformer)
