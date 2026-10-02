# Stopping Distance and Braking  (Physics, AQA 6.5.4.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Stopping = thinking + braking; definitions; FIFA (chains two steps) | base | 8464 6.5.4.3.1 / 8463 4.5.6.3.1 |
| Thinking distance = speed × reaction time (s = vt) | base | 6.5.4.3.2 + 6.5.4.1.2 |
| Reaction time 0.2–0.9 s; tiredness, drugs, alcohol, distraction; measuring it; q2 (q2 wrong — see flags) | base | 8464 6.5.4.3.2 / 8463 4.5.6.3.2 |
| Braking factors: wet/icy road, worn tyres, brakes; estimate stopping distance over typical speeds | base | 8464 6.5.4.3.3 / 8463 4.5.6.3.3 |
| Braking distance ∝ v² (same braking force); q1 | base | 6.5.4.3.1, 6.5.4.3.3 with W = Fs, Ek = ½mv² |
| Work by brake friction removes Ek; brakes heat up; more speed → more force to stop in a given distance; more force → more deceleration; overheating / loss of control | base | 8464 6.5.4.3.4 / 8463 4.5.6.3.4 |
| Worn tyres / water dispersal (`higher` field; actually base) | base | 6.5.4.3.3 |
| Estimate deceleration forces on road vehicles | higher | 6.5.4.3.4 (HT only) |
| Interpret speed–stopping-distance graphs for a range of vehicles | triple | 8463 4.5.6.3.1 (physics only) |
| F = Δp/Δt for deceleration forces (`higher`); seat belts/crumple zones via rate of change of momentum | triple-higher | 8463 4.5.7.3 (physics only) in 4.5.7 (HT only) |
| RP | none | — |

True page routes: CF CH TF TH (HT layer on CH TH; physics-only on TF TH; triple-higher on TH). Site currently ships: CF CH TF TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Define stopping distance and explain factors affecting thinking distance and braking distance.

## theory
```json
[
  {
    "content": "STOPPING DISTANCE = THINKING DISTANCE + BRAKING DISTANCE\n\nTHINKING DISTANCE: distance travelled during the REACTION TIME of the driver (before brakes are applied).\nThinking distance = speed × reaction time\n\nBRAKING DISTANCE: distance travelled from when brakes are APPLIED until the vehicle stops.\n\nEXAMPLE (typical values at 30 mph = 13.3 m/s):\nThinking distance ≈ 9 m\nBraking distance ≈ 14 m\nStopping distance ≈ 23 m\nAt 60 mph: stopping distance ≈ 73 m (much more than double — braking distance increases with v²)",
    "heading": "Stopping Distance"
  },
  {
    "content": "Thinking distance = reaction time × speed\n\nThinking distance INCREASES with:\nHIGHER SPEED — same reaction time but more distance covered.\nIMPAIRED REACTION TIME due to:\nALCOHOL — slows nerve impulse transmission.\nDRUGS (including some prescription medicines) — affect concentration and reaction.\nTIREDNESS/FATIGUE — reduced alertness.\nDISTRACTION — mobile phones, eating, passengers.\n\nTYPICAL REACTION TIME: 0.2–0.9 seconds (average ~0.7 s).\n\nMEASURING REACTION TIME:\nRuler drop test: drop a ruler through a person's fingers — measure how far it falls before they catch it.\nElectronic reaction time testers.\nComputer-based tests.",
    "heading": "Factors Affecting Thinking Distance"
  },
  {
    "content": "Braking distance INCREASES with:\nHIGHER SPEED — braking distance ∝ v² (doubling speed quadruples braking distance).\nPOOR ROAD CONDITIONS:\nWet road: less friction between tyres and road.\nIcy road: dramatically less friction.\nLoose gravel: tyres lose grip.\nDEFECTIVE TYRES:\nBald tyres: little tread → reduced water dispersal → aquaplaning risk.\nUnder-inflated tyres: reduce contact area.\nPOOR BRAKES: worn brake pads, overheated brakes (brake fade).\nHEAVY VEHICLE: more mass → more kinetic energy to remove → longer braking distance (for same braking force).\n\nPHYSICS LINK:\nBraking force does WORK to remove kinetic energy:\nWork = F × d and Ek = ½mv²\nF × d = ½mv²\nSo d = mv² ÷ (2F)\nBraking distance ∝ v² — doubling speed quadruples braking distance.\n\nLARGE DECELERATIONS:\nHard braking → large deceleration → large forces on passengers.\nCould cause injuries — seat belts and crumple zones reduce risk.",
    "heading": "Factors Affecting Braking Distance"
  }
]
```

## higher

Explain the danger of large decelerations: F = Δp/Δt — hard braking produces very large deceleration forces on passengers which can cause injury. Explain why worn tyres increase braking distance — reduced tread depth decreases water dispersal, reducing friction. Evaluate the relationship between deceleration and the risk of injury in vehicle collisions.

## common_mistake

Braking distance ∝ v² — doubling speed QUADRUPLES braking distance (not doubles). Thinking distance is proportional to v (doubles when speed doubles). Students often mix up which factor affects which component.

## key_note

Stopping distance = thinking + braking. Thinking distance affected by speed and reaction time (alcohol, drugs, tiredness, distraction). Braking distance affected by speed (∝v²), road conditions (wet/ice), tyre condition, brake condition, vehicle mass. Double speed → 4× braking distance.

## equations
```json
[
  "Stopping distance = thinking distance + braking distance",
  "Thinking distance = speed × reaction time",
  "Braking distance ∝ v²"
]
```

## fifas
```json
[
  {
    "label": "Stopping Distance",
    "question": "A driver has reaction time 0.6 s and is driving at 20 m/s. The braking distance is 40 m. Calculate the total stopping distance.",
    "steps": [
      [
        "F",
        "Stopping distance = thinking distance + braking distance; thinking distance = speed × reaction time"
      ],
      [
        "I",
        "Speed = 20 m/s, reaction time = 0.6 s, braking distance = 40 m"
      ],
      [
        "F",
        "Thinking distance = 20 × 0.6 = 12 m"
      ],
      [
        "A",
        "Stopping distance = 12 + 40 = 52 m"
      ]
    ]
  }
]
```

## matching
```json
{
  "instruction": "Match each factor to thinking distance or braking distance.",
  "pairs": [
    [
      "Thinking distance",
      "Driver is tired — reaction time increases → more distance covered before braking"
    ],
    [
      "Thinking distance",
      "Driving faster — same reaction time but higher speed → more distance"
    ],
    [
      "Braking distance",
      "Wet road — reduced friction between tyres and surface"
    ],
    [
      "Braking distance",
      "Bald tyres — less tread → reduced grip → longer distance to stop"
    ],
    [
      "Both increase",
      "Higher speed — thinking distance ∝ v AND braking distance ∝ v²"
    ]
  ],
  "title": "Stopping Distance Factors"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "It quadruples — braking distance is proportional to v², so (20/10)² = 4 times longer",
        true
      ],
      [
        "It doubles — speed doubles so distance doubles",
        false
      ],
      [
        "It increases by 10 m — simple addition",
        false
      ],
      [
        "It stays the same — braking distance depends only on road conditions",
        false
      ]
    ],
    "q": "A car's speed doubles from 10 m/s to 20 m/s. How does the braking distance change?",
    "wrong_explanations": {
      "1": "Braking distance ∝ v (not v²) would give doubling — but it's ∝ v², so doubling speed multiplies braking distance by 4.",
      "2": "Braking distance is not fixed — it depends on speed squared, road conditions and braking force.",
      "3": "Braking distance depends strongly on speed (∝v²) — doubling speed quadruples it, not keeps it constant."
    }
  },
  {
    "opts": [
      [
        "Alcohol increases reaction time — the driver takes longer to respond, so thinking distance increases",
        true
      ],
      [
        "Alcohol weakens muscles — the driver cannot press the brakes as hard, increasing braking distance",
        false
      ],
      [
        "Alcohol blurs vision — the driver takes longer to see the hazard and applies brakes later",
        false
      ],
      [
        "Alcohol reduces vehicle mass — lighter car has less braking force available",
        false
      ]
    ],
    "q": "Why does alcohol increase stopping distance?",
    "wrong_explanations": {
      "1": "While impaired vision and muscle weakness may play minor roles, the PRIMARY effect of alcohol on stopping distance is through REACTION TIME (thinking distance component).",
      "2": "Vision is relevant but the primary mechanism tested at GCSE is the effect on REACTION TIME specifically.",
      "3": "Alcohol doesn't change vehicle mass — the driver's mass is a tiny fraction of the vehicle."
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

## fifas — CFIFA form (Convert step added; the four FIFA steps below are verbatim)

**Question:** A driver has reaction time 0.6 s and is driving at 20 m/s. The braking distance is 40 m. Calculate the total stopping distance.

**Convert:** [NEW — examiner-corrected] Nothing to convert — speed is in m/s, reaction time in s and braking distance in m, so thinking distance comes out in metres and adds straight onto the braking distance.

**F:** Stopping distance = thinking distance + braking distance; thinking distance = speed × reaction time

**I:** Speed = 20 m/s, reaction time = 0.6 s, braking distance = 40 m

**F:** Thinking distance = 20 × 0.6 = 12 m

**A:** Stopping distance = 12 + 40 = 52 m

## Spec core missing from the frozen data (written from the spec, examiner)

8464 6.5.4.3.4 / 8463 4.5.6.3.4 (base): "When a force is applied to the brakes of a vehicle, work done by the friction force between the brakes and the wheel reduces the kinetic energy of the vehicle and the temperature of the brakes increases. The greater the speed of a vehicle the greater the braking force needed to stop the vehicle in a certain distance. The greater the braking force the greater the deceleration of the vehicle. Large decelerations may lead to brakes overheating and/or loss of control." "explain the dangers caused by large decelerations"

(HT only): "estimate the forces involved in the deceleration of road vehicles in typical situations on a public road."

8464 6.5.4.3.3 / 8463 4.5.6.3.3 (base): "estimate how the distance required for road vehicles to stop in an emergency varies over a range of typical speeds."

8463 4.5.6.3.1 only — (physics only), TF TH: "Students should be able to estimate how the distance for a vehicle to make an emergency stop varies over a range of speeds typical for that vehicle." "Students will be required to interpret graphs relating speed to stopping distance for a range of vehicles."

8464 6.5.4.3.2 / 8463 4.5.6.3.2 (base): "interpret and evaluate measurements from simple methods to measure the different reaction times of students; evaluate the effect of various factors on thinking distance based on given data."
