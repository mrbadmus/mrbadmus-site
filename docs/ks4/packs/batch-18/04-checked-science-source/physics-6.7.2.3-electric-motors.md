# Electric Motors  (Physics, AQA 6.7.2.3)

**Appears on routes:** Combined Higher, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Coil in a field tends to rotate: forces on opposite sides in opposite directions → turning effect (theory 1) | higher | 8464 6.7.2.3 (HT only) = 8463 4.7.2.3 (HT only) |
| Split-ring commutator and brushes keep it turning (theory 1; common_mistake; key_note) | higher (beyond the spec's wording; standard explanation of continuous rotation) | 8464 6.7.2.3 (HT only) |
| Increasing speed/turning effect: current, field, turns (theory 2) | higher | 8464 6.7.2.2–6.7.2.3 (HT only) |
| Iron core, armature, many coils (theory 2) | not in spec (enrichment) | — |
| Applications; efficiency vs engines (theory 3) | not in spec (context) | — |
| Regenerative braking — motor as generator (theory 3; key_note; q2) | triple-higher (F2) | 8463 4.7.3.1–4.7.3.2 (physics only)(HT only) |
| quiz q1 | higher — wx2 WRONG, do not use as written (F1) | 8464 6.7.2.3 |
| quiz q2 | triple-higher only (F2) | 8463 4.7.3.1 |

True page routes: CH TH, with a TH-only layer if regenerative braking is kept. Site currently ships: CH TH — matches; regenerative braking untagged on CH — flagged.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain how the motor effect causes a coil to rotate in an electric motor.

## theory
```json
[
  {
    "content": "A DC ELECTRIC MOTOR converts electrical energy into kinetic energy (rotation).\n\nKEY COMPONENTS:\nRectangular COIL of wire — sits between the poles of a magnet.\nSPLIT-RING COMMUTATOR — a ring split into two halves, connected to the coil ends.\nBRUSHES — stationary carbon contacts that touch the commutator and connect to the power supply.\n\nHOW IT ROTATES:\n1. Current flows through the coil via the brushes and commutator.\n2. The motor effect creates a FORCE on each side of the coil (F = BIl).\n3. The forces on opposite sides of the coil are in OPPOSITE DIRECTIONS → creates a turning force (TORQUE).\n4. The coil rotates.\n\nWHY IT KEEPS ROTATING — THE COMMUTATOR:\nWithout the commutator: after rotating 90°, the coil would reach vertical — the forces become parallel to the coil plane → no more torque → coil would oscillate, not spin continuously.\nThe SPLIT-RING COMMUTATOR swaps the current direction in the coil every half turn → forces always push the coil in the same rotation direction → continuous rotation.",
    "heading": "How a DC Electric Motor Works"
  },
  {
    "content": "The SPEED and TORQUE (turning force) of a DC motor can be increased by:\n\nINCREASING THE CURRENT:\nMore current → larger motor effect force (F = BIl) → more torque → faster rotation.\n\nINCREASING THE MAGNETIC FLUX DENSITY:\nStronger magnetic field → larger force → more torque.\nUse stronger permanent magnets or increase current in electromagnet.\n\nINCREASING THE NUMBER OF TURNS in the coil:\nMore turns → total force multiplied by number of turns → much more torque.\n\nADDING AN IRON CORE inside the coil:\nConcentrates and strengthens the magnetic field within the coil → more efficient motor.\n\nREAL DC MOTORS:\nUse many coils wound at different angles around an iron cylinder (ARMATURE).\nGives smoother rotation and more consistent torque.\nMultiple commutator segments and brushes.",
    "heading": "Increasing Motor Speed and Torque"
  },
  {
    "content": "Electric motors are found in almost every electrical device that involves rotation:\n\nCONSUMER ELECTRONICS:\nHard disk drives, cooling fans, disc drives, washing machines, vacuum cleaners.\n\nTRANSPORT:\nElectric vehicles: battery-powered motor → no combustion → zero direct emissions.\nHybrid cars: electric motor + petrol engine.\nElectric trains, trams, lifts.\n\nINDUSTRY:\nConveyor belts, pumps, compressors, CNC machine tools.\n\nMEDICAL:\nSurgical drills, ventilators, infusion pumps.\n\nADVANTAGES of electric motors over combustion engines:\nHighly EFFICIENT (>90% vs ~25-35% for petrol engines).\nInstant torque — maximum torque from standstill.\nNo direct exhaust emissions.\nSimple, reliable — fewer moving parts.\nCan act as GENERATORS during braking (regenerative braking — recovers KE back to electrical store).\n\nREGENERATIVE BRAKING:\nMotor reversal — when slowing, the motor acts as a generator.\nKE → electrical energy → stored in battery.\nReduces brake wear and improves overall efficiency.",
    "heading": "Applications of Electric Motors"
  }
]
```

## common_mistake

The SPLIT-RING COMMUTATOR swaps the current direction every half turn — this is what makes a DC motor spin continuously rather than oscillating. Without the commutator, the coil would rock back and forth. The commutator is unique to DC motors — AC motors use a different mechanism.

## key_note

DC motor: coil in magnetic field → motor effect forces → torque → rotation. Split-ring commutator: swaps current every half-turn → continuous rotation. Increase speed: more current, stronger field, more turns, iron core. Applications: EVs, appliances, industrial machines. Regenerative braking: motor acts as generator.

## matching
```json
{
  "instruction": "Match each motor component to its function.",
  "pairs": [
    [
      "Coil of wire",
      "Carries current in the magnetic field — experiences motor effect force"
    ],
    [
      "Permanent magnet",
      "Provides the magnetic field for the motor effect"
    ],
    [
      "Split-ring commutator",
      "Reverses current in coil every half turn — maintains continuous rotation"
    ],
    [
      "Carbon brushes",
      "Stationary contacts that connect the power supply to the rotating commutator"
    ]
  ],
  "title": "Electric Motor Components"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "It reverses the current in the coil every half turn — ensuring the forces always act to rotate the coil in the same direction",
        true
      ],
      [
        "It increases the magnetic field strength — making the motor more powerful",
        false
      ],
      [
        "It converts AC supply to DC for the motor coil",
        false
      ],
      [
        "It connects the motor to the power supply — without it no current would flow",
        false
      ]
    ],
    "q": "Why does a DC motor need a split-ring commutator?",
    "wrong_explanations": {
      "1": "The commutator doesn't affect field strength — it only switches current direction.",
      "2": "A commutator converts DC to pulsed DC in the coil — it's not an AC-to-DC converter (that's a rectifier).",
      "3": "The brushes connect to the supply — the commutator specifically reverses current direction at the right moment."
    }
  },
  {
    "opts": [
      [
        "Kinetic energy → electrical energy — the motor runs in reverse as a generator, charging the battery",
        true
      ],
      [
        "Electrical energy → kinetic energy — the motor accelerates the car to a stop",
        false
      ],
      [
        "Chemical energy → thermal energy — brakes convert stored energy to heat",
        false
      ],
      [
        "Kinetic energy → thermal energy — friction brakes absorb kinetic energy as heat",
        false
      ]
    ],
    "q": "An electric vehicle uses regenerative braking. What energy transfer occurs?",
    "wrong_explanations": {
      "1": "Accelerating the car to a stop makes no sense — regenerative braking decelerates by extracting energy from the motion.",
      "2": "Conventional friction brakes do convert KE to thermal — but regenerative braking specifically avoids this by converting to electrical energy instead.",
      "3": "Both conventional braking (KE → thermal) and regenerative braking (KE → electrical) happen simultaneously in many EVs — but regenerative braking specifically refers to the electrical recovery."
    }
  }
]
```
