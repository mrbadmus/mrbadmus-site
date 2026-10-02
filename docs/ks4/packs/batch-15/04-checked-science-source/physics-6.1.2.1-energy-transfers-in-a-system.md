# Energy Transfers in a System  (Physics, AQA 6.1.2.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Conservation: transferred usefully, stored or dissipated, never created or destroyed; closed system, no net change (theory 1; common_mistake; key_note) | base | 8464 6.1.2.1 / 8463 4.1.2.1 |
| Dissipation: stored in less useful ways, "wasted" (theory 2; q1) | base | 6.1.2.1 / 4.1.2.1 |
| Reducing unwanted transfers: lubrication, streamlining, thermal insulation (theory 3; q2) | base | 6.1.2.1 / 4.1.2.1 |
| Superconductors (theory 3) | off-spec | — |
| Thermal conductivity; building cooling vs wall thickness and conductivity (not in this file) | base — taught in thermal-conductivity (batch 4) | 6.1.2.1 / 4.1.2.1 |
| Thermal-insulators practical (not in this file) | triple — 8463 RP2 (physics only), in thermal-conductivity | 8463 4.1.2.1 |
| "Wasted = total input − useful output" (key_note) | base | 6.1.2.1 (efficiency itself is 6.1.2.2) |
| RP / `higher` | none | — |

True page routes: CF CH TF TH (all base). Site currently ships: CF CH TF TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how energy is conserved, dissipated and how unwanted transfers can be reduced.

## theory
```json
[
  {
    "content": "The LAW OF CONSERVATION OF ENERGY:\nEnergy cannot be CREATED or DESTROYED — it can only be TRANSFERRED between stores or DISSIPATED.\n\nIn a CLOSED SYSTEM:\nTotal energy before = Total energy after — always.\n\nEXAMPLES:\nSwinging pendulum: KE ⇌ GPE, cycling continuously (ignoring air resistance).\nBouncing ball: GPE → KE → elastic PE → KE → GPE → lower each time (energy dissipated).\nBattery-powered torch: chemical → electrical → light + thermal.\n\nEnergy is never destroyed — but it can become less USEFUL when it spreads out into the thermal stores of the surroundings.",
    "heading": "Conservation of Energy"
  },
  {
    "content": "DISSIPATION: energy transferred to less useful stores — typically the thermal stores of the surroundings.\n\nDissipated energy is described as WASTED — not used for the intended purpose.\n\nCauses of dissipation:\nFRICTION — between moving parts → thermal energy.\nAIR RESISTANCE — object transfers energy to air.\nELECTRICAL RESISTANCE — current in wires → heat.\nSOUND — vibrations dissipate energy to the air.\n\nOnce energy is dissipated into the surroundings, it spreads out and becomes very difficult to use again.\n\nEXAMPLES:\nCar: chemical PE → useful KE + wasted thermal (engine, brakes, air resistance).\nFilament bulb: electrical → useful light (10%) + wasted thermal (90%).\nPhone charging: electrical → chemical store + thermal (phone gets warm).",
    "heading": "Dissipation of Energy"
  },
  {
    "content": "LUBRICATION — oil between moving parts reduces friction → less thermal wasted.\nSTREAMLINING — aerodynamic shapes reduce air resistance → less energy to air.\nINSULATION — reduces thermal transfer to/from surroundings:\nThick walls, double glazing, loft insulation, cavity wall insulation.\nBETTER CONDUCTORS — lower resistance in wires → less electrical energy wasted as heat.\nSUPERCONDUCTORS — zero resistance at very low temperatures → zero electrical energy wasted.\n\nThere is always a practical limit — beyond a certain point, the cost of further improvements outweighs the energy saved.",
    "heading": "Reducing Unwanted Energy Transfers"
  }
]
```

## common_mistake

Energy is NEVER destroyed — it is dissipated to less useful stores. 'Lost' energy has been transferred to the thermal energy of the surroundings — it is still there, just spread out and difficult to use again. Never say energy is 'used up' or 'gone'.

## key_note

Conservation of energy: never created or destroyed. Dissipation: energy spreads to surroundings as thermal — less useful. Reduce by: lubrication (friction), streamlining (air resistance), insulation (thermal loss), better conductors (electrical resistance). Wasted = total input − useful output.

## matching
```json
{
  "instruction": "Match each energy dissipation cause to its solution.",
  "pairs": [
    [
      "Friction between moving parts",
      "Lubrication with oil — reduces surface contact, less thermal energy wasted"
    ],
    [
      "Air resistance on moving objects",
      "Streamlining — aerodynamic shape lets air flow smoothly, less energy transferred to air"
    ],
    [
      "Thermal loss from buildings",
      "Insulation — thick walls, double glazing, loft insulation reduce conduction rate"
    ],
    [
      "Electrical resistance in wires",
      "Thicker wires or lower-resistance materials — less heat generated by current"
    ]
  ],
  "title": "Reducing Dissipation"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Dissipated to thermal stores of the surrounding air and pivot through air resistance and friction",
        true
      ],
      [
        "The energy is destroyed — the pendulum stopping proves this",
        false
      ],
      [
        "Stored in the pendulum's elastic potential energy store ready to restart",
        false
      ],
      [
        "Converted to sound only, which then disappears",
        false
      ]
    ],
    "q": "A pendulum swings and eventually stops. Where has the energy gone?",
    "wrong_explanations": {
      "1": "Energy is NEVER destroyed — this violates the law of conservation of energy. The pendulum slows because energy is dissipated, not destroyed.",
      "2": "Once stopped, the pendulum has no stored elastic PE — it is hanging at rest and any elastic PE would have been released.",
      "3": "Some sound is produced, but sound also eventually dissipates to thermal energy in the air. No energy disappears — all ends up as thermal energy of the surroundings."
    }
  },
  {
    "opts": [
      [
        "It slows the rate of thermal energy transfer from the warm house to the cold surroundings — less energy needed to maintain temperature",
        true
      ],
      [
        "It generates heat from the solar radiation it absorbs",
        false
      ],
      [
        "It stores thermal energy during the day and releases it at night",
        false
      ],
      [
        "It prevents cold draughts entering through the roof — stopping convection",
        false
      ]
    ],
    "q": "Why does adding loft insulation reduce heating bills?",
    "wrong_explanations": {
      "1": "Loft insulation works by reducing CONDUCTION through the ceiling — the fibres trap air (poor thermal conductor) and slow heat loss.",
      "2": "While insulation has thermal mass, this is not its primary mechanism — reducing the RATE of heat loss is.",
      "3": "Loft insulation does reduce some convection at the ceiling, but its primary mechanism is reducing thermal CONDUCTION."
    }
  }
]
```
