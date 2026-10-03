# Independent examiner review — frozen KS4 corrections (commit `269afe270`)

Reviewer: independent AQA GCSE science examiner (Claude), 2 Oct 2026. Read-only review of `docs/ks4/FROZEN-CORRECTIONS.md` against `git show 269afe270 -- 'all_subtopics_*.py'`, the original findings (`docs/ks4/packs/batch-{2,3}/DEPARTURES.md` §1 at `269afe270^`), and the AQA spec texts (8461/8462/8463/8464).

## Overall verdict: **PASS — no FIX rows**

All 19 items and AE-1…AE-6 are scientifically correct and creditable by AQA. Each one fully fixes the defect it was raised for, keeps its shape, sits on-spec on every route that carries it, and was applied to exactly the right route copies. Nothing outside the approved rows changed.

## How it was verified (mechanically, not by reading the diff alone)

- I loaded all 12 route files at `269afe270^` and at `269afe270` as Python data and diffed them structurally. That gives **163 leaf changes, all string VALUE changes**. There are no key, type or length changes, so no option was added, removed or reordered. The changed paths match the report's field list exactly: same lessons, same fields, same route files.
- **Residual sweep.** I searched all 12 after-files for the 61 distinct before-strings. The only survivors are the two intended carve-outs:
  - the fridge item on biology TF/TH (B2-W6), which is in-spec there (8461 4.7.2.3) and is the TF/TH rung-1 `K.find`;
  - the KOH mol/dm³ item on chemistry TH (B2-W4), which is in-spec there (8462 4.3.4, HT, chemistry only).

  No route that held a wrong text was missed.
- **Shape.** In every item in the 12 files, exactly one option is `True` and it is at index 0. On all 19 corrected items, `wrong_explanations` is keyed 1–3, key *n* explains option *n*, and each one names that option's misconception (checked by reading each one in full).
- **AQA atom-economy formula confirmed** from 8462 4.3.3.2, verbatim: *"Relative formula mass of desired product from equation ÷ Sum of relative formula masses of all reactants from equation × 100"*. AE-1, AE-3, AE-4 and AE-6 now state exactly this. B3-W9's key is worked in this form.

## Verdict per row

| id | routes | verdict | note |
|---|---|---|---|
| B2-W1 enzymes | CF CH TF TH | **PASS** | "Up to the optimum … rate does increase" is correct; the misconception (hotter = faster beyond the optimum) is now refuted, not taught. |
| B2-W2 atoms-elements-compounds wx3 | CF CH TF TH | **PASS** | Sulfur does melt (~115 °C). The new reason (a new substance has formed) is the creditable one. |
| B2-W3 atoms-elements-compounds stem | CF CH TF TH | **PASS** | Naming water as the product leaves one creditable answer. wx2 now agrees with the stem. |
| B2-W4 using-moles-calculations | CH only | **PASS** | The arithmetic is right: 4.8/24 = 0.2, 3.2/32 = 0.1, 8.0/40 = 0.2, so 2:1:2. Each distractor's working really gives its value: 4.8:3.2:8.0 = 3:2:5, and 3.2/16 = 0.2. The item is 8464 5.3.2.3 (HT) on a Higher route whose lesson covers 5.3.2.3–5.3.2.4, and it does not duplicate q1 (limiting reactant). TH copy correctly untouched. |
| B2-W5 concentration-of-solutions | CF CH TF TH | **PASS** | 80 × 25 = 2000, so the label now matches its own working. wx2 no longer teaches a false relationship. g/dm³ is on Combined Foundation. |
| B2-W6 decomposition | CF CH only | **PASS** | The key paraphrases 8464 4.7.2.2 ("returning carbon to the atmosphere as carbon dioxide and mineral ions to the soil"). Each of the three distractors is a genuine misconception with a matching wx. It does not duplicate q0 (decomposers vs detritivores). TF/TH correctly untouched. |
| B2-W7 relative-formula-mass wx1 | CF CH TF TH | **PASS** | The self-contradiction is gone. 24 + 28 + 96 = 148. |
| B2-W8 percentage-yield | TF TH | **PASS** | "0.7% — forgot to ×100" is a real misconception, and wx1 matches it. |
| B2-W9 carbonates-halides-sulfates | TF TH | **PASS** | "Remove carbonate ions" is the AQA-credited reason. The false claim about sulfate is removed from both the key and wx1. |
| B2-W10 changes-in-energy | CF CH TF TH | **PASS** | Correctly diagnoses doubling instead of squaring (½ × 800 × 40). wx1 no longer reads as a next step. |
| B3-W1 temperature-changes-shc | CF CH TF TH | **PASS** | 900 J = 2 × 450 = m × c. The label and wx3 are now arithmetically true. |
| B3-W2 sound-waves-hearing wx2 | TH | **PASS** | The direction is now right: X-rays pass through soft tissue more easily than bone. The page-placement point (4.6.1.5 content on the 4.6.1.4 page) is outside the approval and is correctly left as a note. |
| B3-W3 microscopy wx2 | CF CH TF TH | **PASS** | ×10 eyepiece × ×40 objective = ×400. The false ×200-objective fact is gone. |
| B3-W4 microscopy wx3 | CF CH TF TH | **PASS** | 45 ÷ 0.01 = 4500 names the real error (rounding). |
| B3-W5 conservation-of-mass | CF CH TF TH | **PASS** | 64 = 24 + 40 is now named correctly. wx1 and wx2 are re-paired with options 1 and 2. |
| B3-W6 atom-economy q2 opt3/wx3 | TF TH | **PASS** | The catalyst distractor is unambiguously wrong as the reason, so the item now has a single creditable answer. |
| B3-W7 types-of-em-waves wx3 | CF CH TF TH | **PASS** | The resonance myth is removed. Absorption by water is correct, and microwaves do sit near the low-frequency end. |
| B3-W8 particle-motion-pressure | CF CH TF TH | **PASS** | Now asks the spec's own statement (8463 4.3.3.1 / 8464 6.3.3.1, "explain qualitatively … at constant volume"). The key carries the mark-scheme points: faster molecules, more frequent collisions, greater force, so pressure increases. No kelvin, no p ∝ T. Option 3 (right direction, wrong reason) is legitimate because the stem asks "and why". |
| B3-W9 atom-economy q1 | TF TH | **PASS** | The stem gives equation Mr values and is self-consistent (100 = 80 + 20). Every distractor names a misconception (waste, desired ÷ waste, inverted fraction) and every wx matches its option. |
| AE-1 equations[0] | TF TH | **PASS** | This is AQA's formula, verbatim in substance. |
| AE-2 common_mistake | TF TH | **PASS** | The contradiction ("not the reactants") is removed. The equivalence with total product Mr (4.3.1.2) is stated correctly. |
| AE-3 key_note | TF TH | **PASS** | Uses the reactants denominator. |
| AE-4 FIFA F | TF TH | **PASS** | Uses the reactants denominator. |
| AE-5 FIFA I | TF TH | **PASS** | C₂H₄ 28 + H₂O 18 = 46. This is consistent with the F step, and the answer of 100% is unchanged. |
| AE-6 th1 | TF TH | **PASS** | The definition is now AQA's. "ALTERNATIVELY" is now an equivalence statement, not a rival formula. |

## Scope (check 6)

- Atom-economy changes are confined to the formula, equation and common_mistake text, plus the same formula repeated within the record (key_note, FIFA F/I, th1). Atom economy does not exist on CF or CH (it is chemistry only), so 2 route copies is correct.
- The withhold entries are removed from `ks4_lessons/batch_{2,3}.py`. The only remaining mentions of `withhold` are in docstrings.

## Notes for a later ruling (outside this approval — not FIX rows)

1. The products-form atom-economy formula still appears in `chemistry_higher.py` (lines ~3588, 4270, 4281, 4364: `conservation-of-mass.higher` and `amounts-in-equations`) and in `chemistry_triple_higher.py` ~4244. FROZEN-CORRECTIONS.md already discloses this. On CH it is also chemistry-only content.
2. "kelvin" still appears 8–9 times in each physics route file, in subtopics other than the corrected item. If the B3-W8 finding holds (kelvin is in neither 8463 nor 8464), those occurrences deserve the same audit.
3. The th2 "high/low" example labels (examiner C5) and the B2-W4 TH "of water" wording (C18) are both outside the approval, as the report states.
