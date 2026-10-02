# Background Radiation  (Physics, AQA 6.4.3 (physics only))

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
True spec reference: **8463 4.4.3.1** (under 4.4.3 "(physics only)"); no 8464 equivalent. The `spec` field "6.4.3" is the site's internal number.

| point | layer | spec ref |
|---|---|---|
| Sources of background, natural and man-made; UK shares (theory 1; key_note; matching) | triple | 8463 4.4.3.1 |
| Correcting for background (theory 2; equation; common_mistake) | triple | 8463 4.4.3.1; 4.4.2.1 |
| Dose in Sv / mSv; location and occupation (theory 3; key_note) | triple | 8463 4.4.3.1 |
| Radon and lung cancer (theory 3) | triple | 8463 4.4.3.1 |
| `higher` field | **triple, not HT** (4.4.3.1 has no HT label) — BACKGROUND-RADIATION-F2 | 8463 4.4.3.1 |
| quiz q1 | triple — stem WRONG ("corrected activity"), do not use as written — F1 | 8463 4.4.2.1 |
| quiz q2 | triple — usable (wording F4) | 8463 4.4.3.1 |

True page routes: TF TH. Site currently ships: TF TH — matches; the `higher` field is shown on TH only but is not HT — flagged F2.

## Spec core missing from the frozen data (written from the spec, examiner)
8463 4.4.3.1, verbatim (the parts the source omits):

> "man-made sources such as the fallout from nuclear weapons testing and nuclear accidents."
> "1000 millisieverts (mSv) = 1 sievert (Sv)"
> "Students will not need to recall the unit of radiation dose."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe sources of background radiation and explain why it must be considered in measurements.

## theory
```json
[
  {
    "content": "BACKGROUND RADIATION is low-level ionising radiation that is present everywhere in the environment at all times — from natural and artificial sources.\n\nIt is always present — even when no radioactive source is in the lab.\n\nSOURCES OF BACKGROUND RADIATION:\n\nNATURAL SOURCES (~85% of total in UK):\nRADON GAS (~50%): naturally occurring radioactive gas from uranium in rocks. Seeps into buildings. Major health risk in granite areas (e.g. Cornwall).\nGAMMA RAYS FROM GROUND AND BUILDINGS (~15%): radioactive isotopes in rocks (granite) and building materials.\nCOSMIC RAYS (~10%): high-energy particles from space. More at high altitude (pilots receive more).\nFOOD AND DRINK (~10%): small amounts of naturally occurring radioactive isotopes (e.g. ¹⁴C, ⁴⁰K).\n\nARTIFICIAL SOURCES (~15% of total):\nMEDICAL: X-rays, CT scans, nuclear medicine.\nNUCLEAR INDUSTRY: small amounts from nuclear power stations and waste.\nNUCLEAR WEAPONS TESTING: historical fallout still present.",
    "heading": "What Is Background Radiation?"
  },
  {
    "content": "WHY IT MATTERS FOR EXPERIMENTS:\nAll measurements of radioactive sources include background radiation.\nIf not corrected, measured activity appears higher than the true source activity.\n\nCORRECTING FOR BACKGROUND:\n1. Measure the count rate without any source present (background count rate).\n2. Measure the count rate with the source present.\n3. Subtract background: corrected count rate = measured count rate − background count rate.\n\nEXAMPLE:\nBackground count rate: 25 counts per minute.\nMeasured count rate with source: 175 counts per minute.\nCorrected count rate from source: 175 − 25 = 150 counts per minute.\n\nThis correction is important for accurate half-life calculations and activity measurements.\n\nVARIATION IN BACKGROUND:\nBackground radiation varies from place to place (geology, altitude).\nBackground radiation varies slightly over time (cosmic ray intensity fluctuates).\nThe count rate of the background should be measured over a long time period and averaged.",
    "heading": "Measuring and Correcting for Background"
  },
  {
    "content": "RADIATION DOSE is measured in SIEVERTS (Sv) or millisieverts (mSv).\nThe dose accounts for both the amount of radiation and its biological effect.\n\nUK AVERAGE ANNUAL DOSE: approximately 2.7 mSv.\nMajority from radon gas and medical procedures.\n\nFACTORS AFFECTING PERSONAL DOSE:\nLocation: granite areas → more radon → higher dose.\nOccupation: pilots, astronauts, nuclear workers → higher doses.\nMedical procedures: X-rays, CT scans add to dose.\nAltitude: more cosmic radiation at high altitude.\n\nRADON GAS RISK:\nRadon decays in lungs → alpha particles emitted → highly ionising → increases lung cancer risk.\nVentilating buildings in high-radon areas reduces exposure.\nRadon test kits available for homes in affected areas.\n\nBENEFIT vs RISK:\nMedical uses (imaging, treatment) involve weighing the benefit of diagnosis/treatment against radiation dose risk.\nRegulated exposure limits protect workers.",
    "heading": "Health Risks and Radiation Dose"
  }
]
```

## higher

Calculate corrected count rates by subtracting background. Evaluate the significance of different background radiation sources for different occupations (pilots, nuclear workers, radon-affected areas). Discuss the health implications of radon gas exposure and how it can be mitigated.

## common_mistake

Background radiation must be SUBTRACTED before any half-life calculations. Using the uncorrected count rate gives a half-life that appears longer than the true value because the count rate never falls to zero. Background should be measured BEFORE introducing any source.

## key_note

Background radiation: always present from natural (radon ~50%, cosmic, food, ground) and artificial (medical, nuclear) sources. Must subtract from measurements. Corrected count rate = measured − background. Dose in sieverts. UK average ~2.7 mSv/year. Radon main natural source — highest in granite areas.

## equations
```json
[
  "Corrected count rate = measured count rate − background count rate"
]
```

## matching
```json
{
  "instruction": "Match each source to its approximate contribution to UK background radiation.",
  "pairs": [
    [
      "Radon gas",
      "~50% of UK background — seeps from uranium in rocks into buildings"
    ],
    [
      "Cosmic rays",
      "~10% — high-energy particles from space, more at altitude"
    ],
    [
      "Medical sources",
      "~15% of total — X-rays, CT scans, nuclear medicine"
    ],
    [
      "Correcting for background",
      "Subtract background count rate from measured rate before calculating activity"
    ]
  ],
  "title": "Sources of Background Radiation"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "300 counts/min — corrected = 320 − 20 = 300 counts/min",
        true
      ],
      [
        "340 counts/min — 320 + 20 = 340 (added instead of subtracted)",
        false
      ],
      [
        "320 counts/min — background is too small to affect the measurement",
        false
      ],
      [
        "16 counts/min — 320 ÷ 20 = 16",
        false
      ]
    ],
    "q": "Background count rate is 20 counts/min. With a source present, the detector reads 320 counts/min. What is the corrected activity of the source?",
    "wrong_explanations": {
      "1": "Background must be SUBTRACTED, not added — adding would overestimate the source activity.",
      "2": "Background should always be corrected for, however small — accurate measurements require it.",
      "3": "Dividing has no physical meaning here — background is subtracted: 320 − 20 = 300."
    }
  },
  {
    "opts": [
      [
        "To establish the baseline radiation level so it can be subtracted from measurements — giving the true activity of the source alone",
        true
      ],
      [
        "To check the Geiger counter is working correctly before the experiment begins",
        false
      ],
      [
        "To calibrate the counter to zero — resetting it before use",
        false
      ],
      [
        "To measure the half-life of the background radiation",
        false
      ]
    ],
    "q": "Why is the background count rate measured before a radioactive source is introduced in an experiment?",
    "wrong_explanations": {
      "1": "Checking equipment is good practice but not the specific reason for measuring background — the purpose is subtraction for accurate source measurement.",
      "2": "Geiger counters don't need resetting to zero — they count ionisation events regardless.",
      "3": "Background radiation has no measurable half-life — it comes from many continuously replenished sources."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
