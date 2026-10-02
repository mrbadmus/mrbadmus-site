# Electromagnetism  (Physics, AQA 6.7.2.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Field round a straight wire: circles; depends on current and distance; how to demonstrate (theory 1) | base | 8464 6.7.2.1 = 8463 4.7.2.1 |
| Grip rule for field direction (theory 1, 2) | base (drawing the direction is spec) | 8464 6.7.2.1 |
| Solenoid: strong uniform field inside, bar-magnet shape outside; iron core strengthens (theory 2) | base | 8464 6.7.2.1 |
| Why a solenoid increases the magnetic effect | base — missing from this file (ELECTROMAGNETISM-F8) | 8464 6.7.2.1 |
| Electromagnet = solenoid + iron core; iron not steel (theory 3; common_mistake; key_note) | base | 8464 6.7.2.1; 6.7.1.1 |
| Explaining how devices work from diagrams (bell, crane, relay, maglev, MRI — theory 3) | triple (F5) | 8463 4.7.2.1 "(Physics only) …interpret diagrams of electromagnetic devices in order to explain how they work" |
| Speakers (theory 3, last line) | triple-higher (F5) | 8463 4.7.2.4 (physics only) (HT only) |
| `higher` (Triple Higher copy): motor effect, F = BIl, Fleming's LHR | higher — belongs to `flemings-left-hand-rule`, not here (F1) | 8464 6.7.2.2 (HT only) |
| `higher` (TH copy): loudspeakers; generator effect | triple-higher — belongs to later lessons (F1) | 8463 4.7.2.4; 4.7.3.1 |
| `higher` (TH copy): "Fleming's Right-Hand Rule" | not in spec (F1) | — |
| `higher` (CF + TF copy): motor effect, F = BIl, LHR, motors, "Induced EMF (generator effect)" | higher / triple-higher shown on FOUNDATION routes — wrong route (F2) | 8464 6.7.2.2–6.7.2.3 (HT only); 8463 4.7.3.1 |
| `rp` "RP21 (Physics)" | not an AQA required practical — OFF-SPEC label (F4) | 8464 RP21 is infrared (6.6.2.2) |
| quiz q1 | base | 8464 6.7.2.1 |
| quiz q2 | base topic, OFF-SPEC key ("directly proportional") — do not use as written (F3) | 8464 6.7.2.1 |

True page routes: CF CH TF TH, with a triple layer (TF TH: interpreting device diagrams) and no HT layer (6.7.2.1 carries no HT content). Site currently ships: CF CH TF TH — matches; but every route's `higher` field is wrong for this lesson (F1, F2) and the triple layer is untagged — flagged.

## Spec core missing from the frozen data (written from the spec, examiner)
8464 6.7.2.1 = 8463 4.7.2.1, verbatim:

> "Shaping a wire to form a solenoid increases the strength of the magnetic field created by a current through the wire. The magnetic field inside a solenoid is strong and uniform."
> "Students should be able to: • describe how the magnetic effect of a current can be demonstrated • draw the magnetic field pattern for a straight wire carrying a current and for a solenoid (showing the direction of the field) • explain how a solenoid arrangement can increase the magnetic effect of the current."
> 8463 only: "(Physics only) Students should be able to interpret diagrams of electromagnetic devices in order to explain how they work."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the magnetic field around a current-carrying wire, solenoid and electromagnet.

## theory
```json
[
  {
    "content": "A current-carrying conductor produces a MAGNETIC FIELD around it.\n\nFor a STRAIGHT WIRE:\nField lines form CONCENTRIC CIRCLES around the wire.\nThe field is in a PLANE PERPENDICULAR to the wire.\nDIRECTION: given by the RIGHT-HAND RULE — point thumb in direction of conventional current (+ to −), fingers curl in direction of field lines.\n\nSTRENGTH depends on:\nSIZE OF CURRENT — larger current → stronger field.\nDISTANCE FROM WIRE — further away → weaker field.\n\nThis was discovered by Oersted (1820) — a compass placed near a current-carrying wire deflected. First evidence that electric current and magnetism are related.",
    "heading": "Magnetic Field Around a Current-Carrying Wire"
  },
  {
    "content": "A SOLENOID is a coil of wire. When current flows, it produces a uniform magnetic field INSIDE the coil.\n\nFIELD PATTERN:\nOutside the solenoid: similar to a bar magnet — lines from N to S.\nInside the solenoid: uniform, parallel field lines along the axis.\nThe solenoid acts like a BAR MAGNET — has a definite north and south end.\n\nIDENTIFYING POLES:\nRight-hand rule for solenoid: curl fingers in direction of conventional current flow around the coil → thumb points towards NORTH pole.\nAlternatively: view each end — if current flows ANTICLOCKWISE = NORTH; CLOCKWISE = SOUTH.\n\nSTRENGTH of solenoid's field:\nIncrease CURRENT → stronger field.\nIncrease NUMBER OF TURNS → stronger field.\nAdd IRON CORE → much stronger field (core becomes an induced magnet).",
    "heading": "The Solenoid"
  },
  {
    "content": "An ELECTROMAGNET is a solenoid with an IRON CORE.\n\nWhy iron (not steel)?\nIRON is a SOFT magnetic material — easily magnetised and demagnetised.\nWhen current is OFF → iron loses its magnetism quickly → electromagnet switches OFF.\nSTEEL would retain magnetism even when current is off — less useful as a switch.\n\nADVANTAGES over permanent magnets:\nCan be switched on and off.\nStrength can be controlled by changing current.\nPolarity can be reversed by reversing current direction.\n\nAPPLICATIONS:\nELECTRIC BELL: electromagnet attracts striker → bell rings → circuit broken → striker returns → repeat.\nELECTRIC CRANE (scrapyard): picks up ferromagnetic scrap when on → releases when off.\nCIRCUIT BREAKER (relay): electromagnet pulls a switch to break a circuit.\nMAGLEV TRAINS: electromagnets in track repel magnets in train → train levitates.\nMRI SCANNER: powerful electromagnets (superconducting) create strong, uniform field.\nSPEAKERS: varying current → changing force on cone → sound.",
    "heading": "Electromagnets"
  }
]
```

## higher

Describe the motor effect: a current-carrying conductor in a magnetic field experiences a force F = BIl. Apply Fleming's Left-Hand Rule to determine force direction. Explain how the motor effect is used in loudspeakers. Describe electromagnetic induction (generator effect): a conductor moving in a magnetic field induces an EMF — Fleming's Right-Hand Rule gives induced current direction.

## common_mistake

An electromagnet uses IRON (soft) — not steel (hard). Iron demagnetises when the current is switched off. Steel would retain magnetism. Increasing CURRENT or NUMBER OF TURNS both increase the strength of an electromagnet's field.

## key_note

Current-carrying wire: circular field lines, stronger with more current, weaker further away. Solenoid: uniform field inside, acts like bar magnet. Electromagnet: solenoid + iron core. Iron (soft): loses magnetism when off. Stronger with more current, more turns, iron core. Applications: cranes, bells, MRI, relays.

## rp

RP21 (Physics) — Investigate the factors affecting the strength of an electromagnet (number of turns, current). Plot field strength vs current or turns.

## matching
```json
{
  "instruction": "Match each feature to the correct description.",
  "pairs": [
    [
      "Magnetic field around a wire",
      "Concentric circles — stronger near the wire, strengthens with more current"
    ],
    [
      "Solenoid field",
      "Uniform inside the coil, acts like a bar magnet with N and S poles"
    ],
    [
      "Why iron core is used",
      "Iron is soft — easily demagnetised when current stops, so electromagnet switches off cleanly"
    ],
    [
      "Increasing field strength",
      "Increase current OR increase number of turns OR add iron core"
    ],
    [
      "Scrapyard crane",
      "Electromagnet picks up ferromagnetic scrap when on, releases when current switched off"
    ]
  ],
  "title": "Electromagnetism Concepts"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Iron is a soft magnetic material — it quickly loses magnetism when the current is switched off, so the electromagnet can be turned off easily",
        true
      ],
      [
        "Iron is harder than steel — it is more durable and resists damage",
        false
      ],
      [
        "Iron has higher electrical conductivity than steel — more current flows through it",
        false
      ],
      [
        "Steel would make the magnet too strong — iron limits the field to a safe level",
        false
      ]
    ],
    "q": "Why is an iron core used in an electromagnet instead of a steel core?",
    "wrong_explanations": {
      "1": "Steel is harder mechanically, but in magnetism 'hard' means it RETAINS magnetism — which is not wanted for a switchable electromagnet.",
      "2": "The iron core is not in the electrical circuit — it is inside the coil. Current flows through the wire coil, not the core.",
      "3": "The goal is NOT to limit strength — electromagnets are made as strong as possible. The issue is being able to switch off."
    }
  },
  {
    "opts": [
      [
        "The field doubles in strength — magnetic field strength is directly proportional to current",
        true
      ],
      [
        "The field halves — more current creates resistance which reduces the field",
        false
      ],
      [
        "The field stays the same — only the number of turns affects field strength",
        false
      ],
      [
        "The field quadruples — field strength increases with current squared",
        false
      ]
    ],
    "q": "What happens to the strength of an electromagnet's field when the current is doubled?",
    "wrong_explanations": {
      "1": "The magnetic field of an electromagnet is proportional to current (and to number of turns) — it doesn't reduce when current increases.",
      "2": "BOTH current and number of turns affect field strength. Doubling current doubles the field.",
      "3": "Field strength is directly proportional to current (not current squared). Doubling current → double field."
    }
  }
]
```

## higher — Combined Foundation copy (differs from the Triple Higher copy above)

The motor effect: a current-carrying conductor in a magnetic field experiences a force. F = BIl (force = flux density × current × length). Fleming's Left-Hand Rule: thumb = force direction, index = field, middle finger = current. Applications: electric motors (rotating coil in field). Induced EMF (generator effect).

## higher — Triple Foundation copy (differs from the Triple Higher copy above)

The motor effect: a current-carrying conductor in a magnetic field experiences a force. F = BIl (force = flux density × current × length). Fleming's Left-Hand Rule: thumb = force direction, index = field, middle finger = current. Applications: electric motors (rotating coil in field). Induced EMF (generator effect).
