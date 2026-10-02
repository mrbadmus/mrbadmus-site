# Examination — Changes of State (changes-of-state) — AQA 8464 6.3.1.2 / 8463 4.3.1.2
Verdict: SOURCE OK WITH FLAGS (no WRONG item; four theory/feedback imprecisions)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.3.1.2-changes-of-state.md`.
Spec sources read: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §6.3.1.1, §6.3.1.2, §6.3.2.1; `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.3.1.1, §4.3.1.2, §4.3.2.1, §4.3.2.3. No equation applies. Route audit `physics.md` row `changes-of-state`; `site-routes.tsv` neighbours `internal-energy` (6.3.2.1) and `specific-latent-heat` ("Changes of State and Specific Latent Heat", 6.3.2.3).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (option 0 is the key on both items). All four route copies identical.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.3.1.2** | Changes of state | base |
| 8463 | **4.3.1.2** | Changes of state | base |
| Supporting | 8464 6.3.1.1 / 8463 4.3.1.1 | particle model of solids, liquids, gases | base; lesson `density-of-materials` |
| Neighbours (keep distinct) | 6.3.2.1 / 4.3.2.1 internal energy; 6.3.2.3 / 4.3.2.3 specific latent heat | | base; batch 2 `internal-energy`, batch 3 `specific-latent-heat` |

Spec statements (verbatim, 8464 = 8463): "Students should be able to describe how, when substances change state (melt, freeze, boil, evaporate, condense or sublimate), mass is conserved. Changes of state are physical changes which differ from chemical changes because the material recovers its original properties if the change is reversed."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Names: melt, freeze, boil/evaporate, condense, sublimate (+ deposition) (theory 1; key_note) | base | 6.3.1.2 (deposition beyond spec, harmless) | OK |
| R2 | Energy supplied / removed for each change (theory 1) | base | 6.3.2.1 (heating → change of state) | OK; keep to one line — internal energy is the neighbour's |
| R3 | Mass conserved; particles neither made nor destroyed; 100 g ice → 100 g water (theory 1; common_mistake; key_note; q1) | base | 6.3.1.2 | OK |
| R4 | Physical not chemical; reversible; recovers original properties (theory 2; common_mistake; q2) | base | 6.3.1.2 | OK; one imprecision (C6) |
| R5 | Burning wood as a contrasting chemical change (theory 2) | base (context) | — | OK |
| R6 | Particle arrangement and motion in solid, liquid, gas (theory 3) | base | 6.3.1.1 | OK; imprecise force wording (C8) |
| R7 | Particle account of melting and boiling (theory 3) | base | 6.3.1.1; 6.3.2.1 | IMPRECISE on boiling (C10) |
| R8 | q1 (200 g water freezes) | base | 6.3.1.2 | OK; usable all four routes |
| R9 | q2 (melting is physical) | base | 6.3.1.2 | OK; usable all four routes |
| — | RP, equations, fifas, `higher` | none | — | correct: 6.3.1.2 has no HT, no equation, no RP |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | six changes with names and energy direction | OK | Spec lists five + sublimate; "deposition" is extra, correct. | 6.3.1.2 |
| C2 | theory 1 | no particles created or destroyed; total mass unchanged | OK | — | 6.3.1.2 |
| C3 | theory 1 | 100 g ice → exactly 100 g water | OK | — | 6.3.1.2 |
| C4 | theory 2 | physical: keeps identity, reversible; chemical: new substances, usually irreversible | OK | "usually" is right (reversible reactions exist, 6.6.2). | 6.3.1.2 |
| C5 | theory 2 | H₂O still H₂O when frozen or evaporated | OK | — | — |
| C6 | theory 2 | "No new chemical bonds are formed or broken between different types of molecule." | IMPRECISE | Muddled. Say: no bonds inside the particles are broken; only the forces between particles are overcome or re-formed, so the arrangement changes and the substance stays the same. Spec test: "the material recovers its original properties if the change is reversed". CHANGES-OF-STATE-F2. | 6.3.1.2 |
| C7 | theory 2 | wood + oxygen → CO₂ + water; can't be recovered | OK | — | — |
| C8 | theory 3 | solid "strong intermolecular forces"; liquid "weaker intermolecular forces than solid"; gas "very weak (effectively none)" | IMPRECISE | The forces do not change in kind on melting; in a liquid the particles have enough energy to move past each other while still attracting. "Intermolecular" fits molecular substances only — metals and salts melt too. Say "forces of attraction between particles". CHANGES-OF-STATE-F3. | 6.3.1.1 |
| C9 | theory 3 | melting: particles vibrate more → forces overcome → lattice breaks down | OK | — | 6.3.2.1 |
| C10 | theory 3 | boiling: particles "escape from liquid surface into gas phase" | IMPRECISE | That describes evaporation. Boiling happens throughout the liquid (bubbles of vapour form inside it) at the boiling point; evaporation is from the surface at any temperature. The spec names both. CHANGES-OF-STATE-F1. | 6.3.1.2 |
| C11 | common_mistake | physical, same compound; mass always conserved | OK | — | 6.3.1.2 |
| C12 | key_note | names; sublimation; physical, reversible, mass conserved | OK | — | 6.3.1.2 |
| C13 | matching (to be replaced) | melting, freezing, evaporation/boiling, condensation, sublimation (dry ice) | OK | — | — |
| C14 | q1 key | 200 g; mass conserved | OK | — | 6.3.1.2 |
| C15 | q1 wx1 | "In a sealed container with no evaporation, mass is perfectly conserved — but even with some evaporation, the PRINCIPLE is conservation of mass in a change of state." | IMPRECISE | Aligned with opt 1, but muddled: if water did escape as vapour, the ice WOULD weigh less. The point is that freezing itself loses no mass; the water that escaped is still mass, just elsewhere. Key right; usable. CHANGES-OF-STATE-F4. | 6.3.1.2 |
| C16 | q1 wx2 | ice larger volume, same mass, less dense | OK | Aligned with opt 2. | 6.3.1.1 |
| C17 | q1 wx3 | temperature affects rate, not mass | OK | Aligned with opt 3. | — |
| C18 | q2 key | no new substances; identity preserved; reversible | OK | Spec criterion. | 6.3.1.2 |
| C19 | q2 wx1 | melting is a bulk process | OK | Aligned. | — |
| C20 | q2 wx2 | both kinds of change involve energy | OK | Aligned. | — |
| C21 | q2 wx3 | arrangement changes, chemical identity doesn't | OK | Aligned. | 6.3.1.2 |

Count: **0 WRONG**; IMPRECISE: C6, C8, C10, C15.

Chained calculations (rule 3): none required by 6.3.1.2. The spec's mass-conserved density calculation (m = ρ₁V₁ then V₂ = m ÷ ρ₂) is owned by `density-of-materials` (6.3.1.1); if Design links to it here, it needs the same Step 1 … Step 2 worked example first.

Neighbour separation: `internal-energy` (batch 2) owns "heating raises temperature or changes state" and the KE + PE definition; `specific-latent-heat` (batch 3, titled "Changes of State and Specific Latent Heat") owns the flat plateau on a heating curve and E = mL. This lesson owns the names, mass conservation and physical-vs-chemical. The source keeps to that; Design should not add a heating curve or E = mL here.

## 4. Frozen items wrong for their route
None. q1 and q2 are both correct, base and usable on all four routes.

## 5. Verdict
SOURCE OK WITH FLAGS. The spec core is fully present and correct. Four imprecisions: boiling described as surface escape, "weaker intermolecular forces" in liquids, a muddled bond sentence, and a muddled q1 wx1.

**For Mide:** nothing.
