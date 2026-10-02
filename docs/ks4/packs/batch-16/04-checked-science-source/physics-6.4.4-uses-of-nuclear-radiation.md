# Uses of Nuclear Radiation  (Physics, AQA 6.4.4 (physics only))

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
True spec reference: **8463 4.4.3.3** (and 4.4.3.2 for half-life choice), both "(physics only)"; no 8464 equivalent. The `spec` field "6.4.4" is the site's internal number.

| point | layer | spec ref |
|---|---|---|
| Radiotherapy; tracers; gamma camera (theory 1; common_mistake; key_note; matching) | triple | 8463 4.4.3.3 |
| Choosing half-life for a use (theory 3; key_note) | triple | 8463 4.4.3.2 |
| Sterilisation (theory 1) | base application | 8464 6.4.2.1; 6.4.2.4 |
| Thickness gauges, smoke detectors, pipelines (theory 2; q1) — already in batch 5 `radioactive-decay` | base application — USES-OF-NUCLEAR-RADIATION-F5 | 8464 6.4.2.1 |
| Choosing type by ionisation/penetration (theory 3) | base | 8464 6.4.2.1 |
| Carbon dating (theory 2) | not in spec (context) | — |
| `higher` field | **triple, not HT** — F1 | 8463 4.4.3.2–4.4.3.3 |
| Evaluate perceived risks from data — missing (F2) | triple | 8463 4.4.3.3 |
| quiz q1 | base application — usable | 8464 6.4.2.1 |
| quiz q2 | triple — usable | 8463 4.4.3.2–4.4.3.3 |

True page routes: TF TH. Site currently ships: TF TH — matches; the `higher` field is shown on TH only but is not HT — flagged F1.

## Spec core missing from the frozen data (written from the spec, examiner)
8463 4.4.3.3, verbatim (the bullet the source never addresses):

> "Students should be able to: … evaluate the perceived risks of using nuclear radiations in relation to given data and consequences."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the uses of alpha, beta and gamma radiation in medicine and industry.

## theory
```json
[
  {
    "content": "CANCER TREATMENT (RADIOTHERAPY):\nGamma rays from cobalt-60 focused on tumour from multiple directions.\nCrossing beams concentrate dose at tumour — minimise dose to surrounding healthy tissue.\nKills cancer cells by damaging DNA.\nGamma used because it penetrates deeply enough to reach internal tumours.\n\nMEDICAL TRACERS:\nA gamma-emitting radioisotope injected into patient.\nGamma camera detects distribution of the tracer in the body.\nReveals function of organs (not just structure like X-rays).\nTechnetium-99m: short half-life (~6 hours) — activity falls rapidly → low patient dose.\nIodine-123: accumulates in thyroid → used to diagnose thyroid disorders.\nGamma used: penetrates body to reach detector outside; shorter range alpha/beta wouldn't exit.\n\nSTERILISATION OF MEDICAL EQUIPMENT:\nGamma radiation from cobalt-60 kills bacteria and viruses on medical instruments.\nEquipment sealed in packaging — gamma penetrates to sterilise contents.\nNo heat needed — suitable for heat-sensitive equipment.\nAlso used to sterilise food (extending shelf life).",
    "heading": "Medical Uses"
  },
  {
    "content": "PAPER/SHEET THICKNESS MONITORING:\nBeta source placed above a moving sheet (paper, metal foil).\nBeta detector below measures transmitted intensity.\nMore beta absorbed → thicker sheet.\nSignal fed back to rollers → adjusts pressure to maintain correct thickness.\nBeta chosen: absorbed by the sheet but not by surrounding air; alpha too weak to penetrate any sheet; gamma too penetrating (wouldn't distinguish thicknesses).\n\nSMOKE DETECTORS:\nAlpha source (americium-241) ionises air between two electrodes.\nIon current flows — circuit active.\nSmoke particles absorb alpha radiation → less ionisation → current drops → alarm triggers.\nAlpha chosen: short range — doesn't escape detector casing, safe for household use; ionises air well.\n\nPIPELINE FAULT DETECTION:\nGamma source moved through underground pipe.\nGamma detector on surface detects escaping radiation.\nCrack or fault → more gamma escapes → indicates location of leak.\n\nCARBON DATING:\nRadioactive ¹⁴C decays with 5730-year half-life.\nCompare ¹⁴C/¹²C ratio in sample vs living material.\nCalculate age from ratio.",
    "heading": "Industrial Uses"
  },
  {
    "content": "SELECTION CRITERIA — match the type to the application:\n\nALPHA:\nHigh ionisation — useful for ionising air (smoke detectors).\nShort range — safe for household devices.\nNOT useful where penetration is needed.\n\nBETA:\nModerate penetration — can pass through a few mm of material.\nAbsorbed by aluminium — useful for thickness monitoring of thin sheets.\nNOT useful for deep tissue medical imaging.\n\nGAMMA:\nHigh penetration — can pass through the body and through thick materials.\nLeast ionising per path — causes less immediate local damage.\nUseful for: medical imaging, radiotherapy, sterilisation, pipeline testing.\nMust be shielded with lead/concrete.\n\nHALF-LIFE SELECTION:\nMedical tracers: SHORT half-life (hours–days) — patient exposure minimal.\nIndustrial sources: LONGER half-life (years) — source doesn't need replacing frequently.\nCarbon dating: half-life comparable to age of sample (thousands of years).",
    "heading": "Choosing the Right Type"
  }
]
```

## higher

Evaluate the choice of radiation type for specific applications using criteria: penetration, ionisation, half-life and safety. Calculate the activity remaining after a given time using half-life. Explain why specific half-lives are chosen for different applications.

## common_mistake

Beta is used for THICKNESS monitoring — not alpha or gamma. Alpha is used for SMOKE detectors — not beta or gamma. Gamma is used for DEEP medical imaging and radiotherapy — because it penetrates to internal organs. Medical tracers need SHORT half-lives to minimise patient dose.

## key_note

Alpha: smoke detectors (ionises air, short range). Beta: thickness gauges (absorbed proportional to thickness). Gamma: radiotherapy, medical tracers, sterilisation, pipeline testing (most penetrating). Medical tracers: gamma + short half-life (Tc-99m, 6 hours). Selection based on penetration, ionisation and half-life.

## matching
```json
{
  "instruction": "Match each use to the radiation type and reason it is chosen.",
  "pairs": [
    [
      "Smoke detector",
      "Alpha — ionises air between electrodes; smoke absorbs alpha → current drops → alarm"
    ],
    [
      "Paper thickness gauge",
      "Beta — absorbed proportional to thickness; gamma too penetrating; alpha too weak"
    ],
    [
      "Medical tracer (organ imaging)",
      "Gamma — penetrates body to reach detector outside; short half-life minimises dose"
    ],
    [
      "Radiotherapy",
      "Gamma — penetrates to deep tumour; multiple beams cross at tumour to concentrate dose"
    ]
  ],
  "title": "Radiation Uses"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Alpha ionises air very effectively between the electrodes AND has short range — it stays safely inside the casing without penetrating the housing",
        true
      ],
      [
        "Alpha is less dangerous than gamma — so it is safer for household use in general",
        false
      ],
      [
        "Gamma cannot ionise air — only alpha radiation can ionise gases",
        false
      ],
      [
        "Alpha has a longer half-life than gamma emitters — so the detector lasts longer",
        false
      ]
    ],
    "q": "Why is americium-241 (an alpha emitter) used in smoke detectors rather than a gamma emitter?",
    "wrong_explanations": {
      "1": "Safety is part of it — but the specific reasons are HIGH IONISATION (needed to create the ion current) and SHORT RANGE (safe containment). Simply being 'less dangerous' isn't precise enough.",
      "2": "Gamma CAN ionise air — all types of ionising radiation can ionise air, but alpha is much MORE efficient per unit path.",
      "3": "Half-life of Am-241 is ~432 years — it does last well in detectors, but the primary reason for alpha selection is ionisation efficiency and range, not half-life."
    }
  },
  {
    "opts": [
      [
        "Gamma penetrates the body to reach an external detector, and short half-life means patient dose is minimal — activity falls quickly after the procedure",
        true
      ],
      [
        "Gamma is most ionising — causes maximum contrast in the image, and short half-life means it works faster",
        false
      ],
      [
        "Gamma is the safest radiation type, so combining with any half-life gives safe imaging",
        false
      ],
      [
        "Short half-life means the tracer stays in the body longer before decaying",
        false
      ]
    ],
    "q": "A medical tracer needs to emit gamma radiation and have a short half-life. Why?",
    "wrong_explanations": {
      "1": "Gamma is LEAST ionising per path — less immediate local tissue damage. High ionisation would cause cell damage, not contrast.",
      "2": "Gamma penetrates body safely — but 'safest' oversimplifies. The combination of penetration (for imaging) AND short half-life (for low dose) is the key.",
      "3": "Short half-life means the tracer DECAYS QUICKLY — activity falls rapidly, reducing the patient's radiation dose."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
