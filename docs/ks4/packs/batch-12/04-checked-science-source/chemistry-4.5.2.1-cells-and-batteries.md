# Cells and Batteries  (Chemistry, AQA 4.5.2.1)

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Simple cell: two different metals + electrolyte (theory 1; key_note) | triple | 8462 4.5.2.1 (chemistry only) |
| Voltage depends on electrodes (reactivity difference) and electrolyte (theory 1; common_mistake; quiz q1) | triple | 8462 4.5.2.1 |
| Battery = 2+ cells in series, greater voltage (theory 2–3; common_mistake) | triple | 8462 4.5.2.1 |
| Non-rechargeable / alkaline; rechargeable reversed by external current (theory 2; key_note; quiz q2) | triple | 8462 4.5.2.1 |
| Interpret reactivity data; evaluate the use of cells (`higher` field) | triple — NOT higher; belongs on TF too | 8462 4.5.2.1 (no HT label) |
| Primary/secondary, Li-ion, lead-acid, NiMH, uses, toxic metals, mAh capacity (theory 2–3; key_note) | off-spec context | 8462 4.5.2.1 "do not need to know details… other than those specified" |

True page routes: TF TH. Site currently ships: TF TH — matches. The `higher` field's content is not HT (flagged, CAB-F3).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how chemical cells and batteries produce electrical energy and factors affecting voltage.

## theory
```json
[
  {
    "content": "A CHEMICAL CELL converts chemical energy into electrical energy through redox reactions.\n\nA SIMPLE CELL consists of:\nTwo different METAL ELECTRODES (e.g. zinc and copper).\nAn ELECTROLYTE — a solution that conducts electricity (e.g. copper sulfate solution or sulfuric acid).\n\nHOW IT WORKS:\nThe more reactive metal (e.g. zinc) acts as the NEGATIVE electrode (anode) — it loses electrons (oxidation).\nThe less reactive metal (e.g. copper) acts as the POSITIVE electrode (cathode) — it gains electrons (reduction).\nElectrons flow through an external circuit from negative to positive electrode.\nIons carry charge through the electrolyte.\n\nFACTORS AFFECTING VOLTAGE:\n1. TYPE OF METALS — the greater the difference in reactivity, the greater the voltage produced.\n2. TYPE OF ELECTROLYTE — different electrolytes give different voltages.\n3. CONCENTRATION OF ELECTROLYTE — affects ion availability.\n4. TEMPERATURE — affects rate of reaction and therefore voltage.",
    "heading": "Chemical Cells"
  },
  {
    "content": "A BATTERY consists of TWO OR MORE CELLS connected in series.\n\nVoltage of a battery = sum of voltages of individual cells.\nTwo 1.5 V cells in series = 3 V battery.\n\nNON-RECHARGEABLE BATTERIES (PRIMARY CELLS):\nChemical reactions are irreversible — the battery is used once and discarded.\nExamples: alkaline batteries (AA, AAA, D), zinc-carbon batteries.\n\nRECHARGEABLE BATTERIES (SECONDARY CELLS):\nChemical reactions are reversible — electrical energy is applied to reverse the cell reactions.\nExamples: lithium-ion (phones, laptops), lead-acid (car batteries), nickel-metal hydride.\n\nWhen a rechargeable battery is recharged, the external power supply REVERSES the redox reactions — restoring the original reactants.\n\nEVENTUALLY:\nRepeated charge-discharge cycles gradually degrade the electrode materials.\nBatteries lose capacity over time and must eventually be replaced.",
    "heading": "Batteries"
  },
  {
    "content": "USES OF BATTERIES:\nPortable electronic devices: phones, laptops, tablets.\nElectric vehicles: large lithium-ion battery packs.\nEnergy storage: grid-scale batteries storing renewable energy.\nMedical devices: pacemakers, hearing aids.\nEmergency backup power.\n\nENVIRONMENTAL CONSIDERATIONS:\nBatteries contain toxic metals (lead, cadmium, lithium, nickel) — must be disposed of carefully.\nRecycling batteries recovers valuable materials and prevents toxic waste.\nRechargeable batteries reduce waste compared to single-use.\n\nCOMPARING CELLS AND BATTERIES:\nA single cell: limited voltage and capacity.\nA battery: higher voltage (cells in series), more energy stored.\n\nBATTERY CAPACITY:\nMeasured in milliamp-hours (mAh) or watt-hours (Wh).\nHigher capacity = more energy stored = longer usage time.",
    "heading": "Uses and Environmental Considerations"
  }
]
```

## higher

Explain how the voltage of a cell depends on the difference in reactivity between the electrode metals. Evaluate different types of batteries (primary, secondary, fuel cells) for specific applications using data on energy density, rechargeability, cost and environmental impact.

## common_mistake

A BATTERY is two or more cells connected in series — a single cell is NOT a battery. The voltage increases when cells are added in series. The greater the difference in reactivity of the two metals in a cell, the greater the voltage produced.

## key_note

Chemical cell: two different metals in electrolyte → voltage. Factors: metal types (reactivity difference), electrolyte type, concentration, temperature. Battery = 2+ cells in series. Non-rechargeable: irreversible reactions. Rechargeable: reversible — external electricity reverses reactions. Li-ion most common rechargeable.

## matching
```json
{
  "instruction": "Match each term to its correct description.",
  "pairs": [
    [
      "Chemical cell",
      "Two different metals in an electrolyte — converts chemical energy to electrical energy"
    ],
    [
      "Battery",
      "Two or more cells connected in series — total voltage = sum of individual cell voltages"
    ],
    [
      "Non-rechargeable",
      "Primary cell — irreversible reactions, used once then discarded"
    ],
    [
      "Rechargeable",
      "Secondary cell — reversible reactions, external electricity restores original reactants"
    ]
  ],
  "title": "Cells and Batteries"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Greater difference in reactivity between the two metals → greater voltage produced",
        true
      ],
      [
        "Using more reactive metals always reduces the voltage — reactive metals react too quickly",
        false
      ],
      [
        "The metal reactivity has no effect on voltage — only electrolyte concentration matters",
        false
      ],
      [
        "Using two metals with the same reactivity gives the highest voltage",
        false
      ]
    ],
    "q": "A simple cell is made from zinc and copper electrodes in sulfuric acid. How does changing to more reactive metals affect the voltage?",
    "wrong_explanations": {
      "1": "More reactive metals react more vigorously but the key factor for voltage is the DIFFERENCE in reactivity between the two electrodes.",
      "2": "Reactivity difference is one of the key factors affecting voltage — it cannot be ignored.",
      "3": "If both metals have the same reactivity, no potential difference exists — the voltage would be zero."
    }
  },
  {
    "opts": [
      [
        "The redox reactions are reversed by the external electricity supply — restoring the original reactants",
        true
      ],
      [
        "New chemicals are added to the battery to replace the used reactants",
        false
      ],
      [
        "The battery temperature increases — heat energy is stored for later use",
        false
      ],
      [
        "The battery simply resets — no chemical change occurs during charging",
        false
      ]
    ],
    "q": "What happens chemically when a rechargeable battery is being charged?",
    "wrong_explanations": {
      "1": "Charging does not physically add new chemicals — the same chemicals inside are chemically restored by reversing the redox reactions.",
      "2": "Charging is an electrochemical process — it reverses the reactions, not a heat-storage process.",
      "3": "Significant chemical changes DO occur during charging — the products of discharge are converted back to reactants."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
