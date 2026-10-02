# Gravity  (Physics, AQA 6.5.1.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Weight = force due to gravity; field around Earth (theory 1, 3; key_note) | base | 8464 6.5.1.3; 8463 4.5.1.3 |
| W = mg (On the sheet, 8464 and 8463 June 2026); units; FIFA | base | 8464 6.5.1.3; 8463 4.5.1.3 |
| Mass vs weight; Moon (theory 2; common_mistake; q1; q2) | base | 8464 6.5.1.3; 8463 4.5.1.3 |
| Newtonmeter measures weight (theory 2) | base | 8464 6.5.1.3; 8463 4.5.1.3 |
| Field lines, g with altitude (theory 3) | beyond spec (context) | — |
| Free fall in orbit (theory 3) | context; orbits are 8463 4.8.1.3 (physics only) | 8463 4.8.1.3 |
| Centre of mass; W ∝ m (∝ symbol) | base — missing from frozen data (GRAVITY-F2) | 8464 6.5.1.3; 8463 4.5.1.3 |
| quiz q1, q2 | base | 8464 6.5.1.3; 8463 4.5.1.3 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches.

## Spec core missing from the frozen data (written from the spec, examiner)
8464 6.5.1.3 = 8463 4.5.1.3, verbatim — the statements the frozen data omits:

> "The weight of an object may be considered to act at a single point referred to as the object's 'centre of mass'."
> "The weight of an object and the mass of an object are directly proportional." — "Students should recognise and be able to use the symbol for proportionality, ∝" (MS 3a)
> "(In any calculation the value of the gravitational field strength (g) will be given.)"

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain weight as gravitational force, distinguish mass from weight, and calculate using W = mg.

## theory
```json
[
  {
    "content": "WEIGHT is the FORCE acting on an object due to GRAVITY — it is a vector quantity acting downward.\n\nWEIGHT EQUATION:\nW = m × g\n\nW = weight (newtons, N)\nm = mass (kilograms, kg)\ng = gravitational field strength (N/kg)\n\nOn Earth: g = 9.8 N/kg (use 10 N/kg for estimates).\nOn the Moon: g ≈ 1.6 N/kg (about 1/6 of Earth's).\n\nMEANING OF g:\nThe gravitational field strength g tells us the weight per unit mass.\nOn Earth: every 1 kg of mass experiences 9.8 N of gravitational force downward.",
    "heading": "Weight and Gravitational Field Strength"
  },
  {
    "content": "MASS:\nAmount of matter in an object.\nScalar quantity — measured in kilograms (kg).\nConstant everywhere in the universe — doesn't change with location.\n\nWEIGHT:\nGravitational force on an object.\nVector quantity — measured in newtons (N).\nChanges with location — depends on gravitational field strength.\n\nEXAMPLES:\nA 70 kg astronaut:\nOn Earth: W = 70 × 9.8 = 686 N\nOn the Moon: W = 70 × 1.6 = 112 N\nIn deep space (no gravity): W = 0 N\nMass is 70 kg everywhere.\n\nMEASURING:\nMass: measured with a balance (compares gravitational force on both sides — same anywhere).\nWeight: measured with a calibrated spring balance/newton meter (reads force directly).",
    "heading": "Mass vs Weight"
  },
  {
    "content": "A GRAVITATIONAL FIELD is a region around a mass where any other mass experiences a force.\n\nField lines point TOWARDS the centre of mass (gravity is always attractive).\nOn Earth's surface, field lines point vertically downward (towards Earth's centre).\n\nGravitational field strength DECREASES with distance from the mass:\nAt Earth's surface: g = 9.8 N/kg\nAt altitude of 400 km (ISS orbit): g ≈ 8.7 N/kg (astronauts are still falling — not weightless!)\n\nWHY 'WEIGHTLESSNESS' IN SPACE:\nAstronauts in orbit are NOT weightless in terms of gravitational force.\nThey are in FREE FALL — constantly falling towards Earth but moving sideways fast enough to miss it.\nThe sensation of weightlessness occurs because everything around them is falling at the same rate.",
    "heading": "Gravitational Fields"
  }
]
```

## common_mistake

Mass and weight are DIFFERENT things. Mass (kg) is constant everywhere. Weight (N) changes with gravitational field strength. On the Moon, your MASS stays the same but your WEIGHT is less. Weight is measured in NEWTONS — not kilograms.

## key_note

W = mg. Weight = gravitational force (N, vector, downward). Mass = amount of matter (kg, scalar, constant). g = 9.8 N/kg on Earth, 1.6 N/kg on Moon. Weight changes with location; mass does not. Gravitational field: region where masses experience force.

## equations
```json
[
  "W = m × g"
]
```

## fifas
```json
[
  {
    "label": "Weight Calculation",
    "question": "Calculate the weight of a 12 kg object on Earth. (g = 9.8 N/kg)",
    "steps": [
      [
        "F",
        "W = m × g"
      ],
      [
        "I",
        "m = 12 kg, g = 9.8 N/kg"
      ],
      [
        "F",
        "W = 12 × 9.8"
      ],
      [
        "A",
        "W = 117.6 N"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "W",
    "Weight",
    "newtons",
    "N"
  ],
  [
    "m",
    "Mass",
    "kilograms",
    "kg"
  ],
  [
    "g",
    "Gravitational field strength",
    "N/kg",
    "N/kg"
  ]
]
```

## matching
```json
{
  "instruction": "Match each statement to mass or weight.",
  "pairs": [
    [
      "Mass",
      "Measured in kilograms — stays the same on the Moon and on Earth"
    ],
    [
      "Weight",
      "Measured in newtons — changes with gravitational field strength"
    ],
    [
      "W = 686 N",
      "70 kg person on Earth — W = 70 × 9.8 = 686 N"
    ],
    [
      "W = 112 N",
      "70 kg person on the Moon — W = 70 × 1.6 = 112 N"
    ]
  ],
  "title": "Mass vs Weight"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "128 N — W = 80 × 1.6 = 128 N",
        true
      ],
      [
        "784 N — W = 80 × 9.8 (used Earth's g)",
        false
      ],
      [
        "50 kg — mass on the Moon is 1/6 of Earth mass",
        false
      ],
      [
        "0 N — astronauts are weightless on the Moon",
        false
      ]
    ],
    "q": "An astronaut has mass 80 kg. What is her weight on the Moon? (g_Moon = 1.6 N/kg)",
    "wrong_explanations": {
      "1": "Use the Moon's gravitational field strength (1.6 N/kg), not Earth's (9.8 N/kg).",
      "2": "Mass NEVER changes — it is 80 kg on the Moon, on Earth, anywhere. Only weight changes.",
      "3": "The Moon has significant gravity (1.6 N/kg) — astronauts are not weightless on the surface. Weightlessness occurs in orbit (free fall)."
    }
  },
  {
    "opts": [
      [
        "Weight is measured in NEWTONS — kilograms measure MASS. Their weight is approximately 588 N (60 × 9.8)",
        true
      ],
      [
        "Nothing is wrong — weight and mass are the same thing and can be measured in the same units",
        false
      ],
      [
        "Weight should be in grams — 60,000 g",
        false
      ],
      [
        "The statement is correct on the Moon but wrong on Earth",
        false
      ]
    ],
    "q": "A student says 'my weight is 60 kg'. What is wrong with this statement?",
    "wrong_explanations": {
      "1": "Weight and mass are different physical quantities — they cannot use the same units.",
      "2": "Grams are a unit of mass — not weight. Weight is always in newtons.",
      "3": "Weight is always in newtons everywhere — the statement would still be wrong on the Moon (just a different wrong value)."
    }
  }
]
```

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** Calculate the weight of a 12 kg object on Earth. (g = 9.8 N/kg)

**Convert:** [NEW — examined ✓] Nothing to convert — mass is already in kg and g is already in N/kg (SI).

**F:** W = m × g

**I:** m = 12 kg, g = 9.8 N/kg

**F:** W = 12 × 9.8

**A:** W = 117.6 N
