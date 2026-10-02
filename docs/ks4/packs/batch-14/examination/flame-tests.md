# Examination — Flame Tests (flame-tests) — AQA 8462 4.8.3.1 (chemistry only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-14/04-checked-science-source/chemistry-4.8.3.1-flame-tests.md`.
Spec sources read as text: `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) §4.8.3 (heading "(chemistry only)"), §4.8.3.1, §4.8.3.5 (RP7 statement), §4.8.3.6–4.8.3.7, §8.2.4, §8.2.7; `AQA-8464-spec.txt` searched: no flame-test content in Combined Trilogy. Route audit row `flame-tests` (TF TH, chem-only).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. The Triple Foundation `higher` copy is `null`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | — | not in Combined Trilogy | — |
| 8462 | **4.8.3.1** | Flame tests | chemistry only (4.8.3 heading) |
| 8462 | **RP7** (§4.8.3.5; §8.2.7) | identify the ions in unknown single ionic compounds, 4.8.3.1–4.8.3.5 | chemistry only |
| Linked | 8462 4.8.3.7 Flame emission spectroscopy | | chemistry only (lesson `instrumental-methods`) |

Spec statements (verbatim): "Flame tests can be used to identify some metal ions (cations). Lithium, sodium, potassium, calcium and copper compounds produce distinctive colours in flame tests: lithium compounds result in a crimson flame; sodium compounds result in a yellow flame; potassium compounds result in a lilac flame; calcium compounds result in an orange-red flame; copper compounds result in a green flame. If a sample containing a mixture of ions is used some flame colours can be masked. Students should be able to identify species from the results of the tests in 4.8.3.1 to 4.8.3.5. Flame colours of other metal ions are not required knowledge." (AT 8; WS 2.2)
RP: "Required practical 7: use of chemical tests to identify the ions in unknown single ionic compounds covering the ions from sections Flame tests (page 73) to Sulfates (page 74)." AT 1 and 8 (§4.8.3.5); §8.2.7 lists AT 2 (Bunsen) and AT 8 ("gas tests, flame tests, precipitation reactions").

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Flame tests identify some metal ions (th1, key_note) | triple | 8462 4.8.3.1 | OK |
| R2 | Five colours: Li crimson, Na yellow, K lilac, Ca orange-red, Cu green (th1, common_mistake, key_note, q1, matching) | triple | 8462 4.8.3.1 | IMPRECISE colour words (FT-F2) |
| R3 | Method: clean nichrome loop (HCl), dip, hold in flame (th1) | triple (RP7) | 8462 4.8.3.1; RP7, AT 2/8 | OK |
| R4 | Mixtures: some colours masked; sodium masks potassium (th2, q2) | triple | 8462 4.8.3.1 | OK |
| R5 | Limitations: similar colours, cations only (th2) | triple | 8462 4.8.3.1, 4.8.3.6 | OK |
| R6 | Electron excitation explanation (th2, `higher`) | **not a layer**, off-spec in 8462 4.8.3 | — | ROUTE / OFF-SPEC (FT-F3) |
| R7 | Flame emission spectroscopy, advantages of instrumental methods (th3, `higher`, key_note) | triple (base within Triple) | 8462 4.8.3.6–4.8.3.7 | OK; owned by `instrumental-methods` (FT-F4) |
| R8 | `rp` RP badge | triple | **Chemistry RP7** | WRONG number (FT-F1) |

True page routes: TF TH. The whole lesson is the triple layer, with no HT layer. Matches what the site ships.

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | clean nichrome loop with HCl, in a blue flame until no colour; dip; hold at edge of blue flame | OK | Standard method. | RP7, AT 8 |
| C2 | th1 | Li⁺ crimson/red | OK | Spec: crimson. | 4.8.3.1 |
| C3 | th1 | Na⁺ yellow/orange | IMPRECISE | Spec: **yellow**. | 4.8.3.1 (FT-F2) |
| C4 | th1 | K⁺ lilac/purple | IMPRECISE | Spec: **lilac**. | 4.8.3.1 (FT-F2) |
| C5 | th1 | Ca²⁺ orange-red | OK | Spec wording. | 4.8.3.1 |
| C6 | th1 | Cu²⁺ green/blue-green | IMPRECISE | Spec: **green**. | 4.8.3.1 (FT-F2) |
| C7 | th1 | mnemonic "Li-Criminal …" | OK | Harmless. | — |
| C8 | th2 | electrons excited, emit light of specific wavelengths | OFF-SPEC | Correct physics, but not in 8462 4.8.3 at any tier. | (FT-F3) |
| C9 | th2 | sodium's yellow masks potassium's lilac | OK | "some flame colours can be masked". | 4.8.3.1 |
| C10 | th2 | Li crimson vs Ca orange-red can be confused; flame tests detect cations only | OK | — | 4.8.3.1 |
| C11 | th2 | "RPCHEM 4: Identify metal ions using flame tests …" | WRONG | It is **RP7**. 8462 RP4 is temperature changes in reacting solutions. | §4.8.3.5, §8.2.7 (FT-F1) |
| C12 | th3 | FES: sample in a flame, light through prism/grating, line spectrum, identify and measure concentration; more precise, quantitative, sensitive, objective | OK | Spec says "passed through a spectroscope"; output a line spectrum; identify ions and measure concentrations. Advantages: "accurate, sensitive and rapid". | 4.8.3.6–4.8.3.7 (FT-F4) |
| C13 | `higher` | electron excitation; energy gap; FES more quantitative | ROUTE / OFF-SPEC | 4.8.3.1 has no HT statement. The FES comparison is chemistry-only base (4.8.3.6), not HT. | (FT-F3) |
| C14 | common_mistake | Na yellow/orange not red; Li crimson; K lilac; Ca orange-red; Na contamination | OK | Same colour-word note as C3. | 4.8.3.1 |
| C15 | key_note | Li crimson, Na yellow/orange, K lilac, Ca orange-red, Cu green | OK | Copper "green" matches the spec. | 4.8.3.1 |
| C16 | rp | "RP Chemistry 4 (chemistry-only) — Identify the ions in an unknown compound. Includes flame tests for metal cations." | WRONG | **Chemistry RP7**. Content right; "single ionic compounds" is the spec's wording. `_extract-notes.md` repeats "RP Chemistry 4". | §4.8.3.5, §8.2.7 (FT-F1) |
| C17 | q1 key | persistent yellow/orange → Na⁺ | OK | Stem's "yellow/orange" still points uniquely to sodium. | 4.8.3.1 |
| C18 | q1 opt 1 / wx1 | potassium lilac/purple, not yellow | OK | Aligned ✓. | 4.8.3.1 |
| C19 | q1 opt 2 / wx2 | calcium orange-red, not yellow | OK | Aligned ✓. | 4.8.3.1 |
| C20 | q1 opt 3 / wx3 | copper green/blue-green, not orange | OK | Aligned ✓. | 4.8.3.1 |
| C21 | q2 key | sodium's yellow masks potassium's lilac | OK | Spec's masking statement. | 4.8.3.1 |
| C22 | q2 opt 1 / wx1 | no chemical reaction; optical masking | OK | Aligned ✓. | — |
| C23 | q2 opt 2 / wx2 | each ion emits its own colour; sodium overpowers | OK | Aligned ✓. | — |
| C24 | q2 opt 3 / wx3 | Na and K can occur separately | OK | Aligned ✓. | — |
| C25 | matching (to be replaced) | five colours | OK | Same colour-word note. | — |

Count: **2 WRONG** (C11, C16: the RP number, in theory and in the frozen `rp` field). IMPRECISE: C3, C4, C6. OFF-SPEC/ROUTE: C8, C13.

## 4. Frozen items wrong for their route
None. **q1 and q2 are usable on TF and TH.**

## 5. For the lesson author
**Misconceptions seen in AQA marking:** sodium "red" or "orange" alone; potassium "purple"/"blue"; lithium and calcium swapped; "copper gives blue" (the mark is green; blue is the copper(II) hydroxide precipitate in 4.8.3.2); naming the element instead of the ion when asked; not cleaning the loop.

**Command words:** Identify (the ion from the result), Give the flame colour, Explain why the result for a mixture may be unreliable, Describe how to carry out a flame test.

**Typical questions** ⚑ examiner-drafted
- *A compound gives a lilac flame. Identify the metal ion. [1]* — potassium / K⁺.
- *Explain why a flame test may not identify both metal ions in a mixture of sodium and potassium compounds. [2]* — sodium's (yellow) flame colour (1); masks the lilac of potassium (1).
- 6-mark RP7: identify the ions in an unknown salt. Flame test for the cation (or NaOH precipitate); acid + limewater for carbonate; nitric acid + silver nitrate for halide; HCl + barium chloride for sulfate.

**Required practical:** **Chemistry RP7** (8462 4.8.3.5; §8.2.7), chemistry only, TF TH. It spans 4.8.3.1–4.8.3.5, so this lesson carries the flame-test part only.

**Equations:** none.

## 6. Verdict
SOURCE HAS ERRORS. The RP is mislabelled "Chemistry 4" in the frozen `rp` field and in th2. It is RP7 (FT-F1). The colour words should be the spec's single words (FT-F2). The electron explanation is off-spec and the `higher` field is not a Higher layer (FT-F3). Both quiz items are correct and usable on TF and TH. No question for Mide.
