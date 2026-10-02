# Sampling Techniques  (Biology, AQA 4.7.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Why sample; random, representative, enough samples (theory 1) | base | 8464/8461 4.7.2.1; RP7/RP9 MS 2d |
| Quadrats, mean, scale up (theory 2) | base | 8464/8461 4.7.2.1; RP7/RP9 AT 1, 3, 6; MS 1d, 2b, 3a |
| Transects, belt/line (theory 3, first half) | base | 8464/8461 4.7.2.1; AT 3 |
| Continuous belt transect (not in the data) | triple (technique) | 8461 8.2.9 AT 8 |
| Mark-recapture (theory 3, second half; equation; variables; FIFA; common_mistake; quiz q2) | OFF-SPEC — not in 8464 or 8461 | — |
| `higher` — random coordinates (base RP method) + mark-recapture assumptions (off-spec) | base / OFF-SPEC — not HT | RP7/RP9 |
| `rp` | base — Combined RP7 / Biology RP9, not "RP6" | 8464 10.2.7; 8461 8.2.9 |
| key_note | base (mark-recapture sentence off-spec) | 8464/8461 4.7.2.1 |
| quiz q1 (quadrat scale-up) | base | MS 1d, 3a |
| quiz q2 (mark-recapture) | OFF-SPEC | — |
| quiz q3 (why random) | base | MS 2d |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches (but the `higher` random-coordinates method is hidden from CF and TF — flagged SAMP-F4; RP number flagged SAMP-F2).

## Spec core missing from the frozen data (written from the spec, examiner)
- 8464/8461 4.7.2.1: "A range of experimental methods using transects and quadrats are used by ecologists to determine the distribution and abundance of species in an ecosystem."
- 8464/8461 4.7.2.1: "In relation to abundance of organisms students should be able to: understand the terms mean, mode and median; calculate arithmetic means; plot and draw appropriate graphs selecting appropriate scales for the axes."
- 8464 RP7 / 8461 RP9: "measure the population size of a common species in a habitat. Use sampling techniques to investigate the effect of a factor on the distribution of this species."
- RP7/RP9 WS 2.3: "apply a range of techniques, including the use of transects and quadrats, and the measurement of an abiotic factor." WS 2.1: "develop hypotheses regarding distribution of a species as a consequence of a factor."
- 8461 RP9 only, AT 8: "use of appropriate techniques in more complex contexts including continuous sampling in an investigation."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how to estimate population size using quadrats, transects and mark-recapture.

## theory
```json
[
  {
    "content": "In ecology, it is usually IMPOSSIBLE to count every individual of a species in a habitat — the area is too large or the organisms too numerous.\n\nInstead, ecologists take a SAMPLE — they count organisms in a smaller, representative section of the habitat and use the results to estimate the total population.\n\nFor a sample to be valid:\nIt must be RANDOM — to avoid bias (e.g. choosing only the easiest areas to access).\nIt must be REPRESENTATIVE — reflect the full range of conditions in the habitat.\nA sufficient NUMBER of samples must be taken — to get a reliable mean.\n\nThree main sampling techniques:\n1. QUADRATS — for slow-moving or stationary organisms.\n2. TRANSECTS — to show how organisms change across a habitat.\n3. MARK-RECAPTURE — for mobile animals.",
    "heading": "Why We Sample"
  },
  {
    "content": "A QUADRAT is a square frame placed on the ground to define a sample area.\n\nTypically 0.5 m × 0.5 m (0.25 m²) or 1 m × 1 m for vegetation.\n\nHow to use quadrats:\n1. Place the quadrat RANDOMLY in the habitat (use random number tables or throw the quadrat over your shoulder).\n2. Count or estimate the abundance of the target species within the quadrat.\n3. Repeat many times across the habitat.\n4. Calculate the MEAN count per quadrat.\n5. SCALE UP: multiply the mean count by the total number of quadrat-sized areas in the whole habitat.\n\nFormula:\nEstimated population = (mean count per quadrat) × (total habitat area ÷ quadrat area)\n\nQUADRATS WORK BEST FOR:\nPlants, mosses, lichens.\nSlow-moving animals: limpets, snails, woodlice.\n\nNOT suitable for fast-moving animals — they escape before being counted.",
    "heading": "Quadrats"
  },
  {
    "content": "TRANSECTS:\nA transect is a LINE drawn across a habitat — organisms are recorded at regular intervals along the line.\n\nUsed to show how species DISTRIBUTION changes across a habitat (e.g. from sea to land on a rocky shore, or from open field to shaded woodland).\n\nBELT TRANSECT: a strip (e.g. 0.5 m wide) along the line — quadrats placed at regular intervals. Records abundance.\nLINE TRANSECT: simply records which species touch the line — presence/absence only.\n\nMARK-RECAPTURE (Lincoln Index):\nUsed for MOBILE ANIMALS that would escape quadrats.\n\nMethod:\n1. Capture a sample of the animal (n₁).\n2. Mark each individual (e.g. paint a small spot on a snail shell, attach a leg ring to a bird, clip a fin on a fish).\n3. Release marked individuals back into the habitat.\n4. Allow time for marked individuals to mix randomly with the population.\n5. Capture a second sample (n₂).\n6. Count the number of MARKED individuals in the second sample (m).\n\nFormula: N = (n₁ × n₂) ÷ m\n\nASSUMPTIONS for the formula to be valid:\nThe mark does not affect survival (does not make animals more visible to predators or less able to move).\nMarked animals mix randomly with the rest of the population.\nNo significant immigration, emigration, births or deaths between the two captures.\nAll individuals are equally likely to be captured.",
    "heading": "Transects and Mark-Recapture"
  }
]
```

## higher

Mark-recapture formula: N = (n₁ × n₂) ÷ m. Assumptions: random mixing of marked animals, no significant births/deaths/migration between captures, marking does not affect survival or recapture probability. Students should be able to evaluate the validity of these assumptions in given scenarios. Students should be able to use random number tables or coordinates to ensure random quadrat placement, reducing sampling bias.

## common_mistake

In the mark-recapture formula N = (n₁ × n₂) ÷ m — students often confuse what n₁, n₂ and m represent. n₁ = first catch (all marked). n₂ = second catch (total number caught). m = marked individuals IN the second catch. Do NOT divide by n₂ or mix up m and n₂.

## key_note

Quadrats: random placement, count organisms, scale up. Transects: show distribution change across habitat. Mark-recapture: N = (n₁ × n₂) ÷ m — for mobile animals. Assumptions: random mixing, no population changes, mark doesn't harm animal.

## equations
```json
[
  "N = (n₁ × n₂) ÷ m"
]
```

## fifas
```json
[
  {
    "label": "Mark-Recapture Calculation",
    "question": "A student catches 40 woodlice, marks them and releases them. The next day, they catch 30 woodlice and find that 6 are marked. Estimate the population.",
    "steps": [
      [
        "F",
        "N = (n₁ × n₂) ÷ m"
      ],
      [
        "I",
        "N = (40 × 30) ÷ 6"
      ],
      [
        "F",
        "N = 1200 ÷ 6"
      ],
      [
        "A",
        "N = 200 woodlice"
      ]
    ]
  }
]
```

## rp

RP6 — Use quadrats or transects to estimate population size or distribution of a species in a habitat. Place quadrats randomly and calculate mean count. Scale up to total habitat area.

## variables
```json
[
  [
    "N",
    "Estimated population size",
    "individuals",
    ""
  ],
  [
    "n₁",
    "Number caught and marked in first sample",
    "individuals",
    ""
  ],
  [
    "n₂",
    "Total number caught in second sample",
    "individuals",
    ""
  ],
  [
    "m",
    "Number of marked individuals in second sample",
    "individuals",
    ""
  ]
]
```

## matching
```json
{
  "instruction": "Match each situation to the best sampling technique.",
  "pairs": [
    [
      "Quadrats",
      "Estimating the population of daisies in a field — stationary plants, random placement"
    ],
    [
      "Transect",
      "Showing how plant species change from an open beach to a sheltered dune"
    ],
    [
      "Mark-recapture",
      "Estimating the population of great crested newts in a pond — mobile animals"
    ],
    [
      "Quadrats",
      "Counting the abundance of limpets on different zones of a rocky shore"
    ],
    [
      "Transect",
      "Recording how lichen cover changes from a roadside to open countryside"
    ]
  ],
  "title": "Match the Sampling Technique"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "2000 — mean count (4) × (total area ÷ quadrat area) = 4 × 500 = 2000",
        true
      ],
      [
        "40 — mean count × number of quadrats = 4 × 10",
        false
      ],
      [
        "500 — total area of field",
        false
      ],
      [
        "50 — total area ÷ number of quadrats",
        false
      ]
    ],
    "q": "A student places 10 quadrats (each 1 m²) randomly in a field (total area 500 m²). Mean dandelion count = 4 per quadrat. Estimate the dandelion population.",
    "wrong_explanations": {
      "1": "40 gives the total counted in ALL quadrats — not the estimated population of the whole field.",
      "2": "500 is just the field area — it has nothing to do with the dandelion count.",
      "3": "50 is just a spatial measurement — the estimated population requires scaling the mean count up to the full habitat area."
    }
  },
  {
    "opts": [
      [
        "100 — N = (25 × 20) ÷ 5 = 100",
        true
      ],
      [
        "250 — N = 25 × 20 ÷ 2 (dividing by wrong number)",
        false
      ],
      [
        "2500 — N = 25 × 20 × 5 (multiplying instead of dividing)",
        false
      ],
      [
        "1 — N = 5 ÷ (25 × 20)",
        false
      ]
    ],
    "q": "In a mark-recapture study: 25 snails marked (n₁), 20 caught second time (n₂), 5 were marked (m). What is the estimated population?",
    "wrong_explanations": {
      "1": "N = (n₁ × n₂) ÷ m = (25 × 20) ÷ 5 = 500 ÷ 5 = 100. Make sure to divide by m (number of marked in second catch = 5), not by n₂.",
      "2": "N = (n₁ × n₂) ÷ m = (25 × 20) ÷ 5 = 100. Multiplying gives an enormous overestimate.",
      "3": "The formula is N = (n₁ × n₂) ÷ m — not the inverse. Dividing m by the product gives a nonsensically small number."
    }
  },
  {
    "opts": [
      [
        "To avoid sampling bias — deliberately choosing areas with lots of organisms would overestimate the population",
        true
      ],
      [
        "Random placement ensures all quadrats are the same size",
        false
      ],
      [
        "Random placement prevents disturbing the organisms in the habitat",
        false
      ],
      [
        "It is a legal requirement for ecological surveys",
        false
      ]
    ],
    "q": "Why must quadrats be placed RANDOMLY in a habitat?",
    "wrong_explanations": {
      "1": "Quadrat size is fixed by the frame — it doesn't change with placement method.",
      "2": "Disturbance is minimised by careful technique — but the reason for random placement is specifically about statistical validity and avoiding bias.",
      "3": "There is no legal requirement for randomness — it is a scientific requirement to ensure the sample is representative of the whole habitat."
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

**Question:** A student catches 40 woodlice, marks them and releases them. The next day, they catch 30 woodlice and find that 6 are marked. Estimate the population.

**Convert:** [NEW — examined ✓] Nothing to convert — n₁, n₂ and m are already plain counts of individuals in matching units.

**F:** N = (n₁ × n₂) ÷ m

**I:** N = (40 × 30) ÷ 6

**F:** N = 1200 ÷ 6

**A:** N = 200 woodlice
