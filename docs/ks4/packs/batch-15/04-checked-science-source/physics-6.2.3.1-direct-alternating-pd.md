# Direct and Alternating Potential Difference  (Physics, AQA 6.2.3.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| dc vs ac: direction (theory 1–2; q1; key_note) | base | 8464 6.2.3.1; 8463 4.2.3.1 |
| UK mains ac, 50 Hz, about 230 V (theory 2; q2; common_mistake) | base | 8464 6.2.3.1; 8463 4.2.3.1 |
| f = 1 ÷ T from a trace (theory 3; equations; FIFA) | base (supporting) | 8464 6.6.1.2; 8463 4.6.1.2 |
| rms, peak ~325 V, volts per division (theory 2–3; common_mistake; q2 wx3) | beyond spec — not on 8463/8464 (DAP-F1) | — |
| why mains is ac (theory 2) | base context; imprecise (DAP-F2) | 8464 6.2.4.3 |

True page routes: CF CH TF TH (all base). Matches the site.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Distinguish dc and ac, state UK mains values and read oscilloscope traces.

## theory
```json
[
  {
    "content": "DIRECT CURRENT (DC) — flows in ONE direction only; pd is constant.\n\nSources: batteries, solar cells, dc power supplies.\n\nOn an oscilloscope:\nDC appears as a HORIZONTAL LINE — constant pd, no oscillation.\nHigher line = higher pd. Line at zero = no pd.",
    "heading": "Direct Current (DC)"
  },
  {
    "content": "ALTERNATING CURRENT (AC) — current and pd REVERSE DIRECTION repeatedly.\n\nSources: mains electricity, generators.\n\nOn an oscilloscope:\nAC appears as a WAVE (sinusoidal) — rises above and below zero.\nFREQUENCY = complete cycles per second (Hz).\nPEAK VOLTAGE = maximum pd from zero.\n\nUK MAINS:\nFrequency: 50 Hz\nVoltage: ~230 V (rms value)\n\nMains is AC because generators naturally produce AC, and AC is easily transformed to different voltages for efficient transmission.",
    "heading": "Alternating Current (AC)"
  },
  {
    "content": "Y-axis: voltage. X-axis: time.\n\nFREQUENCY:\nMeasure the time for ONE complete cycle (period T).\nf = 1 ÷ T\n\nPEAK VOLTAGE:\nMeasure from zero line to peak.\nPeak pd = divisions × volts per division setting.\n\nEXAMPLE:\nPeriod T = 0.02 s:\nf = 1 ÷ 0.02 = 50 Hz — UK mains ✓\n\nDC trace: flat horizontal line.\nAC trace: regular sinusoidal wave.",
    "heading": "Reading Oscilloscope Traces"
  }
]
```

## common_mistake

UK mains is 50 Hz — not 60 Hz (USA). The quoted 230 V is an rms value — the peak voltage is higher (~325 V). A DC trace is a flat line; an AC trace is a wave.

## key_note

DC: constant direction, flat oscilloscope line. AC: reversing, sinusoidal trace. UK mains: 50 Hz, ~230 V rms. f = 1/T. Mains AC because generators produce AC and it can be transformed easily.

## equations
```json
[
  "f = 1 ÷ T"
]
```

## fifas
```json
[
  {
    "label": "Frequency from Period",
    "question": "An oscilloscope trace shows one complete cycle takes 0.02 s. Calculate the frequency.",
    "steps": [
      [
        "F",
        "f = 1 ÷ T"
      ],
      [
        "I",
        "T = 0.02 s"
      ],
      [
        "F",
        "f = 1 ÷ 0.02"
      ],
      [
        "A",
        "f = 50 Hz — UK mains frequency ✓"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "f",
    "Frequency",
    "hertz",
    "Hz"
  ],
  [
    "T",
    "Period",
    "seconds",
    "s"
  ],
  [
    "V",
    "Potential difference",
    "volts",
    "V"
  ]
]
```

## matching
```json
{
  "instruction": "Match each description to DC or AC.",
  "pairs": [
    [
      "DC",
      "Flows in one direction only — flat horizontal oscilloscope trace"
    ],
    [
      "AC",
      "Reverses direction repeatedly — sinusoidal oscilloscope trace"
    ],
    [
      "DC",
      "Produced by batteries and solar cells"
    ],
    [
      "AC",
      "UK mains — 230 V, 50 Hz"
    ],
    [
      "AC",
      "Produced by generators in power stations"
    ]
  ],
  "title": "DC vs AC"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "A direct (dc) supply — the pd is constant and always in the same direction",
        true
      ],
      [
        "An alternating (ac) supply — a steady pd is the average value of an ac supply",
        false
      ],
      [
        "No supply at all — a pd that never changes cannot make a current flow",
        false
      ],
      [
        "A very high frequency ac supply — it changes direction too fast to notice",
        false
      ]
    ],
    "q": "A supply gives a potential difference that stays at the same value and never changes direction. What type of supply is it?",
    "wrong_explanations": {
      "1": "An alternating pd keeps reversing direction. A pd that stays the same and never reverses is direct.",
      "2": "A constant pd still drives a current round a complete circuit. A cell or battery does exactly this.",
      "3": "However fast an ac supply alternates, its pd still reverses direction. This pd never does, so the supply is direct."
    }
  },
  {
    "opts": [
      [
        "50 Hz and 230 V",
        true
      ],
      [
        "60 Hz and 230 V — 60 Hz is the UK standard",
        false
      ],
      [
        "50 Hz and 110 V — 110 V is the UK mains voltage",
        false
      ],
      [
        "50 Hz and 325 V — 325 V is the correct value",
        false
      ]
    ],
    "q": "What are the frequency and voltage of the UK mains supply?",
    "wrong_explanations": {
      "1": "60 Hz is used in the USA — UK is 50 Hz.",
      "2": "110 V is used in the USA — UK mains is ~230 V.",
      "3": "325 V is the PEAK voltage — 230 V is the quoted rms (effective) value."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** An oscilloscope trace shows one complete cycle takes 0.02 s. Calculate the frequency.

**Convert:** [NEW — examined ✓] Nothing to convert — T is already given in seconds (SI), and f = 1 ÷ T needs no other unit.

**F:** f = 1 ÷ T

**I:** T = 0.02 s

**F:** f = 1 ÷ 0.02

**A:** f = 50 Hz — UK mains frequency ✓
