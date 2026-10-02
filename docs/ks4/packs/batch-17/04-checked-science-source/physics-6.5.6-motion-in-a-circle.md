# Motion in a Circle  (Physics, AQA 6.5.6 (HT only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Constant speed, changing velocity, accelerating towards the centre (theory 1; common_mistake; key_note; `higher` s1) | higher | 8464 6.5.4.1.3; 8463 4.5.6.1.3 (HT only) |
| Resultant inward force from existing forces: friction, tension, gravity (theory 2; `higher` s2) | higher | 8464 6.5.4.1.3 with 6.5.4.2.2 |
| Force removed → straight line along the tangent (theory 2; common_mistake; key_note) | higher | 8464 6.5.4.1.3; 6.5.4.2.1 |
| "Centripetal" term; F = mv²/r; electron; roller coaster (theory 1–2) | off-spec (MIC-F4) | — |
| Orbits: gravity provides the force; faster stable orbit → smaller radius (theory 3; `higher` s3; key_note s4) — "spirals" IMPRECISE (MIC-F3) | triple-higher | 8463 4.8.1.3 (physics only, HT only) |
| Geostationary "radius ~36,000 km" (theory 3) | WRONG + off-spec (MIC-F2) | — |
| quiz q1 | higher | 8464 6.5.4.1.3 (HT only) |
| quiz q2 | triple-higher — key reason WRONG, do not use as written (MIC-F1) | 8463 4.8.1.3 (HT only) |

True page routes: CH TH, with a Triple Higher orbit layer. Site currently ships: TH; moving under the route-flag PR (TH → CH TH).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain why circular motion involves constant speed but changing velocity, and identify the centripetal force.

## theory
```json
[
  {
    "content": "An object moving in a circle at CONSTANT SPEED is still ACCELERATING.\n\nWHY?\nVELOCITY is a vector — it has both magnitude (speed) and direction.\nIn circular motion, the DIRECTION continuously changes even if speed stays constant.\nChanging direction → changing velocity → ACCELERATION.\n\nThis seems counterintuitive — 'constant speed = no acceleration' is a common error.\nFor circular motion: speed is constant, but velocity is NOT constant.\n\nCENTRIPETAL ACCELERATION:\nThe acceleration is always directed towards the CENTRE of the circle.\nCentre-seeking = centripetal.\n\nAt any point on the circle:\nVelocity is TANGENTIAL — at 90° to the radius.\nAcceleration (and net force) points towards the CENTRE.",
    "heading": "Speed vs Velocity in Circular Motion"
  },
  {
    "content": "Because the object accelerates towards the centre, there must be a NET FORCE towards the centre.\nThis is the CENTRIPETAL FORCE.\n\nImportant: centripetal force is NOT a new type of force — it is the NET INWARD FORCE produced by existing forces.\n\nEXAMPLES of what provides centripetal force:\nPlanet orbiting Sun: GRAVITY pulls planet towards Sun.\nCar on a roundabout: FRICTION between tyres and road.\nBall on a string: TENSION in the string.\nElectron orbiting nucleus: ELECTROSTATIC ATTRACTION.\nRoller coaster loop at top: NORMAL CONTACT FORCE + GRAVITY.\n\nF_centripetal = mv²/r (not required at GCSE but useful context).\n\nWHAT HAPPENS IF THE CENTRIPETAL FORCE IS REMOVED:\nBall on string: string cuts → ball flies off tangentially (not outward — tangentially).\nThis is Newton's 1st Law: without force, object continues in straight line.",
    "heading": "Centripetal Force"
  },
  {
    "content": "For an ORBIT at constant speed:\nGravitational force provides centripetal force.\nThe orbit is stable when gravitational pull exactly provides the centripetal force needed.\n\nIf SPEED INCREASES (at same orbit radius):\nCentripetal force needed = mv²/r → increases.\nGravity unchanged → less than centripetal force needed → object spirals outward.\n\nFor a STABLE ORBIT at greater speed:\nRadius must DECREASE — smaller orbit compensates for higher speed.\n\nFor a STABLE ORBIT at slower speed:\nRadius must INCREASE — larger orbit.\n\nThis explains why satellites in lower orbits move FASTER than those in higher orbits.\n\nGEOSTATIONARY SATELLITES:\nSpecific radius where orbital speed matches Earth's rotation period.\nRadius: ~36,000 km.\nFaster satellite: needs smaller radius to remain stable.\nSlower satellite: needs larger radius.",
    "heading": "Orbits and Circular Motion"
  }
]
```

## higher

HT only — explain why changing direction means acceleration even at constant speed. Identify what provides centripetal force in different situations. Explain orbital stability in terms of speed and radius relationship.

## common_mistake

An object in circular motion at constant SPEED is NOT in equilibrium — it IS accelerating (velocity changes direction). The centripetal force is NOT a separate force — it is the net resultant of existing forces (gravity, tension, friction etc.) directed towards the centre. If the centripetal force is removed, the object moves in a STRAIGHT LINE tangentially — not outward.

## key_note

Circular motion: constant speed, changing velocity (direction changes) → acceleration towards centre. Centripetal force = net inward force (gravity/tension/friction provides it). Remove centripetal force → straight-line tangential motion. Faster orbit at same radius = spiral outward; stable faster orbit needs smaller radius.

## matching
```json
{
  "instruction": "Match each situation to what provides the centripetal force.",
  "pairs": [
    [
      "Planet orbiting the Sun",
      "Gravitational attraction of the Sun towards the centre"
    ],
    [
      "Car going around a roundabout",
      "Friction between tyres and road surface, directed inward"
    ],
    [
      "Ball on a string in horizontal circle",
      "Tension in the string, directed towards the centre"
    ],
    [
      "Satellite in orbit",
      "Gravity pulling satellite towards Earth — no engine needed for stable orbit"
    ]
  ],
  "title": "Circular Motion"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Yes — its direction continuously changes, so velocity changes, meaning it accelerates towards Earth's centre",
        true
      ],
      [
        "No — constant speed means no acceleration by definition",
        false
      ],
      [
        "Yes — it accelerates away from Earth to maintain altitude",
        false
      ],
      [
        "No — acceleration requires a change in speed, which doesn't occur",
        false
      ]
    ],
    "q": "A satellite orbits Earth at constant speed. Is it accelerating? Explain.",
    "wrong_explanations": {
      "1": "Constant SPEED ≠ constant VELOCITY. Acceleration is rate of change of VELOCITY (a vector) — changing direction changes velocity even at constant speed.",
      "2": "The satellite accelerates TOWARDS Earth, not away from it — gravity provides the centripetal (inward) force.",
      "3": "Acceleration requires change in VELOCITY — this includes change in direction, not just change in speed."
    }
  },
  {
    "opts": [
      [
        "The orbital radius must decrease — a smaller orbit requires less centripetal force at higher speed",
        true
      ],
      [
        "The orbital radius must increase — faster satellites need larger orbits",
        false
      ],
      [
        "Nothing changes — orbital stability doesn't depend on speed",
        false
      ],
      [
        "The satellite must fire engines continuously to maintain the orbit",
        false
      ]
    ],
    "q": "A satellite's orbital speed is increased. What must happen for it to remain in a stable orbit?",
    "wrong_explanations": {
      "1": "Higher orbital radius at higher speed would mean the gravitational force is insufficient — lower orbits (smaller radius) are needed for faster speeds.",
      "2": "Orbital stability absolutely depends on the balance between gravitational force and required centripetal force for the given speed.",
      "3": "Stable circular orbits are maintained by gravity alone — no engines needed for a circular orbit."
    }
  }
]
```
