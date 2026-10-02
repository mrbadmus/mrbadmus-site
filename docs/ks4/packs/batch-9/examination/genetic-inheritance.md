# Examination — Genetic Inheritance (genetic-inheritance) — AQA 8464 4.6.1.4 / 8461 4.6.1.6
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-9/04-checked-science-source/biology-4.6.3-genetic-inheritance.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Version 1.1, 04 Oct 2019) and `AQA-8461-spec.txt` (Version 1.0, 21 Apr 2016). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `genetic-inheritance`.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The site's "4.6.3" is its internal number; true refs are 8464 **4.6.1.4** and 8461 **4.6.1.6**. Route copies identical except `higher` (TH text on CH/TH; `null` on CF/TF).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 Combined Trilogy | **4.6.1.4** | Genetic inheritance | base; one paragraph **(HT only)** |
| 8461 Biology | **4.6.1.6** | Genetic inheritance | base; one paragraph **(HT only)** |
| Supporting | 8464 4.6.1.5 / 8461 4.6.1.7 Inherited disorders (cystic fibrosis, q2) | | base |

Spec statements (verbatim, 8464 4.6.1.4 = 8461 4.6.1.6):
- "Students should be able to explain the terms: gamete, chromosome, gene, allele, dominant, recessive, homozygous, heterozygous, genotype, phenotype."
- "Some characteristics are controlled by a single gene, such as: fur colour in mice; and red-green colour blindness in humans. Each gene may have different forms called alleles."
- "The alleles present, or genotype, operate at a molecular level to develop characteristics that can be expressed as a phenotype."
- "A dominant allele is always expressed, even if only one copy is present. A recessive allele is only expressed if two copies are present (therefore no dominant allele present)."
- "If the two alleles present are the same the organism is homozygous for that trait, but if the alleles are different they are heterozygous."
- "Most characteristics are a result of multiple genes interacting, rather than a single gene."
- "Students should be able to understand the concept of probability in predicting the results of a single gene cross, but recall that most phenotype features are the result of multiple genes rather than single gene inheritance." (MS 2e)
- "Students should be able to use direct proportion and simple ratios to express the outcome of a genetic cross." (MS 1c, 3a)
- "Students should be able to complete a Punnett square diagram and extract and interpret information from genetic crosses and family trees." (MS 2c, 4a)
- "(HT only) Students should be able to construct a genetic cross by Punnett square diagram and use it to make predictions using the theory of probability." (MS 2e, WS 1.2)

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Two copies of most genes; alleles (th1) | base | 4.6.1.4 | all four | OK |
| R2 | Dominant / recessive; capital / lowercase convention (th1; key_note; common_mistake) | base | 4.6.1.4 | all four | OK |
| R3 | Genotype / phenotype; homozygous / heterozygous (th1; key_note) | base | 4.6.1.4 | all four | OK |
| R4 | Carrier (th1; common_mistake; key_note; q2) | base | 4.6.1.4; 4.6.1.5 | all four | OK (not a spec term; used by 4.6.1.5's CF context) |
| R5 | Brown/blue eye colour as a single gene B/b (th1, th2; FIFA) | base skill, wrong example | 4.6.1.4 | all four | IMPRECISE (F3) |
| R6 | Completing a Punnett square; reading ratios 1:2:1, 3:1, % (th2; q1) | base | 4.6.1.4 | all four | OK |
| R7 | Constructing a cross from parents' genotypes (th2 "How to draw one"; FIFA step F "Draw a Punnett square") | **higher** | 4.6.1.4 (HT only) | all four | **ROUTE** — shown as a base skill (F2) |
| R8 | Probability: each pregnancy independent; fraction / % / ratio (th3; q3) | base | 4.6.1.4 (MS 2e) | all four | OK |
| R9 | Genetic counsellors (th3) | base (context) | — | all four | OK |
| R10 | `higher`: codominance, ABO blood groups, IA IB IO | **not in spec** | — | CH TH | **OFF-SPEC** (F1) |
| R11 | Gamete, chromosome, gene defined; mice fur colour, red-green colour blindness; most characteristics are multi-gene; genotype acts at molecular level; family trees | base | 4.6.1.4 | — | **GAP** (F4) |
| R12 | q1 Bb × Bb recessive fraction | base | 4.6.1.4 | all four | OK |
| R13 | q2 carrier of CF | base | 4.6.1.4; 4.6.1.5 | all four | OK |
| R14 | q3 meaning of 1 in 4 | base | 4.6.1.4 (MS 2e) | all four | OK |
| R15 | FIFA: Bb × Bb → P(blue) | construct = higher; complete/read = base | 4.6.1.4 | all four | ROUTE (F2) + IMPRECISE example (F3) |
| — | RP, equations | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | two copies of most genes, one on each chromosome of a pair | OK | ("most" — correct: males have one X.) | 4.6.1.4 |
| C2 | th1 | dominant expressed with one copy; recessive only with two | OK | Spec words. | 4.6.1.4 |
| C3 | th1 | "B for brown eyes … b for blue eyes" | IMPRECISE | Eye colour is controlled by several genes; it is not a one-gene dominant/recessive trait. Spec's single-gene examples: fur colour in mice, red-green colour blindness. | 4.6.1.4 |
| C4 | th1 | genotype = alleles; phenotype = observable characteristic | OK | — | 4.6.1.4 |
| C5 | th1 | homozygous same, heterozygous different | OK | — | 4.6.1.4 |
| C6 | th1 | carrier = Bb, appears normal, can pass the allele on | OK | — | 4.6.1.5 |
| C7 | th2 | Bb × Bb → BB, Bb, Bb, bb; 1:2:1; 3:1; 75% / 25% | OK | ✓ | 4.6.1.4 |
| C8 | th2 | Bb × BB → BB, BB, Bb, Bb; all dominant; 50% carriers | OK | ✓ (heading "Carrier × Normal" fine) | 4.6.1.4 |
| C9 | th3 | 25% per pregnancy, independent; not exactly 1 in 4; small samples vary; 1/4 = 25% = 1 in 4 | OK | — | 4.6.1.4 (MS 2e) |
| C10 | `higher` | codominance; IA, IB codominant, IO recessive; AB = IAIB | OFF-SPEC | True; not in 8461 or 8464 (removed from AQA at the 2016 spec). Not HT. | — |
| C11 | common_mistake | carrier is not "mildly" affected; Bb × Bb → 25% bb | OK | — | 4.6.1.4 |
| C12 | key_note | as th1 | OK | — | 4.6.1.4 |
| C13 | FIFA F | "Draw a Punnett square: Bb × Bb" | OK, HT | Constructing a cross is HT only. | 4.6.1.4 HT |
| C14 | FIFA I | BB, Bb, Bb, bb → 1:2:1 | OK | ✓ | — |
| C15 | FIFA F | only bb blue = 1 out of 4 | OK | ✓ (within the stated model — see C3) | — |
| C16 | FIFA A | 1/4 = 25% | OK | ✓ | — |
| C17 | CFIFA Convert `[NEW]` | "Nothing to convert — this is a genetics probability calculation with no physical units involved." | OK | Examined ✓. | CFIFA amendment |
| C18 | q1 key | Bb × Bb recessive = 1/4 | OK | ✓ | — |
| C19 | q1 wx1 (opt 2 "1/2") | 50% from bb × Bb | OK | aligned ✓; Bb × bb → 2 Bb : 2 bb ✓ | — |
| C20 | q1 wx2 (opt 3 "3/4") | 3/4 is the dominant proportion | OK | aligned ✓ | — |
| C21 | q1 wx3 (opt 4 "0") | two heterozygotes can produce bb | OK | aligned ✓ | — |
| C22 | q2 key | carrier = Ff, healthy, can pass it on | OK | — | 4.6.1.5 |
| C23 | q2 wx1 (opt 2 "mildly") | no symptoms; masked by dominant | OK | aligned ✓ | — |
| C24 | q2 wx2 (opt 3 "ff") | ff has the condition; carrier is Ff | OK | aligned ✓ | — |
| C25 | q2 wx3 (opt 4 "immune system") | CF is genetic, not an infection | OK | aligned ✓ | — |
| C26 | q3 key | each pregnancy independently 25% | OK | — | MS 2e |
| C27 | q3 wx1 (opt 2 "exactly one in four") | 0–4 affected possible | OK | aligned ✓ | — |
| C28 | q3 wx2 (opt 3 "fourth will definitely") | independence; coin | OK | aligned ✓ | — |
| C29 | q3 wx3 (opt 4 "chance reduces") | chance stays 25% | OK | aligned ✓ | — |
| C30 | matching (to be replaced) | definitions | OK | — | — |

Count: **0 WRONG**. OFF-SPEC: F1. ROUTE: F2. IMPRECISE: F3. GAP: F4. All three quiz items usable on all four routes. All arithmetic ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| FIFA | Its first step constructs the cross (HT only); its trait (eye colour) is not single-gene. | Do not use as written (F2, F3). Design writes the worked example on mouse fur colour; base = complete a given square; HT = construct it. |
| q1, q2, q3 | — | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Dominant means more common" / "dominant means stronger or better".
- Carriers "have it mildly".
- 1 in 4 means "exactly one of four children"; after three unaffected, the fourth "must" be affected.
- Gametes written with two alleles (Bb) instead of one (B or b) in the square's headings.
- Genotype and phenotype swapped.
- "Every characteristic is one gene" — most are many genes.

**Command words**: Explain the term …, Complete the Punnett square, Give the ratio / probability, Use the family tree to …, Construct a genetic cross (HT).

**Required practical**: none.

**Calculations**: probability from a single-gene cross (fraction, %, ratio, direct proportion). No units. CFIFA Convert = "nothing to convert"; the real conversion pupils make is between forms (1/4 ↔ 25% ↔ "1 in 4" ↔ a 3:1 phenotype ratio — reading 3:1 as "1 in 3" is a classic error).

## 6. Verdict
SOURCE OK WITH FLAGS. All science and arithmetic correct; all three quiz items usable on all four routes. The `higher` field (codominance) is off-spec; the real HT layer — constructing the cross — is shown as base; the worked example uses eye colour, which the spec's own "most characteristics are multi-gene" point contradicts; family trees, the spec's single-gene examples and three of the ten terms (gamete, chromosome, gene) are missing.

**For Mide:** nothing. All settled spec facts.
