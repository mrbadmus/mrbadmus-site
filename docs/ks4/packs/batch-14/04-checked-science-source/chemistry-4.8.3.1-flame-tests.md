# Flame Tests  (Chemistry, AQA 4.8.3.1)

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Flame tests identify some metal ions; five colours (crimson, yellow, lilac, orange-red, green) (th1, common_mistake, key_note, q1) | triple | 8462 4.8.3.1 (chemistry only) |
| Method: clean nichrome loop, dip, flame (th1) | triple | 8462 4.8.3.1; RP7 |
| Mixtures: colours masked; sodium masks potassium (th2, q2) | triple | 8462 4.8.3.1 |
| FES and advantages of instrumental methods (th3) | triple (base within Triple; owned by `instrumental-methods`, FT-F4) | 8462 4.8.3.6–4.8.3.7 |
| Electron excitation explanation (th2, `higher`) | not a layer, off-spec (FT-F3) | — |
| `rp` | triple. **Chemistry RP7**, not "RP Chemistry 4" (FT-F1) | 8462 4.8.3.5, §8.2.7 |

True page routes: TF TH (whole lesson triple, no HT layer). Matches what the site ships.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Identify metal ions using flame tests and describe the colours produced by each metal.

## theory
```json
[
  {
    "content": "FLAME TESTS identify metal ions by the characteristic colour they produce when heated in a flame.\n\nMETHOD:\n1. Clean a nichrome wire loop with hydrochloric acid and hold in a blue Bunsen flame until no colour is imparted.\n2. Dip the clean loop into the sample (solution or solid).\n3. Hold the loop in the edge of the blue flame.\n4. Observe the flame colour.\n\nFLAME COLOURS:\nLithium (Li⁺): crimson/red\nSodium (Na⁺): yellow/orange — even tiny traces give a strong yellow colour\nPotassium (K⁺): lilac/purple\nCalcium (Ca²⁺): orange-red\nCopper (Cu²⁺): green/blue-green\n\nMemory: Li-Criminal, Na-Yellow, K-Lilac, Ca-Orange-Red, Cu-Green",
    "heading": "Flame Tests — Identifying Metal Ions"
  },
  {
    "content": "WHY FLAME TESTS WORK:\nMetal ions absorb energy from the flame.\nElectrons are excited to higher energy levels.\nAs electrons fall back to lower levels, they emit light at specific wavelengths (colours).\nDifferent metals have different energy level spacings → different coloured light.\n\nIDENTIFYING MIXTURES:\nSodium gives a strong yellow colour that can mask other colours.\nIf sodium is present — its yellow can obscure potassium's lilac.\nSpectroscopy (more precise) can separate colours in a mixture.\n\nLIMITATIONS:\nSome colours look similar (e.g. lithium crimson vs calcium orange-red can be confused).\nSodium contamination is common — masks other colours.\nFlame tests only identify certain cations — cannot detect anions.\nMore precise identification requires instrumental methods.\n\nRPCHEM 4: Identify metal ions using flame tests and other tests in this section.",
    "heading": "Interpreting Flame Test Results"
  },
  {
    "content": "FLAME EMISSION SPECTROSCOPY gives a more precise identification:\nSample atomised and passed through a flame.\nEmitted light passed through a prism/diffraction grating.\nWavelength of light measured precisely.\nEach metal gives a unique pattern of spectral lines.\n\nADVANTAGES over visual flame tests:\nMore precise — can identify multiple ions in a mixture.\nQuantitative — can measure concentration, not just presence.\nMore sensitive — detects trace amounts.\nMore objective — doesn't rely on human colour perception.\n\nThis links to the 4.8.3.7 Flame emission spectroscopy section.",
    "heading": "Using Instrumental Analysis"
  }
]
```

## higher

Explain flame test colours in terms of electron excitation and emission at characteristic wavelengths. Relate the wavelength of emitted light to the energy gap between electron levels. Explain why flame emission spectroscopy is more quantitative and precise than visual flame tests.

## common_mistake

Sodium gives a strong YELLOW/ORANGE colour — not red. Lithium is CRIMSON/RED — don't confuse lithium and sodium. Potassium is LILAC — not blue or violet. Calcium is ORANGE-RED — can be confused with lithium if not observed carefully. Sodium contamination is the most common problem in flame tests.

## key_note

Flame test colours: Li = crimson, Na = yellow/orange, K = lilac, Ca = orange-red, Cu = green. Method: clean nichrome wire, dip in sample, observe flame. Sodium masks other colours. Explained by electron excitation and emission. More precise: flame emission spectroscopy.

## rp

RP Chemistry 4 (chemistry-only) — Identify the ions in an unknown compound. Includes flame tests for metal cations.

## matching
```json
{
  "instruction": "Match each metal ion to its flame test colour.",
  "pairs": [
    [
      "Lithium (Li⁺)",
      "Crimson/red flame"
    ],
    [
      "Sodium (Na⁺)",
      "Yellow/orange flame — even trace amounts give strong colour"
    ],
    [
      "Potassium (K⁺)",
      "Lilac/purple flame"
    ],
    [
      "Calcium (Ca²⁺)",
      "Orange-red flame"
    ],
    [
      "Copper (Cu²⁺)",
      "Green/blue-green flame"
    ]
  ],
  "title": "Flame Test Colours"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Sodium (Na⁺) — sodium gives a strong persistent yellow/orange flame, even in trace amounts",
        true
      ],
      [
        "Potassium (K⁺) — potassium gives a yellow colour like sodium",
        false
      ],
      [
        "Calcium (Ca²⁺) — calcium gives a yellow flame",
        false
      ],
      [
        "Copper (Cu²⁺) — copper burns with an orange colour",
        false
      ]
    ],
    "q": "A flame test on a solution gives a persistent yellow/orange colour. Which ion is most likely present?",
    "wrong_explanations": {
      "1": "Potassium gives LILAC/PURPLE — not yellow. Yellow specifically indicates sodium.",
      "2": "Calcium gives ORANGE-RED — not yellow. These colours are distinct under careful observation.",
      "3": "Copper gives GREEN/BLUE-GREEN — not orange. Orange-red is calcium."
    }
  },
  {
    "opts": [
      [
        "Sodium gives such a strong yellow/orange colour that it masks the lilac colour of potassium, making identification unreliable",
        true
      ],
      [
        "Sodium reacts with potassium in the flame — destroying both ions before they can be detected",
        false
      ],
      [
        "Sodium changes potassium's flame colour from lilac to yellow — giving a false reading",
        false
      ],
      [
        "Potassium and sodium always occur together — if one is present the other always is too",
        false
      ]
    ],
    "q": "Why might sodium contamination cause problems during a flame test for potassium?",
    "wrong_explanations": {
      "1": "Sodium does not chemically react with potassium in a flame test — the problem is optical masking, not chemical reaction.",
      "2": "Sodium doesn't change potassium's emission — both produce their own colours independently. The problem is that sodium's stronger yellow overpowers the weaker lilac.",
      "3": "Sodium and potassium can occur separately — the point is specifically about contamination masking results."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
