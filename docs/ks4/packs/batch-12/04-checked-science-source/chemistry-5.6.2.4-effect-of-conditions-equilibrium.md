# Effect of Changing Conditions on Equilibrium  (Chemistry, AQA 5.6.2.4–5.6.2.7)

**Appears on routes:** Combined Higher, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Le Chatelier: system counteracts a change; catalyst does not shift position (theory 1; key_note) | higher | 8464 5.6.2.4; 8462 4.6.2.4 (HT only) |
| Concentration changes (theory 2; key_note) | higher | 8464 5.6.2.5 (HT only) |
| Pressure changes; counting gas molecules (theory 2; key_note; q1) | higher. q1 wx1 WRONG (F2) | 8464 5.6.2.7 (HT only) |
| Temperature changes; N₂ + 3H₂ ⇌ 2NH₃, ΔH = −92 kJ/mol (theory 3; equations; key_note) | higher | 8464 5.6.2.6 (HT only) |
| Haber compromise: ~450 °C, ~200 atm, iron; rate vs yield (theory 3; key_note; q2) | triple-higher (F3) | 8462 4.10.4.1 (chemistry only; trade-off HT only) |
| common_mistake sentences 2–3 ("determined by temperature only … equilibrium constant") | WRONG and off-spec: do not use (F1) | 8464 5.6.2.5, 5.6.2.7 |
| Equal-molecules (no shift) case; unfamiliar given equations | higher. Missing from the frozen data (F5) | 8464 5.6.2.4, 5.6.2.7 |

True page routes: CH TH (whole page HT), with a Triple Higher layer (Haber compromise) on TH only. Site currently ships: CH TH, which matches; the Haber content and q2 are also served on CH (flagged, F3).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Apply Le Chatelier's principle to predict how changes in concentration, temperature and pressure affect equilibrium.

## theory
```json
[
  {
    "content": "LE CHATELIER'S PRINCIPLE states:\nIf a system at equilibrium is disturbed by a change in conditions, the equilibrium will SHIFT in the direction that OPPOSES the change.\n\nThis is a prediction tool — it allows chemists to predict the effect of changes WITHOUT knowing the detailed kinetics.\n\nTypes of changes:\n1. Changing CONCENTRATION of a reactant or product.\n2. Changing TEMPERATURE.\n3. Changing PRESSURE (for gaseous reactions).\n\nThe system responds by shifting the equilibrium position LEFT (→ more reactants) or RIGHT (→ more products).\n\nNote: a catalyst DOES NOT shift the equilibrium position — it speeds up BOTH forward and reverse reactions equally, so equilibrium is reached FASTER but the position is unchanged.",
    "heading": "Le Chatelier's Principle"
  },
  {
    "content": "CHANGING CONCENTRATION:\nINCREASE concentration of REACTANT → equilibrium shifts RIGHT (→ uses up added reactant, making more product).\nINCREASE concentration of PRODUCT → equilibrium shifts LEFT (← uses up added product, making more reactant).\nREMOVE a product → equilibrium shifts RIGHT to replace it.\n\nExample: N₂ + 3H₂ ⇌ 2NH₃\nAdd more N₂ → equilibrium shifts right → more NH₃ produced.\nRemove NH₃ → equilibrium shifts right → more NH₃ produced.\n\nCHANGING PRESSURE (for gaseous reactions):\nINCREASE pressure → equilibrium shifts towards FEWER moles of gas (to reduce pressure).\nDECREASE pressure → equilibrium shifts towards MORE moles of gas (to increase pressure).\n\nExample: N₂ + 3H₂ ⇌ 2NH₃\nLeft side: 1 + 3 = 4 moles of gas. Right side: 2 moles of gas.\nINCREASE pressure → shifts RIGHT (2 moles) → more NH₃.\nDECREASE pressure → shifts LEFT (4 moles) → less NH₃.",
    "heading": "Effect of Concentration and Pressure"
  },
  {
    "content": "CHANGING TEMPERATURE:\nINCREASE temperature → equilibrium shifts in the ENDOTHERMIC direction.\nDECREASE temperature → equilibrium shifts in the EXOTHERMIC direction.\n\nWhy: the system absorbs the added heat energy by shifting in the endothermic direction, opposing the temperature increase.\n\nExample: N₂ + 3H₂ ⇌ 2NH₃    ΔH = −92 kJ/mol (forward reaction exothermic)\nINCREASE temperature → shifts LEFT (endothermic direction) → less NH₃.\nDECREASE temperature → shifts RIGHT (exothermic direction) → more NH₃.\n\nTHE HABER PROCESS — compromise conditions:\nHigh pressure (200 atm) → favours right (fewer moles of gas) → more NH₃.\nLow temperature → favours right (exothermic) → more NH₃ BUT reaction too slow.\nCompromise temperature ~450°C → fast enough rate, acceptable yield.\nIron catalyst → speeds up reaching equilibrium WITHOUT changing position.\n\nThis shows the trade-off in industrial chemistry: conditions that maximise yield often slow the rate, requiring a catalyst to compensate.",
    "heading": "Effect of Temperature"
  }
]
```

## common_mistake

A catalyst DOES NOT change the equilibrium position — it only speeds up reaching equilibrium. Equilibrium position is determined by temperature only (not concentration or pressure — those affect AMOUNTS but not the equilibrium constant). Temperature is the ONLY factor that changes the equilibrium constant itself.

## key_note

Le Chatelier: equilibrium shifts to OPPOSE any change. Increase reactant conc → shifts right. Increase pressure → shifts to fewer gas moles. Increase temperature → shifts in endothermic direction. Catalyst: faster equilibrium, same position. Haber: high P (more NH₃) + compromise T + Fe catalyst.

## equations
```json
[
  "N₂(g) + 3H₂(g) ⇌ 2NH₃(g)    ΔH = −92 kJ/mol  (Haber process)"
]
```

## matching
```json
{
  "instruction": "For N₂ + 3H₂ ⇌ 2NH₃ (forward = exothermic), predict the effect of each change.",
  "pairs": [
    [
      "Equilibrium shifts right — more NH₃",
      "Increase concentration of N₂ (more reactant added)"
    ],
    [
      "Equilibrium shifts right — more NH₃",
      "Increase pressure (right has fewer moles: 2 vs 4)"
    ],
    [
      "Equilibrium shifts left — less NH₃",
      "Increase temperature (forward is exothermic; reverse is endothermic — heat drives reverse)"
    ],
    [
      "No change in position",
      "Add iron catalyst — same equilibrium position, reached faster"
    ],
    [
      "Equilibrium shifts right — more NH₃",
      "Remove NH₃ as it forms — system produces more to replace it"
    ]
  ],
  "title": "Le Chatelier's Principle Predictions"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Left side has 3 moles of gas (2+1), right has 2 — increasing pressure favours fewer moles (right) to reduce pressure",
        true
      ],
      [
        "Increasing pressure gives molecules more energy — SO₃ forms more easily",
        false
      ],
      [
        "Pressure increase always shifts equilibrium right in all reactions",
        false
      ],
      [
        "SO₃ is a gas — pressure increases its formation",
        false
      ]
    ],
    "q": "For the reaction 2SO₂(g) + O₂(g) ⇌ 2SO₃(g), increasing pressure shifts the equilibrium right. Why?",
    "wrong_explanations": {
      "1": "Pressure increase gives more energy to all species equally — the shift is purely about the mole count of gas on each side.",
      "2": "Pressure increase shifts towards FEWER moles of gas — if there were more moles on the right, it would shift LEFT.",
      "3": "All species in this equilibrium are gases — being a gas alone doesn't determine the direction of shift."
    }
  },
  {
    "opts": [
      [
        "At lower temperatures the reaction is too slow — 450°C is a compromise between yield and acceptable rate, with an iron catalyst to help",
        true
      ],
      [
        "Lower temperature makes the iron catalyst stop working",
        false
      ],
      [
        "Lower temperature shifts equilibrium left — less ammonia",
        false
      ],
      [
        "450°C is chosen to decompose the ammonia into hydrogen for the forward reaction",
        false
      ]
    ],
    "q": "The Haber process uses 450°C rather than a lower temperature. Why, given that lower temperature gives more ammonia?",
    "wrong_explanations": {
      "1": "The iron catalyst works at a range of temperatures — although it may be less active at very low temperatures, the primary reason for 450°C is reaction RATE.",
      "2": "Lower temperature shifts equilibrium RIGHT (more NH₃) — not left. The forward reaction is exothermic, so lower temperature favours it.",
      "3": "The Haber process makes ammonia — the point is to produce NH₃ from N₂ and H₂, not to decompose it."
    }
  }
]
```
