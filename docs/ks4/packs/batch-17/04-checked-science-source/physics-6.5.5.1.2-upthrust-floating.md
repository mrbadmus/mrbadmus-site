# Upthrust and Floating  (Physics, AQA 6.5.5.1.2 (HT only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Upthrust from greater pressure on the bottom than the top (theory 1) | triple-higher | 8463 4.5.5.1.2 (HT only) |
| Floats when upthrust = weight; density comparison; ships; submarines (theory 1–3; key_note) | triple-higher | 8463 4.5.5.1.2 (HT only) |
| "A denser object displaces less volume before sinking" (theory 1) | WRONG (UPF-F2) | 8463 4.5.5.1.2 |
| Archimedes; Upthrust = ρVg; fraction submerged (theory 1–3; equations; variables; key_note; common_mistake; `higher`) | off-spec (UPF-F1) | — |
| Finding density by weighing in water (theory 3) | off-spec (UPF-F4) | — |
| FIFA (ρVg) | off-spec — not usable | — |
| quiz q1 | off-spec — not usable | — |
| quiz q2 | off-spec — not usable | — |

True page routes: TH. Site currently ships: TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain upthrust using pressure differences and apply Archimedes' principle to floating.

## theory
```json
[
  {
    "content": "UPTHRUST is the upward force on an object submerged in a fluid.\n\nCAUSE:\nPressure increases with depth: P = hρg.\nPressure on the BOTTOM of a submerged object > pressure on the TOP.\nNet upward force = pressure difference × cross-sectional area = UPTHRUST.\n\nARCHIMEDES' PRINCIPLE:\nUpthrust = weight of fluid displaced by the object.\nUpthrust = ρ_fluid × V_displaced × g\n\nwhere V_displaced = volume of the object submerged in the fluid.\n\nFLOATING CONDITION:\nObject floats when upthrust = weight.\nThe object sinks until it has displaced enough fluid for the upthrust to equal its weight.\nA denser object displaces less volume before sinking — if density > fluid, it fully submerges and still sinks (upthrust < weight).",
    "heading": "Upthrust from Pressure Difference"
  },
  {
    "content": "WORKED EXAMPLE:\nA wooden block of volume 0.01 m³ and density 600 kg/m³ floats in water (ρ = 1000 kg/m³).\nWeight of block = 600 × 0.01 × 10 = 60 N.\nFor floating: upthrust = 60 N.\nVolume of water displaced: 60 = 1000 × V × 10 → V = 0.006 m³.\nSo 60% of the block is submerged (6/10 of its volume).\n\nFLOATING vs SINKING:\nDensity of object < fluid density → floats (some volume above fluid surface).\nDensity of object = fluid density → neutrally buoyant (hovers at any depth).\nDensity of object > fluid density → sinks (upthrust < weight at full submersion).\n\nWHY SHIPS FLOAT:\nA steel ship is hollow — effective density of hull + air < water density.\nLarge volume displaced → large upthrust = ship's weight.\nIf flooded: air replaced by water → density increases → sinks.",
    "heading": "Applying Archimedes' Principle"
  },
  {
    "content": "UPTHRUST EQUATION:\nUpthrust = ρ_fluid × V_submerged × g\n\nFor a fully submerged object: V_submerged = V_object.\nFor a floating object: V_submerged < V_object (only partially submerged).\n\nFINDING DENSITY OF AN OBJECT:\n1. Weigh in air: W = mg.\n2. Weigh fully submerged in water: W_apparent < W (upthrust reduces apparent weight).\n3. Upthrust = W − W_apparent.\n4. Volume of object = upthrust ÷ (ρ_water × g).\n5. Density of object = mass ÷ volume.\n\nSUBMARINES:\nControl buoyancy by adjusting ballast tanks.\nFill tanks with water → increase density → sink.\nBlow out water with compressed air → decrease density → rise.\nAt neutral buoyancy: density = seawater density.",
    "heading": "Calculating Upthrust"
  }
]
```

## higher

HT only — calculate upthrust using Archimedes' principle. Determine whether objects float or sink by comparing upthrust with weight. Calculate the fraction of a floating object submerged.

## common_mistake

Upthrust = weight of DISPLACED FLUID — not the weight of the object. A 100 N steel block submerged in water experiences upthrust equal to the weight of water it displaces, which is much less than 100 N (since steel is denser than water). This is why it sinks — upthrust < weight.

## key_note

Upthrust = ρ_fluid × V_submerged × g = weight of fluid displaced (Archimedes). Float when upthrust = weight → density_object < density_fluid. Sink when density_object > density_fluid. Ship: hollow hull displaces large volume. Submarine: ballast tanks adjust density.

## equations
```json
[
  "Upthrust = ρ_fluid × V_submerged × g"
]
```

## fifas
```json
[
  {
    "label": "Upthrust Calculation",
    "question": "A block of volume 0.005 m³ is fully submerged in water (ρ = 1000 kg/m³, g = 10 N/kg). Calculate the upthrust.",
    "steps": [
      [
        "F",
        "Upthrust = ρ_fluid × V_submerged × g"
      ],
      [
        "I",
        "ρ = 1000 kg/m³, V = 0.005 m³, g = 10 N/kg"
      ],
      [
        "F",
        "Upthrust = 1000 × 0.005 × 10 = 50"
      ],
      [
        "A",
        "Upthrust = 50 N"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "U",
    "Upthrust",
    "newtons",
    "N"
  ],
  [
    "ρ",
    "Density of fluid",
    "kg/m³",
    "kg/m³"
  ],
  [
    "V",
    "Volume submerged",
    "m³",
    "m³"
  ],
  [
    "g",
    "Gravitational field strength",
    "N/kg",
    "N/kg"
  ]
]
```

## matching
```json
{
  "instruction": "Match each scenario to the correct upthrust or floating explanation.",
  "pairs": [
    [
      "Object with density < water",
      "Floats — partially submerged until upthrust equals weight"
    ],
    [
      "Object with density > water",
      "Sinks — even fully submerged, upthrust < weight"
    ],
    [
      "Upthrust calculation",
      "ρ_fluid × V_submerged × g = weight of fluid displaced"
    ],
    [
      "Submarine rising",
      "Ballast tanks emptied of water — effective density decreases below seawater"
    ]
  ],
  "title": "Upthrust and Floating"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "It sinks — upthrust = 1000 × 0.002 × 10 = 20 N < 30 N weight; net downward force",
        true
      ],
      [
        "It floats — upthrust = 20 N is sufficient to support 30 N",
        false
      ],
      [
        "It hovers — upthrust exactly balances weight",
        false
      ],
      [
        "It rises rapidly — the upthrust of 20 N exceeds the weight",
        false
      ]
    ],
    "q": "A 0.002 m³ object is fully submerged in water (ρ = 1000 kg/m³, g = 10 N/kg). Its weight is 30 N. What happens to it?",
    "wrong_explanations": {
      "1": "20 N < 30 N means upthrust CANNOT balance weight — the object sinks. It would hover only if upthrust = weight (20 N ≠ 30 N).",
      "2": "Upthrust of 20 N does NOT equal weight of 30 N — the object sinks.",
      "3": "For rising, upthrust > weight — here upthrust (20 N) < weight (30 N), so it sinks."
    }
  },
  {
    "opts": [
      [
        "89.5% — ratio of densities: 917/1025 = 0.895 = 89.5% submerged",
        true
      ],
      [
        "10.5% — only the visible part above water is relevant",
        false
      ],
      [
        "50% — objects always float half submerged",
        false
      ],
      [
        "100% — icebergs are fully submerged because ice is denser than water",
        false
      ]
    ],
    "q": "What fraction of a floating iceberg is below water? (Density of ice = 917 kg/m³, seawater = 1025 kg/m³)",
    "wrong_explanations": {
      "1": "10.5% is the fraction ABOVE water — the fraction BELOW is 89.5%.",
      "2": "Only objects with exactly half the density of the fluid float half submerged — fraction submerged = density_object/density_fluid.",
      "3": "Ice (917 kg/m³) is LESS dense than seawater (1025 kg/m³) — it floats. 89.5% is below the surface."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A block of volume 0.005 m³ is fully submerged in water (ρ = 1000 kg/m³, g = 10 N/kg). Calculate the upthrust.

**Convert:** [NEW — examined ✓] Nothing to convert — volume is already in m³, density already in kg/m³ and g already in N/kg, so Upthrust = ρ_fluid × V_submerged × g can be applied directly with no unit change.

**F:** Upthrust = ρ_fluid × V_submerged × g

**I:** ρ = 1000 kg/m³, V = 0.005 m³, g = 10 N/kg

**F:** Upthrust = 1000 × 0.005 × 10 = 50

**A:** Upthrust = 50 N
