# Sex Determination  (Biology, AQA 4.6.3.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| 23 pairs; one pair sex chromosomes; XX female, XY male (theory 1; key_note) | base | 8464 4.6.1.6; 8461 4.6.1.8 |
| SRY gene; the term "autosomes" (theory 1) | not in spec — context only | — |
| Eggs all X; sperm X or Y; sperm decides sex (theory 2; common_mistake) | base | 8464 4.6.1.6 |
| Cross XX × XY; 50% probability; ~1:1 ratio (theory 2, 3) | base | 8464 4.6.1.6 (MS 1c, 3a) |
| `higher`: X-linked inheritance | not in spec | — |
| quiz q1 | base | 8464 4.6.1.6 |
| quiz q2 | base — key says "always 50:50", do not use as written | 8464 4.6.1.6 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches; the `higher` field (sex linkage) is off-spec — flagged SEX-F1.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain how biological sex is determined by the X and Y chromosomes.

## theory
```json
[
  {
    "content": "In humans, biological sex is determined by a pair of SEX CHROMOSOMES — one of the 23 pairs of chromosomes.\n\nFEMALES: XX — two X chromosomes.\nMALES: XY — one X chromosome and one Y chromosome.\n\nThe Y chromosome is smaller than the X chromosome and contains fewer genes. It carries the genes responsible for male development, including the SRY gene which triggers the development of testes.\n\nAll other 22 chromosome pairs are called AUTOSOMES — they are the same in males and females.",
    "heading": "Sex Chromosomes"
  },
  {
    "content": "All eggs produced by a female contain ONE X chromosome (since females are XX).\n\nSperm produced by a male contain EITHER:\nan X chromosome (approximately 50% of sperm), OR\na Y chromosome (approximately 50% of sperm).\n\nAt fertilisation:\nIf an X-bearing sperm fertilises the egg: XX → FEMALE.\nIf a Y-bearing sperm fertilises the egg: XY → MALE.\n\nTherefore: the SPERM determines the biological sex of the offspring — not the egg.\n\nProbability: 50% chance of a female child, 50% chance of a male child in each pregnancy.",
    "heading": "How Sex is Determined at Fertilisation"
  },
  {
    "content": "We can use a Punnett square to show sex determination:\n\nMother (XX) × Father (XY)\n\nSperm: X or Y (50/50)\nEggs: X only (100%)\n\nOffspring:\nXX = female (50%)\nXY = male (50%)\n\nThis shows why the sex ratio in human populations is approximately 50:50.\n\nKey point: the sex of a child is determined RANDOMLY at fertilisation — it cannot be predicted in advance for a specific pregnancy. The 50:50 ratio is the probability, not a guarantee for any given family.",
    "heading": "Punnett Square for Sex Determination"
  }
]
```

## higher

Sex-linked (X-linked) inheritance: genes on the X chromosome with no corresponding allele on the Y. Males (XY) have only one X — so any allele on their single X is expressed, even if recessive. This is why X-linked recessive conditions (colour blindness, haemophilia) are more common in males. Females can be carriers — one recessive allele masked by the dominant on the second X. Students should be able to construct and interpret Punnett squares for X-linked inheritance.

## common_mistake

It is the SPERM that determines the sex of the child — not the egg. All eggs contain an X chromosome. Sperm can contain either X or Y. If a Y-carrying sperm fertilises the egg, the child is male (XY). Historically, women were sometimes blamed for not producing sons — this is biologically incorrect.

## key_note

Female = XX. Male = XY. All eggs carry X. Sperm carry X or Y (50/50). Y-sperm → male (XY). X-sperm → female (XX). Sex determined at fertilisation by which sperm fertilises the egg. 50% probability each time.

## matching
```json
{
  "instruction": "Match each statement to the correct sex chromosome fact.",
  "pairs": [
    [
      "Female",
      "Has sex chromosomes XX — both are X chromosomes"
    ],
    [
      "Male",
      "Has sex chromosomes XY — one X and one smaller Y chromosome"
    ],
    [
      "All eggs",
      "Contain one X chromosome — females are XX so can only pass on X"
    ],
    [
      "Sperm",
      "Contain either X or Y — determines the sex of the offspring"
    ],
    [
      "50%",
      "Probability of a male offspring — same as probability of female offspring"
    ]
  ],
  "title": "Sex Determination Match"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Which type of sperm (X or Y) fertilises the egg — Y-sperm → male, X-sperm → female",
        true
      ],
      [
        "The egg — females produce X and Y eggs, one type producing a boy and the other a girl",
        false
      ],
      [
        "The environment during pregnancy — temperature affects sex",
        false
      ],
      [
        "The age of the parents — older parents are more likely to have girls",
        false
      ]
    ],
    "q": "What determines the biological sex of a human offspring?",
    "wrong_explanations": {
      "1": "Females (XX) can only produce X-bearing eggs — all eggs contain X. It is the SPERM that carries either X or Y.",
      "2": "Temperature does affect sex determination in some reptiles — but in humans, sex is determined genetically by which sperm fertilises the egg.",
      "3": "Parental age can affect fertility and some genetic risks — but does not determine sex."
    }
  },
  {
    "opts": [
      [
        "50% — each pregnancy is independent, the sex ratio is always 50:50",
        true
      ],
      [
        "Higher than 50% — after three girls they are 'due' a boy",
        false
      ],
      [
        "Lower than 50% — this couple clearly produce more girls than boys",
        false
      ],
      [
        "0% — if they have had three girls their sperm cannot produce Y chromosomes",
        false
      ]
    ],
    "q": "A couple have three daughters. What is the probability their next child will be a son?",
    "wrong_explanations": {
      "1": "Each pregnancy is INDEPENDENT — like flipping a coin, the outcomes of previous pregnancies have no effect. This is a common misconception known as the gambler's fallacy.",
      "2": "Having three girls does not indicate a bias — small sample sizes often show runs of one outcome by chance. Males produce X and Y sperm equally.",
      "3": "Males always produce roughly 50% X-bearing and 50% Y-bearing sperm — three daughters doesn't change this."
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
