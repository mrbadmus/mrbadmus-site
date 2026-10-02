# Loudspeakers and Headphones  (Physics, AQA 6.7.2.4 (HT only, physics only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
True spec reference: **8463 4.7.2.4 Loudspeakers (physics only) (HT only)**; no 8464 equivalent. The `spec` field "6.7.2.4" is the site's internal number.

| point | layer | spec ref |
|---|---|---|
| Motor effect drives the coil and cone; AC reverses the force; cone vibrates → pressure variations (theory 1; common_mistake; key_note; `higher`) | triple-higher | 8463 4.7.2.4 |
| Sound frequency = AC frequency; bigger current → louder (theory 1) | triple-higher | 8463 4.7.2.4 |
| Moving-coil headphones, same principle (theory 2, first lines) | triple-higher | 8463 4.7.2.4 |
| Electrostatic / balanced-armature headphones, impedance (theory 2) | not in spec — F2 | — |
| Energy chain, efficiency, woofer/tweeter (theory 3) | not in spec (context) — F1, F2 | — |
| quiz q1, q2 | triple-higher — both usable | 8463 4.7.2.4 |

True page routes: TH. Site currently ships: TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how loudspeakers and headphones use the motor effect to produce sound.

## theory
```json
[
  {
    "content": "A LOUDSPEAKER converts electrical energy (alternating current) into sound energy using the MOTOR EFFECT.\n\nCOMPONENTS:\nPERMANENT MAGNET: provides a strong, constant magnetic field.\nVOICE COIL: a coil of wire attached to the cone.\nCONE (DIAPHRAGM): large paper or plastic surface that moves air to create sound.\n\nOPERATION:\n1. Alternating current (from amplifier) flows through the voice coil.\n2. Voice coil is in the field of the permanent magnet → motor effect.\n3. AC reverses direction → force reverses direction → coil moves back and forth.\n4. Coil attached to cone → cone vibrates in and out.\n5. Vibrating cone pushes and pulls air → creates compressions and rarefactions → SOUND WAVES.\n\nFREQUENCY OF SOUND = frequency of the alternating current.\nAMPLITUDE (loudness) ∝ amplitude of current (larger current → larger force → bigger vibrations → louder sound).",
    "heading": "How Loudspeakers Work"
  },
  {
    "content": "HEADPHONES work on the same principle as loudspeakers but are miniaturised.\n\nSimilar construction: permanent magnet + voice coil + small diaphragm.\nThe smaller diaphragm moves the smaller volume of air needed for in-ear listening.\n\nELECTROSTATIC HEADPHONES (high-end):\nUse electrostatic force instead of motor effect.\nA thin membrane between two charged plates.\nAlternating voltage changes force → membrane vibrates → sound.\nVery low distortion — expensive.\n\nBALANCED ARMATURE (in-ear monitors):\nA small armature (iron bar) is balanced between magnets.\nAlternating current through a coil unbalances the armature → vibrates → moves diaphragm.\nVery efficient — used in hearing aids and professional in-ear monitors.\n\nIMPEDANCE MATCHING:\nDifferent headphones have different electrical resistance (impedance).\nHigh-impedance: require amplifier, better for home use.\nLow-impedance: work directly from phones, more common.",
    "heading": "Headphones"
  },
  {
    "content": "ENERGY TRANSFER IN A LOUDSPEAKER:\nElectrical energy (from amplifier) → kinetic energy (voice coil moving) → sound energy (sound waves).\nInefficiencies: some electrical energy → thermal energy (resistance heating of coil).\nTypical efficiency: 1–5% for most loudspeakers (most energy wasted as heat).\n\nFACTORS AFFECTING SOUND QUALITY:\nFrequency response: good loudspeakers reproduce a wide range of frequencies equally well.\nDistortion: non-linear movement of cone → distorted sound.\nBasic loudspeakers struggle with very low (bass) and very high (treble) frequencies.\n\nDESIGN FOR DIFFERENT FREQUENCIES:\nWOOFER: large cone → moves large volume of air → good for low frequencies (bass).\nTWEETER: small cone → moves quickly → good for high frequencies (treble).\nFULL-RANGE SPEAKER: compromise design.\nSUBWOOFER: very large driver specifically for very low frequencies (<200 Hz).",
    "heading": "Energy Transfers in Loudspeakers"
  }
]
```

## higher

HT only — describe how the motor effect drives a loudspeaker. Explain why alternating current is needed. Relate the frequency and amplitude of the AC signal to the properties of the sound produced.

## common_mistake

The cone of a loudspeaker is driven by the MOTOR EFFECT — the force on a current-carrying conductor in a magnetic field. The alternating current changes direction, so the force changes direction, making the cone move in and out. The frequency of sound produced equals the frequency of the AC signal.

## key_note

Loudspeaker: AC through voice coil in permanent magnet field → motor effect → cone vibrates → sound. AC frequency = sound frequency. Amplitude of current → loudness. Headphones: same principle, miniaturised. Energy: electrical → kinetic → sound (with some thermal losses).

## matching
```json
{
  "instruction": "Match each component to its role in a loudspeaker.",
  "pairs": [
    [
      "Permanent magnet",
      "Provides constant magnetic field in which the voice coil experiences a force"
    ],
    [
      "Voice coil",
      "Carries the AC signal — force from motor effect drives it back and forth"
    ],
    [
      "Cone (diaphragm)",
      "Attached to coil — vibrates to push and pull air, creating sound waves"
    ],
    [
      "Frequency of AC",
      "Determines the frequency (pitch) of the sound produced"
    ]
  ],
  "title": "Loudspeaker Operation"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "DC produces a constant force in one direction — the cone would deflect once and stop. AC reverses direction, reversing the force, making the cone vibrate and produce sound.",
        true
      ],
      [
        "AC provides more power than DC — louder sound is produced",
        false
      ],
      [
        "DC would destroy the voice coil due to overheating — AC protects it",
        false
      ],
      [
        "AC matches the natural frequency of the cone — DC would cause resonance problems",
        false
      ]
    ],
    "q": "Why must the electrical signal driving a loudspeaker be alternating current (AC)?",
    "wrong_explanations": {
      "1": "AC and DC can provide the same power — the reason for AC is about the DIRECTION of force, not power level.",
      "2": "DC heating is a concern, but the fundamental reason is that DC produces unidirectional force — AC reversal creates oscillation.",
      "3": "Resonance happens at specific frequencies — the loudspeaker is designed to respond to all frequencies, not just one."
    }
  },
  {
    "opts": [
      [
        "Low frequency (low pitch) and large amplitude (loud)",
        true
      ],
      [
        "High frequency (low pitch) and large amplitude (loud)",
        false
      ],
      [
        "Low frequency (low pitch) and small amplitude (loud)",
        false
      ],
      [
        "High frequency (loud) and small amplitude (low pitch)",
        false
      ]
    ],
    "q": "A loudspeaker produces a loud, low-pitched sound. What can you say about the AC signal driving it?",
    "wrong_explanations": {
      "1": "Low pitch = LOW frequency AC — high frequency would produce a high-pitched sound.",
      "2": "Low pitch = low frequency AC; loud = large amplitude — small amplitude produces quiet sound.",
      "3": "Loudness comes from AMPLITUDE of AC (larger current → larger force → bigger vibrations); frequency determines pitch."
    }
  }
]
```
