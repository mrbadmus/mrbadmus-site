# Fleming's Left-Hand Rule and the Motor Effect  (Physics, AQA 6.7.2.2)

**Appears on routes:** Combined Higher, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Motor effect: conductor and magnet exert a force on each other (theory 1) | higher | 8464 6.7.2.2 (HT only) = 8463 4.7.2.2 (HT only) |
| Factors: current, flux density, length (theory 1; key_note) | higher | 8464 6.7.2.2 (HT only) |
| F = B × I × l, units (theory 1; equations; variables; FIFA) — On the sheet (8464 and 8463 June 2026, HT) | higher | 8464 6.7.2.2 (HT only) |
| Perpendicular = max, parallel = zero; reversing current or field reverses force (theory 1; q2) | higher | 8464 6.7.2.2 (HT only) |
| Fleming's left-hand rule (theory 2; key_note; q1) | higher | 8464 6.7.2.2 (HT only) |
| Fleming's right-hand rule; generators (theory 2; common_mistake) | not in spec; generator effect is triple-higher (F3) | 8463 4.7.3.1 |
| Loudspeakers (theory 3) | triple-higher (F4) | 8463 4.7.2.4 (physics only)(HT only) |
| DC motors (theory 3) | higher — next lesson | 8464 6.7.2.3 (HT only) |
| Meters, maglev, particle accelerators (theory 3) | not in spec (enrichment) — F5 | — |
| quiz q1 | higher — WRONG key, do not use as written (F1) | 8464 6.7.2.2 |
| quiz q2 | higher | 8464 6.7.2.2 |

True page routes: CH TH. Site currently ships: CH TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Apply Fleming's Left-Hand Rule to predict force on a current-carrying conductor in a magnetic field.

## theory
```json
[
  {
    "content": "When a CURRENT-CARRYING CONDUCTOR is placed in a MAGNETIC FIELD, it experiences a FORCE.\nThis is called the MOTOR EFFECT.\n\nThe force occurs because the magnetic field of the current interacts with the external magnetic field — the two fields combine to create a stronger field on one side and weaker on the other, pushing the conductor towards the weaker side.\n\nFACTORS AFFECTING THE SIZE OF THE FORCE:\nMAGNITUDE OF CURRENT — larger current → larger force.\nMAGNETIC FLUX DENSITY (B) — stronger field → larger force.\nLENGTH of conductor in the field — longer conductor → larger force.\n\nEQUATION:\nF = B × I × l\n\nF = force (N)\nB = magnetic flux density (tesla, T)\nI = current (A)\nl = length of conductor in the field (m)\n\nThe force is MAXIMUM when the conductor is PERPENDICULAR to the field.\nIf the conductor is PARALLEL to the field — no force.\n\nThe force direction can be REVERSED by:\nReversing the current direction, OR\nReversing the magnetic field direction.",
    "heading": "The Motor Effect"
  },
  {
    "content": "FLEMING'S LEFT-HAND RULE predicts the direction of force on a current-carrying conductor in a magnetic field.\n\nHold the left hand with three fingers mutually perpendicular:\n\nFIRST FINGER (index) → direction of MAGNETIC FIELD (N to S)\nSECOND FINGER (middle) → direction of CONVENTIONAL CURRENT (+ to −)\nTHUMB → direction of FORCE (MOTION) on the conductor\n\nMemory: FBI — First finger = Field, seCond finger (B ignored? no) — \nSimpler: F(orce) = thuMb, B(field) = First finger, I(current) = seCond finger.\n\nAll three must be at right angles to each other.\n\nEXAMPLE:\nHorizontal wire carrying current to the right, in a magnetic field pointing upward:\nField = upward (first finger up)\nCurrent = right (second finger right)\nForce = out of the page (thumb points out) — conductor is pushed towards you.\n\nRIGHT-HAND RULE is used for GENERATORS (opposite — motion given, find induced current direction).",
    "heading": "Fleming's Left-Hand Rule"
  },
  {
    "content": "The motor effect is the basis of ELECTRIC MOTORS and other electromagnetic devices.\n\nLOUDSPEAKERS:\nA coil of wire (voice coil) is attached to a paper cone and sits in a magnetic field.\nAlternating current through the coil → alternating force → cone vibrates → produces sound.\nFrequency of current = frequency of sound produced.\n\nDC MOTORS (covered in next subtopic):\nA coil in a magnetic field — motor effect creates a turning force (torque).\n\nMETER MOVEMENTS (galvanometers):\nCurrent through a coil in a magnetic field → coil rotates → needle deflects.\nThe deflection is proportional to the current — used as a current measuring device.\n\nMAGLEV TRAINS:\nElectromagnets in the track interact with superconducting magnets in the train.\nMotor effect provides both levitation and propulsion.\n\nPARTICLE ACCELERATORS:\nCharged particles moving through magnetic fields experience forces (motor effect for moving charges).\nThis curves the path of particles in cyclotrons and synchrotrons.",
    "heading": "Applications of the Motor Effect"
  }
]
```

## common_mistake

Fleming's LEFT-hand rule is for MOTORS (force on current in a field). Fleming's RIGHT-hand rule is for GENERATORS (induced current from motion in a field). Students often use the wrong hand. Remember: Left = motor effect (current → force). Right = generator effect (motion → current).

## key_note

Motor effect: force on current-carrying conductor in magnetic field. F = BIl. Fleming's LEFT-hand rule: First finger = Field, seCond = Current, thuMb = Motion/Force. Force maximised when conductor ⊥ field. Reverse current or field → reverse force. Applications: loudspeakers, motors, meters.

## equations
```json
[
  "F = B × I × l"
]
```

## fifas
```json
[
  {
    "label": "Motor Effect Force",
    "question": "A wire of length 0.05 m carries a current of 4 A in a magnetic field of flux density 2 T (perpendicular to the wire). Calculate the force on the wire.",
    "steps": [
      [
        "F",
        "F = B × I × l"
      ],
      [
        "I",
        "B = 2 T, I = 4 A, l = 0.05 m"
      ],
      [
        "F",
        "F = 2 × 4 × 0.05 = 2 × 0.2"
      ],
      [
        "A",
        "F = 0.4 N"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "F",
    "Force on conductor",
    "newtons",
    "N"
  ],
  [
    "B",
    "Magnetic flux density",
    "tesla",
    "T"
  ],
  [
    "I",
    "Current",
    "amperes",
    "A"
  ],
  [
    "l",
    "Length of conductor in field",
    "metres",
    "m"
  ]
]
```

## matching
```json
{
  "instruction": "Match each finger to what it represents in Fleming's Left-Hand Rule.",
  "pairs": [
    [
      "First finger (index)",
      "Direction of MAGNETIC FIELD — points from N to S"
    ],
    [
      "Second finger (middle)",
      "Direction of conventional CURRENT — points from + to −"
    ],
    [
      "Thumb",
      "Direction of FORCE (motion) on the conductor"
    ],
    [
      "F = BIl",
      "Force increases with stronger field, larger current, longer conductor"
    ]
  ],
  "title": "Fleming's Left-Hand Rule"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Out of the page (towards the observer) — field down, current right, force out",
        true
      ],
      [
        "Into the page — field down, current right, force in",
        false
      ],
      [
        "Upward — force is opposite to the field direction",
        false
      ],
      [
        "To the left — force is opposite to current direction",
        false
      ]
    ],
    "q": "A horizontal wire carries current to the right in a downward magnetic field. Using Fleming's Left-Hand Rule, in which direction is the force on the wire?",
    "wrong_explanations": {
      "1": "Apply the rule carefully: first finger DOWN (field), second finger RIGHT (current), thumb points OUT OF PAGE — not into.",
      "2": "Force is perpendicular to BOTH the field and current — not opposite to either individually.",
      "3": "Force is perpendicular to current, not opposite to it — F = BIl gives a force at right angles to both."
    }
  },
  {
    "opts": [
      [
        "Reverse the current direction OR reverse the magnetic field direction — either change reverses the force",
        true
      ],
      [
        "Increase the current magnitude — larger current reverses the force direction",
        false
      ],
      [
        "Move the conductor parallel to the field — this reverses the force",
        false
      ],
      [
        "Reduce the magnetic flux density to zero then increase it again",
        false
      ]
    ],
    "q": "How can the direction of force on a current-carrying conductor in a magnetic field be reversed?",
    "wrong_explanations": {
      "1": "Changing the MAGNITUDE of current changes the FORCE SIZE — not its direction.",
      "2": "A conductor parallel to the field experiences ZERO force — not reversed force.",
      "3": "Reducing B to zero means no force — increasing it again gives the same direction as before."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A wire of length 0.05 m carries a current of 4 A in a magnetic field of flux density 2 T (perpendicular to the wire). Calculate the force on the wire.

**Convert:** [NEW — examined ✓] Nothing to convert — flux density is already in tesla, current already in amperes and length already in metres, so F = B × I × l gives an answer directly in newtons with no unit change.

**F:** F = B × I × l

**I:** B = 2 T, I = 4 A, l = 0.05 m

**F:** F = 2 × 4 × 0.05 = 2 × 0.2

**A:** F = 0.4 N
