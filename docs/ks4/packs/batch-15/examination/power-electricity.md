# Examination — Power (power-electricity) — AQA 8464 6.2.4.1 / 8463 4.2.4.1
Verdict: SOURCE OK WITH FLAGS (fuse selection is beyond the spec, so q2 is not usable; E = Pt and E = QV belong to 6.2.4.2)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.4.1-power-electricity.md`.
Spec sources read: `AQA-8464-spec.txt` §6.2.4.1, §6.2.4.2, §6.2.1.3; `AQA-8463-spec.txt` §4.2.4.1, §4.2.4.2. Both June 2026 equation sheets. Route audit row `power-electricity` (base / base). Neighbour read: batch-3 `power` examination (6.1.1.4, mechanical power).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both). All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.2.4.1** | Power | base |
| 8463 | **4.2.4.1** | Power | base |
| Supporting | 8464 6.2.4.2 / 8463 4.2.4.2 (E = Pt, E = QV); 6.2.1.3 / 4.2.1.3 (V = IR) | | base |

Spec statements (verbatim, 8463 = 8464): "Students should be able to explain how the power transfer in any circuit device is related to the potential difference across it and the current through it, and to the energy changes over time: power = potential difference × current  P = V I; power = (current)² × resistance  P = I² R" — "Students should be able to recall and apply both equations." Units W, V, A, Ω. MS 3b, c; WS 4.5.

Equation sheets (June 2026): P = V I, P = I² R, E = P t, E = Q V all printed on **both** the 8464 and the 8463 sheet → "On the sheet" on all four routes. None is HT.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | electrical power = rate of energy transfer (theory 1) | base | 6.2.4.1 | OK |
| R2 | P = VI, P = I²R; when to use each (theory 1; equations; variables; key_note) | base | 6.2.4.1 | OK |
| R3 | check: R = V/I then P = I²R (theory 1) | base | 6.2.4.1 + 6.2.1.3 | OK (a two-equation chain) |
| R4 | E = Pt, E = VQ; examples (theory 2; equations; key_note) | base | **6.2.4.2** | OK — owned by `energy-transfers-appliances`; link only |
| R5 | I = P ÷ V (theory 3; common_mistake; key_note) | base | 6.2.4.1 (rearranged) | OK |
| R6 | choosing a fuse rating (theory 3; key_note; matching; q2) | none — beyond spec | — | OFF-SPEC (PE-F1) |
| R7 | P = I²R not I × R² (common_mistake; q1) | base | 6.2.4.1 | OK |
| R8 | FIFA P = 240 × 0.25 | base | 6.2.4.1 | OK |
| R9 | q1 | base | 6.2.4.1 | OK, usable all routes |
| R10 | q2 | beyond spec | — | not usable (PE-F1) |
| — | RP, `higher` | none | — | correct: 6.2.4.1 has no HT and no physics-only content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | electrical power = rate of energy transfer by a component | OK | — | 6.2.4.1 |
| C2 | theory 1; equations; variables | P = V × I; P = I² × R; W, V, A, Ω | OK | — | 6.2.4.1 |
| C3 | theory 1 | 12 V, 2 A → 24 W; R = 6 Ω; 2² × 6 = 24 W | OK | All ✓ | — |
| C4 | theory 2 | E = P × t (J, s); E = V × Q | OK | Spec writes E = QV. | 6.2.4.2 |
| C5 | theory 2 | 60 W for 5 min → 60 × 300 = 18,000 J | OK | ✓ | 6.2.4.2 |
| C6 | theory 2 | 150 C through 12 V → 1800 J | OK | ✓ | 6.2.4.2 |
| C7 | theory 3 | I = P ÷ V; fuse just above; 1, 3, 5, 13 A | OK / OFF-SPEC | I = P ÷ V is on spec; fuse choice is not on 8463/8464. | — |
| C8 | theory 3 | 500 W at 230 V → ≈ 2.2 A → 3 A fuse | OK / OFF-SPEC | 500 ÷ 230 = 2.17 ✓ | — |
| C9 | theory 3 | 2300 W at 230 V → 10 A → 13 A fuse | OK / OFF-SPEC | ✓ | — |
| C10 | common_mistake | current is squared, not R; I = P ÷ V | OK | — | 6.2.4.1 |
| C11 | key_note | P = VI. P = I²R. E = Pt. E = VQ. UK mains 230 V | OK | — | — |
| C12 | FIFA | 240 V, 0.25 A → 60 W | OK | 240 × 0.25 = 60 ✓. 240 V is a lamp rating, not a claim about UK mains (230 V). | 6.2.4.1 |
| C13 | CFIFA Convert `[NEW]` | "Nothing to convert — V and I are both already given in SI units (volts, amps)." | OK | Examined ✓. A second example should convert mA → A or kW → W. | CFIFA amendment |
| C14 | q1 key | 3 A, 8 Ω → 9 × 8 = 72 W | OK | ✓ | 6.2.4.1 |
| C15 | q1 opt 2 / wx1 | "24 W — P = I × R" / "P = I × R gives volts (A × Ω = V)" | OK | Aligned. | 6.2.1.3 |
| C16 | q1 opt 3 / wx2 | "576 W — I² × R²" / "Only CURRENT is squared" | OK | Aligned; 9 × 64 = 576 ✓ | — |
| C17 | q1 opt 4 / wx3 | "2.67 W — P = R ÷ I" / "R ÷ I gives Ω/A" | OK | Aligned; 8 ÷ 3 = 2.67 ✓ | — |
| C18 | q2 key | 1380 ÷ 230 = 6 A → 13 A fuse | OK / OFF-SPEC | Arithmetic ✓. Fuse choice beyond spec. | — |
| C19 | q2 wx1–wx3 | 3 A, 5 A, 1 A would blow | OK | All aligned to options 2–4. | — |
| C20 | matching (to be replaced) | 24 W ✓; 10² × 1 = 100 W ✓; 690 W → 3 A → "3 A fuse"; 2300 W → 13 A | IMPRECISE / OFF-SPEC | A 3 A operating current on a 3 A fuse contradicts the source's own "just above" rule. Replaced anyway. | — |

Count: **0 WRONG**. OFF-SPEC: fuse selection (C7–C9, C18, C20). All arithmetic ✓ (11 calculations rechecked).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | correct; base | Usable on all four routes. |
| q2 | arithmetic right, but the item tests choosing a fuse rating — not on 8463/8464 | Not usable as a rung. The I = P ÷ V step is good on-spec practice — Design writes it fresh without a fuse. |

## 5. For the lesson author
**Not to be confused with** batch-3 `power` (6.1.1.4, P = E/t, P = W/t). This lesson is circuit power.

**Misconceptions seen in AQA marking:** P = I × R² or (I × R)²; squaring before vs after multiplying (I²R with I = 0.5 A); mA left unconverted; "power is the energy" (power is the rate); "a bigger resistance always means more power" (true at fixed I, false at fixed V).

**Typical questions** ⚑ examiner-drafted
- *Write down the equation that links current, power and resistance. [1]* — P = I²R.
- *A heater has a resistance of 24 Ω and a current of 10 A. Calculate its power. [2]* — 10² × 24 (1); 2400 W (1).
- *A 230 V kettle has a power of 2.3 kW. Calculate the current. [3]* — 2300 W (1); I = 2300 ÷ 230 (1); 10 A (1).
- *A 6.0 V lamp has a resistance of 12 Ω. Calculate its power. [3]* — Step 1 I = 6.0 ÷ 12 = 0.50 A (1); Step 2 P = 6.0 × 0.50 (1); 3.0 W (1).

## 6. Verdict
SOURCE OK WITH FLAGS. Both spec equations correct, every number checks. Fuse selection is beyond spec and q2 should not be used. E = Pt and E = QV are `energy-transfers-appliances`' to teach. Nothing for Mide.
