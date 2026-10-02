# Momentum  (Physics, AQA 6.5.5.1–6.5.5.2)

**Appears on routes:** Combined Higher, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| p = mv; units; vector; th1 examples | higher | 8464 6.5.5.1 / 8463 4.5.7.1 (HT only) |
| Conservation in a closed system; describe/explain collisions and explosions qualitatively; common_mistake | higher | 8464 6.5.5.2 / 8463 4.5.7.2 (HT only) |
| Collision/explosion **calculations** — th2 examples, FIFA, q1 | triple-higher | 8463 4.5.7.2 (physics only) |
| Force = rate of change of momentum, F = mΔv/Δt ("impulse") — th1 link, th3, equations, key_note | triple-higher | 8463 4.5.7.3 (physics only) |
| Safety features via rate of change of momentum — th3, q2 | triple-higher | 8463 4.5.7.3 (physics only) |
| RP | none (trolley collisions are an AT suggestion, not an RP) | — |

True page routes: CH TH (physics-only layer TH only). Site currently ships: CH TH — matches; the physics-only layer currently shows on CH and must be gated to TH.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Define momentum, calculate it using p = mv and apply conservation of momentum to collisions.

## theory
```json
[
  {
    "content": "MOMENTUM is a property of any moving object — it depends on both mass and velocity.\n\nEQUATION:\np = m × v\n\np = momentum (kg m/s)\nm = mass (kg)\nv = velocity (m/s)\n\nMomentum is a VECTOR quantity — it has both magnitude and direction.\nDirection of momentum = direction of velocity.\n\nEXAMPLES:\n1000 kg car at 20 m/s: p = 1000 × 20 = 20,000 kg m/s\n0.5 kg cricket ball at 40 m/s: p = 0.5 × 40 = 20 kg m/s\n\nThe car has 1000× more momentum despite same speed — mass matters greatly.\n\nLink to Newton's Second Law:\nForce = rate of change of momentum = Δp ÷ Δt = mΔv ÷ Δt = ma\nThis is the more general form of F = ma.",
    "heading": "What Is Momentum?"
  },
  {
    "content": "In a CLOSED SYSTEM (no external forces), total momentum is CONSERVED.\n\nTotal momentum before event = Total momentum after event\n\nThis applies to:\nCOLLISIONS — two objects collide and stick together or bounce apart.\nEXPLOSIONS — one stationary object breaks apart.\n\nCOLLISION EXAMPLE:\nCar A (1000 kg) at 10 m/s hits stationary car B (800 kg). They stick together.\nBefore: p_total = (1000 × 10) + (800 × 0) = 10,000 kg m/s\nAfter: p_total = (1000 + 800) × v = 1800v\n10,000 = 1800 × v\nv = 10,000 ÷ 1800 = 5.56 m/s\n\nEXPLOSION EXAMPLE:\nA 2 kg rocket at rest fires a 0.1 kg shell at 500 m/s forward.\nBefore: p_total = 0 (at rest)\nAfter: p_shell + p_rocket = 0\n(0.1 × 500) + (1.9 × v) = 0\n50 + 1.9v = 0\nv = −50 ÷ 1.9 = −26.3 m/s (negative = backward)",
    "heading": "Conservation of Momentum"
  },
  {
    "content": "IMPULSE — changing momentum requires a force:\nF × t = Δp (impulse = change in momentum)\nF = Δp ÷ t\n\nTo stop an object with a given momentum:\nLONGER TIME → SMALLER FORCE required.\nSHORTER TIME → LARGER FORCE.\n\nSAFETY APPLICATIONS:\nCRUMPLE ZONES: car crushes slowly on impact → increases time of collision → reduces peak force on occupants.\nSEAT BELTS: stretch slightly → increase time for passenger to decelerate → reduce peak force.\nAIR BAGS: passenger's head decelerates into cushion of air → longer time → smaller force on head.\nHELMETS: foam compresses on impact → longer stopping time → reduced force on skull.\nCATCHING: a cricket ball caught by 'giving' with hands — increases time → reduces force.\nCYCLING HELMETS: foam liner increases stopping time for head in a crash.\n\nAll use the same principle: Δp is fixed (same change in momentum needed) — increasing time reduces the force.",
    "heading": "Momentum, Force and Safety"
  }
]
```

## common_mistake

Momentum is a VECTOR — direction matters. When objects move in opposite directions, one momentum is negative. In conservation problems: always define a positive direction first, then assign signs accordingly. Total momentum is ZERO before an explosion (object at rest), so the two parts fly off with equal and opposite momenta.

## key_note

p = mv. Vector — direction matters. Conservation: total p before = total p after (closed system). Applies to collisions and explosions. Impulse: F = Δp/t. Longer collision time → smaller force. Safety: crumple zones, airbags, seat belts, helmets all increase collision time.

## equations
```json
[
  "p = m × v",
  "Conservation: total p before = total p after",
  "Impulse: F × t = Δp"
]
```

## fifas
```json
[
  {
    "label": "Conservation of Momentum",
    "question": "A 600 kg car travelling at 15 m/s collides with a stationary 400 kg car. They stick together. Find their velocity after the collision.",
    "steps": [
      [
        "F",
        "Total p before = total p after: m₁v₁ + m₂v₂ = (m₁+m₂)v"
      ],
      [
        "I",
        "p before = (600 × 15) + (400 × 0) = 9000 kg m/s"
      ],
      [
        "F",
        "9000 = (600 + 400) × v = 1000v"
      ],
      [
        "A",
        "v = 9000 ÷ 1000 = 9 m/s"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "p",
    "Momentum",
    "kg m/s",
    "kg m/s"
  ],
  [
    "m",
    "Mass",
    "kilograms",
    "kg"
  ],
  [
    "v",
    "Velocity",
    "m/s",
    "m/s"
  ]
]
```

## matching
```json
{
  "instruction": "Match each scenario to the correct momentum or velocity.",
  "pairs": [
    [
      "20,000 kg m/s",
      "1000 kg car at 20 m/s — p = 1000 × 20"
    ],
    [
      "5.56 m/s",
      "1000 kg + 800 kg after collision (p = 10,000 kg m/s) — v = 10000/1800"
    ],
    [
      "Crumple zones",
      "Increase collision time → reduce peak force — same impulse, longer time"
    ],
    [
      "Zero",
      "Total momentum before an explosion — object was stationary"
    ]
  ],
  "title": "Momentum Calculations"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "2 m/s — p before = 0.5 × 8 = 4 kg m/s; (0.5+1.5)v = 4; v = 4/2 = 2 m/s",
        true
      ],
      [
        "4 m/s — using only the moving ball's mass: 4/0.5 = 8... wrong rearrangement",
        false
      ],
      [
        "8 m/s — velocity is conserved, not momentum",
        false
      ],
      [
        "0 m/s — the stationary ball stops the moving one",
        false
      ]
    ],
    "q": "A 0.5 kg ball moving at 8 m/s collides with a stationary 1.5 kg ball. They stick together. What is their combined velocity?",
    "wrong_explanations": {
      "1": "p = 4 kg m/s. After: (0.5+1.5)v = 4; 2v = 4; v = 2 m/s — not 4 (uses wrong total mass).",
      "2": "Velocity is NOT conserved — MOMENTUM is conserved. Speed always decreases when objects stick together.",
      "3": "The stationary ball doesn't have enough momentum to stop the moving one — momentum must balance."
    }
  },
  {
    "opts": [
      [
        "They increase the time of the collision, reducing the peak force on passengers for the same change in momentum",
        true
      ],
      [
        "They reduce the total momentum change — less deceleration occurs",
        false
      ],
      [
        "They absorb all kinetic energy — no force is transmitted to the passenger compartment",
        false
      ],
      [
        "They make the car lighter — less mass means less momentum and a gentler stop",
        false
      ]
    ],
    "q": "Why do modern cars have crumple zones at the front?",
    "wrong_explanations": {
      "1": "The momentum change (impulse) is the same — the car still goes from moving to stationary. Crumple zones increase TIME, not reduce the impulse.",
      "2": "Crumple zones don't absorb ALL kinetic energy without any force — they spread the energy absorption over a longer time to reduce peak force.",
      "3": "Crumple zones add mass (metal structure) — the mass reduction argument is not the mechanism."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A 600 kg car travelling at 15 m/s collides with a stationary 400 kg car. They stick together. Find their velocity after the collision.

**Convert:** [NEW — examined ✓] Nothing to convert — both masses are already in kilograms and the velocity already in m/s, so p = m × v and the conservation sum give kg m/s and m/s directly with no unit change.

**F:** Total p before = total p after: m₁v₁ + m₂v₂ = (m₁+m₂)v

**I:** p before = (600 × 15) + (400 × 0) = 9000 kg m/s

**F:** 9000 = (600 + 400) × v = 1000v

**A:** v = 9000 ÷ 1000 = 9 m/s
