# Power  (Physics, AQA 6.1.1.4)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Define power as rate of energy transfer and calculate power from energy and time.

## theory
```json
[
  {
    "content": "POWER is the RATE at which energy is transferred or work is done.\n\nPower tells us how QUICKLY energy is being used — not how much total energy.\n\nEQUATIONS:\nP = E ÷ t\nP = W ÷ t\n\nP = power (W)\nE = energy transferred (J)\nW = work done (J)\nt = time (s)\n\nUNIT: watt (W) = 1 joule per second\n1 kilowatt (kW) = 1000 W\n1 megawatt (MW) = 1,000,000 W\n\nRearrangements:\nE = P × t\nt = E ÷ P",
    "heading": "What Is Power?"
  },
  {
    "content": "Two machines can do the SAME total work — but the more powerful one does it FASTER.\n\nEXAMPLE:\nMachine A: 1000 J in 10 s → P = 100 W\nMachine B: 1000 J in 5 s → P = 200 W\nMachine B is twice as powerful — same work, half the time.\n\nTypical power values:\n100 W lightbulb → 100 J/s transferred\n2000 W kettle → 2000 J/s transferred\n1000 W (≈1 kW) — elite sprinter sustained output\n50–150 kW — typical car engine\n\nPOWER AND WORK DONE IN CLIMBING:\nP = mgh ÷ t\nThis combines Ep = mgh with P = W/t — useful for stair/ramp problems.",
    "heading": "Comparing Power"
  },
  {
    "content": "ALWAYS convert time to SECONDS before calculating:\n1 minute = 60 s\n1 hour = 3600 s\n\nEXAMPLE 1 — finding energy:\nA 60 W bulb on for 5 minutes:\nt = 5 × 60 = 300 s\nE = 60 × 300 = 18,000 J\n\nEXAMPLE 2 — finding power:\nA motor transfers 36,000 J in 2 minutes:\nt = 2 × 60 = 120 s\nP = 36,000 ÷ 120 = 300 W\n\nEXAMPLE 3 — stair climb:\n60 kg person climbs 3 m in 4 seconds (g = 9.8):\nW = mgh = 60 × 9.8 × 3 = 1764 J\nP = 1764 ÷ 4 = 441 W",
    "heading": "Energy, Power and Time Calculations"
  }
]
```

## common_mistake

Time MUST be in SECONDS when using P = E/t with energy in joules. '5 minutes' = 300 s, NOT 5. Forgetting to convert is the most common mistake in power calculations.

## key_note

Power = rate of energy transfer. P = E/t = W/t. Unit: watt (W) = J/s. E = Pt. Always convert time to seconds. Higher power = same work done faster. P = mgh/t for climbing problems.

## equations
```json
[
  "P = E ÷ t",
  "P = W ÷ t",
  "E = P × t"
]
```

## fifas
```json
[
  {
    "label": "Power — Stair Climb",
    "question": "A 50 kg student climbs 4 m of stairs in 5 seconds. Calculate her power output. (g = 9.8 N/kg)",
    "steps": [
      [
        "F",
        "P = W ÷ t, where W = m × g × h"
      ],
      [
        "I",
        "W = 50 × 9.8 × 4 = 1960 J; t = 5 s"
      ],
      [
        "F",
        "P = 1960 ÷ 5"
      ],
      [
        "A",
        "P = 392 W"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "P",
    "Power",
    "watts",
    "W"
  ],
  [
    "E",
    "Energy transferred",
    "joules",
    "J"
  ],
  [
    "W",
    "Work done",
    "joules",
    "J"
  ],
  [
    "t",
    "Time",
    "seconds",
    "s"
  ]
]
```

## matching
```json
{
  "instruction": "Match each scenario to the correct power value.",
  "pairs": [
    [
      "100 W",
      "Device transfers 1000 J in 10 s — P = 1000 ÷ 10"
    ],
    [
      "500 W",
      "Motor does 30,000 J of work in 1 minute — P = 30,000 ÷ 60"
    ],
    [
      "200 W",
      "Engine transfers 24,000 J in 2 minutes — P = 24,000 ÷ 120"
    ],
    [
      "1 W",
      "1 joule transferred every second — the definition of 1 watt"
    ]
  ],
  "title": "Power Values"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "360,000 J — E = 2000 × (3 × 60) = 2000 × 180 = 360,000 J",
        true
      ],
      [
        "6000 J — used minutes not seconds: E = 2000 × 3",
        false
      ],
      [
        "11.1 J — divided instead of multiplied: 2000 ÷ 180",
        false
      ],
      [
        "6,000,000 J — multiplied by 3000 instead of 180",
        false
      ]
    ],
    "q": "A 2000 W heater is on for 3 minutes. How much energy does it transfer?",
    "wrong_explanations": {
      "1": "3 minutes must be converted to seconds: 3 × 60 = 180 s. E = 2000 × 3 = 6000 J uses minutes, not seconds.",
      "2": "P = E/t → E = P × t, not P ÷ t.",
      "3": "3 minutes = 180 s, not 3000 s. E = 2000 × 180 = 360,000 J."
    }
  },
  {
    "opts": [
      [
        "A has twice B's power — same work (mgh), but A does it in half the time",
        true
      ],
      [
        "Both have the same power — they do the same total work",
        false
      ],
      [
        "B has more power — taking longer means working harder overall",
        false
      ],
      [
        "Cannot compare — they take different times so cannot use the same equation",
        false
      ]
    ],
    "q": "Two students both lift a 10 kg bag 5 m. Student A takes 10 s, B takes 20 s. How do their power outputs compare?",
    "wrong_explanations": {
      "1": "Same work ÷ same time = same power — but the TIMES ARE DIFFERENT. P = W/t; A: P = mgh/10; B: P = mgh/20. A's power is twice B's.",
      "2": "More time for the same work = LESS power. B takes longer so B has lower power.",
      "3": "The same equation P = W/t applies to both — using different times is exactly how power differs between them."
    }
  }
]
```
