# Series and Parallel Circuits  (Physics, AQA 6.2.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Calculate current, potential difference and resistance in series and parallel circuits.

## theory
```json
[
  {
    "content": "In a SERIES circuit, all components are in a SINGLE LOOP — one path for current.\n\nRules:\nCURRENT: same through every component — I₁ = I₂ = I₃\nPD: splits between components — V_total = V₁ + V₂ + V₃\nRESISTANCE: adds up — R_total = R₁ + R₂ + R₃\n\nEXAMPLE:\nR₁ = 4 Ω, R₂ = 6 Ω, battery = 10 V.\nR_total = 10 Ω. I = 10 ÷ 10 = 1 A.\nV₁ = 1 × 4 = 4 V; V₂ = 1 × 6 = 6 V. Check: 4 + 6 = 10 V ✓\n\nIf one component breaks — ALL components stop working.",
    "heading": "Series Circuits"
  },
  {
    "content": "In a PARALLEL circuit, components are in SEPARATE BRANCHES — multiple paths for current.\n\nRules:\nPD: same across every branch — V₁ = V₂ = V₃ = V_supply\nCURRENT: splits — I_total = I₁ + I₂ + I₃\nRESISTANCE: total is LESS than the smallest individual resistance.\n\nEXAMPLE:\n12 V supply. R₁ = 6 Ω, R₂ = 4 Ω.\nI₁ = 12 ÷ 6 = 2 A; I₂ = 12 ÷ 4 = 3 A.\nI_total = 2 + 3 = 5 A.\n\nIf one branch breaks — OTHER branches continue working.",
    "heading": "Parallel Circuits"
  },
  {
    "content": "Domestic wiring is PARALLEL because:\n1. Each appliance gets the FULL mains pd (230 V).\n2. Appliances work INDEPENDENTLY — switching one off doesn't affect others.\n3. Easy to add appliances without affecting existing ones.\n4. Each appliance can have its own fuse.\n\nSECOMPARISON:\nSeries: same current, pd splits, R adds, all-or-nothing.\nParallel: same pd, current splits, R decreases, independent operation.",
    "heading": "Why Household Circuits Are Parallel"
  }
]
```

## common_mistake

In PARALLEL, total resistance is LESS than any individual resistance — more branches = more paths = lower resistance. Adding resistors in SERIES always increases total resistance. Students often mix these up.

## key_note

Series: same I, pd splits, R adds. Parallel: same pd, I splits, total R less than smallest. Household = parallel — full voltage, independent. Series break = all stop. Parallel break = others continue.

## equations
```json
[
  "Series: R_total = R₁ + R₂ + R₃",
  "Series: V_total = V₁ + V₂ + V₃",
  "Parallel: I_total = I₁ + I₂ + I₃"
]
```

## fifas
```json
[
  {
    "label": "Series Circuit",
    "question": "R₁ = 3 Ω and R₂ = 7 Ω in series with a 20 V battery. Find the current and pd across each resistor.",
    "steps": [
      [
        "F",
        "R_total = R₁ + R₂; I = V ÷ R_total; V₁ = I × R₁; V₂ = I × R₂"
      ],
      [
        "I",
        "R_total = 3 + 7 = 10 Ω; V = 20 V"
      ],
      [
        "F",
        "I = 20 ÷ 10 = 2 A; V₁ = 2 × 3 = 6 V; V₂ = 2 × 7 = 14 V"
      ],
      [
        "A",
        "I = 2 A throughout; V₁ = 6 V; V₂ = 14 V (check: 6 + 14 = 20 V ✓)"
      ]
    ]
  }
]
```

## rp

RP15 (Physics) — Construct series and parallel circuits; measure I and V at different points to verify rules.

## variables
```json
[
  [
    "I",
    "Current",
    "amperes",
    "A"
  ],
  [
    "V",
    "Potential difference",
    "volts",
    "V"
  ],
  [
    "R",
    "Resistance",
    "ohms",
    "Ω"
  ]
]
```

## matching
```json
{
  "instruction": "Match each property to the correct circuit type.",
  "pairs": [
    [
      "Series",
      "Current is identical at every point in the loop"
    ],
    [
      "Parallel",
      "Potential difference is the same across every branch"
    ],
    [
      "Series",
      "Total resistance equals the sum of individual resistances"
    ],
    [
      "Parallel",
      "If one component breaks, the others continue working"
    ],
    [
      "Both",
      "The battery provides the total pd for the whole circuit"
    ]
  ],
  "title": "Series vs Parallel"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "6 V each — every branch in a parallel circuit has the same pd as the supply",
        true
      ],
      [
        "3 V each — the pd splits equally between the two parallel lamps",
        false
      ],
      [
        "12 V each — parallel doubles the voltage per branch",
        false
      ],
      [
        "Depends on lamp resistance — cannot determine without values",
        false
      ]
    ],
    "q": "Two lamps are connected in parallel across a 6 V battery. What is the pd across each lamp?",
    "wrong_explanations": {
      "1": "Pd splitting happens in SERIES. In PARALLEL, all branches have the SAME pd as the supply.",
      "2": "Parallel circuits never increase voltage beyond the supply.",
      "3": "In parallel, all branches have the supply pd regardless of resistance — only the branch CURRENT changes with resistance."
    }
  },
  {
    "opts": [
      [
        "Each appliance gets full mains voltage and works independently — switching one off doesn't affect others",
        true
      ],
      [
        "Parallel uses less total current so it is safer",
        false
      ],
      [
        "Series cannot carry enough current for multiple appliances",
        false
      ],
      [
        "Parallel wiring is cheaper to install",
        false
      ]
    ],
    "q": "Why is household wiring parallel rather than series?",
    "wrong_explanations": {
      "1": "Parallel draws MORE total current (I_total = sum of branches) — safety comes from fuses, not lower current.",
      "2": "Series wiring would mean each appliance gets a reduced share of 230 V and all would stop if one broke.",
      "3": "Cost is a secondary concern — the electrical reasons (full voltage, independent operation) are the key ones."
    }
  }
]
```
