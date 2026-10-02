# Examination — Direct and Alternating Potential Difference (direct-alternating-pd) — AQA 8464 6.2.3.1 / 8463 4.2.3.1
Verdict: SOURCE OK WITH FLAGS (rms/peak and oscilloscope settings are beyond the spec; both quiz items usable)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.3.1-direct-alternating-pd.md`.
Spec sources read: `AQA-8464-spec.txt` §6.2.3.1, §6.6.1.2 (T = 1/f); `AQA-8463-spec.txt` §4.2.3.1. Both June 2026 equation sheets. Route audit row `direct-alternating-pd` (base / base). A text search of both spec files for "oscilloscope", "rms" and "peak" returns nothing in either.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both). All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.2.3.1** | Direct and alternating potential difference | base |
| 8463 | **4.2.3.1** | Direct and alternating potential difference | base |
| Supporting | 8464 6.6.1.2 / 8463 4.6.1.2 | Properties of waves (period = 1 / frequency) | base |

Spec statements (verbatim, 8463 = 8464): "Mains electricity is an ac supply. In the United Kingdom the domestic electricity supply has a frequency of 50 Hz and is about 230 V. Students should be able to explain the difference between direct and alternating potential difference."

Equation sheets (June 2026): "period = 1 / frequency, T = 1/f" printed on **both** sheets → "On the sheet" on all four routes (f = 1 ÷ T is its rearrangement).

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | dc: one direction; sources; flat trace (theory 1) | base | 6.2.3.1 | OK, one imprecise (C1) |
| R2 | ac: repeatedly reverses; sources; wave trace (theory 2) | base | 6.2.3.1 | OK |
| R3 | UK mains 50 Hz, about 230 V (theory 2; key_note; q2) | base | 6.2.3.1 | OK |
| R4 | rms 230 V, peak ~325 V (theory 2; common_mistake; key_note; q2 wx3) | none — beyond spec | — | OFF-SPEC (DAP-F1) |
| R5 | why mains is ac (theory 2; key_note) | base context (transformers 6.2.4.3) | 6.2.4.3 | IMPRECISE (DAP-F2) |
| R6 | reading a trace: period, f = 1/T (theory 3; equations; FIFA) | base | 6.6.1.2 applied to 6.2.3.1 | OK |
| R7 | peak pd = divisions × volts/div (theory 3) | none — beyond spec | — | OFF-SPEC (DAP-F1) |
| R8 | q1 (dc) | base | 6.2.3.1 | OK, usable all routes |
| R9 | q2 (50 Hz, 230 V) | base | 6.2.3.1 | OK, usable all routes |
| — | RP, `higher` | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | "DIRECT CURRENT (DC) — flows in ONE direction only; pd is constant." | IMPRECISE (minor) | The defining difference is direction: a direct pd is always in the same direction. Its size is usually steady but need not be. Spec names direct/alternating **potential difference**. | 6.2.3.1 |
| C2 | theory 1 | sources: batteries, solar cells, dc supplies | OK | — | — |
| C3 | theory 1 | dc trace = horizontal line; higher line = higher pd | OK | — | — |
| C4 | theory 2 | ac reverses direction repeatedly; mains, generators | OK | — | 6.2.3.1 |
| C5 | theory 2 | frequency = complete cycles per second (Hz) | OK | — | 6.6.1.2 |
| C6 | theory 2 | UK mains 50 Hz, ~230 V (rms) | OK / OFF-SPEC | 50 Hz, about 230 V is spec. "rms" is beyond it. | 6.2.3.1 |
| C7 | theory 2 | "Mains is AC because generators naturally produce AC, and AC is easily transformed" | IMPRECISE | Power-station generators (alternators) produce ac; a dynamo gives dc. The point that matters is that transformers only work with ac (6.2.4.3). Not required by 6.2.3.1. | 6.2.4.3 |
| C8 | theory 3 | f = 1 ÷ T; 0.02 s → 50 Hz | OK | 1 ÷ 0.02 = 50 ✓ | 6.6.1.2 |
| C9 | theory 3 | peak pd = divisions × volts/div | OFF-SPEC | Correct method, not on 8463/8464. | — |
| C10 | common_mistake | 50 Hz not 60 Hz (USA); 230 V rms, peak ~325 V | OK / OFF-SPEC | 230 × √2 = 325.3 ✓, but rms/peak is beyond spec. | — |
| C11 | key_note | as above | OK | — | — |
| C12 | FIFA | T = 0.02 s → f = 50 Hz | OK | ✓ | 6.6.1.2 |
| C13 | CFIFA Convert `[NEW]` | "Nothing to convert — T is already given in seconds (SI), and f = 1 ÷ T needs no other unit." | OK | Examined ✓. A second example should convert ms → s (20 ms = 0.020 s), the usual trace reading. | CFIFA amendment |
| C14 | q1 key | constant pd, never changes direction → direct | OK | — | 6.2.3.1 |
| C15 | q1 opt 2 / wx1 | "ac — a steady pd is the average of ac" / "An alternating pd keeps reversing direction…" | OK | Aligned. | 6.2.3.1 |
| C16 | q1 opt 3 / wx2 | "No supply — a pd that never changes cannot make a current flow" / "A constant pd still drives a current…" | OK | Aligned. | — |
| C17 | q1 opt 4 / wx3 | "Very high frequency ac" / "However fast… its pd still reverses direction" | OK | Aligned. | 6.2.3.1 |
| C18 | q2 key | 50 Hz and 230 V | OK | Spec values. | 6.2.3.1 |
| C19 | q2 opt 2 / wx1 | 60 Hz / "60 Hz is used in the USA" | OK | Aligned. | — |
| C20 | q2 opt 3 / wx2 | 110 V / "110 V is used in the USA" | OK | Aligned (US nominal 120 V; 110–120 V is fair). | — |
| C21 | q2 opt 4 / wx3 | 325 V / "325 V is the PEAK voltage — 230 V is the quoted rms (effective) value." | OK / OFF-SPEC | True; aligned. Uses beyond-spec terms in feedback only — the item itself tests the spec values. | — |
| C22 | matching (to be replaced) | DC/AC descriptions | OK | — | — |

Count: **0 WRONG**. OFF-SPEC: C6 (rms), C9, C10, C21 (feedback). IMPRECISE: C1, C7. Arithmetic ✓.

## 4. Frozen items wrong for their route
None. q1 and q2 usable on all four routes.

## 5. For the lesson author
**Misconceptions seen in AQA marking:** "ac changes size, dc doesn't" with no mention of direction (does not score — the mark is for direction); "alternating current goes round and comes back" (charges oscillate); UK mains 240 V/110 V/60 Hz; batteries are ac.

**Typical questions** ⚑ examiner-drafted
- *Explain the difference between direct and alternating potential difference. [2]* — direct: always in the same direction (1); alternating: continually/repeatedly changes direction (1).
- *Give the frequency and pd of the UK mains supply. [2]* — 50 Hz (1); 230 V (1).
- *One cycle on the trace takes 20 ms. Calculate the frequency. [2]* — T = 0.020 s, f = 1 ÷ 0.020 (1); 50 Hz (1).

## 6. Verdict
SOURCE OK WITH FLAGS. Spec core all present and right. Strip rms/peak and volts-per-division; keep direction as the defining difference. Both quiz items usable. Nothing for Mide.
