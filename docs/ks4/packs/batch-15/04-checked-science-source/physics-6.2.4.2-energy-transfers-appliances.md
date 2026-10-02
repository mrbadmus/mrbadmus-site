# Energy Transfers in Everyday Appliances  (Physics, AQA 6.2.4.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| appliances transfer energy from batteries / ac mains to motors (kinetic) and heaters (thermal) (theory 1; key_note) | base | 8464 6.2.4.2; 8463 4.2.4.2 |
| E = Pt, t in s; energy depends on power and time (theory 2–3; equations[0]; common_mistake; FIFA; q2) | base | 8464 6.2.4.2; 8463 4.2.4.2 |
| E = QV; work done when charge flows | base — missing from the frozen data (ETA-F4); see section at the end | 8464 6.2.4.2; 8463 4.2.4.2 |
| efficiency remark (theory 1) | base (supporting) | 8464 6.1.2.2; 8463 4.1.2.2 |
| kWh, 1 kWh = 3.6 MJ, cost (theory 2–3; equations[1]; key_note; q1) | beyond spec — not on 8463/8464, not on either sheet (ETA-F1); q1 not usable | — |

True page routes: CF CH TF TH (all base). Matches the site.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Calculate energy transferred using E = Pt, use kWh and describe appliance energy transfers.

## theory
```json
[
  {
    "content": "Every electrical appliance transfers energy from the electrical store:\n\nELECTRIC MOTOR (washing machine, fan, drill): electrical → kinetic + thermal\nELECTRIC HEATER (oven, toaster): electrical → thermal\nLAMP/LED: electrical → light + thermal\nSPEAKER: electrical → sound\nCHARGER: electrical → chemical (battery)\n\nAll appliances dissipate some energy as thermal — no appliance is 100% efficient.",
    "heading": "Energy Transfers in Appliances"
  },
  {
    "content": "E = P × t (joules; time in SECONDS)\n\nEXAMPLE 1:\n2 kW kettle for 3 minutes:\nP = 2000 W, t = 180 s\nE = 2000 × 180 = 360,000 J\n\nKILOWATT-HOUR (kWh) — energy company unit:\nEnergy (kWh) = Power (kW) × time (hours)\n1 kWh = 3,600,000 J\n\nEXAMPLE 2:\n3 kW shower for 0.5 hours:\nEnergy = 3 × 0.5 = 1.5 kWh",
    "heading": "Calculating Energy Transferred"
  },
  {
    "content": "Cost = energy (kWh) × price per kWh\n\nEXAMPLE:\n1.5 kWh at 30p per kWh = 45p\n\nCOMPARING APPLIANCES:\nHigh power × short time vs low power × long time:\nFridge: 200 W × 24 h = 4.8 kWh/day\nKettle: 2 kW × 5 min/day ≈ 0.17 kWh/day\nFridge uses far more despite lower power — it runs continuously.\n\nREDUCING ENERGY USE:\nLED bulbs instead of filament.\nShorter usage times.\nBetter insulation → less heating demand.",
    "heading": "Energy Cost and Comparison"
  }
]
```

## common_mistake

For E = Pt in joules, time must be in SECONDS. For kWh, use kW and hours. Mixing units is the most common error. High-power appliance used briefly can use LESS energy than a low-power one running for hours.

## key_note

E = Pt (J, t in seconds). kWh = kW × hours. 1 kWh = 3.6 MJ. Cost = kWh × price/unit. Motor → kinetic; heater → thermal; lamp → light; speaker → sound; charger → chemical.

## equations
```json
[
  "E = P × t",
  "Energy (kWh) = Power (kW) × time (hours)"
]
```

## fifas
```json
[
  {
    "label": "Energy Calculation",
    "question": "A 1.5 kW toaster is used for 4 minutes. Calculate the energy transferred in joules.",
    "steps": [
      [
        "F",
        "E = P × t"
      ],
      [
        "I",
        "P = 1500 W, t = 4 × 60 = 240 s"
      ],
      [
        "F",
        "E = 1500 × 240"
      ],
      [
        "A",
        "E = 360,000 J (360 kJ)"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "E",
    "Energy transferred",
    "joules",
    "J"
  ],
  [
    "P",
    "Power",
    "watts",
    "W"
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
  "instruction": "Match each appliance to its primary useful energy output.",
  "pairs": [
    [
      "Electric motor",
      "Kinetic energy — spinning drum, fan or drill"
    ],
    [
      "Electric heater",
      "Thermal energy — heating room or food"
    ],
    [
      "Lamp/LED",
      "Light — plus thermal as waste"
    ],
    [
      "Speaker",
      "Sound — kinetic energy of vibrating air"
    ],
    [
      "Phone charger",
      "Chemical energy — stored in rechargeable battery"
    ]
  ],
  "title": "Appliance Energy Transfers"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "6 kWh and £1.50 — 2 × 3 = 6 kWh; 6 × 25p = 150p",
        true
      ],
      [
        "6000 kWh — used watts not kilowatts: 2000 × 3 = 6000",
        false
      ],
      [
        "0.67 kWh — divided instead of multiplied",
        false
      ],
      [
        "6 kWh and 25p — cost = 1 unit regardless of amount",
        false
      ]
    ],
    "q": "A 2 kW heater runs for 3 hours. How much energy does it use and what does it cost at 25p/kWh?",
    "wrong_explanations": {
      "1": "Must use KILOWATTS: 2 kW × 3 h = 6 kWh. Using 2000 W gives 6000 — wrong unit.",
      "2": "Energy = P × t = 2 kW × 3 h = 6 kWh. Must multiply.",
      "3": "Cost = energy × price per unit = 6 × 25p = 150p = £1.50."
    }
  },
  {
    "opts": [
      [
        "The fridge — 200 W × 24 h = 4.8 kWh vs kettle: 2 kW × (5/60) h ≈ 0.17 kWh",
        true
      ],
      [
        "The kettle — much higher power",
        false
      ],
      [
        "They use the same",
        false
      ],
      [
        "Cannot compare without knowing brands",
        false
      ]
    ],
    "q": "A 200 W fridge runs continuously. A 2000 W kettle runs 5 min/day. Which uses more energy in 24 hours?",
    "wrong_explanations": {
      "1": "Higher power ≠ higher energy use — energy = power × TIME. Fridge runs 24 h; kettle runs only 5 min.",
      "2": "Energy = power × time. Fridge: 0.2 × 24 = 4.8 kWh. Kettle: 2 × (5/60) ≈ 0.17 kWh.",
      "3": "Power and time are all that's needed — brand is irrelevant."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A 1.5 kW toaster is used for 4 minutes. Calculate the energy transferred in joules.

**Convert:** [NEW — examined ✓] TWO conversions: kW → W (1.5 kW = 1500 W) and minutes → seconds (4 min = 4 × 60 = 240 s) — both needed before E = Pt gives joules.

**F:** E = P × t

**I:** P = 1500 W, t = 4 × 60 = 240 s

**F:** E = 1500 × 240

**A:** E = 360,000 J (360 kJ)

## Spec core missing from the frozen data (written from the spec, examiner)

Half of this section's equations (E = QV) and the idea behind it are not in this lesson's frozen data. Verbatim, AQA 8464 6.2.4.2 = 8463 4.2.4.2:

> "Work is done when charge flows in a circuit.
> The amount of energy transferred by electrical work can be calculated using the equation:
> energy transferred = power × time  E = P t
> energy transferred = charge flow × potential difference  E = Q V
> [Students should be able to recall and apply both equations.]
> energy transferred, E, in joules, J; power, P, in watts, W; time, t, in seconds, s; charge flow, Q, in coulombs, C; potential difference, V, in volts, V
> Students should be able to explain how the power of a circuit device is related to:
> • the potential difference across it and the current through it
> • the energy transferred over a given time.
> Students should be able to describe, with examples, the relationship between the power ratings for domestic electrical appliances and the changes in stored energy when they are in use."

E = Q V is printed on both June 2026 equation sheets (8464 and 8463).
