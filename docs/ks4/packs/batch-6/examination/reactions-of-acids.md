# Examination — Reactions of Acids with Metals and Bases (reactions-of-acids) — AQA 8464 5.4.2.1–5.4.2.2 / 8462 4.4.2.1–4.4.2.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/chemistry-5.4.2.1-reactions-of-acids.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.1.1.1, 5.4.1.2, 5.4.2.1–5.4.2.4; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.4.2.1–4.4.2.5 (identical wording for 4.4.2.1–4.4.2.4). Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `reactions-of-acids` (base, CF CH TF TH, OK; "HT layer: redox in terms of electrons"). Site neighbours from `site-routes.tsv`: `oxidation-reduction` (5.4.1.4), `salts-neutralisation` (5.4.2.2–5.4.2.3), `ph-scale` (5.4.2.4).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n, as `generate_site_v5.py` pairs them). T1–T3 = theory chunks. Route copies: `higher` is `null` on CF and TF, text on CH and TH. No `[NEW — to be examined]` Convert lines in the file (no calculations).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.4.2.1** | Reactions of acids with metals | base; redox bullets **(HT only)** |
| 8462 | **4.4.2.1** | Reactions of acids with metals | base; redox bullets **(HT only)** |
| 8464 | **5.4.2.2** | Neutralisation of acids and salt production | base |
| 8462 | **4.4.2.2** | Neutralisation of acids and salt production | base |
| Supporting | 5.1.1.1 / 4.1.1.1 "(HT only) write balanced half equations and ionic equations where appropriate"; 5.4.1.2 / 4.4.1.2 reactivity series ("hydrogen and carbon are often included"); 5.4.2.4 / 4.4.2.4 H⁺, OH⁻, H⁺ + OH⁻ → H₂O (base, own lesson `ph-scale`); 5.4.2.3 / 4.4.2.3 soluble salts + RP (own lesson `salts-neutralisation`); 8462 4.8.2.1, 4.8.2.3 / 8464 5.8.2.1, 5.8.2.3 tests for H₂ and CO₂ | | |

Spec statements (verbatim, 8464 = 8462):
- 5.4.2.1: "Acids react with some metals to produce salts and hydrogen. (HT only) Students should be able to: explain in terms of gain or loss of electrons, that these are redox reactions; identify which species are oxidised and which are reduced in given chemical equations. Knowledge of reactions limited to those of magnesium, zinc and iron with hydrochloric and sulfuric acids."
- 5.4.2.2: "Acids are neutralised by alkalis (eg soluble metal hydroxides) and bases (eg insoluble metal hydroxides and metal oxides) to produce salts and water, and by metal carbonates to produce salts, water and carbon dioxide. The particular salt produced in any reaction between an acid and a base or alkali depends on: the acid used (hydrochloric acid produces chlorides, nitric acid produces nitrates, sulfuric acid produces sulfates); the positive ions in the base, alkali or carbonate. Students should be able to: predict products from given reactants; use the formulae of common ions to deduce the formulae of salts."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Acid = H⁺ in water; base; alkali = soluble base, OH⁻ (T1) | base | 5.4.2.4; 5.4.2.2 | all four | OK |
| R2 | Salt naming: chloride / sulfate / nitrate + metal ion (T1; common_mistake; key_note) | base | 5.4.2.2 | all four | OK |
| R3 | Acid + metal → salt + hydrogen; Mg, Zn, Fe; Cu/Ag/Au no reaction (T2; equations) | base | 5.4.2.1; 5.4.1.2 | all four | OK |
| R4 | Redox in terms of electrons; species oxidised/reduced | **higher** | 5.4.2.1 (HT only) | **absent** | GAP (C27) — spec core added to source |
| R5 | Acid + metal oxide → salt + water (T2) | base | 5.4.2.2 | all four | OK |
| R6 | Acid + metal hydroxide → salt + water; H⁺ + OH⁻ → water (T3) | base | 5.4.2.2; 5.4.2.4 | all four | OK |
| R7 | Acid + metal carbonate → salt + water + CO₂; fizzing; limewater (T3; common_mistake) | base | 5.4.2.2; 5.8.2.3 | all four | OK |
| R8 | "Neutralisation" applied only to hydroxides (T3; key_note) | base | 5.4.2.2 | all four | IMPRECISE (C18) |
| R9 | Deduce salt formulae from ion formulae | base | 5.4.2.2 | not taught (examples only) | GAP (C28) |
| R10 | `higher`: ionic equations for neutralisation and precipitation; spectator ions | H⁺ + OH⁻ → H₂O is **base** (5.4.2.4); ionic equations/spectator ions **higher** (5.1.1.1 HT); precipitation **off this lesson** | 5.4.2.4; 5.1.1.1 | CH TH only | ROUTE (C26) |
| R11 | Tests: H₂ squeaky pop; CO₂ limewater (T2, T3; key_note) | base | 5.8.2.1; 5.8.2.3 | all four | OK |
| R12 | Equations (6) | base | 5.4.2.1; 5.4.2.2 | all four | OK |
| R13 | q1 | base | 5.4.2.2 | all four | OK — usable on all routes |
| R14 | q2 | base | 5.4.2.1; 5.4.2.2 | all four | OK — usable on all routes |
| — | RP | none on this page | RP 8 (Combined) / RP 1 (8462) is 5.4.2.3, lesson `salts-neutralisation` | — | correct |
| — | FIFA, `examiner_tip`, variables | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | acid produces H⁺ ions in water; HCl, H₂SO₄, HNO₃ | OK | — | 5.4.2.4 |
| C2 | T1 | base neutralises an acid; bases are metal oxides or hydroxides | OK | Spec examples exactly. | 5.4.2.2 |
| C3 | T1 | alkali = base that dissolves in water, gives OH⁻; NaOH, KOH, Ca(OH)₂ | OK | Ca(OH)₂ only slightly soluble (limewater) — fine. | 5.4.2.2; 5.4.2.4 |
| C4 | T1 | salt = metal ion + negative ion from the acid; chloride/sulfate/nitrate; NaCl, MgCl₂, ZnSO₄, CuSO₄, Ca(NO₃)₂, KNO₃ | OK | All formulae ✓. | 5.4.2.2 |
| C5 | T2 | Mg + 2HCl → MgCl₂ + H₂; Zn + H₂SO₄ → ZnSO₄ + H₂; Fe + 2HCl → FeCl₂ + H₂ | OK | Balanced ✓; exactly the spec's limited set. | 5.4.2.1 |
| C6 | T2 | H₂ test: lit splint → squeaky pop | OK | — | 5.8.2.1 |
| C7 | T2 | only metals above hydrogen react with dilute acids; Cu, Ag, Au no reaction | OK | Hydrogen in the series is in spec. | 5.4.1.2 |
| C8 | T2 | CuO + 2HCl → CuCl₂ + H₂O; ZnO + H₂SO₄ → ZnSO₄ + H₂O; Fe₂O₃ + 3H₂SO₄ → Fe₂(SO₄)₃ + 3H₂O | OK | All balanced ✓ (Fe₂O₃: O 3+12 = 12+3 ✓). | 5.4.2.2 |
| C9 | T2 | metal oxides are bases — neutralise acids | OK | — | 5.4.2.2 |
| C10 | T2 | oxide powder dissolves; solution changes colour "(e.g. blue for copper sulfate)" | IMPRECISE (minor) | The worked example made copper **chloride** (CuO + HCl), which is blue-green; give CuO + H₂SO₄ → CuSO₄ (blue) if the colour is used. | — |
| C11 | T3 | NaOH + HCl → NaCl + H₂O; 2KOH + H₂SO₄ → K₂SO₄ + 2H₂O; Ca(OH)₂ + 2HCl → CaCl₂ + 2H₂O | OK | Balanced ✓. | 5.4.2.2 |
| C12 | T3 | neutralisation: H⁺ + OH⁻ → water | OK | Base (5.4.2.4). | 5.4.2.4 |
| C13 | T3 | CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂; Na₂CO₃ + H₂SO₄ → Na₂SO₄ + H₂O + CO₂; ZnCO₃ + 2HCl → ZnCl₂ + H₂O + CO₂ | OK | Balanced ✓. | 5.4.2.2 |
| C14 | T3 | CO₂ test: limewater turns milky/cloudy | OK | — | 5.8.2.3 |
| C15 | T3 | fizzing; solid carbonate dissolves | OK | — | — |
| C16 | T3 | summary of four general equations | OK | — | 5.4.2.1; 5.4.2.2 |
| C17 | equations | 6 equations | OK | All as C5, C13. | — |
| C18 | T3; key_note | "Acid + metal hydroxide → salt + H₂O (neutralisation)" — the only reaction labelled neutralisation | IMPRECISE | Spec: acids are **neutralised** by alkalis, bases (oxides, insoluble hydroxides) **and** metal carbonates. All three are neutralisation; only acid + metal is not. | 5.4.2.2 |
| C19 | common_mistake | carbonate → three products; salt name from metal + acid | OK | — | 5.4.2.2 |
| C20 | key_note | summary; "metals above H only" | OK | Apart from C18. | — |
| C21 | matching (to be replaced) | four pairs | OK | Replaced anyway. | — |
| C22 | q1 key | ZnCO₃ + H₂SO₄ → zinc sulfate + water + CO₂ | OK | — | 5.4.2.2 |
| C23 | q1 wx1 → opt 1 "Zinc sulfate + hydrogen"; wx2 → opt 2 "Zinc oxide + water + CO₂"; wx3 → opt 3 "Zinc sulfate + water only" | each rebuts its own option | OK | Paired ✓ (no shift). wx2 slightly thin (says "not zinc oxide" without why — the salt is a sulfate) but not false. | 5.4.2.2 |
| C24 | q2 key | Mg + HCl → magnesium chloride | OK | — | 5.4.2.1; 5.4.2.2 |
| C25 | q2 wx1 → opt 1 "sulfate"; wx2 → opt 2 "oxide"; wx3 → opt 3 "hydroxide" | each rebuts its own option | OK | Paired ✓ (no shift). | 5.4.2.2 |
| C26 | `higher` (CH/TH) | "ionic equations for neutralisation and precipitation. Net ionic equation: H⁺ + OH⁻ → H₂O. Spectator ions …" | ROUTE | H⁺ + OH⁻ → H₂O is **base** (5.4.2.4, its own lesson `ph-scale`) and is already in T3 on all routes. Writing ionic equations / spectator ions is HT (5.1.1.1). Precipitation reactions are not in 5.4.2.1–5.4.2.2. The spec's actual HT content for this lesson (redox, C27) is absent. | 5.4.2.1; 5.4.2.4; 5.1.1.1 |
| C27 | (absent) | redox in terms of electrons; identify species oxidised/reduced | GAP (Higher) | e.g. Mg + 2H⁺ → Mg²⁺ + H₂: Mg loses electrons (oxidised); H⁺ gains electrons (reduced). Limited to Mg, Zn, Fe with HCl and H₂SO₄. Added to source as "Spec core missing". | 5.4.2.1 (HT only) |
| C28 | (absent) | use the formulae of common ions to deduce the formulae of salts | GAP | Theory lists salt formulae but never the method (balance the charges: Mg²⁺ + 2Cl⁻ → MgCl₂; 2Na⁺ + SO₄²⁻ → Na₂SO₄). | 5.4.2.2 |

Count: **0 WRONG**; IMPRECISE C10, C18; GAP C27 (Higher), C28; ROUTE C26. **Wrong-explanation alignment checked on both items: every key n explains option n — no one-option-late shift.**

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| None. q1 and q2 correct, base, explanations paired to their own options. | | Use both on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- Acid + carbonate: water or CO₂ omitted.
- Acid + metal gives "salt + water"; acid + oxide gives hydrogen.
- Wrong salt family (sulfuric → chloride); nitrates and sulfates confused.
- Salt formulae with unbalanced charges (MgCl, NaSO₄).
- Copper "reacts slowly" with dilute acid (it does not).
- HT: "the acid is oxidised"; or oxidation given as gain of electrons (OIL RIG reversed).

**Command words**: Name the salt, Complete the word/symbol equation, Predict the products, Describe a test (H₂, CO₂), (HT) Explain in terms of electrons why this is a redox reaction; Identify the species oxidised.

**Typical questions** ⚑ examiner-drafted
- *Name the salt formed when zinc oxide reacts with sulfuric acid. [1]* — zinc sulfate.
- *Complete the word equation: calcium carbonate + hydrochloric acid → ___ + ___ + ___. [2]* — calcium chloride (1); water and carbon dioxide (1).
- *Give the formula of the salt formed from Mg²⁺ and NO₃⁻. [1]* — Mg(NO₃)₂.
- *(HT) Mg + 2H⁺ → Mg²⁺ + H₂. Explain why this is a redox reaction. [2]* — magnesium atoms lose electrons, so are oxidised (1); hydrogen ions gain electrons, so are reduced (1).

**Required practical**: none on this page. The soluble-salt practical (Combined RP 8 / Chemistry 8462 RP 1, 5.4.2.3 / 4.4.2.3, all four routes) belongs to `salts-neutralisation`.

**Equations**: chemical equations only; no formula triangles.

## 6. Verdict
SOURCE OK WITH FLAGS. All frozen chemistry and all 15 equations correct; both quiz items usable on all routes, explanations correctly paired. The spec's one Higher statement (redox in terms of electrons) is missing — the CH/TH `higher` box carries a base equation and off-lesson precipitation instead. Two theory imprecisions (neutralisation applied only to hydroxides; copper colour), one skill gap (salt formulae from ions).

**For Mide:** nothing.
