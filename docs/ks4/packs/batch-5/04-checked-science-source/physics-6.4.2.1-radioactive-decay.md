# Radioactive Decay and Nuclear Radiation  (Physics, AQA 6.4.2.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Unstable nuclei; random decay; activity (Bq); count-rate (GM tube) (T1; q2) | base | 8464 6.4.2.1; 8463 4.4.2.1 |
| α, β, γ (and neutron — missing) emitted; composition (T1, T2) | base | 8464 6.4.2.1 |
| Penetration, range in air, ionising power (T2; common_mistake; key_note; q1) | base | 8464 6.4.2.1 |
| Uses: smoke detector (α), thickness gauge (β), sterilising (γ); choosing the best source (T3) | base | 8464 6.4.2.1 ("apply … to the uses of radiation") |
| Medical uses: exploring internal organs (gamma imaging), destroying unwanted tissue (radiotherapy) (T3; key_note) | triple | 8463 4.4.3.3 (physics only) |
| Ionising radiation damages cells; alpha inside vs gamma outside the body; precautions (T3; q1) | base | 8464 6.4.2.1, 6.4.2.4 |

True page routes: CF CH TF TH; medical uses are a triple layer (TF TH) — or left to the site's `uses-of-nuclear-radiation` lesson. Site currently ships the medical uses on every route; flagged (`_flags/radioactive-decay.md` F4).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe alpha, beta and gamma radiation, their properties and uses and dangers.

## theory
```json
[
  {
    "content": "Some atomic nuclei are UNSTABLE — they spontaneously emit radiation to become more stable.\nThis is RADIOACTIVE DECAY — a RANDOM process (cannot predict exactly when any nucleus will decay).\n\nACTIVITY: the rate at which a source decays — measured in BECQUEREL (Bq).\n1 Bq = 1 decay per second.\n\nCOUNT RATE: decays recorded per second by a detector (e.g. Geiger-Müller tube).\n\nThree main types of nuclear radiation:\nALPHA (α) — helium nucleus (2 protons + 2 neutrons)\nBETA (β) — fast electron from the nucleus\nGAMMA (γ) — high-energy electromagnetic wave",
    "heading": "Radioactive Decay"
  },
  {
    "content": "ALPHA (α):\nComposition: 2 protons + 2 neutrons (helium-4 nucleus, ⁴₂He)\nCharge: +2\nMass: 4 amu\nRange in air: a few centimetres\nPenetration: stopped by a few cm of air, or paper, or skin\nIonisation: STRONGLY ionising — causes most damage to nearby cells\n\nBETA (β):\nComposition: fast-moving electron (⁰₋₁e)\nCharge: −1\nMass: negligible\nRange in air: a few metres\nPenetration: stopped by a few mm of aluminium\nIonisation: moderately ionising\n\nGAMMA (γ):\nComposition: high-energy electromagnetic wave (photon)\nCharge: 0\nMass: 0\nRange in air: effectively unlimited\nPenetration: reduced by several cm of lead or metres of concrete\nIonisation: weakly ionising per unit path\n\nDETECTION: Geiger-Müller tube connected to a counter.",
    "heading": "Properties of Alpha, Beta and Gamma"
  },
  {
    "content": "USES:\nALPHA — smoke detectors: alpha source ionises air → current flows → alarm triggers when smoke absorbs alpha and current drops.\nBETA — paper thickness monitoring: beta passes through paper; more absorbed = thicker paper → adjust rollers.\nGAMMA — medical imaging (gamma cameras), cancer treatment (radiotherapy), sterilising medical equipment, food irradiation.\nGAMMA/BETA — industrial thickness gauges, pipeline fault detection.\n\nDANGERS:\nAll ionising radiation damages living cells by ionising molecules in DNA → mutations → cancer.\nHIGH DOSE → cell death → radiation sickness.\nALPHA: most dangerous INSIDE the body (highly ionising, can't escape). Safe outside the body (stopped by skin).\nGAMMA: most dangerous OUTSIDE the body (penetrates to internal organs). Less ionising per path length.\nBETA: intermediate — penetrates skin, absorbed by soft tissue.\n\nPROTECTION:\nDistance — inverse square law applies (intensity decreases with distance).\nShielding — appropriate materials (paper for alpha, aluminium for beta, lead for gamma).\nTime — minimise exposure duration.\nMonitoring — dosimeters worn by radiation workers.",
    "heading": "Uses and Dangers of Nuclear Radiation"
  }
]
```

## common_mistake

Alpha is the MOST ionising but LEAST penetrating. Gamma is the LEAST ionising per path length but MOST penetrating. These are often confused. Alpha is most dangerous INSIDE the body; gamma is most dangerous OUTSIDE the body.

## key_note

α: helium nucleus (+2), stopped by paper, most ionising. β: fast electron (−1), stopped by aluminium, moderate. γ: EM wave (0 charge), needs lead/concrete, least ionising per path. Activity in Bq. Decay is random. Uses: smoke detectors (α), thickness gauges (β), cancer treatment/sterilisation (γ).

## matching
```json
{
  "instruction": "Match each radiation type to its composition, penetration and use.",
  "pairs": [
    [
      "Alpha (α)",
      "Helium nucleus — stopped by paper — used in smoke detectors"
    ],
    [
      "Beta (β)",
      "Fast electron — stopped by aluminium — used in paper thickness monitoring"
    ],
    [
      "Gamma (γ)",
      "EM wave — needs lead/concrete — used in cancer radiotherapy and sterilisation"
    ],
    [
      "Most ionising",
      "Alpha radiation — causes most ion pairs per cm of path"
    ],
    [
      "Most penetrating",
      "Gamma radiation — passes through most materials, needs lead/concrete shielding"
    ]
  ],
  "title": "Radiation Properties"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Alpha is highly ionising — it causes dense ionisation damage to nearby cells and cannot escape the body to be detected",
        true
      ],
      [
        "Alpha has the highest energy of all three types — more energy means more damage",
        false
      ],
      [
        "Alpha moves fastest — it collides more often with cells",
        false
      ],
      [
        "Alpha is most penetrating — it reaches all organs from a single source",
        false
      ]
    ],
    "q": "Why is alpha radiation the most dangerous type when a source is inside the body?",
    "wrong_explanations": {
      "1": "Alpha does not have the highest energy — gamma photons have very high energies too. The danger is from DENSE IONISATION in a small area.",
      "2": "Alpha is actually the SLOWEST of the three — and its high mass means it interacts strongly with matter.",
      "3": "Alpha is the LEAST penetrating — stopped by a few cm of air. That's exactly why it's so dangerous inside the body — all ionisation is deposited nearby."
    }
  },
  {
    "opts": [
      [
        "340 nuclei in the source are decaying every second, each emitting radiation",
        true
      ],
      [
        "The source has 340 radioactive atoms remaining in total",
        false
      ],
      [
        "The source emits 340 joules of energy every second",
        false
      ],
      [
        "The source has been decaying for 340 seconds",
        false
      ]
    ],
    "q": "A Geiger counter measures 340 Bq from a radioactive source. What does this mean?",
    "wrong_explanations": {
      "1": "Activity = total number of radioactive atoms remaining, not the rate. Bq measures the RATE of decay (per second).",
      "2": "Bq measures rate in decays per second — not joules. Energy per decay is measured in eV or joules, not Bq.",
      "3": "Bq is a rate (per second) — not a duration."
    }
  }
]
```
