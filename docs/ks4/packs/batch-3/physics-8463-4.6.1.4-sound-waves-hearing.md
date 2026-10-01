# Sound Waves and Hearing  (Physics, AQA 6.6.1.4 (HT only, physics only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe sound wave properties and explain the range of human hearing and ultrasound.

## theory
```json
[
  {
    "content": "SOUND WAVES are longitudinal mechanical waves — compressions and rarefactions travel through a medium.\n\nSOUND CANNOT TRAVEL THROUGH A VACUUM — needs particles to vibrate.\n\nFREQUENCY AND PITCH:\nHigher frequency → higher pitch.\nHuman hearing range: approximately 20 Hz to 20,000 Hz (20 kHz).\nINFRASOUND: below 20 Hz — too low for humans to hear.\nULTRASOUND: above 20,000 Hz — too high for humans to hear.\n\nAMPLITUDE AND LOUDNESS:\nLarger amplitude → louder sound.\nMeasured in decibels (dB).\n\nSPEED OF SOUND:\nIn air: ~340 m/s (at room temperature).\nIn water: ~1500 m/s — faster because particles closer together.\nIn solids: even faster — densest medium, most efficient transmission.\nSound travels faster in denser media (unlike EM waves which slow in denser media).\n\nECHOES:\nSound reflects off hard surfaces → echo.\nEcho heard when reflected sound arrives >0.1 s after original → brain distinguishes them.",
    "heading": "Properties of Sound Waves"
  },
  {
    "content": "HUMAN HEARING:\n20 Hz to 20 kHz (varies with age — upper limit decreases with age).\nMost sensitive around 2–5 kHz (conversational speech frequencies).\n\nINFRASOUND (<20 Hz):\nNatural sources: earthquakes, volcanoes, ocean waves.\nSome animals detect infrasound: elephants, whales communicate over long distances.\nHumans can feel vibrations from very low-frequency infrasound.\n\nULTRASOUND (>20 kHz):\nAnimals that use ultrasound: bats (echolocation), dolphins, dogs.\nBats: emit ultrasound pulses → detect reflections → navigate and hunt insects.\n\nMEDICAL ULTRASOUND SCANNING:\nUltrasound sent into body → partially reflected at tissue boundaries.\nTime of reflection used to calculate depth: d = v × t/2.\nBuilds up 2D or 3D image.\nSafer than X-rays — no ionising radiation.\nUsed for: foetal scanning, soft tissue imaging, detecting gallstones/kidney stones.",
    "heading": "Range of Human Hearing"
  },
  {
    "content": "SONAR (Sound Navigation And Ranging):\nUsed by ships and submarines to measure ocean depth and detect objects.\nSend ultrasound pulse → detect echo → calculate distance:\nd = (v × t) / 2  where t = time for echo to return.\n\nINDUSTRIAL ULTRASOUND:\nDetecting cracks in metal structures (non-destructive testing).\nReflection at crack boundaries → detected → locates defect.\nCleaning delicate objects — high-frequency vibrations dislodge dirt.\n\nPREGNANCY SCANNING:\nUltrasound used for foetal monitoring.\nNo ionising radiation → safe for baby.\nCan detect multiple pregnancies, check development, measure foetal size.\n\nECHOCARDIOGRAPHY:\nUltrasound scan of the heart.\nAssesses heart valve function, chamber size, blood flow.\n\nCALCULATIONS:\nIf ultrasound pulse reflects from a boundary at depth d:\nd = v × t / 2\n(divide by 2 because the pulse travels to the boundary AND back)",
    "heading": "Ultrasound Applications"
  }
]
```

## higher

HT only — calculate distance using d = vt/2. Explain why ultrasound is preferred over X-rays for soft tissue scanning. Describe echolocation and SONAR applications quantitatively.

## common_mistake

In sonar/ultrasound calculations, divide the time by 2 because the pulse travels TO the boundary AND BACK. Using the full time gives double the actual distance. Sound travels FASTER in denser media (solid > liquid > gas) — opposite to EM waves.

## key_note

Sound: longitudinal, mechanical, needs medium. Human range: 20 Hz–20 kHz. Infrasound <20 Hz, ultrasound >20 kHz. Speed: solid > liquid > gas. Ultrasound uses: medical scanning, SONAR, non-destructive testing. d = v × t/2 (divide by 2 for return journey).

## equations
```json
[
  "d = v × t / 2  (distance to reflecting surface)"
]
```

## fifas
```json
[
  {
    "label": "SONAR Distance",
    "question": "A ship sends an ultrasound pulse. The echo returns after 0.06 s. Speed of sound in water = 1500 m/s. Calculate the depth of the seabed.",
    "steps": [
      [
        "F",
        "d = v × t / 2"
      ],
      [
        "I",
        "v = 1500 m/s, t = 0.06 s"
      ],
      [
        "F",
        "d = 1500 × 0.06 / 2 = 90 / 2"
      ],
      [
        "A",
        "d = 45 m"
      ]
    ]
  }
]
```

## variables
```json
[
  [
    "d",
    "Depth/distance",
    "metres",
    "m"
  ],
  [
    "v",
    "Speed of sound in medium",
    "m/s",
    "m/s"
  ],
  [
    "t",
    "Time for echo to return",
    "seconds",
    "s"
  ]
]
```

## matching
```json
{
  "instruction": "Match each application to the correct sound wave type and use.",
  "pairs": [
    [
      "SONAR depth sounding",
      "Ultrasound pulse reflected from seabed — d = vt/2"
    ],
    [
      "Foetal scanning",
      "Ultrasound — safe (non-ionising), images soft tissues"
    ],
    [
      "Bat echolocation",
      "Ultrasound emitted and detected — locate insects and navigate"
    ],
    [
      "Elephant communication",
      "Infrasound — below 20 Hz, travels long distances"
    ]
  ],
  "title": "Sound and Ultrasound"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "The pulse travels to the reflecting surface AND back — the total time is twice the one-way travel time",
        true
      ],
      [
        "Ultrasound travels at half the speed of normal sound in water",
        false
      ],
      [
        "Only half the energy of the pulse returns as an echo — the rest is absorbed",
        false
      ],
      [
        "There is always a 50% delay at the reflecting surface before the echo returns",
        false
      ]
    ],
    "q": "Why must you divide the echo time by 2 in SONAR calculations?",
    "wrong_explanations": {
      "1": "Ultrasound speed doesn't change by a factor of 2 — the factor of 2 accounts for the return journey distance.",
      "2": "Energy loss affects amplitude, not the time calculation for distance.",
      "3": "There is no fixed time delay at the surface — the factor of 2 is purely geometric (distance there and back)."
    }
  },
  {
    "opts": [
      [
        "Ultrasound is non-ionising — it doesn't damage cells or DNA like X-rays can; it's safe for the developing baby",
        true
      ],
      [
        "Ultrasound produces higher resolution images than X-rays — better for detailed foetal anatomy",
        false
      ],
      [
        "X-rays cannot penetrate soft tissue — ultrasound is the only option for soft tissue imaging",
        false
      ],
      [
        "Ultrasound is cheaper and faster than X-ray equipment",
        false
      ]
    ],
    "q": "Why is ultrasound used for foetal scanning rather than X-rays?",
    "wrong_explanations": {
      "1": "X-rays actually produce higher resolution images — but the ionising radiation risk outweighs this advantage for foetal scanning.",
      "2": "X-rays DO penetrate soft tissue (though not as well as bone) — but they are not used because of ionising radiation risk to the fetus.",
      "3": "Cost and speed are considerations, but the primary reason is SAFETY — avoiding ionising radiation exposure."
    }
  }
]
```
