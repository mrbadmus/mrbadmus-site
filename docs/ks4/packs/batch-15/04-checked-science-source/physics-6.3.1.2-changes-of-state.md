# Changes of State  (Physics, AQA 6.3.1.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Names: melt, freeze, boil, evaporate, condense, sublimate (+ deposition) (theory 1; key_note) | base | 8464 6.3.1.2 / 8463 4.3.1.2 |
| Energy supplied / removed (theory 1) | base (one line; internal energy is batch 2's) | 8464 6.3.2.1 |
| Mass conserved in every change of state (theory 1; common_mistake; key_note; q1) | base | 8464 6.3.1.2 / 8463 4.3.1.2 |
| Physical not chemical; recovers original properties when reversed (theory 2; common_mistake; q2) | base | 8464 6.3.1.2 / 8463 4.3.1.2 |
| Particle arrangement in solid/liquid/gas; melting and boiling (theory 3) — imprecise, CHANGES-OF-STATE-F1, F3 | base | 8464 6.3.1.1 / 8463 4.3.1.1 |
| q1, q2 | base | 8464 6.3.1.2 |

True page routes: CF CH TF TH, all base (no HT, no separate-science content in 6.3.1.2). Site currently ships: CF CH TF TH, which matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe changes of state in terms of particles and explain why mass is conserved.

## theory
```json
[
  {
    "content": "Matter exists in three main states: SOLID, LIQUID and GAS.\n\nChanges of state occur when enough energy is supplied or removed:\n\nSOLID → LIQUID: MELTING (energy supplied)\nLIQUID → SOLID: FREEZING (energy removed)\nLIQUID → GAS: EVAPORATION/BOILING (energy supplied)\nGAS → LIQUID: CONDENSATION (energy removed)\nSOLID → GAS (directly): SUBLIMATION (energy supplied)\nGAS → SOLID (directly): DEPOSITION (energy removed)\n\nMASS IS CONSERVED:\nWhen a substance changes state, no particles are created or destroyed — they simply rearrange.\nThe total mass before = total mass after.\nExample: 100 g of ice melts to give exactly 100 g of liquid water.",
    "heading": "The States of Matter and Changes of State"
  },
  {
    "content": "Changes of state are PHYSICAL CHANGES — NOT chemical changes.\n\nKey difference:\nPHYSICAL change: the substance keeps its chemical identity — REVERSIBLE.\nCHEMICAL change: new substances are formed — usually irreversible.\n\nWhy changes of state are physical:\nNo new chemical bonds are formed or broken between different types of molecule.\nWater freezing: H₂O molecules are still H₂O — just rearranged in a lattice.\nWater evaporating: H₂O molecules still exist as individual molecules in the gas.\n\nThe change can be REVERSED:\nIce melts → water → refreezes → ice again. Same substance throughout.\n\nContrast with chemical change:\nBurning wood: wood + oxygen → CO₂ + water. Original material cannot be recovered.",
    "heading": "Physical vs Chemical Changes"
  },
  {
    "content": "SOLID:\nParticles in fixed positions in a regular lattice.\nVibrate in place — cannot flow.\nStrong intermolecular forces hold them together.\n\nLIQUID:\nParticles close together but able to move past each other.\nNo fixed arrangement — can flow and take the shape of the container.\nWeaker intermolecular forces than solid.\n\nGAS:\nParticles far apart — mostly empty space.\nMove rapidly in all directions — random motion.\nVery weak intermolecular forces (effectively none).\nFill any container.\n\nDURING MELTING:\nEnergy supplied → particles vibrate more → forces between particles overcome → lattice breaks down → particles begin to flow.\n\nDURING BOILING:\nEnergy supplied → particles gain enough energy to completely overcome intermolecular forces → escape from liquid surface into gas phase.",
    "heading": "Particle Explanation of Changes of State"
  }
]
```

## common_mistake

Changes of state are PHYSICAL changes — not chemical. The substance remains the same chemical compound throughout. Mass is ALWAYS conserved in a change of state — the number of particles doesn't change, only their arrangement.

## key_note

Solid → liquid: melting. Liquid → gas: boiling/evaporation. Reverse: freezing, condensation. Sublimation: solid → gas directly. All are physical changes — reversible, mass conserved. Particles rearrange but are not created or destroyed.

## matching
```json
{
  "instruction": "Match each change of state to its name and direction.",
  "pairs": [
    [
      "Melting",
      "Solid → liquid — energy supplied, particles gain enough energy to break from lattice"
    ],
    [
      "Freezing",
      "Liquid → solid — energy removed, particles slow down and form fixed lattice"
    ],
    [
      "Evaporation/Boiling",
      "Liquid → gas — energy supplied, particles escape intermolecular forces"
    ],
    [
      "Condensation",
      "Gas → liquid — energy removed, particles slow and intermolecular forces pull them together"
    ],
    [
      "Sublimation",
      "Solid → gas directly — e.g. dry ice (solid CO₂) at room temperature"
    ]
  ],
  "title": "Change of State Match"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "200 g — mass is conserved during changes of state; no particles are created or destroyed",
        true
      ],
      [
        "Less than 200 g — some water evaporates as it cools",
        false
      ],
      [
        "More than 200 g — ice is larger in volume so it must be heavier",
        false
      ],
      [
        "Depends on temperature — colder freezers produce heavier ice",
        false
      ]
    ],
    "q": "200 g of water is placed in a freezer and completely freezes. What is the mass of the ice formed?",
    "wrong_explanations": {
      "1": "In a sealed container with no evaporation, mass is perfectly conserved — but even with some evaporation, the PRINCIPLE is conservation of mass in a change of state.",
      "2": "Ice IS larger in volume than liquid water — but volume and mass are different. The MASS is the same; ice is simply less dense.",
      "3": "Temperature affects rate of freezing and final temperature, not the mass of ice formed."
    }
  },
  {
    "opts": [
      [
        "No new substances are formed — the material's chemical identity is preserved and the change is reversible",
        true
      ],
      [
        "Melting only affects the surface of the solid — the inside remains chemically unchanged",
        false
      ],
      [
        "Physical changes always involve energy, while chemical changes do not",
        false
      ],
      [
        "Melting is chemical because the structure of the material is permanently altered",
        false
      ]
    ],
    "q": "Why is melting a physical change rather than a chemical change?",
    "wrong_explanations": {
      "1": "Melting is a bulk process — the entire solid changes state, not just the surface.",
      "2": "Both chemical and physical changes can involve energy. The distinction is whether new chemical substances are formed.",
      "3": "The ARRANGEMENT of particles changes (structure), but the CHEMICAL IDENTITY doesn't — it's still the same compound. Chemical changes produce new substances."
    }
  }
]
```
