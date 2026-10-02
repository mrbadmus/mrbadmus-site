# Factors Affecting the Rate of Reaction  (Chemistry, AQA 5.6.1.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Temperature: more frequent, more energetic collisions; more particles ≥ Ea (theory 1; key_note; quiz q1) | base | 8464 5.6.1.2, 5.6.1.3; 8462 4.6.1.2, 4.6.1.3 |
| Concentration; gas pressure (theory 2; key_note) | base | 8464 5.6.1.2, 5.6.1.3 |
| Surface area / powder vs lumps (theory 3; key_note; quiz q2) | base | 8464 5.6.1.2, 5.6.1.3 |
| Catalysts — the fifth listed factor (absent from this source) | base | 8464 5.6.1.2, 5.6.1.4 |
| Collision explanations (common_mistake) | base | 8464 5.6.1.3 |
| rp — the rate RP is **Combined RP 11 / Chemistry RP 5**, not "RP6"; concentration by a gas-volume AND a colour/turbidity method | base | 8464 5.6.1.2; 8462 4.6.1.2 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches. No HT or triple-only layer.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe and explain how temperature, concentration, surface area and pressure affect reaction rate.

## theory
```json
[
  {
    "content": "INCREASING TEMPERATURE increases reaction rate.\n\nWhy:\nParticles have MORE kinetic energy → move FASTER.\nMore frequent collisions (more collisions per second).\nMORE IMPORTANTLY: a greater PROPORTION of particles have energy ≥ the activation energy.\nMore successful collisions → faster rate.\n\nRule of thumb: increasing temperature by 10°C approximately DOUBLES the rate of many reactions.\n\nDECREASING TEMPERATURE slows the reaction rate — used in food preservation (refrigeration slows bacterial growth and chemical spoilage).\n\nTemperature has a BIGGER effect than just increasing collision frequency — it mainly increases the proportion of successful (high-energy) collisions.",
    "heading": "Temperature"
  },
  {
    "content": "INCREASING CONCENTRATION of a solution increases reaction rate.\n\nWhy:\nMore particles in the same volume.\nParticles are closer together.\nMore frequent collisions per unit time.\nMore successful collisions → faster rate.\n\nExample: doubling concentration approximately doubles the number of collisions.\n\nINCREASING PRESSURE of GASES increases reaction rate:\nGas particles are compressed into a smaller volume.\nParticles are closer together.\nMore frequent collisions → faster rate.\nSame principle as increasing concentration — more particles per unit volume.\n\nNote: pressure only affects GASEOUS reactions — has no significant effect on reactions in solution.",
    "heading": "Concentration and Pressure"
  },
  {
    "content": "INCREASING SURFACE AREA (by using smaller pieces/powder) increases reaction rate.\n\nWhy:\nMore surface area exposed to reactant particles.\nMore collisions possible per unit time.\nMore of the reactant is accessible → faster rate.\n\nThis is why POWDERS react faster than LUMPS of the same mass:\nA 1 g marble chip: small surface area → slow reaction with acid.\nThe same 1 g crushed to powder: massive increase in surface area → much faster reaction with acid.\n\nEXAMPLES:\nPowdered coal dust is EXPLOSIVE — high surface area. Lump coal burns slowly.\nFlour dust in mills can cause explosions.\nCoal fires — smaller pieces of coal burn faster.\n\nSurface area investigation: marble chips vs powder in HCl — compare gas produced over time.",
    "heading": "Surface Area"
  }
]
```

## common_mistake

All four factors (temperature, concentration, surface area, pressure for gases) increase rate by increasing the NUMBER OF SUCCESSFUL COLLISIONS. Temperature is special — it also increases the PROPORTION of particles with sufficient energy (≥ activation energy), making it particularly effective. Always explain in terms of collisions.

## key_note

Higher temperature → faster particles, more collisions, more above activation energy. Higher concentration → more particles per volume, more collisions. Larger surface area → more exposed particles, more collisions. Higher pressure (gases) → more particles per volume, more collisions. All increase rate by increasing successful collisions.

## rp

RP6 (Chemistry) — Investigate effect of concentration on rate (Na₂S₂O₃ + HCl). Can also investigate surface area (marble chips vs powder with HCl) or temperature effects.

## matching
```json
{
  "instruction": "Match each factor change to its effect on reaction rate and why.",
  "pairs": [
    [
      "Increase temperature",
      "Rate increases — more particles exceed activation energy, more frequent and more energetic collisions"
    ],
    [
      "Increase concentration",
      "Rate increases — more particles per unit volume, more frequent collisions"
    ],
    [
      "Use powder instead of lumps",
      "Rate increases — greater surface area exposes more particles to collisions"
    ],
    [
      "Increase pressure (gases)",
      "Rate increases — gas particles compressed into smaller volume, more frequent collisions"
    ],
    [
      "Decrease temperature",
      "Rate decreases — fewer particles have enough energy to react successfully"
    ]
  ],
  "title": "Factor → Effect on Rate"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "A greater proportion of particles now have energy ≥ the activation energy — so more collisions are successful",
        true
      ],
      [
        "Higher temperature makes particles larger — they collide more easily",
        false
      ],
      [
        "Higher temperature dissolves more of the solid reactants — increasing concentration",
        false
      ],
      [
        "Temperature has no extra effect — it only increases collision frequency",
        false
      ]
    ],
    "q": "Why does increasing temperature increase reaction rate more than just increasing the frequency of collisions?",
    "wrong_explanations": {
      "1": "Particles don't change size with temperature — they move faster.",
      "2": "This might apply in some specific cases but is not the general reason why temperature increases rate — the key is the energy distribution.",
      "3": "Temperature does more than increase frequency — it shifts the energy distribution so MORE particles exceed the activation energy threshold."
    }
  },
  {
    "opts": [
      [
        "Rate increases — powder has much greater surface area, more particle collisions per unit time",
        true
      ],
      [
        "Rate stays the same — same mass of marble is used",
        false
      ],
      [
        "Rate decreases — powder dissolves faster so there are fewer particles overall",
        false
      ],
      [
        "Rate increases because powder has less activation energy than chips",
        false
      ]
    ],
    "q": "Marble chips (CaCO₃) react with HCl. The experiment is repeated with the same mass of powdered marble. How does the rate change?",
    "wrong_explanations": {
      "1": "Same MASS does not mean same rate — rate depends on SURFACE AREA. Powder has enormously more surface area than chips.",
      "2": "Powder dissolving faster IS the result of faster rate — the mechanism is increased surface area for collisions.",
      "3": "Activation energy is a property of the reaction, not the physical form of the reactant. Powder and chips have the same activation energy."
    }
  }
]
```
