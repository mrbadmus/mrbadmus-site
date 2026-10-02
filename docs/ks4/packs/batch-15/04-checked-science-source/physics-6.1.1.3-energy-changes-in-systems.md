# Energy Changes in Systems  (Physics, AQA 6.1.1.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| SHC definition; ΔE = m c Δθ; units (theory 1; equations; variables; key_note) | base | 8464 6.1.1.3 / 8463 4.1.1.3 |
| Rearranging; Δθ = final − initial; g → kg (theory 2; common_mistake; FIFA; q1) | base | 6.1.1.3 / 4.1.1.3; MS 3b, 3c |
| Water's high SHC: heating, cooling, climate (theory 3; q2) | base (context) | 6.1.1.3 / 4.1.1.3 |
| Required practical: SHC by electric heater; E = Pt then rearrange for c; heat loss → c too high (theory 3; rp) | base — **Combined RP14 / Physics RP1** | 8464 6.1.1.3 RP14 / 8463 4.1.1.3 RP1 |
| E = P t (inside the RP) | base | 8464 6.2.4.2 / 8463 4.2.4.2 |
| `higher` | none | — |

True page routes: CF CH TF TH (all base). Site currently ships: CF CH TF TH — matches. The `rp` field's "RP14 (Physics)" is the Combined number; the badge must read RP14 on CF/CH and RP1 on TF/TH (flag ENERGY-CHANGES-IN-SYSTEMS-F1).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Use specific heat capacity to calculate energy changes when substances are heated or cooled.

## theory
```json
[
  {
    "content": "Different materials need DIFFERENT amounts of energy to raise their temperature by the same amount. This is described by SPECIFIC HEAT CAPACITY (c).\n\nDEFINITION:\nThe specific heat capacity of a substance is the amount of energy needed to raise the temperature of 1 kg of the substance by 1°C.\n\nEQUATION:\nΔE = m × c × Δθ\n\nΔE = change in thermal energy (J)\nm = mass (kg)\nc = specific heat capacity (J/kg°C)\nΔθ = temperature change (°C)\n\nCommon SHC values:\nWater: 4200 J/kg°C\nAluminium: 900 J/kg°C\nIron/steel: 450 J/kg°C\nCopper: 385 J/kg°C\n\nWater has a very HIGH SHC — it takes a lot of energy to heat it. This makes it ideal for carrying and storing thermal energy.",
    "heading": "Specific Heat Capacity"
  },
  {
    "content": "The equation ΔE = mcΔθ can be rearranged:\nΔθ = ΔE ÷ (m × c)\nm = ΔE ÷ (c × Δθ)\nc = ΔE ÷ (m × Δθ)\n\nEXAMPLE 1 — Energy needed:\nHeat 2 kg of water from 20°C to 100°C:\nΔθ = 100 − 20 = 80°C\nΔE = 2 × 4200 × 80 = 672,000 J = 672 kJ\n\nEXAMPLE 2 — Temperature change:\n27,000 J heats a 3 kg aluminium block (c = 900 J/kg°C):\nΔθ = 27,000 ÷ (3 × 900) = 27,000 ÷ 2700 = 10°C\n\nThe same equation applies when objects COOL — ΔE is the energy released.",
    "heading": "Using the SHC Equation"
  },
  {
    "content": "WHY WATER IS USED IN RADIATORS AND COOLING SYSTEMS:\nHigh SHC = carries large amounts of thermal energy per kg per °C → less water needed to heat a room.\nCar cooling systems: water absorbs heat from the engine efficiently.\nOceans: high SHC means they absorb huge amounts of solar energy → moderate coastal climates.\n\nREQUIRED PRACTICAL:\nRP14 — Determine the SHC of a material:\nHeat a known mass with an electric heater of known power.\nRecord temperature change over time.\nEnergy input: E = P × t\nCompare to ΔE = mcΔθ → rearrange for c.\n\nSOURCES OF ERROR in RP14:\nHeat loss to surroundings → measured c higher than true value.\nHeat not fully transferred to material → same direction of error.\nMinimise by lagging (insulating) the material being heated.",
    "heading": "Applications of Specific Heat Capacity"
  }
]
```

## common_mistake

Temperature change (Δθ) is final temperature MINUS initial temperature — not the final temperature alone. If water heats from 20°C to 60°C, Δθ = 40°C, not 60°C. Also: mass must be in kg — convert grams first (÷1000).

## key_note

SHC (c): energy to raise 1 kg by 1°C. ΔE = mcΔθ. Water c = 4200 J/kg°C (very high). Δθ = final − initial. Rearrange for any unknown. RP14: electric heater method. High SHC of water → used in heating systems and car cooling.

## equations
```json
[
  "ΔE = m × c × Δθ"
]
```

## fifas
```json
[
  {
    "label": "SHC Calculation",
    "question": "How much energy is needed to heat 0.5 kg of water from 25°C to 85°C? (c = 4200 J/kg°C)",
    "steps": [
      [
        "F",
        "ΔE = m × c × Δθ"
      ],
      [
        "I",
        "m = 0.5 kg, c = 4200, Δθ = 85 − 25 = 60°C"
      ],
      [
        "F",
        "ΔE = 0.5 × 4200 × 60 = 0.5 × 252,000"
      ],
      [
        "A",
        "ΔE = 126,000 J (126 kJ)"
      ]
    ]
  }
]
```

## rp

RP14 (Physics) — Determine the specific heat capacity of a material using an electric heater, thermometer and balance. E = Pt gives energy input; rearrange ΔE = mcΔθ to find c.

## variables
```json
[
  [
    "ΔE",
    "Change in thermal energy",
    "joules",
    "J"
  ],
  [
    "m",
    "Mass",
    "kilograms",
    "kg"
  ],
  [
    "c",
    "Specific heat capacity",
    "J/kg°C",
    "J/kg°C"
  ],
  [
    "Δθ",
    "Temperature change",
    "degrees Celsius",
    "°C"
  ]
]
```

## matching
```json
{
  "instruction": "Match each substance and application to the correct SHC fact.",
  "pairs": [
    [
      "Water (c = 4200 J/kg°C)",
      "Highest common SHC — used in central heating, car cooling, moderates ocean climate"
    ],
    [
      "Aluminium (c = 900 J/kg°C)",
      "Higher SHC than iron — heats more slowly for same energy input"
    ],
    [
      "Δθ = final − initial temp",
      "Temperature CHANGE — not the final temperature alone"
    ],
    [
      "ΔE = mcΔθ",
      "Calculates thermal energy change for any heating or cooling process"
    ]
  ],
  "title": "SHC Application Match"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "108,000 J — ΔE = 2 × 450 × 120 = 108,000 J (Δθ = 150 − 30 = 120°C)",
        true
      ],
      [
        "27,000 J — used final temperature (30°C) not temperature change (120°C)",
        false
      ],
      [
        "135,000 J — used initial temperature (150°C) not temperature change",
        false
      ],
      [
        "1350 J — divided instead of multiplied",
        false
      ]
    ],
    "q": "A 2 kg iron block (c = 450 J/kg°C) cools from 150°C to 30°C. How much energy is released?",
    "wrong_explanations": {
      "1": "Δθ = 150 − 30 = 120°C is the temperature CHANGE. Using 30°C gives ΔE = 2 × 450 × 30 = 27,000 J — using the final temperature, not the change.",
      "2": "Δθ is not the initial temperature — it is the CHANGE (150 − 30 = 120). 2 × 450 × 150 = 135,000 J is too large.",
      "3": "ΔE = m × c × Δθ requires multiplication — 2 × 450 × 120 = 108,000 J."
    }
  },
  {
    "opts": [
      [
        "Water has a very high SHC (4200 J/kg°C) — it carries large amounts of thermal energy per kg per °C rise, so less water is needed",
        true
      ],
      [
        "Water has a low SHC — it heats up quickly so the system responds faster",
        false
      ],
      [
        "Water is denser than most liquids — it carries more energy due to its mass",
        false
      ],
      [
        "Water has zero SHC at 100°C — it conducts heat perfectly at boiling point",
        false
      ]
    ],
    "q": "Why is water used in central heating systems rather than a cheaper liquid?",
    "wrong_explanations": {
      "1": "The opposite is true — water's HIGH SHC is the key property. A low SHC would mean it heats quickly but also loses heat quickly and carries less energy.",
      "2": "Water is less dense than many metals — density is not the primary reason it's used in heating systems.",
      "3": "SHC doesn't become zero at any temperature — SHC is a property of the material, roughly constant over normal temperature ranges."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** How much energy is needed to heat 0.5 kg of water from 25°C to 85°C? (c = 4200 J/kg°C)

**Convert:** [NEW — examiner-corrected] Nothing to convert — mass is already in kg and c is already in J/kg°C. Working out Δθ = 85 − 25 = 60°C is part of Insert, not a unit conversion.

**F:** ΔE = m × c × Δθ

**I:** m = 0.5 kg, c = 4200, Δθ = 85 − 25 = 60°C

**F:** ΔE = 0.5 × 4200 × 60 = 0.5 × 252,000

**A:** ΔE = 126,000 J (126 kJ)
