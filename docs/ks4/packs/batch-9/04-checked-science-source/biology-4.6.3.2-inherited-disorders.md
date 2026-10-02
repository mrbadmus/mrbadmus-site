# Inherited Disorders  (Biology, AQA 4.6.3.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Cystic fibrosis: recessive allele, carriers, cell membranes, mucus (theory 1) | base | 8464 4.6.1.5; 8461 4.6.1.7 |
| Polydactyly: dominant allele, extra digits (theory 2) | base | 8464 4.6.1.5; 8461 4.6.1.7 |
| Dominant cannot skip / recessive can skip a generation (theory 2; common_mistake; key_note) | base | 8464 4.6.1.5 + 4.6.1.4 |
| Ethical issues of testing (theory 3) | base | 8464 4.6.1.5 |
| Pre-conception, amniocentesis, CVS, newborn testing (theory 3) | not in spec — context only | — |
| `higher`: embryo screening (PGD), designer babies | base (not HT) | 8464 4.6.1.5; 8461 4.6.1.7 |
| FIFA (constructing Ff × Ff) | higher | 8464 4.6.1.4 (HT only) |
| quiz q1, q2 | base | 8464 4.6.1.5; 8461 4.6.1.7 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches; embryo screening is locked in the `higher` field (CH TH only) though it is base — flagged INH-F1.

## Spec core missing from the frozen data (written from the spec, examiner)
8464 4.6.1.5 = 8461 4.6.1.7, verbatim:

> "Students should make informed judgements about the economic, social and ethical issues concerning embryo screening, given appropriate information."
> (WS 1.3) "Appreciate that embryo screening and gene therapy may alleviate suffering but consider the ethical issues which arise."
> "Cystic fibrosis (a disorder of cell membranes) is caused by a recessive allele."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe cystic fibrosis and polydactyly as examples of inherited genetic disorders.

## theory
```json
[
  {
    "content": "Cystic fibrosis (CF) is caused by a RECESSIVE allele — written as 'f' (faulty) while 'F' is the normal allele.\n\nGENOTYPES:\nFF — unaffected, not a carrier.\nFf — carrier — appears healthy but carries one copy of the faulty allele.\nff — affected — has cystic fibrosis.\n\nFor a child to have CF, they must inherit TWO recessive alleles — one from each parent.\nTwo carriers (Ff × Ff) have a 25% chance of an affected child per pregnancy.\n\nEFFECTS OF CYSTIC FIBROSIS:\nThe faulty allele affects a protein that controls the movement of salt and water across cell membranes.\nThis causes a build-up of THICK, STICKY MUCUS in:\nThe LUNGS — makes breathing difficult, blocks airways, traps bacteria → repeated chest infections → lung damage.\nThe DIGESTIVE SYSTEM — blocks ducts from the pancreas → digestive enzymes cannot reach the gut → poor absorption of nutrients.\n\nTREATMENT: physiotherapy to loosen mucus, antibiotics for infections, enzyme supplements with food. No cure (though gene therapy is in development).\n\nCF is the most common serious inherited disorder in the UK — approximately 1 in 25 people carry the allele.",
    "heading": "Cystic Fibrosis"
  },
  {
    "content": "Polydactyly is caused by a DOMINANT allele — written as 'D' while 'd' is the normal allele.\n\nGENOTYPES:\nDD — affected (rare — very few people have two copies of the dominant allele).\nDd — affected — only ONE copy needed to show the condition.\ndd — unaffected.\n\nA person with polydactyly has one or more EXTRA FINGERS OR TOES.\n\nBecause the allele is DOMINANT:\nOnly ONE copy is needed — so an affected parent (Dd) has a 50% chance of passing the condition to each child.\nThe condition appears in EVERY GENERATION that carries the allele.\nAn affected person has at least one affected parent (unless it arose from a new mutation).\n\nPolydactyly is not life-threatening and can be surgically corrected.\n\nKEY CONTRAST with cystic fibrosis:\nCF = recessive — can skip generations (carriers appear normal).\nPolydactyly = dominant — appears in every generation that carries it.",
    "heading": "Polydactyly"
  },
  {
    "content": "GENETIC TESTING can identify whether a person carries alleles for inherited conditions.\n\nTypes of testing:\nPRE-CONCEPTION testing — couples who have a family history of a genetic condition can be tested to find out if they are carriers before having children.\nPRE-NATAL testing — testing the embryo or foetus during pregnancy. Methods: amniocentesis (sampling amniotic fluid), chorionic villus sampling (CVS — sampling placental tissue).\nNEWBORN SCREENING — blood spot test (heel prick) shortly after birth screens for several conditions including CF.\n\nETHICAL CONSIDERATIONS:\nPrivacy — who has access to genetic information? Could affect insurance or employment.\nDecision-making — if a foetus tests positive, should the pregnancy continue? Raises difficult ethical questions.\nPsychological impact — knowing you carry an allele for a serious condition causes anxiety.\nSocial stigma — discrimination against those known to have certain genetic profiles.\nThese are genuine ethical debates with no single correct answer — the key is to consider multiple perspectives.",
    "heading": "Genetic Testing and Ethical Issues"
  }
]
```

## higher

Embryo screening (PGD — preimplantation genetic diagnosis): embryos from IVF can be tested for genetic conditions before implantation. Allows selection of unaffected embryos. Ethical issues: is this a slippery slope to designer babies? Does it devalue people with that condition? Genetic counselling helps families understand inheritance patterns and risks without being directive about choices.

## common_mistake

Cystic fibrosis is RECESSIVE — both parents can be unaffected carriers. Polydactyly is DOMINANT — at least one parent will always be affected (unless it arose from a new mutation). Students often apply these rules the wrong way round. Remember: recessive conditions can SKIP GENERATIONS (via carriers). Dominant conditions CANNOT skip generations.

## key_note

CF: recessive (ff), thick mucus in lungs and gut, 1 in 25 carriers in UK. Polydactyly: dominant (Dd), extra digits, appears every generation. Recessive can skip generations. Dominant cannot (unless new mutation).

## fifas
```json
[
  {
    "label": "CF Inheritance Cross",
    "question": "Two carriers for cystic fibrosis (Ff × Ff) are expecting a child. What is the probability the child will have CF?",
    "steps": [
      [
        "F",
        "Draw Punnett square: Ff × Ff. CF allele = f (recessive). Normal = F"
      ],
      [
        "I",
        "Offspring: FF, Ff, Ff, ff → ratio 1:2:1"
      ],
      [
        "F",
        "Only ff has cystic fibrosis = 1 out of 4 boxes"
      ],
      [
        "A",
        "Probability of CF = 1/4 = 25%"
      ]
    ]
  }
]
```

## matching
```json
{
  "instruction": "Match each feature to the correct inherited disorder.",
  "pairs": [
    [
      "Cystic fibrosis",
      "Caused by a recessive allele — both copies needed for the condition to show"
    ],
    [
      "Polydactyly",
      "Caused by a dominant allele — only one copy needed to show the condition"
    ],
    [
      "Cystic fibrosis",
      "Causes thick sticky mucus in lungs and digestive system"
    ],
    [
      "Polydactyly",
      "Causes extra fingers or toes — not life-threatening"
    ],
    [
      "Cystic fibrosis",
      "Can skip generations — carriers appear healthy"
    ],
    [
      "Polydactyly",
      "Appears in every generation — an affected person always has at least one affected parent"
    ]
  ],
  "title": "Cystic Fibrosis or Polydactyly?"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Both parents are carriers — genotype Ff — they have one copy of the recessive allele each",
        true
      ],
      [
        "One parent must have cystic fibrosis but is hiding it",
        false
      ],
      [
        "The child developed CF through a random environmental mutation",
        false
      ],
      [
        "The parents must be closely related — CF only occurs in related families",
        false
      ]
    ],
    "q": "Both parents appear healthy but have a child with cystic fibrosis. What must be true of the parents?",
    "wrong_explanations": {
      "1": "CF is a genetic condition — you cannot 'hide' it. If a parent had CF (ff) they would have serious symptoms.",
      "2": "CF is caused by inheriting TWO recessive alleles — both alleles must come from parents. The parents must both be carriers (Ff).",
      "3": "While CF is more common in some populations, it is not caused by family relatedness — it requires two carriers regardless of family relationship."
    }
  },
  {
    "opts": [
      [
        "Polydactyly is dominant — one copy is enough to show it. CF is recessive — carriers (Ff) appear normal and don't show it.",
        true
      ],
      [
        "Polydactyly is caused by a different chromosome than cystic fibrosis",
        false
      ],
      [
        "Cystic fibrosis is more severe so the body suppresses it in some generations",
        false
      ],
      [
        "Polydactyly affects more people so it appears more often",
        false
      ]
    ],
    "q": "Why does polydactyly appear in every generation, while cystic fibrosis can skip generations?",
    "wrong_explanations": {
      "1": "The chromosomal location of a gene is irrelevant to whether the condition skips generations — it's the dominant/recessive nature that matters.",
      "2": "The body doesn't suppress genetic conditions — whether a condition shows depends entirely on genotype and allele dominance.",
      "3": "Prevalence doesn't determine whether a condition skips generations — dominance/recessiveness does."
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

**Question:** Two carriers for cystic fibrosis (Ff × Ff) are expecting a child. What is the probability the child will have CF?

**Convert:** [NEW — examined ✓] Nothing to convert — this is a genetics probability calculation with no physical units involved.

**F:** Draw Punnett square: Ff × Ff. CF allele = f (recessive). Normal = F

**I:** Offspring: FF, Ff, Ff, ff → ratio 1:2:1

**F:** Only ff has cystic fibrosis = 1 out of 4 boxes

**A:** Probability of CF = 1/4 = 25%
