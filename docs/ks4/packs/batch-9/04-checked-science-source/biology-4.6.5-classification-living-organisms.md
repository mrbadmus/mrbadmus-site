# Classification of Living Organisms  (Biology, AQA 4.6.5)

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Linnaeus; binomial naming; hierarchy; species definition (theory 1; common_mistake) — "Carlus" misspelt (CL-F2); five kingdoms are not Linnaeus's (CL-F3) | base | 8464/8461 4.6.4; 4.6.2.2 |
| Woese; rRNA; three domains; Archaea closer to Eukarya (theory 2; key_note) — "1977" IMPRECISE (CL-F4) | base | 8464/8461 4.6.4 |
| Evolutionary trees: nodes, evidence, uses (theory 3) | base | 8464/8461 4.6.4 |
| `higher` field — not HT (CL-F5) | base | 8464/8461 4.6.4 |
| quiz q1, q2 | base — usable | 8464/8461 4.6.4 |

True page routes: CF CH TF TH. Site currently ships: TF TH; moving under the route-flag PR. The site's `triple_only` note ("not in Combined Science") is false — 8464 4.6.4 is unmarked. The data's "4.6.5" is the site's internal number.

## Spec core missing from the frozen data (written from the spec, examiner)
One spec point is absent. Verbatim, 8464 4.6.4 = 8461 4.6.4:

> "Students should be able to describe the impact of developments in biology on classification systems. As evidence of internal structures became more developed due to improvements in microscopes, and the understanding of biochemical processes progressed, new models of classification were proposed."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the Linnaean classification system and the three-domain system, and explain how evolutionary trees show relationships.

## theory
```json
[
  {
    "content": "CLASSIFICATION is the organisation of living things into groups based on their similarities and differences.\n\nCARLUS LINNAEUS (18th century) developed the binomial system of naming organisms:\nEvery organism has a two-part Latin name:\n1. GENUS (capitalised) — a group of closely related species\n2. SPECIES (lowercase) — organisms of the same species can interbreed to produce fertile offspring\n\nEXAMPLES:\nHomo sapiens — genus Homo, species sapiens (modern humans)\nFelis catus — domestic cat\nPanthera leo — lion\n\nHIERARCHY OF GROUPS (largest to smallest):\nKingdom → Phylum → Class → Order → Family → Genus → Species\nMemory: 'King Philip Came Over For Good Soup'\n\nTRADITIONAL KINGDOMS:\nAnimalia, Plantae, Fungi, Protista, Prokaryota (bacteria)",
    "heading": "The Linnaean Classification System"
  },
  {
    "content": "CARL WOESE proposed the THREE-DOMAIN SYSTEM in 1977 based on analysis of ribosomal RNA (rRNA).\n\nThis replaced the five-kingdom system with three domains:\n\n1. ARCHAEA — primitive prokaryotes, often found in extreme environments (hot springs, salt lakes).\nDNA differs significantly from bacteria despite looking similar under a microscope.\n\n2. BACTERIA — true bacteria, the most numerous organisms on Earth.\nCells without membrane-bound nuclei; different cell wall chemistry from Archaea.\n\n3. EUKARYA — all organisms with membrane-bound nuclei.\nIncludes all animals, plants, fungi, and protists.\n\nWHY THREE DOMAINS?\nRNA sequencing showed Archaea are more closely related to Eukaryotes than to Bacteria — despite looking like bacteria under the microscope.\nThis illustrates that observable characteristics can be misleading — molecular evidence is more reliable.",
    "heading": "The Three-Domain System"
  },
  {
    "content": "EVOLUTIONARY TREES (phylogenetic trees) show the evolutionary relationships between organisms.\n\nHow to read an evolutionary tree:\nBranching points (NODES) = common ancestors.\nThe LENGTH of branches may represent evolutionary time.\nOrganisms that share a more RECENT common ancestor are more closely related.\n\nEVIDENCE used to build evolutionary trees:\nAnatomical similarities — homologous structures.\nFossil record — order of appearance of species.\nDNA and RNA sequences — the more similar the sequences, the more closely related.\nProtein similarities — amino acid sequences in key proteins (e.g. cytochrome c).\n\nIMPORTANCE:\nEvolutionary trees help us understand how species are related.\nCan identify the most likely common ancestor of a group.\nHelp in medicine — understanding which organisms are closely related to pathogens.\n\nLINNAEAN vs EVOLUTIONARY:\nLinnaeus classified by appearance/structure (morphology).\nModern classification uses both morphology AND molecular evidence (DNA, RNA).\nMolecular evidence has revised some traditional classifications.",
    "heading": "Evolutionary Trees"
  }
]
```

## higher

Explain how molecular evidence (rRNA sequences, DNA base sequences, amino acid sequences) has revised traditional morphology-based classification. Interpret evolutionary trees built from molecular data and explain why Woese's three-domain system replaced the five-kingdom system. Evaluate the impact of new molecular data on classification — explain that classification systems are working hypotheses, revised as evidence changes.

## common_mistake

A species is defined by the ability to interbreed and produce FERTILE offspring — not just by looking similar. Horses and donkeys can breed but produce sterile mules → they are different species. The three-domain system has Archaea as a SEPARATE domain from Bacteria — they are not the same despite both being prokaryotes.

## key_note

Linnaeus: binomial naming (Genus species), Kingdom→Phylum→Class→Order→Family→Genus→Species. Three-domain system (Woese): Archaea, Bacteria, Eukarya — based on rRNA. Archaea more related to Eukaryotes than Bacteria. Evolutionary trees: nodes = common ancestors; molecular evidence now used alongside morphology.

## matching
```json
{
  "instruction": "Match each term to its correct description.",
  "pairs": [
    [
      "Binomial name",
      "Two-part Latin name: Genus species — e.g. Homo sapiens"
    ],
    [
      "Species",
      "Organisms that can interbreed and produce fertile offspring"
    ],
    [
      "Three-domain system",
      "Archaea, Bacteria, Eukarya — based on rRNA sequences (Woese, 1977)"
    ],
    [
      "Node on evolutionary tree",
      "Represents a common ancestor from which two lineages diverged"
    ]
  ],
  "title": "Classification Concepts"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "rRNA sequence analysis showed Archaea are more closely related to Eukaryotes than to Bacteria — despite appearing similar to bacteria under a microscope",
        true
      ],
      [
        "The five-kingdom system had too many organisms — three domains is simpler to use",
        false
      ],
      [
        "Woese discovered a new type of organism that did not fit into any of the five kingdoms",
        false
      ],
      [
        "DNA evidence showed all five kingdoms were actually the same evolutionary group",
        false
      ]
    ],
    "q": "Why did Carl Woese's three-domain system replace the five-kingdom classification?",
    "wrong_explanations": {
      "1": "Simplicity was not the reason — the three-domain system is based on MOLECULAR EVIDENCE showing fundamental differences in RNA sequences between Archaea and Bacteria.",
      "2": "Archaea were already known — but rRNA sequencing revealed they were fundamentally different from bacteria at the molecular level despite looking similar.",
      "3": "DNA evidence shows the five kingdoms are related but distinct — the change was specifically about separating Archaea from Bacteria based on molecular differences."
    }
  },
  {
    "opts": [
      [
        "The first two species are more closely related — they diverged from a common ancestor more recently",
        true
      ],
      [
        "The first two species are less related — a recent ancestor means they have had less time to evolve together",
        false
      ],
      [
        "Both pairs are equally related — all organisms share a common ancestor eventually",
        false
      ],
      [
        "The species with the older common ancestor is more evolved — older means more advanced",
        false
      ]
    ],
    "q": "Two species share a more recent common ancestor on an evolutionary tree than two other species. What does this indicate?",
    "wrong_explanations": {
      "1": "More RECENT common ancestor = LESS evolutionary time since divergence = MORE closely related. More ancient ancestor = longer time apart = more distantly related.",
      "2": "All organisms do share ancient common ancestors, but sharing a MORE RECENT one indicates a CLOSER relationship — fewer differences have accumulated since divergence.",
      "3": "More evolved does not mean more advanced — evolution has no direction or goal. Having an older common ancestor simply means the lineages have been separate longer."
    }
  }
]
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
