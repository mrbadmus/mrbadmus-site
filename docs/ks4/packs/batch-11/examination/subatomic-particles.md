# Examination — Subatomic Particles (subatomic-particles) — AQA 8464 5.1.1.4–5.1.1.5 / 8462 4.1.1.4–4.1.1.5
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.1.1.4-subatomic-particles.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.1.1.1, 5.1.1.4, 5.1.1.5, 6.4.1.1–6.4.1.2; `AQA-8462-spec.txt` (v1.1) 4.1.1.1, 4.1.1.4, 4.1.1.5. The spec's charge and mass tables are images that do not survive in the text. Their content is the standard AQA table: proton +1 / 1; neutron 0 / 1; electron −1 / very small. Route audit row `subatomic-particles`: base, OK. Physics twin read for overlap: `batch-5` `structure-of-atom` (8464 6.4.1.1; 8463 4.4.1.1).

Conventions: as in model-of-the-atom. No route copy differs.

**Overlap with physics.** Physics `structure-of-atom` (8464 6.4.1.1) covers the nuclear model, scale, and electrons moving between energy levels by absorbing or emitting EM radiation. This chemistry page should be built on the particle table (charge, mass, where each particle is) and on **ions**: counting protons, neutrons and electrons in an atom or ion. Scale gets a short section here, not the flagship. See the brief.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.1.1.4** | Relative electrical charges of subatomic particles | base |
| 8464 | **5.1.1.5** | Size and mass of atoms | base |
| 8462 | **4.1.1.4**, **4.1.1.5** | same titles, same text | base |
| Supporting | 8464 5.1.1.1 / 8462 4.1.1.1 "(HT only) write balanced half equations and ionic equations" | | HT |
| Twin (physics) | 8464 6.4.1.1–6.4.1.2; 8463 4.4.1.1–4.4.1.2 | | base |

Spec statements (verbatim, 8464 = 8462):
- 5.1.1.4: "The relative electrical charges of the particles in atoms are: [table: proton +1; neutron 0; electron −1]. In an atom, the number of electrons is equal to the number of protons in the nucleus. Atoms have no overall electrical charge. The number of protons in an atom of an element is its atomic number. All atoms of a particular element have the same number of protons. Atoms of different elements have different numbers of protons. Students should be able to use the nuclear model to describe atoms."
- 5.1.1.5: "Atoms are very small, having a radius of about 0.1 nm (1 x 10-10 m). The radius of a nucleus is less than 1/10 000 of that of the atom (about 1 x 10-14 m). Almost all of the mass of an atom is in the nucleus. The relative masses of protons, neutrons and electrons are: [table: 1; 1; very small]. The sum of the protons and neutrons in an atom is its mass number. Atoms of the same element can have different numbers of neutrons; these atoms are called isotopes of that element. Atoms can be represented as shown in this example: [²³₁₁Na]. Students should be able to calculate the numbers of protons, neutrons and electrons in an atom or ion, given its atomic number and mass number. Students should be able to relate size and scale of atoms to objects in the physical world."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | p, n, e: charge, relative mass, location (th1; key_note) | base | 5.1.1.4; 5.1.1.5 | all four | OK; "every atom has three" IMPRECISE (F1); electron mass wording (F5) |
| R2 | Neutral atom: protons = electrons (th1; q2) | base | 5.1.1.4 | all four | OK |
| R3 | Almost all mass in the nucleus (th1; common_mistake) | base | 5.1.1.5 | all four | OK |
| R4 | Ions: lose electrons → positive, gain → negative; count electrons (th2; q1) | base | 5.1.1.5 ("atom or ion"); 5.2.1.2 | all four | OK |
| R5 | Ion formation written as half equations (Na → Na⁺ + e⁻ etc.) (th2) | **higher** | 5.1.1.1 (HT only) | all four | ROUTE (F3) |
| R6 | Protons unchanged in a chemical reaction (th2; common_mistake) | base | 5.1.1.4 | all four | OK |
| R7 | Atomic radius 0.1 nm; nucleus 1 × 10⁻¹⁴ m; mostly empty space (th3) | base | 5.1.1.5 | all four | IMPRECISE (F2) |
| R8 | Scale to everyday objects: hair, sand (th3) | base | 5.1.1.5 (MS 1d) | all four | OK |
| R9 | Calculate p, n, e in an atom **or ion** from atomic and mass number | base | 5.1.1.5 | — | GAP (F4) |
| R10 | q1 electrons in Mg²⁺ | base | 5.1.1.5 | all four | OK |
| R11 | q2 why an atom is neutral | base | 5.1.1.4 | all four | OK |
| — | FIFA, equations, RP, `higher` | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | "Every atom contains three types of subatomic particle" | IMPRECISE | Hydrogen-1, the most common atom, has no neutron (F1). | 5.1.1.5 |
| C2 | th1 | proton +1, 1, nucleus; neutron 0, 1, nucleus | OK | — | 5.1.1.4–5 |
| C3 | th1 | electron −1, "approximately 1/1836 — effectively 0" | IMPRECISE (minor) | 1/1836 is right. The spec's word is "very small", so teach that. "0" as an exam answer risks losing the mark (F5). | 5.1.1.5 |
| C4 | th1 | atoms neutral because protons = electrons | OK | — | 5.1.1.4 |
| C5 | th1 | almost all mass in the nucleus; electrons negligible | OK | — | 5.1.1.5 |
| C6 | th2 | ion = charged particle from gaining or losing electrons | OK | — | 5.2.1.2 |
| C7 | th2 | Na → Na⁺ + e⁻; Mg → Mg²⁺ + 2e⁻ | OK (HT form) | Correct half equations. Writing them is HT only (F3). | 5.1.1.1 |
| C8 | th2 | Cl + e⁻ → Cl⁻; O + 2e⁻ → O²⁻ | OK (HT form), IMPRECISE | Fine as atom-level pictures. As full HT half equations chlorine and oxygen are diatomic: Cl₂ + 2e⁻ → 2Cl⁻; O₂ + 4e⁻ → 2O²⁻ (F3). | 5.1.1.1 |
| C9 | th2 | cation/anion | OK, context | These terms are not in the AQA spec. | — |
| C10 | th2 | charge tells how many electrons were gained or lost; protons never change in a chemical reaction | OK | — | 5.1.1.4 |
| C11 | th3 | cannot be seen with a light microscope | OK | — | — |
| C12 | th3 | radius ≈ 1 × 10⁻¹⁰ m (0.1 nm) | OK | Spec value. | 5.1.1.5 |
| C13 | th3 | human hair ≈ 1 million atoms wide | OK (order of magnitude) | Hair is 50–100 µm and an atom's diameter is about 2 × 10⁻¹⁰ m, giving 2.5–5 × 10⁵ atoms. "About a million" is the right order of magnitude. | MS 1d |
| C14 | th3 | grain of sand ≈ 10¹⁸ atoms | OK (order of magnitude) | A 0.5 mm grain of SiO₂ holds about 5 × 10¹⁸ atoms; a 1 mm grain about 4 × 10¹⁹. "About 10¹⁸–10¹⁹" is safer. | MS 1d |
| C15 | th3; common_mistake | "nucleus… about 10,000 times smaller than the whole atom" | IMPRECISE | The spec says "the **radius** of a nucleus is less than 1/10 000 of that of the atom". By volume the nucleus is about 10¹² times smaller. Say "radius" (F2). | 5.1.1.5 |
| C16 | th3 | nuclear radius ≈ 1 × 10⁻¹⁴ m | OK | — | 5.1.1.5 |
| C17 | th3 | consistent with Rutherford: most alphas pass through | OK | Links back to 5.1.1.3. | 5.1.1.3 |
| C18 | common_mistake | protons never change; electrons negligible mass; mostly empty space | OK, except the "10,000 times smaller" wording (C15) | — | — |
| C19 | key_note | proton +1/1; neutron 0/1; electron −1/~0; ions | OK | Say "very small" rather than "~0" (C3). | 5.1.1.5 |
| C20 | matching (to be replaced) | Na⁺ 11p 10e; Cl⁻ 17p 18e | OK | ✓ | — |
| C21 | q1 key (opt 0) | Mg²⁺ has 10 electrons (12 − 2) | OK | ✓ | 5.1.1.5 |
| C22 | q1 wx1 ↔ opt 1 "14 — gains 2" | gaining electrons makes a negative ion; Mg²⁺ is positive | OK, aligned ✓ | — | — |
| C23 | q1 wx2 ↔ opt 2 "12 — stays the same" | Mg²⁺ forms by losing 2: 12 − 2 = 10 | OK, aligned ✓ | — | — |
| C24 | q1 wx3 ↔ opt 3 "2 — only outermost remain" | only the 2 outer electrons are lost; 10 remain | OK, aligned ✓ | — | — |
| C25 | q2 key (opt 0) | protons (+1 each) = electrons (−1 each) | OK | Spec. | 5.1.1.4 |
| C26 | q2 wx1 ↔ opt 1 "protons and neutrons cancel" | neutrons have zero charge | OK, aligned ✓ | — | — |
| C27 | q2 wx2 ↔ opt 2 "electrons shield the nucleus" | shielding is about attraction on outer electrons, not neutrality | OK, aligned ✓ | "Shielding" is not in the GCSE spec, but the statement is true. | — |
| C28 | q2 wx3 ↔ opt 3 "atom vibrates too fast" | vibration does not affect charge | OK, aligned ✓ | — | — |

Count: **0 WRONG**. IMPRECISE: C1, C3, C8, C15. ROUTE: C7–C8 (half equations are HT). GAP: R9. All six wrong_explanations are aligned, checked by reading each one.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | — | Usable on all four routes. |
| q2 | — | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- Electron count for an ion read straight off the atomic number, i.e. charge ignored. q1 is the archetype.
- "A positive ion has gained protons." It has lost electrons; the proton number never changes.
- Neutrons given a charge, or "protons and neutrons cancel".
- "Electron relative mass = 0" or "1/2000 of a gram": the spec word is "very small".
- Neutrons counted as mass number minus electrons, which fails for an ion. Use mass number − atomic number.
- "The nucleus is 10 000 times smaller" without saying it is the **radius**.

**Command words**: Complete the table (charge/mass), Calculate the number of protons, neutrons and electrons, Explain why an atom has no overall charge, Give the radius of an atom.

**Typical questions** ⚑ examiner-drafted
- *Complete the table of relative charge and relative mass for the proton, neutron and electron. [3]*
- *An aluminium ion is ²⁷₁₃Al³⁺. Give the number of protons, neutrons and electrons in the ion. [3]*: 13 (1); 14 (1); 10 (1).
- *Explain why an atom has no overall charge. [2]*: number of protons = number of electrons (1); proton charge +1 and electron −1, so they cancel (1).
- *The radius of an atom is 1 × 10⁻¹⁰ m. The nucleus is about 1/10 000 of this. Give the radius of the nucleus. [1]*: 1 × 10⁻¹⁴ m.

**Required practical**: none. **Equations**: none. This is counting: neutrons = mass number − atomic number; electrons in an ion = protons − charge.

## 6. Verdict
SOURCE OK WITH FLAGS. No wrong science and both frozen items usable on all four routes. Theory imprecisions: "every atom has three particles"; "10 000 times smaller" without "radius"; electron mass "effectively 0". The half equations are HT. Gap: no worked case of p/n/e for an ion given its mass number, which the spec names directly.

**For Mide:** nothing.
