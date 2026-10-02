# Batch 14 — diagram library audit

Method: grepped `figlib/chemistry.py`, `figlib/physics.py`, `figlib/catalogue_
ks3_biochem.py`, `figlib/charts.py`, `shared/ks4-diagrams.js`, `ks3_art/*.py`
and `ks4_lessons/authored/batch-2/` + `batch-3/*.dc.html` for function names
and docstrings naming each lesson's subject matter, then read the matching
function/docstring to confirm it is a real match and not a substring
collision. No forward reference to any of this batch's 15 slugs was found in
the authored batch-2/batch-3 lessons' `endConnects` arrays. `shared/
ks4-diagrams.js`'s `metallic(cols, rows, opt)` — built for the giant-metallic-
structure bonding topic, not for this batch — carries an `opt.alloy` option
that draws oversized atoms disrupting the regular lattice; checked against
`alloys-useful-materials` and confirmed a genuine, not coincidental, match
(see #12 below).

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | pure-substances | **Direct match, partial:** `figlib/physics.py` `heating_curve(substance)` — "Temperature vs time heating curve with melting & boiling plateaus" — draws the sharp, flat melting/boiling plateau this lesson's "pure substance melts at a fixed temperature" content needs. **Not covered:** the PURE-VS-IMPURE comparison itself — `heating_curve()` draws one substance's curve only; there is no overlay of a second, sloped (range-not-point) curve for an impure sample, which is this lesson's actual contrast. |
| 2 | formulations | **Nothing found anywhere searched.** This lesson is a definitional/classification topic (formulation = deliberately proportioned mixture) illustrated by examples (medicines, paints, fertilisers, alloys) rather than a process or apparatus — no figure anywhere draws a "formulation" as a concept. |
| 3 | chromatography | **Direct match, exact name:** `figlib/chemistry.py:2040 chromatography(spots=None)` — "Paper chromatography setup with an unknown beside reference spots... illustrates an unknown matching two of three knowns" — exactly this lesson's RP1 content (separate inks/dyes, measure Rf, compare to knowns). |
| 4 | testing-for-gases | **Direct match, 3 of 4 rows:** `figlib/chemistry.py:2198 ion_tests()` — its "gas" rows name hydrogen (lit splint, squeaky pop), oxygen (glowing splint, relights) and chlorine (damp litmus, bleaches) word for word against this lesson's own theory. **Partial:** the fourth gas, CO₂, appears in the table only via the CO₃²⁻ (carbonate) ion row's result text ("Limewater turns CLOUDY (CO₂)") — same reagent and chemistry as this lesson's own CO₂ test, but not drawn as its own "bubble gas through limewater" row. |
| 5 | flame-tests | **Direct match, exact name:** `figlib/chemistry.py:2132 flame_tests()` — "Reference table: flame test colours for the common Group 1 / 2 metal ions AQA expects students to know" (lithium crimson, sodium yellow, potassium lilac, …) — exactly this lesson's RP content. |
| 6 | instrumental-methods | **Reusable, contingent:** `flame_tests()` (cited under #5) is the lesson's own comparison point — this lesson's theory contrasts flame tests (subjective, visual) against flame emission spectroscopy (objective, wavelength-measured), so the existing flame-test reference table supports half the contrast. **Nothing found** for the instrumental side itself — no figure draws a flame-emission SPECTRUM (wavelength lines, e.g. sodium's 589 nm doublet) anywhere in the repo. |
| 7 | composition-of-atmosphere | **Direct match, exact name:** `figlib/chemistry.py:2257 atmosphere_pie()` — "Composition of today's atmosphere as a pie chart" with the AQA-specified proportions — exactly this lesson's content. |
| 8 | alternative-metal-extraction | **Reusable, contingent only:** `figlib/chemistry.py reactivity_series()` (cited in batches 11–12) — the reactivity ladder underlies WHY phytomining/bioleaching are needed (rich ores running out, low-grade ores uneconomical to smelt by traditional reactivity-based methods) but draws the series itself, not either alternative process. **Nothing found** for phytomining (hyperaccumulator plants → harvest → burn → bio-ore) or bioleaching (bacteria → leachate → displacement with scrap iron) as their own figures — both genuinely missing. |
| 9 | life-cycle-assessment | **Direct match, exact name:** `figlib/chemistry.py:2421 life_cycle_assessment()` — "Flow strip: extraction -> manufacture -> use -> disposal" — exactly this lesson's four-stage LCA content, and exactly this lesson's own name. |
| 10 | reducing-use-of-resources | **Reusable, contingent:** `life_cycle_assessment()` (cited under #9) is the adjacent figure — an LCA informs reduce/reuse/recycle decisions — but does not draw the 3Rs hierarchy itself. **Nothing found** for a dedicated reduce/reuse/recycle figure (e.g. a ranked hierarchy or a recycling-loop diagram) anywhere searched. |
| 11 | corrosion-prevention | **Nothing found anywhere searched.** No rusting (iron + oxygen + water), passivation (aluminium oxide layer), sacrificial-protection (zinc block) or galvanising figure exists in `figlib`, `ks3_art` or `shared/ks4-diagrams.js`. |
| 12 | alloys-useful-materials | **Direct match, exact mechanism:** `shared/ks4-diagrams.js`'s `metallic(cols, rows, opt)` with its `opt.alloy` option — oversized, differently-coloured atoms placed at given grid positions among the regular metal-ion lattice — is precisely this lesson's "different-sized atoms DISRUPT the regular lattice — layers can't slide as easily" mechanism. Built for the giant-metallic-structures bonding topic rather than authored for this lesson, but the match is mechanistic, not coincidental: confirmed by reading the function body (an `alloyAt` list of `[row, col]` positions drawn larger and gold-coloured against the plain lattice). |
| 13 | ceramics-polymers-composites | **False near-hit, checked and ruled out:** `figlib/catalogue_ks3_biochem.py` (`c9-materials-table`, line ~299) names "Carbon-fibre composite" and "Heat-proof glass-ceramic" as ROW LABELS in a KS3 stiff/cheap property-comparison table — a classify exercise using material NAMES, not a diagram of ceramic structure, polymer cross-linking or composite matrix+reinforcement. **Nothing found** for soda-lime/borosilicate glass structure, thermosetting-vs-thermoplastic cross-linking, or a matrix+reinforcement composite diagram. |
| 14 | haber-process | **Nothing found anywhere searched**, consistent with batch-12's finding for the sibling lesson `effect-of-conditions-equilibrium` (Haber process / Le Chatelier) — no reversible-reaction or equilibrium-shift figure exists in `figlib` or `ks3_art` for N₂+3H₂⇌2NH₃ at any batch to date. `figlib/chemistry.py reaction_profile()` (cited in batch-12) is a DIFFERENT figure (energy vs progress, not equilibrium position) and was not re-cited here as it answers a different question. |
| 15 | npk-fertilisers | **Nothing found anywhere searched.** No figure exists for NPK composition, the ammonia→ammonium-salt manufacturing chain, or the eutrophication/leaching pathway this lesson describes. |

## Figures still needed

1. **pure-substances** — a pure-vs-impure OVERLAY on the heating curve: `heating_curve()` draws one sharp plateau; the genuinely missing piece is a second, sloped (range, not point) curve for an impure sample on the same axes.
2. **formulations** — none urgent; this is a definitional topic illustrated by named examples rather than a process diagram.
3. **chromatography** — none needed; `chromatography()` already covers it directly.
4. **testing-for-gases** — a dedicated CO₂-through-limewater row/figure, distinct from the carbonate-ion test it currently rides on in `ion_tests()`; H₂, O₂ and Cl₂ are already covered directly.
5. **flame-tests** — none needed; `flame_tests()` already covers it directly.
6. **instrumental-methods** — a flame-emission spectrum figure (wavelength lines with intensity, e.g. sodium's 589 nm doublet) — the one genuinely missing figure; the flame-test comparison side is already covered by `flame_tests()`.
7. **composition-of-atmosphere** — none needed; `atmosphere_pie()` already covers it directly.
8. **alternative-metal-extraction** — a phytomining figure (hyperaccumulator plants → harvest → burn → bio-ore) and a bioleaching figure (bacteria + low-grade ore → leachate → displacement with scrap iron) — both genuinely missing; `reactivity_series()` only supports the "why" context.
9. **life-cycle-assessment** — none needed; `life_cycle_assessment()` already covers it directly.
10. **reducing-use-of-resources** — a reduce/reuse/recycle hierarchy or loop figure — the one genuinely missing figure; `life_cycle_assessment()` is adjacent but does not draw the 3Rs themselves.
11. **corrosion-prevention** — a rusting/passivation figure (iron + O₂ + H₂O → rust vs aluminium's protective oxide layer) and a sacrificial-protection figure (zinc block on a ship hull or buried pipe) — both genuinely missing.
12. **alloys-useful-materials** — none needed; `shared/ks4-diagrams.js`'s `metallic(cols, rows, {alloy:[...]})` already covers the disrupted-lattice mechanism directly.
13. **ceramics-polymers-composites** — three genuinely missing figures: a glass/ceramic structure figure, a thermosetting-vs-thermoplastic cross-linking comparison, and a composite matrix+reinforcement figure (e.g. CFRP or reinforced concrete).
14. **haber-process** — a reversible-reaction/equilibrium-shift figure for N₂+3H₂⇌2NH₃ showing the rate-vs-yield compromise behind the 450°C/200 atm conditions — the one genuinely missing figure, and still missing across every batch to date.
15. **npk-fertilisers** — an NPK manufacturing flow figure (ammonia → ammonium salt → blended fertiliser) — the one genuinely missing figure for this lesson.
