# Wave Front Diagrams and Refraction  (Physics, AQA 6.6.2 (HT only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Wave fronts: definition, ⊥ travel, plane and circular (theory 1; common_mistake; key_note) — F3 | higher | 8464 6.6.2.2 (HT only); 8463 4.6.2.2 (HT only) |
| Refraction by wave fronts: one end slows first, front turns (theory 1–2; key_note; `higher`) | higher | 8464 6.6.2.2 (HT only) |
| f constant, v and λ change; v = f λ (theory 2; equations; common_mistake; q1) — On the sheet | higher | 8464 6.6.2.2 (HT only); 6.6.1.2 |
| Seismic P-wave paths curve (theory 2) — F2 | triple-higher (TH-only aside) | 8463 4.6.1.5 (physics only)(HT only) |
| Radio waves from oscillating circuits; absorbed → AC (theory 3; key_note; `higher`; q2) — F4 | higher (home: properties-em-waves-2) | 8464 6.6.2.3 (HT only) |
| Ionosphere refraction (theory 3) — F5 | off-spec context | — |
| quiz q1, q2 | higher — both usable on CH TH | 8464 6.6.2.2; 6.6.2.3 (HT only) |

True page routes: CH TH (HT only, not physics only). Site currently ships: TH; moving under the route-flag PR.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Use wave front diagrams to explain refraction and describe radio wave behaviour.

## theory
```json
[
  {
    "content": "A WAVE FRONT is an imaginary line connecting all points of a wave that are at the same phase (e.g. all the crests).\n\nWave fronts are PERPENDICULAR to the direction of wave travel.\n\nFor PLANE WAVES (parallel wave fronts):\nAll points move in the same direction.\nShown as parallel lines with arrows indicating direction of travel.\n\nFor CIRCULAR WAVES (from a point source):\nWave fronts are concentric circles spreading outward.\nFrequency and wavelength shown by spacing between lines.\n\nCLOSER WAVE FRONTS: shorter wavelength or wave fronts bunching up as wave slows.\nFURTHER APART: longer wavelength or wave fronts spreading as wave speeds up.\n\nREFRACTION using wave fronts:\nWhen a wave crosses into a new medium, speed changes.\nPart of the wave front enters the new medium first → that part slows (or speeds up) first.\nThe wave front pivots → wave changes direction.",
    "heading": "Wave Front Diagrams"
  },
  {
    "content": "WHY REFRACTION OCCURS:\nAt a boundary, the wave speed changes.\nIf wave slows: wave fronts bunch together (shorter wavelength), wave turns towards the normal.\nIf wave speeds up: wave fronts spread apart (longer wavelength), wave turns away from the normal.\n\nFREQUENCY DOESN'T CHANGE during refraction — only speed and wavelength change.\nv = fλ → if v decreases and f stays constant → λ decreases.\n\nEXAMPLE — Light entering glass:\nLight travels slower in glass than air.\nWave front entering glass slows down → bends towards the normal.\nWavelength shortens inside glass.\nFrequency unchanged — the eye perceives the same colour.\n\nSEISMIC WAVE REFRACTION:\nP-waves travel faster in denser rock.\nAs P-waves descend through Earth, density increases → speed increases → waves curve upward.\nThis is why P-waves travel in curved paths through the Earth.",
    "heading": "Explaining Refraction with Wave Fronts"
  },
  {
    "content": "RADIO WAVES can be PRODUCED by oscillations in electrical circuits.\nAn oscillating current in an aerial (antenna) produces oscillating electromagnetic field → radio wave emitted.\nFrequency of radio wave = frequency of electrical oscillation.\n\nRADIO WAVE ABSORPTION AND CURRENT INDUCTION:\nWhen a radio wave is ABSORBED by a conductor (receiving aerial):\nThe oscillating electromagnetic field drives electrons in the conductor.\nAn ALTERNATING CURRENT (AC) is induced with the SAME FREQUENCY as the radio wave.\nThis is the basis of all radio and wireless communication receivers.\n\nREFRACTION OF RADIO WAVES:\nRadio waves refract in the ionosphere (upper atmosphere).\nThis allows long-distance communication — waves bent back to Earth's surface.\nDifferent frequencies refract differently — some pass through, some are reflected.",
    "heading": "Radio Waves and Electrical Circuits"
  }
]
```

## higher

HT only — draw and interpret wave front diagrams to explain refraction. Explain refraction in terms of change of speed at a boundary. Describe how radio waves are produced by oscillating electrical circuits and how they induce alternating currents when absorbed.

## common_mistake

During refraction, FREQUENCY stays constant — only SPEED and WAVELENGTH change. v = fλ, so if v decreases and f is constant, λ must decrease proportionally. Wave fronts are perpendicular to the direction of travel — closer wave fronts = shorter wavelength, not higher frequency.

## key_note

Wave fronts ⊥ direction of travel. Refraction: wave crosses boundary → speed changes → wave fronts pivot → direction changes. Frequency constant, speed and wavelength change. Into slower medium: bends towards normal, wavelength decreases. Radio waves: produced by oscillating current; absorbed → induces AC at same frequency.

## equations
```json
[
  "v = f × λ  (speed = frequency × wavelength — frequency unchanged in refraction)"
]
```

## matching
```json
{
  "instruction": "Match each statement to the correct refraction or wave front concept.",
  "pairs": [
    [
      "Wave slows at boundary",
      "Wave fronts bunch together — wavelength decreases, wave bends towards normal"
    ],
    [
      "Frequency during refraction",
      "Unchanged — only speed and wavelength change"
    ],
    [
      "Wave front orientation",
      "Always perpendicular to the direction of wave travel"
    ],
    [
      "Radio wave reception",
      "Oscillating radio wave induces AC at same frequency in the receiving aerial"
    ]
  ],
  "title": "Wave Fronts and Refraction"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Wavelength decreases, frequency stays the same — v = fλ, so if v decreases and f is constant, λ must decrease",
        true
      ],
      [
        "Frequency increases, wavelength stays the same — more wave fronts arrive per second in denser material",
        false
      ],
      [
        "Both wavelength and frequency decrease — the wave loses energy entering the denser medium",
        false
      ],
      [
        "Both remain the same — refraction only changes direction, not wave properties",
        false
      ]
    ],
    "q": "A light wave enters glass from air and slows down. What happens to its wavelength and frequency?",
    "wrong_explanations": {
      "1": "The number of wave fronts arriving per second at the boundary equals the number leaving — frequency is set by the source and cannot change.",
      "2": "The wave does lose some energy (absorbed) but the frequency of transmitted wave remains unchanged.",
      "3": "Direction changes AND wavelength changes during refraction — only frequency is preserved."
    }
  },
  {
    "opts": [
      [
        "By oscillating electrical currents in an aerial (antenna) — the frequency of oscillation equals the frequency of the radio wave emitted",
        true
      ],
      [
        "By heating a metal aerial — hot metal emits radio waves as thermal radiation",
        false
      ],
      [
        "By nuclear decay of radioactive materials — gamma rays are converted to radio waves",
        false
      ],
      [
        "By spinning magnets in generators — rotating magnetic fields directly produce radio waves",
        false
      ]
    ],
    "q": "How are radio waves produced for transmission?",
    "wrong_explanations": {
      "1": "Hot metals emit infrared and visible light — not radio waves. Radio waves require oscillating ELECTRICAL currents.",
      "2": "Nuclear decay produces gamma, alpha and beta radiation — not radio waves.",
      "3": "Spinning magnets produce alternating electrical currents — those currents in an aerial produce radio waves, but the magnet alone doesn't."
    }
  }
]
```
