# Uses of the Generator Effect  (Physics, AQA 6.7.3.2 (HT only, physics only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
True spec reference: **8463 4.7.3.2 Uses of the generator effect (HT only)**, under 4.7.3 "(physics only) (HT only)"; no 8464 equivalent. The `spec` field "6.7.3.2" is the site's internal number.

| point | layer | spec ref |
|---|---|---|
| Alternator: slip rings → ac; dynamo: split-ring commutator → dc (theory 1–2; common_mistake; key_note; `higher`; q1) | triple-higher | 8463 4.7.3.2 |
| pd–time graphs for alternator and dynamo | triple-higher — missing, see below | 8463 4.7.3.2 |
| ac frequency = rotation rate; UK mains 50 Hz | triple-higher (50 Hz itself base) | 8463 4.7.3.2; 8464 6.2.3.1 |
| Rotating-magnet generators, turbines, hydro, smoothing (theory 2–3) | not in spec (context) — F5 | — |
| Back-emf (theory 3; `higher`; key_note; q2) | not in spec — F1 | — |
| quiz q1 | triple-higher — usable | 8463 4.7.3.2 |
| quiz q2 | not in spec — do not use (F1) | — |

True page routes: TH. Site currently ships: TH — matches.

## Spec core missing from the frozen data (written from the spec, examiner)
8463 4.7.3.2, verbatim — the second bullet has no graph anywhere in the frozen data:

> "Students should be able to: • explain how the generator effect is used in an alternator to generate ac and in a dynamo to generate dc • draw/interpret graphs of potential difference generated in the coil against time."

What the graphs show (examiner): alternator — a sine-shaped curve alternating above and below zero, one full cycle per turn; dynamo — the same humps all on one side of zero, falling to zero twice per turn. Turning faster gives taller peaks AND more cycles in the same time (shorter period); a stronger magnet or more turns gives taller peaks at the same period.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe alternators, dynamos and their role as generators of electrical power.

## theory
```json
[
  {
    "content": "An ALTERNATOR is an AC generator — produces alternating current.\n\nCONSTRUCTION:\nCoil of wire rotating in a magnetic field.\nSLIP RINGS and BRUSHES connect the rotating coil to the external circuit.\nBecause slip rings rotate with the coil, they don't reverse the connections — AC produced.\n\nOUTPUT:\nSinusoidal AC — voltage varies as sine wave.\nFrequency of AC = frequency of coil rotation.\nUK mains: 50 Hz — the alternator must rotate at 50 revolutions per second (or 3000 rpm).\n\nUSES:\nPower stations: large alternators driven by steam turbines or gas turbines.\nCar alternators: charge the car battery while the engine runs.\nWind turbines: blades drive an alternator (or permanent magnet generator).",
    "heading": "Alternators"
  },
  {
    "content": "A DYNAMO produces direct current (DC) using a split-ring commutator.\n\nCONSTRUCTION:\nSame as alternator but with a SPLIT-RING COMMUTATOR instead of slip rings.\nThe commutator is a ring split into two halves.\nBrushes make contact with the two halves.\nEvery half-rotation, the connections swap → current in external circuit always flows in the same direction.\n\nOUTPUT:\nPulsing DC — voltage varies from 0 to maximum, never reverses.\nNot perfectly smooth — usually smoothed with capacitors for practical use.\n\nUSES:\nBicycle dynamos: wheel drives a small permanent magnet generator → powers lights.\nSmall DC generators in portable equipment.\n\nALTERNATOR vs DYNAMO:\nAlternator: slip rings → AC output.\nDynamo: split-ring commutator → pulsing DC output.\nBoth: rotating coil in magnetic field (or rotating magnet in fixed coil).",
    "heading": "Dynamos"
  },
  {
    "content": "ROTATING MAGNET GENERATORS (modern design):\nMany modern generators rotate the MAGNET inside a fixed coil of wire.\nAdvantage: no slip rings needed for the high-current output — simpler, more reliable.\nThe changing flux through the fixed coil still induces an emf.\n\nWIND TURBINES:\nBlades rotate by wind → drive a gearbox → speed up rotation → drive a generator.\nModern turbines often use permanent magnet generators without a gearbox.\nOutput: AC electricity fed to the grid.\n\nHYDROELECTRIC POWER:\nFalling water drives turbines → alternators → electricity.\nVery efficient (~90%): gravitational PE → kinetic → electrical.\n\nNUCLEAR AND GAS POWER STATIONS:\nHeat from nuclear fission or burning gas → steam → turbine → alternator.\nElectrical output: typically 50 Hz AC.\n\nBACK-EMF in MOTORS:\nA running electric motor generates a back-emf that opposes the supply voltage.\nAt startup: back-emf = 0, current is high → motor may overheat.\nAt full speed: back-emf nearly equals supply voltage → current is low, motor runs efficiently.",
    "heading": "Electromagnetic Induction in Practice"
  }
]
```

## higher

HT only — describe the construction and output of alternators and dynamos. Explain the difference between slip rings (AC) and split-ring commutators (DC). Describe back-emf in electric motors.

## common_mistake

ALTERNATORS use SLIP RINGS (give AC). DYNAMOS use SPLIT-RING COMMUTATORS (give DC). It's the type of connection, not the mechanical principle, that determines AC vs DC output. In modern generators, the magnet often rotates inside a fixed coil — but electromagnetic induction still occurs.

## key_note

Alternator: slip rings → AC output (50 Hz in UK). Dynamo: split-ring commutator → pulsing DC. Uses: alternators in power stations (steam turbines), car engines (charges battery), wind turbines. Dynamos: bicycle lights. Back-emf in motors: opposes supply, limits current at full speed.

## matching
```json
{
  "instruction": "Match each generator type to its construction and output.",
  "pairs": [
    [
      "Alternator",
      "Slip rings and brushes — output is sinusoidal AC"
    ],
    [
      "Dynamo",
      "Split-ring commutator — output is pulsing DC"
    ],
    [
      "Modern wind turbine generator",
      "Rotating permanent magnet inside fixed coil — no slip rings needed"
    ],
    [
      "Back-emf",
      "Opposing voltage generated by rotating motor — limits current at full speed"
    ]
  ],
  "title": "Alternators and Dynamos"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "The alternator uses slip rings — the connections don't reverse, giving AC. The dynamo uses a split-ring commutator which swaps connections each half-turn, giving pulsing DC.",
        true
      ],
      [
        "Alternators use stronger magnets — this produces AC. Dynamos use weaker magnets producing DC.",
        false
      ],
      [
        "Alternators rotate faster — high-speed rotation produces AC. Slow rotation gives DC.",
        false
      ],
      [
        "Alternators have more coil turns — more turns produces AC. Fewer turns gives DC.",
        false
      ]
    ],
    "q": "Why does an alternator produce AC while a dynamo produces DC?",
    "wrong_explanations": {
      "1": "Magnet strength affects the magnitude of the output, not whether it's AC or DC.",
      "2": "Rotation speed affects frequency and magnitude — not whether the output is AC or DC.",
      "3": "Number of turns affects the magnitude of the emf — not AC vs DC."
    }
  },
  {
    "opts": [
      [
        "A voltage generated by the rotating motor coil that opposes the supply — it limits the current drawn at full speed, making the motor efficient",
        true
      ],
      [
        "A voltage that helps the motor start — providing extra torque at startup",
        false
      ],
      [
        "A signal that tells the motor to reverse direction when needed",
        false
      ],
      [
        "The voltage dropped across the motor's internal resistance — represents wasted energy",
        false
      ]
    ],
    "q": "What is 'back-emf' in an electric motor, and why is it important?",
    "wrong_explanations": {
      "1": "Back-emf OPPOSES the supply — at startup when back-emf = 0, current is HIGH (potentially damaging). It doesn't help startup.",
      "2": "Back-emf has no signalling function — it's a physical consequence of the generator effect in a running motor.",
      "3": "Voltage drop across resistance is IR (Ohm's law) — back-emf is a separate effect from resistance, caused by the generator effect."
    }
  }
]
```
