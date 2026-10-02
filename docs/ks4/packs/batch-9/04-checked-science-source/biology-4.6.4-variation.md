# Variation  (Biology, AQA 4.6.4)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Variation; raw material for natural selection (theory 1) | base | 8464 4.6.2.1; 4.6 intro |
| Continuous / discontinuous (theory 1; key_note) | not in spec (KS3) | — |
| Genetic, environmental, both (theory 2; common_mistake) | base | 8464 4.6.2.1; 8461 4.6.2.1 |
| Mutation: change in base sequence; effects (theory 3; key_note) | base — th3's last sentence is WRONG (VAR-F1) | 8464 4.6.2.1 |
| `higher`: mutagens, synonymous codons | not in spec (4.6.2.1 has no HT) | — |
| quiz q1 | base — wx2 contradicts inherited-disorders, do not use as written | 8464 4.6.2.1 |
| quiz q2 | not in spec (continuous/discontinuous) | — |
| quiz q3 | base | 8464 4.6.2.1 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches; the `higher` field carries no real HT content — flagged VAR-F2.

## Spec core missing from the frozen data (written from the spec, examiner)
8464 4.6.2.1 = 8461 4.6.2.1, verbatim:

> "Students should be able to describe simply how the genome and its interaction with the environment influence the development of the phenotype of an organism."
> "Students should be able to: • state that there is usually extensive genetic variation within a population of a species • recall that all variants arise from mutations and that: most have no effect on the phenotype; some influence phenotype; very few determine phenotype."
> "Mutations occur continuously. Very rarely a mutation will lead to a new phenotype. If the new phenotype is suited to an environmental change it can lead to a relatively rapid change in the species."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the causes of variation and distinguish between genetic, environmental and combination variation.

## theory
```json
[
  {
    "content": "VARIATION refers to the differences in characteristics between individuals of the same species.\n\nVariation is absolutely essential for life on Earth:\nIt is the raw material on which NATURAL SELECTION acts.\nWithout variation, all individuals would be identical and no evolutionary change would be possible.\nVariation allows populations to adapt to changing environments.\n\nVariation can be:\nCONTINUOUS — characteristics that show a range of values with no distinct categories (e.g. height, weight, skin colour).\nDISCONTINUOUS — characteristics that fall into distinct categories with no in-between values (e.g. blood group A, B, AB or O; tongue rolling ability; ability to taste PTC).",
    "heading": "What is Variation?"
  },
  {
    "content": "Variation arises from three main sources:\n\n1. GENETIC VARIATION:\nDifferences in DNA sequences between individuals.\nArises through: MUTATIONS (random changes in DNA sequence), MEIOSIS (shuffling of chromosomes and crossing over), SEXUAL REPRODUCTION (combining DNA from two parents).\nGenetic variation is INHERITED — passed from parents to offspring.\n\n2. ENVIRONMENTAL VARIATION:\nDifferences caused by conditions an organism experiences during its lifetime.\nExamples: height (affected by nutrition during childhood), skin colour (affected by sun exposure), language spoken (learned from environment), scars and injuries.\nEnvironmental variation is NOT inherited — you cannot pass on a learned language or a scar to your offspring.\n\n3. COMBINATION OF BOTH:\nMany characteristics are influenced by BOTH genes AND environment.\nExamples: height (genes set the potential maximum; nutrition determines whether that potential is reached), body weight (genes influence metabolism; diet and exercise are environmental), skin colour (genes determine base colour; UV exposure adds a tan).",
    "heading": "Causes of Variation"
  },
  {
    "content": "A MUTATION is a change in the sequence of DNA bases in a gene or chromosome.\n\nMutations can be:\nSpontaneous — occurring randomly during DNA replication (copying errors).\nInduced — caused by MUTAGENS: chemicals (e.g. carcinogens in tobacco smoke), radiation (UV, gamma rays, X-rays), certain viruses.\n\nEffects of mutations:\nMost mutations are NEUTRAL — they occur in non-coding DNA or don't change the protein significantly.\nSome mutations are HARMFUL — they alter a protein so it cannot function properly (e.g. mutations causing cystic fibrosis, sickle cell disease).\nVery occasionally, a mutation is BENEFICIAL — it improves the function of a protein or produces a new useful function (e.g. mutations that gave early humans more efficient enzymes or better immune responses).\n\nBeneficial mutations are the ultimate source of all new variation in a species — they are the raw material on which natural selection acts.",
    "heading": "Mutations"
  }
]
```

## higher

Mutagens increase the frequency of mutations: UV radiation, ionising radiation (gamma rays, X-rays), certain chemicals (e.g. carcinogens in tobacco smoke). Most mutations are neutral (affect non-coding DNA or produce synonymous codons — same amino acid). The rare beneficial mutation is the raw material for natural selection and evolution. Students should understand that natural selection acts on existing variation — it cannot produce new alleles on demand.

## common_mistake

Environmental variation is NOT inherited — you cannot pass your experiences, injuries or learned skills to your children through DNA. Genetic variation IS inherited. Most mutations are neutral — not harmful. Students often assume all mutations are dangerous, but the vast majority have no detectable effect.

## key_note

Variation: continuous (range of values) or discontinuous (distinct categories). Causes: genetic (mutation, meiosis, sexual reproduction), environmental (nutrition, sun, learned). Many traits = combination of both. Mutations: neutral, harmful or rarely beneficial.

## matching
```json
{
  "instruction": "Match each example to the cause of variation.",
  "pairs": [
    [
      "Genetic",
      "Blood group — determined entirely by inherited alleles"
    ],
    [
      "Environmental",
      "A scar from a childhood accident — not passed to offspring"
    ],
    [
      "Both",
      "Height — genes set the maximum potential; nutrition determines if it is reached"
    ],
    [
      "Environmental",
      "Language spoken — entirely learned from the surrounding environment"
    ],
    [
      "Genetic",
      "Cystic fibrosis — caused by inheriting two copies of the recessive allele"
    ],
    [
      "Both",
      "Body weight — metabolic rate is genetic; diet and exercise are environmental"
    ]
  ],
  "title": "Genetic, Environmental or Both?"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "A combination of genetic potential and favourable environmental factors — e.g. excellent nutrition during childhood",
        true
      ],
      [
        "A mutation that occurred during development, making the child taller",
        false
      ],
      [
        "The child inherited more height genes from distant ancestors than from parents",
        false
      ],
      [
        "Environmental factors alone — height is entirely determined by diet",
        false
      ]
    ],
    "q": "A child is taller than expected given their parents' heights. What is the most likely cause?",
    "wrong_explanations": {
      "1": "A random mutation could theoretically increase height, but this is rare. The more likely explanation is that parents didn't reach their own genetic potential due to environmental factors.",
      "2": "Genes don't skip generations in this simple way — the child can only inherit alleles from their parents.",
      "3": "Height is strongly influenced by genetics — children of tall parents tend to be taller. But environmental factors (particularly nutrition) also play a significant role."
    }
  },
  {
    "opts": [
      [
        "Blood group — a person is type A, B, AB or O with no intermediate values",
        true
      ],
      [
        "Height — people range from very short to very tall with all values in between",
        false
      ],
      [
        "Body weight — a continuous range from very light to very heavy",
        false
      ],
      [
        "Skin colour — a continuous range from very light to very dark",
        false
      ]
    ],
    "q": "Which of the following is an example of DISCONTINUOUS variation?",
    "wrong_explanations": {
      "1": "Height is a classic example of CONTINUOUS variation — there is a smooth range from shortest to tallest with all intermediate heights present.",
      "2": "Body weight is CONTINUOUS — it forms a normal distribution curve across the population.",
      "3": "Skin colour is CONTINUOUS — determined by multiple genes and environmental factors (sun exposure), producing a smooth range of values."
    }
  },
  {
    "opts": [
      [
        "A change in the sequence of DNA bases — can be neutral, harmful or rarely beneficial",
        true
      ],
      [
        "A change in an organism's body caused by the environment during its lifetime",
        false
      ],
      [
        "The process of chromosomes being shuffled during meiosis",
        false
      ],
      [
        "A genetic disease inherited from parents",
        false
      ]
    ],
    "q": "What is a mutation?",
    "wrong_explanations": {
      "1": "Environmental changes to the body (like a tan or muscle growth) are not mutations — they are phenotypic responses that are not passed on through DNA.",
      "2": "Chromosome shuffling during meiosis = INDEPENDENT ASSORTMENT and CROSSING OVER — these create variation but are not mutations.",
      "3": "Inherited diseases are caused by specific alleles — mutations can create new alleles, but the inherited disease itself is not a mutation."
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
