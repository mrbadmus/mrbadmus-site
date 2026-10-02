# Properties of Waves  (Physics, AQA 6.6.1.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Amplitude, wavelength, frequency, period; units (theory 1; common_mistake; key_note; variables) | base | 8464 6.6.1.2; 8463 4.6.1.2 |
| T = 1/f (theory 1; equations; q1) — On the sheet | base | 8464 6.6.1.2 |
| v = f λ, rearrangements, examples (theory 2; equations; FIFA; q2) — On the sheet | base | 8464 6.6.1.2 |
| EM speed 3×10⁸ m/s; sound ~340 m/s (theory 2; key_note) | base | 8464 6.6.2.1; context |
| Ripple tank method (theory 3; `rp`) — labelled "RP19", truly Combined RP20 / Physics RP8 — F1 | base (RP) | 8464 6.6.1.2; 8463 4.6.1.2 |
| Waves in a solid (RP's other half) — absent — F2 | base (RP) | 8464 RP20; 8463 RP8 |
| Speed of sound in air method (theory 3 Method 2; `rp`) — F3 | base | 8464 6.6.1.2 |
| Oscilloscope trace → T → f (theory 3) | base | 8464 6.6.1.2 (MS 1c, 3b, c) |
| Sound changing medium: f fixed, v and λ change — absent — F4 | **triple** | 8463 4.6.1.2 (physics only) |
| quiz q1, q2 | base — both usable | 8464 6.6.1.2 |

True page routes: CF CH TF TH (base + RP + a triple layer). Site currently ships: CF CH TF TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## Spec core missing from the frozen data (written from the spec, examiner)

- 8464 6.6.1.2 / 8463 4.6.1.2: "The wave speed is the speed at which the energy is transferred (or the wave moves) through the medium."
- RP (Combined RP20 = Physics RP8): "make observations to identify the suitability of apparatus to measure the frequency, wavelength and speed of waves in a ripple tank **and waves in a solid** and take appropriate measurements." The frozen data has no waves-in-a-solid method.
- 8463 4.6.1.2: "(Physics only) Students should be able to show how changes in velocity, frequency and wavelength, in transmission of sound waves from one medium to another, are inter-related." Triple only.

## summary

Define amplitude, wavelength, frequency, period and wave speed, and use v = fλ.

## theory
```json
[
  {
    "content": "KEY WAVE PROPERTIES:\n\nAMPLITUDE (A): maximum displacement of a particle from its equilibrium (undisturbed) position.\nMeasured in metres (m). Relates to energy — larger amplitude = more energy.\n\nWAVELENGTH (λ, lambda): distance from one point on a wave to the equivalent point on the next wave.\nFor example: crest to crest, or trough to trough, or compression to compression.\nMeasured in metres (m).\n\nFREQUENCY (f): number of complete waves passing a point per second.\nMeasured in HERTZ (Hz). 1 Hz = 1 complete wave per second.\n\nPERIOD (T): time for one complete wave to pass a point.\nMeasured in seconds (s).\nRelationship: T = 1 ÷ f  (or f = 1 ÷ T)",
    "heading": "Wave Properties"
  },
  {
    "content": "WAVE SPEED EQUATION:\nv = f × λ\n\nv = wave speed (m/s)\nf = frequency (Hz)\nλ = wavelength (m)\n\nRearranging:\nf = v ÷ λ\nλ = v ÷ f\n\nEXAMPLE 1:\nSound wave: frequency 440 Hz, speed 340 m/s:\nλ = 340 ÷ 440 = 0.77 m\n\nEXAMPLE 2:\nEM wave: wavelength 0.1 m, speed 3 × 10⁸ m/s:\nf = 3 × 10⁸ ÷ 0.1 = 3 × 10⁹ Hz = 3 GHz (microwave range)\n\nAll EM waves travel at the SAME speed in vacuum: c = 3 × 10⁸ m/s.\nSound in air: ~340 m/s at room temperature.",
    "heading": "The Wave Equation"
  },
  {
    "content": "REQUIRED PRACTICAL (RP19) — Measure wave speed:\n\nMETHOD 1 — Water waves (ripple tank):\nUse a stroboscope to 'freeze' waves.\nMeasure wavelength from the still image.\nCount frequency from the vibrating bar setting.\nCalculate: v = fλ.\n\nMETHOD 2 — Sound waves:\nConnect a microphone to an oscilloscope.\nDisplay the waveform — measure period T from the trace.\nf = 1/T.\nUsing two microphones and measuring time delay to find speed.\n\nEXAM SKILL — reading oscilloscope traces:\nTime per division (x-axis) → period T → frequency f = 1/T.\nVolts per division (y-axis) → amplitude.",
    "heading": "Measuring Wave Speed — Required Practical"
  }
]
```

## common_mistake

Amplitude is the distance from the equilibrium (centre) to the crest — NOT from crest to trough (that's double the amplitude). Frequency and period are reciprocals: f = 1/T. Don't confuse wavelength (one full cycle length) with amplitude (height from centre).

## key_note

Amplitude: equilibrium to crest (m). Wavelength (λ): crest to crest (m). Frequency (f): waves per second (Hz). Period (T): seconds per wave. T = 1/f. v = fλ. EM waves in vacuum: 3×10⁸ m/s. Sound in air: ~340 m/s. RP19: measure wave speed in ripple tank.

## equations
```json
[
  "v = f × λ",
  "T = 1 ÷ f"
]
```

## fifas
```json
[
  {
    "label": "Wave Equation",
    "question": "A sound wave has frequency 500 Hz and travels at 340 m/s. Calculate its wavelength.",
    "steps": [
      [
        "F",
        "v = f × λ, so λ = v ÷ f"
      ],
      [
        "I",
        "v = 340 m/s, f = 500 Hz"
      ],
      [
        "F",
        "λ = 340 ÷ 500"
      ],
      [
        "A",
        "λ = 0.68 m"
      ]
    ]
  }
]
```

## rp

RP19 (Physics) — Measure the speed of waves in a ripple tank using v = fλ. Measure frequency and wavelength of waves. Also: measure speed of sound using microphones and oscilloscope.

## variables
```json
[
  [
    "v",
    "Wave speed",
    "m/s",
    "m/s"
  ],
  [
    "f",
    "Frequency",
    "hertz",
    "Hz"
  ],
  [
    "λ",
    "Wavelength",
    "metres",
    "m"
  ],
  [
    "T",
    "Period",
    "seconds",
    "s"
  ],
  [
    "A",
    "Amplitude",
    "metres",
    "m"
  ]
]
```

## matching
```json
{
  "instruction": "Match each wave property to its definition and unit.",
  "pairs": [
    [
      "Amplitude",
      "Maximum displacement from equilibrium — measured in metres"
    ],
    [
      "Wavelength (λ)",
      "Distance from one crest to the next — metres"
    ],
    [
      "Frequency (f)",
      "Number of complete waves per second — hertz (Hz)"
    ],
    [
      "Period (T)",
      "Time for one complete wave — seconds; T = 1/f"
    ],
    [
      "Wave speed (v)",
      "v = f × λ — distance travelled per second in m/s"
    ]
  ],
  "title": "Wave Property Definitions"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "0.005 s — T = 1 ÷ f = 1 ÷ 200 = 0.005 s",
        true
      ],
      [
        "200 s — T = f = 200 s",
        false
      ],
      [
        "20 s — T = f ÷ 10",
        false
      ],
      [
        "0.1 s — T = 1/10 of the frequency",
        false
      ]
    ],
    "q": "A wave has frequency 200 Hz. What is its period?",
    "wrong_explanations": {
      "1": "T is not equal to f — they are reciprocals: T = 1/f = 1/200 = 0.005 s.",
      "2": "T = 1/f not f/10.",
      "3": "T = 1/f only — T = 1/200 = 0.005 s."
    }
  },
  {
    "opts": [
      [
        "1 × 10⁸ Hz — f = v ÷ λ = 3×10⁸ ÷ 3 = 1×10⁸ Hz",
        true
      ],
      [
        "9 × 10⁸ Hz — f = v × λ = 3×10⁸ × 3",
        false
      ],
      [
        "1 × 10⁻⁸ Hz — f = λ ÷ v = 3 ÷ 3×10⁸",
        false
      ],
      [
        "3 × 10⁸ Hz — frequency equals wave speed for EM waves",
        false
      ]
    ],
    "q": "A radio wave has wavelength 3 m. What is its frequency? (speed of EM waves = 3 × 10⁸ m/s)",
    "wrong_explanations": {
      "1": "f = v × λ multiplies rather than divides — must use f = v ÷ λ.",
      "2": "f = λ ÷ v inverts the rearrangement. f = v ÷ λ = 3×10⁸ ÷ 3 = 1×10⁸ Hz.",
      "3": "Wave speed and frequency are not the same — they are related by v = fλ."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A sound wave has frequency 500 Hz and travels at 340 m/s. Calculate its wavelength.

**Convert:** [NEW — examined ✓] Nothing to convert — speed is already in m/s and frequency already in Hz, so λ = v ÷ f gives an answer directly in metres with no unit change.

**F:** v = f × λ, so λ = v ÷ f

**I:** v = 340 m/s, f = 500 Hz

**F:** λ = 340 ÷ 500

**A:** λ = 0.68 m
