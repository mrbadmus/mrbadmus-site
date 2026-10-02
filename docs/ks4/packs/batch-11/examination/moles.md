# Examination — Moles (moles) — AQA 8464 5.3.2.1 / 8462 4.3.2.1 (HT only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.3.2.1-moles.md`.
Spec sources read as text: `AQA-8462-spec.txt` 4.3.1.2, 4.3.2.1; `AQA-8464-spec.txt` 5.3.1.2, 5.3.2.1 (identical wording). No equation sheet applies (chemistry). Route audit read: `chemistry.md` row `moles` (OK, HT, CH TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Both route copies identical; no `higher` field.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.3.2.1** | Moles | (HT only) |
| 8462 | **4.3.2.1** | Moles | (HT only) |
| Supporting | 8464 5.3.1.2 / 8462 4.3.1.2 relative formula mass; % by mass | | base |

Spec statement (verbatim, 8464 = 8462): "Chemical amounts are measured in moles. The symbol for the unit mole is mol. The mass of one mole of a substance in grams is numerically equal to its relative formula mass. One mole of a substance contains the same number of the stated particles, atoms, molecules or ions as one mole of any other substance. The number of atoms, molecules or ions in a mole of a given substance is the Avogadro constant. The value of the Avogadro constant is 6.02 x 10²³ per mole. Students should understand that the measurement of amounts in moles can apply to atoms, molecules, ions, electrons, formulae and equations, for example that in one mole of carbon (C) the number of atoms is the same as the number of molecules in one mole of carbon dioxide (CO₂). Students should be able to use the relative formula mass of a substance to calculate the number of moles in a given mass of that substance and vice versa."

8464 5.3.1.2 (base): "Students should be able to calculate the percentage by mass in a compound given the relative formula mass and the relative atomic masses."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Mole as a counting unit; Avogadro constant 6.02 × 10²³ (th1; key_note) | higher | 5.3.2.1 (HT only) | OK (C2 imprecise) |
| R2 | Mass of 1 mol in g = Mr (th1; key_note) | higher | 5.3.2.1 | OK |
| R3 | n = m ÷ Mr and rearrangements (th2; equations 1–2; FIFA) | higher | 5.3.2.1 | OK |
| R4 | particles = n × Nₐ (th2 ex 4; th3; equation 3; q2) | higher | 5.3.2.1 | OK |
| R5 | % mass of an element in a compound (th3; key_note; equation 4) | **base** | 5.3.1.2 | OK; ROUTE note — a recap here; its home is relative-formula-mass (CF CH TF TH) |
| R6 | molecules vs atoms counted (common_mistake) | higher | 5.3.2.1 (spec's C vs CO₂ example) | OK |
| R7 | kg → g before dividing (common_mistake) | higher | 5.3.2.1; MS 3c | OK |
| R8 | q1, q2 | higher | 5.3.2.1 | OK (q2 wx2 misaligned) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | mole, symbol mol; same number of particles; Nₐ = 6.02 × 10²³ | OK | ✓ spec wording | 5.3.2.1 |
| C2 | th1 | "This number is chosen because: 1 mole of carbon-12 atoms has a mass of exactly 12 grams." | IMPRECISE | Pre-2019 definition; since the 2019 SI redefinition Nₐ is fixed and 12 g is no longer exact. Spec needs only "mass of one mole in grams is numerically equal to its Mr". | 5.3.2.1 |
| C3 | th1 | H₂O 18 g; NaCl 58.5 g, formula units; Fe 56 g | OK | ✓ | 4.3.1.2 |
| C4 | th2 | 44 ÷ 44 = 1; 9 ÷ 18 = 0.5; 0.25 × 100 = 25 g | OK | ✓ | 5.3.2.1 |
| C5 | th2 | "What mass of NaOH contains 3.01 × 10²³ molecules?" → 0.5 mol → 20 g | IMPRECISE | Arithmetic ✓. NaOH is ionic: formula units, not molecules (th1 gets this right for NaCl). | 5.3.2.1 |
| C6 | th3 | 2 × 6.02 × 10²³ = 1.204 × 10²⁴; 0.1 × 6.02 × 10²³ = 6.02 × 10²² | OK | ✓ | MS 1b |
| C7 | th3; equation 4 | % O in H₂SO₄ = 64 ÷ 98 × 100 = 65.3 % | OK | ✓ (65.31). Base, 5.3.1.2. | 5.3.1.2 |
| C8 | common_mistake | grams first; 1 mol H₂O = 6.02 × 10²³ molecules = 3 × 6.02 × 10²³ atoms | OK | ✓ | 5.3.2.1 |
| C9 | key_note | "The molar mass = Mr in g/mol." | OK | "Molar mass" is not a spec term; harmless. | — |
| C10 | variables | n mol; m g; Mr no unit; Nₐ mol⁻¹, 6.02 × 10²³ | OK | ✓ | 5.3.2.1 |
| C11 | FIFA | 27 ÷ 27 = 1 mol Al | OK | ✓. "Ar = 27" in the question with "mass ÷ Mr" in the formula — for an element Ar plays the part of Mr; say so once. | 5.3.2.1 |
| C12 | Convert (NEW) | "Nothing to convert — the mass is already in grams, matching the g/mol basis of Ar." | IMPRECISE → corrected | Ar has no unit. Corrected line in the source file. | 5.3.1.2 |
| C13 | q1 key | 9.8 ÷ 98 = 0.1 mol | OK | ✓ | 5.3.2.1 |
| C14 | q1 opt1 / wx1 | 10 mol = 98 ÷ 9.8 / divided the wrong way | OK | Aligned ✓ | — |
| C15 | q1 opt2 / wx2 | 960.4 = 9.8 × 98 / multiplied | OK | Aligned ✓; 9.8 × 98 = 960.4 ✓ | — |
| C16 | q1 opt3 / wx3 | 0.01 = 9.8 ÷ 980 / wrong Mr | OK | Aligned ✓ | — |
| C17 | q2 key | 3.01 × 10²³ ÷ 6.02 × 10²³ = 0.5 mol; × 100 = 50 g | OK | ✓. A two-step chain (rule 3). | 5.3.2.1 |
| C18 | q2 opt1 / wx1 | "100 g — 1 mole has mass 100 g regardless" / "HALF the Avogadro constant… 0.5 mol… 50 g" | OK | Aligned ✓ | — |
| C19 | q2 opt2 / wx2 | "30100 g — multiplying particle count by Mr" / "The Mr gives mass PER MOLE — 3.01 × 10²³ is only 0.5 mol, not 1 mol." | IMPRECISE | **Misaligned**: wx2 answers option 1's error (assuming 1 mol), not option 2's. And option 2's number does not follow its own stated error: 3.01 × 10²³ × 100 = 3.01 × 10²⁵, not 30100. Still a wrong option, so marking is unaffected. | — |
| C20 | q2 opt3 / wx3 | "0.5 g — confusing moles with grams" / multiply by Mr | OK | Aligned ✓ | — |
| C21 | matching (to be replaced) | 1 mol; 88 g; 0.1 mol; 3.01 × 10²³; 40 % | OK | All ✓ | — |

Count: **0 WRONG**. IMPRECISE: C2, C5, C12 (corrected), C19. ROUTE note: R5. 14 calculations rechecked, all ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct, HT | Usable on CH TH. |
| q2 | correct key; wx2 misaligned, option 2's figure inconsistent | Usable on CH TH; if Design shows per-option feedback, flag MOL-F1 stands. |
| FIFA | correct | Keep; it is the "nothing to convert" example. The kg → g example (common_mistake) is the convert case. |

## 5. Calculations and chains (rule 3)
- n = m ÷ Mr (and m = n × Mr, Mr = m ÷ n) — one step. Convert kg → g (× 1000).
- particles = n × Nₐ (and n = particles ÷ Nₐ) — one step; standard form.
- **Chain (th2 ex 4; q2):** Step 1 n = particles ÷ Nₐ (3.01 × 10²³ ÷ 6.02 × 10²³ = 0.5 mol) → Step 2 m = n × Mr (0.5 × 100 = 50 g). Reverse chain also expected: mass → moles → particles.
- % by mass — one step when Mr is given; a chain when it is not (Step 1 Mr from Ar; Step 2 %). Base.

## 6. Verdict
SOURCE OK WITH FLAGS. All 14 calculations correct; both quiz keys correct; q2's second explanation does not match its option. Minor wording (molecules for NaOH; carbon-12 rationale; Ar given a unit). % by mass is base content riding on an HT page. Nothing for Mide.
