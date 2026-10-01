# Efficiency  (Physics, AQA 6.1.2.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Efficiency = useful output energy ÷ total input energy; = useful power output ÷ total power input; decimal or % | base | 8464 6.1.2.2; 8463 4.1.2.2 |
| Wasted = total − useful; dissipation; Sankey diagrams | base | 8464 6.1.2.1–6.1.2.2 |
| Lubrication, thermal insulation reduce unwanted transfers | base | 8464 6.1.2.1; 8463 4.1.2.1 |
| Ways to increase the efficiency of an intended transfer (theory 3 frame; `higher`, every copy) | higher | 8464 6.1.2.2 (HT only); 8463 4.1.2.2 (HT only) |
| fifas; quiz q1, q2 | base | 8464 6.1.2.2 |

True page routes: CF CH TF TH (higher layer CH TH only — the CF/TF `higher` copies must not be shown; see `_flags/efficiency.md`).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Calculate efficiency as a decimal or percentage and interpret Sankey diagrams.

## theory
```json
[
  {
    "content": "EFFICIENCY measures what fraction of total input energy becomes USEFUL output.\n\nNo device is 100% efficient — some energy is always dissipated as thermal energy or sound.\n\nEQUATIONS:\nefficiency = useful output energy ÷ total input energy\nefficiency = useful power output ÷ total power input\n\nExpress as:\nDECIMAL: 0 to 1 (e.g. 0.75)\nPERCENTAGE: multiply decimal by 100 (e.g. 75%)\n\nMax efficiency = 1 (100%) — impossible in practice.\n\nEXAMPLE:\nMotor: 200 J electrical input, 150 J useful mechanical output, 50 J wasted as heat.\nEfficiency = 150 ÷ 200 = 0.75 = 75%\nWasted = 200 − 150 = 50 J",
    "heading": "Efficiency — Definition and Equations"
  },
  {
    "content": "A SANKEY DIAGRAM shows energy transfers visually:\nArrow WIDTH is proportional to the amount of energy.\nInput arrow on the left. Useful output arrow goes right. Wasted outputs go downward.\n\nReading a Sankey diagram:\nEfficiency = width of useful output ÷ width of input arrow.\nThe input arrow = sum of ALL output arrows.\n\nEXAMPLE — incandescent bulb (very inefficient):\nInput: 100 J electrical\nUseful light output: 10 J (thin right arrow)\nWasted heat: 90 J (wide downward arrow)\nEfficiency = 10 ÷ 100 = 0.10 = 10%\n\nEXAMPLE — LED bulb (efficient):\nInput: 100 J\nUseful light: 90 J\nWasted heat: 10 J\nEfficiency = 90 ÷ 100 = 0.90 = 90%",
    "heading": "Sankey Diagrams"
  },
  {
    "content": "REDUCE FRICTION: lubricate moving parts → less thermal wasted.\nREDUCE AIR RESISTANCE: streamlined shapes → less energy to air.\nBETTER INSULATION: less thermal energy escapes hot devices.\nBETTER COMPONENTS: LED lights instead of filament bulbs → more light, less heat.\nREGENERATIVE BRAKING: hybrid/electric cars capture braking KE → stored in battery rather than wasted as thermal.\n\nWHY EFFICIENCY MATTERS:\nHigher efficiency → less fuel for same useful output → lower costs.\nLess fuel → less CO₂ → lower environmental impact.\nBut: no device can exceed 100% efficiency.",
    "heading": "Improving Efficiency"
  }
]
```

## higher

Describe and evaluate specific methods to increase the efficiency of a given energy transfer — e.g. lubrication reduces friction losses, streamlining reduces air resistance, thermal insulation reduces heat loss, LED technology reduces thermal waste in lighting, regenerative braking recovers kinetic energy. Evaluate cost-effectiveness and practicality of each improvement.

## common_mistake

Efficiency = useful output ÷ TOTAL INPUT — not useful ÷ wasted. Result must be ≤ 1 (≤ 100%). If your answer exceeds 1, you have divided the wrong way. Wasted energy = total input − useful output (not the denominator).

## key_note

Efficiency = useful output ÷ total input (decimal, 0–1) or × 100 for %. Wasted = total − useful. Sankey diagrams: arrow width ∝ energy amount. Improve: reduce friction (lube), reduce air resistance (streamline), reduce heat loss (insulation), use LEDs. Max efficiency = 100% (never exceeded).

## equations
```json
[
  "efficiency = useful output energy ÷ total input energy",
  "efficiency = useful power output ÷ total power input",
  "efficiency (%) = (useful output ÷ total input) × 100"
]
```

## fifas
```json
[
  {
    "label": "Efficiency Calculation",
    "question": "A car engine uses 20,000 J of chemical energy and produces 7,000 J of useful kinetic energy. Calculate its efficiency.",
    "steps": [
      [
        "F",
        "efficiency = useful output energy ÷ total input energy"
      ],
      [
        "I",
        "efficiency = 7000 ÷ 20,000"
      ],
      [
        "F",
        "efficiency = 0.35"
      ],
      [
        "A",
        "efficiency = 0.35 (35%)"
      ]
    ]
  }
]
```

## matching
```json
{
  "instruction": "Match each device to its efficiency.",
  "pairs": [
    [
      "0.75 (75%)",
      "Motor: 300 J input, 225 J useful mechanical output — 225÷300"
    ],
    [
      "0.10 (10%)",
      "Incandescent bulb: 100 J electrical, 10 J light — 10÷100"
    ],
    [
      "0.40 (40%)",
      "Engine: 500 J chemical, 200 J kinetic — 200÷500"
    ],
    [
      "0.90 (90%)",
      "LED lamp: 100 J electrical, 90 J light — 90÷100"
    ]
  ],
  "title": "Efficiency Values"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "200 J — useful = 0.6 × 500 = 300 J; wasted = 500 − 300 = 200 J",
        true
      ],
      [
        "300 J — this is the useful output, not the wasted amount",
        false
      ],
      [
        "500 J — all energy is wasted at efficiency 0.6",
        false
      ],
      [
        "833 J — dividing 500 ÷ 0.6",
        false
      ]
    ],
    "q": "A device has efficiency 0.6 and is supplied with 500 J. How much energy is wasted?",
    "wrong_explanations": {
      "1": "300 J is the USEFUL output (60% of 500). WASTED = total − useful = 500 − 300 = 200 J.",
      "2": "At efficiency 0.6, only 40% (200 J) is wasted — not all 500 J.",
      "3": "500 ÷ 0.6 = 833 J: this would be the input needed to get 500 J useful output, not the wasted energy."
    }
  },
  {
    "opts": [
      [
        "89 J/s — LED wastes 1 J/s, bulb wastes 90 J/s; difference = 89 J/s",
        true
      ],
      [
        "0 J/s — both produce the same useful light so waste must be equal",
        false
      ],
      [
        "10 J/s — the useful output is 10 J/s so waste is also 10 J/s",
        false
      ],
      [
        "100 J/s — the bulb uses 100 J/s so wastes all of it",
        false
      ]
    ],
    "q": "An LED uses 11 J/s total and produces 10 J/s of light. A filament bulb produces the same 10 J/s of light but uses 100 J/s. How much more energy per second does the bulb waste?",
    "wrong_explanations": {
      "1": "Same USEFUL output does NOT mean same waste. LED: wastes 11 − 10 = 1 J/s. Bulb: wastes 100 − 10 = 90 J/s. Difference = 89 J/s.",
      "2": "Wasted = total − useful. The TOTAL inputs are very different (11 vs 100 J/s).",
      "3": "Bulb uses 100 J/s but 10 J/s is useful light — it wastes 90 J/s, not 100 J/s."
    }
  }
]
```

## higher — Combined Foundation copy (differs from the Triple Higher copy above)

Describe specific ways to increase efficiency for a given device or system and justify each: lubrication reduces friction losses, streamlining reduces air resistance, thermal insulation reduces heat loss to surroundings, regenerative braking captures KE. Evaluate cost vs benefit of efficiency improvements.

## higher — Triple Foundation copy (differs from the Triple Higher copy above)

Describe specific ways to increase efficiency for a given device or system and justify each: lubrication reduces friction losses, streamlining reduces air resistance, thermal insulation reduces heat loss to surroundings, regenerative braking captures KE. Evaluate cost vs benefit of efficiency improvements.

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A car engine uses 20,000 J of chemical energy and produces 7,000 J of useful kinetic energy. Calculate its efficiency.

**Convert:** [NEW — examined ✓] Nothing to convert — both quantities already in SI units: joules (J).

**F:** efficiency = useful output energy ÷ total input energy

**I:** efficiency = 7000 ÷ 20,000

**F:** efficiency = 0.35

**A:** efficiency = 0.35 (35%)
