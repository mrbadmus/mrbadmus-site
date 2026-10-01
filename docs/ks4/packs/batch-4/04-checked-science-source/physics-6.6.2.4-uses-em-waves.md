# Uses and Applications of Electromagnetic Waves  (Physics, AQA 6.6.2.4)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Wave ↔ use (spec's six pairs; theory lists; key_note) | base | 8464 6.6.2.4; 8463 4.6.2.4 |
| Extra uses beyond the spec list (MRI, radar, CT, tracers, vitamin D…) | base (context, not examinable) | — |
| Why each wave suits its use (theory glosses; common_mistake; `higher`) | higher | 8464 6.6.2.4 (HT only) |
| Ionising types: hazard managed | base | 8464 6.6.2.3 |
| `higher`: optical fibres by total internal reflection | off-spec — do not use (`_flags/uses-em-waves.md` UEM-F2) | — |
| `higher`: ultrasound comparison | triple-higher | 8463 4.6.1.5 (physics only) (HT only) |
| Quiz q1, q2 ("why" items) | higher — usable CH TH only | 8464 6.6.2.4 (HT only) |

True page routes: CF CH TF TH (higher layer CH TH).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the uses of each type of electromagnetic wave and explain why each type is suitable.

## theory
```json
[
  {
    "content": "RADIO WAVES:\nBROADCASTING: AM and FM radio, TV broadcasts — travel long distances, reflect off ionosphere.\nCOMMUNICATION: aircraft, ships, emergency services.\nASTRONOMY: radio telescopes detect radio waves from distant stars and galaxies.\nMRI SCANNERS: radio waves + magnetic field → detailed images of soft tissue (no ionising radiation).\n\nMICROWAVES:\nMOBILE PHONES AND WIFI: short-range communication.\nSATELLITE COMMUNICATION: microwaves pass through the atmosphere and ionosphere (radio waves reflect off ionosphere — limited for satellite use).\nMICROWAVE OVENS: microwave frequency matches water molecules' resonance → absorbed → food heats from inside.\nRADAR: detect aircraft, ships, weather systems — measure distance by timing reflection.",
    "heading": "Uses of Radio Waves and Microwaves"
  },
  {
    "content": "INFRARED (IR):\nHEATING: electric heaters, grills — absorbed by surfaces, converted to heat.\nREMOTE CONTROLS: TV, DVD players — IR pulses carry coded signals.\nFIBRE OPTICS: IR carried along optical fibres for high-speed internet.\nNIGHT VISION CAMERAS: detect IR emitted by warm bodies — useful in darkness.\nTHERMAL IMAGING: medical, security, wildlife observation.\n\nVISIBLE LIGHT:\nPHOTOGRAPHY: cameras capture visible light.\nFIBRE OPTICS: carries data as light pulses — basis of broadband internet.\nPHOTOSYNTHESIS: plants absorb red and blue light.\nLASERS: surgery, barcode scanners, DVD reading.\n\nULTRAVIOLET (UV):\nSTERILISATION: UV kills bacteria and viruses — used in hospitals and water treatment.\nFLUORESCENCE: some materials emit visible light when absorbing UV — security markings, fluorescent lamps.\nBLACK LIGHTS: detect forged bank notes (UV-reactive ink).\nVITAMIN D PRODUCTION: skin produces vitamin D when exposed to UV.",
    "heading": "Uses of Infrared, Visible and Ultraviolet"
  },
  {
    "content": "X-RAYS:\nMEDICAL IMAGING: pass through soft tissue, absorbed by bone → shadow on film/detector.\nCT SCANS: multiple X-ray beams → 3D image of internal structures.\nAIRPORT SECURITY: luggage scanning — detect metal, explosives.\nMATERIAL TESTING: checking for cracks in metal castings and welds.\n\nGAMMA RAYS:\nCANCER TREATMENT (radiotherapy): focused beams kill tumour cells.\nST ERILISATION of medical equipment: kills all microorganisms without heat.\nFOOD IRRADIATION: kills bacteria in food → longer shelf life.\nMEDICAL TRACERS: gamma-emitting radioisotopes injected → gamma camera detects distribution in body → reveals organ function.\nTHICKNESS MONITORING: detect gamma penetration through materials in manufacturing.\n\nMATCHING APPLICATION TO WAVE TYPE:\nThe wave chosen matches its properties to the application:\nMust penetrate enough → not be absorbed too quickly.\nMust interact appropriately with the target material.\nHazard must be managed — ionising types minimised.",
    "heading": "Uses of X-rays and Gamma Rays"
  }
]
```

## higher

Explain why different wavelengths of EM radiation are used for different applications in terms of their properties — penetration, absorption, reflection and refraction behaviour. Evaluate the hazards and benefits of each type in context (e.g. X-rays vs MRI vs ultrasound for medical imaging). Explain how optical fibres work using total internal reflection.

## common_mistake

MRI scanners use RADIO WAVES (not X-rays) — they are safe for soft tissue imaging with no ionising radiation. X-rays are used for imaging BONE and dense structures. Also: microwaves for SATELLITE communication (pass through ionosphere); radio waves for BROADCAST (reflect off ionosphere).

## key_note

Radio: broadcast, MRI. Microwave: satellites, phones, radar, cooking. IR: heating, remote controls, night vision, fibre optics. Visible: photography, fibre optics, photosynthesis. UV: sterilisation, fluorescence, vitamin D. X-ray: medical imaging, airport security, CT. Gamma: radiotherapy, sterilisation, tracers.

## matching
```json
{
  "instruction": "Match each application to the EM wave type used.",
  "pairs": [
    [
      "Radio waves",
      "MRI scanner — safe for soft tissue, no ionising radiation"
    ],
    [
      "Microwaves",
      "Satellite communication — passes through ionosphere to reach satellites"
    ],
    [
      "Infrared",
      "TV remote control — pulses of IR carry the signal to the TV"
    ],
    [
      "X-rays",
      "Medical imaging of bones — absorbed by dense bone, transmitted by soft tissue"
    ],
    [
      "Gamma rays",
      "Radiotherapy — focused beams kill cancer cells"
    ]
  ],
  "title": "EM Wave Applications"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Microwaves pass through the ionosphere — radio waves reflect off it, preventing them from reaching satellites in orbit",
        true
      ],
      [
        "Microwaves are more powerful — they reach greater distances than radio waves",
        false
      ],
      [
        "Radio waves are dangerous at high altitude — microwaves are safer for satellite use",
        false
      ],
      [
        "Satellites can only detect microwaves — their receivers are not compatible with radio waves",
        false
      ]
    ],
    "q": "Why are microwaves used for satellite communications rather than radio waves?",
    "wrong_explanations": {
      "1": "Power determines signal strength at a given distance — but all EM waves travel at the same speed. The key distinction is IONOSPHERE INTERACTION.",
      "2": "Safety is not the relevant factor — the ionosphere physically reflects (most) radio waves back to Earth.",
      "3": "This is backwards — it's the PHYSICS of ionosphere reflection, not receiver incompatibility, that determines which EM type is used."
    }
  },
  {
    "opts": [
      [
        "UV has enough energy to damage DNA in microorganisms — killing or inactivating bacteria and viruses",
        true
      ],
      [
        "UV heats the equipment to high temperatures, killing microorganisms by heat",
        false
      ],
      [
        "UV is absorbed by metal — heating the equipment surface to kill bacteria",
        false
      ],
      [
        "UV converts oxygen to ozone, which then kills bacteria chemically",
        false
      ]
    ],
    "q": "UV light is used to sterilise medical equipment. Why is UV effective for this?",
    "wrong_explanations": {
      "1": "UV can cause some warming but it's not the primary mechanism — UV sterilisation works through DNA damage (photochemical action), not significant heating.",
      "2": "UV sterilisation is used for transparent surfaces, water, and air — metal surfaces are typically sterilised by heat or chemicals.",
      "3": "UV can produce some ozone, but the primary sterilisation mechanism is direct DNA damage from UV photons — not ozone."
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
