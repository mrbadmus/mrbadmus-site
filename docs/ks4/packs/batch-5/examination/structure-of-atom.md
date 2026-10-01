# Examination — The Structure of an Atom (structure-of-atom) — AQA 8464 6.4.1.1 / 8463 4.4.1.1
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/physics-6.4.1.1-structure-of-atom.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.4.1.1–6.4.1.2 and §5.1.1.4–5.1.1.5, 5.1.1.7 (chemistry); `AQA-8463-spec.txt` (v1.1) §4.4.1.1–4.4.1.2; `AQA-8462-spec.txt` §4.1.1.4–4.1.1.7. Equation sheets: none apply. Route audit row `structure-of-atom` (base / base, OK).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. No route copies differ; no `[NEW — to be examined]` lines (no fifas).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.4.1.1** | The structure of an atom | base |
| 8463 | **4.4.1.1** | The structure of an atom | base |
| Supporting | 8464 6.4.1.2 / 8463 4.4.1.2 (electrons = protons; no overall charge); chemistry 8464 5.1.1.4–5.1.1.5, 5.1.1.7 / 8462 4.1.1.4–4.1.1.5, 4.1.1.7 (relative charges and masses; nucleus ~1 × 10⁻¹⁴ m; electronic structure) | | base |

Spec statements (verbatim, 8463 = 8464): "Atoms are very small, having a radius of about 1 × 10⁻¹⁰ metres. The basic structure of an atom is a positively charged nucleus composed of both protons and neutrons surrounded by negatively charged electrons. The radius of a nucleus is less than 1/10 000 of the radius of an atom. Most of the mass of an atom is concentrated in the nucleus. The electrons are arranged at different distances from the nucleus (different energy levels). The electron arrangements may change with the absorption of electromagnetic radiation (move further from the nucleus; a higher energy level) or by the emission of electromagnetic radiation (move closer to the nucleus; a lower energy level)." MS 1b: "recognise expressions given in standard form." 6.4.1.2: "In an atom the number of electrons is equal to the number of protons in the nucleus. Atoms have no overall electrical charge."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Atom radius ~1 × 10⁻¹⁰ m; nucleus of p + n, electrons around (T1; key_note) | base | 6.4.1.1 | all four | OK |
| R2 | Nucleus radius < 1/10 000 atom; mostly empty space (T1; key_note; matching) | base | 6.4.1.1 | all four | IMPRECISE ("≈", F3) |
| R3 | Relative charge/mass of p, n, e (T2; key_note; matching) | base | chem 5.1.1.4–5.1.1.5 | all four | IMPRECISE ("amu", F2) |
| R4 | Mass concentrated in nucleus (T2; common_mistake; q1) | base | 6.4.1.1 | all four | OK |
| R5 | Electrons = protons in neutral atom (T2; q2) | base | 6.4.1.2 | all four | OK |
| R6 | Shells 2, 8, 8; groups; bonding (T3 middle) | base — chemistry 5.1.1.7, not this page's spec | — | all four | OFF-SPEC for this page (F4) |
| R7 | Absorb EM radiation → higher level; emit → lower level (T3 end) | base | 6.4.1.1 | all four | OK |
| — | rp, higher, equations, fifas | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | radius ~1 × 10⁻¹⁰ m = 0.1 nm | OK | — | 6.4.1.1; 5.1.1.5 |
| C2 | T1 | nucleus of protons and neutrons; electrons orbit at different distances (energy levels) | OK | — | 6.4.1.1 |
| C3 | T1; key_note | "Nuclear radius ≈ 1/10,000 of the atomic radius" | IMPRECISE | Spec: "less than 1/10 000". | 6.4.1.1 |
| C4 | T1 | nuclear radius ~1 × 10⁻¹⁴ m | OK | Chemistry spec: "(about 1 x 10⁻¹⁴ m)". | 5.1.1.5 |
| C5 | T1 | football 30 cm → atom ~3 km | OK | 0.3 m × 10 000 = 3000 m ✓ (diameter to diameter). | — |
| C6 | T2 | proton mass 1, charge +1; neutron 1, 0; electron ~1/1836, −1 | IMPRECISE | Values right; AQA wording is "relative mass" and "relative charge"; electron "very small" (1/1836 is fine as enrichment). "amu" is not AQA's term. | 5.1.1.4–5.1.1.5 |
| C7 | T2 | protons = electrons in a neutral atom; no overall charge | OK | — | 6.4.1.2 |
| C8 | T2 | almost all mass in nucleus | OK | — | 6.4.1.1 |
| C9 | T3 | shells 2, 8, 8 for elements 1–20; H 1; C 2,4; Na 2,8,1 | OK (chemistry) | Correct; this is 5.1.1.7, not 6.4.1.1. | 5.1.1.7 |
| C10 | T3 | arrangement determines chemical properties; outer electrons bond; same group = same outer electrons | OK (chemistry) | 5.1.2.x content. | 8464 5.1.2 |
| C11 | T3 | absorb energy → higher shell; release → lower shell emitting EM radiation | OK | Spec says absorption/emission of EM radiation. | 6.4.1.1 |
| C12 | common_mistake | nucleus = p + n, not e; mass from nucleus | OK | — | 6.4.1.1 |
| C13 | key_note | as above; "Shells: 2, 8, 8…" | OK | Shells = chemistry (C9). | — |
| C14 | matching (to be replaced) | four pairs | OK | Same "amu" / "~1/10,000" wording as C3, C6. | — |
| C15 | q1 key | mass in nucleus | OK | — | 6.4.1.1 |
| C16 | q1 wx1 | "There are often as many electrons as protons, but each electron weighs ~1/1836 of a proton" | OK | ("always" in a neutral atom; harmless). | 6.4.1.2 |
| C17 | q1 wx2 | mass concentrated in tiny nucleus | OK | — | — |
| C18 | q1 wx3 | "Outer electrons have even less mass than inner ones" | **WRONG** | All electrons have identical mass wherever they are. | — |
| C19 | q2 key | 8 protons → 8 electrons | OK | — | 6.4.1.2 |
| C20 | q2 wx1–wx3 | pairing; half; removing electrons → positive ion | OK | — | 6.4.1.2 |

Count: **1 WRONG** (C18, q1 wx3); IMPRECISE C3, C6; chemistry content C9–C10 (off this page's spec, correct).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx3 states a false fact (outer electrons lighter) | Do not use as written (STRUCTURE-OF-ATOM-F1). Key and options are fine; usable once wx3 is replaced. |
| q2 | — | Usable on all four routes. |

## 5. Verdict
SOURCE HAS ERRORS (one false wrong-answer explanation). Theory science is correct; wording should follow AQA ("relative mass/charge", "less than 1/10 000"). Shell-filling is chemistry content riding on a physics page.

**For Mide:** nothing.
