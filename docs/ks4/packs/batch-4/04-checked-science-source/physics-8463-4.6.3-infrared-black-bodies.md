# Infrared Emission, Absorption and Black Bodies  (Physics, AQA 6.6.5 (physics only))

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| All bodies emit and absorb IR; hotter → more per second; distribution shifts to shorter λ; black body curves | triple | 8463 4.6.3.1–4.6.3.2 |
| Perfect black body: absorbs all, best emitter | triple | 8463 4.6.3.1 |
| Dark matt / shiny surfaces; solar heaters; silvered flask (quiz q2) | base (RP outcome; taught on `properties-em-waves-1`) | 8464 6.6.2.2 RP21; 8463 4.6.2.2 RP10 |
| Emission vs absorption rate → cools / heats / constant | triple-higher | 8463 4.6.3.2 (HT only) |
| Earth's temperature; greenhouse; `higher` (TH) except its curves line | triple-higher | 8463 4.6.3.2 (HT only) |
| Thermal cameras | base | 8464 6.6.2.4 |
| Star colours; Hubble/JWST | off-spec context | — |
| Quiz q1 (glowing rod) | triple — **not usable as written** (`_flags/infrared-black-bodies.md` IRB-F2) | 8463 4.6.3.2 |

True page routes: TF TH (triple-higher layer TH only). Spec field "6.6.5 (physics only)" is wrong → 8463 4.6.3.1–4.6.3.2; flagged. The IR required practical (RP21/RP10, base) belongs on `properties-em-waves-1`, not this page; flagged.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe infrared emission and absorption by surfaces and explain perfect black body radiation.

## theory
```json
[
  {
    "content": "All objects emit and absorb THERMAL RADIATION (infrared radiation) continuously.\n\nEMISSION:\nAll objects above absolute zero emit infrared radiation.\nHotter objects emit MORE radiation and at SHORTER wavelengths (higher frequency, more energetic).\n\nABSORPTION:\nObjects absorb radiation from their surroundings.\nDark, matt surfaces are better ABSORBERS than light, shiny surfaces.\n\nDark matt surfaces are also better EMITTERS.\nShiny, light surfaces are better REFLECTORS and poorer emitters/absorbers.\n\nEMISSION vs ABSORPTION RATES:\nIf emission rate > absorption rate → object cools.\nIf absorption rate > emission rate → object heats up.\nIf rates are equal → temperature is constant (thermal equilibrium).",
    "heading": "Emission and Absorption of Radiation"
  },
  {
    "content": "A PERFECT BLACK BODY is a theoretical object that:\nABSORBS all radiation that falls on it (reflects none).\nEMITS the maximum amount of radiation for its temperature.\n\nPerfect black bodies emit the most radiation of any object at the same temperature.\nThe emission spectrum of a black body depends ONLY on temperature — not on the material.\n\nBLACK BODY RADIATION CURVES:\nAs temperature increases:\nPeak of emission shifts to SHORTER wavelengths (higher frequency).\nTotal energy emitted per second INCREASES dramatically.\n\nEXAMPLE:\nA cool object: emits mainly low-frequency infrared — invisible to the eye.\nHot iron (600°C): glows dull red — emitting visible red light.\nVery hot iron (1000°C): orange-white — peak moves into visible range.\nThe Sun (~5500°C surface): peak emission in visible light (yellow-green).\n\nA cavity with a small hole acts as an approximate black body.",
    "heading": "Perfect Black Bodies"
  },
  {
    "content": "STARS AS BLACK BODIES:\nStars approximately behave as black bodies.\nThe colour of a star indicates its surface temperature:\nRed stars (~3000 K) → cool → peak in infrared/red.\nYellow stars (like the Sun, ~5500 K) → medium → peak in visible.\nBlue-white stars (~30,000 K) → very hot → peak in UV/blue.\n\nEARTH'S TEMPERATURE:\nThe Earth absorbs solar radiation and re-emits as infrared (longer wavelength — Earth is cooler than Sun).\nGreenhouse gases absorb Earth's infrared emission → trap energy → warming effect.\n\nTHERMAL CAMERAS:\nDetect infrared emitted by warm objects — used in: night vision, firefighting, medical diagnosis (detecting hot spots), building inspection (heat loss).\n\nSPACE TELESCOPES:\nInfrared telescopes detect emission from cool objects like dust clouds in space.\nHubble detects visible light; James Webb Space Telescope detects infrared.\n\nSELECTIVE EMISSION AND ABSORPTION:\nSolar panels: dark, matt surfaces to maximise solar absorption.\nSolar water heaters: black tubes to maximise absorption.\nThermos flasks: silvered walls to minimise emission and absorption (reflect radiation back).",
    "heading": "Applications"
  }
]
```

## higher

Explain black body radiation curves — how peak wavelength depends on temperature. Describe how Earth's radiation balance determines its temperature. Explain the greenhouse effect mechanistically. Evaluate how changes in albedo or greenhouse gas concentration affect Earth's temperature.

## common_mistake

A PERFECT BLACK BODY is black because it absorbs ALL radiation — it also emits MAXIMUM radiation for its temperature. Being a 'perfect emitter' and 'perfect absorber' go together. Hotter objects emit at SHORTER wavelengths — this seems counterintuitive but is why glowing objects change colour from red to white-hot as they get hotter.

## key_note

All objects emit and absorb IR. Dark matt = best emitter and absorber. Shiny = best reflector. Black body: absorbs all radiation, emits maximum for its temperature. Hotter → more emission at shorter wavelength. Stars: colour indicates temperature (red=cool, blue=hot). Earth absorbs solar, re-emits IR — greenhouse effect.

## matching
```json
{
  "instruction": "Match each statement to the correct concept.",
  "pairs": [
    [
      "Dark matt surface",
      "Best emitter and absorber of infrared radiation"
    ],
    [
      "Perfect black body",
      "Absorbs all incident radiation — emits maximum radiation for its temperature"
    ],
    [
      "Hotter object",
      "Emits more radiation AND at shorter wavelengths — peak shifts towards visible/UV"
    ],
    [
      "Blue-white star",
      "Very hot (~30,000 K) — peak emission in UV/blue visible range"
    ]
  ],
  "title": "Infrared and Black Bodies"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "As temperature increases, the peak emission shifts to shorter wavelengths — from infrared through red to shorter visible wavelengths approaching white",
        true
      ],
      [
        "The metal changes chemical composition as it gets hotter, producing different coloured oxides",
        false
      ],
      [
        "Different wavelengths of light are produced by different electrons in the metal",
        false
      ],
      [
        "White light contains all colours — the metal must be emitting all wavelengths at low temperature but only red at high temperature",
        false
      ]
    ],
    "q": "A metal rod is heated in a furnace. First it glows red, then orange, then white. What does this tell us?",
    "wrong_explanations": {
      "1": "The colour change is due to temperature-dependent emission spectra — not chemical changes. A pure metal rod would show the same progression.",
      "2": "Different electrons in the metal contribute to emission, but the pattern follows the temperature-dependent black body spectrum — the overall colour shift is about temperature.",
      "3": "White hot means the peak has moved to visible wavelengths with broad-spectrum emission — cool objects emit IR (invisible) then progress through red, orange, yellow to white as temperature rises."
    }
  },
  {
    "opts": [
      [
        "Silvered walls are poor emitters and poor absorbers of infrared — they reflect radiation back, reducing thermal energy transfer by radiation",
        true
      ],
      [
        "Silver is a good conductor — it rapidly distributes heat evenly around the flask walls",
        false
      ],
      [
        "Silver reacts with oxygen in the air — the oxide layer acts as an insulator",
        false
      ],
      [
        "The bright colour of silver reflects external light, keeping the flask cool",
        false
      ]
    ],
    "q": "Why are the walls of a thermos flask silvered?",
    "wrong_explanations": {
      "1": "Silver is an excellent conductor — but the silvered wall is there to REDUCE radiation transfer, not to conduct heat.",
      "2": "Silver doesn't form a significant protective oxide layer at room temperature — the silvering works by reflection of radiation.",
      "3": "Visible light reflection is not the primary reason — it's the IR radiation reflection that reduces thermal energy transfer."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
