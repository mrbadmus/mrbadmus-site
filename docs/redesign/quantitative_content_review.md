# Quantitative Chemistry — content review (MRB-105)

_AQA 5.3 Quantitative Chemistry. Drafted for Mide's review before the Phase 2 merge. Every question, its options (✔︎ = correct), and a plain-English diagnostic for each wrong option are shown here — you never need to open the Python._

> 🆕 **New since your first copy:** a brand-new page, **Volumes of Gases (Molar Gas Volume)** (AQA 4.3.5, Triple-Higher only), has been added — it was missing from the data files entirely. It is the **last page in this document** and is flagged ⭐ throughout. Everything else is unchanged from your first review copy.

## How the tiers work (the difficulty model, same as Bonding)

- **Difficulty follows the tier, not the pathway.** Combined-Foundation (CF) and Triple-Foundation (TF) are the **same difficulty**; Combined-Higher (CH) and Triple-Higher (TH) both scale up to genuine Higher demand.
- **Triple's extra is coverage, not a harder version of the same content.** On a normal page, **TF = the exact CF set + 2 extra Foundation-level questions**, and **TH = the exact CH set + 2 extra Higher/depth questions**. A Foundation student sees the same difficulty on either pathway; a Triple student simply gets more.
- **This is a calculation unit, so the tier lift is real arithmetic.** Foundation questions give the values in the right units with the formula cued; Higher questions add unit conversions (cm³→dm³, g→mol via Mr, kg→g), require rearrangement, and include two-step / two-formula chains. Every number in every worked example and every calculation distractor has been checked to be arithmetically correct.
- **Every stem is exam-register** (uses an AQA command word) and **every wrong option carries a diagnostic** naming the misconception or the exact wrong move (unit not converted, ratio inverted, forgot to divide by Mr, wrong equation).
- **Counts:** Combined cells 10 questions; Triple cells 12 (Combined set + 2). On the two Triple-only pages (percentage-yield, atom-economy) there is no Combined baseline, so — per your call — each is a full standalone Triple page at **12 Foundation + 12 Higher**.

### Per-page tier presence (detected from the four data files, not assumed)

| Page | AQA | CF | CH | TF | TH |
|---|---|:--:|:--:|:--:|:--:|
| Conservation of Mass and Balanced Equations | 5.3.1.1 | ✓ | ✓ | ✓ | ✓ |
| Relative Formula Mass | 5.3.1.2 | ✓ | ✓ | ✓ | ✓ |
| Mass Changes in Reactions | 5.3.1.3 | ✓ | ✓ | ✓ | ✓ |
| Chemical Measurements | 5.3.1.4 | ✓ | ✓ | ✓ | ✓ |
| Concentration of Solutions | 5.3.2.5 | ✓ | ✓ | ✓ | ✓ |
| Moles | 5.3.2.1 | — | ✓ | — | ✓ |
| Amounts of Substances in Equations | 5.3.2.2 | — | ✓ | — | ✓ |
| Using Moles — Calculations and Limiting Reactants | 5.3.2.3–5.3.2.4 | — | ✓ | — | ✓ |
| Percentage Yield | 4.3.3.1 (Triple only) | — | — | ✓ | ✓ |
| Atom Economy | 4.3.3.2 (Triple only) | — | — | ✓ | ✓ |
| Volumes of Gases (Molar Gas Volume) | 4.3.5 (Triple only, Higher tier) | — | — | — | ✓ |

`moles`, `amounts-in-equations` and `using-moles-calculations` are **Higher-only** in AQA — there is no Foundation cell, so none was invented. `percentage-yield` and `atom-economy` are **Triple-only** (chemistry-only) — no Combined cell. The other five pages exist in all four cells.

### ⭐ Full-review checklist (per the review-tiering rule)

All calculation / formula-derivation items and all FIFA worked examples are flagged ⭐ for your full review; recall/comprehension items are left for your sampling. Per page:

- **Conservation of Mass and Balanced Equations** — 11 calculation/derivation item(s); 3 Foundation FIFA, 3 Higher FIFA
- **Relative Formula Mass** — 17 calculation/derivation item(s); 3 Foundation FIFA, 3 Higher FIFA
- **Mass Changes in Reactions** — 4 calculation/derivation item(s); 3 Foundation FIFA, 3 Higher FIFA
- **Chemical Measurements** — 9 calculation/derivation item(s); 3 Foundation FIFA, 3 Higher FIFA
- **Concentration of Solutions** — 13 calculation/derivation item(s); 3 Foundation FIFA, 3 Higher FIFA
- **Moles** — 10 calculation/derivation item(s); 3 Higher FIFA
- **Amounts of Substances in Equations** — 11 calculation/derivation item(s); 3 Higher FIFA
- **Using Moles — Calculations and Limiting Reactants** — 10 calculation/derivation item(s); 3 Higher FIFA
- **Percentage Yield** — 10 calculation/derivation item(s); 3 Foundation FIFA, 3 Higher FIFA
- **Atom Economy** — 8 calculation/derivation item(s); 3 Foundation FIFA, 3 Higher FIFA
- **Volumes of Gases (Molar Gas Volume)** — 12 calculation/derivation item(s); 3 Higher FIFA

### Audit status (self-checked with `audit_content.py`)

- **Before:** every page carried 2–3 questions per cell, identical across all tiers, with 0–1 FIFA. Across the unit that was **30 count-criticals** (below the floor of 5), plus **113 majors** (26 mistake-first, 12 tier-integrity, 13 triple-depth, 26 FIFA-too-few, 10 FIFA-tier-duplication, 26 FIFA-practice-absent) and **30 register-minors**.
- **After:** **zero critical, zero content majors, zero minors.** The only remaining flags are **31 `no interactive practice mode` majors** — one on every FIFA-bearing cell (30 from the original ten pages, **+1 for the new molar-gas-volume page**). This is the **systemic** flag the brief predicted: the current template renders static FIFA steps only, and building the interactive step-by-step practice mode is the redesign port's job (**MRB-113**), **not** a content defect. Because almost every Quantitative page has FIFA, this flag is expected to be large here (it was only 1 page in Bonding).

| Rule | Severity | Before | After |
|---|---|---:|---:|
| 1-count (below floor of 5) | critical | 30 | **0** |
| 1-register (no command word) | minor | 30 | **0** |
| 3-mistake-first (mislabelled Common Mistake) | major | 26 | **0** |
| 5-tier-integrity (Foundation = Higher) | major | 12 | **0** |
| 1-triple-depth (Triple = Combined) | major | 13 | **0** |
| 2-example-count (FIFA < 3) | major | 26 | **0** |
| 2-tier-duplication (FIFA Foundation = Higher) | major | 10 | **0** |
| 2-practice-absent (systemic FIFA-practice, MRB-113) | major | 26 | **31** |

_(The +1 in the after column vs the original ten-page review is the new molar-gas-volume page's FIFA block — the same expected systemic flag, not a content defect.)_

### Notes for you

1. **Molar gas volume gap — ✅ NOW FIXED.** My first copy flagged that AQA molar gas volume (chemistry-only, Higher: 1 mole of gas = 24 dm³ at RTP) had no page anywhere. You ruled: add it. It is now a full new page, **Volumes of Gases (Molar Gas Volume)** (`molar-gas-volume`, AQA 4.3.5), present in the Triple-Higher build only (chemistry-only + Higher). It auto-appears in the Triple/Higher Quantitative topic index and subtopic navigation. **Still open (your call, not done here):** the titration side of AQA 4.3.4 (concentrations in mol/dm³) has no dedicated page — that work currently lives on `using-moles-calculations` and on the separate `titrations` page (chemical-changes, 4.4.2.5). Flag if you want a dedicated mol/dm³ titration-calculations page later.
2. **Spec numbering — RESOLVED, not a defect.** My first copy flagged that `percentage-yield` / `atom-economy` carry `4.3.3.x` numbering while shared pages use `5.3.x`. On investigation this is a **deliberate, sitewide convention**, not an error: Triple-only (chemistry-only) pages use the AQA **8462** Chemistry-spec numbers (4.x) — percentage-yield 4.3.3.1, atom-economy 4.3.3.2, titrations 4.4.2.5, cells-and-batteries 4.5.2.1 — while pages shared with Combined Science use the **8464** Combined-spec numbers (5.3.x). Existing spec labels are therefore left untouched, and the new molar-gas-volume page correctly takes its 8462 number **4.3.5** (*use of amount of substance in relation to volumes of gases*).

---

## Conservation of Mass and Balanced Equations  ·  `conservation-of-mass`  ·  AQA 5.3.1.1

> **Tier presence:** Combined + Triple, Foundation + Higher (all four cells).
>
> **How the cells are composed** (item numbers below): **CF** → Q1–10; **CH** → Q1–5, 11–15; **TF** → Q1–10, 16–17; **TH** → Q1–5, 11–15, 18–19. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often think they can balance an equation by changing the small subscript numbers inside a formula — writing H₂O as H₂O₂ to get an extra oxygen, for instance. This does not balance the equation, it changes the chemical: H₂O₂ is hydrogen peroxide, not water, so the equation no longer describes the same reaction. Balance only by putting large numbers (coefficients) in FRONT of each formula — never change a subscript.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(all four tiers (CF·CH·TF·TH))_ — 24 g of magnesium reacts completely with oxygen to form 40 g of magnesium oxide. Calculate the mass of oxygen that reacted.
- [✔︎] 16 g — by conservation of mass, mass of oxygen = 40 − 24 = 16 g
- [ ] 40 g — the oxygen has the same mass as the magnesium oxide
    - _why wrong:_ 40 g is the mass of the PRODUCT, which contains both the magnesium and the oxygen — the oxygen alone is 40 − 24 = 16 g.
- [ ] 64 g — add the two masses, 40 + 24
    - _why wrong:_ Adding product and reactant double-counts. The oxygen that reacted is product − magnesium = 40 − 24 = 16 g.
- [ ] 24 g — the oxygen has the same mass as the magnesium
    - _why wrong:_ There is no reason the two reactants have equal mass. Conservation gives mass of oxygen = 40 − 24 = 16 g.

**Q2.** _(all four tiers (CF·CH·TF·TH))_ — Identify which of these equations is correctly balanced.
- [✔︎] 4Fe + 3O₂ → 2Fe₂O₃
- [ ] Fe + O₂ → Fe₂O₃
    - _why wrong:_ Left: 1 Fe, 2 O. Right: 2 Fe, 3 O. Neither element balances.
- [ ] 2Fe + O₂ → Fe₂O₃
    - _why wrong:_ Left: 2 Fe, 2 O. Right: 2 Fe, 3 O. Oxygen does not balance.
- [ ] Fe + 3O₂ → 2Fe₂O₃
    - _why wrong:_ Left: 1 Fe, 6 O. Right: 4 Fe, 6 O. Iron does not balance.

**Q3.** _(all four tiers (CF·CH·TF·TH))_ — Explain why the total mass of the products equals the total mass of the reactants in a chemical reaction.
- [✔︎] No atoms are created or destroyed — they are only rearranged, so the same atoms, and therefore the same total mass, are present before and after
- [ ] The reactants are simply renamed as products, so the mass label stays the same
    - _why wrong:_ A reaction genuinely rearranges atoms into new substances — mass is conserved because the ATOMS are conserved, not because of naming.
- [ ] A reaction always makes the same number of molecules as it uses up
    - _why wrong:_ The number of molecules often changes (2H₂ + O₂ → 2H₂O goes from 3 molecules to 2). It is the number of ATOMS of each element that is conserved.
- [ ] Energy is conserved, and mass is the same thing as energy in a reaction
    - _why wrong:_ Conservation of mass here is about atoms being rearranged; at GCSE it is not an energy argument.

**Q4. ⭐** _(all four tiers (CF·CH·TF·TH))_ — In a sealed container, 12 g of carbon reacts completely with 32 g of oxygen. Calculate the mass of carbon dioxide produced.
- [✔︎] 44 g — mass is conserved, so 12 + 32 = 44 g
- [ ] 20 g — the difference, 32 − 12
    - _why wrong:_ The reactants COMBINE, so their masses add: 12 + 32 = 44 g. Subtracting is only used to find a missing reactant or product.
- [ ] 32 g — the product has the same mass as the oxygen
    - _why wrong:_ The carbon dioxide contains the carbon as well: 12 + 32 = 44 g.
- [ ] 12 g — the product has the same mass as the carbon
    - _why wrong:_ The carbon dioxide contains the oxygen as well: 12 + 32 = 44 g.

**Q5. ⭐** _(all four tiers (CF·CH·TF·TH))_ — Deduce the numbers needed to balance this equation: __H₂ + O₂ → __H₂O.
- [✔︎] 2H₂ + O₂ → 2H₂O
- [ ] H₂ + O₂ → H₂O
    - _why wrong:_ The left has 2 O but the right has only 1 O. Use 2H₂O, then 2H₂ to rebalance the hydrogen.
- [ ] 2H₂ + 2O₂ → 2H₂O
    - _why wrong:_ This gives 4 O on the left but only 2 O on the right. One O₂ is enough: 2H₂ + O₂ → 2H₂O.
- [ ] H₂ + O₂ → 2H₂O
    - _why wrong:_ The right now has 4 H and 2 O but the left has only 2 H. Balance the hydrogen with 2H₂: 2H₂ + O₂ → 2H₂O.

**Q6.** _(both Foundation tiers (CF·TF))_ — State the law of conservation of mass.
- [✔︎] The total mass of the products is equal to the total mass of the reactants
- [ ] Mass is always lost during a chemical reaction
    - _why wrong:_ Mass is never lost overall — the reactant mass equals the product mass.
- [ ] The mass of each product equals the mass of each reactant
    - _why wrong:_ It is the TOTAL mass that is conserved, not the mass of each individual substance.
- [ ] Both mass and energy are destroyed as a reaction proceeds
    - _why wrong:_ Neither mass nor energy is destroyed — mass is conserved.

**Q7.** _(both Foundation tiers (CF·TF))_ — State what happens to the atoms during a chemical reaction.
- [✔︎] They are rearranged into new substances — none are created or destroyed
- [ ] Some atoms are destroyed and new atoms are created
    - _why wrong:_ Atoms are never created or destroyed in a chemical reaction — they are only rearranged.
- [ ] The atoms are converted into energy
    - _why wrong:_ Atoms are not turned into energy in a chemical reaction; they are rearranged.
- [ ] The atoms combine to form larger atoms
    - _why wrong:_ Atoms do not merge into larger atoms — they bond together into molecules and compounds.

**Q8.** _(both Foundation tiers (CF·TF))_ — When balancing an equation, state which numbers you are allowed to change.
- [✔︎] Only the large numbers written in front of each formula (the coefficients)
- [ ] The small subscript numbers inside a formula
    - _why wrong:_ Changing a subscript changes the substance itself (H₂O → H₂O₂). Only the coefficients in front may be changed.
- [ ] Any of the numbers, as long as the equation ends up balanced
    - _why wrong:_ You may not change subscripts — that would change the chemicals. Only the coefficients may be adjusted.
- [ ] The subscripts, but not the coefficients
    - _why wrong:_ This is the wrong way round: coefficients may be changed, subscripts may not.

**Q9. ⭐** _(both Foundation tiers (CF·TF))_ — 8 g of hydrogen reacts completely with 64 g of oxygen to form water. State the mass of water formed.
- [✔︎] 72 g — 8 + 64 = 72 g
- [ ] 56 g — the difference, 64 − 8
    - _why wrong:_ The reactants combine, so add them: 8 + 64 = 72 g.
- [ ] 64 g — the water has the same mass as the oxygen
    - _why wrong:_ The water also contains the hydrogen: 8 + 64 = 72 g.
- [ ] 8 g — the water has the same mass as the hydrogen
    - _why wrong:_ The water also contains the oxygen: 8 + 64 = 72 g.

**Q10.** _(both Foundation tiers (CF·TF))_ — Identify the correctly balanced equation for sodium reacting with chlorine.
- [✔︎] 2Na + Cl₂ → 2NaCl
- [ ] Na + Cl₂ → NaCl
    - _why wrong:_ The left has 2 Cl but the right has 1 Cl, and the sodium is unbalanced too. 2Na + Cl₂ → 2NaCl balances both.
- [ ] Na + Cl → NaCl
    - _why wrong:_ Chlorine exists as Cl₂ molecules, not single Cl atoms. The balanced equation is 2Na + Cl₂ → 2NaCl.
- [ ] 2Na + 2Cl₂ → 2NaCl
    - _why wrong:_ This gives 4 Cl on the left but only 2 on the right. One Cl₂ is enough: 2Na + Cl₂ → 2NaCl.

**Q11. ⭐** _(both Higher tiers (CH·TH))_ — 14 g of nitrogen reacts with hydrogen to form 17 g of ammonia (NH₃). Calculate the mass of hydrogen that reacted.
- [✔︎] 3 g — by conservation of mass, mass of hydrogen = 17 − 14 = 3 g
- [ ] 31 g — add the masses, 17 + 14
    - _why wrong:_ Hydrogen is a reactant; its mass is the product minus the other reactant: 17 − 14 = 3 g. Adding would exceed the product mass.
- [ ] 17 g — the hydrogen has the same mass as the ammonia
    - _why wrong:_ The ammonia contains the nitrogen too — the hydrogen alone is 17 − 14 = 3 g.
- [ ] 14 g — the hydrogen has the same mass as the nitrogen
    - _why wrong:_ There is no reason the two reactants are equal. Mass of hydrogen = 17 − 14 = 3 g.

**Q12. ⭐** _(both Higher tiers (CH·TH))_ — Deduce the coefficients that balance: Fe₂O₃ + __CO → __Fe + __CO₂.
- [✔︎] Fe₂O₃ + 3CO → 2Fe + 3CO₂
- [ ] Fe₂O₃ + CO → 2Fe + CO₂
    - _why wrong:_ Oxygen does not balance: left 3 + 1 = 4 O, right 2 O. You need 3CO and 3CO₂.
- [ ] Fe₂O₃ + 3CO → 2Fe + 2CO₂
    - _why wrong:_ Carbon does not balance: 3 C on the left, 2 C on the right. Use 3CO₂.
- [ ] 2Fe₂O₃ + 3CO → 4Fe + 3CO₂
    - _why wrong:_ Oxygen does not balance: left 6 + 3 = 9 O, right 6 O. The simplest balance is Fe₂O₃ + 3CO → 2Fe + 3CO₂.

**Q13.** _(both Higher tiers (CH·TH))_ — A student reacts marble chips with acid in an open flask standing on a balance. Explain why the balance reading decreases, even though mass is conserved.
- [✔︎] The reaction makes carbon dioxide gas, which escapes from the open flask into the air — the gas still has mass, so the mass left in the flask falls while the total mass of the system is unchanged
- [ ] Some of the reactant mass is destroyed as the reaction happens
    - _why wrong:_ Mass is never destroyed — the reading falls because CO₂ gas leaves the flask, carrying its mass away.
- [ ] The acid evaporates, so the liquid becomes lighter
    - _why wrong:_ The loss is due to CO₂ gas produced by the reaction escaping, not simple evaporation of the acid.
- [ ] Gases have no mass, so making a gas reduces the total mass
    - _why wrong:_ Gases DO have mass. The reading falls only because that gas has left the open flask.

**Q14. ⭐** _(both Higher tiers (CH·TH))_ — Aluminium reduces copper(II) oxide: 2Al + 3CuO → Al₂O₃ + 3Cu. When 5.4 g of aluminium reacts with 24 g of copper(II) oxide, 10.2 g of aluminium oxide forms. Calculate the mass of copper produced.
- [✔︎] 19.2 g — total reactant mass 5.4 + 24 = 29.4 g, so mass of copper = 29.4 − 10.2 = 19.2 g
- [ ] 29.4 g — the total mass of the two reactants
    - _why wrong:_ That is the mass of BOTH products together. The copper is 29.4 − 10.2 (the aluminium oxide) = 19.2 g.
- [ ] 13.8 g — 24 − 10.2, using only the copper oxide
    - _why wrong:_ You must use the TOTAL reactant mass: (5.4 + 24) − 10.2 = 19.2 g.
- [ ] 34.2 g — 24 + 10.2
    - _why wrong:_ The products cannot exceed the 29.4 g of reactants. Mass of copper = 29.4 − 10.2 = 19.2 g.

**Q15. ⭐** _(both Higher tiers (CH·TH))_ — Deduce the coefficients that balance: __Al + __H₂SO₄ → Al₂(SO₄)₃ + __H₂.
- [✔︎] 2Al + 3H₂SO₄ → Al₂(SO₄)₃ + 3H₂
- [ ] Al + H₂SO₄ → Al₂(SO₄)₃ + H₂
    - _why wrong:_ Aluminium and the sulfate group are unbalanced: the product needs 2 Al and 3 SO₄, so use 2Al and 3H₂SO₄.
- [ ] 2Al + 3H₂SO₄ → Al₂(SO₄)₃ + H₂
    - _why wrong:_ Hydrogen does not balance: 6 H on the left (3 × H₂SO₄) but only 2 H on the right. You need 3H₂.
- [ ] 2Al + H₂SO₄ → Al₂(SO₄)₃ + 3H₂
    - _why wrong:_ The sulfate group is unbalanced: the product has 3 SO₄ but the left has only 1. Use 3H₂SO₄.

**Q16.** _(Triple-Foundation extra)_ — A reaction is carried out in a sealed flask. State what happens to the total mass of the flask and its contents during the reaction.
- [✔︎] It stays exactly the same — no substances can enter or leave a sealed flask
- [ ] It increases, because new products are made
    - _why wrong:_ Making products only rearranges the existing atoms — no mass is added, so the total is unchanged.
- [ ] It decreases, because gases are produced
    - _why wrong:_ In a SEALED flask any gas stays inside, so the total mass does not change.
- [ ] It cannot be predicted without the balanced equation
    - _why wrong:_ Conservation of mass guarantees the total is unchanged in a sealed flask, whatever the equation.

**Q17. ⭐** _(Triple-Foundation extra)_ — Deduce the numbers needed to balance: __Ca + O₂ → __CaO.
- [✔︎] 2Ca + O₂ → 2CaO
- [ ] Ca + O₂ → CaO
    - _why wrong:_ Oxygen is unbalanced: 2 O on the left, 1 O on the right. Use 2CaO, then 2Ca.
- [ ] Ca + O₂ → 2CaO
    - _why wrong:_ Now calcium is unbalanced: 1 Ca on the left, 2 Ca on the right. Use 2Ca.
- [ ] 2Ca + 2O₂ → 2CaO
    - _why wrong:_ Oxygen is unbalanced: 4 O on the left, 2 O on the right. One O₂ is enough: 2Ca + O₂ → 2CaO.

**Q18. ⭐** _(Triple-Higher extra)_ — In the Haber process, N₂ + 3H₂ → 2NH₃. 28 g of nitrogen reacts completely with 6 g of hydrogen. Calculate the maximum mass of ammonia that can be produced.
- [✔︎] 34 g — by conservation of mass, 28 + 6 = 34 g
- [ ] 22 g — the difference, 28 − 6
    - _why wrong:_ The reactants combine, so their masses add: 28 + 6 = 34 g.
- [ ] 17 g — the mass of one mole of ammonia
    - _why wrong:_ Both reactants are fully converted, so all 28 + 6 = 34 g ends up as ammonia.
- [ ] 28 g — the ammonia has the same mass as the nitrogen
    - _why wrong:_ The ammonia contains the hydrogen too: 28 + 6 = 34 g.

**Q19. ⭐** _(Triple-Higher extra)_ — Deduce the coefficients that balance the complete combustion of ethane: __C₂H₆ + __O₂ → __CO₂ + __H₂O.
- [✔︎] 2C₂H₆ + 7O₂ → 4CO₂ + 6H₂O
- [ ] C₂H₆ + O₂ → CO₂ + H₂O
    - _why wrong:_ Nothing balances: 2 C and 6 H on the left need 2CO₂ and 3H₂O for one C₂H₆; doubling then clears the odd oxygen.
- [ ] 2C₂H₆ + 5O₂ → 4CO₂ + 6H₂O
    - _why wrong:_ Oxygen is short: the right has 8 + 6 = 14 O, which needs 7O₂, not 5O₂.
- [ ] C₂H₆ + 7O₂ → 2CO₂ + 3H₂O
    - _why wrong:_ With 7O₂ (14 O) you must double the carbons and hydrogens: 2C₂H₆ → 4CO₂ + 6H₂O.

**FIFA worked examples — Foundation (in CF & TF)** ⭐

- **Mass of a product (add the reactants)** — Carbon burns in oxygen: C + O₂ → CO₂. 12 g of carbon reacts completely with 32 g of oxygen. Calculate the mass of carbon dioxide formed.
    - **F** — total mass of products = total mass of reactants
    - **I** — mass of CO₂ = mass of C + mass of O₂ = 12 + 32
    - **F** — 12 + 32 = 44
    - **A** — mass of CO₂ = 44 g
- **Mass of a reactant (subtract)** — Magnesium burns in air: 2Mg + O₂ → 2MgO. 48 g of magnesium forms 80 g of magnesium oxide. Calculate the mass of oxygen that reacted.
    - **F** — total mass of reactants = total mass of products
    - **I** — mass of O₂ = mass of MgO − mass of Mg = 80 − 48
    - **F** — 80 − 48 = 32
    - **A** — mass of oxygen = 32 g
- **A decimal mass in a sealed tube** — Calcium carbonate decomposes in a sealed tube: CaCO₃ → CaO + CO₂. 10.0 g of calcium carbonate produces 5.6 g of calcium oxide. Calculate the mass of carbon dioxide produced.
    - **F** — mass of reactants = mass of products
    - **I** — mass of CO₂ = mass of CaCO₃ − mass of CaO = 10.0 − 5.6
    - **F** — 10.0 − 5.6 = 4.4
    - **A** — mass of CO₂ = 4.4 g

**FIFA worked examples — Higher (in CH & TH)** ⭐

- **Find a missing reactant mass** — Nitrogen reacts with hydrogen: N₂ + 3H₂ → 2NH₃. 14 g of nitrogen reacts with hydrogen to form 17 g of ammonia. Calculate the mass of hydrogen that reacted.
    - **F** — mass of reactants = mass of products, so mass of H₂ = mass of NH₃ − mass of N₂
    - **I** — mass of H₂ = 17 − 14
    - **F** — 17 − 14 = 3
    - **A** — mass of hydrogen = 3 g
- **Two reactants, two products** — Aluminium reduces copper(II) oxide: 2Al + 3CuO → Al₂O₃ + 3Cu. 5.4 g of aluminium reacts with 24.0 g of copper(II) oxide to form 10.2 g of aluminium oxide. Calculate the mass of copper formed.
    - **F** — total product mass = total reactant mass, so mass of Cu = (mass Al + mass CuO) − mass Al₂O₃
    - **I** — mass of Cu = (5.4 + 24.0) − 10.2
    - **F** — 29.4 − 10.2 = 19.2
    - **A** — mass of copper = 19.2 g
- **An open flask losing gas** — Marble chips (CaCO₃) react with hydrochloric acid in an open flask on a balance. The flask and contents fall from 152.4 g to 148.0 g. Calculate the mass of carbon dioxide gas that escaped.
    - **F** — the fall in mass equals the mass of gas that has left the flask
    - **I** — mass of CO₂ = 152.4 − 148.0
    - **F** — 152.4 − 148.0 = 4.4
    - **A** — mass of carbon dioxide = 4.4 g

---

## Relative Formula Mass  ·  `relative-formula-mass`  ·  AQA 5.3.1.2

> **Tier presence:** Combined + Triple, Foundation + Higher (all four cells).
>
> **How the cells are composed** (item numbers below): **CF** → Q1–10; **CH** → Q1–5, 11–15; **TF** → Q1–10, 16–17; **TH** → Q1–5, 11–15, 18–19. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often forget to multiply the atoms inside a bracket by the subscript outside it — reading Ca(OH)₂ as one oxygen and one hydrogen instead of two of each. That undercounts the mass, because the ₂ applies to the WHOLE group: Ca(OH)₂ really contains 2 O and 2 H. Work the bracket out first (2 × O and 2 × H), then add every Ar: 40 + 32 + 2 = 74.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(all four tiers (CF·CH·TF·TH))_ — Calculate the relative formula mass (Mr) of calcium carbonate (CaCO₃). Ar: Ca = 40, C = 12, O = 16.
- [✔︎] 100 — 40 + 12 + (3 × 16) = 40 + 12 + 48
- [ ] 68 — 40 + 12 + 16, counting only one oxygen
    - _why wrong:_ The subscript 3 after O means THREE oxygens: 3 × 16 = 48, not 16.
- [ ] 116 — 40 + 12 + (4 × 16), counting four oxygens
    - _why wrong:_ CO₃ has 3 oxygens, not 4. Only a CO₄ group would have four.
- [ ] 52 — 40 + 12, forgetting the oxygens
    - _why wrong:_ The three oxygens cannot be ignored: 3 × 16 = 48 must be added.

**Q2. ⭐** _(all four tiers (CF·CH·TF·TH))_ — Calculate the relative formula mass of calcium hydroxide, Ca(OH)₂. Ar: Ca = 40, O = 16, H = 1.
- [✔︎] 74 — 40 + (2 × 16) + (2 × 1) = 40 + 32 + 2
- [ ] 57 — 40 + 16 + 1, taking one O and one H
    - _why wrong:_ The ₂ outside the bracket doubles BOTH the O and the H: 2 × 16 and 2 × 1.
- [ ] 58 — 40 + 16 + (2 × 1), doubling only the hydrogen
    - _why wrong:_ The subscript applies to the whole (OH) group, so the oxygen is doubled too: 2 × 16 = 32.
- [ ] 112 — (40 + 16 + 1) × 2, doubling the calcium as well
    - _why wrong:_ The ₂ applies only to the (OH) group in the bracket, not to the calcium outside it.

**Q3. ⭐** _(all four tiers (CF·CH·TF·TH))_ — Calculate the relative formula mass of sulfuric acid, H₂SO₄. Ar: H = 1, S = 32, O = 16.
- [✔︎] 98 — (2 × 1) + 32 + (4 × 16) = 2 + 32 + 64
- [ ] 49 — (1) + 32 + 16, taking one of each atom
    - _why wrong:_ H₂SO₄ has 2 H and 4 O: 2 × 1 = 2 and 4 × 16 = 64.
- [ ] 50 — 2 + 32 + 16, forgetting the O subscript
    - _why wrong:_ The 4 after O means 4 × 16 = 64, not 16.
- [ ] 130 — 2 + 32 + (6 × 16), counting six oxygens
    - _why wrong:_ There are 4 oxygens in H₂SO₄, so 4 × 16 = 64.

**Q4. ⭐** _(all four tiers (CF·CH·TF·TH))_ — Calculate the relative formula mass of magnesium chloride, MgCl₂. Ar: Mg = 24, Cl = 35.5.
- [✔︎] 95 — 24 + (2 × 35.5) = 24 + 71
- [ ] 59.5 — 24 + 35.5, counting only one chlorine
    - _why wrong:_ The ₂ after Cl means two chlorines: 2 × 35.5 = 71.
- [ ] 119 — (24 + 35.5) × 2, doubling the magnesium too
    - _why wrong:_ Only the chlorine is doubled: Mg + (2 × Cl) = 24 + 71 = 95.
- [ ] 120 — 24 + (2 × 48), using 48 for chlorine
    - _why wrong:_ The Ar of chlorine is 35.5, not 48: 2 × 35.5 = 71.

**Q5. ⭐** _(all four tiers (CF·CH·TF·TH))_ — Glucose has the formula C₆H₁₂O₆. Calculate its relative formula mass. Ar: C = 12, H = 1, O = 16.
- [✔︎] 180 — (6 × 12) + (12 × 1) + (6 × 16) = 72 + 12 + 96
- [ ] 34 — 12 + 1 + 16, ignoring all the subscripts
    - _why wrong:_ Each atom is multiplied by its subscript: 6 C, 12 H and 6 O.
- [ ] 29 — 6 + 12 + 6, adding the subscripts instead of using Ar
    - _why wrong:_ The subscripts count the atoms; multiply each by its Ar: (6 × 12) + (12 × 1) + (6 × 16).
- [ ] 168 — 72 + 96, forgetting the hydrogen
    - _why wrong:_ The 12 hydrogens add 12 × 1 = 12 to the total.

**Q6.** _(both Foundation tiers (CF·TF))_ — State what the relative formula mass (Mr) of a compound tells you.
- [✔︎] The sum of the relative atomic masses of all the atoms shown in its formula
- [ ] The mass of one molecule in grams
    - _why wrong:_ Mr is a relative number with no units, not a mass in grams — that is the molar mass.
- [ ] The number of atoms in the formula
    - _why wrong:_ Mr adds up the atomic MASSES, not the number of atoms.
- [ ] The relative atomic mass of the heaviest atom only
    - _why wrong:_ Every atom in the formula is included, not just the heaviest one.

**Q7. ⭐** _(both Foundation tiers (CF·TF))_ — Calculate the relative formula mass of water, H₂O. Ar: H = 1, O = 16.
- [✔︎] 18 — (2 × 1) + 16
- [ ] 17 — 1 + 16, counting only one hydrogen
    - _why wrong:_ The ₂ after H means two hydrogens: 2 × 1 = 2.
- [ ] 34 — (1 + 16) × 2, doubling everything
    - _why wrong:_ Only the hydrogen is doubled: (2 × 1) + 16 = 18.
- [ ] 19 — 2 + 16 + 1, adding an extra hydrogen
    - _why wrong:_ H₂O has exactly 2 H and 1 O: 2 + 16 = 18.

**Q8.** _(both Foundation tiers (CF·TF))_ — State the units of relative formula mass.
- [✔︎] It has no units — it is a ratio of masses
- [ ] Grams (g)
    - _why wrong:_ Grams is the unit of actual mass or molar mass; relative formula mass itself has no units.
- [ ] Grams per mole (g/mol)
    - _why wrong:_ That is the unit of molar mass; Mr is just a number with no units.
- [ ] Moles (mol)
    - _why wrong:_ Moles measure amount of substance; Mr has no units.

**Q9. ⭐** _(both Foundation tiers (CF·TF))_ — Calculate the relative formula mass of oxygen gas, O₂. Ar: O = 16.
- [✔︎] 32 — 2 × 16
- [ ] 16 — one oxygen atom
    - _why wrong:_ Oxygen gas exists as O₂ molecules, so 2 × 16 = 32.
- [ ] 18 — 16 + 2
    - _why wrong:_ The ₂ multiplies the oxygen, it is not added: 2 × 16 = 32.
- [ ] 8 — 16 ÷ 2
    - _why wrong:_ Two atoms means you multiply by 2, not divide: 2 × 16 = 32.

**Q10. ⭐** _(both Foundation tiers (CF·TF))_ — Calculate the relative formula mass of sodium hydroxide, NaOH. Ar: Na = 23, O = 16, H = 1.
- [✔︎] 40 — 23 + 16 + 1
- [ ] 39 — 23 + 16, forgetting the hydrogen
    - _why wrong:_ NaOH contains one H, adding 1 to the total: 23 + 16 + 1 = 40.
- [ ] 24 — 23 + 1, forgetting the oxygen
    - _why wrong:_ The oxygen (16) must be included: 23 + 16 + 1 = 40.
- [ ] 58 — 23 + 16 + 1 + 18, adding water
    - _why wrong:_ NaOH has no water of crystallisation here: just 23 + 16 + 1 = 40.

**Q11. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the relative formula mass of magnesium nitrate, Mg(NO₃)₂. Ar: Mg = 24, N = 14, O = 16.
- [✔︎] 148 — 24 + 2 × (14 + 48) = 24 + (2 × 62)
- [ ] 86 — 24 + 14 + 48, ignoring the bracket subscript
    - _why wrong:_ The ₂ outside the bracket doubles the whole NO₃ group: 2 N and 6 O, i.e. 2 × 62 = 124.
- [ ] 100 — 24 + (2 × 14) + 48, doubling only the nitrogen
    - _why wrong:_ The ₂ doubles the oxygens as well: 6 × 16 = 96, so 2 × (14 + 48) = 124.
- [ ] 124 — 2 × (14 + 48), forgetting the magnesium
    - _why wrong:_ The magnesium (24) is outside the bracket and must be added: 24 + 124 = 148.

**Q12. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the relative formula mass of aluminium sulfate, Al₂(SO₄)₃. Ar: Al = 27, S = 32, O = 16.
- [✔︎] 342 — (2 × 27) + 3 × (32 + 64) = 54 + (3 × 96)
- [ ] 150 — 27 + 32 + (3 × 16) + ..., ignoring the bracket subscript
    - _why wrong:_ The ₃ multiplies the whole SO₄ group: 3 S and 12 O, i.e. 3 × 96 = 288.
- [ ] 246 — 54 + (3 × 32) + (2 × 16 × 3), miscounting the oxygens
    - _why wrong:_ Each SO₄ has 4 O, and there are 3 of them: 12 × 16 = 192, so (SO₄)₃ = 288.
- [ ] 288 — 3 × (32 + 64), forgetting the aluminium
    - _why wrong:_ The two aluminiums add 2 × 27 = 54: total 54 + 288 = 342.

**Q13. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the relative formula mass of hydrated copper(II) sulfate, CuSO₄·5H₂O. Ar: Cu = 63.5, S = 32, O = 16, H = 1.
- [✔︎] 249.5 — CuSO₄ (159.5) + 5 × H₂O (5 × 18 = 90)
- [ ] 159.5 — CuSO₄ only, ignoring the water
    - _why wrong:_ The ·5H₂O adds five water molecules: 5 × 18 = 90, giving 249.5.
- [ ] 177.5 — CuSO₄ + 18, adding only one water
    - _why wrong:_ There are FIVE waters: 5 × 18 = 90, not 18.
- [ ] 249.5 g — the value is right but stated with units
    - _why wrong:_ The value 249.5 is correct, but relative formula mass has no units.

**Q14. ⭐** _(both Higher tiers (CH·TH))_ — A metal oxide has the formula X₂O and a relative formula mass of 94. Ar(O) = 16. Deduce the relative atomic mass of X.
- [✔︎] 39 — (94 − 16) ÷ 2 = 78 ÷ 2
- [ ] 78 — 94 − 16, forgetting there are two X atoms
    - _why wrong:_ There are 2 X atoms sharing the 78, so Ar(X) = 78 ÷ 2 = 39.
- [ ] 55 — 94 ÷ 2 + 16 ÷ ..., mixing up the steps
    - _why wrong:_ Subtract the oxygen first, then halve: (94 − 16) ÷ 2 = 39.
- [ ] 47 — 94 ÷ 2, halving the whole Mr
    - _why wrong:_ Only the two X atoms are halved after removing the oxygen: (94 − 16) ÷ 2 = 39.

**Q15. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the relative formula mass of ammonium sulfate, (NH₄)₂SO₄. Ar: N = 14, H = 1, S = 32, O = 16.
- [✔︎] 132 — 2 × (14 + 4) + 32 + 64 = 36 + 96
- [ ] 114 — (14 + 4) + 32 + 64, ignoring the bracket subscript
    - _why wrong:_ The ₂ doubles the whole NH₄ group: 2 × (14 + 4) = 36.
- [ ] 50 — (14 + 4) + 32, forgetting the four oxygens
    - _why wrong:_ SO₄ contains 4 O: 4 × 16 = 64 must be included.
- [ ] 168 — 2 × (14 + 4) + 2 × (32 + 64), doubling the sulfate too
    - _why wrong:_ The ₂ applies only to the NH₄ group; there is just one SO₄: 36 + 96 = 132.

**Q16. ⭐** _(Triple-Foundation extra)_ — Calculate the relative formula mass of methane, CH₄. Ar: C = 12, H = 1.
- [✔︎] 16 — 12 + (4 × 1)
- [ ] 13 — 12 + 1, counting only one hydrogen
    - _why wrong:_ The ₄ after H means four hydrogens: 4 × 1 = 4.
- [ ] 48 — 12 × 4, multiplying the carbon by 4
    - _why wrong:_ The subscript 4 applies to the hydrogen, not the carbon: 12 + 4 = 16.
- [ ] 17 — 12 + 4 + 1, adding an extra hydrogen
    - _why wrong:_ CH₄ has exactly 4 H: 12 + 4 = 16.

**Q17. ⭐** _(Triple-Foundation extra)_ — Calculate the relative formula mass of calcium oxide, CaO. Ar: Ca = 40, O = 16.
- [✔︎] 56 — 40 + 16
- [ ] 24 — 40 − 16, subtracting instead of adding
    - _why wrong:_ Relative formula mass adds the atoms: 40 + 16 = 56.
- [ ] 40 — the calcium only
    - _why wrong:_ The oxygen must be included: 40 + 16 = 56.
- [ ] 640 — 40 × 16, multiplying the atoms
    - _why wrong:_ The Ar values are added, not multiplied: 40 + 16 = 56.

**Q18. ⭐** _(Triple-Higher extra)_ — Calculate the relative formula mass of hydrated sodium carbonate, Na₂CO₃·10H₂O. Ar: Na = 23, C = 12, O = 16, H = 1.
- [✔︎] 286 — Na₂CO₃ (106) + 10 × H₂O (10 × 18 = 180)
- [ ] 106 — Na₂CO₃ only, ignoring the water
    - _why wrong:_ The ·10H₂O adds ten waters: 10 × 18 = 180, giving 286.
- [ ] 124 — Na₂CO₃ + 18, adding only one water
    - _why wrong:_ There are TEN waters: 10 × 18 = 180, not 18.
- [ ] 196 — Na₂CO₃ + (10 × 9), using 9 for water
    - _why wrong:_ The Mr of water is 18, not 9: 10 × 18 = 180.

**Q19. ⭐** _(Triple-Higher extra)_ — A Group 2 metal M forms an oxide MO with a relative formula mass of 40. Ar(O) = 16. Deduce the metal M. Ar: Be = 9, Mg = 24, Ca = 40.
- [✔︎] Magnesium — Ar(M) = 40 − 16 = 24
- [ ] Calcium — Ar = 40
    - _why wrong:_ 40 is the Mr of the whole oxide; Ar(M) = 40 − 16 = 24, which is magnesium.
- [ ] Beryllium — Ar = 9
    - _why wrong:_ Ar(M) = 40 − 16 = 24, not 9; the metal is magnesium.
- [ ] Calcium — because CaO is a common oxide
    - _why wrong:_ The relative formula mass fixes the answer: Ar(M) = 40 − 16 = 24 = magnesium.

**FIFA worked examples — Foundation (in CF & TF)** ⭐

- **Add up the relative atomic masses** — Calculate the relative formula mass of sulfuric acid (H₂SO₄). Ar: H = 1, S = 32, O = 16.
    - **F** — Mr = sum of (Ar × number of each atom)
    - **I** — H: 2 × 1 = 2;  S: 1 × 32 = 32;  O: 4 × 16 = 64
    - **F** — Mr = 2 + 32 + 64
    - **A** — Mr = 98
- **A compound with three of one atom** — Calculate the relative formula mass of calcium carbonate (CaCO₃). Ar: Ca = 40, C = 12, O = 16.
    - **F** — Mr = sum of (Ar × number of each atom)
    - **I** — Ca: 1 × 40 = 40;  C: 1 × 12 = 12;  O: 3 × 16 = 48
    - **F** — Mr = 40 + 12 + 48
    - **A** — Mr = 100
- **A formula with a bracket** — Calculate the relative formula mass of calcium hydroxide, Ca(OH)₂. Ar: Ca = 40, O = 16, H = 1.
    - **F** — multiply the atoms inside the bracket by the subscript outside, then add every Ar
    - **I** — Ca: 40;  O: 2 × 16 = 32;  H: 2 × 1 = 2
    - **F** — Mr = 40 + 32 + 2
    - **A** — Mr = 74

**FIFA worked examples — Higher (in CH & TH)** ⭐

- **A bracket around a polyatomic group** — Calculate the relative formula mass of magnesium nitrate, Mg(NO₃)₂. Ar: Mg = 24, N = 14, O = 16.
    - **F** — multiply the whole NO₃ group by 2, then add every Ar
    - **I** — Mg: 24;  N: 2 × 14 = 28;  O: 6 × 16 = 96
    - **F** — Mr = 24 + 28 + 96
    - **A** — Mr = 148
- **Two brackets to keep track of** — Calculate the relative formula mass of aluminium sulfate, Al₂(SO₄)₃. Ar: Al = 27, S = 32, O = 16.
    - **F** — multiply the whole SO₄ group by 3, then add every Ar
    - **I** — Al: 2 × 27 = 54;  S: 3 × 32 = 96;  O: 12 × 16 = 192
    - **F** — Mr = 54 + 96 + 192
    - **A** — Mr = 342
- **A hydrated salt (water of crystallisation)** — Calculate the relative formula mass of hydrated copper(II) sulfate, CuSO₄·5H₂O. Ar: Cu = 63.5, S = 32, O = 16, H = 1.
    - **F** — find the Mr of CuSO₄, then add 5 × Mr(H₂O)
    - **I** — CuSO₄ = 63.5 + 32 + 64 = 159.5;  5 × H₂O = 5 × 18 = 90
    - **F** — Mr = 159.5 + 90
    - **A** — Mr = 249.5

---

## Mass Changes in Reactions  ·  `mass-changes-reactions`  ·  AQA 5.3.1.3

> **Tier presence:** Combined + Triple, Foundation + Higher (all four cells).
>
> **How the cells are composed** (item numbers below): **CF** → Q1–10; **CH** → Q1–5, 11–15; **TF** → Q1–10, 16–17; **TH** → Q1–5, 11–15, 18–19. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often expect a metal to LOSE mass when it burns, because burning seems to destroy things. In fact the solid gains mass: oxygen from the air combines with the metal and becomes part of the solid oxide. Mass is still conserved — the gain in the solid is exactly equal to the mass of oxygen taken from the air.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1.** _(all four tiers (CF·CH·TF·TH))_ — A student heats calcium carbonate in an open crucible: CaCO₃ → CaO + CO₂. Predict what happens to the measured mass and explain why.
- [✔︎] The mass decreases — carbon dioxide gas is produced and escapes from the open crucible
- [ ] The mass increases — oxygen from the air is absorbed
    - _why wrong:_ No oxygen is absorbed here: the carbonate is decomposing, not burning. A gas (CO₂) is released and escapes.
- [ ] The mass stays the same — mass is always conserved
    - _why wrong:_ Mass is conserved for the whole system, but in an OPEN crucible the CO₂ leaves, so the mass remaining falls.
- [ ] The mass first rises, then falls
    - _why wrong:_ There is no initial rise — CO₂ is produced and escapes from the moment heating begins.

**Q2.** _(all four tiers (CF·CH·TF·TH))_ — Explain why the mass of iron increases when it rusts in air.
- [✔︎] Oxygen from the air combines with the iron and becomes part of the solid iron oxide, adding to its mass
- [ ] Water condenses on the rust, adding extra mass
    - _why wrong:_ Moisture speeds up rusting, but the mass gain is oxygen from the air becoming part of the solid: 4Fe + 3O₂ → 2Fe₂O₃.
- [ ] The iron becomes denser, so the same volume has more mass
    - _why wrong:_ Density changes do not add matter. The extra mass is oxygen absorbed from the air.
- [ ] Iron oxide has more atoms per formula unit than iron
    - _why wrong:_ It is the MASS of oxygen combined with the iron that increases the total, not the atom count.

**Q3.** _(all four tiers (CF·CH·TF·TH))_ — A piece of magnesium ribbon is burned in an open crucible. Predict what happens to the mass of the solid and explain why.
- [✔︎] It increases — oxygen from the air joins the magnesium to form solid magnesium oxide
- [ ] It decreases — the magnesium is burned away
    - _why wrong:_ Burning does not destroy the magnesium; oxygen is added to it, so the solid gains mass.
- [ ] It stays the same — burning does not change the mass
    - _why wrong:_ The solid gains the mass of the oxygen that combines with it: the reading rises.
- [ ] It decreases — light and heat carry mass away
    - _why wrong:_ Light and heat are energy, not mass. The solid gains mass because oxygen is added.

**Q4.** _(all four tiers (CF·CH·TF·TH))_ — Predict what happens to the measured mass when a metal carbonate is thermally decomposed in an open tube.
- [✔︎] It decreases — carbon dioxide gas is given off and leaves the open tube
- [ ] It increases — a gas is taken in from the air
    - _why wrong:_ Decomposition releases CO₂; no gas is taken in. The mass falls.
- [ ] It stays the same — no gas is involved
    - _why wrong:_ Thermal decomposition of a carbonate releases CO₂ gas, so the open tube loses mass.
- [ ] It increases — the oxide formed is heavier than the carbonate
    - _why wrong:_ The oxide left behind is LIGHTER than the carbonate, because the CO₂ has escaped.

**Q5. ⭐** _(all four tiers (CF·CH·TF·TH))_ — 48 g of magnesium reacts with oxygen and the mass of the solid rises to 80 g of magnesium oxide. Calculate the mass of oxygen added from the air.
- [✔︎] 32 g — mass of oxygen = mass of oxide − mass of metal = 80 − 48
- [ ] 128 g — 80 + 48, adding the masses
    - _why wrong:_ The oxygen added is the GAIN in mass: 80 − 48 = 32 g. Adding would exceed the product mass.
- [ ] 80 g — the oxygen equals the mass of the oxide
    - _why wrong:_ The oxide also contains the magnesium; the oxygen alone is 80 − 48 = 32 g.
- [ ] 48 g — the oxygen equals the mass of the magnesium
    - _why wrong:_ There is no reason these are equal. The oxygen added is 80 − 48 = 32 g.

**Q6.** _(both Foundation tiers (CF·TF))_ — A reaction that produces a gas is carried out in a SEALED container. State what happens to the measured mass.
- [✔︎] It stays the same — the gas cannot escape from a sealed container
- [ ] It decreases, because a gas is made
    - _why wrong:_ In a SEALED container the gas stays inside, so the total mass does not change.
- [ ] It increases, because a gas is made
    - _why wrong:_ Making a gas from the reactants adds no mass; and nothing enters a sealed container.
- [ ] It depends on which gas is made
    - _why wrong:_ In a sealed container the mass is unchanged whatever the gas, because nothing leaves.

**Q7.** _(both Foundation tiers (CF·TF))_ — Name the gas from the air that is absorbed when a metal such as magnesium is burned.
- [✔︎] Oxygen
- [ ] Carbon dioxide
    - _why wrong:_ Metals burn by combining with oxygen, not carbon dioxide.
- [ ] Nitrogen
    - _why wrong:_ Nitrogen is fairly unreactive; it is oxygen that combines with the metal.
- [ ] Hydrogen
    - _why wrong:_ Hydrogen is not the gas absorbed from air; burning adds oxygen to the metal.

**Q8.** _(both Foundation tiers (CF·TF))_ — State why the measured mass appears to decrease when a carbonate reacts with acid in an open flask.
- [✔︎] A gas (carbon dioxide) is produced and escapes into the air
- [ ] The acid is used up and disappears
    - _why wrong:_ The acid reacts but does not disappear; the mass falls because CO₂ gas escapes.
- [ ] Mass is destroyed during the reaction
    - _why wrong:_ Mass is never destroyed; the loss is CO₂ gas leaving the open flask.
- [ ] The flask absorbs some of the liquid
    - _why wrong:_ The flask does not absorb the liquid; the fall is due to CO₂ gas escaping.

**Q9.** _(both Foundation tiers (CF·TF))_ — A piece of magnesium ribbon is burned in a crucible. Predict whether the mass of the solid goes up or down.
- [✔︎] Up — the magnesium gains oxygen from the air
- [ ] Down — the magnesium is burned away
    - _why wrong:_ Burning adds oxygen to the magnesium, so the solid gains mass.
- [ ] It stays the same
    - _why wrong:_ The solid gains the mass of oxygen that combines with it, so it goes up.
- [ ] It cannot be predicted
    - _why wrong:_ Burning a metal in air always adds oxygen, so the solid's mass rises.

**Q10.** _(both Foundation tiers (CF·TF))_ — A reaction produces a gas. State what you could do so that the measured mass does NOT decrease.
- [✔︎] Carry out the reaction in a closed (sealed) container so the gas cannot escape
- [ ] Heat the reaction more strongly
    - _why wrong:_ Heating harder does not stop gas escaping; using a sealed container does.
- [ ] Use more of each reactant
    - _why wrong:_ Using more reactant makes more gas, which still escapes from an open container.
- [ ] Weigh the mixture more quickly
    - _why wrong:_ Weighing faster does not change the result; a sealed container keeps the gas in.

**Q11.** _(both Higher tiers (CH·TH))_ — Explain, in terms of particles, why the mass inside an open flask decreases when a carbonate reacts with acid.
- [✔︎] The reaction makes carbon dioxide particles; these gas particles leave the open flask, and because they still have mass, the mass remaining in the flask falls (the total mass is unchanged)
- [ ] The reacting particles shrink, lowering the mass
    - _why wrong:_ Particles do not shrink. The mass falls because CO₂ gas particles leave the flask.
- [ ] Some particles are destroyed in the reaction
    - _why wrong:_ Particles are never destroyed; they are rearranged into CO₂ which escapes.
- [ ] The gas particles are weightless once formed
    - _why wrong:_ Gas particles have mass. The fall in reading equals the mass of gas that has left.

**Q12. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of magnesium oxide formed when 6 g of magnesium burns completely. 2Mg + O₂ → 2MgO. Ar: Mg = 24, O = 16.
- [✔︎] 10 g — n(Mg) = 6 ÷ 24 = 0.25 mol; ratio Mg:MgO = 1:1; mass = 0.25 × 40
- [ ] 6 g — the oxide has the same mass as the magnesium
    - _why wrong:_ Oxygen is added, so the oxide is heavier: 0.25 mol × 40 = 10 g.
- [ ] 240 g — 6 × 40, using mass instead of moles
    - _why wrong:_ You must convert to moles first: n = 6 ÷ 24 = 0.25 mol, then × Mr(MgO) = 40.
- [ ] 15 g — using Mr(MgO) = 60
    - _why wrong:_ The Mr of MgO is 24 + 16 = 40, not 60: 0.25 × 40 = 10 g.

**Q13. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of carbon dioxide released when 25 g of calcium carbonate decomposes completely. CaCO₃ → CaO + CO₂. Mr: CaCO₃ = 100, CO₂ = 44.
- [✔︎] 11 g — n(CaCO₃) = 25 ÷ 100 = 0.25 mol; ratio 1:1; mass = 0.25 × 44
- [ ] 25 g — the CO₂ has the same mass as the carbonate
    - _why wrong:_ Only part of the carbonate becomes CO₂: n = 0.25 mol, mass = 0.25 × 44 = 11 g.
- [ ] 14 g — the mass of CaO left behind
    - _why wrong:_ The question asks for the CO₂, which is 0.25 × 44 = 11 g (and 25 − 11 = 14 g of CaO remains).
- [ ] 1100 g — 25 × 44, using mass instead of moles
    - _why wrong:_ Convert to moles first: 25 ÷ 100 = 0.25 mol, then × 44 = 11 g.

**Q14.** _(both Higher tiers (CH·TH))_ — A reaction that makes a gas is carried out in a sealed flask, which is weighed before and after. Explain why the reading is unchanged even though a gas is formed.
- [✔︎] The gas cannot leave the sealed flask, so every atom that was present at the start is still inside at the end — no mass enters or leaves, so the total is unchanged
- [ ] The gas has no mass, so making it changes nothing
    - _why wrong:_ The gas does have mass; the reading is unchanged because the gas stays sealed inside.
- [ ] The gas turns back into the reactants
    - _why wrong:_ The reaction still occurs; the mass is unchanged simply because nothing can leave the sealed flask.
- [ ] Mass is created to replace the gas that forms
    - _why wrong:_ No mass is created. The total is unchanged because the sealed flask keeps all the atoms inside.

**Q15.** _(both Higher tiers (CH·TH))_ — Burning magnesium in an open crucible makes the solid appear to gain mass. Evaluate whether this breaks the law of conservation of mass.
- [✔︎] It does not break the law — the gain equals the mass of oxygen taken from the air, so the total mass of the magnesium plus the air it reacts with is unchanged
- [ ] Yes — mass is created when the oxide forms
    - _why wrong:_ No mass is created; the solid gains the oxygen that was already present in the air.
- [ ] Yes — the solid ends up heavier than the reactant
    - _why wrong:_ The solid is heavier only because oxygen has been added to it; counting the air too, mass is conserved.
- [ ] No — because no gas is involved in burning
    - _why wrong:_ A gas IS involved: oxygen from the air. Its mass is added to the solid, so the total is conserved.

**Q16.** _(Triple-Foundation extra)_ — A precipitation reaction between two solutions is carried out in an open beaker, with no gas produced. State what happens to the total mass.
- [✔︎] It stays the same — no gas enters or leaves, so mass is conserved
- [ ] It decreases, because a solid forms
    - _why wrong:_ Forming a precipitate rearranges the dissolved ions; no mass leaves, so the total is unchanged.
- [ ] It increases, because a new solid appears
    - _why wrong:_ The precipitate comes from ions already in solution; no mass is added.
- [ ] It cannot be predicted in an open beaker
    - _why wrong:_ With no gas involved, nothing leaves the open beaker, so the mass is unchanged.

**Q17.** _(Triple-Foundation extra)_ — State one everyday example in which a solid gains mass because a gas is absorbed.
- [✔︎] Iron rusting (or a metal burning) — oxygen from the air combines with the metal
- [ ] Ice melting into water
    - _why wrong:_ Melting is a change of state with no gas absorbed and no change in mass.
- [ ] Sugar dissolving in tea
    - _why wrong:_ Dissolving spreads the sugar out but adds no mass and absorbs no gas.
- [ ] A candle being blown out
    - _why wrong:_ Blowing out a candle stops the reaction; it is not an example of a solid gaining mass.

**Q18. ⭐** _(Triple-Higher extra)_ — Calculate the mass of oxygen needed to burn 4.8 g of magnesium completely. 2Mg + O₂ → 2MgO. Ar: Mg = 24, O = 16.
- [✔︎] 3.2 g — n(Mg) = 4.8 ÷ 24 = 0.2 mol; ratio Mg:O₂ = 2:1 so n(O₂) = 0.1 mol; mass = 0.1 × 32
- [ ] 6.4 g — using a 1:1 ratio for Mg:O₂
    - _why wrong:_ The ratio is 2Mg:1O₂, so n(O₂) = 0.2 ÷ 2 = 0.1 mol, giving 0.1 × 32 = 3.2 g.
- [ ] 1.6 g — using Mr(O₂) = 16
    - _why wrong:_ Oxygen gas is O₂ with Mr = 32, not 16: 0.1 × 32 = 3.2 g.
- [ ] 0.1 g — stopping at the moles of O₂
    - _why wrong:_ 0.1 mol must be multiplied by Mr(O₂) = 32 to get the mass: 3.2 g.

**Q19.** _(Triple-Higher extra)_ — When steel wool is heated in air its mass increases. Explain why this increase is evidence that a new substance has been made.
- [✔︎] The gain equals the mass of oxygen that has combined with the iron to form iron oxide, a new compound; if no reaction had happened the mass would have stayed the same
- [ ] The heat makes the metal expand, raising its mass
    - _why wrong:_ Expansion changes volume, not mass. The gain is oxygen chemically combining to make a new compound.
- [ ] Hot metal always weighs more than cold metal
    - _why wrong:_ Temperature does not change mass. The rise is due to oxygen joining the iron to form iron oxide.
- [ ] The steel wool absorbs moisture from the air
    - _why wrong:_ The gain is oxygen forming iron oxide, a new substance — a chemical change, not just absorbed water.

**FIFA worked examples — Foundation (in CF & TF)** ⭐

- **Mass gained = mass of gas added** — A 40 g sample of copper is heated in air and forms 50 g of copper oxide. Calculate the mass of oxygen that combined with the copper.
    - **F** — mass gained by the solid = mass of oxygen added
    - **I** — mass of O₂ = mass of oxide − mass of metal = 50 − 40
    - **F** — 50 − 40 = 10
    - **A** — mass of oxygen = 10 g
- **Mass lost = mass of gas escaped** — When 25 g of a metal carbonate is heated in an open tube, 16 g of solid oxide is left. Calculate the mass of carbon dioxide that escaped.
    - **F** — mass lost by the solid = mass of gas that escaped
    - **I** — mass of CO₂ = 25 − 16
    - **F** — 25 − 16 = 9
    - **A** — mass of carbon dioxide = 9 g
- **A decimal mass gain** — 3.0 g of magnesium is burned and forms 5.0 g of magnesium oxide. Calculate the mass of oxygen taken from the air.
    - **F** — mass gained by the solid = mass of oxygen added
    - **I** — mass of O₂ = 5.0 − 3.0
    - **F** — 5.0 − 3.0 = 2.0
    - **A** — mass of oxygen = 2.0 g

**FIFA worked examples — Higher (in CH & TH)** ⭐

- **Reacting mass: mass → moles → mass** — Calculate the mass of magnesium oxide formed when 6 g of magnesium burns completely. 2Mg + O₂ → 2MgO. Ar: Mg = 24, O = 16.
    - **F** — mass → moles (÷ Mr) → use the equation ratio → moles → mass (× Mr)
    - **I** — n(Mg) = 6 ÷ 24 = 0.25 mol;  ratio Mg:MgO = 1:1 so n(MgO) = 0.25 mol;  Mr(MgO) = 40
    - **F** — mass(MgO) = 0.25 × 40
    - **A** — mass of magnesium oxide = 10 g
- **Reacting mass for a decomposition** — Calculate the mass of carbon dioxide released when 25 g of calcium carbonate decomposes. CaCO₃ → CaO + CO₂. Mr: CaCO₃ = 100, CO₂ = 44.
    - **F** — mass → moles (÷ Mr) → ratio → moles → mass (× Mr)
    - **I** — n(CaCO₃) = 25 ÷ 100 = 0.25 mol;  ratio 1:1 so n(CO₂) = 0.25 mol;  Mr(CO₂) = 44
    - **F** — mass(CO₂) = 0.25 × 44
    - **A** — mass of carbon dioxide = 11 g
- **Using a 2:1 ratio** — Calculate the mass of oxygen needed to burn 4.8 g of magnesium completely. 2Mg + O₂ → 2MgO. Ar: Mg = 24, O = 16.
    - **F** — mass → moles (÷ Mr) → use the 2:1 ratio → moles → mass (× Mr)
    - **I** — n(Mg) = 4.8 ÷ 24 = 0.2 mol;  ratio Mg:O₂ = 2:1 so n(O₂) = 0.1 mol;  Mr(O₂) = 32
    - **F** — mass(O₂) = 0.1 × 32
    - **A** — mass of oxygen = 3.2 g

---

## Chemical Measurements  ·  `chemical-measurements`  ·  AQA 5.3.1.4

> **Tier presence:** Combined + Triple, Foundation + Higher (all four cells).
>
> **How the cells are composed** (item numbers below): **CF** → Q1–10; **CH** → Q1–5, 11–15; **TF** → Q1–10, 16–17; **TH** → Q1–5, 11–15, 18–19. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often use the TOP of the curved surface (the meniscus) when they read a burette or measuring cylinder, which gives a volume reading that is too large. The scale is calibrated to the BOTTOM of the meniscus, because water curves downwards in a glass tube. Line your eye up level with the bottom of the meniscus and read the scale from there.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(all four tiers (CF·CH·TF·TH))_ — A burette (uncertainty ±0.05 cm³) and a measuring cylinder (uncertainty ±1 cm³) both deliver 25 cm³. Determine which gives the lower percentage uncertainty.
- [✔︎] The burette — % uncertainty = (0.05 ÷ 25) × 100 = 0.2%, against 4% for the cylinder
- [ ] The measuring cylinder — larger apparatus is always more accurate
    - _why wrong:_ Size does not set precision; the smaller uncertainty relative to the reading does. The burette wins at 0.2%.
- [ ] They are the same — both deliver 25 cm³
    - _why wrong:_ Same volume, but different uncertainties: 0.05 cm³ vs 1 cm³. The burette is far more precise.
- [ ] The measuring cylinder — it has the smaller absolute uncertainty
    - _why wrong:_ The cylinder's uncertainty (±1 cm³) is LARGER than the burette's (±0.05 cm³), so it is less precise.

**Q2. ⭐** _(all four tiers (CF·CH·TF·TH))_ — A balance reads to ±0.01 g. A student weighs 2.00 g of solid on it. Calculate the percentage uncertainty in this mass.
- [✔︎] 0.5% — (0.01 ÷ 2.00) × 100
- [ ] 2.0% — (0.01 ÷ 0.5) × 100, using the wrong value
    - _why wrong:_ Divide the uncertainty by the measured value, 2.00 g: (0.01 ÷ 2.00) × 100 = 0.5%.
- [ ] 0.005% — (0.01 ÷ 2.00) without the × 100
    - _why wrong:_ Percentage uncertainty must be multiplied by 100: 0.005 × 100 = 0.5%.
- [ ] 0.02% — dividing 2.00 by 0.01 and misplacing the point
    - _why wrong:_ The calculation is uncertainty ÷ value: 0.01 ÷ 2.00 = 0.005, then × 100 = 0.5%.

**Q3.** _(all four tiers (CF·CH·TF·TH))_ — Explain why a burette gives a more precise volume measurement than a measuring cylinder.
- [✔︎] A burette has a much smaller uncertainty (about ±0.05 cm³) because its graduations are finer, so each reading is closer to the true volume
- [ ] A burette holds a larger volume, so it must be more precise
    - _why wrong:_ Precision depends on the size of the uncertainty, not the capacity; the burette's fine graduations give ±0.05 cm³.
- [ ] A burette is made of thicker glass, which reduces errors
    - _why wrong:_ Glass thickness is irrelevant; it is the fine graduations and small uncertainty that make it precise.
- [ ] A measuring cylinder cannot measure volumes accurately at all
    - _why wrong:_ A measuring cylinder does measure volume, just less precisely (±0.5 to ±1 cm³) than a burette.

**Q4.** _(all four tiers (CF·CH·TF·TH))_ — Two students measure the same 25.0 cm³ volume: one with a pipette (±0.06 cm³), one with a measuring cylinder (±0.5 cm³). Identify who has the more precise measurement and justify your choice.
- [✔︎] The pipette user — a smaller uncertainty (±0.06 cm³) means the reading is more tightly reproducible
- [ ] The measuring cylinder user — it is easier to read
    - _why wrong:_ Ease of reading is not precision; the pipette's smaller uncertainty (±0.06 cm³) makes it more precise.
- [ ] Neither — both measured 25.0 cm³
    - _why wrong:_ They measured the same volume but with different uncertainties; the pipette (±0.06 cm³) is more precise.
- [ ] The measuring cylinder user — a bigger uncertainty means a bigger, clearer scale
    - _why wrong:_ A bigger uncertainty means LESS precision, not more. The pipette is the more precise instrument.

**Q5. ⭐** _(all four tiers (CF·CH·TF·TH))_ — A student measures a temperature rise of 20.0 °C with a thermometer of uncertainty ±0.5 °C. Calculate the percentage uncertainty in this reading.
- [✔︎] 2.5% — (0.5 ÷ 20.0) × 100
- [ ] 0.025% — (0.5 ÷ 20.0) without the × 100
    - _why wrong:_ Percentage uncertainty must be multiplied by 100: 0.025 × 100 = 2.5%.
- [ ] 40% — (20.0 ÷ 0.5), dividing the wrong way
    - _why wrong:_ Divide the uncertainty by the value: (0.5 ÷ 20.0) × 100 = 2.5%.
- [ ] 10% — (0.5 ÷ 5.0) × 100, using the wrong value
    - _why wrong:_ Use the measured value of 20.0 °C: (0.5 ÷ 20.0) × 100 = 2.5%.

**Q6.** _(both Foundation tiers (CF·TF))_ — State where you should read the volume on a burette or measuring cylinder that contains water.
- [✔︎] From the bottom of the meniscus, with your eye level with it
- [ ] From the top of the meniscus
    - _why wrong:_ Reading from the top gives a value that is too large; the scale is set to the bottom of the meniscus.
- [ ] From the middle of the meniscus
    - _why wrong:_ Read consistently from the BOTTOM of the meniscus to match the calibration.
- [ ] From wherever is easiest to see
    - _why wrong:_ The reading point matters: always use the bottom of the meniscus to avoid a systematic error.

**Q7.** _(both Foundation tiers (CF·TF))_ — State the difference between the accuracy and the precision of a measurement.
- [✔︎] Accuracy is how close a reading is to the true value; precision is how close repeated readings are to each other
- [ ] They mean the same thing
    - _why wrong:_ They are different: accuracy is closeness to the true value, precision is reproducibility of repeats.
- [ ] Accuracy is reproducibility; precision is closeness to the true value
    - _why wrong:_ This is the wrong way round: accuracy = close to true value, precision = repeats close together.
- [ ] Accuracy is the size of the equipment; precision is its cost
    - _why wrong:_ Neither relates to size or cost: accuracy = closeness to true value, precision = reproducibility.

**Q8.** _(both Foundation tiers (CF·TF))_ — Name the piece of apparatus used to add an accurately measured, variable volume of solution during a titration.
- [✔︎] A burette
- [ ] A measuring cylinder
    - _why wrong:_ A measuring cylinder is far less precise; a titration uses a burette (±0.05 cm³).
- [ ] A conical flask
    - _why wrong:_ The conical flask holds the solution being tested; the measured volume is added from a burette.
- [ ] A beaker
    - _why wrong:_ A beaker gives only a rough volume; accurate variable volumes come from a burette.

**Q9.** _(both Foundation tiers (CF·TF))_ — Name the piece of apparatus used to measure out one fixed, accurate volume, such as exactly 25.0 cm³.
- [✔︎] A pipette
- [ ] A burette
    - _why wrong:_ A burette delivers variable volumes; a pipette is used for one fixed accurate volume.
- [ ] A measuring cylinder
    - _why wrong:_ A measuring cylinder is less precise; a fixed accurate volume is measured with a pipette.
- [ ] A dropper
    - _why wrong:_ A dropper cannot measure an accurate fixed volume; a pipette can.

**Q10.** _(both Foundation tiers (CF·TF))_ — State why a digital balance should be set to zero (tared) before a mass is measured.
- [✔︎] So that the mass of the container is not included, avoiding a systematic error
- [ ] So the reading changes faster
    - _why wrong:_ Taring does not affect speed; it removes the container's mass so it is not counted.
- [ ] So the balance uses less power
    - _why wrong:_ Taring is about accuracy, not power: it stops the container's mass being included.
- [ ] So the solid does not stick to the pan
    - _why wrong:_ Taring does not stop sticking; it sets the container's mass to zero first.

**Q11. ⭐** _(both Higher tiers (CH·TH))_ — In a titration the initial burette reading is 0.50 cm³ and the final reading is 24.90 cm³. Calculate the volume of solution added (the titre).
- [✔︎] 24.40 cm³ — titre = final − initial = 24.90 − 0.50
- [ ] 25.40 cm³ — 24.90 + 0.50, adding the readings
    - _why wrong:_ The titre is the DIFFERENCE between the readings: 24.90 − 0.50 = 24.40 cm³.
- [ ] 24.90 cm³ — the final reading only
    - _why wrong:_ The burette did not start at zero; subtract the initial reading: 24.90 − 0.50 = 24.40 cm³.
- [ ] 0.50 cm³ — the initial reading only
    - _why wrong:_ That is where the burette started; the titre is 24.90 − 0.50 = 24.40 cm³.

**Q12. ⭐** _(both Higher tiers (CH·TH))_ — A student's concordant titres are 24.10, 24.20 and 24.15 cm³. Calculate the mean titre.
- [✔︎] 24.15 cm³ — (24.10 + 24.20 + 24.15) ÷ 3 = 72.45 ÷ 3
- [ ] 72.45 cm³ — the sum, without dividing by 3
    - _why wrong:_ A mean divides the total by the number of values: 72.45 ÷ 3 = 24.15 cm³.
- [ ] 36.23 cm³ — dividing the sum by 2
    - _why wrong:_ There are three titres, so divide by 3: 72.45 ÷ 3 = 24.15 cm³.
- [ ] 24.20 cm³ — just the largest titre
    - _why wrong:_ The mean uses all three concordant results: 72.45 ÷ 3 = 24.15 cm³.

**Q13. ⭐** _(both Higher tiers (CH·TH))_ — In a titration a burette is read twice, each to ±0.05 cm³, giving a titre of 25.00 cm³. The uncertainty in the titre is 2 × 0.05 = 0.10 cm³. Calculate the percentage uncertainty in the titre.
- [✔︎] 0.40% — (0.10 ÷ 25.00) × 100
- [ ] 0.20% — using only one 0.05 cm³ reading
    - _why wrong:_ Two readings are taken, so the uncertainty is 2 × 0.05 = 0.10 cm³, giving 0.40%.
- [ ] 0.80% — using 0.20 cm³ for the uncertainty
    - _why wrong:_ Two readings give 0.10 cm³, not 0.20 cm³: (0.10 ÷ 25.00) × 100 = 0.40%.
- [ ] 4.0% — dividing by 2.5 instead of 25.00
    - _why wrong:_ Divide by the titre, 25.00 cm³: (0.10 ÷ 25.00) × 100 = 0.40%.

**Q14. ⭐** _(both Higher tiers (CH·TH))_ — Explain why a titration is repeated until concordant results are obtained and only those results are used to calculate the mean.
- [✔︎] Repeats that agree closely (concordant) show the results are reliable; using only the concordant titres removes anomalies, so the mean is more accurate
- [ ] Repeating uses up the leftover solutions
    - _why wrong:_ The purpose is reliability, not using up solution: concordant repeats give a more accurate mean.
- [ ] A single accurate reading is impossible with a burette
    - _why wrong:_ One careful reading can be accurate, but repeats that agree confirm reliability and improve the mean.
- [ ] Averaging every titre, including rough ones, is always best
    - _why wrong:_ Anomalous (non-concordant) titres are excluded; only concordant results are averaged.

**Q15.** _(both Higher tiers (CH·TH))_ — A student measures a mass on a balance of fixed resolution and wants a smaller percentage uncertainty. Suggest how they could achieve this.
- [✔︎] Measure a larger mass — the same absolute uncertainty is then a smaller fraction of the reading
- [ ] Measure a smaller mass
    - _why wrong:_ A smaller mass makes the fixed uncertainty a LARGER fraction, increasing the percentage uncertainty.
- [ ] Repeat the same measurement several times
    - _why wrong:_ Repeating the identical measurement on the same balance does not reduce its fixed resolution uncertainty; a larger mass does.
- [ ] Round the reading to fewer decimal places
    - _why wrong:_ Rounding discards precision and does not lower the true percentage uncertainty; measuring a larger mass does.

**Q16.** _(Triple-Foundation extra)_ — Name a suitable instrument for measuring the temperature change in a reaction and state a typical uncertainty for it.
- [✔︎] A thermometer — typically ±0.5 °C (or ±1 °C)
- [ ] A burette — ±0.05 cm³
    - _why wrong:_ A burette measures volume, not temperature; a thermometer (±0.5 °C) measures temperature change.
- [ ] A balance — ±0.01 g
    - _why wrong:_ A balance measures mass; temperature change is measured with a thermometer.
- [ ] A stopwatch — ±0.1 s
    - _why wrong:_ A stopwatch measures time; temperature change is measured with a thermometer.

**Q17.** _(Triple-Foundation extra)_ — State what is meant by a systematic error and give one example.
- [✔︎] An error that shifts every reading in the same direction by a similar amount — for example, not zeroing (taring) the balance
- [ ] A one-off mistake that affects a single reading
    - _why wrong:_ That describes a random error or slip; a systematic error affects every reading the same way.
- [ ] An error caused by reading the scale differently each time
    - _why wrong:_ That is a random error; a systematic error is a consistent shift, such as a balance not tared.
- [ ] An error that always cancels out on repeating
    - _why wrong:_ Systematic errors do NOT cancel on repeating — they shift every reading the same way.

**Q18. ⭐** _(Triple-Higher extra)_ — A reaction's temperature is measured as rising by 8.0 °C, with the thermometer read to ±0.5 °C at both the start and the end. The uncertainty in the change is 2 × 0.5 = 1.0 °C. Calculate the percentage uncertainty in the temperature change.
- [✔︎] 12.5% — (1.0 ÷ 8.0) × 100
- [ ] 6.25% — using only one 0.5 °C reading
    - _why wrong:_ A change uses two readings, so the uncertainty is 2 × 0.5 = 1.0 °C, giving 12.5%.
- [ ] 1.25% — (1.0 ÷ 8.0) without the × 100
    - _why wrong:_ Multiply by 100 for a percentage: 0.125 × 100 = 12.5%.
- [ ] 16% — using 1.28 °C uncertainty
    - _why wrong:_ The uncertainty is 2 × 0.5 = 1.0 °C: (1.0 ÷ 8.0) × 100 = 12.5%.

**Q19. ⭐** _(Triple-Higher extra)_ — Two burettes each deliver a 20.00 cm³ titre. Burette A has ±0.05 cm³ per reading, burette B ±0.10 cm³ per reading (two readings each). Deduce which gives the lower percentage uncertainty and calculate it.
- [✔︎] Burette A — uncertainty 2 × 0.05 = 0.10 cm³, so (0.10 ÷ 20.00) × 100 = 0.5%
- [ ] Burette B, 0.5% — its uncertainty is smaller
    - _why wrong:_ Burette B has the LARGER uncertainty (±0.10 per reading); A gives the lower value, 0.5%.
- [ ] Burette A, 0.25% — using one reading's 0.05 cm³
    - _why wrong:_ Two readings give 0.10 cm³, so (0.10 ÷ 20.00) × 100 = 0.5%, not 0.25%.
- [ ] Both the same — they deliver the same titre
    - _why wrong:_ Same titre, but A has the smaller uncertainty (0.10 vs 0.20 cm³), so A gives 0.5% vs B's 1.0%.

**FIFA worked examples — Foundation (in CF & TF)** ⭐

- **Percentage uncertainty of one reading** — A student measures 25.0 cm³ using a measuring cylinder with an uncertainty of ±0.5 cm³. Calculate the percentage uncertainty.
    - **F** — % uncertainty = (uncertainty ÷ measured value) × 100
    - **I** — = (0.5 ÷ 25.0) × 100
    - **F** — = 0.02 × 100
    - **A** — = 2.0%
- **A mass on a balance** — A balance with an uncertainty of ±0.01 g is used to weigh 5.00 g of solid. Calculate the percentage uncertainty.
    - **F** — % uncertainty = (uncertainty ÷ measured value) × 100
    - **I** — = (0.01 ÷ 5.00) × 100
    - **F** — = 0.002 × 100
    - **A** — = 0.2%
- **A temperature reading** — A thermometer with an uncertainty of ±0.5 °C reads a temperature of 50.0 °C. Calculate the percentage uncertainty.
    - **F** — % uncertainty = (uncertainty ÷ measured value) × 100
    - **I** — = (0.5 ÷ 50.0) × 100
    - **F** — = 0.01 × 100
    - **A** — = 1.0%

**FIFA worked examples — Higher (in CH & TH)** ⭐

- **Titre and its percentage uncertainty** — A burette is read at the start (0.00 cm³) and end (25.00 cm³), each to ±0.05 cm³. Calculate the titre and its percentage uncertainty.
    - **F** — titre = final − initial; total uncertainty = 2 × 0.05; % uncertainty = (uncertainty ÷ titre) × 100
    - **I** — titre = 25.00 − 0.00 = 25.00 cm³; uncertainty = 0.10 cm³
    - **F** — % uncertainty = (0.10 ÷ 25.00) × 100
    - **A** — titre = 25.00 cm³; percentage uncertainty = 0.40%
- **Mean of concordant titres** — A student's concordant titres are 23.10, 23.20 and 23.15 cm³. Calculate the mean titre to use in a concentration calculation.
    - **F** — mean = sum of concordant titres ÷ number of titres
    - **I** — = (23.10 + 23.20 + 23.15) ÷ 3
    - **F** — = 69.45 ÷ 3
    - **A** — mean titre = 23.15 cm³
- **Uncertainty in a measured change** — A temperature rise of 8.0 °C is measured with a thermometer read to ±0.5 °C at the start and end. Calculate the percentage uncertainty in the temperature change.
    - **F** — uncertainty in a change = 2 × (uncertainty of one reading); % uncertainty = (uncertainty ÷ change) × 100
    - **I** — uncertainty = 2 × 0.5 = 1.0 °C; % uncertainty = (1.0 ÷ 8.0) × 100
    - **F** — = 0.125 × 100
    - **A** — = 12.5%

---

## Concentration of Solutions  ·  `concentration-of-solutions`  ·  AQA 5.3.2.5

> **Tier presence:** Combined + Triple, Foundation + Higher (all four cells).
>
> **How the cells are composed** (item numbers below): **CF** → Q1–10; **CH** → Q1–5, 11–15; **TF** → Q1–10, 16–17; **TH** → Q1–5, 11–15, 18–19. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students frequently forget to convert the volume from cm³ into dm³ before using the concentration formula, so their answer comes out 1000 times too big or too small. The formula needs the volume in dm³: divide any volume in cm³ by 1000 first (250 cm³ = 0.250 dm³). Convert the volume before you divide, every single time.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(all four tiers (CF·CH·TF·TH))_ — 25 g of glucose is dissolved in water to make 500 cm³ of solution. Calculate the concentration in g/dm³.
- [✔︎] 50 g/dm³ — volume = 500 ÷ 1000 = 0.5 dm³, so concentration = 25 ÷ 0.5
- [ ] 0.05 g/dm³ — 25 ÷ 500, without converting to dm³
    - _why wrong:_ The volume must be in dm³: 500 cm³ = 0.5 dm³, giving 25 ÷ 0.5 = 50 g/dm³ (this answer is 1000× too small).
- [ ] 12 500 g/dm³ — 25 × 500
    - _why wrong:_ Concentration is mass ÷ volume, not mass × volume, and the volume must be in dm³.
- [ ] 2.5 g/dm³ — 25 ÷ 10
    - _why wrong:_ 500 cm³ converts to 0.5 dm³ (÷1000), not 10 dm³: 25 ÷ 0.5 = 50 g/dm³.

**Q2. ⭐** _(all four tiers (CF·CH·TF·TH))_ — A solution has a concentration of 80 g/dm³. Calculate the mass of solute in 250 cm³ of it.
- [✔︎] 20 g — mass = concentration × volume = 80 × 0.25 dm³
- [ ] 20 000 g — 80 × 250, without converting to dm³
    - _why wrong:_ Convert 250 cm³ to 0.25 dm³ first: 80 × 0.25 = 20 g.
- [ ] 0.32 g — 80 ÷ 250
    - _why wrong:_ Dividing gives a volume, not a mass. Mass = concentration × volume = 80 × 0.25 = 20 g.
- [ ] 320 g — 80 × (250 ÷ 10)
    - _why wrong:_ 250 cm³ = 0.25 dm³ (÷1000), not 25 dm³: 80 × 0.25 = 20 g.

**Q3. ⭐** _(all four tiers (CF·CH·TF·TH))_ — 40 g of copper sulfate is dissolved to make 2 dm³ of solution. Calculate the concentration in g/dm³.
- [✔︎] 20 g/dm³ — 40 ÷ 2
- [ ] 80 g/dm³ — 40 × 2
    - _why wrong:_ Concentration is mass ÷ volume, not mass × volume: 40 ÷ 2 = 20 g/dm³.
- [ ] 0.05 g/dm³ — 2 ÷ 40
    - _why wrong:_ Divide mass by volume, not volume by mass: 40 ÷ 2 = 20 g/dm³.
- [ ] 42 g/dm³ — 40 + 2
    - _why wrong:_ Concentration is a division, not an addition: 40 ÷ 2 = 20 g/dm³.

**Q4.** _(all four tiers (CF·CH·TF·TH))_ — A solution is diluted by adding more water. Predict what happens to its concentration and explain why.
- [✔︎] The concentration decreases — the same mass of solute is now spread through a larger volume
- [ ] It increases — there is more liquid so more solute
    - _why wrong:_ Adding water adds no solute; the fixed mass in a larger volume means a lower concentration.
- [ ] It stays the same — dilution does not change concentration
    - _why wrong:_ Dilution increases the volume without adding solute, so the concentration falls.
- [ ] It increases — water is a solute as well
    - _why wrong:_ Water is the solvent here, not the solute; adding it lowers the concentration of the dissolved solid.

**Q5. ⭐** _(all four tiers (CF·CH·TF·TH))_ — A solution has a concentration of 25 g/dm³. Calculate the volume, in dm³, that contains 10 g of solute.
- [✔︎] 0.4 dm³ — volume = mass ÷ concentration = 10 ÷ 25
- [ ] 250 dm³ — 10 × 25
    - _why wrong:_ Volume is mass ÷ concentration, not mass × concentration: 10 ÷ 25 = 0.4 dm³.
- [ ] 2.5 dm³ — 25 ÷ 10
    - _why wrong:_ Divide the mass by the concentration, not the other way round: 10 ÷ 25 = 0.4 dm³.
- [ ] 15 dm³ — 25 − 10
    - _why wrong:_ Volume comes from a division, not a subtraction: 10 ÷ 25 = 0.4 dm³.

**Q6.** _(both Foundation tiers (CF·TF))_ — Define the concentration of a solution.
- [✔︎] The mass (or amount) of solute dissolved in a given volume of solution
- [ ] The total volume of the solution
    - _why wrong:_ Concentration is not just the volume; it is how much solute is present per unit volume.
- [ ] The mass of the solvent used
    - _why wrong:_ Concentration is about the SOLUTE per volume of solution, not the mass of solvent.
- [ ] The temperature at which a solid dissolves
    - _why wrong:_ That is solubility-related; concentration is solute mass per unit volume of solution.

**Q7.** _(both Foundation tiers (CF·TF))_ — State the units of concentration used most often in this topic.
- [✔︎] Grams per cubic decimetre (g/dm³)
- [ ] Grams (g)
    - _why wrong:_ Grams alone measure mass; concentration is a mass per volume, g/dm³.
- [ ] Cubic decimetres (dm³)
    - _why wrong:_ dm³ measures volume; concentration is mass per volume, g/dm³.
- [ ] Grams per gram (g/g)
    - _why wrong:_ Concentration relates mass of solute to VOLUME of solution: g/dm³.

**Q8.** _(both Foundation tiers (CF·TF))_ — State how you convert a volume measured in cm³ into dm³.
- [✔︎] Divide the volume in cm³ by 1000
- [ ] Multiply the volume in cm³ by 1000
    - _why wrong:_ That makes the number bigger; to go from cm³ to dm³ you divide by 1000.
- [ ] Divide the volume in cm³ by 100
    - _why wrong:_ There are 1000 cm³ in 1 dm³, so divide by 1000, not 100.
- [ ] Multiply the volume in cm³ by 10
    - _why wrong:_ The conversion factor is 1000: divide cm³ by 1000 to get dm³.

**Q9. ⭐** _(both Foundation tiers (CF·TF))_ — 5 g of salt is dissolved to make 0.5 dm³ of solution. State the concentration in g/dm³.
- [✔︎] 10 g/dm³ — 5 ÷ 0.5
- [ ] 2.5 g/dm³ — 5 × 0.5
    - _why wrong:_ Concentration is mass ÷ volume: 5 ÷ 0.5 = 10 g/dm³.
- [ ] 0.1 g/dm³ — 0.5 ÷ 5
    - _why wrong:_ Divide the mass by the volume, not the volume by the mass: 5 ÷ 0.5 = 10 g/dm³.
- [ ] 5 g/dm³ — the mass of salt used
    - _why wrong:_ The volume is only 0.5 dm³, so the concentration is 5 ÷ 0.5 = 10 g/dm³.

**Q10.** _(both Foundation tiers (CF·TF))_ — State whether a concentrated solution contains more or less solute per dm³ than a dilute one.
- [✔︎] More solute per dm³
- [ ] Less solute per dm³
    - _why wrong:_ 'Concentrated' means MORE solute per unit volume; 'dilute' means less.
- [ ] The same amount, but in a larger volume
    - _why wrong:_ A concentrated solution has more solute per dm³, not the same amount spread out.
- [ ] It depends only on the temperature
    - _why wrong:_ Concentration is about solute per volume; concentrated = more solute per dm³.

**Q11. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the concentration in mol/dm³ of a solution containing 0.5 mol of HCl in 250 cm³ of solution.
- [✔︎] 2 mol/dm³ — volume = 0.25 dm³, so concentration = 0.5 ÷ 0.25
- [ ] 0.002 mol/dm³ — 0.5 ÷ 250, without converting to dm³
    - _why wrong:_ Convert 250 cm³ to 0.25 dm³ first: 0.5 ÷ 0.25 = 2 mol/dm³.
- [ ] 125 mol/dm³ — 0.5 × 250
    - _why wrong:_ Concentration is moles ÷ volume, and the volume must be in dm³: 0.5 ÷ 0.25 = 2 mol/dm³.
- [ ] 0.5 mol/dm³ — using the moles as the concentration
    - _why wrong:_ Divide the moles by the volume in dm³: 0.5 ÷ 0.25 = 2 mol/dm³.

**Q12. ⭐** _(both Higher tiers (CH·TH))_ — A sodium hydroxide solution has a concentration of 80 g/dm³. Calculate its concentration in mol/dm³. Mr of NaOH = 40.
- [✔︎] 2 mol/dm³ — concentration (mol/dm³) = concentration (g/dm³) ÷ Mr = 80 ÷ 40
- [ ] 3200 mol/dm³ — 80 × 40
    - _why wrong:_ Divide by the Mr, do not multiply: 80 ÷ 40 = 2 mol/dm³.
- [ ] 40 mol/dm³ — 80 ÷ 2
    - _why wrong:_ Divide by the Mr of NaOH (40), not by 2: 80 ÷ 40 = 2 mol/dm³.
- [ ] 0.5 mol/dm³ — 40 ÷ 80, dividing the wrong way
    - _why wrong:_ Concentration in mol/dm³ = g/dm³ ÷ Mr = 80 ÷ 40 = 2 mol/dm³.

**Q13. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of sodium hydroxide in 100 cm³ of a 2.0 mol/dm³ solution. Mr of NaOH = 40.
- [✔︎] 8 g — moles = 2.0 × 0.100 = 0.2 mol; mass = 0.2 × 40
- [ ] 80 g — 2.0 × 40, forgetting the volume
    - _why wrong:_ First find the moles: n = c × V = 2.0 × 0.100 = 0.2 mol, then × 40 = 8 g.
- [ ] 0.2 g — stopping at the moles
    - _why wrong:_ 0.2 mol must be multiplied by the Mr (40) to get the mass: 0.2 × 40 = 8 g.
- [ ] 800 g — using 100 cm³ as 100 dm³
    - _why wrong:_ 100 cm³ = 0.100 dm³, so n = 2.0 × 0.100 = 0.2 mol and mass = 8 g.

**Q14. ⭐** _(both Higher tiers (CH·TH))_ — 100 cm³ of a 60 g/dm³ solution is diluted with water to a total volume of 300 cm³. Calculate the new concentration.
- [✔︎] 20 g/dm³ — mass of solute stays 60 × 0.100 = 6 g; new concentration = 6 ÷ 0.300
- [ ] 180 g/dm³ — 60 × 3, multiplying by the dilution factor
    - _why wrong:_ Diluting LOWERS the concentration. Mass is fixed at 6 g; 6 ÷ 0.300 = 20 g/dm³.
- [ ] 60 g/dm³ — dilution does not change concentration
    - _why wrong:_ Adding water triples the volume, so the concentration falls to one third: 20 g/dm³.
- [ ] 6 g/dm³ — using the mass of solute as the concentration
    - _why wrong:_ 6 g is the mass of solute; divide by the new volume 0.300 dm³ to get 20 g/dm³.

**Q15.** _(both Higher tiers (CH·TH))_ — Explain why diluting a solution changes its concentration but not the mass of solute present.
- [✔︎] Adding water increases the volume without adding any solute, so the same mass is spread through more solution and concentration (mass ÷ volume) falls
- [ ] Some solute leaves the solution when water is added
    - _why wrong:_ No solute leaves; the mass stays the same. Only the volume, and therefore the concentration, changes.
- [ ] The added water reacts with the solute and reduces its mass
    - _why wrong:_ Water does not react away the solute here; the mass is unchanged and the concentration simply falls.
- [ ] Both the mass and the concentration double
    - _why wrong:_ The mass is unchanged; adding water lowers the concentration, it does not raise it.

**Q16. ⭐** _(Triple-Foundation extra)_ — 12 g of sugar is dissolved to make 3 dm³ of solution. State the concentration in g/dm³.
- [✔︎] 4 g/dm³ — 12 ÷ 3
- [ ] 36 g/dm³ — 12 × 3
    - _why wrong:_ Concentration is mass ÷ volume: 12 ÷ 3 = 4 g/dm³.
- [ ] 0.25 g/dm³ — 3 ÷ 12
    - _why wrong:_ Divide the mass by the volume, not the volume by the mass: 12 ÷ 3 = 4 g/dm³.
- [ ] 15 g/dm³ — 12 + 3
    - _why wrong:_ Concentration is a division, not an addition: 12 ÷ 3 = 4 g/dm³.

**Q17. ⭐** _(Triple-Foundation extra)_ — A solution has a concentration of 20 g/dm³. State the mass of solute in exactly 1 dm³ of it.
- [✔︎] 20 g — 1 dm³ contains exactly the concentration in grams
- [ ] 1 g — the volume in dm³
    - _why wrong:_ 1 dm³ contains 20 g, because the concentration is 20 g per dm³.
- [ ] 20 g/dm³ — the concentration with units
    - _why wrong:_ The mass is 20 g; g/dm³ is the unit of concentration, not of mass.
- [ ] 10 g — half of the concentration
    - _why wrong:_ 1 dm³ (a full dm³) contains the whole 20 g, not half.

**Q18. ⭐** _(Triple-Higher extra)_ — Calculate the concentration in mol/dm³ of a solution made by dissolving 0.10 mol of solute in 500 cm³ of solution.
- [✔︎] 0.2 mol/dm³ — volume = 0.5 dm³, so 0.10 ÷ 0.5
- [ ] 0.0002 mol/dm³ — 0.10 ÷ 500, without converting
    - _why wrong:_ Convert 500 cm³ to 0.5 dm³ first: 0.10 ÷ 0.5 = 0.2 mol/dm³.
- [ ] 50 mol/dm³ — 0.10 × 500
    - _why wrong:_ Concentration is moles ÷ volume in dm³: 0.10 ÷ 0.5 = 0.2 mol/dm³.
- [ ] 0.10 mol/dm³ — using the moles as the concentration
    - _why wrong:_ Divide the moles by the volume in dm³: 0.10 ÷ 0.5 = 0.2 mol/dm³.

**Q19. ⭐** _(Triple-Higher extra)_ — A potassium hydroxide solution has a concentration of 1.5 mol/dm³. Calculate its concentration in g/dm³. Mr of KOH = 56.
- [✔︎] 84 g/dm³ — concentration (g/dm³) = concentration (mol/dm³) × Mr = 1.5 × 56
- [ ] 0.027 g/dm³ — 1.5 ÷ 56
    - _why wrong:_ Multiply by the Mr to go from mol/dm³ to g/dm³: 1.5 × 56 = 84 g/dm³.
- [ ] 37.3 g/dm³ — 56 ÷ 1.5
    - _why wrong:_ Multiply, do not divide: 1.5 × 56 = 84 g/dm³.
- [ ] 56 g/dm³ — the Mr on its own
    - _why wrong:_ Multiply the Mr by the concentration in mol/dm³: 1.5 × 56 = 84 g/dm³.

**FIFA worked examples — Foundation (in CF & TF)** ⭐

- **Concentration from mass and volume** — 15 g of sodium hydroxide (NaOH) is dissolved to make 500 cm³ of solution. Calculate the concentration in g/dm³.
    - **F** — concentration (g/dm³) = mass (g) ÷ volume (dm³)
    - **I** — volume = 500 ÷ 1000 = 0.5 dm³;  mass = 15 g
    - **F** — concentration = 15 ÷ 0.5
    - **A** — concentration = 30 g/dm³
- **A smaller volume** — 8 g of salt is dissolved to make 250 cm³ of solution. Calculate the concentration in g/dm³.
    - **F** — concentration (g/dm³) = mass (g) ÷ volume (dm³)
    - **I** — volume = 250 ÷ 1000 = 0.25 dm³;  mass = 8 g
    - **F** — concentration = 8 ÷ 0.25
    - **A** — concentration = 32 g/dm³
- **Rearranging for the mass** — Calculate the mass of solute in 2 dm³ of a solution whose concentration is 15 g/dm³.
    - **F** — mass (g) = concentration (g/dm³) × volume (dm³)
    - **I** — = 15 × 2
    - **F** — = 30
    - **A** — mass = 30 g

**FIFA worked examples — Higher (in CH & TH)** ⭐

- **Concentration in mol/dm³** — Calculate the concentration in mol/dm³ of a solution containing 0.25 mol of HCl in 500 cm³ of solution.
    - **F** — concentration (mol/dm³) = moles ÷ volume (dm³)
    - **I** — volume = 500 ÷ 1000 = 0.5 dm³
    - **F** — concentration = 0.25 ÷ 0.5
    - **A** — concentration = 0.5 mol/dm³
- **Converting g/dm³ to mol/dm³** — A sodium hydroxide solution has a concentration of 80 g/dm³. Calculate its concentration in mol/dm³. Mr of NaOH = 40.
    - **F** — concentration (mol/dm³) = concentration (g/dm³) ÷ Mr
    - **I** — = 80 ÷ 40
    - **F** — = 2
    - **A** — concentration = 2 mol/dm³
- **A dilution** — 50 cm³ of a 100 g/dm³ solution is diluted with water to a total volume of 250 cm³. Calculate the new concentration in g/dm³.
    - **F** — the mass of solute is unchanged, so new concentration = mass ÷ new volume
    - **I** — mass = 100 × 0.050 = 5 g;  new volume = 250 ÷ 1000 = 0.25 dm³
    - **F** — concentration = 5 ÷ 0.25
    - **A** — concentration = 20 g/dm³

---

## Moles  ·  `moles`  ·  AQA 5.3.2.1

> **Tier presence:** Higher only — no Foundation cell exists in AQA (CH + TH).
>
> **How the cells are composed** (item numbers below): **CH** → Q1–10; **TH** → Q1–12. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often divide the Mr by the mass instead of the mass by the Mr when finding the number of moles, which turns the answer upside down. The rule is moles = mass ÷ Mr, so for 9.8 g of a substance with Mr 98 the answer is 9.8 ÷ 98 = 0.1 mol, not 10 mol. Also make sure the mass is in GRAMS first — if it is given in kilograms, multiply by 1000 before dividing.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the number of moles in 9.8 g of sulfuric acid (H₂SO₄). Mr = 98.
- [✔︎] 0.1 mol — n = mass ÷ Mr = 9.8 ÷ 98
- [ ] 10 mol — 98 ÷ 9.8, dividing the wrong way
    - _why wrong:_ Moles = mass ÷ Mr, not Mr ÷ mass: 9.8 ÷ 98 = 0.1 mol.
- [ ] 960.4 mol — 9.8 × 98
    - _why wrong:_ Multiplying mass by Mr gives a meaningless number; divide instead: 9.8 ÷ 98 = 0.1 mol.
- [ ] 0.01 mol — 9.8 ÷ 980, using the wrong Mr
    - _why wrong:_ The Mr of H₂SO₄ is 98, not 980: 9.8 ÷ 98 = 0.1 mol.

**Q2. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the number of moles in 80 g of sodium hydroxide (NaOH). Mr = 40.
- [✔︎] 2 mol — n = 80 ÷ 40
- [ ] 0.5 mol — 40 ÷ 80, dividing the wrong way
    - _why wrong:_ Moles = mass ÷ Mr: 80 ÷ 40 = 2 mol, not 0.5.
- [ ] 3200 mol — 80 × 40
    - _why wrong:_ Divide the mass by the Mr, do not multiply: 80 ÷ 40 = 2 mol.
- [ ] 40 mol — using the Mr as the answer
    - _why wrong:_ The Mr is the mass of one mole; here there are 80 ÷ 40 = 2 mol.

**Q3. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of 0.25 mol of calcium carbonate (CaCO₃). Mr = 100.
- [✔︎] 25 g — mass = moles × Mr = 0.25 × 100
- [ ] 0.0025 g — 0.25 ÷ 100
    - _why wrong:_ Mass = moles × Mr, not moles ÷ Mr: 0.25 × 100 = 25 g.
- [ ] 400 g — 100 ÷ 0.25
    - _why wrong:_ Multiply the moles by the Mr: 0.25 × 100 = 25 g.
- [ ] 100 g — the Mr on its own
    - _why wrong:_ 0.25 mol is a quarter of a mole, so 0.25 × 100 = 25 g.

**Q4. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of calcium carbonate (Mr = 100) that contains 3.01 × 10²³ formula units. (Avogadro constant = 6.02 × 10²³ per mol.)
- [✔︎] 50 g — 3.01 × 10²³ ÷ 6.02 × 10²³ = 0.5 mol, so mass = 0.5 × 100
- [ ] 100 g — one mole regardless of the particle count
    - _why wrong:_ 3.01 × 10²³ is HALF of Avogadro's number, so 0.5 mol; mass = 0.5 × 100 = 50 g.
- [ ] 30 100 g — multiplying the particle count by the Mr
    - _why wrong:_ First convert particles to moles (0.5 mol), then × Mr: 0.5 × 100 = 50 g.
- [ ] 0.5 g — confusing moles with grams
    - _why wrong:_ 0.5 is the number of moles; multiply by the Mr (100) to get 50 g.

**Q5. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the number of molecules in 0.5 mol of water. (Avogadro constant = 6.02 × 10²³ per mol.)
- [✔︎] 3.01 × 10²³ — number of particles = moles × Avogadro constant = 0.5 × 6.02 × 10²³
- [ ] 6.02 × 10²³ — one mole's worth, ignoring the 0.5
    - _why wrong:_ 0.5 mol contains half of Avogadro's number: 0.5 × 6.02 × 10²³ = 3.01 × 10²³.
- [ ] 1.204 × 10²⁴ — 2 × 6.02 × 10²³
    - _why wrong:_ Multiply the Avogadro constant by the moles (0.5), not by 2: 3.01 × 10²³.
- [ ] 12.04 × 10²³ — dividing 6.02 × 10²³ by 0.5
    - _why wrong:_ Multiply by the moles: 0.5 × 6.02 × 10²³ = 3.01 × 10²³.

**Q6.** _(both Higher tiers (CH·TH))_ — State what is meant by one mole of a substance.
- [✔︎] The amount of substance that contains 6.02 × 10²³ particles (Avogadro's number)
- [ ] The mass of one molecule of the substance
    - _why wrong:_ A mole is an AMOUNT (a fixed number of particles), not the mass of one molecule.
- [ ] Exactly one gram of the substance
    - _why wrong:_ A mole is not one gram; its mass in grams equals the Mr, which varies with the substance.
- [ ] The volume occupied by a gas at room temperature
    - _why wrong:_ That is molar gas volume; a mole is defined by the number of particles, 6.02 × 10²³.

**Q7.** _(both Higher tiers (CH·TH))_ — State the value of the Avogadro constant.
- [✔︎] 6.02 × 10²³ particles per mole
- [ ] 6.02 × 10²³ grams per mole
    - _why wrong:_ The Avogadro constant counts particles, not grams: 6.02 × 10²³ particles per mole.
- [ ] 1000 particles per mole
    - _why wrong:_ One mole contains far more: 6.02 × 10²³ particles.
- [ ] 6.02 × 10²³ moles per particle
    - _why wrong:_ It is the number of particles PER mole: 6.02 × 10²³ particles per mole.

**Q8. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the number of moles in 0.024 kg of magnesium. Ar = 24.
- [✔︎] 1 mol — convert to grams (0.024 kg = 24 g), then n = 24 ÷ 24
- [ ] 0.001 mol — 0.024 ÷ 24, without converting kg to g
    - _why wrong:_ Convert the mass to grams first: 0.024 kg = 24 g, so n = 24 ÷ 24 = 1 mol.
- [ ] 1000 mol — 24 000 ÷ 24, using grams as milligrams
    - _why wrong:_ 0.024 kg is 24 g, not 24 000 g: n = 24 ÷ 24 = 1 mol.
- [ ] 576 mol — 24 × 24
    - _why wrong:_ Divide the mass in grams by the Ar: 24 ÷ 24 = 1 mol.

**Q9. ⭐** _(both Higher tiers (CH·TH))_ — A sample contains 0.2 mol of a compound and has a mass of 8 g. Calculate the relative formula mass (Mr) of the compound.
- [✔︎] 40 — Mr = mass ÷ moles = 8 ÷ 0.2
- [ ] 1.6 — 8 × 0.2
    - _why wrong:_ Rearranging moles = mass ÷ Mr gives Mr = mass ÷ moles = 8 ÷ 0.2 = 40.
- [ ] 0.025 — 0.2 ÷ 8, dividing the wrong way
    - _why wrong:_ Mr = mass ÷ moles = 8 ÷ 0.2 = 40, not 0.025.
- [ ] 8 — using the mass as the Mr
    - _why wrong:_ The mass is 8 g for 0.2 mol; one mole would be 8 ÷ 0.2 = 40 g, so Mr = 40.

**Q10. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the percentage by mass of calcium in calcium carbonate (CaCO₃). Ar: Ca = 40, C = 12, O = 16.
- [✔︎] 40% — (Ar of Ca ÷ Mr) × 100 = (40 ÷ 100) × 100
- [ ] 12% — using the carbon instead of the calcium
    - _why wrong:_ The question asks for calcium: (40 ÷ 100) × 100 = 40%.
- [ ] 2.5% — (1 ÷ 40) × 100, using one atom over the Ar
    - _why wrong:_ Use (Ar of the element ÷ Mr of the compound) × 100: (40 ÷ 100) × 100 = 40%.
- [ ] 40% of 100 g = 4 g, so 4%
    - _why wrong:_ The percentage IS 40%; do not take a percentage of a percentage.

**Q11. ⭐** _(Triple-Higher extra)_ — Ammonium nitrate (NH₄NO₃) is used as a fertiliser because it is rich in nitrogen. Calculate the percentage by mass of nitrogen in ammonium nitrate. Ar: N = 14, H = 1, O = 16.
- [✔︎] 35% — Mr = 80, nitrogen = 2 × 14 = 28, so (28 ÷ 80) × 100
- [ ] 17.5% — using only one nitrogen atom
    - _why wrong:_ NH₄NO₃ contains TWO nitrogen atoms: 2 × 14 = 28, so (28 ÷ 80) × 100 = 35%.
- [ ] 28% — using the mass of nitrogen as the percentage
    - _why wrong:_ 28 is the mass of nitrogen; divide by the Mr (80) and × 100: 35%.
- [ ] 14% — using one nitrogen over 100
    - _why wrong:_ Use both nitrogens (28) over the correct Mr (80): (28 ÷ 80) × 100 = 35%.

**Q12. ⭐** _(Triple-Higher extra)_ — Calculate the total number of atoms in 0.1 mol of water (H₂O). (Avogadro constant = 6.02 × 10²³ per mol.)
- [✔︎] 1.806 × 10²³ — 0.1 mol has 0.1 × 6.02 × 10²³ = 6.02 × 10²² molecules, each with 3 atoms
- [ ] 6.02 × 10²² — the number of molecules, not atoms
    - _why wrong:_ Each water molecule has 3 atoms (2 H + 1 O), so multiply the molecules by 3: 1.806 × 10²³.
- [ ] 6.02 × 10²³ — one mole's worth of particles
    - _why wrong:_ 0.1 mol is a tenth: 0.1 × 6.02 × 10²³ = 6.02 × 10²² molecules, then × 3 atoms = 1.806 × 10²³.
- [ ] 2 × 6.02 × 10²² — counting only the hydrogen atoms
    - _why wrong:_ Count all 3 atoms per molecule (2 H + 1 O): 3 × 6.02 × 10²² = 1.806 × 10²³.

**FIFA worked examples (in CH & TH)** ⭐

- **Moles from a mass** — Calculate the number of moles in 27 g of aluminium (Ar = 27).
    - **F** — moles = mass ÷ Mr
    - **I** — moles = 27 ÷ 27
    - **F** — = 1
    - **A** — 1 mol of aluminium
- **Mass from a number of moles** — Calculate the mass of 0.5 mol of carbon dioxide (CO₂). Mr = 44.
    - **F** — mass = moles × Mr
    - **I** — mass = 0.5 × 44
    - **F** — = 22
    - **A** — 22 g of carbon dioxide
- **Number of particles** — Calculate the number of molecules in 2 mol of water. (Avogadro constant = 6.02 × 10²³ per mol.)
    - **F** — number of particles = moles × Avogadro constant
    - **I** — = 2 × 6.02 × 10²³
    - **F** — = 12.04 × 10²³
    - **A** — = 1.204 × 10²⁴ molecules

---

## Amounts of Substances in Equations  ·  `amounts-in-equations`  ·  AQA 5.3.2.2

> **Tier presence:** Higher only — no Foundation cell exists in AQA (CH + TH).
>
> **How the cells are composed** (item numbers below): **CH** → Q1–10; **TH** → Q1–12. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often assume the moles of one substance equal the moles of another, forgetting to use the ratio from the balanced equation — writing that 0.4 mol of A makes 0.4 mol of B when the equation says 2A → B. In fact you must scale by the coefficients: 2 mol of A makes 1 mol of B, so 0.4 mol of A makes only 0.2 mol of B. Always read the ratio off the big numbers in the balanced equation before you convert.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(both Higher tiers (CH·TH))_ — N₂ + 3H₂ → 2NH₃. Calculate the number of moles of ammonia produced from 0.6 mol of hydrogen.
- [✔︎] 0.4 mol — ratio H₂:NH₃ = 3:2, so 0.6 × (2 ÷ 3)
- [ ] 0.6 mol — the same number of moles as the hydrogen
    - _why wrong:_ The ratio H₂:NH₃ is 3:2, not 1:1, so 0.6 × (2/3) = 0.4 mol.
- [ ] 0.9 mol — 0.6 × (3 ÷ 2), inverting the ratio
    - _why wrong:_ The ratio must be applied as NH₃ = H₂ × (2/3): 0.6 × (2/3) = 0.4 mol.
- [ ] 1.2 mol — doubling the hydrogen
    - _why wrong:_ Doubling would need a 1:2 ratio; here H₂:NH₃ = 3:2, giving 0.4 mol.

**Q2. ⭐** _(both Higher tiers (CH·TH))_ — 2Mg + O₂ → 2MgO. Calculate the number of moles of magnesium oxide formed from 0.3 mol of magnesium.
- [✔︎] 0.3 mol — ratio Mg:MgO = 2:2 = 1:1
- [ ] 0.6 mol — doubling the magnesium
    - _why wrong:_ The ratio Mg:MgO is 1:1, so 0.3 mol of Mg gives 0.3 mol of MgO.
- [ ] 0.15 mol — halving the magnesium
    - _why wrong:_ The ratio is 1:1 (2:2), not 2:1, so 0.3 mol of Mg gives 0.3 mol of MgO.
- [ ] 0.3 mol of O₂ instead
    - _why wrong:_ The question asks for MgO; the ratio Mg:MgO = 1:1 gives 0.3 mol of MgO.

**Q3. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of magnesium oxide formed when 4.8 g of magnesium reacts completely with oxygen. 2Mg + O₂ → 2MgO. Ar: Mg = 24, O = 16.
- [✔︎] 8 g — n(Mg) = 4.8 ÷ 24 = 0.2 mol; ratio 1:1; mass = 0.2 × 40
- [ ] 4.8 g — the oxide has the same mass as the metal
    - _why wrong:_ Oxygen is added, so the oxide is heavier: 0.2 mol × 40 = 8 g.
- [ ] 192 g — 4.8 × 40, skipping the moles
    - _why wrong:_ Convert to moles first: n = 4.8 ÷ 24 = 0.2 mol, then × Mr(MgO) = 40 → 8 g.
- [ ] 0.2 g — stopping at the moles
    - _why wrong:_ 0.2 mol must be multiplied by Mr(MgO) = 40 to give the mass: 8 g.

**Q4. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of carbon dioxide produced when 10 g of calcium carbonate decomposes completely. CaCO₃ → CaO + CO₂. Mr: CaCO₃ = 100, CO₂ = 44.
- [✔︎] 4.4 g — n(CaCO₃) = 10 ÷ 100 = 0.1 mol; ratio 1:1; mass = 0.1 × 44
- [ ] 10 g — the CO₂ equals the mass of the carbonate
    - _why wrong:_ Only part of the carbonate becomes CO₂: 0.1 mol × 44 = 4.4 g.
- [ ] 440 g — 10 × 44, skipping the moles
    - _why wrong:_ Convert to moles first: 10 ÷ 100 = 0.1 mol, then × 44 = 4.4 g.
- [ ] 5.6 g — the mass of CaO left behind
    - _why wrong:_ That is the residue; the CO₂ is 0.1 × 44 = 4.4 g.

**Q5. ⭐** _(both Higher tiers (CH·TH))_ — H₂ + Cl₂ → 2HCl. Calculate the mass of hydrogen chloride formed from 0.2 mol of hydrogen. Mr of HCl = 36.5.
- [✔︎] 14.6 g — ratio H₂:HCl = 1:2 so n(HCl) = 0.4 mol; mass = 0.4 × 36.5
- [ ] 7.3 g — using a 1:1 ratio
    - _why wrong:_ The ratio H₂:HCl is 1:2, so n(HCl) = 0.4 mol, giving 0.4 × 36.5 = 14.6 g.
- [ ] 0.4 g — stopping at the moles of HCl
    - _why wrong:_ 0.4 mol must be multiplied by Mr(HCl) = 36.5: 14.6 g.
- [ ] 73 g — using 0.2 mol × 36.5 × ..., misplacing a factor
    - _why wrong:_ n(HCl) = 2 × 0.2 = 0.4 mol; 0.4 × 36.5 = 14.6 g.

**Q6.** _(both Higher tiers (CH·TH))_ — State what the large numbers (coefficients) in a balanced equation tell you about the amounts reacting.
- [✔︎] They give the ratio of the number of moles of each substance that react and form
- [ ] They give the masses of each substance in grams
    - _why wrong:_ Coefficients give the mole RATIO, not the masses; convert to mass using Mr.
- [ ] They give the number of atoms in each formula
    - _why wrong:_ The subscripts give atoms per formula; the coefficients give the mole ratio.
- [ ] They give the percentage yield of the reaction
    - _why wrong:_ Coefficients set the mole ratio; percentage yield comes from an experiment.

**Q7. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of magnesium needed to make 8.0 g of magnesium oxide. 2Mg + O₂ → 2MgO. Ar: Mg = 24, O = 16.
- [✔︎] 4.8 g — n(MgO) = 8.0 ÷ 40 = 0.2 mol; ratio 1:1; mass = 0.2 × 24
- [ ] 8.0 g — the metal equals the mass of the oxide
    - _why wrong:_ The oxide is heavier than the metal: n(MgO) = 0.2 mol, so mass(Mg) = 0.2 × 24 = 4.8 g.
- [ ] 192 g — 8.0 × 24, skipping the moles
    - _why wrong:_ Convert to moles first: 8.0 ÷ 40 = 0.2 mol, then × 24 = 4.8 g.
- [ ] 0.2 g — stopping at the moles
    - _why wrong:_ 0.2 mol × Ar(Mg) = 0.2 × 24 = 4.8 g.

**Q8. ⭐** _(both Higher tiers (CH·TH))_ — N₂ + 3H₂ → 2NH₃. Calculate the number of moles of hydrogen needed to react completely with 2 mol of nitrogen.
- [✔︎] 6 mol — ratio N₂:H₂ = 1:3, so 2 × 3
- [ ] 2 mol — the same as the nitrogen
    - _why wrong:_ The ratio N₂:H₂ is 1:3, so 2 mol of N₂ needs 6 mol of H₂.
- [ ] 0.67 mol — 2 ÷ 3, inverting the ratio
    - _why wrong:_ Multiply by the ratio: 2 × 3 = 6 mol of H₂.
- [ ] 5 mol — adding the coefficients
    - _why wrong:_ Use the 1:3 ratio: 2 × 3 = 6 mol of H₂.

**Q9. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the mass of water formed when 2 g of hydrogen burns completely in oxygen. 2H₂ + O₂ → 2H₂O. Ar: H = 1, O = 16.
- [✔︎] 18 g — n(H₂) = 2 ÷ 2 = 1 mol; ratio H₂:H₂O = 1:1; mass = 1 × 18
- [ ] 2 g — the water equals the mass of the hydrogen
    - _why wrong:_ Oxygen is added, so the water is heavier: 1 mol × 18 = 18 g.
- [ ] 36 g — using a 1:2 ratio
    - _why wrong:_ The ratio H₂:H₂O is 1:1 (2:2), so n(H₂O) = 1 mol and mass = 18 g.
- [ ] 9 g — using Mr(H₂O) = 9
    - _why wrong:_ The Mr of water is 18, not 9: 1 × 18 = 18 g.

**Q10. ⭐** _(both Higher tiers (CH·TH))_ — Deduce the mass of oxygen required to react completely with 6 g of carbon. C + O₂ → CO₂. Ar: C = 12, O = 16.
- [✔︎] 16 g — n(C) = 6 ÷ 12 = 0.5 mol; ratio C:O₂ = 1:1; mass = 0.5 × 32
- [ ] 6 g — the oxygen equals the mass of the carbon
    - _why wrong:_ Their masses differ: n(O₂) = 0.5 mol, so mass = 0.5 × 32 = 16 g.
- [ ] 8 g — using Mr(O₂) = 16
    - _why wrong:_ Oxygen gas is O₂ with Mr = 32, not 16: 0.5 × 32 = 16 g.
- [ ] 0.5 g — stopping at the moles
    - _why wrong:_ 0.5 mol × Mr(O₂) = 0.5 × 32 = 16 g.

**Q11. ⭐** _(Triple-Higher extra)_ — Calculate the mass of aluminium oxide formed when 5.4 g of aluminium reacts completely with oxygen. 4Al + 3O₂ → 2Al₂O₃. Ar: Al = 27, O = 16.
- [✔︎] 10.2 g — n(Al) = 5.4 ÷ 27 = 0.2 mol; ratio Al:Al₂O₃ = 4:2 so n(Al₂O₃) = 0.1 mol; mass = 0.1 × 102
- [ ] 20.4 g — using a 1:1 ratio for Al:Al₂O₃
    - _why wrong:_ The ratio is 4:2 = 2:1, so n(Al₂O₃) = 0.2 ÷ 2 = 0.1 mol, giving 10.2 g.
- [ ] 0.1 g — stopping at the moles of Al₂O₃
    - _why wrong:_ 0.1 mol × Mr(Al₂O₃) = 0.1 × 102 = 10.2 g.
- [ ] 5.4 g — the oxide equals the mass of the metal
    - _why wrong:_ Oxygen is added, and the ratio is 2:1: 0.1 × 102 = 10.2 g.

**Q12. ⭐** _(Triple-Higher extra)_ — Calculate the mass of iron produced when 16 g of iron(III) oxide is reduced completely. Fe₂O₃ + 3CO → 2Fe + 3CO₂. Mr: Fe₂O₃ = 160, Ar Fe = 56.
- [✔︎] 11.2 g — n(Fe₂O₃) = 16 ÷ 160 = 0.1 mol; ratio Fe₂O₃:Fe = 1:2 so n(Fe) = 0.2 mol; mass = 0.2 × 56
- [ ] 5.6 g — using a 1:1 ratio
    - _why wrong:_ Each Fe₂O₃ gives 2 Fe, so n(Fe) = 0.2 mol, giving 0.2 × 56 = 11.2 g.
- [ ] 0.2 g — stopping at the moles of iron
    - _why wrong:_ 0.2 mol × Ar(Fe) = 0.2 × 56 = 11.2 g.
- [ ] 16 g — the iron equals the mass of the oxide
    - _why wrong:_ Oxygen is removed, so the iron is lighter: 0.2 × 56 = 11.2 g.

**FIFA worked examples (in CH & TH)** ⭐

- **Mass of a product with a 1:1 ratio** — Calculate the mass of hydrogen produced when 1.2 g of magnesium reacts with excess hydrochloric acid. Mg + 2HCl → MgCl₂ + H₂. Ar: Mg = 24, H = 1.
    - **F** — mass → moles (÷ Mr); use the equation ratio; mass = moles × Mr
    - **I** — n(Mg) = 1.2 ÷ 24 = 0.05 mol;  ratio Mg:H₂ = 1:1 so n(H₂) = 0.05 mol;  Mr(H₂) = 2
    - **F** — mass(H₂) = 0.05 × 2
    - **A** — 0.1 g of hydrogen
- **A larger mass** — Calculate the mass of carbon dioxide made when 24 g of carbon burns completely. C + O₂ → CO₂. Ar: C = 12, O = 16.
    - **F** — mass → moles (÷ Mr); use the ratio; mass = moles × Mr
    - **I** — n(C) = 24 ÷ 12 = 2 mol;  ratio C:CO₂ = 1:1 so n(CO₂) = 2 mol;  Mr(CO₂) = 44
    - **F** — mass(CO₂) = 2 × 44
    - **A** — 88 g of carbon dioxide
- **Using a non-1:1 ratio** — Calculate the mass of ammonia (NH₃) formed when 0.5 mol of nitrogen reacts completely with hydrogen. N₂ + 3H₂ → 2NH₃. Mr of NH₃ = 17.
    - **F** — use the equation ratio, then mass = moles × Mr
    - **I** — ratio N₂:NH₃ = 1:2 so n(NH₃) = 0.5 × 2 = 1 mol;  Mr(NH₃) = 17
    - **F** — mass(NH₃) = 1 × 17
    - **A** — 17 g of ammonia

---

## Using Moles — Calculations and Limiting Reactants  ·  `using-moles-calculations`  ·  AQA 5.3.2.3–5.3.2.4

> **Tier presence:** Higher only — no Foundation cell exists in AQA (CH + TH).
>
> **How the cells are composed** (item numbers below): **CH** → Q1–10; **TH** → Q1–12. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often pick the limiting reactant simply as the one with the smaller number of moles, ignoring the equation's ratio. That can be wrong: a reactant present in fewer moles may still be in excess if the equation needs less of it. Compare the moles you HAVE with the moles the balanced equation NEEDS — the reactant that runs out first, relative to the ratio, is the limiting one.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the concentration in mol/dm³ of a solution made by dissolving 0.3 mol of KOH in 300 cm³ of solution.
- [✔︎] 1 mol/dm³ — volume = 0.3 dm³, so c = 0.3 ÷ 0.3
- [ ] 0.001 mol/dm³ — 0.3 ÷ 300, without converting
    - _why wrong:_ Convert 300 cm³ to 0.3 dm³ first: 0.3 ÷ 0.3 = 1 mol/dm³.
- [ ] 90 mol/dm³ — 0.3 × 300
    - _why wrong:_ Concentration is moles ÷ volume in dm³, not moles × volume: 0.3 ÷ 0.3 = 1 mol/dm³.
- [ ] 0.3 mol/dm³ — using the moles as the concentration
    - _why wrong:_ Divide the moles by the volume in dm³: 0.3 ÷ 0.3 = 1 mol/dm³.

**Q2. ⭐** _(both Higher tiers (CH·TH))_ — 0.1 mol of sodium is mixed with 0.05 mol of chlorine. 2Na + Cl₂ → 2NaCl. Deduce the limiting reactant.
- [✔︎] Neither — 0.1 mol Na needs exactly 0.05 mol Cl₂ (a 2:1 ratio), so both run out together
- [ ] Sodium, because there is more chlorine in molar terms
    - _why wrong:_ The 2:1 ratio means 0.1 mol Na needs exactly 0.05 mol Cl₂ — both are used up exactly.
- [ ] Chlorine, because 0.05 mol is fewer than 0.1 mol
    - _why wrong:_ Raw moles cannot be compared directly; against the 2:1 ratio, 0.05 mol Cl₂ is exactly right.
- [ ] Cannot be decided without the masses
    - _why wrong:_ Moles and the equation ratio are enough: 0.1 mol Na : 0.05 mol Cl₂ is exactly 2:1.

**Q3.** _(both Higher tiers (CH·TH))_ — Mg + 2HCl → MgCl₂ + H₂. 0.1 mol of magnesium is added to 0.15 mol of hydrochloric acid. Identify the limiting reactant.
- [✔︎] Hydrochloric acid — 0.1 mol Mg needs 0.2 mol HCl, but only 0.15 mol is present
- [ ] Magnesium, because it is a solid
    - _why wrong:_ State does not decide it: 0.1 mol Mg needs 0.2 mol HCl and only 0.15 is present, so HCl limits.
- [ ] Neither, because 0.1 and 0.15 are close
    - _why wrong:_ The ratio is 1:2, so 0.1 mol Mg needs 0.2 mol HCl; only 0.15 mol is present, so HCl limits.
- [ ] Magnesium, because there is less of it
    - _why wrong:_ There are fewer moles of Mg, but it needs 0.2 mol HCl, more than the 0.15 available — HCl limits.

**Q4. ⭐** _(both Higher tiers (CH·TH))_ — A compound contains 2.4 g of carbon and 0.8 g of hydrogen. Determine its empirical formula. Ar: C = 12, H = 1.
- [✔︎] CH₄ — n(C) = 0.2 mol, n(H) = 0.8 mol, ratio 0.2:0.8 = 1:4
- [ ] CH — using the masses directly as the ratio
    - _why wrong:_ Convert masses to moles first: C = 2.4÷12 = 0.2, H = 0.8÷1 = 0.8, ratio 1:4 → CH₄.
- [ ] C₄H — inverting the ratio
    - _why wrong:_ The moles are C 0.2 : H 0.8, i.e. 1 C to 4 H → CH₄, not C₄H.
- [ ] C₃H — using 2.4 and 0.8 without dividing by Ar
    - _why wrong:_ Divide each mass by its Ar first: 0.2 : 0.8 = 1:4 → CH₄.

**Q5. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the number of moles of HCl in 250 cm³ of a 0.20 mol/dm³ solution.
- [✔︎] 0.05 mol — n = c × V = 0.20 × 0.25
- [ ] 50 mol — 0.20 × 250, without converting to dm³
    - _why wrong:_ Convert 250 cm³ to 0.25 dm³ first: 0.20 × 0.25 = 0.05 mol.
- [ ] 0.8 mol — 0.20 ÷ 0.25, dividing instead of multiplying
    - _why wrong:_ Moles = concentration × volume: 0.20 × 0.25 = 0.05 mol.
- [ ] 0.20 mol — using the concentration as the moles
    - _why wrong:_ Multiply the concentration by the volume in dm³: 0.20 × 0.25 = 0.05 mol.

**Q6.** _(both Higher tiers (CH·TH))_ — State how you identify the limiting reactant in a reaction.
- [✔︎] Convert each reactant to moles, compare with the equation's mole ratio, and find the one that runs out first
- [ ] The reactant with the smallest mass is always limiting
    - _why wrong:_ Mass alone does not decide it; you must compare moles against the equation ratio.
- [ ] The reactant with the smallest number of moles is always limiting
    - _why wrong:_ Only after comparing with the ratio; a reactant in fewer moles can still be in excess.
- [ ] The reactant that is a gas is always limiting
    - _why wrong:_ State is irrelevant; compare moles with the balanced equation's ratio.

**Q7. ⭐** _(both Higher tiers (CH·TH))_ — A compound is 40% calcium, 12% carbon and 48% oxygen by mass. Determine its empirical formula. Ar: Ca = 40, C = 12, O = 16.
- [✔︎] CaCO₃ — in 100 g: Ca 40÷40 = 1, C 12÷12 = 1, O 48÷16 = 3, ratio 1:1:3
- [ ] CaCO — dropping the oxygen ratio
    - _why wrong:_ The oxygen gives 48÷16 = 3, so the ratio is 1:1:3 → CaCO₃.
- [ ] Ca₄C₁₂O₄₈ — using the percentages as the atom counts
    - _why wrong:_ Divide each percentage by the Ar first: 1:1:3 → CaCO₃.
- [ ] CaC₃O — mixing up the carbon and oxygen
    - _why wrong:_ Carbon is 1 (12÷12) and oxygen is 3 (48÷16): CaCO₃.

**Q8. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the volume, in cm³, of 2.0 mol/dm³ hydrochloric acid that contains 0.10 mol of HCl.
- [✔︎] 50 cm³ — V = n ÷ c = 0.10 ÷ 2.0 = 0.05 dm³
- [ ] 0.2 cm³ — 0.10 × 2.0, multiplying instead of dividing
    - _why wrong:_ Volume = moles ÷ concentration = 0.10 ÷ 2.0 = 0.05 dm³ = 50 cm³.
- [ ] 20 cm³ — 2.0 ÷ 0.10, dividing the wrong way
    - _why wrong:_ Divide the moles by the concentration: 0.10 ÷ 2.0 = 0.05 dm³ = 50 cm³.
- [ ] 0.05 cm³ — forgetting to convert dm³ to cm³
    - _why wrong:_ 0.05 dm³ × 1000 = 50 cm³.

**Q9. ⭐** _(both Higher tiers (CH·TH))_ — 2H₂ + O₂ → 2H₂O. 0.4 mol of hydrogen reacts with 0.3 mol of oxygen. Deduce which reactant is in excess.
- [✔︎] Oxygen — 0.4 mol H₂ needs only 0.2 mol O₂, but 0.3 mol is present, so oxygen is in excess
- [ ] Hydrogen, because there is more of it
    - _why wrong:_ Hydrogen is the limiting reactant: it needs 0.2 mol O₂ and 0.3 mol is available, so oxygen is in excess.
- [ ] Neither, because 0.4 and 0.3 are close
    - _why wrong:_ Against the 2:1 ratio, 0.4 mol H₂ needs 0.2 mol O₂; the extra 0.1 mol O₂ is in excess.
- [ ] Oxygen is limiting, because 0.3 is fewer than 0.4
    - _why wrong:_ Raw moles do not decide it: 0.4 mol H₂ needs only 0.2 mol O₂, so oxygen is in excess.

**Q10. ⭐** _(both Higher tiers (CH·TH))_ — Calculate the concentration in mol/dm³ of a solution containing 0.05 mol of NaOH in 200 cm³ of solution.
- [✔︎] 0.25 mol/dm³ — volume = 0.2 dm³, so 0.05 ÷ 0.2
- [ ] 0.00025 mol/dm³ — 0.05 ÷ 200, without converting
    - _why wrong:_ Convert 200 cm³ to 0.2 dm³ first: 0.05 ÷ 0.2 = 0.25 mol/dm³.
- [ ] 10 mol/dm³ — 0.05 × 200
    - _why wrong:_ Concentration is moles ÷ volume in dm³: 0.05 ÷ 0.2 = 0.25 mol/dm³.
- [ ] 0.05 mol/dm³ — using the moles as the concentration
    - _why wrong:_ Divide the moles by the volume in dm³: 0.05 ÷ 0.2 = 0.25 mol/dm³.

**Q11. ⭐** _(Triple-Higher extra)_ — A compound has the empirical formula CH₂ and a relative formula mass of 42. Determine its molecular formula. Ar: C = 12, H = 1.
- [✔︎] C₃H₆ — empirical mass of CH₂ = 14; 42 ÷ 14 = 3, so multiply the formula by 3
- [ ] CH₂ — assuming the molecular formula equals the empirical formula
    - _why wrong:_ The Mr (42) is 3 times the empirical mass (14), so the molecular formula is C₃H₆.
- [ ] C₂H₄ — using a factor of 2
    - _why wrong:_ 42 ÷ 14 = 3, not 2, so the formula is (CH₂)₃ = C₃H₆.
- [ ] C₄₂H₈₄ — multiplying by the Mr itself
    - _why wrong:_ Divide the Mr by the empirical mass first: 42 ÷ 14 = 3 → C₃H₆.

**Q12. ⭐** _(Triple-Higher extra)_ — 3.0 g of magnesium is added to 100 cm³ of 2.0 mol/dm³ hydrochloric acid. Mg + 2HCl → MgCl₂ + H₂. Deduce the limiting reactant. Ar: Mg = 24.
- [✔︎] Hydrochloric acid — n(Mg) = 0.125 mol needs 0.25 mol HCl, but only n(HCl) = 2.0 × 0.1 = 0.2 mol is present
- [ ] Magnesium, because 0.125 mol is a small amount
    - _why wrong:_ 0.125 mol Mg would need 0.25 mol HCl; only 0.2 mol HCl is present, so HCl is limiting.
- [ ] Neither, because both are 0.2 mol
    - _why wrong:_ n(Mg) = 3.0 ÷ 24 = 0.125 mol, not 0.2 mol; the HCl (0.2 mol) runs out first.
- [ ] Magnesium, because it is the solid reactant
    - _why wrong:_ State is irrelevant; comparing moles with the 1:2 ratio shows HCl is limiting.

**FIFA worked examples (in CH & TH)** ⭐

- **Limiting reactant and product mass** — 2.4 g of magnesium reacts with 3.65 g of hydrochloric acid. Mg + 2HCl → MgCl₂ + H₂. Identify the limiting reactant and calculate the mass of hydrogen produced. Ar: Mg = 24, H = 1, Cl = 35.5.
    - **F** — convert each reactant to moles; compare with the equation ratio; the one that runs out is limiting
    - **I** — n(Mg) = 2.4 ÷ 24 = 0.1 mol;  n(HCl) = 3.65 ÷ 36.5 = 0.1 mol;  0.1 mol Mg needs 0.2 mol HCl but only 0.1 mol is present
    - **F** — HCl limits;  n(H₂) = 0.1 ÷ 2 = 0.05 mol;  mass = 0.05 × 2
    - **A** — HCl is limiting;  0.1 g of hydrogen
- **Empirical formula from masses** — A compound contains 2.4 g of carbon and 0.8 g of hydrogen. Determine its empirical formula. Ar: C = 12, H = 1.
    - **F** — moles of each = mass ÷ Ar; then find the simplest whole-number ratio
    - **I** — n(C) = 2.4 ÷ 12 = 0.2 mol;  n(H) = 0.8 ÷ 1 = 0.8 mol
    - **F** — ratio C:H = 0.2 : 0.8 = 1 : 4
    - **A** — empirical formula = CH₄
- **Concentration in mol/dm³** — Calculate the concentration in mol/dm³ of a solution made by dissolving 0.3 mol of KOH in 300 cm³ of solution.
    - **F** — concentration (mol/dm³) = moles ÷ volume (dm³)
    - **I** — volume = 300 ÷ 1000 = 0.3 dm³
    - **F** — concentration = 0.3 ÷ 0.3
    - **A** — 1 mol/dm³

---

## Percentage Yield  ·  `percentage-yield`  ·  AQA 4.3.3.1 (Triple only)

> **Tier presence:** Triple only — no Combined cell exists in AQA (TF + TH).
>
> **How the cells are composed** (item numbers below): **TF** → Q1–12; **TH** → Q1–6, 13–18. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often divide the theoretical yield by the actual yield, getting a percentage bigger than 100% and not noticing anything is wrong. Percentage yield can never be more than 100%, because you cannot collect more product than the balanced equation predicts. Always divide the ACTUAL yield by the THEORETICAL yield, then multiply by 100.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(both Triple tiers (TF·TH))_ — A reaction has a theoretical yield of 20 g, but only 14 g of product is obtained. Calculate the percentage yield.
- [✔︎] 70% — (actual ÷ theoretical) × 100 = (14 ÷ 20) × 100
- [ ] 143% — (20 ÷ 14) × 100, dividing the wrong way
    - _why wrong:_ Percentage yield cannot exceed 100%. Divide actual by theoretical: (14 ÷ 20) × 100 = 70%.
- [ ] 30% — 100% minus 70%, giving the loss
    - _why wrong:_ 30% is the percentage LOST; the yield is (14 ÷ 20) × 100 = 70%.
- [ ] 14% — using the actual yield in grams as the percentage
    - _why wrong:_ 14 g is a mass, not a percentage; divide by the theoretical yield: 70%.

**Q2.** _(both Triple tiers (TF·TH))_ — Explain why the actual yield of a reaction is almost always less than the theoretical yield.
- [✔︎] Some product is lost in practice (on glassware, in filtering or transferring), reactions may be reversible or incomplete, and side reactions can make other products
- [ ] The law of conservation of mass means mass is lost in every reaction
    - _why wrong:_ Mass is conserved; the desired product is just less than the maximum because of losses and side reactions.
- [ ] Theoretical yields are always calculated too high by rounding
    - _why wrong:_ Theoretical yield comes from exact stoichiometry, not rounding; the shortfall is from real losses.
- [ ] All of the product decomposes back into the reactants
    - _why wrong:_ Not all product reverts; the shortfall is from practical losses, incomplete or side reactions.

**Q3. ⭐** _(both Triple tiers (TF·TH))_ — A reaction has a theoretical yield of 50 g and an actual yield of 40 g. Calculate the percentage yield.
- [✔︎] 80% — (40 ÷ 50) × 100
- [ ] 125% — (50 ÷ 40) × 100, dividing the wrong way
    - _why wrong:_ Yield cannot exceed 100%: (40 ÷ 50) × 100 = 80%.
- [ ] 20% — 100% minus 80%, giving the loss
    - _why wrong:_ 20% is the loss; the yield is (40 ÷ 50) × 100 = 80%.
- [ ] 40% — using the actual yield in grams
    - _why wrong:_ 40 g is a mass; divide by the theoretical yield: (40 ÷ 50) × 100 = 80%.

**Q4.** _(both Triple tiers (TF·TH))_ — State what is meant by the theoretical yield of a reaction.
- [✔︎] The maximum mass of product that the balanced equation predicts, assuming the reaction is complete with no losses
- [ ] The mass of product actually collected in the experiment
    - _why wrong:_ That is the ACTUAL yield; the theoretical yield is the maximum predicted by the equation.
- [ ] The mass of the limiting reactant used
    - _why wrong:_ The theoretical yield is the product mass predicted, not the mass of a reactant.
- [ ] The percentage of reactant converted to product
    - _why wrong:_ That is closer to percentage yield; theoretical yield is a maximum product mass.

**Q5. ⭐** _(both Triple tiers (TF·TH))_ — A student obtains 18 g of product from a reaction whose theoretical yield is 24 g. Calculate the percentage yield.
- [✔︎] 75% — (18 ÷ 24) × 100
- [ ] 133% — (24 ÷ 18) × 100, dividing the wrong way
    - _why wrong:_ Yield cannot exceed 100%: (18 ÷ 24) × 100 = 75%.
- [ ] 25% — 100% minus 75%, giving the loss
    - _why wrong:_ 25% is the loss; the yield is (18 ÷ 24) × 100 = 75%.
- [ ] 6% — using the 6 g difference
    - _why wrong:_ The 6 g shortfall is not the yield; (18 ÷ 24) × 100 = 75%.

**Q6.** _(both Triple tiers (TF·TH))_ — Explain why a high percentage yield is desirable in an industrial process.
- [✔︎] More of the reactants are turned into useful product, so less is wasted and the raw materials are used more efficiently and cheaply
- [ ] A high yield always means the reaction is faster
    - _why wrong:_ Yield is about how much product is made, not the rate; a fast reaction can still have a low yield.
- [ ] A high yield means the product is always purer
    - _why wrong:_ Yield measures quantity, not purity; a high yield does not guarantee a pure product.
- [ ] A high yield reduces the atom economy of the process
    - _why wrong:_ Yield and atom economy are separate measures; a high yield does not lower atom economy.

**Q7. ⭐** _(Triple-Foundation extra)_ — State the equation used to calculate the percentage yield of a reaction.
- [✔︎] Percentage yield = (actual yield ÷ theoretical yield) × 100
- [ ] Percentage yield = (theoretical yield ÷ actual yield) × 100
    - _why wrong:_ This is upside down and gives values over 100%; use actual ÷ theoretical.
- [ ] Percentage yield = (actual yield − theoretical yield) × 100
    - _why wrong:_ Percentage yield is a ratio, not a difference: (actual ÷ theoretical) × 100.
- [ ] Percentage yield = actual yield × theoretical yield
    - _why wrong:_ Percentage yield divides the two yields and × 100, it does not multiply them.

**Q8.** _(Triple-Foundation extra)_ — State why the percentage yield of a reaction can never be greater than 100%.
- [✔︎] You cannot collect more product than the maximum predicted by the balanced equation
- [ ] Because some product always evaporates
    - _why wrong:_ Evaporation is one type of loss; the real reason is you cannot exceed the maximum the equation allows.
- [ ] Because reactions always speed up over time
    - _why wrong:_ Rate is unrelated; the cap at 100% is because the equation sets the maximum possible product.
- [ ] Because the balance cannot read above 100 g
    - _why wrong:_ The balance reads mass in grams, not percentage; yield is capped at 100% by the equation.

**Q9.** _(Triple-Foundation extra)_ — Give one practical reason why product is lost when a solid is separated by filtration.
- [✔︎] Some of the solid stays on the filter paper or sticks to the glassware and is not collected
- [ ] The solid reacts with the filter paper
    - _why wrong:_ The usual loss is product left on the paper or glassware, not a reaction with the paper.
- [ ] Filtration creates new waste atoms
    - _why wrong:_ Filtration makes no atoms; some product is simply left behind on the paper or apparatus.
- [ ] The solid turns into a gas during filtration
    - _why wrong:_ Filtration does not vaporise the solid; product is lost by being left on the paper or glassware.

**Q10. ⭐** _(Triple-Foundation extra)_ — A reaction has a theoretical yield of 10 g and an actual yield of 9 g. State the percentage yield.
- [✔︎] 90% — (9 ÷ 10) × 100
- [ ] 111% — (10 ÷ 9) × 100
    - _why wrong:_ Yield cannot exceed 100%: (9 ÷ 10) × 100 = 90%.
- [ ] 10% — 100% minus 90%
    - _why wrong:_ 10% is the loss; the yield is (9 ÷ 10) × 100 = 90%.
- [ ] 1% — using the 1 g difference
    - _why wrong:_ The 1 g shortfall is not the yield; (9 ÷ 10) × 100 = 90%.

**Q11.** _(Triple-Foundation extra)_ — State which is normally larger: the theoretical yield or the actual yield.
- [✔︎] The theoretical yield
- [ ] The actual yield
    - _why wrong:_ The actual yield is normally smaller, because of losses and incomplete reactions.
- [ ] They are always exactly equal
    - _why wrong:_ In practice the actual yield is less than the theoretical yield.
- [ ] It depends only on the temperature
    - _why wrong:_ Whatever the conditions, the actual yield is normally below the theoretical maximum.

**Q12.** _(Triple-Foundation extra)_ — State one thing a consistently low percentage yield tells a manufacturer about their process.
- [✔︎] The process is wasteful — a lot of the reactants are not ending up as useful product, which costs money
- [ ] The process is running too quickly
    - _why wrong:_ Yield is about how much product forms, not speed; a low yield signals waste, not high rate.
- [ ] The product must be very pure
    - _why wrong:_ Yield does not measure purity; a low yield indicates waste of reactants.
- [ ] The balanced equation must be wrong
    - _why wrong:_ A low yield is normally due to real losses, not an incorrect equation.

**Q13. ⭐** _(Triple-Higher extra)_ — Magnesium burns in oxygen: 2Mg + O₂ → 2MgO. Calculate the theoretical yield of magnesium oxide when 4.8 g of magnesium is burned. Ar: Mg = 24, O = 16.
- [✔︎] 8 g — n(Mg) = 4.8 ÷ 24 = 0.2 mol; ratio 1:1; mass = 0.2 × 40
- [ ] 4.8 g — the oxide equals the mass of the metal
    - _why wrong:_ Oxygen is added, so the oxide is heavier: 0.2 mol × 40 = 8 g.
- [ ] 192 g — 4.8 × 40, skipping the moles
    - _why wrong:_ Convert to moles first: 4.8 ÷ 24 = 0.2 mol, then × 40 = 8 g.
- [ ] 0.2 g — stopping at the moles
    - _why wrong:_ 0.2 mol × Mr(MgO) = 0.2 × 40 = 8 g.

**Q14. ⭐** _(Triple-Higher extra)_ — When 4.8 g of magnesium is burned (theoretical yield of magnesium oxide = 8.0 g), 6.4 g of magnesium oxide is actually collected. Calculate the percentage yield.
- [✔︎] 80% — (6.4 ÷ 8.0) × 100
- [ ] 125% — (8.0 ÷ 6.4) × 100, dividing the wrong way
    - _why wrong:_ Yield cannot exceed 100%: (6.4 ÷ 8.0) × 100 = 80%.
- [ ] 20% — 100% minus 80%, giving the loss
    - _why wrong:_ 20% is the loss; the yield is (6.4 ÷ 8.0) × 100 = 80%.
- [ ] 64% — using the actual yield in grams
    - _why wrong:_ 6.4 g is a mass; divide by the theoretical yield: (6.4 ÷ 8.0) × 100 = 80%.

**Q15. ⭐** _(Triple-Higher extra)_ — A reaction has a theoretical yield of 25 g and a percentage yield of 60%. Calculate the actual yield obtained.
- [✔︎] 15 g — actual yield = (60 ÷ 100) × 25
- [ ] 41.7 g — 25 ÷ 0.60, dividing instead of multiplying
    - _why wrong:_ Actual yield = (% ÷ 100) × theoretical = 0.6 × 25 = 15 g.
- [ ] 60 g — using the percentage as a mass
    - _why wrong:_ 60 is a percentage; the actual yield is 0.6 × 25 = 15 g.
- [ ] 10 g — 25 minus 60% of something
    - _why wrong:_ Multiply the theoretical yield by 0.6: 0.6 × 25 = 15 g.

**Q16. ⭐** _(Triple-Higher extra)_ — A student obtains an actual yield of 21 g at a percentage yield of 70%. Calculate the theoretical yield.
- [✔︎] 30 g — theoretical = actual ÷ (percentage ÷ 100) = 21 ÷ 0.70
- [ ] 14.7 g — 21 × 0.70, multiplying instead of dividing
    - _why wrong:_ Theoretical yield = actual ÷ 0.70 = 21 ÷ 0.70 = 30 g.
- [ ] 70 g — using the percentage as a mass
    - _why wrong:_ 70 is a percentage; theoretical = 21 ÷ 0.70 = 30 g.
- [ ] 15 g — 21 × 0.70 then rounding
    - _why wrong:_ Divide, do not multiply: 21 ÷ 0.70 = 30 g.

**Q17. ⭐** _(Triple-Higher extra)_ — Calcium carbonate decomposes: CaCO₃ → CaO + CO₂. 25 g of calcium carbonate is heated and 11.2 g of calcium oxide is collected. Calculate the percentage yield. Mr: CaCO₃ = 100, CaO = 56.
- [✔︎] 80% — theoretical CaO = 0.25 mol × 56 = 14 g; (11.2 ÷ 14) × 100
- [ ] 44.8% — dividing 11.2 by 25 (the carbonate mass)
    - _why wrong:_ Compare with the theoretical CaO (14 g), not the carbonate: (11.2 ÷ 14) × 100 = 80%.
- [ ] 125% — (14 ÷ 11.2) × 100, dividing the wrong way
    - _why wrong:_ Yield cannot exceed 100%: (11.2 ÷ 14) × 100 = 80%.
- [ ] 20% — 100% minus 80%, giving the loss
    - _why wrong:_ 20% is the loss; the yield is (11.2 ÷ 14) × 100 = 80%.

**Q18.** _(Triple-Higher extra)_ — The Haber process, N₂ + 3H₂ ⇌ 2NH₃, is reversible. Explain why its yield of ammonia is always less than 100%.
- [✔︎] Because the reaction is reversible and reaches an equilibrium, so ammonia breaks back down and not all of the nitrogen and hydrogen is converted to ammonia
- [ ] Because ammonia is a gas that always escapes the reactor
    - _why wrong:_ The key reason is reversibility and equilibrium, not gas escaping; the reaction does not go to completion.
- [ ] Because the nitrogen and hydrogen are impure
    - _why wrong:_ Even with pure reactants the yield is limited, because the reaction reaches equilibrium.
- [ ] Because ammonia has a very high atom economy
    - _why wrong:_ Atom economy is a separate measure; the yield is limited because the reaction is reversible.

**FIFA worked examples — Foundation (in TF)** ⭐

- **Percentage yield from two masses** — A student expects to make 8.0 g of copper sulfate but collects only 6.2 g. Calculate the percentage yield.
    - **F** — percentage yield = (actual yield ÷ theoretical yield) × 100
    - **I** — actual = 6.2 g;  theoretical = 8.0 g
    - **F** — = (6.2 ÷ 8.0) × 100 = 0.775 × 100
    - **A** — percentage yield = 77.5%
- **Another pair of masses** — A reaction should produce 40 g of product but only 30 g is obtained. Calculate the percentage yield.
    - **F** — percentage yield = (actual yield ÷ theoretical yield) × 100
    - **I** — actual = 30 g;  theoretical = 40 g
    - **F** — = (30 ÷ 40) × 100
    - **A** — percentage yield = 75%
- **A high yield** — A theoretical yield is 50 g and 45 g of product is collected. Calculate the percentage yield.
    - **F** — percentage yield = (actual yield ÷ theoretical yield) × 100
    - **I** — actual = 45 g;  theoretical = 50 g
    - **F** — = (45 ÷ 50) × 100
    - **A** — percentage yield = 90%

**FIFA worked examples — Higher (in TH)** ⭐

- **Theoretical yield first, then percentage yield** — Magnesium burns: 2Mg + O₂ → 2MgO. 4.8 g of magnesium is burned and 6.4 g of magnesium oxide is collected. Calculate the percentage yield. Ar: Mg = 24, O = 16.
    - **F** — find the theoretical yield from the equation, then % yield = (actual ÷ theoretical) × 100
    - **I** — n(Mg) = 4.8 ÷ 24 = 0.2 mol;  n(MgO) = 0.2 mol;  theoretical = 0.2 × 40 = 8.0 g;  actual = 6.4 g
    - **F** — % yield = (6.4 ÷ 8.0) × 100
    - **A** — percentage yield = 80%
- **Rearranging to find the actual yield** — A reaction has a theoretical yield of 25 g and a percentage yield of 60%. Calculate the actual yield.
    - **F** — actual yield = (percentage yield ÷ 100) × theoretical yield
    - **I** — = (60 ÷ 100) × 25
    - **F** — = 0.6 × 25
    - **A** — actual yield = 15 g
- **A decomposition, two steps** — Calcium carbonate decomposes: CaCO₃ → CaO + CO₂. 25 g of CaCO₃ gives 11.2 g of CaO. Calculate the percentage yield. Mr: CaCO₃ = 100, CaO = 56.
    - **F** — find the theoretical yield of CaO, then % yield = (actual ÷ theoretical) × 100
    - **I** — n(CaCO₃) = 25 ÷ 100 = 0.25 mol;  n(CaO) = 0.25 mol;  theoretical = 0.25 × 56 = 14 g
    - **F** — % yield = (11.2 ÷ 14) × 100
    - **A** — percentage yield = 80%

---

## Atom Economy  ·  `atom-economy`  ·  AQA 4.3.3.2 (Triple only)

> **Tier presence:** Triple only — no Combined cell exists in AQA (TF + TH).
>
> **How the cells are composed** (item numbers below): **TF** → Q1–12; **TH** → Q1–6, 13–18. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often confuse atom economy with percentage yield, or work it out from the reactants instead of the products. Atom economy uses only the products: it is the Mr of the DESIRED product divided by the sum of the Mr of ALL the products, × 100. Percentage yield is about how much product you actually collect; atom economy is a property of the balanced equation itself.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(both Triple tiers (TF·TH))_ — A reaction makes a desired product of Mr 80 and a waste product of Mr 20. Calculate the atom economy.
- [✔︎] 80% — (80 ÷ (80 + 20)) × 100 = (80 ÷ 100) × 100
- [ ] 20% — using the waste product (20 ÷ 100)
    - _why wrong:_ Atom economy uses the DESIRED product: 80 ÷ 100 × 100 = 80%.
- [ ] 400% — (80 ÷ 20) × 100, dividing by the waste only
    - _why wrong:_ Divide by the TOTAL of all products (80 + 20 = 100): 80 ÷ 100 × 100 = 80%.
- [ ] 100% — assuming all reactions are 100%
    - _why wrong:_ There is a waste product here, so the atom economy is 80 ÷ 100 × 100 = 80%.

**Q2.** _(both Triple tiers (TF·TH))_ — Explain why an addition reaction has an atom economy of 100%.
- [✔︎] There is only one product, so all of the atoms from the reactants end up in it and none are wasted
- [ ] Because addition reactions always go to completion
    - _why wrong:_ Going to completion is about yield; 100% atom economy is because there is only one product and no waste.
- [ ] Because the reactants and products have the same Mr by coincidence
    - _why wrong:_ It is not coincidence: with a single product, every reactant atom must be in it, so 100%.
- [ ] Because addition reactions release energy
    - _why wrong:_ Energy is not a product counted in atom economy; the 100% comes from having no by-products.

**Q3.** _(both Triple tiers (TF·TH))_ — State what a high atom economy tells you about a reaction.
- [✔︎] A large proportion of the reactant atoms end up in the desired product, so little is wasted
- [ ] The reaction produces a very pure product
    - _why wrong:_ Atom economy is about proportion of atoms in the desired product, not purity.
- [ ] The reaction has a very high percentage yield
    - _why wrong:_ Atom economy and yield are different; a high atom economy does not guarantee a high yield.
- [ ] The reaction is very fast
    - _why wrong:_ Atom economy says nothing about rate; it measures how much of the reactant mass is useful product.

**Q4.** _(both Triple tiers (TF·TH))_ — State the difference between atom economy and percentage yield.
- [✔︎] Atom economy is the proportion of reactant atoms that end up in the desired product (from the equation); percentage yield is how much product is actually collected compared with the maximum
- [ ] They are two names for the same quantity
    - _why wrong:_ They are different: atom economy comes from the equation, percentage yield from the experiment.
- [ ] Atom economy is measured in the lab; percentage yield is calculated from the equation
    - _why wrong:_ It is the other way round: atom economy is from the equation, percentage yield from the experiment.
- [ ] Atom economy is always larger than percentage yield
    - _why wrong:_ Neither is always larger; they measure different things.

**Q5. ⭐** _(both Triple tiers (TF·TH))_ — A reaction produces a desired product of Mr 44 and a by-product of Mr 56. Calculate the atom economy.
- [✔︎] 44% — (44 ÷ (44 + 56)) × 100 = (44 ÷ 100) × 100
- [ ] 56% — using the by-product instead
    - _why wrong:_ Atom economy uses the DESIRED product: 44 ÷ 100 × 100 = 44%.
- [ ] 79% — (44 ÷ 56) × 100, dividing by the by-product
    - _why wrong:_ Divide by the total of all products (44 + 56 = 100): 44 ÷ 100 × 100 = 44%.
- [ ] 100% — assuming one product
    - _why wrong:_ There is a by-product here, so atom economy is 44 ÷ 100 × 100 = 44%.

**Q6.** _(both Triple tiers (TF·TH))_ — Give one reason why chemists prefer reactions with a high atom economy.
- [✔︎] Less waste is produced, so raw materials are used more efficiently and fewer by-products need disposing of — cheaper and more sustainable
- [ ] The product is always formed faster
    - _why wrong:_ Rate is unrelated to atom economy; the benefit is less waste and better use of raw materials.
- [ ] The percentage yield is automatically 100%
    - _why wrong:_ Atom economy does not fix the yield; its benefit is efficient use of atoms and less waste.
- [ ] Less energy is always needed to start the reaction
    - _why wrong:_ Activation energy is separate; a high atom economy means less waste, not lower activation energy.

**Q7. ⭐** _(Triple-Foundation extra)_ — State the equation used to calculate the atom economy of a reaction.
- [✔︎] Atom economy = (Mr of the desired product ÷ sum of the Mr of all products) × 100
- [ ] Atom economy = (Mr of the desired product ÷ Mr of the reactants) × 100
    - _why wrong:_ Atom economy uses the PRODUCTS, not the reactants, on the bottom.
- [ ] Atom economy = (actual yield ÷ theoretical yield) × 100
    - _why wrong:_ That is percentage yield; atom economy uses the Mr of the products.
- [ ] Atom economy = (Mr of the waste ÷ Mr of the desired product) × 100
    - _why wrong:_ It is the DESIRED product over the total products, not waste over desired.

**Q8.** _(Triple-Foundation extra)_ — State which type of reaction always has an atom economy of 100%.
- [✔︎] An addition reaction (only one product is formed)
- [ ] A combustion reaction
    - _why wrong:_ Combustion makes more than one product (e.g. CO₂ and H₂O), so its atom economy is below 100%.
- [ ] A decomposition reaction
    - _why wrong:_ Decomposition makes two or more products, so its atom economy is below 100%.
- [ ] A neutralisation reaction
    - _why wrong:_ Neutralisation makes a salt and water, so its atom economy is below 100%.

**Q9.** _(Triple-Foundation extra)_ — State one economic reason a company wants a reaction with a high atom economy.
- [✔︎] Less raw material is wasted, so making the product costs less
- [ ] The reaction will finish more quickly
    - _why wrong:_ Speed is unrelated; the economic benefit is less wasted raw material and lower cost.
- [ ] A high atom economy means no catalyst is needed
    - _why wrong:_ Catalysts are a separate matter; the benefit is less waste and lower cost.
- [ ] The product will sell for a higher price
    - _why wrong:_ Atom economy affects efficiency and cost of making the product, not its selling price.

**Q10. ⭐** _(Triple-Foundation extra)_ — A reaction makes a desired product of Mr 60 and a waste product of Mr 40. State the atom economy.
- [✔︎] 60% — (60 ÷ (60 + 40)) × 100
- [ ] 40% — using the waste product
    - _why wrong:_ Atom economy uses the desired product: 60 ÷ 100 × 100 = 60%.
- [ ] 150% — (60 ÷ 40) × 100
    - _why wrong:_ Divide by the total of all products (100): 60 ÷ 100 × 100 = 60%.
- [ ] 100% — assuming one product
    - _why wrong:_ There is a waste product, so atom economy is 60 ÷ 100 × 100 = 60%.

**Q11.** _(Triple-Foundation extra)_ — State one environmental reason why a high atom economy is desirable.
- [✔︎] Less waste is produced, so the process uses resources more sustainably and pollutes less
- [ ] It uses up more raw materials
    - _why wrong:_ A high atom economy uses raw materials more efficiently, wasting LESS, not more.
- [ ] It always produces a gas that can be sold
    - _why wrong:_ The environmental benefit is less waste overall, not producing a saleable gas.
- [ ] It makes the product decompose harmlessly
    - _why wrong:_ Atom economy is about waste during manufacture, not how the product breaks down later.

**Q12.** _(Triple-Foundation extra)_ — State whether atom economy depends on the actual experiment or on the balanced equation.
- [✔︎] On the balanced equation — it is worked out from the relative formula masses of the products
- [ ] On the actual experiment, like percentage yield
    - _why wrong:_ That describes percentage yield; atom economy is fixed by the balanced equation.
- [ ] On the temperature used in the reaction
    - _why wrong:_ Temperature does not change atom economy; it is set by the equation's products.
- [ ] On how carefully the product is collected
    - _why wrong:_ Careful collection affects yield, not atom economy, which comes from the equation.

**Q13. ⭐** _(Triple-Higher extra)_ — Calcium oxide is made by heating limestone: CaCO₃ → CaO + CO₂. Calculate the atom economy for making calcium oxide. Mr: CaO = 56, CO₂ = 44.
- [✔︎] 56% — (56 ÷ (56 + 44)) × 100 = (56 ÷ 100) × 100
- [ ] 44% — using the carbon dioxide as the desired product
    - _why wrong:_ The desired product is CaO: 56 ÷ 100 × 100 = 56%.
- [ ] 127% — (56 ÷ 44) × 100, dividing by the CO₂ only
    - _why wrong:_ Divide by the total of all products (56 + 44 = 100): 56%.
- [ ] 100% — assuming one product
    - _why wrong:_ There are two products (CaO and CO₂), so atom economy is 56 ÷ 100 × 100 = 56%.

**Q14. ⭐** _(Triple-Higher extra)_ — Hydrogen can be made by reacting zinc with sulfuric acid: Zn + H₂SO₄ → ZnSO₄ + H₂. Calculate the atom economy for making hydrogen. Mr: H₂ = 2, ZnSO₄ = 161.
- [✔︎] 1.2% — (2 ÷ (2 + 161)) × 100 = (2 ÷ 163) × 100
- [ ] 98.8% — using the zinc sulfate as the desired product
    - _why wrong:_ The desired product is hydrogen (Mr 2): 2 ÷ 163 × 100 ≈ 1.2%.
- [ ] 50% — assuming the two products share the mass equally
    - _why wrong:_ The products have very different Mr (2 and 161): 2 ÷ 163 × 100 ≈ 1.2%.
- [ ] 100% — assuming one product
    - _why wrong:_ There are two products; the hydrogen is a tiny fraction: 2 ÷ 163 × 100 ≈ 1.2%.

**Q15. ⭐** _(Triple-Higher extra)_ — Ethanol can be made by fermentation (C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂) or by the hydration of ethene (C₂H₄ + H₂O → C₂H₅OH). Deduce which route has the higher atom economy.
- [✔︎] Hydration of ethene — it is an addition reaction with only one product, so its atom economy is 100%, higher than fermentation which also makes CO₂
- [ ] Fermentation, because glucose is a large molecule
    - _why wrong:_ Fermentation makes CO₂ as well, so its atom economy is below 100%; hydration (one product) is 100%.
- [ ] They have the same atom economy
    - _why wrong:_ Hydration makes only ethanol (100%); fermentation also makes CO₂, so it is lower.
- [ ] Fermentation, because it does not need high temperatures
    - _why wrong:_ Conditions do not set atom economy; hydration has one product (100%), higher than fermentation.

**Q16. ⭐** _(Triple-Higher extra)_ — Ethanol is made by fermentation: C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂. Calculate the atom economy for producing ethanol. Mr: C₂H₅OH = 46, CO₂ = 44.
- [✔︎] 51.1% — desired = 2 × 46 = 92; all products = 92 + (2 × 44) = 180; (92 ÷ 180) × 100
- [ ] 52% — using one ethanol molecule (46 ÷ 88)
    - _why wrong:_ There are TWO ethanol molecules (2 × 46 = 92) and two CO₂; 92 ÷ 180 × 100 = 51.1%.
- [ ] 104% — (92 ÷ 88) × 100, dividing by the CO₂ only
    - _why wrong:_ Divide by the total of all products (92 + 88 = 180): 92 ÷ 180 × 100 = 51.1%.
- [ ] 100% — assuming one product
    - _why wrong:_ Fermentation also makes CO₂, so the atom economy is 92 ÷ 180 × 100 = 51.1%.

**Q17.** _(Triple-Higher extra)_ — Explain how a reaction can have a high percentage yield but a low atom economy.
- [✔︎] Percentage yield measures how much of the possible product is collected, while atom economy measures how much of the reactant mass becomes the desired product; a reaction can convert almost completely (high yield) yet still make a large waste by-product (low atom economy)
- [ ] It cannot — a high yield always means a high atom economy
    - _why wrong:_ They are independent: a reaction can collect nearly all its product (high yield) yet make lots of waste (low atom economy).
- [ ] Because a high yield destroys some of the atoms
    - _why wrong:_ Atoms are conserved; the low atom economy is due to a large by-product, not destroyed atoms.
- [ ] Because atom economy falls as the temperature rises
    - _why wrong:_ Atom economy is fixed by the equation, not temperature; it is low when there is a big by-product.

**Q18.** _(Triple-Higher extra)_ — The hydration of ethene is C₂H₄ + H₂O → C₂H₅OH. State its atom economy and explain your answer.
- [✔︎] 100% — there is only one product, so every atom from the reactants ends up in the ethanol with no waste
- [ ] Less than 100%, because two reactants are used
    - _why wrong:_ The number of reactants does not matter; with a single product, all atoms are used, so 100%.
- [ ] 50%, because water is also a product
    - _why wrong:_ Water is a reactant here, not a product; the only product is ethanol, so 100%.
- [ ] It cannot be found without the yield
    - _why wrong:_ Atom economy comes from the equation alone; one product means 100%.

**FIFA worked examples — Foundation (in TF)** ⭐

- **Atom economy of an addition reaction** — Calculate the atom economy for making ethanol in the addition reaction C₂H₄ + H₂O → C₂H₅OH. Mr of C₂H₅OH = 46.
    - **F** — atom economy = (Mr of desired product ÷ sum of Mr of all products) × 100
    - **I** — only one product, C₂H₅OH, Mr = 46;  sum of all products = 46
    - **F** — = (46 ÷ 46) × 100
    - **A** — 100% — an addition reaction with one product
- **A reaction with a by-product** — A reaction makes a desired product of Mr 70 and a by-product of Mr 30. Calculate the atom economy.
    - **F** — atom economy = (Mr of desired product ÷ sum of Mr of all products) × 100
    - **I** — desired = 70;  all products = 70 + 30 = 100
    - **F** — = (70 ÷ 100) × 100
    - **A** — atom economy = 70%
- **Another by-product example** — A reaction makes a desired product of Mr 90 and a waste product of Mr 60. Calculate the atom economy.
    - **F** — atom economy = (Mr of desired product ÷ sum of Mr of all products) × 100
    - **I** — desired = 90;  all products = 90 + 60 = 150
    - **F** — = (90 ÷ 150) × 100
    - **A** — atom economy = 60%

**FIFA worked examples — Higher (in TH)** ⭐

- **Atom economy from a full equation** — Calculate the atom economy for making calcium oxide by heating limestone: CaCO₃ → CaO + CO₂. Mr: CaO = 56, CO₂ = 44.
    - **F** — atom economy = (Mr of desired product ÷ sum of Mr of all products) × 100
    - **I** — desired = CaO = 56;  all products = 56 + 44 = 100
    - **F** — = (56 ÷ 100) × 100
    - **A** — atom economy = 56%
- **Products with coefficients** — Calculate the atom economy for making iron: Fe₂O₃ + 3CO → 2Fe + 3CO₂. Mr: Fe = 56, CO₂ = 44.
    - **F** — multiply each product's Mr by its coefficient; atom economy = (desired ÷ all products) × 100
    - **I** — desired = 2 × 56 = 112;  all products = 112 + (3 × 44) = 112 + 132 = 244
    - **F** — = (112 ÷ 244) × 100
    - **A** — atom economy = 45.9%
- **A fermentation route** — Calculate the atom economy for making ethanol by fermentation: C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂. Mr: C₂H₅OH = 46, CO₂ = 44.
    - **F** — multiply each product's Mr by its coefficient; atom economy = (desired ÷ all products) × 100
    - **I** — desired = 2 × 46 = 92;  all products = 92 + (2 × 44) = 92 + 88 = 180
    - **F** — = (92 ÷ 180) × 100
    - **A** — atom economy = 51.1%

---

## Volumes of Gases (Molar Gas Volume)  ·  `molar-gas-volume`  ·  AQA 4.3.5 (Triple only, Higher tier)

> 🆕 **NEW PAGE — added since your first review copy.** Molar gas volume was missing from the data files entirely; this is the whole page (all blocks and questions are new). Flagged ⭐ throughout for your full review.
>
> **Tier presence:** Triple-Higher only — chemistry-only AND Higher tier, so the single TH cell.
>
> **How the cells are composed** (item numbers below): **TH** → Q1–12. Shared items are written once and appear in every cell they are tagged for.

**Common Mistake (reformatted — ✅ mistake-first):**

> Students often divide by 24 when they should multiply, or forget that 24 dm³ is 24 000 cm³ and end up 1000 times out. To go from moles to a volume in dm³ you MULTIPLY by 24; to go from a volume back to moles you DIVIDE by 24. And watch the units: 24 dm³ = 24 000 cm³, so a volume given in cm³ must be divided by 1000 before you use it as dm³.

**Question bank** (each item shows the tiers it appears in; ⭐ = full-review flag):

**Q1. ⭐** _(Triple-Higher (the only tier this page has))_ — State the volume occupied by one mole of any gas at room temperature and pressure (RTP).
- [✔︎] 24 dm³
- [ ] 1 dm³ — one mole occupies one unit of volume
    - _why wrong:_ One mole is a fixed NUMBER of particles, not one unit of volume; at RTP any gas occupies 24 dm³.
- [ ] 24 cm³ — the molar volume in cm³
    - _why wrong:_ The molar gas volume is 24 dm³, which is 24 000 cm³ — not 24 cm³.
- [ ] 22.4 dm³ — the value at STP, not RTP
    - _why wrong:_ 22.4 dm³ is the older STP value; AQA uses 24 dm³ at RTP.

**Q2. ⭐** _(Triple-Higher (the only tier this page has))_ — Calculate the volume of 2 mol of carbon dioxide at RTP.
- [✔︎] 48 dm³ — volume = moles × 24 = 2 × 24
- [ ] 0.083 dm³ — 2 ÷ 24, dividing instead of multiplying
    - _why wrong:_ Moles to volume is a MULTIPLICATION: 2 × 24 = 48 dm³. Dividing is used to go from volume back to moles.
- [ ] 88 dm³ — 2 × 44, using the Mr of CO₂
    - _why wrong:_ The molar gas volume (24), not the Mr (44), converts moles to volume: 2 × 24 = 48 dm³.
- [ ] 26 dm³ — 2 + 24, adding instead of multiplying
    - _why wrong:_ Multiply the moles by 24: 2 × 24 = 48 dm³.

**Q3. ⭐** _(Triple-Higher (the only tier this page has))_ — Calculate the amount, in moles, of gas in 72 dm³ of oxygen at RTP.
- [✔︎] 3 mol — moles = volume ÷ 24 = 72 ÷ 24
- [ ] 1728 mol — 72 × 24, multiplying instead of dividing
    - _why wrong:_ Volume to moles is a DIVISION: 72 ÷ 24 = 3 mol.
- [ ] 0.33 mol — 24 ÷ 72, dividing the wrong way
    - _why wrong:_ Divide the volume by 24, not 24 by the volume: 72 ÷ 24 = 3 mol.
- [ ] 2.25 mol — 72 ÷ 32, using the Mr of O₂
    - _why wrong:_ Use the molar gas volume (24), not the Mr (32): 72 ÷ 24 = 3 mol.

**Q4. ⭐** _(Triple-Higher (the only tier this page has))_ — Calculate the volume, in cm³, of 0.5 mol of hydrogen at RTP.
- [✔︎] 12 000 cm³ — 0.5 × 24 = 12 dm³, then × 1000
- [ ] 12 cm³ — 0.5 × 24 but not converted to cm³
    - _why wrong:_ 0.5 × 24 = 12 dm³; convert to cm³ by × 1000, giving 12 000 cm³.
- [ ] 24 000 cm³ — used 1 mol instead of 0.5 mol
    - _why wrong:_ 0.5 mol occupies half of 24 dm³: 0.5 × 24 = 12 dm³ = 12 000 cm³.
- [ ] 6 cm³ — 0.5 × 12, using 12 as the molar volume
    - _why wrong:_ The molar gas volume is 24 dm³: 0.5 × 24 = 12 dm³ = 12 000 cm³.

**Q5. ⭐** _(Triple-Higher (the only tier this page has))_ — Calculate the volume occupied at RTP by 8 g of oxygen gas (O₂). Ar: O = 16.
- [✔︎] 6 dm³ — moles = 8 ÷ 32 = 0.25 mol; volume = 0.25 × 24
- [ ] 192 dm³ — 8 × 24, using the mass instead of the moles
    - _why wrong:_ Convert the mass to moles first: 8 ÷ 32 = 0.25 mol, then × 24 = 6 dm³.
- [ ] 0.33 dm³ — 8 ÷ 24, treating the mass as a volume
    - _why wrong:_ Find the moles first (8 ÷ 32 = 0.25 mol), then × 24 = 6 dm³.
- [ ] 12 dm³ — using Mr = 16 for oxygen
    - _why wrong:_ Oxygen gas is O₂ with Mr = 32, not 16: moles = 8 ÷ 32 = 0.25 mol, volume = 6 dm³.

**Q6. ⭐** _(Triple-Higher (the only tier this page has))_ — Calculate the volume of carbon dioxide produced at RTP when 0.1 mol of calcium carbonate decomposes completely. CaCO₃ → CaO + CO₂.
- [✔︎] 2.4 dm³ — ratio 1:1 so 0.1 mol CO₂; volume = 0.1 × 24
- [ ] 0.0042 dm³ — 0.1 ÷ 24, dividing instead of multiplying
    - _why wrong:_ Moles to volume multiplies by 24: 0.1 × 24 = 2.4 dm³.
- [ ] 4.4 dm³ — 0.1 × 44, using the Mr of CO₂
    - _why wrong:_ Use the molar gas volume (24), not the Mr (44): 0.1 × 24 = 2.4 dm³.
- [ ] 24 dm³ — using 1 mol instead of 0.1 mol
    - _why wrong:_ Only 0.1 mol of CO₂ is made: 0.1 × 24 = 2.4 dm³.

**Q7. ⭐** _(Triple-Higher (the only tier this page has))_ — Calculate the volume of hydrogen produced at RTP when 0.24 g of magnesium reacts completely with excess acid. Mg + 2HCl → MgCl₂ + H₂. Ar: Mg = 24.
- [✔︎] 0.24 dm³ — moles Mg = 0.24 ÷ 24 = 0.01 mol; ratio 1:1; volume = 0.01 × 24
- [ ] 5.76 dm³ — 0.24 × 24, using the mass instead of the moles
    - _why wrong:_ Convert the mass to moles first: 0.24 ÷ 24 = 0.01 mol, then × 24 = 0.24 dm³.
- [ ] 0.01 dm³ — stopping at the moles of hydrogen
    - _why wrong:_ 0.01 mol must be multiplied by 24: 0.01 × 24 = 0.24 dm³.
- [ ] 0.48 dm³ — using a 1:2 ratio for Mg:H₂
    - _why wrong:_ The ratio Mg:H₂ is 1:1, so moles of H₂ = 0.01 mol and volume = 0.24 dm³.

**Q8. ⭐** _(Triple-Higher (the only tier this page has))_ — Equal volumes of two different gases are measured at the same temperature and pressure. Deduce what must be equal about the two samples.
- [✔︎] They contain equal numbers of moles (and molecules) — this is Avogadro's law
- [ ] They must have equal masses
    - _why wrong:_ Equal volumes have equal MOLES, but the masses differ because the gases have different Mr values.
- [ ] They must have equal relative formula masses
    - _why wrong:_ Their Mr values can differ; what is equal is the number of moles (Avogadro's law).
- [ ] They must contain equal numbers of atoms
    - _why wrong:_ They have equal numbers of MOLECULES, but not necessarily atoms — the molecules can have different numbers of atoms.

**Q9. ⭐** _(Triple-Higher (the only tier this page has))_ — In N₂ + 3H₂ → 2NH₃, all gas volumes are measured at RTP. Calculate the volume of hydrogen needed to react completely with 20 cm³ of nitrogen.
- [✔︎] 60 cm³ — equal volumes contain equal moles, so the volume ratio is 1:3: 20 × 3
- [ ] 6.67 cm³ — 20 ÷ 3, inverting the ratio
    - _why wrong:_ Hydrogen is in a 3:1 ratio to nitrogen, so multiply: 20 × 3 = 60 cm³.
- [ ] 20 cm³ — assuming a 1:1 ratio
    - _why wrong:_ The ratio N₂:H₂ is 1:3, so 20 cm³ of N₂ needs 60 cm³ of H₂.
- [ ] 40 cm³ — using the 1:2 ammonia ratio
    - _why wrong:_ 1:2 is the N₂:NH₃ ratio; for hydrogen the ratio is 1:3, giving 60 cm³.

**Q10. ⭐** _(Triple-Higher (the only tier this page has))_ — Calculate the volume, in dm³, of 0.05 mol of methane (CH₄) at RTP.
- [✔︎] 1.2 dm³ — volume = moles × 24 = 0.05 × 24
- [ ] 0.0021 dm³ — 0.05 ÷ 24, dividing instead of multiplying
    - _why wrong:_ Moles to volume multiplies by 24: 0.05 × 24 = 1.2 dm³.
- [ ] 0.8 dm³ — 0.05 × 16, using the Mr of methane
    - _why wrong:_ Use the molar gas volume (24), not the Mr (16): 0.05 × 24 = 1.2 dm³.
- [ ] 24 dm³ — the molar volume regardless of the moles
    - _why wrong:_ 24 dm³ is for one mole; 0.05 mol occupies 0.05 × 24 = 1.2 dm³.

**Q11. ⭐** _(Triple-Higher (the only tier this page has))_ — A sample of carbon dioxide has a volume of 6 dm³ at RTP. Calculate its mass. Mr of CO₂ = 44.
- [✔︎] 11 g — moles = 6 ÷ 24 = 0.25 mol; mass = 0.25 × 44
- [ ] 264 g — 6 × 44, using the volume as the moles
    - _why wrong:_ Convert the volume to moles first: 6 ÷ 24 = 0.25 mol, then × 44 = 11 g.
- [ ] 0.25 g — stopping at the moles
    - _why wrong:_ 0.25 mol must be multiplied by the Mr (44): 0.25 × 44 = 11 g.
- [ ] 6 g — using the volume as the mass
    - _why wrong:_ The volume must be converted through moles: 6 ÷ 24 = 0.25 mol, mass = 11 g.

**Q12. ⭐** _(Triple-Higher (the only tier this page has))_ — Calculate the volume of carbon dioxide produced at RTP when 5 g of calcium carbonate decomposes completely. CaCO₃ → CaO + CO₂. Mr of CaCO₃ = 100.
- [✔︎] 1.2 dm³ — moles = 5 ÷ 100 = 0.05 mol; ratio 1:1; volume = 0.05 × 24
- [ ] 120 dm³ — 5 × 24, using the mass instead of the moles
    - _why wrong:_ Convert the mass to moles first: 5 ÷ 100 = 0.05 mol, then × 24 = 1.2 dm³.
- [ ] 0.05 dm³ — stopping at the moles
    - _why wrong:_ 0.05 mol must be multiplied by 24: 0.05 × 24 = 1.2 dm³.
- [ ] 2.2 dm³ — 0.05 × 44, using the Mr of CO₂
    - _why wrong:_ Use the molar gas volume (24), not the Mr (44): 0.05 × 24 = 1.2 dm³.

**FIFA worked examples (Triple-Higher)** ⭐

- **Moles to gas volume** — Calculate the volume of 0.5 mol of oxygen gas at RTP.
    - **F** — volume of gas (dm³) = moles × 24 (at RTP)
    - **I** — = 0.5 × 24
    - **F** — = 12
    - **A** — volume = 12 dm³
- **Mass to gas volume (two steps)** — Calculate the volume occupied at RTP by 11 g of carbon dioxide. Mr of CO₂ = 44.
    - **F** — first moles = mass ÷ Mr, then volume = moles × 24
    - **I** — moles = 11 ÷ 44 = 0.25 mol;  volume = 0.25 × 24
    - **F** — = 0.25 × 24 = 6
    - **A** — volume = 6 dm³
- **Gas volume from a reacting mass, in cm³** — Calculate the volume of hydrogen, in cm³, produced at RTP when 0.48 g of magnesium reacts with excess acid. Mg + 2HCl → MgCl₂ + H₂. Ar: Mg = 24.
    - **F** — moles Mg = mass ÷ Ar; use the 1:1 ratio for H₂; volume (dm³) = moles × 24; then × 1000 for cm³
    - **I** — n(Mg) = 0.48 ÷ 24 = 0.02 mol;  n(H₂) = 0.02 mol;  volume = 0.02 × 24 = 0.48 dm³
    - **F** — 0.48 dm³ × 1000 = 480
    - **A** — volume = 480 cm³

---

