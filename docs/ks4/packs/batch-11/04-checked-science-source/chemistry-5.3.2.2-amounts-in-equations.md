# Amounts of Substances in Equations  (Chemistry, AQA 5.3.2.2)

**Appears on routes:** Combined Higher, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Coefficients = molar ratio (theory 1; common_mistake; key_note) | higher | 8464 5.3.2.2; 8462 4.3.2.2 (HT only) |
| Reacting-mass method (theory 2; FIFA) | higher | 8464 5.3.2.2 (HT only) |
| n = m ÷ Mr (equations[0]) | higher | 8464 5.3.2.1 (HT only) |
| Yield, % yield (theory 3; key_note; equations[1]) | triple — off-spec on CH; off-topic (AIE-F2) | 8462 4.3.3.1 (chemistry only) |
| Atom economy (theory 3; key_note; equations[2]) | triple — WRONG formula, do not use (AIE-F1) | 8462 4.3.3.2 (chemistry only) |
| quiz q1 | higher | 8464 5.3.2.2 (HT only) |
| quiz q2 (% yield) | triple — TH only, if kept | 8462 4.3.3.1 (chemistry only) |

True page routes: CH TH. Site currently ships: CH TH, with the chemistry-only yield and atom-economy content also on CH — flagged AIE-F1, AIE-F2.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Use balanced equations and moles to calculate masses of reactants and products.

## theory
```json
[
  {
    "content": "A BALANCED equation gives the MOLAR RATIO of reactants and products — the coefficients show the ratio of moles.\n\nExamples:\n2Mg + O₂ → 2MgO\nMeans: 2 mol Mg reacts with 1 mol O₂ to produce 2 mol MgO.\nMolar ratio Mg : O₂ : MgO = 2 : 1 : 2.\n\nMg + 2HCl → MgCl₂ + H₂\nMeans: 1 mol Mg reacts with 2 mol HCl to produce 1 mol MgCl₂ and 1 mol H₂.\n\nN₂ + 3H₂ → 2NH₃\nMeans: 1 mol N₂ reacts with 3 mol H₂ to produce 2 mol NH₃.\n\nKey principle: the molar ratio in the balanced equation is always maintained, whatever the actual quantities used.",
    "heading": "Molar Ratios from Balanced Equations"
  },
  {
    "content": "STANDARD METHOD for calculating masses in reactions:\n\nStep 1: Write the balanced equation.\nStep 2: Write the molar ratio from the equation.\nStep 3: Convert given mass to moles: n = mass ÷ Mr.\nStep 4: Use the molar ratio to find moles of the unknown substance.\nStep 5: Convert moles back to mass: mass = n × Mr.\n\nEXAMPLE:\nHow much magnesium oxide forms when 4.8 g of magnesium burns?\n2Mg + O₂ → 2MgO\nStep 1: 2 mol Mg → 2 mol MgO (ratio 1:1)\nStep 2: n(Mg) = 4.8 ÷ 24 = 0.2 mol\nStep 3: n(MgO) = 0.2 mol (same ratio)\nStep 4: mass(MgO) = 0.2 × 40 = 8.0 g",
    "heading": "Calculating Masses Using Moles — The Method"
  },
  {
    "content": "THEORETICAL YIELD: the maximum mass of product calculated from the equation.\nACTUAL YIELD: the mass actually obtained in the experiment.\nActual yield is always LESS than or equal to theoretical yield.\n\nWhy actual yield < theoretical yield:\nReaction may not go to completion (reversible reactions).\nSide reactions produce unwanted products.\nProduct lost during transfer/purification.\nReactants may be impure.\n\nPERCENTAGE YIELD:\n% yield = (actual yield ÷ theoretical yield) × 100\n\nEXAMPLE:\nTheoretical yield of MgO = 8.0 g. Actual yield = 7.2 g.\n% yield = (7.2 ÷ 8.0) × 100 = 90%\n\nATOM ECONOMY:\nAtom economy = (Mr of desired products ÷ Mr of ALL products) × 100\nHigh atom economy = less waste, more sustainable, more cost-effective.\nAddition reactions have 100% atom economy (one product only).",
    "heading": "Percentage Yield"
  }
]
```

## common_mistake

Always use the MOLAR RATIO from the balanced equation when converting between moles of different substances. If 2 mol of A produces 1 mol of B, then 0.4 mol of A produces 0.2 mol of B — not 0.4 mol of B. The ratio comes from the COEFFICIENTS in the balanced equation.

## key_note

Balanced equation coefficients = molar ratios. Method: mass → moles (÷Mr) → use ratio → moles → mass (×Mr). % yield = (actual ÷ theoretical) × 100. Atom economy = (Mr desired ÷ Mr all products) × 100. High atom economy = less waste.

## equations
```json
[
  "n = m ÷ Mr",
  "% yield = (actual yield ÷ theoretical yield) × 100",
  "atom economy = (Mr desired products ÷ Mr all products) × 100"
]
```

## fifas
```json
[
  {
    "label": "Mass Calculation from Equation",
    "question": "Calculate the mass of hydrogen produced when 1.2 g of magnesium reacts with excess HCl. Mg + 2HCl → MgCl₂ + H₂. Ar: Mg=24, H=1.",
    "steps": [
      [
        "F",
        "n = mass ÷ Mr; then use molar ratio; then mass = n × Mr"
      ],
      [
        "I",
        "n(Mg) = 1.2 ÷ 24 = 0.05 mol. Ratio Mg:H₂ = 1:1, so n(H₂) = 0.05 mol. Mr(H₂) = 2"
      ],
      [
        "F",
        "mass(H₂) = 0.05 × 2 = 0.1"
      ],
      [
        "A",
        "0.1 g of hydrogen produced"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "n",
    "Amount in moles",
    "mol",
    "mol"
  ],
  [
    "m",
    "Mass",
    "grams",
    "g"
  ],
  [
    "Mr",
    "Relative formula mass",
    "",
    ""
  ]
]
```

## matching
```json
{
  "instruction": "Match each equation to the correct molar ratio statement.",
  "pairs": [
    [
      "2Mg + O₂ → 2MgO",
      "2 mol Mg reacts with 1 mol O₂ — Mg:MgO ratio is 1:1"
    ],
    [
      "N₂ + 3H₂ → 2NH₃",
      "1 mol N₂ reacts with 3 mol H₂ — N₂:NH₃ ratio is 1:2"
    ],
    [
      "Mg + 2HCl → MgCl₂ + H₂",
      "1 mol Mg reacts with 2 mol HCl to produce 1 mol MgCl₂ and 1 mol H₂"
    ],
    [
      "CaCO₃ → CaO + CO₂",
      "1 mol CaCO₃ produces 1 mol CaO and 1 mol CO₂"
    ]
  ],
  "title": "Molar Ratios from Equations"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "0.4 mol — ratio H₂:NH₃ = 3:2, so 0.6 × (2/3) = 0.4 mol",
        true
      ],
      [
        "0.6 mol — same moles as H₂ used",
        false
      ],
      [
        "0.9 mol — multiply 0.6 by the coefficient 3/2",
        false
      ],
      [
        "1.2 mol — double the H₂ moles",
        false
      ]
    ],
    "q": "N₂ + 3H₂ → 2NH₃. How many moles of NH₃ are produced from 0.6 mol of H₂?",
    "wrong_explanations": {
      "1": "The molar ratio must be used — 3 mol H₂ produces 2 mol NH₃, so 0.6 mol H₂ produces 0.6 × (2/3) = 0.4 mol NH₃.",
      "2": "0.6 × (3/2) = 0.9 — this inverts the ratio. H₂:NH₃ = 3:2, so NH₃ = H₂ × (2/3).",
      "3": "Doubling would only apply if the ratio were 1:2 — but H₂:NH₃ = 3:2."
    }
  },
  {
    "opts": [
      [
        "80% — % yield = (20 ÷ 25) × 100 = 80%",
        true
      ],
      [
        "125% — % yield = (25 ÷ 20) × 100",
        false
      ],
      [
        "5% — % yield = (5 ÷ 25) × 100 (using the difference)",
        false
      ],
      [
        "20% — using 20 directly as the percentage",
        false
      ]
    ],
    "q": "The theoretical yield of a product is 25 g but only 20 g is obtained. What is the percentage yield?",
    "wrong_explanations": {
      "1": "Dividing theoretical ÷ actual gives a value over 100% — meaningless for yield. Always divide ACTUAL ÷ THEORETICAL.",
      "2": "The 5 g difference is the LOST yield, not the yield itself. % yield = actual ÷ theoretical × 100.",
      "3": "20 is the actual yield in grams — not the percentage. Must divide by theoretical yield."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** Calculate the mass of hydrogen produced when 1.2 g of magnesium reacts with excess HCl. Mg + 2HCl → MgCl₂ + H₂. Ar: Mg=24, H=1.

**Convert:** [NEW — examined ✓] Nothing to convert — the mass of magnesium is already in grams throughout the calculation.

**F:** n = mass ÷ Mr; then use molar ratio; then mass = n × Mr

**I:** n(Mg) = 1.2 ÷ 24 = 0.05 mol. Ratio Mg:H₂ = 1:1, so n(H₂) = 0.05 mol. Mr(H₂) = 2

**F:** mass(H₂) = 0.05 × 2 = 0.1

**A:** 0.1 g of hydrogen produced
