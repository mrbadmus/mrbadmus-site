# Microphones  (Physics, AQA 6.7.3.3 (HT only, physics only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
True spec reference: **8463 4.7.3.3 Microphones (HT only)**, under 4.7.3 "(physics only) (HT only)"; no 8464 equivalent. The `spec` field "6.7.3.3" is the site's internal number.

| point | layer | spec ref |
|---|---|---|
| Moving-coil microphone: sound → diaphragm → coil moves in field → generator effect → current varying at the sound's frequency (theory 1; common_mistake; key_note; `higher`) | triple-higher | 8463 4.7.3.3 |
| Reverse of the loudspeaker (theory 1) | triple-higher | 8463 4.7.3.3; 4.7.2.4 |
| Condenser / ribbon / electret, quality factors, ADC (theory 2–3) | not in spec — F3 | — |
| "induction works both ways … Einstein's principle of symmetry" (theory 3) | WRONG — F1 | — |
| quiz q1 | triple-higher — usable | 8463 4.7.3.3 |
| quiz q2 | triple-higher — not usable as written (wx2, F2) | 8463 4.7.3.3 |

True page routes: TH. Site currently ships: TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how microphones use electromagnetic induction to convert sound into electrical signals.

## theory
```json
[
  {
    "content": "A MICROPHONE converts sound energy into electrical energy using ELECTROMAGNETIC INDUCTION — the reverse of a loudspeaker.\n\nDYNAMIC MICROPHONE (most common):\nCOMPONENTS: diaphragm, attached coil, permanent magnet.\n\nOPERATION:\n1. Sound waves hit the diaphragm → diaphragm vibrates.\n2. Coil attached to diaphragm moves back and forth in the permanent magnet's field.\n3. Moving coil cuts magnetic field lines → GENERATOR EFFECT → induced emf.\n4. Induced current alternates at the SAME FREQUENCY as the sound wave.\n5. This AC signal is sent to amplifiers and recording equipment.\n\nMICROPHONE vs LOUDSPEAKER:\nLoudspeaker: AC in → coil vibrates → sound (motor effect).\nMicrophone: sound → coil vibrates → AC out (generator effect).\nThey are both electromagnetic transducers — one is the reverse of the other.",
    "heading": "How Microphones Work"
  },
  {
    "content": "CONDENSER (CAPACITOR) MICROPHONE:\nUses a thin conductive diaphragm very close to a fixed backplate (forming a capacitor).\nSound waves vibrate diaphragm → capacitance changes → voltage changes → electrical signal.\nRequires power supply (phantom power from the mixer).\nVery sensitive, wide frequency response — used in recording studios.\n\nRIBBON MICROPHONE:\nA thin metal ribbon suspended between magnets.\nSound waves vibrate the ribbon → ribbon cuts field lines → induced emf.\nWarm, natural sound — used in broadcasting and music recording.\n\nELECTRET MICROPHONE:\nSmall, cheap condenser microphone with permanently charged material.\nUsed in phones, computers, headsets.\n\nFACTORS AFFECTING MICROPHONE QUALITY:\nFrequency response: how evenly it responds across all audible frequencies.\nSensitivity: how much output voltage for a given sound level.\nNoise floor: self-generated noise — lower is better.\nDirectional pattern: omnidirectional, cardioid, bidirectional.",
    "heading": "Types of Microphones"
  },
  {
    "content": "MICROPHONE OUTPUT:\nVery small AC voltage — millivolts level.\nMust be amplified before use.\nPre-amplifier (preamp) boosts the signal.\n\nDIGITAL RECORDING:\nAnalogue signal from microphone → analogue-to-digital converter (ADC).\nSampled at high rate (44,100 times per second for CD quality).\nEach sample converted to a binary number.\nBinary data stored on digital media.\n\nSIGNAL CHAIN:\nSound source → microphone → preamp → ADC → digital processing → storage/transmission.\n\nCONNECTION TO PHYSICS:\nMicrophones demonstrate that electromagnetic induction works in both directions:\nCurrent in magnetic field → motion (motor effect) = loudspeaker.\nMotion in magnetic field → current (generator effect) = microphone.\nEinstein's principle of symmetry — if one works, the reverse also works.",
    "heading": "Signal Processing"
  }
]
```

## higher

HT only — describe how a dynamic microphone uses the generator effect to convert sound to electrical signals. Compare with the motor effect in loudspeakers. Explain why the induced current has the same frequency as the sound.

## common_mistake

A microphone uses the GENERATOR EFFECT (motion → current), not the motor effect. A loudspeaker uses the MOTOR EFFECT (current → motion). They are exact reverses of each other. The frequency of the induced AC from a microphone equals the frequency of the sound waves hitting the diaphragm.

## key_note

Dynamic microphone: sound → diaphragm vibrates → coil in magnetic field → generator effect → AC signal at same frequency as sound. Reverse of loudspeaker. Condenser: capacitance change method. Output: small AC (millivolts) → needs amplification. Both microphone and loudspeaker are electromagnetic transducers.

## matching
```json
{
  "instruction": "Match each device to the energy conversion and physical principle.",
  "pairs": [
    [
      "Loudspeaker",
      "Electrical energy → sound — AC current drives coil by motor effect → cone vibrates"
    ],
    [
      "Dynamic microphone",
      "Sound → electrical energy — sound vibrates coil in magnetic field → generator effect → AC"
    ],
    [
      "Both",
      "Use a coil of wire moving in a permanent magnetic field"
    ],
    [
      "Condenser microphone",
      "Sound changes capacitance of diaphragm-backplate gap → voltage signal"
    ]
  ],
  "title": "Microphone vs Loudspeaker"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Microphone: sound moves the coil → generator effect → AC output. Loudspeaker: AC input → motor effect → coil moves cone → sound. They are exact reverses.",
        true
      ],
      [
        "Microphone has a smaller coil than a loudspeaker — smaller coils detect sound, larger coils produce it",
        false
      ],
      [
        "Loudspeaker uses AC while microphone uses DC — different current types for different functions",
        false
      ],
      [
        "Microphone uses the motor effect to detect sound — the force on the diaphragm is measured",
        false
      ]
    ],
    "q": "A dynamic microphone and a loudspeaker have similar construction. How does their operation differ?",
    "wrong_explanations": {
      "1": "Size differs for practical reasons — but the principle difference is MOTOR EFFECT (loudspeaker) vs GENERATOR EFFECT (microphone).",
      "2": "Both microphones and loudspeakers deal with AC signals — microphone output IS AC at the sound frequency.",
      "3": "The microphone uses the GENERATOR EFFECT — sound moves the coil, inducing current — not the motor effect."
    }
  },
  {
    "opts": [
      [
        "440 Hz — the coil vibrates at 440 Hz (driven by the sound wave) so the induced current alternates at 440 Hz",
        true
      ],
      [
        "880 Hz — the frequency doubles due to electromagnetic induction",
        false
      ],
      [
        "220 Hz — the frequency halves as mechanical vibration converts to electrical",
        false
      ],
      [
        "50 Hz — AC output is always at mains frequency regardless of sound frequency",
        false
      ]
    ],
    "q": "What frequency is the AC output from a microphone when someone sings a note at 440 Hz?",
    "wrong_explanations": {
      "1": "Frequency doesn't double — the coil vibrates at exactly the same rate as the sound wave, so the induced current frequency matches.",
      "2": "Frequency halves — the coil vibrates at the same rate as the sound, inducing AC at the same frequency.",
      "3": "AC output frequency matches the input sound frequency — 50 Hz would mean all sounds come out at the same frequency regardless of pitch."
    }
  }
]
```
