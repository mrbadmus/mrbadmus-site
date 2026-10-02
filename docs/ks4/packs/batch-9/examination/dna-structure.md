# Examination — DNA Structure (dna-structure) — AQA 8461 4.6.1.5 (biology only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-9/04-checked-science-source/biology-4.6.2.1-dna-structure.md`.
Spec sources read as text: `AQA-8461-spec.txt` (Version 1.0, 21 Apr 2016) and `AQA-8464-spec.txt` (Version 1.1, 04 Oct 2019). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `dna-structure`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The site's "4.6.2.1" is its internal number; the true ref is 8461 **4.6.1.5** (8461 4.6.2.1 is Variation). Route copies identical except `higher` (TH text; `null` on TF). Sibling lesson `dna-genome` (all four routes, 8464 4.6.1.3 / 8461 4.6.1.4) owns double helix, gene, chromosome and genome.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8461 Biology | **4.6.1.5** | DNA structure | **(biology only)**; six paragraphs also **(HT only)** |
| Supporting | 8464 4.6.1.3 / 8461 4.6.1.4 | DNA and the genome (double helix, gene) | base |
| Supporting | 8464 4.6.2.1 / 8461 4.6.2.1 | Variation ("all variants arise from mutations") | base |
| 8464 | — | not in Combined Science | — |

Spec statements (8461 4.6.1.5, verbatim):
- "Students should be able to describe DNA as a polymer made from four different nucleotides. Each nucleotide consists of a common sugar and phosphate group with one of four different bases attached to the sugar. DNA contains four bases, A, C, G and T. A sequence of three bases is the code for a particular amino acid. The order of bases controls the order in which amino acids are assembled to produce a particular protein. The long strands of DNA consist of alternating sugar and phosphate sections. Attached to each sugar is one of the four bases. The DNA polymer is made up of repeating nucleotide units." (WS 1.2: "Interpret a diagram of DNA structure but will not be required to reproduce it.")
- "(HT only) Students should be able to: • recall a simple description of protein synthesis • explain simply how the structure of DNA affects the protein made • describe how genetic variants may influence phenotype: a) in coding DNA by altering the activity of a protein: and b) in non-coding DNA by altering how genes are expressed."
- "(HT only) In the complementary strands a C is always linked to a G on the opposite strand and a T to an A."
- "(HT only) Students are not expected to know or understand the structure of mRNA, tRNA, or the detailed structure of amino acids or proteins."
- "(HT only) Students should be able to explain how a change in DNA structure may result in a change in the protein synthesised by a gene."
- "(HT only) Proteins are synthesised on ribosomes, according to a template. Carrier molecules bring specific amino acids to add to the growing protein chain in the correct order."
- "(HT only) When the protein chain is complete it folds up to form a unique shape. This unique shape enables the proteins to do their job as enzymes, hormones or forming structures in the body such as collagen."
- "(HT only) Mutations occur continuously. Most do not alter the protein, or only alter it slightly so that its appearance or function is not changed." (WS 1.2: "Modelling insertions and deletions in chromosomes to illustrate mutations.")
- "(HT only) A few mutations code for an altered protein with a different shape. An enzyme may no longer fit the substrate binding site or a structural protein may lose its strength."
- "(HT only) Not all parts of DNA code for proteins. Non-coding parts of DNA can switch genes on and off, so variations in these areas of DNA may affect how genes are expressed."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | DNA carries genetic information; double helix of two strands (th1) | base (context here) | 8464 4.6.1.3 | TF TH | OK |
| R2 | Nucleotides: sugar + phosphate + one of four bases A T G C (th1; key_note) | triple | 8461 4.6.1.5 | TF TH | OK |
| R3 | Alternating sugar–phosphate strands, base on each sugar; repeating nucleotide units | triple | 8461 4.6.1.5 | — | **GAP** — implied, never stated (F5) |
| R4 | Strands held by weak hydrogen bonds (th1; matching "two/three hydrogen bonds") | not in spec | — | TF TH | OFF-SPEC (F3) |
| R5 | Complementary pairing A–T, G–C; work out the other strand (th1; common_mistake; key_note; matching) | **triple-higher** | 8461 4.6.1.5 (HT only) | TF TH | **ROUTE leak onto TF** (F1) |
| R6 | Gene = sequence of bases coding for a protein (th2; key_note) | base | 8464 4.6.1.3 | TF TH | OK |
| R7 | Three bases code for one amino acid; order of bases → order of amino acids (th2; key_note) | triple | 8461 4.6.1.5 | TF TH | OK ("codon" is a name the spec does not use; harmless) |
| R8 | 4³ = 64 codons, 20 amino acids (th2) | not in spec | — | TF TH | OFF-SPEC (F3) |
| R9 | Amino-acid order → protein shape → function (th2) | triple-higher | 8461 4.6.1.5 (HT only) | TF TH | ROUTE leak onto TF (F1); spec's examples (enzymes, hormones, collagen) missing (F5) |
| R10 | Non-coding DNA; some regulates when genes are switched on/off (th2) | triple-higher | 8461 4.6.1.5 (HT only) | TF TH | ROUTE leak onto TF (F1) |
| R11 | Protein synthesis: transcription → mRNA → ribosome → translation → folds (th2; key_note) | triple-higher | 8461 4.6.1.5 (HT only) | TF TH | ROUTE leak onto TF (F1); IMPRECISE vs spec's simple description — no carrier molecules (F5) |
| R12 | Replication: unwinding, templates, free nucleotides, semi-conservative (th3; key_note; `higher`; q2) | not in spec | — | TF TH | OFF-SPEC (F2) |
| R13 | Mutations change base sequence → may alter protein → may affect organism (th3) | triple-higher | 8461 4.6.1.5 (HT only) | TF TH | ROUTE leak onto TF (F1) |
| R14 | `higher`: replication + DNA polymerase | not in spec | — | TH | OFF-SPEC (F2) |
| R15 | `higher`: substitution / insertion / deletion change amino-acid sequence → structure and function of protein | triple-higher | 8461 4.6.1.5 (HT only; WS 1.2 insertions and deletions) | TH | OK |
| R16 | q1 complementary strand of ATCGTA | triple-higher | 8461 4.6.1.5 (HT only) | TF TH | ROUTE (F1); item defect (F4) |
| R17 | q2 semi-conservative replication | not in spec | — | TF TH | OFF-SPEC (F2) |
| — | RP, FIFA, equations | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | DNA carries genetic information in all living organisms | OK | — | 4.6.1.3 |
| C2 | th1 | double helix, two strands, "twisted ladder" | OK | — | 4.6.1.3 |
| C3 | th1 | nucleotide = sugar (deoxyribose) + phosphate + one of A, T, G, C | OK | Spec says "a common sugar"; naming deoxyribose is correct but not required. | 4.6.1.5 |
| C4 | th1 | strands held together by weak hydrogen bonds | OFF-SPEC | True; not in spec. Do not test. | — |
| C5 | th1 | A pairs with T, G with C; know one strand → work out the other | OK, HT | Spec: "a C is always linked to a G … and a T to an A" (HT only). | 4.6.1.5 HT |
| C6 | th1 | "complementary pairing is essential for accurate DNA replication" | OFF-SPEC | True; replication not in spec. | — |
| C7 | th2 | gene = sequence of bases coding for a specific protein | OK | Spec: "a small section of DNA on a chromosome … codes for a particular sequence of amino acids". | 4.6.1.3 |
| C8 | th2 | three bases (codon) → one amino acid; order of amino acids → shape → function | OK | — | 4.6.1.5 |
| C9 | th2 | 4³ = 64 codons, more than enough for 20 amino acids | OFF-SPEC | Arithmetic ✓ (4 × 4 × 4 = 64). Not in spec. | — |
| C10 | th2 | non-coding DNA between genes; some switches genes on/off | OK, HT | — | 4.6.1.5 HT |
| C11 | th2 | transcribed to mRNA; mRNA leaves nucleus to ribosomes; translated; chain folds | OK, HT, IMPRECISE | Correct science; spec wants the simple version ("synthesised on ribosomes, according to a template. Carrier molecules bring specific amino acids … in the correct order") and says mRNA/tRNA structure is not expected. Carrier molecules are missing. | 4.6.1.5 HT |
| C12 | th3 | replication: unwind, separate, templates, free nucleotides, two identical helices each with one original strand | OFF-SPEC | Correct science (A-level). Not in 8461. | — |
| C13 | th3 | mutations = change in base sequence → may alter protein | OK, HT | Spec adds "most do not alter the protein, or only alter it slightly". | 4.6.1.5 HT |
| C14 | `higher` | semi-conservative replication, DNA polymerase | OFF-SPEC | Cut. | — |
| C15 | `higher` | substitution, insertion, deletion → amino-acid sequence → structure and function | OK, HT | — | 4.6.1.5 HT |
| C16 | common_mistake | A–T, C–G fixed; "Apples in Trees, Cars in Garages" | OK, HT | — | 4.6.1.5 HT |
| C17 | key_note | as th1–th3 | OK / OFF-SPEC | Replication sentence off-spec (C12). | — |
| C18 | matching (to be replaced) | A–T "two hydrogen bonds", G–C "three hydrogen bonds" | OFF-SPEC | True; not in spec. Replaced anyway. | — |
| C19 | q1 key | complement of ATCGTA = TAGCAT | OK | A→T, T→A, C→G, G→C, T→A, A→T = TAGCAT ✓ | 4.6.1.5 HT |
| C20 | q1 opt 2 / wx1 | ATCGTA "identical" | OK | wx1 explains option 2 ✓ (aligned). | — |
| C21 | q1 opt 3 / wx2 | UAGCAU "RNA bases" | OK | wx2 explains option 3 ✓ (aligned). Uracil is off-spec but the explanation is true. | — |
| C22 | q1 opt 4 / wx3 | "TACGAT — bases pair like-for-like: A with A, T with T" | **IMPRECISE (item defect)** | wx3 explains option 4 ✓ (aligned), but the option's sequence does not follow its own stated rule: like-for-like pairing gives ATCGTA (option 2's sequence), not TACGAT. The distractor contradicts itself. | — |
| C23 | q2 key | semi-conservative: each original strand is a template | OFF-SPEC | Correct science; not in 8461. | — |
| C24 | q2 wx1–wx3 | conservative model disproved; not random; both strands copied | OFF-SPEC | All true and aligned (wx1→opt 2, wx2→opt 3, wx3→opt 4 ✓). | — |
| C25 | `higher` TF copy | `null` | OK | TF must not carry the HT layer. | — |

Count: **0 WRONG**. ROUTE: F1. OFF-SPEC: F2, F3. IMPRECISE: F4 (q1 option 4). GAP: F5.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | Complementary pairing is HT only; option 4 contradicts itself (F4). | Not as written. If a corrected copy is allowed, TH only. |
| q2 | Semi-conservative replication is not in the spec (F2). | Not usable on any route. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- A pairs with G / C pairs with T (or like-for-like).
- "A gene is a protein" / "DNA is made of amino acids" — DNA codes for the order of amino acids.
- "Every mutation causes a disease" — most do not alter the protein, or only slightly (HT).
- "All DNA is genes" — non-coding parts exist and can switch genes on and off (HT).
- Proteins "made in the nucleus" — they are synthesised on ribosomes (HT).

**Command words**: Describe (the structure of DNA), Give (the complementary base), Explain (how a change in DNA can change the protein — HT), Use the diagram / Interpret.

**Required practical**: none.

**Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All factual statements are true; nothing is wrong science. But about a third of the file is A-level (replication, hydrogen bonds, 64 codons), every pairing / protein-synthesis / mutation point is HT and currently shows on Triple Foundation, and the spec's own HT core (carrier molecules, folding → enzymes/hormones/collagen, how a mutation changes an enzyme's fit or a structural protein's strength) is missing. Neither frozen quiz item is usable as written.

**For Mide:** nothing. All settled spec facts.
