# Distance–Time Graphs  (Physics, AQA 6.5.4.1.4)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| d–t graph; gradient = speed; flat = stationary; straight = constant speed; curve = changing speed | base | 8464 6.5.4.1.4 / 8463 4.5.6.1.4 |
| Downward line = returning (only with axis "distance from start") | base | 6.5.4.1.4 |
| speed = Δd ÷ Δt; large triangle; FIFA | base | 6.5.4.1.4 |
| Draw a d–t graph from measurements (not in the frozen data) | base | 6.5.4.1.4 |
| Average speed for a whole non-uniform journey | base | 8464 6.5.4.1.2 / 8463 4.5.6.1.2 |
| Tangent to a curve → instantaneous speed (th3 "TANGENT TRICK"; `higher`) | higher | 6.5.4.1.4 (HT only) |
| q1, q2 | base | 6.5.4.1.4 |
| RP | none | — |

True page routes: CF CH TF TH (HT layer on CH TH). Site currently ships: CF CH TF TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Interpret distance–time graphs and calculate speed from the gradient.

## theory
```json
[
  {
    "content": "A DISTANCE–TIME GRAPH shows distance from a reference point (y-axis) against time (x-axis).\n\nGRADIENT = SPEED:\nSteeper gradient → faster speed.\nFlat (horizontal) line → stationary (speed = 0).\nDownward slope → returning towards start.\n\nUNIFORM MOTION (constant speed): straight line with constant gradient.\nNON-UNIFORM MOTION (changing speed): curved line — gradient changes.\n\nCALCULATING SPEED FROM GRADIENT:\nspeed = Δd ÷ Δt = (change in distance) ÷ (change in time)\nPick two clear points on the line and divide the vertical change by the horizontal change.",
    "heading": "Reading Distance–Time Graphs"
  },
  {
    "content": "STATIONARY: horizontal straight line (distance doesn't change).\nCONSTANT SPEED: straight line with positive gradient.\nACCELERATING: curve with increasing gradient (getting steeper).\nDECELERATING: curve with decreasing gradient (getting shallower).\nRETURNING: line going back down — distance from starting point decreasing.\n\nEXAMPLE:\nGraph shows: 0–4 s: straight line to 20 m (constant speed).\n4–6 s: horizontal (stationary).\n6–10 s: straight line back to 0 m.\n\nSpeed in first section: 20 m ÷ 4 s = 5 m/s\nSpeed stationary: 0 m/s\nReturn speed: 20 m ÷ 4 s = 5 m/s",
    "heading": "Different Motion Shapes"
  },
  {
    "content": "EXAM TECHNIQUE:\nAlways use a large triangle when calculating gradient — minimises reading errors.\nRead coordinates from the axis, not from the line itself if possible.\nCheck units — distance in metres, time in seconds → speed in m/s.\n\nTANGENT TRICK (Higher Tier):\nFor a curved distance–time graph, draw a tangent at the point of interest.\nGradient of tangent = instantaneous speed at that point.\n\nFOUNDATION LEVEL:\nOnly need to find average speed from a straight-line section.\nDescribe the motion from different sections of the graph.",
    "heading": "Using the Graph"
  }
]
```

## higher

Calculate the instantaneous speed of an accelerating object at a specific time by drawing a tangent to the curve at that point on a distance–time graph and calculating its gradient. Distinguish between instantaneous and average speed.

## common_mistake

A FLAT (horizontal) section means the object is STATIONARY — not moving at constant speed. Constant speed gives a diagonal straight line. A steeper line means FASTER speed.

## key_note

Gradient of d–t graph = speed. Steep straight line = fast constant speed. Flat line = stationary. Curve = changing speed (accelerating or decelerating). Negative gradient = returning to start. Calculate speed: pick two points, speed = Δd/Δt.

## equations
```json
[
  "Speed = gradient of distance–time graph = Δd ÷ Δt"
]
```

## fifas
```json
[
  {
    "label": "Speed from d–t Graph",
    "question": "A d–t graph shows an object moving from 0 m to 60 m in the first 12 seconds. Calculate the speed.",
    "steps": [
      [
        "F",
        "Speed = gradient = Δd ÷ Δt"
      ],
      [
        "I",
        "Δd = 60 − 0 = 60 m, Δt = 12 − 0 = 12 s"
      ],
      [
        "F",
        "Speed = 60 ÷ 12"
      ],
      [
        "A",
        "Speed = 5 m/s"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "v",
    "Speed",
    "m/s",
    "m/s"
  ],
  [
    "d",
    "Distance",
    "metres",
    "m"
  ],
  [
    "t",
    "Time",
    "seconds",
    "s"
  ]
]
```

## matching
```json
{
  "instruction": "Match each section of a d–t graph to the motion it represents.",
  "pairs": [
    [
      "Steep straight line upward",
      "Fast constant speed away from start"
    ],
    [
      "Horizontal flat line",
      "Stationary — object has stopped"
    ],
    [
      "Gentle straight line upward",
      "Slow constant speed away from start"
    ],
    [
      "Straight line downward",
      "Constant speed returning towards starting point"
    ],
    [
      "Upward curve (increasing steepness)",
      "Accelerating — speed increasing over time"
    ]
  ],
  "title": "Distance–Time Graph Sections"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "The object is stationary — no change in distance means zero speed",
        true
      ],
      [
        "The object is moving at constant speed — horizontal means steady motion",
        false
      ],
      [
        "The object is accelerating — the line is preparing to slope upward",
        false
      ],
      [
        "The object has reached maximum speed and is maintaining it",
        false
      ]
    ],
    "q": "On a distance–time graph, what does a horizontal section of the line tell you about the object?",
    "wrong_explanations": {
      "1": "A horizontal line on a VELOCITY–time graph means constant velocity — but on a DISTANCE–time graph it means zero speed (stationary).",
      "2": "Flat line = zero gradient = zero speed. Constant speed on a d–t graph is a SLOPED straight line.",
      "3": "Acceleration on a d–t graph shows as a CURVE (increasing gradient) — not a flat section."
    }
  },
  {
    "opts": [
      [
        "Section A — steeper gradient on a d–t graph means higher speed",
        true
      ],
      [
        "Section B — less steep means the object is working harder to maintain motion",
        false
      ],
      [
        "They are the same speed — both are straight lines",
        false
      ],
      [
        "Section B — a gentler slope indicates faster, more efficient motion",
        false
      ]
    ],
    "q": "Section A of a distance–time graph has a gradient of 8 m/s and section B has a gradient of 2 m/s. Which section shows faster motion?",
    "wrong_explanations": {
      "1": "Gentler slope does not imply harder work — gradient directly equals speed on a d–t graph.",
      "2": "Both are straight lines (constant speed) but at DIFFERENT speeds — the gradient value gives the speed.",
      "3": "Gentle slope = smaller gradient = slower speed. Fast motion = steeper slope = larger gradient."
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

**Question:** A d–t graph shows an object moving from 0 m to 60 m in the first 12 seconds. Calculate the speed.

**Convert:** [NEW — examined ✓] Nothing to convert — the distance change is already in metres and the time change already in seconds, so Speed = Δd ÷ Δt gives an answer directly in m/s with no unit change.

**F:** Speed = gradient = Δd ÷ Δt

**I:** Δd = 60 − 0 = 60 m, Δt = 12 − 0 = 12 s

**F:** Speed = 60 ÷ 12

**A:** Speed = 5 m/s

## Spec core missing from the frozen data (written from the spec, examiner)

8464 6.5.4.1.4 / 8463 4.5.6.1.4 (base): "Students should be able to draw distance–time graphs from measurements and extract and interpret lines and slopes of distance–time graphs, translating information between graphical and numerical form."

8464 6.5.4.1.2 / 8463 4.5.6.1.2 (base): "Students should be able to calculate average speed for non-uniform motion." (average speed = total distance ÷ total time)
