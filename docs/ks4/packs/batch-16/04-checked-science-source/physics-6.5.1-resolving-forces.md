# Resolving Forces and Vector Diagrams  (Physics, AQA 6.5.1 (HT only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| A force resolves into two perpendicular components with the same effect (theory 1) | higher | 8464 6.5.1.4 (HT only) · 8463 4.5.1.4 (HT only) |
| Resultant of two forces by scale drawing: tip-to-tail, parallelogram (theory 2 Methods 1–2) | higher | 8464 6.5.1.4 (HT only) |
| Equilibrium: closed triangle of forces; scale-drawing technique (theory 3; key_note; q2) | higher | 8464 6.5.1.4 (HT only) |
| Fx = F cos θ, Fy = F sin θ, R = √(Fx² + Fy²), arctan (theory 1, theory 2 Method 3; equations; common_mistake; FIFA method; q1; `higher`) | off-spec | — (spec: "scale drawings only") |
| Projectile problems (theory 1) | off-spec | — |

True page routes: CH TH. Site currently ships: TH; moving under the route-flag PR.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Resolve forces into components and use vector diagrams to find resultants.

## theory
```json
[
  {
    "content": "A single force can be RESOLVED into two PERPENDICULAR COMPONENTS.\nThis is the reverse of finding a resultant — splitting one force into two.\n\nFOR FORCE F AT ANGLE θ TO HORIZONTAL:\nHorizontal component: Fx = F cos θ\nVertical component: Fy = F sin θ\n\nWHY RESOLVE FORCES?\nMakes calculations simpler — can treat horizontal and vertical motion separately.\nEssential for inclined plane problems, projectile problems, force equilibrium.\n\nEXAMPLE:\nA 50 N force at 37° to the horizontal:\nFx = 50 cos 37° = 50 × 0.799 = 40 N (horizontal)\nFy = 50 sin 37° = 50 × 0.602 = 30 N (vertical)\nNote: 40² + 30² = 1600 + 900 = 2500 = 50² ✓ (Pythagoras check)",
    "heading": "Resolving Forces into Components"
  },
  {
    "content": "To find the RESULTANT of two forces not along the same line:\n\nMETHOD 1 — SCALE DRAWING (tip-to-tail):\n1. Choose a scale (e.g. 1 cm = 10 N).\n2. Draw the first force vector to scale.\n3. From the tip of the first vector, draw the second force vector to scale.\n4. Draw the resultant from the start of the first to the tip of the second.\n5. Measure the resultant length → convert to force. Measure the angle.\n\nMETHOD 2 — PARALLELOGRAM OF FORCES:\n1. Draw both forces from the same point to scale.\n2. Complete the parallelogram.\n3. The diagonal = resultant.\n\nMETHOD 3 — COMPONENT METHOD:\n1. Resolve all forces into x and y components.\n2. Sum all x-components: ΣFx.\n3. Sum all y-components: ΣFy.\n4. Resultant magnitude: R = √(ΣFx² + ΣFy²).\n5. Angle: θ = arctan(ΣFy / ΣFx).",
    "heading": "Vector Diagrams — Finding Resultants"
  },
  {
    "content": "EQUILIBRIUM: an object is in equilibrium when the resultant of all forces is zero.\n\nFor THREE FORCES in equilibrium:\nWhen drawn tip-to-tail, they form a CLOSED TRIANGLE (the triangle of forces).\nIf the triangle closes, the object is in equilibrium.\n\nPRACTICAL APPLICATIONS:\nFinding the tension in two strings supporting a weight.\nAnalysing forces on a stationary object on a slope.\nDetermining the direction of motion when two forces act.\n\nSCALE DRAWING TECHNIQUE:\nAccuracy matters — use a ruler and protractor.\nAlways state the scale used.\nConvert measurements back to actual forces using the scale.\n\nLIMITATIONS:\nScale drawings introduce measurement errors — component method is more precise.\nFor GCSE, scale drawings are acceptable for force problems.",
    "heading": "Equilibrium and Scale Drawings"
  }
]
```

## higher

HT only — resolve forces into components using trigonometry. Use vector diagrams (scale drawing, tip-to-tail, parallelogram) to determine resultants and solve equilibrium problems.

## common_mistake

When resolving a force, horizontal component uses COS and vertical uses SIN (for angle measured from horizontal). If angle is measured from the VERTICAL, swap sin and cos. Always check with Pythagoras: Fx² + Fy² should equal F².

## key_note

Resolve F at angle θ: Fx = F cosθ, Fy = F sinθ. Find resultant: component method R = √(Fx²+Fy²), or scale drawing tip-to-tail. Equilibrium: three forces form closed triangle. Parallelogram of forces: diagonal = resultant.

## equations
```json
[
  "Fx = F cos θ",
  "Fy = F sin θ",
  "R = √(Fx² + Fy²)"
]
```

## fifas
```json
[
  {
    "label": "Resultant of Two Forces",
    "question": "Forces of 3 N east and 4 N north act on an object. Find the resultant.",
    "steps": [
      [
        "F",
        "R = √(Fx² + Fy²); θ = arctan(Fy/Fx)"
      ],
      [
        "I",
        "Fx = 3 N (east), Fy = 4 N (north)"
      ],
      [
        "F",
        "R = √(3² + 4²) = √(9+16) = √25 = 5 N; θ = arctan(4/3) = 53° north of east"
      ],
      [
        "A",
        "Resultant = 5 N at 53° north of east"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "Fx",
    "Horizontal component",
    "newtons",
    "N"
  ],
  [
    "Fy",
    "Vertical component",
    "newtons",
    "N"
  ],
  [
    "F",
    "Resultant force",
    "newtons",
    "N"
  ],
  [
    "θ",
    "Angle to horizontal",
    "degrees",
    "°"
  ]
]
```

## matching
```json
{
  "instruction": "Match each vector quantity to the correct component formula.",
  "pairs": [
    [
      "Horizontal component",
      "Fx = F cos θ  (θ measured from horizontal)"
    ],
    [
      "Vertical component",
      "Fy = F sin θ  (θ measured from horizontal)"
    ],
    [
      "Resultant magnitude",
      "R = √(Fx² + Fy²)  — Pythagoras from components"
    ],
    [
      "Three forces in equilibrium",
      "Form a closed triangle when drawn tip-to-tail"
    ]
  ],
  "title": "Vector Components"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Horizontal = 5 N, vertical = 12 N — Fx = 13×0.385 = 5 N; Fy = 13×0.923 = 12 N",
        true
      ],
      [
        "Horizontal = 12 N, vertical = 5 N — Fx = 13×0.923; Fy = 13×0.385",
        false
      ],
      [
        "Both = 9.2 N — equal components at 67.4°",
        false
      ],
      [
        "Horizontal = 13 N, vertical = 0 — horizontal force has no vertical component",
        false
      ]
    ],
    "q": "A 13 N force acts at 67.4° to the horizontal. What are the horizontal and vertical components? (sin67.4° = 0.923, cos67.4° = 0.385)",
    "wrong_explanations": {
      "1": "Horizontal uses COS (angle from horizontal), vertical uses SIN — they are swapped in this option.",
      "2": "Components are only equal when θ = 45° — at 67.4° the components are unequal.",
      "3": "A force at an angle to the horizontal ALWAYS has both horizontal and vertical components unless it's purely horizontal."
    }
  },
  {
    "opts": [
      [
        "The object is in equilibrium — the resultant of the three forces is zero",
        true
      ],
      [
        "The three forces are all equal in magnitude — equilateral triangle",
        false
      ],
      [
        "The object is accelerating — closed triangles indicate net force",
        false
      ],
      [
        "The forces all act in the same direction — parallel vectors form triangles",
        false
      ]
    ],
    "q": "Three forces acting on an object form a closed triangle when drawn tip-to-tail. What does this tell us?",
    "wrong_explanations": {
      "1": "A closed triangle means the forces cancel — but they don't have to be equal. A closed triangle can be scalene (all different sides).",
      "2": "A closed triangle means ZERO resultant, which means equilibrium — zero resultant = zero acceleration.",
      "3": "Parallel forces cannot form a triangle — vectors must point in different directions."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** Forces of 3 N east and 4 N north act on an object. Find the resultant.

**Convert:** [NEW — examiner-corrected] Choose a scale, e.g. 1 cm = 1 N: 3 N east → 3 cm, 4 N north → 4 cm. Draw tip-to-tail, measure the resultant (5.0 cm) and convert back: 5.0 cm → 5 N; angle by protractor. (AQA: scale drawings only — the F, I, F steps below use Pythagoras/arctan, which is off-spec; see flags.)

**F:** R = √(Fx² + Fy²); θ = arctan(Fy/Fx)

**I:** Fx = 3 N (east), Fy = 4 N (north)

**F:** R = √(3² + 4²) = √(9+16) = √25 = 5 N; θ = arctan(4/3) = 53° north of east

**A:** Resultant = 5 N at 53° north of east
