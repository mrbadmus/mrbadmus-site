# Scalar and Vector Quantities  (Physics, AQA 6.5.1.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Scalar / vector definitions; lists; arrows (theory 1; key_note) | base | 8464 6.5.1.1; 8463 4.5.1.1 |
| Distance/displacement, speed/velocity (theory 2; common_mistake; q1) | base | 8464 6.5.4.1.1, 6.5.4.1.3; 8463 4.5.6.1.1, 4.5.6.1.3 |
| Mass vs weight (theory 2) | base | 8464 6.5.1.3; 8463 4.5.1.3 |
| Adding forces in a line (theory 3; key_note; q2) | base | 8464 6.5.1.4; 8463 4.5.1.4 |
| Forces at right angles: Pythagoras, scale drawing (theory 3; key_note; `equations`) | higher (spec: "scale drawings only") | 8464 6.5.1.4 (HT only); 8463 4.5.1.4 (HT only) |
| Circle at constant speed → changing velocity (common_mistake) | higher | 8464 6.5.4.1.3 (HT only); 8463 4.5.6.1.3 (HT only) |
| quiz q1, q2 | base | 8464 6.5.4.1.1; 6.5.1.4 |

True page routes: CF CH TF TH, with an HT layer (right-angle resultants; circular motion). Site currently ships: CF CH TF TH with no HT layer — HT content shown on Foundation, flagged (SCALAR-VECTOR-QUANTITIES-F1).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Distinguish scalar and vector quantities and represent vectors with arrows.

## theory
```json
[
  {
    "content": "SCALAR quantities have MAGNITUDE (size) only.\nVECTOR quantities have both MAGNITUDE and DIRECTION.\n\nSCALARS:\nDistance, speed, mass, time, temperature, energy, power, pressure.\n\nVECTORS:\nDisplacement, velocity, force, acceleration, momentum, weight.\n\nWhy direction matters:\nA force of 10 N to the right and 10 N to the left cancel out — net force is zero.\nIf force were scalar (no direction), you couldn't distinguish these.\n\nVECTOR REPRESENTATION:\nAn arrow represents a vector.\nLength of arrow ∝ magnitude.\nDirection of arrow = direction of the quantity.",
    "heading": "Scalars and Vectors"
  },
  {
    "content": "Several pairs are commonly confused:\n\nDISTANCE vs DISPLACEMENT:\nDistance: total path length travelled — scalar.\nDisplacement: straight-line distance from start to finish, with direction — vector.\nExample: walking 3 m east then 3 m west → distance = 6 m; displacement = 0 m.\n\nSPEED vs VELOCITY:\nSpeed: how fast — scalar (magnitude only).\nVelocity: speed in a specified direction — vector.\nExample: car at 30 m/s — speed = 30 m/s. Velocity = 30 m/s north.\n\nMASS vs WEIGHT:\nMass: amount of matter — scalar (kg).\nWeight: gravitational force — vector (N, acts downward).",
    "heading": "Distinguishing Common Pairs"
  },
  {
    "content": "When adding SCALAR quantities: simple arithmetic.\n3 kg + 5 kg = 8 kg (always).\n\nWhen adding VECTOR quantities: direction matters.\nTwo forces in the SAME direction: add magnitudes.\n10 N + 5 N (both right) = 15 N right.\n\nTwo forces in OPPOSITE directions: subtract smaller from larger.\n10 N right + 5 N left = 5 N right (resultant).\n\nTwo forces at RIGHT ANGLES: use Pythagoras.\nResultant² = F₁² + F₂²\n3 N up + 4 N right → resultant = √(9 + 16) = 5 N (at an angle).\n\nScale drawings can also be used to find the resultant of vectors at any angle.",
    "heading": "Adding Vectors"
  }
]
```

## common_mistake

SPEED is scalar, VELOCITY is vector. DISTANCE is scalar, DISPLACEMENT is vector. The most common error is treating velocity and speed as the same thing. A car travelling in a circle at constant SPEED has changing VELOCITY (direction changes).

## key_note

Scalar: magnitude only (distance, speed, mass, energy). Vector: magnitude + direction (displacement, velocity, force, acceleration, weight). Arrow length = magnitude; direction = vector direction. Adding vectors: same direction = add; opposite = subtract; right angles = Pythagoras.

## equations
```json
[
  "Resultant² = F₁² + F₂²  (for perpendicular vectors)"
]
```

## matching
```json
{
  "instruction": "Sort each quantity into scalar or vector.",
  "pairs": [
    [
      "Scalar",
      "Speed — magnitude of motion with no direction"
    ],
    [
      "Vector",
      "Velocity — speed in a specified direction"
    ],
    [
      "Scalar",
      "Distance — total path length, no direction"
    ],
    [
      "Vector",
      "Displacement — straight-line distance from start, with direction"
    ],
    [
      "Vector",
      "Force — magnitude and direction (e.g. 10 N downward)"
    ]
  ],
  "title": "Scalar or Vector?"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Distance = 400 m, displacement = 0 m — the runner returns to the starting point",
        true
      ],
      [
        "Distance = 0 m, displacement = 400 m — same as the lap distance",
        false
      ],
      [
        "Distance = 400 m, displacement = 400 m — both equal the lap length",
        false
      ],
      [
        "Both are zero — one full lap cancels everything out",
        false
      ]
    ],
    "q": "A runner completes one full lap of a 400 m circular track. What is the runner's distance and displacement?",
    "wrong_explanations": {
      "1": "Displacement is the NET change in position. After a full lap the runner is back at start → displacement = 0. Distance is the total path = 400 m.",
      "2": "Distance = displacement only for straight-line motion in one direction — a full lap gives zero displacement.",
      "3": "Distance is never zero if the runner moved — it counts total path length regardless of direction."
    }
  },
  {
    "opts": [
      [
        "5 N to the right — 8 − 3 = 5 N; direction is that of the larger force",
        true
      ],
      [
        "11 N to the right — 8 + 3 = 11 N (added without considering direction)",
        false
      ],
      [
        "5 N to the left — 3 − 8 = −5 N so leftward",
        false
      ],
      [
        "Zero — two forces always cancel out",
        false
      ]
    ],
    "q": "Two forces act on a box: 8 N to the right and 3 N to the left. What is the resultant force?",
    "wrong_explanations": {
      "1": "Vectors in OPPOSITE directions SUBTRACT. Adding gives 11 N which ignores direction.",
      "2": "The net force is in the direction of the LARGER force — 8 N is larger than 3 N so resultant is rightward.",
      "3": "Forces only cancel when equal in magnitude AND opposite in direction. 8 N ≠ 3 N so they don't cancel."
    }
  }
]
```
