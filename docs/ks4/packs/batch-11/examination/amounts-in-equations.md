# Examination — Amounts of Substances in Equations (amounts-in-equations) — AQA 8464 5.3.2.2 / 8462 4.3.2.2 (HT only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.3.2.2-amounts-in-equations.md`.
Spec sources read as text: `AQA-8462-spec.txt` 4.3.1.2, 4.3.2.1–4.3.2.2, 4.3.3.1–4.3.3.2; `AQA-8464-spec.txt` 5.3.1.2, 5.3.2.1–5.3.2.2 (identical wording), and searched for yield / atom economy — absent from 8464. No equation sheet applies (chemistry). Route audit read: `chemistry.md` rows `amounts-in-equations` (OK, HT, CH TH), `percentage-yield` (TF TH, 4.3.3.1), `atom-economy` (TF TH, 4.3.3.2).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Both route copies identical; no `higher` field.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.3.2.2** | Amounts of substances in equations | (HT only) |
| 8462 | **4.3.2.2** | Amounts of substances in equations | (HT only) |
| Supporting | 8464 5.3.2.1 / 8462 4.3.2.1 Moles | | (HT only) |
| Off-topic, carried in the data | 8462 4.3.3.1 Percentage yield; 4.3.3.2 Atom economy | | (chemistry only); theoretical mass of product is (HT only) |

Spec statement (verbatim, 8464 = 8462): "The masses of reactants and products can be calculated from balanced symbol equations. Chemical equations can be interpreted in terms of moles. For example: Mg + 2HCl → MgCl₂ + H₂ shows that one mole of magnesium reacts with two moles of hydrochloric acid to produce one mole of magnesium chloride and one mole of hydrogen gas. Students should be able to: calculate the masses of substances shown in a balanced symbol equation; calculate the masses of reactants and products from the balanced symbol equation and the mass of a given reactant or product."

8462 4.3.3.2 (chemistry only), the formula as printed: "Relative formula mass of desired product from equation ÷ Sum of relative formula masses of all reactants from equation × 100".

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Coefficients = molar ratio (th1; common_mistake; key_note) | higher | 5.3.2.2 (HT only) | OK |
| R2 | Reacting-mass method (th2; key_note; FIFA) | higher | 5.3.2.2 (HT only) | OK; method numbering IMPRECISE (C5) |
| R3 | n = m ÷ Mr (equation 1) | higher | 5.3.2.1 (HT only) | OK |
| R4 | Theoretical/actual yield, reasons, % yield (th3; key_note; equation 2) | **triple** (theoretical mass from an equation: triple-higher) | 8462 4.3.3.1 (chemistry only) | OFF-SPEC on CH; off-topic (own page `percentage-yield`) |
| R5 | Atom economy (th3; key_note; equation 3) | triple | 8462 4.3.3.2 (chemistry only) | **WRONG formula**; off-topic (own page `atom-economy`) |
| R6 | q1 — moles of NH₃ from H₂ | higher | 5.3.2.2 | OK |
| R7 | q2 — % yield | triple | 8462 4.3.3.1 (chemistry only) | OK science; TH only |
| — | "calculate the masses of substances shown in a balanced symbol equation" | higher | 5.3.2.2 | GAP — not taught as such |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | 2Mg + O₂ → 2MgO = 2 : 1 : 2 | OK | ✓ | 5.3.2.2 |
| C2 | th1 | Mg + 2HCl → MgCl₂ + H₂: 1 : 2 : 1 : 1 | OK | The spec's own example ✓ | 5.3.2.2 |
| C3 | th1 | N₂ + 3H₂ → 2NH₃: 1 : 3 : 2 | OK | ✓ | — |
| C4 | th1 | "the molar ratio … is always maintained, whatever the actual quantities used" | OK | (When one reactant is in excess, the ratio applies to what reacts — limiting reactants, 5.3.2.4.) | 5.3.2.4 |
| C5 | th2 | method lists Steps 1–5; the example numbers Steps 1–4 with different meanings (method Step 1 = write the equation; example Step 1 = ratio) | IMPRECISE | Re-cut to one numbered method used identically in the example and around the FIFA. | — |
| C6 | th2 | 4.8 ÷ 24 = 0.2 mol; 1 : 1; 0.2 × 40 = 8.0 g | OK | ✓ | 5.3.2.2 |
| C7 | th3 | theoretical vs actual yield; actual ≤ theoretical; reasons: reversible, side reactions, lost in separation, impure reactants | OK (off-topic) | Matches 4.3.3.1's three reasons; "impure reactants" is an acceptable addition. Chemistry only. | 4.3.3.1 |
| C8 | th3; equation 2; key_note | % yield = actual ÷ theoretical × 100; 7.2 ÷ 8.0 × 100 = 90 % | OK (off-topic) | ✓ AQA wording: "mass of product actually made ÷ maximum theoretical mass of product × 100". Chemistry only — off-spec on CH. | 4.3.3.1 |
| C9 | th3; equation 3; key_note | "Atom economy = (Mr of desired products ÷ Mr of ALL products) × 100" | **WRONG** | AQA's formula: (Mr of desired product from equation ÷ sum of Mr of all REACTANTS from equation) × 100. Products-denominator equals it only when every product is counted with its coefficient (conservation, 4.3.1.2); as worded ("Mr of ALL products", no "from equation") it invites dropping coefficients. Also off-topic and chemistry only. | 4.3.3.2 |
| C10 | th3 | "Addition reactions have 100% atom economy (one product only)"; high atom economy = less waste, sustainable, economic | OK (off-topic) | ✓ | 4.3.3.2 |
| C11 | common_mistake | 2 : 1 — 0.4 mol A → 0.2 mol B | OK | ✓ | 5.3.2.2 |
| C12 | key_note | mass → moles → ratio → moles → mass | OK | ✓; the yield and atom-economy sentences carry C8/C9 | — |
| C13 | FIFA | 1.2 ÷ 24 = 0.05 mol; 1 : 1; Mr(H₂) = 2; 0.05 × 2 = 0.1 g | OK | ✓. Insert step crams three operations — a three-step chain (rule 3). | 5.3.2.2 |
| C14 | Convert (NEW) | "Nothing to convert — the mass of magnesium is already in grams throughout the calculation." | OK | Examined ✓ | CFIFA amendment |
| C15 | q1 key | 0.6 × 2/3 = 0.4 mol | OK | ✓ | 5.3.2.2 |
| C16 | q1 opt1 / wx1 | 0.6 — same moles / use the ratio | OK | Aligned ✓ | — |
| C17 | q1 opt2 / wx2 | 0.9 — "multiply 0.6 by 3/2" / inverts the ratio | OK | Aligned ✓; 0.6 × 1.5 = 0.9 ✓ | — |
| C18 | q1 opt3 / wx3 | 1.2 — double / only for 1 : 2 | OK | Aligned ✓ | — |
| C19 | q2 key | 20 ÷ 25 × 100 = 80 % | OK | ✓ chemistry only | 4.3.3.1 |
| C20 | q2 opt1 / wx1 | 125 % — inverted | OK | Aligned ✓ | — |
| C21 | q2 opt2 / wx2 | "5% — % yield = (5 ÷ 25) × 100 (using the difference)" / the 5 g is the lost yield | IMPRECISE | Aligned ✓. But the option's own working gives 20 %, not 5 % — and 20 % is option 3. Still a wrong option; marking unaffected. | — |
| C22 | q2 opt3 / wx3 | 20 % — used 20 directly | OK | Aligned ✓ | — |
| C23 | matching (to be replaced) | four ratio statements | OK | All ✓ | — |

Count: **1 WRONG** (C9 — the atom-economy formula, in theory, key_note and the frozen equations list). OFF-SPEC/off-topic: R4, R5. IMPRECISE: C5, C21. GAP: "masses of substances shown in a balanced equation". 9 calculations rechecked, all ✓.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| equations[2] (atom economy) | wrong form of AQA's formula; chemistry only; off-topic | **Do not use.** Atom economy lives on `atom-economy` (TF TH). |
| equations[1] (% yield); q2 | chemistry only — off-spec on CH; off-topic | Not on CH. Recommended: leave out and link to `percentage-yield`. If kept, TH only, triple-badged. |
| q1, FIFA, equations[0] | HT | Usable on CH TH. |

## 5. Calculations and chains (rule 3)
- **Masses in an equation (GAP):** e.g. 2Mg + O₂ → 2MgO read as 48 g + 32 g → 80 g. One step per substance. HT.
- **Moles of B from moles of A by the ratio (q1):** one step. HT.
- **Reacting masses (th2; FIFA):** Step 1 n(given) = m ÷ Mr → Step 2 n(wanted) by the molar ratio → Step 3 m(wanted) = n × Mr. A three-step chain; each step gets its own CFIFA. Convert: tonnes or kg → g before Step 1 (e.g. 2.4 kg Mg → 2400 g). HT.
- (Off-topic, TH only if kept) theoretical mass then % yield — Step 1 the reacting-mass chain; Step 2 % yield.

## 6. Verdict
SOURCE HAS ERRORS. The HT core (molar ratios, reacting masses, q1, FIFA) is correct. The page also carries two chemistry-only topics that have their own pages; one of them (atom economy) uses a denominator that is not AQA's formula. Nothing for Mide: the spec prints the formula.
