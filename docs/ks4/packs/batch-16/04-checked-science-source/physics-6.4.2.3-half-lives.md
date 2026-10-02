# Half-Lives and Radioactive Decay  (Physics, AQA 6.4.2.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Random decay; large-sample predictability (theory 1; key_note) | base | 8464 6.4.2.3; 8463 4.4.2.3 |
| Half-life definition; constant for an isotope (theory 2; key_note; q2) | base | 8464 6.4.2.3 |
| Half-life from a graph or data (theory 3) | base | 8464 6.4.2.3 (MS 4a) |
| What remains after n half-lives by repeated halving (theory 2 example; common_mistake; q1) | base | 8464 6.4.2.3 |
| Fraction remaining (½)ⁿ / N = N₀(½)ⁿ / net decline as a ratio (theory 2; equation; FIFA second F step) | **higher** — HALF-LIVES-F1 | 8464 6.4.2.3 (HT only) |
| FIFA overall: n = t ÷ T½ then N = N₀(½)ⁿ — chains two steps | base result (by halving); Step 2 as (½)ⁿ is higher — F4 | 8464 6.4.2.3 |
| Example half-lives; hazard differs with half-life; nuclear waste (theory 2–3) | **triple** | 8463 4.4.3.2 (physics only) |
| Tracers, cancer treatment — choosing isotopes (theory 3; `higher`; key_note; matching) | **triple** (not HT) — F2 | 8463 4.4.3.2–4.4.3.3 (physics only) |
| Background radiation; subtract it (theory 3; common_mistake; key_note) | **triple** — F2 | 8463 4.4.3.1 (physics only) |
| Carbon dating (theory 3; key_note) | not in spec (context) | — |
| `higher` field | ratio clause higher; "cannot be changed" base; "compare isotopes" triple — F2 | 8464 6.4.2.3; 8463 4.4.3.2 |
| quiz q1, q2 | base — both usable (q1 wx3 imprecise, F5) | 8464 6.4.2.3 |

True page routes: CF CH TF TH (base page + HT layer + triple layer). Site currently ships: CF CH TF TH — matches; the `higher` field carries triple content as if it were HT — flagged HALF-LIVES-F2.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Define half-life, calculate remaining activity and explain the random nature of decay.

## theory
```json
[
  {
    "content": "Radioactive decay is a RANDOM PROCESS:\nIt is impossible to predict exactly WHEN any individual nucleus will decay.\nIt is impossible to predict WHICH nucleus in a sample will decay next.\nDecay is spontaneous — NOT triggered by temperature, pressure or chemical state.\n\nHowever, for a LARGE SAMPLE:\nWe can predict the PROPORTION that will decay in a given time.\nStatistical behaviour becomes predictable even though individual decays are random.\n\nThis is similar to flipping a large number of coins — we cannot predict any individual flip, but we can confidently predict about 50% will be heads.\n\nACTIVITY decreases over time as the number of unstable nuclei falls.",
    "heading": "Radioactive Decay Is Random"
  },
  {
    "content": "The HALF-LIFE of a radioactive isotope is the time for:\nThe number of UNDECAYED NUCLEI to halve, OR\nThe ACTIVITY (or count rate) of the source to halve.\n\nHalf-life is CONSTANT for a given isotope — it doesn't change.\n\nEXAMPLES:\nCarbon-14: half-life ~5730 years (used in carbon dating)\nIodine-131: half-life ~8 days (medical uses — short enough to leave the body)\nUranium-238: half-life ~4.5 billion years\nRadon-222: half-life ~3.8 days\n\nCALCULATING REMAINING ACTIVITY/NUCLEI:\nAfter 1 half-life: ½ remains\nAfter 2 half-lives: ¼ remains\nAfter 3 half-lives: ⅛ remains\nAfter n half-lives: (½)ⁿ remains\n\nEXAMPLE:\nSource starts at 800 Bq. Half-life = 2 hours. What is the activity after 6 hours?\n6 hours ÷ 2 hours = 3 half-lives\n800 → 400 → 200 → 100 Bq",
    "heading": "Half-Life"
  },
  {
    "content": "DECAY CURVE:\nGraph of activity (or count rate) against time.\nCurve starts high and decreases exponentially.\nTo find half-life from graph: find initial activity, halve it, read off time → then verify the next halving takes the same time.\n\nPRACTICAL SELECTION of isotopes:\nMEDICAL TRACERS: short half-life needed — activity falls quickly so patient receives minimal long-term dose. Technetium-99m: 6 hours.\nCANCER TREATMENT: short enough to deliver dose in treatment window, then decay away.\nCARBON DATING: 14C half-life ~5730 years — compares ¹⁴C/¹²C ratio of living things vs sample.\nNUCLEAR WASTE: long half-life isotopes are the biggest storage problem — some remain dangerous for thousands of years.\n\nBACKGROUND RADIATION:\nAll measurements of radioactive sources include BACKGROUND RADIATION — radiation from natural sources (rocks, cosmic rays, radon gas, food).\nBackground must be measured and SUBTRACTED from readings.",
    "heading": "Uses of Half-Life and Decay Curves"
  }
]
```

## higher

Use the concept of half-life to calculate the number of undecayed nuclei or activity remaining after a given number of half-lives. Explain why half-life cannot be changed by physical or chemical means — it is a fundamental nuclear property. Compare the suitability of different isotopes for specific uses based on their half-lives and radiation type.

## common_mistake

After each half-life, the activity halves AGAIN from its current value — not from the original. After 3 half-lives starting at 1000 Bq: 500 → 250 → 125 Bq. Also: background radiation must be subtracted before half-life calculations.

## key_note

Half-life: time for activity (or nuclei count) to halve. Constant for a given isotope. Random decay — can't predict individual nucleus. After n half-lives: (½)ⁿ remains. Decay curve: exponential fall. Background radiation must be subtracted. Medical tracers need short half-lives; carbon dating uses 5730-year ¹⁴C half-life.

## equations
```json
[
  "After n half-lives: fraction remaining = (½)ⁿ"
]
```

## fifas
```json
[
  {
    "label": "Half-Life Calculation",
    "question": "A source has initial activity 960 Bq. Its half-life is 3 hours. What is the activity after 12 hours?",
    "steps": [
      [
        "F",
        "Number of half-lives = total time ÷ half-life; remaining = initial × (½)ⁿ"
      ],
      [
        "I",
        "n = 12 ÷ 3 = 4 half-lives"
      ],
      [
        "F",
        "960 × (½)⁴ = 960 × 1/16 = 960 ÷ 16"
      ],
      [
        "A",
        "Activity = 60 Bq"
      ]
    ]
  }
]
```

## matching
```json
{
  "instruction": "Match each scenario to the correct remaining activity.",
  "pairs": [
    [
      "400 Bq",
      "Initial activity 1600 Bq, after 2 half-lives: 1600 → 800 → 400"
    ],
    [
      "125 Bq",
      "Initial activity 1000 Bq, after 3 half-lives: 1000 → 500 → 250 → 125"
    ],
    [
      "Longer half-life needed",
      "Carbon dating — need isotope with half-life comparable to age of sample (thousands of years)"
    ],
    [
      "Shorter half-life needed",
      "Medical tracer — activity must fall quickly to reduce patient radiation dose"
    ]
  ],
  "title": "Half-Life Calculations"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "80 Bq — 12 ÷ 4 = 3 half-lives; 640 → 320 → 160 → 80 Bq",
        true
      ],
      [
        "160 Bq — only 2 half-lives calculated (8 hours, not 12)",
        false
      ],
      [
        "320 Bq — only 1 half-life applied",
        false
      ],
      [
        "0 Bq — the source has fully decayed after 12 hours",
        false
      ]
    ],
    "q": "A radioactive source has a half-life of 4 hours and initial activity 640 Bq. What is the activity after 12 hours?",
    "wrong_explanations": {
      "1": "12 ÷ 4 = 3 half-lives. After 2: 640 → 320 → 160 (only 8 hours). After 3: → 80 Bq.",
      "2": "After 1 half-life (4 h): 640 → 320. After 2 (8 h): → 160. After 3 (12 h): → 80.",
      "3": "Radioactive sources never fully reach zero — activity halves each half-life but never reaches exactly zero (exponential decay)."
    }
  },
  {
    "opts": [
      [
        "It always takes the same time for the activity to halve, regardless of temperature, pressure or how much has already decayed",
        true
      ],
      [
        "It stays constant because the number of atoms in the sample doesn't change",
        false
      ],
      [
        "It is constant because decay rate increases to compensate as fewer atoms remain",
        false
      ],
      [
        "It is constant only at room temperature — at high temperatures the half-life changes",
        false
      ]
    ],
    "q": "Why is the half-life of a radioactive isotope described as a 'constant'?",
    "wrong_explanations": {
      "1": "The number of undecayed atoms DOES decrease — but the proportion that decay per unit time stays fixed, so the time to halve is always the same.",
      "2": "If rate increased to compensate, activity would stay constant — but it falls exponentially, halving each half-life.",
      "3": "Half-life is independent of temperature, pressure, or chemical state — this is one of the key properties of radioactive decay."
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

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A source has initial activity 960 Bq. Its half-life is 3 hours. What is the activity after 12 hours?

**Convert:** [NEW — examiner-corrected] Nothing to convert — the total time (12 hours) and the half-life (3 hours) are already in the same unit. n = total time ÷ half-life only needs both times in the SAME unit (any unit — seconds are never required); if they differed, you would convert one to match the other first.

**F:** Number of half-lives = total time ÷ half-life; remaining = initial × (½)ⁿ

**I:** n = 12 ÷ 3 = 4 half-lives

**F:** 960 × (½)⁴ = 960 × 1/16 = 960 ÷ 16

**A:** Activity = 60 Bq
