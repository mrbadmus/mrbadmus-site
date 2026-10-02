# Reaction Profiles  (Chemistry, AQA 5.5.1.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Profile features: reactants, products, activation energy, overall energy change; exo/endo profiles (theory 1–2; common_mistake; key_note; equations; variables; quiz q1) | base | 8464 5.5.1.2 / 8462 4.5.1.2 |
| Catalyst: different pathway, lower Ea, same ΔH (theory 3; key_note; quiz q2) | base | 8464 5.6.1.4 / 8462 4.6.1.4 |
| `higher` — label features; sketch with/without catalyst | base (not HT) | 8464 5.5.1.2, 5.6.1.4 / 8462 4.5.1.2, 4.6.1.4 |

True page routes: CF CH TF TH, no HT or separate-science layer. Site currently ships: CF CH TF TH with the `higher` labelling/sketching on CH TH only — flagged RPR-F1.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Draw and interpret reaction profile diagrams for exothermic and endothermic reactions.

## theory
```json
[
  {
    "content": "A REACTION PROFILE (also called an energy profile diagram) shows how the ENERGY of the system changes as a reaction progresses.\n\nThe x-axis shows PROGRESS OF REACTION (from reactants to products).\nThe y-axis shows ENERGY (in kJ or kJ/mol).\n\nKey features on every reaction profile:\nREACTANTS — the starting energy level (left).\nPRODUCTS — the final energy level (right).\nACTIVATION ENERGY (Ea) — the energy barrier that must be overcome for the reaction to start — shown as the PEAK of the curve above the reactant level.\nOVERALL ENERGY CHANGE (ΔH) — the difference in energy between reactants and products.",
    "heading": "What is a Reaction Profile?"
  },
  {
    "content": "EXOTHERMIC REACTION PROFILE:\nProducts are at a LOWER energy level than reactants.\nThe curve rises to a peak (activation energy) then falls below the reactant level.\nΔH is NEGATIVE (products lower than reactants — energy released).\nThe difference between the peak and the REACTANT energy level = activation energy.\n\nENDOTHERMIC REACTION PROFILE:\nProducts are at a HIGHER energy level than reactants.\nThe curve rises to a peak (activation energy) then falls — but levels off ABOVE the reactant starting point.\nΔH is POSITIVE (products higher than reactants — energy absorbed).\nThe difference between the peak and the REACTANT energy level = activation energy.\n\nACTIVATION ENERGY:\nAll reactions need activation energy to get started — even exothermic ones.\nActivation energy = minimum energy needed to break existing bonds and start the reaction.\nLow activation energy → fast reaction.\nHigh activation energy → slow reaction (even if very exothermic once started).",
    "heading": "Exothermic and Endothermic Profiles"
  },
  {
    "content": "A CATALYST provides an ALTERNATIVE REACTION PATHWAY with a LOWER ACTIVATION ENERGY.\n\nOn a reaction profile, adding a catalyst:\nLOWERS the peak of the curve (lower activation energy hump).\nDoes NOT change the energy levels of reactants or products.\nDoes NOT change ΔH — the overall energy change is the same.\n\nThis means:\nMore molecules have enough energy to react → faster reaction rate.\nThe same overall energy is released or absorbed per mole of reaction.\n\nWhy catalysts are important:\nWithout catalysts, many industrially and biologically important reactions would be too slow to be useful.\nIn biology, ENZYMES act as biological catalysts — lowering activation energy of specific reactions.\nIn industry, transition metals (iron, platinum, nickel) are common catalysts.\n\nA lower activation energy hump on a reaction profile diagram represents a CATALYSED reaction.",
    "heading": "Effect of Catalysts on Reaction Profiles"
  }
]
```

## higher

Label all features on a reaction profile: reactant energy level, product energy level, activation energy (Ea), ΔH. Sketch profiles for exothermic and endothermic reactions both with and without a catalyst. Explain that a catalyst lowers Ea without changing ΔH or the energy of reactants/products.

## common_mistake

The activation energy is measured from the REACTANT level to the PEAK — NOT from the reactant level to the product level. The overall energy change (ΔH) is from reactants to PRODUCTS. These are two different measurements on the same diagram. Students often confuse them.

## key_note

Reaction profile: x = reaction progress, y = energy. Exothermic: products LOWER than reactants (ΔH negative). Endothermic: products HIGHER than reactants (ΔH positive). Activation energy = reactant level to peak. Catalyst: lower peak, same reactant/product levels, same ΔH.

## equations
```json
[
  "ΔH = energy of products − energy of reactants",
  "Activation energy = energy of peak − energy of reactants"
]
```

## variables
```json
[
  [
    "Ea",
    "Activation energy",
    "kJ/mol",
    "kJ/mol"
  ],
  [
    "ΔH",
    "Overall energy change (enthalpy change)",
    "kJ/mol",
    "kJ/mol"
  ]
]
```

## matching
```json
{
  "instruction": "Match each feature of a reaction profile to its description.",
  "pairs": [
    [
      "Activation energy",
      "Energy gap from reactant level up to the peak of the curve"
    ],
    [
      "ΔH (exothermic)",
      "Products are lower than reactants — energy released — ΔH is negative"
    ],
    [
      "ΔH (endothermic)",
      "Products are higher than reactants — energy absorbed — ΔH is positive"
    ],
    [
      "Effect of catalyst",
      "Lowers the peak — lower activation energy — same ΔH — faster reaction"
    ]
  ],
  "title": "Reaction Profile Features"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "−30 kJ — products (50) − reactants (80) = −30 kJ — exothermic reaction",
        true
      ],
      [
        "+30 kJ — reactants (80) − products (50) = +30 kJ",
        false
      ],
      [
        "+130 kJ — adding reactant and product energies",
        false
      ],
      [
        "−80 kJ — the reactant energy is lost",
        false
      ]
    ],
    "q": "On a reaction profile, the reactants are at 80 kJ and the products are at 50 kJ. What is ΔH?",
    "wrong_explanations": {
      "1": "ΔH = products − reactants = 50 − 80 = −30. Positive 30 would mean products are HIGHER than reactants — but here products (50) are lower than reactants (80).",
      "2": "Adding energies gives a meaningless value — ΔH = products MINUS reactants.",
      "3": "The reactant energy of 80 kJ is not 'lost' — ΔH shows the NET energy change from reactants to products."
    }
  },
  {
    "opts": [
      [
        "The activation energy peak is lower — but reactant and product energy levels and ΔH stay the same",
        true
      ],
      [
        "The reactant energy level increases — they become more energetic",
        false
      ],
      [
        "Both the activation energy and ΔH decrease",
        false
      ],
      [
        "The product energy level increases — products formed are higher energy",
        false
      ]
    ],
    "q": "A catalyst is added to a reaction. What changes on the reaction profile?",
    "wrong_explanations": {
      "1": "Catalysts do not give reactants more energy — they provide an ALTERNATIVE PATHWAY with a lower energy barrier.",
      "2": "ΔH (the overall energy change) is NOT changed by a catalyst — only the activation energy peak is lowered.",
      "3": "Products are the same compounds regardless of whether a catalyst is used — their energy level doesn't change."
    }
  }
]
```

## higher — Combined Foundation copy (differs from the Triple Higher copy above)
```json
null
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
