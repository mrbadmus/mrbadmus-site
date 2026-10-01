# Waves for Detection and Exploration  (Physics, AQA 6.6.1.5 (HT only, physics only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how waves are used for detection and exploration including seismic waves and echo sounding.

## theory
```json
[
  {
    "content": "SEISMIC WAVES are produced by earthquakes (or explosions) and travel through the Earth.\n\nTWO MAIN TYPES:\nP-WAVES (Primary/Pressure waves):\nLongitudinal — compressions and rarefactions.\nTravel through solids AND liquids.\nFaster — arrive first at seismograph.\nSpread out in all directions from the earthquake focus.\n\nS-WAVES (Secondary/Shear waves):\nTransverse — particles vibrate perpendicular to direction of travel.\nTravel through SOLIDS ONLY — cannot travel through liquids.\nSlower — arrive after P-waves.\n\nSEISMIC EVIDENCE FOR EARTH'S STRUCTURE:\nS-waves do not pass through the outer core → outer core must be LIQUID.\nP-waves are refracted (change speed) at the core boundary → core is DENSER than mantle.\nSeismographs detect arrival times of P and S waves → map Earth's interior.\n\nSHADOW ZONES:\nRegions on Earth's surface that receive neither P nor S waves after a distant earthquake.\nS-wave shadow zone: region directly opposite the earthquake (S-waves blocked by liquid core).\nP-wave shadow zone: P-waves refracted by core → gaps in coverage.",
    "heading": "Seismic Waves"
  },
  {
    "content": "ECHO SOUNDING uses reflected sound (or ultrasound) pulses to measure depth and map the seabed.\n\nPRINCIPLE:\nEmit pulse → detect echo → measure time → calculate distance:\nd = v × t / 2\n\nAPPLICATIONS:\nOCEAN FLOOR MAPPING: ships emit ultrasound → build up contour map of seabed.\nFISH DETECTION: fishing vessels detect shoals of fish by their sonar reflections.\nSUBMARINE DETECTION: military sonar detects submarines.\nGLACIER THICKNESS: radar waves (EM) used for ice penetration.\n\nSEISMIC SURVEYING FOR OIL:\nExplosions on Earth's surface → seismic waves travel down → reflect off rock layers.\nReflected waves detected at surface → timing reveals depth and structure of rock layers.\nGeologists use this to locate oil and gas reservoirs.",
    "heading": "Echo Sounding and SONAR"
  },
  {
    "content": "Different substances may ABSORB, TRANSMIT, REFRACT or REFLECT waves — in ways that vary with wavelength.\n\nREFRACTION:\nWaves change speed when passing between media → change direction.\nSeismic P-waves refract as they pass through Earth's layers → curved paths.\nLight refracts when passing through a lens or prism.\nSound refracts when passing between air layers at different temperatures.\n\nREFLECTION:\nWaves reflect off boundaries between media.\nEchoes: sound reflected from walls.\nSonar: sound reflected from seabed.\nRadar: radio waves reflected from aircraft.\n\nABSORPTION:\nSome wavelengths absorbed by specific materials.\nInfrared absorbed by greenhouse gases.\nUltraviolet absorbed by ozone layer.\nX-rays absorbed by bone more than soft tissue.\n\nTRANSMISSION:\nWaves that pass through a material.\nVisible light transmitted through glass.\nP-waves transmitted through liquid outer core.",
    "heading": "Refraction, Reflection and Absorption of Waves"
  }
]
```

## higher

HT only — use seismic wave data to infer Earth's internal structure. Explain the difference between P and S waves and why S-waves don't pass through the outer core. Calculate depths from echo sounding data.

## common_mistake

S-waves cannot travel through LIQUIDS — this is the key evidence that Earth's outer core is liquid. P-waves can travel through both solids and liquids. Seismic waves travel in curved paths through the Earth because their speed changes gradually with depth (refraction).

## key_note

P-waves: longitudinal, solid + liquid. S-waves: transverse, solid only. S-waves blocked by outer core → outer core = liquid. Echo sounding: d = vt/2. Seismic surveying: find oil layers. Refraction at boundaries: wave changes speed → changes direction.

## equations
```json
[
  "d = v × t / 2  (echo sounding depth calculation)"
]
```

## matching
```json
{
  "instruction": "Match each wave type to its properties and what it can travel through.",
  "pairs": [
    [
      "P-waves (Primary)",
      "Longitudinal — travel through solids AND liquids — arrive first at seismograph"
    ],
    [
      "S-waves (Secondary)",
      "Transverse — travel through solids ONLY — cannot pass through liquid outer core"
    ],
    [
      "S-wave shadow zone",
      "Region where S-waves don't arrive — evidence that outer core is liquid"
    ],
    [
      "Seismic surveying",
      "Explosions create seismic waves — reflections from rock layers reveal oil/gas deposits"
    ]
  ],
  "title": "Seismic Waves"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Earth has a liquid outer core — S-waves cannot travel through liquids, so they are blocked",
        true
      ],
      [
        "S-waves are too weak to travel to the opposite side of the Earth",
        false
      ],
      [
        "S-waves are absorbed by the mantle before reaching the outer core",
        false
      ],
      [
        "The opposite side of the Earth is too far — all wave types have a maximum range",
        false
      ]
    ],
    "q": "After a distant earthquake, S-waves are not detected on the opposite side of Earth. What does this indicate?",
    "wrong_explanations": {
      "1": "S-waves lose energy over distance, but can still be detected across Earth if the path is clear — the specific S-wave shadow zones indicate a LIQUID barrier.",
      "2": "S-waves do attenuate, but the pattern of shadow zones is specifically consistent with a liquid outer core, not general distance attenuation.",
      "3": "P-waves ARE detected on the opposite side — so 'too far' doesn't apply. The distinction between P and S wave shadows points to the liquid core explanation."
    }
  },
  {
    "opts": [
      [
        "300 m — d = 1500 × 0.4 / 2 = 600 / 2 = 300 m",
        true
      ],
      [
        "600 m — d = 1500 × 0.4 = 600 m (forgot to divide by 2)",
        false
      ],
      [
        "3750 m — d = 1500 / 0.4 = 3750 m (divided instead of multiplied)",
        false
      ],
      [
        "150 m — d = 1500 × 0.4 / 4 = 150 m",
        false
      ]
    ],
    "q": "A ship sends a sonar pulse and receives the echo 0.4 s later. Speed of sound in water = 1500 m/s. What is the water depth?",
    "wrong_explanations": {
      "1": "600 m doesn't account for the return journey — the pulse travels TO the seabed AND back, so divide total time by 2.",
      "2": "Speed divided by time gives a rate of change of speed, not distance — use d = v × t / 2.",
      "3": "There's no physical reason to divide by 4 — divide by 2 for the two-way journey."
    }
  }
]
```
