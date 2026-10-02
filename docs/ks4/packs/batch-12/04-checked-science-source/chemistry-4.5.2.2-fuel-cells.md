# Fuel Cells  (Chemistry, AQA 4.5.2.2)

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Fuel cell: external fuel + oxygen/air, fuel oxidised electrochemically → p.d. (theory 1; common_mistake) | triple | 8462 4.5.2.2 (chemistry only) |
| Overall reaction 2H₂ + O₂ → 2H₂O; only product water (theory 1; equations; key_note; quiz q1) | triple | 8462 4.5.2.2 |
| Evaluate fuel cells vs rechargeable batteries (theory 2–3; quiz q2; `higher` second sentence) | triple — NOT higher; belongs on TF too | 8462 4.5.2.2 bullet 1 (no HT label) |
| Electrode half equations (`higher` first sentence) | triple-higher | 8462 4.5.2.2 bullet 2 (HT only) |
| Steam reforming, platinum, FCEV models, Apollo (theory 2–3) | off-spec context supporting evaluation | — |

True page routes: TF TH. Site currently ships: TF TH — matches. Only the half equations are HT (flagged, FUC-F2).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how hydrogen fuel cells work and evaluate their advantages and disadvantages.

## theory
```json
[
  {
    "content": "A FUEL CELL is an electrochemical cell that continuously converts the chemical energy of a fuel directly into electrical energy, as long as fuel and oxygen are supplied.\n\nHYDROGEN FUEL CELL:\nFuel: hydrogen gas (H₂) supplied continuously.\nOxidant: oxygen (O₂) from air.\nProduct: water (H₂O) — the only chemical product.\n\nOVERALL REACTION:\nH₂ + ½O₂ → H₂O (or: 2H₂ + O₂ → 2H₂O)\n\nHydrogen is OXIDISED at the negative electrode (anode).\nOxygen is REDUCED at the positive electrode (cathode).\nElectrons flow through external circuit → electrical energy.\n\nKEY DIFFERENCE from batteries:\nA battery stores a fixed amount of reactants — it 'runs out'.\nA fuel cell is supplied continuously — it works as long as fuel is provided.",
    "heading": "How Hydrogen Fuel Cells Work"
  },
  {
    "content": "ENVIRONMENTAL ADVANTAGES:\nOnly product is water — no CO₂, no NOₓ, no particulates emitted during operation.\nZero direct emissions — appealing for transport in cities.\n\nEFFICIENCY ADVANTAGES:\nConverts chemical energy directly to electrical energy — more efficient than combustion engines.\nNo moving parts in the cell itself — less mechanical energy lost to friction.\n\nPRACTICAL ADVANTAGES:\nRefuel quickly — fill hydrogen tank in minutes (vs hours to recharge batteries).\nLong range — hydrogen has very high energy density per kg.\nContinuous operation — unlike batteries which discharge over time.\n\nAPPLICATIONS:\nFuel cell vehicles (FCEVs): Toyota Mirai, Hyundai Nexo.\nBuses and HGVs where range and refuelling speed matter.\nPortable power generators.\nSpace exploration (used on Apollo missions — water produced was also used by crew).",
    "heading": "Advantages of Hydrogen Fuel Cells"
  },
  {
    "content": "HYDROGEN PRODUCTION:\nMost hydrogen is currently made from NATURAL GAS (steam reforming) — releases CO₂.\n'Green hydrogen' made by electrolysis of water using renewable energy — still expensive.\nUntil green hydrogen is widespread, fuel cells are not truly zero-carbon overall.\n\nSTORAGE AND DISTRIBUTION:\nHydrogen is highly flammable and must be stored under pressure or as a liquid.\nRequires new infrastructure — hydrogen refuelling stations are rare.\nStorage tanks take up significant space and add weight.\n\nCOST:\nFuel cells use platinum as a catalyst — platinum is rare and very expensive.\nFuel cell vehicles are more expensive than petrol or battery-electric vehicles currently.\n\nSAFETY:\nHighly flammable — requires careful handling and leak detection.\nHigh pressure storage adds engineering complexity.\n\nCOMPARISON WITH RECHARGEABLE BATTERIES:\nFuel cells: faster refuelling, longer range, but expensive hydrogen infrastructure.\nBattery-electric: established infrastructure (electricity grid), lower cost, but slower charging.\nBoth are zero direct emission — choice depends on application.",
    "heading": "Disadvantages and Challenges"
  }
]
```

## higher

Write half equations for the hydrogen fuel cell: negative electrode (anode): H₂ − 2e⁻ → 2H⁺; positive electrode (cathode): O₂ + 4H⁺ + 4e⁻ → 2H₂O. Evaluate hydrogen fuel cells vs rechargeable batteries for transport applications using data.

## common_mistake

Fuel cells are NOT the same as batteries. A battery stores fixed reactants and runs out. A fuel cell is continuously supplied with fuel — it runs as long as hydrogen and oxygen are provided. The ONLY product of a hydrogen fuel cell is water — no CO₂ is produced during operation.

## key_note

Hydrogen fuel cell: H₂ + O₂ → H₂O. Only product = water. Continuous supply of fuel. More efficient than combustion. Advantages: zero direct emissions, fast refuelling, high energy density. Disadvantages: hydrogen production (usually from natural gas), storage challenges, platinum catalyst (expensive), limited infrastructure.

## equations
```json
[
  "2H₂ + O₂ → 2H₂O  (overall fuel cell reaction)"
]
```

## matching
```json
{
  "instruction": "Sort each statement into advantage or disadvantage of hydrogen fuel cells.",
  "pairs": [
    [
      "Advantage",
      "Only product is water — zero direct emissions during operation"
    ],
    [
      "Advantage",
      "Refuels quickly — hydrogen tank filled in minutes unlike battery charging"
    ],
    [
      "Disadvantage",
      "Most hydrogen is made from natural gas — produces CO₂ in production"
    ],
    [
      "Disadvantage",
      "Platinum catalyst is rare and expensive — increases fuel cell cost"
    ],
    [
      "Disadvantage",
      "Hydrogen is highly flammable and requires high-pressure storage"
    ]
  ],
  "title": "Fuel Cell Pros and Cons"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Water (H₂O) — hydrogen is oxidised and oxygen is reduced; the only product is water",
        true
      ],
      [
        "Carbon dioxide — hydrogen combustion always produces CO₂",
        false
      ],
      [
        "Hydrogen peroxide — formed from the combination of H₂ and O₂",
        false
      ],
      [
        "Oxygen — unreacted oxygen is released as a by-product",
        false
      ]
    ],
    "q": "What is the only chemical product of a hydrogen fuel cell during operation?",
    "wrong_explanations": {
      "1": "Hydrogen fuel cells do NOT combust hydrogen — they electrochemically oxidise it. No carbon is present so no CO₂ is produced.",
      "2": "H₂O₂ is not the product — the electrochemical reaction produces water (H₂O), not hydrogen peroxide.",
      "3": "Oxygen is a REACTANT in a fuel cell — it is consumed at the cathode, not produced."
    }
  },
  {
    "opts": [
      [
        "Most hydrogen is produced from natural gas (steam reforming) which releases CO₂ — the emissions occur during hydrogen production not operation",
        true
      ],
      [
        "The fuel cell itself produces CO₂ as a waste product alongside water",
        false
      ],
      [
        "Platinum used in the catalyst is a carbon compound that releases CO₂",
        false
      ],
      [
        "Hydrogen fuel cells require electricity to start, which comes from fossil fuels",
        false
      ]
    ],
    "q": "Why are hydrogen fuel cells not yet truly 'zero carbon' in most current applications?",
    "wrong_explanations": {
      "1": "The fuel cell ITSELF only produces water — no CO₂ at all. The issue is the CARBON FOOTPRINT OF HYDROGEN PRODUCTION.",
      "2": "Platinum is a metal element (not a carbon compound) — it does not produce CO₂.",
      "3": "The start-up electricity is a minor consideration — the main carbon footprint comes from steam reforming during hydrogen manufacture."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
