# Examination — Relative Atomic Mass, Atomic Number and Isotopes (relative-atomic-mass) — AQA 8464 5.1.1.6 (+5.1.1.5) / 8462 4.1.1.6 (+4.1.1.5)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.1.1.6-relative-atomic-mass.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.1.1.5–5.1.1.6, 6.4.1.2; `AQA-8462-spec.txt` (v1.1) 4.1.1.5–4.1.1.6. Both spec texts searched for "mass spectr": **no match** in 8462 or 8464. No equation sheet applies: chemistry papers carry none, and the 8464 sheet is physics only. Route audit row `relative-atomic-mass`: base, OK. Physics twin for isotopes: 8464 6.4.1.2 / 8463 4.4.1.2 (batch 5 `structure-of-atom` supporting).

Conventions: as in model-of-the-atom. Route copies identical except `higher`: TH text on CH/TH, `null` on CF/TF.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.1.1.6** | Relative atomic mass | base |
| 8462 | **4.1.1.6** | Relative atomic mass | base |
| Supporting | 8464 5.1.1.5 / 8462 4.1.1.5 (atomic number, mass number, isotopes, notation) | | base |
| Not in spec | mass spectrometry / mass spectra | | — |

Spec statements (verbatim, 8464 = 8462):
- 5.1.1.6: "The relative atomic mass of an element is an average value that takes account of the abundance of the isotopes of the element. Students should be able to calculate the relative atomic mass of an element given the percentage abundance of its isotopes."
- 5.1.1.5: "The sum of the protons and neutrons in an atom is its mass number. Atoms of the same element can have different numbers of neutrons; these atoms are called isotopes of that element. Atoms can be represented as shown in this example: [²³₁₁Na]. Students should be able to calculate the numbers of protons, neutrons and electrons in an atom or ion, given its atomic number and mass number."
- 5.1.1.4: "The number of protons in an atom of an element is its atomic number."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Atomic number = protons; mass number = p + n; neutrons = A − Z (th1; key_note; equations 1–2) | base | 5.1.1.4–5 | all four | OK; periodic-table sentence IMPRECISE (F4) |
| R2 | Sodium-23 worked count (th1) | base | 5.1.1.5 | all four | OK |
| R3 | Isotopes: same protons, different neutrons (th2; common_mistake; q1) | base | 5.1.1.5 | all four | OK |
| R4 | Same chemical / different physical properties (th2; common_mistake; key_note) | base context (not stated in spec; true) | — | all four | OK |
| R5 | Carbon and chlorine isotope examples (th2) | base | 5.1.1.5–6 | all four | OK |
| R6 | Ar = weighted mean of isotopes; often non-integer (th3; key_note; common_mistake) | base | 5.1.1.6 | all four | IMPRECISE "NOT a whole number" (F3) |
| R7 | Ar = Σ(% × mass number) ÷ 100; chlorine example (th3; equation 3) | base | 5.1.1.6 | all four | OK |
| R8 | FIFA boron | base | 5.1.1.6 | all four | **Insert step WRONG** (F1) |
| R9 | `higher`: mass spectrometry; interpret mass spectra; non-integer Ar | **not in spec** / base | — / 5.1.1.6 | CH TH only | OFF-SPEC + ROUTE (F2) |
| R10 | q1 Cl-35 vs Cl-37 | base | 5.1.1.5 | all four | OK (wx1 IMPRECISE, F5) |
| R11 | q2 Ar from 60/40 | base | 5.1.1.6 | all four | OK |
| — | RP | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | atomic number = protons, unique to each element; C has 6, Fe has 26 | OK | ✓ | 5.1.1.4 |
| C2 | th1 | mass number = protons + neutrons; neutrons = A − Z | OK | — | 5.1.1.5 |
| C3 | th1 | Na-23: 11 p, 11 e, 12 n | OK | ✓ | — |
| C4 | th1 | "In the periodic table, the ATOMIC NUMBER is the SMALLER number" | IMPRECISE | On the AQA periodic table the larger number is the **relative atomic mass**, not the mass number. The mass number belongs to one isotope's symbol (²³₁₁Na). Teach the two separately (F4). | 5.1.1.5–6 |
| C5 | th2 | isotopes: same atomic number, different mass number | OK | — | 5.1.1.5 |
| C6 | th2 | same chemical properties (same electrons); different physical properties (density, diffusion rate) | OK, context | True; not stated in the spec. | — |
| C7 | th2 | C-12 6p 6n ~98.9%; C-13 6p 7n ~1.1%; C-14 6p 8n radioactive, dating | OK | ✓ (C-14 is a trace.) | — |
| C8 | th2 | Cl-35 17p 18n ~75%; Cl-37 17p 20n ~25%; Ar ≈ 35.5 | OK | Real values 75.8 % / 24.2 %. ✓ | — |
| C9 | th3 | Ar = weighted average relative to 1/12 of a C-12 atom | OK | The C-12 standard is beyond GCSE but true. Spec: "an average value that takes account of the abundance of the isotopes". | 5.1.1.6 |
| C10 | th3 | "Because most elements have multiple isotopes… Ar is NOT a whole number" | IMPRECISE | **Often** not a whole number. Many Ar values on the AQA table are whole numbers (C 12, O 16, Na 23), and an element with one stable isotope (F, Na, Al) has an Ar close to a whole number (F3). | 5.1.1.6 |
| C11 | th3; equation 3 | Ar = Σ(% abundance × mass number) ÷ 100 | OK | The GCSE form. Mass number stands in for isotope relative mass. | 5.1.1.6 |
| C12 | th3 | Cl: (75 × 35 + 25 × 37) ÷ 100 = (2625 + 925) ÷ 100 = 35.5 | OK | ✓ all three steps. | — |
| C13 | `higher` | mass spectrometry; mass spectra (abundance vs m/z) | OFF-SPEC | Not in 8462 or 8464 (searched). A-level content (F2). | — |
| C14 | `higher` | "non-integer Ar values result from isotope mixtures" | ROUTE | True and **base**. It is already in the theory for every route (F2). | 5.1.1.6 |
| C15 | common_mistake | weighted not simple average; 50/50 → 36; heavier isotope has less influence (Cl) | OK | ✓ | 5.1.1.6 |
| C16 | key_note | as R1–R6 | OK | — | — |
| C17 | equations 1–2 | mass number = p + n; neutrons = A − Z | OK | — | 5.1.1.5 |
| C18 | FIFA F | Ar = Σ(% abundance × mass number) ÷ 100 | OK | — | 5.1.1.6 |
| C19 | FIFA I | "Ar = (20 × 10) + (80 × 11) ÷ 100" | **WRONG** | The outer brackets are missing. By order of operations this line equals 200 + 8.8 = 208.8, not 10.8. Correct line: **Ar = [(20 × 10) + (80 × 11)] ÷ 100**. Frozen text stays as it is; Design must not show it as written (F1). | MS 1a |
| C20 | FIFA F (fine-tune) | (200 + 880) ÷ 100 = 1080 ÷ 100 | OK | ✓ correctly bracketed. | — |
| C21 | FIFA A | Ar = 10.8 | OK | ✓. Real boron is 19.9 % B-10 and 80.1 % B-11, Ar 10.81. | — |
| C22 | CFIFA Convert `[NEW]` | "Nothing to convert — the percentage abundances and the isotope mass numbers are already in matching, dimensionless units for the formula." | OK | Examined ✓. | CFIFA amendment |
| C23 | matching (to be replaced) | five term–definition pairs | OK | — | — |
| C24 | q1 key (opt 0) | same atomic number (17 p, 17 e); Cl-35 18 n, Cl-37 20 n | OK | ✓ | 5.1.1.5 |
| C25 | q1 wx1 ↔ opt 1 "Same: mass number. Different: atomic number and proton count." | "If mass numbers were the same they would be identical — isotopes are DEFINED by having different mass numbers." | IMPRECISE, aligned ✓ | It does not deal with the option's other half: a different atomic number makes a different **element**. Not false, so usable (F5). | 5.1.1.5 |
| C26 | q1 wx2 ↔ opt 2 "Same: everything" | same chemistry, but differ in neutrons and mass | OK, aligned ✓ | — | — |
| C27 | q1 wx3 ↔ opt 3 "Same neutron number, different proton number" | different protons → different elements | OK, aligned ✓ | — | 5.1.1.4 |
| C28 | q2 key (opt 0) | (60 × 63 + 40 × 65) ÷ 100 = 6380 ÷ 100 = 63.8 | OK | 3780 + 2600 = 6380 ✓ | 5.1.1.6 |
| C29 | q2 wx1 ↔ opt 1 "64.0 — simple average" | 64 only if 50/50; more of the lighter isotope pulls it below | OK, aligned ✓ | — | — |
| C30 | q2 wx2 ↔ opt 2 "128 — sum" | adding mass numbers has no meaning | OK, aligned ✓ | — | — |
| C31 | q2 wx3 ↔ opt 3 "63 — most abundant only" | ignores the 40 % at 65 | OK, aligned ✓ | — | — |

Count: **1 WRONG** (C19, a frozen FIFA step). IMPRECISE: C4, C10, C25. OFF-SPEC/ROUTE: C13–C14. All 15 numbers and 9 calculation steps were rechecked. All six wrong_explanations are aligned, checked by reading each one.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| FIFA Insert step | missing brackets: as written it evaluates to 208.8 | Use the worked example with the Insert line corrected to `[(20 × 10) + (80 × 11)] ÷ 100`. The other three steps and the answer stand. |
| q1 | wx1 imprecise, not false | Usable on all four routes. |
| q2 | — | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- Simple average instead of weighted (q2 opt 1).
- Dividing by 2 or by the number of isotopes instead of by 100.
- Missing brackets, so only the second product is divided. The frozen FIFA makes this error itself.
- "Isotopes have different numbers of protons / electrons."
- "Isotopes react differently."
- Rounding the answer to a whole number "because mass numbers are whole".

**Command words**: Calculate the relative atomic mass, Explain why Ar is not a whole number, What is meant by isotopes, Give the number of neutrons.

**Typical questions** ⚑ examiner-drafted
- *Copper has two isotopes: 69 % copper-63 and 31 % copper-65. Calculate the relative atomic mass of copper. Give your answer to 1 decimal place. [2]*: (69 × 63 + 31 × 65) ÷ 100 (1); = 63.6 (1).
- *Explain why the relative atomic mass of chlorine is not a whole number. [2]*: chlorine has isotopes / atoms with different mass numbers (1); Ar is an average that takes account of their abundance (1).
- *What is meant by isotopes? [2]*: atoms of the same element / same number of protons (1); different numbers of neutrons (1).

**Required practical**: none.

**Equations**: Ar = Σ(% abundance × mass number) ÷ 100. "Learn it": chemistry papers have no equation sheet. It is a weighted sum, so a formula triangle does not apply.

## 6. Verdict
SOURCE HAS ERRORS. One frozen worked-example step is wrong: the FIFA Insert line has no outer brackets and, as written, gives 208.8. The rest of the science is correct and both frozen quiz items are usable on all four routes. The `higher` field is off-spec (mass spectrometry is not in GCSE) and must not be built as an HT layer. Every point in this lesson is base. Minor theory imprecisions: "Ar is NOT a whole number"; the periodic table's larger number called the mass number.

**For Mide:** nothing.
