# Resistant Bacteria  (Biology, AQA 4.6.5)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Resistance by natural selection: random mutation → antibiotic kills non-resistant → survivors reproduce → population rises (theory 1; common_mistake; key_note) | base | 8464 4.6.3.4; 8461 4.6.3.7 |
| MRSA (theory 2) — "acquired resistance through repeated exposure" IMPRECISE (RB-F2) | base | 8464 4.6.3.4; 8461 4.6.3.7 |
| Causes, slow new antibiotics, reducing resistance (theory 3) | base | 8464 4.6.3.4; 8461 4.6.3.7 |
| Phage therapy, hygiene (theory 3) | context, beyond spec | — |
| `higher` field — not HT (RB-F1) | base | 8464 4.6.3.4 |
| quiz q1, q2, q3 | base — usable | 8464 4.6.3.4 |

True page routes: CF CH TF TH. Matches the site. The data's "4.6.5" is the site's internal number.

## Spec core missing from the frozen data (written from the spec, examiner)
One spec sentence is absent. Verbatim, 8464 4.6.3.4 = 8461 4.6.3.7:

> "The resistant strain will then spread because people are not immune to it and there is no effective treatment."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain how antibiotic resistance develops through natural selection and why it is a global health threat.

## theory
```json
[
  {
    "content": "Antibiotic resistance is a direct example of EVOLUTION BY NATURAL SELECTION occurring in our lifetimes.\n\nThe process:\n1. VARIATION — within a population of bacteria, individuals vary slightly due to random mutations. A very small number may have a mutation that gives RESISTANCE to a particular antibiotic.\n2. SELECTION PRESSURE — when antibiotics are used, they KILL bacteria that are NOT resistant. The resistant bacteria SURVIVE.\n3. REPRODUCTION — resistant bacteria reproduce (bacteria can double every 20 minutes). They pass on the resistance gene to offspring.\n4. SPREAD — resistant bacteria become increasingly common in the population. The antibiotic no longer works.\n\nThis is natural selection in real time — the antibiotic acts as the selection pressure. The resistant mutation existed BEFORE the antibiotic was used — the antibiotic didn't create the mutation, it selected for it.",
    "heading": "How Antibiotic Resistance Develops"
  },
  {
    "content": "MRSA (Methicillin-resistant Staphylococcus aureus) is a bacterium that has developed resistance to many commonly used antibiotics.\n\nStaphylococcus aureus is normally a relatively harmless skin bacterium found on about 30% of people.\n\nMRSA has acquired resistance through repeated exposure to antibiotics — particularly in hospital settings where antibiotics are widely used.\n\nWhy MRSA is dangerous:\nDifficult to treat — standard antibiotics don't work.\nCan cause serious infections: bloodstream infections (sepsis), pneumonia, wound infections.\nParticularly dangerous for hospital patients who are already weakened or have wounds.\nFew effective antibiotics remain — some strains are resistant to almost everything.\n\nMRSA shows what can happen when antibiotic resistance goes unchecked — a common bacterium becomes a serious, life-threatening pathogen.",
    "heading": "MRSA — A Serious Example"
  },
  {
    "content": "Antibiotic resistance is one of the greatest threats to global health, food security and development — according to the World Health Organisation.\n\nThe problem is accelerating because:\nOVER-PRESCRIPTION — antibiotics given for viral infections (where they have no effect) or 'just in case'.\nINCOMPLETE COURSES — stopping antibiotics early leaves the most resistant bacteria alive to reproduce.\nAGRICULTURAL USE — antibiotics widely used in livestock farming to prevent disease and promote growth → resistant bacteria enter food chains.\nGLOBAL SPREAD — resistant bacteria travel with people internationally.\nSLOW DEVELOPMENT of new antibiotics — pharmaceutical companies have reduced investment because new antibiotics are not as profitable as drugs for chronic diseases.\n\nWhat can be done:\nPrescribe antibiotics ONLY when necessary.\nPatients must COMPLETE FULL COURSES.\nDevelop NEW antibiotics and alternative treatments (e.g. phage therapy — using viruses that kill bacteria).\nReduce agricultural antibiotic use.\nBetter hygiene to prevent spread of resistant bacteria.",
    "heading": "Why Antibiotic Resistance is a Global Crisis"
  }
]
```

## higher

MRSA developed resistance through natural selection in hospital environments where antibiotics are heavily used. Strategies to manage resistance: prescribe only when necessary, complete courses, reduce agricultural use, develop new antibiotics, explore alternative therapies (bacteriophage therapy — viruses that infect bacteria). Students should be able to explain why resistance is evolutionarily inevitable if antibiotics are overused — resistant variants will always be selected for.

## common_mistake

Antibiotics do NOT CAUSE mutations — they SELECT resistant bacteria that already exist. The mutation happened randomly, long before the antibiotic was used. The antibiotic is the selection pressure that determines which bacteria survive. This is a key distinction — evolution acts on existing variation, it doesn't create new variation in response to need.

## key_note

Resistance develops by natural selection: random resistance mutation exists → antibiotic kills non-resistant bacteria → resistant bacteria survive and reproduce → resistance spreads. Antibiotics select for resistance — they don't cause it. MRSA = serious hospital-acquired resistant bacterium.

## matching
```json
{
  "instruction": "Put the steps of antibiotic resistance development in order by matching each step.",
  "pairs": [
    [
      "Step 1 — Variation",
      "A random mutation gives one bacterium resistance to an antibiotic — before any antibiotic is used"
    ],
    [
      "Step 2 — Selection pressure",
      "Antibiotic is used — kills all non-resistant bacteria, resistant one survives"
    ],
    [
      "Step 3 — Reproduction",
      "Resistant bacterium reproduces — passing resistance gene to millions of offspring"
    ],
    [
      "Step 4 — Population change",
      "Resistant bacteria dominate the population — the antibiotic no longer works"
    ]
  ],
  "title": "Steps in Developing Antibiotic Resistance"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "A random mutation gives some bacteria resistance — antibiotics kill non-resistant bacteria but resistant ones survive and reproduce",
        true
      ],
      [
        "Bacteria deliberately mutate themselves when exposed to antibiotics to survive",
        false
      ],
      [
        "Antibiotics cause the mutation that produces resistance in bacteria",
        false
      ],
      [
        "Resistant bacteria migrate from other areas after non-resistant bacteria are killed",
        false
      ]
    ],
    "q": "How does antibiotic resistance develop in bacteria?",
    "wrong_explanations": {
      "1": "Bacteria cannot deliberately change their DNA — mutations are RANDOM and SPONTANEOUS. Bacteria cannot respond to threats by choosing to mutate.",
      "2": "Antibiotics are the SELECTION PRESSURE — they select pre-existing resistant variants. They do not cause the mutations that produce resistance.",
      "3": "Migration can spread resistance — but the PRIMARY mechanism of resistance developing in a population is natural selection of pre-existing resistant mutants."
    }
  },
  {
    "opts": [
      [
        "Stopping early leaves the most resistant bacteria alive — they survive to reproduce and pass on resistance genes",
        true
      ],
      [
        "The remaining antibiotics are needed to prevent the infection returning to full strength",
        false
      ],
      [
        "Unfinished antibiotics are wasted medicine that could have been used by others",
        false
      ],
      [
        "Stopping early makes the side effects of antibiotics worse",
        false
      ]
    ],
    "q": "Why is it important to complete a full course of antibiotics even if you feel better?",
    "wrong_explanations": {
      "1": "Infections can return if bacteria are not fully cleared — but the MORE IMPORTANT reason in terms of antibiotic resistance is that the survivors of partial treatment are the most resistant bacteria.",
      "2": "While waste is a concern, the primary medical reason is resistance selection — the survivors of an incomplete course are more likely to be resistant.",
      "3": "Side effects are not affected by course completion — the resistance argument is the primary public health reason."
    }
  },
  {
    "opts": [
      [
        "Through natural selection — repeated antibiotic use in hospitals selected for bacteria with resistance mutations, which then multiplied",
        true
      ],
      [
        "MRSA was deliberately engineered in a laboratory as a biological weapon",
        false
      ],
      [
        "MRSA infected humans from animals and naturally carries more mutations than other bacteria",
        false
      ],
      [
        "Hospital cleaning products cause bacteria to mutate and become resistant",
        false
      ]
    ],
    "q": "MRSA is resistant to many antibiotics. How did this resistance arise?",
    "wrong_explanations": {
      "1": "MRSA arose naturally through the evolutionary process of natural selection — not deliberate engineering.",
      "2": "Staphylococcus aureus is primarily a human pathogen — while zoonotic transmission does occur, MRSA's resistance arose through natural selection in hospital environments.",
      "3": "Cleaning products can select for resistance to disinfectants — but antibiotic resistance specifically arises from exposure to antibiotics, not cleaning agents."
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
