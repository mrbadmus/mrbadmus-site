# Chemical Measurements  (Chemistry, AQA 5.3.1.4)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Accuracy vs precision (theory 1; key_note) | base (use WS 3.7 wording — CM-F4) | 8464 5.3.1.4; WS 3.7 |
| Units and conversions (theory 1) | base | 8464 5.3.1.4 |
| Uncertainty; random and systematic error; repeats and mean (theory 2) | base | 8464 5.3.1.4; WS 3.7 |
| % uncertainty (theory 2; equations; variables; key_note; FIFA) | not in spec — extension only (CM-F2) | — |
| Apparatus, meniscus, parallax, tare (theory 3; common_mistake) | base | AT 1; WS 3.7 |
| quiz q1 | base idea, off-spec calculation — extension only | WS 3.7 |
| quiz q2 | base — do not use as written (CM-F3) | AT 1 |
| Range about the mean as uncertainty | base — MISSING from the data (below) | 8464 5.3.1.4; 8462 4.3.1.4 |

True page routes: CF CH TF TH, all base. Site currently ships: CF CH TF TH — matches.

## Spec core missing from the frozen data (written from the spec, examiner)
8464 5.3.1.4 = 8462 4.3.1.4 (base, all routes), verbatim: "Whenever a measurement is made there is always some uncertainty about the result obtained. Students should be able to: represent the distribution of results and make estimations of uncertainty; use the range of a set of measurements about the mean as a measure of uncertainty."

WS 3.7, verbatim: "An accurate measurement is one that is close to the true value. Measurements are precise if they cluster closely. Measurements are repeatable when repetition, under the same conditions by the same investigator, gives similar results. Measurements are reproducible if similar results are obtained by different investigators with different equipment. Measurements are affected by random error due to results varying in unpredictable ways; these errors can be reduced by making more measurements and reporting a mean value. Systematic error is due to measurement results differing from the true value by a consistent amount each time."

What Design needs (examiner): the uncertainty is ± half the range about the mean. Worked example: titres 24.10, 24.30, 24.20 cm³ → mean 24.20 cm³; range 0.20 cm³; result 24.20 ± 0.10 cm³.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the importance of precise measurements in chemistry and sources of uncertainty.

## theory
```json
[
  {
    "content": "Quantitative chemistry relies on PRECISE and ACCURATE measurements.\n\nACCURACY — how close a measurement is to the TRUE value.\nPRECISION — how reproducible/consistent measurements are (close to each other).\n\nA measurement can be precise but not accurate (consistently wrong), or accurate but not precise (correct on average but variable).\n\nIn chemistry, measurements include:\nMASSES — measured using a balance (in grams, g).\nVOLUMES of solutions — measured using a burette, pipette or measuring cylinder (in cm³ or dm³).\nTEMPERATURES — measured using a thermometer (in °C).\nTIMES — measured using a stopwatch (in seconds).\n\nUnits matter enormously:\n1 dm³ = 1 litre = 1000 cm³\n1 cm³ = 0.001 dm³ = 1 mL",
    "heading": "Why Measurements Matter in Chemistry"
  },
  {
    "content": "Every measurement has some UNCERTAINTY — a range within which the true value lies.\n\nSources of uncertainty:\nREADING ERROR — difficulty in reading exact values from scales (e.g. reading a burette between markings).\nSYSTEMATIC ERROR — a consistent bias in one direction (e.g. a balance not zeroed correctly, a calibration error).\nRANDOM ERROR — unpredictable variations that scatter measurements around the true value.\n\nReduce uncertainty by:\nUsing more precise equipment (e.g. a 25 cm³ pipette is more precise than a 100 cm³ measuring cylinder).\nTaking REPEAT measurements and calculating a MEAN.\nUsing appropriate measuring equipment for the scale of measurement.\n\nPercentage uncertainty = (uncertainty ÷ measured value) × 100\n\nThe percentage uncertainty of a small measurement is higher than that of a large measurement with the same absolute uncertainty — this is why measuring small volumes with a large cylinder is poor practice.",
    "heading": "Uncertainty in Measurements"
  },
  {
    "content": "Common measuring equipment and their precision:\n\nBALANCE (digital): typically ±0.01 g or ±0.001 g — high precision.\n\nBURETTE: 50 cm³ burette with 0.1 cm³ markings. Read to ±0.05 cm³ (between markings). Used for accurate volume delivery in titrations.\n\nPIPETTE: fixed volume (e.g. exactly 25.00 cm³). Very high precision for delivering one specific volume. Used to deliver precise volumes of solutions.\n\nMEASURING CYLINDER: less precise than a burette or pipette. Read from the BOTTOM of the MENISCUS (the curved water surface).\n\nTHERMOMETER: typically ±1°C or ±0.5°C depending on type.\n\nKEY SKILLS:\nRead burettes and measuring cylinders at eye level to avoid PARALLAX ERROR.\nRead from the BOTTOM of the meniscus for water-based solutions.\nZero the balance before each measurement (tare).\nRepeat and average for reliability.",
    "heading": "Practical Measurement Techniques"
  }
]
```

## common_mistake

Read the volume from the BOTTOM of the meniscus — not the top. Water curves downward in a glass tube, creating a concave meniscus. Reading from the top overestimates the volume. Also: zeroing the balance (taring) before each measurement is essential — failing to do so introduces a systematic error.

## key_note

Accuracy: how close to true value. Precision: how reproducible. Burette: ±0.05 cm³ — most precise for volumes. Pipette: exact fixed volume. Read from bottom of meniscus at eye level. % uncertainty = (uncertainty ÷ measured value) × 100. Larger measurement → smaller % uncertainty.

## equations
```json
[
  "% uncertainty = (uncertainty ÷ measured value) × 100"
]
```

## fifas
```json
[
  {
    "label": "Percentage Uncertainty",
    "question": "A student measures 25.0 cm³ of solution using a measuring cylinder with an uncertainty of ±0.5 cm³. Calculate the percentage uncertainty.",
    "steps": [
      [
        "F",
        "% uncertainty = (uncertainty ÷ measured value) × 100"
      ],
      [
        "I",
        "% uncertainty = (0.5 ÷ 25.0) × 100"
      ],
      [
        "F",
        "% uncertainty = 0.02 × 100"
      ],
      [
        "A",
        "% uncertainty = 2.0%"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "% uncertainty",
    "Percentage uncertainty",
    "%",
    ""
  ]
]
```

## matching
```json
{
  "instruction": "Match each piece of equipment to its use and precision.",
  "pairs": [
    [
      "Burette",
      "Accurately delivers variable volumes of solution — read to ±0.05 cm³ — used in titrations"
    ],
    [
      "Pipette",
      "Delivers one precise fixed volume — e.g. exactly 25.00 cm³ of solution"
    ],
    [
      "Measuring cylinder",
      "Less precise volume measurement — read from bottom of meniscus"
    ],
    [
      "Digital balance",
      "Measures mass precisely — typically ±0.01 g — zero before each use"
    ],
    [
      "Thermometer",
      "Measures temperature — typically ±0.5°C or ±1°C"
    ]
  ],
  "title": "Match the Measuring Equipment"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "The burette — % uncertainty = (0.05 ÷ 25) × 100 = 0.2%, vs the cylinder at 4%",
        true
      ],
      [
        "The measuring cylinder — larger equipment is always more accurate",
        false
      ],
      [
        "They are the same — both deliver 25 cm³",
        false
      ],
      [
        "The measuring cylinder — it has a smaller absolute uncertainty",
        false
      ]
    ],
    "q": "A student measures a volume using a burette and a measuring cylinder. The burette has an uncertainty of ±0.05 cm³ and the cylinder ±1 cm³. Both deliver 25 cm³. Which gives the lower percentage uncertainty?",
    "wrong_explanations": {
      "1": "Equipment size doesn't determine accuracy — precision depends on the uncertainty relative to the measurement.",
      "2": "Both deliver the same VOLUME but with different UNCERTAINTIES — the burette (±0.05) is far more precise than the measuring cylinder (±1).",
      "3": "The measuring cylinder has a LARGER absolute uncertainty (±1 cm³ vs ±0.05 cm³) — it is LESS precise, not more."
    }
  },
  {
    "opts": [
      [
        "From the bottom of the meniscus — water curves downward, creating a concave surface",
        true
      ],
      [
        "From the top of the meniscus — this gives the largest volume reading",
        false
      ],
      [
        "From the middle of the meniscus — splitting the difference",
        false
      ],
      [
        "It doesn't matter — the meniscus reading is always correct",
        false
      ]
    ],
    "q": "When reading a burette or measuring cylinder containing water, where should you read the volume?",
    "wrong_explanations": {
      "1": "Reading from the TOP of the meniscus gives an overestimate — the markings are calibrated for the bottom of the meniscus.",
      "2": "Reading from the middle introduces error — always read from the BOTTOM consistently to match calibration.",
      "3": "Reading from the wrong part of the meniscus introduces a systematic error — it DOES matter and affects accuracy."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A student measures 25.0 cm³ of solution using a measuring cylinder with an uncertainty of ±0.5 cm³. Calculate the percentage uncertainty.

**Convert:** [NEW — examined ✓] Nothing to convert — the measured volume and its uncertainty are both already in cm³, the same unit.

**F:** % uncertainty = (uncertainty ÷ measured value) × 100

**I:** % uncertainty = (0.5 ÷ 25.0) × 100

**F:** % uncertainty = 0.02 × 100

**A:** % uncertainty = 2.0%
