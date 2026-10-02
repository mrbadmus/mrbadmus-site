# Pure Substances  (Chemistry, AQA 5.8.1.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Chemical meaning of pure (one element or compound), everyday meaning (th1, common_mistake, key_note, q2) | base | 8464 5.8.1.1 / 8462 4.8.1.1 |
| Pure: specific mp/bp; mixture: over a range; use mp/bp data to tell pure from impure (th1, th2, key_note, q1) | base | 8464 5.8.1.1 / 8462 4.8.1.1 |
| Impurity lowers mp / raises bp (th1, key_note) | base detail beyond the spec; bp clause imprecise (PS-F1) | — |
| Purity in context (th3) | base context; thalidomide line off-spec (PS-F2) | — |
| `higher` field | not a layer: no HT statement in 5.8.1.1; data comparison is base, lattice mechanism off-spec (PS-F3) | 8464 5.8.1.1 |

True page routes: CF CH TF TH, all base (no HT or triple layer). Matches what the site ships.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Define a pure substance in chemistry and use melting/boiling point data to assess purity.

## theory
```json
[
  {
    "content": "In everyday language, 'pure' might mean clean or natural (e.g. 'pure orange juice').\n\nIn CHEMISTRY, a PURE SUBSTANCE has a precise meaning:\nA pure substance contains only ONE type of element or compound — nothing else mixed in.\nA pure substance has FIXED, SHARP melting and boiling points.\n\nExamples:\nPure water: boils at exactly 100°C, melts at exactly 0°C (at standard pressure).\nPure iron: melts at exactly 1538°C.\nPure ethanol: boils at exactly 78.4°C.\n\nIMPURE substances (mixtures):\nMelt and boil over a RANGE of temperatures — not at a fixed point.\nMelting point is LOWER than that of the pure substance (melting point depression).\nBoiling point is HIGHER than that of the pure substance (boiling point elevation).\n\nThis gives chemists a way to test purity.",
    "heading": "What is a Pure Substance in Chemistry?"
  },
  {
    "content": "MELTING POINT TEST:\nHeat a small sample slowly and record the temperature at which it starts and finishes melting.\n\nPURE substance: melts at a SHARP, PRECISE temperature — starts and finishes at the same temperature.\nExample: pure aspirin melts at exactly 135°C.\n\nIMPURE substance: melts over a RANGE of temperatures — starts melting below the expected temperature.\nExample: aspirin with impurity might melt from 128°C to 133°C.\n\nBOILING POINT TEST:\nPure substance: boils at a fixed temperature throughout.\nMixture: temperature changes during boiling as components evaporate at different rates.\n\nIDENTIFYING SUBSTANCES:\nComparing measured melting/boiling point to known data tables identifies the substance.\nA substance that melts at 135°C and matches pure aspirin data → likely aspirin.\n\nThis method is simple, quick and requires only a small sample — very useful in organic chemistry.",
    "heading": "Using Melting and Boiling Points to Test Purity"
  },
  {
    "content": "PHARMACEUTICAL PURITY:\nMedicines must be extremely pure — even tiny impurities could be toxic or reduce effectiveness.\nThalidomide showed how critically purity (and stereochemistry) matters — one form was therapeutic, another caused birth defects.\n\nFOOD PURITY:\nFood standards require ingredients at specific purities.\nSugar (sucrose) in food must meet purity standards — impurities affect flavour and safety.\n\nINDUSTRIAL PURITY:\nSome industrial processes require specific purity levels.\nSemiconductors (silicon chips) need extremely high purity silicon — impurities disrupt electrical properties.\n\nCHEMICAL ANALYSIS:\nChemists use melting and boiling points alongside other techniques (chromatography, spectroscopy) to confirm identity and purity of compounds.",
    "heading": "Purity in Context"
  }
]
```

## higher

Melting point depression: impurities disrupt lattice, requiring less energy to melt, lowering MP and broadening the range. Use melting point data to assess purity quantitatively. Compare measured values with data table values. Understand the role of melting point in pharmaceutical quality control.

## common_mistake

In chemistry, 'pure' does NOT mean natural or healthy — it means containing only ONE substance with no impurities. A mixture of two pure chemicals is NOT a pure substance. Orange juice (even 100% natural) is a MIXTURE — not a pure substance in the chemical sense.

## key_note

Pure substance: one element or compound only — sharp fixed melting and boiling points. Impure (mixture): melts/boils over a range of temperatures. Impurity lowers melting point and raises boiling point. Use melting/boiling point data to identify substances and test purity.

## matching
```json
{
  "instruction": "Match each observation to pure substance or impure mixture.",
  "pairs": [
    [
      "Pure substance",
      "Melts at exactly one temperature — sharp melting point"
    ],
    [
      "Impure mixture",
      "Melts over a range of temperatures — starts below expected melting point"
    ],
    [
      "Pure substance",
      "Boils at a constant temperature throughout"
    ],
    [
      "Impure mixture",
      "Boiling point higher than expected for the pure substance"
    ],
    [
      "Pure substance",
      "Has a fixed composition — contains only one type of compound"
    ]
  ],
  "title": "Pure or Impure?"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "The sample is impure — impurities lower the melting point and cause it to melt over a range",
        true
      ],
      [
        "The sample is a different compound with a lower melting point",
        false
      ],
      [
        "The student heated it too quickly — this is a measurement error only",
        false
      ],
      [
        "The sample is pure but at a different pressure",
        false
      ]
    ],
    "q": "A student heats a solid and records that it melts between 118°C and 125°C. Pure samples of this compound melt at 135°C. What does this suggest?",
    "wrong_explanations": {
      "1": "It could be a different compound — but the wider context of the question (testing purity of a sample) suggests the most likely explanation is impurity.",
      "2": "Rapid heating can cause errors, but both a lower AND a range of melting temperatures strongly suggest impurity — not just measurement error.",
      "3": "Standard lab conditions are at atmospheric pressure — pressure effects on melting points are negligible without extreme pressure changes."
    }
  },
  {
    "opts": [
      [
        "It is a mixture of water, sugars, vitamins, acids and many other compounds — not a single element or compound",
        true
      ],
      [
        "Orange juice contains preservatives — these impurities make it impure",
        false
      ],
      [
        "It has not been distilled — only distilled liquids can be pure",
        false
      ],
      [
        "Orange juice changes colour — pure substances do not change colour",
        false
      ]
    ],
    "q": "Why is 'pure orange juice' not a pure substance in the chemical sense?",
    "wrong_explanations": {
      "1": "Even 'pure' orange juice without added preservatives contains many dissolved compounds — it is always a mixture.",
      "2": "Distillation is one way to purify a liquid but is not the definition of purity — a single compound that has never been distilled can still be chemically pure.",
      "3": "Many pure substances change colour (e.g. copper sulfate changing from blue hydrated to white anhydrous on heating)."
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
