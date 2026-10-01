# Examination — DNA and the Genome (dna-genome) — AQA 8464 4.6.1.3 / 8461 4.6.1.4
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.6.2-dna-genome.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Version 1.1, 04 Oct 2019) and `AQA-8461-spec.txt` (Version 1.0, 21 Apr 2016). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `dna-genome`.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The site's "4.6.2" is its internal number; true refs are 8464 4.6.1.3 and 8461 4.6.1.4 (8461 4.6.2 is "Variation and evolution"). Route copies identical except `higher` (TH text on CH/TH; `null` on CF/TF). Sibling lesson `dna-structure` (TF TH, 8461 4.6.1.5) owns nucleotides and base pairing.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 Combined Trilogy | **4.6.1.3** | DNA and the genome | base |
| 8461 Biology | **4.6.1.4** | DNA and the genome | base |
| Layer (leaks into this page) | 8461 **4.6.1.5** | DNA structure | **(biology only)**; its complementary-pairing, protein-synthesis and non-coding-DNA paragraphs are also **(HT only)** |
| Supporting | 8464 4.6.1.4 / 8461 4.6.1.6 Genetic inheritance (allele, chromosome pairs) | | base |

Spec statement (verbatim, 8464 4.6.1.3 = 8461 4.6.1.4): "Students should be able to describe the structure of DNA and define genome. The genetic material in the nucleus of a cell is composed of a chemical called DNA. DNA is a polymer made up of two strands forming a double helix. The DNA is contained in structures called chromosomes. A gene is a small section of DNA on a chromosome. Each gene codes for a particular sequence of amino acids, to make a specific protein. The genome of an organism is the entire genetic material of that organism. The whole human genome has now been studied and this will have great importance for medicine in the future. Students should be able to discuss the importance of understanding the human genome. This is limited to the: • search for genes linked to different types of disease • understanding and treatment of inherited disorders • use in tracing human migration patterns from the past."

8461 4.6.1.5 (biology only), as it bears on this file: "DNA as a polymer made from four different nucleotides. Each nucleotide consists of a common sugar and phosphate group with one of four different bases attached to the sugar. DNA contains four bases, A, C, G and T. A sequence of three bases is the code for a particular amino acid. … (HT only) In the complementary strands a C is always linked to a G on the opposite strand and a T to an A. … (HT only) Not all parts of DNA code for proteins. Non-coding parts of DNA can switch genes on and off, so variations in these areas of DNA may affect how genes are expressed."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | DNA carries genetic information; polymer; two strands; double helix (th1) | base | 4.6.1.3 | all four | OK |
| R2 | Nucleotides: sugar, phosphate, one of four bases A T C G (th1; matching) | **triple** | 8461 4.6.1.5 (biology only) | all four | **ROUTE leak** onto CF CH (F1) |
| R3 | Complementary pairing A–T, C–G; hydrogen bonds; accurate replication (th1; common_mistake; key_note; matching) | **triple-higher** | 8461 4.6.1.5 (biology only, HT only) | all four | **ROUTE leak** onto CF CH TF (F1) |
| R4 | Gene = section of DNA coding for a sequence of amino acids → specific protein (th2; key_note) | base | 4.6.1.3 | all four | OK |
| R5 | Chromosomes = long coiled DNA; 46 = 23 pairs, one from each parent; ~20 000 genes (th2) | base | 4.6.1.3; 4.1.2.1; 4.6.1.4 | all four | OK |
| R6 | Alleles = versions of a gene (th2; matching) | base | 8464 4.6.1.4 / 8461 4.6.1.6 | all four | OK (owned by genetic inheritance; fine here) |
| R7 | Genome definition (th3; common_mistake; key_note) | base | 4.6.1.3 | all four | IMPRECISE wording (F5) |
| R8 | Human Genome Project 1990–2003, ~3 billion base pairs (th3) | base | 4.6.1.3 ("whole human genome has now been studied") | all four | OK |
| R9 | Importance: disease genes, personalised medicine, evolution, forensics (th3) | base (first two only) | 4.6.1.3 "This is limited to the: …" | all four | migration GAP (F4); forensics / evolution beyond list (F6) |
| R10 | `higher`: codon = triplet → one amino acid | **triple** (not HT) | 8461 4.6.1.5 (biology only) | CH TH | **ROUTE** — served on CH (F2) |
| R11 | `higher`: universal code → common ancestry | NOT-IN-SPEC | — | CH TH | OFF-SPEC (F2) |
| R12 | `higher`: non-coding DNA (regulatory) | **triple-higher** | 8461 4.6.1.5 (HT only) | CH TH | **ROUTE** — served on CH (F2) |
| R13 | q1 — base pairs | **triple-higher** | 8461 4.6.1.5 (HT only) | all four | usable TH only |
| R14 | q2 — what is a gene | base | 4.6.1.3 | all four | OK, all four |
| R15 | q3 — Human Genome Project | base | 4.6.1.3 | all four | wx2/wx3 swapped (F3) — do not use as written |
| — | RP, equations, FIFA, examiner_tip | none | — | — | correct |

True routes: CF CH TF TH (matches the site), with a triple layer and a triple-higher layer.

## 3. Check table
| # | item | claim (verbatim or abridged) | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | DNA carries genetic information in all living organisms | OK | — | 4.6.1.3 |
| C2 | th1 | polymer of repeating nucleotides; sugar, phosphate, one of four bases A T C G | OK science, ROUTE | Biology only. (F1) | 8461 4.6.1.5 |
| C3 | th1 | two strands → double helix, "twisted ladder" | OK | — | 4.6.1.3 |
| C4 | th1 | strands held by hydrogen bonds between complementary base pairs; A–T, C–G; allows accurate replication | OK science, ROUTE | Pairing is biology only, HT only. Hydrogen bonds and replication are true but not in spec. (F1) | 8461 4.6.1.5 (HT) |
| C5 | th2 | gene = specific sequence of bases coding for a specific protein; base sequence → amino-acid sequence | OK | Spec words: "a small section of DNA on a chromosome … codes for a particular sequence of amino acids, to make a specific protein". "Order of bases controls the order of amino acids" is 8461 4.6.1.5 wording but harmless here. | 4.6.1.3 |
| C6 | th2 | chromosomes = long, tightly coiled DNA; 46 = 23 pairs; one of each pair from each parent | OK | — | 4.1.2.1; 4.6.1.4 |
| C7 | th2 | "approximately 20,000–25,000 protein-coding genes" | OK | Current estimate ≈ 20 000; range acceptable. | — |
| C8 | th2 | alleles = different versions of the same gene, slightly different base sequences, same position on homologous chromosomes | OK | — | 8464 4.6.1.4 |
| C9 | th3 | "The GENOME is the complete set of genetic information in an organism — every gene in every chromosome." | IMPRECISE | "Every gene" undersells it: most of the genome is not genes. Spec: "the entire genetic material of that organism". (F5) | 4.6.1.3 |
| C10 | th3 | HGP: international, 1990–2003, ~3 billion base pairs, location and sequence of human genes | OK | — | 4.6.1.3 |
| C11 | th3 | why it matters: genes linked to inherited disease (BRCA1/2, cystic fibrosis); personalised medicine | OK | = spec bullets 1–2. | 4.6.1.3 |
| C12 | th3 | "Understanding HUMAN EVOLUTION and our relationship to other species" | IMPRECISE | Spec's item is narrower: "use in tracing human migration patterns from the past". Missing as written. (F4) | 4.6.1.3 |
| C13 | th3 | "Forensic science — DNA profiling to identify individuals." | IMPRECISE | Not on the spec's limited list, and DNA profiling (1984) predates and does not depend on the HGP. Cut. (F6) | 4.6.1.3 |
| C14 | higher | codon (triplet) → one amino acid | OK science, ROUTE | Biology only, not HT; served on CH. (F2) | 8461 4.6.1.5 |
| C15 | higher | universal genetic code → common ancestry | OK science, OFF-SPEC | Not in spec. (F2) | — |
| C16 | higher | non-coding DNA: regulatory sequences, non-protein RNA; most DNA non-coding | OK science; ROUTE | Non-coding DNA switching genes on/off is biology only, HT only; "non-protein RNA" not in spec (and spec excludes mRNA/tRNA detail). (F2) | 8461 4.6.1.5 (HT) |
| C17 | common_mistake | gene ≠ chromosome; genome = all genetic information; A–T, C–G only | OK | Last sentence is the triple-higher layer (F1). | 4.6.1.3; 8461 4.6.1.5 |
| C18 | key_note | double helix; A-T C-G; gene; chromosome; genome; ~20 000 genes, ~3 billion base pairs | OK | "A-T and C-G base pairs" is triple-higher (F1). | 4.6.1.3 |
| C19 | matching | 6 pairs | OK | To be replaced; nucleotide and base-pairing pairs are triple / triple-higher. | — |
| C20 | q1 key | A with T, C with G | OK | Triple-higher. | 8461 4.6.1.5 (HT) |
| C21 | q1 wx1 | A–G does not occur; 2 and 3 hydrogen bonds | OK, aligned | H-bond counts true, not in spec. | — |
| C22 | q1 wx2 | A–C, G–T do not occur | OK, aligned | — | — |
| C23 | q1 wx3 | not random | OK, aligned | — | — |
| C24 | q2 key | specific sequence of bases coding for a particular protein | OK | — | 4.6.1.3 |
| C25 | q2 wx1 | chromosome contains thousands of genes | OK, aligned | — | 4.6.1.3 |
| C26 | q2 wx2 | genes do more than appearance (enzymes etc.) | OK, aligned | — | — |
| C27 | q2 wx3 | not all DNA codes for proteins; genes are the protein-coding sequences | OK, aligned | Non-coding DNA is a triple-higher idea but the statement is true and needs no prior teaching on base routes. | 8461 4.6.1.5 |
| C28 | q3 key | international project; sequenced ~3 billion base pairs; mapped human genes | OK | — | 4.6.1.3 |
| C29 | q3 wx1 | not about modifying humans | OK, aligned | — | — |
| C30 | q3 wx2 | (option 2 = "A database of all known genetic diseases and their cures") wx2 reads "While comparisons with other species were made … the primary goal was mapping and sequencing the HUMAN genome itself." | **WRONG — misaligned** | Explains option 3 (chimpanzees). (F3) | — |
| C31 | q3 wx3 | (option 3 = "A study comparing the DNA of humans to chimpanzees") wx3 reads "While the HGP has helped identify disease genes, it was a mapping and sequencing project — not a medical treatment database." | **WRONG — misaligned** | Explains option 2 (database). wx2 and wx3 are swapped. (F3) | — |

Count: **1 WRONG item** (q3: wx2 and wx3 swapped, C30–C31, frozen); **3 IMPRECISE** (C9, C12, C13, all re-cuttable theory); ROUTE leaks (C2, C4, C14, C16, C17, C18, q1); GAP (migration patterns — spec-core section added to the source). The batch's `_extract-notes.md` says "No shifted-key defect found anywhere in this batch"; that is not so for q3 here (or for meiosis q1). No `[NEW — to be examined]` lines in this file.
