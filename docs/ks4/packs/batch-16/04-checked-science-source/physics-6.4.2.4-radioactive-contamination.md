# Radioactive Contamination  (Physics, AQA 6.4.2.4)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Contamination vs irradiation (theory 1; common_mistake; key_note) — X-ray examples imprecise, RADIOACTIVE-CONTAMINATION-F2 | base | 8464 6.4.2.4; 8463 4.4.2.4 |
| Hazard depends on radiation type: α inside, γ/β outside (theory 2; q1) | base | 8464 6.4.2.4; 6.4.2.1 |
| Precautions against contamination and irradiation (theory 3; q2) — inverse-square line off-spec, F3 | base | 8464 6.4.2.4 |
| Benefits vs risks (theory 3) | base | 8464 6.4.2.4 (WS 1.5) |
| Irradiated object does not become radioactive; peer review — missing, see below (F1) | base | 8464 6.4.2.4 |
| quiz q1, q2 | base — both usable | 8464 6.4.2.4 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches.

## Spec core missing from the frozen data (written from the spec, examiner)
8464 6.4.2.4 = 8463 4.4.2.4, verbatim:

> "Irradiation is the process of exposing an object to nuclear radiation. The irradiated object does not become radioactive."
> "Students should understand that it is important for the findings of studies into the effects of radiation on humans to be published and shared with other scientists so that the findings can be checked by peer review."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Distinguish contamination from irradiation and explain the hazards and precautions for each.

## theory
```json
[
  {
    "content": "These two terms are often confused but describe very different situations:\n\nRADIOACTIVE CONTAMINATION:\nUnwanted radioactive material is DEPOSITED ON or INSIDE a person or object.\nThe contaminating material continues to emit radiation over time.\nThe source stays with the person/object — ongoing exposure.\nExample: breathing in radon gas; swallowing radioactive dust; radioactive material on skin.\n\nIRRADIATION:\nThe person or object is EXPOSED TO RADIATION from a source that is NOT attached to them.\nWhen the person moves away from the source, exposure stops.\nExample: standing near a radioactive source; medical X-ray; radiotherapy.\n\nKEY DIFFERENCE:\nContamination = source stays with you.\nIrradiation = source is external, exposure ends when you move away.",
    "heading": "Contamination vs Irradiation"
  },
  {
    "content": "CONTAMINATION HAZARDS:\nAlpha sources are especially dangerous as INTERNAL CONTAMINANTS:\nAlpha particles are highly ionising but very short range.\nInside the body they deposit all their energy in nearby cells → severe local tissue damage.\nExternal alpha contamination (on skin) is less dangerous — alpha cannot penetrate skin.\nBeta and gamma internal contamination is also serious — penetrate to internal organs.\n\nIRRADIATION HAZARDS:\nDepends on radiation type, dose and duration.\nGamma is most dangerous external source — penetrates deeply into tissue.\nAlpha from external source: stopped by skin, relatively safe.\nBeta: penetrates skin, can damage underlying tissue.\n\nLONG-TERM EFFECTS:\nIonising radiation damages DNA → mutations → increased cancer risk.\nHigh acute doses → radiation sickness, cell death.\nEyes, bone marrow and gonads particularly sensitive.",
    "heading": "Hazards of Each Type"
  },
  {
    "content": "PRECAUTIONS TO PREVENT CONTAMINATION:\nNever touch radioactive materials directly — use TONGS or remote handling.\nWear PROTECTIVE CLOTHING (gloves, lab coat) to prevent skin contact.\nWORK IN WELL-VENTILATED areas to prevent inhaling radioactive dust or gases.\nNo eating, drinking or applying make-up in radioactive areas — prevents ingestion.\nSeal radioactive materials in appropriate containers.\n\nPRECAUTIONS TO REDUCE IRRADIATION:\nDISTANCE — intensity follows inverse square law; doubling distance reduces dose by ¾.\nSHIELDING — appropriate material (paper for alpha, aluminium for beta, lead/concrete for gamma).\nTIME — minimise exposure duration.\nDOSIMETERS — worn by radiation workers to monitor cumulative dose.\n\nPROFESSIONAL GUIDELINES:\nRadiation workers have annual dose limits.\nRegular monitoring of workplace radiation levels.\nStorage of radioactive sources in lead-lined containers when not in use.\n\nBENEFITS vs RISKS:\nMedical uses (X-rays, radiotherapy, tracers) involve balancing dose risk vs diagnostic/treatment benefit.\nRisk is managed, not eliminated.",
    "heading": "Precautions and Safe Use"
  }
]
```

## common_mistake

Contamination and irradiation are NOT the same. Contamination: radioactive material on/in you — source travels with you. Irradiation: external source — exposure stops when you move away. Alpha is most dangerous as INTERNAL contaminant (highly ionising, short range → all energy deposits locally).

## key_note

Contamination: source deposits on/in person — ongoing. Irradiation: external exposure — stops when away from source. Alpha most dangerous internally. Gamma most dangerous externally. Precautions: tongs, shielding, distance, dosimeters, sealed containers, ventilation. Benefits vs risks must be balanced.

## matching
```json
{
  "instruction": "Sort each scenario into contamination or irradiation.",
  "pairs": [
    [
      "Contamination",
      "Breathing in radioactive dust — source is now inside the body"
    ],
    [
      "Contamination",
      "Radioactive material spilled on skin — source remains in contact"
    ],
    [
      "Irradiation",
      "Standing near a gamma source — move away and exposure stops"
    ],
    [
      "Irradiation",
      "Medical X-ray — brief external exposure, no source deposited"
    ],
    [
      "Most dangerous internally",
      "Alpha radiation — highly ionising, short range, deposits all energy nearby"
    ]
  ],
  "title": "Contamination vs Irradiation"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Alpha is highly ionising — inside the body all the ionising energy is deposited in nearby lung tissue, causing severe local damage",
        true
      ],
      [
        "Alpha travels far inside the body reaching all organs — more widespread damage",
        false
      ],
      [
        "Alpha is easily exhaled — it escapes before causing harm",
        false
      ],
      [
        "Alpha inside the body becomes beta radiation — which is more penetrating",
        false
      ]
    ],
    "q": "A worker accidentally inhales radioactive dust containing an alpha emitter. Why is this particularly dangerous?",
    "wrong_explanations": {
      "1": "Alpha has very SHORT range — it doesn't travel far. That's exactly the problem: all its energy is deposited locally in lung tissue.",
      "2": "Radioactive dust lodges in lung tissue and continues to emit radiation there — it doesn't simply get exhaled.",
      "3": "Radiation types don't change — alpha always remains alpha. Different isotopes emit different types, but the type doesn't transform."
    }
  },
  {
    "opts": [
      [
        "Leaving the room while the X-ray is taken — distance and a lead-lined wall reduces irradiation when not needed",
        true
      ],
      [
        "Wearing a lead apron while staying in the room — lead blocks all radiation types",
        false
      ],
      [
        "Taking fewer breaths during the X-ray — radiation enters through breathing",
        false
      ],
      [
        "Washing hands after each X-ray — removes radiation from skin",
        false
      ]
    ],
    "q": "A radiographer takes X-rays of patients all day. Which precaution best reduces their radiation dose?",
    "wrong_explanations": {
      "1": "A lead apron is useful protection but does not cover all body parts — leaving the room is more effective for reducing total dose.",
      "2": "X-rays are electromagnetic radiation — they are not inhaled. The concern is external irradiation, not contamination.",
      "3": "X-rays from the machine don't contaminate surfaces — the radiographer's dose comes from irradiation (external source), not contamination."
    }
  }
]
```
