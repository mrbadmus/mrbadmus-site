# Examination — Metal Hydroxides (metal-hydroxides) — not in 8464 · AQA 8462 4.8.3.2 (chemistry only) + Required practical 7
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/chemistry-4.8.3.2-metal-hydroxides.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019. 8464's "Chemical analysis" (5.8) stops at gas tests (5.8.2), so ion tests are chemistry only.
Route copies, checked directly: the record exists only in TF and TH. They differ only in `higher` (TF `null`).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks.

## 1. Spec reference
| spec | section | title | page | label |
|---|---|---|---|---|
| 8464 | — | **not in 8464** | — | — |
| 8462 | **4.8.3.2** | Metal hydroxides (in 4.8.3 "Identification of ions by chemical and spectroscopic means (chemistry only)") | p.74 | triple; no HT marker in the section |
| 8462 | **RP7** (Appendix 8.2.7) | "use of chemical tests to identify the ions in unknown single ionic compounds covering the ions from sections Flame tests … to Sulfates" (AT 2, 8) | p.74; p.107 | triple |
| 8462 | 4.8.3.1 | Flame tests, including "Students should be able to identify species from the results of the tests in 4.8.3.1 to 4.8.3.5." | p.73 | triple |
| 8462 | 4.1.1.1 | "(HT only) write balanced half equations and ionic equations where appropriate." | p.18 | higher, so triple-higher here |

BATCH-PLAN ("— · 8462 4.8.3.2 · TF TH · CLASSIFY") is right.

Spec statement (verbatim): "Sodium hydroxide solution can be used to identify some metal ions (cations). Solutions of aluminium, calcium and magnesium ions form white precipitates when sodium hydroxide solution is added but only the aluminium hydroxide precipitate dissolves in excess sodium hydroxide solution. Solutions of copper(II), iron(II) and iron(III) ions form coloured precipitates when sodium hydroxide solution is added. Copper(II) forms a blue precipitate, iron(II) a green precipitate and iron(III) a brown precipitate. Students should be able to write balanced equations for the reactions to produce the insoluble hydroxides. **Students are not expected to write equations for the production of sodium aluminate.**"

**`rp` field:** "RP Chemistry 4 (chemistry-only) — Test for metal ions using NaOH" is the **wrong number**.
- The ion-tests practical is **8462 Required practical 7**.
- RP4 is "investigate the variables that affect temperature changes in reacting solutions".
- There is no Combined Science equivalent, since 8464 has no ion-tests RP.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | NaOH test: method, precipitate colours Cu²⁺ blue, Fe²⁺ green, Fe³⁺ brown, Ca²⁺ / Mg²⁺ / Al³⁺ white (th1; key_note; matching; q1) | triple | 4.8.3.2 | TF, TH | OK |
| R2 | Only Al(OH)₃ dissolves in excess (th1; th2; common_mistake; q2) | triple | 4.8.3.2 | TF, TH | OK |
| R3 | **Balanced (full) symbol equations** for forming the hydroxides, for example CuSO₄ + 2NaOH → Cu(OH)₂ + Na₂SO₄ | **triple** (no HT marker in 4.8.3.2) | 4.8.3.2 | **absent** | **Missing base content.** The author must add it for TF and TH. |
| R4 | Ionic equations M²⁺ + 2OH⁻ → M(OH)₂ etc. (th2; equations; `higher`) | **triple-higher** | 4.1.1.1 (HT only, ionic equations) | th2 and equations: TF and TH. `higher`: TH. | **HT content shown as base on TF** (th2 and the equations field). Tag it `triple-higher`. |
| R5 | Al(OH)₃ + OH⁻ → Al(OH)₄⁻; "amphoteric"; "aluminate ion" (th2; `higher`; key_note; q2 key text) | **NOT-IN-SPEC** | 4.8.3.2: "not expected to write equations for the production of sodium aluminate" | TF, TH (`higher` asks pupils to *write* it) | Cut the equation and the instruction to write it. "Amphoteric" may stay as a word, untested. |
| R6 | Ammonium ion test: warm with NaOH, ammonia turns damp red litmus blue (th1; th3; key_note) | **NOT-IN-SPEC** | absent from 4.8.3 (the ions are those of 4.8.3.1–4.8.3.5) | TF, TH | Cut, or keep as a clearly marked untested aside. **Never a rung.** |
| R7 | Combining flame test + NaOH (th3) | triple | 4.8.3.1 ("identify species from the results of the tests in 4.8.3.1 to 4.8.3.5"); RP7 | TF, TH | OK on route. The example's parenthetical is wrong (C14). |
| R8 | "Carry out and interpret systematic ion identification" (`higher`) | **triple** (base), not HT | 4.8.3.1; RP7 | TH only | **Base content withheld from TF.** |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | NaOH + metal-salt solutions → insoluble hydroxide precipitates; colour identifies the ion | OK | — | 4.8.3.2 |
| C2 | th1 method | a few drops; observe; then excess | OK | — | RP7 |
| C3 | th1 | Cu²⁺ blue Cu(OH)₂; Fe²⁺ green Fe(OH)₂; Fe³⁺ "brown/rust-red" Fe(OH)₃ | OK | The spec says "brown". "Rust-red" / "orange-brown" are acceptable synonyms in AQA mark schemes, but teach **brown** as the answer to write. Fe(OH)₂ often darkens to brown on standing, as air oxidises it. Worth one line, because pupils see it in RP7. | 4.8.3.2 |
| C4 | th1 | Ca²⁺ white Ca(OH)₂ "(sparingly soluble)"; Mg²⁺ white; Al³⁺ white | OK | — | 4.8.3.2 |
| C5 | th1 / th3 / key_note | NH₄⁺: no precipitate; warm → NH₃ turns damp red litmus blue | OK (chemistry) / NOT-IN-SPEC | See R6. | — |
| C6 | th2 | M²⁺(aq) + 2OH⁻(aq) → M(OH)₂(s); M³⁺ + 3OH⁻ → M(OH)₃ | OK (science) / route **triple-higher** | See R4. | 4.1.1.1 HT |
| C7 | th2 | Cu²⁺ / Fe²⁺ / Fe³⁺ specific ionic equations | OK / triple-higher | They are balanced and charge-balanced. | 4.1.1.1 HT |
| C8 | th2 | "Al(OH)₃ is AMPHOTERIC — dissolves in both acids and excess alkali" | OK (chemistry) / NOT-IN-SPEC | — | — |
| C9 | th2 | Al(OH)₃ + OH⁻ → Al(OH)₄⁻ | OK (chemistry) / **NOT-IN-SPEC (explicitly excluded)** | See R5. | 4.8.3.2 |
| C10 | th2 | Al dissolves in excess; Ca and Mg do not | OK | — | 4.8.3.2 |
| C11 | th3 | "Flame test first — identifies Na, K, Li, Ca, Cu positively" | OK | These are the five flame-test ions of 4.8.3.1. | 4.8.3.1 |
| C12 | th3 | NaOH identifies Cu, Fe²⁺, Fe³⁺ and distinguishes Al from Ca/Mg | OK | Add: **Ca²⁺ and Mg²⁺ are then told apart by flame test** (Ca orange-red; Mg gives no colour in the spec's list). This is a classic RP7 question. | 4.8.3.1–4.8.3.2 |
| C13 | th3 | "transition metals (Cu, Fe²⁺, Fe³⁺)" | OK | — | 8462 4.1.3 (transition metals, chemistry only) |
| C14 | th3 | "blue precipitate … AND green flame → likely copper(II) ions (but the flame test wouldn't show green for dissolved Cu²⁺ in solution — would use spectroscopy for that)" | **WRONG** | Copper compounds, including solutions on a wire loop or splint, do give a green flame. 4.8.3.1 says "copper compounds result in a green flame". Delete the parenthetical. The first half (blue precipitate + green flame → Cu²⁺) is right. | 4.8.3.1 |
| C15 | `higher` | "Write balanced ionic equations for precipitate formation" | OK / triple-higher | — | 4.1.1.1 HT |
| C16 | `higher` | "Write the equation for dissolution of Al(OH)₃ in excess NaOH" | **NOT-IN-SPEC (explicitly excluded)** | Cut. | 4.8.3.2 |
| C17 | `higher` | "combine flame test + NaOH test results to identify both cation and anion" | **WRONG** / route | Both tests identify **cations** only. Anions need the carbonate, halide and sulfate tests (4.8.3.3–4.8.3.5). Combining results is base triple, not HT (R8). | 4.8.3.1–4.8.3.5 |
| C18 | common_mistake | Fe²⁺ green vs Fe³⁺ brown; Al dissolves in excess, Ca and Mg do not | OK | — | 4.8.3.2 |
| C19 | key_note | colour list | OK | — | 4.8.3.2 |
| C20 | key_note | "NH₄⁺: warm with NaOH → ammonia gas (blue litmus)" | NOT-IN-SPEC / IMPRECISE | "(blue litmus)" reads as "blue litmus paper" rather than "turns damp red litmus blue". Cut, with R6. | — |
| C21 | key_note | "Aluminium unique: amphoteric" | NOT-IN-SPEC (term) | Write "only aluminium hydroxide dissolves in excess NaOH", which is the spec's wording. | 4.8.3.2 |
| C22 | equations | M²⁺(aq) + 2OH⁻(aq) → M(OH)₂(s) | OK / triple-higher | — | 4.1.1.1 HT |
| C23 | rp | "RP Chemistry 4" | **WRONG** | 8462 **RP7**. | 8462 p.74, Appendix 8.2.7 |
| C24 | matching (to be replaced) | Cu blue, Fe²⁺ green, Fe³⁺ brown, Al white dissolves, Ca white remains | OK | — | 4.8.3.2 |
| C25 | q1 key | brown → Fe³⁺ | OK | — | 4.8.3.2 |
| C26 | q1 wx1–3 | Fe²⁺ green; Cu blue; Ca white | OK | — | 4.8.3.2 |
| C27 | q2 key | Al³⁺, "Al(OH)₃ is amphoteric and dissolves in excess NaOH to form aluminate" | OK | It is true. "Amphoteric / aluminate" goes beyond the spec, but the keyed identification is exactly 4.8.3.2. | 4.8.3.2 |
| C28 | q2 wx1–3 | Ca(OH)₂ and Mg(OH)₂ do not dissolve in excess; Na⁺ gives no precipitate | OK | — | 4.8.3.2 |

## 4. Frozen items wrong for their route
None is route-wrong. Both quiz items are triple and correctly keyed.
- **q1** ("An unknown solution gives a brown precipitate…"): usable as rung 1 on TF and TH.
- **q2** ("A white precipitate forms … then dissolves…"): usable as rung 1 or 2 on TF and TH. Its keyed text mentions "aluminate" (true, beyond the spec), which does not make it wrong. **Do not** build a rung that asks for the aluminate *equation*.

## 5. For the lesson author

**Misconceptions commonly seen**
- **Swapping iron(II) green and iron(III) brown.** The single most common error.
- **The colour of the solution versus the colour of the precipitate.** Copper(II) sulfate *solution* is blue too. Pupils must report the precipitate.
- **Adding excess NaOH at once** and missing the transient Al(OH)₃ precipitate, so aluminium is reported as "no precipitate".
- **Calling every white precipitate "calcium"**, without testing in excess or doing a flame test.
- **Writing the precipitate as NaOH or as the metal**, or getting the hydroxide formula wrong (Fe(OH)₃ vs Fe(OH)₂, unbalanced OH).
- **Believing the flame test identifies all metals**, including Mg, Al and Fe.
- **Thinking the NaOH test identifies the anion.**

**Command words:** Identify, Describe (a test and its result), Give (the result), Complete (an equation), Write (a balanced equation), Explain (how to distinguish), Suggest, Plan (RP7).

**Typical questions (⚑ examiner-drafted)**
- ⚑ examiner-drafted, 2 marks, Describe, **triple**: *"Describe how sodium hydroxide solution can show that a solution contains iron(III) ions."*
  - (1) Add (a few drops of) sodium hydroxide solution.
  - (1) A brown precipitate forms.
- ⚑ examiner-drafted, 2 marks, Complete / Write, **triple**: *"Complete the balanced equation: CuSO₄ + __NaOH → Cu(OH)₂ + ____"*
  - (1) 2.
  - (1) Na₂SO₄.
- ⚑ examiner-drafted, 2 marks, Write, **triple-higher**: *"Write the ionic equation for the formation of iron(II) hydroxide."*
  - (1) Fe²⁺ + 2OH⁻ → Fe(OH)₂.
  - (1) Correct state symbols: (aq) + (aq) → (s).
  - Allow the first mark for the correct species even if unbalanced.
- ⚑ examiner-drafted, 6 marks, levels of response, Plan, **triple** (RP7): *"Three unlabelled solutions are aluminium sulfate, calcium chloride and magnesium nitrate. Plan how to identify each one using only chemical tests from this course."*
  - Level 3 (5–6): a logical plan that would distinguish all three, naming both the NaOH test (with excess) and the flame test, with results for each solution.
  - Level 2 (3–4): a plan that distinguishes at least two, with results.
  - Level 1 (1–2): a relevant test named with a partial result.
  - Indicative content:
    - add NaOH dropwise: all three give a white precipitate
    - add excess: only aluminium's dissolves
    - flame test on the other two: calcium orange-red, magnesium no colour
    - nichrome wire cleaned with acid
    - small samples in separate tubes

**Required practical: 8462 RP7** (ions in unknown single ionic compounds)
- **Method (NaOH part):**
  - Place about 1 cm³ of the test solution in a test tube.
  - Add dilute NaOH dropwise, and record the colour of any precipitate.
  - Add NaOH in excess, shaking. Record whether a white precipitate dissolves.
- **Variables:** not a variables investigation. Identification is the outcome. Control the use of small, equal volumes and clean tubes.
- **Risks:**
  - NaOH is an irritant, or corrosive at higher concentration, and especially harmful to the eyes: wear eye protection.
  - Some metal salts are harmful or toxic (copper and barium compounds, in the anion part): avoid skin contact and wash hands.
  - The flame test part uses a Bunsen burner (AT 2): hot wire, hair tied back.
- **Typical results:** Cu²⁺ blue gelatinous precipitate; Fe²⁺ green, which darkens on standing; Fe³⁺ orange-brown; Al³⁺ white, which dissolves in excess to a colourless solution; Ca²⁺ white (can be faint); Mg²⁺ white.

**Equations to learn (recalled)**
- Full balanced equations for forming the hydroxides, for example CuSO₄ + 2NaOH → Cu(OH)₂ + Na₂SO₄, and FeCl₃ + 3NaOH → Fe(OH)₃ + 3NaCl. **Triple.**
- Ionic equations Mⁿ⁺ + nOH⁻ → M(OH)ₙ with state symbols. **Triple-higher.**
- **Not** the aluminate equation (excluded by the spec).

## 6. Verdict
**SOURCE OK WITH FLAGS.**
- **Route corrections (3).**
  - Ionic equations are shown as base on TF (th2 and the equations field).
  - "Systematic identification" is base, but is withheld from TF in `higher`.
  - The full balanced equations, which are base triple, are missing.
- **NOT-IN-SPEC (2).** The aluminate equation (explicitly excluded by the spec) and the ammonium-ion test.
- **WRONG (3).**
  - The copper flame-test parenthetical (C14).
  - "Identify both cation and anion" (C17).
  - The `rp` number: RP4, which should be RP7 (C23).
- **IMPRECISE (1).** The key-note litmus wording.
- **The `rp` field:** a real AQA RP with the **wrong number**. It is 8462 RP7, and there is no Combined equivalent.

Only Mide can rule: **none.**
- Tagging the full equations as triple and the ionic equations as triple-higher follows from reading 4.8.3.2 (no HT marker) together with 4.1.1.1 (ionic equations HT only).
- That is a lookup, not a conflict between AQA sources.

Note for the commander: there is no `examiner_tip`.
