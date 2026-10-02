# Free Body Diagrams  (Physics, AQA 6.5.1 (HT only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| FBD: all forces ON one object, arrows to scale, labelled; describe qualitatively (theory 1, 2; common_mistake; key_note; q2) | higher | 8464 6.5.1.4 (HT only) · 8463 4.5.1.4 (HT only) |
| Force names; weight at centre of mass (theory 1) | base | 8464 6.5.1.2, 6.5.1.3 |
| Balanced → Newton's 1st; unbalanced → Newton's 2nd; terminal velocity (theory 2; q2) | base | 8464 6.5.4.2.1–2, 6.5.4.1.5 |
| Upthrust (theory 1) | triple-higher | 8463 4.5.5.1.2 (physics only)(HT only) |
| Resultant of angled forces by scale drawing (theory 2) | higher | 8464 6.5.1.4 (HT only) |
| Trig components; slope W sin θ / W cos θ (theory 2 "or trigonometry", theory 3; equations; key_note; `higher`; q1) | off-spec | — (FBDs "qualitatively"; "scale drawings only") |

True page routes: CH TH. Site currently ships: TH; moving under the route-flag PR.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Draw and interpret free body diagrams to represent the forces acting on an object.

## theory
```json
[
  {
    "content": "A FREE BODY DIAGRAM (FBD) shows all the forces acting ON a single object, drawn as arrows from (or through) the object.\n\nRULES:\nArrow length ∝ force magnitude.\nArrow direction = direction of force.\nLabel each force with its type AND magnitude (if known).\nDraw forces from the centre of mass or contact point.\nInclude ALL forces — weight, normal contact, friction, tension, drag, upthrust, applied forces.\n\nCOMMON FORCES TO SHOW:\nWEIGHT (W): always downward, from centre of mass.\nNORMAL CONTACT FORCE (N): perpendicular to the surface, away from surface.\nFRICTION: along the surface, opposing motion (or tendency to move).\nDRAG / AIR RESISTANCE: opposing motion, in fluid.\nTENSION: along string/rope/rod, towards the attachment point.\nUPTHRUST: upward, in a fluid.\nTHRUST/ENGINE FORCE: direction of motion.",
    "heading": "What Is a Free Body Diagram?"
  },
  {
    "content": "BALANCED FORCES (resultant = 0):\nIf all force arrows cancel out → object in EQUILIBRIUM.\nObject either stationary OR moving at constant velocity (Newton's 1st Law).\n\nUNBALANCED FORCES (resultant ≠ 0):\nNet force in one direction → object ACCELERATES in that direction (Newton's 2nd Law).\n\nEXAMPLES:\nBook on a table: weight down = normal contact force up → balanced → stationary.\nCar accelerating: thrust > drag → net forward force → accelerates.\nSky diver in free fall: weight down, drag up. Initially weight > drag → accelerates down. At terminal velocity: weight = drag → balanced → constant velocity.\nBox pushed on rough surface: applied force forward, friction backward → if equal → constant velocity.\n\nFINDING RESULTANT FROM FBD:\nAdd all force vectors (tip-to-tail or by resolving into components).\nIf forces are not at right angles, use scale drawing or trigonometry.",
    "heading": "Interpreting Free Body Diagrams"
  },
  {
    "content": "When forces act at angles, resolve them into HORIZONTAL and VERTICAL COMPONENTS.\n\nFOR A FORCE F AT ANGLE θ TO HORIZONTAL:\nHorizontal component: Fx = F cos θ\nVertical component: Fy = F sin θ\n\nThis allows calculation of resultant in each direction separately.\n\nEQUILIBRIUM using components:\nSum of horizontal forces = 0\nSum of vertical forces = 0\n\nEXAMPLE — inclined plane:\nObject on slope at angle θ:\nComponent of weight along slope: W sin θ (down the slope)\nComponent of weight perpendicular to slope: W cos θ (into slope)\nNormal contact force = W cos θ\nFriction force (if stationary) = W sin θ",
    "heading": "Resolving Forces from Free Body Diagrams"
  }
]
```

## higher

HT only — draw and interpret free body diagrams. Resolve forces into perpendicular components. Determine resultant force from FBD using scale drawing or components. Identify whether an object is in equilibrium from a FBD.

## common_mistake

All forces in a free body diagram act ON the object — not forces the object exerts on others. Weight always acts downward from the centre of mass. Normal contact force is PERPENDICULAR to the surface — not vertical (unless surface is horizontal).

## key_note

FBD: all forces on one object as arrows (length = magnitude). Balanced: resultant = 0, object stationary or constant velocity. Unbalanced: net force → acceleration. Resolve angled forces: Fx = F cosθ, Fy = F sinθ. Equilibrium: sum horizontal = 0 AND sum vertical = 0.

## equations
```json
[
  "Horizontal component: Fx = F cos θ",
  "Vertical component: Fy = F sin θ"
]
```

## matching
```json
{
  "instruction": "Match each situation to the correct FBD description.",
  "pairs": [
    [
      "Book at rest on table",
      "Weight down = normal contact up — balanced forces, resultant = 0"
    ],
    [
      "Skydiver at terminal velocity",
      "Weight down = drag up — balanced, constant velocity"
    ],
    [
      "Car accelerating",
      "Thrust > drag — net forward force, accelerates in direction of motion"
    ],
    [
      "Object on slope at rest",
      "Normal force perpendicular to slope = W cosθ; friction along slope = W sinθ"
    ]
  ],
  "title": "Free Body Diagrams"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "5 N — Fy = F sinθ = 10 × sin30° = 10 × 0.5 = 5 N",
        true
      ],
      [
        "8.66 N — Fy = F cosθ = 10 × cos30° = 10 × 0.866",
        false
      ],
      [
        "10 N — vertical component equals the full force at 30°",
        false
      ],
      [
        "3.33 N — Fy = F ÷ θ = 10 ÷ 30 = 0.33 N",
        false
      ]
    ],
    "q": "A 10 N force acts at 30° to the horizontal. What is the vertical component?",
    "wrong_explanations": {
      "1": "8.66 N is the HORIZONTAL component (F cosθ) — the vertical component uses sinθ: 10 × sin30° = 5 N.",
      "2": "The vertical component is only equal to the full force when θ = 90° — at 30°, Fy = F sinθ = 5 N.",
      "3": "Dividing by the angle has no physical meaning — components are found using sin and cos."
    }
  },
  {
    "opts": [
      [
        "Weight = drag force — the forces are balanced, resultant = 0, velocity is constant",
        true
      ],
      [
        "Weight > drag — the skydiver is still accelerating at terminal velocity",
        false
      ],
      [
        "Drag > weight — the upward force exceeds weight, so the skydiver slows down rapidly",
        false
      ],
      [
        "No forces act — terminal velocity means free fall with no air resistance",
        false
      ]
    ],
    "q": "In a free body diagram of a skydiver falling at terminal velocity, what must be true?",
    "wrong_explanations": {
      "1": "At terminal velocity, acceleration = 0 which means forces are BALANCED — but this means the skydiver continues at the same speed, not that they've stopped.",
      "2": "If drag > weight, the skydiver would decelerate — they'd slow below terminal velocity until drag equals weight again.",
      "3": "Terminal velocity specifically occurs because air resistance (drag) equals weight — forces do act."
    }
  }
]
```
