# Examination — Development of the Periodic Table (development-periodic-table) — AQA 8464 5.1.2.2 / 8462 4.1.2.2
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-4/04-checked-science-source/chemistry-5.1.2.2-development-periodic-table.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.1.1.4–5.1.1.6, 5.1.2.2; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.1.2.2. Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `development-periodic-table` (base, CF CH TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). T1–T3 = theory chunks. No route copies; no `higher` field.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.1.2.2** | Development of the periodic table | base |
| 8462 | **4.1.2.2** | Development of the periodic table | base |
| Supporting | 8464 5.1.1.5 / 8462 4.1.1.5 isotopes; 5.1.1.6 / 4.1.1.6 relative atomic mass | | base |

Spec statement (verbatim, 8464 = 8462): "Before the discovery of protons, neutrons and electrons, scientists attempted to classify the elements by arranging them in order of their atomic weights. The early periodic tables were incomplete and some elements were placed in inappropriate groups if the strict order of atomic weights was followed. Mendeleev overcame some of the problems by leaving gaps for elements that he thought had not been discovered and in some places changed the order based on atomic weights. Elements with properties predicted by Mendeleev were discovered and filled the gaps. Knowledge of isotopes made it possible to explain why the order based on atomic weights was not always correct. Students should be able to describe these steps in the development of the periodic table." Skills: WS 1.1, 1.6 — "Explain how testing a prediction can support or refute a new scientific idea."

The spec names no scientist except Mendeleev. Newlands and Moseley are legitimate context (AQA papers have used Newlands as "an early periodic table").

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Before subatomic particles, elements ordered by atomic weight (T1) | base | 5.1.2.2 | all four | OK |
| R2 | Newlands' octaves and their limits (T1; key_note; q1) | base (context: "early periodic tables") | 5.1.2.2 | all four | OK in T1; q1 wx3 WRONG (C17) |
| R3 | Early tables incomplete, elements in inappropriate groups (T1) | base | 5.1.2.2 | all four | OK |
| R4 | Mendeleev: gaps; changed order against atomic weight (T1, T3) | base | 5.1.2.2 | all four | OK |
| R5 | Predicted elements discovered: Ga, Sc, Ge (T1, T3; q2) | base | 5.1.2.2 | all four | OK |
| R6 | Testing a prediction supports an idea (T3) | base | WS 1.1, 1.6 | all four | OK |
| R7 | Moseley, atomic number (T2; key_note) | base (context) | 5.1.2.1 | all four | OK |
| R8 | Noble gases discovered later, fit as Group 0 (T2) | base (context) | — | all four | OK |
| R9 | **Isotopes explain why atomic-weight order was not always correct** | base | 5.1.2.2 | — | **GAP — not in the source** (C11) |
| R10 | common_mistake: Mendeleev by Ar, modern by atomic number | base | 5.1.2.1–2 | all four | IMPRECISE example (C13) |
| R11 | q1 | base | 5.1.2.2 | all four | WRONG wx3 (C17) |
| R12 | q2 | base | 5.1.2.2 | all four | OK |
| — | RP, FIFA, equations, `higher`, examiner_tip | none | — | — | correct: 5.1.2.2 has no HT or separate-science content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | early classification by relative atomic mass, before atomic numbers known | OK | Spec: "atomic weights". | 5.1.2.2 |
| C2 | T1 | Newlands, Law of Octaves, 1864 | OK | First noted 1864, set out as the "law of octaves" 1865. Either date is acceptable. | — |
| C3 | T1 | every 8th element similar; limits: only worked for the first 16 elements; forced elements into groups; no gaps; not accepted | OK | "Worked only for the lighter elements (up to calcium)" is the usual mark-scheme phrasing; "first 16" is acceptable. | 5.1.2.2 |
| C4 | T1 | Mendeleev 1869, by Ar, left gaps, predicted properties | OK | — | 5.1.2.2 |
| C5 | T1 | rearranged some elements, chemical properties above strict Ar order | OK | Spec: "in some places changed the order based on atomic weights". The classic example is tellurium (Ar 127.6) before iodine (Ar 126.9). | 5.1.2.2 |
| C6 | T1 | eka-silicon = germanium, discovered 1886, matched predictions | OK | (Winkler, 1886.) | 5.1.2.2 |
| C7 | T2 | Moseley 1913, X-ray experiments, atomic numbers | OK | — | — |
| C8 | T2 | arranging by atomic number resolved inconsistencies "where some elements seemed in the wrong order" | OK | — | — |
| C9 | T2 | atomic number (protons = electrons) determines chemical properties | OK | Strictly, the arrangement of electrons does; the number follows from atomic number. Fine. | 5.1.2.1 |
| C10 | T2 | argon 1894; noble gases discovered after Mendeleev's table; fitted as Group 0 | OK | (Rayleigh and Ramsay, 1894.) | — |
| C11 | — | isotopes | **GAP** | The spec's own explanation of why atomic-weight order was sometimes wrong is isotopes, and the source never mentions it. Needed: relative atomic mass is a mean of the masses of an element's isotopes, weighted by abundance, so an element with fewer protons can have a higher Ar if its heavier isotopes are more common — e.g. argon (18 protons, Ar 39.9) before potassium (19 protons, Ar 39.1); tellurium (52, Ar 127.6) before iodine (53, Ar 126.9). See source's "Spec core missing" section. | 5.1.2.2; 5.1.1.5–6 |
| C12 | T3 | eka-aluminium = gallium; eka-silicon = germanium; eka-boron = scandium; matched predictions | OK | Ga 1875, Sc 1879, Ge 1886. | 5.1.2.2 |
| C13 | common_mistake | "Mendeleev's arrangement had a few inconsistencies … (e.g. argon and potassium)" | IMPRECISE | Argon was unknown in 1869, so it was never in Mendeleev's table. Mendeleev's own swap was **tellurium and iodine**. Argon/potassium is the standard example of the atomic-weight order going wrong in the *modern* table — the isotope example. Re-cut: "Mendeleev swapped some pairs, e.g. tellurium and iodine, to keep groups right; argon and potassium show the same problem." | 5.1.2.2 |
| C14 | key_note | Newlands rejected; Mendeleev gaps, accepted; modern by atomic number (Moseley 1913) | OK | Should also say isotopes explain the out-of-order pairs. | 5.1.2.2 |
| C15 | q1 key | only worked for first 16 elements; forced elements into groups regardless of properties | OK | ✓ | 5.1.2.2 |
| C16 | q1 wx1, wx2 | Newlands used relative atomic mass; presented to the Chemical Society, 1866 | OK | (1 March 1866 ✓.) | — |
| C17 | q1 wx3 | "Not leaving gaps was a problem for **Mendeleev too initially** — but the bigger issue for Newlands was that his pattern broke down after the first 16 elements." | **WRONG** | Mendeleev's defining step was **leaving** gaps (spec). He never had a "no gaps" problem. The distractor it explains ("Newlands did not leave gaps — but neither did he need to") is also half-true: its first clause is a correct reason for rejection, which the source's own T1 and key_note list. Do not use as written. | 5.1.2.2 |
| C18 | q2 key | predicted properties of undiscovered elements; predictions accurate | OK | Exactly the spec's point and WS 1.1. | 5.1.2.2 |
| C19 | q2 wx1–wx3 | Newlands also by mass; noble gases discovered by others (Ramsay) later; evidence and prediction, not simplicity | OK | — | — |

Count: **1 WRONG** (C17, frozen quiz q1). GAP: C11. IMPRECISE: C13. No calculations; no Convert lines.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx3 says Mendeleev also failed to leave gaps "initially" — false; the option it explains is half-true | **Do not use as written** on any route. |
| q2 | correct, base | **Usable on all four routes.** |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Mendeleev arranged elements by atomic number" — by atomic weight; atomic number came later.
- "Gaps were mistakes / elements he forgot" — they were deliberate, for undiscovered elements.
- "Mendeleev was accepted because his table included every element."
- "Mendeleev used protons/electrons" — they were not yet discovered.
- Isotopes ignored: pupils cannot say why Ar/K or Te/I are out of mass order.

**Command words**: Describe (the steps); Explain why … was accepted; Explain how … supports …; Suggest why.

**Typical questions** ⚑ examiner-drafted
- *Give two ways Mendeleev's table differed from earlier tables. [2]* — left gaps for undiscovered elements (1); changed the order of some elements away from atomic weight order (1).
- *Explain why Mendeleev's table came to be accepted. [2]* — elements he predicted were discovered (1); their properties matched his predictions (1).
- *Iodine has a lower relative atomic mass than tellurium but comes after it. Explain why, using ideas about atomic structure. [3]* — elements ordered by atomic/proton number (1); iodine has more protons (1); relative atomic mass depends on the isotopes and their abundance (1).

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE HAS ERRORS. History and dates are correct; q2 is good on all routes. But the spec's key explanatory step — isotopes explain why atomic-weight order was not always right — is missing; frozen q1's wx3 is false; the common_mistake's argon/potassium example is historically misplaced for Mendeleev.

**For Mide:** nothing. All points are settled science.
