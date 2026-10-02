# Relative Atomic Mass, Atomic Number and Isotopes  (Chemistry, AQA 5.1.1.6)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Atomic number, mass number, neutrons = A − Z (theory 1; equations 1–2; key_note) | base. Periodic-table sentence imprecise (F4) | 8464 5.1.1.4–5.1.1.5; 8462 4.1.1.4–4.1.1.5 |
| Isotopes; same chemical / different physical properties (theory 2; common_mistake; q1) | base | 8464 5.1.1.5; 8462 4.1.1.5 |
| Ar = weighted mean; Σ(% × mass number) ÷ 100; chlorine example (theory 3; equation 3; q2) | base. "NOT a whole number" imprecise (F3) | 8464 5.1.1.6; 8462 4.1.1.6 |
| FIFA boron | base. **Insert line WRONG**: missing brackets (F1) | 8464 5.1.1.6; 8462 4.1.1.6 |
| `higher`: mass spectrometry / mass spectra | not in spec (F2) | — |
| quiz q1, q2 | base, usable as written | 8464 5.1.1.5–5.1.1.6 |

True page routes: CF CH TF TH, with no HT layer. Site currently ships: CF CH TF TH, which matches. The `higher` copy (CH/TH) is off-spec and flagged (F2).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Define atomic number, mass number, isotopes and relative atomic mass — and calculate Ar from isotope abundances.

## theory
```json
[
  {
    "content": "Every element is defined by its ATOMIC NUMBER (proton number):\n\nATOMIC NUMBER (Z) = number of PROTONS in the nucleus.\nThis is unique to each element — all carbon atoms have 6 protons, all iron atoms have 26.\nIn a neutral atom: protons = electrons.\n\nMASS NUMBER (A) = total number of PROTONS + NEUTRONS in the nucleus.\n\nFrom these two numbers:\nNeutrons = mass number − atomic number\n\nExample — sodium-23:\nMass number = 23, atomic number = 11.\nProtons = 11, electrons = 11 (neutral), neutrons = 23 − 11 = 12.\n\nIn the periodic table, the ATOMIC NUMBER is the SMALLER number (it cannot exceed the mass number as you cannot have negative neutrons).",
    "heading": "Atomic Number and Mass Number"
  },
  {
    "content": "ISOTOPES are atoms of the SAME ELEMENT with the SAME ATOMIC NUMBER but DIFFERENT MASS NUMBERS.\n\nSame protons → same element → same chemical properties.\nDifferent neutrons → different mass → different physical properties (e.g. density, rate of diffusion).\n\nIsotopes have IDENTICAL CHEMICAL behaviour — because chemical reactions depend on electron configuration (determined by proton number, which is the same).\n\nExamples:\nCARBON ISOTOPES:\nCarbon-12 (¹²C): 6p + 6n — the standard (98.9% of carbon)\nCarbon-13 (¹³C): 6p + 7n — stable, ~1.1%\nCarbon-14 (¹⁴C): 6p + 8n — radioactive, used in carbon dating\n\nCHLORINE ISOTOPES:\nChlorine-35 (³⁵Cl): 17p + 18n — ~75% of chlorine\nChlorine-37 (³⁷Cl): 17p + 20n — ~25% of chlorine\nBecause of this mixture, the Ar of chlorine ≈ 35.5 — between the two isotope masses.",
    "heading": "Isotopes"
  },
  {
    "content": "The RELATIVE ATOMIC MASS (Ar) is the WEIGHTED AVERAGE mass of all atoms of an element compared to 1/12 of the mass of a carbon-12 atom.\n\nBecause most elements have multiple isotopes in different abundances, Ar is NOT a whole number.\n\nFormula:\nAr = Σ (% abundance × mass number) ÷ 100\n\nExample — chlorine:\nAr = (75 × 35 + 25 × 37) ÷ 100\nAr = (2625 + 925) ÷ 100\nAr = 3550 ÷ 100 = 35.5\n\nThis explains why periodic table Ar values are often not whole numbers — they are weighted averages across all naturally occurring isotopes.",
    "heading": "Relative Atomic Mass"
  }
]
```

## higher

Use mass spectrometry data to calculate Ar from isotope masses and percentage abundances. Interpret mass spectra showing relative abundance on y-axis and mass/charge on x-axis. Understand that non-integer Ar values result from isotope mixtures.

## common_mistake

Ar is a WEIGHTED average — not a simple average. Chlorine has Ar 35.5 because ~75% is Cl-35 and only ~25% is Cl-37. If both were 50/50, Ar would be 36. The heavier isotope has LESS influence because it's less abundant. Also: isotopes have SAME chemical properties (same electrons) but DIFFERENT physical properties (different mass).

## key_note

Atomic number = protons. Mass number = protons + neutrons. Neutrons = mass number − atomic number. Isotopes: same element, same protons, different neutrons — same chemical, different physical properties. Ar = weighted average of isotope masses.

## equations
```json
[
  "Mass number = protons + neutrons",
  "Neutrons = mass number − atomic number",
  "Ar = Σ(% abundance × mass number) ÷ 100"
]
```

## fifas
```json
[
  {
    "label": "Relative Atomic Mass Calculation",
    "question": "Boron has two isotopes: 20% boron-10 and 80% boron-11. Calculate the relative atomic mass of boron.",
    "steps": [
      [
        "F",
        "Ar = Σ(% abundance × mass number) ÷ 100"
      ],
      [
        "I",
        "Ar = (20 × 10) + (80 × 11) ÷ 100"
      ],
      [
        "F",
        "Ar = (200 + 880) ÷ 100 = 1080 ÷ 100"
      ],
      [
        "A",
        "Ar = 10.8"
      ]
    ]
  }
]
```

## matching
```json
{
  "instruction": "Match each term to its correct definition.",
  "pairs": [
    [
      "Atomic number",
      "Number of protons — unique to each element"
    ],
    [
      "Mass number",
      "Total protons + neutrons in the nucleus"
    ],
    [
      "Isotopes",
      "Same element, same protons, different number of neutrons"
    ],
    [
      "Relative atomic mass",
      "Weighted average of all isotope masses — often not a whole number"
    ],
    [
      "Number of neutrons",
      "Mass number minus atomic number"
    ]
  ],
  "title": "Atomic Number, Mass Number and Isotopes"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Same: atomic number (17 protons and 17 electrons). Different: mass number — Cl-35 has 18 neutrons, Cl-37 has 20 neutrons.",
        true
      ],
      [
        "Same: mass number. Different: atomic number and proton count.",
        false
      ],
      [
        "Same: everything — isotopes are identical atoms.",
        false
      ],
      [
        "Same: neutron number. Different: proton number.",
        false
      ]
    ],
    "q": "Chlorine-35 and chlorine-37 are isotopes. What is the same and what differs between them?",
    "wrong_explanations": {
      "1": "If mass numbers were the same they would be identical — isotopes are DEFINED by having different mass numbers.",
      "2": "Isotopes DO have the same chemical properties — but they are NOT identical. They differ in neutron count and mass.",
      "3": "If neutron numbers were the same but proton numbers differed, they would be different ELEMENTS — not isotopes."
    }
  },
  {
    "opts": [
      [
        "63.8 — Ar = (60 × 63 + 40 × 65) ÷ 100 = 6380 ÷ 100",
        true
      ],
      [
        "64.0 — simple average of 63 and 65",
        false
      ],
      [
        "128 — total of both mass numbers added together",
        false
      ],
      [
        "63 — just the most abundant isotope mass",
        false
      ]
    ],
    "q": "An element has two isotopes: 60% at mass 63 and 40% at mass 65. What is its Ar?",
    "wrong_explanations": {
      "1": "Simple average gives 64 only if BOTH isotopes are 50/50 abundant. Since there is more of the lighter isotope (60% at mass 63), the weighted average is pulled below 64.",
      "2": "Adding mass numbers has no physical meaning — Ar is a weighted average, not a sum.",
      "3": "Using only the most abundant isotope ignores the 40% contribution from mass 65 — the true Ar is pulled above 63 by the heavier isotope."
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

**Question:** Boron has two isotopes: 20% boron-10 and 80% boron-11. Calculate the relative atomic mass of boron.

**Convert:** [NEW — examined ✓] Nothing to convert — the percentage abundances and the isotope mass numbers are already in matching, dimensionless units for the formula.

**F:** Ar = Σ(% abundance × mass number) ÷ 100

**I:** Ar = (20 × 10) + (80 × 11) ÷ 100

**F:** Ar = (200 + 880) ÷ 100 = 1080 ÷ 100

**A:** Ar = 10.8
