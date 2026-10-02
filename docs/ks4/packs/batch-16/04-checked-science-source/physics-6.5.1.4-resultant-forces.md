# Resultant Forces  (Physics, AQA 6.5.1.4)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Resultant = single force, same effect; straight-line add/subtract (theory 1; key_note) | base | 8464 6.5.1.4 · 8463 4.5.1.4 |
| Zero resultant → still or constant velocity; non-zero → accelerates (theory 1, 3; common_mistake; q1) | base | 8464 6.5.4.2.1 · 8463 4.5.6.2.1 |
| Terminal velocity (theory 3; key_note; q2) | base | 8464 6.5.4.1.5 · 8463 4.5.6.1.5 |
| Free body diagrams (theory 2) | higher | 8464 6.5.1.4 (HT only) |
| Scale drawing of a resultant at an angle (theory 3; `higher`) | higher | 8464 6.5.1.4 (HT only) |
| Perpendicular resultant changes direction; circle (theory 3; `higher`) | higher | 8464 6.5.4.1.3 (HT only) |
| Pythagoras / trigonometry for angled forces (theory 1) | off-spec | — ("scale drawings only", 6.5.1.4) |
| "centripetal force" (`higher`) | off-spec term | — |

True page routes: CF CH TF TH (HT layer on CH TH).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Find the resultant of forces and relate it to the motion of an object.

## theory
```json
[
  {
    "content": "When MULTIPLE FORCES act on an object, they can be replaced by a SINGLE RESULTANT FORCE that has the same effect.\n\nFinding the resultant:\nFORCES IN THE SAME DIRECTION: add magnitudes.\nFORCES IN OPPOSITE DIRECTIONS: subtract smaller from larger; direction = that of larger force.\nFORCES AT RIGHT ANGLES: use Pythagoras; direction from trigonometry or scale drawing.\n\nBALANCED FORCES (resultant = 0):\nIf resultant force = 0, the object is either:\nStationary (at rest), OR\nMoving at CONSTANT VELOCITY (constant speed in a straight line).\nThis is Newton's First Law.\n\nUNBALANCED FORCES (resultant ≠ 0):\nIf resultant force ≠ 0, the object ACCELERATES (changes speed or direction).",
    "heading": "What Is a Resultant Force?"
  },
  {
    "content": "A FREE BODY DIAGRAM shows all forces acting ON a single object as arrows:\nLength ∝ magnitude of force.\nArrow points in direction of force.\nObject represented as a box or dot at the centre.\n\nEXAMPLES:\nStationary book on table:\n↑ Normal contact force (upward)\n↓ Weight (downward)\nResultant = 0 → balanced → stationary ✓\n\nCar accelerating forward:\n→ Driving force (forward, larger)\n← Friction + air resistance (backward, smaller)\nResultant = driving force − resistance → forwards → accelerates ✓\n\nSkydiver in free fall (before terminal velocity):\n↓ Weight (downward)\n↑ Air resistance (upward, smaller)\nResultant = weight − air resistance → downward → accelerates downward",
    "heading": "Free Body Diagrams"
  },
  {
    "content": "An object is in EQUILIBRIUM when the resultant force is zero:\nAll forces balance — no net force.\nObject stays still or moves at constant velocity.\n\nWhen forces are UNBALANCED:\nResultant force in the direction of motion → object SPEEDS UP.\nResultant force opposite to direction of motion → object SLOWS DOWN.\nResultant force perpendicular to motion → object CHANGES DIRECTION.\n\nSCALE DRAWING METHOD:\nDraw vectors head-to-tail to scale.\nResultant = vector from tail of first to head of last.\nMeasure magnitude with ruler (× scale factor).\nMeasure direction with protractor.\n\nTERMINAL VELOCITY:\nAs a falling object speeds up → air resistance increases.\nEventually air resistance = weight → resultant = 0 → constant velocity = terminal velocity.\nFor skydivers: terminal velocity ≈ 55 m/s (120 mph) before parachute.",
    "heading": "Equilibrium and Resultant"
  }
]
```

## higher

Resolve forces into components and use vector addition to find resultants of forces at angles (not just along a line). Describe examples of forces on objects travelling in a circle — centripetal force is always directed towards the centre. Explain why an object moving in a circle has a constantly changing velocity (direction changes) even at constant speed, and therefore is accelerating.

## common_mistake

A resultant force of ZERO does NOT mean the object is stationary — it means CONSTANT VELOCITY (which includes stationary). An object moving at constant speed in a straight line also has zero resultant force.

## key_note

Resultant = single force with same effect as all forces combined. Balanced (zero resultant): stationary or constant velocity. Unbalanced: acceleration. Free body diagrams: arrows from object, length = magnitude. Terminal velocity: air resistance = weight → zero resultant → constant speed.

## matching
```json
{
  "instruction": "Match each situation to the correct description of the resultant force and motion.",
  "pairs": [
    [
      "Resultant = 0, stationary",
      "Book on table — weight balanced by normal contact force"
    ],
    [
      "Resultant = 0, moving",
      "Car at constant speed on motorway — driving force equals resistance"
    ],
    [
      "Resultant forward",
      "Car accelerating — driving force greater than air resistance + friction"
    ],
    [
      "Terminal velocity",
      "Skydiver at constant speed — weight = air resistance, zero resultant"
    ]
  ],
  "title": "Resultant Force and Motion"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "The resultant force is zero — driving force equals resistive forces (friction + air resistance)",
        true
      ],
      [
        "No forces act on the car — it moves freely",
        false
      ],
      [
        "The driving force is greater than resistive forces — the car is accelerating",
        false
      ],
      [
        "The car must be slowing down — constant speed requires deceleration",
        false
      ]
    ],
    "q": "A car travels at constant speed along a straight road. What does this tell us about the forces on the car?",
    "wrong_explanations": {
      "1": "Forces always act on a moving car — gravity, normal, driving force, air resistance. Constant speed means they BALANCE.",
      "2": "Constant speed means balanced forces (resultant = 0) — not acceleration. Acceleration requires UNBALANCED forces.",
      "3": "Constant speed is neither speeding up nor slowing down — it requires balanced forces."
    }
  },
  {
    "opts": [
      [
        "Air resistance increases with speed until it equals weight — resultant becomes zero, so acceleration stops",
        true
      ],
      [
        "The skydiver runs out of energy from the jump — no more acceleration",
        false
      ],
      [
        "Gravity decreases with altitude — weight reduces to zero at terminal velocity",
        false
      ],
      [
        "Terminal velocity means constant acceleration, not constant speed",
        false
      ]
    ],
    "q": "A skydiver jumps from a plane. Initially they accelerate. Later they reach terminal velocity. Why do they stop accelerating?",
    "wrong_explanations": {
      "1": "Skydivers don't 'run out of energy' — gravity continuously acts on them. Acceleration stops when forces BALANCE.",
      "2": "Gravity changes very little over the heights of a typical skydive — weight stays approximately constant.",
      "3": "Terminal velocity means CONSTANT SPEED (zero acceleration) — not constant acceleration."
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
