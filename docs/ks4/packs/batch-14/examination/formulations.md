# Examination — Formulations (formulations) — AQA 8464 5.8.1.2 / 8462 4.8.1.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-14/04-checked-science-source/chemistry-5.8.1.2-formulations.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §5.8.1.2, §5.2.2.7; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) §4.8.1.2, §4.3.3 (chemistry only), §4.8.3.1 (chemistry only). Route audit row `formulations` (CF CH TF TH, base).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Both `higher` route copies are `null`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.8.1.2** | Formulations | base |
| 8462 | **4.8.1.2** | Formulations | base |

Spec statements (verbatim, 8464 = 8462): "A formulation is a mixture that has been designed as a useful product. Many products are complex mixtures in which each chemical has a particular purpose. Formulations are made by mixing the components in carefully measured quantities to ensure that the product has the required properties. Formulations include fuels, cleaning agents, paints, medicines, alloys, fertilisers and foods. Students should be able to identify formulations given appropriate information. Students do not need to know the names of components in proprietary products." (WS 1.4, 2.2)

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Definition: designed mixture, useful product (th1, common_mistake, key_note) | base | 5.8.1.2 / 4.8.1.2 | OK |
| R2 | Each component has a purpose; measured quantities give the required properties (th1, th2, q2) | base | 5.8.1.2 / 4.8.1.2 | OK |
| R3 | The spec's seven examples (th1, th3) | base | 5.8.1.2 / 4.8.1.2 | OK (C3 minor) |
| R4 | Identify a formulation from information (q1) | base | 5.8.1.2 / 4.8.1.2 | OK |
| R5 | th3 "Flame tests identify metal ions" | **triple** | 8462 4.8.3.1 (chemistry only) | ROUTE (FO-F2) |
| R6 | th3 "Chromatography can separate and identify components" | base | 5.8.1.3 / 4.8.1.3 | OK |
| R7 | `higher`: evaluate components (base), atom economy (chemistry only, not formulations), green chemistry (off-spec) | **not a layer** | 5.8.1.2; 8462 4.3.3.2 | ROUTE / OFF-SPEC (FO-F1) |
| — | equations, fifas, rp | none | — | correct |

True page routes: CF CH TF TH, all base, no HT or triple layer. Matches what the site ships.

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | formulation = mixture designed for a purpose; specific measured amounts | OK | Spec wording. | 5.8.1.2 |
| C2 | th1 | random mixture is not a formulation | OK | — | 5.8.1.2 |
| C3 | th1 | "ALLOYS: specific proportions of metals" | IMPRECISE (minor) | An alloy can contain a non-metal, and common_mistake itself names steel as iron + carbon. Say "a metal mixed with other elements". | 8462 4.10.3.2 |
| C4 | th1 | medicines, paints, fuels, fertilisers, food, cleaning products, cosmetics | OK | Cosmetics is an extra example, which is fine. | 5.8.1.2 |
| C5 | th2 | tablet roles: active ingredient, binder, filler, coating, preservative | OK | Generic roles, not proprietary names, so within "do not need to know names of components in proprietary products". Not required knowledge. | 5.8.1.2 |
| C6 | th2 | paint: pigment, binder, solvent, additives | OK | Not required knowledge. | — |
| C7 | th3 | anti-knock agents, corrosion inhibitors, sports drinks, sunscreen, NPK | OK | Context. | — |
| C8 | th3 | "Flame tests identify metal ions" | ROUTE | Flame tests are 8462 4.8.3.1, chemistry only. Not taught on CF CH. | FO-F2 |
| C9 | `higher` | "Atom economy in pharmaceutical synthesis… Green chemistry principles" | OFF-SPEC / ROUTE | Atom economy is 8462 4.3.3.2 (chemistry only), not HT and not formulation content. Green chemistry is not on the spec. | FO-F1 |
| C10 | common_mistake | steel is a formulation (iron and carbon) | OK | Alloys are named formulations. | 5.8.1.2 |
| C11 | key_note | summary | OK | — | — |
| C12 | q1 key | toothpaste is a formulation | OK | Components given generically. | 5.8.1.2 |
| C13 | q1 opt 1 / wx1 | tap water is not deliberately designed | OK | Aligned ✓. | — |
| C14 | q1 opt 2 / wx2 | sand and gravel is a random mixture | OK | Aligned ✓. | — |
| C15 | q1 opt 3 / wx3 | pure ethanol is a single compound, not a mixture | OK | Aligned ✓. Links to 5.8.1.1. | 5.8.1.1 |
| C16 | q2 key | exact dose: too little ineffective, too much toxic | OK | "carefully measured quantities … required properties". | 5.8.1.2 |
| C17 | q2 opt 1 / wx1 | colour from pigments or coatings | OK | Aligned ✓. | — |
| C18 | q2 opt 2 / wx2 | cost is secondary to safety | OK | Aligned ✓. | — |
| C19 | q2 opt 3 / wx3 | size is set by fillers | OK | Aligned ✓. | — |
| C20 | matching (to be replaced) | tablet roles | OK | — | — |

Count: **0 WRONG**. IMPRECISE: C3. ROUTE: C8. OFF-SPEC/ROUTE: C9.

## 4. Frozen items wrong for their route
None. **q1 and q2 are usable on all four routes.**

## 5. For the lesson author
**Misconceptions seen in AQA marking:** any mixture counts as a formulation; a single pure compound counts as a formulation; describing a formulation without saying that the quantities are measured or controlled (the mark usually needs "carefully measured quantities" or "each component has a purpose").

**Command words:** Identify, Give, Explain why … is a formulation, Suggest.

**Typical questions** ⚑ examiner-drafted
- *What is a formulation? [2]* — a mixture designed as a useful product (1); made by mixing components in carefully measured quantities (1).
- *A label lists the percentages of five ingredients in a paint. Explain why the paint is a formulation. [2]* — it is a mixture of several substances, each with a purpose (1); in measured/specific proportions (1).

## 6. Verdict
SOURCE OK WITH FLAGS. Spec content is complete and correct, and both quiz items work on every route. The `higher` field carries no Higher content: it is chemistry-only atom economy plus off-spec green chemistry (FO-F1). The flame-test mention is chemistry-only (FO-F2). No question for Mide.
