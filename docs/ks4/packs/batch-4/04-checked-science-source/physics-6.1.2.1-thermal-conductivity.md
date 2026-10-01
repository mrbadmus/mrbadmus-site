# Thermal Conductivity and Reducing Unwanted Energy Transfers  (Physics, AQA 6.1.3 (physics only))

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Higher thermal conductivity → higher rate of conduction; metals vs insulators | base | 8464 6.1.2.1; 8463 4.1.2.1 |
| Reducing unwanted transfers: insulation, lubrication (streamlining as a further example) | base | 8464 6.1.2.1 |
| Rate of cooling of a building vs wall thickness and conductivity | base | 8464 6.1.2.1 |
| W/m·K unit and values; k × A × ΔT ÷ thickness | off-spec context ("do not need to know the definition") | 8464 6.1.2.1 |
| "Electromagnetic shielding" | none — wrong (`_flags/thermal-conductivity.md` TC-F2) | — |
| RP2 thermal insulators (theory 3; `rp`) | triple | 8463 4.1.2.1 RP2 (physics only) |
| `higher` (TH) | none — no HT content exists; do not use (TC-F3) | — |
| Quiz q1 | base | 8464 6.1.2.1 |
| Quiz q2 | triple (RP2) — **not usable as written** (TC-F4) | 8463 RP2 |

True page routes: CF CH TF TH (RP2 layer TF TH only). Site currently ships: TF TH; moving under the route-flag PR. Spec field "6.1.3 (physics only)" is wrong → 8464 6.1.2.1 / 8463 4.1.2.1.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain thermal conductivity and describe how insulation reduces unwanted energy transfers.

## theory
```json
[
  {
    "content": "THERMAL CONDUCTIVITY measures how well a material transfers thermal energy by conduction.\n\nGood THERMAL CONDUCTORS: metals (copper, aluminium, iron). Transfer energy quickly. Free electrons carry thermal energy through the material.\n\nGood THERMAL INSULATORS: air, wood, fibreglass, polystyrene, wool. Transfer energy slowly. No free electrons; energy transferred only by vibration between tightly packed or sparse particles.\n\nUnit of thermal conductivity: W/m·K (watts per metre per kelvin).\n\nHigher thermal conductivity → energy transferred faster for the same temperature difference and thickness.\n\nExamples:\nCopper: ~400 W/m·K — excellent conductor.\nGlass: ~1 W/m·K — poor conductor.\nAir: ~0.025 W/m·K — excellent insulator.",
    "heading": "Thermal Conductivity"
  },
  {
    "content": "All energy transfers involve some unwanted dissipation — energy transferred to the thermal store of the surroundings.\n\nMETHODS TO REDUCE THERMAL ENERGY LOSS:\n\n1. INSULATION:\nSurround objects with poor conductors.\nCavity wall insulation (fibreglass or foam) — reduces conduction through walls.\nLoft insulation — reduces conduction through roof.\nDouble-glazing — air gap between panes of glass reduces conduction.\nFoam lagging on hot water pipes — reduces heat loss to surroundings.\n\n2. LUBRICATION:\nReduces friction between moving surfaces.\nLess friction → less thermal energy dissipated.\nMachine oil, grease used in engines, bearings, chains.\n\n3. STREAMLINING:\nReduces air resistance on moving vehicles.\nLess drag → less energy wasted overcoming resistance.\n\n4. ELECTROMAGNETIC SHIELDING:\nReduces energy loss from electrical components.\n\nTHICKNESS AND THERMAL CONDUCTIVITY:\nThicker insulation → less energy transferred per second (for same temperature difference).\nMore insulating material (lower conductivity) → less energy transferred.\nEnergy lost per second ∝ thermal conductivity × area × (temperature difference) ÷ thickness.",
    "heading": "Reducing Unwanted Energy Transfers"
  },
  {
    "content": "REQUIRED PRACTICAL (RP2 — physics only):\nInvestigate the effectiveness of different materials as thermal insulators.\n\nMETHOD:\nWrap beakers of hot water in different materials (wool, bubble wrap, newspaper, foil).\nMeasure temperature of water at regular time intervals.\nPlot temperature-time graphs for each material.\nCompare rate of cooling — steeper gradient = less effective insulator.\n\nVARIABLES:\nIndependent: type of insulating material.\nDependent: rate of cooling (temperature change per unit time).\nControlled: initial temperature, volume of water, thickness of insulation, surface area.\n\nCONCLUSION:\nMaterial with lowest thermal conductivity → slowest cooling → best insulator.\nAir is often the best insulator — sealed air pockets in fibreglass work well.\n\nAPPLICATIONS:\nBuilding insulation — reduces heating bills and carbon footprint.\nRefrigeration — insulated walls slow thermal energy entering the cold space.\nCryogenics — extreme insulation to maintain very low temperatures.",
    "heading": "Required Practical — Thermal Insulation"
  }
]
```

## higher

Describe the factors affecting the rate of thermal conduction: thermal conductivity, thickness and temperature difference. Calculate rate of energy transfer through a material. Evaluate different insulation methods quantitatively using U-values or thermal conductivity data. Explain why double-glazing is more effective with wider gaps.

## common_mistake

INSULATORS do not stop heat transfer — they slow it down. A perfect insulator doesn't exist. Trapped air is one of the best insulators because air is a poor conductor and convection is reduced when it is trapped in small spaces.

## key_note

Thermal conductivity: rate of energy transfer by conduction. Metals = good conductors (free electrons). Air/fibreglass = good insulators. Reducing losses: insulation, lubrication, streamlining. Thicker insulation = less energy lost. RP2: compare materials by rate of cooling.

## rp

RP2 (physics only) — Investigate effectiveness of different thermal insulators. Measure rate of cooling of hot water wrapped in different materials.

## matching
```json
{
  "instruction": "Match each material to its thermal conductivity property.",
  "pairs": [
    [
      "Copper",
      "Very high thermal conductivity — free electrons transfer energy rapidly"
    ],
    [
      "Air (trapped)",
      "Very low thermal conductivity — excellent insulator when trapped"
    ],
    [
      "Cavity wall insulation",
      "Fibreglass with trapped air — reduces energy loss through walls"
    ],
    [
      "Lubrication",
      "Reduces friction between surfaces — less energy wasted as heat"
    ]
  ],
  "title": "Thermal Conductivity"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Air has much lower thermal conductivity than glass — it transfers energy by conduction very slowly",
        true
      ],
      [
        "Air is lighter than glass — lower density means less thermal energy stored",
        false
      ],
      [
        "Glass transmits light which carries thermal energy — air does not",
        false
      ],
      [
        "Air molecules move randomly, transferring energy away from hot objects faster",
        false
      ]
    ],
    "q": "Why is trapped air a better insulator than glass?",
    "wrong_explanations": {
      "1": "Density affects heat capacity but not thermal conductivity directly — air's insulating property comes from its very low thermal conductivity.",
      "2": "Light transmission (transparency) is unrelated to thermal conductivity.",
      "3": "Moving air molecules would increase CONVECTION — trapped air cannot convect, so only slow conduction occurs."
    }
  },
  {
    "opts": [
      [
        "Rate of temperature decrease — steeper temperature-time graph = less effective insulator",
        true
      ],
      [
        "Final temperature after 10 minutes — higher temperature = better conductor",
        false
      ],
      [
        "Mass of insulating material used — more mass = more insulation",
        false
      ],
      [
        "Colour of the insulating material — darker colours absorb more radiation",
        false
      ]
    ],
    "q": "A student investigates thermal insulators by wrapping identical beakers in different materials. Which measurement gives the best comparison?",
    "wrong_explanations": {
      "1": "Final temperature alone doesn't account for starting conditions or time — rate of cooling (gradient) is a fairer comparison.",
      "2": "Mass is not controlled in this way — thickness and type of material matter, not total mass.",
      "3": "Colour affects radiation absorption — relevant for infrared studies but not primary factor in conduction-based insulation tests."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
