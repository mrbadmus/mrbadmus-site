# Antibiotics and Painkillers  (Biology, AQA 4.3.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec |
|---|---|---|
| Antibiotics (e.g. penicillin) kill bacteria; specific antibiotics for specific bacteria | base | 8464/8461 4.3.1.8 (header's "4.3.3" is site numbering) |
| Antibiotics greatly reduced deaths — missing from source (ANTIBIOTICS-PAINKILLERS-F2) | base | 4.3.1.8 |
| Antibiotics cannot kill viruses | base | 4.3.1.8 |
| Resistance: mutation, selection, MRSA, how to slow it | base | 4.3.1.8; 8464 4.6.3.4 / 8461 4.6.3.7 |
| Painkillers treat symptoms, do not kill pathogens | base | 4.3.1.8 |
| Hard to make drugs that kill viruses without damaging body tissues | base | 4.3.1.8 |
| `higher` box: resistance by natural selection | base, not HT (ANTIBIOTICS-PAINKILLERS-F1) | 4.6.3.4 / 4.6.3.7 |
| quiz q1, q2 | base — both usable | 4.3.1.8; 4.6.3.4 |

True page routes: CF CH TF TH (all base; no Higher layer). Site currently ships: CF CH TF TH — matches (its CH/TH `higher` copy is base content).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Explain how antibiotics work, why antibiotic resistance is a threat, and the role of painkillers.

## theory
```json
[
  {
    "content": "Antibiotics are drugs that kill bacteria or prevent them from reproducing — they are used to treat BACTERIAL infections.\n\nHow they work: Antibiotics target specific structures in bacteria that are NOT present in human cells — for example:\nPENICILLIN (and similar antibiotics) disrupts bacterial CELL WALL synthesis. Human cells have no cell wall, so penicillin doesn't harm them.\nOther antibiotics target bacterial ribosomes or DNA replication.\n\nDifferent antibiotics work on different bacteria:\nBROAD SPECTRUM antibiotics work against many different bacterial species.\nNARROW SPECTRUM antibiotics target specific types of bacteria.\n\nAntibiotics CANNOT treat viral infections because:\nViruses have no cell walls, no bacterial ribosomes and no bacterial DNA replication machinery — there is nothing for antibiotics to target.\nViruses live INSIDE host cells — drugs that killed them would also damage the host cell.\n\nAntibiotics were discovered by Alexander Fleming in 1928 — he noticed Penicillium mould was killing bacteria on a petri dish.",
    "heading": "Antibiotics"
  },
  {
    "content": "Antibiotic resistance is one of the greatest threats to global health.\n\nHow it develops through NATURAL SELECTION:\n1. Within a population of bacteria, random MUTATIONS occur naturally during reproduction.\n2. Occasionally, a mutation gives a bacterium resistance to an antibiotic.\n3. When antibiotics are used, non-resistant bacteria are killed.\n4. Resistant bacteria SURVIVE and REPRODUCE — passing on the resistance gene to offspring.\n5. Over time, the entire population becomes resistant — the antibiotic no longer works.\n\nWhy resistance is spreading:\nOVER-PRESCRIBING — doctors prescribing antibiotics for viral infections or 'just in case'.\nNOT COMPLETING COURSES — stopping early leaves some bacteria alive; the survivors are more likely to be partially resistant.\nAGRICULTURE — antibiotics used to promote growth in livestock, creating resistant bacteria in food chains.\n\nConsequences: Infections once easily treated (e.g. tuberculosis, some pneumonias) are becoming dangerous again. MRSA (methicillin-resistant Staphylococcus aureus) is an example of a serious antibiotic-resistant bacterium.\n\nHow to slow resistance:\nOnly use antibiotics when genuinely necessary.\nAlways complete the full course.\nNever share or save antibiotics for later.\nReduce agricultural antibiotic use.",
    "heading": "Antibiotic Resistance — A Global Crisis"
  },
  {
    "content": "Painkillers (analgesics) relieve pain and reduce fever — but they do NOT kill pathogens or treat the cause of infection.\n\nCommon painkillers: paracetamol, ibuprofen, aspirin.\n\nThey treat SYMPTOMS — making the patient feel more comfortable — but the immune system still needs to fight the infection.\n\nA patient with a bacterial infection may take BOTH:\nAntibiotics — to kill the bacteria (treating the cause).\nPainkillers — to manage fever, pain and discomfort (treating the symptoms).\n\nANTIVIRAL DRUGS are medicines that do treat viral infections — but they are much harder to develop than antibiotics because viruses use the host cell's own machinery.\nExamples: oseltamivir (Tamiflu) for influenza, antiretroviral drugs (ARVs) for HIV.\nAntivirals don't kill viruses outright — they usually prevent replication.",
    "heading": "Painkillers"
  }
]
```

## higher

Antibiotic resistance develops through natural selection: random resistance mutations exist in a bacterial population → antibiotics act as selection pressure killing non-resistant bacteria → resistant bacteria survive, reproduce and pass on resistance genes → resistance spreads. MRSA is a clinically important example. Students should be able to explain why reducing unnecessary antibiotic use and completing courses slows resistance development.

## common_mistake

Painkillers do NOT treat infections — they only relieve symptoms. A patient taking only paracetamol for a bacterial infection is NOT treating the infection. Also: always complete antibiotic courses — stopping early is a major driver of resistance because the bacteria that survive are likely to be the more resistant ones.

## key_note

Antibiotics: kill bacteria, NO effect on viruses, target bacterial cell walls/ribosomes. Antibiotic resistance: natural selection of resistant mutants — avoid misuse. Painkillers: treat symptoms only, don't kill pathogens.

## matching
```json
{
  "instruction": "Sort each statement to the correct type of drug.",
  "pairs": [
    [
      "Antibiotic",
      "Kills bacteria — works by targeting bacterial cell walls or ribosomes"
    ],
    [
      "Painkiller",
      "Relieves fever and pain — does not kill any pathogens"
    ],
    [
      "Antiviral",
      "Prevents viral replication — used for HIV and influenza"
    ],
    [
      "Antibiotic",
      "Has no effect on viral infections — useless against flu or measles"
    ],
    [
      "Painkiller",
      "Examples: paracetamol, ibuprofen, aspirin"
    ]
  ],
  "title": "Antibiotic, Painkiller or Antiviral?"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Viruses don't have cell walls or bacterial ribosomes — the structures antibiotics target don't exist in viruses",
        true
      ],
      [
        "Viruses are too small for antibiotics to reach",
        false
      ],
      [
        "Antibiotics are absorbed too slowly to reach viruses in the bloodstream",
        false
      ],
      [
        "Viruses produce enzymes that destroy antibiotics",
        false
      ]
    ],
    "q": "Why can't antibiotics treat viral infections?",
    "wrong_explanations": {
      "1": "Viruses are smaller than bacteria — but size is not why antibiotics don't work. Antibiotics target specific bacterial structures that viruses simply don't have.",
      "2": "Antibiotics are absorbed into the bloodstream — but they have no biological target in virus particles, so reaching them makes no difference.",
      "3": "Some resistant bacteria do produce enzymes that destroy antibiotics — but this is a bacterial resistance mechanism, not a general viral property."
    }
  },
  {
    "opts": [
      [
        "Stopping early leaves the most resistant bacteria alive — they survive and reproduce, increasing resistance",
        true
      ],
      [
        "Stopping early means the antibiotics already taken are wasted and have no effect",
        false
      ],
      [
        "Partial courses make the bacteria grow faster as a response",
        false
      ],
      [
        "It doesn't matter — stopping early is fine if symptoms improve",
        false
      ]
    ],
    "q": "Why is it important to always complete a full course of antibiotics?",
    "wrong_explanations": {
      "1": "The antibiotics already taken do have effect — they kill susceptible bacteria. The problem is that the resistant survivors are left to reproduce.",
      "2": "Bacteria don't 'grow faster' in response to antibiotics stopping — the issue is selective survival of resistant variants.",
      "3": "This is a dangerous misconception — symptoms improving means the immune system and antibiotics are working, but bacteria may still be present. Stopping early increases resistance risk."
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
