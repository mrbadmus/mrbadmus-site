# Examination — Sex Determination (sex-determination) — AQA 8464 4.6.1.6 / 8461 4.6.1.8
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-9/04-checked-science-source/biology-4.6.3.3-sex-determination.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Version 1.1, 04 Oct 2019) and `AQA-8461-spec.txt` (Version 1.0, 21 Apr 2016). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/biology.md` row `sex-determination`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The site's "4.6.3.3" is its internal number; true refs are 8464 **4.6.1.6** and 8461 **4.6.1.8**. Route copies identical except `higher` (TH text on CH/TH; `null` on CF/TF).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 Combined Trilogy | **4.6.1.6** | Sex determination | base |
| 8461 Biology | **4.6.1.8** | Sex determination | base |
| Supporting | 8464 4.6.1.2 / 8461 4.6.1.2 Meiosis (gametes carry one set) | | base |

Spec statements (verbatim, 8464 4.6.1.6 = 8461 4.6.1.8):
- "Ordinary human body cells contain 23 pairs of chromosomes. 22 pairs control characteristics only, but one of the pairs carries the genes that determine sex. • In females the sex chromosomes are the same (XX). • In males the chromosomes are different (XY)."
- "Students should be able to carry out a genetic cross to show sex inheritance."
- "Students should understand and use direct proportion and simple ratios in genetic crosses." (MS 1c, 3a)

Note: unlike 4.6.1.4, carrying out the sex cross here is **unlabelled — base on every route**.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | 23 pairs; one pair sex chromosomes; XX female, XY male (th1; key_note) | base | 4.6.1.6 | all four | OK |
| R2 | Y smaller, fewer genes; SRY triggers testes (th1) | not in spec | — | all four | OFF-SPEC detail (F3) |
| R3 | 22 other pairs = "autosomes", same in males and females (th1) | base (term off-spec) | 4.6.1.6 ("22 pairs control characteristics only") | all four | OK; the name is not required (F3) |
| R4 | Eggs all X; sperm X or Y ~50/50; sperm decides sex (th2; common_mistake; key_note) | base | 4.6.1.6 + 4.6.1.2 | all four | OK |
| R5 | Punnett square XX × XY → 50% female, 50% male (th3) | base | 4.6.1.6 ("carry out a genetic cross") | all four | OK |
| R6 | Probability, not a guarantee; ~50:50 population ratio (th2, th3) | base | 4.6.1.6 (MS 1c, 3a) | all four | OK |
| R7 | `higher`: X-linked inheritance, colour blindness, haemophilia, carrier females | **not in spec** | — | CH TH | **OFF-SPEC** (F1) |
| R8 | q1 what determines sex | base | 4.6.1.6 | all four | OK |
| R9 | q2 three daughters → P(son) | base | 4.6.1.6 | all four | key wording IMPRECISE (F2) |
| — | RP, FIFA, equations | none | — | — | correct (no FIFA in source; the cross is a base calculation — see brief) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | sex chromosomes are one of 23 pairs; XX female; XY male | OK | Spec words. | 4.6.1.6 |
| C2 | th1 | Y smaller, fewer genes; SRY triggers testis development | OK, OFF-SPEC | True; not in spec. | — |
| C3 | th1 | 22 autosome pairs same in males and females | OK | Spec: "22 pairs control characteristics only". | 4.6.1.6 |
| C4 | th2 | all eggs carry X; sperm ~50% X, ~50% Y | OK | — | 4.6.1.6; 4.6.1.2 |
| C5 | th2 | X sperm → XX female; Y sperm → XY male; sperm determines sex | OK | — | 4.6.1.6 |
| C6 | th2 | 50% chance of each sex per pregnancy | OK | (At GCSE; real birth ratio ≈ 105 boys : 100 girls — not required.) | 4.6.1.6 |
| C7 | th3 | Punnett XX × XY → XX 50%, XY 50%; population ratio ~50:50; probability not guarantee | OK | ✓ | 4.6.1.6 |
| C8 | `higher` | X-linked: no allele on Y; males express a single recessive X allele; colour blindness, haemophilia more common in males; carrier females | OK science, OFF-SPEC | True; not in 8464 or 8461 at any tier. Red-green colour blindness appears in the spec only as a single-gene example (4.6.1.4). | — |
| C9 | common_mistake | sperm determines sex; women historically blamed | OK | — | 4.6.1.6 |
| C10 | key_note | as th1–th3 | OK | — | — |
| C11 | matching (to be replaced) | XX, XY, eggs X, sperm X/Y, 50% | OK | — | — |
| C12 | q1 key | which sperm (X or Y) fertilises the egg | OK | — | 4.6.1.6 |
| C13 | q1 wx1 (opt 2 "X and Y eggs") | eggs all X | OK | aligned ✓ | — |
| C14 | q1 wx2 (opt 3 "temperature") | temperature decides sex in some reptiles, not humans | OK | aligned ✓; reptile fact true | — |
| C15 | q1 wx3 (opt 4 "age of parents") | age doesn't determine sex | OK | aligned ✓ | — |
| C16 | q2 key | "50% — each pregnancy is independent, the sex ratio is always 50:50" | **IMPRECISE** | 50% ✓ and independence ✓, but "the sex ratio is always 50:50" is false and contradicts the lesson's own th3 ("approximately 50:50 … the probability, not a guarantee"); the very family in the question is 3:0. | 4.6.1.6 |
| C17 | q2 wx1 (opt 2 "due a boy") | independence; gambler's fallacy | OK | aligned ✓ | — |
| C18 | q2 wx2 (opt 3 "produce more girls") | runs happen by chance; X and Y sperm equal | OK | aligned ✓ | — |
| C19 | q2 wx3 (opt 4 "0%") | ~50/50 sperm regardless | OK | aligned ✓ | — |

Count: **0 WRONG**. OFF-SPEC: F1, F3. IMPRECISE: F2 (q2 key).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | — | Usable on all four routes. |
| q2 | Key says "the sex ratio is always 50:50" (F2). | Do not use as written. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "The mother decides the sex" / eggs can be X or Y.
- Gametes written as XX or XY instead of X, X and X, Y.
- "After three girls a boy is more likely."
- "Males have 23 pairs plus a Y" / sex chromosomes outside the 23 pairs.
- Probability given as "50:50" when a fraction or % is asked; 1:1 read as "1 in 1".

**Command words**: Complete the genetic diagram, Give the probability / ratio, Explain why the probability is the same for each child, Describe.

**Required practical**: none.

**Calculations**: the XX × XY cross → probability of a boy/girl 1/2 = 50% = 0.5, ratio 1:1 (base). No units.

## 6. Verdict
SOURCE OK WITH FLAGS. All on-spec science correct; q1 usable on all routes. The `higher` field (sex linkage) is off-spec and should go; q2's key states the sex ratio is "always 50:50", which the lesson itself denies — not usable as written.

**For Mide:** nothing. All settled spec facts.
