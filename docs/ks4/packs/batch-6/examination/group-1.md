# Examination — Group 1, Alkali Metals (group-1) — AQA 8464 5.1.2.5 / 8462 4.1.2.5
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/chemistry-5.1.2.5-group-1.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.1.2.5, 5.1.2.6, 5.2.1.2; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.1.2.5 (identical wording), 4.1.3.1. Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `group-1` (base, CF CH TF TH, OK). Densities and melting points checked against standard data (Li 0.53 g/cm³, 181 °C; Na 0.97 g/cm³, 98 °C; K 0.86 g/cm³, 63 °C).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n, as `generate_site_v5.py` pairs them: `orig_wrong_exp.get(orig_j)`). T1–T3 = theory chunks. Route copies: `higher` is `null` on CF and TF, text on CH and TH. No `[NEW — to be examined]` Convert lines in the file (no calculations).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.1.2.5** | Group 1 | base |
| 8462 | **4.1.2.5** | Group 1 | base |
| Supporting | 8464 5.2.1.2 / 8462 4.2.1.2 (Group 1 metals form +1 ions); 5.1.2.6 / 4.1.2.6 (Group 7, contrast in common_mistake); 8462 4.1.3.1 (transition metals compared with Group 1 — chemistry only, its own lesson) | | base |

Spec statements (verbatim, 8464 = 8462): "The elements in Group 1 of the periodic table are known as the alkali metals and have characteristic properties because of the single electron in their outer shell. Students should be able to describe the reactions of the first three alkali metals with oxygen, chlorine and water. In Group 1, the reactivity of the elements increases going down the group." Students should be able to: "explain how properties of the elements in Group 1 depend on the outer shell of electrons of the atoms"; "predict properties from given trends down the group." (WS 1.2)

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Members; one outer electron; form +1 ions (T1; key_note) | base | 5.1.2.5; 5.2.1.2 | all four | OK |
| R2 | Physical properties: soft, low density, low m.p., shiny/tarnish, stored under oil (T1) | base (context) | 5.1.2.5 ("characteristic properties") | all four | OK |
| R3 | Reactions with water: hydroxide + hydrogen; observations Li/Na/K; alkaline solution (T2; equations) | base | 5.1.2.5 | all four | OK (C9 minor) |
| R4 | Reactions with oxygen and chlorine | base | 5.1.2.5 | **absent** | GAP (C13) — spec core added to source |
| R5 | Reactivity increases down the group (T2, T3; common_mistake; key_note) | base | 5.1.2.5 | all four | OK |
| R6 | Explanation of the trend from the outer electron (T3; common_mistake) | base | 5.1.2.5 (WS 1.2 "explain how properties … depend on the outer shell") | all four | OK |
| R7 | `higher`: same explanation + "lower ionisation energy" + "Predict properties of Rb and Cs" | **base** (explanation, prediction); "ionisation energy" off-spec | 5.1.2.5 | CH TH only | ROUTE (C14) — not a Higher layer |
| R8 | Predict properties from given trends | base | 5.1.2.5 (WS 1.2) | only in CH/TH `higher` | ROUTE/GAP (C15) |
| R9 | Group 7 contrast (common_mistake) | base | 5.1.2.6 | all four | OK |
| R10 | Equations (4 symbol equations) | base | 5.1.2.5; 5.1.1.1 | all four | OK |
| R11 | q1 | base | 5.1.2.5 | all four | OK — usable on all routes |
| R12 | q2 | base | 5.1.2.5 | all four | OK — usable on all routes |
| — | RP, FIFA, `examiner_tip`, variables | none | — | — | correct: none on spec |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | Li 3, Na 11, K 19; Rb, Cs, Fr below | OK | — | — |
| C2 | T1 | 1 outer electron, lost easily → +1 ions | OK | — | 5.1.2.5; 5.2.1.2 |
| C3 | T1 | soft — cut with a knife | OK | — | — |
| C4 | T1 | Li, Na, K all float on water | OK | Densities 0.53, 0.97, 0.86 g/cm³ — all < 1. | — |
| C5 | T1 | low m.p./b.p. compared to other metals | OK | — | 8462 4.1.3.1 |
| C6 | T1 | shiny when cut, tarnish quickly (react with oxygen); stored under oil | OK | — | 5.1.2.5 |
| C7 | T1 | "React vigorously with WATER" (all Group 1) | IMPRECISE | Contradicts T2 ("Lithium: fizzes gently"). Say "react with water; more vigorously down the group". | 5.1.2.5 |
| C8 | T2; equations | 2M + 2H₂O → 2MOH + H₂; Li, Na, K versions | OK | All balanced ✓. | 5.1.2.5 |
| C9 | T2 | Li fizzes gently, moves on surface; Na fizzes vigorously, moves rapidly, "may catch fire"; K hydrogen ignites, lilac flame | OK | Sodium also melts into a ball (common mark-scheme observation) — worth adding; "may catch fire" acceptable (usually only if held still). | 5.1.2.5 |
| C10 | T2 | hydroxide is a strong alkali; universal indicator → purple | OK | pH 13–14 → purple/violet ✓. | 5.4.2.4 |
| C11 | T2 | K more reactive than Na, Na than Li | OK | — | 5.1.2.5 |
| C12 | T3 | larger atoms, outer electron further from nucleus, weaker attraction (distance and shielding), more easily lost → more reactive | OK | AQA mark schemes credit "more shells / further from nucleus / weaker attraction / more easily lost"; "shielding" is creditable but not needed. | 5.1.2.5 |
| C13 | (absent) | reactions with oxygen and chlorine | GAP | Spec requires the first three alkali metals with oxygen **and chlorine**. Only "tarnish (react with oxygen)" appears. Added to source as "Spec core missing". | 5.1.2.5 |
| C14 | `higher` (CH/TH) | "… lower ionisation energy … Predict properties of Rb and Cs" | ROUTE / OFF-SPEC term | Nothing in 5.1.2.5 is HT. The explanation and the prediction are base on every route (T3 already teaches it on all four). "Ionisation energy" is A-level; AQA credits "outer electron more easily lost". | 5.1.2.5 |
| C15 | (absent on CF/TF) | predict properties from given trends | GAP | Base skill. Data T1 can support: reactivity with water (Rb, Cs more violent), melting point falls down the group (Li 181, Na 98, K 63 °C). | 5.1.2.5 (WS 1.2) |
| C16 | T3 | Rb, Cs "can ignite explosively in water or air" | OK | Both ignite spontaneously in air and react explosively with water. | — |
| C17 | common_mistake | reactivity increases down Group 1, decreases down Group 7 ("harder to attract an extra electron") | OK | — | 5.1.2.5; 5.1.2.6 |
| C18 | key_note | summary | OK | — | 5.1.2.5 |
| C19 | matching (to be replaced) | five pairs | OK | All correct. Replaced anyway. | — |
| C20 | q1 key | Na + water → NaOH + H₂ | OK | — | 5.1.2.5 |
| C21 | q1 wx1 → opt 1 "Sodium oxide and water" | Na + O₂ gives the oxide; water gives hydroxide + hydrogen | OK | Paired to its own option ✓. | 5.1.2.5 |
| C22 | q1 wx2 → opt 2 "NaCl and hydrogen" | NaCl from chlorine or HCl, not water | OK | Paired ✓. | 5.1.2.5 |
| C23 | q1 wx3 → opt 3 "hydroxide and oxygen" | no oxygen released; 2Na + 2H₂O → 2NaOH + H₂ | OK | Paired ✓. | 5.1.2.5 |
| C24 | q2 key | more shells, outer electron further, more easily lost | OK | — | 5.1.2.5 |
| C25 | q2 wx1 → opt 1 "more protons" | more protons alone would hold the electron harder; distance/shells outweigh it | OK | Paired ✓. Slightly beyond GCSE but correct. | — |
| C26 | q2 wx2 → opt 2 "surface area" | surface area affects rate, not inherent reactivity | OK | Paired ✓. | — |
| C27 | q2 wx3 → opt 3 "higher charge" | all electrons carry the same charge | OK | Paired ✓. | — |

Count: **0 WRONG**; IMPRECISE C7; GAP C13, C15; ROUTE C14. **Wrong-explanation alignment checked on both items: every key n explains option n — no one-option-late shift.**

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| None. q1 and q2 are correct, base, and their explanations are paired to their own options. | | Use both on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- Reactivity decreases down Group 1 (carried over from Group 7).
- "More protons, so more reactive" — the nucleus's pull is what holds the electron; distance and shells win.
- Products of Na + water given as sodium oxide, or hydrogen omitted / oxygen given.
- Hydrogen "burns with a lilac flame" read as the hydrogen's colour — the lilac is potassium.
- Explanations in terms of "wants to lose an electron" rather than weaker attraction.

**Command words**: Describe (observations), Explain (trend, from the outer electron), Predict (Rb/Cs from trend), Write a balanced equation, Complete the word equation.

**Typical questions** ⚑ examiner-drafted
- *Describe what you would see when a small piece of sodium is added to water. [3]* — fizzes/bubbles (1); moves around on the surface (1); melts into a ball / gets smaller and disappears (1).
- *Explain why potassium is more reactive than sodium. [3]* — potassium's outer electron is further from the nucleus / more shells (1); weaker attraction to the nucleus (1); so the outer electron is lost more easily (1).
- *Predict how rubidium reacts with water. [2]* — more vigorously than potassium / explodes (1); forms rubidium hydroxide and hydrogen (1).
- *Balance: __Na + Cl₂ → __NaCl. [1]* — 2Na + Cl₂ → 2NaCl.

**Required practical**: none.

**Equations**: chemical equations only; no formula triangles.

## 6. Verdict
SOURCE OK WITH FLAGS. All frozen science correct; both quiz items usable on all routes, explanations correctly paired. The spec's reactions with oxygen and chlorine are missing (added to the source as spec core). The CH/TH `higher` box is base content and must not be a Higher layer. One theory self-contradiction (T1 "vigorously").

**For Mide:** nothing.
