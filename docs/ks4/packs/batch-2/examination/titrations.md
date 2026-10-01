# Examination — Titrations (titrations) — not in 8464 · AQA 8462 4.4.2.5 (chemistry only) + Required practical 2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/chemistry-4.4.2.5-titrations.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019.
- 8464 has no titration section and no titration RP. Its chemistry RPs are 8 to 13: salts, electrolysis, temperature change, rates, chromatography and water.
- RP method conventions beyond the spec sentence come from examiner knowledge of the AQA Chemistry practical handbook and mark schemes: rough titre, concordance within 0.10 cm³, reading to 0.05 cm³, and the white tile.

Route copies, checked directly: the record exists only in the triple modules, TF and TH. They differ only in `higher` (TF `null`). Everything else is identical.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks.

## 1. Spec reference
| spec | section | title | page | label |
|---|---|---|---|---|
| 8464 | — | **not in 8464** | — | — |
| 8462 | **4.4.2.5** | Titrations (chemistry only) | p.48 | triple, plus one HT bullet |
| 8462 | **RP2** (Appendix 8.2.2) | "(Chemistry only) determination of the reacting volumes of solutions of a strong acid and a strong alkali by titration. (HT only) determination of the concentration of one of the solutions in mol/dm3 and g/dm3 from the reacting volumes and the known concentration of the other solution." AT 1, 8. | p.48; p.103 | triple; the HT sentence is triple-higher |
| 8462 | 4.3.4 | Using concentrations of solutions in mol/dm³ (chemistry only) (HT only) | p.42 | triple-higher |
| supporting | 8462 4.3.1.4 / 8464 5.3.1.4 | Chemical measurements: uncertainty, "use the range of a set of measurements about the mean as a measure of uncertainty" | p.38 / — | base |

BATCH-PLAN ("— · 8462 4.4.2.5 · TF TH · REQUIRED PRACTICAL") is right.

Spec statement (verbatim): "The volumes of acid and alkali solutions that react with each other can be measured by titration using a suitable indicator. Students should be able to: describe how to carry out titrations using strong acids and strong alkalis only (sulfuric, hydrochloric and nitric acids only) to find the reacting volumes accurately; (HT Only) calculate the chemical quantities in titrations involving concentrations in mol/dm3 and in g/dm3."

**`rp` field:** "RP Chemistry 2 (chemistry-only)" is **correct**. It is AQA 8462 Required practical 2, and there is no Combined Science number.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | What a titration measures (th1; summary; key_note) | triple | 4.4.2.5 | TF, TH | OK |
| R2 | Strong acids (H₂SO₄, HCl, HNO₃) and strong alkalis only (th1) | triple | 4.4.2.5 | TF, TH | OK on route. The wording "at Foundation level" is wrong (C2). |
| R3 | Apparatus: burette, pipette, conical flask, indicator, white tile (th1; matching) | triple | 4.4.2.5; RP2 AT 1 | TF, TH | OK |
| R4 | Method; rough titre; dropwise near the end point; concordant results (th2; q2; common_mistake; key_note; rp) | triple | RP2; 4.4.2.5 | TF, TH | OK |
| R5 | Errors and improvements: parallax, meniscus, rinsing (th3) | triple | RP2 (WS 2.4) | TF, TH | OK |
| R6 | Mean titre from concordant results (th3; FIFA; q1) | triple | RP2 (MS 2a); 4.3.1.4 | TF, TH | OK |
| R7 | Concentration and volume calculations from titration data, molar ratios (`higher`) | triple-higher | 4.4.2.5 HT; RP2 HT; 4.3.4 | TH | OK. **No worked example exists**, so see §5. |
| R8 | g/dm³ result from a titration (RP2 HT: "in mol/dm3 **and g/dm3**") | triple-higher | RP2 HT; 4.4.2.5 HT | **absent** | **Missing.** Add it to the TH worked example (×Mr). |

No Combined content. Nothing is misplaced between TF and TH.

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | titration finds the exact volume of one solution that reacts completely with a known volume of another | OK | — | 4.4.2.5 |
| C2 | th1 | "Used with STRONG ACIDS only at Foundation level: sulfuric, hydrochloric, nitric" | IMPRECISE | The restriction applies at **both** tiers. Write "AQA only uses strong acids (sulfuric, hydrochloric, nitric) and strong alkalis". | 4.4.2.5 |
| C3 | th1 | strong alkalis NaOH, KOH | OK | — | — |
| C4 | th1 | "BURETTE — holds the acid; accurate to ±0.05 cm³" | OK | Readings are taken to the nearest 0.05 cm³, which is the standard AQA convention. | RP2 AT 1 |
| C5 | th1 | "PIPETTE — … exactly … 25.00 cm³" | OK | — | — |
| C6 | th1 | "INDICATOR — changes colour sharply at the equivalence point (endpoint)" | OK | GCSE conflates the two terms. AQA uses "end point". | — |
| C7 | th1 | methyl orange yellow in alkali, red in acid; phenolphthalein pink in alkali, colourless in acid | OK | The spec names neither and only asks for "a suitable indicator". Add: **universal indicator is not suitable**, because it changes gradually with no sharp end point. That is a frequent mark-scheme point. | 4.4.2.5 |
| C8 | th1 | white tile to see the colour change | OK | — | — |
| C9 | th2 steps 1–7 | rinse and fill the burette, record the initial reading; pipette 25.00 cm³; 2–3 drops of indicator; swirl; dropwise near the end point; stop at a permanent colour change; titre = final − initial | OK | — | RP2 |
| C10 | th2 step 8 | concordant = "within 0.10 cm³ of each other" | OK | This is the AQA convention. | RP2 |
| C11 | th2 step 9 | mean of concordant titres only; ignore the rough run | OK | — | RP2 |
| C12 | th2 | "Random errors affect individual readings — averaging concordant results improves reliability." | IMPRECISE | AQA's 2016 working-scientifically vocabulary does not use "reliability". Write: "Repeating until results are concordant shows they are repeatable (precise). The mean of concordant results reduces the effect of random error." | WS 2; 4.3.1.4 |
| C13 | th2 | "A rough titration is done first … subsequent runs are more precise" | OK | — | — |
| C14 | th3 | parallax: eye level, bottom of the meniscus | OK | — | RP2 AT 1 |
| C15 | th3 | overshoot makes the titre too large | OK | — | — |
| C16 | th3 | not rinsing with the correct solution dilutes it; too much indicator can affect the end point | OK | Indicators are weak acids or bases, so the second point is acceptable. | — |
| C17 | th3 | rinse the pipette with alkali and the burette with acid; rough titre first; ≥2 concordant | OK | Add: the conical flask is rinsed with **distilled water only**, because water does not change the moles of alkali pipetted in. This is a common exam distinction. | RP2 |
| C18 | th3 | "discard any outliers"; 24.60, 24.55, 24.65, 25.10 → discard 25.10 → mean 24.60 cm³ | OK | 73.80 ÷ 3 = 24.60 ✓. AQA's word is "anomalous". | MS 2a |
| C19 | `higher` | moles = c × V (dm³); titre + known concentration → moles → unknown concentration; molar ratios | OK | — | 4.4.2.5 HT; 4.3.4 |
| C20 | common_mistake | concordant within 0.10 cm³; end point = permanent colour change from one drop | OK | — | RP2 |
| C21 | key_note | "Burette (acid) + pipette (alkali 25 cm³) … RP Chemistry 2 (chemistry-only)" | OK | — | 4.4.2.5; RP2 |
| C22 | equations | Titre = final − initial burette reading | OK | — | RP2 |
| C23 | FIFA | 24.85, 24.80, 24.90, 25.45: concordant three; 74.55 ÷ 3 = 24.85 cm³ | OK | The three span 0.10 cm³, so they are concordant ✓. 25.45 is 0.55 above the highest concordant value ✓. The answer is to 2 dp, consistent with the data ✓. **CFIFA Convert step:** "Nothing to convert: all titres in cm³." | RP2; MS 2a |
| C24 | rp | "RP Chemistry 2 (chemistry-only) — … strong acid and strong alkali by titration" | OK | It is a real AQA RP: 8462 RP2, with no 8464 number. The field omits RP2's HT sentence (concentration in mol/dm³ and g/dm³). That sentence is triple-higher, so add it to the TH copy of the RP block. | RP2 |
| C25 | matching (to be replaced) | burette, pipette, indicator, concordant | OK | — | — |
| C26 | q1 key | use 24.60, 24.55, 24.65; discard 25.10 | OK | — | RP2 |
| C27 | q1 wx1 | "25.10 is 0.50 cm³ away from the other three" | IMPRECISE | It is 0.45–0.55 cm³ above them, or 0.50 cm³ above their mean. | — |
| C28 | q1 wx2, wx3 | no basis for picking the highest values; use all concordant results | OK | — | — |
| C29 | q2 key | dropwise near the end point to avoid overshooting, which gives a titre that is too large | OK | — | RP2 |
| C30 | q2 wx1–3 | safety is not the reason; indicators respond quickly; neutralisation heat will not boil the solution | OK | — | — |

## 4. Frozen items wrong for their route
None. Both quiz items are triple content and correctly keyed.
- **q1** ("A student records titres of 24.60…"): rung 2 (apply) on TF and TH. wx1's "0.50" is a minor imprecision.
- **q2** ("why is the acid added dropwise"): rung 1 or a body check on both routes.

## 5. For the lesson author

**Required practical (8462 RP2) — method**
1. Use a pipette and pipette filler to transfer 25.00 cm³ of alkali (for example sodium hydroxide) into a conical flask, standing on a white tile.
2. Add a few drops of a suitable indicator (methyl orange or phenolphthalein; not universal indicator).
3. Rinse the burette with the acid, then fill it using a funnel, below eye level. Remove the funnel, and record the initial reading to the nearest 0.05 cm³ at the bottom of the meniscus.
4. Run in the acid while swirling. Do a rough titration first, then repeat, adding acid dropwise near the end point, until a single drop gives a permanent colour change.
5. Record the final reading. Titre = final − initial.
6. Repeat until there are at least two concordant titres (within 0.10 cm³). Calculate the mean of the concordant titres.

**Variables**

This is a measurement practical, not a variable investigation.

| type | what |
|---|---|
| measured | titre (cm³) |
| fixed | volume of alkali (25.00 cm³); concentration of the known solution; the same indicator and number of drops |
| controlled | the same end-point colour judgement, the same apparatus |

**Risks**

| hazard | control |
|---|---|
| dilute acids and alkalis are irritants; NaOH is especially hazardous to eyes | wear eye protection |
| mouth pipetting | always use a pipette filler |
| filling the burette above head height | fill it below eye level, using a funnel |
| broken glassware | handle with care |
| indicators dissolved in ethanol are flammable | keep away from flames |

**Typical results:** titres of about 20–25 cm³ for about 0.1 mol/dm³ solutions. The rough titre is typically 0.5–1 cm³ high. Concordant titres within 0.10 cm³. The mean is reported to 2 dp.

**HT worked example the author must write new** (checked; R7/R8):

*"25.00 cm³ of sodium hydroxide solution is neutralised by a mean titre of 20.00 cm³ of 0.100 mol/dm³ sulfuric acid. H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O. Calculate the concentration of the NaOH in mol/dm³ and in g/dm³ (Mr NaOH = 40)."*

| CFIFA step | working |
|---|---|
| Convert | 20.00 cm³ → 0.02000 dm³; 25.00 cm³ → 0.02500 dm³ |
| Formula | n = c × V |
| Insert | n(H₂SO₄) = 0.100 × 0.02000 = 0.00200 mol |
| Fine-tune | 1 : 2 ratio, so n(NaOH) = 0.00400 mol; c = n ÷ V = 0.00400 ÷ 0.02500 |
| Answer | 0.160 mol/dm³; × 40 = 6.40 g/dm³ |

The 1:2 ratio is the deliberate trap. Forgetting it gives 0.0800, which is the commonest HT error.

**Misconceptions commonly seen**
- **Universal indicator chosen as the indicator.**
- **Including the rough titre, or an anomalous titre,** in the mean.
- **"Repeat to make it more accurate"**, versus the AQA wording: repeat to check it is repeatable, then calculate a mean.
- **Rinsing the burette or pipette with water**, which dilutes the solution. The reverse error is rinsing the flask with alkali, which adds extra alkali.
- **Reading the top of the meniscus,** or not at eye level.
- **Titre = final reading only**, forgetting to subtract the initial reading.
- **HT:**
  - Ignoring a 2:1 or 1:2 mole ratio (H₂SO₄).
  - Not converting cm³ to dm³.
  - Using the volume of the other solution.
  - Confusing g/dm³ with mol/dm³.

**Command words:** Describe (method), Explain (a step), Suggest (an improvement or source of error), Calculate (mean titre; HT concentration), Identify (an anomalous result), Give.

**Typical questions (⚑ examiner-drafted)**
- ⚑ examiner-drafted, 6 marks, levels of response, Describe, **triple**: *"Describe how a student could use titration to find the volume of dilute hydrochloric acid that reacts with 25.0 cm³ of sodium hydroxide solution."*
  - Level 3 (5–6): a coherent, logically sequenced method that would give accurate results. It includes measuring the alkali with a pipette, adding an indicator, adding acid from a burette with swirling, dropwise near the end point, a colour change, reading the volume, and repeating to concordant results.
  - Level 2 (3–4): the main steps, with some omissions in sequence or accuracy features.
  - Level 1 (1–2): isolated relevant points.
  - Indicative content:
    - pipette (with filler) 25.0 cm³ of NaOH into a conical flask
    - a few drops of a named suitable indicator
    - acid in a burette; initial reading
    - add acid while swirling
    - white tile
    - dropwise near the end point
    - stop at the colour change (for example methyl orange yellow → red)
    - final reading; titre = final − initial
    - rough titre first; repeat to concordant (within 0.10 cm³); mean
- ⚑ examiner-drafted, 2 marks, Calculate, **triple**: *"Titres: 22.40, 22.10, 22.15, 22.20 cm³. Calculate the mean titre."*
  - (1) Identifies concordant results: 22.10, 22.15, 22.20, with 22.40 excluded (it is the rough or anomalous titre).
  - (1) 22.15 cm³.
- ⚑ examiner-drafted, 2 marks, Explain, **triple**: *"Explain why the student rinsed the burette with acid, not water, before filling it."*
  - (1) Water would dilute the acid.
  - (1) This would lower its concentration, so the titre would be larger or inaccurate.
- ⚑ examiner-drafted, 4–5 marks, Calculate, **triple-higher**: the H₂SO₄ / NaOH example above.
  - (1) Moles of acid.
  - (1) Ratio ×2.
  - (1) ÷ 0.02500.
  - (1) 0.160 mol/dm³.
  - (+1 where asked) 6.40 g/dm³.

**Equations to learn (recalled)**
- Titre = final reading − initial reading. **Triple.**
- Mean of concordant titres. **Triple.**
- n = c × V (dm³); c = n ÷ V; g/dm³ = mol/dm³ × Mr. **Triple-higher.**

## 6. Verdict
**SOURCE OK WITH FLAGS.**
- **Route corrections: none.** TF/TH tagging is correct throughout.
- **Missing (1).** The HT worked calculation, including g/dm³. A checked version is in §5.
- **WRONG: 0.**
- **IMPRECISE (3).** C2 "at Foundation level", C12 "reliability", C27 "0.50 cm³".
- **The `rp` field** is a real AQA RP with the right number (8462 RP2). The HT sentence of RP2 is missing from it.

Only Mide can rule: **none.**

Note for the commander: there is no `examiner_tip`.
