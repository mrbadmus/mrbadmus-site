# Moments, Levers and Gears  (Physics, AQA 6.5.3 (physics only))

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Moment, M = F d, perpendicular distance, units (theory 1; equations; variables; common_mistake) | triple | 8463 4.5.4 |
| Principle of moments; seesaw (theory 2; key_note) | triple | 8463 4.5.4 |
| Levers as force multipliers (theory 2) — tweezers/fishing rod WRONG (MLG-F3) | triple | 8463 4.5.4 |
| Lever classes 1–3 (theory 2) | off-spec, context only | — |
| Gears: opposite rotation, slower with bigger moment (theory 3; key_note) — "more force" IMPRECISE (MLG-F4) | triple | 8463 4.5.4 |
| Gear ratio (theory 3; key_note; `higher`) | off-spec | — |
| `higher` — moments and principle of moments | triple — not HT (MLG-F5) | 8463 4.5.4 |
| FIFA (seesaw, chains: Step 1 / Step 2) | triple | 8463 4.5.4 |
| quiz q1 | triple — wx1 WRONG, do not use as written (MLG-F1) | 8463 4.5.4 |
| quiz q2 | triple — wx1 WRONG, do not use as written (MLG-F2) | 8463 4.5.4 |

True page routes: TF TH (one triple layer; no HT content). Site currently ships: TF TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Calculate moments, apply the principle of moments and describe levers and gears as force multipliers.

## theory
```json
[
  {
    "content": "A MOMENT is the turning effect of a force about a pivot.\n\nEQUATION:\nMoment = Force × perpendicular distance from the pivot\nM = F × d\n\nM = moment (newton-metres, N·m)\nF = force (newtons, N)\nd = perpendicular distance from line of action of force to pivot (metres, m)\n\nDirection:\nCLOCKWISE moment: force tends to turn the object clockwise.\nANTICLOCKWISE moment: force tends to turn the object anticlockwise.\n\nEXAMPLE:\nA 50 N force applied 0.4 m from a pivot:\nM = 50 × 0.4 = 20 N·m\n\nLARGER MOMENT can be achieved by:\nIncreasing the FORCE, OR\nIncreasing the DISTANCE from the pivot.\nThis is why door handles are at the edge, not the hinge side.",
    "heading": "Moments"
  },
  {
    "content": "PRINCIPLE OF MOMENTS (equilibrium condition):\nFor an object in equilibrium, total clockwise moments = total anticlockwise moments about any pivot.\n\nΣ(F × d) clockwise = Σ(F × d) anticlockwise\n\nEXAMPLE — balanced seesaw:\nChild A (600 N) sits 1.5 m from pivot.\nClockwise moment = 600 × 1.5 = 900 N·m\nChild B must produce 900 N·m anticlockwise.\nIf Child B weighs 450 N: distance = 900 ÷ 450 = 2 m from pivot.\n\nLEVERS as FORCE MULTIPLIERS:\nA lever is a rigid rod that pivots about a fulcrum (pivot).\nSmall input force × long distance = large output force × short distance.\nEXAMPLES: wheelbarrow, crowbar, scissors, tweezers, nutcracker, fishing rod.\n\nDifferent CLASSES of levers have pivot, effort and load in different positions:\nClass 1: pivot between effort and load (seesaw, crowbar).\nClass 2: load between pivot and effort (wheelbarrow, nutcracker).\nClass 3: effort between pivot and load (tweezers, fishing rod).",
    "heading": "Principle of Moments and Levers"
  },
  {
    "content": "GEARS are toothed wheels that transmit force and rotation.\n\nHow gears work:\nMeshed gears rotate in OPPOSITE DIRECTIONS.\nThe teeth interlock — no slipping.\n\nGEAR RATIO:\nGear ratio = number of teeth on driven gear ÷ number of teeth on driving gear\n\nLARGE GEAR driven by SMALL GEAR:\nOutput gear rotates SLOWER but with MORE FORCE (torque).\nUsed to increase turning force — e.g. low gear in a car for acceleration.\n\nSMALL GEAR driven by LARGE GEAR:\nOutput gear rotates FASTER but with LESS FORCE.\nUsed to increase speed — e.g. high gear in a car at speed.\n\nGEARS AS FORCE MULTIPLIERS:\nLike levers, gears convert a small force over a large rotation into a large force over a small rotation (or vice versa).\nEnergy is conserved — work done is the same (ignoring friction).\n\nAPPLICATIONS:\nBicycle gears — change between speed and force.\nCar gearbox — match engine output to driving conditions.\nClocks — precise speed reduction from mainspring to hour hand.\nWind turbines — gearbox speeds up slow blade rotation for the generator.",
    "heading": "Gears"
  }
]
```

## higher

Calculate moments and apply the principle of moments to solve equilibrium problems. Solve problems involving multiple forces and pivots. Calculate gear ratios and predict output speed/force. Explain the relationship between gear ratio, speed and force (torque).

## common_mistake

Distance in moments must be the PERPENDICULAR distance from the line of action of the force to the pivot — not the distance along the lever. For the principle of moments, the object must be in equilibrium (balanced and not rotating).

## key_note

Moment = F × d (N·m). Principle of moments: clockwise = anticlockwise for equilibrium. Levers: force multipliers — small force × long distance = large force × short distance. Gears: large driven by small = more force, less speed; small driven by large = more speed, less force. Gear ratio = teeth_driven ÷ teeth_driving.

## equations
```json
[
  "M = F × d",
  "Principle of moments: Σ clockwise moments = Σ anticlockwise moments"
]
```

## fifas
```json
[
  {
    "label": "Moment Calculation",
    "question": "A 300 N person sits 2 m to the right of a seesaw pivot. How far to the left must an 400 N person sit to balance?",
    "steps": [
      [
        "F",
        "Principle of moments: clockwise moments = anticlockwise moments → F₁ × d₁ = F₂ × d₂"
      ],
      [
        "I",
        "300 × 2 = 400 × d₂"
      ],
      [
        "F",
        "600 = 400 × d₂ → d₂ = 600 ÷ 400"
      ],
      [
        "A",
        "d₂ = 1.5 m"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "M",
    "Moment",
    "newton-metres",
    "N·m"
  ],
  [
    "F",
    "Force",
    "newtons",
    "N"
  ],
  [
    "d",
    "Perpendicular distance from pivot",
    "metres",
    "m"
  ]
]
```

## matching
```json
{
  "instruction": "Match each scenario to the correct moment or principle.",
  "pairs": [
    [
      "20 N·m",
      "50 N force applied 0.4 m from pivot — M = 50 × 0.4"
    ],
    [
      "Principle of moments (equilibrium)",
      "Total clockwise moments = total anticlockwise moments"
    ],
    [
      "Force multiplier (lever)",
      "Small input force × long distance = large output force × short distance"
    ],
    [
      "Large gear driven by small gear",
      "Output rotates slower but with more turning force (torque)"
    ]
  ],
  "title": "Moments and Levers"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "20 N·m — M = F × d = 40 × 0.5 = 20 N·m",
        true
      ],
      [
        "80 N·m — M = F ÷ d = 40 ÷ 0.5 = 80",
        false
      ],
      [
        "40.5 N·m — M = F + d = 40 + 0.5",
        false
      ],
      [
        "0.0125 N·m — M = d ÷ F = 0.5 ÷ 40",
        false
      ]
    ],
    "q": "A force of 40 N is applied 0.5 m from a pivot. What is the moment?",
    "wrong_explanations": {
      "1": "M = F ÷ d gives the force needed to produce a given moment at that distance — not the moment itself.",
      "2": "Adding force and distance gives meaningless units — M = F × d = 40 × 0.5 = 20 N·m.",
      "3": "M = d ÷ F inverts the relationship — M = F × d = 40 × 0.5 = 20 N·m."
    }
  },
  {
    "opts": [
      [
        "The back wheel turns slowly but with more turning force — useful for climbing hills",
        true
      ],
      [
        "The back wheel turns faster than the pedals — useful for high speeds",
        false
      ],
      [
        "The wheel and pedals turn at the same speed — no mechanical advantage",
        false
      ],
      [
        "The force decreases and speed increases — gears always trade force for speed",
        false
      ]
    ],
    "q": "A bicycle is in a low gear — a small driving gear meshes with a large driven gear. What is the effect?",
    "wrong_explanations": {
      "1": "Small driving → large driven gear gives MORE SPEED not more force. Low gear = large driving sprocket (at pedals) → small sprocket (at wheel) in cycling, OR equivalently small driving → large driven output.",
      "2": "Equal speeds = gear ratio of 1 — this is only when gears are identical.",
      "3": "Gears CAN either trade force for speed OR speed for force — it depends on which gear is driving which."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A 300 N person sits 2 m to the right of a seesaw pivot. How far to the left must an 400 N person sit to balance?

**Convert:** [NEW — examined ✓] Nothing to convert — both forces are already in newtons and the distance is already in metres, so M = F × d can be applied directly with no unit change.

**F:** Principle of moments: clockwise moments = anticlockwise moments → F₁ × d₁ = F₂ × d₂

**I:** 300 × 2 = 400 × d₂

**F:** 600 = 400 × d₂ → d₂ = 600 ÷ 400

**A:** d₂ = 1.5 m
